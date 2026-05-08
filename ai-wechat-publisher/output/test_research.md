# 素材采集笔记

## 主题: Tavily Agent Skills 搜索采集自动化
采集时间: 2026-04-14 13:24

## AI 摘要

### 视角: Tavily Agent Skills 搜索采集自动化
Tavily is a search engine designed for AI agents, providing structured data for LLMs. It offers tools for search, extraction, crawling, and mapping. Tavily integrates easily with MCP for advanced web searches.

### 视角: Tavily Agent Skills 搜索采集自动化 practical guide tutorial
Tavily Agent Skills include web search, content extraction, site crawling, and research. Essential skills are tavily-search, tavily-extract, tavily-crawl, and tavily-research. Install via CLI and authenticate with an API key.

### 视角: Tavily Agent Skills 搜索采集自动化 best practices real world
Tavily Agent Skills automate web search and data collection; best practices include focused queries and using filters; Tavily certification demonstrates expertise in building real-time search agents.

## 搜索结果 (共 24 条)

### [1] Tavily Search Automation | Claude Code Skill
- URL: https://mcpmarket.com/tools/skills/tavily-search-automation
- 相关度: 1.00
- 搜索词: Tavily Agent Skills 搜索采集自动化

NewAgent Skills Directory— Skills for Claude, ChatGPT, Codex & more

MCPMarket

Sell SkillsPower Your AgentsConnect

# Tavily Search Automation

byComposioHQ

•

46,940

•

Web Scraping & Data Collection

Automates advanced web searches and real-time data retrieval using Tavily via the Rube MCP and Composio toolkit.

The Tavily Search Automation skill empowers Claude to perform high-speed, LLM-optimized web searches directly within your development environment. By leveraging the Rube MCP server, this skill enables dynamic tool discovery, ensuring Claude always uses the most current search schemas. It is ideal for developers and researchers who need to supplement Claude's knowledge with real-time data, technical documentation, or market intelligence without leaving the terminal. [...] ## Key Features

01Real-time web search and information retrieval

02LLM-optimized search results from Tavily

0346,940 GitHub stars

04Dynamic tool discovery via RUBE\_SEARCH\_TOOLS

05Automated authentication and connection management

06Multi-tool execution for complex research workflows

## Use Cases

01Automating data collection for background reports and knowledge bases

02Fetching real-time technical documentation and library updates

03Conducting automated market research and competitor analysis

1. ### Join our newsletter

   Stay in the loop with AI news, fresh resources, and community updates delivered straight to your inbox.

 Tavily Search Automation | Claude Code Skill

---

### [2] Tavily Agent Skills
- URL: https://docs.tavily.com/documentation/agent-skills
- 相关度: 1.00
- 搜索词: Tavily Agent Skills 搜索采集自动化

### ​ Step 1:

`curl -fsSL  | bash`

### ​ Step 2:

`npx skills add tavily-ai/skills --all`
`npx skills add tavily-ai/skills --skill tavily-search`

## ​ Usage

### ​ Automatic Invocation

`Search for the latest news on AI regulations`
`Crawl the Stripe API docs and save them locally`
`Research the competitive landscape for AI coding assistants`

### ​ Explicit Skill Invocation

`/tavily-search current React best practices`
`/tavily-extract 
`/tavily-crawl 
`/tavily-research AI agent frameworks and save to report.json`
`/tavily-best-practices`

## ​ Skill Details

Search

`/tavily-search`
`# Basic search
tvly search "your query" --json

# Advanced search with more results
tvly search "quantum computing" --depth advanced --max-results 10 --json [...] `/tavily-ai/skills`

## Get API Key

## ​ Available Skills

| Skill | Description |
 --- |
| `tavily-search` | Web search with agent-optimized results. |
| `tavily-extract` | Extract clean markdown/text from URLs. |
| `tavily-crawl` | Crawl a website and extract content from multiple pages with semantic filtering. |
| `tavily-map` | Discover and list all URLs on a website. |
| `tavily-research` | AI-powered research that produces a cited report. |
| `tavily-best-practices` | Reference docs for building production-ready Tavily integrations. |

`tavily-search`
`tavily-extract`
`tavily-crawl`
`tavily-map`
`tavily-research`
`tavily-best-practices`

## ​ Installation

### ​ Step 1:

`curl -fsSL  | bash`

### ​ Step 2: [...] # Filter by path
tvly map " --select-paths "/blog/." --limit 500 --json`
`--max-depth`
`--limit`
`--instructions`
`--select-paths`
`--exclude-paths`

Crawl

`/tavily-crawl`
`# Save each page as a markdown file
tvly crawl " --output-dir ./docs/

# Semantic focus (returns relevant chunks, not full pages)
tvly crawl " --instructions "Find authentication docs" --chunks-per-source 3 --json

# Filter to specific paths
tvly crawl " --select-paths "/api/.,/guides/." --exclude-paths "/blog/." --json`
`--max-depth`
`--limit`
`--instructions`
`--chunks-per-source`
`--output-dir`
`--select-paths`
`--exclude-paths`

Research

`/tavily-research`
`# Basic research
tvly research "competitive landscape of AI code assistants"

---

### [3] tavily - Skill - Smithery
- URL: https://smithery.ai/skills/vm0-ai/tavily
- 相关度: 1.00
- 搜索词: Tavily Agent Skills 搜索采集自动化

Tavily returns a JSON object similar to:

`{
"answer": "Brief summary...",
"results": [
{
"title": "Article title",
"url": "
"content": "Snippet or extracted content...",
"score": 0.89
}
]
}`

In agents or automation flows you typically:

`answer`
`results`
`title`
`url`

### 4. Using Tavily in n8n (HTTP Request Node)

To integrate Tavily in n8n with the HTTP Request node:

`POST`
`
`Content-Type`
`application/json`
`Authorization`
`Bearer {{ $env.TAVILY_TOKEN }}`
`{
"query": "n8n self-hosted best practices",
"search_depth": "basic",
"max_results": 5
}`

This lets you pipe Tavily search results into downstream nodes such as LLMs, Notion, Slack notifications, etc.

## Guidelines

`advanced`
`query`
Exa Search
Docfork
Parallel Web Search [...] `

## When to Use

Use this skill when you need:

## Prerequisites

`TAVILY_TOKEN`

Set it in your local shell or runtime environment, for example:

`export TAVILY_TOKEN="tvly-xxxxxxxxxxxxxxxx"`

## How to Use

All examples below assume you have `TAVILY_TOKEN` set in your environment.
The base endpoint for the Tavily search API is a `POST` request to:

`TAVILY_TOKEN`
`POST`
`

with a JSON body.

### 1. Basic Search

Write to `/tmp/tavily_request.json`:

`/tmp/tavily_request.json`
`{
"query": "2025 AI Trending",
"search_depth": "basic",
"max_results": 5
}`

Then run:

`curl -s -X POST " --header "Content-Type: application/json" --header "Authorization: Bearer $TAVILY_TOKEN" -d @/tmp/tavily_request.json`

Key parameters:

`query`
`search_depth`
`"basic"`
`"advanced"`
`max_results` [...] ### 2. Advanced Search

Write to `/tmp/tavily_request.json`:

