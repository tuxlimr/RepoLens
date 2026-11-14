# Project structure: redux-saga/redux-saga

**Analysed commit:** `1bfaded683f1161a6b749d62c5c2a70cbcbc6a94`

**Commit reference:** [1bfaded683f1161a6b749d62c5c2a70cbcbc6a94](https://github.com/redux-saga/redux-saga/commit/1bfaded683f1161a6b749d62c5c2a70cbcbc6a94)

**Tree at this commit:** [redux-saga/redux-saga@1bfaded683f1](https://github.com/redux-saga/redux-saga/tree/1bfaded683f1161a6b749d62c5c2a70cbcbc6a94)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | redux-saga/redux-saga |
| Description | An alternative side effect model for Redux apps |
| Stars | 22410 |
| Forks | 1929 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `1bfaded683f1161a6b749d62c5c2a70cbcbc6a94` |
| Retrieved at | 2026-11-14T19:11:08.964291+00:00 |
| Files in this snapshot | 399 |

## Directory tree

```text
.changeset/  (2 files)
  README.md
  config.json
.github/  (11 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    custom.md
  actions/  (1 files)
    ci-setup/  (1 files)
      … 1 files under this directory
  workflows/  (4 files)
    ci.yml
    docs.yml
    publish.yml
    size.yml
  CODEOWNERS
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
.husky/  (1 files)
  pre-commit
docs/  (26 files)
  advanced/  (13 files)
    Channels.md
    ComposingSagas.md
    Concurrency.md
    ForkModel.md
    FutureActions.md
    NonBlockingCalls.md
    RacingEffects.md
    RootSaga.md
    RunningTasksInParallel.md
    SequencingSagas.md
    TaskCancellation.md
    Testing.md
    UsingRunSaga.md
  basics/  (5 files)
    DeclarativeEffects.md
    DispatchingActions.md
    Effect.md
    ErrorHandling.md
    UsingSagaHelpers.md
  introduction/  (2 files)
    BeginnerTutorial.md
    GettingStarted.md
  API.md
  About.md
  ExternalResources.md
  Glossary.md
  Recipes.md
  Troubleshooting.md
examples/  (87 files)
  async/  (14 files)
    src/  (9 files)
      … 9 files under this directory
    test/  (1 files)
      … 1 files under this directory
    README.md
    index.html
    package.json
    vite.config.js
  cancellable-counter/  (11 files)
    src/  (6 files)
      … 6 files under this directory
    test/  (1 files)
      … 1 files under this directory
    README.md
    index.html
    package.json
    vite.config.js
  counter/  (9 files)
    src/  (4 files)
      … 4 files under this directory
    test/  (1 files)
      … 1 files under this directory
    README.md
    index.html
    package.json
    vite.config.js
  counter-vanilla/  (3 files)
    README.md
    index.html
    package.json
  error-demo/  (9 files)
    src/  (4 files)
      … 4 files under this directory
    test/  (1 files)
      … 1 files under this directory
    README.md
    index.html
    package.json
    vite.config.js
  real-world/  (22 files)
    app/  (17 files)
      … 17 files under this directory
    .gitignore
    README.md
    package.json
    react-router.config.js
    vite.config.js
  shopping-cart/  (19 files)
    src/  (14 files)
      … 14 files under this directory
    test/  (1 files)
      … 1 files under this directory
    README.md
    index.html
    package.json
    vite.config.js
logo/  (1 files)
  README.md
packages/  (229 files)
  babel-plugin-redux-saga/  (54 files)
    src/  (1 files)
      … 1 files under this directory
    test/  (49 files)
      … 49 files under this directory
    CHANGELOG.md
    LICENSE
    README.md
    package.json
  core/  (79 files)
    __tests__/  (35 files)
      … 35 files under this directory
    effects/  (1 files)
      … 1 files under this directory
    src/  (32 files)
      … 32 files under this directory
    types/  (7 files)
      … 7 files under this directory
    CHANGELOG.md
    LICENSE
    README.md
    package.json
  deferred/  (5 files)
    src/  (2 files)
      … 2 files under this directory
    CHANGELOG.md
    LICENSE
    package.json
  delay-p/  (7 files)
    src/  (4 files)
      … 4 files under this directory
    CHANGELOG.md
    LICENSE
    package.json
  is/  (5 files)
    src/  (2 files)
      … 2 files under this directory
    CHANGELOG.md
    LICENSE
    package.json
  redux-saga/  (9 files)
    effects/  (1 files)
      … 1 files under this directory
    src/  (4 files)
      … 4 files under this directory
    CHANGELOG.md
    LICENSE
    README.md
    package.json
  simple-saga-monitor/  (14 files)
    src/  (11 files)
      … 11 files under this directory
    CHANGELOG.md
    LICENSE
    package.json
  symbols/  (5 files)
    src/  (2 files)
      … 2 files under this directory
    CHANGELOG.md
    LICENSE
    package.json
  testing-utils/  (10 files)
    __tests__/  (2 files)
      … 2 files under this directory
    src/  (2 files)
      … 2 files under this directory
    types/  (3 files)
      … 3 files under this directory
    CHANGELOG.md
    LICENSE
    package.json
  types/  (7 files)
    src/  (2 files)
      … 2 files under this directory
    types/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    LICENSE
    README.md
    package.json
  unplugin/  (34 files)
    esbuild/  (1 files)
      … 1 files under this directory
    rolldown/  (1 files)
      … 1 files under this directory
    rollup/  (1 files)
      … 1 files under this directory
    rspack/  (1 files)
      … 1 files under this directory
    src/  (17 files)
      … 17 files under this directory
    test/  (3 files)
      … 3 files under this directory
    types/  (4 files)
      … 4 files under this directory
    vite/  (1 files)
      … 1 files under this directory
    webpack/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    LICENSE
    README.md
    package.json
patches/  (1 files)
  @preconstruct__cli@2.8.13.patch
scripts/  (1 files)
  combine-umd-builds.js
website/  (17 files)
  src/  (9 files)
    components/  (4 files)
      … 4 files under this directory
    css/  (3 files)
      … 3 files under this directory
    pages/  (2 files)
      … 2 files under this directory
  static/  (2 files)
    .nojekyll
    CNAME
  .gitignore
  README.md
  babel.config.js
  docusaurus.config.js
  package.json
  sidebars.js
.browserslistrc
.gitignore
.lintstagedrc
.prettierignore
.prettierrc
CHANGELOG.md
CONTRIBUTING.md
LICENSE
LICENSE-logo.md
README.md
README_es.md
README_ja.md
README_ru.md
README_zh-cn.md
README_zh-hant.md
SECURITY.md
SUMMARY.md
babel.config.js
eslint.config.js
package.json
pnpm-workspace.yaml
tsconfig.json
vitest.config.mjs
```

## Entry points

- [examples/counter-vanilla/index.html](https://github.com/redux-saga/redux-saga/blob/1bfaded683f1161a6b749d62c5c2a70cbcbc6a94/examples/counter-vanilla/index.html)
- [packages/babel-plugin-redux-saga/src/index.js](https://github.com/redux-saga/redux-saga/blob/1bfaded683f1161a6b749d62c5c2a70cbcbc6a94/packages/babel-plugin-redux-saga/src/index.js)
- [packages/core/src/index.js](https://github.com/redux-saga/redux-saga/blob/1bfaded683f1161a6b749d62c5c2a70cbcbc6a94/packages/core/src/index.js)
- [packages/deferred/src/index.js](https://github.com/redux-saga/redux-saga/blob/1bfaded683f1161a6b749d62c5c2a70cbcbc6a94/packages/deferred/src/index.js)
- [packages/delay-p/src/index.js](https://github.com/redux-saga/redux-saga/blob/1bfaded683f1161a6b749d62c5c2a70cbcbc6a94/packages/delay-p/src/index.js)
- [packages/is/src/index.js](https://github.com/redux-saga/redux-saga/blob/1bfaded683f1161a6b749d62c5c2a70cbcbc6a94/packages/is/src/index.js)
- [packages/redux-saga/src/index.js](https://github.com/redux-saga/redux-saga/blob/1bfaded683f1161a6b749d62c5c2a70cbcbc6a94/packages/redux-saga/src/index.js)
- [packages/simple-saga-monitor/src/index.js](https://github.com/redux-saga/redux-saga/blob/1bfaded683f1161a6b749d62c5c2a70cbcbc6a94/packages/simple-saga-monitor/src/index.js)
- [packages/symbols/src/index.js](https://github.com/redux-saga/redux-saga/blob/1bfaded683f1161a6b749d62c5c2a70cbcbc6a94/packages/symbols/src/index.js)
- [packages/testing-utils/src/index.js](https://github.com/redux-saga/redux-saga/blob/1bfaded683f1161a6b749d62c5c2a70cbcbc6a94/packages/testing-utils/src/index.js)
- [packages/types/src/index.js](https://github.com/redux-saga/redux-saga/blob/1bfaded683f1161a6b749d62c5c2a70cbcbc6a94/packages/types/src/index.js)
- [packages/unplugin/src/index.js](https://github.com/redux-saga/redux-saga/blob/1bfaded683f1161a6b749d62c5c2a70cbcbc6a94/packages/unplugin/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 28 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 53 file(s) under packages package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 73 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 57 file(s) under tests (observed from repository paths and static analysis). |
| website package | library | Observed | Groups 8 file(s) under website package (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/actions/ci-setup/action.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/docs.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.github/workflows/size.yml` (ci)
- `examples/async/package.json` (manifest)
- `examples/cancellable-counter/package.json` (manifest)
- `examples/counter-vanilla/package.json` (manifest)
- `examples/counter/package.json` (manifest)
- `examples/error-demo/package.json` (manifest)
- `examples/real-world/package.json` (manifest)
- `examples/shopping-cart/package.json` (manifest)
- `package.json` (manifest)
- `packages/babel-plugin-redux-saga/package.json` (manifest)
- `packages/core/effects/package.json` (manifest)
- `packages/core/package.json` (manifest)
- `packages/core/types/tsconfig.json` (config)
- `packages/deferred/package.json` (manifest)
- `packages/delay-p/package.json` (manifest)
- `packages/is/package.json` (manifest)
- `packages/redux-saga/effects/package.json` (manifest)
- `packages/redux-saga/package.json` (manifest)
- `packages/simple-saga-monitor/package.json` (manifest)
- `packages/symbols/package.json` (manifest)
- `packages/testing-utils/package.json` (manifest)
- `packages/testing-utils/types/tsconfig.json` (config)
- `packages/types/package.json` (manifest)
- `packages/unplugin/esbuild/package.json` (manifest)
- `packages/unplugin/package.json` (manifest)
- `packages/unplugin/rolldown/package.json` (manifest)
- `packages/unplugin/rollup/package.json` (manifest)
- `packages/unplugin/rspack/package.json` (manifest)
- `packages/unplugin/src/package.json` (manifest)
- `packages/unplugin/types/tsconfig.adapters.json` (config)
- `packages/unplugin/types/tsconfig.json` (config)
- `packages/unplugin/vite/package.json` (manifest)
- `packages/unplugin/webpack/package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `tsconfig.json` (config)
- `website/package.json` (manifest)

## Top-level layout

- `packages` — 229 analysed file(s)
- `examples` — 87 analysed file(s)
- `docs` — 26 analysed file(s)
- `(root files)` — 23 analysed file(s)
- `website` — 17 analysed file(s)
- `.github` — 11 analysed file(s)
- `.changeset` — 2 analysed file(s)
- `.husky` — 1 analysed file(s)
- `logo` — 1 analysed file(s)
- `patches` — 1 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `1bfaded683f1161a6b749d62c5c2a70cbcbc6a94` is the revision these paths and observations refer to.
