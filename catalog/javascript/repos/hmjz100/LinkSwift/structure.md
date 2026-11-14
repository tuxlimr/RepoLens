# Project structure: hmjz100/LinkSwift

**Analysed commit:** `192789966834ecffcf21f1d9c96f2849bf6baa59`

**Commit reference:** [192789966834ecffcf21f1d9c96f2849bf6baa59](https://github.com/hmjz100/LinkSwift/commit/192789966834ecffcf21f1d9c96f2849bf6baa59)

**Tree at this commit:** [hmjz100/LinkSwift@192789966834](https://github.com/hmjz100/LinkSwift/tree/192789966834ecffcf21f1d9c96f2849bf6baa59)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | hmjz100/LinkSwift |
| Description | 一个基于 JavaScript 的网盘文件下载地址获取工具。基于【网盘直链下载助手】修改 ，支持 百度网盘 / 阿里云盘 / 中国移动云盘 / 天翼云盘 / 迅雷云盘 / 夸克网盘 / UC网盘 / 123云盘 八大网盘 |
| Stars | 39861 |
| Forks | 2877 |
| Licence | AGPL-3.0 |
| Language | JavaScript |
| Default branch | dev |
| Analysed commit | `192789966834ecffcf21f1d9c96f2849bf6baa59` |
| Retrieved at | 2026-11-14T19:10:40.960839+00:00 |
| Files in this snapshot | 19 |

## Directory tree

```text
.github/  (5 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.yml
    config.yml
    feature_request.yml
  CODE_OF_CONDUCT.md
  contributing.md
config/  (6 files)
  ali.json
  config.json
  quark.json
  tianyi.json
  xunlei.json
  yidong.json
.gitattributes
.gitignore
LICENSE
README-ScriptCat.md
README.md
eslint.config.mjs
package.json
（改）百度网盘会员青春版.user.js
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |

## Important files

- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `config/ali.json` (config)
- `config/config.json` (config)
- `config/quark.json` (config)
- `config/tianyi.json` (config)
- `config/xunlei.json` (config)
- `config/yidong.json` (config)
- `package.json` (manifest)

## Top-level layout

- `(root files)` — 8 analysed file(s)
- `config` — 6 analysed file(s)
- `.github` — 5 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x generated/minified file excluded).
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `192789966834ecffcf21f1d9c96f2849bf6baa59` is the revision these paths and observations refer to.
