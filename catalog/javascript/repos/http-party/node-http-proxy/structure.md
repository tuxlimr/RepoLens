# Project structure: http-party/node-http-proxy

**Analysed commit:** `9b96cd725127a024dabebec6c7ea8c807272223d`

**Commit reference:** [9b96cd725127a024dabebec6c7ea8c807272223d](https://github.com/http-party/node-http-proxy/commit/9b96cd725127a024dabebec6c7ea8c807272223d)

**Tree at this commit:** [http-party/node-http-proxy@9b96cd725127](https://github.com/http-party/node-http-proxy/tree/9b96cd725127a024dabebec6c7ea8c807272223d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | http-party/node-http-proxy |
| Description | A full-featured http proxy for node.js |
| Stars | 14119 |
| Forks | 1987 |
| Licence | Other |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `9b96cd725127a024dabebec6c7ea8c807272223d` |
| Retrieved at | 2026-11-14T19:11:46.626492+00:00 |
| Files in this snapshot | 55 |

## Directory tree

```text
benchmark/  (4 files)
  scripts/  (3 files)
    hello.js
    proxy.js
    websockets-throughput.js
  README.md
examples/  (24 files)
  balancer/  (2 files)
    simple-balancer-with-websockets.js
    simple-balancer.js
  helpers/  (1 files)
    store.js
  http/  (14 files)
    basic-proxy.js
    concurrent-proxy.js
    custom-proxy-error.js
    error-handling.js
    forward-and-target-proxy.js
    forward-proxy.js
    latent-proxy.js
    ntlm-authentication.js
    proxy-http-to-https.js
    proxy-https-to-http.js
    proxy-https-to-https.js
    reverse-proxy.js
    sse.js
    standalone-proxy.js
  middleware/  (3 files)
    bodyDecoder-middleware.js
    gzip-middleware.js
    modifyResponse-middleware.js
  websocket/  (3 files)
    latent-websocket-proxy.js
    standalone-websocket-proxy.js
    websocket-proxy.js
  package.json
lib/  (6 files)
  http-proxy/  (5 files)
    passes/  (3 files)
      … 3 files under this directory
    common.js
    index.js
  http-proxy.js
test/  (7 files)
  examples-test.js
  lib-http-proxy-common-test.js
  lib-http-proxy-passes-web-incoming-test.js
  lib-http-proxy-passes-web-outgoing-test.js
  lib-http-proxy-passes-ws-incoming-test.js
  lib-http-proxy-test.js
  lib-https-proxy-test.js
.auto-changelog
.gitattributes
.gitignore
.npmignore
.travis.yml
CHANGELOG.md
CODE_OF_CONDUCT.md
LICENSE
README.md
UPGRADING.md
codecov.yml
index.js
package.json
renovate.json
```

## Entry points

- [index.js](https://github.com/http-party/node-http-proxy/blob/9b96cd725127a024dabebec6c7ea8c807272223d/index.js)
- [lib/http-proxy/index.js](https://github.com/http-party/node-http-proxy/blob/9b96cd725127a024dabebec6c7ea8c807272223d/lib/http-proxy/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| benchmark package | library | Observed | Groups 3 file(s) under benchmark package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 6 file(s) under lib package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 7 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.travis.yml` (ci)
- `codecov.yml` (config)
- `examples/package.json` (manifest)
- `package.json` (manifest)
- `renovate.json` (config)

## Top-level layout

- `examples` — 24 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `test` — 7 analysed file(s)
- `lib` — 6 analysed file(s)
- `benchmark` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 3 file(s) were skipped during inventory (2 x likely secret file excluded; 1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `9b96cd725127a024dabebec6c7ea8c807272223d` is the revision these paths and observations refer to.
