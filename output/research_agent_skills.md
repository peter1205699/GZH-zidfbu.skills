# Agent Skills 深度研究报告

> 本报告为微信公众号文章撰写提供全面的研究素材，涵盖 Agent Skills 的历史、技术定义、核心架构、生态系统与实践案例。

---

## 一、历史与时间线

### 1.1 Agent Skills 的诞生背景

2025年，AI Agent（智能体）技术快速发展，但一个核心问题始终困扰着开发者和企业：**如何让 AI Agent 准确、可靠地执行特定领域的复杂任务？** 大语言模型虽然具备强大的通用能力，但在处理特定格式文件（如 PDF 表单填写、PPT 生成）、遵循特定工作流、或操作特定工具时，往往表现不稳定。

Anthropic 的工程团队将这个问题类比为：**"为一个新员工准备入职手册"**——Agent Skills 本质上就是为 AI Agent 准备的标准化操作手册。

### 1.2 关键时间节点

| 时间 | 事件 |
|------|------|
| **2025年10月** | Anthropic 推出 Agent Skills 功能，作为 Claude 产品的核心能力扩展机制。同时在 API 中引入 beta header `skills-2025-10-02` |
| **2025年10月** | 发布四项预构建 Skills：PowerPoint (pptx)、Excel (xlsx)、Word (docx)、PDF (pdf) |
| **2025年10月** | 开源 Claude API Skill，覆盖 8 种编程语言，随 Claude Code 捆绑发布 |
| **2025年12月18日** | 发布开放标准规范，上线 agentskills.io 网站，公开 SKILL.md 格式规范 |
| **2025年12月18日** | Anthropic 发表工程博客 "Equipping Agents for the Real World with Agent Skills"，详细阐述设计理念 |

### 1.3 设计哲学

Agent Skills 的核心设计哲学来自 Anthropic 工程师 Barry Zhang、Keith Lazaka 和 Mahesh Murag 的阐述：

> "Building a skill for an agent is like putting together an onboarding guide for a new hire."
> "为 Agent 构建一个 Skill，就像为一名新员工准备入职手册。"

关键理念包括：
- **模块化**：每个 Skill 是一个独立的文件夹，包含指令、脚本和资源
- **渐进式披露（Progressive Disclosure）**：按需加载，不浪费上下文窗口
- **代码执行**：确定性操作通过脚本完成，不消耗模型推理能力
- **开放标准**：格式规范完全公开，任何人都可以创建和分享 Skills

---

## 二、技术定义

### 2.1 什么是 Agent Skills？

**Agent Skills** 是一组模块化的能力包，通过文件系统中的目录结构来扩展 AI Agent 的功能。每个 Skill 是一个包含指令、脚本和资源的文件夹，Agent 可以发现并使用这些 Skill 来更准确、更高效地完成任务。

官方定义：
> "Agent Skills are folders of instructions, scripts, and resources that agents can discover and use to do things more accurately and efficiently."

### 2.2 三类核心内容

Agent Skills 包含三类内容：

| 内容类型 | 说明 | 示例 |
|----------|------|------|
| **Instructions（指令）** | 用自然语言编写的操作指南，告诉 Agent 如何完成特定任务 | PDF 表单字段的识别与填写规则 |
| **Code/Scripts（代码/脚本）** | 可执行的程序脚本，处理确定性操作 | `scripts/fill_form.py` 自动填写 PDF 表单 |
| **Resources（资源）** | 参考文档、模板、数据文件等辅助材料 | 模板文件、参考手册、数据集 |

### 2.3 目录结构

一个标准的 Skill 目录结构如下：

```
my-skill/
├── SKILL.md          # 必需：技能定义文件（YAML frontmatter + Markdown）
├── scripts/          # 可选：可执行脚本
│   ├── process.py
│   └── validate.sh
├── references/       # 可选：参考文档（按需加载）
│   ├── REFERENCE.md
│   ├── FORMS.md
│   └── api-guide.md
└── assets/           # 可选：模板、图片、数据文件
    ├── template.pptx
    └── schema.json
```

