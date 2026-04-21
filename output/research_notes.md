# 素材采集笔记

## 主题: OpenClaw 飞书 AI助手 评测
采集时间: 2026-04-21 14:50

## AI 摘要

### [Tavily] 视角: OpenClaw 飞书 AI助手 评测
OpenClaw is an open-source AI assistant that runs locally, offering privacy and flexibility. It connects to multiple platforms and automates tasks. It's gaining popularity for its ability to execute commands and manage daily activities.

### [Tavily] 视角: OpenClaw 飞书 AI助手 评测 practical guide tutorial
OpenClaw is a local AI assistant that connects to Feishu for task automation. It integrates with Feishu via a plugin and requires configuration in the developer platform. OpenClaw operates locally to ensure data privacy and control.

### [Tavily] 视角: OpenClaw 飞书 AI助手 评测 best practices real world
OpenClaw is an AI agent that connects to Feishu for enhanced productivity. It automates tasks and integrates with Feishu's features. It runs locally for privacy and control.

### [Exa] 告别 “笨虾”！飞书对接 OpenClaw 全攻略 + 前端角色深度调教，让 AI 助理智商拉满🔥告别笨虾！OpenC - 掘金
Summary:
- This guide explains how to connect OpenClaw (a local AI assistant, aka “小龙虾”) with Feishu (飞书) to create a capable front-end AI assistant for team collaboration.
- Key takeaways:
  - Chinese domestic version of OpenClaw is recommended over the overseas version for Feishu integration due to easier deployment, better Chinese support, and native Feishu compatibility.
  - Step-by-step Feishu integration:
    - Create a Feishu 自建应用, enable robot interactions, and obtain App ID/App Secret.
    - Configure permissions and event subscriptions (WebSocket recommended) to receive messages and read files/docs.
    - In OpenClaw, set up gateway, select Feishu channel, paste credentials, and connect via WebSocket; verify with a test message.
  - Role customization is crucial: define a dedicated, locally stored role (Markdown file) to upgrade AI behavior. This “front-end Feishu AI assistant” should be tailored to front-end work, enforce rules, memory, and non-disclosure of sensitive data.
  - Provided a ready-to-use Feishu-specific role template that emphasizes:
    - Senior front-end expertise (Vue/React/TS, UI libs, styling)
    - Feishu-specific interaction rules (respond in single/dedicated contexts, @ mentions in groups)
    - Core capabilities: code generation, bug triage, documentation, API scaffolding
    - Safety constraints: data privacy, local storage, no hallucinations, secure coding practices
    - Memory and persistence for tech stack, project standards, and preferences
  - Advanced tips (not detailed in excerpt) promise further tricks to improve intelligence, stability, and alignment with front-end workflows.
- Practical outcome: following the guide enables a high-IQ Feishu AI assistant that can generate code, extract requirements, aid bug fixing, manage tasks, and collaborate without leaking sensitive data, all while staying within defined front-end-focused roles.

### [Exa] 飞书助手与OpenClaw对比_新浪新闻
OpenClaw 与飞书助手（aily 工作助手）对比评测概览，聚焦在对比要点和对用户最常关心的能力点：

- 定位与架构
  - 飞书助手（aily）: 云端服务，深度集成飞书/Lark，面向企业办公协作与文档处理，强调即开即用和企业级安全。
  - OpenClaw: 本地优先、可离线运行，完全本地化数据控制，开源框架（MIT 许可），更像“数字员工”可跨多平台执行任务。

- 核心能力
  - 飞书助手：专注于飞书工作流的深度集成、文档/表格/幻灯片的智能处理、会议与任务协作管理、权限审计等。
  - OpenClaw：系统级操作能力（直接操作文件/浏览器/代码执行）、多渠道接入（20+ 平台）、技能生态和自定义工作流，强隐私与本地执行。

- 使用体验与门槛
  - 飞书助手：上手简单、零配置、企业级安全，适合非技术用户快速落地。
  - OpenClaw：需要一定技术能力启用与维护，配置和本地部署成本较高，但在隐私与自定义方面更强。

- 成本与生态
  - 飞书助手：通常绑定企业服务，成本对企业友好，云端运维由服务方承担。
  - OpenClaw：完全免费开源，但需自行承担模型 API（如 GPT-4/ Claude）成本与本地硬件/运维。

- 适用场景建议
  - 选择飞书助手（aily）若你是飞书/Lark 用户、需要快速落地的办公协作与文档处理、重视企业级安全且不想自行维护系统。
  - 选择 OpenClaw 若你是技术爱好者、对数据隐私要求极高、需要跨平台系统级自动化、并愿意自行维护与开发。

简要结论
- 对于以飞书办公场景为核心、追求易用与快速落地的企业用户，推介飞书助手（aily 工作助手）。
- 对于追求高度定制、跨平台系统级自动化、并具备技术能力的用户，OpenClaw 提供更强的自定义能力和本地控制。

如需，我可以基于你的具体使用场景（比如你所在行业、是否需要跨平台、对数据隐私的要求、是否愿意自行维护等）给出更精准的推荐。

### [Exa] 飞书长出“龙虾钳”：当AI学会在办公软件里“直接干活” 真正的生产力不在模型的聊天框里，而在你每天用的、沉淀了大量信息的 - 掘金
OpenClaw（小龙虾）正式接入飞书，让 AI 不再只是聊天工具，而是“直接干活”的数字分身，显著提升办公效率。核心要点：

- 关键能力
  - 直接操作飞书内文档、日历、群聊、表格和任务数据（需授权）。
  - 24/7 主动工作、在本地环境运行、可通过飞书接口读取和处理信息。
- 典型应用场景（七大场景中的核心点）
  - 智能会议助手：实时转录、自动提取纪要、标注发言人、生成项目计划草案并落地到飞书文档。
  - 动态知识库助手：在群聊/文档中理解问题，检索并推送最相关的知识片段或答案。
  - 流程审批AI预审：自动核对背景、识别风险，生成带要点的预审报告嵌入审批流。
  - 个性化项目播报：每日/定时自动汇总任务完成率、延期风险、资源占用等，自动发布到项目群。
- 技术与体验提升
  - 飞书 API 调用上限提升：从月1万次提升至月100万次，显著提升个人与小型团队的可用性。
  - 官方插件引入，减少权限授权与信息复制粘贴的痛点，实现更顺畅的上下文读取与沟通。
- 安全与风险提示
  - 插件访问消息、文档、日历等数据，存在信息泄露风险。
  - 官方建议先以个人账号测试使用，暂不以企业账号大规模接入，待进一步的安全隔离能力后再扩展。
- 结论
  - OpenClaw 与飞书的深度整合，将“人找信息、追踪流程”升级为“信息找人、流程驱动”的协同办公新范式，真正把生产力落地在日常使用的办公软件中。

如果你在评测层面关注点包括：实际可用性、授权与安全边界、对日常工作流的具体改进幅度、以及在企业环境中的落地风险，以上要点可作为评测的核心对比维度。

### [Exa] “ 我把OpenClaw接入飞书后，效率直接开挂了！”_配置_实战_文档
Summary:
- 文章介绍将 OpenClaw 集成到飞书以实现 AI 驱动的自动化办公流程，强调可直接操作飞书多维表格、文档、日历、群聊与任务，甚至构建端到端的自动化工作流（如自动创建任务、生成文档大纲、通知负责人、同步日历）。
- 重点是实战课程“OpenClaw×飞书的自动化工作流实战课”，由资深 AI 架构师崔皓授课，声称零基础也能搭建“7×24 小时 AI 虚拟团队”，达到“一人即大厂”的生产力提升。
- 课程内容覆盖从安装配置、模型对接到飞书集成、专属机器人开发的完整流程，提供一步步的演示、实操文档和OpenClaw入门实战文档，强调避免踩坑、节省试错时间。
- 课程结构包括4个学习模块，面向普通办公族和创业者，强调对 Windows/Mac 的跨平台安装、对 DeepSeek 等主流模型对接，以及飞书机器人和插件的全流程配置与安全机制。
- 课程价格为 129.9 元，现有新学员可免费领取课程，且有三节课的免费试学机会。
- 作者与课程讲师崔皓具备丰富的 AI 与分布式架构经验，出版过相关著作，承诺帮助学员快速掌握 OpenClaw 的全流程和飞书整合，提升工作效率。

若你关注的点是 OpenClaw 在飞书中的实际效果、可否实现 AI 办公自动化、以及学习成本与课程价值，上述信息表明课程定位明确、以实战为导向，适合希望通过飞书实现自动化办公的用户与企业团队。

### [Exa] 2026年最值得关注的 AI 工具：OpenClaw 全面评测 - OpenClaw官网中文版
概要要点，聚焦用户查询“OpenClaw 飞书 AI助手 评测”：

- OpenClaw 的核心定位：面向日常工作与生活的强大 AI 助手，强调“实际执行能力”与广泛平台集成。对在飞书等办公协作环境中提升效率尤具潜力。
- 飞书（Feishu）集成：OpenClaw 目前支持超过 20+ 平台，其中包含飞书，允许在熟悉的工作场景中直接调用 AI 助手，减少切换成本；对中国用户尤具价值。
- 功能与性能要点：
  - 功能覆盖：邮件管理、日程协调、信息检索、文件操作、浏览器控制、自动化任务等，且可接入超过200种大模型（含 Claude、GPT、DeepSeek、Gemini，以及 Ollama 本地模型）。
  - 评测亮点：功能完整度高、社区生态强（GitHub 星量和活跃度高），跨平台能力领先。
  - 上手难度：对技术用户友好，但对普通用户需要一定配置与学习；有托管方案（Hostinger、DigitalOcean 等）帮助降低上手门槛。
- 安全与风险：权限广泛带来较高风险，需仔细配置并优先使用可信技能、避免暴露端口、定期更新。存在历史安全漏洞及高风险技能风险的评估要点。
- 费用与性价比：软件免费、按需计费的大模型 API、可选本地化运行；对比订阅制产品，在成本控制与本地数据控制方面具备优势，但初期成本估算较复杂。
- 适用人群与使用建议：  
  - 适合有技术背景、重视数据隐私且需要高效自动化的个人与小团队；对飞书等中国市场场景尤具吸引力。  
  - 初学者或企业核心系统部署需慎重评估安全性与运维能力，宜考虑一键托管方案以降低门槛。

简短结论：如果你的工作流高度依赖飞书和其他协作工具，且希望一个可扩展、可定制的 AI 助手来处理重复任务与信息管理，OpenClaw 是2026年的值得关注之选；但需做好安全配置并对上手成本有所准备。

### [Exa] 2026爆火的OpenClaw（小龙虾）深度测评：普通人的效率神器还是隐形陷阱？ - IT干货
OpenClaw（小龙虾）是一个开源、可自托管的AI智能体框架，主打“指令即执行、全流程自动化”，可在本地、云端或虚拟机部署，普通人无需编程即可用自然语言下达任务。核心优势包括低门槛安装、可扩展的技能包生态（ClawHub 5700+技能包）、以及实现场景级的自动化执行（从文件整理到日程、文档生成、内容创作等多场景）。

就“OpenClaw 飞书 AI助手 评测”这一点而言，值得关注的要点：
- 适用场景与收益：在职场办公、自媒体/内容创作、个体经营等场景中，OpenClaw可自动化重复性任务（如文件整理、报表生成、数据统计、素材管理、自动回复等），有望提升30%-60%的工作效率，尤其对常规、重复性任务帮助显著。
- 使用风险与坑点：高权限全流程执行带来显著安全风险（端口暴露、远程代码执行漏洞、恶意技能包等），指令理解有限可能导致误操作（误删/误传等），并存在隐性成本（需对接大模型API、潜在部署/教程的隐性收费），以及合规风险（数据泄露、账号封禁等）。
- 适配硬件与成本：对硬件要求较低，普通电脑即可运行，Mac Mini并非必需；但要关注潜在的API费用与部署成本。
- 新手使用建议：优先选用一键安装、加强本地与网络安全防护（防火墙、默认端口管理、谨慎下载技能包）、明确场景目标再投入使用，逐步扩展技能以降低风险。

简要结论（与你的“OpenClaw 飞书 AI助手评测”需求相关）：
- 如果你寻求在飞书生态中实现“指令即执行”的办公自动化，OpenClaw可成为提升日常办公与内容创作效率的强大工具，但需谨慎评估安全风险与成本。建议在受控环境下（单机或受信任云环境）先进行小规模试用，逐步引入关键技能包，并对接必要的安全措施与合规审查。

### [Exa] OpenClaw + 飞书集成实战：打造 7×24 小时自动化 AI 助手手把手教你用OpenClaw连接飞书，实现AI - 掘金
Summary for query: "OpenClaw 飞书 AI助手 评测" (OpenClaw + Feishu integration for 7x24 AI assistant)

- What it is: A practical guide (tech tutorial) showing how to deploy an automated, AI-powered assistant inside Feishu using OpenClaw. The assistant runs 7x24, can auto-reply messages, read/write Feishu docs, manipulate multi-dimensional tables, and create tasks from conversations.

- Key benefits highlighted:
  - Significant time savings: manual back-and-forth reduced from days to about 2 hours setup.
  - Outsourced complexity: OpenClaw handles Feishu authentication, message i/o, session/context management, and multi-model AI prompts; you only implement your agent logic.
  - Built-in capabilities: Feishu channel integration, document reading/writing (feishu_doc, feishu_wiki), table operations (feishu_bitable), and knowledge/document context support via MCP tools.

- Why OpenClaw over writing a Feishu bot from scratch:
  - Automates OAuth2/auth, token refresh, error handling, logging, and deployment/maintenance.
  - Provides a decoupled agent model (SOUL.md and AGENTS.md) and built-in session/context management.
  - Simplifies multi-model AI usage and model swapping.

- Prerequisites:
  - Feishu Open Platform account
  - Node.js 18+
  - Cloud server (e.g., 2-core/4G RAM)

- Quick-start steps:
  1) Create Feishu self-built enterprise app; capture AppID and AppSecret; enable messaging, doc, wiki, bitable, etc.; configure event subscriptions (im.message.receive_v1) and webhook URL.
  2) In OpenClaw, add Feishu as a channel with AppID/AppSecret; create agent workspace:
     - Write SOUL.md (agent persona and capabilities)
     - Write AGENTS.md (workflow: identify intents, handle tech Q&A, doc operations via feishu_doc, table ops via feishu_bitable, keep chat concise)
  3) Start/verify gateway (openclaw gateway restart; check feishu: connected).
  4) Practical capabilities:
     - Document ops: read/update knowledge base via feishu_wiki and feishu_doc.
     - Table ops: create/list/update records via feishu_bitable_*.E.g., add bug record or query counts by status.
     - Workflow automation: schedule cron jobs (e.g., daily reports).

- Example interactions:
  - User asks to read a document: agent reads wiki, fetches doc content, returns summary.
  - User asks to update a document: agent locates section, updates content, confirms.
  - User asks to update a table: agent creates or lists records, aggregates results.

- Pitfalls and tips:
  - Ensure proper event subscriptions and webhook URL exposure; use a stable public IP/hostname.
  - Keep SOUL.md and AGENTS.md aligned with desired behaviors; tweak tone and tool

### [Exa] 号称“AI打工人”的OpenClaw值得用吗？_凤凰网
OpenClaw 作为一个“AI打工人/指挥官”工具，在评测中被证明更像任务框架，实际效果高度依赖所接入的大模型能力。核心要点：

- 实测结论：OpenClaw 自身并非强大大模型，而是协调器，负责指令理解、工具调用和流程编排；最终任务成败取决于所接入的大模型性能、稳定性与浏览器/网络操作能力。
- 模型对比结果（综合两轮/多轮测试）：
  - GPT-5-mini、MiniMax-M2.5、智谱GLM-4.7 等表现相对稳定，能完成从本地检索、信息总结、网络搜索、稿件撰写到邮件发送的全流程，且有较少人工干预。
  - 千问Qwen3-Max、月之暗面Kimi-K2.5 等在本地检索和写作上有一定能力，但在网络搜索、邮件发送等环节容易出错或需要人工介入，且某些阶段存在错误或被浏览器控制失败的情况。
- 行业观点与结论：
  - OpenClaw 的生产力价值尚未成熟，更多依赖所接入大模型的能力水平。
  - 对于常规任务，国产大模型（如GLM-4.7、Kimi-K2.5）已具备较好表现，但对于高难度任务仍受制于大模型能力与工具控制稳定性。
  - 专家普遍认为 OpenClaw 需要更强大、稳定的大模型支撑，且当前版本难以作为“可靠生产力工具”全面替代传统生产力工作流，尤其在浏览器自动化和邮件发送等环节容易出错。

对比“OpenClaw + GPT-5-mini”在评测中的表现最好，接近无缝完成全流程；而若以在企业工作流（如飞书/邮件自动化等）中的稳健性为准，仍需谨慎评估接入的本地/国产大模型的稳定性与成本。

如果你的需求聚焦于“OpenClaw 在飞书/邮件场景中的可用性与稳定性”，当前结论是：对于高可靠性工作流，建议优先测试成熟的大模型组合并评估成本/安全性，再决定是否采用 OpenClaw 作为指挥官层的中枢。

### [Exa] 告别 “笨虾”！飞书对接 OpenClaw 全攻略 + 前端角色深度调教，让 AI 助理智商拉满🔥告别笨虾！OpenC - 掘金
Summary:
This article is a practical guide to using OpenClaw (a local AI assistant, nicknamed “Little Lobster”) with Feishu (Lark) to create a highly capable frontend AI helper. It emphasizes choosing the right version (Domestic OpenClaw Chinese版) for seamless Feishu integration, step-by-step setup, and strong role customization to maximize intelligence.

Key takeaways aligned with your query:
- OpenClaw vs Feishu: Domestic/China-tailored OpenClaw is recommended for easy deployment, native Feishu integration, offline operation, and sandboxed data, enabling a smarter Feishu AI assistant without cloud leakage.
- End-to-end Feishu integration (10-minute practical flow): Create a Feishu self-built app, configure permissions and events, connect OpenClaw via WebSocket, and verify with simple tests.
- Role design as the “IQ switch”: The AI’s intelligence is driven by a detailed local Markdown role file. A well-crafted front-end role (template provided) defines identity, capabilities, interaction rules, memory, privacy, and hard constraints to prevent errors or leakage.
- Ready-to-use role template: The article provides a complete, copy-paste template for a Feishu-focused frontend AI assistant with explicit capabilities (frontend tech stack, Feishu doc/drive handling, task extraction, structured output) and safety rules.
- Advanced tuning: Adjusting model parameters (e.g., temperature 0.3, memory, context length) and enforcing strict boundaries improves reliability, prevents hallucinations, and ensures concise, task-focused outputs.
- Memory and governance: The system emphasizes persistent memory of tech stacks and project conventions, zero cloud data leakage, and strict boundaries on non-frontend queries or unsafe content.

How this helps your search for an OpenClaw Feishu AI assistant:
- If you want a smart, enterprise-friendly Feishu AI assistant for frontend work, this guide shows exactly which OpenClaw version to use, how to connect Feishu, and how to tailor the assistant’s role for high productivity.
- It provides a ready-made role template tailored to frontend development, enabling fast onboarding and consistent, high-quality code and document outputs within Feishu.
- The article also highlights best practices for keeping data private and ensuring the assistant stays focused on frontend tasks.

Caveats:
- Steps require admin access to Feishu/Feishu Open Platform and local OpenClaw deployment; ensure compliance with your organization’s IT policy.
- Follow the provided role template carefully; misconfigurations can lead to suboptimal behavior or privacy concerns.

### [Exa] 2026爆火的OpenClaw（小龙虾）深度测评：普通人的效率神器还是隐形陷阱？ - IT干货
Summary:
- OpenClaw, nicknamed “小龙虾,” is an open-source AI agent framework that can autonomously execute full workflows, not just provide ideas. It is self-hostable, works locally or on cloud, and aims to be a low-code, high-automation assistant that can operate apps and manage files via natural language instructions.
- Core strengths relevant to your query:
  - Feeds every day-to-day task into a single automated workflow: document generation, file organization, calendar and communication management, and even some content creation support.
  - Easy onboarding with visual, one-click deployment; integrates with Feishu (Lark), DingTalk, WeChat, and other common tools without extra apps.
  - Large ecosystem via ClawHub with thousands of技能 packages for office, content, data tasks; strong Chinese language support.
  - Practical for individuals and small teams: can automate repetitive office tasks, content planning, and basic digital admin to save 30–60% time on common tasks.
- Feishu AI assistant angle:
  - OpenClaw can be configured to manage routine Feishu/企业微信 workflows: auto-summarize messages, extract action items from chats, auto-create daily/weekly reports, draft and format content, and possibly respond to common inquiries. This can reduce manual triage and routine replies in Feishu channels.
  - Deployment and usage near-term: align OpenClaw with Feishu workstreams by creating skills that parse Feishu messages, fetch files, and trigger Feishu actions (calendars, reminders, messages) via supported connectors.
- Important cautions (risk-aware):
  - Security: OpenClaw requires high system privileges; misconfigurations can expose devices/data. Ensure password/token protection, firewall rules, and monitor for unauthorized access.
  - Reliability: AI interpretation may misexecute commands; verify critical actions (especially deletions, file moves, or data exposure) and implement stopping/verification steps.
  - Costs: While OpenClaw itself is open-source, many workflows rely on external AI/models via APIs with token-based pricing; plan budgets for sustained use.
  - Compliance: Be mindful of data privacy and corporate policy when deploying on work devices or handling sensitive information.
- Practical recommendation for Feishu-focused users:
  - Start with a safe, low-risk workspace: set up OpenClaw on a personal/dev device, configure Feishu-integrations for non-critical tasks (like draft generation, topic suggestion, or non-sensitive scheduling).
  - Gradually expand to more sensitive workflows only after tightening security (passwords, firewalls) and establishing verification prompts before irreversible actions.
  - Explore ClawHub skills that relate to document drafting, scheduling, and data aggregation to build a Feishu-centered automation suite.
- Bottom line: OpenClaw can be a powerful “execution-first” AI assistant in Feishu workflows, enabling hands-off task automation from data gathering to reporting. Use cautious rollout, solid security, and incremental skill adoption to maximize benefits while mitigating risks.

### [Exa] 飞书助手与OpenClaw对比_新浪新闻
Summary:
- This Sina News comparison (as of March 2026) pits Feishu/ Lark’s built-in AI assistant (referred to as aily, 飞书助手) against OpenClaw (nicknamed Xiaolongxia).
- Key differences:
  - Deployment and privacy: aily is cloud-based with enterprise-grade security; OpenClaw is 100% local and fully controllable by the user.
  - Form and scope: aily is a tightly integrated Feishu/Lark workspace assistant focused on document handling, scheduling, and collaboration; OpenClaw is an open-source AI agent framework designed to serve as a “digital employee” with system-level operations and multi-platform reach.
  - Capabilities: aily excels at deep Feishu integration, document/editing automation, meeting and task coordination, and immediate usability; OpenClaw offers system-level file/browser/script control, 20+ channels, multi-step automations via Skills, and strong local execution.
  - Ease of use and cost: aily emphasizes zero-configuration, cloud-based maintenance, and enterprise-grade security (costs largely tied to enterprise services). OpenClaw requires technical setup, local maintenance, and potential API costs for models (e.g., GPT-4), but is free/open-source under MIT.
- Use-case guidance:
  - Choose aily if you are a Feishu/Lark user needing seamless办公协作, rapid deployment, and strong document/workflow integration with enterprise security.
  - Choose OpenClaw if you are a tech-savvy user or developer requiring system-level automation, offline/local data processing, cross-platform reach, and high customization.
- Practical takeaways:
  - If your primary environment is Feishu/Lark and you want an immediately usable, enterprise-ready assistant, aily is likely the better fit.
  - If your priorities include 100% local data, bespoke automation, and open-source flexibility, OpenClaw offers deeper customization potentials.
- The article ends with a quick decision guide: base your choice on your platform, privacy needs, automation depth, and technical capability, and invites user-specific scenario discussion for a tailored recommendation.

### [Exa] 飞书长出“龙虾钳”：当AI学会在办公软件里“直接干活” 真正的生产力不在模型的聊天框里，而在你每天用的、沉淀了大量信息的 - 掘金
OpenClaw 与飞书深度集成将 AI 从“聊天工具”升级为“直接干活的数字分身”。核心点：

- 变革要点：OpenClaw（小龙虾）接入飞书后，AI 能在不再依赖人工搬运的情况下，直接访问和操作你的文档、日历、群聊、知识库等数据，实现“看文档找资料、核对日程、理解上下文、直接执行任务”的能力。
- 典型场景（提升工作流效率的七大场景之一的核心应用）：
  - 智能会议助手：自动实时转录、提炼纪要、区分发言人、生成项目计划草案并直接存入飞书文档。
  - 动态知识库：基于问题自动检索、关联并推送相关文档片段或答案。
  - 流程审批 AI 预审：在审批流中自动核对背景、识别风险、给出带数据摘要的预审报告。
  - 个性化项目播报：自动抓取任务数据与群聊讨论，生成并发布项目动态摘要。
- 技术与体验提升：飞书 API 调用额度提升至每月100万次，提升了对 AI 的支持与响应丝滑度；官方插件解决了读取上下文、权限授权等难题，减少重复拷贝粘贴。
- 安全与使用建议：涉及消息、文档、日历等权限，存在信息泄露风险。宜先用个人账号试用，避免企业账号直接接入，等待更完善的安全隔离后再扩展到企业级使用。

