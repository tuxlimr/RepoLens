# Project structure: catdad/canvas-confetti

**Analysed commit:** `20eebad51dde793070c373d594099a7ed8d96e22`

**Commit reference:** [20eebad51dde793070c373d594099a7ed8d96e22](https://github.com/catdad/canvas-confetti/commit/20eebad51dde793070c373d594099a7ed8d96e22)

**Tree at this commit:** [catdad/canvas-confetti@20eebad51dde](https://github.com/catdad/canvas-confetti/tree/20eebad51dde793070c373d594099a7ed8d96e22)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | catdad/canvas-confetti |
| Description | 🎉 performant confetti animation in the browser |
| Stars | 12860 |
| Forks | 471 |
| Licence | ISC |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `20eebad51dde793070c373d594099a7ed8d96e22` |
| Retrieved at | 2026-11-14T19:12:02.710438+00:00 |
| Files in this snapshot | 22 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (1 files)
    ci.yml
  funding.yml
bin/  (1 files)
  on_failure.sh
fixtures/  (5 files)
  debug.html
  page.browserify.html
  page.html
  page.minified.html
  page.module.html
src/  (1 files)
  confetti.js
test/  (3 files)
  .eslintrc.yml
  index.test.js
  ssr.test.js
.brackets.json
.editorconfig
.eslintrc.yml
.gitattributes
.gitignore
.npmignore
LICENSE
README.md
index.html
package.json
```

## Entry points

- [src/confetti.js](https://github.com/catdad/canvas-confetti/blob/20eebad51dde793070c373d594099a7ed8d96e22/src/confetti.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bin package | library | Observed | Groups 1 file(s) under bin package (observed from repository paths and static analysis). |
| confetti.js package | library | Observed | Groups 1 file(s) under confetti.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 3 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.brackets.json` (config)
- `.editorconfig` (config)
- `.eslintrc.yml` (config)
- `.github/funding.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `package.json` (manifest)

## Top-level layout

- `(root files)` — 10 analysed file(s)
- `fixtures` — 5 analysed file(s)
- `test` — 3 analysed file(s)
- `.github` — 2 analysed file(s)
- `bin` — 1 analysed file(s)
- `src` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 4 file(s) were skipped during inventory (1 x likely secret file excluded; 3 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `20eebad51dde793070c373d594099a7ed8d96e22` is the revision these paths and observations refer to.