**核心文件**：`SKILL.md` 是唯一必需的文件，其余目录和文件都是可选的。

### 2.4 触发机制

Agent Skills 的触发是一个三阶段过程：

```
阶段1: 元数据加载 → Agent 系统提示中包含所有 Skill 的 name + description
                         ↓（当用户请求匹配某个 Skill 时）
阶段2: 指令加载   → Agent 通过 bash 命令读取 SKILL.md 的完整内容
                         ↓（当任务需要额外信息时）
阶段3: 资源加载   → Agent 按需读取 references/ 目录中的文件
```

这种设计确保了：
- **未使用的 Skill 几乎不消耗上下文**（仅 ~100 tokens 的元数据）
- **只有被触发的 Skill 才会加载完整指令**（< 5000 tokens）
- **参考资料按需加载**（无实际大小限制）

---

## 三、"最后一公里"问题

### 3.1 问题定义

AI 领域的"最后一公里"问题指的是：**大语言模型已经具备强大的通用能力，但在将这种能力转化为特定场景下的可靠、精确执行时，仍然存在显著差距。**

具体表现包括：
- **格式准确性**：生成 PPT 时幻灯片布局不正确
- **工作流遵循**：处理 PDF 表单时跳过必要步骤
- **工具操作**：使用 API 时参数格式错误
- **领域知识**：特定行业的专业术语和处理规则

### 3.2 Agent Skills 如何解决

Agent Skills 通过三个层面解决"最后一公里"问题：

#### 3.2.1 指令层面：精确的操作指南

SKILL.md 中的指令提供了精确的、上下文相关的操作步骤，而非泛泛的通用建议。例如，PDF Skill 不只是告诉 Agent "填写表单"，而是详细说明了：
- 如何识别不同类型的表单字段
- 每种字段应使用何种填写方式
- 如何处理日期、金额等特殊格式
- 如何验证填写结果的正确性

#### 3.2.2 代码层面：确定性执行

通过 `scripts/` 目录中的脚本，将需要精确执行的操作从模型推理中剥离出来：
- 模型负责理解和决策
- 脚本负责精确执行
- 两者配合，既保留了灵活性，又确保了准确性

例如，`fill_form.py` 脚本可以精确地将数据填入 PDF 表单的指定位置，避免了模型可能产生的格式错误。

#### 3.2.3 架构层面：渐进式披露

渐进式披露设计确保 Agent 能够：
1. 快速了解所有可用能力（通过元数据）
2. 深入学习与当前任务相关的操作指南（通过 SKILL.md）
3. 按需查阅详细的参考资料（通过 references/）

这种分层设计使得 Agent 在有限的上下文窗口内，既能"知道有什么"，又能"学会怎么做"，还能"查阅详细信息"。

### 3.3 实际效果

以 PDF Skill 为例，Anthropic 展示了完整的工作流：

```
用户："帮我填写这份税务表格"
  ↓
Agent 识别匹配 PDF Skill（阶段1：元数据匹配）
  ↓
读取 SKILL.md 中的 PDF 处理指令（阶段2：指令加载）
  ↓
读取 FORMS.md 中的表单字段定义（阶段3：资源加载）
  ↓
读取 REFERENCE.md 中的 API 参考（阶段3：资源加载）
  ↓
调用 scripts/fill_form.py 填写表单（代码执行）
  ↓
返回填写完成的 PDF 文件
```

---

## 四、生态系统与社区

### 4.1 Anthropic 官方 Skills

#### 预构建 Skills（Pre-built Skills）

Anthropic 提供了四项预构建 Skills，开箱即用：

| Skill | 功能 | 适用场景 |
|-------|------|----------|
| **pptx** | 创建和编辑 PowerPoint 演示文稿 | 自动生成报告演示、数据可视化 |
| **xlsx** | 创建和编辑 Excel 电子表格 | 数据分析报表、财务建模 |
| **docx** | 创建和编辑 Word 文档 | 自动生成报告、合同模板 |
| **pdf** | 处理 PDF 文件，包括表单填写 | 自动化文档处理、批量表单填写 |

#### 开源 Skill：Claude API Skill

