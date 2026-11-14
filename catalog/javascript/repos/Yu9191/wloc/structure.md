# Project structure: Yu9191/wloc

**Analysed commit:** `2644722da7f61256786686983b4fb8500904de8b`

**Commit reference:** [2644722da7f61256786686983b4fb8500904de8b](https://github.com/Yu9191/wloc/commit/2644722da7f61256786686983b4fb8500904de8b)

**Tree at this commit:** [Yu9191/wloc@2644722da7f6](https://github.com/Yu9191/wloc/tree/2644722da7f61256786686983b4fb8500904de8b)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Yu9191/wloc |
| Description | 修改 Apple 网络定位（gs-loc）返回坐标 · 支持 Surge / Quantumult X / Loon / Stash · 快捷指令一键设置/恢复定位 |
| Stars | 10825 |
| Forks | 2672 |
| Licence | AGPL-3.0 |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `2644722da7f61256786686983b4fb8500904de8b` |
| Retrieved at | 2026-11-14T19:12:30.905681+00:00 |
| Files in this snapshot | 20 |

## Directory tree

```text
docs/  (1 files)
  shortcut-guide.md
modules/  (5 files)
  wloc.conf
  wloc.lpx
  wloc.module
  wloc.sgmodule
  wloc.stoverride
worker/  (11 files)
  functions/  (1 files)
    [[route]].js
  src/  (4 files)
    gcj-browser.js
    index.js
    page.js
    parse.js
  test/  (2 files)
    parse.test.mjs
    wloc-stash-output.test.js
  .gitignore
  package.json
  wrangler.jsonc
  wrangler.pages.jsonc
.gitignore
LICENSE
README.md
```

## Entry points

- [worker/src/index.js](https://github.com/Yu9191/wloc/blob/2644722da7f61256786686983b4fb8500904de8b/worker/src/index.js)
- [worker/src/page.js](https://github.com/Yu9191/wloc/blob/2644722da7f61256786686983b4fb8500904de8b/worker/src/page.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 2 file(s) under tests (observed from repository paths and static analysis). |
| worker package | library | Observed | Groups 5 file(s) under worker package (observed from repository paths and static analysis). |

## Important files

- `worker/package.json` (manifest)

## Top-level layout

- `worker` — 11 analysed file(s)
- `modules` — 5 analysed file(s)
- `(root files)` — 3 analysed file(s)
- `docs` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 4 file(s) were skipped during inventory (1 x lockfile excluded; 3 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `2644722da7f61256786686983b4fb8500904de8b` is the revision these paths and observations refer to.
