# Project structure: Netflix/falcor

**Analysed commit:** `39d64776cf9d87781b2791615dcbae73b2bcd2e1`

**Commit reference:** [39d64776cf9d87781b2791615dcbae73b2bcd2e1](https://github.com/Netflix/falcor/commit/39d64776cf9d87781b2791615dcbae73b2bcd2e1)

**Tree at this commit:** [Netflix/falcor@39d64776cf9d](https://github.com/Netflix/falcor/tree/39d64776cf9d87781b2791615dcbae73b2bcd2e1)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Netflix/falcor |
| Description | A JavaScript library for efficient data fetching |
| Stars | 10565 |
| Forks | 440 |
| Licence | Apache-2.0 |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `39d64776cf9d87781b2791615dcbae73b2bcd2e1` |
| Retrieved at | 2026-11-14T19:12:37.436232+00:00 |
| Files in this snapshot | 336 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (2 files)
    ci.yml
    docs.yml
doc/  (43 files)
  DataSource.html
  FromEsObserverAdapter.html
  Model.html
  Model.js.html
  ModelResponse.html
  ModelResponseObserver.html
  Observable.html
  Subscription.html
  ToEsSubscriptionAdapter.html
  get_getCache.js.html
  global.html
  index.html
  index.js.html
  internal_index.js.html
  invalidate_invalidatePathMaps.js.html
  invalidate_invalidatePathSets.js.html
  request_GetRequestV2.js.html
  request_RequestQueueV2.js.html
  request_complement.js.html
  response_AssignableDisposable.js.html
  response_ModelResponse.js.html
  response_ModelResponseObserver.js.html
  response_get_GetResponse.js.html
  response_set_SetResponse.js.html
  … 19 more files
examples/  (1 files)
  datasource/  (1 files)
    webWorkerSource.js
lib/  (143 files)
  deref/  (3 files)
    hasValidParentReference.js
    index.js
    sync.js
  errors/  (7 files)
    BoundJSONGraphModelError.js
    InvalidDerefInputError.js
    InvalidModelError.js
    InvalidSourceError.js
    MaxRetryExceededError.js
    NullInPathError.js
    applyErrorPrototype.js
  get/  (19 files)
    util/  (4 files)
      … 4 files under this directory
    followReference.js
    get.js
    getBoundValue.js
    getCache.js
    getCachePosition.js
    getValue.js
    getValueSync.js
    getVersion.js
    index.js
    onError.js
    onMissing.js
    onValue.js
    onValueType.js
    sync.js
    walkPath.js
  internal/  (18 files)
    absolutePath.js
    context.js
    head.js
    index.js
    invalidated.js
    key.js
    model-created.js
    next.js
    parent.js
    path.js
    prev.js
    privatePrefix.js
    ref-index.js
    ref.js
    refs-length.js
    reservedPrefix.js
    tail.js
    version.js
  invalidate/  (2 files)
    invalidatePathMaps.js
    invalidatePathSets.js
  lru/  (3 files)
    collect.js
    promote.js
    splice.js
  request/  (6 files)
    GetRequestV2.js
    RequestQueueV2.js
    RequestTypes.js
    complement.js
    flushGetRequest.js
    sendSetRequest.js
  response/  (16 files)
    get/  (6 files)
      … 6 files under this directory
    set/  (5 files)
      … 5 files under this directory
    AssignableDisposable.js
    CallResponse.js
    InvalidateResponse.js
    ModelResponse.js
    ModelResponseObserver.js
  schedulers/  (3 files)
    ASAPScheduler.js
    ImmediateScheduler.js
    TimeoutScheduler.js
  set/  (6 files)
    index.js
    setJSONGraphs.js
    setPathMaps.js
    setPathValues.js
    setValue.js
    sync.js
  support/  (38 files)
    array-flat-map.js
    clone.js
    createHardlink.js
    currentCacheVersion.js
    expireNode.js
    getExpires.js
    getSize.js
    getTimestamp.js
    getType.js
    hasOwn.js
    identity.js
    incrementVersion.js
    insertNode.js
    isAlreadyExpired.js
    isExpired.js
    isFunction.js
    isInternalKey.js
    isJSONEnvelope.js
    isJSONGraphEnvelope.js
    isObject.js
    isPathInvalidation.js
    isPathValue.js
    isPrimitive.js
    mergeJSONGraphNode.js
    … 14 more files
  typedefs/  (12 files)
    Atom.js
    DataSource.js
    JSONEnvelope.js
    JSONGraph.js
    JSONGraphEnvelope.js
    Key.js
    KeySet.js
    Observable.js
    Path.js
    PathSet.js
    PathValue.js
    Range.js
  types/  (3 files)
    atom.js
    error.js
    ref.js
  values/  (2 files)
    expires-never.js
    expires-now.js
  Model.js
  ModelDataSourceAdapter.js
  ModelRoot.js
  index.js
  toEsObservable.js
performance/  (29 files)
  formatter/  (2 files)
    CSVFormatter.js
    CSVTransform.js
  models/  (3 files)
    legacy/  (2 files)
      … 2 files under this directory
    index.js
  reporters/  (3 files)
    browserTestReporter.js
    karmaBenchmarkCSVReporter.js
    nodeTestReporter.js
  scripts/  (1 files)
    transformCSV.js
  tests/  (13 files)
    clone/  (1 files)
      … 1 files under this directory
    deref/  (1 files)
      … 1 files under this directory
    get/  (4 files)
      … 4 files under this directory
    lru/  (1 files)
      … 1 files under this directory
    request/  (1 files)
      … 1 files under this directory
    set/  (1 files)
      … 1 files under this directory
    inMemoryCache.js
    standard.js
    testMerge.js
    testSuite.js
  README.md
  TriggerDataSource.js
  browser.js
  device.js
  karma.conf.js
  node.js
  testRunner.js
test/  (98 files)
  data/  (10 files)
    expected/  (5 files)
      … 5 files under this directory
    Cache.js
    ErrorDataSource.js
    LocalDataSource.js
    ReducedCache.js
    asyncifyDataSource.js
  falcor/  (26 files)
    call/  (1 files)
      … 1 files under this directory
    deref/  (3 files)
      … 3 files under this directory
    error/  (1 files)
      … 1 files under this directory
    get/  (9 files)
      … 9 files under this directory
    invalidate/  (2 files)
      … 2 files under this directory
    schedulers/  (1 files)
      … 1 files under this directory
    set/  (8 files)
      … 8 files under this directory
    operations.spec.js
  get-core/  (8 files)
    deref.spec.js
    edges.spec.js
    errors.spec.js
    get.cache.spec.js
    missing.spec.js
    null.spec.js
    references.spec.js
    values.spec.js
  hardlink/  (2 files)
    hardlink.add.spec.js
    hardlink.remove.spec.js
  integration/  (4 files)
    call.spec.js
    dedupe.spec.js
    express.spec.js
    get.spec.js
  internal/  (7 files)
    request/  (5 files)
      … 5 files under this directory
    sync/  (1 files)
      … 1 files under this directory
    ModelRoot.comparator.spec.js
  invalidate/  (3 files)
    invalidate.spec.js
    pathMaps.spec.js
    pathSets.spec.js
  lru/  (4 files)
    lru.promote.get.spec.js
    lru.promote.set.spec.js
    lru.splice.expired.spec.js
    lru.splice.overwrite.spec.js
  response/  (1 files)
    ModelResponseObserver.spec.js
  set/  (22 files)
    jsonGraphs/  (5 files)
      … 5 files under this directory
    pathMaps/  (4 files)
      … 4 files under this directory
    pathValues/  (4 files)
      … 4 files under this directory
    support/  (8 files)
      … 8 files under this directory
    edge-cases.spec.js
  .eslintrc.yaml
  CacheGenerator.js
  Model.spec.js
  cleanData.js
  getCoreRunner.js
  getTestRunner.js
  isAssertionError.js
  outputGenerator.js
  testRunner.js
  toObs.js
  zipSpy.js
.bithoundrc
.editorconfig
.eslintrc
.gitignore
.npmignore
.travis.yml
CHANGELOG.md
LICENSE.txt
MIGRATIONS.md
OSSMETADATA
README.md
all.js
authors.txt
bower.json
browser.js
conf.json
gulpfile.js
package.json
server.js
webpack.config.js
```

## Entry points

- [lib/index.js](https://github.com/Netflix/falcor/blob/39d64776cf9d87781b2791615dcbae73b2bcd2e1/lib/index.js)
- [lib/deref/index.js](https://github.com/Netflix/falcor/blob/39d64776cf9d87781b2791615dcbae73b2bcd2e1/lib/deref/index.js)
- [lib/get/index.js](https://github.com/Netflix/falcor/blob/39d64776cf9d87781b2791615dcbae73b2bcd2e1/lib/get/index.js)
- [lib/internal/index.js](https://github.com/Netflix/falcor/blob/39d64776cf9d87781b2791615dcbae73b2bcd2e1/lib/internal/index.js)
- [lib/response/get/index.js](https://github.com/Netflix/falcor/blob/39d64776cf9d87781b2791615dcbae73b2bcd2e1/lib/response/get/index.js)
- [lib/response/set/index.js](https://github.com/Netflix/falcor/blob/39d64776cf9d87781b2791615dcbae73b2bcd2e1/lib/response/set/index.js)
- [lib/set/index.js](https://github.com/Netflix/falcor/blob/39d64776cf9d87781b2791615dcbae73b2bcd2e1/lib/set/index.js)
- [performance/models/index.js](https://github.com/Netflix/falcor/blob/39d64776cf9d87781b2791615dcbae73b2bcd2e1/performance/models/index.js)
- [performance/models/legacy/index.js](https://github.com/Netflix/falcor/blob/39d64776cf9d87781b2791615dcbae73b2bcd2e1/performance/models/legacy/index.js)
- [server.js](https://github.com/Netflix/falcor/blob/39d64776cf9d87781b2791615dcbae73b2bcd2e1/server.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 5 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 3 file(s) under data layer (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 143 file(s) under lib package (observed from repository paths and static analysis). |
| performance package | library | Observed | Groups 12 file(s) under performance package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 111 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/docs.yml` (ci)
- `.travis.yml` (ci)
- `bower.json` (config)
- `conf.json` (config)
- `package.json` (manifest)

## Top-level layout

- `lib` — 143 analysed file(s)
- `test` — 98 analysed file(s)
- `doc` — 43 analysed file(s)
- `performance` — 29 analysed file(s)
- `(root files)` — 20 analysed file(s)
- `.github` — 2 analysed file(s)
- `examples` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 26 file(s) were skipped during inventory (1 x likely secret file excluded; 25 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `39d64776cf9d87781b2791615dcbae73b2bcd2e1` is the revision these paths and observations refer to.
