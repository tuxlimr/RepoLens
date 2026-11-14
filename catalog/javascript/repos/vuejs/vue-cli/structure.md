# Project structure: vuejs/vue-cli

**Analysed commit:** `7eb93c169c7520935252e2473387f923ef80d856`

**Commit reference:** [7eb93c169c7520935252e2473387f923ef80d856](https://github.com/vuejs/vue-cli/commit/7eb93c169c7520935252e2473387f923ef80d856)

**Tree at this commit:** [vuejs/vue-cli@7eb93c169c75](https://github.com/vuejs/vue-cli/tree/7eb93c169c7520935252e2473387f923ef80d856)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | vuejs/vue-cli |
| Description | 🛠️ webpack-based tooling for Vue.js Development |
| Stars | 29495 |
| Forks | 6217 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | dev |
| Analysed commit | `7eb93c169c7520935252e2473387f923ef80d856` |
| Retrieved at | 2026-11-14T19:10:47.667291+00:00 |
| Files in this snapshot | 785 |

## Directory tree

```text
.circleci/  (1 files)
  config.yml
.github/  (5 files)
  ISSUE_TEMPLATE/  (1 files)
    config.yml
  COMMIT_CONVENTION.md
  CONTRIBUTING.md
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
__mocks__/  (2 files)
  fs.js
  inquirer.js
docs/  (98 files)
  .vitepress/  (6 files)
    theme/  (4 files)
      … 4 files under this directory
    config.js
    self-destroying-service-worker.js
  config/  (1 files)
    index.md
  core-plugins/  (12 files)
    babel.md
    e2e-cypress.md
    e2e-nightwatch.md
    e2e-webdriverio.md
    eslint.md
    index.md
    pwa.md
    router.md
    typescript.md
    unit-jest.md
    unit-mocha.md
    vuex.md
  dev-guide/  (6 files)
    generator-api.md
    plugin-api.md
    plugin-dev.md
    ui-api.md
    ui-info.md
    ui-localization.md
  guide/  (14 files)
    browser-compatibility.md
    build-targets.md
    cli-service.md
    creating-a-project.md
    css.md
    deployment.md
    html-and-static-assets.md
    index.md
    installation.md
    mode-and-env.md
    plugins-and-presets.md
    prototyping.md
    troubleshooting.md
    webpack.md
  migrations/  (2 files)
    migrate-from-v3.md
    migrate-from-v4.md
  public/  (2 files)
    icons/  (1 files)
      … 1 files under this directory
    manifest.json
  ru/  (35 files)
    config/  (1 files)
      … 1 files under this directory
    core-plugins/  (12 files)
      … 12 files under this directory
    dev-guide/  (6 files)
      … 6 files under this directory
    guide/  (14 files)
      … 14 files under this directory
    migrating-from-v3/  (1 files)
      … 1 files under this directory
    index.md
  zh/  (19 files)
    config/  (1 files)
      … 1 files under this directory
    dev-guide/  (4 files)
      … 4 files under this directory
    guide/  (13 files)
      … 13 files under this directory
    index.md
  index.md
packages/  (668 files)
  @vue/  (668 files)
    babel-preset-app/  (6 files)
      … 6 files under this directory
    cli-init/  (4 files)
      … 4 files under this directory
    cli-overlay/  (4 files)
      … 4 files under this directory
    cli-plugin-babel/  (22 files)
      … 22 files under this directory
    cli-plugin-e2e-cypress/  (14 files)
      … 14 files under this directory
    cli-plugin-e2e-nightwatch/  (21 files)
      … 21 files under this directory
    cli-plugin-e2e-webdriverio/  (17 files)
      … 17 files under this directory
    cli-plugin-eslint/  (21 files)
      … 21 files under this directory
    cli-plugin-pwa/  (15 files)
      … 15 files under this directory
    cli-plugin-router/  (14 files)
      … 14 files under this directory
    cli-plugin-typescript/  (32 files)
      … 32 files under this directory
    cli-plugin-unit-jest/  (18 files)
      … 18 files under this directory
    cli-plugin-unit-mocha/  (12 files)
      … 12 files under this directory
    cli-plugin-vuex/  (9 files)
      … 9 files under this directory
    cli-service/  (69 files)
      … 69 files under this directory
    cli-shared-utils/  (22 files)
      … 22 files under this directory
    cli-test-utils/  (20 files)
      … 20 files under this directory
    cli-ui/  (298 files)
      … 298 files under this directory
    cli-ui-addon-webpack/  (28 files)
      … 28 files under this directory
    cli-ui-addon-widgets/  (22 files)
      … 22 files under this directory
.editorconfig
.eslintignore
.eslintrc.js
.gitignore
.tidelift.yml
LICENSE
README.md
appveyor.yml
jest.config.js
lerna.json
package.json
```

## Entry points

- [packages/@vue/babel-preset-app/index.js](https://github.com/vuejs/vue-cli/blob/7eb93c169c7520935252e2473387f923ef80d856/packages/%40vue/babel-preset-app/index.js)
- [packages/@vue/cli-init/index.js](https://github.com/vuejs/vue-cli/blob/7eb93c169c7520935252e2473387f923ef80d856/packages/%40vue/cli-init/index.js)
- [packages/@vue/cli-plugin-babel/index.js](https://github.com/vuejs/vue-cli/blob/7eb93c169c7520935252e2473387f923ef80d856/packages/%40vue/cli-plugin-babel/index.js)
- [packages/@vue/cli-plugin-e2e-cypress/index.js](https://github.com/vuejs/vue-cli/blob/7eb93c169c7520935252e2473387f923ef80d856/packages/%40vue/cli-plugin-e2e-cypress/index.js)
- [packages/@vue/cli-plugin-e2e-nightwatch/index.js](https://github.com/vuejs/vue-cli/blob/7eb93c169c7520935252e2473387f923ef80d856/packages/%40vue/cli-plugin-e2e-nightwatch/index.js)
- [packages/@vue/cli-plugin-e2e-webdriverio/index.js](https://github.com/vuejs/vue-cli/blob/7eb93c169c7520935252e2473387f923ef80d856/packages/%40vue/cli-plugin-e2e-webdriverio/index.js)
- [packages/@vue/cli-plugin-eslint/index.js](https://github.com/vuejs/vue-cli/blob/7eb93c169c7520935252e2473387f923ef80d856/packages/%40vue/cli-plugin-eslint/index.js)
- [packages/@vue/cli-plugin-pwa/index.js](https://github.com/vuejs/vue-cli/blob/7eb93c169c7520935252e2473387f923ef80d856/packages/%40vue/cli-plugin-pwa/index.js)
- [packages/@vue/cli-plugin-router/index.js](https://github.com/vuejs/vue-cli/blob/7eb93c169c7520935252e2473387f923ef80d856/packages/%40vue/cli-plugin-router/index.js)
- [packages/@vue/cli-plugin-typescript/index.js](https://github.com/vuejs/vue-cli/blob/7eb93c169c7520935252e2473387f923ef80d856/packages/%40vue/cli-plugin-typescript/index.js)
- [packages/@vue/cli-plugin-unit-jest/index.js](https://github.com/vuejs/vue-cli/blob/7eb93c169c7520935252e2473387f923ef80d856/packages/%40vue/cli-plugin-unit-jest/index.js)
- [packages/@vue/cli-plugin-unit-mocha/index.js](https://github.com/vuejs/vue-cli/blob/7eb93c169c7520935252e2473387f923ef80d856/packages/%40vue/cli-plugin-unit-mocha/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 13 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 39 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| __mocks__ package | library | Observed | Groups 2 file(s) under __mocks__ package (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 413 file(s) under packages package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 22 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.circleci/config.yml` (ci)
- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.tidelift.yml` (config)
- `appveyor.yml` (config)
- `docs/public/manifest.json` (config)
- `lerna.json` (config)
- `package.json` (manifest)
- `packages/@vue/babel-preset-app/package.json` (manifest)
- `packages/@vue/cli-init/package.json` (manifest)
- `packages/@vue/cli-overlay/package.json` (manifest)
- `packages/@vue/cli-plugin-babel/package.json` (manifest)
- `packages/@vue/cli-plugin-e2e-cypress/generator/template/cypress.json` (config)
- `packages/@vue/cli-plugin-e2e-cypress/package.json` (manifest)
- `packages/@vue/cli-plugin-e2e-nightwatch/package.json` (manifest)
- `packages/@vue/cli-plugin-e2e-webdriverio/package.json` (manifest)
- `packages/@vue/cli-plugin-eslint/package.json` (manifest)
- `packages/@vue/cli-plugin-pwa/package.json` (manifest)
- `packages/@vue/cli-plugin-router/package.json` (manifest)
- `packages/@vue/cli-plugin-typescript/generator/template/tsconfig.json` (config)
- `packages/@vue/cli-plugin-typescript/package.json` (manifest)
- `packages/@vue/cli-plugin-unit-jest/package.json` (manifest)
- `packages/@vue/cli-plugin-unit-mocha/package.json` (manifest)
- `packages/@vue/cli-plugin-vuex/package.json` (manifest)
- `packages/@vue/cli-service/generator/template/jsconfig.json` (config)
- `packages/@vue/cli-service/package.json` (manifest)
- `packages/@vue/cli-service/types/tsconfig.json` (config)
- `packages/@vue/cli-shared-utils/package.json` (manifest)
- `packages/@vue/cli-test-utils/package.json` (manifest)
- `packages/@vue/cli-test-utils/types/tsconfig.json` (config)
- `packages/@vue/cli-ui-addon-webpack/package.json` (manifest)
- `packages/@vue/cli-ui-addon-webpack/src/assets/speeds.json` (config)
- `packages/@vue/cli-ui-addon-webpack/src/locales/en.json` (config)
- `packages/@vue/cli-ui-addon-widgets/package.json` (manifest)
- `packages/@vue/cli-ui/cypress.json` (config)
- `packages/@vue/cli-ui/locales/en.json` (config)
- `packages/@vue/cli-ui/package.json` (manifest)

## Top-level layout

- `packages` — 668 analysed file(s)
- `docs` — 98 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `.github` — 5 analysed file(s)
- `__mocks__` — 2 analysed file(s)
- `.circleci` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 15 file(s) were skipped during inventory (2 x likely secret file excluded; 13 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `7eb93c169c7520935252e2473387f923ef80d856` is the revision these paths and observations refer to.
