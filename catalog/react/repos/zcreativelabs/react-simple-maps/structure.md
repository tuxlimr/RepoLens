# Project structure: zcreativelabs/react-simple-maps

**Analysed commit:** `80d87555f3226ab0267119ef7bf4c36658a52be5`

**Commit reference:** [80d87555f3226ab0267119ef7bf4c36658a52be5](https://github.com/zcreativelabs/react-simple-maps/commit/80d87555f3226ab0267119ef7bf4c36658a52be5)

**Tree at this commit:** [zcreativelabs/react-simple-maps@80d87555f322](https://github.com/zcreativelabs/react-simple-maps/tree/80d87555f3226ab0267119ef7bf4c36658a52be5)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | zcreativelabs/react-simple-maps |
| Description | Composable SVG map charts for data visualization in React |
| Stars | 3393 |
| Forks | 460 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `80d87555f3226ab0267119ef7bf4c36658a52be5` |
| Retrieved at | 2026-11-14T19:15:20.943244+00:00 |
| Files in this snapshot | 45 |

## Directory tree

```text
scripts/  (1 files)
  smoke-types.sh
src/  (33 files)
  core/  (24 files)
    components/  (18 files)
      … 18 files under this directory
    hooks/  (2 files)
      … 2 files under this directory
    types/  (1 files)
      … 1 files under this directory
    index.ts
    utils.test.ts
    utils.ts
  zoom/  (8 files)
    components/  (4 files)
      … 4 files under this directory
    hooks/  (2 files)
      … 2 files under this directory
    types/  (1 files)
      … 1 files under this directory
    index.ts
  index.ts
.gitignore
.prettierrc.json
CHANGELOG.md
CODE_OF_CONDUCT.md
LICENSE
README.md
package.json
rollup.config.js
tsconfig.build.json
tsconfig.json
vitest.config.ts
```

## Entry points

- [src/core/index.ts](https://github.com/zcreativelabs/react-simple-maps/blob/80d87555f3226ab0267119ef7bf4c36658a52be5/src/core/index.ts)
- [src/core/types/index.ts](https://github.com/zcreativelabs/react-simple-maps/blob/80d87555f3226ab0267119ef7bf4c36658a52be5/src/core/types/index.ts)
- [src/index.ts](https://github.com/zcreativelabs/react-simple-maps/blob/80d87555f3226ab0267119ef7bf4c36658a52be5/src/index.ts)
- [src/zoom/index.ts](https://github.com/zcreativelabs/react-simple-maps/blob/80d87555f3226ab0267119ef7bf4c36658a52be5/src/zoom/index.ts)
- [src/zoom/types/index.ts](https://github.com/zcreativelabs/react-simple-maps/blob/80d87555f3226ab0267119ef7bf4c36658a52be5/src/zoom/types/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| index.ts package | library | Observed | Groups 1 file(s) under index.ts package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 24 file(s) under service / domain layer (observed from repository paths and static analysis). |
| zoom package | library | Observed | Groups 8 file(s) under zoom package (observed from repository paths and static analysis). |

## Important files

- `.prettierrc.json` (config)
- `package.json` (manifest)
- `tsconfig.build.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `src` — 33 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `80d87555f3226ab0267119ef7bf4c36658a52be5` is the revision these paths and observations refer to.
