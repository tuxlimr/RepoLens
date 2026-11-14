# Project structure: vuejs/vuex

**Analysed commit:** `bd907467b8392d6671bb115738285ff7f63d0cf6`

**Commit reference:** [bd907467b8392d6671bb115738285ff7f63d0cf6](https://github.com/vuejs/vuex/commit/bd907467b8392d6671bb115738285ff7f63d0cf6)

**Tree at this commit:** [vuejs/vuex@bd907467b839](https://github.com/vuejs/vuex/tree/bd907467b8392d6671bb115738285ff7f63d0cf6)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | vuejs/vuex |
| Description | 🗃️ Centralized State Management for Vue.js. |
| Stars | 28285 |
| Forks | 9376 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `bd907467b8392d6671bb115738285ff7f63d0cf6` |
| Retrieved at | 2026-11-14T19:10:49.576074+00:00 |
| Files in this snapshot | 223 |

## Directory tree

```text
.github/  (6 files)
  ISSUE_TEMPLATE/  (1 files)
    bug_report.yml
  workflows/  (1 files)
    ci.yml
  FUNDING.yml
  ISSUE_TEMPLATE.md
  commit-convention.md
  contributing.md
docs/  (77 files)
  .vitepress/  (3 files)
    styles/  (1 files)
      … 1 files under this directory
    theme/  (1 files)
      … 1 files under this directory
    config.js
  api/  (1 files)
    index.md
  guide/  (15 files)
    actions.md
    composition-api.md
    forms.md
    getters.md
    hot-reload.md
    index.md
    migrating-to-4-0-from-3-x.md
    modules.md
    mutations.md
    plugins.md
    state.md
    strict.md
    structure.md
    testing.md
    typescript-support.md
  ja/  (18 files)
    api/  (1 files)
      … 1 files under this directory
    guide/  (15 files)
      … 15 files under this directory
    index.md
    installation.md
  ptbr/  (18 files)
    api/  (1 files)
      … 1 files under this directory
    guide/  (15 files)
      … 15 files under this directory
    index.md
    installation.md
  public/  (2 files)
    icons/  (1 files)
      … 1 files under this directory
    _redirects
  zh/  (18 files)
    api/  (1 files)
      … 1 files under this directory
    guide/  (15 files)
      … 15 files under this directory
    index.md
    installation.md
  index.md
  installation.md
examples/  (91 files)
  classic/  (44 files)
    chat/  (14 files)
      … 14 files under this directory
    counter/  (4 files)
      … 4 files under this directory
    counter-hot/  (7 files)
      … 7 files under this directory
    shopping-cart/  (11 files)
      … 11 files under this directory
    todomvc/  (8 files)
      … 8 files under this directory
  composition/  (43 files)
    chat/  (14 files)
      … 14 files under this directory
    counter/  (4 files)
      … 4 files under this directory
    counter-hot/  (7 files)
      … 7 files under this directory
    shopping-cart/  (10 files)
      … 10 files under this directory
    todomvc/  (8 files)
      … 8 files under this directory
  global.css
  index.html
  server.js
  webpack.config.js
scripts/  (2 files)
  build.js
  release.js
src/  (12 files)
  module/  (2 files)
    module-collection.js
    module.js
  plugins/  (2 files)
    devtool.js
    logger.js
  helpers.js
  index.cjs.js
  index.js
  index.mjs
  injectKey.js
  store-util.js
  store.js
  util.js
test/  (16 files)
  e2e/  (4 files)
    cart.spec.js
    chat.spec.js
    counter.spec.js
    todomvc.spec.js
  esm/  (2 files)
    esm-import.mjs
    esm-test.js
  unit/  (7 files)
    module/  (2 files)
      … 2 files under this directory
    helpers.spec.js
    hot-reload.spec.js
    modules.spec.js
    store.spec.js
    util.spec.js
  .eslintrc.json
  helpers.js
  setup.js
types/  (10 files)
  test/  (4 files)
    helpers.ts
    index.ts
    tsconfig.json
    vue.ts
  README.md
  helpers.d.ts
  index.d.ts
  logger.d.ts
  tsconfig.json
  vue.d.ts
.babelrc
.eslintrc.json
.gitignore
CHANGELOG.md
LICENSE
README.md
jest.config.js
package.json
rollup.config.js
```

## Entry points

- [src/index.js](https://github.com/vuejs/vuex/blob/bd907467b8392d6671bb115738285ff7f63d0cf6/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| helpers.js package | library | Observed | Groups 1 file(s) under helpers.js package (observed from repository paths and static analysis). |
| index.cjs.js package | library | Observed | Groups 1 file(s) under index.cjs.js package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| index.mjs package | library | Observed | Groups 1 file(s) under index.mjs package (observed from repository paths and static analysis). |
| injectKey.js package | library | Observed | Groups 1 file(s) under injectkey.js package (observed from repository paths and static analysis). |
| module package | library | Observed | Groups 2 file(s) under module package (observed from repository paths and static analysis). |
| plugins package | library | Observed | Groups 2 file(s) under plugins package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 2 file(s) under scripts package (observed from repository paths and static analysis). |
| store.js package | library | Observed | Groups 1 file(s) under store.js package (observed from repository paths and static analysis). |
| store-util.js package | library | Observed | Groups 1 file(s) under store-util.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 20 file(s) under tests (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 4 file(s) under types package (observed from repository paths and static analysis). |
| util.js package | library | Observed | Groups 1 file(s) under util.js package (observed from repository paths and static analysis). |

## Important files

- `.eslintrc.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `package.json` (manifest)
- `types/tsconfig.json` (config)

## Top-level layout

- `examples` — 91 analysed file(s)
- `docs` — 77 analysed file(s)
- `test` — 16 analysed file(s)
- `src` — 12 analysed file(s)
- `types` — 10 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `.github` — 6 analysed file(s)
- `scripts` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `bd907467b8392d6671bb115738285ff7f63d0cf6` is the revision these paths and observations refer to.
