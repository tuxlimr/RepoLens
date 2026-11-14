# Project structure: basecamp/trix

**Analysed commit:** `e2df97a56bcf1b6689ccd08d0d11a3f96006da8b`

**Commit reference:** [e2df97a56bcf1b6689ccd08d0d11a3f96006da8b](https://github.com/basecamp/trix/commit/e2df97a56bcf1b6689ccd08d0d11a3f96006da8b)

**Tree at this commit:** [basecamp/trix@e2df97a56bcf](https://github.com/basecamp/trix/tree/e2df97a56bcf1b6689ccd08d0d11a3f96006da8b)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | basecamp/trix |
| Description | A rich text editor for everyday writing |
| Stars | 20017 |
| Forks | 1134 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `e2df97a56bcf1b6689ccd08d0d11a3f96006da8b` |
| Retrieved at | 2026-11-14T19:11:15.859705+00:00 |
| Files in this snapshot | 306 |

## Directory tree

```text
.github/  (4 files)
  workflows/  (1 files)
    ci.yml
  ISSUE_TEMPLATE.md
  dependabot.yml
  stale.yml
action_text-trix/  (73 files)
  app/  (2 files)
    assets/  (2 files)
      … 2 files under this directory
  bin/  (1 files)
    rails
  lib/  (3 files)
    action_text/  (3 files)
      … 3 files under this directory
  test/  (61 files)
    dummy/  (57 files)
      … 57 files under this directory
    fixtures/  (1 files)
      … 1 files under this directory
    system/  (1 files)
      … 1 files under this directory
    application_system_test_case.rb
    test_helper.rb
  .gitignore
  Gemfile
  LICENSE
  README.md
  Rakefile
  action_text-trix.gemspec
assets/  (27 files)
  trix/  (24 files)
    images/  (17 files)
      … 17 files under this directory
    stylesheets/  (7 files)
      … 7 files under this directory
  index.html
  test.html
  trix.scss
bin/  (3 files)
  ci
  sass-build
  setup
src/  (188 files)
  inspector/  (28 files)
    templates/  (6 files)
      … 6 files under this directory
    views/  (6 files)
      … 6 files under this directory
    watchdog/  (8 files)
      … 8 files under this directory
    control_element.js
    debugger.js
    element.js
    global.js
    inspector.js
    templates.js
    view.js
    watchdog.js
  test/  (66 files)
    system/  (22 files)
      … 22 files under this directory
    test_helpers/  (23 files)
      … 23 files under this directory
    unit/  (17 files)
      … 17 files under this directory
    system.js
    test.js
    test_helper.js
    unit.js
  trix/  (94 files)
    config/  (14 files)
      … 14 files under this directory
    controllers/  (9 files)
      … 9 files under this directory
    core/  (28 files)
      … 28 files under this directory
    elements/  (3 files)
      … 3 files under this directory
    filters/  (3 files)
      … 3 files under this directory
    models/  (21 files)
      … 21 files under this directory
    observers/  (3 files)
      … 3 files under this directory
    operations/  (3 files)
      … 3 files under this directory
    views/  (8 files)
      … 8 files under this directory
    constants.js
    trix.js
.eslintrc
.gitignore
.node-version
.npmignore
CODE_OF_CONDUCT.md
LICENSE
README.md
babel.config.json
package.json
rollup.config.js
web-test-runner.config.mjs
```

## Entry points

- [src/trix/config/index.js](https://github.com/basecamp/trix/blob/e2df97a56bcf1b6689ccd08d0d11a3f96006da8b/src/trix/config/index.js)
- [src/trix/controllers/index.js](https://github.com/basecamp/trix/blob/e2df97a56bcf1b6689ccd08d0d11a3f96006da8b/src/trix/controllers/index.js)
- [src/trix/core/index.js](https://github.com/basecamp/trix/blob/e2df97a56bcf1b6689ccd08d0d11a3f96006da8b/src/trix/core/index.js)
- [src/trix/elements/index.js](https://github.com/basecamp/trix/blob/e2df97a56bcf1b6689ccd08d0d11a3f96006da8b/src/trix/elements/index.js)
- [src/trix/filters/index.js](https://github.com/basecamp/trix/blob/e2df97a56bcf1b6689ccd08d0d11a3f96006da8b/src/trix/filters/index.js)
- [src/trix/models/index.js](https://github.com/basecamp/trix/blob/e2df97a56bcf1b6689ccd08d0d11a3f96006da8b/src/trix/models/index.js)
- [src/trix/observers/index.js](https://github.com/basecamp/trix/blob/e2df97a56bcf1b6689ccd08d0d11a3f96006da8b/src/trix/observers/index.js)
- [src/trix/operations/index.js](https://github.com/basecamp/trix/blob/e2df97a56bcf1b6689ccd08d0d11a3f96006da8b/src/trix/operations/index.js)
- [src/trix/views/index.js](https://github.com/basecamp/trix/blob/e2df97a56bcf1b6689ccd08d0d11a3f96006da8b/src/trix/views/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| action_text-trix package | library | Observed | Groups 3 file(s) under action_text-trix package (observed from repository paths and static analysis). |
| API layer | api | Observed | Groups 23 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 16 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 21 file(s) under data layer (observed from repository paths and static analysis). |
| inspector package | library | Observed | Groups 22 file(s) under inspector package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 28 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 127 file(s) under tests (observed from repository paths and static analysis). |
| trix package | library | Observed | Groups 14 file(s) under trix package (observed from repository paths and static analysis). |

## Important files

- `.github/dependabot.yml` (config)
- `.github/stale.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `babel.config.json` (config)
- `package.json` (manifest)

## Top-level layout

- `src` — 188 analysed file(s)
- `action_text-trix` — 73 analysed file(s)
- `assets` — 27 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `.github` — 4 analysed file(s)
- `bin` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `e2df97a56bcf1b6689ccd08d0d11a3f96006da8b` is the revision these paths and observations refer to.
