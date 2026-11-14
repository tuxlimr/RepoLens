# Project structure: chalk/chalk

**Analysed commit:** `72110019e147683f60e13fa0ff5c14a0c27cd9fe`

**Commit reference:** [72110019e147683f60e13fa0ff5c14a0c27cd9fe](https://github.com/chalk/chalk/commit/72110019e147683f60e13fa0ff5c14a0c27cd9fe)

**Tree at this commit:** [chalk/chalk@72110019e147](https://github.com/chalk/chalk/tree/72110019e147683f60e13fa0ff5c14a0c27cd9fe)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | chalk/chalk |
| Description | 🖍 Terminal string styling done right |
| Stars | 23338 |
| Forks | 1442 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `72110019e147683f60e13fa0ff5c14a0c27cd9fe` |
| Retrieved at | 2026-11-14T19:11:05.074727+00:00 |
| Files in this snapshot | 26 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (1 files)
    main.yml
  funding.yml
  security.md
examples/  (2 files)
  rainbow.js
  screenshot.js
media/  (1 files)
  logo.svg
source/  (3 files)
  index.d.ts
  index.js
  utilities.js
test/  (8 files)
  _fixture.js
  _force-color-fixture.js
  chalk.js
  force-color.js
  instance.js
  level.js
  no-color-support.js
  visible.js
.editorconfig
.gitattributes
.gitignore
benchmark.js
code-of-conduct.md
contributing.md
license
package.json
readme.md
```

## Entry points

- [source/index.js](https://github.com/chalk/chalk/blob/72110019e147683f60e13fa0ff5c14a0c27cd9fe/source/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| source package | library | Observed | Groups 3 file(s) under source package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 8 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/funding.yml` (config)
- `.github/workflows/main.yml` (ci)
- `package.json` (manifest)

## Top-level layout

- `(root files)` — 9 analysed file(s)
- `test` — 8 analysed file(s)
- `.github` — 3 analysed file(s)
- `source` — 3 analysed file(s)
- `examples` — 2 analysed file(s)
- `media` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 7 file(s) were skipped during inventory (1 x likely secret file excluded; 6 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `72110019e147683f60e13fa0ff5c14a0c27cd9fe` is the revision these paths and observations refer to.
