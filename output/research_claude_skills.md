# Claude Code Skills System -- Technical Research

> Research compiled: 2026-04-03
> Sources: Official Anthropic documentation, local environment inspection, installed plugin analysis

---

## Table of Contents

1. [SKILL.md Format and Fields](#1-skillmd-format-and-fields)
2. [Skill Discovery and Loading](#2-skill-discovery-and-loading)
3. [Model-Invoked vs User-Invoked Skills](#3-model-invoked-vs-user-invoked-skills)
4. [Relationships to CLAUDE.md, Hooks, and MCP](#4-relationships-to-claudemd-hooks-and-mcp)
5. [Best Practices](#5-best-practices)
6. [Examples](#6-examples)
7. [Plugin System Integration](#7-plugin-system-integration)
8. [Appendix: Related Systems](#appendix-related-systems)

---

## 1. SKILL.md Format and Fields

### Basic Structure

Every Skill is defined by a `SKILL.md` file using YAML frontmatter + Markdown body:

```markdown
---
name: your-skill-name
description: Brief description of what this Skill does and when to use it
---

# Your Skill Name

## Instructions
Provide clear, step-by-step guidance for Claude.

## Examples
Show concrete examples of using this Skill.
```

### Frontmatter Fields

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Identifier for the skill. Used in logs, debugging, and references. |
| `description` | Yes | Brief description of what the Skill does and **when to use it**. This is critical because Claude reads the description to decide whether to activate the skill. |
| `allowed-tools` | No | Comma-separated list of tools Claude is restricted to when this Skill is active. If omitted, all tools are available. |

### allowed-tools Field

Restricts which tools Claude can use while the Skill is active. This is a security/scoping mechanism:

```markdown
---
name: safe-file-reader
description: Read files without making changes. Use when you need read-only file access.
allowed-tools: Read, Grep, Glob
---
```

When `allowed-tools` is set, Claude can ONLY use the listed tools during skill execution. This prevents a skill from accidentally modifying files, running dangerous commands, etc.

### Markdown Body

The body of SKILL.md contains the actual instructions Claude follows when the skill is activated. It supports standard Markdown formatting:

- **Headers** for organization
- **Code blocks** for examples and templates
- **Lists** for step-by-step procedures
- **Tables** for structured data
- **Bold/italic** for emphasis

### Multi-File Skills

Skills can include supporting files that are loaded on demand (progressive disclosure):

```
my-skill/
├── SKILL.md           (required - entry point)
├── reference.md       (optional - detailed reference docs)
├── examples.md        (optional - usage examples)
├── scripts/
│   └── helper.py      (optional - utility scripts)
└── templates/
    └── template.txt   (optional - file templates)
```

Supporting files are NOT loaded into context until Claude specifically needs them. This keeps the initial context window small while providing access to richer documentation when needed.

---

## 2. Skill Discovery and Loading

### Discovery Sources

Claude Code discovers Skills from three sources:

#### Personal Skills (`~/.claude/skills/`)

Available in ALL projects for the current user. Stored in the user's home directory:

```
~/.claude/skills/
├── my-personal-skill/
│   └── SKILL.md
└── another-skill/
    └── SKILL.md
```

#### Project Skills (`.claude/skills/`)

Available only within a specific project. Stored in the project root:

```
your-project/
├── .claude/
│   └── skills/
│       ├── project-skill/
│       │   └── SKILL.md
│       └── another-project-skill/
│           └── SKILL.md
├── src/
└── ...
```

#### Plugin Skills

Bundled within installed plugins. Auto-available when the plugin is installed:

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json
├── skills/
│   └── plugin-skill/
│       └── SKILL.md
└── ...
```

### Discovery Process

1. At session start, Claude scans all three skill directories.
2. For each discovered SKILL.md, Claude reads the frontmatter (name + description).
3. The full SKILL.md content is NOT loaded initially -- only metadata.
4. When Claude determines a skill is relevant to the current task, it invokes the skill.
5. Upon invocation, the full SKILL.md content is loaded into context.
6. Supporting files (scripts, templates, reference docs) are loaded only when the skill instructions reference them (progressive disclosure).

### Loading Behavior

Skills are loaded **on demand**, not eagerly. This means:

- Starting a session does not load all skill content into context
- Skills are activated only when Claude judges them relevant
- The `description` field is critical -- it must accurately describe WHEN to use the skill
- Poor descriptions lead to skills never being activated, or being activated inappropriately

### Debugging Discovery

You can check which skills Claude has discovered by looking at the session start logs or by asking Claude directly. If a skill is not being activated:

1. Check that the SKILL.md file is in the correct directory
2. Verify the YAML frontmatter is valid
3. Ensure the `description` field clearly states when the skill should be used
4. Check for conflicting skill names across sources

---

## 3. Model-Invoked vs User-Invoked Skills

### Skills: Model-Invoked

Skills are **autonomously activated by Claude** based on context analysis. The key characteristics:

- **No explicit command needed**: Claude reads the skill descriptions and decides when to activate
- **Context-driven**: The current conversation, task, and codebase context trigger skill selection
- **Description is the trigger**: The `description` field in frontmatter determines when Claude considers the skill relevant
- **Automatic loading**: When Claude decides a skill applies, it invokes the Skill tool and loads the full content

Example flow:
1. User asks: "Add a REST API endpoint for user authentication"
2. Claude scans available skill descriptions
3. If a "tdd" skill has description "Use for all code implementation tasks", Claude activates it
4. The skill's instructions guide Claude's approach (e.g., write tests first, then implement)

### Slash Commands: User-Invoked

In contrast, slash commands require explicit user invocation:

- **Explicit activation**: User types `/command-name` in the CLI
- **No context guessing**: Claude does not decide whether to use a slash command
- **Defined in `commands/` directories**: Separate from skills

Slash command format (`.md` file in `commands/` directory):

```markdown
---
description: Deploy the application to production
allowed-tools: Bash(git push*), Bash(npm run deploy*)
argument-hint: "<environment>"
model: claude-sonnet-4-20250514
---

# Deploy Command

Deploy the application to the specified environment...
```

Slash command frontmatter fields:

| Field | Description |
|-------|-------------|
| `description` | What the command does (shown in `/` menu) |
| `allowed-tools` | Tool restrictions during execution |
| `argument-hint` | Placeholder shown for arguments |
| `model` | Specific model to use for this command |

### Key Differences

| Aspect | Skills | Slash Commands |
|--------|--------|---------------|
| Activation | Automatic (model decides) | Manual (user types `/command`) |
| Location | `skills/` directory | `commands/` directory |
| Discovery | Description-based | Listed in `/` menu |
| Context cost | Low (metadata only until activated) | Visible in menu |
| Use case | Recurring patterns/workflows | Specific user-triggered actions |
| Argument hint | N/A | Supported via `argument-hint` |

---

## 4. Relationships to CLAUDE.md, Hooks, and MCP

### Skills and CLAUDE.md

**CLAUDE.md** is the memory/instruction system. It provides persistent context and instructions:

**Four tiers of CLAUDE.md (in priority order)**:
1. Enterprise policy (managed by org admins)
2. Project `./CLAUDE.md` (checked into repo, shared with team)
3. User `~/.claude/CLAUDE.md` (personal preferences)
4. Local `./CLAUDE.local.md` (deprecated, use project CLAUDE.md)

**Relationship to Skills**:
- CLAUDE.md provides **global instructions** that apply to all interactions
- Skills provide **specific, context-activated instructions** for particular workflows
- Skills can reference CLAUDE.md conventions (e.g., "Follow the coding style defined in CLAUDE.md")
- CLAUDE.md can instruct Claude to prefer certain skills: "Always use the tdd skill for code changes"
- Skills can be thought of as "specialized extensions" of CLAUDE.md instructions

**Imports**: CLAUDE.md supports importing other files with `@path/to/import` syntax, allowing skills to be referenced or documentation to be shared.

### Skills and Hooks

**Hooks** are event-driven automation triggers defined in `settings.json`:

**Hook events**:
- `PreToolUse` -- Before a tool is called
- `PostToolUse` -- After a tool completes
- `UserPromptSubmit` -- When user submits a message
- `Stop` -- When Claude finishes responding
- `SessionStart` -- When a session begins
- `Notification` -- When a notification is sent

**Relationship to Skills**:
- Hooks provide **infrastructure-level automation** (e.g., linting after file edits, logging)
- Skills provide **instructional guidance** for Claude's behavior
- A Skill can instruct Claude to use tools that trigger hooks
- Hooks can enforce constraints that Skills rely on (e.g., a hook ensures tests run after file changes)
- They are complementary: Skills tell Claude WHAT to do, hooks enforce HOW things happen

**Example integration**:
- Skill: "When implementing API endpoints, always validate input schemas"
- Hook (PostToolUse on Write/Edit): Automatically runs a schema validator on modified files

### Skills and MCP

**MCP (Model Context Protocol)** connects Claude to external tools and services:

**Configuration scopes**:
1. Local `.mcp.json` (project-level, not committed)
2. Project `.mcp.json` (committed, shared with team)
3. User `~/.claude/.mcp.json` (personal tools)
4. Plugin `.mcp.json` (bundled with plugin)

**Relationship to Skills**:
- MCP provides **tools** (external capabilities)
- Skills provide **workflows** (how to use tools effectively)
- A Skill can instruct Claude on how to use specific MCP tools
- Skills can reference MCP tools by name and provide usage patterns
- `allowed-tools` in a Skill can include or exclude MCP tools

**Example integration**:
- MCP: GitHub MCP server provides PR/issue tools
- Skill: "When reviewing PRs, always check for test coverage using the GitHub MCP tools"

### Skills and Subagents

**Subagents** are specialized Claude instances dispatched for specific tasks. They can auto-load Skills via the `skills` field in their frontmatter:

```markdown
---
name: code-reviewer
model: claude-sonnet-4-20250514
tools:
  - Read
  - Grep
  - Glob
skills:
  - security-review
  - performance-analysis
---

# Code Reviewer Agent

Review code for security and performance issues...
```

This means subagents can have their own skill sets, independent of the main conversation's skills.

### Ecosystem Diagram

```
CLAUDE.md (Memory/Instructions)
  |
  ├── Provides global context and preferences
  |
  ├── Skills (Context-Activated Workflows)
  |     ├── Activated by Claude based on description matching
  |     ├── Can reference CLAUDE.md conventions
  |     ├── Can use MCP tools
  |     └── Can trigger Hooks through tool usage
  |
  ├── Hooks (Event-Driven Automation)
  |     ├── PreToolUse / PostToolUse
  |     ├── UserPromptSubmit / Stop
  |     ├── SessionStart / Notification
  |     └── Enforces constraints Skills rely on
  |
  ├── MCP (External Tool Connections)
  |     ├── Provides tools Skills can reference
  |     ├── Can be bundled in plugins alongside Skills
  |     └── Extends Claude's capabilities
  |
  ├── Slash Commands (User-Invoked Actions)
  |     ├── Explicit `/command` activation
  |     └── For specific user-triggered workflows
  |
  └── Subagents (Specialized Instances)
        ├── Can auto-load specific Skills
        ├── Have their own tool restrictions
        └── Run independently for specific tasks
```

---

## 5. Best Practices

### Skill Design

1. **Write precise descriptions**: The description determines when Claude activates the skill. Be specific about triggers:
   - Good: "Use when implementing React components that need responsive layout"
   - Bad: "Use for frontend work"

2. **Keep SKILL.md focused**: One skill should address one workflow or pattern. Avoid creating "super-skills" that try to cover everything.

3. **Use progressive disclosure**: Put detailed reference material in supporting files, not in SKILL.md itself. The main file should contain the core instructions; examples, references, and scripts go in separate files.

4. **Restrict tools when appropriate**: Use `allowed-tools` to prevent a skill from making unintended changes:
   - Read-only analysis skills: `allowed-tools: Read, Grep, Glob`
   - Code generation skills: `allowed-tools: Read, Write, Edit, Grep, Glob`
   - Safe exploration skills: `allowed-tools: Read, Grep, Glob, Bash(ls*)`

### Skill Organization

5. **Use multi-file structure for complex skills**: When a skill needs more than ~200 lines of instructions, split into supporting files.

6. **Name skills descriptively**: The name appears in logs and debugging output. Use kebab-case: `react-component-builder`, not `rcb` or `ReactComponentBuilder`.

7. **Organize by workflow, not by technology**: A skill like "add-api-endpoint" (covering routes, controllers, tests, docs) is more useful than separate skills for each file type.

### Testing and Debugging

8. **Test skill activation**: Ask Claude "What skills do you have available?" to verify discovery. If a skill is not listed, check the file location and frontmatter.

9. **Test skill behavior**: After skill activation, verify Claude follows the instructions by checking its actions against the skill content.

10. **Iterate on descriptions**: If a skill is activating too often or not enough, adjust the description field.

### Security

11. **Principle of least privilege**: Use `allowed-tools` to restrict what skills can do. A skill that only needs to read files should not have access to `Write` or `Bash`.

12. **Review plugin skills**: Before installing a plugin, review its skills' `allowed-tools` to understand what capabilities they require.

---

## 6. Examples

### Example 1: TDD Skill

```markdown
---
name: tdd
description: Use for all code implementation tasks. Ensures test-driven development workflow.
allowed-tools: Read, Write, Edit, Bash, Grep, Glob
---

# Test-Driven Development

## Instructions

1. **Write tests first**: Before implementing any feature, write failing tests that define expected behavior.
2. **Run tests**: Verify tests fail for the right reasons.
3. **Implement minimum code**: Write the simplest code that makes tests pass.
4. **Refactor**: Clean up while keeping tests green.
5. **Repeat**: Continue the cycle for each new requirement.

## Rules

- Never write implementation before tests
- Never skip running tests after changes
- Always commit green tests separately from implementation
```

### Example 2: Read-Only Code Review Skill

```markdown
---
name: code-review
description: Use when reviewing pull requests or existing code. Provides structured review workflow.
allowed-tools: Read, Grep, Glob
---

# Code Review

## Review Checklist

For each file changed:
1. **Correctness**: Does the code do what it claims?
2. **Security**: Any injection risks, exposed secrets, or auth issues?
3. **Performance**: N+1 queries, unnecessary loops, memory leaks?
4. **Style**: Follows project conventions in CLAUDE.md?
5. **Tests**: Are changes adequately tested?

## Output Format

Provide review as:
- **Critical issues** (must fix before merge)
- **Suggestions** (should consider)
- **Questions** (need clarification)
```

### Example 3: Multi-File Skill Structure

```
api-endpoint-skill/
├── SKILL.md
│   ---
│   name: api-endpoint
│   description: Use when adding new REST API endpoints. Covers routing, controllers, validation, and tests.
│   ---
│   # API Endpoint Generator
│   ## Instructions
│   Follow the project's API patterns defined in @reference.md
│   Use @templates/controller.ts for the controller structure.
├── reference.md
│   # API Reference
│   ## Project API Patterns
│   - REST endpoints follow `/api/v{version}/{resource}` pattern
│   - All endpoints require authentication middleware
│   - Response format: { data: ..., meta: ..., errors: ... }
├── templates/
│   ├── controller.ts
│   ├── route.ts
│   ├── test.ts
│   └── validation.ts
└── scripts/
    └── generate-endpoint.py
```

### Example 4: Observed Skills in Current Environment

The following skills are installed in the current Claude Code environment (from system reminder context):

**From `superpowers` plugin**:
- `superpowers:using-superpowers` -- Skill discovery and usage instructions
- `superpowers:brainstorming` -- Brainstorming/planning skill
- `superpowers:tdd` -- Test-driven development workflow
- `superpowers:frontend-design` -- Frontend design implementation
- `superpowers:mcp-builder` -- MCP server builder
- `superpowers:debugging` -- Debugging workflow
- `superpowers:patterns` -- Design patterns reference

**From `skill-creator` plugin**:
- `skill-creator:skill-creator` -- Creates new skills

**From personal skills (`~/.claude/skills/`)**:
- `article-illustration` -- Article illustration generation

---

## 7. Plugin System Integration

### Plugin Structure

A complete plugin can bundle multiple components:

```
my-first-plugin/
├── .claude-plugin/
│   └── plugin.json          # Plugin metadata
├── commands/                # Slash commands
│   └── hello.md
├── agents/                  # Subagent definitions
│   └── helper.md
├── skills/                  # Skills (the focus of this research)
│   └── my-skill/
│       └── SKILL.md
├── hooks/                   # Hook definitions
│   └── hooks.json
└── .mcp.json               # MCP server configurations
```

### Plugin Metadata (`plugin.json`)

```json
{
  "name": "my-first-plugin",
  "version": "1.0.0",
  "description": "A sample Claude Code plugin"
}
```

### Skill Distribution via Plugins

- Skills bundled in a plugin's `skills/` directory are automatically discovered when the plugin is installed
- Plugin skills have the same format as personal/project skills
- Plugin skills are namespaced (e.g., `superpowers:tdd`) to avoid conflicts
- Users can override plugin skills by creating a same-named skill in personal or project directory

---

## Appendix: Related Systems

### A. Slash Commands (Detail)

**Built-in commands**: `/help`, `/clear`, `/compact`, `/init`, etc.

**Custom commands**: `.md` files in `commands/` directories (same discovery as skills: personal, project, plugin).

**Command frontmatter**:

```markdown
---
description: Deploy to staging environment
allowed-tools: Bash(git push*), Bash(npm run deploy*)
argument-hint: "<service-name>"
model: claude-sonnet-4-20250514
---
```

| Field | Description |
|-------|-------------|
| `description` | Shown in the `/` autocomplete menu |
| `allowed-tools` | Tool restrictions (supports glob patterns for Bash) |
| `argument-hint` | Placeholder text shown to user |
| `model` | Override the default model for this command |

### B. Hooks (Detail)

**Configuration**: `settings.json` at project or user level.

**Hook schema**:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          {
            "type": "command",
            "command": "python validate.py"
          }
        ]
      }
    ],
    "PostToolUse": [...],
    "UserPromptSubmit": [...],
    "Stop": [...],
    "SessionStart": [...],
    "Notification": [...]
  }
}
```

**Hook input/output**: Hooks receive JSON via stdin containing event data (tool name, input, output, etc.). They can return JSON to modify behavior or simply exit with code 0 (success) or 2 (block the action).

### C. MCP (Detail)

**Configuration example (`.mcp.json`)**:

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

**Scopes**:
1. Local `.mcp.json` -- Developer-specific, not committed
2. Project `.mcp.json` -- Team-shared, committed to repo
3. User `~/.claude/.mcp.json` -- Personal, applies to all projects
4. Plugin `.mcp.json` -- Bundled with plugin

### D. Subagents (Detail)

Subagents are defined as `.md` files with frontmatter:

```markdown
---
name: researcher
model: claude-sonnet-4-20250514
tools:
  - Read
  - Grep
  - Glob
  - WebSearch
skills:
  - web-research
  - source-analysis
---

# Research Agent

Conduct thorough research on the given topic...
```

Key subagent fields:

| Field | Description |
|-------|-------------|
| `name` | Agent identifier |
| `model` | Model to use |
| `tools` | Available tools (restricts from default set) |
| `skills` | Skills to auto-load when agent is dispatched |

CLI configuration: `claude --agents agents/` to specify agent directory.

---

## Source References

- Official Skills Documentation: https://docs.anthropic.com/en/docs/claude-code/skills
- Official Plugins Documentation: https://docs.anthropic.com/en/docs/claude-code/plugins
- Official Hooks Documentation: https://docs.anthropic.com/en/docs/claude-code/hooks
- Official Slash Commands: https://docs.anthropic.com/en/docs/claude-code/slash-commands
- Official MCP Documentation: https://docs.anthropic.com/en/docs/claude-code/mcp
- Official Subagents Documentation: https://docs.anthropic.com/en/docs/claude-code/subagents
- Official Memory/CLAUDE.md Documentation: https://docs.anthropic.com/en/docs/claude-code/memory

### Limitations of This Research

- **Community examples**: Web search was unavailable during research. Community-built skills from GitHub, blog posts, and forums were not retrievable. The examples section is based on official documentation and observed environment skills.
- **skill-creator plugin**: The full documentation for the `skill-creator` plugin was not retrieved. The plugin is installed in the current environment but its detailed usage instructions were not available for review.
- **Best practices page**: A dedicated "skills-best-practices" page at the Anthropic docs returned 404 and may not exist as a separate resource.