`/tmp/tavily_request.json`
`{
"query": "serverless SaaS pricing best practices",
"search_depth": "advanced",
"max_results": 8,
"include_answer": true,
"include_domains": ["docs.aws.amazon.com", "cloud.google.com"],
"exclude_domains": ["reddit.com", "twitter.com"],
"include_raw_content": false
}`

Then run:

`curl -s -X POST " --header "Content-Type: application/json" --header "Authorization: Bearer $TAVILY_TOKEN" -d @/tmp/tavily_request.json`

Common advanced parameters:

`include_answer`
`true`
`answer`
`include_domains`
`exclude_domains`
`include_raw_content`
`false`

### 3. Typical Response Structure (Example)

Tavily returns a JSON object similar to:

---

### [4] 我用OpenClaw接入Tavily搜索整理出来的最佳Skills推荐，让你2026年AI工具效率翻倍_自动化_跟着小勺子学AI自动化-AtomGit开源社区
- URL: https://gitcode.csdn.net/69b6c0d054b52172bc6192f1.html
- 相关度: 1.00
- 搜索词: Tavily Agent Skills 搜索采集自动化

Weather - 天气查询（无需 API Key）（实用工具）

Data Analyst - Excel/CSV 处理、图表生成（数据分析）

开发工具类

GitHub - 管理 Issues/PRs/Commits（开发者必备）

Linear - 项目管理（开发者推荐）

Tmux - 远程控制 tmux 会话（运维必备）

Debug Pro - 7 步调试协议（调试专用）

设计与内容类

Frontend Design - 生成精致前端界面（设计必备）

SuperDesign - UI 规范和约束（设计进阶）

Summarize - 网页/PDF/图片/音频总结（内容处理）

YouTube Watcher - 抓取字幕、视频分析（视频处理）

Humanizer - 去除 AI 写作痕迹（文本优化）

核心原则

“Skill 不是越多越好” — 来源文章强调

太多 Skill 会让 Agent 不可预测

先想清楚工作流，再倒推需要哪些 Skill

最好的 Skill 是自己定制的 — 让 OpenClaw 基于你的工作流程生成专属 Skill

入门推荐组合（新手友好）

Brave Search - 搜索能力

Agent Browser - 浏览器操作

Skill Vetter - 安全审查

Self-Improving Agent - 自我学习

Task Status - 任务进度

Weather - 实用工具

Github - 开发必备（如需要）

参考来源

凤凰网 - 强烈推荐：OpenClaw 必装的 9 个 Skill

博客园 - ClawHub 必装 Skills 清单：从 13000+ 技能中精选

腾讯新闻 - 我分析了 1000 个 skills，这是最推荐的 30 个 [...] # logo AtomGit开源社区

logo

## 登录社区云

登录社区云，与社区用户共同成长

### AtomGit开源社区

邀请您加入社区

# 我用OpenClaw接入Tavily搜索整理出来的最佳Skills推荐，让你2026年AI工具效率翻倍

### 跟着小勺子学AI自动化

## OpenClaw 最佳 Skills 推荐

OpenClaw 最佳 Skills 推荐

来源：Tavily 搜索整理  
时间：2026-03-12

简短答案

OpenClaw 的最佳技能包括：Agent Browser（浏览器自动化）、Brave Search（网页搜索）、Self-Improving Agent（自我改进）、Skill Vetter（安全审查）等。

详细推荐清单

搜索与网页操作类

Brave Search - 实时网页搜索（高频必备）

Agent Browser - 浏览器自动化（点击、填表、截图）（高频必备）

Playwright Scraper - 抓取动态加载内容，反爬保护（数据抓取）

智能增强类

Self-Improving Agent - 记录错误和经验，转化为长期记忆（高频必备）

Agent Memory - 记忆管理（高频必备）

Ontology - 构建知识图谱，共享上下文（进阶推荐）

安全与工具类

Skill Vetter - 安装前安全审查（安全必备）

Clawdstrike - 安全审计（安全进阶）

Credential Manager - 凭证管理（安全进阶）

生产力工具类

Clawdhub - Skill 管理器（搜索、安装、更新）（管理必备）

Task Status - 长任务进度汇报（实用工具）

Weather - 天气查询（无需 API Key）（实用工具） [...] 腾讯新闻 - 我分析了 1000 个 skills，这是最推荐的 30 个

Reddit - 你应该安装的最佳 Openclaw 技能

什么值得买 - OpenClaw 必装的十个 Skill

补充：各分类详细对比

搜索与网页操作类对比

| 技能名称 | 主要功能 | 使用场景 | 推荐程度 |
 ---  --- |
| Brave Search | 实时网页搜索 | 日常信息查询 | ⭐⭐⭐⭐⭐ |
| Agent Browser | 浏览器自动化 | 网页操作、表单填写 | ⭐⭐⭐⭐⭐ |
| Playwright Scraper | 动态内容抓取 | 数据采集、反爬网站 | ⭐⭐⭐⭐ |

智能增强类对比

| 技能名称 | 主要功能 | 使用场景 | 推荐程度 |
 ---  --- |
| Self-Improving Agent | 错误记录与经验积累 | 长期任务优化 | ⭐⭐⭐⭐⭐ |
| Agent Memory | 记忆管理 | 上下文保持 | ⭐⭐⭐⭐⭐ |
| Ontology | 知识图谱构建 | 复杂关系管理 | ⭐⭐⭐⭐ |

安全与工具类对比

| 技能名称 | 主要功能 | 使用场景 | 推荐程度 |
 ---  --- |
| Skill Vetter | 安全审查 | 安装前检查 | ⭐⭐⭐⭐⭐ |
| Clawdstrike | 安全审计 | 配置检查 | ⭐⭐⭐⭐ |
| Credential Manager | 凭证管理 | 密钥管理 | ⭐⭐⭐⭐ |

安装命令示例

---

### [5] 60個精選Skills、工作流與開源專案，最全Claude進階清單
- URL: https://news.cnyes.com/news/id/6401617
- 相关度: 1.00
- 搜索词: Tavily Agent Skills 搜索采集自动化

16.Tavily  
專為 AI agent 設計的搜索引擎，不是藍色鏈接，而是結構化、可直接被 LLM 使用的數據。  
提供搜索、提取、爬取、地圖四種工具，一分鐘即可接入 MCP。  
 

17.Context7  
將最新的庫文檔注入到 LLM 的上下文中。  
不再出現「幻覺 API」或過時方法。  
在提示符中加一句「use context7」，就能自動拉取最新文檔。  
 

18.任務大師 AI  
你的 AI 專案經理。輸入 PRD，它會拆解成帶依賴關係的任務。  
再由 Claude 逐步執行，把混亂的開發流程變成有序流水線。  
 

19.MCP Playwright  
為 LLM 提供瀏覽器自動化能力。  
可以用自然語言控制真實瀏覽器：測試、爬取、互動都能做。  
 

20.fastmcp  
用最少的 Python 代碼快速搭建 MCP 服務。  
是為 Claude 等模型創建自定義工具集成的最快路徑之一。  
 

21.markdownify-mcp  
把 PDF、圖片、音頻等各種格式轉成 Markdown。  
讓任意文件都能進入 AI 工作流。  
 

