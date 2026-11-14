# Project structure: yang991178/fluent-reader

**Analysed commit:** `5912070309759eff37204a5046caba3c780fa4c0`

**Commit reference:** [5912070309759eff37204a5046caba3c780fa4c0](https://github.com/yang991178/fluent-reader/commit/5912070309759eff37204a5046caba3c780fa4c0)

**Tree at this commit:** [yang991178/fluent-reader@591207030975](https://github.com/yang991178/fluent-reader/tree/5912070309759eff37204a5046caba3c780fa4c0)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | yang991178/fluent-reader |
| Description | Modern desktop RSS reader built with Electron, React, and Fluent UI |
| Stars | 9792 |
| Forks | 552 |
| Licence | BSD-3-Clause |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `5912070309759eff37204a5046caba3c780fa4c0` |
| Retrieved at | 2026-11-14T19:13:32.863695+00:00 |
| Files in this snapshot | 146 |

## Directory tree

```text
.github/  (6 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (3 files)
    pages.yml
    release-linux.yml
    release-main.yml
  FUNDING.yml
.vscode/  (2 files)
  launch.json
  settings.json
docs/  (4 files)
  imgs/  (2 files)
    logo.svg
    mac_store.svg
  index.html
  styles.css
src/  (119 files)
  bridges/  (3 files)
    db.ts
    settings.ts
    utils.ts
  components/  (61 files)
    cards/  (7 files)
      … 7 files under this directory
    feeds/  (4 files)
      … 4 files under this directory
    settings/  (25 files)
      … 25 files under this directory
    utils/  (16 files)
      … 16 files under this directory
    article.tsx
    context-menu.tsx
    list-view.tsx
    log-menu.tsx
    menu.tsx
    nav.tsx
    page.tsx
    root.tsx
    settings.tsx
  containers/  (3 files)
    settings/  (3 files)
      … 3 files under this directory
  db/  (1 files)
    schema.ts
  main/  (6 files)
    db.ts
    settings.ts
    touchbar.ts
    update-scripts.ts
    utils.ts
    window.ts
  scripts/  (40 files)
    i18n/  (22 files)
      … 22 files under this directory
    models/  (13 files)
      … 13 files under this directory
    date.ts
    db.ts
    reducer.ts
    settings.ts
    utils.ts
  electron.ts
  index.html
  index.tsx
  preload.ts
  schema-types.ts
tests/  (1 files)
  README.md
.gitattributes
.gitignore
.gitmodules
.prettierignore
.prettierrc.yml
AGENTS.md
LICENSE
README.md
drizzle.config.ts
electron-builder-mas.yml
electron-builder.yml
package.json
tsconfig.json
webpack.config.js
```

## Entry points

- [src/components/page.tsx](https://github.com/yang991178/fluent-reader/blob/5912070309759eff37204a5046caba3c780fa4c0/src/components/page.tsx)
- [src/components/settings/app.tsx](https://github.com/yang991178/fluent-reader/blob/5912070309759eff37204a5046caba3c780fa4c0/src/components/settings/app.tsx)
- [src/index.tsx](https://github.com/yang991178/fluent-reader/blob/5912070309759eff37204a5046caba3c780fa4c0/src/index.tsx)
- [src/scripts/models/app.ts](https://github.com/yang991178/fluent-reader/blob/5912070309759eff37204a5046caba3c780fa4c0/src/scripts/models/app.ts)
- [src/scripts/models/page.ts](https://github.com/yang991178/fluent-reader/blob/5912070309759eff37204a5046caba3c780fa4c0/src/scripts/models/page.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bridges package | library | Observed | Groups 3 file(s) under bridges package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 36 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 52 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 14 file(s) under data layer (observed from repository paths and static analysis). |
| electron.ts package | library | Observed | Groups 1 file(s) under electron.ts package (observed from repository paths and static analysis). |
| index.tsx package | library | Observed | Groups 1 file(s) under index.tsx package (observed from repository paths and static analysis). |
| main package | library | Observed | Groups 6 file(s) under main package (observed from repository paths and static analysis). |
| preload.ts package | library | Observed | Groups 1 file(s) under preload.ts package (observed from repository paths and static analysis). |
| schema-types.ts package | library | Observed | Groups 1 file(s) under schema-types.ts package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 6 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/workflows/pages.yml` (ci)
- `.github/workflows/release-linux.yml` (ci)
- `.github/workflows/release-main.yml` (ci)
- `.prettierrc.yml` (config)
- `.vscode/launch.json` (config)
- `.vscode/settings.json` (config)
- `electron-builder-mas.yml` (config)
- `electron-builder.yml` (config)
- `package.json` (manifest)
- `src/scripts/i18n/cs.json` (config)
- `src/scripts/i18n/de.json` (config)
- `src/scripts/i18n/en-US.json` (config)
- `src/scripts/i18n/es.json` (config)
- `src/scripts/i18n/fi-FI.json` (config)
- `src/scripts/i18n/fr-FR.json` (config)
- `src/scripts/i18n/it.json` (config)
- `src/scripts/i18n/ja.json` (config)
- `src/scripts/i18n/ko.json` (config)
- `src/scripts/i18n/nl.json` (config)
- `src/scripts/i18n/pl.json` (config)
- `src/scripts/i18n/pt-BR.json` (config)
- `src/scripts/i18n/pt-PT.json` (config)
- `src/scripts/i18n/ru.json` (config)
- `src/scripts/i18n/sk.json` (config)
- `src/scripts/i18n/sv.json` (config)
- `src/scripts/i18n/tr.json` (config)
- `src/scripts/i18n/uk.json` (config)
- `src/scripts/i18n/zh-CN.json` (config)
- `src/scripts/i18n/zh-TW.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `src` — 119 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `.github` — 6 analysed file(s)
- `docs` — 4 analysed file(s)
- `.vscode` — 2 analysed file(s)
- `tests` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 25 file(s) were skipped during inventory (25 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `5912070309759eff37204a5046caba3c780fa4c0` is the revision these paths and observations refer to.
