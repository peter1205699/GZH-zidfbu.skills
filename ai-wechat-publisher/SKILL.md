---
name: ai-wechat-publisher
description: AI热点公众号一键发布。从搜索采集到草稿箱发布全流程自动化。当用户提到"写公众号文章"、"发公众号"、"AI热点"、"发布文章"、"写一篇关于XX的文章到公众号"、"gzh发布"、"auto publish wechat"、"draft to wechat"时触发。即使用户只说"帮我写篇文章"且上下文涉及公众号，也应触发。
---

# AI 微信公众号一键发布

用户只需提供主题关键词（如 "写一篇 DeepSeek 的文章"），即可自动完成从素材采集到草稿箱发布的全流程。

## 前置条件

项目根目录 `.env` 文件需配置：

```
WECHAT_APP_ID=公众号AppID
WECHAT_APP_SECRET=公众号AppSecret
APIMART_API_KEY=APImart API Key（图片生成）
```

依赖安装：`pip install -r requirements.txt`

---

## 工作流程（严格按顺序执行）

### 第 0 步：收集用户偏好

**触发条件**：用户给出主题关键词后，先确认以下偏好再开始工作。

**向用户询问**（简洁提问，不要一次问太多）：

```
主题：DeepSeek（用户已提供）
请选择文章风格：
  1. 技术深度 — 面向开发者，深入技术细节
  2. 通俗易懂 — 面向大众，生动有趣
  3. 行业分析 — 面向投资人/从业者，侧重市场分析

配图数量（1-5张，默认2张）：__
```

如果用户没有明确回复，使用默认值：通俗易懂风格 + 2 张配图。不要反复追问，耽误用户时间。

---

### 第 1 步：智能搜索采集

**目标**：获取主题相关的最新高质量素材。

**操作**：

1. 使用 Exa 或 Tavily MCP 搜索工具，构建精准搜索词：
   - 英文搜索：`"<主题> AI latest news update"`、`"<主题> breakthrough 2025"`
   - 中文搜索：`"<主题> 最新消息 动态"`

2. 搜索策略：
   - 优先获取 24 小时内的内容
   - 每次搜索返回 5-8 条结果
   - 重点关注：官方公告、权威媒体报道、技术博客、社交平台热议

3. 结构化整理采集到的信息：
   - 事实数据（数字、日期、版本号）
   - 关键观点和引用
   - 市场反应和行业评价

4. 保存素材摘要到 `output/research_notes.md`。

---

### 第 2 步：内容生成引擎

**目标**：基于采集素材和用户偏好风格，生成高质量公众号文章。

**操作**：

1. 先读取 `references/style-guide.md` 获取写作风格指南。这一步很重要——遵循风格指南才能写出不像 AI 生成的文章。

2. 按以下结构生成文章（Markdown 格式）：

```markdown
# [吸引人的标题，不要太长]

[开篇 — 用一个引人入胜的切入，不要用"近日"、"随着"开头]

---

## [第一部分标题]

<!-- IMAGE_1: 配图描述文字 -->

[正文内容]

## [第二部分标题]

<!-- IMAGE_2: 配图描述文字 -->

[正文内容]

...

---

[结尾 — 简洁有力，引发思考或讨论]
```

3. 配图标记规则：
   - 使用 `<!-- IMAGE_N: 描述文字 -->` 格式
   - N 从 1 开始递增，数量与用户要求的配图数量一致
   - 描述文字要具体、可视化（不是"相关图片"，而是"科技蓝色背景下展示的神经网络可视化图表，带有DeepSeek logo元素"）
   - 配图标记分散在文章各处，不要全部堆在一起

4. 保存到 `output/article.md`。

---

### 第 3 步：配图生成

**目标**：为每张配图标记生成高质量图片。

**操作**：

1. 解析 `output/article.md` 中所有 `<!-- IMAGE_N: ... -->` 标记，提取编号和描述。

2. 对每个图片描述进行优化：
   - 在英文描述基础上追加风格关键词
   - 添加 `"digital art style, high quality, 16:9 aspect ratio"`
   - 如果描述是中文，翻译为英文后再提交给 API

3. 调用 APImart (Gemini-3-Pro) API 生成配图（异步模式，脚本自动轮询）：
   ```bash
   python scripts/image_gen.py generate "优化后的英文prompt" --output "output/image_N.jpg"
   # 可选高分辨率
   python scripts/image_gen.py generate "优化后的英文prompt" --output "output/image_N.jpg" --resolution 2K
   ```

4. 如果某张图生成失败，使用 fallback 方案：
   ```bash
   python scripts/image_gen.py fallback "简短描述" --output "output/image_N.jpg"
   ```

5. 所有图片保存到 `output/` 目录。

---

### 第 4 步：微信集成发布

**目标**：将文章和图片上传到微信，创建草稿箱文章。

**操作**：

1. **上传所有配图到微信服务器**：
   ```bash
   python scripts/wechat_api.py batch-upload output/image_1.jpg output/image_2.jpg ...
   ```
   记录每张图片返回的 `url`（微信 mmbiz 域名 URL）。

2. **转换并发布**：
   ```bash
   python scripts/publish.py output/article.md \
     --replacements "IMAGE_1:微信URL1" "IMAGE_2:微信URL2" \
     --cover-index 1
   ```
   脚本会：
   - 将 Markdown 转为公众号兼容的内联样式 HTML
   - 用微信图片 URL 替换占位标记
   - 第一张图作为封面（thumb_media_id）
   - 调用微信草稿箱 API 创建草稿

3. 成功后记录返回的 `media_id`。

---

### 第 5 步：用户确认

**目标**：通知用户并提供后续操作指引。

**操作**：输出以下内容：

```
✅ 文章已发布到公众号草稿箱！

📋 标题：<标题>
🆔 media_id：<media_id>
🖼 配图：<N> 张

请前往 mp.weixin.qq.com → 内容管理 → 草稿箱 检查文章。

需要我帮你：
  1. 直接发布（确认内容无误后）
  2. 修改文章（告诉我需要改哪里）
  3. 重新生成配图
```

如果用户回复"直接发布"或"发布"：
```bash
python scripts/wechat_api.py publish <media_id>
```

---

## 脚本说明

| 脚本 | 功能 |
|------|------|
| `scripts/wechat_api.py` | 微信 API：token管理、图片上传、草稿箱、发布 |
| `scripts/publish.py` | Markdown→HTML转换、占位符替换、草稿创建 |
| `scripts/image_gen.py` | APImart (Gemini-3-Pro) 配图生成（异步轮询）+ fallback占位图 |

每个脚本都支持 `--help` 查看详细用法。

## 错误处理

| 错误场景 | 处理方式 |
|---------|---------|
| access_token 过期 | 自动刷新，重试一次 |
| 图片上传失败 | 检查大小(<10MB)和格式(jpg/png)，重新尝试 |
| APImart 图片生成失败 | 自动使用 fallback 占位图 |
| 草稿箱创建失败 | 检查 HTML 长度(<20000字符)，精简内容后重试 |
| 搜索结果不足 | 扩大时间范围到 7 天，或使用备用关键词 |
