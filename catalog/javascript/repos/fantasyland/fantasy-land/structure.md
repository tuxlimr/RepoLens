# Project structure: fantasyland/fantasy-land

**Analysed commit:** `0fc5ba5b3699046b024d21fe023c8bfef8d482d0`

**Commit reference:** [0fc5ba5b3699046b024d21fe023c8bfef8d482d0](https://github.com/fantasyland/fantasy-land/commit/0fc5ba5b3699046b024d21fe023c8bfef8d482d0)

**Tree at this commit:** [fantasyland/fantasy-land@0fc5ba5b3699](https://github.com/fantasyland/fantasy-land/tree/0fc5ba5b3699046b024d21fe023c8bfef8d482d0)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | fantasyland/fantasy-land |
| Description | Specification for interoperability of common algebraic structures in JavaScript |
| Stars | 10244 |
| Forks | 369 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `0fc5ba5b3699046b024d21fe023c8bfef8d482d0` |
| Retrieved at | 2026-11-14T19:12:42.132213+00:00 |
| Files in this snapshot | 22 |

## Directory tree

```text
figures/  (2 files)
  dependencies.dot
  dependencies.sh
scripts/  (5 files)
  generate-es
  generate-js
  generate-readme
  generate-ts
  lint
test/  (2 files)
  index.js
  mocha.opts
.config
.eslintrc.json
.gitignore
.travis.yml
CONTRIBUTING.md
LICENSE
README.md
implementations.md
index.d.ts
index.js
index.mjs
names
package.json
```

## Entry points

- [index.js](https://github.com/fantasyland/fantasy-land/blob/0fc5ba5b3699046b024d21fe023c8bfef8d482d0/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| figures package | library | Observed | Groups 1 file(s) under figures package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 2 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.eslintrc.json` (config)
- `.travis.yml` (ci)
- `package.json` (manifest)

## Top-level layout

- `(root files)` — 13 analysed file(s)
- `scripts` — 5 analysed file(s)
- `figures` — 2 analysed file(s)
- `test` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `0fc5ba5b3699046b024d21fe023c8bfef8d482d0` is the revision these paths and observations refer to.
