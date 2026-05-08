# OpenClaw 研究素材

## 基本信息
- OpenClaw：个人AI助手平台，MIT开源协议
- 创建者：Peter Steinberger
- GitHub仓库：openclaw/openclaw

## 核心架构：四层设计

### 1. Channels（通道层）
- 支持 20+ 消息平台：WhatsApp、Telegram、Slack、Discord、微信、飞书、CLI等
- 用户可在任意平台与同一个AI助手对话
- 统一的消息接收和发送接口

### 2. Brain（大脑层）
- LLM推理引擎：支持多种大语言模型
- Gateway控制面板：ws://127.0.0.1:18789
- Pi agent运行时：任务分解与规划、工具选择与调用
- 多模型切换能力

### 3. Skills（技能层）
- 文件操作、Shell命令执行
- 浏览器控制（Browser Use）
- Live Canvas（实时画布）
- API集成、Webhooks
- Cron定时任务
- Nodes节点系统
- ClawHub技能市场：类似插件商店，可浏览和安装技能

### 4. Memory & Identity（记忆与身份层）
- IDENTITY.md：AI的身份定义
- SOUL.md：AI的"灵魂"设定
- USER.md：用户画像
- MEMORY.md：持久化记忆
- 基于Markdown文件的记忆系统，简单透明

## 其他特性
- Voice Wake：语音唤醒功能
- macOS/iOS/Android原生应用
- 本地优先设计，数据可控

## 竞品对比
- LobeChat：开源AI聊天UI，支持多模型，但更偏向聊天界面
- OpenClaw更注重"全平台个人助手"定位，强调技能扩展和记忆系统
