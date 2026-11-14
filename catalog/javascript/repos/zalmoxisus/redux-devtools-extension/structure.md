# Project structure: zalmoxisus/redux-devtools-extension

**Analysed commit:** `955cfc4f9c2ed7b4212ad8ff50883ad322051678`

**Commit reference:** [955cfc4f9c2ed7b4212ad8ff50883ad322051678](https://github.com/zalmoxisus/redux-devtools-extension/commit/955cfc4f9c2ed7b4212ad8ff50883ad322051678)

**Tree at this commit:** [zalmoxisus/redux-devtools-extension@955cfc4f9c2e](https://github.com/zalmoxisus/redux-devtools-extension/tree/955cfc4f9c2ed7b4212ad8ff50883ad322051678)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | zalmoxisus/redux-devtools-extension |
| Description | Redux DevTools extension. |
| Stars | 13430 |
| Forks | 1005 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `955cfc4f9c2ed7b4212ad8ff50883ad322051678` |
| Retrieved at | 2026-11-14T19:11:56.455255+00:00 |
| Files in this snapshot | 200 |

## Directory tree

```text
docs/  (13 files)
  API/  (3 files)
    Arguments.md
    Methods.md
    README.md
  Features/  (1 files)
    Trace.md
  Articles.md
  Credits.md
  FAQ.md
  Feedback.md
  Integrations.md
  README.md
  Recipes.md
  Troubleshooting.md
  Videos.md
examples/  (87 files)
  counter/  (17 files)
    actions/  (1 files)
      … 1 files under this directory
    components/  (1 files)
      … 1 files under this directory
    containers/  (1 files)
      … 1 files under this directory
    reducers/  (2 files)
      … 2 files under this directory
    store/  (1 files)
      … 1 files under this directory
    test/  (5 files)
      … 5 files under this directory
    .babelrc
    index.html
    index.js
    package.json
    server.js
    webpack.config.js
  react-counter-messaging/  (6 files)
    components/  (1 files)
      … 1 files under this directory
    .babelrc
    index.html
    index.js
    package.json
    webpack.config.js
  router/  (28 files)
    actions/  (1 files)
      … 1 files under this directory
    components/  (5 files)
      … 5 files under this directory
    constants/  (2 files)
      … 2 files under this directory
    containers/  (3 files)
      … 3 files under this directory
    reducers/  (2 files)
      … 2 files under this directory
    store/  (1 files)
      … 1 files under this directory
    test/  (8 files)
      … 8 files under this directory
    .babelrc
    index.html
    index.js
    package.json
    server.js
    webpack.config.js
  saga-counter/  (8 files)
    src/  (4 files)
      … 4 files under this directory
    .babelrc
    index.html
    package.json
    webpack.config.js
  todomvc/  (27 files)
    actions/  (2 files)
      … 2 files under this directory
    components/  (5 files)
      … 5 files under this directory
    constants/  (2 files)
      … 2 files under this directory
    containers/  (1 files)
      … 1 files under this directory
    reducers/  (2 files)
      … 2 files under this directory
    store/  (1 files)
      … 1 files under this directory
    test/  (8 files)
      … 8 files under this directory
    .babelrc
    index.html
    index.js
    package.json
    server.js
    webpack.config.js
  buildAll.js
npm-package/  (11 files)
  utils/  (1 files)
    assign.js
  README.md
  developmentOnly.d.ts
  developmentOnly.js
  index.d.ts
  index.js
  logOnly.d.ts
  logOnly.js
  logOnlyInProduction.d.ts
  logOnlyInProduction.js
  package.json
src/  (54 files)
  app/  (22 files)
    api/  (6 files)
      … 6 files under this directory
    containers/  (1 files)
      … 1 files under this directory
    middlewares/  (4 files)
      … 4 files under this directory
    reducers/  (5 files)
      … 5 files under this directory
    service/  (1 files)
      … 1 files under this directory
    stores/  (5 files)
      … 5 files under this directory
  assets/  (1 files)
    img/  (1 files)
      … 1 files under this directory
  browser/  (31 files)
    extension/  (24 files)
      … 24 files under this directory
    firefox/  (1 files)
      … 1 files under this directory
    views/  (6 files)
      … 6 files under this directory
test/  (15 files)
  app/  (4 files)
    containers/  (1 files)
      … 1 files under this directory
    inject/  (2 files)
      … 2 files under this directory
    setup.js
  chrome/  (1 files)
    extension.spec.js
  electron/  (5 files)
    fixture/  (4 files)
      … 4 files under this directory
    devpanel.spec.js
  perf/  (2 files)
    data.js
    send.spec.js
  utils/  (2 files)
    e2e.js
    inject.js
  .eslintrc
webpack/  (6 files)
  replace/  (2 files)
    JsonpMainTemplate.runtime.js
    log-apply-result.js
  base.config.js
  dev.config.js
  prod.config.js
  wrap.config.js
.babelrc
.bookignore
.eslintignore
.eslintrc
.gitignore
.travis.yml
CHANGELOG.md
CODE_OF_CONDUCT.md
LICENSE
README.md
appveyor.yml
book.json
gulpfile.babel.js
package.json
```

## Entry points

- [npm-package/index.js](https://github.com/zalmoxisus/redux-devtools-extension/blob/955cfc4f9c2ed7b4212ad8ff50883ad322051678/npm-package/index.js)
- [test/electron/fixture/main.js](https://github.com/zalmoxisus/redux-devtools-extension/blob/955cfc4f9c2ed7b4212ad8ff50883ad322051678/test/electron/fixture/main.js)
- [src/app/api/index.js](https://github.com/zalmoxisus/redux-devtools-extension/blob/955cfc4f9c2ed7b4212ad8ff50883ad322051678/src/app/api/index.js)
- [src/app/containers/App.js](https://github.com/zalmoxisus/redux-devtools-extension/blob/955cfc4f9c2ed7b4212ad8ff50883ad322051678/src/app/containers/App.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 6 file(s) under api layer (observed from repository paths and static analysis). |
| app package | library | Observed | Groups 15 file(s) under app package (observed from repository paths and static analysis). |
| browser package | library | Observed | Groups 23 file(s) under browser package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| npm-package package | library | Observed | Groups 9 file(s) under npm-package package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 1 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 36 file(s) under tests (observed from repository paths and static analysis). |
| webpack package | library | Observed | Groups 6 file(s) under webpack package (observed from repository paths and static analysis). |

## Important files

- `.travis.yml` (ci)
- `appveyor.yml` (config)
- `book.json` (config)
- `examples/counter/package.json` (manifest)
- `examples/react-counter-messaging/package.json` (manifest)
- `examples/router/package.json` (manifest)
- `examples/saga-counter/package.json` (manifest)
- `examples/todomvc/package.json` (manifest)
- `npm-package/package.json` (manifest)
- `package.json` (manifest)
- `src/browser/extension/manifest.json` (config)
- `src/browser/firefox/manifest.json` (config)

## Top-level layout

- `examples` — 87 analysed file(s)
- `src` — 54 analysed file(s)
- `test` — 15 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `docs` — 13 analysed file(s)
- `npm-package` — 11 analysed file(s)
- `webpack` — 6 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `955cfc4f9c2ed7b4212ad8ff50883ad322051678` is the revision these paths and observations refer to.
