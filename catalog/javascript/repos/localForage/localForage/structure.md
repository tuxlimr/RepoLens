# Project structure: localForage/localForage

**Analysed commit:** `fb78c77ee583fb727a558c439b5174aca38c5924`

**Commit reference:** [fb78c77ee583fb727a558c439b5174aca38c5924](https://github.com/localForage/localForage/commit/fb78c77ee583fb727a558c439b5174aca38c5924)

**Tree at this commit:** [localForage/localForage@fb78c77ee583](https://github.com/localForage/localForage/tree/fb78c77ee583fb727a558c439b5174aca38c5924)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | localForage/localForage |
| Description | 💾 Offline storage, improved. Wraps IndexedDB, WebSQL, or localStorage using a simple but powerful API. |
| Stars | 25801 |
| Forks | 1288 |
| Licence | Apache-2.0 |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `fb78c77ee583fb727a558c439b5174aca38c5924` |
| Retrieved at | 2026-11-14T19:10:59.820267+00:00 |
| Files in this snapshot | 87 |

## Directory tree

```text
docs/  (9 files)
  fonts/  (1 files)
    icomoon.svg
  scripts/  (2 files)
    flatdoc.js
    legacy.js
  theme/  (3 files)
    localforage.css
    script.js
    style.css
  README.txt
  api.md
  index.html
examples/  (10 files)
  dbquota-error.html
  dropInstance.html
  index.html
  indexeddb-invalidstate.html
  main.js
  no-driver.html
  polyfill.html
  require.html
  require.js
  websql-foo.html
src/  (17 files)
  drivers/  (3 files)
    indexeddb.js
    localstorage.js
    websql.js
  utils/  (13 files)
    createBlob.js
    executeCallback.js
    executeTwoCallbacks.js
    getCallback.js
    idb.js
    includes.js
    isArray.js
    isIndexedDBValid.js
    isLocalStorageValid.js
    isWebSQLValid.js
    normalizeKey.js
    promise.js
    serializer.js
  localforage.js
test/  (30 files)
  dummyStorageDriver.js
  runner.browserify.js
  runner.js
  runner.webpack.js
  saucelabs-browsers.js
  serviceworker-client.js
  test.api.js
  test.browserify.html
  test.callwhenready.html
  test.callwhenready.js
  test.config.js
  test.customdriver.html
  test.customdriver.js
  test.datatypes.js
  test.drivers.js
  test.faultydriver.html
  test.faultydriver.js
  test.iframecontents.html
  test.iframes.js
  test.main.html
  test.main1.html
  test.min.html
  test.nodriver.html
  test.nodriver.js
  … 6 more files
typing-tests/  (2 files)
  localforage-tests.ts
  tsconfig.json
typings/  (1 files)
  localforage.d.ts
.babelrc
.babelrc-umd
.eslintrc
.gitignore
.huskyrc
.lintstagedrc
.npmignore
.prettierrc
.travis.yml
CHANGELOG.md
CONTRIBUTING.md
Gruntfile.js
LICENSE
README.md
bower.json
component.json
contribute.json
package.json
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| drivers package | library | Observed | Groups 3 file(s) under drivers package (observed from repository paths and static analysis). |
| localforage.js package | library | Observed | Groups 1 file(s) under localforage.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 30 file(s) under tests (observed from repository paths and static analysis). |
| typing-tests package | library | Observed | Groups 1 file(s) under typing-tests package (observed from repository paths and static analysis). |
| typings package | library | Observed | Groups 1 file(s) under typings package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 13 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.travis.yml` (ci)
- `bower.json` (config)
- `component.json` (config)
- `contribute.json` (config)
- `package.json` (manifest)
- `typing-tests/tsconfig.json` (config)

## Top-level layout

- `test` — 30 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `src` — 17 analysed file(s)
- `examples` — 10 analysed file(s)
- `docs` — 9 analysed file(s)
- `typing-tests` — 2 analysed file(s)
- `typings` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 3 file(s) were skipped during inventory (1 x likely secret file excluded; 2 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `fb78c77ee583fb727a558c439b5174aca38c5924` is the revision these paths and observations refer to.
