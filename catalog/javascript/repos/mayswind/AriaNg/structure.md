# Project structure: mayswind/AriaNg

**Analysed commit:** `56d44dc9e822a6f59aae13a542a0cab6cf292d30`

**Commit reference:** [56d44dc9e822a6f59aae13a542a0cab6cf292d30](https://github.com/mayswind/AriaNg/commit/56d44dc9e822a6f59aae13a542a0cab6cf292d30)

**Tree at this commit:** [mayswind/AriaNg@56d44dc9e822](https://github.com/mayswind/AriaNg/tree/56d44dc9e822a6f59aae13a542a0cab6cf292d30)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | mayswind/AriaNg |
| Description | AriaNg, a modern web frontend making aria2 easier to use. |
| Stars | 13274 |
| Forks | 1362 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `56d44dc9e822a6f59aae13a542a0cab6cf292d30` |
| Retrieved at | 2026-11-14T19:11:59.467287+00:00 |
| Files in this snapshot | 111 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (3 files)
    build-non-main-branch.yml
    build-release.yml
    build-snapshot.yml
i18n/  (1 files)
  en.sample.txt
src/  (99 files)
  langs/  (10 files)
    cz_CZ.txt
    de_DE.txt
    es.txt
    fr_FR.txt
    it_IT.txt
    ja_JP.txt
    pl_PL.txt
    ru_RU.txt
    zh_Hans.txt
    zh_Hant.txt
  scripts/  (65 files)
    config/  (10 files)
      … 10 files under this directory
    controllers/  (9 files)
      … 9 files under this directory
    core/  (5 files)
      … 5 files under this directory
    directives/  (12 files)
      … 12 files under this directory
    filters/  (11 files)
      … 11 files under this directory
    services/  (18 files)
      … 18 files under this directory
  styles/  (11 files)
    controls/  (7 files)
      … 7 files under this directory
    core/  (2 files)
      … 2 files under this directory
    theme/  (2 files)
      … 2 files under this directory
  views/  (11 files)
    debug.html
    export-command-api-dialog.html
    list.html
    new.html
    notification-reloadable.html
    setting-dialog.html
    setting.html
    settings-aria2.html
    settings-ariang.html
    status.html
    task-detail.html
  index.html
  robots.txt
.editorconfig
.eslintrc.json
.gitattributes
.gitignore
LICENSE
README.md
gulpfile.js
package.json
```

## Entry points

- [src/scripts/controllers/main.js](https://github.com/mayswind/AriaNg/blob/56d44dc9e822a6f59aae13a542a0cab6cf292d30/src/scripts/controllers/main.js)
- [src/scripts/core/app.js](https://github.com/mayswind/AriaNg/blob/56d44dc9e822a6f59aae13a542a0cab6cf292d30/src/scripts/core/app.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 9 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 11 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 23 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 23 file(s) under service / domain layer (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.eslintrc.json` (config)
- `.github/workflows/build-non-main-branch.yml` (ci)
- `.github/workflows/build-release.yml` (ci)
- `.github/workflows/build-snapshot.yml` (ci)
- `package.json` (manifest)

## Top-level layout

- `src` — 99 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `.github` — 3 analysed file(s)
- `i18n` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `56d44dc9e822a6f59aae13a542a0cab6cf292d30` is the revision these paths and observations refer to.
