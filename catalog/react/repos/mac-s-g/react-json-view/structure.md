# Project structure: mac-s-g/react-json-view

**Analysed commit:** `443465ebdaa236da8c5d0e7bda2b7e57ca5d5a7b`

**Commit reference:** [443465ebdaa236da8c5d0e7bda2b7e57ca5d5a7b](https://github.com/mac-s-g/react-json-view/commit/443465ebdaa236da8c5d0e7bda2b7e57ca5d5a7b)

**Tree at this commit:** [mac-s-g/react-json-view@443465ebdaa2](https://github.com/mac-s-g/react-json-view/tree/443465ebdaa236da8c5d0e7bda2b7e57ca5d5a7b)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | mac-s-g/react-json-view |
| Description | JSON viewer for react |
| Stars | 3658 |
| Forks | 493 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `443465ebdaa236da8c5d0e7bda2b7e57ca5d5a7b` |
| Retrieved at | 2026-11-14T19:15:10.718240+00:00 |
| Files in this snapshot | 108 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    ci-tests.yml
demo/  (7 files)
  src/  (7 files)
    js/  (4 files)
      … 4 files under this directory
    style/  (3 files)
      … 3 files under this directory
dev-server/  (1 files)
  src/  (1 files)
    index.js
doc/  (3 files)
  example-usage.js
  rjv-icon-alt.svg
  rjv-icon.svg
docker/  (17 files)
  entrypoints/  (7 files)
    build.sh
    coverage.sh
    debug.sh
    demo.sh
    dev-server.sh
    test-watch.sh
    test.sh
  README.md
  build-container.sh
  build-demo.sh
  build-dist.sh
  coverage.sh
  debug.sh
  dev-server.sh
  shell.sh
  test-watch.sh
  test.sh
src/  (34 files)
  js/  (33 files)
    components/  (24 files)
      … 24 files under this directory
    helpers/  (4 files)
      … 4 files under this directory
    stores/  (1 files)
      … 1 files under this directory
    themes/  (3 files)
      … 3 files under this directory
    index.js
  style/  (1 files)
    scss/  (1 files)
      … 1 files under this directory
test/  (29 files)
  testHelpers/  (1 files)
    requireSources.js
  tests/  (28 files)
    js/  (28 files)
      … 28 files under this directory
webpack/  (3 files)
  webpack.config-demo.js
  webpack.config-dev.js
  webpack.config.js
.babelrc
.coveralls.yml
.eslintrc.json
.gitignore
.npmignore
.nycrc
.prettierrc.json
.travis.yml
Dockerfile
LICENSE
README.md
index.d.ts
package.json
```

## Entry points

- [demo/src/js/index.js](https://github.com/mac-s-g/react-json-view/blob/443465ebdaa236da8c5d0e7bda2b7e57ca5d5a7b/demo/src/js/index.js)
- [dev-server/src/index.js](https://github.com/mac-s-g/react-json-view/blob/443465ebdaa236da8c5d0e7bda2b7e57ca5d5a7b/dev-server/src/index.js)
- [src/js/index.js](https://github.com/mac-s-g/react-json-view/blob/443465ebdaa236da8c5d0e7bda2b7e57ca5d5a7b/src/js/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| demo package | library | Observed | Groups 4 file(s) under demo package (observed from repository paths and static analysis). |
| dev-server package | library | Observed | Groups 1 file(s) under dev-server package (observed from repository paths and static analysis). |
| docker package | library | Observed | Groups 16 file(s) under docker package (observed from repository paths and static analysis). |
| js package | library | Observed | Groups 33 file(s) under js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 29 file(s) under tests (observed from repository paths and static analysis). |
| webpack package | library | Observed | Groups 3 file(s) under webpack package (observed from repository paths and static analysis). |

## Important files

- `.coveralls.yml` (config)
- `.eslintrc.json` (config)
- `.github/workflows/ci-tests.yml` (ci)
- `.prettierrc.json` (config)
- `.travis.yml` (ci)
- `Dockerfile` (container)
- `package.json` (manifest)

## Top-level layout

- `src` — 34 analysed file(s)
- `test` — 29 analysed file(s)
- `docker` — 17 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `demo` — 7 analysed file(s)
- `doc` — 3 analysed file(s)
- `webpack` — 3 analysed file(s)
- `.github` — 1 analysed file(s)
- `dev-server` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `443465ebdaa236da8c5d0e7bda2b7e57ca5d5a7b` is the revision these paths and observations refer to.
