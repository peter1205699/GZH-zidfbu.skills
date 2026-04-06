# Claude Code Workflow 研究笔记

> 研究目标：了解开发者如何使用 Claude Code CLI 从需求到提交 PR 的完整工作流
> 研究时间：2026-04-02
> 资料来源：Anthropic 官方文档、GitHub 仓库

---

## 一、关键事实 (Key Facts)

### 基本信息
- **定位**：Claude Code 是一个驻留在终端中的 AI 编程代理工具，理解你的代码库，通过自然语言命令帮你更快编码
- **官方描述**："an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows"
- **核心理念**：遵循 Unix 哲学——可组合、可脚本化
- **GitHub 仓库**：https://github.com/anthropics/claude-code

### 安装方式 (2026 年最新)
- **macOS/Linux (推荐)**：`curl -fsSL https://claude.ai/install.sh | bash`
- **Homebrew (macOS/Linux)**：`brew install --cask claude-code`
- **Windows (推荐)**：`irm https://claude.ai/install.ps1 | iex`
- **WinGet (Windows)**：`winget install Anthropic.ClaudeCode`
- **NPM (已弃用)**：`npm install -g @anthropic-ai/claude-code`（官方标注为 deprecated）

### 运行模式
| 模式 | 命令 | 说明 |
|------|------|------|
| 交互模式 | `claude` | 启动交互式 REPL 会话 |
| 单次模式 | `claude -p "query"` | 执行单条提示并退出 |
| 恢复模式 | `claude --continue` / `claude --resume` | 继续之前的对话 |
| 管道模式 | `tail -f log \| claude -p "..."` | Unix 管道集成 |

### 输出格式 (CI/CD 集成)
- `--output-format text`：纯文本输出，适合简单集成
- `--output-format json`：完整对话日志，适合程序解析
- `--output-format stream-json`：实时流式输出，适合实时处理

---

## 二、核心工作流功能

### 2.1 从需求到 PR 的完整流程

Claude Code 支持以下开发工作流教程（官方教程目录）：

1. **理解新代码库** — 快速获取代码库概览，查找相关代码
2. **修复 Bug** — 诊断错误信息，定位问题源头
3. **重构代码** — 将遗留代码现代化，保持向后兼容
4. **测试协作** — 添加测试覆盖，覆盖边界情况
5. **创建 PR** — 生成结构完整的 Pull Request
6. **文档处理** — 生成代码文档（JSDoc、docstrings 等）
7. **图像分析** — 分析截图、UI 设计稿、架构图

**创建 PR 的官方建议**：
- 直接让 Claude 帮你创建 PR："Ask Claude directly to make a PR for you"
- 在提交前审查 Claude 生成的 PR
- 让 Claude 指出潜在风险和注意事项

### 2.2 Git Worktree 并行开发

**适用场景**：需要同时处理多个任务，且 Claude Code 实例之间需要完全代码隔离。

**关键特性**：
- 每个 worktree 拥有独立的文件状态，非常适合并行 Claude Code 会话
- 一个 worktree 中的修改不会影响其他 worktree，防止 Claude 实例互相干扰
- 所有 worktree 共享相同的 Git 历史和远程连接
- 可以让 Claude 在一个 worktree 中处理长期任务，同时在另一个中继续开发
- 使用描述性目录名来标识每个任务对应的 worktree
- **重要提醒**：每个新 worktree 需要初始化开发环境（`npm install`、虚拟环境等）

### 2.3 会话管理

- `--continue` (`-c`)：自动继续最近的对话
- `--resume` (`-r`)：显示对话选择器，选择特定历史对话
- 对话历史自动保存在本地，包含完整消息历史
- 恢复时保留工具使用状态和结果
- 恢复的对话使用与原始对话相同的模型和配置

### 2.4 扩展思考 (Extended Thinking)

用于处理复杂任务：
- 规划复杂架构变更
- 调试复杂问题
- 为新功能创建实施计划
- 理解复杂代码库
- 评估不同方案的权衡

**触发方式**：
- "think" 触发基本扩展思考
- "think more"、"think a lot"、"think harder"、"think longer" 触发更深层次的思考

---

## 三、自动化与扩展功能

### 3.1 斜杠命令 (Slash Commands)

