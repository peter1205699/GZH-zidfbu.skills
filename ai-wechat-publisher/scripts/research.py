"""
搜索采集工具（Tavily + Exa 双引擎）
支持搜索、提取、深度研究三种模式，结果保存为 research_notes.md

用法:
  python research.py search "Claude Code best practices" --max-results 5
  python research.py search "query" --max-results 5 --depth advanced --topic news
  python research.py exa-search "query" --max-results 5 --type neural
  python research.py extract "https://example.com/article"
  python research.py extract "url1" "url2" --query "authentication API"
  python research.py research "Claude Code 落地实操" --save output/research_notes.md
  python research.py research "topic" --engine all --save output/report.md
"""

import os
import sys
import json
import time
import argparse
from pathlib import Path

import requests


def load_env():
    env_path = Path(__file__).resolve().parent.parent.parent / ".env"
    if env_path.exists():
        with open(env_path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, _, value = line.partition("=")
                    os.environ[key.strip()] = value.strip()


load_env()
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY", "")
TAVILY_BASE = "https://api.tavily.com"

EXA_API_KEY = os.environ.get("EXA_API_KEY", "")
EXA_BASE = "https://api.exa.ai"


def search(query, max_results=5, depth="advanced", topic="general",
           time_range=None, include_domains=None, exclude_domains=None,
           include_answer=True):
    """Tavily 搜索并返回结构化结果"""
    payload = {
        "query": query,
        "api_key": TAVILY_API_KEY,
        "search_depth": depth,
        "max_results": max_results,
        "include_answer": include_answer,
        "topic": topic,
    }
    if time_range:
        payload["time_range"] = time_range
    if include_domains:
        payload["include_domains"] = include_domains
    if exclude_domains:
        payload["exclude_domains"] = exclude_domains

    resp = requests.post(f"{TAVILY_BASE}/search", json=payload, timeout=30)
    resp.raise_for_status()
    return resp.json()


def exa_search(query, max_results=5, search_type="neural",
               category=None, include_domains=None, exclude_domains=None,
               start_published_date=None, use_autoprompt=True,
               include_text=False, include_summary=False):
    """Exa 语义搜索，擅长高质量内容发现

    Args:
        query: 搜索关键词
        max_results: 最大结果数
        search_type: "neural"（语义搜索）或 "keyword"（关键词搜索）
        category: 分类过滤（company, research paper, news, github, tweet, movie, song, personal site, pdf）
        include_domains: 仅搜索这些域名
        exclude_domains: 排除这些域名
        start_published_date: 起始发布日期（如 "2024-01-01"）
        use_autoprompt: 自动优化查询
        include_text: 是否返回页面正文
        include_summary: 是否返回 AI 摘要
    """
    if not EXA_API_KEY:
        print("警告: EXA_API_KEY 未配置，跳过 Exa 搜索", file=sys.stderr)
        return {"results": []}

    headers = {
        "x-api-key": EXA_API_KEY,
        "Content-Type": "application/json",
    }

    payload = {
        "query": query,
        "numResults": max_results,
        "type": search_type,
        "useAutoprompt": use_autoprompt,
        "contents": {
            "text": include_text,
            "summary": include_summary,
        },
    }

    if category:
        payload["category"] = category
    if include_domains:
        payload["includeDomains"] = include_domains
    if exclude_domains:
        payload["excludeDomains"] = exclude_domains
    if start_published_date:
        payload["startPublishedDate"] = start_published_date

    resp = requests.post(f"{EXA_BASE}/search", json=payload, headers=headers, timeout=30)
    resp.raise_for_status()
    data = resp.json()

    # 统一结果格式
    results = []
    for r in data.get("results", []):
        item = {
            "title": r.get("title", ""),
            "url": r.get("url", ""),
            "content": r.get("text", "") or r.get("summary", "") or "",
            "score": r.get("score", 0),
            "query": query,
            "source": "exa",
        }
        if r.get("summary"):
            item["summary"] = r["summary"]
        if r.get("publishedDate"):
            item["published_date"] = r["publishedDate"]
        if r.get("author"):
            item["author"] = r["author"]
        results.append(item)

    return {
        "results": results,
        "total_sources": len(results),
    }


def exa_contents(urls, include_summary=False, include_text=True):
    """Exa 内容提取，获取网页正文

    Args:
        urls: 一个或多个 URL
        include_summary: 是否返回 AI 摘要
        include_text: 是否返回正文
    """
    if not EXA_API_KEY:
        print("警告: EXA_API_KEY 未配置", file=sys.stderr)
        return {"results": []}

    headers = {
        "x-api-key": EXA_API_KEY,
        "Content-Type": "application/json",
    }

    url_list = urls if isinstance(urls, list) else [urls]

    payload = {
        "ids": url_list,
        "contents": {
            "text": include_text,
            "summary": include_summary,
        },
    }

    resp = requests.post(f"{EXA_BASE}/contents", json=payload, headers=headers, timeout=60)
    resp.raise_for_status()
    data = resp.json()

    results = []
    for r in data.get("results", []):
        item = {
            "url": r.get("url", ""),
            "title": r.get("title", ""),
            "content": r.get("text", ""),
        }
        if r.get("summary"):
            item["summary"] = r["summary"]
        results.append(item)

    return {"results": results}


def extract(urls, query=None, extract_depth="advanced", format="markdown"):
    """提取 URL 内容为 markdown/text"""
    payload = {
        "urls": urls if isinstance(urls, list) else [urls],
        "api_key": TAVILY_API_KEY,
        "extract_depth": extract_depth,
        "format": format,
    }
    if query:
        payload["query"] = query

    resp = requests.post(f"{TAVILY_BASE}/extract", json=payload, timeout=60)
    resp.raise_for_status()
    return resp.json()


def deep_research(query, model="auto", max_results=10, engine="all"):
    """深度研究，生成带引用的报告

    Args:
        query: 研究主题
        model: 保留参数
        max_results: 每个引擎最大结果数
        engine: "tavily", "exa", "all"
    """
    queries = [
        query,
        f"{query} practical guide tutorial",
        f"{query} best practices real world",
    ]

    all_results = []
    answer_parts = []

    # Tavily 搜索
    if engine in ("tavily", "all") and TAVILY_API_KEY:
        print(f"[Tavily] 搜索中...")
        for q in queries:
            try:
                data = search(q, max_results=max_results, depth="advanced",
                             include_answer=True)
                if data.get("answer"):
                    answer_parts.append(f"### [Tavily] 视角: {q}\n{data['answer']}")
                for r in data.get("results", []):
                    all_results.append({
                        "title": r.get("title", ""),
                        "url": r.get("url", ""),
                        "content": r.get("content", ""),
                        "score": r.get("score", 0),
                        "query": q,
                        "source": "tavily",
                    })
            except Exception as e:
                print(f"[Tavily] 搜索失败 [{q}]: {e}", file=sys.stderr)

    # Exa 语义搜索
    if engine in ("exa", "all") and EXA_API_KEY:
        print(f"[Exa] 语义搜索中...")
        exa_queries = [
            query,
            f"{query} analysis review",
        ]
        for q in exa_queries:
            try:
                data = exa_search(q, max_results=max_results, search_type="neural",
                                  include_text=True, include_summary=True)
                for r in data.get("results", []):
                    if r.get("summary"):
                        answer_parts.append(f"### [Exa] {r['title']}\n{r['summary']}")
                    all_results.append(r)
            except Exception as e:
                print(f"[Exa] 搜索失败 [{q}]: {e}", file=sys.stderr)

    # 去重（按 URL）
    seen_urls = set()
    unique_results = []
    for r in all_results:
        if r["url"] not in seen_urls:
            seen_urls.add(r["url"])
            unique_results.append(r)

    # 按相关度排序
    unique_results.sort(key=lambda x: x.get("score", 0), reverse=True)

    return {
        "answers": answer_parts,
        "results": unique_results,
        "total_sources": len(unique_results),
    }


def format_as_markdown(data, query):
    """将研究结果格式化为 markdown"""
    lines = [f"# 素材采集笔记\n"]
    lines.append(f"## 主题: {query}")
    lines.append(f"采集时间: {time.strftime('%Y-%m-%d %H:%M')}\n")

    # AI 摘要
    if data.get("answers"):
        lines.append("## AI 摘要\n")
        for ans in data["answers"]:
            lines.append(f"{ans}\n")

    # 详细结果
    lines.append(f"## 搜索结果 (共 {data.get('total_sources', 0)} 条)\n")
    for i, r in enumerate(data.get("results", []), 1):
        source = r.get("source", "tavily")
        source_tag = f"[{source.upper()}]" if source else ""
        lines.append(f"### [{i}] {r['title']} {source_tag}")
        lines.append(f"- URL: {r['url']}")
        lines.append(f"- 相关度: {r.get('score', 0):.2f}")
        lines.append(f"- 搜索词: {r.get('query', '')}")
        if r.get("published_date"):
            lines.append(f"- 发布日期: {r['published_date']}")
        if r.get("author"):
            lines.append(f"- 作者: {r['author']}")
        lines.append(f"\n{r.get('content', '')}\n")
        lines.append("---\n")

    return "\n".join(lines)


def save_results(data, output_path, query):
    """保存结果到文件"""
    md = format_as_markdown(data, query)

    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(md, encoding="utf-8")

    # 同时保存 JSON 原始数据
    json_path = out.with_suffix(".json")
    json_path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

    print(f"研究笔记已保存: {output_path}")
    print(f"原始数据已保存: {json_path}")
    print(f"共采集 {data.get('total_sources', 0)} 条素材")


def main():
    parser = argparse.ArgumentParser(description="Tavily 搜索采集工具")
    sub = parser.add_subparsers(dest="command")

    # search 子命令
    s = sub.add_parser("search", help="Tavily Web 搜索")
    s.add_argument("query", help="搜索关键词")
    s.add_argument("--max-results", type=int, default=5)
    s.add_argument("--depth", default="advanced",
                   choices=["basic", "advanced"])
    s.add_argument("--topic", default="general",
                   choices=["general", "news", "finance"])
    s.add_argument("--time-range", default=None,
                   choices=["day", "week", "month", "year"])
    s.add_argument("--include-domains", nargs="*", default=None)
    s.add_argument("--exclude-domains", nargs="*", default=None)
    s.add_argument("--save", default=None, help="保存到文件路径")

    # exa-search 子命令
    es = sub.add_parser("exa-search", help="Exa 语义搜索（高质量内容发现）")
    es.add_argument("query", help="搜索关键词")
    es.add_argument("--max-results", type=int, default=5)
    es.add_argument("--type", default="neural",
                   choices=["neural", "keyword"],
                   help="搜索类型：neural=语义，keyword=关键词")
    es.add_argument("--category", default=None,
                   choices=["company", "research paper", "news", "github",
                           "tweet", "movie", "song", "personal site", "pdf"],
                   help="分类过滤")
    es.add_argument("--include-domains", nargs="*", default=None)
    es.add_argument("--exclude-domains", nargs="*", default=None)
    es.add_argument("--start-date", default=None,
                   help="起始发布日期 (如 2024-01-01)")
    es.add_argument("--with-text", action="store_true",
                   help="返回页面正文")
    es.add_argument("--with-summary", action="store_true",
                   help="返回 AI 摘要")
    es.add_argument("--save", default=None, help="保存到文件路径")

    # extract 子命令
    e = sub.add_parser("extract", help="提取 URL 内容")
    e.add_argument("urls", nargs="+", help="一个或多个 URL")
    e.add_argument("--query", default=None, help="聚焦查询")
    e.add_argument("--format", default="markdown",
                   choices=["markdown", "text"])
    e.add_argument("--save", default=None, help="保存到文件路径")

    # research 子命令（深度研究）
    r = sub.add_parser("research", help="深度研究（多角度搜索+报告）")
    r.add_argument("query", help="研究主题")
    r.add_argument("--max-results", type=int, default=10)
    r.add_argument("--engine", default="all",
                   choices=["tavily", "exa", "all"],
                   help="搜索引擎：tavily/exa/all（默认双引擎）")
    r.add_argument("--save", default="output/research_notes.md",
                   help="输出文件路径")

    args = parser.parse_args()

    if not TAVILY_API_KEY and not EXA_API_KEY:
        print("错误: 至少需要配置一个搜索 API（TAVILY_API_KEY 或 EXA_API_KEY）",
              file=sys.stderr)
        sys.exit(1)

    if args.command == "exa-search":
        if not EXA_API_KEY:
            print("错误: EXA_API_KEY 未配置", file=sys.stderr)
            sys.exit(1)

        data = exa_search(
            args.query,
            max_results=args.max_results,
            search_type=args.type,
            category=args.category,
            include_domains=args.include_domains,
            exclude_domains=args.exclude_domains,
            start_published_date=args.start_date,
            include_text=args.with_text,
            include_summary=args.with_summary,
        )

        for r in data.get("results", []):
            score = r.get("score", 0)
            date_str = f" ({r['published_date'][:10]})" if r.get("published_date") else ""
            print(f"[{score:.2f}] {r['title']}{date_str}")
            print(f"  {r['url']}")
            if r.get("summary"):
                print(f"  摘要: {r['summary'][:200]}")
            if r.get("content") and args.with_text:
                print(f"  正文: {r['content'][:200]}...")
            print()

        if args.save:
            wrapped = {
                "answers": [],
                "results": data.get("results", []),
                "total_sources": data.get("total_sources", 0),
            }
            save_results(wrapped, args.save, args.query)

    elif args.command == "search":
        data = search(
            args.query,
            max_results=args.max_results,
            depth=args.depth,
            topic=args.topic,
            time_range=args.time_range,
            include_domains=args.include_domains,
            exclude_domains=args.exclude_domains,
        )

        # 输出摘要
        if data.get("answer"):
            print(f"\nAI 摘要: {data['answer']}\n")

        for r in data.get("results", []):
            score = r.get("score", 0)
            print(f"[{score:.2f}] {r['title']}")
            print(f"  {r['url']}")
            print(f"  {r.get('content', '')[:200]}")
            print()

        if args.save:
            wrapped = {
                "answers": [f"### {args.query}\n{data.get('answer', '')}"],
                "results": [
                    {"title": r.get("title", ""),
                     "url": r.get("url", ""),
                     "content": r.get("content", ""),
                     "score": r.get("score", 0),
                     "query": args.query}
                    for r in data.get("results", [])
                ],
                "total_sources": len(data.get("results", [])),
            }
            save_results(wrapped, args.save, args.query)

    elif args.command == "extract":
        data = extract(args.urls, query=args.query, format=args.format)
        for r in data.get("results", []):
            url = r.get("url", "")
            text = r.get("raw_content", "") or r.get("text", "")
            print(f"=== {url} ===")
            print(text[:2000])
            print()

        if args.save:
            out = Path(args.save)
            out.parent.mkdir(parents=True, exist_ok=True)
            content = "\n\n".join(
                f"## {r.get('url', '')}\n\n{r.get('raw_content', '') or r.get('text', '')}"
                for r in data.get("results", [])
            )
            out.write_text(content, encoding="utf-8")
            print(f"内容已保存: {args.save}")

    elif args.command == "research":
        print(f"开始深度研究: {args.query} (引擎: {args.engine})")
        data = deep_research(args.query, max_results=args.max_results,
                             engine=args.engine)
        save_results(data, args.save, args.query)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