- 覆盖 **8 种编程语言**的代码生成辅助
- 随 Claude Code 捆绑发布
- 开源在 GitHub 上

### 4.2 跨平台支持

Agent Skills 在不同 Claude 产品中的支持情况：

| 平台 | Skills 支持 | 运行环境限制 | 分享范围 |
|------|------------|-------------|----------|
| **claude.ai** | 预构建 Skills + 自定义 Skills | 网络访问权限因用户等级而异 | 个人级别 |
| **Claude API** | 通过 beta API 调用 | 无网络访问，无法运行时安装 | Workspace 级别 |
| **Claude Code** | 完整支持 + 自定义 Skills | 完整网络访问 | 个人/项目级别（`.claude/skills/`） |
| **Claude Agent SDK** | 完整支持 | 取决于部署环境 | 取决于部署配置 |

### 4.3 API 集成

在 Claude API 中使用 Skills 需要：

**Beta Headers:**
```
code-execution-2025-08-25
skills-2025-10-02
files-api-2025-04-14
```

**Container 参数:**
```json
{
  "container": {
    "skills": [
      {
        "type": "anthropic",
        "skill_id": "pdf",
        "version": "latest"
      }
    ]
  }
}
```

**Python SDK 示例:**
```python
# 列出可用的 Anthropic Skills
skills = client.beta.skills.list(
    source="anthropic",
    betas=["skills-2025-10-02"]
)

# 使用 Skill 创建消息
response = client.beta.messages.create(
    model="claude-sonnet-4-20250514",
    messages=[{"role": "user", "content": "Create a presentation about AI trends"}],
    container={
        "skills": [{"type": "anthropic", "skill_id": "pptx"}]
    },
    betas=["skills-2025-10-02", "code-execution-2025-08-25"]
)
```

### 4.4 开放标准与社区

**agentskills.io** 是 Agent Skills 的开放标准发布站点，于 2025年12月18日上线。该网站声明：
- Agent Skills 规范完全开放
- 被领先的 AI 开发工具所支持
- 任何人都可以创建、分享和使用 Skills

**验证工具：** Anthropic 提供了命令行验证工具：
```bash
skills-ref validate ./my-skill
```

### 4.5 限制与注意事项

- **不支持 ZDR（Zero Data Retention）** 环境
- Skills 提供新的能力，但安全性取决于来源——只使用可信来源的 Skills
- 不同平台的运行时环境限制不同（网络访问、安装权限等）

---

## 五、SKILL.md 格式技术深度解析

### 5.1 文件格式

SKILL.md 采用 YAML frontmatter + Markdown body 的格式：

```markdown
---
name: skill-name
description: A clear description of what this skill does and when to use it.
license: MIT
compatibility: claude-code, claude-api
metadata:
  author: developer-name
  version: 1.0.0
allowed-tools: bash read write
---

# Skill Instructions

Your detailed instructions for the agent go here.
Use Markdown formatting for clarity.
```

### 5.2 Frontmatter 字段详解

#### name（必需）

| 属性 | 要求 |
|------|------|
| 长度 | 1-64 个字符 |
| 允许字符 | 小写字母 a-z、数字 0-9、连字符 `-` |
| 限制 | 不允许连续连字符（`--`）、不能以连字符开头或结尾 |
| 匹配规则 | 必须与父目录名称完全一致 |

有效示例：`processing-pdfs`、`data-analysis`、`code-review`
无效示例：`PDF-Processing`（大写）、`pdf--processing`（连续连字符）、`-pdf`（连字符开头）

**命名规范**：推荐使用动名词形式（gerund form），如：
- `processing-pdfs`（而非 `pdf-processor`）
- `analyzing-spreadsheets`（而非 `spreadsheet-analyzer`）
- `generating-reports`（而非 `report-generator`）

#### description（必需）

| 属性 | 要求 |
|------|------|
| 长度 | 1-1024 个字符 |
| 内容 | 描述 Skill 的功能 **以及** 何时应使用它 |

**描述规范**：
- 使用第三人称描述
- 包含具体关键词以提高触发准确率
- 明确说明触发条件