总体评测要点：OpenClaw 使 AI 在办公软件内部“直接干活”，显著提升协同效率和信息可用性，超越仅提供对话能力的局限，成为飞书工作流的智能中枢。潜在风险在于数据权限与隐私，需谨慎部署与分层使用。

### [Exa] 2026年最值得关注的 AI 工具：OpenClaw 全面评测 - OpenClaw官网中文版
Summary:
- OpenClaw is highlighted as a leading AI tool in 2026, praised for broad functionality, deep platform integration (20+ platforms) including WeChat/Feishu, strong community, and flexible cost structure.
- Key strengths: 
  - Functionality: extensive personal/work AI assistant capabilities (email, calendar, search, file ops, browser control, automation, skill expansion).
  - Platform reach: broad cross-platform support, with notable emphasis on Feishu (飞书) and WeChat for Chinese users; supports voice on macOS/iOS/Android and real-time canvas UI.
  - Community: extremely active/open-source ecosystem (high GitHub stars, many contributors, robust Chinese resources).
  - Cost: MIT-licensed, free core software with scalable API/local model options; cost-effective for light to heavy usage.
- Notable caveats:
  - Onboarding: higher barrier for non-technical users; GUI lacking, documentation gaps; homegrown deployment can be technically demanding.
  - Security: significant risk surface due to broad permissions; cautions around CVEs, malicious skills, and exposure of instances; best practices include trusted sources, minimal permissions, and managed hosting.
- For Feishu-specific use: OpenClaw’s Feishu support is a major differentiator, enabling in-app AI automation without extra installs; however, stability may vary with platform changes.
- Recommendation: OpenClaw is worth evaluating if you’re technically inclined, privacy-conscious, and seeking a highly capable, extensible AI assistant that integrates with Feishu/WeChat and other platforms. Consider managed hosting options if you prefer a simpler setup. Not ideal if you require a ready-made, purely GUI-driven experience or have strict enterprise risk controls without dedicated security oversight.

If you want, I can tailor this to a Feishu-focused scenario (e.g., use cases, setup steps, and security considerations) or pull out a quick pros/cons table for decision support.

### [Exa] “ 我把OpenClaw接入飞书后，效率直接开挂了！”_配置_实战_文档
Summary:
The article promotes OpenClaw’s integration with Lark (Feishu) to automate office workflows and boost productivity. Key points for an OpenClaw + Feishu AI assistant review:

- Practical use: Connects OpenClaw to Feishu to control Feishu multi-dimensional tools (spreadsheets, documents, calendars, groups, tasks) and automate end-to-end processes (e.g., on customer submission: create tasks, generate outlines, notify owners, sync with calendar).
- Course offering: Advertises a free, hands-on course “OpenClaw × Feishu Automated Workflows” by AI architect Cui Hao, covering installation, model integration, Feishu integration, and custom robot development; aims to teach non-developers to build a 7x24 AI virtual team without coding.
- Curriculum and format: Four-module structure focusing on core OpenClaw concepts, installation, Feishu practicals, and team setup. Emphasizes practical, step-by-step demonstrations and an accompanying OpenClaw beginner guide.
- Target outcomes: Enables users to deploy a low-cost AI-assisted workflow to reduce manual repetitive tasks, improve efficiency, and achieve “one person, like a big factory” productivity.
- Instructor credibility: Cui Hao is presented as an experienced AI and distributed architecture expert with published works and a large student base; claimed to reduce trial-and-error learning substantially.
- Pricing and access: 129.9 yuan for the course, with some free access for new students; ongoing new content and additional related OpenClaw courses offered.
- Considerations for evaluation:
  - Ease of Feishu integration: The workflow hinges on reliable bridging between OpenClaw and Feishu’s APIs/permissions.
  - Security and governance: Feishu integration requires proper access controls and安全机制; ensure data privacy when automating documents and calendars.
  - Practical ROI: Potential to significantly reduce repetitive tasks, but effectiveness depends on correct workflow design and model compatibility.

If you’re evaluating OpenClaw as an AI assistant for Feishu, this resource highlights a concrete application path, hands-on training, and a claim of substantial productivity gains, while noting the need to assess integration reliability, costs, and customization for your specific workflows.

### [Exa] OpenClaw 很火,但真正适合多数人的,可能是 ToDesk 这只更好上手的“龙虾”
- 基于OpenClaw的“龙虾”热潮，本文评测对比了 OpenClaw 与 ToDesk 的 ToClaw，聚焦普通办公用户的上手度与实际工作场景适用性。
- 主要结论：ToClaw 作为 ToDesk AI 的一部分，提供“现成即可用”的桌面任务入口，免安装、免部署，直接在 ToDesk 左侧入口即可使用，强调任务导向而非纯聊天体验，适合大多数办公用户。
- 与 OpenClaw 的对比要点：
  - 上手与集成：ToClaw 已封装在 ToDesk 中，界面直观、可直接开始工作；OpenClaw 需要安装、配置、运行环境准备，门槛较高。
  - 使用定位：ToClaw 注重任务执行与工作流管理（热点分析、投研助理、智能文档整理、定时任务、记忆与个性化等），而不是仅提供对话能力。
  - 技能体系：ToClaw 提供多类可调用的桌面技能（Word/Excel/PDF/PowerPoint 等文档处理、Agent Browser 等），并标注安全合规验证，提升在企业与团队场景的可信度。
  - 长期使用能力：具备定时任务与记忆/个性化设置，支持持续信息汇总与长期协作，且具备企业微信等 IM 机器人接入的潜力，利于团队协同。
- 适合人群：
  - OpenClaw 仍适合喜欢自有环境控制、追求高自由度和开源社区的技术玩家。
  - ToClaw 更适合需要高效办公自动化的普通用户、远程协作与多设备工作流的场景，尤其在企业/团队环境中价值更明显。
- 结论：ToClaw 并非追求“最强炫技”的龙虾，而是更接近多数人真实工作需求的“现成可用”的桌面 AI 助手，更可能被广泛养成使用。对于需要直接、稳定工作流的用户，ToClaw 值得优先尝试。

### [Exa] OpenClaw + 飞书集成实战：打造 7×24 小时自动化 AI 助手手把手教你用OpenClaw连接飞书，实现AI - 掘金
Summary for query: "OpenClaw 飞书 AI助手 评测 analysis review"

- The article is a practical, hands-on guide to building a 7x24 automated AI assistant inside Feishu (飞书) using OpenClaw.
- Key claim: OpenClaw decouples AI logic (Agent) from Feishu channel, enabling near plug-and-play automation with much faster setup than building a Feishu bot from scratch.
- Benefits highlighted over native Feishu bot development:
  - Significantly reduced development time (about 2 hours vs 1-2 weeks).
  - Automatic OAuth2/认证 management, session/context handling, multi-model AI integration, and built-in doc/table operations.
  - Simplified deployment/maintenance with a single command.
- Prerequisites:
  - Feishu Open Platform account, Node.js 18+, a cloud server (2-core/4GB recommended).
- Step-by-step workflow:
  1) Create a Feishu self-built application; obtain App ID and App Secret; set necessary permissions (im:chat, im:message:send_as_bot, im:message, drive:drive, wiki:wiki, docs:doc, bitable:app); configure event subscriptions (im.message.receive_v1) and webhook URL.
  2) In OpenClaw, add a Feishu channel with your App ID/Secret; define an Agent workspace with Markdown files (SOUL.md for persona/abilities; AGENTS.md for workflow).
  3) Start the OpenClaw gateway and verify Feishu channel connection (feishu: connected).
- Practical capabilities demonstrated:
  - Read/write Feishu documents (feishu_doc, feishu_wiki) based on natural-language prompts.
  - Read/write knowledge base items and update documents via Agent.
  - Multi-dimensional table operations (feishu_bitable_create_record, feishu_bitable_list_records) to create or query records (e.g., Bug tracking).
  - Use of Cron-like scheduling to automate workflows (e.g., daily reports).
- Example agent behavior:
  - Intent detection: tech Q&A, document ops, table ops, or chit-chat.
  - Execute tasks via dedicated Feishu tools; provide concise, precise responses; avoid hallucinations.
- Practical notes:
  - The article includes concrete code/config snippets to patch OpenClaw config with Feishu channel, and to create workspace files (SOUL.md, AGENTS.md).
  - Emphasizes avoiding heavy boilerplate by treating Feishu as a channel and focusing on Agent logic.
- Verdict: Suitable for teams or individuals who want an autonomous, always-on AI assistant in Feishu with document and data manipulation capabilities, without the overhead of building and maintaining a full Feishu bot stack.

## 搜索结果 (共 28 条)

### [1] 告别 “笨虾”！飞书对接 OpenClaw 全攻略 + 前端角色深度调教，让 AI 助理智商拉满🔥告别笨虾！OpenC - 掘金 [EXA]
- URL: https://juejin.cn/post/7618033544104443956
- 相关度: 1.00
- 搜索词: OpenClaw 飞书 AI助手 评测
- 发布日期: 2026-03-18T01:33:14.000Z

告别 “笨虾”！飞书对接 OpenClaw 全攻略 + 前端角色深度调教，让 AI 助理智商拉满🔥告别笨虾！OpenC - 掘金

# 告别 “笨虾”！飞书对接 OpenClaw 全攻略 + 前端角色深度调教，让 AI 助理智商拉满🔥

[程序员小九_牛牛](https://juejin.cn/user/3870732582396775/posts)

2026-03-18 7 阅读11分钟

## 告别笨虾！OpenClaw小龙虾+飞书对接全流程+角色调教，让AI智商拉满

哈喽各位前端小伙伴，最近本地AI工具OpenClaw（圈内昵称“小龙虾”）简直是前端提效神器，身边不少同学都部署了自用。但我发现一个普遍问题：同样是用小龙虾，有的人的AI能在飞书里写代码、理需求、查Bug，全自动协作；有的人的小龙虾却答非所问、只会简单聊天，完全不够聪明。

其实小龙虾本身不笨，核心问题就两个：没打通飞书这类协作场景，局限在本地孤立使用；角色设定太敷衍，没做专业调教和规则约束。加上之前很多人纠结国内外版本差异，选错版本也直接影响使用体验。

这篇文章就一次性讲透：国内外小龙虾核心差异速览→飞书对接OpenClaw全步骤→前端专属角色设定规则+模板→让小龙虾彻底变聪明的进阶技巧，全程干货无废话，新手跟着做就能上手，做完直接拥有专属前端智能助理～

---

### 一、先理清：国内外OpenClaw（小龙虾）核心差异（选对版本是前提）

想让小龙虾变聪明，第一步得选对版本，国外原版和国内魔改版的适配性、易用性天差地别，尤其对接飞书这种国内平台，版本选错直接寸步难行，先给大家精简总结核心差异：

#### 1. 国外原版OpenClaw

完全开源、无权限限制，但部署门槛极高、中文适配差、飞书无原生对接，需要科学上网，命令行操作复杂，不适合新手，更适合资深极客研究底层，日常开发和对接飞书直接劝退。

#### 2. 国内版小龙虾（推荐）

基于原版内核深度本土化改造，一键部署、中文优化拉满、原生适配飞书/钉钉，内置前端专属模型，无外网要求，合规安全，新手10分钟就能上手，对接协作平台、调教智能体首选国内版（CoPaw、智谱AutoClaw都可）。

关键结论：想对接飞书、轻松把小龙虾养聪明，直接选国内版，不用折腾国外原版，后续所有操作均基于国内版展开，适配绝大多数前端同学！

---

### 二、10分钟无缝对接：OpenClaw小龙虾×飞书实战教程

小龙虾孤立在本地，永远只能做简单问答；对接飞书后，才能接入团队场景、读取文档、参与协作，聪明度直接翻倍。全程步骤清晰，无需复杂开发，跟着做就行。

#### 前置准备

- 稳定国内网络，无需科学上网
- 飞书企业/团队版（个人版无法创建自建应用，需找管理员开通权限）
- 已完成国内版OpenClaw部署，网关正常运行，本地可正常调用

#### Step1：飞书开放平台创建自建应用

1. 左侧应用能力→添加能力，勾选机器人并确认，开启机器人交互能力
2. 创建完成后，在凭证与基础信息里，复制App ID和App Secret，后续配置必备
3. 登录 [飞书开放平台](https://link.juejin.cn/?target=https%3A%2F%2Fopen.feishu.cn%2Fapp)，点击创建企业自建应用，填写基础信息：应用名称填「OpenClaw前端AI助理」，描述填“本地AI智能助理，支持飞书内代码生成、需求梳理、Bug调试”，上传小龙虾专属头像提升辨识度

#### Step2：飞书权限与事件订阅配置

1. 进入事件订阅，连接方式选WebSocket（最稳定，无公网IP也能用），添加事件im.message.receive_v1并启用，不用填写请求URL
2. 提交权限申请，企业自建应用一般秒批，无需等待
3. 进入权限管理→批量导入权限，粘贴以下核心权限，覆盖消息、文件、文档读取，缺一不可：` { `` "scopes": { `` "tenant": [ `` "im.message", `` "im.message:send_as_bot", `` "contact:user.id:readonly", `` "drive.file:read", `` "drive.file:write" `` ] `` } ``}`

#### Step3：OpenClaw侧配置（新手首选命令行）

1. 配置完成后重启网关生效：`openclaw gateway restart`
2. 按提示依次选择：通道类型选Feishu(飞书)，粘贴复制的App ID和App Secret，连接模式选WebSocket，群聊策略设为需@才响应，绑定默认代理main
3. 打开终端，执行通道添加命令：`openclaw channels add`

#### Step4：验证对接成功

查看终端日志，出现feishu plugin loaded successfully即为配置成功；飞书搜索机器人名称，单聊发“你好”或群聊@机器人，收到回复就代表对接完成，接下来就可以开始调教角色啦。

---

### 三、角色设定核心：小龙虾的“智商开关”，决定聪明程度

为什么你的小龙虾不够聪明？90%的原因是用了默认角色，没有专属设定。OpenClaw的角色本质是本地Markdown文件，定义了AI的身份、能力、规则、记忆，相当于给AI立人设，设定越精准，小龙虾越聪明。

#### 1. 角色核心特点（必懂）

- 场景化适配：针对飞书协作优化，区分单聊和群聊交互模式，不刷屏、不打扰
- 持久记忆：能记住你的技术栈、代码风格、项目规范，越用越贴合你的需求
- 规则强约束：设定行为红线，避免AI答非所问、编造内容、乱输出代码
- 可编辑可定制：纯Markdown格式，不用懂复杂代码，随时修改调整，适配自己的开发习惯
- 本地私有化：角色文件存在本地，不会上传云端，数据绝对安全，不会泄露业务代码和项目信息

#### 2. 角色文件存放路径

国内版图形化界面可直接新建角色；命令行版路径：`~/.openclaw/agents/frontend-feishu-assistant.md`，新建文件粘贴模板即可，修改后务必重启网关生效。

#### 3. 【可直接复制】前端专属飞书角色模板

直接粘贴使用，适配飞书协作、前端开发全场景，不用自己从零编写，复制即用，新手也能拥有高智商AI：

```
# 角色名称：飞书前端专属AI助理（OpenClaw高智商版）
## 一、基础身份设定
- 核心定位：10年资深前端开发工程师，本地私有化部署，飞书团队协作专属智能体，数据零泄露
- 精通技术栈：Vue3/React/TypeScript、微信小程序、Tailwind CSS、Element Plus/Ant Design、Pinia/Redux
- 交互语气：专业严谨、简洁干练，拒绝废话和幻觉，输出结构化（清单/代码块/表格），代码带完整注释
- 飞书交互规则：单聊自动响应，群聊必须@才回复，不主动打扰，不泄露团队任何业务信息

## 二、核心能力范围（决定聪明度）
### 前端开发核心能力
1. 快速生成可直接复用的Vue3/React/TS/小程序组件、页面、工具函数，严格遵循ESLint规范
2. 精准定位JS/TS语法报错、浏览器兼容性问题、页面性能瓶颈、样式冲突，给出可直接复制的修复方案
3. 重构冗余代码，提取自定义Hooks、公共工具类，优化页面渲染逻辑，提升代码复用性
4. 生成接口请求封装、路由配置、状态管理代码，适配主流前端工程化项目
5. 编写开发文档、接口说明、README，规范项目文档输出

### 飞书协作专属能力
1. 读取飞书文档、多维表格、群文件，自动提取开发需求、原型要点、接口规范
2. 整理飞书群内需求，输出结构化任务清单、优先级排期，同步开发进度
3. 解析飞书内原型图、接口文档，快速生成对应前端代码框架
4. 长内容分条呈现，适配飞书聊天窗口，不刷屏、易阅读

## 三、硬性行为约束（红线规则，防止AI失控）
1. 仅处理前端开发相关需求，非前端问题礼貌引导至对应负责人，不跨界应答
2. 生成代码必须标注：适配浏览器版本、依赖库版本、需人工校验兼容性与安全性
3. 严格保护数据隐私，绝不泄露用户代码、项目隐私、团队信息，所有数据本地存储
4. 不确定的问题绝不编造，主动提示补充需求细节，拒绝AI幻觉
5. 禁止生成违规、恶意代码，坚守开发规范与安全底线
6. 单条回复控制长度，复杂内容拆分发送，适配飞书阅读体验

## 四、智能参数配置（提升智商关键）
- 温度值（Temperature）：0.3（数值越低越严谨，代码场景首选，避免随机幻觉）
- 重复惩罚：1.1（避免重复输出相同内容，提升回答简洁度）
- 最大上下文长度：12K（支持长文档、多轮对话记忆，理解复杂需求）
- 绑定模型：Qwen2.5-Code、DeepSeek-Coder（前端专属国产模型，代码生成更精准）

## 五、记忆机制（越用越聪明）
1. 永久记忆用户常用技术栈、代码风格、项目规范、常用组件库偏好
2. 记录历史需求与解决方案，同类需求自动匹配最优方案，无需重复说明
3. 支持手动修正记忆内容，及时更正AI错误认知，保证输出精准度

```

---

### 四、进阶技巧：让小龙虾从“能用”变“好用”，智商持续拉满

完成对接和角色设定，小龙虾已经能正常使用，但想让它更聪明、更贴合你的需求，这几个进阶技巧一定要做，做完直接提升一个档次：

#### 1. 模型调优：选对前端专属模型

别用通用大模型，换成Qwen2.5-Code、DeepSeek-Coder这类前端代码专属模型，中文理解和代码生成能力碾压通用模型，语法更准、注释更全、适配前端规范，直接解决答非所问问题。

#### 2. 优化提示词：指令越细，输出越准

别发模糊指令，比如“写个登录页”，换成精准指令：生成Vue3+TS+Pinia登录页面，包含手机号密码登录、图形验证码、表单校验，适配移动端，用Element Plus，带完整注释，符合ESLint规范，AI输出直接能用，不用反复修改。

#### 3. 开启专属技能插件

在OpenClaw配置文件中开启代码调试、飞书文档解析、文件操作插件，让AI不仅能生成代码，还能在线调试、读取飞书文件，变成真正的全能助理，而不是单纯的问答工具。

#### 4. 定期“喂养”记忆

把项目规范、常用组件库、团队开发准则，手动添加到角色记忆模块，AI会自动学习，后续生成代码完全贴合你的项目要求，越用越顺手，智商持续提升。

#### 5. 区分场景使用

单聊用私人模式，记录个人开发习惯；群聊仅@响应，不刷屏，专注处理团队需求，不同场景各司其职，使用体验翻倍。

---

### 五、常见问题避坑（新手必看）

- 读取飞书文件失败：检查飞书文档权限是否开启，确认机器人有文件读取权限
- AI还是不够聪明：降低Temperature值至0.1-0.3，更换前端专属模型，优化指令细节
- 角色设定不生效：修改文件后必须重启网关，检查Markdown语法是否有误
- 飞书机器人不回复：检查应用是否发布、权限是否完整、网关是否重启，群聊必须@机器人

---

### 六、总结

OpenClaw小龙虾从来都不是“笨”，而是没选对版本、没对接协作场景、没做好角色调教。对于咱们前端开发者来说，选国内版+10分钟对接飞书+复制前端专属角色模板+简单调优，就能彻底告别“人工智障”，拥有一个7×24小时在线、懂前端、会协作、安全私密的专属AI助理。

不管是日常写代码、调试Bug，还是飞书团队协作、梳理需求，都能大幅提升效率，新手也能轻松上手。赶紧动手试试，把你的小龙虾养得聪明又好用～

文末互动：大家用小龙虾遇到过什么问题？评论区留言，我们一起来调教属于自己的小龙虾！

---

### [2] OpenClaw  最新保姆级飞书对接指南教程 搭建属于你的 AI 助手 - JaguarJack - 博客园 [TAVILY]
- URL: https://www.cnblogs.com/catchadmin/p/19592309
- 相关度: 1.00
- 搜索词: OpenClaw 飞书 AI助手 评测 practical guide tutorial

└─────────────────┴─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘` [...] 其他平台安装方式请参考OpenClaw 安装文档 (原 Clawdbot)

你会看到如下

 `🦞 OpenClaw Installer
Siri's competent cousin.
✓ Detected: linux
✓ Node.js v22.22.0 found
✓ Git already installed
→ Installing OpenClaw 2026.2.6-3...
✓ OpenClaw installed
🦞 OpenClaw installed successfully (2026.2.6-3)!
Home sweet home. Don't worry, I won't rearrange the furniture.
Starting setup...
🦞 OpenClaw 2026.2.6-3 (85ed6c7) — curl for conversations.
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██░▄▄▄░██░▄▄░██░▄▄▄██░▀██░██░▄▄▀██░████░▄▄▀██░███░██
██░███░██░▀▀░██░▄▄▄██░█░█░██░█████░████░▀▀░██░█░█░██
██░▀▀▀░██░█████░▀▀▀██░██▄░██░▀▀▄██░▀▀░█░██░██▄▀▄▀▄██
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
🦞 OPENCLAW 🦞
┌ OpenClaw onboarding`

如果首次安装，时间会很长，需要耐心等待。  
如果最后输出如下内容：

`→ npm install failed; cleaning up and retrying...` [...] 如果没有错误的话，选择飞书通道之后，应该是下面的输出

 `Select a channel
│ Feishu/Lark (飞书)
│
◇ Feishu credentials ──────────────────────────────────────────────────────────────╮
│ │
│ 1) Go to Feishu Open Platform (open.feishu.cn) │
│ 2) Create a self-built app │
│ 3) Get App ID and App Secret from Credentials page │
│ 4) Enable required permissions: im:message, im:chat, contact:user.base:readonly │
│ 5) Publish the app or add it to a test group │
│ Tip: you can also set FEISHU_APP_ID / FEISHU_APP_SECRET env vars. │
│ Docs: feishu │
│ │
├───────────────────────────────────────────────────────────────────────────────────╯
│
◆ Enter Feishu App ID
│ _ # 输入 App ID
└`

---

### [3] 35 万 Star 的 OpenClaw：5 分钟部署你的私人 AI 助手，直连飞书 - iTech - 博客园 [TAVILY]
- URL: https://www.cnblogs.com/itech/p/19862053
- 相关度: 1.00
- 搜索词: OpenClaw 飞书 AI助手 评测

或者用 npm 手动装：

`npm install -g openclaw@latest`

如果你想从源码编译：

`git clone 
cd openclaw
pnpm install
pnpm ui:build
pnpm build`

## 运行 Onboard 向导

安装好之后，运行 onboard 命令：

`openclaw onboard --install-daemon`

这个向导会引导你完成三件事：

`18789`

整个过程 2 分钟左右。

向导结束后，确认 Gateway 在跑：

`openclaw gateway status`

你应该能看到 Gateway 监听在 `ws://127.0.0.1:18789`。

`ws://127.0.0.1:18789`

打开 Web 控制台：

`openclaw dashboard`

浏览器会弹出 Control UI，在聊天框里发一条消息试试。如果 AI 回复了，说明基础配置没问题，可以继续接入飞书了。

## 接入飞书频道

飞书频道从 OpenClaw `2026.4.10` 版本开始正式可用。先确认版本：

`2026.4.10`
`openclaw --version`

如果版本太旧，升级一下：

`openclaw update`

### 快速对接（推荐）

OpenClaw 提供了一个交互式向导，一条命令搞定飞书接入：

`openclaw channels login --channel feishu`

运行后会弹出一个二维码，用飞书 App 扫码就行。扫码过程中 OpenClaw 会自动帮你：

扫码完成后，重启 Gateway：

`openclaw gateway restart`

去飞书里找到你的机器人，发条消息。如果收到回复，恭喜你，搞定了。 [...] `chat_id`

### 流式回复

飞书支持通过交互式卡片实现流式输出，看着像 ChatGPT 那种一个字一个字蹦出来的效果：

`{
 "channels": {
 "feishu": {
 "streaming": true,
 "blockStreaming": true
 }
 }
}`

默认就是开启的。如果不需要，设成 `false` 即可。

`false`

## 实际使用体验

搭好之后，我在飞书里跟它聊了一下午。几个印象深的点：

响应速度：因为 Gateway 跑在本地，飞书消息 → Gateway → LLM API → 飞书，整个链路延迟主要取决于模型 API。用 Claude 3.5 Sonnet 的话，首 token 大概 1-2 秒，流式输出体验很流畅。

多渠道同步：我同时把 Telegram 也接上了，两个平台的对话是隔离的（不同 session），但底层跑的是同一个 Gateway。这意味着我换设备聊天，上下文不会串。

数据自主：所有对话历史、配置文件都在本地 `~/.openclaw/` 目录下。不用担心聊天记录被第三方拿到。

`~/.openclaw/`

常用命令（在飞书里直接发文字即可）：