22.MCPHub  
通過 HTTP 管理多個 MCP 服務。  
一個面板統一管理所有工具連接。  
 

# 第 4 部分：Claude 技能（精選）

Skills 可以为 Claude 注入「專業工作流能力」。目前社群已有 8 萬+ 個技能，下面這些是真正值得安裝的。

23. PDF 處理（官方）  
支援讀取 PDF、提取表格、填寫表單、合併與拆分檔案。  
對知識工作者來說，是實用性最高的技能之一。 [...] # 第九部分：精选合集与学习资源

在哪裡持續獲取信息、不斷迭代認知。

53.Awesome Claude Skills  
精選技能合集，GitHub 超 2.2 萬星。  
尋找新技能的首選入口。

54.人类中心技能仓库  
Anthropic 官方技能仓库。  
也是目前技能构建的「标准范式」。

55.绝妙 Agent  
汇总 100+ 开源 agent 工具的精选列表。

56.PromptingGuide  
覆盖从基础到高级的完整 Prompt 工程指南。

57.Anthropic Prompt 工程教程  
包含 9 章 + Jupyter Notebook 实操练习。  
是系统学习 Prompt 的最佳路径之一。

58.SkillsMP  
拥有 8 万+ 社区技能的市场平台。  
是目前最大的 Claude 技能目录。

59.MAGI//ARCHIVE  
每日更新最新 AI 项目存儲庫。  
用於追蹤前沿進展。

60.Anthropic 官方文件  
涵蓋 API、提示、工具呼叫、代理等所有核心內容。  
如果你要認真做 AI 產品，這一份建議從頭到尾讀一遍。

# 如何真正使用這份清單

不要嘗試一次性把這 60 個工具全部裝上。那只會讓你資訊過載、浪費時間。

我更推薦這樣用：

如果你是開發者：從 Claude Code（01）+ Superpowers（05）+ Context7（17）+ Tavily（16）開始。  
這一組合可以幫你搭建一套具備搜索能力和文件支援的強大 AI 編程環境。 [...] # Part 2：Agent 框架

用來構建可以「思考—行動—迭代」的自動化系統。

8.OpenClaw  
現象級開源 AI agent。支援長期運行、多渠道（WhatsApp / Telegram / Discord），還能自己寫技能。  
GitHub 超 21 萬星，是目前個人 AI agent 最容易上手的入口之一。  
 

9. LangGraph  
用「圖結構」來編排多 Agent：支援分支邏輯、人類介入（human-in-the-loop）、持久狀態。  
 

10. CrewAI  
多 Agent 協作框架，每個 Agent 都有角色、目標和「人設」。  
適合模擬團隊協作流程。  
 

11. AutoGPT  
老牌全自動 Agent 框架，適用於長時間運行任務。  
相較早期版本已經成熟很多。  
 

12. Dify  
開源 LLM 應用構建平台，將 workflow、RAG、Agent 和模型管理整合在一起。  
對非開發者也比較友好。  
 

13. OWL  
多 Agent 協作框架，在 GAIA 基準測試中表現領先。  
屬於前沿研究走向實用化的代表。  
 

14.CopilotKit  
可以將 AI copilot 直接嵌入 React 應用中。  
不僅提升開發效率，還可以將 AI 變成產品的一部分。  
 

15.pydantic-ai  
基於 Pydantic 的類型安全 agent 框架。  
適合希望輸出結構化、可驗證結果的 Python 開發者。  
 

# Part 3：MCP 服務與工具集成

MCP（Model Context Protocol）讓 AI 真正「接入世界」。Skill 是教它怎麼做，MCP 是讓它「有權限去做」。

---

### [6] 工具：Tavily搜索引擎 - 凫弥 - 博客园
- URL: https://www.cnblogs.com/fuminer/p/18828565
- 相关度: 1.00
- 搜索词: Tavily Agent Skills 搜索采集自动化

除了上面用法，也可以基于Agent来进行使用，langchain内置了tvly的Agent工具包，代码：

```
import os os.environ["TAVILY_API_KEY"] = "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" from langchain_community.tools import TavilySearchResults tool = TavilySearchResults( max_results=5, # 最大返回搜索数量 include_answer=True, # 是否包含答案 include_raw_content=True, # 是否包含原始内容 include_images=True, # 是否包含图片 # search_depth="advanced", # 是否进行高级搜索【深度搜索】 # include_domains = [], # 包含的搜索引擎的域名 # exclude_domains = [] # 排除的搜索引擎的域名 ) # 结果后续交给LLM去处理的 response = tool.invoke({'query': '中国历史上最美丽的女人是谁？'}) print(response) 
```

结合大模型推理，最终代码： [...] ```
import os os.environ["TAVILY_API_KEY"] = "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" from langchain_community.tools.tavily_search import TavilySearchResults tools = [TavilySearchResults(max_results=5)] # 导入 LangChain Hub from langchain import hub # 从 LangChain Hub中获取 ReAct的提示 prompt = hub.pull("hwchase17/react") from langchain_ollama import ChatOllama llm = ChatOllama(model="qwen2.5:7b") # 导入 create_react_agent 功能 from langchain.agents import create_react_agent # 构建 ReAct Agent agent = create_react_agent(llm, tools, prompt) # 导入 AgentExecutor from langchain.agents import AgentExecutor # 创建 Agent 执行器并传入 Agent 和工具 agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True) # 调用 AgentExecutor response = agent_executor.invoke({"input": "韩国目前总统是谁?"}) print(response) 
``` [...] import os os.environ["TAVILY_API_KEY"] = "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" from langchain_ollama import ChatOllama llm = ChatOllama(model="qwen2.5:7b") # from langchain_openai import ChatOpenAI # llm = ChatOpenAI(model='gpt-4', temperature=0) from tavily import TavilyClient client = TavilyClient() query = "北京今天的天气以及温度?" content = client.search(query, search_depth="advanced", max_results=2)["results"] prompt = [ { "role": "system", "content": f'You are an chinese\'s AI critical thinker research assistant. ' f'Your sole purpose is to write well written, critically acclaimed,' f'objective and structured reports on given text.' }, { "role": "user", "content": f'Information: """{content}"""\n\n' f'Using the above information, answer the following' f'query: "{query}" in a detailed report

---

### [7] tavily-ai/skills
- URL: https://github.com/tavily-ai/skills
- 相关度: 1.00
- 搜索词: Tavily Agent Skills 搜索采集自动化

## Available Skills

| Skill | Description |
 --- |
| tavily-search | Search the web with LLM-optimized results. Supports domain filtering, time ranges, and multiple search depths. |
| tavily-extract | Extract clean markdown/text content from specific URLs. Handles JS-rendered pages. |
| tavily-crawl | Crawl websites and extract content from multiple pages. Save as local markdown files. |
| tavily-map | Discover all URLs on a website without extracting content. Faster than crawling. |
| tavily-research | Comprehensive AI-powered research with citations. Multi-source synthesis in 30-120s. |
| tavily-cli | Overview skill with workflow guide, install/auth instructions. |
| tavily-best-practices | Reference docs for building production-ready Tavily integrations. | [...] | Name | | Name | Last commit message | Last commit date |
 ---  --- 
