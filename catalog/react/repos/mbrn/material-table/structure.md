# Project structure: mbrn/material-table

**Analysed commit:** `dc776f55ab38e4a0bd95a827922169bd664e1113`

**Commit reference:** [dc776f55ab38e4a0bd95a827922169bd664e1113](https://github.com/mbrn/material-table/commit/dc776f55ab38e4a0bd95a827922169bd664e1113)

**Tree at this commit:** [mbrn/material-table@dc776f55ab38](https://github.com/mbrn/material-table/tree/dc776f55ab38e4a0bd95a827922169bd664e1113)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | mbrn/material-table |
| Description | Datatable for React based on material-ui's table with additional features |
| Stars | 3479 |
| Forks | 988 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `dc776f55ab38e4a0bd95a827922169bd664e1113` |
| Retrieved at | 2026-11-14T19:15:17.592970+00:00 |
| Files in this snapshot | 48 |

## Directory tree

```text
.github/  (12 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    feature_request.md
    help.md
  actions/  (1 files)
    setup-node
  workflows/  (1 files)
    prettier.yml
  CODEOWNERS
  CODE_OF_CONDUCT.md
  CONTRIBUTING.md
  FUNDING.yml
  ROADMAP.md
  pull_request_template.md
  stale.yml
configs/  (2 files)
  .babelrc
  .eslintrc
demo/  (3 files)
  demo.js
  index.html
  webpack.config.js
src/  (25 files)
  components/  (16 files)
    index.js
    m-table-action.js
    m-table-actions.js
    m-table-body-row.js
    m-table-body.js
    m-table-cell.js
    m-table-edit-cell.js
    m-table-edit-field.js
    m-table-edit-row.js
    m-table-filter-row.js
    m-table-group-row.js
    m-table-groupbar.js
    m-table-header.js
    m-table-pagination.js
    m-table-stepped-pagination.js
    m-table-toolbar.js
  utils/  (5 files)
    polyfill/  (2 files)
      … 2 files under this directory
    common-values.js
    data-manager.js
    index.js
  default-props.js
  index.js
  material-table.js
  prop-types.js
types/  (1 files)
  index.d.ts
.gitignore
.travis.yml
LICENSE
README.md
package.json
```

## Entry points

- [src/components/index.js](https://github.com/mbrn/material-table/blob/dc776f55ab38e4a0bd95a827922169bd664e1113/src/components/index.js)
- [src/index.js](https://github.com/mbrn/material-table/blob/dc776f55ab38e4a0bd95a827922169bd664e1113/src/index.js)
- [src/utils/index.js](https://github.com/mbrn/material-table/blob/dc776f55ab38e4a0bd95a827922169bd664e1113/src/utils/index.js)
- [src/utils/polyfill/index.js](https://github.com/mbrn/material-table/blob/dc776f55ab38e4a0bd95a827922169bd664e1113/src/utils/polyfill/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| components package | library | Observed | Groups 16 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| default-props.js package | library | Observed | Groups 1 file(s) under default-props.js package (observed from repository paths and static analysis). |
| demo package | library | Observed | Groups 2 file(s) under demo package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| material-table.js package | library | Observed | Groups 1 file(s) under material-table.js package (observed from repository paths and static analysis). |
| prop-types.js package | library | Observed | Groups 1 file(s) under prop-types.js package (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 1 file(s) under types package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 5 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/stale.yml` (config)
- `.github/workflows/prettier.yml` (ci)
- `.travis.yml` (ci)
- `package.json` (manifest)

## Top-level layout

- `src` — 25 analysed file(s)
- `.github` — 12 analysed file(s)
- `(root files)` — 5 analysed file(s)
- `demo` — 3 analysed file(s)
- `configs` — 2 analysed file(s)
- `types` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `dc776f55ab38e4a0bd95a827922169bd664e1113` is the revision these paths and observations refer to.
