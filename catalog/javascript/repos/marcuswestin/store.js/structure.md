# Project structure: marcuswestin/store.js

**Analysed commit:** `fe77ae9e7ca1c8fb9af27b9f53a14722cd14d9d4`

**Commit reference:** [fe77ae9e7ca1c8fb9af27b9f53a14722cd14d9d4](https://github.com/marcuswestin/store.js/commit/fe77ae9e7ca1c8fb9af27b9f53a14722cd14d9d4)

**Tree at this commit:** [marcuswestin/store.js@fe77ae9e7ca1](https://github.com/marcuswestin/store.js/tree/fe77ae9e7ca1c8fb9af27b9f53a14722cd14d9d4)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | marcuswestin/store.js |
| Description | Cross-browser storage for all use cases, used across the web. |
| Stars | 13971 |
| Forks | 1293 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `fe77ae9e7ca1c8fb9af27b9f53a14722cd14d9d4` |
| Retrieved at | 2026-11-14T19:11:48.151077+00:00 |
| Files in this snapshot | 61 |

## Directory tree

```text
.circleci/  (1 files)
  config.yml
plugins/  (24 files)
  lib/  (2 files)
    json2.js
    lz-string.js
  all.js
  all_tests.js
  compression.js
  compression_test.js
  defaults.js
  defaults_test.js
  dump.js
  dump_test.js
  events.js
  events_test.js
  expire.js
  expire_test.js
  json2.js
  json2_test.js
  observe.js
  observe_test.js
  operations.js
  operations_test.js
  update.js
  update_test.js
  v1-backcompat.js
  v1-backcompat_test.js
scripts/  (11 files)
  saucelabs/  (5 files)
    list-supported-browsers.js
    saucelabs-api.js
    saucelabs-platformSets.js
    saucelabs.js
    tunnel.js
  compile-builds.js
  create-tunnel.js
  release.sh
  run-browser-tests-live-reload.js
  run-node-tests.js
  run-saucelabs-tests.js
src/  (2 files)
  store-engine.js
  util.js
storages/  (7 files)
  all.js
  cookieStorage.js
  localStorage.js
  memoryStorage.js
  oldFF-globalStorage.js
  oldIE-userDataStorage.js
  sessionStorage.js
tests/  (7 files)
  bugs/  (5 files)
    all.js
    gh-215.js
    gh-235.js
    gh-236.js
    gh-239.js
  tests.js
  util.js
.gitignore
COPYRIGHT
Changelog
LICENSE
Makefile
README-More.md
README.md
package.json
sublime-storejs.sublime-project
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| plugins package | library | Observed | Groups 24 file(s) under plugins package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 11 file(s) under scripts package (observed from repository paths and static analysis). |
| storages package | library | Observed | Groups 7 file(s) under storages package (observed from repository paths and static analysis). |
| store-engine.js package | library | Observed | Groups 1 file(s) under store-engine.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 7 file(s) under tests (observed from repository paths and static analysis). |
| util.js package | library | Observed | Groups 1 file(s) under util.js package (observed from repository paths and static analysis). |

## Important files

- `.circleci/config.yml` (ci)
- `package.json` (manifest)

## Top-level layout

- `plugins` — 24 analysed file(s)
- `scripts` — 11 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `storages` — 7 analysed file(s)
- `tests` — 7 analysed file(s)
- `src` — 2 analysed file(s)
- `.circleci` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 6 file(s) were skipped during inventory (1 x lockfile excluded; 5 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `fe77ae9e7ca1c8fb9af27b9f53a14722cd14d9d4` is the revision these paths and observations refer to.