好的示例：
```
Processes PDF forms by extracting fields, validating data, and filling
in values. Use when the user needs to fill, extract, or modify PDF
form fields, or when working with structured PDF documents.
```

差的示例：
```
Works with PDFs.
```

#### license（可选）

标准开源许可证标识，如 `MIT`、`Apache-2.0`。

#### compatibility（可选）

| 属性 | 要求 |
|------|------|
| 长度 | 最大 500 个字符 |
| 内容 | 说明 Skill 兼容的平台和环境 |

示例：`claude-code, claude-api, claude.ai`

#### metadata（可选）

任意键值对，用于存储额外的元信息。可以包含：
- `author`：作者信息
- `version`：版本号
- `tags`：分类标签
- 其他自定义字段

#### allowed-tools（实验性，可选）

| 属性 | 要求 |
|------|------|
| 格式 | 空格分隔的工具名称列表 |
| 状态 | 实验性功能 |
| 用途 | 声明 Skill 需要使用的工具 |

示例：`bash read write edit`

### 5.3 Body（指令正文）

SKILL.md 的 Markdown 正文是给 Agent 的操作指令，**没有格式限制**。但有以下建议：

| 建议 | 说明 |
|------|------|
| **长度控制** | 保持在 500 行以内 |
| **拆分策略** | 超过 500 行时，将详细内容拆分到 `references/` 目录 |
| **清晰结构** | 使用标题、列表、代码块等 Markdown 格式提高可读性 |

### 5.4 参考文档组织（references/）

`references/` 目录用于存放按需加载的详细文档：

```
references/
├── REFERENCE.md      # 主参考文档
├── FORMS.md          # 表单相关文档
└── api-guide.md      # 特定领域文档
```

**组织建议**：
- 保持 `references/` 与 `SKILL.md` 之间只有一级深度
- 不要创建深层嵌套的参考文档结构
- 每个参考文件应聚焦一个主题

### 5.5 脚本目录（scripts/）

`scripts/` 中的脚本应满足：
- **自包含**：不依赖外部库（除非是运行时环境中已有的）
- **友好的错误信息**：出错时提供清晰的诊断信息
- **幂等性**：重复执行应产生相同结果

### 5.6 渐进式披露的三种模式

根据 Anthropic 最佳实践文档，推荐三种渐进式披露模式：

#### 模式一：高层指南 + 参考文档

```
SKILL.md → 高层操作指南
references/REFERENCE.md → 详细技术参考
```
适用于：大多数通用型 Skills

#### 模式二：领域特定组织

```
SKILL.md → 核心指令
references/FORMS.md → 表单处理专题
references/API.md → API 使用专题
```
适用于：多子领域的复合型 Skills

#### 模式三：条件性细节

```
SKILL.md → 基础流程 + 条件分支说明
references/edge-cases.md → 特殊情况处理
```
适用于：有复杂边界情况的 Skills

### 5.7 验证与质量保证

使用 Anthropic 提供的验证工具检查 Skill 格式：

```bash
skills-ref validate ./my-skill
```

**反馈循环**：验证 → 修复 → 重新验证，直到通过所有检查。

### 5.8 反模式（Anti-patterns）

应避免的常见错误：

| 反模式 | 说明 |
|--------|------|
| **使用 Windows 路径** | 不要使用反斜杠路径，统一使用正斜杠 |
| **提供过多选项** | 过多的分支选择会让 Agent 困惑 |
| **深层嵌套引用** | references/ 下不要再嵌套子目录 |
| **冗长的解释** | 指令应简洁明确，不要长篇解释"为什么" |

---

## 六、实践案例与使用指南

### 6.1 案例一：使用预构建 Skill 生成 PowerPoint

```python
import anthropic

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-sonnet-4-20250514",
    messages=[{
        "role": "user",
        "content": "创建一份关于2025年AI趋势的演示文稿，包含10张幻灯片"
    }],
    container={
        "skills": [
            {"type": "anthropic", "skill_id": "pptx"}
        ]
    },
    betas=["skills-2025-10-02", "code-execution-2025-08-25", "files-api-2025-04-14"]
)

# 通过 Files API 下载生成的文件
```

