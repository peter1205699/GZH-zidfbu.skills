# 快速参考

> 写作时随时查阅的速查表

---

## 📝 两种输入模式

| 模式 | 触发 | 流程 |
|------|------|------|
| A 从零创作 | 用户提供主题 | 定类型 → 选风格 → 搜素材 → 写 → 质检 → 配图 → 发布 |
| B 改写草稿 | 用户提供全文 | 定类型 → 识别风格 → 搜素材 → 改写 → 质检 → 配图 → 发布 |

---

## 📋 内容类型

| 类型 | 定位 | 核心目标 |
|------|------|----------|
| 热点解读型 | 新鲜事快速反应 | 帮读者「看懂」发生了什么 |
| 案例复盘型 | 项目/事件深度拆解 | 还原过程 + 提炼可复制经验 |
| 观点思考型 | 个人见解输出 | 给读者「新角度」启发 |
| 工具测评型 | 产品深度体验 | 帮读者「决策」是否使用 |
| 实战教程型 | 可操作指南 | 带读者「学会」某技能 |

---

## 🎨 风格选择

### 风格 A：知鱼说（默认）

```
🐟 知鱼说：别被"..."这种假象骗了，今天咱只讲一个事儿——[核心观点]
```

### 风格 B：卡兹克

```
最近这两天，被...给刷屏了。
（从具体事件切入，无固定格式）
```

---

## 📐 排版规则

| 项目 | 知鱼说 | 卡兹克 |
|------|--------|--------|
| 小标题 | emoji + **加粗** | 口语化转场，无小标题 |
| 列表 | 第一、第二 | 自然叙述 |
| 引用 | > 引用块 | > 引用块 |
| 冒号 | ❌ 禁用 | ❌ 禁用 |
| 破折号 | ❌ 禁用 | ❌ 禁用 |
| 双引号 | ❌ 用「」 | ❌ 用「」 |

---

## 📝 富文本格式

| 格式 | 语法 | 使用场景 |
|------|------|---------|
| **加粗** | `**文本**` | 核心观点、关键词、重要数据 |
| *斜体* | `*文本*` | 强调，英文术语需加中文翻译 | *context switching*（上下文切换） |
| ``代码`` | `` `代码` `` | 命令、函数名、配置项 |
| 代码块 | \```语言 \n 代码 \n \``` | 完整代码示例 |
| > 引用 | `> 内容` | 引用观点、官方说明、重要提示 |
| [链接](url) | `[文本](url)` | 参考资料 |

**原则**：
- ✅ 核心观点必须加粗
- ✅ 代码相关必须用代码块
- ✅ 引用资料必须用引用块
- ✅ 英文术语首次出现加括号附中文翻译
- ✅ 深度+通俗：用通俗语言讲有深度的内容
- ❌ 避免过度加粗（< 10%）
- ❌ 主副标题内容必须不同

---

## 🖼️ 配图规则

**3 张，位置 30% / 60% / 90%**

```bash
py ai-wechat-publisher/scripts/image_gen.py generate "[英文 prompt]" --output output/image_N.jpg --size 16:9
```

**质量校验**：文件 > 100KB 才合格，不合格重新生成。

```bash
ls -la output/image_*.jpg
```

---

## ✅ 四层质检

### L1 硬性规则（0 容忍）

- ❌ 禁用词：说白了、意味着什么、本质上、换句话说、不可否认、综上所述
- ❌ 禁用标点：冒号：、破折号——、双引号"" → 用「」
- ❌ 结构套话：让我们来看看、随着...的发展
- ✅ 工具名全部具体
- ✅ 代码块必须指定语言
- ✅ 引用资料用引用块
- ✅ 主副标题内容不同

### L2 风格一致性

- [ ] 开头从具体事件切入
- [ ] ≥ 3 处单句独立成段
- [ ] 口语化词组 ≥ 8 个
- [ ] ≥ 1 处自嘲
- [ ] 核心观点加粗、代码用代码块

### L3 内容质量

- [ ] 观点有场景/数据支撑
- [ ] 知识自然带出
- [ ] **有文化升维**
- [ ] 有对立面理解

### L4 活人感

- [ ] 体感记忆式情绪
- [ ] 独特角度
- [ ] 非导师姿态
- [ ] 心流顺畅

---

## 🔍 素材采集

```bash
# 双引擎（推荐）
py ai-wechat-publisher/scripts/research.py research "[主题]" --engine all --save output/research_notes.md

# Tavily（综合/新闻）
py ai-wechat-publisher/scripts/research.py search "[主题]" --topic news --time-range week

# Exa（语义/学术）
py ai-wechat-publisher/scripts/research.py exa-search "[主题]" --category news --with-summary
```

---

## 🚀 发布命令

**上传配图**：
```bash
NO_PROXY=api.weixin.qq.com HTTP_PROXY= HTTPS_PROXY \
py ai-wechat-publisher/scripts/wechat_api.py batch-upload output/image_1.jpg output/image_2.jpg output/image_3.jpg
```

**发布草稿箱**：
```bash
NO_PROXY=api.weixin.qq.com HTTP_PROXY= HTTPS_PROXY \
py ai-wechat-publisher/scripts/publish.py output/article.md \
  --replacements "IMAGE_1:URL1" "IMAGE_2:URL2" "IMAGE_3:URL3" \
  --cover-index 1
```

**直接发布**：
```bash
py ai-wechat-publisher/scripts/wechat_api.py publish <media_id>
```

---

## ⚡ 常见问题速查

| 问题 | 解决 |
|------|------|
| IP 白名单报错 | 后台添加报错中的 IP |
| 代理连接失败 | 命令前加 `NO_PROXY=api.weixin.qq.com HTTP_PROXY= HTTPS_PROXY=` |
| 配图太小 < 100KB | 重新执行 generate |

---

*最后更新：2026-04-25*
