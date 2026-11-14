# Project structure: pure-css/pure

**Analysed commit:** `4e079fc499869dd8cb333c52a0bbfe5360514739`

**Commit reference:** [4e079fc499869dd8cb333c52a0bbfe5360514739](https://github.com/pure-css/pure/commit/4e079fc499869dd8cb333c52a0bbfe5360514739)

**Tree at this commit:** [pure-css/pure@4e079fc49986](https://github.com/pure-css/pure/tree/4e079fc499869dd8cb333c52a0bbfe5360514739)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | pure-css/pure |
| Description | A set of small, responsive CSS modules that you can use in every web project. |
| Stars | 23716 |
| Forks | 2399 |
| Licence | Other |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `4e079fc499869dd8cb333c52a0bbfe5360514739` |
| Retrieved at | 2026-11-14T19:11:04.370738+00:00 |
| Files in this snapshot | 113 |

## Directory tree

```text
.github/  (9 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (4 files)
    dependabot-automerge.yml
    deploy.yml
    publish.yml
    test.yml
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
  stale.yml
lib/  (1 files)
  grids.js
scripts/  (6 files)
  build.mjs
  lint-css.mjs
  prefix-selectors.mjs
  release.mjs
  util.mjs
  watch.mjs
site/  (53 files)
  components/  (6 files)
    CodeBlock.js
    Example.js
    Footer.js
    Header.js
    Menu.js
    SectionHeader.js
  lib/  (2 files)
    pure.js
    utils.js
  src/  (19 files)
    pages/  (17 files)
      … 17 files under this directory
    theme/  (1 files)
      … 1 files under this directory
    index.js
  static/  (20 files)
    css/  (1 files)
      … 1 files under this directory
    js/  (4 files)
      … 4 files under this directory
    layouts/  (14 files)
      … 14 files under this directory
    .nojekyll
  tests/  (1 files)
    render.spec.mjs
  .gitignore
  README.md
  docusaurus.config.js
  package.json
  playwright.config.mjs
src/  (18 files)
  base/  (1 files)
    css/  (1 files)
      … 1 files under this directory
  buttons/  (3 files)
    css/  (2 files)
      … 2 files under this directory
    tests/  (1 files)
      … 1 files under this directory
  forms/  (3 files)
    css/  (2 files)
      … 2 files under this directory
    tests/  (1 files)
      … 1 files under this directory
  grids/  (3 files)
    css/  (1 files)
      … 1 files under this directory
    tests/  (1 files)
      … 1 files under this directory
    README.md
  menus/  (6 files)
    css/  (5 files)
      … 5 files under this directory
    tests/  (1 files)
      … 1 files under this directory
  tables/  (2 files)
    css/  (1 files)
      … 1 files under this directory
    tests/  (1 files)
      … 1 files under this directory
test/  (12 files)
  fixtures/  (10 files)
    base-context.css
    base-input.css
    cases.json
    grids-12-custom-prefix-media.css
    grids-12-decimals-2.css
    grids-12-default-indent.css
    grids-12-old-ie.css
    grids-12-unreduced.css
    grids-responsive.css
    grids-units.css
  grids.mjs
  index.mjs
.csslintrc
.gitignore
.nvmrc
CODE_OF_CONDUCT.md
CONTRIBUTING.md
CREDITS.md
HISTORY.md
LICENSE
README.md
RELEASE.md
composer.json
eslint.config.mjs
index.js
package.json
```

## Entry points

- [index.js](https://github.com/pure-css/pure/blob/4e079fc499869dd8cb333c52a0bbfe5360514739/index.js)
- [site/src/index.js](https://github.com/pure-css/pure/blob/4e079fc499869dd8cb333c52a0bbfe5360514739/site/src/index.js)
- [site/src/pages/index.js](https://github.com/pure-css/pure/blob/4e079fc499869dd8cb333c52a0bbfe5360514739/site/src/pages/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 1 file(s) under lib package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 6 file(s) under scripts package (observed from repository paths and static analysis). |
| site package | library | Observed | Groups 28 file(s) under site package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 18 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/dependabot.yml` (config)
- `.github/stale.yml` (config)
- `.github/workflows/dependabot-automerge.yml` (ci)
- `.github/workflows/deploy.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `composer.json` (config)
- `package.json` (manifest)
- `site/package.json` (manifest)

## Top-level layout

- `site` — 53 analysed file(s)
- `src` — 18 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `test` — 12 analysed file(s)
- `.github` — 9 analysed file(s)
- `scripts` — 6 analysed file(s)
- `lib` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `4e079fc499869dd8cb333c52a0bbfe5360514739` is the revision these paths and observations refer to.