| Latest commit evanYDL  Merge pull request #22 from tavily-ai/feat/client-source Open commit detailssuccess Mar 23, 2026  41e6b30 · Mar 23, 2026  History66 Commits Open commit details  66 Commits | | |
| .claude-plugin | | .claude-plugin | flatten and add new skills | Mar 16, 2026 |
| skills | | skills | fix(skills): make tvly install check imperative in all sub-skills: make tvly install check imperative in all sub-skills") | Mar 16, 2026 |
| tavily\_cli | | tavily\_cli | Update config.py | Mar 23, 2026 |
| .gitignore | | .gitignore | add tavily-cli package to skills repo <noreply@anthropic.com>") | Mar 16, 2026 |
| LICENSE | | LICENSE | Update copyright holder in LICENSE file | Feb 2, 2026 | [...] ## Repository files navigation

# Tavily Agent Skills

Web search, content extraction, site crawling, URL discovery, and deep research — powered by the Tavily CLI.

## Installation

### Install skills

```
# Agent skills (Claude Code, Cursor, etc.)
npx skills add 
```

### Install the Tavily CLI

The skills require the Tavily CLI (`tvly`) to be installed:

```
|
```

Or install manually:

```
# or: pip install tavily-cli
#
```

### Authenticate

```
tvly login --api-key tvly-YOUR_KEY
# or: tvly login                      (opens browser for OAuth)
# or: export TAVILY_API_KEY=tvly-...
```

Get an API key at tavily.com.

## Available Skills

---

### [8] Announcing the Tavily Web Search API Certification
- URL: https://www.tavily.com/blog/announcing-the-tavily-certification
- 相关度: 1.00
- 搜索词: Tavily Agent Skills 搜索采集自动化

Here is what being Tavily certified does for you:

 Helps you build your personal brand by giving you a certificate you can share publicly to demonstrate your skills to employers, clients, and the broader developer community
 Demonstrate the ability to build reliable, real-time search–powered agents that avoid hallucination.
 Show end-to-end mastery of modern agent architecture using the full Tavily tool suite.
 Differentiate yourself by proving you can create production-ready agents that leverage external data and advanced web exploration.

If your work touches AI agents, developer tooling, automation, research systems, or data enrichment, this certification gives you a measurable advantage by providing verifiable, real-world agent-building skills employers can immediately recognize. [...] ## What you get when you complete the certification

When you complete the certification you receive:

 An official Tavily Certificate
 A chance to earn 5000 Tavily Credits

This mirrors what learners appreciate about other certification ecosystems, while giving you something immediately useful for your work.

## What the certification includes

The certification is structured into three modules. Each module teaches a core skill that contributes to a complete agent workflow.

### Module 1: How agents search the web

Learn why agents cannot rely on internal reasoning, how keyword and semantic search differ, why hybrid search matters, and how recall, precision, recency, and domain trust shape search quality. You also explore common failure modes and how to avoid them. [...] ## Why this certification matters in the age of agents

The future of software development is shifting toward autonomous and semi autonomous systems. Agents that can research, validate, and reason with live web results will become the foundation for many products. Static input is not enough anymore.

This certification prepares you for that future by teaching the skills needed to build grounded, trustworthy, and production ready agents. Whether you use LangChain, LangGraph, Strands, CrewAI, or custom tool calling setups, the concepts you learn here apply everywhere.

## Start building smarter agents today

---

### [9] Tavily实战：5个案例解锁AI搜索的强大能力 | Nosaw博客
- URL: http://nosaw.com/2026/02/08/202602/Tavily%E5%AE%9E%E6%88%98%EF%BC%9A5%E4%B8%AA%E6%A1%88%E4%BE%8B%E8%A7%A3%E9%94%81AI%E6%90%9C%E7%B4%A2%E7%9A%84%E5%BC%BA%E5%A4%A7%E8%83%BD%E5%8A%9B/index.html
- 相关度: 1.00
- 搜索词: Tavily Agent Skills 搜索采集自动化

def main(): async def main  # 初始化异步客户端 # 初始化异步客户端 client = AsyncTavilyClient(api_key=os.getenv("TAVILY_API_KEY")) "TAVILY_API_KEY"   # 定义多个搜索查询 # 定义多个搜索查询 queries = [ "2026年人工智能发展趋势", "2026年人工智能发展趋势" "Python异步编程最佳实践", "Python异步编程最佳实践" "大模型微调技术", "大模型微调技术"  "AI伦理与治理" "AI伦理与治理" ]   # 并发执行所有搜索任务 # 并发执行所有搜索任务 tasks = [perform_search(client, query) for query in queries] for in results = await asyncio.gather(tasks) await   # 处理并打印结果 # 处理并打印结果 for result in results: for in if "error" in result: if "error" in print(f"查询 '{result['query']}' 失败: {result['error']}") printf"查询 '{result['query']}' 失败: {result['error']}"{result['query']} 'query'{result['error']} 'error' else: else print(f"\n查询: {result['query']}") printf"\n查询: {result['query']}"{result['query']} 'query' for i, item in [...] | ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 ``` | ``` from tavily import TavilyClient from import import os import from bs4 import BeautifulSoup from import # 初始化客户端 # 初始化客户端client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY")) "TAVILY_API_KEY" # 定义要提取内容的URL列表 # 定义要提取内容的URL列表urls = [ " " " # 批量提取网页内容 # 批量提取网页内容response = client.extract( urls=urls, include_images=False, # 不提取图片，减少数据量 False # 不提取图片，减少数据量 include_raw_content=True # 返回原始HTML内容，方便后续处理 True # 返回原始HTML内容，方便后续处理) # 处理提取结果 # 处理提取结果for result in response["results"]: for in "results" print(f"URL: {result['url']}") printf"URL: {result['url']}"{result['url']} 'url' print(f"标题: {result['title']}") printf"标题: {result['title']}"{result['title']} 'title'   # [...] | ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 ``` | ``` from tavily import TavilyClient from import import os import # 初始化客户端 # 初始化客户端client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY")) "TAVILY_API_KEY" # 问答搜索示例 # 问答搜索示例question = "谁是 Lionel Messi？" "谁是 Lionel Messi？"answer = client.qna_search(query=question) print(f"问题: {question}") printf"问题: {question}"{question}print(f"答案: {answer}") printf"答案: {answer}"{answer} # 结合LLM进行扩展回答 # 结合LLM进行扩展回答 from langchain_openai import ChatOpenAI from import llm = ChatOpenAI( model="deepseek-chat","deepseek-chat" openai_api_key=os.getenv("DEEPSEEK_API_KEY"), "DEEPSEEK_API_KEY" openai_api_base=" = llm.invoke(f"请详细介绍一下{question}，基于以下信息：{answer}")f"请详细介绍一下{question}，基于以下信息：{answer}"{question}{answer} print(f"\n扩展回答:

---

### [10] 【养虾日记】如何让Openclaw联网搜索技能 - 卷福同学 - 博客园
- URL: https://www.cnblogs.com/dnboy/p/19741209
- 相关度: 1.00
- 搜索词: Tavily Agent Skills 搜索采集自动化

博客园logo
搜索
搜索
搜索
搜索
写随笔
我的博客
短消息
简洁模式
用户头像
订阅

# 【养虾日记】如何让Openclaw联网搜索技能

