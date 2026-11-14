# Project structure: liyupi/ai-guide

**Analysed commit:** `e3abe9ab41cc1fc1823801fe81c6338217d534f0`

**Commit reference:** [e3abe9ab41cc1fc1823801fe81c6338217d534f0](https://github.com/liyupi/ai-guide/commit/e3abe9ab41cc1fc1823801fe81c6338217d534f0)

**Tree at this commit:** [liyupi/ai-guide@e3abe9ab41cc](https://github.com/liyupi/ai-guide/tree/e3abe9ab41cc1fc1823801fe81c6338217d534f0)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | liyupi/ai-guide |
| Description | 程序员鱼皮的 AI 资源大全 + Vibe Coding 零基础教程，分享 OpenClaw 保姆级教程、大模型玩法（DeepSeek / GPT / Gemini / Claude / GLM）、最新 AI 资讯、Prompt 提示词大全、AI 知识百科（Agent Skills / RAG / MCP / A2A）、AI 编程教程（Harness Engineering）、AI 工具用法（Cursor / Claude Code / TRAE / Codex / Copilot）、AI 开发框架教程（Spring AI / LangChain）、AI 产品变现指南，帮你快速掌握 AI 技… |
| Stars | 22104 |
| Forks | 2406 |
| Licence | Other |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `e3abe9ab41cc1fc1823801fe81c6338217d534f0` |
| Retrieved at | 2026-11-14T19:11:10.131003+00:00 |
| Files in this snapshot | 588 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (2 files)
    deploy.yml
    sync-vibe-coding-course.yml
.vuepress/  (36 files)
  public/  (8 files)
    icon/  (6 files)
      … 6 files under this directory
    BingSiteAuth.xml
    baidu_verify_codeva-hlChwhGcel.html
  scripts/  (5 files)
    formatMdContent.js
    genReadme.js
    generateSidebar.js
    getMdNumber.js
    send-email.js
  sidebars/  (1 files)
    ai.ts
  theme/  (14 files)
    components/  (10 files)
      … 10 files under this directory
    layouts/  (1 files)
      … 1 files under this directory
    styles/  (1 files)
      … 1 files under this directory
    util/  (1 files)
      … 1 files under this directory
    index.js
  config.bundled_1748596791389.mjs
  config.bundled_1768295118604.mjs
  config.bundled_1768295118612.mjs
  config.ts
  extraSideBar.ts
  footer.ts
  navbar.ts
  sidebar.ts
AI/  (190 files)
  AI应用场景/  (34 files)
    AI + 内容创作/  (7 files)
      … 7 files under this directory
    AI + 创意设计/  (7 files)
      … 7 files under this directory
    AI + 办公效率/  (9 files)
      … 9 files under this directory
    AI + 理财/  (4 files)
      … 4 files under this directory
    AI + 编程开发/  (6 files)
      … 6 files under this directory
    README.md
  AI行业资讯/  (106 files)
    2025-02/  (29 files)
      … 29 files under this directory
    2025-03/  (20 files)
      … 20 files under this directory
    2025-04/  (22 files)
      … 22 files under this directory
    2025-05/  (2 files)
      … 2 files under this directory
    2025-06/  (10 files)
      … 10 files under this directory
    2025-07/  (10 files)
      … 10 files under this directory
    2025-08/  (10 files)
      … 10 files under this directory
    2025-09/  (1 files)
      … 1 files under this directory
    2025-10/  (1 files)
      … 1 files under this directory
    2025-11/  (1 files)
      … 1 files under this directory
  AI项目教程/  (6 files)
    AI + Cursor 开发一个亲戚计算器.md
    AI + Cursor 开发一个模拟面试系统.md
    AI + Cursor 开发一个肺活量测试器.md
    AI 海龟汤项目教程.md
    README.md
    🔥 企业级项目：开发 AI 恋爱大师应用 + 拥有自主规划能力的超级智能体.md
  DeepSeek使用指南/  (17 files)
    DeepSeek 提问技巧/  (6 files)
      … 6 files under this directory
    2分钟学会 DeepSeek API，竟然比官方更好用！.md
    DeepSeek 发布新模型 V3-0324，附使用教程.md
    DeepSeek 本地部署教程.md
    README.md
    【汇总】满血版 DeepSeek 第三方使用渠道.md
    几个技巧，教你去除文章的 AI 味！.md
    如何在iPhone上用语音调用Deepseek.md
    完整攻略：如何用好DeepSeek，一文汇总！.md
    普通人能用DeepSeek做什么？20个实用建议.md
    最新清华大学DeepSeek使用手册第1-5版，官方完整版PDF免费下载.md
    🔥DeepSeek 小白快速上手指南.md
  DeepSeek技术解析/  (12 files)
    DeepSeek 技术分析/  (7 files)
      … 7 files under this directory
    DeepSeek 模型训练/  (4 files)
      … 4 files under this directory
    README.md
  DeepSeek资源汇总/  (5 files)
    DeepSeek 学习资料.md
    DeepSeek 官方链接.md
    DeepSeek 开源项目.md
    DeepSeek官方整理的模型应用和工具.md
    README.md
  关于DeepSeek/  (4 files)
    DeepSeek 创始团队介绍.md
    DeepSeek 发展历程.md
    README.md
    什么是 DeepSeek.md
  鱼皮的 AI 指南/  (5 files)
    鱼皮的 AI 指南 - 0、开篇.md
    鱼皮的 AI 指南 - 1、AI 核心概念.md
    鱼皮的 AI 指南 - 2、AI 实用工具.md
    鱼皮的 AI 指南 - 3、AI 编程技巧.md
    鱼皮的 AI 指南 - 4、AI 编程技术.md
  README.md
OpenClaw 保姆级教程/  (19 files)
  00 OpenClaw 保姆级教程导读.md
  01 OpenClaw 是什么.md
  02 本地安装 OpenClaw.md
  03 OpenClaw 一键安装脚本.md
  04 云端部署 OpenClaw.md
  05 OpenClaw 一站式部署平台大全.md
  06 OpenClaw 接入 QQ 和飞书.md
  07 OpenClaw 初始化和基础使用.md
  08 OpenClaw 模型选择与切换.md
  09 OpenClaw 工具管理与多媒体能力.md
  10 OpenClaw Skills 技能系统.md
  11 OpenClaw 定时任务与自动化.md
  12 OpenClaw 多 Agent 协作.md
  13 OpenClaw 记忆管理与成本控制.md
  14 OpenClaw 安全指南.md
  15 OpenClaw 一键卸载脚本.md
  OpenClaw 实战 - 用 GLM-5 打造你的 AI 伴侣.md
  OpenClaw 接入微信保姆级教程.md
  番外 - OpenClaw 创始人的故事.md
Vibe Coding 零基础教程/  (177 files)
  10 编程工具/  (49 files)
    Claude Code/  (6 files)
      … 6 files under this directory
    Codex/  (3 files)
      … 3 files under this directory
    Cursor/  (2 files)
      … 2 files under this directory
    DeepSeek Harness/  (7 files)
      … 7 files under this directory
    工具实战/  (20 files)
      … 20 files under this directory
    00 AI 编程工具大全.md
    01 AI 模型选择指南.md
    02 AI 零代码平台.md
    03 AI 智能体平台.md
    04 AI 代码编辑器.md
    05 AI 命令行编程工具.md
    06 AI IDE 插件.md
    07 OpenClaw 保姆级安装教程.md
    08 AI 辅助工具集.md
    09 我的 AI 工具箱推荐.md
    10 优质 AI 编程扩展推荐.md
  15 模型动态/  (21 files)
    00 模型动态导读.md
    Claude Fable 5 编程能力实测 - 对比 Opus 4.8 和 GPT-5.5.md
    Claude Fable 5.1 编程能力实测 - 3 个项目案例.md
    Claude Opus 5 编程能力实测 - 7 个项目案例.md
    Claude Opus 5.5 双模型横评 - 对比 GPT-6 Sol 实测 5 个案例.md
    DeepSeek V4 Flash Vision 视觉能力实测 - 8 个场景.md
    DeepSeek V4 Pro 编程能力实测 - 7 个项目案例.md
    DeepSeek V4.1 Flash 1017 编程能力实测 - 4 个项目案例.md
    DeepSeek V4.1 Flash 编程能力实测 - 对比 V4 Pro 和 GLM-5.3-Flash.md
    GLM-5.3 三模型横评 - DeepSeek Harness 统一评测.md
    GLM-5.3-Flash 编程能力实测 - 3 个项目案例.md
    GPT Images 2.5 生图能力实测 - 10 个创意玩法.md
    GPT-5.6 三模型横评 - 全栈项目实测.md
    GPT-6 Astra 发布解读 - 跑分、官方案例和争议.md
    GPT-6 Astra 编程能力实测 - 4 个项目案例.md
    Gemini 3.8 Flash 编程能力实测 - 3 个项目案例.md
    Gemini 4 Argon 编程能力实测 - 3 个项目案例.md
    Jev 决策模型实测 - 从入门到实战.md
    Kimi K3 编程能力实测 - 7 个项目案例.md
    Opus 4.8 四模型横评 - 全栈项目实测.md
    小米 MiMo 编程能力实测 - 4 个项目案例.md
  20 项目实战/  (40 files)
    AI 创意应用/  (10 files)
      … 10 files under this directory
    AI 实用工具/  (9 files)
      … 9 files under this directory
    AI 智能体和平台/  (6 files)
      … 6 files under this directory
    AI 跨端应用/  (5 files)
      … 5 files under this directory
    00 Vibe Coding 项目实战导读.md
    01 Vibe Coding 项目开发流程.md
    02 Vibe Coding 个人工具开发.md
    03 Vibe Coding AI 应用开发.md
    04 Vibe Coding 全栈应用开发.md
    05 Vibe Coding 小程序开发.md
    06 项目部署上线教程.md
    10 Vibe Coding 项目灵感大全.md
    进阶 - 企业级 AI 编程实战项目.md
    进阶 - 企业项目开发流程.md
  30 经验技巧/  (20 files)
    大厂 AI 编程经验/  (3 files)
      … 3 files under this directory
    00 Vibe Coding 经验技巧总览.md
    01 Vibe Coding 五大核心心法.md
    02 Vibe Coding 对话工程技巧.md
    03 Vibe Coding 上下文管理技巧.md
    04 Vibe Coding 幻觉和死循环处理.md
    05 Vibe Coding 效率提升技巧.md
    06 Vibe Coding 代码质量保障.md
    07 Vibe Coding 代码重构技巧.md
    08 Vibe Coding 性能优化技巧.md
    09 Vibe Coding 安全防护技巧.md
    10 Vibe Coding 成本控制技巧.md
    11 Vibe Coding 团队协作技巧.md
    12 Vibe Coding 网站美化技巧.md
    Harness Engineering 保姆级教程.md
    Loop Engineering 保姆级教程.md
    用 grill-me 让 AI 拷问你的需求.md
    鱼皮的 AI 工作流分享.md
  40 编程学习/  (16 files)
    01 编程学习路线.md
    02 编程知识百科.md
    03 编程资源大全.md
    04 AI 编程技术.md
    05 AI 绘图指南.md
    06 AI 应用开发面试题.md
    07 程序员简历模板.md
    08 程序员面试刷题.md
    09 程序员工作技巧.md
    10 程序员成长大法.md
    11 编程工具大全.md
    AI 时代新岗位 FDE 前线部署工程师.md
    AI 时代程序员必须做的 20 件事.md
    AI 编程技术栈速查.md
    MCP 服务开发.md
    团队研发规范.md
  50 产品变现/  (19 files)
    00 产品变现导读.md
    01 为什么要做产品变现？.md
    02 需求分析和产品规划.md
    03 文档沉淀和知识管理.md
    04 技术选型实战指南.md
    05 系统架构设计实践.md
    06 项目研发流程选择.md
    07 产品盈利模式设计.md
    08 产品付费策略设计.md
    09 SEO 搜索引擎优化实战.md
    10 GEO 生成式引擎优化实战.md
    云服务安全防护实践.md
    我的 GitHub 涨星涨粉技巧.md
    我的个人站长实战经验.md
    我的自媒体涨粉运营之路.md
    我的自媒体起号经验.md
    系统监控告警实践.md
    网站数据保护实践.md
    网站数据分析实战.md
  70 AI 编程概念大全/  (5 files)
    00 Vibe Coding 概念大全.md
    AI 动态工作流详解.md
    AI 大模型原理入门.md
    Personal Agent 详解.md
    主流 AI 应用开发模式.md
  00 Vibe Coding 简介.md
  01 快速上手 Vibe Coding.md
  02 AI 编程学习路线.md
  60 Vibe Coding 资源大全.md
  65 鱼皮的 AI 编程实战视频课.md
  90 Vibe Coding 常见问题和解决.md
  README.md
translations/  (157 files)
  en/  (156 files)
    Vibe Coding 零基础教程/  (156 files)
      … 156 files under this directory
  zh-TW/  (1 files)
    Vibe Coding 零基础教程/  (1 files)
      … 1 files under this directory
.gitignore
AI 编程学习资源.md
CONTRIBUTING.md
LICENSE
LICENSE-CODE
README.md
package.json
```

## Entry points

- [.vuepress/theme/index.js](https://github.com/liyupi/ai-guide/blob/e3abe9ab41cc1fc1823801fe81c6338217d534f0/.vuepress/theme/index.js)
- [.vuepress/theme/util/index.js](https://github.com/liyupi/ai-guide/blob/e3abe9ab41cc1fc1823801fe81c6338217d534f0/.vuepress/theme/util/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/deploy.yml` (ci)
- `.github/workflows/sync-vibe-coding-course.yml` (ci)
- `package.json` (manifest)

## Top-level layout

- `AI` — 190 analysed file(s)
- `Vibe Coding 零基础教程` — 177 analysed file(s)
- `translations` — 157 analysed file(s)
- `.vuepress` — 36 analysed file(s)
- `OpenClaw 保姆级教程` — 19 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `.github` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `e3abe9ab41cc1fc1823801fe81c6338217d534f0` is the revision these paths and observations refer to.