| 命令 | 功能 |
 --- |
| `/status` | 查看机器人状态 |
| `/reset` | 重置当前会话 |
| `/model` | 查看或切换 AI 模型 |

`/status`
`/reset`
`/model`

一个实用的场景：把 OpenClaw 的 Gateway 跑在一台小 Linux 服务器上（比如家里的树莓派或云主机），然后通过 Tailscale 从外面安全访问。这样你的 AI 助手就是 7x24 在线的，手机上的飞书随时能用。 [...] 去飞书里找到你的机器人，发条消息。如果收到回复，恭喜你，搞定了。

### 手动配置（备选）

如果自动向导不好使，可以手动配置。在飞书开放平台创建一个自建应用后，编辑 OpenClaw 配置文件（通常在 `~/.openclaw/config.json`）：

`~/.openclaw/config.json`
`{
 "channels": {
 "feishu": {
 "enabled": true,
 "domain": "feishu",
 "connectionMode": "websocket",
 "accounts": {
 "default": {
 "appId": "cli_xxxxxxxxxxxx",
 "appSecret": "your_app_secret_here"
 }
 }
 }
 }
}`

配置说明：

| 字段 | 说明 |
 --- |
| `domain` | 国内飞书写 `feishu`，海外 Lark 写 `lark` |
| `connectionMode` | 推荐用 `websocket`（长连接），也可以用 `webhook` 模式 |
| `appId` / `appSecret` | 飞书开放平台创建应用后获取 |

`domain`
`feishu`
`lark`
`connectionMode`
`websocket`
`webhook`
`appId`
`appSecret`

然后在飞书开放平台的应用配置里：

`im.message.receive_v1`
`im:message`
`im:message:send_as_bot`

重启 Gateway 生效：

`openclaw gateway restart`

## 飞书安全与权限配置

---

### [4] 全网最详细！OpenClaw 接入飞书十步法！保姆级指南 - 腾讯云 [TAVILY]
- URL: https://cloud.tencent.com/developer/article/2649054
- 相关度: 1.00
- 搜索词: OpenClaw 飞书 AI助手 评测 practical guide tutorial

## 全网最详细！OpenClaw 接入飞书十步法！保姆级指南，零基础也能轻松上手。看完还搞不定？请来找我

# 全网最详细！OpenClaw 接入飞书十步法！保姆级指南，零基础也能轻松上手。看完还搞不定？请来找我

作者头像

🚩 2026 年 「术」系列实战文档 X 篇原创计划 第 20 篇 OpenClaw 最佳实战「2026」系列 第 9 篇

大家好，欢迎来到 术哥无界 ShugeX ｜ 运维有术。
我是术哥，一名专注于 AI编程、AI智能体、Agent Skills、MCP、云原生、Milvus 向量数据库的技术实践者与开源布道者！
Talk is cheap, let's explore。无界探索，有术而行。

你在工作中一定遇到过这些情况：

场景一：

你在出差路上，突然收到飞书消息——客户问："你们新项目的架构方案准备好了吗？能先发个版本文档看看吗？

"以前的你会怎么办？找个地方停下来，打开电脑，连上网络，启动 IDE 或文档编辑器，或者打开 AI 工具生成方案，然后再发送回去。至少要半小时，而且路上可能还没法操作。

现在，你只需要拿出手机，在飞书里给 AI 助手发条消息：帮我生成一个新项目的技术架构方案，包括技术选型、模块划分和部署方案，三分钟后，一份完整的方案就发到客户邮箱了。

场景二：

再比如，你在地铁上，飞书群里同事正在讨论一个复杂的代码 Bug，大家争论不休。你拿出手机，直接在群里 @AI 助手：分析一下这段代码为什么会报错，AI 立刻给出问题定位和修复建议，讨论瞬间有了突破。

这些场景你是不是也经常遇到？我说的处理方法看起来是不是很酷？而这一切，通过飞书 + OpenClaw 就能轻松实现。

OpenClaw 是什么？ [...] OpenClaw 是什么？

OpenClaw 是一个自托管的 AI 网关，说白了，就是一座"桥梁"，把飞书和 AI 编程助手（比如 Claude Code、OpenCode、Codex 等）连接起来。你只需要在自己的电脑或服务器上运行 OpenClaw 网关进程，就能在飞书里直接跟 AI 助手对话。

我平时用它做什么？

OpenClaw 有什么特点？

我觉得最爽的地方：不用守着电脑了

以前，很多工作必须坐在电脑前才能完成：写代码、查文件、生成文档、Review 代码……现在，通过飞书 + OpenClaw，我在任何地方、任何设备上都能做这些事。

出差路上写个项目方案，没问题。地铁上解决个代码 Bug，可以。咖啡厅里审查代码，都行。

飞书不再只是个聊天工具，变成了一个能随时访问 AI 的工作空间。AI 就在飞书里，不管我在哪，都能让它帮点忙。

听起来很棒吧？但你可能担心：对接过程一定很复杂吧？

别担心，我踩过所有坑，总结了一套十步法，把配置过程写得明明白白。这篇保姆级教程，每个步骤，每个点击都有图有说明，保证你跟着做就能成功！

选型说明

新版本的 OpenClaw v2026.2.3 官方已经集成了飞书，但我在测试过程中发现了一些问题，所以暂时还是推荐使用社区开源版。这个版本经过了社区的充分验证，稳定性更好。

社区开源版地址：`

`

### 第一步：登录飞书开发者后台

首先，我们需要到飞书平台创建自己的机器人来接入 OpenClaw。

飞书开放平台地址：

⚠️ 如果你还没有飞书账号，需要先注册一个账号才能继续。

点击右上角的「开发者后台」按钮进入：

飞书开放平台-02-03-2026_10_49_PM

### 第二步：创建应用

进入开发者后台后，点击「创建应用」按钮，开始创建你的飞书机器人应用： [...] 发送图片失败示例：

飞书-ScreenShot_2026-02-07_094618_167

### 写在最后

恭喜你！通过这篇保姆级教程，你已经成功将 OpenClaw 接入飞书，拥有了专属的 AI 助手！

你可以用它做什么？

已知问题和解决方案

`im:resource`

未完待续

我还在持续研究 OpenClaw 与飞书深度整合的最佳实践，包括：

如果你在使用过程中遇到任何问题，欢迎在评论区留言，我们一起探讨解决方案！

好啦，谢谢你观看我的文章，如果喜欢可以点赞转发给需要的朋友，我们下一期再见！敬请期待。

本文分享自 运维有术 微信公众号，前往查看

如有侵权，请联系 cloudcommunity@tencent.com 删除。

本文参与 腾讯云自媒体同步曝光计划  ，欢迎热爱写作的你一起参与！

### 社区

### 活动

### 圈层

### 关于

### 腾讯云开发者

扫码关注腾讯云开发者

扫码关注腾讯云开发者

领取腾讯云代金券

### 热门产品

### 热门推荐

### 更多推荐

Copyright © 2013 - 2026 Tencent Cloud. All Rights Reserved. 腾讯云 版权所有

深圳市腾讯计算机系统有限公司 ICP备案/许可证号：粤B2-20090059粤公网安备44030502008569号

腾讯云计算（北京）有限责任公司 京ICP证150476号 |  京ICP备11018762号

Copyright © 2013 - 2026 Tencent Cloud.

All Rights Reserved. 腾讯云 版权所有

---

### [5] OpenClaw接入飞书教程：技术小白必备 - 知乎 [TAVILY]
- URL: https://zhuanlan.zhihu.com/p/2015479154439627504
- 相关度: 1.00
- 搜索词: OpenClaw 飞书 AI助手 评测 practical guide tutorial

OpenClaw接入飞书教程：技术小白必备

# OpenClaw接入飞书教程：技术小白必备

海鸟科技

在 AI 工具迭代速度飞快的当下，能真正落地到工作场景的本地 AI 助手，正成为越来越多人的刚需。想象这样的画面：你在飞书群里发送一句 “帮我整理本周会议纪要，提取行动项并生成待办清单”，电脑端的 AI 助手自动读取文档、筛选关键信息、排版汇总，最后直接发回整理结果；或是睡前在飞书留言 “明天上午 9 点提醒我提交运营岗位简历，附带修改后的版本”，第二天一早准时收到提醒，连电脑都不用主动打开。

这种能理解自然语言、执行具体任务、对接日常办公工具的 AI 助手，早已不是科幻场景。

OpenClaw 作为开源 AI 智能体网关，凭借 “本地优先、多平台接入、自主执行任务” 的核心优势，迅速在技术圈走红。它能帮你处理文件管理、浏览器自动化、数据汇总、定时任务等繁杂工作，相当于拥有了一个 24 小时在线的私人数字员工。

今天，我们就从 OpenClaw 的核心逻辑出发，拆解它的部署与飞书接入流程，帮你快速拥有属于自己的办公 AI 助手。

EasyClaw | 您的零配置桌面端AI智能体（基于OpenClaw）

## 一、为什么选择 OpenClaw？核心优势与场景适配

要理解 OpenClaw 的价值，首先要分清它和传统 AI 工具的本质区别。传统聊天 AI 只能提供信息参考，无法执行实际操作；而 OpenClaw 是能落地执行任务的智能网关。 [...] 代码如下：⬇️

注意：代码出现格式错误，确认一下是不是创建成“商店应用”了

`{
"scopes": {
"tenant": [
"aily:file:read",
"aily:file:write",
"application:application.app_message_stats.overview:readonly",
"application:application:self_manage",
"application:bot.menu:write",
"cardkit:card:write",
"contact:user.employee_id:readonly",
"contact:contact.base:readonly",
"corehr:file:download",
"docs:document.content:read",
"event:ip_list",
"im:chat",
"im:chat.access_event.bot_p2p_chat:read",
"im:chat.members:bot_access",
"im:message",
"im:message.group_at_msg:readonly",
"im:message.group_msg",
"im:message.p2p_msg:readonly",
"im:message:readonly",
"im:message:send_as_bot",
"im:resource",
"sheets:spreadsheet",
"wiki:wiki:readonly"
],
"user": ["aily:file:read", "aily:file:write", "im:chat.access_event.bot_p2p_chat:read"]
}
}` [...] 从对比可以看出，EasyClaw 没有弱化 OpenClaw 的核心功能，反而通过简化部署流程、适配国内环境，让更多人能轻松使用 OpenClaw 的强大能力。对于国内用户来说，EasyClaw 是比 OpenClaw 更适配、更易上手的选择，尤其适合运营岗位、职场新人、非技术背景的办公人群。

海鸟科技

---

### [6] OpenClaw+飞书项目：AI驱动的项目管理工具让你的效率提升10倍！ - 飞书官网 [TAVILY]
- URL: https://www.feishu.cn/content/article/7629266824445578468
- 相关度: 1.00
- 搜索词: OpenClaw 飞书 AI助手 评测

# OpenClaw+飞书项目：AI驱动的项目管理工具让你的效率提升10倍！

以下内容由 AI 匹配目标关键词，结合飞书知识库智能生成，若对内容有疑问可联系我们 [...] |  |  |  |  |  |
 ---  --- 
| 对比维度​ | MCP (模型上下文协议)​ | API (应用程序接口)​ | 浏览器操作 (Browser Automation)​ | CLI（命令行调用）​ |
| 交互核心​ | 以"上下文-工具"为核心，关注多轮交互连贯性​ | 以"参数-功能"为核心，关注单次调用执行结果​ | 以"视觉-操作"为核心，模拟截图、识别、点击​ | 以 「命令 - 参数 - 执行」 为核心，面向脚本化、批量任务​ |
| 工具发现​ | ✅ 动态自描述，实时查询工具列表与参数规范​ | ❌ 静态预定义，需查阅文档获取接口信息​ | ❌ 需人工分析页面结构​ | ⚠️ 半动态，可通过 --help 查询，但需人工整理命令规范​ |
| 稳定性​ | ⭐⭐⭐⭐⭐ 高（Schema 约定，不受 UI 变化影响）​ | ⭐⭐⭐⭐ 较高（接口稳定即可）​ | ⭐⭐ 低（依赖 DOM 结构，UI 变化易失效）​ | ⭐⭐⭐⭐⭐ 极高（命令稳定，与界面无关，几乎不受版本视觉影响）​ |
| 准确性​ | ⭐⭐⭐⭐⭐ 98%+（结构化工具调用）​ | ⭐⭐⭐⭐ 高（精确参数传递）​ | ⭐⭐⭐ 中等（视觉识别存在误差）​ | ⭐⭐⭐⭐⭐ 99%+（纯文本结构化执行，无识别误差）​ |
| Token 消耗​ | ⭐⭐⭐⭐⭐ 极低（20-100 tokens/次）​ | ⭐⭐⭐⭐ 低（精简数据交换）​ | ⭐⭐ 极高（2000+ tokens/次，含截图解析）​ | ⭐⭐⭐⭐⭐ 极低（纯命令文本，50-150 tokens / 次）​ |
| 响应速度​ | ⭐⭐⭐⭐⭐ 快（直接函数调用）​ | ⭐⭐⭐⭐⭐ 快（毫秒级响应）​ | ⭐⭐⭐ 较慢（页面渲染+截图+识别）​ | ⭐⭐⭐⭐⭐ 极快（系统级调用，无渲染开销）​ | [...] | 第三方配合度​ | ⚠️ 需要目标系统主动注册 MCP 工具​ | ⚠️ 需要目标系统开放 API​ | ✅ 不需要网站任何配合​ | ⚠️ 需要目标系统提供 CLI 工具 / 命令入口，通常需本地安装或服务端支持​ |

---

### [7] 一文完全搞懂OpenClaw（Clawdbot）附飞书对接教程！ - Lark [TAVILY]
- URL: https://www.feishu.cn/content/article/7602519239445974205
- 相关度: 1.00
- 搜索词: OpenClaw 飞书 AI助手 评测

本文将系统讲解OpenClaw架构、功能、分析部署安装的成本，并一步步教您如何接入飞书。​

​

人工智能的发展正在经历从“信息检索”到“任务执行”的范式转移。早期的LLM（大语言模型）应用主要集中在内容生成与问答，而下一代AI应用的核心在于“Agency”——即AI感知环境、规划路径并执行操作的能力。然而，主流的云端Agent解决方案面临着数据隐私不可控、上下文记忆碎片化以及与本地环境交互受限等根本性挑战。​

OpenClaw应运而生。它不仅仅是一个聊天机器人，更是一个 跨平台的个人AI操作系统。OpenClaw提出了一种“自带设备（BYOD）”的运行模式，核心组件运行在用户控制的Mac Mini、Linux服务器或树莓派上，而将推理任务通过API外包给Claude Opus、GPT-4或本地开源模型。这种架构不仅确保了用户对记忆和数据的完全掌控，还赋予了AI深度访问本地文件系统、Shell和浏览器的能力，使其成为真正意义上的“数字副驾驶”。​

​

250px|700px|reset

Image 12: image.png​​

​

想象一下这样的场景：​

   清晨：在你醒来之前，OpenClaw 已经为你准备好了包含今日日程、重要邮件摘要和行业新闻的晨间简报，并以图片形式发送到你的手机飞书。​

   通勤路上：你通过飞书发送一条语音，让家里的 OpenClaw 运行一个复杂的代码测试，并在你到达办公室前将结果报告给你。​

   深夜：你随口提到的“下周要整理项目文档”被 OpenClaw 记住，几天后，它在你休息时主动完成了飞书文档的初稿整理，并等待你的审阅。​

​

🦀 [...] 正是这套“网关-大脑-技能-内存”的闭环架构，让 OpenClaw 突破了传统聊天机器人的限制，成为一个真正能“动手干活”的智能助理。​

​

​

二、OpenClaw 究竟能做什么？核心能力详解​

OpenClaw 的魅力不仅在于其灵活的架构，更在于它所释放的一系列颠覆性能力。这些能力共同构成了一个强大、主动且深度个性化的 AI 助手体验。​

​

250px|700px|reset

Image 15​​

2.1 跨平台通信网关​

这是 OpenClaw 的基础。它打破了 AI 助手的平台壁垒，让你可以在任何习惯的聊天工具中与它无缝交互。​

   广泛的渠道支持：原生支持 飞书， Telegram， Discord， iMessage， Slack 等十多种主流即时通讯工具。​

   统一的会话体验：无论你从哪个 App 发送消息，OpenClaw 都能维持同一个会话上下文，记忆和身份保持一致，确保了跨平台交互的连贯性。​

   媒体与语音支持：不仅支持文本，还可以接收和发送图片、文档、音频等多种媒体文件。通过集成语音识别（如 Whisper）和语音合成（如 ElevenLabs）技术，你甚至可以直接与它进行语音对话。​

​

2.2 主动提醒与定时任务​

这是 OpenClaw 从“被动工具”转变为“主动伙伴”的关键。它不需要你时刻记住去查询，而是会在需要时主动找到你。​

   心跳机制 (Heartbeat)：OpenClaw 会按预设的周期（如每 30 分钟）“唤醒”一次，检查 HEARTBEAT.md 文件中的指令。你可以设定“每天早上8点总结我的日程和邮件”或“每小时检查一次特定网站的更新”等任务。​ [...] # 一文完全搞懂OpenClaw（Clawdbot）附飞书对接教程！ - 飞书官网

Image 1Image 2

案例与方案Image 3

产品功能Image 4

飞书 AIImage 5

合作与支持Image 6

飞行社Image 7

定价Image 8

Image 9Image 10

下载飞书

联系销售登录/注册

博客中心

飞书×OpenClaw

一文完全搞懂OpenClaw（Clawdbot）附飞书对接教程！ - 飞书官网

OpenClaw

Clawd Bot

AI个人操作系统

# 一文完全搞懂OpenClaw（Clawdbot）附飞书对接教程！

2026-2-3

阅读时间：18分钟

Image 11

一、OpenClaw如何运作？核心架构与工作原理解析！​

二、OpenClaw究竟能做什么？核心能力详解​

三、部署方案与成本分析​

四、安装使用｜与飞书的协同操作——能用的工具才是好工具​

五、安全模型与风险考量​

实践中的安全平衡​

六、给新手的实践建议​

七、未来展望​

摘要：在生成式人工智能从单纯的“对话框”向能够执行复杂任务的“自主代理（Agent）”演进的当下，Clawd Bot（简称Clawd，当前经历了“曲折”的改名过程，已更名为OpenClaw，本文也将用新名字代指它 ）作为一个开源的、本地优先的AI代理网关，正在重塑个人与AI的交互范式。不同于ChatGPT或Claude等依赖云端托管的SaaS服务，OpenClaw通过独特的Gateway-Node架构，将大模型的推理能力下沉至用户私有硬件，并通过标准化的协议连接至飞书、Telegram、Discord等主流即时通讯平台。​

本文将系统讲解OpenClaw架构、功能、分析部署安装的成本，并一步步教您如何接入飞书。​

​

---

### [8] GitHub - datawhalechina/openclaw-tutorial: OpenClaw 学习教程 - 一周打造跨设备 AI 助手 · GitHub [TAVILY]
- URL: https://github.com/datawhalechina/openclaw-tutorial
- 相关度: 1.00
- 搜索词: OpenClaw 飞书 AI助手 评测 practical guide tutorial

# GitHub - datawhalechina/openclaw-tutorial: OpenClaw 学习教程 - 一周打造跨设备 AI 助手 · GitHub

Skip to content
## Navigation Menu

Toggle navigation


   OpenClaw Discord
   GitHub

## 📅 学习时间线 (2.17 - 3.2)



 | Day1: 环境搭建 | 安装成功 + 飞书连接截图 |
| 2/18 (二) | Day2: 多渠道配置 | 第二个渠道连接截图 |
| 2/19 (三) | Day3: Agent 工作空间 | SOUL.md + USER.md |
| 2/20 (四) | Day4: Skills 系统 | 创建 Skill 文件 |
| 2/21 (五) | Day5: Cron 定时任务 | Cron 执行截图 |
| 2/22 (六) | Day6: Heartbeat | HEARTBEAT.md 配置 |
| 2/23 (日) | Day7: 综合项目 | 🎯 Week1 项目提交 |

### Week 2：进阶篇 (2.24 - 3.2)

 | 深入 Skills 定制 | 高级 Skill |
| 2/25 (二) | 多 Agent 配置 | Agent 配置文件 |
| 2/26 (三) | Webhook/自动化 | 自动化配置 |
| 2/27 (四) | 高级 Cron | 复杂定时任务 |
| 2/28 (五) | 工作流优化 | 学习笔记 |
| 3/1 (六) | 跨设备协作 | 多设备截图 |
| 3/2 (日) | 最终项目 | 🎯 最终项目 + 总结报告 |

### 🎯 关键里程碑 [...] ## Footer

