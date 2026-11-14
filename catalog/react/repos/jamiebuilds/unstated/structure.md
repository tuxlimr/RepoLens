# Project structure: jamiebuilds/unstated

**Analysed commit:** `0c8b3102d2ed404672a641d768f888804a2e7d2e`

**Commit reference:** [0c8b3102d2ed404672a641d768f888804a2e7d2e](https://github.com/jamiebuilds/unstated/commit/0c8b3102d2ed404672a641d768f888804a2e7d2e)

**Tree at this commit:** [jamiebuilds/unstated@0c8b3102d2ed](https://github.com/jamiebuilds/unstated/tree/0c8b3102d2ed404672a641d768f888804a2e7d2e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | jamiebuilds/unstated |
| Description | State so simple, it goes without saying |
| Stars | 7709 |
| Forks | 259 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `0c8b3102d2ed404672a641d768f888804a2e7d2e` |
| Retrieved at | 2026-11-14T19:13:49.756863+00:00 |
| Files in this snapshot | 21 |

## Directory tree

```text
__tests__/  (2 files)
  unstated.js
  unstated.tsx
example/  (4 files)
  complex.js
  index.html
  shared.js
  simple.js
flow-typed/  (1 files)
  npm/  (1 files)
    jest_v22.x.x.js
src/  (2 files)
  unstated.d.ts
  unstated.js
.babelrc
.babelrc.js
.flowconfig
.gitignore
.prettierrc
.travis.yml
LICENSE
README.md
logo.svg
package.json
rollup.config.js
tsconfig.json
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| flow-typed package | library | Observed | Groups 1 file(s) under flow-typed package (observed from repository paths and static analysis). |
| __tests__ package | library | Observed | Groups 2 file(s) under __tests__ package (observed from repository paths and static analysis). |
| unstated.d.ts package | library | Observed | Groups 1 file(s) under unstated.d.ts package (observed from repository paths and static analysis). |
| unstated.js package | library | Observed | Groups 1 file(s) under unstated.js package (observed from repository paths and static analysis). |

## Important files

- `.travis.yml` (ci)
- `package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `(root files)` — 12 analysed file(s)
- `example` — 4 analysed file(s)
- `__tests__` — 2 analysed file(s)
- `src` — 2 analysed file(s)
- `flow-typed` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `0c8b3102d2ed404672a641d768f888804a2e7d2e` is the revision these paths and observations refer to.
