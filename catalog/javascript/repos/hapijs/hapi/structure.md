# Project structure: hapijs/hapi

**Analysed commit:** `f2837a006535a6fbbcf33692067c1bd497ba8124`

**Commit reference:** [f2837a006535a6fbbcf33692067c1bd497ba8124](https://github.com/hapijs/hapi/commit/f2837a006535a6fbbcf33692067c1bd497ba8124)

**Tree at this commit:** [hapijs/hapi@f2837a006535](https://github.com/hapijs/hapi/tree/f2837a006535a6fbbcf33692067c1bd497ba8124)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | hapijs/hapi |
| Description | The Simple, Secure Framework Developers Trust |
| Stars | 14798 |
| Forks | 1352 |
| Licence | Other |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `f2837a006535a6fbbcf33692067c1bd497ba8124` |
| Retrieved at | 2026-11-14T19:11:42.672170+00:00 |
| Files in this snapshot | 70 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    ci-module.yml
lib/  (38 files)
  types/  (18 files)
    server/  (12 files)
      … 12 files under this directory
    index.d.ts
    plugin.d.ts
    request.d.ts
    response.d.ts
    route.d.ts
    utils.d.ts
  auth.js
  compression.js
  config.js
  core.js
  cors.js
  ext.js
  handler.js
  headers.js
  index.d.ts
  index.js
  methods.js
  request.js
  response.js
  route.js
  security.js
  server.js
  streams.js
  toolkit.js
  transmit.js
  validation.js
test/  (24 files)
  file/  (1 files)
    note.txt
  templates/  (3 files)
    plugin/  (1 files)
      … 1 files under this directory
    invalid.html
    test.html
  types/  (1 files)
    index.ts
  .hidden
  auth.js
  common.js
  core.js
  cors.js
  handler.js
  headers.js
  index.js
  methods.js
  payload.js
  request.js
  response.js
  route.js
  security.js
  server.js
  state.js
  toolkit.js
  transmit.js
  validation.js
.gitignore
API.md
LICENSE.md
README.md
SPONSORS.md
package.json
typescript.md
```

## Entry points

- [lib/index.js](https://github.com/hapijs/hapi/blob/f2837a006535a6fbbcf33692067c1bd497ba8124/lib/index.js)
- [lib/server.js](https://github.com/hapijs/hapi/blob/f2837a006535a6fbbcf33692067c1bd497ba8124/lib/server.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 38 file(s) under lib package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 24 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/ci-module.yml` (ci)
- `package.json` (manifest)

## Top-level layout

- `lib` — 38 analysed file(s)
- `test` — 24 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `f2837a006535a6fbbcf33692067c1bd497ba8124` is the revision these paths and observations refer to.
