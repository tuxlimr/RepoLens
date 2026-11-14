# Project structure: facebookexperimental/Recoil

**Analysed commit:** `c1b97f3a0117cad76cbc6ab3cb06d89a9ce717af`

**Commit reference:** [c1b97f3a0117cad76cbc6ab3cb06d89a9ce717af](https://github.com/facebookexperimental/Recoil/commit/c1b97f3a0117cad76cbc6ab3cb06d89a9ce717af)

**Tree at this commit:** [facebookexperimental/Recoil@c1b97f3a0117](https://github.com/facebookexperimental/Recoil/tree/c1b97f3a0117cad76cbc6ab3cb06d89a9ce717af)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | facebookexperimental/Recoil |
| Description | Recoil is an experimental state management library for React apps. It provides several capabilities that are difficult to achieve with React alone, while being compatible with the newest features of React. |
| Stars | 19400 |
| Forks | 1207 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `c1b97f3a0117cad76cbc6ab3cb06d89a9ce717af` |
| Retrieved at | 2026-11-14T19:11:17.536507+00:00 |
| Files in this snapshot | 345 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (2 files)
    nightly.yml
    nodejs.yml
eslint-rules/  (1 files)
  no-fb-only.js
flow-typed/  (18 files)
  npm/  (15 files)
    ReactDOM_vx.x.x.js
    ReactTestUtils_vx.x.x.js
    d3-array_vx.x.x.js
    d3-collection_vx.x.x.js
    d3-interpolate_vx.x.x.js
    d3-scale_vx.x.x.js
    d3-selection_vx.x.x.js
    d3-transition_vx.x.x.js
    d3_vx.x.x.js
    hamt_plus_vx.x.x.js
    immutable_vx.x.x.js
    jest_v26.x.x.js
    jsondiffpatch-for-react_vx.x.x.js
    nullthrows_vx.x.x.js
    react-dom_v18.x.x.js
  jest.js
  package.json.js
  public-stubs.js
packages/  (192 files)
  recoil/  (97 files)
    adt/  (7 files)
      … 7 files under this directory
    caches/  (15 files)
      … 15 files under this directory
    contrib/  (3 files)
      … 3 files under this directory
    core/  (25 files)
      … 25 files under this directory
    hooks/  (24 files)
      … 24 files under this directory
    recoil_values/  (20 files)
      … 20 files under this directory
    Recoil_index.js
    package-for-release.json
    package.json
  recoil-relay/  (18 files)
    __test_utils__/  (1 files)
      … 1 files under this directory
    __tests__/  (8 files)
      … 8 files under this directory
    RecoilRelay_Environments.js
    RecoilRelay_graphQLMutationEffect.js
    RecoilRelay_graphQLQueryEffect.js
    RecoilRelay_graphQLSelector.js
    RecoilRelay_graphQLSelectorFamily.js
    RecoilRelay_graphQLSubscriptionEffect.js
    RecoilRelay_index.js
    package-for-release.json
    package.json
  recoil-sync/  (17 files)
    __test_utils__/  (1 files)
      … 1 files under this directory
    __tests__/  (9 files)
      … 9 files under this directory
    RecoilSync.js
    RecoilSync_URL.js
    RecoilSync_URLJSON.js
    RecoilSync_URLTransit.js
    RecoilSync_index.js
    package-for-release.json
    package.json
  refine/  (14 files)
    __tests__/  (5 files)
      … 5 files under this directory
    Refine_API.js
    Refine_Checkers.js
    Refine_ContainerCheckers.js
    Refine_JSON.js
    Refine_PrimitiveCheckers.js
    Refine_UtilityCheckers.js
    Refine_index.js
    package-for-release.json
    package.json
  shared/  (46 files)
    __test_utils__/  (2 files)
      … 2 files under this directory
    polyfill/  (7 files)
      … 7 files under this directory
    util/  (36 files)
      … 36 files under this directory
    package.json
packages-ext/  (91 files)
  recoil-devtools/  (74 files)
    src/  (63 files)
      … 63 files under this directory
    utils/  (3 files)
      … 3 files under this directory
    .babelrc
    .eslintignore
    .eslintrc
    .gitignore
    .prettierignore
    flow.js
    package.json
    webpack.config.js
  todo-example/  (17 files)
    public/  (3 files)
      … 3 files under this directory
    src/  (11 files)
      … 11 files under this directory
    .gitignore
    README.md
    package.json
scripts/  (6 files)
  build.mjs
  deploy_nightly_build.js
  pack.mjs
  project-root-dir.mjs
  rollup-configs.mjs
  utils.mjs
typescript/  (11 files)
  index.d.ts
  recoil-relay-test.ts
  recoil-relay.d.ts
  recoil-sync-test.ts
  recoil-sync.d.ts
  recoil-test.ts
  recoil.d.ts
  refine-test.ts
  refine.d.ts
  tsconfig.json
  tslint.json
.eslintignore
.eslintrc.js
.flowconfig
.gitignore
.prettierignore
.prettierrc
.watchmanconfig
CHANGELOG-recoil-relay.md
CHANGELOG-recoil-sync.md
CHANGELOG-recoil.md
CHANGELOG-refine.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README-recoil-relay.md
README-recoil-sync.md
README-refine.md
README.md
babel.config.json
jest.config.js
package.json
relay.config.js
rollup.config.js
setupJestMock.js
```

## Entry points

- [packages/recoil-relay/RecoilRelay_index.js](https://github.com/facebookexperimental/Recoil/blob/c1b97f3a0117cad76cbc6ab3cb06d89a9ce717af/packages/recoil-relay/RecoilRelay_index.js)
- [packages/recoil-sync/RecoilSync_index.js](https://github.com/facebookexperimental/Recoil/blob/c1b97f3a0117cad76cbc6ab3cb06d89a9ce717af/packages/recoil-sync/RecoilSync_index.js)
- [packages/recoil/Recoil_index.js](https://github.com/facebookexperimental/Recoil/blob/c1b97f3a0117cad76cbc6ab3cb06d89a9ce717af/packages/recoil/Recoil_index.js)
- [packages/refine/Refine_index.js](https://github.com/facebookexperimental/Recoil/blob/c1b97f3a0117cad76cbc6ab3cb06d89a9ce717af/packages/refine/Refine_index.js)
- [packages-ext/todo-example/src/App.js](https://github.com/facebookexperimental/Recoil/blob/c1b97f3a0117cad76cbc6ab3cb06d89a9ce717af/packages-ext/todo-example/src/App.js)
- [packages-ext/todo-example/src/index.js](https://github.com/facebookexperimental/Recoil/blob/c1b97f3a0117cad76cbc6ab3cb06d89a9ce717af/packages-ext/todo-example/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 17 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| eslint-rules package | library | Observed | Groups 1 file(s) under eslint-rules package (observed from repository paths and static analysis). |
| flow-typed package | library | Observed | Groups 18 file(s) under flow-typed package (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 156 file(s) under packages package (observed from repository paths and static analysis). |
| packages-ext package | library | Observed | Groups 72 file(s) under packages-ext package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 6 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 25 file(s) under service / domain layer (observed from repository paths and static analysis). |
| typescript package | library | Observed | Groups 9 file(s) under typescript package (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/nightly.yml` (ci)
- `.github/workflows/nodejs.yml` (ci)
- `babel.config.json` (config)
- `package.json` (manifest)
- `packages-ext/recoil-devtools/package.json` (manifest)
- `packages-ext/recoil-devtools/src/manifest.json` (config)
- `packages-ext/todo-example/package.json` (manifest)
- `packages-ext/todo-example/public/manifest.json` (config)
- `packages/recoil-relay/package-for-release.json` (config)
- `packages/recoil-relay/package.json` (manifest)
- `packages/recoil-sync/package-for-release.json` (config)
- `packages/recoil-sync/package.json` (manifest)
- `packages/recoil/package-for-release.json` (config)
- `packages/recoil/package.json` (manifest)
- `packages/refine/package-for-release.json` (config)
- `packages/refine/package.json` (manifest)
- `packages/shared/package.json` (manifest)
- `typescript/tsconfig.json` (config)
- `typescript/tslint.json` (config)

## Top-level layout

- `packages` — 192 analysed file(s)
- `packages-ext` — 91 analysed file(s)
- `(root files)` — 24 analysed file(s)
- `flow-typed` — 18 analysed file(s)
- `typescript` — 11 analysed file(s)
- `scripts` — 6 analysed file(s)
- `.github` — 2 analysed file(s)
- `eslint-rules` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `c1b97f3a0117cad76cbc6ab3cb06d89a9ce717af` is the revision these paths and observations refer to.
