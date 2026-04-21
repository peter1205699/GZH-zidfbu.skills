---
name: ai-wechat-publisher
description: 公众号工具集（搜索采集 + AI配图生成）。支持知鱼说和卡兹克两种写作风格。写作规范见 WORKFLOW.md，写作由 wechraft-writer skill 处理，发布由 baoyu-post-to-wechat skill 处理。
---

# 公众号工具集：搜索采集 + AI 配图

本工具集负责公众号工作流中的两个环节：**素材搜索采集** 和 **AI 配图生成**。

> 📖 **写作风格和流程规范** 请参阅项目根目录的 **[WORKFLOW.md](../WORKFLOW.md)**

---

## 🎨 写作风格

系统支持两种写作风格，可根据内容类型自动选择或由用户指定：

### 风格 A：知鱼说（默认）

- **特点**：实战派，不整虚的概念，只讲能落地的玩法
- **适合**：行业分析、趋势解读、方法论分享
- **排版**：🔥📊💡🎯⚡ emoji 章节，引用块开头结尾

### 风格 B：卡兹克

- **特点**：有见识的普通人在认真聊一件打动他的事
- **适合**：产品体验、调查实验、个人观点
- **排版**：无小标题，口语化转场，固定尾部

> 详见 [WORKFLOW.md → 文章风格选择](../WORKFLOW.md#-文章风格选择)

---

## 🎯 快速触发

用户输入以下任一内容即可开始创作：

- "写一篇关于 [主题] 的文章" → 默认使用知鱼说风格
- "用卡兹克风格写 [主题]" → 使用卡兹克风格 + 四层自检
- "写 [主题] 公众号文章" → 默认知鱼说风格 + 四层自检（所有风格统一质检）
- "创作 [主题] 内容" → 自动判断风格

系统会自动按照 [WORKFLOW.md](../WORKFLOW.md) 的标准流程完成创作。

---

## 📋 文档分工

| 文档 | 负责内容 |
|------|----------|
| **[WORKFLOW.md](../WORKFLOW.md)** | 📝 两种写作风格、排版格式、配图规则、质量检查、四层自检体系 |
| **[SKILL.md](./SKILL.md)** (本文件) | 🛠️ 脚本使用、API 配置、技术实现 |

---

## 前置条件

项目根目录 `.env` 文件需配置：

```env
# APImart 图片生成
APIMART_API_KEY=你的API密钥

# Tavily 搜索（可选）
TAVILY_API_KEY=你的API密钥
```

微信 API 凭证由 `baoyu-post-to-wechat` skill 管理。

依赖安装：

```bash
pip install -r requirements.txt
```

---

## 脚本说明

| 脚本 | 功能 | 对应 WORKFLOW 步骤 |
|------|------|-------------------|
| `scripts/research.py` | Tavily + Exa 双引擎搜索采集 | Step 2: 搜索素材 |
| `scripts/image_gen.py` | APImart AI 配图生成 | Step 5: 生成配图 |
| `scripts/wechat_api.py` | 微信素材上传 | Step 6: 上传图片 |
| `scripts/publish.py` | 微信草稿箱发布 | Step 7: 发布到微信 |

---

## 1. 素材搜索采集

**目标**：获取主题相关的最新高质量素材。

**双引擎支持**：
- **Tavily**：综合搜索，支持新闻/财经分类、时间范围过滤
- **Exa**：语义搜索，擅长高质量内容发现、AI 摘要、学术/技术内容

### 深度研究（推荐，双引擎）

```bash
cd <项目根>
# 双引擎搜索（默认，Tavily + Exa）
py ai-wechat-publisher/scripts/research.py research "<主题>" --save output/research_notes.md

# 仅 Tavily
py ai-wechat-publisher/scripts/research.py research "<主题>" --engine tavily --save output/research_notes.md

# 仅 Exa
py ai-wechat-publisher/scripts/research.py research "<主题>" --engine exa --save output/research_notes.md
```

### Tavily 搜索

```bash
# 基础搜索
py ai-wechat-publisher/scripts/research.py search "<主题>" --max-results 5 --save output/research_notes.md

# 新闻搜索
py ai-wechat-publisher/scripts/research.py search "<主题>" --topic news --time-range week

# 域名过滤
py ai-wechat-publisher/scripts/research.py search "<主题>" --include-domains github.com,docs.anthropic.com
```

### Exa 语义搜索

```bash
# 基础语义搜索
py ai-wechat-publisher/scripts/research.py exa-search "<主题>" --max-results 5 --with-summary

# 按分类搜索（company/research paper/news/github/tweet/pdf）
py ai-wechat-publisher/scripts/research.py exa-search "<主题>" --category "research paper" --with-text

# 按日期过滤
py ai-wechat-publisher/scripts/research.py exa-search "<主题>" --start-date "2025-01-01" --with-summary

# 关键词搜索
py ai-wechat-publisher/scripts/research.py exa-search "<主题>" --type keyword
```

### 深度提取

```bash
py ai-wechat-publisher/scripts/research.py extract "https://example.com/article" --save output/extracted.md
```

---

## 2. AI 配图生成

**配图规则**（详见 [WORKFLOW.md](../WORKFLOW.md)）：
- 数量：3 张
- 位置：30% / 60% / 90%（按文章进度）
  - IMAGE_1（30%）吸引注意力，配合正文展开
  - IMAGE_2（60%）缓冲节奏，配合转折分析
  - IMAGE_3（90%）收尾升华，配合总结判断
- 比例：16:9

### 生成图片

```bash
py ai-wechat-publisher/scripts/image_gen.py generate "英文 prompt, digital art style, high quality, 16:9 aspect ratio" --output output/image_1.jpg --size 16:9
```

### 高分辨率

```bash
py ai-wechat-publisher/scripts/image_gen.py generate "英文 prompt" --output output/image_1.jpg --resolution 2K
```

### 失败回退

```bash
py ai-wechat-publisher/scripts/image_gen.py fallback "简短描述" --output output/image_1.jpg
```

---

## 3. 微信发布

### 上传图片

```bash
py ai-wechat-publisher/scripts/wechat_api.py batch-upload output/image_1.jpg output/image_2.jpg output/image_3.jpg
```

返回示例：
```json
[
  {"media_id": "xxx", "url": "http://mmbiz.qpic.cn/...", "file": "output\\image_1.jpg"},
  {"media_id": "yyy", "url": "http://mmbiz.qpic.cn/...", "file": "output\\image_2.jpg"}
]
```

### 发布到草稿箱

```bash
py ai-wechat-publisher/scripts/publish.py output/article.md \
  --replacements "IMAGE_1:url1" "IMAGE_2:url2" "IMAGE_3:url3" \
  --cover-index 1
```

---

## 完整工作流

```
用户: "写一篇关于 XX 的文章"
         │
         ▼
┌─────────────────────────────────────────────────────────┐
│  1️⃣ 选择风格                                            │
│     - 默认：知鱼说（实战派）                             │
│     - 可选：卡兹克（有见识的普通人）                     │
└─────────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────┐
│  2️⃣ 撰写文章                                            │
│     按选定风格规范撰写                                    │
│     - 知鱼说：emoji 章节标记，引用块开头结尾              │
│     - 卡兹克：口语化转场，无小标题                        │
│     - 统一：四层质检（L1→L2→L3→L4）                      │
└─────────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────┐
│  3️⃣ ai-wechat-publisher (本工具集)                       │
│     - research.py → 搜索采集素材（可选）                  │
│     - image_gen.py → 生成 3 张配图                       │
│     - wechat_api.py → 上传图片                           │
└─────────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────┐
│  4️⃣ baoyu-post-to-wechat                                │
│     - publish.py → 发布到微信草稿箱                      │
└─────────────────────────────────────────────────────────┘
```

---

## 错误处理

| 错误场景 | 处理方式 |
|---------|---------|
| APImart 图片生成失败 | 自动使用 fallback 占位图 |
| Tavily API 报错 | 检查 TAVILY_API_KEY，自动降级到 Exa |
| Exa API 报错 | 检查 EXA_API_KEY，自动降级到 Tavily |
| 双引擎都失败 | 检查网络连接，手动搜索补充素材 |
| 搜索结果不足 | 扩大时间范围，或使用备用关键词 |
| WeChat IP 白名单 | 登录后台添加当前 IP |

---

## 📚 相关文档

- **[WORKFLOW.md](../WORKFLOW.md)** - 两种写作风格、流程规范、四层自检体系
- **[README.md](../README.md)** - 项目说明和快速开始
- **[khazix-skills/khazix-writer/SKILL.md](~/.claude/skills/khazix-skills/khazix-writer/SKILL.md)** - 卡兹克风格完整参考