### 6.2 案例二：PDF 表单自动填写

完整的 PDF 表单填写流程：

```
1. 用户上传 PDF 表单 + 数据文件
2. Agent 匹配 PDF Skill
3. 读取 SKILL.md 中的表单处理指令
4. 按需读取 FORMS.md 了解字段类型
5. 按需读取 REFERENCE.md 查阅 API
6. 调用 scripts/fill_form.py 执行填写
7. 返回填写完成的 PDF
```

### 6.3 案例三：Claude Code 中使用自定义 Skill

在 Claude Code 中，自定义 Skills 存放在 `.claude/skills/` 目录下：

```
.claude/skills/
└── code-review/
    ├── SKILL.md
    ├── scripts/
    │   └── lint.sh
    └── references/
        └── style-guide.md
```

Skill 会在项目级别自动发现和加载。

### 6.4 最佳实践：评估驱动开发

Anthropic 推荐的 Skill 开发流程：

```
1. 识别差距 → 分析 Agent 在哪些任务上表现不佳
2. 创建评估 → 为每个差距创建测试用例
3. 基线测量 → 不使用 Skill 时的表现
4. 最小指令 → 编写最少量的指令来改善表现
5. 迭代优化 → 根据评估结果持续改进
```

### 6.5 "Claude A / Claude B" 迭代开发模式

Anthropic 推荐一种有趣的开发模式：

- **Claude A（专家辅助者）**：帮助人类开发者创建和优化 Skill
- **Claude B（Agent 用户）**：使用 Skill 执行实际任务

开发循环：
```
人类 + Claude A → 编写/优化 SKILL.md
       ↓
Claude B → 使用 Skill 执行任务
       ↓
评估结果 → 发现问题
       ↓
人类 + Claude A → 修复问题
       ↓
（循环继续）
```

### 6.6 有效 Skill 检查清单

**核心质量：**
- [ ] name 使用动名词形式，符合命名规范
- [ ] description 清晰说明功能和触发条件
- [ ] 指令简洁明确，不超过 500 行
- [ ] 使用了合适的渐进式披露模式

**代码/脚本：**
- [ ] 脚本自包含，无外部依赖
- [ ] 错误信息清晰友好
- [ ] 通过 `skills-ref validate` 验证

**测试：**
- [ ] 在所有目标模型上测试
- [ ] 覆盖正常和边界情况
- [ ] 根据评估结果优化

---

## 七、安全考量

### 7.1 Anthropic 官方安全建议

- **只使用可信来源的 Skills**：Skills 通过指令和代码提供新能力，不安全的 Skill 可能导致意外行为
- **审计 Skill 内容**：在使用第三方 Skill 前，仔细审查其指令和脚本
- **注意数据暴露**：Skill 可能会访问和处理敏感数据
- **工具使用风险**：注意 Skill 声明的 `allowed-tools`，防止工具滥用

### 7.2 不符合 ZDR 要求

Agent Skills **不支持 Zero Data Retention (ZDR)** 环境。对数据保留有严格要求的组织需要注意这一限制。

---

## 八、未来展望

Anthropic 在工程博客中暗示了 Agent Skills 的未来方向：

> "未来，我们将使 Agent 能够自主创建、编辑和评估 Skills。"

这意味着：
- Agent 将能够根据自己的经验自动改进 Skills
- Skill 的创建门槛将进一步降低
- Skills 生态系统将实现自我进化

---

## 九、信息来源

本报告的研究数据来自以下官方来源：

1. **agentskills.io** - Agent Skills 开放标准官方网站
2. **agentskills.io/specification** - SKILL.md 格式完整规范
3. **platform.claude.com/docs/en/agents-and-tools/agent-skills/overview** - Anthropic 官方 Skills 概述文档
4. **platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices** - Anthropic 官方最佳实践指南
5. **platform.claude.com/docs/en/agents-and-tools/agent-skills/quickstart** - Anthropic 官方快速入门教程
6. **anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills** - Anthropic 工程博客（作者：Barry Zhang, Keith Lazaka, Mahesh Murag）
