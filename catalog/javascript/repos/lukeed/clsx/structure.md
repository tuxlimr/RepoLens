# Project structure: lukeed/clsx

**Analysed commit:** `925494cf31bcd97d3337aacd34e659e80cae7fe2`

**Commit reference:** [925494cf31bcd97d3337aacd34e659e80cae7fe2](https://github.com/lukeed/clsx/commit/925494cf31bcd97d3337aacd34e659e80cae7fe2)

**Tree at this commit:** [lukeed/clsx@925494cf31bc](https://github.com/lukeed/clsx/tree/925494cf31bcd97d3337aacd34e659e80cae7fe2)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | lukeed/clsx |
| Description | A tiny (239B) utility for constructing `className` strings conditionally. |
| Stars | 9848 |
| Forks | 189 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `925494cf31bcd97d3337aacd34e659e80cae7fe2` |
| Retrieved at | 2026-11-14T19:12:48.677419+00:00 |
| Files in this snapshot | 18 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (1 files)
    ci.yml
  FUNDING.yml
bench/  (3 files)
  index.js
  package.json
  readme.md
bin/  (1 files)
  index.js
src/  (2 files)
  index.js
  lite.js
test/  (3 files)
  classnames.js
  index.js
  lite.js
.editorconfig
.gitignore
clsx.d.mts
clsx.d.ts
license
package.json
readme.md
```

## Entry points

- [bench/index.js](https://github.com/lukeed/clsx/blob/925494cf31bcd97d3337aacd34e659e80cae7fe2/bench/index.js)
- [bin/index.js](https://github.com/lukeed/clsx/blob/925494cf31bcd97d3337aacd34e659e80cae7fe2/bin/index.js)
- [src/index.js](https://github.com/lukeed/clsx/blob/925494cf31bcd97d3337aacd34e659e80cae7fe2/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bench package | library | Observed | Groups 1 file(s) under bench package (observed from repository paths and static analysis). |
| bin package | library | Observed | Groups 1 file(s) under bin package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| lite.js package | library | Observed | Groups 1 file(s) under lite.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 3 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `bench/package.json` (manifest)
- `package.json` (manifest)

## Top-level layout

- `(root files)` — 7 analysed file(s)
- `bench` — 3 analysed file(s)
- `test` — 3 analysed file(s)
- `.github` — 2 analysed file(s)
- `src` — 2 analysed file(s)
- `bin` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `925494cf31bcd97d3337aacd34e659e80cae7fe2` is the revision these paths and observations refer to.
