# Project structure: frappe/charts

**Analysed commit:** `7b15424c3af80b1c8e178d8e612c290d2d630904`

**Commit reference:** [7b15424c3af80b1c8e178d8e612c290d2d630904](https://github.com/frappe/charts/commit/7b15424c3af80b1c8e178d8e612c290d2d630904)

**Tree at this commit:** [frappe/charts@7b15424c3af8](https://github.com/frappe/charts/tree/7b15424c3af80b1c8e178d8e612c290d2d630904)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | frappe/charts |
| Description | Simple, responsive, modern SVG Charts with zero dependencies |
| Stars | 15097 |
| Forks | 756 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `7b15424c3af80b1c8e178d8e612c290d2d630904` |
| Retrieved at | 2026-11-14T19:11:40.948667+00:00 |
| Files in this snapshot | 49 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (1 files)
    npm-publish.yml
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
docs/  (10 files)
  assets/  (7 files)
    css/  (3 files)
      … 3 files under this directory
    js/  (4 files)
      … 4 files under this directory
  _config.yml
  docs.html
  index.html
src/  (27 files)
  css/  (2 files)
    charts.scss
    chartsCss.js
  js/  (25 files)
    charts/  (7 files)
      … 7 files under this directory
    objects/  (2 files)
      … 2 files under this directory
    utils/  (14 files)
      … 14 files under this directory
    chart.js
    index.js
.babelrc
.eslintrc.json
.gitignore
.travis.yml
LICENSE
Makefile
README.md
package.json
rollup.config.js
```

## Entry points

- [src/js/index.js](https://github.com/frappe/charts/blob/7b15424c3af80b1c8e178d8e612c290d2d630904/src/js/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| css package | library | Observed | Groups 1 file(s) under css package (observed from repository paths and static analysis). |
| js package | library | Observed | Groups 23 file(s) under js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 2 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.eslintrc.json` (config)
- `.github/workflows/npm-publish.yml` (ci)
- `.travis.yml` (ci)
- `docs/_config.yml` (config)
- `package.json` (manifest)

## Top-level layout

- `src` — 27 analysed file(s)
- `docs` — 10 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `.github` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x generated/minified file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `7b15424c3af80b1c8e178d8e612c290d2d630904` is the revision these paths and observations refer to.