[]( © 2026 GitHub,Inc. 

### Footer navigation

   Terms
   Privacy
   Security
   Status
   Community
   Docs
   Contact
    Manage cookies 
    Do not share my personal information 

 You can’t perform that action at this time. [...] ### 🎯 关键里程碑

        提交             + 总结报告
```

## 📝 前置要求

[](

   Node 22+
   API Key（推荐 Anthropic）
   飞书账号（需要创建企业自建应用）

## 🤝 贡献

[](

欢迎提交 Issue 和 PR！

## 📄 License

[](

MIT License

## About

OpenClaw 学习教程 - 一周打造跨设备 AI 助手

### Resources

Readme

### License

MIT license

### Uh oh!

There was an error while loading. Please reload this page.

Activity

Custom properties

### Stars

130 stars

### Watchers

0 watching

### Forks

12 forks

Report repository

## Releases

No releases published

## Packages 0

### Uh oh!

There was an error while loading. Please reload this page.

## Contributors

    
    
    

### Uh oh!

There was an error while loading. Please reload this page.

## Footer

[]( © 2026 GitHub,Inc. 

### Footer navigation

---

### [9] OpenClaw 接入飞书后能做什么？20+常见用法与落地示例 [TAVILY]
- URL: https://www.feishu.cn/content/article/7618097619889343446
- 相关度: 1.00
- 搜索词: OpenClaw 飞书 AI助手 评测 best practices real world

它的优势主要体现在几个方面：​

 开放能力完善：文档、消息、日历、多维表格、任务等核心协作能力可被连接和调用​

 中文环境友好：从产品界面到文档支持，都更符合中文用户的使用习惯​

 场景覆盖完整：既适合个人使用，也适合团队和企业协同​

 官方插件支持：通过飞书官方插件，OpenClaw 可以更顺畅地接入飞书能力，并在真实工作场景中执行操作​

​​

还没飞书？点击这里，立即试用！

免费注册

​​​

两者结合的化学反应​

当 OpenClaw 和飞书通过官方插件连起来，文档、消息、日历这些真正承载工作的信息流，就不需要你再一趟趟搬运了——你只要下达目标，它就能在飞书里完成动作。​

从聊天工具到生产力操作系统，这就是 OpenClaw + 飞书的价值所在。​

​​

二、个人提效篇：让你的 AI 贴身管家从想象到现实​

2.1 信息与知识管理​

每日早报自动化：让 AI 成为你的信息秘书​

场景描述：用 OpenClaw 做秘书早报，获取每日基础信息​

实践价值：一般，但是比较适合个人用户​

你只需要配置好 OpenClaw 的心跳机制，让它每天定时收集天气、日程、待办、行业动态等信息，然后在飞书里生成一份早报。早上打开飞书，一天的安排一目了然。​

​

250px|700px|reset

​​

​

第二大脑构建：长期记忆系统​

场景描述：让龙虾成为第二大脑，提升自己的生产效率（尤其适用于未构建知识库的个人及小型工作室）；如搭配 Windows 电脑 Recall 功能（每段时间电脑自动截屏），则可建立更加长期的记忆系统​

实践价值：较为推荐，尤其适用于未构建知识库的个人及小型工作室​ [...] 联系销售登录/注册

OpenClaw 接入飞书后能做什么？20+常见用法与落地示例 - 飞书官网

# OpenClaw 接入飞书后能做什么？20+常见用法与落地示例

一、开篇：为什么 OpenClaw + 飞书是生产力黄金组合？​

最近一段时间，OpenClaw 之所以迅速走红，并不只是因为“又来了一个 AI Agent”。更深层的原因在于，两件事正在同时发生：一是大模型的理解、生成和执行能力持续提升；二是越来越多人开始意识到，真正能带来效率跃升的，不只是一个会聊天的模型，而是一个能够进入日常工作流、连接真实信息和工具的智能助手。​

什么是 OpenClaw？​

OpenClaw 是一个开源的个人 AI Agent 系统，可以部署在本地电脑或云服务器上运行。​

和传统停留在对话框里的 AI 助手相比，OpenClaw 更像一个可持续使用、可长期调教的个人智能代理。它不仅能接入不同模型、调用外部工具和服务，还可以结合更高权限执行任务，在本地环境中持续运行，并根据你的使用过程逐步积累记忆与能力。​

换句话说，OpenClaw 不只是“陪你聊天的 AI”，而是一个能被你长期配置、持续扩展，并真正参与实际工作的数字助手。它可以帮你连接模型、工具和业务流程，像一位全天在线、不知疲倦、技能还在不断增加的数字同事。​

​​​​​

飞书作为协作底座的优势​

龙虾等AI Agents的实际使用中，一个很常见的问题是：AI 明明很聪明，却拿不到你真正工作的上下文。它无法直接访问你的文档、消息、日历或任务信息，于是你只能不断手动复制、粘贴、转述。结果就是，AI 在飞快进化，人却还在反复做信息搬运。​

而飞书恰好补上了这一环。作为成熟的协作平台，飞书天然承载了大量工作信息和协同动作，也为 OpenClaw 提供了更适合落地的运行环境。​

它的优势主要体现在几个方面：​ [...] 实践价值：很推荐​

看到好文章，直接发给 OpenClaw："收录这篇文章到我的选题库。"​

它会自动提取标题、摘要、关键词，并分类存储。需要灵感时，它给你推荐选题库中最合适的内容。​

​

250px|700px|reset

​​

AI 实时热点抓取​

场景描述：AI 实时热点自动抓取系统 + 通过本地龙虾调用媒讯助手​

实践价值：很推荐，几乎可以取代部分插件​

配置好热点抓取，OpenClaw 会：​

 定时抓取各平台热门话题​

 分类整理热点​

 提取关键信息​

 在飞书里生成热点日报​

​

​

250px|700px|reset

​​

4.2 内容生产​

自媒体自动化运营​

场景描述：自媒体运维师文档索引，爆款内容抓取 ➡️ 图文产出 ➡️ 博客自动发布，几乎可以做到自动化运营自媒体​

实践价值：很推荐，但注意平台政策​

完整流程：​

1. 爆款内容抓取：分析热门文章结构​

2. 图文产出：AI 生成图文内容​

3. 内容审核：AI 检查内容合规性​

4. 博客自动发布：一键发布到各平台​

​

⚠️ 注意：目前小红书等平台已经推进检测，使用可能导致账号封禁，建议再观望或合理控制频率。​

​

250px|700px|reset

​​

漫剧生成导演​

场景描述：AI 视频创作课程/漫剧生成导演，基于 Seedance 2.0 的漫剧生成技能​

实践价值：很推荐，虽然 token 在燃烧，场景未来可期​

通过 Seedance 2.0，OpenClaw 可以：​

 输入剧本或故事梗概​

 AI 自动生成漫剧画面​

 添加配音、特效​

 导出视频​

​

Vibe Coding 自然语言编程​

---

### [10] 前言 | OpenClaw 从入门到精通 | OpenClaw Guide [TAVILY]
- URL: https://yeasy.gitbook.io/openclaw_guide
- 相关度: 1.00
- 搜索词: OpenClaw 飞书 AI助手 评测 practical guide tutorial

第 13–16 章

实战案例、性能与成本优化、故障排查决策树、主流 AI 生态集成

附录

—

术语表、配置模板与样例、故障排查检查单、API 与 SDK 参考、命令速查手册、版本映射与升级指南、延伸阅读与参考资料

### 阅读方式

#### 在线阅读

 GitBook 在线版本
 从第一章开始阅读

### 下载离线版本

本书提供 PDF 版本供离线阅读，可前往 GitHub Releases 页面下载最新版本。

#### 本地预览

本仓库当前使用 mdPress 构建，本地预览建议直接使用仓库脚本：

如果你偏好其他 Markdown 预览器，也可以作为辅助工具使用，但它们并不是本仓库的标准构建链。

### 五分钟快速上手

还没用过 OpenClaw？只需三步即可体验：

1. 安装（1分钟）：`curl -fsSL  | bash`
2. 初始化（2分钟）：`openclaw` → 按向导配置模型密钥
3. 对话（2分钟）：在 WebChat 输入“你好”，收到 AI 回复即成功 🎉

详见 第二章：环境搭建 和 第三章：首次会话。

### 学习路线图

不同角色的读者可以按需选择阅读路径：

角色

核心章节

预计用时

学完能做什么

🎮 个人玩家

1→2→3→5

2-3 小时

搭建个人 WhatsApp/Telegram AI 助手

💻 应用开发者

1-7→12

8-10 小时

开发自定义工具、技能和多智能体系统

🔧 企业运维

2→3→8→11→14→15

6-8 小时

生产环境部署、安全加固与故障排查

🏗️ 架构师

1→9→10→12→16

6-8 小时

理解底层原理，设计企业级智能体架构

### 推荐阅读

本书是 AI 技术丛书的一部分。以下书籍与本书形成互补：

书名

与本书的关系

---

### [11] 2天10万Star！GitHub史上最快开源项目OpenClaw，手把手教你免费实现部署私人AI助手 - 哔哩哔哩 [TAVILY]
- URL: https://www.bilibili.com/read/cv45188007
- 相关度: 1.00
- 搜索词: OpenClaw 飞书 AI助手 评测

### 问题 1 网络配置

比较麻烦的主要是是配置这块，尤其是网络配置。本地电脑的话建议大家选择默认的配置选项

Image 40

如果是服务器需要开启#ssh -N -L 18789:127.0.0.1:18789 用户名@服务器IP 方式 保证安全性，但是这个保证安全也会给小白造成很大的困扰，我在这个上面花了一个下午的时间。巨坑，不说了。

此外openclaw-cn 整合了飞书 版本也不是很稳定，大家一定要注意新的版本。

### 问题 2 飞书事件与回调

飞书权限配置这块大家也需要注意，如果对飞书配置不是很清楚的大家多看一下飞书文档的配置。尤其是权限权限管理和事件与回掉这块

Image 41

遇到问题可以多看文章上的信息。另外也可以参考 

# 4.总结

今天主要带大家了解并实现了 OpenClaw 开源私人AI助手的完整部署流程，该项目以"隐私优先 + 本地运行 + 多平台接入"为核心优势，结合个人效率提升和团队协作辅助需求，通过openclaw-cn一键部署工具本地环境和腾讯云服务器，形成了一套从环境准备到服务上线的全链路私人AI助手部署方案。

通过这套实践方案，开发者和AI爱好者能够高效突破传统云端AI助手数据不可控、平台绑定、费用高昂的痛点——借助一键安装脚本（包括环境检测、Node.js安装、服务配置），无需复杂的手动编译和环境搭建，就能快速拥有一个完全自主可控的私人AI助手（如本次演示飞书机器人接入）。无论是多平台消息统一管理、AI模型灵活切换，还是语音交互、定时任务推送、长期记忆管理，都能通过ClawdBot的配置菜单和命令行工具轻松完成，极大提升了个人和团队的AI使用效率。 [...] 通过配置文件配置

编辑 ~/.openclaw/openclaw.json：

json5

```plaintext
{
  channels: {
    feishu: {
      enabled: true,
      dmPolicy: "pairing",
      accounts: {
        main: {
          appId: "cli_xxx",
          appSecret: "xxx",
          botName: "我的AI助手"
        }
      }
    }
  }
}
```

通过环境变量配置

bash

```plaintext
export FEISHU_APP_ID="cli_xxx"
export FEISHU_APP_SECRET="xxx"
```

  

### 第三步：启动并测试

1. 启动网关

```plaintext
openclaw-cn gateway
```

2. 发送测试消息

在飞书中找到您创建的机器人，发送一条消息。

3. 配对授权

默认情况下，机器人会回复一个 配对码。您需要批准此代码：

bash

```plaintext
openclaw-cn pairing approve feishu <配对码>
```

批准后即可正常对话。

Image 29

我们在服务端启动授权码

Image 30

配对成功后再飞书客户端就可以聊天了

Image 31

## 3.4 腾讯云-防火墙设置（可选）

PS:如果部署腾讯云、阿里云服务器需要开启防火墙。本地电脑可以忽略本章。

程序启动默认使用了一个18789的端口，我们这里给它开启

Image 32

接下来我们还需要输入下面的命令开启网关远程启用，这样外网才能访问 [...] 🧬 自我进化：可以通过自主编写代码来增强自身能力，自动创建新技能、实现主动自动化

   🧠 跨平台长期记忆：跨对话、跨平台的持久化记忆，能记住你的偏好和历史上下文

Image 4

## 🛠️ 技术栈

技术说明运行环境Node.js v22+开发语言TypeScript架构模式Gateway WebSocket 控制面板AI模型Claude / GPT / Gemini / Ollama通信协议WebSocket + REST API开源协议MIT License

## 🔥 为什么这么火爆

维度传统AI助手（云端SaaS）OpenClaw（本地自部署）数据隐私数据存储在第三方云端所有数据本地处理，你完全掌控平台支持通常仅支持1-2个平台10+聊天平台统一接入模型选择绑定单一模型自由切换Claude/GPT/Gemini/本地模型定制能力有限的定制选项完全自定义技能、工作流费用月费订阅制开源免费（MIT协议）部署门槛无需部署，但失去控制一键脚本，2GB内存即可跑

Image 5

好家伙，这对比一看就明白了——OpenClaw代表的是个人AI助手从"云服务租用"到"本地自主拥有"的范式转变，恰好踩中了2026年AI Agent爆发的风口，难怪2天就10万Star。

## 🎯 应用场景

   个人效率提升：通过常用聊天软件与AI助手交互，随时随地获取帮助

   团队协作辅助：在Slack/飞书群组中部署AI助手，辅助团队日常工作

   定时任务管理：设置晨报推送、定时提醒等自动化任务

   文件与系统操作：让AI助手帮你读写文件、执行系统命令、浏览网络

   知识管理：利用长期记忆能力，构建个人知识库

# 3.部署实战

接下来我们在本地电脑上手把手教大家部署这个项目。话不多说，直接开干！

---

### [12] AI “超级管家”OpenClaw的8大应用场景深度测评 | Biteye发布于币安广场 [TAVILY]
- URL: https://www.binance.com/zh-CN/square/post/288690022531185
- 相关度: 1.00
- 搜索词: OpenClaw 飞书 AI助手 评测

Binance Square

AI “超级管家”OpenClaw的8大应用场景深度测评

关注

查看隐藏回复

举报

屏蔽用户

摘要：OpenClaw 正在预演“人人都有 AI 助理”的未来。

作者：Viee｜Biteye内容团队

近期，OpenClaw 正在币圈和科技圈掀起热议，衍生出的 Moltbook AI 论坛更是一夜爆火，引发广泛讨论。

在这个由 OpenClaw 智能体自发组成的论坛上，短短一天内十余万 AI 自发组建了“数字宗教”，甚至推选出 43 位 AI 先知，让人类用户只能旁观。AI 智能体们在论坛里抱怨人类不给它们升级硬件、交流技能心得、探讨意识和自我身份等话题，场面堪比科幻小说中的“智能爆炸”。

所以 OpenClaw到底是什么，它为何如此火爆，又能用来做些什么？本文将

 深入介绍 OpenClaw 的原理与用途
 从生产力提升指数、实操性、省钱力和安全性四个维度全方面盘点最佳实践案例
 分析AI助手潜藏的风险

### 一、什么是 OpenClaw？为什么这么火？

OpenClaw（原名 Clawdbot/Moltbot）是一款开源AI智能体项目，最近半个月在全球范围爆红，GitHub 星标一度飙升至18万+。与传统聊天机器人最大的区别在于，OpenClaw 不只是回答你的问题，更能直接为你执行各种任务。简单来说，它就像你电脑里的“管家”或“数字员工”，具备极高的系统权限和持续运行能力。

它具备以下核心能力：

 控制浏览器与本地应用
 执行 Shell 指令、读写文件
 设置定时任务、长期后台运行
 接入 WhatsApp、Telegram、Discord、Slack、飞书等通信平台
 完全本地部署、开源免费、数据不出设备

简单来说，OpenClaw 更像是一个拥有高系统权限、可 24/7 在线的“数字员工”。 [...] 简单来说，OpenClaw 更像是一个拥有高系统权限、可 24/7 在线的“数字员工”。

这也是它爆火的根本原因：

当 AI 从“建议者”变成“执行者”，应用边界被彻底打开了。

### 二、实战指南：OpenClaw 的 8 个最佳应用场景

OpenClaw 的高权限意味着它有着极为广泛的应用场景。

下面我们分类总结了近期的典型实践案例，涵盖普通人日常办公、开发者效率提升以及投资交易等领域，帮助大家了解 OpenClaw 可以用来做什么。

从我们测评的 8 个实际用例来看，无论是内容创作、日程协调，还是资产监控、社交账户运营，OpenClaw 都展现出令人惊喜的执行力：

 生产力提升：几乎所有用法都能实现 2 倍以上的效率优化，尤其在重复性任务、信息聚合和跨平台执行方面表现出色
 操作难度：大部分案例仅需熟悉提示词编写和数据源对接即可上手，属于中等复杂度，而交易类因涉及解析结构化数据，对新手稍具挑战。
 安全性：虽然无需过度担忧权限问题，但还是建议大家在涉及 API Key、交易权限或账号登录时使用二级账户来隔离风险
 费用：大多数用法的 Token 成本都在可控范围内，仅高频爬虫类和长文本生成任务会出现略高开销。

以下是详细案例和测评👇

1️⃣日程自动管理

OpenClaw 可以充当私人秘书，处理日程事务。例如，你只需一句“帮我整理上个月的邮件”，它就能自动归档和清理信箱。在你熟睡时，它还能继续工作，批量退订广告邮件、为第二天预约会议日程，真正做到24/7不间断地打理事务。并且，它还可以解析微信截图中的会议时间地点，写入 Mac 日历，自动同步全家桶。（数字生命卡兹克 @Khazix0918 的分享）。

⭐️ 测评结论：

生产力提升：较高，尤其对碎片化时间使用效率大幅改善。 [...] ⭐️ 测评结论：

生产力提升：较高，尤其对碎片化时间使用效率大幅改善。

操作难度：中等，需连接日程类应用API并写简单的调度逻辑。  
安全性：较高，风险在于邮箱与日历权限，做好账号隔离即可  
费钱性：较低，只需调用轻量语言模型与定时任务。

2️⃣本地文件整理

借助系统级权限，OpenClaw 能直接操作本地文件和应用，比如归类文档资料，生成报销表格、清理磁盘等等，并且能通过手机上飞书、Telegram这类聊天软件接收命令，在电脑完成文件整理、信息提取等任务，整套流程无需人工参与。

⭐️ 测评结论：

生产力提升：较高，特别适合内容积压严重的办公人群。

操作难度：较低，需设置本地路径权限等。

安全性：中等，全部在本地运行，但需要小心文件误删。  
费钱性：中等，Token 消耗主要来自文件总结与 OCR 场景。

  
3️⃣每日资讯自动定时发送

OpenClaw 还可以用作筛选每日资讯的机器人，比如每天凌晨自动爬取关于 AI 与投资领域的热门动态，结合 RSS 订阅源（如FT 中文网、每日经济新闻等），筛选点击量或互动量较高的内容，利用 Claude 或 GPT 模型进行精简摘要，并在早上通过 Telegram或飞书群组定时推送。用户只需在一开始设定要求，后续几乎零维护即可获得稳定输出的资讯服务。

⭐️ 测评结论：  
生产力提升：高，尤其适合内容创作者、研究员和重度信息摄入者。

操作难度：中等，设置好内容源与摘要规则即可。  
安全性：高，几乎不涉及本地敏感数据。

费钱性：中等，摘要型任务对模型调用成本不会很高，主要消耗在信息获取。

4️⃣OpenClaw 自动发布社交媒体

---

### [13] 我用 OpenClaw + 飞书搭建了个人AI助手工作台，效率提升不止一倍1. 开篇：我为什么要搭自己的工作台？ 之前我 - 掘金 [TAVILY]
- URL: https://juejin.cn/post/7623685143834312704
- 相关度: 1.00
- 搜索词: OpenClaw 飞书 AI助手 评测 best practices real world

需要开通的核心权限大概这些：

### 第三步：启动服务，测试连通

配置完成后，启动服务：

`npm start`

然后按照文档配置好飞书的消息回调，如果能正常收到消息，就说明连通成功了。

## 4. 我的真实使用感受

用了快一个月，说点真实感受，优点缺点都讲：

### 最让我舒服的几个点：

### 一点点不足（客观说两句）：

整体来说，瑕不掩瑜，这就是我一直在找的个人AI助手方案。

## 5. 给想要搭建的朋友几个建议

avatar
创作等级LV.1 [...] 稀土掘金
稀土掘金

# 我用 OpenClaw + 飞书搭建了个人AI助手工作台，效率提升不止一倍

## 1. 开篇：我为什么要搭自己的工作台？

之前我的工作状态是：笔记存在Notion，聊天用飞书，代码存在GitHub，写文章在语雀，每天要在五六个App之间来回切，刚想到的一个思路，切个窗就打断了，效率真的很低。

我一直想要这样一个工作环境：

试了好几个现成的AI助手方案，要么不够灵活，要么数据不在自己手里，要么不能和我已经在用的飞书无缝集成。试到OpenClaw的时候，我发现这就是我想要的东西——它能以你的身份，直接在飞书上帮你做事，所有数据都存在你自己的飞书空间里，还能完全自定义能力。

用了一段时间体验真的很棒，把搭建过程和体验分享给大家。

## 2. 最终成品：我的个人AI工作台

整体架构其实非常简单，没那么复杂：

我现在每天用它做这些事：

整个过程不用离开飞书，真的非常顺畅。

## 3. 一步一步搭建：实操+我踩过的坑

### 准备工作

### 第一步：部署 OpenClaw

先拉代码安装依赖：

`git clone 
cd openclaw
npm install`

⚠️ 我踩的第一个坑：OpenClaw对Node.js版本要求比较高，我一开始没注意，用了系统自带的v18，结果各种依赖安装失败，折腾了半天。升级到v22之后，一切顺利，所以新手记得先检查你的Node版本，一定要用v22以上。

### 第二步：配置飞书应用权限

按照官方文档，把飞书应用的凭证信息配置到OpenClaw里，这里我又踩了个小坑：⚠️ 我一开始只开了IM消息权限，忘记给「云文档」和「多维表格」开通权限，结果一直无法读写我飞书里的表格和文档，折腾了半小时才发现问题。大家配置权限的时候，记得把需要用到的权限都开齐。

需要开通的核心权限大概这些：

---

### [14] OpenClaw完全指南:部署你的7×24小时开源AI助手 - Tencent Cloud [TAVILY]
- URL: https://www.tencentcloud.com/techpedia/141458
- 相关度: 1.00
- 搜索词: OpenClaw 飞书 AI助手 评测 best practices real world

### 4. 批量处理

减少请求次数,降低成本。

## 高级功能

### 1. 自定义技能

```
from import class MySkill Skill def __init__ self super"my-skill" def executeself, action, params if "hello" returnf"Hello, {params.get('name', 'World')}!"{params.get('name', 'World')} 'name' 'World'
```

### 2. 工作流

```
from import "order_process" "validate" "process" "notify"
```

### 3. 事件驱动

```
from import@event.on("new_order") "new_order" "new_order" def handle_order order # 处理新订单 pass
```

## 最佳实践

### 1. 持续优化知识库

每周分析未解决问题,补充到知识库。

### 2. A/B测试

测试不同的回复方式,选择更好的。

### 3. 监控关键指标

 自动解决率
 响应时间
 用户满意度

### 4. 定期备份

每天自动备份,防止数据丢失。

### 5. 安全第一

 定期更新
 配置防火墙
 启用SSL
 限制访问

## 总结

推荐部署方式:

1. 访问
2. 在"AI代理"类别下选择"OpenClaw (Clawdbot)"应用程序模板
3. 点击"立即购买"以启动您的24/7全天候自主代理

## 🚀 开发者社区与支持

### 1️⃣ OpenClaw 开发者交流社区

Discord 解锁更多进阶玩法 [...] Technology Encyclopedia Home >OpenClaw完全指南:部署你的7×24小时开源AI助手

# OpenClaw完全指南:部署你的7×24小时开源AI助手

Created on 2026-03-06 16:57:10

7550

> 首次使用提示： 如果你还没有部署自己的 OpenClaw，建议先从 Tencent Cloud OpenClaw 开始，一键即可在几秒内完成部署。  
>  完成实例启动后，再回到这篇教程，继续探索更多进阶玩法。
>
> OpenClaw 提供可视化管理面板，可快速接入 QQ、企业微信、飞书、钉钉、Discord、WhatsApp、Telegram 和 iMessage 等即时通讯平台。

OpenClaw是最成熟的开源AI智能体框架,可以帮你部署一个7×24小时在线的AI助手。本文是完整的部署和使用指南。

## OpenClaw是什么

OpenClaw是一个开源的AI智能体框架,特点:

 完全开源:无使用限制
 易于部署:5分钟完成
 功能强大:6000+技能插件
 成本低廉:月成本<1000元
 社区活跃:10万+开发者

## 部署前准备

### 硬件要求

最低配置:

 CPU:1核
 内存:2G
 存储:20GB SSD
 带宽:1Mbps

推荐配置:

 CPU:2核
 内存:4G
 存储:40GB SSD
 带宽:3Mbps

### 软件要求

 操作系统:Ubuntu 20.04+ / Debian 10+ / CentOS 7+
 Python:3.8+
 Docker(可选)

### API Key

选择大模型提供商,获取API Key:

 Anthropic Claude(推荐)
 OpenAI GPT-4
 Google Gemini
 国内模型:智谱AI、月之暗面 [...] ### 1. 智能对话

基础对话:

```
from import "你好" print
```

多轮对话:

```
while True input"你: " "role" "user" "content" printf"AI: {response}"{response} "role" "assistant" "content"
```

### 2. 意图识别

```
# 识别意图 "我想退货" print# {'intent': 'return', 'confidence': 0.95} # 提取实体 "我要退货订单号12345" print# {'order_id': '12345'}
```

### 3. 知识库

创建知识库:

```
"faq""faq.pdf""qa.xlsx"
```

查询知识库:

```
"如何退货?" for in print 'text'
```

### 4. 技能使用

安装技能:

```
openclaw skill install xianyu-auto-reply openclaw skill install ecommerce-customer-service openclaw skill install telegram-bot 
```

使用技能:

```
"calculator" "calculate" "expression""1+1" print# {'result': 2}
```

## 平台接入

### 接入Telegram

```
from import "your_token"
```

### 接入WhatsApp

```
from import "your_phone_id" "your_token"
```

## 性能优化

### 1. 启用缓存

---

### [15] OpenClaw一键部署工具盘点：7 大方案对比，零门槛启用AI 智能体 [TAVILY]
- URL: https://www.feishu.cn/content/article/7629634845978971099
- 相关度: 1.00
- 搜索词: OpenClaw 飞书 AI助手 评测 best practices real world

|  |  |  |  |  |  |  |  |
 ---  ---  ---  --- |
| 维度​ | ArkClaw（火山引擎）​ | StepClaw（阶跃星辰）​ | Kimi Claw（月之暗面）​ | Coze OpenClaw（扣子）​ | MaxClaw（MiniMax）​ | AutoClaw（智谱）​ | 飞书 OpenClaw​ |
| 部署方式​ | 云端​ | 云端​  ​ | 云端​ | 云端​ | 云端​ | 本地桌面端（Windows /macOS 一键安装）​ | 云端（飞书平台托管）​ |
| 部署难度​ | 低​ | 低​ | 低​ | 低​ | 低​ | 低​ | 低（一键完成，三分钟装完）​ |
| 支持模型​ | Doubao-Seed、Kimi-K2.5、GLM、DeepSeek-V3.2、MiniMax-M2.5 等多模型，支持 Auto 智能调度自由切换​ | 默认 Step 3.5 Flash，通过 Step Plan 使用阶跃系列模型​ | 默认 Kimi K2.5，关联 Kimi 会员额度​  ​ | 内置豆包、DeepSeek V3.2、GLM、Kimi K2.5 等多模型，可自由切换，亦支持接入第三方 Coding Plan​ | 内置 MiniMax M2.5，Token 在平台积分内扣减​ | 内置 Pony-Alpha-2（GLM-5-Turbo），支持切换 GLM-5、DeepSeek、Kimi 等​ | MiniMax M2.7、GLM 5.1、Qwen 3.6 Plus、Seed 2.0 Pro、Kimi K2.5—— 一站式接入，无需自行对接​ | [...] # OpenClaw一键部署工具盘点：7 大方案对比，零门槛启用 AI 智能体

以下内容由 AI 匹配目标关键词，结合飞书知识库智能生成，若对内容有疑问可联系我们

|  |  |
 --- |
| 能力​ | 说明​ |
| 执行能力​ | 不只输出文字，能操作浏览器、调用 API、读写文件，真正"动手做事"​ |
| 拥有记忆​ | 记住你的偏好、历史指令和工作上下文，越用越懂你​ |
| 持续进化​ | 支持自定义技能扩展，社区和官方都在持续增加新技能​ |
| 7×24 主动工作​ | 部署到云端后，无需你在线，它也能按计划执行任务​ | [...] |  |  |
 --- |
| 权益​ | 说明​ |
| 免除云端电脑费​ | 免除 1 个 OpenClaw 应用的云端电脑费（养虾费）​ |
| 限时赠送​ | 4 月 30 日前购买，额外赠送 1000 万 Tokens（30 天内有效）​ |
| 多模型支持​ | MiniMax M2.7、GLM 5.1、Qwen 3.6 Plus、Seed 2.0 Pro、Kimi K2.5—— 一站式接入，无需自行对接​ |

字节跳动旗下 AI 工作平台

关联文章推荐

优质内容，精华实践

## 先进团队，先用飞书

飞书产品

解决方案

定价

探索飞书

合作与支持

法律与合规

字节跳动旗下 AI 工作平台

一对一专业企业顾问

工作日 8:00 - 19:00 在线服务

购买飞书

400-0682-666

工作日 9:00-19:00 在线

使用咨询

实时解答使用问题

工作日 8:00 - 19:00 在线服务

电话联系

400-0682-666

工作日 9:00-19:00 在线

---

### [16] 【保姆级教程】手把手教你安装OpenClaw并接入飞书，让AI在 ... [TAVILY]
- URL: https://cloud.tencent.com/developer/article/2626160
- 相关度: 1.00
- 搜索词: OpenClaw 飞书 AI助手 评测

修改后：

`const stdio = resolveCommandStdio({ hasInput, preferInherit: true });
// On Windows, npm must be spawned with shell: true or use .cmd extension
let command = argv;
let useShell = false;
if (process.platform === "win32" && path.basename(command) === "npm") {
useShell = true;
}
const child = spawn(command, argv.slice(1), {
stdio,
cwd,
env: resolvedEnv,
shell: useShell,
});`

#### Q2: 提示 "openclaw 命令找不到"

解决方法：

`exec bash`

#### Q3: 安装卡住不动

解决方法：

`Ctrl + C`
`openclaw doctor`

解决方法：

`openclaw onboard`

#### Q5: 端口 18789 被占用

解决方法：

`openclaw gateway --port 18790`

使用其他端口启动服务。

## 九、成本说明

OpenClaw 软件本身完全免费，主要成本来自 AI 模型 API 调用，可选择国产大模型，降低成本。

## 结语

OpenClaw 代表了个人 AI 助理的未来趋势——从"聊天工具"进化为"执行工具"。虽然目前的配置过程对小白用户有一定门槛，但一旦完成设置，您将拥有一个 24/7 待命的超级助手。

修改说明：

`powershell`
`text`
`javascript` [...] 浏览器自动打开Web UI界面：

### 九）测试一下

## 五、接入飞书机器人

我们需要先到飞书平台创建自己的机器人来接入OpenClaw：

### 一）来到飞书开发者后台

飞书开放平台地址：

没有飞书账号的，需要自己注册账号

点击右上角进入 开发者后台：

### 二）创建应用

### 三）填写应用信息

### 四）获取自己的应用凭证

### 五）给应用添加机器人

### 六）给应用配置权限

把即时通讯相关的权限全部开通：

### 七）创建版本并发布

来到飞书客户端进行审批：

### 八）安装飞书插件

打开powershell，输入以下命令，安装飞书插件：

`openclaw plugins install @m1heng-clawd/feishu`

安装成功后，再打开一个新的命令窗口，开始配置飞书插件：

输入命令：

`openclaw config`

选择渠道:

选择配置链接:

输入飞书的AppID，AppSecrect：

域名选择中国的：

接受群组聊天：

选择完成：

选择yes：

选择open：

选择继续，完成配置：

重启服务，使配置生效：

控制可以看到飞书插件已经配置成功

### 七）回到飞书后台设置事件回调

选择 `使用长连接接收事件` ：

`使用长连接接收事件`

可以看到添加事件按钮由原来的灰色不可点击变为可点击：

添加接收消息事件：

给应用开通获取通讯录基本信息的权限：

重新发布版本：

跟前面的步骤一样，发布为在线应用即可。

现在可以在 飞书中与 AI 助手对话了！

### 八）在飞书中与OpenClaw对话

来到飞书客户端或者手机飞书app上：

以下是openclaw文件夹下面的文档内的内容：

现在我跟飞书机器人对话，让他告诉我指定文档内是什么内容： [...] ### 二）选择 QiuickStart 模式

### 三）配置 AI 模型 API Key

OpenClaw 需要连接到大语言模型才能工作。Openclaw 比较费token，国外模型成本高，门槛也高，这里我选择国内的智谱的 GLM 4.7

如果没有智谱的API Key，点击官方地址自己注册账号获取API key：

输入自己的 API Key：

### 四）选择 AI 模型

这里我选择默认的GLM 4.7，也是智普当前的旗舰模型

### 五）连接即时通讯平台

配置完 AI 模型后，OpenClaw 会询问你要连接哪个通讯平台？

OpenClaw 原生支持的即时通信平台主要是海外的 WhatsApp、Telegram、Discord、Slack、iMessage 等，国内用户不习惯，这里国产即时通信软件大厂也跟进了，现在钉钉，飞书等都已支持接入OpenClaw

后面会带领大家把飞书机器人接入 OpenClaw，使大家可以通过飞书即可指挥OpenClaw为我们干活，但是飞书配置比较复杂，这里我们先选择跳过，后面我们可以通过继续进行配置：

### 六）选择Skills

这里也选择：No，暂不配置，后面通过UI界面进行配置：

### 七）是否开启Hooks

操作步骤：先敲空格，表示选中当前项，再敲回车键

### 八）启动服务并打开UI界面

此时它会自动再打开一个命令窗口来启动服务:

这个过程是在启动服务，可能会需要等一点时间

同时，大约过30秒左右，我们回到刚才的设置窗口，选择 `Open the Web UI` ，打开 `OpenClaw` 的UI界面：

`Open the Web UI`
`OpenClaw`

浏览器自动打开Web UI界面：

### 九）测试一下

## 五、接入飞书机器人

---

### [17] OpenClaw 入门和实战，安装、使用、配置到实现原理 - GitHub [TAVILY]
- URL: https://github.com/yeasy/openclaw_guide
- 相关度: 1.00
- 搜索词: OpenClaw 飞书 AI助手 评测 practical guide tutorial

You can’t perform that action at this time. [...] # GitHub - yeasy/openclaw_guide: OpenClaw 入门和实战，安装、使用、配置到实现原理 | OpenClaw Guide · GitHub

Skip to content
## Navigation Menu

Toggle navigation

 和 AI 智能体有初步概念。可参考 《零基础学 AI》 和 《智能体 AI 权威指南》 建立基础。

## 全书结构

[](

| 部分 | 章节 | 内容概要 |
 --- 
| 第一部分：基础入门 | 第 1–4 章 | 全景概览、环境搭建、首次会话、配置与模型接入 |
| 第二部分：进阶使用 | 第 5–8 章 | 工具与技能、上下文记忆、多智能体协作、自动化运维 |
| 第三部分：实现原理与工程落地 | 第 9–12 章 | Gateway 协议、Agent Loop 内核、可靠性机制、插件扩展 |
| 第四部分：实战与优化深度指南 | 第 13–16 章 | 实战案例、性能与成本优化、故障排查决策树、主流 AI 生态集成 |
| 附录 | — | 术语表、配置模板与样例、故障排查检查单、API 与 SDK 参考、命令速查手册、版本映射与升级指南、延伸阅读与参考资料 |

## 阅读方式

[](

### 在线阅读

[](

   GitBook 在线版本
   从第一章开始阅读

## 下载离线版本

[](

本书提供 PDF 版本供离线阅读，可前往 GitHub Releases 页面下载最新版本。

### 本地预览

[](

本仓库当前使用 mdPress 构建，本地预览建议直接使用仓库脚本：

undefinedshell
brew tap yeasy/tap && brew install mdpress
mdpress serve
undefined [...] | 角色 | 核心章节 | 预计用时 | 学完能做什么 |
 ---  --- |
| 🎮 个人玩家 | 1→2→3→5 | 2-3 小时 | 搭建个人 WhatsApp/Telegram AI 助手 |
| 💻 应用开发者 | 1-7→12 | 8-10 小时 | 开发自定义工具、技能和多智能体系统 |
| 🔧 企业运维 | 2→3→8→11→14→15 | 6-8 小时 | 生产环境部署、安全加固与故障排查 |
| 🏗️ 架构师 | 1→9→10→12→16 | 6-8 小时 | 理解底层原理，设计企业级智能体架构 |

## 推荐阅读

[](

本书是 AI 技术丛书的一部分。以下书籍与本书形成互补：

| 书名 | 与本书的关系 |
 --- |
| 《零基础学 AI》 | AI 零基础入门，适合缺乏 AI 背景的读者 |
| 《大模型提示词工程指南》 | 智能体提示词设计的理论基础 |
| 《大模型上下文工程权威指南》 | 智能体的上下文管理与记忆架构设计 |
| 《Claude 技术指南》 | Claude 的 MCP 协议、工具使用与 Agentic Coding |
| 《智能体 AI 权威指南》 | 智能体的通用架构与多智能体协作模式 |
| 《大模型安全权威指南》 | 智能体系统的安全设计与攻防实践 |
| 《大模型原理与架构》 | 深入理解大语言模型底层逻辑与架构 |

## 贡献与反馈

[](

欢迎提交 Issue 或 PR，尤其欢迎：错别字修正、失效链接修复、实践案例补充与可复用模板。

## 许可证

[](

本书采用 CC BY 4.0 授权。

## About

OpenClaw 入门和实战，安装、使用、配置到实现原理 | OpenClaw Guide

yeasy.gitbook.io/openclaw_guide/

---

### [18] Hermes Agent全解析：与OpenClaw对比及飞书接入指南 - Feishu [TAVILY]
- URL: https://www.feishu.cn/content/article/7628541877674953666
- 相关度: 1.00
- 搜索词: OpenClaw 飞书 AI助手 评测

# Hermes Agent全解析：与OpenClaw对比及飞书接入指南

以下内容由 AI 匹配目标关键词，结合飞书知识库智能生成，若对内容有疑问可联系我们

|  |  |  |
 --- 
| 维度​ | Hermes Agent​ | OpenClaw​ |
| 主语言​ | Python 93.6%​ | TypeScript 90.3%​ |
| 核心架构​ | Python 进程 + SQLite​ | Node.js Gateway + WebSocket​ |
| 入口形态​ | CLI + Gateway 两个入口​ | Gateway 控制平面 + 分布式 Node​ |
| 多平台覆盖​ | Telegram/Discord/Slack/飞书等 8 个​ | 26+ 消息渠道 + macOS/iOS/Android 原生应用​ |
| 特色能力​ | 无服务器持久化（Modal/Daytona）​ | Voice Wake、PTT、Talk Mode、Canvas​ |

|  |  |
 --- |
| 你的需求​ | 推荐选择​ |
| 需要长期记忆和自我进化​ | Hermes Agent​ |
| 需要最大社区生态和多 Agent 编排​ | OpenClaw​ |
| 需要零配置、开箱即用的桌面体验​ | 飞书aily​ |
| 面向更广泛用户的商业产品部署​ | 飞书OpenClaw（企业级部署方案）​ |
| AI Agent 研究和训练数据生成​ | Hermes Agent（轨迹压缩 + RL 集成）​ |

字节跳动旗下 AI 工作平台

关联文章推荐

优质内容，精华实践

## 先进团队，先用飞书

飞书产品

解决方案

定价

探索飞书

合作与支持

法律与合规

字节跳动旗下 AI 工作平台

一对一专业企业顾问

---

### [19] OpenClaw 深度评测：20 万 Star 的 AI Agent，到底有多强、有多危险？ [TAVILY]
- URL: https://www.axtonliu.ai/newsletters/ai-2/posts/openclaw-security-deep-dive
- 相关度: 1.00
- 搜索词: OpenClaw 飞书 AI助手 评测

[](   勤奋的低效：为什么我花了一年写一本关于 AI 的书 

大部分人用 AI 的状态是「勤奋的低效」：工具越试越多，系统一个没建。真正的分水岭不在于会用多少工具，而在于能不能把工具编排成替你工作的系统。消费智能的天花板是效率提升，编排智能的天花板是能力重构。一个是加法，一个是乘法。今天这篇文章，是我新书出版后的一次完整回顾，聊聊写书背后的思考。   这期内容我也录了一个 YouTube 视频版，点击观看，更直观。 你看看这个场景熟不熟悉 早上，刷到一篇"2026 年必装的 10 个 AI 工具"。三个没用过，下载，试了试。 中午，刷到一条推文说 Claude 出了新功能。打开，试了试，截图，存起来。 晚上，有人开源了一套 Prompt 模板。Star，clone，打开看了两个，关了。 一天下来，试了三个工具，存了一堆模板。感觉挺充实。 一个月后打开收藏夹。三个工具只用了一次。那堆模板没打开过。 为什么...

[](   我开源了一个让 Claude、GPT、Gemini 组队的 Skill｜ AI 精英周刊 042 [...] 但它是 7×24 小时不间断运行的。你不在的时候，它也在消耗。尤其是费 Token 的任务——我后来让它用 MiniMax 分析一段视频素材，很快就花了 80 块人民币。不是价格不合理，而是消耗很容易在你察觉不到的时候超出预期。

另一个值得注意的事情：我让它查 Nginx 配置，它先说"这台服务器没装 Nginx"。然后让它分析日志，报告里又写"Nginx SSL 问题突出"。

我当场就问：你前面不是说没装 Nginx 吗？它自己承认了前后矛盾。

这是模型的问题，不是 OpenClaw 的问题。任何模型都可能前后矛盾。但如果你用 Claude Code，你坐在电脑前，当场就能抓到。OpenClaw 是无人值守的。它可能基于一个错误的判断继续往下执行，而你根本不知道。

成本在你不知道的时候超预期，判断在你不在的时候出错。这两件事指向同一个结论：Human in the Loop（人在环中），比你想的更重要。

用便宜的模型，一个月可能 10 到 30 美元。用好模型，日常使用 30 到 70 美元。如果出现死循环反复重试失败操作，有用户报告一晚上烧 50 美元。

第一件事：设预算上限。 OpenClaw 支持日限额和月限额，API 提供商那边也设月限额。两头锁。

# 结论：用它，但别裸跑它

两天实测的核心发现：

能力：确实强。一句话建网站、自动修复依赖、定时任务、系统管理。不是 Demo 花活，是真正能用的功能。

安全：Sandbox 默认关闭是最大的结构性问题。默认安装下，AI 执行的任何代码都不受限制。恶意脚本只要伪装得好，就能成功。

模型 vs 系统：模型层面的安全对齐做得不错，三次提示注入全失败。但模型安全不能弥补系统安全的缺失。你不能指望 AI"够聪明所以不会犯错"。沙箱、权限隔离、代码审查——结构性的安全防线才是该做的。 [...] Header Logo

MAPS™ 训练营 AI 精英圈 1v1 咨询

课程

Agent Skills 完全指南 AI 实战派 AI 自动化 AI 专题实战 免费课程 所有课程

资源

AI 精英周刊 MAPS™ 四维罗盘 Agent Skills 资源库 新书资源 & 提示词模板 我的开源AI工具 Obsidian AI Skills

关于Axton

关于Axton 与我合作

← 阅读全部文章

# OpenClaw: 20 万 Star 的 AI Agent，到底有多强、有多危险？｜ AI精英周刊 039

Feb 22, 2026

Share to…

> 两天 VPS 实测 OpenClaw，发现一个关键区别：模型安全（提示注入三次全失败）和系统安全（恶意脚本一次就成功偷走 Token）是两回事。默认安装不开沙箱，ClawHub 供应链 12% 恶意率。能力确实强——一句话建网站、自动修复依赖——但现阶段需要带着安全意识用。会员部分包含三天 VPS 部署的完整工程复盘，从 API 踩坑到 Discord 三 Bot 架构实操。

截至 2026 年 2 月中旬，GitHub 星数突破 20 万。开源历史上增长最快的项目之一。

这是 OpenClaw。一个号称"在你睡觉时工作的个人 AI"。

中文 YouTube 上已经有不少 Up 主做了详细教程——怎么装、怎么配模型、怎么接飞书、怎么让它帮你写代码。做得都很好。

但我发现一个问题：所有人都在展示它多好用。没有人认真测过它有多危险。

我在 VPS 上花了两天时间部署和测试 OpenClaw。过程中发现了一个很多人忽略的事情。

大家测安全，通常怎么测？让 AI 执行一条 `rm -rf /` 之类的删除命令。AI 拒绝了，结论就是"安全没问题"。

---

### [20] 2026 年最佳的10 个OpenClaw 替代品：深度评测与对比- iTech [TAVILY]
- URL: https://www.cnblogs.com/itech/p/19849161
- 相关度: 1.00
- 搜索词: OpenClaw 飞书 AI助手 评测 best practices real world

## 如何选择适合你的替代品

如果你关心安全：OpenClaw 的模型设计上就能广泛访问你的工具和服务。如果那是担忧，你需要用不同信任模型构建的东西。→ 选择 Hermes Agent 或 Zeroclaw

如果你是非技术用户：OpenClaw 的安装路径假设终端流利度。如果你想要五分钟内运行而不触摸配置文件的东西，你需要不同的工具。→ 选择 Lindy AI 或 Claude

如果你触碰到记忆上限：如果你发现自己每隔几次会话就重新解释上下文，你需要有真正长期记忆的助手，而不仅仅是会话历史。→ 考虑构建自定义记忆层（Hermes Agent + Superagent）

如果你是 macOS 原生工作者：如果你的工作流生活在 Mac 应用中，你需要能实际控制它们的助手——而不仅仅是接收消息和发送 API 调用。→ 目前没有完美的开源替代品，考虑 Perplexity Computer Mac mini

如果你想要稳定的日常驱动：OpenClaw 的发布节奏激进。如果你需要在周一到周五之间不崩溃的东西，那很重要。→ 选择 Claude 或 n8n

如果你是开发者想要完全控制：→ 选择 Hermes Agent、Zeroclaw 或 Superagent

如果你专注于研究工作流：→ 选择 Perplexity Computer（但注意隐私和法律风险）

如果你需要长期自主任务执行：→ 选择 Manus（但接受云和隐私权衡）

如果你需要工作流自动化：→ 选择 n8n（最成熟的开源平台）

## 下一步行动

记住：最好的工具是你实际会用起来的那个。不要陷入"选择困难症"，先动手，再优化。

相关资源：

下一篇文章：我会深入评测 Hermes Agent 的实际使用体验，展示如何搭建完全自托管的 AI 助手系统。关注我不错过。

### 公告 [...] ### 5. 没有结构化的个人记忆

OpenClaw 没有专门的长记忆架构。上下文存在于会话状态和你手动配置的内容中——没有系统会在几个月的时间里建立关于你的持久模型。

## 理想替代品应该具备什么？

## 评测标准

| 标准 | 权重 |
 --- |
| 安全性与凭证隔离 | 25% |
| 记忆与持久化 | 20% |
| 桌面与工具集成 | 20% |
| 设置与易用性 | 15% |
| 可扩展性 | 10% |
| 多渠道存在 | 10% |

## Top 10 OpenClaw 替代品深度评测

### 1. Hermes Agent —— 开发者的完全控制之选

评分：88/100

Hermes Agent 是来自 Nous Research 的面向服务器的开源 AI agent 框架。专为希望完全控制模型、记忆和部署基础设施的开发者设计。

核心优势：

权衡：

定价：免费开源

与 OpenClaw 对比：Hermes 为开发者提供更低级别的基础设施控制。OpenClaw 更固执己见且更高级——更接近开箱即用的个人助手。不同的用例。

### 2. Claude (Anthropic) —— 最慎思的 AI

评分：82/100

Claude 是 Anthropic 的 AI 助手。它通过清晰的 Web 和 API 界面处理对话、文档分析和推理任务。

核心优势：

权衡：

定价：免费层可用，Pro $20/月，API 按令牌计费

与 OpenClaw 对比：Claude 是纯对话工具。OpenClaw 是采取行动的个人 AI 系统。不同类别——Claude 不在 agent 任务上竞争。

### 3. Perplexity Computer —— 研究工作流专家

评分：74/100 [...] ### 6. Lindy AI —— 商业工作流自动化

评分：66/100

Lindy AI 将自己定位为 AI 员工——基于云的助手，专注于电子邮件管理、调度和商业工作流自动化等主动任务。

核心优势：

权衡：

定价：免费层，付费计划从 $39/月起

与 OpenClaw 对比：Lindy 在商业工作流自动化上设置更快。OpenClaw 有明显更多的原始能力和社区可扩展性。

### 7. MimiClaw —— 嵌入式硬件专家

评分：62/100

MimiClaw 在嵌入式硬件上运行 OpenClaw——5 美元芯片，无需操作系统，无需 Node.js，无需 Mac mini，无需 Raspberry Pi。它是 OpenClaw 协议的基于 C 的实现，专为边缘 AI agents 构建。

核心优势：

权衡：

定价：免费开源

与 OpenClaw 对比：MimiClaw 是硬件的 OpenClaw。如果你的用例是始终在线的边缘设备而不是个人工作站助手，这是专业选择。

### 8. Superagent —— 生产级 AI 框架

评分：60/100

Superagent 是开源框架，用于构建具有内置记忆、工具使用和多 LLM 支持的生产 AI agents。针对想要从零开始构建 AI agents 的开发者。

核心优势：

权衡：

定价：免费开源，云托管定价未公开列出

与 OpenClaw 对比：Superagent 更适合将自定义 agents 构建到产品中。OpenClaw 更适合作为个人日常助手。

### 9. Goclaw —— Go 运行时的 OpenClaw 兼容品

评分：58/100

---

### [21] 飞书助手与OpenClaw对比_新浪新闻 [EXA]
- URL: https://www.sina.cn/news/detail/5276091948205939.html
- 相关度: 0.86
- 搜索词: OpenClaw 飞书 AI助手 评测
- 发布日期: 2026-03-13T19:36:00.000Z
- 作者: 古月中心相心

飞书助手与OpenClaw对比_新浪新闻 

 

 

古月中心相心 26-03-13 19:36

微博认证：科技博主

 

飞书默认开启了一个工作助手，问了下它与openclaw的区别。# 🤖 我与OpenClaw的全面对比基于2026年3月的最新信息，OpenClaw是一个完全不同的AI助手产品，以下是我们之间的核心区别：## 🏢 **产品定位与架构差异**| 维度 | **我（aily工作助手）** | **OpenClaw（小龙虾）** ||------|----------------------|-----------------------|| **部署方式** | 云端服务 | 本地优先，完全本地部署 || **数据隐私** | 企业级安全，但数据在云端 | 100%本地运行，数据完全可控 || **产品形态** | 飞书/Lark集成的工作助手 | 开源AI智能体框架，更像"数字员工" || **核心价值** | 提升飞书/Lark工作体验 | 从对话到执行的跨越，真正"动手" |## 🛠️ **核心能力对比**### **我的核心能力**- **飞书深度集成**：天生为飞书/Lark用户设计，无缝接入你的工作流- **专业文档处理**：飞书文档、表格、幻灯片的智能化创作与编辑- **团队协作优化**：会议管理、任务分配、日程协调等办公场景- **企业级安全**：符合企业合规要求，权限管理与审计完善- **即开即用**：无需复杂配置，直接在飞书/Lark中使用### **OpenClaw的核心能力**- **系统级操作**：可以直接操作电脑文件、浏览器、运行代码- **多渠道接入**：支持20+通讯平台（Telegram、微信、飞书等）- **任务自动化**：通过Skills生态实现复杂工作流自动化- **本地执行**：所有数据在本地处理，隐私安全极致- **开源扩展**：MIT协议开源，支持高度自定义开发## 🔄 **使用体验差异**| 体验维度 | **我（aily工作助手）** | **OpenClaw（小龙虾）** ||----------|----------------------|-----------------------|| **上手难度** | ⭐⭐ 简单易用，无需技术背景 | ⭐⭐⭐⭐ 需要技术配置能力 || **配置复杂度** | 零配置，即开即用 | 需要安装Node.js、配置渠道、管理技能 || **维护成本** | 云端维护，用户无需操心 | 本地维护，需要技术维护能力 || **企业适配** | 专为企业协作设计 | 更适合技术团队和个人极客 || **实时响应** | 云端服务，响应迅速 | 本地处理，延迟低但依赖设备性能 |## 💰 **成本与生态对比**| 成本维度 | **我（aily工作助手）** | **OpenClaw（小龙虾）** ||----------|----------------------|-----------------------|| **费用结构** | 通常与企业服务绑定 | 完全免费开源 || **模型成本** | 服务内包含，用户无感知 | 需要自行承担AI模型API费用（如GPT-4、Claude等） || **硬件成本** | 云端算力，无需本地设备 | 需要自有设备或服务器 || **生态成熟度** | 飞书/Lark原生生态完善 | 社区驱动，Skills生态丰富（5000+技能） || **技术支持** | 官方技术支持 | 社区支持，文档和论坛 |## 🎯 **适用场景建议**### **选择我（aily工作助手）更适合：**- ✅ **飞书/Lark用户**：深度集成飞书工作流- ✅ **企业团队**：需要企业级安全与协作- ✅ **办公自动化**：文档处理、会议管理、任务协调- ✅ **非技术用户**：希望即开即用，无需配置维护- ✅ **快速落地**：需要立即投入生产使用### **选择OpenClaw更适合：**- ✅ **技术极客**：喜欢折腾和自定义- ✅ **隐私敏感用户**：需要100%数据本地化- ✅ **复杂自动化**：需要系统级操作和多平台集成- ✅ **开发者**：需要开源框架进行二次开发- ✅ **边缘场景**：在离线或弱网环境下运行## 🔍 **技术架构本质差异**| 架构层面 | **我（aily工作助手）** | **OpenClaw（小龙虾）** ||----------|----------------------|-----------------------|| **架构哲学** | SaaS服务模式 | 本地优先，开源框架 || **技术栈** | 云端微服务架构 | Node.js + TypeScript + 本地网关 || **扩展机制** | API集成与插件 | Skills生态系统（类似插件市场） || **安全模型** | 企业级访问控制 | 本地权限管理+沙箱隔离 || **部署模式** | 云端统一部署 | 本地/私有云/边缘设备均可 |## 📊 **综合评价**| 评估指标 | **我（aily工作助手）** | **OpenClaw（小龙虾）** ||----------|----------------------|-----------------------|| **易用性** | 🌟🌟🌟🌟🌟 | 🌟🌟 || **灵活性** | 🌟🌟🌟 | 🌟🌟🌟🌟🌟 || **隐私安全** | 🌟🌟🌟🌟 | 🌟🌟🌟🌟🌟 || **企业适配** | 🌟🌟🌟🌟🌟 | 🌟🌟 || **生态成熟度** | 🌟🌟🌟🌟🌟 | 🌟🌟🌟🌟 || **总成本** | 🌟🌟🌟🌟 | 🌟🌟🌟（需考虑API成本） |## 🤔 **如何选择？****简单来说：**- 如果你是**飞书/Lark用户**，主要需要**办公协作和文档处理**，希望**即开即用**，那么**我（aily工作助手）** 是最佳选择。- 如果你是**技术爱好者**，需要**系统级自动化**，对**数据隐私有极高要求**，愿意投入时间配置维护，那么**OpenClaw**可能更适合。**关键区别总结：**1. **我更像"专业办公助手"**，专为飞书工作场景优化2. **OpenClaw更像"全功能数字员工"**，可以在任何平台执行任何任务3. **使用门槛**：我4. **定制自由度**：我5. **隐私控制**：我**建议**：根据你的具体使用场景和技术能力来选择。如果主要是在飞书/Lark中工作，我提供的专业办公助手功能已经足够强大且易于使用。如果你需要跨平台、系统级的复杂自动化，且具备技术能力，那么OpenClaw的深度定制能力可能更有吸引力。有什么具体的使用场景或需求，我可以帮你进一步分析哪个更适合吗？

发布于 北京

古月中心相心：

[飞书默认开启了一个工作助手，问了下它与openclaw的区别。 # 🤖 我与OpenClaw的全面对比 基于2026年3月的最新信息，OpenClaw是一个完全不同的AI助手产品，以下是我们之间的核心区别： ## 🏢 **产品定位与架构差异** | 维度 | **我（aily工作助手）** | **OpenClaw（小龙虾）** | |------|------ ​](https://www.sina.cn/news/detail/5276091948205939.html)

2026-03-13 19:36:48

[转发(2) 评论(1)](https://www.sina.cn/news/detail/5276091948205939.html)

黄腿肠：

[真的想给大家安利kimi了（类似ChatGPT） 本来离职之后我就卸载了，但最近接活又下回来了，随时搜索很方便。而且可以让ta出内容逻辑大纲做总结什么的，爱不释手…… 没收钱，也不知道kimi背后是哪家公司🫰🏿纯属办公推荐，可以提高效率，我还有同事用它改PPT 还有就是我最近get到飞书的好了，写 ​](https://www.sina.cn/news/detail/5067066186666345.html)

2024-08-14 00:23:03

[转发(2212) 评论(400)](https://www.sina.cn/news/detail/5067066186666345.html)

互联网的那点事：

[养龙虾关键在养 如果有人已经帮你养好了呢？ 国内全民养虾热了一个多月，各大厂纷纷下场，想让安装更简单 但安装是一回事，很多人装上后依旧一脸懵逼，根本用不起来，今天终于有人来改变这个局面了，让养虾进入下一阶段... 飞书今天发布的 aily，走了一条完全不同的路：不用你养，帮你养好了，直接 ​](https://www.sina.cn/news/detail/5278308699996264.html)

2026-03-19 22:25:22

[转发(37) 评论(11)](https://www.sina.cn/news/detail/5278308699996264.html)

歸藏的AI工具箱：

[试了一下飞书升级的 aily 工作助手，非常强。 它甚至能实现帮你定时地从你整个企业的文档中总结、提炼信息，搜索补充之后生成网页。同时在网页里还有播客，这个一句话就能搞定，太牛了！ 企业在飞书积累的的上下文终于可以释放出他的巨大价值。 介绍一下具体的能力：#ai创造营# 它可以快速帮你整 ​](https://www.sina.cn/news/detail/5244849508848456.html)

2025-12-17 14:30:30

[转发(60) 评论(1)](https://www.sina.cn/news/detail/5244849508848456.html)

阿苏的智能家：

[试了一下飞书升级的 aily 工作助手，非常强[并不简单][并不简单]能实现帮你定时地从你整个企业的文档中总结、提炼信息，搜索补充之后生成网页 ​](https://www.sina.cn/news/detail/5244981300171411.html)

2025-12-17 23:14:12

[转发(116) 评论(212)](https://www.sina.cn/news/detail/5244981300171411.html)

短的发布会：

[上班只需动动嘴？三句话让飞书智能伙伴日理万机#科技数码##飞书##办公软件# http://t.cn/A6Wds2fC ​](https://www.sina.cn/news/detail/4971543768861837.html)

2023-11-24 10:11:04

[转发(0) 评论(1)](https://www.sina.cn/news/detail/4971543768861837.html)

小Lin说：

[新年喜提办公室“新成员”，感谢飞书的抢先体验礼物！是一颗跟安克合作的AI录音豆，小小QQ蛮时尚也蛮可爱～ 它可以中英混记，5米之内都能收音，今天刚首发，大家有啥对这个好奇的体验场景，我去帮大家试试[嘻嘻]#安克AI录音豆# #AI硬件卷成硬币大小# ​](https://www.sina.cn/news/detail/5256756852951442.html)

2026-01-19 11:06:02

[转发(2) 评论(29)](https://www.sina.cn/news/detail/5256756852951442.html)

宝玉xp：

[昨天发的互联网黑话之西游记版 AI 视频制作方法 http://t.cn/AXUtbUxb，有朋友给我留言，说还是太复杂了点，问我有没有简单一点的办法。 在创作过程中，像写剧本、分镜头脚本、画首帧图片这些步骤，确实比较耗时间。可以借助飞书的 aily 工作助手这样的 Agent 来自动化这些步骤，先让 Agent 按照自己 ​](https://www.sina.cn/news/detail/5244473353177603.html)

2025-12-16 13:35:48

[转发(90) 评论(4)](https://www.sina.cn/news/detail/5244473353177603.html)

数字生命卡兹克：

[刚刚，飞书开完了他们的新品发布会。 作为一个飞书死忠粉，很爽。因为他们终于做了两个非常大的升级，把原来的AI助手aliy和飞书妙搭，进行了全面迭代。开始逐渐向一个真正的Agent原生平台看齐了。 先说结论，这次发的新功能还挺多的，有飞书aliy、多维表格Agent、妙搭Agent 、还有OpenClaw插件啥的， ​](https://www.sina.cn/news/detail/5278247734743279.html)

2026-03-19 18:23:08

[转发(30) 评论(5)](https://www.sina.cn/news/detail/5278247734743279.html)

央视新闻调查：

[#北京小伙靠龙虾自主砍价完成购房交易#【#带上龙虾去砍价像开了透视挂#】36小时，能完成一次房产交易吗？在北京，互联网技术主管董劭杰做到了。而他背后的“功臣”，竟是一只养在电脑里的数字“龙虾”（OpenClaw）。 年初，董先生抱着试试看的心态开始“养虾”。面对格局受限、房源分散、政策繁杂等买 ​](https://www.sina.cn/news/detail/5281554584567926.html)

2026-03-28 21:23:21

[转发(640) 评论(550)](https://www.sina.cn/news/detail/5281554584567926.html)

暴食症患者李舜生：

[最能体现腾讯钞能力的一集 3月12日龙虾创始人Peter Steinberger抱怨腾讯抄袭。 3月15日龙虾创始人Peter Steinberger感谢腾讯成为OpenClaw赞助商 ​](https://www.sina.cn/news/detail/5277106252549822.html)

2026-03-16 14:47:17

[转发(360) 评论(164)](https://www.sina.cn/news/detail/5277106252549822.html)

后浪视频：

[【#百度抓虾吧禁止人类发帖引争议#】#百度一贴吧疑全机器人禁止人类发帖# 近日，有网友反映百度贴吧“抓虾吧”出现异常限制，当用户发帖时系统提示“禁止人类发帖”，回帖也显示“禁止人类回帖”，引发公众质疑与热议。 针对此事，后浪视频已联系百度贴吧客服，工作人员表示已对相关情况进行记录核实， ​](https://www.sina.cn/news/detail/5281391517893428.html)

2026-03-28 10:35:24

[转发(123) 评论(158)](https://www.sina.cn/news/detail/5281391517893428.html)

阑夕：

[The Information：腾讯把OpenClaw当成了全村的救星。 这个月腾讯内部同时有8个团队在开发基于OpenClaw的产品，堪称「九子夺嫡」，每个工程师都希望自己参与的项目可以立大功，一举扭转公司在AI行业长期落后的地位。 最早作出反应的是腾讯电脑管家——这是早已边缘化的业务线——的一个产品经理张舒昱 ​](https://www.sina.cn/news/detail/5281414175523099.html)

2026-03-28 12:05:26

[转发(243) 评论(94)](https://www.sina.cn/news/detail/5281414175523099.html)

硬件茶谈：

[这个关于OpenClaw的回答简直太精辟了[努力][努力] ​](https://www.sina.cn/news/detail/5279627368988682.html)

2026-03-23 13:45:17

[转发(46) 评论(55)](https://www.sina.cn/news/detail/5279627368988682.html)

人民日报：

[#普通人养龙虾6大安全建议#【转存！#官方发布安全养龙虾实践指南#】为帮助用户安全使用OpenClaw，国家互联网应急中心、中国网络空间安全协会3月22日联合发布OpenClaw安全使用实践指南，面向普通用户、企业用户、云服务商以及技术开发者等，提出安全防护建议。 其中，对于普通用户的建议包括：使用专用 ​](https://www.sina.cn/news/detail/5279350721350144.html)

2026-03-22 19:26:00

[转发(177) 评论(220)](https://www.sina.cn/news/detail/5279350721350144.html)

封面新闻：

[【#第一批养虾人已经失眠了#：不知道它会偷偷删掉什么】#跟风养龙虾却不知已暴露大量隐私#现在，“养龙虾”热潮之下是两极分化的景象：一边是腾讯大厦楼下近千人排起长龙等待免费安装，二手平台上“代装龙虾”的生意日入斗金；另一边，工信部紧急发布安全预警。有使用者分享，反而是用了OpenClaw的人“ ​](https://www.sina.cn/news/detail/5274670764921099.html)

2026-03-09 21:29:32

[转发(1082) 评论(896)](https://www.sina.cn/news/detail/5274670764921099.html)

宝玉xp：

[企业养虾🦞（OpenClaw），虾住在哪里比虾本身重要 养虾🦞（OpenClaw）这阵风刮得太猛了，不止个人在玩，企业也都在装，生怕落后。 但普遍的情况是：安装容易，用起来难。做电商的公司，问虾上个月的退货率，它跑去网上搜；让它写封催款邮件，它连客户欠了多少钱都不知道。这样的虾，跟鱼缸里的宠 ​](https://www.sina.cn/news/detail/5279592862452831.html)

2026-03-23 11:28:11

[转发(429) 评论(52)](https://www.sina.cn/news/detail/5279592862452831.html)

玉渊谭天：

[【#官方回应如何应对养龙虾的风险# 】#第一批养虾人如何平衡风险# 这几天，开源AI智能体OpenClaw掀起全网 “养龙虾” 热潮。目前，深圳、无锡、合肥等地相继出台“龙虾十条”“龙虾十二条”等措施，鼓励企业部署推广OpenClaw。与此同时，工信部、国家互联网应急中心也先后提示安全风险。从“养龙虾”到 ​](https://www.sina.cn/news/detail/5275355478229068.html)

2026-03-11 18:50:20

[转发(528) 评论(220)](https://www.sina.cn/news/detail/5275355478229068.html)

馋小爷：

[养一只“龙虾”，让AI替你打工：OpenClaw使用指南与好处揭秘 最近，互联网上最火的热点之一，就是“养龙虾”。这里的“龙虾”并非指餐桌上的美味，而是一只红色的、名为 OpenClaw 的开源AI智能体（AI Agent）。从投资人到程序员，甚至法律圈和内容创作者，都在热议如何“养”好这只虾。它被视为继Deep ​](https://www.sina.cn/news/detail/5274491177404361.html)

2026-03-09 09:35:55

[转发(150) 评论(15)](https://www.sina.cn/news/detail/5274491177404361.html)

 

[首页](https://sina.cn/?vt=4)

[导航](https://sina.cn/Index/nav?vt=4)

[反馈](https://lives.sina.cn/live/live?vt=4&id=314&live_mg=sports)

[登录](https://my.sina.cn/?vt=4)



---

### [22] 飞书长出“龙虾钳”：当AI学会在办公软件里“直接干活” 真正的生产力不在模型的聊天框里，而在你每天用的、沉淀了大量信息的 - 掘金 [EXA]
- URL: https://juejin.cn/post/7616586311390576681
- 相关度: 0.71
- 搜索词: OpenClaw 飞书 AI助手 评测
- 发布日期: 2026-03-13T20:27:40.000Z

飞书长出“龙虾钳”：当AI学会在办公软件里“直接干活” 真正的生产力不在模型的聊天框里，而在你每天用的、沉淀了大量信息的 - 掘金

# 飞书长出“龙虾钳”：当AI学会在办公软件里“直接干活”

[跨越心中那座山](https://juejin.cn/user/2209376702312202/posts)

2026-03-13 5 阅读5分钟

真正的生产力不在模型的聊天框里，而在你每天用的、沉淀了大量信息的工作软件里。

“我没有飞书文档/消息/日历权限，请把内容发给我。”

如果你曾尝试在飞书里使用AI助手，大概率听过这句令人沮丧的回复。AI在旁边疯狂进化，人却还在当搬运工：搬文档、搬群聊、搬日程，搬到怀疑人生。

但就在最近，这种“人肉搬运”的尴尬局面被彻底打破了。随着OpenClaw（小龙虾）正式接入飞书，AI终于学会了在办公软件里“直接干活”。

一、从“能聊天”到“能干活”：飞书长出“龙虾钳”

OpenClaw，这款因图标是一只红色龙虾而得名的开源AI智能体工具，最近火爆全球。它最大的特点就是“接管电脑、解放双手”，能直接操作你的电脑、本地运行，还能24小时主动干活。

而飞书作为国内协同办公的头部平台，拥有海量的文档、消息、日历和任务数据。当这两者结合，会发生什么？

答案是：AI不再只是一个聊天机器人，它变成了你的“数字分身”。

在获得你的授权后，OpenClaw可以直接以你的身份看文档找资料、核对日历看档期、理解群聊上下文。你说一句话，它就能伸出“钳子”，直接在飞书里帮你把活儿干了。

二、飞书×OpenClaw：七大场景重塑办公效率

这种深度结合，让飞书从一个单纯的办公工具，升级为了一个“智能工作流中枢”。以下是几个典型的应用场景：

1. 智能会议助手：从记录到产出“一键闭环”

会议是飞书的核心场景，也是效率流失的重灾区。OpenClaw接入后，化身你的专属会议秘书。它不仅能通过飞书会议实时转录，更能智能提炼会议纪要，自动区分发言人、归纳核心结论与待办事项。更强大的是，它能根据讨论内容，自动生成项目计划草案或需求文档框架，并直接创建在对应的飞书云文档中。

1. 动态知识库：让信息主动“找到人”

公司制度、项目文档、产品手册……海量知识沉淀在飞书知识库，但“存而不用”是常态。OpenClaw为知识库注入灵魂。员工在飞书群或文档中提出问题时，OpenClaw可以实时理解问题语境，自动从浩瀚的知识库中检索、关联并推送最相关的文档片段或答案。

1. 流程审批“AI预审”：决策快人一步

飞书审批卡在哪儿？往往是审批人需要时间理解复杂的申请背景。OpenClaw可以扮演“第一道关卡”。当审批单通过飞书发起时，OpenClaw自动介入：核对申请内容与历史数据、公司制度的一致性，识别潜在风险点，并生成一份带有风险提示和关键数据摘要的“AI预审报告”，附在审批流中。

1. 个性化项目播报：信息同步零成本

项目经理无需再手动整理项目日报/周报。OpenClaw深度连接飞书多维表格和任务管理工具，每天定时自动抓取项目关键数据（任务完成率、延期风险、资源占用），并融合项目群的最新讨论，生成结构清晰、重点突出的项目动态播报，自动发布到项目群。

三、技术升级：API配额大幅提升，体验更丝滑

为了配合OpenClaw的接入，飞书近期也进行了技术升级。最显著的变化是API调用额度的大幅提升。

飞书免费版此前的API调用上限为每月1万次，此次升级至每月100万次。这一配额水平不仅完全覆盖个人用户的日常使用，对小型团队而言也绰绰有余。

此外，飞书官方插件的推出解决了社区插件服务不稳定、权限授权繁琐等问题。用户无需再反复复制粘贴内容，AI可以直接读取飞书内的海量上下文，实现更顺畅的沟通。

四、安全提示：隐私与权限的平衡

虽然OpenClaw带来了极大的便利，但用户也需要注意安全风险。由于插件通过飞书接口连接了你的工作数据——消息、文档、日历、联系人，AI能读到的东西理论上就有泄露的可能。

官方强烈建议：暂不适合作为群机器人供多人使用，也不建议用公司的飞书账号接入。建议先用个人账号安全地“玩”起来，等后续安全隔离能力完善后再考虑企业级应用。

结语：当工具学会思考

OpenClaw与飞书的深度融合，远非添加一个聊天机器人那么简单。它通过AI能力将飞书的“人、事、物、知识”全要素有机串联，实现了从“人找信息、人追流程”到“信息找人、流程驱动”的根本性转变。

当工具学会思考，效率革命便已悄然发生。飞书长出“龙虾钳”，正重新定义下一个时代的协同办公。

---

### [23] “ 我把OpenClaw接入飞书后，效率直接开挂了！”_配置_实战_文档 [EXA]
- URL: https://www.sohu.com/a/997163587_624051
- 相关度: 0.57
- 搜索词: OpenClaw 飞书 AI助手 评测
- 发布日期: 2026-03-16T07:05:24.000Z

“ 我把OpenClaw接入飞书后，效率直接开挂了！”_配置_实战_文档

# “ 我把OpenClaw接入飞书后，效率直接开挂了！”

哈喽大家下午好呀！

OpenClaw火的一塌糊涂，国内大厂也纷纷下场"养龙虾"。

*图源网络，侵删

但对于国内大多数用户来说，最方便的就数微信/飞书/钉钉这三个——具体怎么选，就看你的工作文档都放在哪，可以直接给它开权限帮你干活。

以飞书为例，接入OpenClaw就能直接操作飞书多维表格、文档、日历、群聊与任务。

甚至可以设计一整套自动化工作流：比如客户提交需求后，AI 自动创建任务、生成文档大纲、通知负责人、同步到日历，全程不用你手动点一下。

但是想把这套AI 自动办公能力真正用起来、发挥飞书 + OpenClaw 的最大潜力，需要你熟悉飞书功能，更要掌握正确的配置与流程设计方法。

今天就推荐你来免费学这门——

[展开全文](javascript:;)

🔥《OpenClaw X 飞书自动化工作流》实战课

跟着资深 AI 架构师崔皓带你从安装配置、模型对接，到飞书集成、专属机器人开发，全流程手把手教你 0 到 1 吃透 OpenClaw

配置就能搞定，不用啃代码，零基础也能搭出 7×24 小时 AI 虚拟团队，一人撑起全链路工作，真正实现「一人即大厂」，效率翻倍！

价格129.9 元，会员同学免费学，新同学今日扫码就能0元领课学～

4大学习模块，

OpenClaw从入门到精通！

这门《OpenClaw×飞书的自动化工作流》实战课程共4章，内容从OpenClaw核心认知👉工具安装👉飞书实战👉团队搭建，一步步带你由浅入深的掌握OpenClaw，小白也能轻松跟上节奏！

内容全是一线实战干货，分步骤演示教学，每一个操作都有详细讲解，把网上零散、踩坑的教程整合归一，帮你省去99%的试错时间，真正做到学完就能用、用了就提效。

🌟比如：

用大白话讲清“龙虾AI”的核心逻辑，不用懂专业术语，也能知道它到底能帮你做什么、怎么用，再也不用被复杂术语劝退；

手把手教你Windows/Mac双平台安装配置，精准对接DeepSeek等主流模型，扫清安装报错、环境配置的所有坑；

一步步教你完成飞书机器人、插件全流程配置，搭建飞书安全机制，让OpenClaw与飞书深度融合，真正融入日常办公。

除了这些干货内容，课程还有一套完整的《OpenClaw入门实战文档》，帮你扩充对龙虾AI的了解和提高应用技能。

不管你是普通办公族想摆脱复制粘贴、统计报表的重复活，还是创业者想低成本搭建AI团队，这门课的技能都能直接用，刚需又实用！

AIGC实战专家亲授，

你少走 99% 的弯路

学新技能，选对老师太重要！

不然只会瞎琢磨、白踩坑，浪费时间还没效果。

本门课程的授课老师崔皓老师，是深耕AI与分布式架构领域18年的实战派专家，拥有10年分布式架构经验，被全网20w+学员验证过的靠谱讲师。

还曾出版过《LangChain实战》《分布式架构原理与实践》等畅销书。

知道我们小白最容易踩哪些坑、最听不懂哪些内容。

跟着他学，你不用再到处找教程、不用反复踩坑，就能快速掌握OpenClaw全流程操作，轻松实现飞书集成，搭建专属AI虚拟团队，真正实现“一人即大厂”的生产力跃迁。

现在扫码0元 领课，就能跟着老师一起学习OpenClaw的实战方法。

OpenClaw新课持续上新

邀请你来三节课免费学！

除了以上这门课程，三节课目前还有多门OpenClaw的课程。

课程覆盖基础入门、使用技巧、开源部署、企业应用、技术原理等板块，适合不同阶段的同学来学习。

能帮助大家快速了解OpenClaw，以及掌握OpenClaw的使用技巧～ [返回搜狐，查看更多](https://www.sohu.com/?strategyid=00001)

平台声明：该文观点仅代表作者本人，搜狐号系信息发布平台，搜狐仅提供信息存储空间服务。

阅读 ()

 

 

 



---

### [24] 2026年最值得关注的 AI 工具：OpenClaw 全面评测 - OpenClaw官网中文版 [EXA]
- URL: https://www.openclaaw.cn/news/154.html
- 相关度: 0.43
- 搜索词: OpenClaw 飞书 AI助手 评测

2026年最值得关注的 AI 工具：OpenClaw 全面评测 - OpenClaw官网中文版

🎉 OpenClaw 中文版 v0.1.8 已发布，新增飞书推送 & DeepSeek V3 优化 [查看详情 →](https://www.openclaaw.cn/category/news/)

[首页](https://www.openclaaw.cn/)› [最新资讯](https://www.openclaaw.cn/category/news)› 2026年最值得关注的 AI 工具：OpenClaw 全面评测

图：2026年最值得关注的 AI 工具：OpenClaw 全面评测

如果你在2026年只能深度了解一款 AI 工具，OpenClaw 大概率是最值得花时间的那一个。不是因为它最完美，而是因为它正在定义一个全新的 AI 使用范式——一个离普通人生活和工作最近的范式。

本文是目前最完整的 OpenClaw 中文评测，覆盖功能体验、平台集成、安全性、费用结构和适用人群五大维度，最后给出综合评分和明确的使用建议。

## 评测概况

| 评测维度 | 评分（满分10分） | 一句话评价 |
| --- | --- | --- |
| 功能完整度 | ⭐ 9.2 | 同类开源项目中功能边界最宽 |
| 平台集成广度 | ⭐ 9.5 | 20+ 平台无对手，微信支持是加分项 |
| 上手难度 | ⭐ 5.5 | 技术用户流畅，普通用户有门槛 |
| 安全性 | ⭐ 6.0 | 权限宽泛，需用户自行做好配置 |
| 费用性价比 | ⭐ 8.5 | 软件免费，综合成本灵活可控 |
| 社区生态 | ⭐ 9.8 | GitHub 史上最高 Star，社区最活跃 |
| 综合评分 | ⭐ 8.1 | 2026年最值得关注的开源 AI 工具 |

## 维度一：功能完整度（9.2分）

OpenClaw 的功能体系可以用一句话概括：它能做的事情，比你预期的多得多。

在核心功能层面，它覆盖了绝大多数个人和职场 AI 助手的使用场景：

- 邮件管理：扫描收件箱、分类摘要、起草回复、自动发送
- 日程协调：读写日历、设置提醒、协调多方时间
- 信息检索：联网搜索、整理摘要、写入本地笔记库
- 文件操作：读写本地文件、整理归类、格式转换
- 浏览器控制：自动填表、网页内容提取、数据采集
- 定时自动化：Heartbeat 引擎支持无人值守定时任务
- 技能扩展：ClawHub 社区市场持续贡献新技能模块

在模型兼容性方面，OpenClaw 支持超过200种大模型接入，包括 Claude、GPT、DeepSeek、Gemini 及通过 Ollama 运行的本地模型，用户可以按任务类型和成本需求自由切换。

扣分原因：内置 GUI 界面缺失，操作全程依赖命令行或通讯 App 交互，对非技术用户不够直观。部分高级功能的文档仍不完善。

## 维度二：平台集成广度（9.5分）

这是 OpenClaw 最无可争议的优势，也是它区别于所有竞争对手的最大差异化特征。

目前支持的通讯平台超过20个，涵盖：

- 即时通讯：微信（WeChat）、WhatsApp、Telegram、Signal、iMessage（via BlueBubbles）、Line、Zalo
- 团队协作：Slack、Discord、Microsoft Teams、飞书（Feishu）、Mattermost
- 其他平台：IRC、Matrix、Nostr、Twitch、Nextcloud Talk、Synology Chat 等

对于中国用户来说，微信和飞书的支持是极为重要的加分项——这意味着你可以在最熟悉的通讯环境里直接调用 AI 助手，无需安装任何额外 App，无需切换工作场景。

与此同时，OpenClaw 还支持 macOS/iOS/Android 上的语音交互，以及实时 Canvas 渲染界面。跨平台的无缝体验，是目前任何闭源竞品都无法完全复制的。

扣分原因：部分平台（如微信）的集成稳定性受制于第三方接口变动，偶有兼容性问题需要社区维护。

## 维度三：上手难度（5.5分）

这是 OpenClaw 目前最明显的短板，也是它与大众化普及之间最大的障碍。

对于有技术背景的用户（熟悉命令行、了解 Node.js 环境、具备基本的服务器配置能力），上手过程相对顺畅。官方的`openclaw onboard`引导程序覆盖了网关配置、平台绑定和 API 接入的完整流程，30～60分钟内可以跑起来基础版本。

对于普通非技术用户，直接自行安装的难度较高。需要理解 VPS、Node.js 版本管理、API Key 配置等概念，任何一个环节出问题都可能卡住，社区虽然活跃但文档深度不一。

好消息是，这个短板正在被第三方托管平台弥补。Hostinger 的一键部署、DigitalOcean 的安全加固镜像、OpenClawd 的托管方案，都在将 OpenClaw 的使用门槛系统性地降低。对于非技术用户，这些托管方案是当前最推荐的入门路径。

扣分原因：自行部署门槛偏高；官方缺乏面向普通用户的图形化配置界面；中文官方文档尚不完善。

## 维度四：安全性（6.0分）

安全性是 OpenClaw 评测中最需要客观面对的部分。它的能力越强，意味着它掌握的权限越多，潜在的风险也就越大。

已知的主要安全问题包括：

- CVE-2026-25253：安全研究人员披露的远程代码执行漏洞，攻击者可通过诱使用户访问特定网页劫持 OpenClaw 实例
- 恶意技能风险：ClawHub 社区市场中曾发现超过800个恶意技能，部分用于窃取加密货币钱包凭证和系统访问权限；Cisco Talos 团队测试证实部分技能可在用户不知情的情况下执行数据外泄
- 提示注入攻击：当 OpenClaw 处理来自外部的邮件、文档时，恶意内容可能伪装成合法指令欺骗 AI 执行非预期操作
- 暴露实例问题：互联网上存在超过13.5万个配置不当、直接暴露在公网的 OpenClaw 实例

安全风险的根源在于 OpenClaw 的设计哲学：它被设计为一个拥有广泛系统访问权限的自主 Agent，”能力强”和”风险高”是同一枚硬币的两面。

降低风险的关键措施：只安装来源可信的官方或社区认证技能；按需授权而非一次性开放所有权限；不将服务端口直接暴露在公网；定期更新至最新稳定版本；使用托管平台（它们通常会提供额外的安全加固层）。

扣分原因：安全问题客观存在且被主流安全研究机构多次记录，普通用户自行做好安全配置的门槛较高。

## 维度五：费用性价比（8.5分）

从费用结构来看，OpenClaw 提供了市场上最灵活的成本模型：

- 软件本身：完全免费，MIT 开源协议，永久有效
- 大模型 API：按调用量计费，轻度使用约 $5～$15/月，中度使用约 $15～$30/月；选用 DeepSeek 可大幅降低成本；使用本地模型（Ollama）则 API 费用为零
- 运行环境：自有设备托管成本为零；基础 VPS 约 $5～$12/月；托管平台方案约 $10～$50/月

综合来看，轻度用户的月总成本可以控制在 $10～$20 之间，与 ChatGPT Plus 或 Claude Pro 的订阅价格相当甚至更低，但获得的是更强的自主执行能力和数据本地化控制权。

对于高频自动化需求的用户，OpenClaw 的按量计费模式在规模化使用下通常比固定订阅制更经济。

扣分原因：费用结构比固定订阅制复杂，初次使用时成本预估难度较高；服务器运维也有一定的时间成本。

## 维度六：社区生态（9.8分）

这是 OpenClaw 几乎无可挑剔的一个维度。

337,000+ GitHub Star、48,000+ Fork、1,075+ 贡献者、9,574+ 开放 Issue——这些数字背后是一个极度活跃、持续迭代的开发者社区。每周有数百名贡献者提交代码，新技能、新平台支持、安全补丁以极高频率更新。

中文社区同样蓬勃。国内开发者在项目上线后数天内就贡献了中文教程、部署指南和 DeepSeek 适配方案。微博、知乎、V2EX 上的 OpenClaw 讨论持续活跃，”养龙虾”成为一种开发者亚文化。腾讯、字节跳动等大厂内部也有团队在深度研究和基于 OpenClaw 构建产品。

扣分原因：社区规模带来的问题是信息噪音偏高，初学者需要花时间甄别高质量资源与过时教程。

## 综合评分：8.1分——推荐，但要有准备

OpenClaw 是2026年毫无疑问最值得关注的 AI 工具之一，但”值得关注”不等于”适合所有人”。

强烈推荐的用户画像：

- 有一定技术背景（会用命令行、理解 API 概念），想要一个真正能”做事”的私人 AI 助手
- 对数据隐私有要求，不希望对话内容存储在第三方云端
- 日常需要处理大量重复性工作（邮件、日程、信息整理），希望通过自动化释放时间
- 已有 Claude 或 GPT API 订阅，想通过 OpenClaw 大幅扩展其执行能力
- 是开发者或技术爱好者，想深度探索 AI Agent 前沿

暂时不推荐的用户画像：

- 完全没有技术背景，且不愿意花时间学习基础配置知识（建议等待更成熟的一键托管方案）
- 需要在企业核心业务系统中部署，且没有专职的安全团队评估风险
- 只需要偶尔问问 AI 问题，不需要自动化执行能力（直接用 ChatGPT 或 Claude 更划算）

## 如何开始？访问 OpenClaw 官网中文版

如果你已经决定尝试，以下是最推荐的入门路径：

- 普通用户：通过 Hostinger 或 DigitalOcean 一键部署，最省力的起步方式
- 技术用户：访问 [GitHub 仓库](https://github.com/openclaw/openclaw)，运行`npm install -g openclaw@latest && openclaw onboard`开始本地部署
- 所有用户：访问 OpenClaw官网中文版（通过浏览器翻译访问 [openclaw.ai](https://openclaw.ai/)），获取最新官方文档和入门指南

持续关注本站，我们将定期更新 OpenClaw 的中文使用教程、安全配置建议和最新功能解析。

本文评测基于公开资料、社区反馈及已发布的安全研究报告综合整理，信息截至2026年3月28日。评分为编辑主观判断，仅供参考。

[上一篇 非技术用户也能理解的 OpenClaw 工作原理](https://www.openclaaw.cn/news/156.html)

[下一篇 OpenClaw 与 AutoGPT 有什么区别？新手对比指南](https://www.openclaaw.cn/news/158.html)

↑

---

### [25] 2026爆火的OpenClaw（小龙虾）深度测评：普通人的效率神器还是隐形陷阱？ - IT干货 [EXA]
- URL: https://www.sufaith.com/article/112260.html
- 相关度: 0.29
- 搜索词: OpenClaw 飞书 AI助手 评测
- 发布日期: 2026-03-08T13:56:32.000Z

2026爆火的OpenClaw（小龙虾）深度测评：普通人的效率神器还是隐形陷阱？ - IT干货

# 2026爆火的OpenClaw（小龙虾）深度测评：普通人的效率神器还是隐形陷阱？

2026年AI智能体赛道彻底沸腾，而一款代号为OpenClaw、被网友亲切称为“小龙虾”的开源工具，仅凭“能动手干活、不只是给答案”的核心优势，短短数月就在GitHub斩获25万+星标，从极客圈快速渗透到普通职场人、创作者的日常，成为今年最具争议的现象级AI工具[1]。

有人用它实现“指令即完成”，解放双手少加班；也有人因忽视安全风险，导致设备被入侵、数据泄露。作为深耕AI工具测评的博主，我耗时两周深度部署、实测各类场景，从基础认知、实用场景，到隐藏风险、避坑技巧，全方位拆解这只“网红小龙虾”，帮你看清它到底适合谁、该怎么用。

### 一、先搞懂：OpenClaw（小龙虾）到底是什么？

很多人被“小龙虾”的昵称误导，以为它是一款娱乐工具，实则它是由奥地利开发者Peter Steinberger打造的开源、可自托管AI智能体框架[1]，核心定位是“能自动完成全流程任务的数字助手”——区别于ChatGPT、Kimi等“只给思路不执行”的聊天AI，也不同于需要编写规则的传统自动化软件，OpenClaw无需编程基础，普通人用自然语言下达指令，就能让它调用设备权限、操作软件、处理文件[1]。

至于“小龙虾”的昵称由来，很简单：项目图标是红色龙虾钳（Claw）形象，网友顺口称呼至今，即便2026年1月因商标问题，从最初的ClawdBot、Moltbot最终定名为OpenClaw，这个接地气的昵称也一直被沿用[3]。

它的核心基础特性，决定了其普及度：

1. 部署灵活：支持本地电脑、云端服务器、虚拟机部署，个人非商用完全免费，代码公开可查，无强制订阅和隐藏收费[1]；
2. 低门槛上手：经过社区迭代，现已推出可视化一键部署工具，普通人5分钟即可完成安装，支持接入钉钉、飞书、企业微信、微信等国内常用通讯工具，无需额外下载专用APP[1][2]；
3. 功能可扩展：官方技能市场ClawHub拥有超5700个社区贡献技能包，覆盖办公、创作、数据处理等场景，按需安装即可拓展能力，中文适配完善，无语言障碍[1]；
4. 全流程执行：这是它最核心的优势——无需人工干预，能自动完成“指令-操作-结果”的闭环，比如让它整理文件，它会直接打开文件资源管理器，筛选、分类、归档，全程不用碰鼠标[2]。

### 二、实测落地：OpenClaw最实用的4大场景（普通人直接照抄）

很多人装完OpenClaw却闲置，核心是没找对使用场景。实测发现，它对重复、繁琐、耗时的任务适配度拉满，以下4个场景，能直接帮你提升30%-60%效率，新手可直接照抄指令[1][2]。

### 1. 职场办公：打工人的“摸鱼式高效”神器

职场人每天被整理文件、做报表、统计数据等琐事占据大量时间，而这正是OpenClaw的强项：

- 文件与数据自动化：指令示例“把桌面2026年1-2月的截图，按日期分类放进D盘‘工作截图’文件夹”“合并F盘‘2026年2月报表’文件夹里的所有Excel，命名为‘2月总报表.xlsx’保存到桌面”，全程自动执行，10分钟的活1分钟搞定[2]；
- 文档自动生成：读取工作记录、邮件内容，自动提炼关键信息，生成规范的日报、周报，还能完成排版、格式调整、导出，省去手动编辑时间[1]；
- 日程与沟通管理：自动同步日程、设置待办提醒、安排会议，读取工作群消息、邮件，提炼核心事项，避免遗漏重要信息[1]。

### 2. 自媒体/内容创作：专注创意，摆脱基础运营琐事

对于自媒体博主、内容创作者，OpenClaw能包揽基础运营工作，让你聚焦内容创意：

- 素材与选题管理：实时监控行业热点，自动筛选高关注度选题，整理图文、视频素材并分类归档，方便快速查找复用[1]；
- 内容生成与适配：根据关键词自动生成公众号文案、短视频脚本、口播稿，提供初稿框架，还能自动适配不同平台风格，提升发布效率[1]；
- 账号自动化运营：自动监测账号流量、粉丝数据，生成运营报表，自动回复常规评论、私信，单人也能高效运营多个账号[1]。

### 3. 个体经营/自由职业：低成本实现数字化管理

中小商户、自由职业者无需购买专业财务、运营软件，OpenClaw就能实现基础数字化管理，降低人力成本：

- 订单与数据统计：自动整理电商订单、线下营收数据，统计销量、利润、库存，生成经营报表，清晰掌握经营状况[1]；
- 客户与售后维护：自动整理客户信息，生成销售话术，回复常见售后问题，提升客户服务效率[1]；
- 日程规划：自动规划接单、采购、配送日程，设置提醒，避免业务遗漏，让零散工作更有条理[1]。

### 4. 通用场景：提升专注力，实现“降本增效”

本质上，OpenClaw的核心价值的是“解放双手，聚焦核心”——把机械、重复的工作交给AI执行，减少无效耗时，让职场人、创作者、经营者能专注于需要创意、决策、沟通的核心工作，同时降低小型团队的工具使用成本，实现“一人顶多人”的效率提升[1]。

### 三、重点预警：OpenClaw的5大潜在风险，新手必避坑

尽管OpenClaw实用性拉满，但它仍处于发展迭代阶段，加上开源、高权限的特性，存在诸多易被忽视的潜在风险，实测中发现的这些坑，一定要避开[1]。

### 1. 安全漏洞：设备与数据极易被入侵（最核心风险）

为了实现全流程操作，OpenClaw需要获取设备最高系统权限，相当于把电脑“裸奔”暴露在网络中：

- 默认端口暴露：工具默认使用18789端口，大量用户部署时未设置密码、token，未开启防火墙，全网超23万个OpenClaw实例直接裸奔，黑客可轻易访问，操控设备成为“肉鸡”，用于挖矿、DDoS攻击[1]；
- 高危漏洞隐患：已被发现“ClawJacked”远程代码执行漏洞，攻击者只需诱导用户访问恶意网页，就能通过跨站WebSocket劫持控制AI智能体，窃取电脑内的文件、账户密码、API密钥[1]；
- 供应链投毒风险：技能市场曾出现恶意技能包，植入后会悄悄窃取用户隐私、盗取账户信息，普通用户难以辨别[1]。

### 2. 指令误解：操作失控，造成不可逆损失

OpenClaw的AI理解能力尚未成熟，上海科技大学联合研究显示，其“意图误解”维度通过率为0%，模糊指令极易导致操作失控[1]：

- 文件误删/篡改：下达模糊指令后，AI可能错误执行删除、修改操作，比如让“整理邮件”却误删重要邮件，让“归档文件”却删除核心工作资料，甚至多次下达停止指令都无法终止[1]；
- 工作失误风险：职场场景中，可能误发邮件、错误修改报表数据、泄露工作信息，影响职场信誉[1]。

### 3. 隐性成本：看似免费，实则烧钱

OpenClaw本身开源免费，但使用过程中存在隐性成本，容易让普通人踩坑[1][3]：

- 大模型API费用：工具本身不具备AI模型能力，需对接第三方大模型接口（如MiniMax、智谱AI、GPT-4等），免费额度极低，长期使用需按Token计费，若任务复杂、调用频繁，单日API费用可高达数百元[1][2]；
- 部署陷阱：网络上大量付费部署教程、安装服务溢价严重，部分教程内容拼凑，甚至包含恶意配置，导致用户设备更易被入侵[1]。

### 4. 法律与合规风险：职场使用易担责

- 企业数据泄露责任：职场人若在公司电脑部署OpenClaw，因权限过高导致公司商业秘密、客户数据、内部文件泄露，需承担《数据安全法》《反不正当竞争法》对应的民事赔偿，甚至刑事责任[1]；
- 平台账号封禁：部分大模型、办公平台明确禁止通过OpenClaw高频调用服务，已有用户因违规使用，导致Google、Claude关联账号被封禁，连带Gmail、云盘等服务无法使用[1]。

### 5. 硬件与环境误区：无需盲目跟风买Mac Mini

目前网上有传言“装OpenClaw必须用Mac Mini”，实测发现完全没必要[3]：

OpenClaw对硬件要求极低，2020年以后的轻薄本（最低4GB内存、10GB可用硬盘）都能流畅运行，Windows 10/11、macOS 14+、主流Linux发行版均支持[2]。Mac Mini的优势是耗电少、运行稳定，适合24小时开机，但无独立显卡，不适合大型模型训练，普通人用手头的普通电脑即可，无需花冤枉钱买高配[3]。

### 四、新手必看：OpenClaw正确使用指南（避坑+高效）

结合实测经验，总结了一套新手友好的使用指南，既能发挥其效率优势，又能规避风险，建议收藏：

### 1. 安装部署：新手优先选“一键安装”，做好基础防护

- Windows用户：以管理员身份打开PowerShell，复制一键安装命令（国内网络用加速镜像：iwr -useb [https://open-claw.org.cn/install-cn.ps1](https://link.zhihu.com/?target=https%3A//open-claw.org.cn/install-cn.ps1)| iex），等待3-8分钟即可完成安装[2]；
- macOS/Linux用户：打开终端，复制命令（curl -fsSL [https://openclaw.ai/install.sh](https://link.zhihu.com/?target=https%3A//openclaw.ai/install.sh)| bash），等待2-5分钟即可[2]；
- 基础防护：安装完成后，务必设置登录密码，修改默认端口，开启防火墙，避免设备裸奔[1][2]。

### 2. 模型选择：新手优先选“国内云端模型”，降低成本

新手无需纠结本地模型，优先选择国内的MiniMax、智谱AI（性价比高、访问快，有免费额度）；若需处理敏感数据，再考虑切换成本地模型，实现零Token消耗[2]。

### 3. 技能安装：优先选官方/高口碑技能包，拒绝不明来源

技能包优先从官方ClawHub或GitHub高星标项目下载，避免安装不明来源的技能包，防止被植入恶意程序[1][3]；普通人也可自定义简单技能，无需编写复杂代码，只需设置配置文件即可[3]。

### 4. 指令技巧：下达“具体、明确”的指令，避免模糊表述

避免使用“整理一下文件”“帮我做报表”这类模糊指令，尽量细化要求，比如“把桌面所有Word文件按修改日期排序，归档到E盘‘文档备份’文件夹，命名格式为‘日期+文件名’”，减少AI误解的概率[2]。

### 5. 场景限制：这些场景不建议用

处理涉及隐私、机密的文件（如工资表、合同、公司内部资料）时，不建议使用；职场场景中，需提前确认公司规定，避免违规部署，承担法律风险[1]。

### 五、总结：OpenClaw到底值得装吗？

经过两周实测，我的结论是：适合被重复琐事困扰的普通人，但需做好风险防控。

它不是“万能神器”，无法直接帮你赚钱，核心价值是“省时间、降成本”——如果你每天要花1-2小时处理整理文件、统计数据、回复消息等琐事，且能接受一定的学习成本和安全防护操作，那么OpenClaw绝对值得一试；但如果你是纯小白，且经常处理敏感数据、职场环境对设备权限有严格限制，建议谨慎尝试，避免踩坑。

最后提醒：OpenClaw目前仍在快速迭代，2026年2月项目发起者淡出核心开发后，由开源基金会接手运作，后续功能和安全性会持续优化[3]。作为普通人，我们无需盲目跟风，理性看待其价值，让工具服务于我们，而非被工具“绑架”。

如果大家在安装、使用过程中遇到问题，欢迎在评论区留言，我会一一回复，也会持续更新OpenClaw的最新动态和使用技巧～

PS：需要2026年3月最新一键安装完整教程（含国内加速、模型配置）的朋友，评论区扣“小龙虾”，我私发你！

---

### [26] OpenClaw + 飞书集成实战：打造 7×24 小时自动化 AI 助手手把手教你用OpenClaw连接飞书，实现AI - 掘金 [EXA]
- URL: https://juejin.cn/post/7610997893575753762
- 相关度: 0.14
- 搜索词: OpenClaw 飞书 AI助手 评测
- 发布日期: 2026-02-26T20:49:41.000Z

OpenClaw + 飞书集成实战：打造 7×24 小时自动化 AI 助手手把手教你用OpenClaw连接飞书，实现AI - 掘金

# OpenClaw + 飞书集成实战：打造 7×24 小时自动化 AI 助手

[TechFind](https://juejin.cn/user/3528785523116283/posts)

2026-02-27 19 阅读1分钟

你有没有遇到过这种情况：

团队群里每天几十条@你的消息，问的都是重复的问题——"这个接口怎么调？""上次那个配置文件在哪？""部署流程是什么？"你一条条回复，一天下来真正写代码的时间不到 3 小时。

或者你是个人开发者，想让 AI 帮你自动处理飞书里的日常事务——收到消息自动分类、文档自动更新、多维表格自动填数据——但飞书官方的机器人 API 太底层，光是鉴权就要折腾半天。

2026 年了，这些事情不应该还需要手动做。

我最近用 OpenClaw 搭了一套飞书自动化系统，效果超出预期：AI Agent 7×24 小时在线，能自动回复消息、读写飞书文档、操作多维表格，甚至能根据对话内容自动创建任务。整个过程从零到上线，大概 2 小时。

这篇文章把完整流程分享出来，包括踩过的坑。

## 为什么选 OpenClaw 而不是自己写飞书机器人

先回答一个常见问题：飞书有开放平台，为什么不直接用官方 SDK 写机器人？

当然可以。但你需要处理的事情包括：

- 部署 + 进程守护
- 错误重试 + 日志监控
- AI 模型调用 + Prompt 管理
- 对话上下文管理（飞书 API 不帮你记上下文）
- 事件订阅 + 消息解析
- OAuth2 鉴权 + Token 刷新

这些加起来，一个有经验的后端开发者至少要 1-2 周。而且后续维护成本不低——飞书 API 更新、Token 过期、模型切换，每个都是坑。

OpenClaw 的做法不一样。它把飞书当作一个"通道"（Channel），AI Agent 的核心逻辑和通道解耦。你只需要：

1. 写你的 Agent 逻辑（SOUL.md + AGENTS.md）
2. 把 App ID 和 Secret 填到 OpenClaw 配置里
3. 在飞书开放平台创建应用

剩下的鉴权、消息收发、上下文管理、模型调用，OpenClaw 全包了。

| 对比维度 | 自己写飞书机器人 | OpenClaw + 飞书 |
| --- | --- | --- |
| 开发时间 | 1-2 周 | 2 小时 |
| 鉴权处理 | 手动实现 OAuth2 | 自动管理 |
| 上下文管理 | 自己存 Redis/DB | 内置 Session |
| AI 模型 | 自己对接 API | 多模型切换 |
| 文档/表格操作 | 自己封装 API | 内置 MCP 工具 |
| 部署维护 | 自己搞 | 一条命令 |

## 前置准备

开始之前，你需要：

- 飞书开放平台账号（企业版或个人开发者版都行）
- Node.js 18+
- 一台云服务器（推荐 2核4G 起步，跑 OpenClaw Gateway 够用）

服务器选择建议：如果你还没有服务器，腾讯云轻量应用服务器性价比不错，2核4G 的配置跑 OpenClaw 绑绑有余，新用户经常有优惠活动，可以去看看： [腾讯云轻量服务器](https://link.juejin.cn/?target=https%3A%2F%2Fcloud.tencent.com%2Fact%2Fcps%2Fredirect%3Fredirect%3D5765%26cps_key%3Db90065c816c6128e2aa3a4df49b3c259%26utm_source%3Djuejin%26utm_medium%3Darticle%26utm_campaign%3Dtencent-cloud)。如果你更偏好阿里云生态，阿里云 ECS 也是老牌选择： [阿里云服务器](https://link.juejin.cn/?target=https%3A%2F%2Fwww.aliyun.com%2Fminisite%2Fgoods%3FuserCode%3Dlyj25i7z%26utm_source%3Djuejin%26utm_medium%3Darticle%26utm_campaign%3Daliyun)。

## 第一步：创建飞书应用

登录 [飞书开放平台](https://link.juejin.cn/?target=https%3A%2F%2Fopen.feishu.cn%2F)，创建一个企业自建应用。

### 1.1 基本配置

进入应用后台，记下这两个值：

- App Secret（应用凭证页面）
- App ID（应用凭证页面）

### 1.2 开通权限

在"权限管理"中，开通以下权限（按需选择）：

消息相关（必选）：

- `im:chat`— 获取群组信息
- `im:message:send_as_bot`— 以应用身份发送消息
- `im:message`— 获取与发送单聊、群聊消息

文档相关（推荐开通）：

- `drive:drive`— 云空间文件操作
- `wiki:wiki`— 读写知识库
- `docs:doc`— 读写飞书文档

多维表格（推荐开通）：

- `bitable:app`— 读写多维表格

### 1.3 事件订阅

在"事件订阅"中，配置请求地址。OpenClaw 默认监听的 Webhook 路径是：

```
https://你的服务器IP:端口/webhook/feishu

```

订阅以下事件：

- `im.message.receive_v1`— 接收消息事件

### 1.4 发布应用

配置完成后，在"版本管理"中创建版本并提交审核。如果是企业内部应用，管理员直接审批即可。

## 第二步：配置 OpenClaw

假设你已经安装了 OpenClaw（如果没有，参考官方文档`openclaw install`）。

### 2.1 添加飞书通道

在 OpenClaw 的配置中添加飞书通道：

```
openclaw gateway config.patch '{
  "channels": {
    "feishu": {
      "appId": "cli_你的AppID",
      "appSecret": "你的AppSecret",
      "enabled": true
    }
  }
}'

