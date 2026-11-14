# Project structure: wangrongding/wechat-bot

**Analysed commit:** `43c6c5075393ca50a430629108251d9be104d5b9`

**Commit reference:** [43c6c5075393ca50a430629108251d9be104d5b9](https://github.com/wangrongding/wechat-bot/commit/43c6c5075393ca50a430629108251d9be104d5b9)

**Tree at this commit:** [wangrongding/wechat-bot@43c6c5075393](https://github.com/wangrongding/wechat-bot/tree/43c6c5075393ca50a430629108251d9be104d5b9)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | wangrongding/wechat-bot |
| Description | 🤖 Multi-platform IM AI Agent for Telegram, WhatsApp, Lark, and WeChat. Connects ChatGPT / Claude / Kimi / DeepSeek / Ollama / Pi for auto-replies, community analysis, contact management, and inactive-friend detection. |
| Stars | 11558 |
| Forks | 1308 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `43c6c5075393ca50a430629108251d9be104d5b9` |
| Retrieved at | 2026-11-14T19:12:16.193917+00:00 |
| Files in this snapshot | 61 |

## Directory tree

```text
.husky/  (1 files)
  pre-commit
.vscode/  (1 files)
  settings.json
docs/  (2 files)
  pi-im-agent.md
  pi-im-agent.zh-CN.md
src/  (45 files)
  302ai/  (2 files)
    __test__.js
    index.js
  adapters/  (5 files)
    lark.js
    opencli.js
    pi.js
    telegram.js
    whatsapp.js
  analysis/  (2 files)
    __test__.js
    wechatAnalyzer.js
  chatgpt/  (1 files)
    index.js
  claude/  (1 files)
    index.js
  config/  (1 files)
    env.js
  deepseek/  (2 files)
    __test__.js
    index.js
  deepseek-free/  (2 files)
    __test__.js
    index.js
  dify/  (2 files)
    __test__.js
    index.js
  doubao/  (2 files)
    __test__.js
    index.js
  kimi/  (2 files)
    __test__.js
    index.js
  ollama/  (2 files)
    __test__.js
    index.js
  openai/  (2 files)
    __test__.js
    index.js
  pi/  (1 files)
    index.js
  platforms/  (9 files)
    lark/  (2 files)
      … 2 files under this directory
    telegram/  (2 files)
      … 2 files under this directory
    wechat/  (3 files)
      … 3 files under this directory
    whatsapp/  (2 files)
      … 2 files under this directory
  tongyi/  (1 files)
    index.js
  utils/  (1 files)
    process.js
  wechaty/  (3 files)
    sendMessage.js
    serve.js
    testMessage.js
  xunfei/  (3 files)
    __test__.js
    index.js
    xunfei.js
  index.js
.dockerignore
.env.example
.gitignore
.prettierrc.cjs
Dockerfile
Dockerfile.alpine
LICENSE.md
README.md
README.zh-CN.md
RECORD.md
cli.js
package.json
```

## Entry points

- [cli.js](https://github.com/wangrongding/wechat-bot/blob/43c6c5075393ca50a430629108251d9be104d5b9/cli.js)
- [src/302ai/index.js](https://github.com/wangrongding/wechat-bot/blob/43c6c5075393ca50a430629108251d9be104d5b9/src/302ai/index.js)
- [src/chatgpt/index.js](https://github.com/wangrongding/wechat-bot/blob/43c6c5075393ca50a430629108251d9be104d5b9/src/chatgpt/index.js)
- [src/claude/index.js](https://github.com/wangrongding/wechat-bot/blob/43c6c5075393ca50a430629108251d9be104d5b9/src/claude/index.js)
- [src/deepseek-free/index.js](https://github.com/wangrongding/wechat-bot/blob/43c6c5075393ca50a430629108251d9be104d5b9/src/deepseek-free/index.js)
- [src/deepseek/index.js](https://github.com/wangrongding/wechat-bot/blob/43c6c5075393ca50a430629108251d9be104d5b9/src/deepseek/index.js)
- [src/dify/index.js](https://github.com/wangrongding/wechat-bot/blob/43c6c5075393ca50a430629108251d9be104d5b9/src/dify/index.js)
- [src/doubao/index.js](https://github.com/wangrongding/wechat-bot/blob/43c6c5075393ca50a430629108251d9be104d5b9/src/doubao/index.js)
- [src/index.js](https://github.com/wangrongding/wechat-bot/blob/43c6c5075393ca50a430629108251d9be104d5b9/src/index.js)
- [src/kimi/index.js](https://github.com/wangrongding/wechat-bot/blob/43c6c5075393ca50a430629108251d9be104d5b9/src/kimi/index.js)
- [src/ollama/index.js](https://github.com/wangrongding/wechat-bot/blob/43c6c5075393ca50a430629108251d9be104d5b9/src/ollama/index.js)
- [src/openai/index.js](https://github.com/wangrongding/wechat-bot/blob/43c6c5075393ca50a430629108251d9be104d5b9/src/openai/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| analysis package | library | Observed | Groups 2 file(s) under analysis package (observed from repository paths and static analysis). |
| 302ai package | library | Observed | Groups 2 file(s) under 302ai package (observed from repository paths and static analysis). |
| chatgpt package | library | Observed | Groups 1 file(s) under chatgpt package (observed from repository paths and static analysis). |
| claude package | library | Observed | Groups 1 file(s) under claude package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| deepseek package | library | Observed | Groups 2 file(s) under deepseek package (observed from repository paths and static analysis). |
| deepseek-free package | library | Observed | Groups 2 file(s) under deepseek-free package (observed from repository paths and static analysis). |
| dify package | library | Observed | Groups 2 file(s) under dify package (observed from repository paths and static analysis). |
| doubao package | library | Observed | Groups 2 file(s) under doubao package (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 5 file(s) under external integrations (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| kimi package | library | Observed | Groups 2 file(s) under kimi package (observed from repository paths and static analysis). |
| ollama package | library | Observed | Groups 2 file(s) under ollama package (observed from repository paths and static analysis). |
| openai package | library | Observed | Groups 2 file(s) under openai package (observed from repository paths and static analysis). |
| pi package | library | Observed | Groups 1 file(s) under pi package (observed from repository paths and static analysis). |
| platforms package | library | Observed | Groups 9 file(s) under platforms package (observed from repository paths and static analysis). |
| tongyi package | library | Observed | Groups 1 file(s) under tongyi package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 1 file(s) under utils package (observed from repository paths and static analysis). |
| wechaty package | library | Observed | Groups 3 file(s) under wechaty package (observed from repository paths and static analysis). |
| xunfei package | library | Observed | Groups 3 file(s) under xunfei package (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.env.example` (config)
- `.vscode/settings.json` (config)
- `Dockerfile` (container)
- `Dockerfile.alpine` (container)
- `package.json` (manifest)

## Top-level layout

- `src` — 45 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `docs` — 2 analysed file(s)
- `.husky` — 1 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `43c6c5075393ca50a430629108251d9be104d5b9` is the revision these paths and observations refer to.
