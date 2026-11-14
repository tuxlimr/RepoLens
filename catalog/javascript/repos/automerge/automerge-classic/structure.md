# Project structure: automerge/automerge-classic

**Analysed commit:** `0605308926a03353eb1072c3afa2a3a8580fcef9`

**Commit reference:** [0605308926a03353eb1072c3afa2a3a8580fcef9](https://github.com/automerge/automerge-classic/commit/0605308926a03353eb1072c3afa2a3a8580fcef9)

**Tree at this commit:** [automerge/automerge-classic@0605308926a0](https://github.com/automerge/automerge-classic/tree/0605308926a03353eb1072c3afa2a3a8580fcef9)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | automerge/automerge-classic |
| Description | A JSON-like data structure (a CRDT) that can be modified concurrently by different users, and merged again automatically. |
| Stars | 14681 |
| Forks | 460 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `0605308926a03353eb1072c3afa2a3a8580fcef9` |
| Retrieved at | 2026-11-14T19:11:43.620375+00:00 |
| Files in this snapshot | 54 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    automerge-ci.yml
@types/  (1 files)
  automerge/  (1 files)
    index.d.ts
backend/  (7 files)
  backend.js
  columnar.js
  encoding.js
  index.js
  new.js
  sync.js
  util.js
frontend/  (10 files)
  apply_patch.js
  constants.js
  context.js
  counter.js
  index.js
  numbers.js
  observable.js
  proxies.js
  table.js
  text.js
img/  (3 files)
  brandmark.svg
  lockup.svg
  sign.svg
src/  (3 files)
  automerge.js
  common.js
  uuid.js
test/  (17 files)
  backend_test.js
  columnar_test.js
  context_test.js
  encoding_test.js
  frontend_test.js
  fuzz_test.js
  helpers.js
  new_backend_test.js
  observable_test.js
  proxies_test.js
  sync_test.js
  table_test.js
  test.js
  text_test.js
  typescript_test.ts
  uuid_test.js
  wasm.js
.babelrc
.eslintrc.json
.gitignore
.mocharc.yaml
CHANGELOG.md
LICENSE
README.md
karma.conf.js
karma.sauce.js
package.json
tsconfig.json
webpack.config.js
```

## Entry points

- [src/automerge.js](https://github.com/automerge/automerge-classic/blob/0605308926a03353eb1072c3afa2a3a8580fcef9/src/automerge.js)
- [backend/index.js](https://github.com/automerge/automerge-classic/blob/0605308926a03353eb1072c3afa2a3a8580fcef9/backend/index.js)
- [frontend/index.js](https://github.com/automerge/automerge-classic/blob/0605308926a03353eb1072c3afa2a3a8580fcef9/frontend/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| automerge.js package | library | Observed | Groups 1 file(s) under automerge.js package (observed from repository paths and static analysis). |
| backend package | library | Observed | Groups 7 file(s) under backend package (observed from repository paths and static analysis). |
| common.js package | library | Observed | Groups 1 file(s) under common.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| frontend package | library | Observed | Groups 10 file(s) under frontend package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 17 file(s) under tests (observed from repository paths and static analysis). |
| @types package | library | Observed | Groups 1 file(s) under @types package (observed from repository paths and static analysis). |
| uuid.js package | library | Observed | Groups 1 file(s) under uuid.js package (observed from repository paths and static analysis). |

## Important files

- `.eslintrc.json` (config)
- `.github/workflows/automerge-ci.yml` (ci)
- `.mocharc.yaml` (config)
- `package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `test` — 17 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `frontend` — 10 analysed file(s)
- `backend` — 7 analysed file(s)
- `img` — 3 analysed file(s)
- `src` — 3 analysed file(s)
- `.github` — 1 analysed file(s)
- `@types` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `0605308926a03353eb1072c3afa2a3a8580fcef9` is the revision these paths and observations refer to.
