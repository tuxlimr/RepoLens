# Project structure: tj/co

**Analysed commit:** `249bbdc72da24ae44076afd716349d2089b31c4c`

**Commit reference:** [249bbdc72da24ae44076afd716349d2089b31c4c](https://github.com/tj/co/commit/249bbdc72da24ae44076afd716349d2089b31c4c)

**Tree at this commit:** [tj/co@249bbdc72da2](https://github.com/tj/co/tree/249bbdc72da24ae44076afd716349d2089b31c4c)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | tj/co |
| Description | The ultimate generator based flow-control goodness for nodejs (supports thunks, promises, etc) |
| Stars | 11823 |
| Forks | 778 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `249bbdc72da24ae44076afd716349d2089b31c4c` |
| Retrieved at | 2026-11-14T19:12:13.666970+00:00 |
| Files in this snapshot | 19 |

## Directory tree

```text
test/  (11 files)
  arguments.js
  arrays.js
  context.js
  generator-functions.js
  generators.js
  invalid.js
  objects.js
  promises.js
  recursion.js
  thunks.js
  wrap.js
.gitignore
.travis.yml
History.md
LICENSE
Readme.md
component.json
index.js
package.json
```

## Entry points

- [index.js](https://github.com/tj/co/blob/249bbdc72da24ae44076afd716349d2089b31c4c/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 11 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.travis.yml` (ci)
- `component.json` (config)
- `package.json` (manifest)

## Top-level layout

- `test` — 11 analysed file(s)
- `(root files)` — 8 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `249bbdc72da24ae44076afd716349d2089b31c4c` is the revision these paths and observations refer to.
