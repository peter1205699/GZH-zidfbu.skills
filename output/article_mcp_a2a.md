# Anthropic 和 Google 同时出手，AI Agent 的「修路时代」到了

> 🐟 知鱼说：2026 年最值得关注的不是哪个模型更强，而是谁在给 AI Agent 铺路。

最近几个月有一个事，不知道你注意到没有。

*MCP* 和 *A2A*，这两个名字开始在技术文档、开发者论坛甚至招聘 JD 里反复出现。一个来自 Anthropic，一个来自 Google DeepMind。各自推了一个协议，各自解决一个问题。

说实话，一开始我以为又是那种大厂推标准抢地盘的老戏码。

但深挖下去发现，这事比我想的有意思。这两个协议一个管「手」，一个管「嘴」，合在一起正在给 AI Agent 铺一套完整的基础设施。

<!-- IMAGE_1: A futuristic blueprint schematic showing two interconnected protocol layers, one glowing blue layer connecting to tools and databases, one glowing amber layer connecting AI agent nodes to each other, clean technical drawing style with flowing data streams between layers, dark background, digital art style, high quality, 16:9 aspect ratio -->

---

**🔥 先搞清楚一个前提**

聊协议之前，得先说清楚 AI Agent 是什么。

到目前为止，大多数人用 AI 还是「我问你答」模式。你在对话框里打字，模型给你回复。一轮一轮的，像面试。

Agent 不一样。

你给它一个目标，它自己拆任务，自己找工具，自己执行，自己检查，最后把结果交给你。中间可能跑几分钟甚至几小时，全程不用你盯着。

坦率的讲，这玩意到 2025 年下半年才真正开始成熟。之前大家都在喊 Agent，但能稳定跑在生产环境里的几乎没有。原因很简单，Agent 要跟真实世界打交道，得调数据库、读文件、发消息、搜网页。每接一个新系统，就得写一套新的对接代码。

这种对接的混乱和成本，严重拖慢了 Agent 落地的节奏。

直到 MCP 出来。

---

**📊 MCP，给 Agent 装上「手」**

Anthropic 在 2024 年底推出了 *MCP*，全称 *Model Context Protocol*（模型上下文协议）。

听着挺唬人的。说实话我第一次看到这个名字的时候，脑子里蹦出的第一个念头是，又来一个概念要学 。。。但了解之后发现，做的事情特别朴素，就是定了一个统一标准，让所有 AI 模型都用同一种方式连接外部工具和数据。

打个不太精确的比方。以前每买一个新电器，就得配一个不同的充电器。MCP 做的事相当于给 AI 世界做了一个 USB-C 口。只要工具接上这个口，不管什么模型都能用。

从技术上说，MCP 暴露三种能力。*Tools*（工具）让 Agent 能执行动作，调 API、读写文件、发邮件。*Resources*（资源）让 Agent 能访问数据，数据库记录、文档内容。*Prompts*（提示模板）把常用的交互模式封装起来复用。一个 MCP Server 把这些能力暴露出去，一个 MCP Client 去发现和调用，中间走标准的 JSON-RPC 2.0 协议，没什么黑魔法。

到 2026 年初，公开注册的 MCP Server 已经超过一万个。Redis、MongoDB、AWS、Azure、GCP 这些主流云厂商全部接入。连 OpenAI 和 Google 自己的产品也开始兼容 MCP。

一个 Anthropic 推出的协议，最后被所有大厂接受。说实话这事挺离谱的 = =

---

**💡 A2A，让 Agent 之间能「对话」**

MCP 解决了 Agent 连接工具的问题。但还有另一个问题。

如果你有三个 Agent，一个负责调研，一个负责写代码，一个负责测试，它们之间怎么协作？

Google DeepMind 在 2025 年给出了答案，推出了 *A2A*，全称 *Agent-to-Agent*（智能体间通信协议）。

做的事情也很直觉。它定义了一套标准，让不同的 Agent 能够互相发现、委派任务、追踪进度、返回结果。

每个 Agent 发布一张 *Agent Card*（智能体名片），上面写清楚自己能干什么、需要什么输入、返回什么格式。任务从创建到完成有完整的生命周期。长时间运行的任务不用轮询，Agent 可以主动推送状态更新。

这个推送的设计我觉得特别好。在生产环境里，Agent 可能一跑就是十几分钟，你要是一直轮询状态，系统开销受不了。