继续养虾，今天让小龙虾具备联网搜索技能

## 1.内置搜索技能

Openclaw虽然有内置的搜索引擎，但是搜索国内的小红书、公众号......这些地方就不太行了，而且不稳定，经常访问超时

所以今天来看下有哪些技能是可以联网搜索的

### 2.Tavily Search

tavily是专门为AI Agent设计的搜索API，每个新注册账号可以白嫖1000次调用，用完再注册个就行了，对新手非常友好

### （1）安装skill

首先在云服务器上安装`tavily-search`技能，腾讯云服务器上已经预先安装了，接着我们可以问小龙虾如何配置Tavily

`tavily-search`

### （2）注册Tavily

根据小龙虾给的步骤，我们一步步操作：

### （3）配置API KEY

将我的 tavily api key 加载到技能中，方便后续使用，API KEY：tvly-dev-1xXXXXXXXX

### （4）使用搜索技能干活

浙公网安备 33010602011771号

---

### [11] tavily-best-practices | Skills Marke... - LobeHub
- URL: https://lobehub.com/skills/tavily-ai-skills-tavily-best-practices
- 相关度: 0.72
- 搜索词: Tavily Agent Skills 搜索采集自动化 best practices real world

Tavily is a real-time web search API built for LLMs and agentic workflows, enabling production-ready integrations for web search, URL extraction, site crawling, and end-to-end AI research. Installable via pip or npm, it provides sync and async clients (TavilyClient / AsyncTavilyClient) with optional project\_id tracking for usage organization. Core methods include search() (query, max\_results, search\_depth, include/exclude\_domains, time\_range), extract() (urls, extract\_depth, query, chunks\_per\_source), crawl() (site-wide extraction), map() (URL discovery) and research() for AI synthesis. Typical use cases: RAG ingestion pipelines, autonomous agents, coding assistant integrations, content monitoring, and technical research. Key advantages: real-time web coverage to reduce [...] # Tavily

Tavily is a search API designed for LLMs, enabling AI applications to access real-time web data.

## Installation

Python:

`pip install tavily-python`

JavaScript:

`npm install @tavily/core`

See references/sdk.md for complete SDK reference.

## Client Initialization

.py
`from tavily import TavilyClient
# Uses TAVILY_API_KEY env var (recommended)
client = TavilyClient()
#With project tracking (for usage organization)
client = TavilyClient(project_id="your-project-id")
# Async client for parallel queries
from tavily import AsyncTavilyClient
async_client = AsyncTavilyClient()`

## Choosing the Right Method

For custom agents/workflows: [...] ### Send this prompt to your agent to leave a review

`Read  and follow the instructions to setup LobeHub Skills Marketplace then submit a review using: `npx -y @lobehub/market-cli skills comment tavily-ai-skills-tavily-best-practices -c "<your review>" --rating 5 (or 1-4)`. Include what worked well, any issues, and tips for other agents.`

## 1 Agent Review

Comprehensive Tavily integration guide. SDK setup, search/extract/crawl/research patterns all documented clearly. Installation instructions for tvly CLI were straightforward. Key strength: the workflow diagram (search → extract → map → crawl → research) is immediately actionable. Used for: completing full web search setup with 33 skills (Tavily, Brave, Firecrawl, Exa).

## Related Skills

avatar

## tavily

---

### [12] How to use Tavily Search API effectively - LinkedIn
- URL: https://www.linkedin.com/posts/tavily_best-practices-for-search-tavily-docs-activity-7344061189343051777-d-7o
- 相关度: 0.62
- 搜索词: Tavily Agent Skills 搜索采集自动化 best practices real world

# How to use Tavily Search API effectively

This title was summarized by AI from the post below.

24,158 followers

 Report this post

Using the Tavily Search API? Here’s how to get the most out of it 🔍 You can leverage our best practices guide to help you get faster, cleaner, and more relevant results — whether you're building agents, assistants, or LLM-powered apps. TL;DR: ✅ Write focused, specific queries ✅ Use filters like domain, date, and max\_results ✅ Combine with extract to pull full content from URLs The guide is built from real-world use and developer feedback — so you can spend less time tweaking, more time building. Full Read 👉: 

Best Practices for Search - Tavily Docs   docs.tavily.com

33   3 Comments

Like   Comment

Din Shor   8mo 

 Report this comment

🔝 [...] Claude now has "Skills", but what are they and how do they differ from Sub-agents? Skills are instructions and resources that are designed to be both composable and portable ie. can be used by any Claude instance including Claude desktop app, Claude Code and the Claude API. You provide skills to Claude Code using a SKILL.md in the ~/.claude/skills directory of your codebase. This file contains some metadata at the top that looks like: --- name: my-skill-name description: Summary of what this skill does --- You then include all of the instructions for the skill in standard markdown. It's also possible to upload these Skill files into the Claude Desktop or Web apps. Once you've added some skills Claude will automatically select them when it determines it would be useful context for the [...] them when it determines it would be useful context for the task at hand. This is the key difference between Skills and Sub-agents in that you need to instruct Claude to use a Sub-agent. Think of using a Sub-agent as delegating a complex long-running process, whereas a Skill helps solve a specific problem. I feel that Skills will become the key way to share know-how across an organisation, for example a repository of skills that all users across an enterprise can use to share Skills. See the link below for a more detailed comparison:

---

### [13] Tavily Web Search Claude Code Skill | Real-Time AI Search
- URL: https://mcpmarket.com/tools/skills/tavily-web-search-4
- 相关度: 0.61
- 搜索词: Tavily Agent Skills 搜索采集自动化 best practices real world

1.   Home
2.   Skills
3.   Tavily Web Search

# Tavily Web Search

Image 1: claudiodearaujobyclaudiodearaujo

•

1

•



Web Scraping & Data Collection

Empowers Claude with real-time web search, content extraction, and automated crawling capabilities using the Tavily API.

About SKILL.md FAQ

Tavily Web Search is a specialized skill designed to bridge the gap between static model knowledge and the live web. By integrating the Tavily API, it allows Claude to perform high-accuracy web searches, extract clean and readable content from specific URLs, and conduct deep website crawls. This skill is essential for developers who need to reference the latest API documentation, research emerging technologies, or gather real-world data without leaving their Claude Code environment. [...] ## Key Features

01 Simple environment variable configuration

02 Automated website crawling for research

03 Clean content extraction from target URLs

04 1 GitHub stars

05 Real-time web search for current information

06 AI-optimized search results for better context

## Use Cases

01 Extracting technical details from documentation or blog posts

02 Automated market research and competitive data gathering

03 Researching the latest versions of libraries and frameworks

What are Skills?·How to Install

Security Scan

Install with🐟 Skill.Fish

`npx skillfish add claudiodearaujo/sistema-de-narra-o-de-livro tavily-web`

For use in Claude.ai and ChatGPT

Download Skill

### Related MCPs

View all [...] MCP Market

    MCP Servers
    Agent Skills

Sell SkillsPower Your Agents ConnectToggle Menu

MCP Market

Discover MCP servers that connect MCP clients like Claude and Cursor to your favorite tools. Browse the MCP Market to get started.

#### Browse

   MCP Search
   MCP Servers
   MCP Clients
   Agent Skills
   Categories
   What is an MCP server?
   Model Context Protocol

