# Project structure: mjmlio/mjml

**Analysed commit:** `40ddfbb4c04e13dd9572aa0d5b1c58826a163289`

**Commit reference:** [40ddfbb4c04e13dd9572aa0d5b1c58826a163289](https://github.com/mjmlio/mjml/commit/40ddfbb4c04e13dd9572aa0d5b1c58826a163289)

**Tree at this commit:** [mjmlio/mjml@40ddfbb4c04e](https://github.com/mjmlio/mjml/tree/40ddfbb4c04e13dd9572aa0d5b1c58826a163289)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | mjmlio/mjml |
| Description | MJML: the only framework that makes responsive email easy |
| Stars | 18295 |
| Forks | 1009 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `40ddfbb4c04e13dd9572aa0d5b1c58826a163289` |
| Retrieved at | 2026-11-14T19:11:22.583715+00:00 |
| Files in this snapshot | 245 |

## Directory tree

```text
.github/  (5 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (3 files)
    build-documentation.yml
    mjml-workflow.yml
    npm-publish.yml
doc/  (21 files)
  basic.md
  body_components.md
  community-components.md
  community-contributions.md
  components_1.md
  components_2.md
  config.json
  create.md
  ending-tags.md
  getting_started.md
  guide.md
  head_components.md
  install.md
  mjml-bar-chart.md
  mjml-chart.md
  mjml-chartjs.md
  mjml-mso-button.md
  mjml-qr-code.md
  ports.md
  tooling.md
  using_mjml_in_json.md
packages/  (203 files)
  mjml/  (34 files)
    bin/  (1 files)
      … 1 files under this directory
    src/  (1 files)
      … 1 files under this directory
    test/  (30 files)
      … 30 files under this directory
    README.md
    package.json
  mjml-accordion/  (7 files)
    src/  (5 files)
      … 5 files under this directory
    README.md
    package.json
  mjml-body/  (4 files)
    src/  (2 files)
      … 2 files under this directory
    README.md
    package.json
  mjml-browser/  (10 files)
    browser-mocks/  (6 files)
      … 6 files under this directory
    README.md
    package.json
    smoke-browser-global.js
    webpack.config.js
  mjml-button/  (3 files)
    src/  (1 files)
      … 1 files under this directory
    README.md
    package.json
  mjml-carousel/  (5 files)
    src/  (3 files)
      … 3 files under this directory
    README.md
    package.json
  mjml-cli/  (11 files)
    bin/  (1 files)
      … 1 files under this directory
    src/  (8 files)
      … 8 files under this directory
    README.md
    package.json
  mjml-column/  (3 files)
    src/  (1 files)
      … 1 files under this directory
    README.md
    package.json
  mjml-core/  (38 files)
    src/  (29 files)
      … 29 files under this directory
    tests/  (7 files)
      … 7 files under this directory
    README.md
    package.json
  mjml-divider/  (3 files)
    src/  (1 files)
      … 1 files under this directory
    README.md
    package.json
  mjml-group/  (3 files)
    src/  (1 files)
      … 1 files under this directory
    README.md
    package.json
  mjml-head/  (2 files)
    src/  (1 files)
      … 1 files under this directory
    package.json
  mjml-head-attributes/  (3 files)
    src/  (1 files)
      … 1 files under this directory
    README.md
    package.json
  mjml-head-breakpoint/  (3 files)
    src/  (1 files)
      … 1 files under this directory
    README.md
    package.json
  mjml-head-font/  (3 files)
    src/  (1 files)
      … 1 files under this directory
    README.md
    package.json
  mjml-head-html-attributes/  (3 files)
    src/  (1 files)
      … 1 files under this directory
    README.md
    package.json
  mjml-head-preview/  (3 files)
    src/  (1 files)
      … 1 files under this directory
    README.md
    package.json
  mjml-head-style/  (3 files)
    src/  (1 files)
      … 1 files under this directory
    README.md
    package.json
  mjml-head-title/  (3 files)
    src/  (1 files)
      … 1 files under this directory
    README.md
    package.json
  mjml-hero/  (3 files)
    src/  (1 files)
      … 1 files under this directory
    README.md
    package.json
  mjml-image/  (3 files)
    src/  (1 files)
      … 1 files under this directory
    README.md
    package.json
  mjml-navbar/  (5 files)
    src/  (3 files)
      … 3 files under this directory
    README.md
    package.json
  mjml-parser-xml/  (10 files)
    src/  (4 files)
      … 4 files under this directory
    test/  (5 files)
      … 5 files under this directory
    package.json
  mjml-preset-core/  (4 files)
    src/  (2 files)
      … 2 files under this directory
    README.md
    package.json
  mjml-raw/  (3 files)
    src/  (1 files)
      … 1 files under this directory
    README.md
    package.json
  mjml-section/  (3 files)
    src/  (1 files)
      … 1 files under this directory
    README.md
    package.json
  mjml-social/  (5 files)
    src/  (3 files)
      … 3 files under this directory
    README.md
    package.json
  mjml-spacer/  (3 files)
    src/  (1 files)
      … 1 files under this directory
    README.md
    package.json
  mjml-table/  (3 files)
    src/  (1 files)
      … 1 files under this directory
    README.md
    package.json
  mjml-text/  (3 files)
    src/  (1 files)
      … 1 files under this directory
    README.md
    package.json
  mjml-validator/  (11 files)
    src/  (9 files)
      … 9 files under this directory
    README.md
    package.json
  mjml-wrapper/  (3 files)
    src/  (1 files)
      … 1 files under this directory
    README.md
    package.json
scripts/  (1 files)
  smoke-cli-pack.sh
.editorconfig
.eslintignore
.eslintrc
.gitignore
.prettierignore
.prettierrc
CONTRIBUTING.md
LICENSE.md
README.md
babel.config.js
lerna.json
package.json
readme-ja.md
test.js
type.js
```

## Entry points

- [packages/mjml-cli/bin/mjml](https://github.com/mjmlio/mjml/blob/40ddfbb4c04e13dd9572aa0d5b1c58826a163289/packages/mjml-cli/bin/mjml)
- [packages/mjml/bin/mjml](https://github.com/mjmlio/mjml/blob/40ddfbb4c04e13dd9572aa0d5b1c58826a163289/packages/mjml/bin/mjml)
- [packages/mjml-accordion/src/index.js](https://github.com/mjmlio/mjml/blob/40ddfbb4c04e13dd9572aa0d5b1c58826a163289/packages/mjml-accordion/src/index.js)
- [packages/mjml-body/src/index.js](https://github.com/mjmlio/mjml/blob/40ddfbb4c04e13dd9572aa0d5b1c58826a163289/packages/mjml-body/src/index.js)
- [packages/mjml-button/src/index.js](https://github.com/mjmlio/mjml/blob/40ddfbb4c04e13dd9572aa0d5b1c58826a163289/packages/mjml-button/src/index.js)
- [packages/mjml-carousel/src/index.js](https://github.com/mjmlio/mjml/blob/40ddfbb4c04e13dd9572aa0d5b1c58826a163289/packages/mjml-carousel/src/index.js)
- [packages/mjml-column/src/index.js](https://github.com/mjmlio/mjml/blob/40ddfbb4c04e13dd9572aa0d5b1c58826a163289/packages/mjml-column/src/index.js)
- [packages/mjml-core/src/index.js](https://github.com/mjmlio/mjml/blob/40ddfbb4c04e13dd9572aa0d5b1c58826a163289/packages/mjml-core/src/index.js)
- [packages/mjml-divider/src/index.js](https://github.com/mjmlio/mjml/blob/40ddfbb4c04e13dd9572aa0d5b1c58826a163289/packages/mjml-divider/src/index.js)
- [packages/mjml-group/src/index.js](https://github.com/mjmlio/mjml/blob/40ddfbb4c04e13dd9572aa0d5b1c58826a163289/packages/mjml-group/src/index.js)
- [packages/mjml-head-attributes/src/index.js](https://github.com/mjmlio/mjml/blob/40ddfbb4c04e13dd9572aa0d5b1c58826a163289/packages/mjml-head-attributes/src/index.js)
- [packages/mjml-head-breakpoint/src/index.js](https://github.com/mjmlio/mjml/blob/40ddfbb4c04e13dd9572aa0d5b1c58826a163289/packages/mjml-head-breakpoint/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 34 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 97 file(s) under packages package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 42 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/workflows/build-documentation.yml` (ci)
- `.github/workflows/mjml-workflow.yml` (ci)
- `.github/workflows/npm-publish.yml` (ci)
- `doc/config.json` (config)
- `lerna.json` (config)
- `package.json` (manifest)
- `packages/mjml-accordion/package.json` (manifest)
- `packages/mjml-body/package.json` (manifest)
- `packages/mjml-browser/package.json` (manifest)
- `packages/mjml-button/package.json` (manifest)
- `packages/mjml-carousel/package.json` (manifest)
- `packages/mjml-cli/package.json` (manifest)
- `packages/mjml-column/package.json` (manifest)
- `packages/mjml-core/package.json` (manifest)
- `packages/mjml-divider/package.json` (manifest)
- `packages/mjml-group/package.json` (manifest)
- `packages/mjml-head-attributes/package.json` (manifest)
- `packages/mjml-head-breakpoint/package.json` (manifest)
- `packages/mjml-head-font/package.json` (manifest)
- `packages/mjml-head-html-attributes/package.json` (manifest)
- `packages/mjml-head-preview/package.json` (manifest)
- `packages/mjml-head-style/package.json` (manifest)
- `packages/mjml-head-title/package.json` (manifest)
- `packages/mjml-head/package.json` (manifest)
- `packages/mjml-hero/package.json` (manifest)
- `packages/mjml-image/package.json` (manifest)
- `packages/mjml-navbar/package.json` (manifest)
- `packages/mjml-parser-xml/package.json` (manifest)
- `packages/mjml-preset-core/package.json` (manifest)
- `packages/mjml-raw/package.json` (manifest)
- `packages/mjml-section/package.json` (manifest)
- `packages/mjml-social/package.json` (manifest)
- `packages/mjml-spacer/package.json` (manifest)
- `packages/mjml-table/package.json` (manifest)
- `packages/mjml-text/package.json` (manifest)
- `packages/mjml-validator/package.json` (manifest)
- `packages/mjml-wrapper/package.json` (manifest)
- `packages/mjml/package.json` (manifest)

## Top-level layout

- `packages` — 203 analysed file(s)
- `doc` — 21 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `.github` — 5 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `40ddfbb4c04e13dd9572aa0d5b1c58826a163289` is the revision these paths and observations refer to.