你可能注意到了，MCP 和 A2A 解决的是完全不同层面的事。MCP 是 Agent 对工具，向下连接基础设施。A2A 是 Agent 对 Agent，横向连接同伴。

<!-- IMAGE_2: A top-down network visualization showing multiple AI agent nodes each surrounded by MCP-connected tools in blue glow, while golden A2A pathways connect agents to each other forming a constellation pattern, flowing data streams between all nodes, dark space background, digital art style, high quality, 16:9 aspect ratio -->

---

**🎯 这事跟你有什么关系**

你可能会说，协议嘛，技术圈的事，跟我有什么关系。

还真有。

2026 年美国招聘市场上有一个数据让我挺意外 ？？？招聘信息中提到 *Agentic AI*（自主代理型 AI）技能的岗位数量增长了超过 **280%**。

280%。

企业不再找「会用 ChatGPT 的人」了。他们在找「能让 AI 自主完成复杂任务的人」。而从「聊天助手」到「自主代理」，中间缺的就是标准化的通信基础设施。

就像互联网需要 HTTP 和 TCP/IP 一样，AI Agent 需要 MCP 和 A2A。

这不是技术人在自嗨。这是整个行业在发生结构性迁移的信号。

---

**⚡ 一个已经跑起来的真实案例**

Anthropic 在 2026 年 4 月推出了 *Claude Managed Agents*，把 MCP 的一整套理念落地成了产品。

怎么理解呢。你在云端定义一个 Agent，给它系统提示词、工具列表、MCP Server 地址，然后直接在云端跑起来。不需要本地机器，不用自己搭 Agent 循环，不用管沙箱环境。

架构拆得很清楚。*Brain*（推理层）负责思考和规划，跑 Claude 模型。*Hands*（执行层）是一个安全沙箱容器，Agent 在里面调工具、跑命令。*Session*（状态层）保存对话历史和工具调用结果，断开了还能重新接上。

我看到了几个真实案例。有人搭了一个每周自动生成 AI 新闻摘要发到 Telegram 的 Agent，跑一整天大概 2.4 美元。有人用它做代码审查，一个 Agent 读代码，一个 Agent 跑测试，各自独立运行再汇总结果。我自己还没真正在生产环境跑过，坦率的讲还在摸索阶段。但方向是很清楚的。

说真的，这种多 Agent 协作的模式，就是 MCP + A2A 在真实世界里的样子。

---

**🔄 回到那个更大的画面**

你想想看，为什么两个竞争对手推出的协议，最后走上了互补而不是对抗的路？

我觉得有一个深层原因。

AI Agent 需要连接的不是一个世界，是两个。一个是工具的世界，数据库、API、文件系统。另一个是其他 Agent 的世界，协调、分工、汇总、互相对齐。

工具是被动响应的，你调用它就给你返回结果。Agent 是主动决策的，它需要知道同伴在干什么、能干什么、现在忙不忙。这两种通信的逻辑完全不同。用一个协议同时解决两种模式，几乎不可能。

所以 MCP 和 A2A 各管一块，反而是最合理的设计。

<!-- IMAGE_3: A dramatic visualization of two protocol layers merging into one expanding wave of light, bottom layer showing structured tool connections in circuit-board pattern, top layer showing autonomous agent nodes in constellation pattern, the merge point creating a bright radiant expansion, blue and gold color scheme, dark background, digital art style, high quality, 16:9 aspect ratio -->

---

说到这个，我突然想起一段历史。

1980 年代，互联网的基础协议栈也是分层的。*TCP* 负责可靠的端到端传输，*IP* 负责寻址和路由。两个协议各管一件事，合在一起构成了整个互联网的通信基础。后来的 HTTP、SMTP、DNS，全部跑在这个基础之上。

MCP 和 A2A 很可能在做同样的事。只不过这次连接的不是电脑，而是 AI Agent。

如果你是开发者，建议很直接。先从 MCP 开始，把你的工具和数据用 MCP Server 暴露出来。涉及多 Agent 协作时再引入 A2A 做编排。

如果你不是开发者，关注一个信号就够了。你所在的公司有没有人在讨论 AI Agent。如果有，MCP 和 A2A 这两个名字迟早会出现在你的工作场景里。

协议不性感。TCP/IP 也不性感。

可你离不了它。

---

> 🐟 **关于知鱼**
>
> 专注 AI 赛道的实战派，不追热点，只讲怎么用。
>
> 如果这篇文章帮到你，点个赞，让更多人看到。