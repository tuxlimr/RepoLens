# Project structure: lodash/lodash

**Analysed commit:** `2b5e6f7399a7b48005140b5d5c6bc6c0e62919a8`

**Commit reference:** [2b5e6f7399a7b48005140b5d5c6bc6c0e62919a8](https://github.com/lodash/lodash/commit/2b5e6f7399a7b48005140b5d5c6bc6c0e62919a8)

**Tree at this commit:** [lodash/lodash@2b5e6f7399a7](https://github.com/lodash/lodash/tree/2b5e6f7399a7b48005140b5d5c6bc6c0e62919a8)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | lodash/lodash |
| Description | A modern JavaScript utility library delivering modularity, performance, & extras. |
| Stars | 61355 |
| Forks | 7269 |
| Licence | Other |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `2b5e6f7399a7b48005140b5d5c6bc6c0e62919a8` |
| Retrieved at | 2026-11-14T19:10:35.863218+00:00 |
| Files in this snapshot | 61 |

## Directory tree

```text
.github/  (9 files)
  workflows/  (8 files)
    browser-testing.yml
    ci-bun.yml
    ci-dist-sync.yml
    ci-docs.yml
    ci-node.yml
    codeql.yml
    renovate.yml
    scorecards.yml
  CONTRIBUTING.md
fp/  (4 files)
  _baseConvert.js
  _convertBrowser.js
  _mapping.js
  placeholder.js
lib/  (21 files)
  common/  (5 files)
    file.js
    mapping.js
    minify.js
    uglify.options.js
    util.js
  fp/  (12 files)
    template/  (9 files)
      … 9 files under this directory
    build-dist.js
    build-doc.js
    build-modules.js
  main/  (4 files)
    build-dist.js
    build-doc.js
    build-modules.js
    build-site.js
perf/  (3 files)
  asset/  (1 files)
    perf-ui.js
  index.html
  perf.js
test/  (9 files)
  asset/  (2 files)
    test-ui.js
    worker.js
  backbone.html
  fp.html
  index.html
  playwright-runner.spec.js
  remove.js
  test-fp.js
  underscore.html
.editorconfig
.gitattributes
.gitignore
.jscsrc
.markdown-doctest-setup.js
CHANGELOG
GOVERNANCE.md
LICENSE
README.md
SECURITY.md
incident_response_plan.md
package.json
playwright.config.js
renovate.json
threat-model.md
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| fp package | library | Observed | Groups 4 file(s) under fp package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 12 file(s) under lib package (observed from repository paths and static analysis). |
| perf package | library | Observed | Groups 2 file(s) under perf package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 9 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/workflows/browser-testing.yml` (ci)
- `.github/workflows/ci-bun.yml` (ci)
- `.github/workflows/ci-dist-sync.yml` (ci)
- `.github/workflows/ci-docs.yml` (ci)
- `.github/workflows/ci-node.yml` (ci)
- `.github/workflows/codeql.yml` (ci)
- `.github/workflows/renovate.yml` (ci)
- `.github/workflows/scorecards.yml` (ci)
- `package.json` (manifest)
- `renovate.json` (config)

## Top-level layout

- `lib` — 21 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `.github` — 9 analysed file(s)
- `test` — 9 analysed file(s)
- `fp` — 4 analysed file(s)
- `perf` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 33 file(s) were skipped during inventory (33 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `2b5e6f7399a7b48005140b5d5c6bc6c0e62919a8` is the revision these paths and observations refer to.
