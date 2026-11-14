# Project structure: dvajs/dva

**Analysed commit:** `b60e6c0baf59450ac9cba5a3100fd2c17a6851fa`

**Commit reference:** [b60e6c0baf59450ac9cba5a3100fd2c17a6851fa](https://github.com/dvajs/dva/commit/b60e6c0baf59450ac9cba5a3100fd2c17a6851fa)

**Tree at this commit:** [dvajs/dva@b60e6c0baf59](https://github.com/dvajs/dva/tree/b60e6c0baf59450ac9cba5a3100fd2c17a6851fa)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | dvajs/dva |
| Description | 🌱 React and redux based, lightweight and elm-style framework. (Inspired by elm and choo) |
| Stars | 16124 |
| Forks | 3092 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `b60e6c0baf59450ac9cba5a3100fd2c17a6851fa` |
| Retrieved at | 2026-11-14T19:11:34.165474+00:00 |
| Files in this snapshot | 173 |

## Directory tree

```text
.circleci/  (1 files)
  config.yml
.github/  (7 files)
  ISSUE_TEMPLATE/  (4 files)
    bug_report.md
    bug_report_cn.md
    feature_request.md
    rfc_cn.md
  workflows/  (1 files)
    ci.yml
  PULL_REQUEST_TEMPLATE.md
  stale.yml
docs/  (16 files)
  .vuepress/  (2 files)
    config.js
    override.styl
  api/  (1 files)
    README.md
  guide/  (8 files)
    README.md
    concepts.md
    develop-complex-spa.md
    examples-and-boilerplates.md
    fig-show.md
    getting-started.md
    introduce-class.md
    source-code-explore.md
  knowledgemap/  (1 files)
    README.md
  API.md
  Concepts.md
  GettingStarted.md
  README.md
examples/  (78 files)
  func-test/  (14 files)
    src/  (10 files)
      … 10 files under this directory
    .eslintrc
    .roadhogrc
    .roadhogrc.mock.js
    package.json
  user-dashboard/  (27 files)
    src/  (20 files)
      … 20 files under this directory
    .editorconfig
    .eslintrc
    .gitignore
    .umirc.js
    .webpackrc
    README.md
    package.json
  with-immer/  (5 files)
    pages/  (1 files)
      … 1 files under this directory
    .umirc.js
    dva.js
    model.js
    package.json
  with-nextjs/  (11 files)
    model/  (2 files)
      … 2 files under this directory
    pages/  (2 files)
      … 2 files under this directory
    utils/  (1 files)
      … 1 files under this directory
    .babelrc
    .eslintignore
    .eslintrc
    .gitignore
    README.md
    package.json
  with-react-router-3/  (14 files)
    src/  (10 files)
      … 10 files under this directory
    .eslintrc
    .roadhogrc
    .roadhogrc.mock.js
    package.json
  with-redux-undo/  (7 files)
    src/  (3 files)
      … 3 files under this directory
    .babelrc
    .gitignore
    README.md
    package.json
packages/  (56 files)
  dva/  (16 files)
    src/  (2 files)
      … 2 files under this directory
    test/  (2 files)
      … 2 files under this directory
    .fatherrc.js
    README.md
    dynamic.d.ts
    dynamic.js
    fetch.d.ts
    fetch.js
    index.d.ts
    package.json
    router.d.ts
    router.js
    saga.js
    warnAboutDeprecatedCJSRequire.js
  dva-core/  (28 files)
    src/  (14 files)
      … 14 files under this directory
    test/  (10 files)
      … 10 files under this directory
    .fatherrc.js
    README.md
    package.json
    saga.js
  dva-immer/  (5 files)
    src/  (1 files)
      … 1 files under this directory
    test/  (1 files)
      … 1 files under this directory
    .fatherrc.js
    README.md
    package.json
  dva-loading/  (7 files)
    src/  (1 files)
      … 1 files under this directory
    test/  (2 files)
      … 2 files under this directory
    .fatherrc.js
    README.md
    index.d.ts
    package.json
scripts/  (1 files)
  publish.js
website/  (3 files)
  .gitignore
  now.json
  package.json
.editorconfig
.eslintignore
.eslintrc
.gitignore
.prettierrc
LICENSE
README.md
README_zh-CN.md
jest.config.js
lerna.json
package.json
```

## Entry points

- [packages/dva-core/src/index.js](https://github.com/dvajs/dva/blob/b60e6c0baf59450ac9cba5a3100fd2c17a6851fa/packages/dva-core/src/index.js)
- [packages/dva-immer/src/index.js](https://github.com/dvajs/dva/blob/b60e6c0baf59450ac9cba5a3100fd2c17a6851fa/packages/dva-immer/src/index.js)
- [packages/dva-loading/src/index.js](https://github.com/dvajs/dva/blob/b60e6c0baf59450ac9cba5a3100fd2c17a6851fa/packages/dva-loading/src/index.js)
- [packages/dva/src/index.js](https://github.com/dvajs/dva/blob/b60e6c0baf59450ac9cba5a3100fd2c17a6851fa/packages/dva/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 8 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 33 file(s) under packages package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 15 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.circleci/config.yml` (ci)
- `.editorconfig` (config)
- `.github/stale.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `examples/func-test/package.json` (manifest)
- `examples/user-dashboard/.editorconfig` (config)
- `examples/user-dashboard/package.json` (manifest)
- `examples/with-immer/package.json` (manifest)
- `examples/with-nextjs/package.json` (manifest)
- `examples/with-react-router-3/package.json` (manifest)
- `examples/with-redux-undo/package.json` (manifest)
- `lerna.json` (config)
- `package.json` (manifest)
- `packages/dva-core/package.json` (manifest)
- `packages/dva-immer/package.json` (manifest)
- `packages/dva-loading/package.json` (manifest)
- `packages/dva/package.json` (manifest)
- `website/now.json` (config)
- `website/package.json` (manifest)

## Top-level layout

- `examples` — 78 analysed file(s)
- `packages` — 56 analysed file(s)
- `docs` — 16 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `.github` — 7 analysed file(s)
- `website` — 3 analysed file(s)
- `.circleci` — 1 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 5 file(s) were skipped during inventory (1 x likely secret file excluded; 4 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `b60e6c0baf59450ac9cba5a3100fd2c17a6851fa` is the revision these paths and observations refer to.
