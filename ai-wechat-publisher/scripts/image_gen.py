"""
APImart (Seedream-4.0) 配图生成 + fallback 占位图
异步模式：提交任务 → 轮询结果 → 下载图片

用法:
  python image_gen.py generate "prompt描述" --output output/image_1.jpg
  python image_gen.py generate "prompt描述" --output output/image_1.jpg --size 16:9
  python image_gen.py generate "prompt描述" --output output/image_1.jpg --resolution 2K
  python image_gen.py fallback "简短描述" --output output/image_1.jpg
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
API_KEY = os.environ.get("APIMART_API_KEY", "")
API_BASE = "https://api.apimart.ai"

# 轮询配置
POLL_INTERVAL = 5   # 每5秒查询一次
POLL_TIMEOUT = 180  # 最多等3分钟


def generate_image(prompt, output_path, size="16:9", resolution="1080p"):
    """调用 APImart Seedream-4.0 图片生成（异步模式）"""
    if not API_KEY:
        print("错误: APIMART_API_KEY 未配置", file=sys.stderr)
        return False

    # prompt 优化
    optimized = f"{prompt}, digital art style, high quality, clean composition"

    print(f"提交生成任务: {optimized[:80]}...")

    # 第1步：提交生成任务
    url = f"{API_BASE}/v1/images/generations"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": "doubao-seedream-4.0",
        "prompt": optimized,
        "size": _convert_size(size),
        "resolution": resolution if resolution else "1080p",
        "n": 1,
    }

    try:
        resp = requests.post(url, headers=headers, json=payload, timeout=30)
        resp.raise_for_status()
        data = resp.json()
    except requests.exceptions.RequestException as e:
        print(f"提交任务失败: {e}", file=sys.stderr)
        return False

    # 解析 task_id
    task_id = None
    if data.get("code") == 200 and isinstance(data.get("data"), list) and len(data["data"]) > 0:
        task_id = data["data"][0].get("task_id")
    elif data.get("task_id"):
        task_id = data["task_id"]

    if not task_id:
        # 可能是同步返回了图片
        image_url = _extract_image_url(data)
        if image_url:
            return _download_image(image_url, output_path)
        print(f"未获取到 task_id，响应: {json.dumps(data, ensure_ascii=False)[:300]}", file=sys.stderr)
        return False

    print(f"任务已提交，task_id: {task_id}，等待生成...")

    # 第2步：轮询查询结果
    start_time = time.time()
    while time.time() - start_time < POLL_TIMEOUT:
        time.sleep(POLL_INTERVAL)

        try:
            result = _query_task(task_id)
        except Exception as e:
            print(f"查询任务异常: {e}", file=sys.stderr)
            continue

        # 响应格式: {"code": 200, "data": {"status": "completed", "result": {...}}}
        data_inner = result.get("data", {})
        status = data_inner.get("status", result.get("status", ""))

        if status in ("succeeded", "completed", "done"):
            image_url = _extract_image_url(result)
            if image_url:
                return _download_image(image_url, output_path)
            print(f"任务完成但无图片URL: {json.dumps(result, ensure_ascii=False)[:300]}", file=sys.stderr)
            return False

        elif status in ("failed", "error"):
            print(f"任务失败: {json.dumps(result, ensure_ascii=False)[:300]}", file=sys.stderr)
            return False

        # 还在处理中
        elapsed = int(time.time() - start_time)
        progress = data_inner.get("progress", "")
        progress_info = f" ({progress}%)" if progress else ""
        print(f"  生成中... ({elapsed}s){progress_info}")

    print(f"任务超时 ({POLL_TIMEOUT}s)", file=sys.stderr)
    return False


def _query_task(task_id):
    """查询异步任务状态"""
    url = f"{API_BASE}/v1/tasks/{task_id}?language=en"
    headers = {"Authorization": f"Bearer {API_KEY}"}

    try:
        resp = requests.get(url, headers=headers, timeout=15)
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.RequestException as e:
        print(f"查询任务失败: {e}", file=sys.stderr)
        return {"status": "unknown"}


def _convert_size(size):
    """将尺寸格式转为 API 支持的比例格式

    Seedream-4.0 支持的比例: 1:1, 2:3, 3:2, 3:4, 4:3, 9:16, 16:9, 21:9, 9:21
    """
    # 如果已经是比例格式（如 16:9），直接返回
    if ":" in str(size):
        return str(size)
    # 兼容旧的 WxH 格式
    s = str(size).lower().replace("x", ":")
    mapping = {
        "1024:576": "16:9",
        "1024:768": "4:3",
        "768:1024": "3:4",
        "1024:1024": "1:1",
        "576:1024": "9:16",
    }
    return mapping.get(s, "16:9")


def _extract_image_url(data):
    """从响应中提取图片 URL

    异步任务完成后的响应格式:
    {
      "code": 200,
      "data": {
        "status": "completed",
        "result": {
          "images": [{"url": ["https://..."], "expires_at": ...}]
        }
      }
    }
    """
    # 优先路径: data.data.result.images[0].url[0]
    try:
        images = data["data"]["result"]["images"]
        if images and images[0].get("url"):
            url_list = images[0]["url"]
            if isinstance(url_list, list) and url_list:
                return url_list[0]
            elif isinstance(url_list, str):
                return url_list
    except (KeyError, IndexError, TypeError):
        pass

    # 备选路径：同步返回格式
    paths = [
        ("data", 0, "url"),
        ("data", 0, "image_url"),
        ("output", "url"),
        ("output", "image_url"),
        ("url",),
        ("image_url",),
    ]
    for path in paths:
        try:
            val = data
            for key in path:
                if isinstance(val, list):
                    val = val[key]
                elif isinstance(val, dict):
                    val = val[key]
                else:
                    break
            if isinstance(val, str) and (val.startswith("http") or val.startswith("data:")):
                return val
        except (KeyError, IndexError, TypeError):
            continue
    return None


def _download_image(url, output_path):
    """下载图片到本地"""
    try:
        if url.startswith("data:"):
            import base64
            b64_data = url.split(",", 1)[1]
            img_bytes = base64.b64decode(b64_data)
        else:
            resp = requests.get(url, timeout=60)
            resp.raise_for_status()
            img_bytes = resp.content

        output = Path(output_path)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_bytes(img_bytes)
        print(f"配图已保存: {output_path} ({len(img_bytes) // 1024}KB)")
        return True

    except Exception as e:
        print(f"图片下载失败: {e}", file=sys.stderr)
        return False


def generate_fallback(description, output_path):
    """生成 fallback 占位图"""
    try:
        from PIL import Image, ImageDraw, ImageFont
        return _fallback_pillow(description, output_path)
    except ImportError:
        return _fallback_png(output_path)


def _fallback_pillow(description, output_path):
    from PIL import Image, ImageDraw, ImageFont
    import random

    w, h = 1024, 576
    img = Image.new("RGB", (w, h))
    draw = ImageDraw.Draw(img)

    # 渐变背景
    for y in range(h):
        r = int(10 + 50 * y / h)
        g = int(15 + 30 * y / h)
        b = int(80 + 80 * y / h)
        draw.line([(0, y), (w, y)], fill=(r, g, b))

    # 装饰圆点
    for _ in range(20):
        cx = random.randint(50, w - 50)
        cy = random.randint(50, h - 50)
        radius = random.randint(3, 15)
        draw.ellipse([cx - radius, cy - radius, cx + radius, cy + radius],
                     fill=(255, 255, 255))

    short_desc = description[:30]
    try:
        font = ImageFont.truetype("arial.ttf", 32)
    except (OSError, IOError):
        font = ImageFont.load_default()

    bbox = draw.textbbox((0, 0), short_desc, font=font)
    tw = bbox[2] - bbox[0]
    draw.text(((w - tw) / 2, h / 2 - 16), short_desc, fill="white", font=font)

    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    img.save(str(output), "JPEG", quality=90)
    print(f"占位图已生成: {output_path}")
    return True


def _fallback_png(output_path):
    import struct
    import zlib

    w, h = 1024, 576

    def chunk(ctype, data):
        c = ctype + data
        crc = struct.pack(">I", zlib.crc32(c) & 0xFFFFFFFF)
        return struct.pack(">I", len(data)) + c + crc

    raw = b""
    for y in range(h):
        raw += b"\x00"
        r = int(10 + 50 * y / h)
        g = int(15 + 30 * y / h)
        b = int(80 + 80 * y / h)
        raw += bytes([r, g, b]) * w

    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    with open(str(output), "wb") as f:
        f.write(b"\x89PNG\r\n\x1a\n")
        f.write(chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0)))
        f.write(chunk(b"IDAT", zlib.compress(raw)))
        f.write(chunk(b"IEND", b""))

    print(f"纯色占位图已生成: {output_path}")
    return True


def main():
    parser = argparse.ArgumentParser(description="APImart 配图生成工具")
    sub = parser.add_subparsers(dest="command")

    gen = sub.add_parser("generate", help="调用 APImart API 生成配图")
    gen.add_argument("prompt", help="图片描述 prompt")
    gen.add_argument("--output", required=True, help="输出路径")
    gen.add_argument("--size", default="16:9",
                     help="图片比例 (默认 16:9，支持 1:1, 4:3, 9:16 等)")
    gen.add_argument("--resolution", default="1080p",
                     help="分辨率 (480p/720p/1080p，默认 1080p)")

    fb = sub.add_parser("fallback", help="生成 fallback 占位图")
    fb.add_argument("description", help="简短描述")
    fb.add_argument("--output", required=True, help="输出路径")

    args = parser.parse_args()

    if args.command == "generate":
        ok = generate_image(args.prompt, args.output, args.size, args.resolution)
        if not ok:
            print("API 生成失败，使用 fallback 占位图...", file=sys.stderr)
            generate_fallback(args.prompt, args.output)
    elif args.command == "fallback":
        generate_fallback(args.description, args.output)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
