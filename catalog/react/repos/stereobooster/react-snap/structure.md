# Project structure: stereobooster/react-snap

**Analysed commit:** `e2746ebe63cc75a4943d076585fff5aa5b50751d`

**Commit reference:** [e2746ebe63cc75a4943d076585fff5aa5b50751d](https://github.com/stereobooster/react-snap/commit/e2746ebe63cc75a4943d076585fff5aa5b50751d)

**Tree at this commit:** [stereobooster/react-snap@e2746ebe63cc](https://github.com/stereobooster/react-snap/tree/e2746ebe63cc75a4943d076585fff5aa5b50751d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | stereobooster/react-snap |
| Description | 👻 Zero-configuration framework-agnostic static prerendering for SPAs |
| Stars | 5123 |
| Forks | 394 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `e2746ebe63cc75a4943d076585fff5aa5b50751d` |
| Retrieved at | 2026-11-14T19:14:27.937395+00:00 |
| Files in this snapshot | 57 |

## Directory tree

```text
.github/  (5 files)
  ISSUE_TEMPLATE/  (3 files)
    Bug_report.md
    Feature_request.md
    Support_question.md
  PULL_REQUEST_TEMPLATE.md
  renovate.json
doc/  (7 files)
  alternatives.md
  an-almost-static-stack-optimization.md
  anatomy-of-js-static-website-generator.md
  behind-the-scenes.md
  emotion-site-optimization.md
  load-performance-optimizations.md
  recipes.md
src/  (2 files)
  puppeteer_utils.js
  tracker.js
tests/  (34 files)
  __snapshots__/  (1 files)
    defaultOptions.test.js.snap
  examples/  (30 files)
    cra/  (3 files)
      … 3 files under this directory
    many-pages/  (1 files)
      … 1 files under this directory
    one-page/  (1 files)
      … 1 files under this directory
    other/  (22 files)
      … 22 files under this directory
    partial/  (2 files)
      … 2 files under this directory
    processed/  (1 files)
      … 1 files under this directory
  defaultOptions.test.js
  helper.js
  run.test.js
.gitignore
.node-version
.travis.yml
CHANGELOG.md
LICENSE
Readme.md
index.js
package.json
run.js
```

## Entry points

- [index.js](https://github.com/stereobooster/react-snap/blob/e2746ebe63cc75a4943d076585fff5aa5b50751d/index.js)
- [run.js](https://github.com/stereobooster/react-snap/blob/e2746ebe63cc75a4943d076585fff5aa5b50751d/run.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| puppeteer_utils.js package | library | Observed | Groups 1 file(s) under puppeteer_utils.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 34 file(s) under tests (observed from repository paths and static analysis). |
| tracker.js package | library | Observed | Groups 1 file(s) under tracker.js package (observed from repository paths and static analysis). |

## Important files

- `.github/renovate.json` (config)
- `.travis.yml` (ci)
- `package.json` (manifest)

## Top-level layout

- `tests` — 34 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `doc` — 7 analysed file(s)
- `.github` — 5 analysed file(s)
- `src` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `e2746ebe63cc75a4943d076585fff5aa5b50751d` is the revision these paths and observations refer to.
