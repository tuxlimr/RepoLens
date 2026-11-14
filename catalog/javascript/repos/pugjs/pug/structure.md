# Project structure: pugjs/pug

**Analysed commit:** `c323ed3e630b931bc04790efb509d34ac5927040`

**Commit reference:** [c323ed3e630b931bc04790efb509d34ac5927040](https://github.com/pugjs/pug/commit/c323ed3e630b931bc04790efb509d34ac5927040)

**Tree at this commit:** [pugjs/pug@c323ed3e630b](https://github.com/pugjs/pug/tree/c323ed3e630b931bc04790efb509d34ac5927040)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | pugjs/pug |
| Description | Pug – robust, elegant, feature rich template engine for Node.js |
| Stars | 21818 |
| Forks | 1932 |
| Licence | Not detected |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `c323ed3e630b931bc04790efb509d34ac5927040` |
| Retrieved at | 2026-11-14T19:11:10.546771+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.github/  (4 files)
  workflows/  (2 files)
    rollingversions.yml
    test.yml
  FUNDING.yml
  ISSUE_TEMPLATE.md
packages/  (789 files)
  pug/  (315 files)
    examples/  (34 files)
      … 34 files under this directory
    lib/  (1 files)
      … 1 files under this directory
    support/  (1 files)
      … 1 files under this directory
    test/  (274 files)
      … 274 files under this directory
    History.md
    LICENSE
    README.md
    package.json
    register.js
  pug-attrs/  (5 files)
    test/  (1 files)
      … 1 files under this directory
    LICENSE
    README.md
    index.js
    package.json
  pug-code-gen/  (5 files)
    HISTORY.md
    LICENSE
    README.md
    index.js
    package.json
  pug-error/  (6 files)
    src/  (1 files)
      … 1 files under this directory
    test/  (1 files)
      … 1 files under this directory
    LICENSE
    README.md
    package.json
    tsconfig.json
  pug-filters/  (30 files)
    lib/  (2 files)
      … 2 files under this directory
    test/  (23 files)
      … 23 files under this directory
    CHANGELOG.md
    LICENSE
    README.md
    index.js
    package.json
  pug-lexer/  (153 files)
    test/  (147 files)
      … 147 files under this directory
    History.md
    LICENSE
    README.md
    index.d.ts
    index.js
    package.json
  pug-linker/  (105 files)
    test/  (100 files)
      … 100 files under this directory
    HISTORY.md
    LICENSE
    README.md
    index.js
    package.json
  pug-load/  (11 files)
    test/  (6 files)
      … 6 files under this directory
    HISTORY.md
    LICENSE
    README.md
    index.js
    package.json
  pug-parser/  (127 files)
    lib/  (1 files)
      … 1 files under this directory
    test/  (121 files)
      … 121 files under this directory
    HISTORY.md
    LICENSE
    README.md
    index.js
    package.json
  pug-runtime/  (10 files)
    test/  (1 files)
      … 1 files under this directory
    .gitignore
    CHANGELOG.md
    LICENSE
    README.md
    build.js
    index.js
    package.json
    prepublish.js
    wrap.js
  pug-strip-comments/  (14 files)
    test/  (8 files)
      … 8 files under this directory
    CHANGELOG.md
    LICENSE
    LICENSE.md
    README.md
    index.js
    package.json
  pug-walk/  (8 files)
    test/  (1 files)
      … 1 files under this directory
    .gitignore
    .travis.yml
    HISTORY.md
    LICENSE
    README.md
    index.js
    package.json
.editorconfig
.gitattributes
.gitignore
.prettierrc.js
README.md
SECURITY.md
package.json
```

## Entry points

- [packages/pug-attrs/index.js](https://github.com/pugjs/pug/blob/c323ed3e630b931bc04790efb509d34ac5927040/packages/pug-attrs/index.js)
- [packages/pug-code-gen/index.js](https://github.com/pugjs/pug/blob/c323ed3e630b931bc04790efb509d34ac5927040/packages/pug-code-gen/index.js)
- [packages/pug-error/src/index.ts](https://github.com/pugjs/pug/blob/c323ed3e630b931bc04790efb509d34ac5927040/packages/pug-error/src/index.ts)
- [packages/pug-filters/index.js](https://github.com/pugjs/pug/blob/c323ed3e630b931bc04790efb509d34ac5927040/packages/pug-filters/index.js)
- [packages/pug-lexer/index.js](https://github.com/pugjs/pug/blob/c323ed3e630b931bc04790efb509d34ac5927040/packages/pug-lexer/index.js)
- [packages/pug-linker/index.js](https://github.com/pugjs/pug/blob/c323ed3e630b931bc04790efb509d34ac5927040/packages/pug-linker/index.js)
- [packages/pug-load/index.js](https://github.com/pugjs/pug/blob/c323ed3e630b931bc04790efb509d34ac5927040/packages/pug-load/index.js)
- [packages/pug-parser/index.js](https://github.com/pugjs/pug/blob/c323ed3e630b931bc04790efb509d34ac5927040/packages/pug-parser/index.js)
- [packages/pug-runtime/index.js](https://github.com/pugjs/pug/blob/c323ed3e630b931bc04790efb509d34ac5927040/packages/pug-runtime/index.js)
- [packages/pug-strip-comments/index.js](https://github.com/pugjs/pug/blob/c323ed3e630b931bc04790efb509d34ac5927040/packages/pug-strip-comments/index.js)
- [packages/pug-walk/index.js](https://github.com/pugjs/pug/blob/c323ed3e630b931bc04790efb509d34ac5927040/packages/pug-walk/index.js)
- [packages/pug/lib/index.js](https://github.com/pugjs/pug/blob/c323ed3e630b931bc04790efb509d34ac5927040/packages/pug/lib/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 15 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 34 file(s) under packages package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 683 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/workflows/rollingversions.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `package.json` (manifest)
- `packages/pug-attrs/package.json` (manifest)
- `packages/pug-code-gen/package.json` (manifest)
- `packages/pug-error/package.json` (manifest)
- `packages/pug-error/tsconfig.json` (config)
- `packages/pug-filters/package.json` (manifest)
- `packages/pug-lexer/package.json` (manifest)
- `packages/pug-linker/package.json` (manifest)
- `packages/pug-load/package.json` (manifest)
- `packages/pug-parser/package.json` (manifest)
- `packages/pug-runtime/package.json` (manifest)
- `packages/pug-strip-comments/package.json` (manifest)
- `packages/pug-walk/.travis.yml` (ci)
- `packages/pug-walk/package.json` (manifest)
- `packages/pug/package.json` (manifest)

## Top-level layout

- `packages` — 789 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `.github` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `c323ed3e630b931bc04790efb509d34ac5927040` is the revision these paths and observations refer to.