| 命令 | 功能 |
|------|------|
| `/bug` | 报告问题（直接在 Claude Code 内） |
| `/clear` | 清除对话历史 |
| `/compact [instructions]` | 压缩对话（可选指令） |
| `/config` | 打开配置 |
| `/cost` | 显示 token 使用统计 |
| `/doctor` | 检查 Claude Code 健康状况 |
| `/help` | 显示帮助信息 |
| `/init` | 初始化项目的 CLAUDE.md |
| `/login` | 登录 Anthropic 账户 |
| `/logout` | 登出 |
| `/memory` | 编辑 CLAUDE.md 内存文件 |
| `/pr_comments` | 查看 PR 评论 |
| `/review` | 代码审查 |
| `/status` | 显示账户状态 |
| `/terminal-setup` | 配置终端集成 |
| `/vim` | 切换 Vim 编辑模式 |

**自定义斜杠命令**：
- 项目级命令：放在 `.claude/commands/` 目录下，前缀为 `/project:`
  - 如 `.claude/commands/optimize.md` 变为 `/project:optimize`
  - 支持子目录：`.claude/commands/frontend/component.md` 变为 `/project:frontend:component`
- 个人命令：前缀为 `/user:`，跨所有项目可用
- 支持 `$ARGUMENTS` 占位符，传递用户输入

### 3.2 Hooks 系统

Hooks 允许在特定事件发生时执行自定义 Shell 命令，实现工作流自动化。

**事件类型**：
| 事件 | 触发时机 |
|------|----------|
| PreToolUse | 工具调用前 |
| PostToolUse | 工具调用后 |
| Notification | 发送通知时 |
| UserPromptSubmit | 用户提交提示时 |
| Stop | Claude 停止响应时 |
| SubagentStop | 子代理停止时 |
| PreCompact | 压缩对话前 |
| SessionStart | 会话开始时 |
| SessionEnd | 会话结束时 |

**Matcher 匹配器**：支持正则表达式，精确控制哪些工具调用触发 Hook

**退出码行为**：
- 退出码 0：成功，正常继续
- 退出码 2：阻止操作（用于 PreToolUse）
- JSON 输出：支持高级控制（如动态修改决策）

**安全最佳实践**：
- 验证输入参数
- 引用变量以防止注入
- 阻止路径遍历攻击
- 使用绝对路径

### 3.3 Skills 技能系统

Skills 是 Claude 自主决定何时使用的自动化能力单元。

**SKILL.md 结构**（YAML 前置元数据）：
```yaml
---
name: skill-name
description: 描述技能的功能和使用时机
allowed-tools: [tool1, tool2]  # 可选，限制工具访问
---
```

**设计原则**：
- "One Skill should address one capability" — 一个技能对应一个能力
- Description 必须包含**做什么**和**何时使用**
- 技能是模型调用的（model-invoked）— Claude 自主决定何时使用

**技能存储位置**：
- 个人技能：`~/.claude/skills/`
- 项目技能：`.claude/skills/`
- 插件技能：通过插件系统安装

### 3.4 MCP (Model Context Protocol)

MCP 是开放协议，让 LLM 访问外部工具和数据源。

**配置范围**：
- `local`（默认）：仅你在当前项目可用
- `project`：通过 `.mcp.json` 与团队共享（应提交到版本控制）
- `user`：跨所有项目可用

**关键特性**：
- 本地范围 > 项目范围 > 用户范围（同名服务器优先级）
- 项目范围的 MCP 服务器需经用户审批
- `/mcp` 命令随时查看服务器状态
- Claude Code 本身也可以作为 MCP 服务器暴露给其他应用

---

## 四、内存与上下文管理

### 4.1 CLAUDE.md 内存层级

| 层级 | 文件位置 | 优先级 | 说明 |
|------|----------|--------|------|
| 企业策略 | — | 最高 | 组织级策略 |
| 项目 | `./CLAUDE.md` | 高 | 团队共享的项目指令 |
| 用户 | `~/.claude/CLAUDE.md` | 中 | 个人跨项目偏好 |
| 本地 | `./CLAUDE.local.md` | 低 | 已弃用 |

### 4.2 导入机制
- 使用 `@path/to/import` 语法导入其他文件
- 支持递归导入，最多 5 跳

### 4.3 快速内存操作
- `/memory` 命令：编辑 CLAUDE.md
- `#` 快捷方式：在对话中快速添加内存条目

### 4.4 CLAUDE.md 最佳实践
- 包含常用命令（build、test、lint）避免重复搜索
- 记录代码风格偏好和命名约定
- 添加项目特有的架构模式
- 区分团队共享指令和个人偏好

---

## 五、知名引言与设计哲学

