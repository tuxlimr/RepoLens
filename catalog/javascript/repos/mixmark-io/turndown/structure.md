# Project structure: mixmark-io/turndown

**Analysed commit:** `b86e2b18539fa4922acf7001902255e2ce5bf0b9`

**Commit reference:** [b86e2b18539fa4922acf7001902255e2ce5bf0b9](https://github.com/mixmark-io/turndown/commit/b86e2b18539fa4922acf7001902255e2ce5bf0b9)

**Tree at this commit:** [mixmark-io/turndown@b86e2b18539f](https://github.com/mixmark-io/turndown/tree/b86e2b18539fa4922acf7001902255e2ce5bf0b9)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | mixmark-io/turndown |
| Description | 🛏 An HTML to Markdown converter written in JavaScript |
| Stars | 11511 |
| Forks | 1002 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `b86e2b18539fa4922acf7001902255e2ce5bf0b9` |
| Retrieved at | 2026-11-14T19:12:17.417710+00:00 |
| Files in this snapshot | 30 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    test.yml
bench/  (2 files)
  cases.js
  index.js
config/  (9 files)
  rollup.config.browser.cjs.mjs
  rollup.config.browser.es.mjs
  rollup.config.browser.umd.mjs
  rollup.config.cjs.mjs
  rollup.config.es.mjs
  rollup.config.iife.mjs
  rollup.config.mjs
  rollup.config.test.mjs
  rollup.config.umd.mjs
src/  (8 files)
  collapse-whitespace.js
  commonmark-rules.js
  html-parser.js
  node.js
  root-node.js
  rules.js
  turndown.js
  utilities.js
test/  (3 files)
  index.html
  internals-test.js
  turndown-test.js
.gitignore
.tm_properties
LICENSE
README.md
SECURITY.md
index.html
package.json
```

## Entry points

- [bench/index.js](https://github.com/mixmark-io/turndown/blob/b86e2b18539fa4922acf7001902255e2ce5bf0b9/bench/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bench package | library | Observed | Groups 2 file(s) under bench package (observed from repository paths and static analysis). |
| collapse-whitespace.js package | library | Observed | Groups 1 file(s) under collapse-whitespace.js package (observed from repository paths and static analysis). |
| commonmark-rules.js package | library | Observed | Groups 1 file(s) under commonmark-rules.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 10 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| html-parser.js package | library | Observed | Groups 1 file(s) under html-parser.js package (observed from repository paths and static analysis). |
| node.js package | library | Observed | Groups 1 file(s) under node.js package (observed from repository paths and static analysis). |
| root-node.js package | library | Observed | Groups 1 file(s) under root-node.js package (observed from repository paths and static analysis). |
| rules.js package | library | Observed | Groups 1 file(s) under rules.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 3 file(s) under tests (observed from repository paths and static analysis). |
| turndown.js package | library | Observed | Groups 1 file(s) under turndown.js package (observed from repository paths and static analysis). |
| utilities.js package | library | Observed | Groups 1 file(s) under utilities.js package (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/test.yml` (ci)
- `package.json` (manifest)

## Top-level layout

- `config` — 9 analysed file(s)
- `src` — 8 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `test` — 3 analysed file(s)
- `bench` — 2 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `b86e2b18539fa4922acf7001902255e2ce5bf0b9` is the revision these paths and observations refer to.
