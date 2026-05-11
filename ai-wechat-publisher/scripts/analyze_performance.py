"""
公众号文章表现分析工具
- 生成性能报告（markdown）
- 输出关键洞察摘要

用法:
  python analyze_performance.py report --output output/performance_report.md
  python analyze_performance.py insights
"""

import json
import sys
import argparse
from pathlib import Path
from datetime import datetime

PUBLISHED_JSON = Path(__file__).resolve().parent.parent.parent / "output" / "published_articles.json"


def load_data():
    if not PUBLISHED_JSON.exists():
        print("发布档案不存在，请先发布文章。", file=sys.stderr)
        sys.exit(1)
    return json.loads(PUBLISHED_JSON.read_text(encoding="utf-8"))


def _has_analytics(article):
    a = article.get("analytics", {})
    return a.get("read_count") is not None


def _get_articles_with_data(pub):
    return [a for a in pub.get("articles", []) if _has_analytics(a)]


def generate_report(pub):
    articles = _get_articles_with_data(pub)
    if not articles:
        return "# 性能报告\n\n暂无已同步数据的文章。请先运行 `wechat_analytics.py sync`。\n"

    lines = ["# 公众号文章性能报告", "", f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}", ""]
    lines.append(f"已发布文章: {len(pub['articles'])} 篇 | 已同步数据: {len(articles)} 篇")
    lines.append("")

    # --- 概览表 ---
    lines.append("---")
    lines.append("")
    lines.append("## 文章数据概览")
    lines.append("")
    lines.append("| # | 标题 | 日期 | 风格 | 阅读量 | 分享 | 点赞 | 收藏 |")
    lines.append("|---|------|------|------|--------|------|------|------|")

    for i, a in enumerate(articles, 1):
        an = a.get("analytics", {})
        title = a["title"][:20] + ("..." if len(a["title"]) > 20 else "")
        lines.append(
            f"| {i} | {title} | {a.get('publish_date', '-')} | {a.get('style', '-')} "
            f"| {an.get('read_count', '-')} | {an.get('share_count', '-')} "
            f"| {an.get('like_count', '-')} | {an.get('collect_count', '-')} |"
        )

    lines.append("")

    # --- 关键指标 ---
    lines.append("---")
    lines.append("")
    lines.append("## 关键指标统计")
    lines.append("")

    reads = [a["analytics"].get("read_count", 0) for a in articles]
    shares = [a["analytics"].get("share_count", 0) for a in articles]
    likes = [a["analytics"].get("like_count", 0) for a in articles]
    collects = [a["analytics"].get("collect_count", 0) for a in articles]

    lines.append(f"- 平均阅读量: **{sum(reads) // len(reads):,}**")
    lines.append(f"- 最高阅读量: **{max(reads):,}**")
    lines.append(f"- 平均分享数: **{sum(shares) / len(shares):.1f}**")
    lines.append(f"- 平均点赞数: **{sum(likes) / len(likes):.1f}**")
    lines.append(f"- 平均收藏数: **{sum(collects) / len(collects):.1f}**")
    lines.append("")

    # --- 最佳/最差 ---
    best = max(articles, key=lambda a: a["analytics"].get("read_count", 0))
    worst = min(articles, key=lambda a: a["analytics"].get("read_count", 0))
    lines.append(f"- 最佳表现: **「{best['title']}」** — {best['analytics'].get('read_count', 0):,} 阅读")
    lines.append(f"- 最低表现: **「{worst['title']}」** — {worst['analytics'].get('read_count', 0):,} 阅读")
    lines.append("")

    # --- 风格对比 ---
    style_groups = {}
    for a in articles:
        s = a.get("style", "未知")
        style_groups.setdefault(s, []).append(a)

    if len(style_groups) > 1:
        lines.append("---")
        lines.append("")
        lines.append("## 风格对比")
        lines.append("")
        for style, group in style_groups.items():
            avg_read = sum(a["analytics"].get("read_count", 0) for a in group) // len(group)
            avg_share = sum(a["analytics"].get("share_count", 0) for a in group) / len(group)
            lines.append(f"- **{style}**（{len(group)} 篇）: 平均阅读 {avg_read:,}，平均分享 {avg_share:.1f}")
        lines.append("")

    return "\n".join(lines)