### Unix 哲学
> "Claude Code is composable and scriptable. `tail -f app.log | claude -p 'Slack me if you see any anomalies'` works."
> — Anthropic 官方文档

### 核心价值主张
- "build features from descriptions" — 从描述构建功能
- "debug and fix issues" — 调试和修复问题
- "navigate codebases" — 导航代码库
- "automate tedious tasks" — 自动化繁琐任务

### 官方插件生态
> "This repository includes several Claude Code plugins that extend functionality with custom commands and agents."

### 社区
- Discord 社区：Claude Developers Discord
- GitHub Issues：https://github.com/anthropics/claude-code/issues

---

## 六、最佳实践总结

### 官方推荐的工作流最佳实践

1. **理解代码库**
   - 先问宽泛问题，再逐步聚焦到具体领域
   - 询问项目使用的编码约定和模式
   - 要求提供项目特定术语表

2. **修复 Bug**
   - 告诉 Claude 复现问题的命令和获取堆栈跟踪的方法
   - 说明复现步骤
   - 注明错误是间歇性还是持续性的

3. **重构代码**
   - 要求 Claude 解释现代方法的好处
   - 需要时要求保持向后兼容
   - 以小的、可测试的增量进行重构

4. **添加测试**
   - 要求覆盖边界情况和错误条件
   - 同时请求单元测试和集成测试
   - 让 Claude 解释测试策略

5. **创建 PR**
   - 直接要求 Claude 创建 PR
   - 提交前审查 Claude 的生成内容
   - 让 Claude 指出潜在风险

6. **使用扩展思考**
   - 用于复杂架构决策
   - 用于难以解决的 Bug
   - 用于规划多步骤实施
   - 通过 "think harder" 等短语触发更深思考

7. **配置 CLAUDE.md**
   - 包含常用命令（build、test、lint）
   - 文档化代码风格偏好
   - 添加项目特定的架构模式

8. **并行开发**
   - 使用 Git Worktree 实现多任务并行
   - 每个 worktree 独立初始化开发环境
   - 使用描述性目录名标识任务

9. **MCP 集成**
   - 项目级 MCP 配置提交到版本控制以团队共享
   - 使用最小权限原则配置数据库连接
   - 利用 `/mcp` 命令监控服务器状态

10. **自定义命令**
    - 为团队创建项目级斜杠命令
    - 使用 `$ARGUMENTS` 实现灵活参数化
    - 个人命令跨项目复用

---

## 七、关键 CLI 参数速查

| 参数 | 说明 |
|------|------|
| `-p` / `--print` | 非交互模式，执行后退出 |
| `-c` / `--continue` | 继续最近的对话 |
| `-r` / `--resume` | 恢复指定对话 |
| `--output-format` | 输出格式：text / json / stream-json |
| `--verbose` | 详细输出模式 |
| `--max-turns` | 限制对话轮次 |
| `--permission-prompt-tool` | 权限提示工具 |
| `--dangerously-skip-permissions` | 跳过权限确认（危险） |

---

## 八、资料来源

1. Anthropic 官方文档 - Overview: https://docs.anthropic.com/en/docs/claude-code/overview
2. Anthropic 官方文档 - CLI Usage: https://docs.anthropic.com/en/docs/claude-code/cli-usage
3. Anthropic 官方文档 - Hooks: https://docs.anthropic.com/en/docs/claude-code/hooks
4. Anthropic 官方文档 - Skills: https://docs.anthropic.com/en/docs/claude-code/skills
5. Anthropic 官方文档 - Memory: https://docs.anthropic.com/en/docs/claude-code/memory
6. Anthropic 官方文档 - Tutorials: https://docs.anthropic.com/en/docs/claude-code/tutorials
7. GitHub 仓库 README: https://github.com/anthropics/claude-code/blob/main/README.md

---

## 九、未获取的信息（研究限制）

由于访问权限限制，以下页面未能成功获取：
- Worktree 详细文档页（403 Forbidden）
- Plan Mode 文档（URL 未确认）
- Best Practices 独立页面（重定向到首页）
- Changelog 详细内容（重定向到首页）
- 社区博客文章和用户体验（WebSearch 被拒绝）

建议后续通过以下方式补充：
- 在浏览器中直接访问上述受限页面
- 搜索 Twitter/X、Reddit、Hacker News 上的开发者体验分享
- 查看 YouTube 上的 Claude Code 教程视频
- 关注 Anthropic 官方博客的更新