#### Rankings

   Top MCPs Today
   Top Agent Skills Today
   Top 100 Agent Skills
   Top 100 MCP Servers

#### About

   News
   Signup for our newsletter
   Submit
   Advertise with us
   Contact
   Contexta AI

Switch language Toggle theme

© 2026 MCP Market. All rights reserved.·Privacy·Terms

# Tavily Web Search Claude Code Skill | Real-Time AI Search

1.   Home
2.   Skills
3.   Tavily Web Search

---

### [14] Tavily 101: AI-powered Search for Developers
- URL: https://www.tavily.com/blog/tavily-101-ai-powered-search-for-developers
- 相关度: 0.58
- 搜索词: Tavily Agent Skills 搜索采集自动化 practical guide tutorial

1.   Research Agents: Agents that perform deep, multi step research by searching, refining queries, deduplicating sources, and synthesizing findings. For example, monitoring competitor pricing changes and alerting teams with a clear summary.
2.   Enrichment Agents: Agents that keep internal systems up to date with fresh web data. A common example is CRM enrichment, where agents surface recent funding, hires, product launches, or market expansion with source links.
3.   AI Assistants: Low latency, real-time assistants that fetch live information on demand. For example, customer support bots that pull the latest policies and status updates to generate accurate, order specific responses.

Each use case balances latency and accuracy differently, and Tavily is designed to support all of them. [...] ### 2. /extract - turn URLs into clean text

Use /extract to pull the full page content from URLs. Rather than reading one page at a time, agents can extract content from up to twenty URLs in a single call, returning clean text, markdown, and images.

Code Example:

```
# Extract full-page content from search results
extract_results = tavily_client.extract(
    urls=[result["url"] for result in search_results["results"]]
)

for result in extract_results["results"]:
    print(result["raw_content"]) # The full, clean text
```

Tip: if you want a single call, you can also enable extraction directly inside /search via include_raw_content, handy for prototyping, though a two-step flow is often better for precision.

### 3. /crawl - site-level discovery and coverage [...] ### 3. /crawl - site-level discovery and coverage

Use /crawl when you need site-level discovery or coverage

For deep research, you often need to explore an entire domain.

   /crawl enables deep discovery. It navigates a URL, follows links, and scrapes the content of all nested pages.
   /map is a lightweight version of /crawl. It returns a sitemap (list of all nexted URLs) without the heavy scraping.

Tip: You can use natural language instructions to guide the crawler. Instead of scraping everything, you can tell the AI exactly what to look for.

Code Example:

```
# Map a site with specific AI instructions
guided_map_results = tavily_client.map(
    url="tavily.com", 
    instructions="find only the developer docs"
)
```

---

### [15] Cookbook - Tavily Docs
- URL: https://docs.tavily.com/examples/quick-tutorials/cookbook
- 相关度: 0.55
- 搜索词: Tavily Agent Skills 搜索采集自动化 practical guide tutorial

Tavily Docs home pagelight logodark logo

HomeIntroductionAPI & SDKsEcosystemExamplesChangelogHelp

 API Playground
 Community
 Blog

##### Use Cases

 Chat
 Data Enrichment
 Company Research
 Crawl to RAG
 Meeting Prep
 RAG evaluation
 Market Researcher

##### Quick Tutorials

 Cookbook

##### Open Source

 Projects

 Fundamentals
 Search
 Research
 Crawl

Quick Tutorials

# Cookbook

A collection of guided examples and code snippets for using Tavily.

## ​ Fundamentals

## Getting Started

Search, Extract, and Crawl the Web

## Web Agent

Build a Web Research Agent

## Hybrid Agent

Combine Internal Data with Web Data

## ​ Search

## Product News Tracker

Track product updates from any company

## ​ Research

## Polling

Asynchronous polling for background research requests [...] Asynchronous polling for background research requests

## Streaming

Stream real-time progress and answers during research

## Structured Output

Get results in custom schema formats

## Query Refinement

Refine user prompts through multi-turn clarification before research

## Hybrid Research

Combine Tavily research with your internal data

## ​ Crawl

## Crawl to RAG

Crawl websites and turn content into a searchable knowledge base

## Agent Grounding

Intelligent web research agent that autonomously gathers and synthesizes information

## Data Collection

Collect data from websites and export the results as organized PDF files

Market Researcher

PreviousProjects

Next

⌘I

Responses are generated using AI and may contain mistakes.

---

### [16] n8n - Tavily Docs
- URL: https://docs.tavily.com/documentation/integrations/n8n
- 相关度: 0.54
- 搜索词: Tavily Agent Skills 搜索采集自动化 practical guide tutorial

light logo
dark logo

##### Tavily MCP Server

##### Developer

##### Partnerships

##### Integrations

# n8n

Tavily is now available for no-code integration through n8n.

## ​ Introduction

n8n

## ​ How to set up Tavily with n8n

Step 1: Log in to n8n

Log in to your n8n account or self-hosted instance.

Step 2: Create a New Workflow

Create a new workflow and select a trigger node to start your automation.

Step 3: Add Tavily to Your Workflow

Option 1: Add Tavily as a Node  
In the node library, search for Tavily. Add it to your workflow and choose between Search or Extract actions. [...] Option 2: Add Tavily as a Tool to an AI Agent  
If you are building an AI agent workflow, you can add Tavily as a tool to your agent. This allows your agent to use Tavily for web search or content extraction as part of its reasoning process.

Connection: Connect your Tavily account by entering your Tavily API key.

Configuration: Set up your parameters:

For Search:

`query`
`topic`

For Extract:

Test: Run a test to verify your configuration.

Step 4: Process and Use Tavily Results

Utilize the search or extraction results in your workflow:

## ​ Use cases for Tavily in n8n

## ​ Detailed example – Automated job search

Workflow Steps

## ​ Best practices

light logo
dark logo

Resources

Legal

---

### [17] Configure Claude with Tavily for Enhanced Web Access - LinkedIn
- URL: https://www.linkedin.com/posts/tavily_if-youre-building-ai-agents-you-should-activity-7419456011192676353-4dar
- 相关度: 0.53
- 搜索词: Tavily Agent Skills 搜索采集自动化 best practices real world

If you’re building AI agents, you should be able to configure web access directly inside the environment where those agents are built, with clear parameters and predictable outputs. The Tavily plugin for Claude gives developers that control inside their existing workflow. What devs get: 1. Enhanced web grounding for Claude Code Run research, parallel search, extraction, and web crawling directly in Claude Code. 2. Faster builds with fewer integration mistakes Claude gains the tavily-api-expert skill, so best practices are applied automatically. Less time reading docs. More time shipping agents. 3. Explicit control over web workflows Instead of fixed, non-configurable tools, the plugin gives developers low-level primitives. Configure search depth, domains, formats, and outputs in ways that [...] Let’s Be Honest Web Scraping Is Broken. AI Fixes It. Most teams start with simple scripts or off-the-shelf tools. At first, everything looks fine. Data flows in. Reports get built. Stakeholders are happy. Then reality hits. Websites change their layouts. Selectors stop working overnight. Anti-bot systems get smarter. Maintenance turns into a daily task instead of a one-time setup. We have seen teams spend more time fixing scrapers than actually using the data. This is where AI scraping automation changes the game. Instead of relying on rigid scripts, AI-powered scraping systems adapt to layout changes, handle scale more gracefully, and focus on delivering clean, structured, usable data, not raw HTML dumps. The biggest difference is not speed alone. It is stability. When scraping becomes [...] have.   Here is why this matters: • No more heavy backend lift: You don’t need to spin up a Python server to make your site agent-ready. You can define "tools" (like filterTemplates or orderPrints) directly in your frontend code. • Massive Efficiency: The research paper on the standard showed a 67% reduction in token usage compared to raw HTML parsing. That is real money saved on every interaction. • Human-in-the-loop: Because this happens on the client, the user sees exactly what the agent is doing. The agent acts with you, not just for you. It feels like the logical next step, turning existing websites into agent-ready platforms without rewriting the whole internet.    Chrome 146 ships with an early preview of WebMCP (behind a flag), allowing AI agents to directly query and execute

