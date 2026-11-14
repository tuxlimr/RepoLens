# Project structure: faisalman/ua-parser-js

**Analysed commit:** `8b7f9284d56fdfa9f94d3a1939029db197b94cf2`

**Commit reference:** [8b7f9284d56fdfa9f94d3a1939029db197b94cf2](https://github.com/faisalman/ua-parser-js/commit/8b7f9284d56fdfa9f94d3a1939029db197b94cf2)

**Tree at this commit:** [faisalman/ua-parser-js@8b7f9284d56f](https://github.com/faisalman/ua-parser-js/tree/8b7f9284d56fdfa9f94d3a1939029db197b94cf2)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | faisalman/ua-parser-js |
| Description | UAParser.js: The Essential Web Development Tool for User-Agent Detection. Detect Browsers, OS, Devices, Bots, Apps, AI Crawlers, and more. Run in Browser or Node |
| Stars | 10212 |
| Forks | 1215 |
| Licence | AGPL-3.0 |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `8b7f9284d56fdfa9f94d3a1939029db197b94cf2` |
| Retrieved at | 2026-11-14T19:12:42.806674+00:00 |
| Files in this snapshot | 393 |

## Directory tree

```text
.github/  (12 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  PULL_REQUEST_TEMPLATE/  (1 files)
    pull_request_template.md
  workflows/  (7 files)
    ai-assistant-spam-detection.yml
    analysis-codeql.yml
    analysis-dependency.yml
    analysis-scorecard.yml
    ci-build-test.yml
    publish-docker.yml
    publish-npm.yml
  PULL_REQUEST_TEMPLATE.md
  funding.yml
script/  (4 files)
  build-dist.sh
  build-esm.js
  cli.js
  test-all.sh
src/  (21 files)
  bot-detection/  (3 files)
    bot-detection.d.ts
    bot-detection.js
    bot-detection.mjs
  browser-detection/  (3 files)
    browser-detection.d.ts
    browser-detection.js
    browser-detection.mjs
  device-detection/  (3 files)
    device-detection.d.ts
    device-detection.js
    device-detection.mjs
  enums/  (3 files)
    ua-parser-enums.d.ts
    ua-parser-enums.js
    ua-parser-enums.mjs
  extensions/  (3 files)
    ua-parser-extensions.d.ts
    ua-parser-extensions.js
    ua-parser-extensions.mjs
  helpers/  (3 files)
    ua-parser-helpers.d.ts
    ua-parser-helpers.js
    ua-parser-helpers.mjs
  main/  (3 files)
    ua-parser.d.ts
    ua-parser.js
    ua-parser.mjs
test/  (345 files)
  data/  (330 files)
    ua/  (329 files)
      … 329 files under this directory
    ua-ch/  (1 files)
      … 1 files under this directory
  e2e/  (1 files)
    browser.spec.mjs
  fuzz/  (1 files)
    redos.js
  static/  (1 files)
    dts-lint.ts
  unit/  (12 files)
    cli/  (3 files)
      … 3 files under this directory
    submodules/  (5 files)
      … 5 files under this directory
    es6.mjs
    main.js
    redos.js
    ua-ch.js
.gitignore
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
Dockerfile
INCIDENT_RESPONSE.md
LICENSE.md
README.md
SECURITY.md
THIRD_PARTY_NOTICES.md
package.json
```

## Entry points

- [src/main/ua-parser.js](https://github.com/faisalman/ua-parser-js/blob/8b7f9284d56fdfa9f94d3a1939029db197b94cf2/src/main/ua-parser.js)
- [script/cli.js](https://github.com/faisalman/ua-parser-js/blob/8b7f9284d56fdfa9f94d3a1939029db197b94cf2/script/cli.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bot-detection package | library | Observed | Groups 3 file(s) under bot-detection package (observed from repository paths and static analysis). |
| browser-detection package | library | Observed | Groups 3 file(s) under browser-detection package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| device-detection package | library | Observed | Groups 3 file(s) under device-detection package (observed from repository paths and static analysis). |
| enums package | library | Observed | Groups 3 file(s) under enums package (observed from repository paths and static analysis). |
| extensions package | library | Observed | Groups 3 file(s) under extensions package (observed from repository paths and static analysis). |
| helpers package | library | Observed | Groups 3 file(s) under helpers package (observed from repository paths and static analysis). |
| main package | library | Observed | Groups 3 file(s) under main package (observed from repository paths and static analysis). |
| script package | library | Observed | Groups 4 file(s) under script package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 345 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/funding.yml` (config)
- `.github/workflows/ai-assistant-spam-detection.yml` (ci)
- `.github/workflows/analysis-codeql.yml` (ci)
- `.github/workflows/analysis-dependency.yml` (ci)
- `.github/workflows/analysis-scorecard.yml` (ci)
- `.github/workflows/ci-build-test.yml` (ci)
- `.github/workflows/publish-docker.yml` (ci)
- `.github/workflows/publish-npm.yml` (ci)
- `Dockerfile` (container)
- `package.json` (manifest)

## Top-level layout

- `test` — 345 analysed file(s)
- `src` — 21 analysed file(s)
- `.github` — 12 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `script` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 153 file(s) were skipped during inventory (153 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `8b7f9284d56fdfa9f94d3a1939029db197b94cf2` is the revision these paths and observations refer to.
