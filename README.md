# 公众号写作助手

> 基于 Claude Code + wechraft-writer + ai-wechat-publisher 的自动化写作系统

**支持两种写作风格**：知鱼说（实战派）+ 卡兹克（有见识的普通人）

---

## 🚀 快速开始

只需输入你的创作主题，例如：

```
写一篇关于 AI Agent 的文章
```

系统会自动按照标准流程完成：**写作 → 配图 → 发布**

**指定风格**：
```
用卡兹克风格写一篇关于 DeepSeek 的文章
```

---

## 📖 文档导航

| 文档 | 用途 | 适合人群 |
|------|------|----------|
| **[WORKFLOW.md](WORKFLOW.md)** 📝 | 两种写作风格、排版格式、配图规则、质量检查 | 写作时查阅 |
| **[ai-wechat-publisher/SKILL.md](ai-wechat-publisher/SKILL.md)** 🛠️ | 脚本使用、API 配置、技术实现 | 开发时查阅 |
| **[README.md](README.md)** (本文件) 📚 | 项目说明、快速开始、环境配置 | 新手入门 |
| **[QUICKREF.md](QUICKREF.md)** ⚡ | 快速参考卡片、风格对比 | 写作时速查 |

---

## 🎨 写作风格

### 风格 A：知鱼说（默认）

**特点**：实战派，不整虚的概念，只讲能落地的玩法

**适合**：行业分析、趋势解读、方法论分享

```markdown
> 🐟 知鱼说：别被"..."这种假象骗了，今天咱只讲一个事儿——...
```

### 风格 B：卡兹克

**特点**：有见识的普通人在认真聊一件打动他的事

**适合**：产品体验、调查实验、个人观点

```markdown
最近这两天，被...给刷屏了。
（从具体事件切入，无固定格式）
```

> 📖 **详细对比** 请参阅 **[WORKFLOW.md → 文章风格选择](WORKFLOW.md#-文章风格选择)**

---

## 📁 项目结构

```
GZH-zhidangfb/
├── WORKFLOW.md              # 📝 两种写作风格、流程规范
├── README.md                # 📚 本文件
├── QUICKREF.md              # ⚡ 快速参考卡片
├── .env                     # API 密钥配置
├── output/                  # 输出目录
│   ├── article.md          # 文章内容
│   └── image_*.jpg         # 配图
└── ai-wechat-publisher/     # 写作工具集
    ├── SKILL.md            # 🛠️ 技能定义（技术文档）
    └── scripts/            # 脚本工具
```

---

## 🎯 风格选择建议

| 场景 | 推荐风格 | 理由 |
|------|----------|------|
| 行业分析、趋势解读 | 知鱼说 | 更有条理，适合分析类内容 |
| 产品体验、调查实验 | 卡兹克 | 更有故事感，适合叙事类内容 |
| 方法论、工具分享 | 知鱼说 | 更清晰，适合教学类内容 |
| 个人观点、情绪表达 | 卡兹克 | 更真实，适合观点类内容 |

---

## 🛠️ 环境配置

### 安装依赖

```bash
pip install -r requirements.txt
```

### 配置 API 密钥

编辑 `.env` 文件：

```env
# 微信公众号
WECHAT_APP_ID=你的AppID
WECHAT_APP_SECRET=你的AppSecret

# APImart 图片生成
APIMART_API_KEY=你的API密钥

# Tavily 搜索（可选）
TAVILY_API_KEY=你的API密钥
```

---

## 🔧 常用命令

### 生成配图

```bash
py ai-wechat-publisher/scripts/image_gen.py generate "描述" --output output/image_1.jpg --size 16:9
```

### 上传图片到微信

```bash
py ai-wechat-publisher/scripts/wechat_api.py batch-upload output/image_1.jpg output/image_2.jpg output/image_3.jpg
```

### 发布到草稿箱

```bash
py ai-wechat-publisher/scripts/publish.py output/article.md \
  --replacements "IMAGE_1:url1" "IMAGE_2:url2" "IMAGE_3:url3" \
  --cover-index 1
```

---

## 🔄 完整工作流

```
用户输入主题
     │
     ▼
┌─────────────────────────────────────────────────────────┐
│  1️⃣ 选择风格（知鱼说 / 卡兹克）                          │
└─────────────────────────────────────────────────────────┘
     │
     ▼
┌─────────────────────────────────────────────────────────┐
│  2️⃣ 撰写文章                                            │
│     按选定风格规范撰写                                    │
└─────────────────────────────────────────────────────────┘
     │
     ▼
┌─────────────────────────────────────────────────────────┐
│  3️⃣ 生成配图（3张，16:9，30%/60%/90%位置）               │
└─────────────────────────────────────────────────────────┘
     │
     ▼
┌─────────────────────────────────────────────────────────┐
│  4️⃣ 发布到微信草稿箱                                    │
└─────────────────────────────────────────────────────────┘
```

---

## 📚 快速查找

| 我想... | 查看文档 |
|---------|----------|
| 了解两种写作风格 | [WORKFLOW.md → 文章风格选择](WORKFLOW.md#-文章风格选择) |
| 查看配图规则 | [WORKFLOW.md → 配图规则](WORKFLOW.md#-配图规则) |
| 知鱼说质量检查 | [WORKFLOW.md → 质量检查](WORKFLOW.md#-质量检查清单) |
| 卡兹克四层自检 | [WORKFLOW.md → 质量检查](WORKFLOW.md#-质量检查清单) |
| 快速风格对比 | [QUICKREF.md](QUICKREF.md) |
| 使用搜索脚本 | [SKILL.md → 素材搜索](ai-wechat-publisher/SKILL.md#1-素材搜索采集) |
| 配图生成命令 | [SKILL.md → AI 配图](ai-wechat-publisher/SKILL.md#2-ai-配图生成) |
| 微信发布流程 | [SKILL.md → 微信发布](ai-wechat-publisher/SKILL.md#3-微信发布) |

---

*最后更新：2026-04-21*
