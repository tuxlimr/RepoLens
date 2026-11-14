# Project structure: atomiks/tippyjs

**Analysed commit:** `ad85f6feb79cf6c5853c43bf1b2a50c4fa98e7a1`

**Commit reference:** [ad85f6feb79cf6c5853c43bf1b2a50c4fa98e7a1](https://github.com/atomiks/tippyjs/commit/ad85f6feb79cf6c5853c43bf1b2a50c4fa98e7a1)

**Tree at this commit:** [atomiks/tippyjs@ad85f6feb79c](https://github.com/atomiks/tippyjs/tree/ad85f6feb79cf6c5853c43bf1b2a50c4fa98e7a1)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | atomiks/tippyjs |
| Description | Tooltip, popover, dropdown, and menu library |
| Stars | 12228 |
| Forks | 538 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `ad85f6feb79cf6c5853c43bf1b2a50c4fa98e7a1` |
| Retrieved at | 2026-11-14T19:12:08.488416+00:00 |
| Files in this snapshot | 184 |

## Directory tree

```text
.config/  (6 files)
  .prettierignore
  babel.config.js
  eslint.config.js
  jest-puppeteer.config.js
  jest.config.js
  rollup.config.js
.github/  (6 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    config.yml
    feature_request.md
  workflows/  (2 files)
    cd.yml
    ci.yml
  FUNDING.yml
headless/  (1 files)
  package.json
src/  (43 files)
  addons/  (2 files)
    createSingleton.ts
    delegate.ts
  plugins/  (4 files)
    animateFill.ts
    followCursor.ts
    inlinePositioning.ts
    sticky.ts
  scss/  (23 files)
    animations/  (13 files)
      … 13 files under this directory
    themes/  (4 files)
      … 4 files under this directory
    _mixins.scss
    _vars.scss
    backdrop.scss
    border.scss
    index.scss
    svg-arrow.scss
  _babel.d.ts
  bindGlobalEventListeners.ts
  browser.ts
  constants.ts
  createTippy.ts
  css.ts
  dom-utils.ts
  index.ts
  props.ts
  template.ts
  types-internal.ts
  types.ts
  utils.ts
  validation.ts
test/  (31 files)
  functional/  (5 files)
    border.test.js
    followCursor.test.js
    inlinePositioning.test.js
    sticky.test.js
    themes.test.js
  integration/  (11 files)
    __snapshots__/  (2 files)
      … 2 files under this directory
    addons/  (2 files)
      … 2 files under this directory
    plugins/  (4 files)
      … 4 files under this directory
    bindGlobalEventListeners.test.js
    createTippy.test.js
    props.test.js
  unit/  (8 files)
    __snapshots__/  (2 files)
      … 2 files under this directory
    css.test.js
    dom-utils.test.js
    props.test.js
    tippy.test.js
    utils.test.js
    validation.test.js
  visual/  (4 files)
    index.css
    index.html
    index.js
    tests.js
  image-reporter.js
  setup.js
  utils.js
website/  (89 files)
  scripts/  (2 files)
    should-deploy-docs.js
    should-deploy-docs.sh
  src/  (80 files)
    components/  (27 files)
      … 27 files under this directory
    css/  (2 files)
      … 2 files under this directory
    hooks/  (1 files)
      … 1 files under this directory
    images/  (11 files)
      … 11 files under this directory
    pages/  (38 files)
      … 38 files under this directory
    utils.js
  .eslintignore
  .gitignore
  LICENSE
  README.md
  gatsby-config.js
  gatsby-node.js
  package.json
.editorconfig
.gitignore
LICENSE
MIGRATION_GUIDE.md
README.md
index.test-d.ts
package.json
tsconfig.json
```

## Entry points

- [src/index.ts](https://github.com/atomiks/tippyjs/blob/ad85f6feb79cf6c5853c43bf1b2a50c4fa98e7a1/src/index.ts)
- [website/src/components/Main.js](https://github.com/atomiks/tippyjs/blob/ad85f6feb79cf6c5853c43bf1b2a50c4fa98e7a1/website/src/components/Main.js)
- [website/src/css/index.js](https://github.com/atomiks/tippyjs/blob/ad85f6feb79cf6c5853c43bf1b2a50c4fa98e7a1/website/src/css/index.js)
- [website/src/hooks/index.js](https://github.com/atomiks/tippyjs/blob/ad85f6feb79cf6c5853c43bf1b2a50c4fa98e7a1/website/src/hooks/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| addons package | library | Observed | Groups 2 file(s) under addons package (observed from repository paths and static analysis). |
| _babel.d.ts package | library | Observed | Groups 1 file(s) under _babel.d.ts package (observed from repository paths and static analysis). |
| bindGlobalEventListeners.ts package | library | Observed | Groups 1 file(s) under bindglobaleventlisteners.ts package (observed from repository paths and static analysis). |
| browser.ts package | library | Observed | Groups 1 file(s) under browser.ts package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| constants.ts package | library | Observed | Groups 1 file(s) under constants.ts package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| createTippy.ts package | library | Observed | Groups 1 file(s) under createtippy.ts package (observed from repository paths and static analysis). |
| css.ts package | library | Observed | Groups 1 file(s) under css.ts package (observed from repository paths and static analysis). |
| dom-utils.ts package | library | Observed | Groups 1 file(s) under dom-utils.ts package (observed from repository paths and static analysis). |
| index.ts package | library | Observed | Groups 1 file(s) under index.ts package (observed from repository paths and static analysis). |
| plugins package | library | Observed | Groups 4 file(s) under plugins package (observed from repository paths and static analysis). |
| props.ts package | library | Observed | Groups 1 file(s) under props.ts package (observed from repository paths and static analysis). |
| template.ts package | library | Observed | Groups 1 file(s) under template.ts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 31 file(s) under tests (observed from repository paths and static analysis). |
| types-internal.ts package | library | Observed | Groups 1 file(s) under types-internal.ts package (observed from repository paths and static analysis). |
| types.ts package | library | Observed | Groups 1 file(s) under types.ts package (observed from repository paths and static analysis). |
| utils.ts package | library | Observed | Groups 1 file(s) under utils.ts package (observed from repository paths and static analysis). |
| validation.ts package | library | Observed | Groups 1 file(s) under validation.ts package (observed from repository paths and static analysis). |
| website package | library | Observed | Groups 36 file(s) under website package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/cd.yml` (ci)
- `.github/workflows/ci.yml` (ci)
- `headless/package.json` (manifest)
- `package.json` (manifest)
- `tsconfig.json` (config)
- `website/package.json` (manifest)
- `website/src/pages/.prettierrc.json` (config)

## Top-level layout

- `website` — 89 analysed file(s)
- `src` — 43 analysed file(s)
- `test` — 31 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `.config` — 6 analysed file(s)
- `.github` — 6 analysed file(s)
- `headless` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 27 file(s) were skipped during inventory (1 x likely secret file excluded; 26 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `ad85f6feb79cf6c5853c43bf1b2a50c4fa98e7a1` is the revision these paths and observations refer to.