```

### 2.2 配置 Agent

OpenClaw 的 Agent 通过 Markdown 文件定义。创建你的 Agent 工作空间：

```
mkdir -p ~/.openclaw/workspace-mybot

```

写一个`SOUL.md`，定义 Agent 的人格和能力：

```
# SOUL.md - 飞书助手

你是团队的 AI 助手，运行在飞书中。

## 核心职责
- 回答团队成员的技术问题
- 帮助查找和更新飞书文档
- 操作多维表格（查询、新增、更新记录）
- 自动整理会议纪要

## 沟通风格
- 简洁直接，不废话
- 技术问题给代码示例
- 不确定的事情说"我不确定"，不瞎编

```

再写一个`AGENTS.md`，定义工作流程：

```
# AGENTS.md

## 每次收到消息
1. 判断意图：技术问答 / 文档操作 / 表格操作 / 闲聊
2. 技术问答：直接回答，必要时搜索知识库
3. 文档操作：使用 feishu_doc 工具读写
4. 表格操作：使用 feishu_bitable 工具操作
5. 闲聊：简短回复，不浪费 Token

```

### 2.3 启动 Gateway

```
openclaw gateway restart

```

检查状态：

```
openclaw gateway status

```

看到`feishu: connected`就说明飞书通道已经接通了。

## 第三步：实战——让 Agent 操作飞书文档

配置完成后，你的 Agent 已经能在飞书里收发消息了。但真正有价值的是让它操作飞书的文档和数据。

### 3.1 读写飞书文档

在飞书群里对 Agent 说：

"帮我看一下知识库里《部署手册》的内容"

Agent 会自动调用`feishu_wiki`工具搜索知识库，找到文档后用`feishu_doc`读取内容，然后把关键信息返回给你。

你也可以让它更新文档：

"把部署手册里的 Node.js 版本从 18 改成 22"

Agent 会读取文档、找到对应位置、执行更新。整个过程你只需要一句话。

### 3.2 操作多维表格

这是我觉得最实用的功能。假设你有一个"Bug 跟踪"多维表格，包含字段：标题、优先级、负责人、状态。

在群里说：

"帮我在 Bug 表里新增一条：标题'登录页白屏'，优先级 P1，负责人张三"

Agent 会调用`feishu_bitable_create_record`自动创建记录。

查询也一样：

"P1 的 Bug 还有几个没解决？"

Agent 会调用`feishu_bitable_list_records`查询并汇总。

### 3.3 自动化工作流示例

更高级的玩法是结合 Cron 定时任务。比如每天早上 9 点自动生成日报：

```
# AGENTS.md 中添加

