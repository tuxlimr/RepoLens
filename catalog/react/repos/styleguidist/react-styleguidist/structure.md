# Project structure: styleguidist/react-styleguidist

**Analysed commit:** `c223f9a279f4e872cf6ff925fb21d2a7f6e27a77`

**Commit reference:** [c223f9a279f4e872cf6ff925fb21d2a7f6e27a77](https://github.com/styleguidist/react-styleguidist/commit/c223f9a279f4e872cf6ff925fb21d2a7f6e27a77)

**Tree at this commit:** [styleguidist/react-styleguidist@c223f9a279f4](https://github.com/styleguidist/react-styleguidist/tree/c223f9a279f4e872cf6ff925fb21d2a7f6e27a77)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | styleguidist/react-styleguidist |
| Description | Isolated React component development environment with a living style guide |
| Stars | 11048 |
| Forks | 1405 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `c223f9a279f4e872cf6ff925fb21d2a7f6e27a77` |
| Retrieved at | 2026-11-14T19:13:27.952144+00:00 |
| Files in this snapshot | 737 |

## Directory tree

```text
.github/  (13 files)
  ISSUE_TEMPLATE/  (4 files)
    Bug_report.md
    Feature_request.md
    Question.md
    Support.md
  workflows/  (4 files)
    coverage.yml
    danger-js.yml
    node.js.yml
    release.yml
  Code_of_Conduct.md
  Contributing.md
  FUNDING.yml
  Issue_Template.md
  stale.yml
docs/  (12 files)
  API.md
  CLI.md
  Components.md
  Configuration.md
  Cookbook.md
  Development.md
  Documenting.md
  GettingStarted.md
  Maintenance.md
  Readme.md
  Thirdparties.md
  Webpack.md
examples/  (204 files)
  basic/  (28 files)
    src/  (24 files)
      … 24 files under this directory
    Readme.md
    babel.config.js
    package.json
    styleguide.config.js
  cra/  (19 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (15 files)
      … 15 files under this directory
    Readme.md
    package.json
    styleguide.config.js
  customised/  (23 files)
    src/  (15 files)
      … 15 files under this directory
    styleguide/  (4 files)
      … 4 files under this directory
    Readme.md
    babel.config.js
    package.json
    styleguide.config.js
  express/  (7 files)
    src/  (3 files)
      … 3 files under this directory
    Readme.md
    babel.config.js
    package.json
    styleguide.config.js
  preact/  (26 files)
    src/  (22 files)
      … 22 files under this directory
    Readme.md
    babel.config.js
    package.json
    styleguide.config.js
  react-native/  (13 files)
    src/  (4 files)
      … 4 files under this directory
    .editorconfig
    .gitignore
    .watchmanconfig
    App.js
    README.md
    app.json
    babel.config.js
    package.json
    styleguide.config.js
  sections/  (37 files)
    docs/  (5 files)
      … 5 files under this directory
    src/  (27 files)
      … 27 files under this directory
    styleguide/  (1 files)
      … 1 files under this directory
    Readme.md
    babel.config.js
    package.json
    styleguide.config.js
  styled-components/  (17 files)
    src/  (12 files)
      … 12 files under this directory
    Readme.md
    babel.config.js
    package.json
    styleguide.config.js
    tsconfig.json
  themed/  (13 files)
    src/  (7 files)
      … 7 files under this directory
    Readme.md
    babel.config.js
    package.json
    styleguide.config.js
    styleguide.styles.js
    styleguide.theme.js
  webpack/  (20 files)
    src/  (15 files)
      … 15 files under this directory
    Readme.md
    babel.config.js
    package.json
    styleguide.config.js
    webpack.config.js
  .eslintrc
site/  (35 files)
  scripts/  (2 files)
    deploy.sh
    sync.js
  src/  (23 files)
    components/  (14 files)
      … 14 files under this directory
    css/  (1 files)
      … 1 files under this directory
    pages/  (4 files)
      … 4 files under this directory
    plugins/  (1 files)
      … 1 files under this directory
    theme/  (2 files)
      … 2 files under this directory
    .eslintrc.json
  static/  (2 files)
    img/  (2 files)
      … 2 files under this directory
  .eslintrc.json
  .gitignore
  CNAME
  Readme.md
  docusaurus.config.js
  package.json
  remark.js
  sidebars.js
src/  (413 files)
  bin/  (3 files)
    __tests__/  (1 files)
      … 1 files under this directory
    .eslintrc
    styleguidist.js
  client/  (284 files)
    rsg-components/  (226 files)
      … 226 files under this directory
    styles/  (9 files)
      … 9 files under this directory
    utils/  (46 files)
      … 46 files under this directory
    consts.ts
    index.ts
    polyfills.ts
  loaders/  (66 files)
    __tests__/  (3 files)
      … 3 files under this directory
    utils/  (60 files)
      … 60 files under this directory
    examples-loader.ts
    props-loader.ts
    styleguide-loader.ts
  scripts/  (35 files)
    __mocks__/  (2 files)
      … 2 files under this directory
    __tests__/  (7 files)
      … 7 files under this directory
    schemas/  (1 files)
      … 1 files under this directory
    utils/  (16 files)
      … 16 files under this directory
    build.ts
    config.ts
    consts.ts
    create-server.ts
    index.esm.ts
    index.ts
    logger.ts
    make-webpack-config.ts
    server.ts
  typings/  (25 files)
    dependencies/  (15 files)
      … 15 files under this directory
    RecursivePartial.ts
    RsgComponent.ts
    RsgExample.ts
    RsgPropsObject.ts
    RsgRequireItResult.ts
    RsgSection.ts
    RsgStyleguidistConfig.ts
    RsgTheme.ts
    index.ts
    test.Classes.d.ts
templates/  (1 files)
  DefaultExample.md
test/  (42 files)
  apps/  (11 files)
    basic/  (3 files)
      … 3 files under this directory
    cra/  (1 files)
      … 1 files under this directory
    defaults/  (5 files)
      … 5 files under this directory
    no-webpack/  (2 files)
      … 2 files under this directory
  components/  (12 files)
    Annotation/  (1 files)
      … 1 files under this directory
    Button/  (2 files)
      … 2 files under this directory
    Label/  (2 files)
      … 2 files under this directory
    Placeholder/  (4 files)
      … 4 files under this directory
    Price/  (1 files)
      … 1 files under this directory
    RandomButton/  (1 files)
      … 1 files under this directory
    .eslintrc
  cypress/  (7 files)
    fixtures/  (1 files)
      … 1 files under this directory
    integration/  (2 files)
      … 2 files under this directory
    plugins/  (1 files)
      … 1 files under this directory
    support/  (2 files)
      … 2 files under this directory
    .eslintrc
  data/  (4 files)
    badconfig.config.js
    styleguide.config.js
    webpack.config.func.js
    webpack.config.js
  browser.js
  classes.js
  deabsdeepSerializer.js
  empty.js
  jestsetup.js
  raf-polyfill.js
  run.build.js
  run.server.js
.editorconfig
.eslintignore
.eslintrc
.gitignore
.npmignore
.nvmrc
.prettierignore
.prettierrc
License.md
Readme.md
babel.config.js
cypress.json
dangerfile.ts
package.json
styleguide.config.js
tsconfig.json
tsconfig.types.json
```

## Entry points

- [site/src/pages/index.js](https://github.com/styleguidist/react-styleguidist/blob/c223f9a279f4e872cf6ff925fb21d2a7f6e27a77/site/src/pages/index.js)
- [src/client/index.ts](https://github.com/styleguidist/react-styleguidist/blob/c223f9a279f4e872cf6ff925fb21d2a7f6e27a77/src/client/index.ts)
- [src/client/styles/index.ts](https://github.com/styleguidist/react-styleguidist/blob/c223f9a279f4e872cf6ff925fb21d2a7f6e27a77/src/client/styles/index.ts)
- [src/scripts/__mocks__/server.ts](https://github.com/styleguidist/react-styleguidist/blob/c223f9a279f4e872cf6ff925fb21d2a7f6e27a77/src/scripts/__mocks__/server.ts)
- [src/scripts/index.ts](https://github.com/styleguidist/react-styleguidist/blob/c223f9a279f4e872cf6ff925fb21d2a7f6e27a77/src/scripts/index.ts)
- [src/scripts/server.ts](https://github.com/styleguidist/react-styleguidist/blob/c223f9a279f4e872cf6ff925fb21d2a7f6e27a77/src/scripts/server.ts)
- [src/typings/index.ts](https://github.com/styleguidist/react-styleguidist/blob/c223f9a279f4e872cf6ff925fb21d2a7f6e27a77/src/typings/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bin package | library | Observed | Groups 2 file(s) under bin package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 246 file(s) under external integrations (observed from repository paths and static analysis). |
| loaders package | library | Observed | Groups 51 file(s) under loaders package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 34 file(s) under scripts package (observed from repository paths and static analysis). |
| site package | library | Observed | Groups 16 file(s) under site package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 42 file(s) under tests (observed from repository paths and static analysis). |
| typings package | library | Observed | Groups 25 file(s) under typings package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/stale.yml` (config)
- `.github/workflows/coverage.yml` (ci)
- `.github/workflows/danger-js.yml` (ci)
- `.github/workflows/node.js.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `cypress.json` (config)
- `examples/basic/package.json` (manifest)
- `examples/cra/package.json` (manifest)
- `examples/customised/package.json` (manifest)
- `examples/customised/src/components/Button/Button.json` (config)
- `examples/customised/src/components/Placeholder/Placeholder.json` (config)
- `examples/customised/src/components/RandomButton/RandomButton.json` (config)
- `examples/express/package.json` (manifest)
- `examples/preact/package.json` (manifest)
- `examples/react-native/.editorconfig` (config)
- `examples/react-native/app.json` (config)
- `examples/react-native/package.json` (manifest)
- `examples/sections/package.json` (manifest)
- `examples/styled-components/package.json` (manifest)
- `examples/styled-components/tsconfig.json` (config)
- `examples/themed/package.json` (manifest)
- `examples/webpack/package.json` (manifest)
- `package.json` (manifest)
- `site/.eslintrc.json` (config)
- `site/package.json` (manifest)
- `site/src/.eslintrc.json` (config)
- `tsconfig.json` (config)
- `tsconfig.types.json` (config)

## Top-level layout

- `src` — 413 analysed file(s)
- `examples` — 204 analysed file(s)
- `test` — 42 analysed file(s)
- `site` — 35 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `.github` — 13 analysed file(s)
- `docs` — 12 analysed file(s)
- `templates` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `c223f9a279f4e872cf6ff925fb21d2a7f6e27a77` is the revision these paths and observations refer to.
