# Project structure: vasturiano/react-force-graph

**Analysed commit:** `8c301c7a05b22c489b5724301bec52911b51d966`

**Commit reference:** [8c301c7a05b22c489b5724301bec52911b51d966](https://github.com/vasturiano/react-force-graph/commit/8c301c7a05b22c489b5724301bec52911b51d966)

**Tree at this commit:** [vasturiano/react-force-graph@8c301c7a05b2](https://github.com/vasturiano/react-force-graph/tree/8c301c7a05b22c489b5724301bec52911b51d966)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | vasturiano/react-force-graph |
| Description | React component for 2D, 3D, VR and AR force directed graphs |
| Stars | 3364 |
| Forks | 356 |
| Licence | MIT |
| Language | HTML |
| Default branch | master |
| Analysed commit | `8c301c7a05b22c489b5724301bec52911b51d966` |
| Retrieved at | 2026-11-14T19:15:22.015747+00:00 |
| Files in this snapshot | 66 |

## Directory tree

```text
.github/  (2 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
example/  (32 files)
  all-modes/  (1 files)
    index.html
  ar-graph/  (1 files)
    index.html
  auto-colored/  (1 files)
    index.html
  basic/  (1 files)
    index.html
  bloom-effect/  (1 files)
    index.html
  camera-auto-orbit/  (1 files)
    index.html
  click-to-focus/  (1 files)
    index.html
  collision-detection/  (1 files)
    index.html
  curved-links/  (1 files)
    index.html
  custom-node-shape/  (2 files)
    index-canvas.html
    index-three.html
  datasets/  (4 files)
    d3-dependencies.csv
    forcegraph-dependencies.json
    miserables.json
    random-data.js
  directional-links-arrows/  (1 files)
    index.html
  directional-links-particles/  (1 files)
    index.html
  dynamic/  (1 files)
    index.html
  emit-particles/  (1 files)
    index.html
  expandable-nodes/  (1 files)
    index.html
  fit-to-canvas/  (1 files)
    index.html
  fix-dragged-nodes/  (1 files)
    index.html
  forcegraph-dependencies/  (1 files)
    index.html
  highlight/  (1 files)
    index.html
  html-nodes/  (1 files)
    index.html
  img-nodes/  (1 files)
    index.html
  large-graph/  (1 files)
    index.html
  multi-selection/  (1 files)
    index.html
  text-links/  (1 files)
    index-3d.html
  text-nodes/  (2 files)
    index-2d.html
    index-3d.html
  tree/  (1 files)
    index.html
src/  (23 files)
  packages/  (20 files)
    react-force-graph-2d/  (5 files)
      … 5 files under this directory
    react-force-graph-3d/  (5 files)
      … 5 files under this directory
    react-force-graph-ar/  (5 files)
      … 5 files under this directory
    react-force-graph-vr/  (5 files)
      … 5 files under this directory
  forcegraph-proptypes.js
  index.d.ts
  index.js
.babelrc
.gitignore
.npmignore
LICENSE
README.md
_config.yml
package.json
rollup.config.dev.js
rollup.config.js
```

## Entry points

- [src/index.js](https://github.com/vasturiano/react-force-graph/blob/8c301c7a05b22c489b5724301bec52911b51d966/src/index.js)
- [src/packages/react-force-graph-2d/index.js](https://github.com/vasturiano/react-force-graph/blob/8c301c7a05b22c489b5724301bec52911b51d966/src/packages/react-force-graph-2d/index.js)
- [src/packages/react-force-graph-3d/index.js](https://github.com/vasturiano/react-force-graph/blob/8c301c7a05b22c489b5724301bec52911b51d966/src/packages/react-force-graph-3d/index.js)
- [src/packages/react-force-graph-ar/index.js](https://github.com/vasturiano/react-force-graph/blob/8c301c7a05b22c489b5724301bec52911b51d966/src/packages/react-force-graph-ar/index.js)
- [src/packages/react-force-graph-vr/index.js](https://github.com/vasturiano/react-force-graph/blob/8c301c7a05b22c489b5724301bec52911b51d966/src/packages/react-force-graph-vr/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| forcegraph-proptypes.js package | library | Observed | Groups 1 file(s) under forcegraph-proptypes.js package (observed from repository paths and static analysis). |
| index.d.ts package | library | Observed | Groups 1 file(s) under index.d.ts package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 16 file(s) under packages package (observed from repository paths and static analysis). |

## Important files

- `_config.yml` (config)
- `example/datasets/forcegraph-dependencies.json` (config)
- `example/datasets/miserables.json` (config)
- `package.json` (manifest)
- `src/packages/react-force-graph-2d/package.json` (manifest)
- `src/packages/react-force-graph-3d/package.json` (manifest)
- `src/packages/react-force-graph-ar/package.json` (manifest)
- `src/packages/react-force-graph-vr/package.json` (manifest)

## Top-level layout

- `example` — 32 analysed file(s)
- `src` — 23 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `.github` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `8c301c7a05b22c489b5724301bec52911b51d966` is the revision these paths and observations refer to.
