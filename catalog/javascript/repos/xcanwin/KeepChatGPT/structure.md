# Project structure: xcanwin/KeepChatGPT

**Analysed commit:** `5cff8fb5b1b57ae37ca3b910a7abe472be7369af`

**Commit reference:** [5cff8fb5b1b57ae37ca3b910a7abe472be7369af](https://github.com/xcanwin/KeepChatGPT/commit/5cff8fb5b1b57ae37ca3b910a7abe472be7369af)

**Tree at this commit:** [xcanwin/KeepChatGPT@5cff8fb5b1b5](https://github.com/xcanwin/KeepChatGPT/tree/5cff8fb5b1b57ae37ca3b910a7abe472be7369af)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | xcanwin/KeepChatGPT |
| Description | 这是一款提高ChatGPT的数据安全能力和效率的插件。并且免费共享大量创新功能，如：自动刷新、保持活跃、数据安全、取消审计、克隆对话、言无不尽、净化页面、展示大屏、拦截跟踪、日新月异、明察秋毫等。让我们的AI体验无比安全、顺畅、丝滑、高效、简洁。 |
| Stars | 14889 |
| Forks | 741 |
| Licence | GPL-2.0 |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `5cff8fb5b1b57ae37ca3b910a7abe472be7369af` |
| Retrieved at | 2026-11-14T19:11:42.358271+00:00 |
| Files in this snapshot | 17 |

## Directory tree

```text
assets/  (1 files)
  logo.svg
docs/  (2 files)
  README_EN.md
  README_ES.md
tests/  (3 files)
  KeepChatGPT.test.js
  dev-server.test.js
  setup.js
tools/  (3 files)
  dev-server.js
  kcg_doc_cdn.py
  kcg_i18n.py
.gitignore
AGENTS.md
CLAUDE.md
KeepChatGPT.dev.user.js
KeepChatGPT.user.js
LICENSE
README.md
package.json
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 3 file(s) under tests (observed from repository paths and static analysis). |
| tools package | library | Observed | Groups 3 file(s) under tools package (observed from repository paths and static analysis). Observed top-level functions: format_json, lang_add, lang_del, main, save. |

## Important files

- `package.json` (manifest)

## Top-level layout

- `(root files)` — 8 analysed file(s)
- `tests` — 3 analysed file(s)
- `tools` — 3 analysed file(s)
- `docs` — 2 analysed file(s)
- `assets` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `5cff8fb5b1b57ae37ca3b910a7abe472be7369af` is the revision these paths and observations refer to.