def generate_insights(pub):
    """输出关键洞察摘要（控制台）"""
    articles = _get_articles_with_data(pub)
    if not articles:
        print("暂无已同步数据的文章。请先运行 `wechat_analytics.py sync`。", file=sys.stderr)
        return

    reads = [a["analytics"].get("read_count", 0) for a in articles]
    avg_read = sum(reads) // len(reads)

    best = max(articles, key=lambda a: a["analytics"].get("read_count", 0))
    worst = min(articles, key=lambda a: a["analytics"].get("read_count", 0))

    print("=" * 50)
    print("公众号文章表现洞察")
    print("=" * 50)
    print(f"已分析: {len(articles)} 篇文章")
    print(f"平均阅读量: {avg_read:,}")
    print(f"最佳: {best['title']} ({best['analytics'].get('read_count', 0):,})")
    print(f"最低: {worst['title']} ({worst['analytics'].get('read_count', 0):,})")
    print()

    # 标题特征分析
    digit_titles = [a for a in articles if any(c.isdigit() for c in a["title"])]
    no_digit_titles = [a for a in articles if not any(c.isdigit() for c in a["title"])]

    if digit_titles and no_digit_titles:
        avg_digit = sum(a["analytics"].get("read_count", 0) for a in digit_titles) // len(digit_titles)
        avg_no_digit = sum(a["analytics"].get("read_count", 0) for a in no_digit_titles) // len(no_digit_titles)
        print(f"标题带数字（{len(digit_titles)} 篇）: 平均阅读 {avg_digit:,}")
        print(f"标题无数字（{len(no_digit_titles)} 篇）: 平均阅读 {avg_no_digit:,}")
        if avg_digit > avg_no_digit:
            print("→ 标题带数字的文章表现更好")
        else:
            print("→ 标题不带数字的文章表现更好")
        print()

    # 风格对比
    style_groups = {}
    for a in articles:
        s = a.get("style", "未知")
        style_groups.setdefault(s, []).append(a)

    if len(style_groups) > 1:
        print("风格对比:")
        for style, group in style_groups.items():
            avg = sum(a["analytics"].get("read_count", 0) for a in group) // len(group)
            print(f"  {style}（{len(group)} 篇）: 平均阅读 {avg:,}")
        print()

    # 建议摘要（可写入 Memory）
    print("--- 可写入 Memory 的洞察 ---")
    print(f"平均阅读量基准: {avg_read:,}")
    if digit_titles and no_digit_titles:
        ratio = avg_digit / avg_no_digit if avg_no_digit > 0 else 0
        if ratio > 1.2:
            print(f"标题带数字的文章阅读量是普通标题的 {ratio:.1f}x")
    best_style = max(style_groups.items(), key=lambda x: sum(a["analytics"].get("read_count", 0) for a in x[1]) // len(x[1])) if style_groups else None
    if best_style:
        print(f"最佳风格: {best_style[0]}")


def main():
    parser = argparse.ArgumentParser(description="公众号文章表现分析")
    sub = parser.add_subparsers(dest="command")

    rpt = sub.add_parser("report", help="生成性能报告")
    rpt.add_argument("--output", default="output/performance_report.md", help="输出文件路径")

    sub.add_parser("insights", help="输出关键洞察")

    args = parser.parse_args()

    pub = load_data()

    if args.command == "report":
        report = generate_report(pub)
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(report, encoding="utf-8")
        print(f"报告已生成: {out_path}")
    elif args.command == "insights":
        generate_insights(pub)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
