# Project structure: websockets/ws

**Analysed commit:** `fc667e495bd63052ac78fc2a149dbf948d1d3d02`

**Commit reference:** [fc667e495bd63052ac78fc2a149dbf948d1d3d02](https://github.com/websockets/ws/commit/fc667e495bd63052ac78fc2a149dbf948d1d3d02)

**Tree at this commit:** [websockets/ws@fc667e495bd6](https://github.com/websockets/ws/tree/fc667e495bd63052ac78fc2a149dbf948d1d3d02)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | websockets/ws |
| Description | Simple to use, blazing fast and thoroughly tested WebSocket client and server for Node.js |
| Stars | 22829 |
| Forks | 2682 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `fc667e495bd63052ac78fc2a149dbf948d1d3d02` |
| Retrieved at | 2026-11-14T19:11:06.630302+00:00 |
| Files in this snapshot | 57 |

## Directory tree

```text
.github/  (4 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.yml
    config.yml
  workflows/  (1 files)
    ci.yml
  FUNDING.yml
bench/  (3 files)
  parser.benchmark.js
  sender.benchmark.js
  speed.js
doc/  (1 files)
  ws.md
examples/  (8 files)
  express-session-parse/  (4 files)
    public/  (2 files)
      … 2 files under this directory
    index.js
    package.json
  server-stats/  (3 files)
    public/  (1 files)
      … 1 files under this directory
    index.js
    package.json
  ssl.js
lib/  (13 files)
  buffer-util.js
  constants.js
  event-target.js
  extension.js
  limiter.js
  permessage-deflate.js
  receiver.js
  sender.js
  stream.js
  subprotocol.js
  validation.js
  websocket-server.js
  websocket.js
test/  (16 files)
  autobahn-server.js
  autobahn.js
  buffer-util.test.js
  create-websocket-stream.test.js
  duplex-pair.js
  event-target.test.js
  extension.test.js
  limiter.test.js
  permessage-deflate.test.js
  receiver.test.js
  sender.test.js
  subprotocol.test.js
  validation.test.js
  websocket-server.test.js
  websocket.integration.js
  websocket.test.js
.gitattributes
.gitignore
.prettierrc.yaml
FUNDING.json
LICENSE
README.md
SECURITY.md
browser.js
eslint.config.js
index.js
package.json
wrapper.mjs
```

## Entry points

- [index.js](https://github.com/websockets/ws/blob/fc667e495bd63052ac78fc2a149dbf948d1d3d02/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bench package | library | Observed | Groups 3 file(s) under bench package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 13 file(s) under lib package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 16 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.prettierrc.yaml` (config)
- `FUNDING.json` (config)
- `examples/express-session-parse/package.json` (manifest)
- `examples/server-stats/package.json` (manifest)
- `package.json` (manifest)

## Top-level layout

- `test` — 16 analysed file(s)
- `lib` — 13 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `examples` — 8 analysed file(s)
- `.github` — 4 analysed file(s)
- `bench` — 3 analysed file(s)
- `doc` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 7 file(s) were skipped during inventory (7 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `fc667e495bd63052ac78fc2a149dbf948d1d3d02` is the revision these paths and observations refer to.
