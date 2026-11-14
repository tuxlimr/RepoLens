# Project structure: moment/moment

**Analysed commit:** `c2a703a4d84aa57ee2722ff8fb4a8016279fb3c4`

**Commit reference:** [c2a703a4d84aa57ee2722ff8fb4a8016279fb3c4](https://github.com/moment/moment/commit/c2a703a4d84aa57ee2722ff8fb4a8016279fb3c4)

**Tree at this commit:** [moment/moment@c2a703a4d84a](https://github.com/moment/moment/tree/c2a703a4d84aa57ee2722ff8fb4a8016279fb3c4)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | moment/moment |
| Description | Parse, validate, manipulate, and display dates in javascript. |
| Stars | 47873 |
| Forks | 6971 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | develop |
| Analysed commit | `c2a703a4d84aa57ee2722ff8fb4a8016279fb3c4` |
| Retrieved at | 2026-11-14T19:10:37.775116+00:00 |
| Files in this snapshot | 659 |

## Directory tree

```text
.agents/  (1 files)
  skills/  (1 files)
    locale-review/  (1 files)
      … 1 files under this directory
.githooks/  (2 files)
  post-checkout
  pre-commit
.github/  (11 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.yml
    config.yml
    locale_report.yml
  workflows/  (7 files)
    ci.yml
    coverage.yml
    fossa.yml
    pull-request.yml
    release.yml
    runtime-compatibility.yml
    timezones.yml
  CODEOWNERS
benchmarks/  (16 files)
  add.js
  clone.js
  compare.js
  endOf.js
  fromDate.js
  fromDateUtc.js
  get.js
  isObjectEmpty.js
  load-missing.js
  makeDuration.js
  parseCompactWeekday.js
  query.js
  set.js
  startOf.js
  subtract.js
  zeroFill.js
locale/  (139 files)
  af.js
  am-et.js
  ar-dz.js
  ar-kw.js
  ar-ly.js
  ar-ma.js
  ar-ps.js
  ar-sa.js
  ar-tn.js
  ar.js
  az.js
  be.js
  bg.js
  bm.js
  bn-bd.js
  bn.js
  bo.js
  br.js
  bs.js
  ca.js
  cs.js
  cv.js
  cy.js
  da.js
  … 115 more files
meteor/  (4 files)
  README.md
  export.js
  package.js
  test.js
scripts/  (14 files)
  benchmark.js
  build.js
  bump-version.js
  check-months-parse.js
  check-package.js
  install-hooks.js
  locales.js
  minify.js
  qunit-reporter.js
  test-runtime.js
  test-typescript-package.js
  test.js
  update-component.js
  update-index.js
src/  (447 files)
  lib/  (109 files)
    create/  (12 files)
      … 12 files under this directory
    duration/  (13 files)
      … 13 files under this directory
    format/  (1 files)
      … 1 files under this directory
    locale/  (14 files)
      … 14 files under this directory
    moment/  (19 files)
      … 19 files under this directory
    parse/  (2 files)
      … 2 files under this directory
    units/  (21 files)
      … 21 files under this directory
    utils/  (27 files)
      … 27 files under this directory
  locale/  (139 files)
    af.js
    am-et.js
    ar-dz.js
    ar-kw.js
    ar-ly.js
    ar-ma.js
    ar-ps.js
    ar-sa.js
    ar-tn.js
    ar.js
    az.js
    be.js
    bg.js
    bm.js
    bn-bd.js
    bn.js
    bo.js
    br.js
    bs.js
    ca.js
    cs.js
    cv.js
    cy.js
    da.js
    … 115 more files
  test/  (198 files)
    helpers/  (7 files)
      … 7 files under this directory
    locale/  (140 files)
      … 140 files under this directory
    moment/  (51 files)
      … 51 files under this directory
  moment.js
.editorconfig
.gitattributes
.gitignore
.markdownlint-cli2.jsonc
.npmignore
.prettierignore
.prettierrc
.spmignore
AGENTS.md
CHANGELOG.md
CONTRIBUTING.md
LICENSE
README.md
RELEASING.md
SECURITY.md
THREAT_MODEL.md
bower.json
component.json
composer.json
dojo.profile.js
ender.js
eslint.config.js
moment.d.ts
moment.js
… 1 more files
```

## Entry points

- [moment.js](https://github.com/moment/moment/blob/c2a703a4d84aa57ee2722ff8fb4a8016279fb3c4/moment.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| benchmarks package | library | Observed | Groups 16 file(s) under benchmarks package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 5 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 109 file(s) under lib package (observed from repository paths and static analysis). |
| locale package | library | Observed | Groups 278 file(s) under locale package (observed from repository paths and static analysis). |
| meteor package | library | Observed | Groups 3 file(s) under meteor package (observed from repository paths and static analysis). |
| moment.js package | library | Observed | Groups 1 file(s) under moment.js package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 14 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 198 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/locale_report.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/coverage.yml` (ci)
- `.github/workflows/fossa.yml` (ci)
- `.github/workflows/pull-request.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/runtime-compatibility.yml` (ci)
- `.github/workflows/timezones.yml` (ci)
- `bower.json` (config)
- `component.json` (config)
- `composer.json` (config)
- `package.json` (manifest)

## Top-level layout

- `src` — 447 analysed file(s)
- `locale` — 139 analysed file(s)
- `(root files)` — 25 analysed file(s)
- `benchmarks` — 16 analysed file(s)
- `scripts` — 14 analysed file(s)
- `.github` — 11 analysed file(s)
- `meteor` — 4 analysed file(s)
- `.githooks` — 2 analysed file(s)
- `.agents` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 141 file(s) were skipped during inventory (1 x lockfile excluded; 140 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `c2a703a4d84aa57ee2722ff8fb4a8016279fb3c4` is the revision these paths and observations refer to.