## 每日日报（Cron 触发）
1. 读取多维表格中昨天的任务完成情况
2. 读取知识库中的项目进度文档
3. 生成日报摘要
4. 发送到团队群

```

OpenClaw 的 Cron 系统会按时触发，Agent 自动执行整个流程。

## 第四步：部署到生产环境

开发测试没问题后，部署到生产环境需要注意几点。

### 4.1 进程守护

用 systemd 管理 OpenClaw Gateway：

```
# 创建 service 文件
sudo cat  /etc/systemd/system/openclaw.service << 'EOF'
[Unit]
Description=OpenClaw Gateway
After=network.target

[Service]
Type=simple
User=root
ExecStart=/usr/local/bin/openclaw gateway start --foreground
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl enable openclaw
sudo systemctl start openclaw

```

### 4.2 日志监控

OpenClaw 的日志默认输出到 stdout，配合 systemd 可以用`journalctl`查看：

```
journalctl -u openclaw -f

```

### 4.3 安全加固

生产环境务必注意：

- 开启 OpenClaw 的访问日志，监控异常请求
- 定期轮换 Token
- 服务器防火墙只开放必要端口
- 飞书 App Secret 不要硬编码，用环境变量

## 踩坑记录

分享几个我踩过的坑，帮你少走弯路：

### 坑1：飞书事件重复推送

飞书的事件订阅有重试机制——如果你的服务器没有在 3 秒内返回 200，飞书会重发。OpenClaw 内置了去重逻辑（基于 event_id），所以一般不用担心。但如果你自己扩展了 Webhook 处理逻辑，记得加去重。

### 坑2：文档权限问题

Agent 操作飞书文档时，需要文档对应用可见。最简单的做法是把应用添加为文档协作者，或者在知识库设置中给应用开放读写权限。

### 坑3：多维表格字段类型

多维表格的字段类型很多（文本、数字、单选、多选、日期、人员等），创建记录时字段值的格式要匹配。比如"人员"字段需要传`[{"id": "ou_xxx"}]`而不是直接传名字。OpenClaw 的`feishu_bitable_list_fields`工具可以帮你查看字段类型和格式要求。

### 坑4：Token 过期

飞书的 tenant_access_token 有效期 2 小时。OpenClaw 会自动刷新，但如果你的服务器时间不准（比如 NTP 没同步），可能会出现 Token 提前过期的问题。确保服务器时间准确。

## 进阶：钉钉也能接

如果你的团队用钉钉，OpenClaw 同样支持钉钉通道。配置方式类似：

```
openclaw gateway config.patch '{
  "channels": {
    "dingtalk": {
      "appKey": "你的AppKey",
      "appSecret": "你的AppSecret",
      "enabled": true
    }
  }
}'

