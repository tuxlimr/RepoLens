# Project structure: tariqbuilds/linux-dash

**Analysed commit:** `186a802ea76e8bfcab7e8e7ebc533b74f80306fc`

**Commit reference:** [186a802ea76e8bfcab7e8e7ebc533b74f80306fc](https://github.com/tariqbuilds/linux-dash/commit/186a802ea76e8bfcab7e8e7ebc533b74f80306fc)

**Tree at this commit:** [tariqbuilds/linux-dash@186a802ea76e](https://github.com/tariqbuilds/linux-dash/tree/186a802ea76e8bfcab7e8e7ebc533b74f80306fc)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | tariqbuilds/linux-dash |
| Description | A beautiful web dashboard for Linux |
| Stars | 10575 |
| Forks | 1179 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `186a802ea76e8bfcab7e8e7ebc533b74f80306fc` |
| Retrieved at | 2026-11-14T19:12:36.825580+00:00 |
| Files in this snapshot | 57 |

## Directory tree

```text
app/  (7 files)
  server/  (6 files)
    config/  (1 files)
      … 1 files under this directory
    index.go
    index.js
    index.php
    index.py
    linux_json_api.sh
  index.html
bin/  (1 files)
  linux-dash
src/  (41 files)
  css/  (5 files)
    README.md
    buttons.css
    main.css
    plugins-cotnainer.css
    tables.css
  js/  (36 files)
    core/  (25 files)
      … 25 files under this directory
    plugins/  (10 files)
      … 10 files under this directory
    README.md
.gitignore
LICENSE.md
README.md
demo.js
ecosystem.config.js
gulpfile.js
index.html
package.json
```

## Entry points

- [app/server/index.py:50](https://github.com/tariqbuilds/linux-dash/blob/186a802ea76e8bfcab7e8e7ebc533b74f80306fc/app/server/index.py#L50)
- [app/server/index.js](https://github.com/tariqbuilds/linux-dash/blob/186a802ea76e8bfcab7e8e7ebc533b74f80306fc/app/server/index.js)
- [bin/linux-dash](https://github.com/tariqbuilds/linux-dash/blob/186a802ea76e8bfcab7e8e7ebc533b74f80306fc/bin/linux-dash)
- [src/js/core/app.js](https://github.com/tariqbuilds/linux-dash/blob/186a802ea76e8bfcab7e8e7ebc533b74f80306fc/src/js/core/app.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| app package | library | Observed | Groups 4 file(s) under app package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: MainHandler, ThreadedHTTPServer. |
| js package | library | Observed | Groups 8 file(s) under js package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 14 file(s) under service / domain layer (observed from repository paths and static analysis). |

## Important files

- `package.json` (manifest)

## Top-level layout

- `src` — 41 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `app` — 7 analysed file(s)
- `bin` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x generated/minified file excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `186a802ea76e8bfcab7e8e7ebc533b74f80306fc` is the revision these paths and observations refer to.
