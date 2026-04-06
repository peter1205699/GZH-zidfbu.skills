# AI编程到底怎么做：真实案例、关键步骤与失败教训

> 研究资料汇总，用于微信公众号文章《AI编程到底怎么做，真实案例里最关键的一步是什么》
> 整理时间：2026年4月

---

## 一、真实开发者案例（2025-2026）

### 1.1 Addy Osmani：90% 的代码由 AI 自己编写

**人物**：Google Chrome 团队工程师，Web 性能领域权威

**案例**：Addy Osmani 在 2025 年底公开分享，他使用 Claude Code 进行开发，约 **90% 的 Claude Code 代码是由 Claude Code 自己编写的**。他提出了完整的 10 步 AI 编码工作流：

1. 从清晰的计划开始（先写规格说明，再写代码）
2. 将工作拆分为小块
3. 提供充分的上下文
4. 选择合适的模型
5. 在整个生命周期中利用 AI（不仅是编码，还包括规划、测试、调试）
6. 保持人在回路中
7. 频繁提交
8. 自定义 AI 行为（CLAUDE.md 等配置文件）
9. 积极拥抱测试
10. 持续学习

来源：[My LLM coding workflow going into 2026](https://addyosmani.com/blog/ai-coding-workflow/)

---

### 1.2 Peter Steinberger：不再读代码的 iOS 独立开发者

**人物**：著名 iOS 开发者，PSPDFKit 创始人

**案例**：Peter Steinberger 公开表示："我不再读太多代码了。"他使用 AI 工具进行大规模代码生成，将审查重心从逐行阅读转向**验证行为和测试结果**。他的工作模式代表了 "资深开发者 + AI = 产出倍增" 的典型路径。

来源：Simon Willison 引述，simonwillison.net/tags/ai/

---

### 1.3 StrongDM 的"黑暗工厂"模式

**人物**：StrongDM 工程团队

**案例**：StrongDM 实现了 Dan Shapiro 提出的"Five Levels"模型中最高等级——**Dark Factory（暗黑工厂）**：没有人审查代码。系统通过**大量测试来自证正确性**。

Dan Shapiro 的五级模型：
- Level 1：Spicy Autocomplete（热辣自动补全）
- Level 2：Coding Intern（编程实习生）
- Level 3：Junior Dev（初级开发者）
- Level 4：Developer / Full-time Reviewer（全职审查者）
- Level 5：Engineering Team → Dark Factory（暗黑工厂）

**关键洞察**：Dark Factory 不是"不用审查"，而是**用测试替代人工审查**。测试覆盖率必须极高，系统才能自证。

来源：Simon Willison 引述 StrongDM 团队，simonwillison.net/tags/ai-assisted-programming/

---

### 1.4 embedding-shapes：一人三天写两万行 Rust

**案例**：一位开发者使用"一个 agent，一个浏览器"的模式，在 3 天内用 AI 生成了 **20,000 行 Rust 代码**。这是 AI 辅助编程中单兵作战能力的极致展示。

来源：Simon Willison 引述，simonwillison.net/tags/ai-assisted-programming/

---

### 1.5 Mitchell Hashimoto（HashiCorp 联合创始人）的 AI 采用之路

**人物**：Mitchell Hashimoto，HashiCorp 联合创始人

**方法论**：
- **复现自己的工作**：用 AI 复现你本可以自己写的东西，来学习 AI 的能力边界
- **"下班 agent"模式**：让 agent 在下班后继续工作，第二天早上验收结果

来源：Simon Willison 引述，simonwillison.net/tags/ai-assisted-programming/

---

### 1.6 Karel D'Oosterlinck：$10,000 的 Codex 自动化

**案例**：花费 $10,000 使用 OpenAI Codex 进行自动化开发，探索了 AI 编码的成本边界和产出效率。

来源：Simon Willison 引述，simonwillison.net/tags/ai-assisted-programming/

---

### 1.7 Paul Ford（纽约时报文章）：AI 编程的经济价值估算

**人物**：Paul Ford，知名技术作家

**关键数据**：Ford 在纽约时报发表的文章中估算，AI 辅助编程能产生 **$25,000 - $350,000 等值的工作产出**。这个范围反映了不同使用模式下的巨大差异——从简单补全到完整的自主代理。

来源：Simon Willison 引述 Paul Ford NYT 文章，simonwillison.net/tags/ai/

---

### 1.8 Chris Ashworth：AI 编程在艺术领域的应用（QLab）

**案例**：将 AI 编程工具应用于 QLab（专业音视频控制软件）的艺术创作场景，展示了 AI 编程不仅适用于传统软件开发。

来源：Simon Willison 引述，simonwillison.net/tags/ai-assisted-programming/

---

### 1.9 行业级宏观数据

来自 Addy Osmani 汇总的数据（来源：The Factory Model）：

| 指标 | 数据 |
|------|------|
| 新建网站数量 | 同比增长 40% |
| iOS 应用数量 | 同比增长约 50% |
| GitHub 推送量（美国） | 跳涨 35% |
| 约 30% 高级开发者 | 主要交付 AI 生成的代码 |

来源：[The Factory Model](https://addyosmani.com/blog/factory-model/)

---

## 二、"最关键的一步"之争

### 2.1 核心争议

在 AI 编程工作流中，专家们对"哪一步最关键"存在分歧：

| 专家/来源 | 认为最关键的步骤 | 理由 |
|-----------|-----------------|------|
| Addy Osmani | **写好规格说明（Spec）** | "Spec 是你最大的杠杆点" |
| GitHub（分析 2,500+ 配置文件） | **设定边界和规则** | 三层边界系统防止 AI 犯错 |
| Simon Willison | **验证（Verification）** | 生成已解决，验证是未解决的问题 |
| OCaml 维护者 | **代码审查（Review）** | 直接拒绝了 13,000 行 AI PR |
| Dan Shapiro / StrongDM | **测试（Testing）** | 测试是唯一能让 Dark Factory 运转的保障 |
| Steve Yegge | **人的判断力** | "AI Vampire"——警惕 AI 带来的倦怠 |
| Martin Fowler | **领域知识** | LLM 正在蚕食专业技能 |

### 2.2 Addy Osmani 的观点：Spec First（规格先行）

Addy Osmani 在多篇文章中反复强调：**"先写规格说明，再写代码"** 是 AI 编程中最重要的原则。

他的核心论点：
- 在 AI 时代，spec 的 ROI（投资回报率）被极大放大——一份好的 spec 可以让 AI 生成数十次高质量代码
- 传统的 spec 是写给人看的，现在是写给 AI 看的，格式和内容需要调整
- **"诅咒指令"（Curse of Instructions）**：一个 prompt 中塞入过多指令，反而会降低模型遵循度

GitHub 对 2,500+ agent 配置文件的分析，发现好的 spec 应覆盖 6 个核心领域：
1. **命令（Commands）**：如何构建、测试、运行
2. **测试（Testing）**：测试策略和期望
3. **项目结构（Project Structure）**：代码组织方式
4. **代码风格（Code Style）**：命名、格式、模式
5. **Git 工作流（Git Workflow）**：提交、分支策略
6. **边界（Boundaries）**：AI 可以做和不可以做的事

**三层边界系统**：
- **Always Do**（始终做）：使用特定模式、遵循命名约定
- **Ask First**（先问再做）：涉及架构决策、外部依赖
- **Never Do**（绝对不做）：不修改特定文件、不引入新依赖

来源：[How to write a good spec for AI agents](https://addyosmani.com/blog/good-spec/)

### 2.3 规格驱动开发（Spec-Driven Development）四阶段工作流

GitHub 的 Spec Kit 提出了 4 阶段门控工作流：

```
阶段 1: Specify（规格化）
    ↓ 门控审查
阶段 2: Plan（规划）
    ↓ 门控审查
阶段 3: Tasks（任务拆分）
    ↓ 门控审查
阶段 4: Implement（实施）
```

每个阶段结束都有**门控审查**，确保方向正确后才进入下一阶段。

### 2.4 Simon Willison 的观点：验证是瓶颈

Simon Willison 反复强调的核心观点：

> "生成（Generation）已经解决了。验证（Verification）才是未解决的问题。"

他的论点：
- AI 可以在几秒内生成代码，但验证这些代码是否正确、安全、符合需求的时间并没有减少
- 随着生成速度的提升，验证负担反而加重
- **"致命三要素"（Lethal Trifecta）**：速度 + 非确定性 + 成本 = 危险的 AI 使用

### 2.5 专家共识

尽管专家们对"最关键的一步"有不同看法，但存在以下共识：

1. **不能跳过审查**：即使使用 AI，代码审查仍然不可省略（但形式可能改变）
2. **测试是基础**：没有好的测试，AI 编码就是盲飞
3. **规格说明是杠杆**：投入时间写好 spec 的回报远大于直接开始编码
4. **经验至关重要**：资深开发者使用 AI 的效果远好于初级开发者
5. **人在回路中**：完全自主的 AI 编码目前仍不可靠

---

## 三、常见失败模式

### 3.1 OCaml 维护者拒绝 13,000 行 AI PR

**事件**：有人提交了一个 13,000 行的 AI 生成 PR 到 OCaml 项目。

**结果**：维护者直接拒绝。

**教训**：
- 大型 AI 生成的 PR 审查成本极高
- 社区对 AI 生成代码的质量仍存疑
- **PR 规模是信号**：过大的 PR 本身就是红旗

来源：[AI writes code faster. Your job is still to prove it works](https://addyosmani.com/blog/code-review-ai/)

### 3.2 AI 生成代码的安全缺陷

来自 Addy Osmani 汇总的研究数据：

| 安全指标 | AI 代码 vs 人类代码 |
|----------|-------------------|
| 45% 的 AI 代码 | 存在安全缺陷 |
| 逻辑错误率 | 人类的 1.75 倍 |
| XSS 漏洞率 | 高 2.74 倍 |
| PR 规模 | 平均大 18% |
| 每个 PR 的事故率 | 上升 24% |
| 变更失败率 | 上升 30% |

**核心问题**：AI 生成的代码看起来正确，但逻辑缺陷和安全漏洞的比例显著高于人类代码。

来源：[AI writes code faster. Your job is still to prove it works](https://addyosmani.com/blog/code-review-ai/)

### 3.3 Vibe Coding（氛围编程）的危险

**定义**：Andrej Karpathy 创造的术语，指不审查 AI 生成的代码，"感觉对了就直接用"。

**失败模式**：
- 代码"能用"但不可维护
- 隐藏的逻辑错误在边缘情况爆发
- 安全漏洞被忽视
- 技术债快速积累

Addy Osmani 明确区分了两种模式：
- **Vibe Coding**（氛围编程）：不加审查地使用 AI → 危险
- **Agentic Engineering**（代理工程）：有纪律地使用 AI agent → 有效

来源：[Agentic Engineering](https://addyosmani.com/blog/agentic-engineering/)

### 3.4 认知债务（Cognitive Debt）

**概念提出者**：Margaret-Anne Storey

**定义**：不同于传统的技术债务，认知债务是指**开发者对系统的共享心智模型的丧失**。

**发生机制**：
1. 使用 AI 快速生成大量代码
2. 没有充分理解生成的代码
3. 团队逐渐失去对系统整体架构的理解
4. 当需要修改或调试时，没有人真正理解系统如何工作

**为什么比技术债更危险**：
- 技术债可以通过重构解决
- 认知债务需要人重新理解系统，这个过程更慢更难
- 累积的认知债务可能导致系统无法维护

来源：Simon Willison 引述 Margaret-Anne Storey，simonwillison.net/tags/ai-assisted-programming/

### 3.5 Steve Yegge 的 "AI Vampire" 警告

**人物**：Steve Yegge，知名开发者/博主

**核心警告**：AI 工具就像"吸血鬼"——它们让你产出更多，但也让你**更快倦怠**。

**失败模式**：
- 开发者被 AI 的速度裹挟，失去对代码质量的掌控感
- 持续高强度审查 AI 代码导致审查疲劳
- 产出增加了，但满足感下降了

来源：Simon Willison 引述，simonwillison.net/tags/ai/

### 3.6 "诅咒指令"问题

**问题**：在单个 prompt 中塞入过多指令，反而导致 AI 遵循度下降。

**表现**：
- AI 忽略部分指令
- 生成的代码不符合某些规范
- 越复杂的 prompt，AI 越可能"选择性遗忘"

**解决方案**：
- 将大 spec 拆分为多个小文件
- 使用 CLAUDE.md 等配置文件而非单个 prompt
- 使用"扩展目录"（Extended TOC）技术：先给 AI 一个目录概览，再按需加载详细章节

### 3.7 Thoughtworks 的发现：初中级工程师的困境

**发现来源**：Thoughtworks 的技术雷达/团队调研

**核心发现**：
- 初级和中级工程师使用 AI 工具时，**缺乏判断 AI 输出质量的能力**
- 资深工程师能快速识别 AI 生成代码的问题
- 这加剧了行业经验鸿沟——AI 帮助资深者更高效，但可能让初中级者养成坏习惯

---

## 四、实践者工作流模板

### 4.1 Addy Osmani 的 10 步工作流（完整版）

这是目前最完整、被引用最多的 AI 编程工作流：

**步骤 1：从清晰的计划开始**
- 在让 AI 写代码之前，先明确你要做什么
- 写一份简短的 spec 或计划文档
- "Spec first, code second"

**步骤 2：将工作拆分为小块**
- 每个任务应该足够小，可以在一次对话中完成
- 任务粒度：一个函数、一个组件、一个测试
- 小任务让 AI 更容易理解上下文

**步骤 3：提供充分的上下文**
- 不要只给一个简短的 prompt
- 提供相关代码、文档、约束条件
- "Context packing"（上下文打包）是高产出开发者的核心技能

**步骤 4：选择合适的模型**
- 不同任务适合不同模型
- 简单补全：用轻量模型
- 复杂架构：用最强模型
- 不要"一刀切"

**步骤 5：在整个生命周期中利用 AI**
- 不仅用于编码，还用于：
  - 规划和设计
  - 测试生成
  - 调试
  - 文档编写
  - 代码审查

**步骤 6：保持人在回路中**
- 不要完全信任 AI 输出
- 验证关键逻辑
- 理解 AI 生成的每一行代码

**步骤 7：频繁提交**
- 小步提交，降低回滚成本
- 每个提交对应一个小的、可验证的变更
- 便于追踪 AI 生成代码的问题

**步骤 8：自定义 AI 行为**
- 使用 CLAUDE.md 等配置文件
- 定义项目规范、编码风格、边界
- 让 AI 在你的约束条件下工作

**步骤 9：积极拥抱测试**
- 用 AI 生成测试
- 在 AI 生成代码之前先生成测试（TDD）
- Red/Green TDD 与 AI 结合是最高杠杆的指令

**步骤 10：持续学习**
- AI 工具快速进化
- 保持学习新的 prompt 技巧
- 与社区分享经验

来源：[My LLM coding workflow going into 2026](https://addyosmani.com/blog/ai-coding-workflow/)

---

### 4.2 规格驱动开发工作流（GitHub Spec Kit）

```
┌─────────────┐
│   Specify    │  明确需求、约束、边界
│  (规格化)    │
└──────┬──────┘
       │ 门控审查 ✓
┌──────▼──────┐
│    Plan     │  制定技术方案
│   (规划)    │
└──────┬──────┘
       │ 门控审查 ✓
┌──────▼──────┐
│   Tasks     │  拆分为可执行的小任务
│  (任务拆分)  │
└──────┬──────┘
       │ 门控审查 ✓
┌──────▼──────┐
│  Implement  │  AI 辅助编码
│   (实施)    │
└─────────────┘
```

**关键原则**：每个阶段结束都有门控审查，确保方向正确。

来源：[How to write a good spec for AI agents](https://addyosmani.com/blog/good-spec/)

---

### 4.3 PR Contract 框架（AI 代码审查）

用于 AI 生成 PR 的标准化审查框架：

| 要素 | 内容 |
|------|------|
| What & Why | 这个 PR 做了什么，为什么做 |
| Proof it works | 证明它工作的证据（测试结果、截图等） |
| Risk + AI Role | 风险评估 + AI 的参与程度 |
| Review Focus | 请审查者重点关注什么 |

**使用场景**：当代码主要由 AI 生成时，用这个框架帮助审查者快速理解变更。

来源：[AI writes code faster. Your job is still to prove it works](https://addyosmani.com/blog/code-review-ai/)

---

### 4.4 Dan Shapiro 五级模型

描述团队/个人 AI 编程成熟度的框架：

| 级别 | 名称 | 描述 | 人类角色 |
|------|------|------|----------|
| 1 | Spicy Autocomplete | 增强版自动补全 | 主力编写，AI 辅助 |
| 2 | Coding Intern | AI 像实习生一样写代码 | 指导 + 审查 |
| 3 | Junior Dev | AI 处理常规任务 | 分配任务 + 审查 |
| 4 | Developer / Full-time Reviewer | AI 编写大部分代码 | 全职审查 |
| 5 | Dark Factory | 没有人审查代码 | 设计系统，确保测试覆盖 |

**实践建议**：大多数团队目前处于 Level 2-3，少数先进团队达到 Level 4。

---

### 4.5 Mitchell Hashimoto 的方法论

1. **复现自己的工作**：用 AI 复现你本可以自己写的东西，来学习 AI 的能力边界
2. **"下班 agent"模式**：让 agent 在下班后继续工作，第二天早上验收结果

**关键洞察**：先在安全环境中学习 AI 的能力边界，再逐步扩大使用范围。

---

### 4.6 Agentic Engineering vs Vibe Coding 对比

| 维度 | Vibe Coding | Agentic Engineering |
|------|-------------|-------------------|
| 核心态度 | 信任 AI 输出 | 验证 AI 输出 |
| 规格说明 | 很少或没有 | 详细、结构化 |
| 测试策略 | 事后补测试 | 测试先行（TDD） |
| 代码审查 | 跳过或敷衍 | 严格、结构化 |
| 提交频率 | 大批量 | 小步频繁 |
| 适用人群 | 所有级别 | 需要经验判断 |
| 风险等级 | 高 | 中低 |

来源：[Agentic Engineering](https://addyosmani.com/blog/agentic-engineering/)

---

## 五、关键引用与金句

### 来自 Addy Osmani

> "You are no longer just writing code. You are building the factory that builds your software."
> （你不再只是在写代码。你在建造一个制造你的软件的工厂。）

> "Generation is solved. Verification is the unsolved problem."
> （生成已经解决了。验证是未解决的问题。）

> "Spec first, code second. In the age of AI, your spec is your biggest lever."
> （先规格，后代码。在 AI 时代，你的规格说明是最大的杠杆。）

> "~90% of Claude Code is written by Claude Code itself."
> （约 90% 的 Claude Code 代码是由 Claude Code 自己编写的。）

### 来自 Simon Willison

> "The lethal trifecta: speed + non-determinism + cost = dangerous AI agent usage."
> （致命三要素：速度 + 非确定性 + 成本 = 危险的 AI agent 使用。）

### 来自 Peter Steinberger

> "I don't read much code anymore."
> （我不再读太多代码了。）

### 来自 David Crawshaw

关于 AI 编程是否减少了编程的乐趣——这是一个在社区中广泛讨论的话题。

### 来自 Andrej Karpathy

创造了 "Vibe Coding" 一词，最初带有随意的含义，后来被社区用来描述一种不负责任的 AI 编程方式。

### 来自 Martin Fowler

> "LLMs are eating specialty skills."
> （大语言模型正在蚕食专业技能。）

---

## 六、数据汇总

### AI 编码效率提升

| 开发者类型 | 效率提升 | 来源 |
|-----------|---------|------|
| 资深工程师 | 2x - 5x+ | Addy Osmani |
| 初级工程师 | 不确定/可能下降 | Thoughtworks |
| 整体行业 PR 产出 | +18%（但事故率也上升） | Addy Osmani 汇总 |

### AI 代码质量问题

| 问题 | 数据 |
|------|------|
| AI 代码安全缺陷率 | 45% |
| AI 逻辑错误率（vs 人类） | 1.75x |
| AI XSS 漏洞率（vs 人类） | 2.74x |
| 变更失败率上升 | 30% |
| 每 PR 事故率上升 | 24% |

### 行业增长数据

| 指标 | 增长 |
|------|------|
| 新建网站 | +40% YoY |
| iOS 应用 | +50% YoY |
| GitHub 推送（美国） | +35% |
| Claude Code 收入 | $2.5B |

---

## 七、核心结论（文章框架建议）

### 7.1 最关键的一步是什么？

综合所有研究，**最关键的步骤是"规格说明"（Spec）**，理由如下：

1. **杠杆效应最大**：一份好 spec 可以让 AI 反复生成高质量代码，投入产出比最高
2. **所有失败模式都指向 spec 缺失**：Vibe Coding、安全缺陷、认知债务——根源都是"没想清楚就让 AI 开始写"
3. **专家共识度最高**：Addy Osmani、GitHub、Simon Willison 都强调了 spec/specification 的重要性
4. **但验证是紧随其后的第二关键步骤**：没有验证，再好的 spec 也无法保证质量

### 7.2 成功的 AI 编程工作流公式

```
成功的 AI 编程 = 好的 Spec + 小任务拆分 + TDD + 严格审查 + 频繁提交
```

### 7.3 文章建议结构

1. **开篇**：用一个震撼案例开头（如 90% 代码由 AI 自己编写、一人三天两万行 Rust）
2. **现状**：行业数据（网站增长 40%、GitHub 推送增长 35%）
3. **争议**：最关键的一步是什么？展示不同专家的观点
4. **答案**：Spec First——为什么规格说明是最关键的
5. **反面教材**：失败案例（OCaml PR 拒绝、安全缺陷数据、认知债务）
6. **实操指南**：Addy Osmani 的 10 步工作流
7. **分级模型**：Dan Shapiro 五级模型，帮读者定位自己
8. **结尾**：Vibe Coding vs Agentic Engineering——选择权在你

---

## 八、参考来源

1. [Addy Osmani - My LLM coding workflow going into 2026](https://addyosmani.com/blog/ai-coding-workflow/)
2. [Addy Osmani - The Factory Model](https://addyosmani.com/blog/factory-model/)
3. [Addy Osmani - Agentic Engineering](https://addyosmani.com/blog/agentic-engineering/)
4. [Addy Osmani - How to write a good spec for AI agents](https://addyosmani.com/blog/good-spec/)
5. [Addy Osmani - AI writes code faster](https://addyosmani.com/blog/code-review-ai/)
6. [Simon Willison - AI tag](https://simonwillison.net/tags/ai/)
7. [Simon Willison - AI-assisted programming tag](https://simonwillison.net/tags/ai-assisted-programming/)
