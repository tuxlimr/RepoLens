# Project structure: konvajs/react-konva

**Analysed commit:** `be9feb46cacfdff6c4c3bb0277b222448c7c94f7`

**Commit reference:** [be9feb46cacfdff6c4c3bb0277b222448c7c94f7](https://github.com/konvajs/react-konva/commit/be9feb46cacfdff6c4c3bb0277b222448c7c94f7)

**Tree at this commit:** [konvajs/react-konva@be9feb46cacf](https://github.com/konvajs/react-konva/tree/be9feb46cacfdff6c4c3bb0277b222448c7c94f7)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | konvajs/react-konva |
| Description | React components for the Konva 2d canvas library. Build interactive graphics, design editors, and whiteboards with JSX. |
| Stars | 6446 |
| Forks | 294 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `be9feb46cacfdff6c4c3bb0277b222448c7c94f7` |
| Retrieved at | 2026-11-14T19:14:05.407925+00:00 |
| Files in this snapshot | 63 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (2 files)
    release.yml
    test.yml
  FUNDING.yml
benchmarks/  (8 files)
  README.md
  counts-results.json
  counts.bench.tsx
  events-results.json
  events.bench.tsx
  run.mjs
  vitest.config.mts
  vitest.counts.config.mts
docs/  (1 files)
  react-compatibility.md
src/  (5 files)
  EventBatch.ts
  ReactKonva.ts
  ReactKonvaCore.tsx
  ReactKonvaHostConfig.ts
  makeUpdates.ts
test/  (36 files)
  helpers/  (4 files)
    html-fixture.tsx
    konva-helpers.ts
    mocking.ts
    render.tsx
  types/  (2 files)
    consumer.tsx
    tsconfig.json
  01-mounting.test.tsx
  02-scheduler.test.tsx
  03-suspense.test.tsx
  04-strict-mode.test.tsx
  05-roots-portals.test.tsx
  06-sync-external-store.test.tsx
  07-mobx-race.test.tsx
  08-stage-destroy.test.tsx
  09-event-handling.test.tsx
  10-refs-lifecycle.test.tsx
  11-ssr.mjs
  12-memory.test.tsx
  13-error-handling.test.tsx
  15-design-decisions.test.tsx
  16-scheduling-invariants.test.tsx
  17-transformer-state-sync.test.tsx
  18-drawing.test.tsx
  19-test-cleanup.test.tsx
  20-transformer-geometry.test.tsx
  21-native-events.test.tsx
  22-optional-event-batch.test.tsx
  23-event-batch-composition.test.tsx
  24-package-exports.mjs
  24-transformer-group-children.test.tsx
  … 6 more files
.gitignore
.travis.yml
LICENSE
README.md
RELEASE_NOTES.md
ReactKonvaCore.d.ts
build.mjs
package.json
tsconfig.json
vitest.config.mts
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| benchmarks package | library | Observed | Groups 3 file(s) under benchmarks package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| EventBatch.ts package | library | Observed | Groups 1 file(s) under eventbatch.ts package (observed from repository paths and static analysis). |
| makeUpdates.ts package | library | Observed | Groups 1 file(s) under makeupdates.ts package (observed from repository paths and static analysis). |
| ReactKonva.ts package | library | Observed | Groups 1 file(s) under reactkonva.ts package (observed from repository paths and static analysis). |
| ReactKonvaCore.tsx package | library | Observed | Groups 1 file(s) under reactkonvacore.tsx package (observed from repository paths and static analysis). |
| ReactKonvaHostConfig.ts package | library | Observed | Groups 1 file(s) under reactkonvahostconfig.ts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 36 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `.travis.yml` (ci)
- `benchmarks/counts-results.json` (config)
- `benchmarks/events-results.json` (config)
- `package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `test` — 36 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `benchmarks` — 8 analysed file(s)
- `src` — 5 analysed file(s)
- `.github` — 3 analysed file(s)
- `docs` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `be9feb46cacfdff6c4c3bb0277b222448c7c94f7` is the revision these paths and observations refer to.
