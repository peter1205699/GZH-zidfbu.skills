"""
微信公众号 API 封装
- access_token 管理（自动刷新）
- 素材上传（单张/批量）
- 草稿箱操作（创建/获取/发布）

用法:
  python wechat_api.py upload-image <path>
  python wechat_api.py batch-upload <path1> <path2> ...
  python wechat_api.py publish <media_id>
  python wechat_api.py get-draft <media_id>
"""

import os
import sys
import json
import time
import argparse
import requests
from pathlib import Path


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

APP_ID = os.environ.get("WECHAT_APP_ID", "")
APP_SECRET = os.environ.get("WECHAT_APP_SECRET", "")

TOKEN_CACHE = Path(__file__).resolve().parent.parent.parent / ".wechat_token.json"


def _parse_json(resp):
    """安全解析微信API响应，确保UTF-8编码正确

    微信API返回 Content-Type: text/plain（无charset），
    requests 默认用 ISO-8859-1 解码导致中文乱码。
    直接从 resp.content（bytes）解析避免此问题。
    """
    return json.loads(resp.content)


def get_access_token():
    """获取 access_token，缓存有效期内复用，提前5分钟刷新"""
    if TOKEN_CACHE.exists():
        try:
            cache = json.loads(TOKEN_CACHE.read_text(encoding="utf-8"))
            if cache.get("expires_at", 0) > time.time() + 300:
                return cache["access_token"]
        except (json.JSONDecodeError, KeyError):
            pass

    url = "https://api.weixin.qq.com/cgi-bin/token"
    resp = requests.get(url, params={
        "grant_type": "client_credential",
        "appid": APP_ID,
        "secret": APP_SECRET,
    }, timeout=30)
    data = _parse_json(resp)

    if "access_token" not in data:
        print(f"获取 access_token 失败: {json.dumps(data, ensure_ascii=False)}", file=sys.stderr)
        sys.exit(1)

    cache = {
        "access_token": data["access_token"],
        "expires_at": time.time() + data.get("expires_in", 7200),
    }
    TOKEN_CACHE.write_text(json.dumps(cache, ensure_ascii=False), encoding="utf-8")
    print("access_token 已刷新", file=sys.stderr)
    return data["access_token"]


def upload_image(image_path):
    """上传单张图片到微信素材库，返回 {media_id, url, file}"""
    token = get_access_token()
    url = f"https://api.weixin.qq.com/cgi-bin/material/add_material?access_token={token}&type=image"

    path = Path(image_path)
    if not path.exists():
        print(f"文件不存在: {image_path}", file=sys.stderr)
        return None

    mime = "image/jpeg" if path.suffix.lower() in (".jpg", ".jpeg") else "image/png"

    with open(path, "rb") as f:
        files = {"media": (path.name, f, mime)}
        resp = requests.post(url, files=files, timeout=60)

    data = _parse_json(resp)
    if "media_id" not in data:
        print(f"上传失败 {image_path}: {json.dumps(data, ensure_ascii=False)}", file=sys.stderr)
        return None

    return {"media_id": data["media_id"], "url": data.get("url", ""), "file": str(path)}


def batch_upload(image_paths):
    """批量上传图片，返回成功的结果列表"""
    results = []
    for p in image_paths:
        r = upload_image(p)
        if r:
            results.append(r)
        else:
            print(f"跳过失败的文件: {p}", file=sys.stderr)
    return results


import re  # needed for add_draft


def _truncate_utf8(text, max_bytes):
    """截断文本使UTF-8编码不超过max_bytes"""
    result = ""
    for ch in text:
        if len((result + ch).encode("utf-8")) > max_bytes:
            break
        result += ch
    return result


def add_draft(title, content, thumb_media_id, author="AI", digest=""):
    """创建草稿箱文章，返回 media_id

    微信API字段长度限制很严格：
    - title: 约32字节
    - author: 约8字节
    - digest: 约100字节
    """
    token = get_access_token()
    url = f"https://api.weixin.qq.com/cgi-bin/draft/add?access_token={token}"

    # 截断 title 到32字节
    title = _truncate_utf8(title, 32)

    # 截断 author 到8字节
    author = _truncate_utf8(author, 8)

    if not digest:
        # 纯文本摘要，去掉 HTML 标签
        plain = re.sub(r'<[^>]+>', '', content)
        plain = plain.strip().replace("\n", " ")
        digest = _truncate_utf8(plain, 80)
        digest = digest.strip() + "..."

    payload = {
        "articles": [{
            "title": title,
            "author": author,
            "digest": digest,
            "content": content,
            "thumb_media_id": thumb_media_id,
            "need_open_comment": 1,
            "only_fans_can_comment": 0,
        }]
    }

    headers = {"Content-Type": "application/json; charset=utf-8"}
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    resp = requests.post(url, data=body, headers=headers, timeout=30)
    data = _parse_json(resp)

    if "media_id" not in data:
        print(f"创建草稿失败: {json.dumps(data, ensure_ascii=False)}", file=sys.stderr)
        return None

    return data["media_id"]


def get_draft(media_id):
    """获取草稿详情"""
    token = get_access_token()
    url = f"https://api.weixin.qq.com/cgi-bin/draft/get?access_token={token}"
    resp = requests.post(url, json={"media_id": media_id}, timeout=30)
    return _parse_json(resp)


def publish_draft(media_id):
    """从草稿箱发布文章（需要公众号已认证）"""
    token = get_access_token()
    url = f"https://api.weixin.qq.com/cgi-bin/freepublish/submit?access_token={token}"
    resp = requests.post(url, json={"media_id": media_id}, timeout=30)
    data = _parse_json(resp)

    if data.get("errcode", 0) != 0:
        print(f"发布失败: {json.dumps(data, ensure_ascii=False)}", file=sys.stderr)
        return None

    return data.get("publish_id") or data


def main():
    parser = argparse.ArgumentParser(description="微信公众号 API 工具")
    sub = parser.add_subparsers(dest="command")

    ui = sub.add_parser("upload-image", help="上传单张图片")
    ui.add_argument("image_path")

    bu = sub.add_parser("batch-upload", help="批量上传图片")
    bu.add_argument("image_paths", nargs="+")

    pub = sub.add_parser("publish", help="发布草稿箱文章")
    pub.add_argument("media_id")

    gd = sub.add_parser("get-draft", help="获取草稿详情")
    gd.add_argument("media_id")

    args = parser.parse_args()

    if args.command == "upload-image":
        result = upload_image(args.image_path)
        if result:
            print(json.dumps(result, ensure_ascii=False))
    elif args.command == "batch-upload":
        results = batch_upload(args.image_paths)
        print(json.dumps(results, ensure_ascii=False, indent=2))
    elif args.command == "publish":
        result = publish_draft(args.media_id)
        if result:
            print(f"发布任务已提交！media_id: {args.media_id}")
            print(json.dumps(result, ensure_ascii=False))
    elif args.command == "get-draft":
        data = get_draft(args.media_id)
        print(json.dumps(data, ensure_ascii=False, indent=2))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
