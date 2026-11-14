# Project structure: you-dont-need/You-Dont-Need-Momentjs

**Analysed commit:** `43977cf990a4af509a758a4e9a6af40f4485d34d`

**Commit reference:** [43977cf990a4af509a758a4e9a6af40f4485d34d](https://github.com/you-dont-need/You-Dont-Need-Momentjs/commit/43977cf990a4af509a758a4e9a6af40f4485d34d)

**Tree at this commit:** [you-dont-need/You-Dont-Need-Momentjs@43977cf990a4](https://github.com/you-dont-need/You-Dont-Need-Momentjs/tree/43977cf990a4af509a758a4e9a6af40f4485d34d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | you-dont-need/You-Dont-Need-Momentjs |
| Description | List of functions which you can use to replace moment.js + ESLint Plugin |
| Stars | 13280 |
| Forks | 312 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `43977cf990a4af509a758a4e9a6af40f4485d34d` |
| Retrieved at | 2026-11-14T19:11:58.776187+00:00 |
| Files in this snapshot | 19 |

## Directory tree

```text
__tests__/  (2 files)
  index.js
  performance.js
docs/  (3 files)
  .nojekyll
  README.md
  index.html
lib/  (8 files)
  __tests__/  (1 files)
    index.js
  rules/  (6 files)
    methods.json
    no-dynamic-import-moment.js
    no-import-moment.js
    no-moment-constructor.js
    no-moment-methods.js
    no-require-moment.js
  index.js
.gitignore
.prettierrc
.travis.yml
LICENSE
README.md
package.json
```

## Entry points

- [lib/index.js](https://github.com/you-dont-need/You-Dont-Need-Momentjs/blob/43977cf990a4af509a758a4e9a6af40f4485d34d/lib/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 7 file(s) under lib package (observed from repository paths and static analysis). |
| __tests__ package | library | Observed | Groups 2 file(s) under __tests__ package (observed from repository paths and static analysis). |

## Important files

- `.travis.yml` (ci)
- `lib/rules/methods.json` (config)
- `package.json` (manifest)

## Top-level layout

- `lib` — 8 analysed file(s)
- `(root files)` — 6 analysed file(s)
- `docs` — 3 analysed file(s)
- `__tests__` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `43977cf990a4af509a758a4e9a6af40f4485d34d` is the revision these paths and observations refer to.
