# Project structure: snapappointments/bootstrap-select

**Analysed commit:** `939e94b14a34759e193f616b753e0a33081cc0c5`

**Commit reference:** [939e94b14a34759e193f616b753e0a33081cc0c5](https://github.com/snapappointments/bootstrap-select/commit/939e94b14a34759e193f616b753e0a33081cc0c5)

**Tree at this commit:** [snapappointments/bootstrap-select@939e94b14a34](https://github.com/snapappointments/bootstrap-select/tree/939e94b14a34759e193f616b753e0a33081cc0c5)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | snapappointments/bootstrap-select |
| Description | :rocket: The jQuery plugin that brings select elements into the 21st century with intuitive multiselection, searching, and much more. |
| Stars | 9807 |
| Forks | 2652 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `939e94b14a34759e193f616b753e0a33081cc0c5` |
| Retrieved at | 2026-11-14T19:12:52.630061+00:00 |
| Files in this snapshot | 95 |

## Directory tree

```text
.github/  (8 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (3 files)
    cypress.yml
    linting.yml
    publishing.yml
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
  move.yml
cypress/  (5 files)
  integration/  (2 files)
    basic.spec.js
    max-options.spec.js
  plugins/  (1 files)
    index.js
  support/  (2 files)
    commands.js
    index.js
docs/  (16 files)
  custom_theme/  (6 files)
    ajax/  (1 files)
      … 1 files under this directory
    css/  (1 files)
      … 1 files under this directory
    js/  (1 files)
      … 1 files under this directory
    main.html
    nav.html
    toc.html
  docs/  (9 files)
    css/  (1 files)
      … 1 files under this directory
    playground/  (4 files)
      … 4 files under this directory
    examples.md
    index.md
    methods.md
    options.md
  mkdocs.yml
js/  (45 files)
  i18n/  (41 files)
    defaults-am_ET.js
    defaults-ar_AR.js
    defaults-bg_BG.js
    defaults-cs_CZ.js
    defaults-da_DK.js
    defaults-de_DE.js
    defaults-en_US.js
    defaults-es_CL.js
    defaults-es_ES.js
    defaults-et_EE.js
    defaults-eu.js
    defaults-fa_IR.js
    defaults-fi_FI.js
    defaults-fr_FR.js
    defaults-hr_HR.js
    defaults-hu_HU.js
    defaults-id_ID.js
    defaults-it_IT.js
    defaults-ja_JP.js
    defaults-kh_KM.js
    defaults-ko_KR.js
    defaults-lt_LT.js
    defaults-lv_LV.js
    defaults-nb_NO.js
    … 17 more files
  .eslintrc.json
  bootstrap-select.js
  umd-intro.js
  umd-outro.js
less/  (2 files)
  bootstrap-select.less
  variables.less
nuget/  (2 files)
  MyGet.ps1
  bootstrap-select.nuspec
sass/  (2 files)
  bootstrap-select.scss
  variables.scss
tests/  (4 files)
  bootstrap4.html
  bootstrap5.html
  index.html
  main.js
.eslintignore
.gitignore
CHANGELOG.md
CONTRIBUTING.md
Gruntfile.js
LICENSE
README.md
bower.json
composer.json
cypress.json
package.json
```

## Entry points

- [cypress/plugins/index.js](https://github.com/snapappointments/bootstrap-select/blob/939e94b14a34759e193f616b753e0a33081cc0c5/cypress/plugins/index.js)
- [cypress/support/index.js](https://github.com/snapappointments/bootstrap-select/blob/939e94b14a34759e193f616b753e0a33081cc0c5/cypress/support/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| cypress package | library | Observed | Groups 3 file(s) under cypress package (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 2 file(s) under external integrations (observed from repository paths and static analysis). |
| js package | library | Observed | Groups 44 file(s) under js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 4 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/move.yml` (config)
- `.github/workflows/cypress.yml` (ci)
- `.github/workflows/linting.yml` (ci)
- `.github/workflows/publishing.yml` (ci)
- `bower.json` (config)
- `composer.json` (config)
- `cypress.json` (config)
- `docs/mkdocs.yml` (config)
- `js/.eslintrc.json` (config)
- `package.json` (manifest)

## Top-level layout

- `js` — 45 analysed file(s)
- `docs` — 16 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `.github` — 8 analysed file(s)
- `cypress` — 5 analysed file(s)
- `tests` — 4 analysed file(s)
- `less` — 2 analysed file(s)
- `nuget` — 2 analysed file(s)
- `sass` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 44 file(s) were skipped during inventory (1 x generated/minified file excluded; 43 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `939e94b14a34759e193f616b753e0a33081cc0c5` is the revision these paths and observations refer to.
