# Project structure: pqina/filepond

**Analysed commit:** `2a2e2871f2fe1428bec102857d3fb5d8b2877aff`

**Commit reference:** [2a2e2871f2fe1428bec102857d3fb5d8b2877aff](https://github.com/pqina/filepond/commit/2a2e2871f2fe1428bec102857d3fb5d8b2877aff)

**Tree at this commit:** [pqina/filepond@2a2e2871f2fe](https://github.com/pqina/filepond/tree/2a2e2871f2fe1428bec102857d3fb5d8b2877aff)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | pqina/filepond |
| Description | 🌊 A flexible and fun JavaScript file upload library |
| Stars | 16396 |
| Forks | 851 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `2a2e2871f2fe1428bec102857d3fb5d8b2877aff` |
| Retrieved at | 2026-11-14T19:11:33.269197+00:00 |
| Files in this snapshot | 298 |

## Directory tree

```text
.github/  (4 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.yml
    config.yml
    feature_request.yml
  FUNDING.yml
locale/  (48 files)
  am-et.js
  ar-ar.js
  az-az.js
  ca-ca.js
  cs-cz.js
  cy-cy.js
  da-dk.js
  de-de.js
  el-el.js
  en-en.js
  es-es.js
  et-ee.js
  fa_ir.js
  fi-fi.js
  fr-fr.js
  he-he.js
  hr-hr.js
  hu-hu.js
  id-id.js
  it-it.js
  ja-ja.js
  km-km.js
  ko-kr.js
  ku-ckb.js
  … 24 more files
src/  (227 files)
  css/  (22 files)
    assistant.css
    browser.css
    data.css
    drip.css
    drop-label.css
    file-action-button.css
    file-info.css
    file-status.css
    file-wrapper.css
    file.css
    hopper.css
    item-order.css
    item.css
    list-scroller.css
    list.css
    modifiers.css
    panel-root.css
    panel.css
    progress-indicator.css
    root-order.css
    root.css
    styles.css
  js/  (205 files)
    __tests__/  (10 files)
      … 10 files under this directory
    app/  (96 files)
      … 96 files under this directory
    utils/  (92 files)
      … 92 files under this directory
    createApp.js
    createAppAPI.js
    createAppAtElement.js
    createAppObject.js
    createAppPlugin.js
    filter.js
    index.js
types/  (2 files)
  index.d.ts
  tsconfig.json
.babelrc
.gitattributes
.gitignore
.nvmrc
.prettierignore
.prettierrc
CHANGELOG.md
LICENSE
README.md
banner-cli.js
banner.js
index.html
jest.config.js
jest.stubs.js
package.json
rollup.config.js
rollup.scripts.js
```

## Entry points

- [src/js/app/index.js](https://github.com/pqina/filepond/blob/2a2e2871f2fe1428bec102857d3fb5d8b2877aff/src/js/app/index.js)
- [src/js/index.js](https://github.com/pqina/filepond/blob/2a2e2871f2fe1428bec102857d3fb5d8b2877aff/src/js/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 6 file(s) under core modules (observed from repository paths and static analysis). |
| js package | library | Observed | Groups 204 file(s) under js package (observed from repository paths and static analysis). |
| locale package | library | Observed | Groups 48 file(s) under locale package (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 1 file(s) under types package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `package.json` (manifest)
- `types/tsconfig.json` (config)

## Top-level layout

- `src` — 227 analysed file(s)
- `locale` — 48 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `.github` — 4 analysed file(s)
- `types` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `2a2e2871f2fe1428bec102857d3fb5d8b2877aff` is the revision these paths and observations refer to.
