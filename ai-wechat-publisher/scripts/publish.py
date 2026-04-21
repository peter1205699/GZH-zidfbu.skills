"""
Markdown → 公众号 HTML 转换 + 草稿箱发布
支持多张配图替换

用法:
  python publish.py output/article.md --replacements "IMAGE_1:url1" "IMAGE_2:url2" --cover-index 1
  python publish.py output/article.md --cover-file output/image_1.jpg
"""

import os
import sys
import re
import json
import argparse
import tempfile
from pathlib import Path

import markdown2
import requests as http_requests

from wechat_api import add_draft, upload_image


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


def markdown_to_wechat_html(md_content, replacements=None):
    """将 Markdown 转为公众号兼容 HTML（内联样式）

    replacements: {"IMAGE_1": "https://mmbiz.qpic.cn/...", ...}
    """
    # 替换图片占位标记 <!-- IMAGE_N: 描述文字 -->
    if replacements:
        for key, url in replacements.items():
            pattern = re.compile(r'<!--\s*' + re.escape(key) + r'\s*:\s*[^>]*\s*-->', re.IGNORECASE)
            md_content = pattern.sub(f'![配图]({url})', md_content)

    # 移除残留的未匹配占位标记
    md_content = re.sub(r'<!--\s*IMAGE_\d+\s*:\s*[^>]*\s*-->', '', md_content)

    # Markdown → HTML
    html_body = markdown2.markdown(
        md_content,
        extras=["fenced-code-blocks", "tables", "strike", "task_list"]
    )

    # 添加内联样式
    return _apply_inline_styles(html_body)


def _apply_inline_styles(html):
    """为公众号 HTML 添加内联样式"""
    try:
        from bs4 import BeautifulSoup
        return _style_with_bs4(html)
    except ImportError:
        return _style_with_regex(html)


def _style_with_bs4(html):
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    tag_styles = {
        "h1": "font-size:22px;font-weight:bold;color:#1a1a1a;margin:20px 0 10px;text-align:center;",
        "h2": "font-size:19px;font-weight:bold;color:#1a1a1a;margin:18px 0 8px;border-left:4px solid #07c160;padding-left:10px;",
        "h3": "font-size:17px;font-weight:bold;color:#333;margin:14px 0 6px;",
        "p": "font-size:16px;line-height:1.75;color:#333;margin:8px 0;",
        "img": "max-width:100%;height:auto;border-radius:8px;margin:12px 0;display:block;",
        "blockquote": "border-left:4px solid #07c160;padding:10px 15px;background:#f6f6f6;margin:12px 0;",
        "code": "background:#f0f0f0;padding:2px 6px;border-radius:3px;font-family:Menlo,Monaco,Consolas,monospace;font-size:14px;",
        "pre": "background:#2d2d2d;color:#f8f8f2;padding:16px;border-radius:8px;overflow-x:auto;margin:12px 0;",
        "li": "font-size:16px;line-height:1.75;color:#333;margin:4px 0;",
        "strong": "color:#1a1a1a;font-weight:bold;",
        "a": "color:#07c160;text-decoration:none;",
    }

    for tag_name, style in tag_styles.items():
        for tag in soup.find_all(tag_name):
            existing = tag.get("style", "")
            tag["style"] = style + existing

    # pre > code 不需要额外背景
    for pre in soup.find_all("pre"):
        for code in pre.find_all("code"):
            code["style"] = "color:inherit;padding:0;background:none;font-size:13px;line-height:1.6;"

    # blockquote > p 特殊样式
    for bq in soup.find_all("blockquote"):
        for p in bq.find_all("p"):
            p["style"] = "color:#666;font-size:15px;margin:4px 0;"

    return str(soup)


