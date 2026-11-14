# Project structure: facebookarchive/flux

**Analysed commit:** `4ee8c50865c357e005cb40ea03cdd403533aad26`

**Commit reference:** [4ee8c50865c357e005cb40ea03cdd403533aad26](https://github.com/facebookarchive/flux/commit/4ee8c50865c357e005cb40ea03cdd403533aad26)

**Tree at this commit:** [facebookarchive/flux@4ee8c50865c3](https://github.com/facebookarchive/flux/tree/4ee8c50865c357e005cb40ea03cdd403533aad26)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | facebookarchive/flux |
| Description | Application Architecture for Building User Interfaces |
| Stars | 17435 |
| Forks | 3363 |
| Licence | Other |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `4ee8c50865c357e005cb40ea03cdd403533aad26` |
| Retrieved at | 2026-11-14T19:11:27.765482+00:00 |
| Files in this snapshot | 158 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    node.js.yml
docs/  (9 files)
  Dispatcher.ko-KR.md
  Dispatcher.md
  Flux-Utils.md
  In-Depth-Overview.md
  Overview.ko-KR.md
  Overview.md
  Related-Libraries.md
  Videos.ko-KR.md
  Videos.md
examples/  (102 files)
  flux-async/  (32 files)
    flow/  (4 files)
      … 4 files under this directory
    server/  (1 files)
      … 1 files under this directory
    src/  (16 files)
      … 16 files under this directory
    todomvc-common/  (4 files)
      … 4 files under this directory
    .babelrc
    .flowconfig
    .gitignore
    README.md
    index.html
    package.json
    webpack.config.js
  flux-concepts/  (1 files)
    README.md
  flux-flow/  (16 files)
    flow/  (2 files)
      … 2 files under this directory
    src/  (7 files)
      … 7 files under this directory
    .babelrc
    .flowconfig
    .gitignore
    README.md
    index.html
    package.json
    webpack.config.js
  flux-jest/  (5 files)
    src/  (1 files)
      … 1 files under this directory
    .babelrc
    .gitignore
    README.md
    package.json
  flux-jest-container/  (6 files)
    src/  (2 files)
      … 2 files under this directory
    .babelrc
    .gitignore
    README.md
    package.json
  flux-logging/  (9 files)
    src/  (3 files)
      … 3 files under this directory
    .babelrc
    .gitignore
    README.md
    index.html
    package.json
    webpack.config.js
  flux-shell/  (7 files)
    src/  (1 files)
      … 1 files under this directory
    .babelrc
    .gitignore
    README.md
    index.html
    package.json
    webpack.config.js
  flux-todomvc/  (21 files)
    src/  (11 files)
      … 11 files under this directory
    todomvc-common/  (4 files)
      … 4 files under this directory
    .babelrc
    .gitignore
    README.md
    index.html
    package.json
    webpack.config.js
  todomvc-common/  (4 files)
    .bower.json
    base.css
    bower.json
    readme.md
  README.md
scripts/  (3 files)
  babel/  (1 files)
    default-options.js
  jest/  (2 files)
    environment.js
    preprocessor.js
src/  (14 files)
  __tests__/  (2 files)
    Dispatcher-test.js
    FluxStoreGroup-test.js
  container/  (3 files)
    __tests__/  (1 files)
      … 1 files under this directory
    FluxContainer.js
    FluxContainerSubscriptions.js
  stores/  (4 files)
    __tests__/  (2 files)
      … 2 files under this directory
    FluxReduceStore.js
    FluxStore.js
  utils/  (1 files)
    abstractMethod.js
  .flowconfig
  Dispatcher.js
  FluxMixinLegacy.js
  FluxStoreGroup.js
website/  (14 files)
  src/  (4 files)
    css/  (1 files)
      … 1 files under this directory
    pages/  (3 files)
      … 3 files under this directory
  static/  (5 files)
    img/  (5 files)
      … 5 files under this directory
  .gitignore
  README.md
  docusaurus.config.js
  package.json
  sidebars.js
.gitignore
.npmignore
.prettierrc
.watchmanconfig
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
Gulpfile.js
LICENSE
README.md
bower.json
index.js
jest.config.js
package.json
utils.js
```

## Entry points

- [index.js](https://github.com/facebookarchive/flux/blob/4ee8c50865c357e005cb40ea03cdd403533aad26/index.js)
- [website/src/pages/index.js](https://github.com/facebookarchive/flux/blob/4ee8c50865c357e005cb40ea03cdd403533aad26/website/src/pages/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| container package | library | Observed | Groups 3 file(s) under container package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| Dispatcher.js package | library | Observed | Groups 1 file(s) under dispatcher.js package (observed from repository paths and static analysis). |
| FluxMixinLegacy.js package | library | Observed | Groups 1 file(s) under fluxmixinlegacy.js package (observed from repository paths and static analysis). |
| FluxStoreGroup.js package | library | Observed | Groups 1 file(s) under fluxstoregroup.js package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 3 file(s) under scripts package (observed from repository paths and static analysis). |
| stores package | library | Observed | Groups 4 file(s) under stores package (observed from repository paths and static analysis). |
| __tests__ package | library | Observed | Groups 2 file(s) under __tests__ package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 1 file(s) under utils package (observed from repository paths and static analysis). |
| website package | library | Observed | Groups 4 file(s) under website package (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/node.js.yml` (ci)
- `bower.json` (config)
- `examples/flux-async/package.json` (manifest)
- `examples/flux-async/todomvc-common/.bower.json` (config)
- `examples/flux-async/todomvc-common/bower.json` (config)
- `examples/flux-flow/package.json` (manifest)
- `examples/flux-jest-container/package.json` (manifest)
- `examples/flux-jest/package.json` (manifest)
- `examples/flux-logging/package.json` (manifest)
- `examples/flux-shell/package.json` (manifest)
- `examples/flux-todomvc/package.json` (manifest)
- `examples/flux-todomvc/todomvc-common/.bower.json` (config)
- `examples/flux-todomvc/todomvc-common/bower.json` (config)
- `examples/todomvc-common/.bower.json` (config)
- `examples/todomvc-common/bower.json` (config)
- `package.json` (manifest)
- `website/package.json` (manifest)

## Top-level layout

- `examples` — 102 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `src` — 14 analysed file(s)
- `website` — 14 analysed file(s)
- `docs` — 9 analysed file(s)
- `scripts` — 3 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `4ee8c50865c357e005cb40ea03cdd403533aad26` is the revision these paths and observations refer to.
