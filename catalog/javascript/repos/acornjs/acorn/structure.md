# Project structure: acornjs/acorn

**Analysed commit:** `e4516ce0f49aea06b98ae1a551644119958ed4e1`

**Commit reference:** [e4516ce0f49aea06b98ae1a551644119958ed4e1](https://github.com/acornjs/acorn/commit/e4516ce0f49aea06b98ae1a551644119958ed4e1)

**Tree at this commit:** [acornjs/acorn@e4516ce0f49a](https://github.com/acornjs/acorn/tree/e4516ce0f49aea06b98ae1a551644119958ed4e1)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | acornjs/acorn |
| Description | A small, fast, JavaScript-based JavaScript parser |
| Stars | 11474 |
| Forks | 1063 |
| Licence | Not detected |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `e4516ce0f49aea06b98ae1a551644119958ed4e1` |
| Retrieved at | 2026-11-14T19:12:18.166722+00:00 |
| Files in this snapshot | 117 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    ci.yml
acorn/  (35 files)
  bin/  (1 files)
    acorn
  src/  (28 files)
    bin/  (1 files)
      … 1 files under this directory
    generated/  (5 files)
      … 5 files under this directory
    acorn.d.ts
    expression.js
    identifier.js
    index.js
    location.js
    locutil.js
    lval.js
    node.js
    options.js
    package.json
    parseutil.js
    regexp.js
    scope.js
    scopeflags.js
    state.js
    statement.js
    tokencontext.js
    tokenize.js
    tokentype.js
    unicode-property-data.js
    util.js
    whitespace.js
  .npmignore
  CHANGELOG.md
  LICENSE
  README.md
  package.json
  rollup.config.mjs
acorn-loose/  (14 files)
  src/  (8 files)
    acorn-loose.d.ts
    expression.js
    index.js
    package.json
    parseutil.js
    state.js
    statement.js
    tokenize.js
  .npmignore
  CHANGELOG.md
  LICENSE
  README.md
  package.json
  rollup.config.mjs
acorn-walk/  (9 files)
  src/  (3 files)
    index.js
    package.json
    walk.d.ts
  .npmignore
  CHANGELOG.md
  LICENSE
  README.md
  package.json
  rollup.config.mjs
bin/  (6 files)
  generate-identifier-regex.js
  generate-unicode-script-values.js
  run_test262.js
  test262.unsupported-features
  test262.whitelist
  update_authors.sh
test/  (39 files)
  bench/  (7 files)
    fixtures/  (2 files)
      … 2 files under this directory
    common.js
    index.html
    index.js
    package.json
    worker.js
  driver.js
  run.js
  tests-async-iteration.js
  tests-asyncawait.js
  tests-await-top-level.js
  tests-bigint.js
  tests-class-features-2022.js
  tests-commonjs.js
  tests-directive.js
  tests-dynamic-import.js
  tests-es7.js
  tests-export-all-as-ns-from-source.js
  tests-export-named.js
  tests-import-attributes.js
  tests-import-meta.js
  tests-json-superset.js
  tests-logical-assignment-operators.js
  tests-module-string-names.js
  tests-nullish-coalescing.js
  tests-numeric-separators.js
  tests-optional-catch-binding.js
  tests-optional-chaining.js
  tests-regexp-2018.js
  tests-regexp-2020.js
  … 8 more files
.editorconfig
.gitattributes
.gitignore
.mailmap
.npmignore
.nvmrc
.tern-project
AUTHORS
CONTRIBUTING.md
README.md
eslint.config.mjs
logo.svg
package.json
```

## Entry points

- [acorn/bin/acorn](https://github.com/acornjs/acorn/blob/e4516ce0f49aea06b98ae1a551644119958ed4e1/acorn/bin/acorn)
- [acorn-loose/src/index.js](https://github.com/acornjs/acorn/blob/e4516ce0f49aea06b98ae1a551644119958ed4e1/acorn-loose/src/index.js)
- [acorn-walk/src/index.js](https://github.com/acornjs/acorn/blob/e4516ce0f49aea06b98ae1a551644119958ed4e1/acorn-walk/src/index.js)
- [acorn/src/index.js](https://github.com/acornjs/acorn/blob/e4516ce0f49aea06b98ae1a551644119958ed4e1/acorn/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| acorn package | library | Observed | Groups 28 file(s) under acorn package (observed from repository paths and static analysis). |
| acorn-loose package | library | Observed | Groups 8 file(s) under acorn-loose package (observed from repository paths and static analysis). |
| acorn-walk package | library | Observed | Groups 3 file(s) under acorn-walk package (observed from repository paths and static analysis). |
| bin package | library | Observed | Groups 4 file(s) under bin package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 39 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/workflows/ci.yml` (ci)
- `acorn-loose/package.json` (manifest)
- `acorn-loose/src/package.json` (manifest)
- `acorn-walk/package.json` (manifest)
- `acorn-walk/src/package.json` (manifest)
- `acorn/package.json` (manifest)
- `acorn/src/package.json` (manifest)
- `package.json` (manifest)

## Top-level layout

- `test` — 39 analysed file(s)
- `acorn` — 35 analysed file(s)
- `acorn-loose` — 14 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `acorn-walk` — 9 analysed file(s)
- `bin` — 6 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `e4516ce0f49aea06b98ae1a551644119958ed4e1` is the revision these paths and observations refer to.
