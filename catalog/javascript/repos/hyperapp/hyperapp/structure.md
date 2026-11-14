# Project structure: hyperapp/hyperapp

**Analysed commit:** `5a113fa00450302be9234e0a74ee634ed5574243`

**Commit reference:** [5a113fa00450302be9234e0a74ee634ed5574243](https://github.com/hyperapp/hyperapp/commit/5a113fa00450302be9234e0a74ee634ed5574243)

**Tree at this commit:** [hyperapp/hyperapp@5a113fa00450](https://github.com/hyperapp/hyperapp/tree/5a113fa00450302be9234e0a74ee634ed5574243)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | hyperapp/hyperapp |
| Description | 1kB-ish JavaScript framework for building hypertext applications |
| Stars | 19190 |
| Forks | 777 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `5a113fa00450302be9234e0a74ee634ed5574243` |
| Retrieved at | 2026-11-14T19:11:17.506332+00:00 |
| Files in this snapshot | 36 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    ci.yml
docs/  (13 files)
  api/  (4 files)
    app.md
    h.md
    memo.md
    text.md
  architecture/  (7 files)
    actions.md
    dispatch.md
    effects.md
    flowchart.md
    state.md
    subscriptions.md
    views.md
  reference.md
  tutorial.md
packages/  (15 files)
  dom/  (3 files)
    README.md
    index.js
    package.json
  events/  (3 files)
    README.md
    index.js
    package.json
  html/  (3 files)
    README.md
    index.js
    package.json
  svg/  (3 files)
    README.md
    index.js
    package.json
  time/  (3 files)
    README.md
    index.js
    package.json
tests/  (1 files)
  index.test.js
.gitignore
LICENSE.md
README.md
index.d.ts
index.js
package.json
```

## Entry points

- [index.js](https://github.com/hyperapp/hyperapp/blob/5a113fa00450302be9234e0a74ee634ed5574243/index.js)
- [packages/dom/index.js](https://github.com/hyperapp/hyperapp/blob/5a113fa00450302be9234e0a74ee634ed5574243/packages/dom/index.js)
- [packages/events/index.js](https://github.com/hyperapp/hyperapp/blob/5a113fa00450302be9234e0a74ee634ed5574243/packages/events/index.js)
- [packages/html/index.js](https://github.com/hyperapp/hyperapp/blob/5a113fa00450302be9234e0a74ee634ed5574243/packages/html/index.js)
- [packages/svg/index.js](https://github.com/hyperapp/hyperapp/blob/5a113fa00450302be9234e0a74ee634ed5574243/packages/svg/index.js)
- [packages/time/index.js](https://github.com/hyperapp/hyperapp/blob/5a113fa00450302be9234e0a74ee634ed5574243/packages/time/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 5 file(s) under packages package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/ci.yml` (ci)
- `package.json` (manifest)
- `packages/dom/package.json` (manifest)
- `packages/events/package.json` (manifest)
- `packages/html/package.json` (manifest)
- `packages/svg/package.json` (manifest)
- `packages/time/package.json` (manifest)

## Top-level layout

- `packages` — 15 analysed file(s)
- `docs` — 13 analysed file(s)
- `(root files)` — 6 analysed file(s)
- `.github` — 1 analysed file(s)
- `tests` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `5a113fa00450302be9234e0a74ee634ed5574243` is the revision these paths and observations refer to.
