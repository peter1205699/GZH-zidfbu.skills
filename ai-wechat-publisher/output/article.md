# 一个搜索 API 让 AI 工作流开了挂，接入 5 分钟省下无数小时

事情是这样的。

上周写 Claude Code 那篇文章的时候，我犯了一个错误。

我用 Claude 自带的 WebSearch 去搜集素材，结果 API 报错，搜索全挂了。最后不得不一个个手动抓网页，把 URL 喂给 web reader，一点一点地拼素材。

整个过程花了我快两个小时。

就在那时我想，肯定有更好的办法。

然后我发现了 Tavily。

不是那种「又一个搜索引擎」的发现，是那种「等等，这玩意儿怎么不早点告诉我」的发现。。。

<!-- IMAGE_1: A dramatic visual of a glowing search interface emerging from a sea of dark data streams, bright orange and blue light cutting through darkness, symbolizing the moment of discovery, digital art style, high quality, 16:9 aspect ratio -->

先说它是什么吧。Tavily 是一个专门给 AI 用的搜索 API。

注意，不是给人用的。不是 Google，不是 Bing。它的搜索结果就是给大模型吃的。返回的每一条结果都带内容摘要、相关度评分，格式干净，拿来就能用。

你可能觉得这有什么稀奇的。搜索引擎多了去了，API 谁都能调。

但 Tavily 不一样的地方在于，它围绕 AI agent 的使用场景，做了一整套能力矩阵。

具体来说有五个。

第一个，search。这是最基本的，搜索网页。但跟普通搜索 API 不同的是，它有四种深度模式，从 ultra-fast 到 advanced。快速模式秒回，advanced 模式会深度挖掘，返回更详细的内容。你还能按时间范围过滤，限制域名，搜索新闻主题。

第二个，extract。扔给它一个或多个 URL，它帮你把网页内容提取成干净的 markdown。JavaScript 渲染的页面也能处理。

第三个，crawl。不只是提取一个页面，而是爬取整个网站，按你的需求过滤。比如你可以让它只爬某个网站的 API 文档部分，其他忽略。

第四个，map。如果你不知道网站里有什么页面，先用 map 发现所有 URL。比 crawl 快，适合先摸底再下手。

第五个，也是我觉得最炸的，research。

这个功能相当于帮你做一轮完整的研究。你给它一个主题，它自己从多个角度搜索，收集来源，分析整合，最后给你一份带引用的研究报告。

30 到 120 秒出结果。

怎么说呢，就是把你「打开十个浏览器标签页疯狂搜索然后手动整理笔记」这个过程，压缩到了两分钟以内。

<!-- IMAGE_2: A visual of five distinct glowing modules arranged in a circular pattern around a central core, each module representing a different capability (search, extract, crawl, map, research) with unique icons and colors, connected by light beams, dark background with warm amber and cool blue tones, digital art style, high quality, 16:9 aspect ratio -->

说到这块，我必须讲一下我自己的真实使用体验。

我做的第一件事，就是把 Tavily 接进了我的公众号发布系统。

之前那个系统的第一步是「搜索采集素材」，但一直是个空架子，实际操作全靠我手动搜索。现在呢，我写了一个 research.py 脚本，封装了 Tavily 的搜索、提取和深度研究三个功能。

效果有多明显呢？

写 Claude Code 那篇文章的时候，我用 research 命令跑了一遍「Claude Code 落地实操」这个主题，30 秒不到，搜到了 24 条高质量素材。每条都有标题、URL、内容摘要、相关度评分。

然后我又用 extract 命令深度提取了两篇最核心的文章，拿到了完整的实操指南内容。

整个过程，不到 3 分钟。

上次手动做这件事，花了快两个小时。

坦率的讲，接入也不复杂。Python 里调 Tavily API 就是发一个 POST 请求，把 API Key 和查询参数传过去，JSON 就回来了。我写的那个脚本总共不到 200 行，包含了搜索、提取、深度研究三种模式，还自带去重和排序。

注册 Tavily 账号就能拿到 API Key，免费额度够日常使用。

然后更有意思的事来了。

Tavily 团队做了一个东西叫 Agent Skills。

什么意思呢，他们把 Tavily 的能力打包成了一套标准化的技能模块，可以直接安装到 Claude Code、Cursor、Codex 这些 AI 编程工具里。安装之后，你的 AI agent 就自动拥有了搜索、提取、爬取、研究的能力。

安装就两行命令。

装完之后你不需要任何额外配置，你的 agent 就能自动在合适的时候调用搜索。比如你跟 Claude Code 说「帮我调研一下竞品」，它就会自动用 Tavily 去搜。

这让我想到了一个更大的变化。

以前 AI 的知识是静态的。训练完就固化了，它不知道今天发生了什么事。现在通过搜索 API，AI 可以实时获取信息，知识变成了流动的。

<!-- IMAGE_3: A split visualization showing two worlds, left side shows static frozen bookshelves covered in ice representing static AI knowledge, right side shows flowing streams of data and light representing real-time dynamic knowledge, a glowing bridge connecting the two sides, dramatic contrast between cold blue and warm gold, digital art style, high quality, 16:9 aspect ratio -->

你想想看。

以前的 AI 像一本百科全书，内容再丰富也有出版日期。

现在加了搜索能力的 AI，更像一个能随时上网查资料的研究助手。

这两者的差距，不是 20% 的提升，是质的不同。

但我也得说句实在话。Tavily 不是万能的。

搜索质量取决于你给的查询词。查询词太模糊，返回的结果就一般。英文搜索效果明显好于中文。如果你要做中文内容的深度调研，还是需要配合其他工具。

然后 research 功能虽然方便，但生成的报告还是 AI 综合的结果，可能遗漏一些细节数据。如果你的选题对数据准确性要求很高，最好还是 cross-check 一下原始来源。

不过话说回来，对于一个「帮你快速建立认知框架」的工具来说，Tavily 已经足够好了。先花 3 分钟拿到素材全貌，再花时间精读关键文章，比从零开始大海捞针高效得多。

如果你在做任何跟信息采集有关的工作，不管是写公众号、做市场调研、还是给 AI agent 加实时数据能力，我的建议是，花 5 分钟接入 Tavily 试一下。

不夸张的说，就这一个 API，能让你的信息获取效率翻好几倍。

我自己的感受是，接入之后，我再也不怕写需要大量素材支撑的文章了。以前想到要搜集资料就头疼，现在一个命令跑完，结构化的素材就摆在面前。

这种感觉，就像以前出门靠走路，突然有了自行车。

你还是会走路，但能骑车的时候，谁还走路呢。
