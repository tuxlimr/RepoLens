# Project structure: validatorjs/validator.js

**Analysed commit:** `9ff342479591ca5a43cb30000195bcf55c1bbed9`

**Commit reference:** [9ff342479591ca5a43cb30000195bcf55c1bbed9](https://github.com/validatorjs/validator.js/commit/9ff342479591ca5a43cb30000195bcf55c1bbed9)

**Tree at this commit:** [validatorjs/validator.js@9ff342479591](https://github.com/validatorjs/validator.js/tree/9ff342479591ca5a43cb30000195bcf55c1bbed9)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | validatorjs/validator.js |
| Description | String validation |
| Stars | 23741 |
| Forks | 2551 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `9ff342479591ca5a43cb30000195bcf55c1bbed9` |
| Retrieved at | 2026-11-14T19:11:04.288432+00:00 |
| Files in this snapshot | 149 |

## Directory tree

```text
.github/  (6 files)
  ISSUE_TEMPLATE/  (1 files)
    bug_report.md
  workflows/  (3 files)
    ci.yml
    codeql-analysis.yml
    npm-publish.yml
  FUNDING.yml
  pull_request_template.md
src/  (114 files)
  lib/  (113 files)
    util/  (10 files)
      … 10 files under this directory
    alpha.js
    blacklist.js
    contains.js
    equals.js
    escape.js
    isAbaRouting.js
    isAfter.js
    isAlpha.js
    isAlphanumeric.js
    isAscii.js
    isBIC.js
    isBase32.js
    isBase58.js
    isBase64.js
    isBefore.js
    isBoolean.js
    isBtcAddress.js
    isByteLength.js
    isCreditCard.js
    isCurrency.js
    isDataURI.js
    isDate.js
    isDecimal.js
    isDivisibleBy.js
    … 79 more files
  index.js
test/  (14 files)
  validators/  (9 files)
    isAfter.test.js
    isBase64.test.js
    isBefore.test.js
    isFQDN.test.js
    isIP.test.js
    isISBN.test.js
    isISO31661Alpha2.test.js
    isISO31661Alpha3.test.js
    isLength.test.js
  clientSide.test.js
  exports.test.js
  sanitizers.test.js
  testFunctions.js
  util.test.js
.babelrc
.eslintrc.json
.gitignore
.nycrc
AGENTS.md
CHANGELOG.md
CONTRIBUTING.md
LICENSE
README.md
SECURITY.md
THREAT_MODEL.md
bower.json
build-browser.mjs
jsconfig.json
package.json
```

## Entry points

- [src/index.js](https://github.com/validatorjs/validator.js/blob/9ff342479591ca5a43cb30000195bcf55c1bbed9/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 113 file(s) under lib package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 14 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.eslintrc.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/codeql-analysis.yml` (ci)
- `.github/workflows/npm-publish.yml` (ci)
- `bower.json` (config)
- `jsconfig.json` (config)
- `package.json` (manifest)

## Top-level layout

- `src` — 114 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `test` — 14 analysed file(s)
- `.github` — 6 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `9ff342479591ca5a43cb30000195bcf55c1bbed9` is the revision these paths and observations refer to.
