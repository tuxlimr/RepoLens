# Project structure: VulcanJS/Vulcan

**Analysed commit:** `5b81976dc67a5af280131ce093d889a29a736d93`

**Commit reference:** [5b81976dc67a5af280131ce093d889a29a736d93](https://github.com/VulcanJS/Vulcan/commit/5b81976dc67a5af280131ce093d889a29a736d93)

**Tree at this commit:** [VulcanJS/Vulcan@5b81976dc67a](https://github.com/VulcanJS/Vulcan/tree/5b81976dc67a5af280131ce093d889a29a736d93)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | VulcanJS/Vulcan |
| Description | 🌋 A toolkit to quickly build apps with React, GraphQL & Meteor |
| Stars | 7888 |
| Forks | 1803 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | devel |
| Analysed commit | `5b81976dc67a5af280131ce093d889a29a736d93` |
| Retrieved at | 2026-11-14T19:13:44.211917+00:00 |
| Files in this snapshot | 798 |

## Directory tree

```text
.circleci/  (1 files)
  config.yml
.github/  (4 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  CONTRIBUTING.md
  stale.yml
.meteor/  (8 files)
  .finished-upgraders
  .gitignore
  .id
  cordova-plugins
  packages
  platforms
  release
  versions
.storybook/  (14 files)
  decorators/  (2 files)
    BootstrapDecorator.js
    MaterialUIDecorator.js
  loaders/  (1 files)
    starter-example-loader.js
  mocks/  (6 files)
    Meteor.js
    Mongo.js
    Vulcan.js
    meteor-apollo.js
    meteor-server-render.js
    vulcan-email.js
  addons.js
  config.js
  helpers.js
  startup.js
  webpack.config.js
.vscode/  (1 files)
  launch.json
.vulcan/  (6 files)
  prettier/  (1 files)
    index.js
  shared/  (2 files)
    listChangedFiles.js
    pathsByLanguageVersion.js
  .gitignore
  prestart_vulcan.js
  update_package.js
packages/  (743 files)
  _boilerplate-generator/  (10 files)
    .npm/  (3 files)
      … 3 files under this directory
    .gitignore
    README.md
    generator.js
    package.js
    template-web.browser.js
    template-web.cordova.js
    template.js
  _buffer/  (2 files)
    buffer.js
    package.js
  meteor-mocha/  (8 files)
    browser-shim.js
    client.js
    package.js
    package.json
    prepForHTMLReporter.js
    runtimeArgs.js
    server.handleCoverage.js
    server.js
  vulcan-accounts/  (29 files)
    imports/  (25 files)
      … 25 files under this directory
    README.md
    main_client.js
    main_server.js
    package.js
  vulcan-admin/  (16 files)
    lib/  (14 files)
      … 14 files under this directory
    README.md
    package.js
  vulcan-backoffice/  (29 files)
    lib/  (21 files)
      … 21 files under this directory
    test/  (4 files)
      … 4 files under this directory
    .gitignore
    README.md
    package.js
    package.json
  vulcan-cloudinary/  (9 files)
    lib/  (7 files)
      … 7 files under this directory
    README.md
    package.js
  vulcan-core/  (101 files)
    lib/  (88 files)
      … 88 files under this directory
    test/  (11 files)
      … 11 files under this directory
    README.md
    package.js
  vulcan-debug/  (38 files)
    lib/  (36 files)
      … 36 files under this directory
    README.md
    package.js
  vulcan-email/  (13 files)
    lib/  (10 files)
      … 10 files under this directory
    .gitignore
    README.md
    package.js
  vulcan-embed/  (15 files)
    lib/  (12 files)
      … 12 files under this directory
    .gitignore
    README.md
    package.js
  vulcan-errors/  (12 files)
    lib/  (10 files)
      … 10 files under this directory
    README.md
    package.js
  vulcan-errors-sentry/  (9 files)
    lib/  (7 files)
      … 7 files under this directory
    README.md
    package.js
  vulcan-events/  (6 files)
    lib/  (4 files)
      … 4 files under this directory
    README.md
    package.js
  vulcan-events-ga/  (6 files)
    lib/  (4 files)
      … 4 files under this directory
    README.md
    package.js
  vulcan-events-intercom/  (7 files)
    lib/  (5 files)
      … 5 files under this directory
    README.md
    package.js
  vulcan-events-internal/  (10 files)
    lib/  (8 files)
      … 8 files under this directory
    README.md
    package.js
  vulcan-events-segment/  (7 files)
    lib/  (5 files)
      … 5 files under this directory
    README.md
    package.js
  vulcan-forms/  (39 files)
    lib/  (29 files)
      … 29 files under this directory
    test/  (8 files)
      … 8 files under this directory
    README.md
    package.js
  vulcan-forms-tags/  (4 files)
    lib/  (2 files)
      … 2 files under this directory
    README.md
    package.js
  vulcan-forms-upload/  (6 files)
    lib/  (4 files)
      … 4 files under this directory
    README.md
    package.js
  vulcan-i18n/  (13 files)
    lib/  (9 files)
      … 9 files under this directory
    test/  (2 files)
      … 2 files under this directory
    README.md
    package.js
  vulcan-i18n-en-us/  (3 files)
    lib/  (1 files)
      … 1 files under this directory
    README.md
    package.js
  vulcan-i18n-es-es/  (3 files)
    lib/  (1 files)
      … 1 files under this directory
    README.md
    package.js
  vulcan-i18n-fa-ir/  (3 files)
    lib/  (1 files)
      … 1 files under this directory
    README.md
    package.js
  vulcan-i18n-fr-fr/  (3 files)
    lib/  (1 files)
      … 1 files under this directory
    README.md
    package.js
  vulcan-lib/  (126 files)
    lib/  (103 files)
      … 103 files under this directory
    test/  (21 files)
      … 21 files under this directory
    README.md
    package.js
  vulcan-newsletter/  (22 files)
    lib/  (18 files)
      … 18 files under this directory
    .gitignore
    README.md
    package.js
    scss.json
  vulcan-payments/  (19 files)
    lib/  (17 files)
      … 17 files under this directory
    README.md
    package.js
  vulcan-redux/  (15 files)
    lib/  (8 files)
      … 8 files under this directory
    test/  (5 files)
      … 5 files under this directory
    README.md
    package.js
  vulcan-scss/  (23 files)
    .github/  (1 files)
      … 1 files under this directory
    plugin/  (1 files)
      … 1 files under this directory
    test/  (12 files)
      … 12 files under this directory
    .gitignore
    .travis.yml
    .versions
    ISSUE_TEMPLATE.md
    LICENSE.txt
    README.md
    package.js
    scss-config.json
    tests.js
  vulcan-styled-components/  (6 files)
    lib/  (4 files)
      … 4 files under this directory
    README.md
    package.js
  vulcan-subscribe/  (11 files)
    lib/  (9 files)
      … 9 files under this directory
    README.md
    package.js
  vulcan-test/  (13 files)
    lib/  (11 files)
      … 11 files under this directory
    README.md
    package.js
  vulcan-ui-bootstrap/  (49 files)
    lib/  (47 files)
      … 47 files under this directory
    README.md
    package.js
  vulcan-ui-material/  (57 files)
    lib/  (52 files)
      … 52 files under this directory
    accounts.css
    en_US.js
    forms.css
    fr_FR.js
    history.md
  .gitignore
.babelrc
.editorconfig
.eslintignore
.eslintrc
.gitignore
.jshintrc
.meteorignore
.nvmrc
.prettierrc.js
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
Dockerfile
MIGRATING.md
README.md
RELEASE.md
jsconfig.json
jsdoc-conf.json
jsdoc.json
license.md
package.json
```

## Entry points

- [packages/vulcan-backoffice/package.js](https://github.com/VulcanJS/Vulcan/blob/5b81976dc67a5af280131ce093d889a29a736d93/packages/vulcan-backoffice/package.js)
- [.vulcan/prettier/index.js](https://github.com/VulcanJS/Vulcan/blob/5b81976dc67a5af280131ce093d889a29a736d93/.vulcan/prettier/index.js)
- [packages/meteor-mocha/server.js](https://github.com/VulcanJS/Vulcan/blob/5b81976dc67a5af280131ce093d889a29a736d93/packages/meteor-mocha/server.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 1 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 17 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 2 file(s) under data layer (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 58 file(s) under external integrations (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 541 file(s) under packages package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 7 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 63 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.circleci/config.yml` (ci)
- `.editorconfig` (config)
- `.github/stale.yml` (config)
- `.vscode/launch.json` (config)
- `Dockerfile` (container)
- `jsconfig.json` (config)
- `jsdoc-conf.json` (config)
- `jsdoc.json` (config)
- `package.json` (manifest)
- `packages/_boilerplate-generator/.npm/package/npm-shrinkwrap.json` (config)
- `packages/meteor-mocha/package.json` (manifest)
- `packages/vulcan-backoffice/package.json` (manifest)
- `packages/vulcan-newsletter/scss.json` (config)
- `packages/vulcan-scss/.github/workflows/comment-issue.yml` (ci)
- `packages/vulcan-scss/.travis.yml` (ci)
- `packages/vulcan-scss/scss-config.json` (config)

## Top-level layout

- `packages` — 743 analysed file(s)
- `(root files)` — 21 analysed file(s)
- `.storybook` — 14 analysed file(s)
- `.meteor` — 8 analysed file(s)
- `.vulcan` — 6 analysed file(s)
- `.github` — 4 analysed file(s)
- `.circleci` — 1 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (1 x generated/minified file excluded; 1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `5b81976dc67a5af280131ce093d889a29a736d93` is the revision these paths and observations refer to.
