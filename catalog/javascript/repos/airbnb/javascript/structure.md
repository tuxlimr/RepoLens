# Project structure: airbnb/javascript

**Analysed commit:** `8ed19247bef145e3cc41b24a02dd1fe6d9b5e681`

**Commit reference:** [8ed19247bef145e3cc41b24a02dd1fe6d9b5e681](https://github.com/airbnb/javascript/commit/8ed19247bef145e3cc41b24a02dd1fe6d9b5e681)

**Tree at this commit:** [airbnb/javascript@8ed19247bef1](https://github.com/airbnb/javascript/tree/8ed19247bef145e3cc41b24a02dd1fe6d9b5e681)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | airbnb/javascript |
| Description | JavaScript Style Guide |
| Stars | 148006 |
| Forks | 26512 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `8ed19247bef145e3cc41b24a02dd1fe6d9b5e681` |
| Retrieved at | 2026-11-14T19:10:31.581003+00:00 |
| Files in this snapshot | 58 |

## Directory tree

```text
.github/  (4 files)
  workflows/  (4 files)
    node-pretest.yml
    node.yml
    rebase.yml
    require-allow-edits.yml
css-in-javascript/  (1 files)
  README.md
linters/  (4 files)
  SublimeLinter/  (1 files)
    SublimeLinter.sublime-settings
  .eslintrc
  .jshintrc
  .markdownlint.json
packages/  (42 files)
  eslint-config-airbnb/  (20 files)
    rules/  (3 files)
      … 3 files under this directory
    test/  (4 files)
      … 4 files under this directory
    .babelrc
    .eslintrc
    CHANGELOG.md
    LICENSE.md
    README.md
    base.js
    hooks.js
    index.js
    legacy.js
    package.json
    whitespace-async.js
    whitespace.js
    whitespaceRules.js
  eslint-config-airbnb-base/  (22 files)
    rules/  (8 files)
      … 8 files under this directory
    test/  (3 files)
      … 3 files under this directory
    .babelrc
    .eslintrc
    CHANGELOG.md
    LICENSE.md
    README.md
    index.js
    legacy.js
    package.json
    whitespace-async.js
    whitespace.js
    whitespaceRules.js
react/  (1 files)
  README.md
.editorconfig
.gitignore
CODE_OF_CONDUCT.md
LICENSE.md
README.md
package.json
```

## Entry points

- [packages/eslint-config-airbnb-base/index.js](https://github.com/airbnb/javascript/blob/8ed19247bef145e3cc41b24a02dd1fe6d9b5e681/packages/eslint-config-airbnb-base/index.js)
- [packages/eslint-config-airbnb/index.js](https://github.com/airbnb/javascript/blob/8ed19247bef145e3cc41b24a02dd1fe6d9b5e681/packages/eslint-config-airbnb/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 23 file(s) under packages package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 7 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/workflows/node-pretest.yml` (ci)
- `.github/workflows/node.yml` (ci)
- `.github/workflows/rebase.yml` (ci)
- `.github/workflows/require-allow-edits.yml` (ci)
- `linters/.markdownlint.json` (config)
- `package.json` (manifest)
- `packages/eslint-config-airbnb-base/package.json` (manifest)
- `packages/eslint-config-airbnb/package.json` (manifest)

## Top-level layout

- `packages` — 42 analysed file(s)
- `(root files)` — 6 analysed file(s)
- `.github` — 4 analysed file(s)
- `linters` — 4 analysed file(s)
- `css-in-javascript` — 1 analysed file(s)
- `react` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `8ed19247bef145e3cc41b24a02dd1fe6d9b5e681` is the revision these paths and observations refer to.