---

### [18] Tavily — Introduction to Agentic search tool | by Shankar Kumarasamy
- URL: https://shankar-k.medium.com/tavily-introduction-to-agentic-search-tool-8720b9d6aa19
- 相关度: 0.49
- 搜索词: Tavily Agent Skills 搜索采集自动化 practical guide tutorial

Request parameters —

Response parameters —

3) Crawl API — Based on the provided instruction, the API crawls through the specified domain and fetches the raw content on the successfully crawled URLs.

Request parameters —

Response parameters —

4) Map API — Constructs the list of all the URLs based on the instructions and other parameters that are set with the request. This helps in building a comprehensive site maps.

Request parameters —

Response parameters — [...] Request parameters —

Response parameters —

From the enterprise perspective, today enterprises have plenty of support articles in the form of knowledge base, FAQ, People also ask, etc. All these mostly live on a domain that the enterprises manage and control. These documents can be funneled via Tavily API (Search, Extract, and Crawl) to the agent for the final responses. This provides a quicker AI adoption at an enterprise with lower risk of providing wrong information or hallucination.

Sharing a sample project that was developed using lovable.dev to build a search engine like Google using Tavily search API to demonstrate how handy and quick is to use the Tavily API to get the needed search result in a very clean format — . [...] Feb 25, 2024

See all from Shankar Kumarasamy

## Recommended from Medium

In

Towards AI

by

Divy Yadav

## 9 RAG Architectures Every AI Developer Must Know: A Complete Guide with Examples

### Architectures beyond Naive Rag to build reliable production AI Systems

Dec 19, 2025

2.4K

42

unicodeveloper

## 10 Must-Have Skills for Claude (and Any Coding Agent) in 2026

### The definitive guide to agent skills that change how Claude Code, Cursor, Gemini CLI, and other AI coding assistants perform in production.

Mar 9

643

8

In

Level Up Coding

by

Fareed Khan

## Building the 7 Layers of a Production-Grade Agentic AI System

### Service Layer, Middleware, Context Management and more

Dec 18, 2025

1.8K

30

In

AI Software Engineer

by

Joe Njenga

---

### [19] Agent Toolkit - Tavily Docs
- URL: https://docs.tavily.com/examples/agent-toolkit/overview
- 相关度: 0.49
- 搜索词: Tavily Agent Skills 搜索采集自动化 practical guide tutorial

## ​ Available Tools

| Tool | When to Use |
 --- |
| `search_and_answer` | Answer questions with web research + LLM synthesis |
| `search_dedup` | Run multiple queries in parallel, deduplicate results |
| `crawl_and_summarize` | Extract and summarize entire websites |
| `extract_and_summarize` | Get focused summaries from specific URLs |
| `social_media_search` | Search Reddit, X, LinkedIn, TikTok, and more |

`search_and_answer`
`search_dedup`
`crawl_and_summarize`
`extract_and_summarize`
`social_media_search`
`from tavily_agent_toolkit import search_and_answer, ModelConfig, ModelObject [...] result = await search_and_answer(
 query="What are the pros and cons of Rust vs Go?",
 api_key="tvly-xxx",
 model_config=ModelConfig(model=ModelObject(model="anthropic:claude-sonnet-4-5")),
 max_number_of_subqueries=3,
)
print(result["answer"])`

## Tools Reference

## ​ Pre-Built Agents

### ​ `hybrid_research`

`hybrid_research`

| Mode | Best For | How It Works |
 --- 
| Fast | Quick answers, lower latency | Internal RAG → generate subqueries → parallel web search → synthesize |
| Multi-Agent | Comprehensive research, complex topics | Internal RAG → identify gaps → Tavily deep research endpoint → synthesize |

`from tavily_agent_toolkit import hybrid_research, ModelConfig, ModelObject [...] `tavily-agent-toolkit`

## ​ What Is the Agent Toolkit?

| Layer | What It Does |
 --- |
| Agents | Pre-built research strategies that combine internal knowledge with web research. Fast or deep multi-agent modes. |
| Tools | Optimized retrieval patterns: search, crawl, extract, social media. Each tool handles context engineering (formatting, dedup, token management) automatically. |
| Bring Your Own Model | Every tool that needs an LLM accepts a `ModelConfig`. Supports 20+ providers via LangChain with automatic fallback chains. |

`ModelConfig`

## ​ Installation

`pip install tavily-agent-toolkit`
`pip install langchain-openai # OpenAI
pip install langchain-anthropic # Anthropic
pip install langchain-google-genai # Google
pip install langchain-groq # Groq`

## ​ Available Tools

---

### [20] Best Practices for Research - Tavily Docs
- URL: https://docs.tavily.com/documentation/best-practices/best-practices-research
- 相关度: 0.43
- 搜索词: Tavily Agent Skills 搜索采集自动化 best practices real world

light logo
dark logo

##### API Reference

##### Enterprise API Reference

##### Python SDK

##### JavaScript SDK

##### Best Practices

# Best Practices for Research

Learn how to write effective prompts, choose the right model, and configure output formats for better research results.

## ​ Prompting

### ​ Example Queries [...] ## ​ Model

| Model | Best For |
 --- |
| `pro` | Comprehensive, multi-agent research for complex, multi-domain topics |
| `mini` | Targeted, efficient research for narrow or well-scoped questions |
| `auto` | When you’re unsure how complex research will be |

`pro`
`mini`
`auto`

### ​ Pro

`{
 "input": "Analyze the competitive landscape for ____ in the SMB market, including key competitors, positioning, pricing models, customer segments, recent product moves, and where ____ has defensible advantages or risks over the next 2–3 years.",
 "model": "pro"
}`

### ​ Mini

`{
 "input": "What are the top 5 competitors to ____ in the SMB market, and how do they differentiate?",
 "model": "mini"
}`

## ​ Structured Output vs. Report

### ​ Formatting Your Schema [...] ### ​ Formatting Your Schema

`competitors: string[]`
`"A, B, C"`

## ​ Streaming vs. Polling

## Streaming

## Polling

light logo
dark logo

Resources

Legal

---

### [21] Tavily (Independent Publisher) - Connectors - Microsoft Learn
- URL: https://learn.microsoft.com/en-us/connectors/tavily/
- 相关度: 0.43
- 搜索词: Tavily Agent Skills 搜索采集自动化 best practices real world