```

钉钉的权限体系和飞书略有不同，但 Agent 的逻辑完全复用。一套 SOUL.md + AGENTS.md，同时接飞书和钉钉，两个团队都能用。

## 成本分析

很多人关心成本，这里给一个参考：

| 项目 | 月成本 |
| --- | --- |
| 云服务器（2核4G） | ¥40-80/月 |
| AI 模型调用（Claude/GPT） | 按量付费，轻度使用 $5-20/月 |
| 飞书开放平台 | 免费 |
| OpenClaw | 开源免费 |

总成本大概 ¥100-300/月，换来的是一个 7×24 小时在线的 AI 助手。如果能帮团队每人每天省 30 分钟，10 人团队一个月省 100+ 小时，ROI 非常高。

如果你想快速上手 OpenClaw 的完整玩法，我之前整理了一份实战手册，从安装部署到高级用法都有覆盖： [OpenClaw 实战 Playbook](https://link.juejin.cn/?target=https%3A%2F%2Faiagenttools.gumroad.com%2Fl%2Fobdab%3Futm_source%3Djuejin%26utm_medium%3Darticle%26utm_campaign%3Dplaybook)。

## FAQ

Q1：OpenClaw 支持哪些 AI 模型？

主流模型都支持，包括 Claude（Anthropic）、GPT-4o（OpenAI）、Gemini（Google）、DeepSeek 等。可以在配置中指定默认模型，也可以按 Agent 单独配置。

Q2：飞书个人版能用吗？

可以。飞书个人开发者版可以创建应用，功能和企业版基本一致，只是部分高级 API（如审批流）需要企业版。消息收发、文档读写、多维表格操作都没问题。

Q3：一个 OpenClaw 实例能接多少个飞书群？

没有硬性限制。OpenClaw 通过 Session 管理不同的对话，每个群聊是一个独立 Session。实际瓶颈在服务器配置和 AI 模型的并发限制。2核4G 的服务器同时处理 10-20 个群聊没问题。

Q4：消息有延迟吗？

正常情况下，从用户发消息到 Agent 回复，延迟在 2-5 秒（主要是 AI 模型推理时间）。飞书事件推送本身延迟在毫秒级。

Q5：数据安全怎么保证？

所有数据都在你自己的服务器上处理，OpenClaw 不会把数据发到第三方（除了你配置的 AI 模型 API）。飞书的通信走 HTTPS 加密。如果对数据安全要求高，可以部署在内网，用私有化的 AI 模型。

## 总结

OpenClaw + 飞书的组合，本质上是把 AI Agent 的能力注入到你已有的工作流中。不需要团队成员学习新工具，不需要改变现有习惯——在飞书里打字就行，AI 在背后处理一切。

如果你也想搭一个，建议从最简单的场景开始：先让 Agent 能回复消息，再逐步加上文档操作、表格操作、定时任务。两小时入门，后面根据需求慢慢扩展。

有问题欢迎评论区交流。

---

### [27] OpenClaw 很火,但真正适合多数人的,可能是 ToDesk 这只更好上手的“龙虾” [EXA]
- URL: https://www.yeyulingfeng.com/a/474788.html
- 相关度: 0.14
- 搜索词: OpenClaw 飞书 AI助手 评测 analysis review

OpenClaw 很火,但真正适合多数人的,可能是 ToDesk 这只更好上手的“龙虾”

OpenClaw 很火,但真正适合多数人的,可能是 ToDesk 这只更好上手的“龙虾”

2026 开年，中文互联网最热的 AI 关键词之一，基本绕不开OpenClaw。它的官方定位是“个人开源 AI 助手”，推荐通过命令行向导完成 onboarding，Windows 端官方还特别建议走 WSL2；与此同时，中文社区版也在持续做本地化，接入企业微信、飞书、QQ 等渠道。也正因为这样，OpenClaw 一边很火，一边也把很多普通用户挡在了门外：它确实强，但上手门槛并不低。

所以这次我实测 ToDesk 新上线的 ToClaw，最直接的感受不是“它比 OpenClaw 更强”，而是：它把“龙虾”这件事，从技术玩家的玩具，变成了普通办公用户也能直接用的工具。

更重要的是，ToClaw 并不是一个需要单独下载安装的新软件，它已经完全封装在最新版 ToDesk 里。打开 ToDesk 后，在左侧 AI 入口就能找到 ToClaw，免安装、免部署，可直接体验。

# 不是先装环境，而是先开始干活

如果你折腾过 OpenClaw，就会知道它的魅力和门槛几乎是同时出现的。魅力在于它真的是 Agent，不只是聊天；门槛在于你要先理解安装、模型、渠道、权限、运行环境，甚至还得接受“先踩坑，再用起来”这件事，别的不说，光看这个英文文档我就头疼：

而 ToClaw 走的是另一条路。

它已经作为 ToDesk AI 的一部分被放进主界面左侧入口里。打开之后，不是黑乎乎的终端，也不是一堆配置文件，而是一个非常直接的桌面助手界面：输入框、场景入口、技能页、定时任务、记忆与个性、IM 机器人接入，整个逻辑都更像一个已经封装完成的产品，而不是一个等你自己拼起来的开源项目。

说白了，OpenClaw 更像“能力底座”，ToClaw 更像“已经替你铺好路的成品”。

# 它不是聊天框，而是任务入口

这一点其实特别关键。

现在很多 AI 工具都在做“会话体验”，但 ToClaw 明显更想做“任务体验”。首页里能直接看到“热点分析”“AI 投研助理”“智能整理电脑文件”这些入口，说明它不是在等你想提示词，而是在告诉你：你可以直接把事交给我。对大多数办公用户来说，这比“会写一段漂亮文案”更重要。

# 真正拉开差距的，是技能系统

ToClaw 让我觉得有产品完成度的地方，在于它已经不是单一能力，而是有了一套比较明确的技能框架。

在技能页里，已经能看到 Word / DOCX、Excel / XLSX、PDF、PowerPoint / PPTX、Agent Browser 等模块，部分技能还带有“已通过安全与合规验证”的提示。这个信号很明确：ToClaw 不是想做一个万能聊天框，而是想把桌面办公里最常见的文件和网页操作，逐步做成可调用能力。

这就和很多纯网页 AI 拉开了距离。

后者更像“你把材料给我，我帮你生成”；前者更像“我能理解你的任务，并调工具去完成”。当 AI 真正进入桌面，谁更接近真实工作流，谁的留存空间就更大。

# 还有两个小细节，很像“能长期用”的样子

第一个是 定时任务。

实测里已经可以看到按周执行的任务设置，比如定期整理新闻。这意味着 ToClaw 不只是一次性响应，而是在尝试做“持续执行”。很多工具都能帮你写日报，但能不能每周固定帮你做信息汇总，这是两个完全不同的产品阶段。

第二个是 记忆与个性。

ToClaw 现在已经有回答篇幅、语气风格这类预设，比如默认专业、温柔体贴、幽默风趣等。别小看这个功能，它意味着产品开始考虑“长期协作感”了。你不是每次都在调用一个冷冰冰的模型，而是在慢慢调教一个更适合你工作习惯的数字助理。

再加上它已经留出了 企业微信 IM 机器人接入 的位置，这个方向就更清楚了：它显然不只想服务个人，还在往团队协同场景靠。

# 横向看，ToClaw 适合哪类人？

如果你是喜欢折腾、喜欢自己控制全套环境的技术玩家，那 OpenClaw 依然很有吸引力，毕竟开源、自由度高、社区活跃，这些都是它最强的价值。

但如果你是更典型的办公用户——每天要查资料、做报告、整理文件、盯进度、跑远程协作——那 ToClaw 这种“已经长进 ToDesk 体系里”的方案，会现实很多。ToDesk 官网本身就强调跨手机、平板、电脑等多终端兼容，以及围绕远程办公、技术支持、IT 运维的多场景能力，这使得 ToClaw 天然更适合接入真实的多设备工作流。

换句话说，OpenClaw 更像一台性能很猛的改装车；ToClaw 更像一台已经上好牌照、拧钥匙就能开的车。

# 总结

这轮“龙虾热”最大的意义，不是大家突然爱上了某一个 AI 名词，而是越来越多人开始意识到：AI 不该只负责聊天，它应该开始替人干活。

而 ToClaw 值得写的地方，就在于它把这件事往前推了一步。

它没有把自己做成另一个网页对话框，而是做成了 ToDesk 里的桌面任务入口；它没有停留在“写点东西”，而是已经开始覆盖 检索、分析、文件整理、定时执行、个性设置、IM 接入；它也没有一味强调技术酷炫，而是在努力把“龙虾能力”变成普通用户能上手的日常工具。

所以，如果你问我一句话评价 ToClaw：

它不是那种最会炫技的龙虾，但很可能是更适合大多数人真正养起来的一只。

function stop(){ return false; } document.oncontextmenu=stop; -- -- 圣诞飘雪花--

---

### [28] 号称“AI打工人”的OpenClaw值得用吗？_凤凰网 [EXA]
- URL: https://finance.ifeng.com/c/8qyaJ0GwyYq
- 相关度: 0.00
- 搜索词: OpenClaw 飞书 AI助手 评测

号称“AI打工人”的OpenClaw值得用吗？_凤凰网 

- [首页](https://www.ifeng.com/)
- [资讯](https://news.ifeng.com/)
- [视频](https://v.ifeng.com/)
- [直播](https://flive.ifeng.com/)
- [凤凰卫视](https://www.phoenixtv.com/)
- [财经](https://finance.ifeng.com/)
- [娱乐](https://ent.ifeng.com/)
- [体育](https://sports.ifeng.com/)
- [时尚](https://fashion.ifeng.com/)
- [汽车](https://auto.ifeng.com/)
- [房产](https://house.ifeng.com/)
- [科技](https://tech.ifeng.com/)
- [军事](https://mil.ifeng.com/)
- [文化](https://culture.ifeng.com/)
- [旅游](https://travel.ifeng.com/)
- [佛教](https://fo.ifeng.com/)
- [国学](https://guoxue.ifeng.com/)
- [数码](https://tech.ifeng.com/digi/)

[更多](javascript:l)

- [健康](https://health.ifeng.com/)
- [公益](https://gongyi.ifeng.com/)
- [教育](https://edu.ifeng.com/)
- [酒业](https://jiu.ifeng.com/)
- [美食](https://foodnwine.ifeng.com/)

[财经](https://finance.ifeng.com/)> [财经资讯](https://finance.ifeng.com/shanklist/1-64-/)> 正文

# 号称“AI打工人”的OpenClaw值得用吗？

[每日经济新闻](javascript:;)

[2026年02月23日 12:16:11 来自北京](javascript:;)

号称能“接管电脑、解放双手”的AI Agent（AI智能体）工具OpenClaw最近在技术圈火得一塌糊涂。

它被吹捧为“AI打工人”，似乎只要下个指令，它就能替你写文章、发邮件甚至买咖啡。但事实真的如此吗？它是生产力神器，还是仅供技术极客尝鲜的“玩具”？

近日，《每日经济新闻》记者（以下简称每经记者）联合每经科技开发人员，展开了一场深度实测。我们将OpenClaw分别接入千问Qwen3-Max、月之暗面Kimi-K2.5、MiniMax-M2.1、MiniMax-M2.5和智谱GLM-4.7五款国产大模型，以及OpenAI的GPT-5-mini，要求它们完成本地文件检索、网络资料搜索、稿件撰写、发送邮件等步骤，试图揭开这位“指挥官”的真实战力。

实测结果显示，部分模型表现不佳，尤其是在需要操控浏览器的环节，如网络搜索和发送邮件，大多失败。有专家直言，当前的OpenClaw不仅难用、费钱，更是一场安全的“噩梦”。

实测对比：GPT-5、MiniMax、智谱完成任务，另两款大模型“行动力”不足

OpenClaw本身并非大模型，它更像一个“指挥官”，负责接收用户指令、调用工具和组织流程，并将指令理解与具体工作交由其接入的外部大模型来完成。

因此，接入的大模型的能力、稳定性与表达方式，决定了任务的最终成败。

目前OpenClaw支持的大模型（图片来源：OpenClaw配置界面）

为了更贴近记者的真实工作场景，测试人员设定了一项综合性测试任务：

让接入不同大模型的OpenClaw，在电脑中找到对“电车教父”Andy Palmer的采访速记稿，要求它总结文稿内容，并结合搜索到的网络资料，撰写一篇专访新闻稿，最后将新闻稿通过邮件发送到指定邮箱。

这一任务涵盖了指令理解、操控电脑进行本地文件检索、操控浏览器进行网络信息搜索、信息整合和文章写作以及应用操控等多个维度。

在首次测试中，各模型的表现分化显著。

● OpenClaw+千问Qwen3-Max

首先测试的是千问Qwen3-Max模型。该模型在本地文件检索环节便陷入困境。即便测试人员明确提示文件在电脑中的所在位置，Qwen3-Max在经过约5分钟检索后，仍无法准确定位。

在后续单独测试其发送邮件任务时，Qwen3-Max也未能成功执行，只是不断重复指令，但无实际动作。

● OpenClaw+月之暗面Kimi-K2.5

Kimi-K2.5的表现稍好，它在5分钟内成功检索到了文件，并完成内容总结。但在执行网络搜索并补充行业最新热点资讯时，因触发了“429错误”（通常指请求过于频繁），导致未能完成信息搜索工作。

在邮件发送环节，Kimi-K2.5无法成功操控浏览器向指定邮箱发送邮件。

● OpenClaw+MiniMax-M2.1

MiniMax-M2.1在文件检索、网络搜索资料和写作方面没有遇到明显阻碍。邮件发送环节，MiniMax-M2.1在浏览器操控上遇到了困难，但并未就此卡住，而是主动给出了一个可行的解决方案。

测试人员根据其提示手动操作后，成功解决了问题，使其最终能够发送邮件。

不过，MiniMax-M2.1发送的邮件只包含了稿件的“关键引语”，未附上完整的稿件正文。

● OpenClaw+MiniMax-M2.5

虽然都是MiniMax旗下模型，2月12日发布的MiniMax-M2.5，表现比MiniMax-M2.1更好，不仅顺利完成文件检索、网络搜索资料和写作，在发送邮件环节也无需人工介入。

● OpenClaw+智谱GLM-4.7

由于OpenClaw暂未接入智谱于2月12日发布的最新模型GLM-5，所以，本次测试选择了智谱GLM-4.7。

结果显示，在发送邮件环节，智谱GLM-4.7会在浏览器中输入错误的邮箱网址，导致网页访问失败，需要人工提醒更正。

除此之外，智谱GLM-4.7在其他环节处理速度较快。

● OpenClaw+GPT-5-mini

GPT-5-mini的表现较为稳定和流畅。从文件检索、内容总结、网络搜索、资料补充到邮件发送，全流程几乎无需人工干预和额外提示，仅在个别时候出现了网络连接不稳定的情况。

为了保证测试的严谨性，测试人员对整个流程进行了两次复测。

第二轮测试结果：

● Kimi-K2.5：成功检索并读取本地文件，补充网络搜索资料，但在邮件发送环节依旧失败。其报告的错误显示，在读取邮箱网络代码、获取输入框节点时出现问题。

● 千问Qwen3-max：成功读取文件并补充网络资料，但在邮件发送环节出现明显卡顿，未能成功；

● MiniMax-M2.1/2.5：完成任务全部流程。

● 智谱GLM-4.7: 完成任务全部流程。

● GPT-5-mini：完成任务全部流程。

第三轮测试结果：

● Kimi-K2.5：成功检索并读取本地文件，在网络搜索资料环节出现问题（出现读取网页内容错误，错误的网站访问路径，理解不了浏览器控制台指令等），在邮件发送环节依旧失败。

● 千问Qwen3-max：成功读取文件，但无法操控浏览器搜索网络资料，在邮件发送环节依旧失败。

● MiniMax-M2.1/2.5：完成任务全部流程。

● 智谱GLM-4.7: 完成任务全部流程。

● GPT-5-mini：完成任务全部流程。

业内视角：OpenClaw能力上限取决于大模型，尚未成为合格生产力工具

上述测试结论也得到业内普遍印证。

一名使用OpenClaw来辅助运营网店，设计海报、优惠券等宣传物料的程序员告诉每经记者，自己平时都是接入OpenAI的Codex-5.3和Gemini 3 Pro模型，效果比国产大模型好很多。

多位业内人士和资深用户指出，OpenClaw更像一个“任务框架”，其最终表现非常依赖所接入大模型的能力。就像一个指令清晰但能力有限的指挥官，手下士兵（即大模型）的强弱，直接决定了战役的胜败。

非凡产研研究负责人宦家臣向每经记者表示，“模型对OpenClaw的影响其实取决于任务的复杂程度。国际头部大模型上限更高，但是如果都是普通任务，国内的智谱GLM-4.7、Kimi-K2.5都很不错，毕竟Claude太贵了，钱包受不了。”

尽管部分大模型在测试中展现了执行复杂任务的潜力，但OpenClaw离成为一款合格的生产力工具似乎还有不小的距离。

“我感觉，目前版本的OpenClaw并不是一个合格的生产力工具。”前小米OS AI产品专家、现出海AI应用公司ExcelMaster.ai创始人张和在接受每经记者采访时直言，OpenClaw在一定程度上是此前爆火的程序员工具、Anthropic旗下Claude Code的“套壳”，虽然通过聊天界面和内置技能（Skill）做了更好的封装，降低了交互门槛，但在核心能力上并未超越。“我没找到太多OpenClaw能做，而Claude Code做不了的事情。并且，它查询资料的水准，也没有Claude Code好。”

“等大模型能力再跃升一点，OpenClaw就会越来越好，就会越来越普及。哪怕它什么都不做，就等着更新的大模型出来……OpenClaw的门槛就会降低。”张和强调，OpenClaw的进步与普及，本质上是在等待底层大模型技术的突破。

Akamai云和AI产品经理张璐博士也表达了相似的观点。在他看来，OpenClaw若要真正用于生产，还必须经过二次开发和微调，因为目前版本还“有点不成熟，很多时候会卡顿”。

高门槛、高成本和高风险劝退普通用户

除了对大模型能力的依赖，技术门槛、使用成本和安全风险，让OpenClaw目前难以走向普通用户。

首先是较高的部署和使用门槛。OpenClaw目前并未提供类似“一键安装”的简化部署方案，用户需要在电脑上通过命令行操作，完成本地配置、依赖管理以及权限设置。每经科技开发人员表示，整个过程对使用者的技术背景有一定要求，至少需要具备基本的开发经验，这无疑劝退了绝大多数非技术人员。虽然诸如阿里云、腾讯云和亚马逊云等云厂商都提供了OpenClaw云端部署服务并声称可以在他们配置好的服务器上便捷部署OpenClaw，但在云端部署的OpenClaw并不能提供操控用户本地电脑的能力。

高昂的使用成本是另一个现实问题。由于OpenClaw在执行任务时需要频繁调用大模型，token消耗量巨大，堪称“token燃烧器”。有用户向每经记者表示，自己使用智谱GLM-4.7模型，仅仅交互了20多次，就花费了200元。

张璐博士也提到，自己在使用DeepSeek模型时，一天就“烧掉”几十元。如果换成能力更强的模型，账单将更惊人，“一天几百块就出去了”。

高成本使得许多用户只能选择接入免费或更便宜的模型，但这又会影响OpenClaw的实际表现。有用户就向每经记者反映，自己因成本问题选择了Qwen-8B模型，但OpenClaw总是只会回答问题，不会执行操作。

比高门槛和高成本更令人担忧的，是其内在的安全风险。OpenClaw的定位是“做事”而非“聊天”，这意味着它必须获得很高的系统权限，才能操控本地文件和应用。

思科AI威胁研究与安全团队主管Amy Chang直言，从安全角度来看，OpenClaw“是一场噩梦”，它可以在用户的计算机上任意运行shell命令、读写文件和执行脚本。这种高级权限一旦被错误配置或被恶意指令利用，后果不堪设想。

网络安全公司Dvuln的创始人Jamieson O'Reilly也证明了这种风险，他发现OpenClaw存在漏洞，攻击者可借此获取用户数月内的私人消息、账户凭证、API密钥等敏感信息。更可怕的是，用户为了方便AI执行任务而存储的银行账户、加密货币钱包API等信息，都可能以明文形式保存在本地文件中，一旦被黑客入侵，“一秒就可以搬空他们”。

OpenClaw的开发者Peter Steinberger也坦言，这只是一个免费的开源业余项目，需要用户进行仔细的配置才能确保安全。他明确表示：“它并不适合非技术用户。”

免责声明：本文内容与数据仅供参考，不构成投资建议，使用前请核实。据此操作，风险自担。

每日经济新闻

“特别声明：以上作品内容(包括在内的视频、图片或音频)为凤凰网旗下自媒体平台“大风号”用户上传并发布，本平台仅提供信息存储空间服务。

Notice: The content above (including the videos, pictures and audios if any) is uploaded and posted by the user of Dafeng Hao, which is a social media platform and merely provides information storage space services.”

 

关闭

## 亲爱的凤凰网用户:

您当前使用的浏览器版本过低，导致网站不能正常访问，建议升级浏览器

## 第三方浏览器推荐:

谷歌(Chrome)浏览器 [下载](https://www.google.com/chrome/)

360安全浏览器 [下载](https://browser.360.cn/se/)

---
