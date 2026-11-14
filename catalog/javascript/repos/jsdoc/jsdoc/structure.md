# Project structure: jsdoc/jsdoc

**Analysed commit:** `536d8502494e4ee6722627ce88996f87cb4544d6`

**Commit reference:** [536d8502494e4ee6722627ce88996f87cb4544d6](https://github.com/jsdoc/jsdoc/commit/536d8502494e4ee6722627ce88996f87cb4544d6)

**Tree at this commit:** [jsdoc/jsdoc@536d8502494e](https://github.com/jsdoc/jsdoc/tree/536d8502494e4ee6722627ce88996f87cb4544d6)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | jsdoc/jsdoc |
| Description | An API documentation generator for JavaScript. |
| Stars | 15473 |
| Forks | 1489 |
| Licence | Apache-2.0 |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `536d8502494e4ee6722627ce88996f87cb4544d6` |
| Retrieved at | 2026-11-14T19:11:38.466189+00:00 |
| Files in this snapshot | 653 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (1 files)
    ci.yaml
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
.husky/  (2 files)
  install.js
  pre-commit
packages/  (630 files)
  jsdoc/  (385 files)
    test/  (378 files)
      … 378 files under this directory
    .eslintignore
    .npmignore
    LICENSE
    README.md
    conf.json.EXAMPLE
    jsdoc.js
    package.json
  jsdoc-ast/  (14 files)
    lib/  (4 files)
      … 4 files under this directory
    test/  (5 files)
      … 5 files under this directory
    .npmignore
    LICENSE
    README.md
    index.js
    package.json
  jsdoc-cli/  (16 files)
    lib/  (4 files)
      … 4 files under this directory
    test/  (7 files)
      … 7 files under this directory
    .npmignore
    LICENSE
    README.md
    index.js
    package.json
  jsdoc-core/  (28 files)
    lib/  (4 files)
      … 4 files under this directory
    test/  (19 files)
      … 19 files under this directory
    .npmignore
    LICENSE
    README.md
    index.js
    package.json
  jsdoc-doclet/  (18 files)
    lib/  (6 files)
      … 6 files under this directory
    test/  (7 files)
      … 7 files under this directory
    .npmignore
    LICENSE
    README.md
    index.js
    package.json
  jsdoc-eslint-config/  (5 files)
    .npmignore
    LICENSE
    README.md
    index.js
    package.json
  jsdoc-name/  (8 files)
    lib/  (1 files)
      … 1 files under this directory
    test/  (2 files)
      … 2 files under this directory
    .npmignore
    LICENSE
    README.md
    index.js
    package.json
  jsdoc-parse/  (14 files)
    lib/  (3 files)
      … 3 files under this directory
    test/  (6 files)
      … 6 files under this directory
    .npmignore
    LICENSE
    README.md
    index.js
    package.json
  jsdoc-plugins/  (25 files)
    test/  (11 files)
      … 11 files under this directory
    .npmignore
    LICENSE
    README.md
    comment-convert.js
    comments-only.js
    escape-html.js
    event-dumper.js
    overload-helper.js
    package.json
    partial.js
    rails-template.js
    source-tag.js
    summarize.js
    underscore.js
  jsdoc-prettier-config/  (5 files)
    .npmignore
    LICENSE
    README.md
    index.js
    package.json
  jsdoc-salty/  (8 files)
    lib/  (1 files)
      … 1 files under this directory
    test/  (2 files)
      … 2 files under this directory
    .npmignore
    LICENSE
    README.md
    index.js
    package.json
  jsdoc-tag/  (23 files)
    lib/  (11 files)
      … 11 files under this directory
    test/  (7 files)
      … 7 files under this directory
    .npmignore
    LICENSE
    README.md
    index.js
    package.json
  jsdoc-task-runner/  (11 files)
    lib/  (3 files)
      … 3 files under this directory
    test/  (3 files)
      … 3 files under this directory
    .npmignore
    LICENSE
    README.md
    index.js
    package.json
  jsdoc-template-legacy/  (28 files)
    lib/  (3 files)
      … 3 files under this directory
    plugins/  (1 files)
      … 1 files under this directory
    static/  (2 files)
      … 2 files under this directory
    test/  (1 files)
      … 1 files under this directory
    tmpl/  (16 files)
      … 16 files under this directory
    .npmignore
    LICENSE
    README.md
    package.json
    publish.js
  jsdoc-test-matchers/  (5 files)
    .npmignore
    LICENSE
    README.md
    index.js
    package.json
  jsdoc-util/  (10 files)
    lib/  (2 files)
      … 2 files under this directory
    test/  (3 files)
      … 3 files under this directory
    .npmignore
    LICENSE
    README.md
    index.js
    package.json
  jsdoc-web-assets/  (27 files)
    scripts/  (9 files)
      … 9 files under this directory
    static/  (2 files)
      … 2 files under this directory
    styles/  (15 files)
      … 15 files under this directory
    package.json
.editorconfig
.gitignore
.license-check.json
.license-header.txt
.licensee.json
.npmignore
.prettierignore
.prettierrc.cjs
.renovaterc.json
CHANGES.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
Herebyfile.js
LICENSE
README.md
eslint.config.js
lerna.json
package.json
```

## Entry points

- [packages/jsdoc-eslint-config/index.js](https://github.com/jsdoc/jsdoc/blob/536d8502494e4ee6722627ce88996f87cb4544d6/packages/jsdoc-eslint-config/index.js)
- [packages/jsdoc-parse/index.js](https://github.com/jsdoc/jsdoc/blob/536d8502494e4ee6722627ce88996f87cb4544d6/packages/jsdoc-parse/index.js)
- [packages/jsdoc-prettier-config/index.js](https://github.com/jsdoc/jsdoc/blob/536d8502494e4ee6722627ce88996f87cb4544d6/packages/jsdoc-prettier-config/index.js)
- [packages/jsdoc-template-legacy/publish.js](https://github.com/jsdoc/jsdoc/blob/536d8502494e4ee6722627ce88996f87cb4544d6/packages/jsdoc-template-legacy/publish.js)
- [packages/jsdoc/jsdoc.js](https://github.com/jsdoc/jsdoc/blob/536d8502494e4ee6722627ce88996f87cb4544d6/packages/jsdoc/jsdoc.js)
- [packages/jsdoc-ast/index.js](https://github.com/jsdoc/jsdoc/blob/536d8502494e4ee6722627ce88996f87cb4544d6/packages/jsdoc-ast/index.js)
- [packages/jsdoc-cli/index.js](https://github.com/jsdoc/jsdoc/blob/536d8502494e4ee6722627ce88996f87cb4544d6/packages/jsdoc-cli/index.js)
- [packages/jsdoc-core/index.js](https://github.com/jsdoc/jsdoc/blob/536d8502494e4ee6722627ce88996f87cb4544d6/packages/jsdoc-core/index.js)
- [packages/jsdoc-doclet/index.js](https://github.com/jsdoc/jsdoc/blob/536d8502494e4ee6722627ce88996f87cb4544d6/packages/jsdoc-doclet/index.js)
- [packages/jsdoc-name/index.js](https://github.com/jsdoc/jsdoc/blob/536d8502494e4ee6722627ce88996f87cb4544d6/packages/jsdoc-name/index.js)
- [packages/jsdoc-salty/index.js](https://github.com/jsdoc/jsdoc/blob/536d8502494e4ee6722627ce88996f87cb4544d6/packages/jsdoc-salty/index.js)
- [packages/jsdoc-tag/index.js](https://github.com/jsdoc/jsdoc/blob/536d8502494e4ee6722627ce88996f87cb4544d6/packages/jsdoc-tag/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 20 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 78 file(s) under packages package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 451 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/workflows/ci.yaml` (ci)
- `.license-check.json` (config)
- `.licensee.json` (config)
- `.renovaterc.json` (config)
- `lerna.json` (config)
- `package.json` (manifest)
- `packages/jsdoc-ast/package.json` (manifest)
- `packages/jsdoc-cli/package.json` (manifest)
- `packages/jsdoc-core/package.json` (manifest)
- `packages/jsdoc-doclet/package.json` (manifest)
- `packages/jsdoc-eslint-config/package.json` (manifest)
- `packages/jsdoc-name/package.json` (manifest)
- `packages/jsdoc-parse/package.json` (manifest)
- `packages/jsdoc-plugins/package.json` (manifest)
- `packages/jsdoc-prettier-config/package.json` (manifest)
- `packages/jsdoc-salty/package.json` (manifest)
- `packages/jsdoc-tag/package.json` (manifest)
- `packages/jsdoc-task-runner/package.json` (manifest)
- `packages/jsdoc-template-legacy/package.json` (manifest)
- `packages/jsdoc-test-matchers/package.json` (manifest)
- `packages/jsdoc-util/package.json` (manifest)
- `packages/jsdoc-web-assets/package.json` (manifest)
- `packages/jsdoc-web-assets/scripts/.babelrc.json` (config)
- `packages/jsdoc/package.json` (manifest)

## Top-level layout

- `packages` — 630 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `.github` — 3 analysed file(s)
- `.husky` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `536d8502494e4ee6722627ce88996f87cb4544d6` is the revision these paths and observations refer to.
