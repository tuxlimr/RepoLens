# Project structure: willmcpo/body-scroll-lock

**Analysed commit:** `79c4cf2c956eb7d5cf8d54a03d12751bc6ac8aa3`

**Commit reference:** [79c4cf2c956eb7d5cf8d54a03d12751bc6ac8aa3](https://github.com/willmcpo/body-scroll-lock/commit/79c4cf2c956eb7d5cf8d54a03d12751bc6ac8aa3)

**Tree at this commit:** [willmcpo/body-scroll-lock@79c4cf2c956e](https://github.com/willmcpo/body-scroll-lock/tree/79c4cf2c956eb7d5cf8d54a03d12751bc6ac8aa3)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | willmcpo/body-scroll-lock |
| Description | Body scroll locking that just works with everything 😏 |
| Stars | 4090 |
| Forks | 323 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `79c4cf2c956eb7d5cf8d54a03d12751bc6ac8aa3` |
| Retrieved at | 2026-11-14T19:14:53.229729+00:00 |
| Files in this snapshot | 31 |

## Directory tree

```text
.circleci/  (1 files)
  config.yml
examples/  (14 files)
  modal/  (7 files)
    .gitignore
    README.md
    bundle.js
    index.html
    main.js
    now.json
    package.json
  vanilla/  (7 files)
    .gitignore
    README.md
    bundle.js
    index.html
    main.js
    now.json
    package.json
flow-typed/  (1 files)
  globals.js
lib/  (3 files)
  bodyScrollLock.es6.js
  bodyScrollLock.esm.js
  bodyScrollLock.js
src/  (1 files)
  bodyScrollLock.js
.babelrc
.editorconfig
.eslintrc
.flowconfig
.gitignore
.npmignore
.prettierignore
.prettierrc
LICENSE
README.md
package.json
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bodyScrollLock.js package | library | Observed | Groups 1 file(s) under bodyscrolllock.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| flow-typed package | library | Observed | Groups 1 file(s) under flow-typed package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 3 file(s) under lib package (observed from repository paths and static analysis). |

## Important files

- `.circleci/config.yml` (ci)
- `.editorconfig` (config)
- `examples/modal/now.json` (config)
- `examples/modal/package.json` (manifest)
- `examples/vanilla/now.json` (config)
- `examples/vanilla/package.json` (manifest)
- `package.json` (manifest)

## Top-level layout

- `examples` — 14 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `lib` — 3 analysed file(s)
- `.circleci` — 1 analysed file(s)
- `flow-typed` — 1 analysed file(s)
- `src` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `79c4cf2c956eb7d5cf8d54a03d12751bc6ac8aa3` is the revision these paths and observations refer to.
