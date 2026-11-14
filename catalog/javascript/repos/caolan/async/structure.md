# Project structure: caolan/async

**Analysed commit:** `3921e54bd0704157dbea238fdfcc0c3619abde1a`

**Commit reference:** [3921e54bd0704157dbea238fdfcc0c3619abde1a](https://github.com/caolan/async/commit/3921e54bd0704157dbea238fdfcc0c3619abde1a)

**Tree at this commit:** [caolan/async@3921e54bd070](https://github.com/caolan/async/tree/3921e54bd0704157dbea238fdfcc0c3619abde1a)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | caolan/async |
| Description | Async utilities for node and the browser |
| Stars | 28117 |
| Forks | 2386 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `3921e54bd0704157dbea238fdfcc0c3619abde1a` |
| Retrieved at | 2026-11-14T19:10:50.305457+00:00 |
| Files in this snapshot | 433 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (1 files)
    ci.yml
  ISSUE_TEMPLATE.md
  dependabot.yml
docs/  (208 files)
  v2/  (104 files)
    data/  (2 files)
      … 2 files under this directory
    fonts/  (8 files)
      … 8 files under this directory
    img/  (1 files)
      … 1 files under this directory
    scripts/  (6 files)
      … 6 files under this directory
    styles/  (3 files)
      … 3 files under this directory
    apply.js.html
    applyEach.js.html
    applyEachSeries.js.html
    asyncify.js.html
    auto.js.html
    autoInject.js.html
    cargo.js.html
    compose.js.html
    concat.js.html
    concatLimit.js.html
    concatSeries.js.html
    constant.js.html
    detect.js.html
    detectLimit.js.html
    detectSeries.js.html
    dir.js.html
    doDuring.js.html
    doUntil.js.html
    doWhilst.js.html
    during.js.html
    each.js.html
    eachLimit.js.html
    eachOf.js.html
    eachOfLimit.js.html
    … 60 more files
  v3/  (102 files)
    data/  (2 files)
      … 2 files under this directory
    fonts/  (8 files)
      … 8 files under this directory
    img/  (1 files)
      … 1 files under this directory
    scripts/  (5 files)
      … 5 files under this directory
    styles/  (3 files)
      … 3 files under this directory
    apply.js.html
    applyEach.js.html
    applyEachSeries.js.html
    asyncify.js.html
    auto.js.html
    autoInject.js.html
    cargo.js.html
    cargoQueue.js.html
    compose.js.html
    concat.js.html
    concatLimit.js.html
    concatSeries.js.html
    constant.js.html
    detect.js.html
    detectLimit.js.html
    detectSeries.js.html
    dir.js.html
    doUntil.js.html
    doWhilst.js.html
    each.js.html
    eachLimit.js.html
    eachOf.js.html
    eachOfLimit.js.html
    eachOfSeries.js.html
    … 59 more files
  .nojekyll
  index.html
lib/  (102 files)
  internal/  (25 files)
    DoublyLinkedList.js
    Heap.js
    applyEach.js
    asyncEachOfLimit.js
    awaitify.js
    breakLoop.js
    consoleFunc.js
    createTester.js
    eachOfLimit.js
    filter.js
    getIterator.js
    initialParams.js
    isArrayLike.js
    iterator.js
    map.js
    once.js
    onlyOnce.js
    parallel.js
    promiseCallback.js
    queue.js
    range.js
    reject.js
    setImmediate.js
    withoutIndex.js
    … 1 more files
  apply.js
  applyEach.js
  applyEachSeries.js
  asyncify.js
  auto.js
  autoInject.js
  cargo.js
  cargoQueue.js
  compose.js
  concat.js
  concatLimit.js
  concatSeries.js
  constant.js
  detect.js
  detectLimit.js
  detectSeries.js
  dir.js
  doUntil.js
  doWhilst.js
  each.js
  eachLimit.js
  eachOf.js
  eachOfLimit.js
  eachOfSeries.js
  … 53 more files
logo/  (1 files)
  async-logo.svg
perf/  (3 files)
  benchmark.js
  memory.js
  suites.js
support/  (47 files)
  jsdoc/  (38 files)
    theme/  (34 files)
      … 34 files under this directory
    jsdoc-custom.js
    jsdoc-fix-html.js
    jsdoc-import-path-plugin.js
    jsdoc.json
  aliases.txt
  build.test.js
  es.test.js
  generate-index.js
  index-template.js
  module_template.md
  sync-cjs-package.js
  sync-es-package.js
  xyz.sh
test/  (52 files)
  es2017/  (3 files)
    asyncFunctions.js
    asyncGenerators.js
    awaitableFunctions.js
  support/  (2 files)
    get_function_object.js
    setup.js
  .jshintrc
  apply.js
  applyEach.js
  asyncFunctions.js
  asyncify.js
  auto.js
  autoInject.js
  cargo.js
  cargoQueue.js
  compose.js
  concat.js
  consoleFunctions.js
  constant.js
  detect.js
  each.js
  eachOf.js
  ensureAsync.js
  every.js
  filter.js
  forever.js
  groupBy.js
  heap.js
  linked_list.js
  map.js
  … 23 more files
.babelrc
.editorconfig
.eslintignore
.eslintrc.json
.gitattributes
.gitignore
.npmignore
CHANGELOG.md
LICENSE
Makefile
README.es.md
README.md
bower.json
index.js
intro.md
karma.conf.js
package.json
```

## Entry points

- [index.js](https://github.com/caolan/async/blob/3921e54bd0704157dbea238fdfcc0c3619abde1a/index.js)
- [lib/index.js](https://github.com/caolan/async/blob/3921e54bd0704157dbea238fdfcc0c3619abde1a/lib/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 102 file(s) under lib package (observed from repository paths and static analysis). |
| perf package | library | Observed | Groups 3 file(s) under perf package (observed from repository paths and static analysis). |
| support package | library | Observed | Groups 14 file(s) under support package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 52 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.eslintrc.json` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `bower.json` (config)
- `docs/v2/data/methodNames.json` (config)
- `docs/v2/data/sourceFiles.json` (config)
- `docs/v3/data/methodNames.json` (config)
- `docs/v3/data/sourceFiles.json` (config)
- `package.json` (manifest)
- `support/jsdoc/jsdoc.json` (config)

## Top-level layout

- `docs` — 208 analysed file(s)
- `lib` — 102 analysed file(s)
- `test` — 52 analysed file(s)
- `support` — 47 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `.github` — 3 analysed file(s)
- `perf` — 3 analysed file(s)
- `logo` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 3 file(s) were skipped during inventory (3 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `3921e54bd0704157dbea238fdfcc0c3619abde1a` is the revision these paths and observations refer to.
