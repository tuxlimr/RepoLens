# Project structure: zenorocha/clipboard.js

**Analysed commit:** `899378dee9681dcf4cb3d702c23a3f3cd9f473d8`

**Commit reference:** [899378dee9681dcf4cb3d702c23a3f3cd9f473d8](https://github.com/zenorocha/clipboard.js/commit/899378dee9681dcf4cb3d702c23a3f3cd9f473d8)

**Tree at this commit:** [zenorocha/clipboard.js@899378dee968](https://github.com/zenorocha/clipboard.js/tree/899378dee9681dcf4cb3d702c23a3f3cd9f473d8)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | zenorocha/clipboard.js |
| Description | :scissors: Modern copy to clipboard. No Flash. Just 3kb gzipped :clipboard: |
| Stars | 34078 |
| Forks | 3894 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `899378dee9681dcf4cb3d702c23a3f3cd9f473d8` |
| Retrieved at | 2026-11-14T19:10:44.246876+00:00 |
| Files in this snapshot | 52 |

## Directory tree

```text
.github/  (7 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    documentation.md
    proposal.md
  workflows/  (2 files)
    publish.yml
    test.js.yml
  PULL_REQUEST_TEMPLATE.md
  stale.yml
.husky/  (2 files)
  .gitignore
  pre-commit
demo/  (12 files)
  constructor-node.html
  constructor-nodelist.html
  constructor-selector.html
  function-target.html
  function-text.html
  target-div.html
  target-input-number.html
  target-input.html
  target-programmatic-copy.html
  target-programmatic-cut.html
  target-textarea.html
  text-programmatic-copy.html
src/  (8 files)
  actions/  (3 files)
    copy.js
    cut.js
    default.js
  common/  (2 files)
    command.js
    create-fake-element.js
  clipboard.d.ts
  clipboard.js
  clipboard.test-d.ts
test/  (6 files)
  actions/  (3 files)
    copy.js
    cut.js
    default.js
  common/  (2 files)
    command.js
    create-fake-element.js
  clipboard.js
.babelrc.json
.editorconfig
.eslintignore
.eslintrc.json
.gitignore
.nvmrc
.prettierignore
.prettierrc.json
LICENSE
bower.json
composer.json
contributing.md
karma.conf.js
package.js
package.json
readme.md
webpack.config.js
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| actions package | library | Observed | Groups 3 file(s) under actions package (observed from repository paths and static analysis). |
| clipboard.d.ts package | library | Observed | Groups 1 file(s) under clipboard.d.ts package (observed from repository paths and static analysis). |
| clipboard.js package | library | Observed | Groups 1 file(s) under clipboard.js package (observed from repository paths and static analysis). |
| clipboard.test-d.ts package | library | Observed | Groups 1 file(s) under clipboard.test-d.ts package (observed from repository paths and static analysis). |
| common package | library | Observed | Groups 2 file(s) under common package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 6 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.babelrc.json` (config)
- `.editorconfig` (config)
- `.eslintrc.json` (config)
- `.github/stale.yml` (config)
- `.github/workflows/publish.yml` (ci)
- `.github/workflows/test.js.yml` (ci)
- `.prettierrc.json` (config)
- `bower.json` (config)
- `composer.json` (config)
- `package.json` (manifest)

## Top-level layout

- `(root files)` — 17 analysed file(s)
- `demo` — 12 analysed file(s)
- `src` — 8 analysed file(s)
- `.github` — 7 analysed file(s)
- `test` — 6 analysed file(s)
- `.husky` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `899378dee9681dcf4cb3d702c23a3f3cd9f473d8` is the revision these paths and observations refer to.
