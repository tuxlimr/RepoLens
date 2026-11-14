# Project structure: supnate/rekit

**Analysed commit:** `987d852fe541c1cf3507a5c1cb14f829d8bf624b`

**Commit reference:** [987d852fe541c1cf3507a5c1cb14f829d8bf624b](https://github.com/supnate/rekit/commit/987d852fe541c1cf3507a5c1cb14f829d8bf624b)

**Tree at this commit:** [supnate/rekit@987d852fe541](https://github.com/supnate/rekit/tree/987d852fe541c1cf3507a5c1cb14f829d8bf624b)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | supnate/rekit |
| Description | IDE and toolkit for building scalable web applications with React, Redux and React-router |
| Stars | 4413 |
| Forks | 254 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `987d852fe541c1cf3507a5c1cb14f829d8bf624b` |
| Retrieved at | 2026-11-14T19:14:46.766112+00:00 |
| Files in this snapshot | 18 |

## Directory tree

```text
bin/  (1 files)
  rekit.js
scripts/  (1 files)
  craToRekit.js
tests/  (9 files)
  sanity/  (6 files)
    npmSanity.js
    plugin.js
    pluginSample.js
    rekit.js
    sanity.js
    twoPlugins.js
  .eslintrc
  npm_test.js
  sanity_test.js
.eslintrc
.gitignore
.prettierrc
LICENSE
README.md
package.json
rekit.json
```

## Entry points

- [bin/rekit.js](https://github.com/supnate/rekit/blob/987d852fe541c1cf3507a5c1cb14f829d8bf624b/bin/rekit.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bin package | library | Observed | Groups 1 file(s) under bin package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 9 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `package.json` (manifest)
- `rekit.json` (config)

## Top-level layout

- `tests` — 9 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `bin` — 1 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `987d852fe541c1cf3507a5c1cb14f829d8bf624b` is the revision these paths and observations refer to.
