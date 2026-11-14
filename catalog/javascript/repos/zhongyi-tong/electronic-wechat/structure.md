# Project structure: zhongyi-tong/electronic-wechat

**Analysed commit:** `dc50c871d9b5928234fdf91350ad5a90717804f3`

**Commit reference:** [dc50c871d9b5928234fdf91350ad5a90717804f3](https://github.com/zhongyi-tong/electronic-wechat/commit/dc50c871d9b5928234fdf91350ad5a90717804f3)

**Tree at this commit:** [zhongyi-tong/electronic-wechat@dc50c871d9b5](https://github.com/zhongyi-tong/electronic-wechat/tree/dc50c871d9b5928234fdf91350ad5a90717804f3)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | zhongyi-tong/electronic-wechat |
| Description | :speech_balloon: A better WeChat on macOS and Linux. Built with Electron by Zhongyi Tong. |
| Stars | 13810 |
| Forks | 2645 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `dc50c871d9b5928234fdf91350ad5a90717804f3` |
| Retrieved at | 2026-11-14T19:11:50.398200+00:00 |
| Files in this snapshot | 37 |

## Directory tree

```text
scripts/  (5 files)
  build-all.sh
  build-win32.bat
  build.sh
  qiniu.sh
  tar-all.sh
src/  (21 files)
  handlers/  (3 files)
    menu.js
    message.js
    update.js
  inject/  (6 files)
    badge_count.js
    css.js
    emoji_parser.js
    mention_menu.js
    preload.js
    share_menu.js
  windows/  (8 files)
    controllers/  (4 files)
      … 4 files under this directory
    styles/  (2 files)
      … 2 files under this directory
    views/  (2 files)
      … 2 files under this directory
  common.js
  common_cn.js
  configuration.js
  main.js
.eslintrc
.gitignore
.travis.yml
CHANGELOG.md
CONTRIBUTING.md
ISSUE_TEMPLATE.md
LICENSE.md
README.md
README_zh.md
config.json
package.json
```

## Entry points

- [src/main.js](https://github.com/zhongyi-tong/electronic-wechat/blob/dc50c871d9b5928234fdf91350ad5a90717804f3/src/main.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 7 file(s) under api layer (observed from repository paths and static analysis). |
| common_cn.js package | library | Observed | Groups 1 file(s) under common_cn.js package (observed from repository paths and static analysis). |
| common.js package | library | Observed | Groups 1 file(s) under common.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| configuration.js package | library | Observed | Groups 1 file(s) under configuration.js package (observed from repository paths and static analysis). |
| inject package | library | Observed | Groups 6 file(s) under inject package (observed from repository paths and static analysis). |
| main.js package | library | Observed | Groups 1 file(s) under main.js package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 4 file(s) under scripts package (observed from repository paths and static analysis). |

## Important files

- `.travis.yml` (ci)
- `config.json` (config)
- `package.json` (manifest)

## Top-level layout

- `src` — 21 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `scripts` — 5 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `dc50c871d9b5928234fdf91350ad5a90717804f3` is the revision these paths and observations refer to.
