# Project structure: mariusandra/pigeon-maps

**Analysed commit:** `3da030e2966fa27e563c0f4db3efb9dfd1356719`

**Commit reference:** [3da030e2966fa27e563c0f4db3efb9dfd1356719](https://github.com/mariusandra/pigeon-maps/commit/3da030e2966fa27e563c0f4db3efb9dfd1356719)

**Tree at this commit:** [mariusandra/pigeon-maps@3da030e2966f](https://github.com/mariusandra/pigeon-maps/tree/3da030e2966fa27e563c0f4db3efb9dfd1356719)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | mariusandra/pigeon-maps |
| Description | ReactJS Maps without external dependencies |
| Stars | 3520 |
| Forks | 144 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `3da030e2966fa27e563c0f4db3efb9dfd1356719` |
| Retrieved at | 2026-11-14T19:15:15.784762+00:00 |
| Files in this snapshot | 26 |

## Directory tree

```text
demo/  (4 files)
  Demo.tsx
  PigeonIcon.tsx
  index.html
  index.tsx
providers/  (1 files)
  package.json
src/  (10 files)
  controls/  (1 files)
    ZoomControl.tsx
  map/  (1 files)
    Map.tsx
  overlays/  (4 files)
    Draggable.tsx
    GeoJson.tsx
    Marker.tsx
    Overlay.tsx
  index.tsx
  providers.ts
  types.ts
  utils.ts
.babelrc
.eslintrc.js
.gitignore
.prettierrc.js
CHANGELOG.md
LICENSE.md
README.md
package.json
rollup.config.js
tsconfig.json
webpack.config.js
```

## Entry points

- [demo/index.tsx](https://github.com/mariusandra/pigeon-maps/blob/3da030e2966fa27e563c0f4db3efb9dfd1356719/demo/index.tsx)
- [src/index.tsx](https://github.com/mariusandra/pigeon-maps/blob/3da030e2966fa27e563c0f4db3efb9dfd1356719/src/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| controls package | library | Observed | Groups 1 file(s) under controls package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| demo package | library | Observed | Groups 3 file(s) under demo package (observed from repository paths and static analysis). |
| index.tsx package | library | Observed | Groups 1 file(s) under index.tsx package (observed from repository paths and static analysis). |
| map package | library | Observed | Groups 1 file(s) under map package (observed from repository paths and static analysis). |
| overlays package | library | Observed | Groups 4 file(s) under overlays package (observed from repository paths and static analysis). |
| providers.ts package | library | Observed | Groups 1 file(s) under providers.ts package (observed from repository paths and static analysis). |
| types.ts package | library | Observed | Groups 1 file(s) under types.ts package (observed from repository paths and static analysis). |
| utils.ts package | library | Observed | Groups 1 file(s) under utils.ts package (observed from repository paths and static analysis). |

## Important files

- `package.json` (manifest)
- `providers/package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `(root files)` — 11 analysed file(s)
- `src` — 10 analysed file(s)
- `demo` — 4 analysed file(s)
- `providers` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `3da030e2966fa27e563c0f4db3efb9dfd1356719` is the revision these paths and observations refer to.
