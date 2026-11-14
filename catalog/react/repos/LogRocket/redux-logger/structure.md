# Project structure: LogRocket/redux-logger

**Analysed commit:** `5816a9fc8da9b417589380e381ed66f1114ebd9a`

**Commit reference:** [5816a9fc8da9b417589380e381ed66f1114ebd9a](https://github.com/LogRocket/redux-logger/commit/5816a9fc8da9b417589380e381ed66f1114ebd9a)

**Tree at this commit:** [LogRocket/redux-logger@5816a9fc8da9](https://github.com/LogRocket/redux-logger/tree/5816a9fc8da9b417589380e381ed66f1114ebd9a)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | LogRocket/redux-logger |
| Description | Logger for Redux |
| Stars | 5710 |
| Forks | 316 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `5816a9fc8da9b417589380e381ed66f1114ebd9a` |
| Retrieved at | 2026-11-14T19:14:14.837219+00:00 |
| Files in this snapshot | 15 |

## Directory tree

```text
.circleci/  (1 files)
  config.yml
spec/  (3 files)
  diff.spec.js
  helpers.spec.js
  index.spec.js
src/  (5 files)
  core.js
  defaults.js
  diff.js
  helpers.js
  index.js
.babelrc
.gitignore
LICENSE
README.md
package.json
rollup.config.js
```

## Entry points

- [src/index.js](https://github.com/LogRocket/redux-logger/blob/5816a9fc8da9b417589380e381ed66f1114ebd9a/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| core.js package | library | Observed | Groups 1 file(s) under core.js package (observed from repository paths and static analysis). |
| defaults.js package | library | Observed | Groups 1 file(s) under defaults.js package (observed from repository paths and static analysis). |
| diff.js package | library | Observed | Groups 1 file(s) under diff.js package (observed from repository paths and static analysis). |
| helpers.js package | library | Observed | Groups 1 file(s) under helpers.js package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| spec package | library | Observed | Groups 3 file(s) under spec package (observed from repository paths and static analysis). |

## Important files

- `.circleci/config.yml` (ci)
- `package.json` (manifest)

## Top-level layout

- `(root files)` — 6 analysed file(s)
- `src` — 5 analysed file(s)
- `spec` — 3 analysed file(s)
- `.circleci` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `5816a9fc8da9b417589380e381ed66f1114ebd9a` is the revision these paths and observations refer to.
