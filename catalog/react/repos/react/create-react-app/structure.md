# Project structure: react/create-react-app

**Analysed commit:** `6254386531d263688ccfa542d0e628fbc0de0b28`

**Commit reference:** [6254386531d263688ccfa542d0e628fbc0de0b28](https://github.com/react/create-react-app/commit/6254386531d263688ccfa542d0e628fbc0de0b28)

**Tree at this commit:** [react/create-react-app@6254386531d2](https://github.com/react/create-react-app/tree/6254386531d263688ccfa542d0e628fbc0de0b28)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | react/create-react-app |
| Description | Set up a modern web app by running one command. |
| Stars | 103224 |
| Forks | 26852 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `6254386531d263688ccfa542d0e628fbc0de0b28` |
| Retrieved at | 2026-11-14T19:12:55.707520+00:00 |
| Files in this snapshot | 501 |

## Directory tree

```text
.github/  (11 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    proposal.md
    question.md
  workflows/  (3 files)
    build-and-test.yml
    e2e-base.yml
    lint.yml
  CODEOWNERS
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
  lock.yml
  stale.yml
docusaurus/  (55 files)
  docs/  (44 files)
    adding-a-css-modules-stylesheet.md
    adding-a-router.md
    adding-a-sass-stylesheet.md
    adding-a-stylesheet.md
    adding-bootstrap.md
    adding-css-reset.md
    adding-custom-environment-variables.md
    adding-flow.md
    adding-images-fonts-and-files.md
    adding-relay.md
    adding-typescript.md
    advanced-configuration.md
    alternatives-to-ejecting.md
    analyzing-the-bundle-size.md
    available-scripts.md
    can-i-use-decorators.md
    code-splitting.md
    custom-templates.md
    debugging-tests.md
    deployment.md
    developing-components-in-isolation.md
    documentation-intro.md
    fetching-data-with-ajax-requests.md
    folder-structure.md
    … 20 more files
  website/  (11 files)
    src/  (3 files)
      … 3 files under this directory
    static/  (3 files)
      … 3 files under this directory
    .gitignore
    README.md
    docusaurus.config.js
    package.json
    sidebars.json
packages/  (318 files)
  babel-plugin-named-asset-import/  (4 files)
    LICENSE
    index.js
    index.test.js
    package.json
  babel-preset-react-app/  (10 files)
    LICENSE
    README.md
    create.js
    dependencies.js
    dev.js
    index.js
    package.json
    prod.js
    test.js
    webpack-overrides.js
  confusing-browser-globals/  (5 files)
    LICENSE
    README.md
    index.js
    package.json
    test.js
  cra-template/  (16 files)
    template/  (13 files)
      … 13 files under this directory
    README.md
    package.json
    template.json
  cra-template-typescript/  (16 files)
    template/  (13 files)
      … 13 files under this directory
    README.md
    package.json
    template.json
  create-react-app/  (7 files)
    __tests__/  (2 files)
      … 2 files under this directory
    LICENSE
    README.md
    createReactApp.js
    index.js
    package.json
  eslint-config-react-app/  (6 files)
    LICENSE
    README.md
    base.js
    index.js
    jest.js
    package.json
  react-app-polyfill/  (7 files)
    LICENSE
    README.md
    ie11.js
    ie9.js
    jsdom.js
    package.json
    stable.js
  react-dev-utils/  (41 files)
    __tests__/  (4 files)
      … 4 files under this directory
    FileSizeReporter.js
    ForkTsCheckerWarningWebpackPlugin.js
    ForkTsCheckerWebpackPlugin.js
    InlineChunkHtmlPlugin.js
    InterpolateHtmlPlugin.js
    LICENSE
    ModuleNotFoundPlugin.js
    ModuleScopePlugin.js
    README.md
    WebpackDevServerUtils.js
    browsersHelper.js
    chalk.js
    checkRequiredFiles.js
    clearConsole.js
    crossSpawn.js
    errorOverlayMiddleware.js
    eslintFormatter.js
    evalSourceMapMiddleware.js
    formatWebpackMessages.js
    getCSSModuleLocalIdent.js
    getCacheIdentifier.js
    getProcessForPort.js
    getPublicUrlOrPath.js
    globby.js
    … 13 more files
  react-error-overlay/  (75 files)
    fixtures/  (6 files)
      … 6 files under this directory
    flow/  (1 files)
      … 1 files under this directory
    src/  (57 files)
      … 57 files under this directory
    .babelrc
    .flowconfig
    .gitattributes
    .gitignore
    .npmignore
    LICENSE
    README.md
    build.js
    package.json
    webpack.config.iframe.js
    webpack.config.js
  react-scripts/  (131 files)
    bin/  (1 files)
      … 1 files under this directory
    config/  (10 files)
      … 10 files under this directory
    fixtures/  (106 files)
      … 106 files under this directory
    lib/  (1 files)
      … 1 files under this directory
    scripts/  (7 files)
      … 7 files under this directory
    template/  (1 files)
      … 1 files under this directory
    template-typescript/  (1 files)
      … 1 files under this directory
    .npmignore
    LICENSE
    README.md
    package.json
tasks/  (15 files)
  .gitignore
  cra.js
  e2e-behavior.sh
  e2e-installs.sh
  e2e-kitchensink-eject.sh
  e2e-kitchensink.sh
  e2e-old-node.sh
  e2e-simple.sh
  local-registry.sh
  local-test.sh
  publish.sh
  screencast-start.js
  screencast.js
  screencast.sh
  verdaccio.yaml
test/  (78 files)
  fixtures/  (75 files)
    __shared__/  (4 files)
      … 4 files under this directory
    boostrap-sass/  (4 files)
      … 4 files under this directory
    builds-with-multiple-runtimes/  (3 files)
      … 3 files under this directory
    global-scss-asset-resolution/  (5 files)
      … 5 files under this directory
    issue-5176-flow-class-properties/  (4 files)
      … 4 files under this directory
    issue-5947-not-typescript/  (2 files)
      … 2 files under this directory
    jsconfig/  (7 files)
      … 7 files under this directory
    mjs-support/  (5 files)
      … 5 files under this directory
    relative-paths/  (5 files)
      … 5 files under this directory
    typescript/  (6 files)
      … 6 files under this directory
    typescript-advanced/  (5 files)
      … 5 files under this directory
    typescript-typecheck/  (4 files)
      … 4 files under this directory
    webpack-message-formatting/  (21 files)
      … 21 files under this directory
  integration/  (1 files)
    create-react-app/  (1 files)
      … 1 files under this directory
  README.md
  jest.config.js
.alexignore
.alexrc
.eslintignore
.eslintrc.json
.gitattributes
.gitignore
.prettierignore
.prettierrc
CHANGELOG-0.x.md
CHANGELOG-1.x.md
CHANGELOG-2.x.md
CHANGELOG-3.x.md
CHANGELOG-4.x.md
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
SECURITY.md
lerna.json
netlify.toml
package.json
screencast-error.svg
screencast.svg
```

## Entry points

- [packages/babel-plugin-named-asset-import/index.js](https://github.com/react/create-react-app/blob/6254386531d263688ccfa542d0e628fbc0de0b28/packages/babel-plugin-named-asset-import/index.js)
- [packages/confusing-browser-globals/index.js](https://github.com/react/create-react-app/blob/6254386531d263688ccfa542d0e628fbc0de0b28/packages/confusing-browser-globals/index.js)
- [packages/create-react-app/index.js](https://github.com/react/create-react-app/blob/6254386531d263688ccfa542d0e628fbc0de0b28/packages/create-react-app/index.js)
- [packages/react-scripts/fixtures/kitchensink/template.json](https://github.com/react/create-react-app/blob/6254386531d263688ccfa542d0e628fbc0de0b28/packages/react-scripts/fixtures/kitchensink/template.json)
- [packages/react-scripts/bin/react-scripts.js](https://github.com/react/create-react-app/blob/6254386531d263688ccfa542d0e628fbc0de0b28/packages/react-scripts/bin/react-scripts.js)
- [packages/babel-preset-react-app/index.js](https://github.com/react/create-react-app/blob/6254386531d263688ccfa542d0e628fbc0de0b28/packages/babel-preset-react-app/index.js)
- [packages/eslint-config-react-app/index.js](https://github.com/react/create-react-app/blob/6254386531d263688ccfa542d0e628fbc0de0b28/packages/eslint-config-react-app/index.js)
- [packages/react-error-overlay/src/index.js](https://github.com/react/create-react-app/blob/6254386531d263688ccfa542d0e628fbc0de0b28/packages/react-error-overlay/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 40 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| docusaurus package | library | Observed | Groups 2 file(s) under docusaurus package (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 5 file(s) under external integrations (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 210 file(s) under packages package (observed from repository paths and static analysis). |
| tasks package | library | Observed | Groups 13 file(s) under tasks package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 78 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.eslintrc.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/lock.yml` (config)
- `.github/stale.yml` (config)
- `.github/workflows/build-and-test.yml` (ci)
- `.github/workflows/e2e-base.yml` (ci)
- `.github/workflows/lint.yml` (ci)
- `docusaurus/website/package.json` (manifest)
- `docusaurus/website/sidebars.json` (config)
- `lerna.json` (config)
- `netlify.toml` (config)
- `package.json` (manifest)
- `packages/babel-plugin-named-asset-import/package.json` (manifest)
- `packages/babel-preset-react-app/package.json` (manifest)
- `packages/confusing-browser-globals/package.json` (manifest)
- `packages/cra-template-typescript/package.json` (manifest)
- `packages/cra-template-typescript/template.json` (config)
- `packages/cra-template-typescript/template/public/manifest.json` (config)
- `packages/cra-template/package.json` (manifest)
- `packages/cra-template/template.json` (config)
- `packages/cra-template/template/public/manifest.json` (config)
- `packages/create-react-app/package.json` (manifest)
- `packages/eslint-config-react-app/package.json` (manifest)
- `packages/react-app-polyfill/package.json` (manifest)
- `packages/react-dev-utils/package.json` (manifest)
- `packages/react-error-overlay/fixtures/bundle-default.json` (config)
- `packages/react-error-overlay/fixtures/bundle.json` (config)
- `packages/react-error-overlay/fixtures/bundle2.json` (config)
- `packages/react-error-overlay/package.json` (manifest)
- `packages/react-scripts/fixtures/kitchensink/package.json` (manifest)
- `packages/react-scripts/fixtures/kitchensink/template.json` (config)
- `packages/react-scripts/fixtures/kitchensink/template/jsconfig.json` (config)
- `packages/react-scripts/fixtures/kitchensink/template/src/features/webpack/assets/abstract.json` (config)
- `packages/react-scripts/package.json` (manifest)
- `tasks/verdaccio.yaml` (config)

## Top-level layout

- `packages` — 318 analysed file(s)
- `test` — 78 analysed file(s)
- `docusaurus` — 55 analysed file(s)
- `(root files)` — 24 analysed file(s)
- `tasks` — 15 analysed file(s)
- `.github` — 11 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 4 file(s) were skipped during inventory (4 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `6254386531d263688ccfa542d0e628fbc0de0b28` is the revision these paths and observations refer to.
