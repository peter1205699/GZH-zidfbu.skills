"""
微信公众号数据分析采集工具
- 文章阅读/分享/收藏/评论数据
- 账号概览与用户统计
- 一键同步到发布档案

用法:
  python wechat_analytics.py article-detail --date 2026-05-11
  python wechat_analytics.py daily-read --date 2026-05-11
  python wechat_analytics.py daily-share --date 2026-05-11
  python wechat_analytics.py summary --begin-date 2026-05-01 --end-date 2026-05-11
  python wechat_analytics.py user-stats --begin-date 2026-05-01 --end-date 2026-05-07
  python wechat_analytics.py user-total --begin-date 2026-05-01 --end-date 2026-05-07
  python wechat_analytics.py sync
"""

import os
import sys
import json
import argparse
from pathlib import Path
from datetime import datetime, timedelta

import requests

# 复用 wechat_api 的 token 管理
sys.path.insert(0, str(Path(__file__).resolve().parent))
from wechat_api import get_access_token, _parse_json

BASE_URL = "https://api.weixin.qq.com/datacube"

PUBLISHED_JSON = Path(__file__).resolve().parent.parent.parent / "output" / "published_articles.json"


def _post(endpoint, body):
    token = get_access_token()
    url = f"{BASE_URL}{endpoint}?access_token={token}"
    headers = {"Content-Type": "application/json; charset=utf-8"}
    resp = requests.post(
        url,
        data=json.dumps(body, ensure_ascii=False).encode("utf-8"),
        headers=headers,
        timeout=30,
    )
    data = _parse_json(resp)
    if data.get("errcode", 0) != 0:
        print(f"API 错误 ({endpoint}): {json.dumps(data, ensure_ascii=False)}", file=sys.stderr)
    return data


def article_detail(date_str):
    """拉取某篇文章的详细数据（阅读/分享/收藏/评论）"""
    data = _post("/getarticletotaldetail", {"begin_date": date_str, "end_date": date_str})
    return data


def daily_read(date_str):
    """某天所有文章的每日阅读指标"""
    data = _post("/getarticleread", {"begin_date": date_str, "end_date": date_str})
    return data


def daily_share(date_str):
    """某天所有文章的分享指标"""
    data = _post("/getarticleshare", {"begin_date": date_str, "end_date": date_str})
    return data


def summary(begin_date, end_date):
    """某段时间内账号发表内容汇总概览"""
    data = _post("/getbizsummary", {"begin_date": begin_date, "end_date": end_date})
    return data


def user_stats(begin_date, end_date):
    """用户增减数据"""
    data = _post("/getusersummary", {"begin_date": begin_date, "end_date": end_date})
    return data


def user_total(begin_date, end_date):
    """累计用户数据"""
    data = _post("/getusercumulate", {"begin_date": begin_date, "end_date": end_date})
    return data


def _load_published():
    if PUBLISHED_JSON.exists():
        return json.loads(PUBLISHED_JSON.read_text(encoding="utf-8"))
    return {"articles": []}


def _save_published(data):
    PUBLISHED_JSON.parent.mkdir(parents=True, exist_ok=True)
    PUBLISHED_JSON.write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def sync():
    """一键同步：拉取所有已发布文章的最新数据，更新到 published_articles.json"""
    pub = _load_published()
    if not pub["articles"]:
        print("发布档案为空，没有文章可同步。", file=sys.stderr)
        return

    today = datetime.now().strftime("%Y-%m-%d")
    updated = 0

    for article in pub["articles"]:
        pub_date = article.get("publish_date", "")
        if not pub_date:
            continue

        # 微信 datacube 只统计发表后 30 天内的数据
        pub_dt = datetime.strptime(pub_date, "%Y-%m-%d")
        if (datetime.now() - pub_dt).days > 30:
            print(f"  跳过（超过30天）: {article['title']}", file=sys.stderr)
            continue

        print(f"  同步: {article['title']} ...", file=sys.stderr)

        detail = article_detail(pub_date)
        items = detail.get("list", [])

        if items:
            # 找到匹配的文章（通过 title 或取第一条）
            matched = None
            for item in items:
                if item.get("title") == article["title"]:
                    matched = item
                    break
            if not matched:
                matched = items[0]

            stats = matched.get("details", matched)
            article["analytics"] = {
                "last_synced": today,
                "read_count": stats.get("int_page_read_count", 0),
                "read_user": stats.get("int_page_read_user", 0),
                "ori_read_count": stats.get("ori_page_read_count", 0),
                "share_count": stats.get("share_count", 0),
                "share_user": stats.get("share_user_count", 0),
                "like_count": stats.get("like_count", 0),
                "comment_count": stats.get("comment_count", 0),
                "collect_count": stats.get("collect_count", 0),
            }
            updated += 1
        else:
            print(f"    未获取到数据", file=sys.stderr)

    _save_published(pub)
    print(f"\n同步完成：更新 {updated} 篇文章的数据", file=sys.stderr)
    print(json.dumps(pub, ensure_ascii=False, indent=2))


def main():
    parser = argparse.ArgumentParser(description="微信公众号数据分析工具")
    sub = parser.add_subparsers(dest="command")

    ad = sub.add_parser("article-detail", help="文章详细数据")
    ad.add_argument("--date", required=True, help="日期 YYYY-MM-DD")

    dr = sub.add_parser("daily-read", help="每日阅读指标")
    dr.add_argument("--date", required=True, help="日期 YYYY-MM-DD")

    ds = sub.add_parser("daily-share", help="每日分享指标")
    ds.add_argument("--date", required=True, help="日期 YYYY-MM-DD")

    sm = sub.add_parser("summary", help="账号内容概览")
    sm.add_argument("--begin-date", required=True, help="开始日期 YYYY-MM-DD")
    sm.add_argument("--end-date", required=True, help="结束日期 YYYY-MM-DD")

    us = sub.add_parser("user-stats", help="用户增减数据")
    us.add_argument("--begin-date", required=True, help="开始日期 YYYY-MM-DD")
    us.add_argument("--end-date", required=True, help="结束日期 YYYY-MM-DD")

    ut = sub.add_parser("user-total", help="累计用户数据")
    ut.add_argument("--begin-date", required=True, help="开始日期 YYYY-MM-DD")
    ut.add_argument("--end-date", required=True, help="结束日期 YYYY-MM-DD")

    sub.add_parser("sync", help="一键同步所有文章数据到发布档案")

    args = parser.parse_args()

    if args.command == "article-detail":
        data = article_detail(args.date)
        print(json.dumps(data, ensure_ascii=False, indent=2))
    elif args.command == "daily-read":
        data = daily_read(args.date)
        print(json.dumps(data, ensure_ascii=False, indent=2))
    elif args.command == "daily-share":
        data = daily_share(args.date)
        print(json.dumps(data, ensure_ascii=False, indent=2))
    elif args.command == "summary":
        data = summary(args.begin_date, args.end_date)
        print(json.dumps(data, ensure_ascii=False, indent=2))
    elif args.command == "user-stats":
        data = user_stats(args.begin_date, args.end_date)
        print(json.dumps(data, ensure_ascii=False, indent=2))
    elif args.command == "user-total":
        data = user_total(args.begin_date, args.end_date)
        print(json.dumps(data, ensure_ascii=False, indent=2))
    elif args.command == "sync":
        sync()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