def _style_with_regex(html):
    """无 BeautifulSoup 时用正则处理"""
    replacements = [
        (r"<h1>", '<h1 style="font-size:22px;font-weight:bold;color:#1a1a1a;margin:20px 0 10px;text-align:center;">'),
        (r"<h2>", '<h2 style="font-size:19px;font-weight:bold;color:#1a1a1a;margin:18px 0 8px;border-left:4px solid #07c160;padding-left:10px;">'),
        (r"<h3>", '<h3 style="font-size:17px;font-weight:bold;color:#333;margin:14px 0 6px;">'),
        (r"<p>", '<p style="font-size:16px;line-height:1.75;color:#333;margin:8px 0;">'),
        (r"<img ", '<img style="max-width:100%;height:auto;border-radius:8px;margin:12px 0;display:block;" '),
        (r"<li>", '<li style="font-size:16px;line-height:1.75;color:#333;margin:4px 0;">'),
        (r"<strong>", '<strong style="color:#1a1a1a;font-weight:bold;">'),
    ]
    for pattern, replacement in replacements:
        html = re.sub(pattern, replacement, html)
    return html


def extract_title(md_content):
    match = re.search(r'^#\s+(.+)', md_content, re.MULTILINE)
    return match.group(1).strip() if match else "AI 热点速递"


def main():
    parser = argparse.ArgumentParser(description="Markdown → 公众号草稿箱发布")
    parser.add_argument("markdown_file", help="Markdown 文件路径")
    parser.add_argument("--replacements", nargs="*", default=[],
                        help="图片替换列表，格式: IMAGE_N:url")
    parser.add_argument("--cover-file", help="封面图本地路径", default=None)
    parser.add_argument("--cover-media-id", help="已上传的封面图 media_id", default=None)
    parser.add_argument("--cover-index", type=int, default=1,
                        help="使用第N张配图作为封面（默认第1张）")
    parser.add_argument("--author", default="AI", help="作者名")
    args = parser.parse_args()

    md_path = Path(args.markdown_file)
    if not md_path.exists():
        print(f"文件不存在: {md_path}", file=sys.stderr)
        sys.exit(1)

    md_content = md_path.read_text(encoding="utf-8")
    title = extract_title(md_content)

    # 解析替换参数: "IMAGE_1:url" → {"IMAGE_1": "url"}
    replacements = {}
    for r in args.replacements:
        if ":" in r:
            key, _, url = r.partition(":")
            replacements[key.strip()] = url.strip()

    # 转换 HTML
    html_content = markdown_to_wechat_html(md_content, replacements)

    # 封面图处理
    thumb_media_id = args.cover_media_id

    if not thumb_media_id and args.cover_file:
        result = upload_image(args.cover_file)
        if result:
            thumb_media_id = result["media_id"]

    # 从替换列表中找封面图下载上传
    if not thumb_media_id and replacements:
        cover_key = f"IMAGE_{args.cover_index}"
        cover_url = replacements.get(cover_key)
        if cover_url:
            try:
                resp = http_requests.get(cover_url, timeout=30)
                with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tmp:
                    tmp.write(resp.content)
                    tmp_path = tmp.name
                result = upload_image(tmp_path)
                if result:
                    thumb_media_id = result["media_id"]
                os.unlink(tmp_path)
            except Exception as e:
                print(f"封面图处理失败: {e}", file=sys.stderr)

    if not thumb_media_id:
        print("警告: 没有封面图，草稿可能无法正常显示", file=sys.stderr)
        thumb_media_id = ""

    # 创建草稿
    media_id = add_draft(title, html_content, thumb_media_id, author=args.author)

    if media_id:
        print(f"""
[OK] 文章已发布到公众号草稿箱！

标题：{title}
media_id：{media_id}
配图：{len(replacements)} 张

请前往 mp.weixin.qq.com -> 内容管理 -> 草稿箱 检查文章。

提醒：
  1. 登录后确认图片显示正常
  2. 检查内容（可补充/修改摘要）
  3. 点击【预览】发送到手机确认效果
""")
    else:
        print("发布失败", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
