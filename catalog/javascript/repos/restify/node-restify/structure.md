# Project structure: restify/node-restify

**Analysed commit:** `71e09da528112619ec42b600a2bbab240e3eff60`

**Commit reference:** [71e09da528112619ec42b600a2bbab240e3eff60](https://github.com/restify/node-restify/commit/71e09da528112619ec42b600a2bbab240e3eff60)

**Tree at this commit:** [restify/node-restify@71e09da52811](https://github.com/restify/node-restify/tree/71e09da528112619ec42b600a2bbab240e3eff60)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | restify/node-restify |
| Description | The future of Node.js REST development |
| Stars | 10687 |
| Forks | 976 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `71e09da528112619ec42b600a2bbab240e3eff60` |
| Retrieved at | 2026-11-14T19:12:34.383348+00:00 |
| Files in this snapshot | 188 |

## Directory tree

```text
.github/  (11 files)
  ISSUE_TEMPLATE/  (2 files)
    1-bug-report.md
    2-feature-request.md
  workflows/  (3 files)
    ci.yml
    npm-publish.yml
    release-please.yml
  PULL_REQUEST_TEMPLATE.md
  prerelease-config.json
  prerelease-manifest.json
  release-config.json
  release-manifest.json
  stale.yml
benchmark/  (8 files)
  benchmarks/  (4 files)
    middleware.js
    response-json.js
    response-text.js
    router-heavy.js
  lib/  (2 files)
    autocannon.js
    bench.js
  index.js
  package.json
bin/  (1 files)
  report-latency
docs/  (22 files)
  _api/  (5 files)
    formatters.md
    plugins.md
    request.md
    response.md
    server.md
  api/  (6 files)
    formatters-usage.md
    plugins-usage.md
    request-events.md
    request-log.md
    server-errors.md
    server-events.md
  config/  (4 files)
    formatters.yaml
    plugins.yaml
    request.yaml
    server.yaml
  guides/  (6 files)
    4TO5GUIDE.md
    6to7guide.md
    8to9guide.md
    client.md
    dtrace.md
    server.md
  index.md
examples/  (15 files)
  dtrace/  (3 files)
    demo.js
    handler-timing.d
    hello.js
  http2/  (1 files)
    http2.js
  jsonp/  (1 files)
    jsonp.js
  sockio/  (2 files)
    package.json
    sockio.js
  todoapp/  (7 files)
    lib/  (3 files)
      … 3 files under this directory
    test/  (1 files)
      … 1 files under this directory
    README.md
    main.js
    package.json
  example.js
lib/  (56 files)
  formatters/  (5 files)
    binary.js
    index.js
    json.js
    jsonp.js
    text.js
  helpers/  (1 files)
    chainComposer.js
  plugins/  (37 files)
    pre/  (7 files)
      … 7 files under this directory
    utils/  (4 files)
      … 4 files under this directory
    accept.js
    audit.js
    authorization.js
    bodyParser.js
    bodyReader.js
    conditionalHandler.js
    conditionalRequest.js
    cpuUsageThrottle.js
    date.js
    fieldedTextBodyParser.js
    formBodyParser.js
    fullResponse.js
    gzip.js
    index.js
    inflightRequestThrottle.js
    jsonBodyParser.js
    jsonp.js
    metrics.js
    multipartBodyParser.js
    oauth2TokenParser.js
    query.js
    requestExpiry.js
    requestLogger.js
    static.js
    … 2 more files
  chain.js
  deprecationWarnings.js
  dtrace.js
  errorTypes.js
  http_date.js
  index.js
  request.js
  response.js
  router.js
  routerRegistryRadix.js
  server.js
  upgrade.js
  utils.js
test/  (54 files)
  lib/  (3 files)
    helper.js
    server-withDisableUncaughtException.js
    streamRecorder.js
  plugins/  (37 files)
    files/  (4 files)
      … 4 files under this directory
    testStaticFiles/  (5 files)
      … 5 files under this directory
    .eslintrc
    accept.test.js
    audit.test.js
    authorization.test.js
    bodyReader.test.js
    conditionalHandler.test.js
    conditionalRequest.test.js
    context.test.js
    cpuUsageThrottle.test.js
    dedupeSlashes.test.js
    fieldedTextParser.test.js
    formBodyParser.test.js
    gzip.test.js
    inflightRequestThrottle.test.js
    jsonBodyParser.test.js
    metrics.test.js
    multipart.test.js
    oauth2.test.js
    plugins.test.js
    query.test.js
    reqIdHeaders.test.js
    requestExpiry.test.js
    static.test.js
    staticFiles.test.js
    … 4 more files
  .eslintrc
  chain.test.js
  chainComposer.test.js
  formatter-optional.test.js
  formatter.test.js
  index.test.js
  request.test.js
  response.test.js
  router.test.js
  routerRegistryRadix.test.js
  server.test.js
  serverHttp2.test.js
  upgrade.test.js
  utils.test.js
tools/  (4 files)
  mk/  (3 files)
    Makefile.defs
    Makefile.deps
    Makefile.targ
  docsBuild.js
.dir-locals.el
.eslintignore
.eslintrc.js
.gitignore
.npmignore
.prettierignore
.prettierrc
.tern-project
CHANGELOG.md
CHANGES.md
CONTRIBUTING.md
FEATURE_REQUESTS.md
LICENSE
Makefile
README.md
SECURITY.md
package.json
```

## Entry points

- [benchmark/index.js](https://github.com/restify/node-restify/blob/71e09da528112619ec42b600a2bbab240e3eff60/benchmark/index.js)
- [examples/sockio/sockio.js](https://github.com/restify/node-restify/blob/71e09da528112619ec42b600a2bbab240e3eff60/examples/sockio/sockio.js)
- [examples/todoapp/main.js](https://github.com/restify/node-restify/blob/71e09da528112619ec42b600a2bbab240e3eff60/examples/todoapp/main.js)
- [lib/index.js](https://github.com/restify/node-restify/blob/71e09da528112619ec42b600a2bbab240e3eff60/lib/index.js)
- [bin/report-latency](https://github.com/restify/node-restify/blob/71e09da528112619ec42b600a2bbab240e3eff60/bin/report-latency)
- [lib/formatters/index.js](https://github.com/restify/node-restify/blob/71e09da528112619ec42b600a2bbab240e3eff60/lib/formatters/index.js)
- [lib/plugins/index.js](https://github.com/restify/node-restify/blob/71e09da528112619ec42b600a2bbab240e3eff60/lib/plugins/index.js)
- [lib/server.js](https://github.com/restify/node-restify/blob/71e09da528112619ec42b600a2bbab240e3eff60/lib/server.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| benchmark package | library | Observed | Groups 7 file(s) under benchmark package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 56 file(s) under lib package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 55 file(s) under tests (observed from repository paths and static analysis). |
| tools package | library | Observed | Groups 1 file(s) under tools package (observed from repository paths and static analysis). |

## Important files

- `.github/prerelease-config.json` (config)
- `.github/prerelease-manifest.json` (config)
- `.github/release-config.json` (config)
- `.github/release-manifest.json` (config)
- `.github/stale.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/npm-publish.yml` (ci)
- `.github/workflows/release-please.yml` (ci)
- `benchmark/package.json` (manifest)
- `docs/config/formatters.yaml` (config)
- `docs/config/plugins.yaml` (config)
- `docs/config/request.yaml` (config)
- `docs/config/server.yaml` (config)
- `examples/sockio/package.json` (manifest)
- `examples/todoapp/package.json` (manifest)
- `package.json` (manifest)

## Top-level layout

- `lib` — 56 analysed file(s)
- `test` — 54 analysed file(s)
- `docs` — 22 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `examples` — 15 analysed file(s)
- `.github` — 11 analysed file(s)
- `benchmark` — 8 analysed file(s)
- `tools` — 4 analysed file(s)
- `bin` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 6 file(s) were skipped during inventory (6 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `71e09da528112619ec42b600a2bbab240e3eff60` is the revision these paths and observations refer to.
