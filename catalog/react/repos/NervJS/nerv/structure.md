# Project structure: NervJS/nerv

**Analysed commit:** `aaa405e79de5926e30ff07a0bb1b94dc994e9446`

**Commit reference:** [aaa405e79de5926e30ff07a0bb1b94dc994e9446](https://github.com/NervJS/nerv/commit/aaa405e79de5926e30ff07a0bb1b94dc994e9446)

**Tree at this commit:** [NervJS/nerv@aaa405e79de5](https://github.com/NervJS/nerv/tree/aaa405e79de5926e30ff07a0bb1b94dc994e9446)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | NervJS/nerv |
| Description | A blazing fast React alternative, compatible with IE8 and React 16. |
| Stars | 5404 |
| Forks | 261 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `aaa405e79de5926e30ff07a0bb1b94dc994e9446` |
| Retrieved at | 2026-11-14T19:14:20.533442+00:00 |
| Files in this snapshot | 174 |

## Directory tree

```text
benchmarks/  (21 files)
  DBMonster/  (9 files)
    ENV.js
    app.js
    build.js
    index.html
    memory-stats.js
    monitor.js
    readme.md
    style.css
    webpack.config.js
  isomorphic-ui-benchmarks/  (1 files)
    README.md
  js-framwork-bench/  (6 files)
    src/  (2 files)
      … 2 files under this directory
    .babelrc
    index.html
    readme.md
    webpack.config.js
  uibench/  (5 files)
    app.js
    build.js
    index.html
    readme.md
    rollup.config.js
browsers/  (3 files)
  ie8.js
  karma.js
  polyfill.js
packages/  (129 files)
  nerv/  (63 files)
    __tests__/  (23 files)
      … 23 files under this directory
    src/  (34 files)
      … 34 files under this directory
    .npmignore
    CHANGELOG.md
    README.md
    index.js
    package.json
    rollup.config.js
  nerv-create-class/  (6 files)
    src/  (1 files)
      … 1 files under this directory
    .npmignore
    CHANGELOG.md
    index.js
    package.json
    rollup.config.js
  nerv-devtools/  (8 files)
    src/  (3 files)
      … 3 files under this directory
    .npmignore
    CHANGELOG.md
    index.js
    package.json
    rollup.config.js
  nerv-is/  (4 files)
    src/  (1 files)
      … 1 files under this directory
    index.js
    package.json
    rollup.config.js
  nerv-redux/  (10 files)
    __tests__/  (2 files)
      … 2 files under this directory
    src/  (3 files)
      … 3 files under this directory
    .npmignore
    CHANGELOG.md
    index.js
    package.json
    rollup.config.js
  nerv-server/  (9 files)
    __tests__/  (1 files)
      … 1 files under this directory
    src/  (3 files)
      … 3 files under this directory
    .npmignore
    CHANGELOG.md
    index.js
    package.json
    rollup.config.js
  nerv-shared/  (6 files)
    src/  (1 files)
      … 1 files under this directory
    .npmignore
    CHANGELOG.md
    index.js
    package.json
    rollup.config.js
  nerv-test-utils/  (8 files)
    __tests__/  (2 files)
      … 2 files under this directory
    src/  (1 files)
      … 1 files under this directory
    .npmignore
    CHANGELOG.md
    index.js
    package.json
    rollup.config.js
  nerv-utils/  (15 files)
    __tests__/  (4 files)
      … 4 files under this directory
    src/  (6 files)
      … 6 files under this directory
    .npmignore
    CHANGELOG.md
    index.js
    package.json
    rollup.config.js
.babelrc
.editorconfig
.eslintignore
.eslintrc.js
.gitignore
.travis.yml
CHANGELOG.md
LICENSE
README.md
README_CN.md
afterbuild.js
azure-pipelines.yml
index.js
jest.config.js
karma.conf.js
lerna.json
package.json
release.js
tsconfig.json
tslint.json
typing.js
```

## Entry points

- [packages/nerv-create-class/index.js](https://github.com/NervJS/nerv/blob/aaa405e79de5926e30ff07a0bb1b94dc994e9446/packages/nerv-create-class/index.js)
- [packages/nerv-is/index.js](https://github.com/NervJS/nerv/blob/aaa405e79de5926e30ff07a0bb1b94dc994e9446/packages/nerv-is/index.js)
- [packages/nerv-redux/index.js](https://github.com/NervJS/nerv/blob/aaa405e79de5926e30ff07a0bb1b94dc994e9446/packages/nerv-redux/index.js)
- [packages/nerv-server/index.js](https://github.com/NervJS/nerv/blob/aaa405e79de5926e30ff07a0bb1b94dc994e9446/packages/nerv-server/index.js)
- [packages/nerv-shared/index.js](https://github.com/NervJS/nerv/blob/aaa405e79de5926e30ff07a0bb1b94dc994e9446/packages/nerv-shared/index.js)
- [packages/nerv-test-utils/index.js](https://github.com/NervJS/nerv/blob/aaa405e79de5926e30ff07a0bb1b94dc994e9446/packages/nerv-test-utils/index.js)
- [packages/nerv-utils/index.js](https://github.com/NervJS/nerv/blob/aaa405e79de5926e30ff07a0bb1b94dc994e9446/packages/nerv-utils/index.js)
- [packages/nerv/index.js](https://github.com/NervJS/nerv/blob/aaa405e79de5926e30ff07a0bb1b94dc994e9446/packages/nerv/index.js)
- [benchmarks/DBMonster/app.js](https://github.com/NervJS/nerv/blob/aaa405e79de5926e30ff07a0bb1b94dc994e9446/benchmarks/DBMonster/app.js)
- [benchmarks/js-framwork-bench/src/Main.jsx](https://github.com/NervJS/nerv/blob/aaa405e79de5926e30ff07a0bb1b94dc994e9446/benchmarks/js-framwork-bench/src/Main.jsx)
- [benchmarks/uibench/app.js](https://github.com/NervJS/nerv/blob/aaa405e79de5926e30ff07a0bb1b94dc994e9446/benchmarks/uibench/app.js)
- [index.js](https://github.com/NervJS/nerv/blob/aaa405e79de5926e30ff07a0bb1b94dc994e9446/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| benchmarks package | library | Observed | Groups 12 file(s) under benchmarks package (observed from repository paths and static analysis). |
| browsers package | library | Observed | Groups 3 file(s) under browsers package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 14 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 6 file(s) under core modules (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 102 file(s) under packages package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.travis.yml` (ci)
- `azure-pipelines.yml` (ci)
- `lerna.json` (config)
- `package.json` (manifest)
- `packages/nerv-create-class/package.json` (manifest)
- `packages/nerv-devtools/package.json` (manifest)
- `packages/nerv-is/package.json` (manifest)
- `packages/nerv-redux/package.json` (manifest)
- `packages/nerv-server/package.json` (manifest)
- `packages/nerv-shared/package.json` (manifest)
- `packages/nerv-test-utils/package.json` (manifest)
- `packages/nerv-utils/package.json` (manifest)
- `packages/nerv/package.json` (manifest)
- `tsconfig.json` (config)
- `tslint.json` (config)

## Top-level layout

- `packages` — 129 analysed file(s)
- `(root files)` — 21 analysed file(s)
- `benchmarks` — 21 analysed file(s)
- `browsers` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `aaa405e79de5926e30ff07a0bb1b94dc994e9446` is the revision these paths and observations refer to.
