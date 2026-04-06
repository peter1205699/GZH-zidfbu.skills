# 我用Claude Code十分钟搓了一个公众号自动发布系统

上周有个朋友问我："你公众号文章怎么发的？"我说："让Claude Code帮我写，帮我排版，帮我发到草稿箱。全程我只需要说一句话。"

他觉得我在吹牛。但这是真的。而且整个系统从零搭建到跑通，只花了大概十分钟。

今天就把这个过程拆开给你看。不是炫耀什么——说实话，这事儿真没那么难。难的是你不知道Claude Code有个东西叫**Skills**。

---

<!-- IMAGE_1: A cozy desk setup scene with a laptop screen showing a terminal with green code text, a cup of coffee nearby, and floating holographic interface elements showing "SKILL.md" and WeChat article preview, warm ambient lighting, modern minimalist digital illustration style -->

## 先说说痛点

运营公众号的人都知道这个流程有多折磨：

1. 找选题、搜素材（30分钟起步）
2. 写文章（1-3小时，取决于你的打字速度和拖延症程度）
3. 找配图（要么花钱买图，要么忍受低质量免费图）
4. 排版（公众号编辑器……用过的人都知道）
5. 预览、调整、发布

一篇文章从有想法到发出去，保守估计**2-4小时**。而且大部分时间花在了"搬砖"上——排版、找图、上传这些机械操作。

我就想：这些机械操作能不能自动化？

---

## Skills是什么：给AI一份"操作手册"

Claude Code是Anthropic出品的命令行AI编程工具。你可以把它理解成一个住在终端里的程序员——能读文件、写代码、执行命令。

但默认情况下，它不知道你想要什么。你说"帮我写篇公众号文章"，它可能给你一段纯文本，没有排版，没有配图，更不可能帮你发出去。

**Skills就是解决这个问题的。** 它本质上是一个Markdown文件，叫`SKILL.md`，放在项目目录里。Claude Code启动时会自动扫描这些文件，然后在合适的时机按里面的指令行事。

打个比方：Skills就像给新来的实习生一本SOP手册。不用每次口头交代，他翻开手册就知道该怎么做。

---

<!-- IMAGE_2: A technical blueprint-style diagram showing a flowchart of the article publishing pipeline - left side shows "Topic Input" flowing through "Research" "Writing" "Image Gen" "WeChat API" boxes connected by arrows, each box with small icon, dark blue background with neon cyan connecting lines, clean technical illustration style -->

## 十分钟搭建：从头拆解

整个系统就三个Python脚本加一个SKILL.md文件。结构长这样：

```
ai-wechat-publisher/
├── SKILL.md              # 核心中的核心：定义完整工作流
├── references/
│   └── style-guide.md    # 写作风格指南
└── scripts/
    ├── wechat_api.py     # 微信API封装
    ├── publish.py        # Markdown转HTML+发草稿
    └── image_gen.py      # AI配图生成
```

**第一步：写SKILL.md（5分钟）**

这是最关键的一步。我把整个创作流程拆成了5个步骤写进去：

- 第0步：问用户要什么主题、什么风格
- 第1步：搜索素材
- 第2步：按风格指南生成文章
- 第3步：AI生成配图
- 第4步：自动上传到微信草稿箱

每一步都有具体的指令，比如"用`<!-- IMAGE_N: 描述 -->`标记配图位置"、"调用`python scripts/publish.py`发布"。

Claude Code读到这份文件后，就会严格按流程执行。我说"写一篇关于DeepSeek的文章"，它自动走完全部5步。

**第二步：写辅助脚本（3分钟）**

三个脚本各司其职：

- `wechat_api.py`：封装微信的access_token管理、图片上传、草稿箱操作。最麻烦的是token刷新和中文编码问题，这些踩过的坑都帮你处理了
- `publish.py`：把Markdown转成公众号兼容的内联样式HTML。公众号不支持外部CSS，所以必须逐标签加style
- `image_gen.py`：调用APImart的Gemini图片生成API。异步提交+轮询，生成失败还有fallback占位图兜底

说实话，这三个脚本大部分代码都是Claude Code自己写的。我只告诉它"我需要一个微信API封装"和"图片生成要用异步模式"，它就搞定了。

**第三步：写风格指南（2分钟）**

`style-guide.md`是最被低估的文件。它告诉AI**怎么写才不像AI写的**：

- 禁止用"近日""随着...的发展"开头
- 禁止用"赋能""抓手""底层逻辑"这些互联网黑话
- 要用具体数字，不要说"大幅提升"
- 段落要短，适合手机阅读

这篇文章本身就是在遵守这些规则的前提下生成的。你读到现在，有没有觉得像AI写的？

---

<!-- IMAGE_3: A split-screen comparison showing two workflows - left side shows a frustrated person drowning in browser tabs with scattered documents and image editing tools labeled "Before: 4 hours", right side shows a relaxed person watching a single terminal window with automated progress bar labeled "After: one sentence", warm vs cool color contrast, clean modern illustration style -->

## 实际体验：一句话搞定

现在我的工作流变成了这样：

> 我：写一篇关于Claude Code Skills的文章，通俗易懂风格，3张配图

然后Claude Code自动执行：

1. 搜索Skills相关的最新资料
2. 按`style-guide.md`的风格写文章
3. 用Gemini API生成3张配图
4. 把文章和图片上传到微信草稿箱
5. 告诉我`media_id`，让我去后台确认发布

**从一句话到草稿箱，全程不需要我动手。**

当然，我一般会检查一下内容，改几个措辞，换张不满意的图。但核心工作量从4小时压缩到了十几分钟的微调。

---

## 几个你可能想问的

**Q：配图质量怎么样？**
说实话，不如专业设计师做的。但对于大部分公众号文章来说够用了。而且你可以在SKILL.md里定义配图的风格偏好。

**Q：文章质量靠谱吗？**
取决于你的素材质量和风格指南写得好不好。AI不是凭空创作，它是基于你提供的素材和规则来生成。风格指南越具体，输出越可控。

**Q：这不是作弊吗？**
用WordPress发文章算作弊吗？用Grammarly改语法算作弊吗？工具只是把机械的部分自动化了。选题、角度、观点——这些才是真正有价值的东西。

**Q：我也能做吗？**
能。你需要的东西：一个微信公众号（获取API凭证）、Claude Code（免费就能用）、一个图片生成API（有很多选择）。然后照着我的SKILL.md模板改一改就行。

---

## 关键在于"可复用"

回顾一下这个系统的价值：

**效率是表面。** 真正重要的是，这套流程变成了一个**可复用、可分享、可迭代**的文件。我写好一次SKILL.md，以后每次写文章都能用。我可以把它分享给同事，他们改改风格指南就能用在自己公众号上。

这就是Skills的核心理念：把"怎么做事"的知识，从人脑转移到文件中。

以前，一个资深运营的效率秘诀只存在于他脑子里——他知道什么选题容易爆、什么排版读者爱看、什么标题点击率高。新人来了只能慢慢学。

现在，这些经验可以写进SKILL.md。知识不再跟着人走，而是跟着项目走。

十分钟搓一个工具，换来的是以后每篇文章省4小时。这笔账，怎么算都划算。