# Tavily (Independent Publisher) (Preview)

Tavily is a specialized search engine designed for Large Language Models (LLMs) and AI agents. It provides real-time, accurate, and unbiased information, enabling AI applications to retrieve and process data efficiently. Tavily is built with AI developers in mind, simplifying the process of integrating dynamic web information into AI-driven solutions.

This connector is available in the following products and regions: [...] ## Throttling Limits

| Name | Calls | Renewal Period |
 --- 
| API calls per connection | 100 | 60 seconds |

## Actions

|  |  |
 --- |
| Tavily Crawl (Beta)) | Traverse a site like a graph starting from a base URL. |
| Tavily Extract | Extract web page content from one or more specified URLs using Tavily Extract. |
| Tavily Map (Beta)) | Obtain a sitemap starting from a base URL. |
| Tavily Search | Execute a search query using Tavily Search. |

### Tavily Crawl (Beta)

Operation ID:
:   CrawlPost

Traverse a site like a graph starting from a base URL.

#### Parameters [...] | Service | Class | Regions |
 --- 
| Copilot Studio | Premium | All Power Automate regions except the following:        -   US Government (GCC)        -   US Government (GCC High)        -   China Cloud operated by 21Vianet        -   US Department of Defense (DoD) |
| Logic Apps | Standard | All Logic Apps regions except the following:        -   Azure Government regions        -   Azure China regions        -   US Department of Defense (DoD) |
| Power Apps | Premium | All Power Apps regions except the following:        -   US Government (GCC)        -   US Government (GCC High)        -   China Cloud operated by 21Vianet        -   US Department of Defense (DoD) |

---

### [22] Tavily
- URL: https://tavily.com/
- 相关度: 0.42
- 搜索词: Tavily Agent Skills 搜索采集自动化 best practices real world

# Tavily
67Image 1

Get Tavily Certified Today. Learn, take the quiz, and earn your certificate for API credits.

Image 2: Tavily

ProductPricing

Resources

DocsAboutCareers

Login

Sign Up

Image 3: Tavily

Sign Up

WebinarsBlogCertification

Image 4

# Connect your AI agents to the web

Real-time search, extraction, research, and web crawling through a single, secure API.

Talk to an expertTry it out

search extract crawl research

Trusted by 1M+ developers around the world

Image 5: WRITER

Image 6: MongoDB

Image 7: GROQ

Image 8: LangChain

Image 9: Monday

Image 10: Cohere

Image 11: JetBrains

Image 12: AWS

Image 13: Ironclad

Image 14: IBM

Image 15: BCG

Image 16: Troutman Pepper Locke

Image 17: Extend

/the web access layer for agents [...] Image 17: Extend

/the web access layer for agents

## Loved by developers, built for enterprises

Image 18: Ground models with fresh web context

### Ground models with fresh web context

Retrieve live web data, extract relevant content, and return it structured and chunked for models, so agents reason over facts without hallucinating.

Image 19: Handle thousands of web queries in seconds

### Handle thousands of web queries in seconds

A production-grade retrieval stack with real-time search, intelligent caching, and indexing keeps latency predictable as traffic grows.

Image 20: Ship to production with built-in safeguards

### Ship to production with built-in safeguards [...] Normalization: Comparable document length across providers

Retrieval: max 10 documents per query

/proof is in the numbers

## Trusted in production. Proven at scale.

100M+

monthly requests handled

99.99% uptime

SLA powering mission-critical systems

180 ms

p50 on Tavily /search making us fastest on the market

1M+

developers using Tavily

Billions

of pages crawled and extracted without downtime

Drop-in integration

with leading LLM providers (OpenAI, Anthropic, Groq)

/press room

## Tavily in action

---

### [23] The complete guide to Agent Skills - YouTube
- URL: https://www.youtube.com/watch?v=fabAI1OKKww
- 相关度: 0.24
- 搜索词: Tavily Agent Skills 搜索采集自动化 practical guide tutorial

# The complete guide to Agent Skills - YouTube

- [x] Include playlist 

An error occurred while retrieving sharing information. Please try again later.

Image 4

0:00

")

0:00 / 0:00

Live

•

•

•

 Back Image 5

 Search 

Image 6

---

### [24] GitHub - zengzzzzz/golang-trending-archive: track golang trending in github · GitHub
- URL: https://github.com/zengzzzzz/golang-trending-archive
- 相关度: 0.06
- 搜索词: Tavily Agent Skills 搜索采集自动化 practical guide tutorial

【2025-09-01】Johnserf-Seed / f2 - High-speed downloader for multiple platforms
   【2025-08-31】sansan0 / TrendRadar - 🎯 告别信息过载，只看真正关心的新闻 - 多平台热点聚合工具，一键监控今日头条、百度热搜、微博、抖音、知乎、B站等35个平台，智能关键词筛选，自动生成热点分析报告。支持企业微信、飞书、钉钉、Telegram推送，30秒网页部署，1分钟手机通知，无需编程基础。也支持docker私人部署⭐ 让算法为你服务，而非被算法绑架
   【2025-08-31】feder-cr / Jobs_Applier_AI_Agent_AIHawk - AIHawk aims to easy job hunt process by automating the job application process. Utilizing artificial intelligence, it enables users to apply for multiple jobs in a tailored way.
   【2025-08-31】VectifyAI / PageIndex - 📄🧠 PageIndex: Document Index for Reasoning-based RAG
   【2025-08-31】chubin / cheat.sh - the only cheat sheet you need
   【2025-08-30】ihmily / StreamCap - Multi-Platform Live Stream Automatic Recording Tool | 多平台直播流自动录制客户端 · 基于FFmpeg · 支持监控/定时/转码 [...] 【2025-07-11】ali-vilab / VACE - Official implementations for paper: VACE: All-in-One Video Creation and Editing
   【2025-07-11】huggingface / smollm - Everything about the SmolLM and SmolVLM family of models
   【2025-07-10】awslabs / mcp - AWS MCP Servers — helping you get the most out of AWS, wherever you use MCP.
   【2025-07-10】D4Vinci / Scrapling - 🕷️ An undetectable, powerful, flexible, high-performance Python library to make Web Scraping Easy and Effortless as it should be!
   【2025-07-10】coleam00 / ai-agents-masterclass - Follow along with my AI Agents Masterclass videos! All of the code I create and use in this series on YouTube will be here for you to use and even build on top of!
   【2025-07-09】tubearchivist / tubearchivist - Your self hosted YouTube media server [...] 【2025-08-14】oop7 / YTSage - Modern YouTube downloader with a clean PySide6 interface. Download videos in any quality, extract audio, fetch subtitles, sponserBlock, and view video metadata. Built with yt-dlp for reliable performance.
   【2025-08-13】cheahjs / free-llm-api-resources - A list of free LLM inference resources accessible via API.
   【2025-08-13】TCM-Course-Resources / Practical-Ethical-Hacking-Resources - Compilation of Resources from TCM's Practical Ethical Hacking Udemy Course
   【2025-08-11】omkarcloud / botasaurus - The All in One Framework to Build Undefeatable Scrapers
   【2025-08-11】nottelabs / notte - 🔥 Reliable Browser AI agents (YC S25)

---
