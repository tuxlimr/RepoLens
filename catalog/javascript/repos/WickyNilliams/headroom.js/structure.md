# Project structure: WickyNilliams/headroom.js

**Analysed commit:** `0f53fc75f41b0025a80b6075bcdd0d1ea51478be`

**Commit reference:** [0f53fc75f41b0025a80b6075bcdd0d1ea51478be](https://github.com/WickyNilliams/headroom.js/commit/0f53fc75f41b0025a80b6075bcdd0d1ea51478be)

**Tree at this commit:** [WickyNilliams/headroom.js@0f53fc75f41b](https://github.com/WickyNilliams/headroom.js/tree/0f53fc75f41b0025a80b6075bcdd0d1ea51478be)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | WickyNilliams/headroom.js |
| Description | Give your pages some headroom. Hide your header until you need it |
| Stars | 10840 |
| Forks | 794 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `0f53fc75f41b0025a80b6075bcdd0d1ea51478be` |
| Retrieved at | 2026-11-14T19:12:30.383864+00:00 |
| Files in this snapshot | 21 |

## Directory tree

```text
cypress/  (6 files)
  fixtures/  (1 files)
    index.html
  integration/  (1 files)
    headroom.spec.js
  plugins/  (1 files)
    index.js
  support/  (2 files)
    commands.js
    index.js
  .eslintrc
src/  (7 files)
  .eslintrc
  Headroom.js
  angular.headroom.js
  features.js
  jQuery.headroom.js
  scroller.js
  trackScroll.js
.eslintrc
.gitignore
.travis.yml
LICENSE
README.md
cypress.json
package.json
rollup.config.js
```

## Entry points

- [cypress/plugins/index.js](https://github.com/WickyNilliams/headroom.js/blob/0f53fc75f41b0025a80b6075bcdd0d1ea51478be/cypress/plugins/index.js)
- [cypress/support/index.js](https://github.com/WickyNilliams/headroom.js/blob/0f53fc75f41b0025a80b6075bcdd0d1ea51478be/cypress/support/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| angular.headroom.js package | library | Observed | Groups 1 file(s) under angular.headroom.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| cypress package | library | Observed | Groups 3 file(s) under cypress package (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 1 file(s) under external integrations (observed from repository paths and static analysis). |
| features.js package | library | Observed | Groups 1 file(s) under features.js package (observed from repository paths and static analysis). |
| Headroom.js package | library | Observed | Groups 1 file(s) under headroom.js package (observed from repository paths and static analysis). |
| jQuery.headroom.js package | library | Observed | Groups 1 file(s) under jquery.headroom.js package (observed from repository paths and static analysis). |
| scroller.js package | library | Observed | Groups 1 file(s) under scroller.js package (observed from repository paths and static analysis). |
| trackScroll.js package | library | Observed | Groups 1 file(s) under trackscroll.js package (observed from repository paths and static analysis). |

## Important files

- `.travis.yml` (ci)
- `cypress.json` (config)
- `package.json` (manifest)

## Top-level layout

- `(root files)` — 8 analysed file(s)
- `src` — 7 analysed file(s)
- `cypress` — 6 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `0f53fc75f41b0025a80b6075bcdd0d1ea51478be` is the revision these paths and observations refer to.
