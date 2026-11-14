# Project structure: pedronauck/docz

**Analysed commit:** `e0a53cb64fa8bb7a9e02f4f39eada7f74566dd3c`

**Commit reference:** [e0a53cb64fa8bb7a9e02f4f39eada7f74566dd3c](https://github.com/pedronauck/docz/commit/e0a53cb64fa8bb7a9e02f4f39eada7f74566dd3c)

**Tree at this commit:** [pedronauck/docz@e0a53cb64fa8](https://github.com/pedronauck/docz/tree/e0a53cb64fa8bb7a9e02f4f39eada7f74566dd3c)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | pedronauck/docz |
| Description | ✍ It has never been so easy to document your things! |
| Stars | 23555 |
| Forks | 1396 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `e0a53cb64fa8bb7a9e02f4f39eada7f74566dd3c` |
| Retrieved at | 2026-11-14T19:13:06.862071+00:00 |
| Files in this snapshot | 675 |

## Directory tree

```text
.circleci/  (1 files)
  config.yml
.github/  (6 files)
  ISSUE_TEMPLATE/  (3 files)
    ---bug-report.md
    ---feature-request.md
    ---support-question.md
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
  stale.yml
.vscode/  (2 files)
  launch.json
  settings.json
core/  (227 files)
  docz/  (31 files)
    bin/  (1 files)
      … 1 files under this directory
    src/  (20 files)
      … 20 files under this directory
    .babelrc
    .eslintignore
    .eslintrc.js
    .lintstagedrc
    CHANGELOG.md
    LICENSE.md
    README.md
    package.json
    rollup.config.js
    tsconfig.json
  docz-core/  (73 files)
    __fixtures__/  (4 files)
      … 4 files under this directory
    __tests__/  (4 files)
      … 4 files under this directory
    bin/  (1 files)
      … 1 files under this directory
    src/  (46 files)
      … 46 files under this directory
    templates/  (7 files)
      … 7 files under this directory
    .babelrc
    .eslintignore
    .eslintrc.js
    .lintstagedrc
    CHANGELOG.md
    LICENSE.md
    README.md
    nodemon.json
    package.json
    rollup.config.js
    tsconfig.json
  docz-rollup/  (10 files)
    src/  (4 files)
      … 4 files under this directory
    .eslintrc.js
    .lintstagedrc
    CHANGELOG.md
    LICENSE.md
    README.md
    package.json
  docz-utils/  (20 files)
    __tests__/  (1 files)
      … 1 files under this directory
    src/  (9 files)
      … 9 files under this directory
    .babelrc
    .eslintignore
    .eslintrc.js
    .lintstagedrc
    CHANGELOG.md
    LICENSE.md
    README.md
    package.json
    rollup.config.js
    tsconfig.json
  gatsby-theme-docz/  (65 files)
    lib/  (8 files)
      … 8 files under this directory
    src/  (45 files)
      … 45 files under this directory
    .eslintrc.js
    .gitignore
    .lintstagedrc
    CHANGELOG.md
    LICENSE.md
    README.md
    gatsby-browser.js
    gatsby-config.js
    gatsby-node.js
    gatsby-ssr.js
    index.js
    package.json
  rehype-docz/  (14 files)
    src/  (4 files)
      … 4 files under this directory
    .eslintignore
    .eslintrc.js
    .lintstagedrc
    CHANGELOG.md
    LICENSE.md
    README.md
    jest.config.js
    package.json
    rollup.config.js
    tsconfig.json
  remark-docz/  (14 files)
    src/  (4 files)
      … 4 files under this directory
    .eslintignore
    .eslintrc.js
    .lintstagedrc
    CHANGELOG.md
    LICENSE.md
    README.md
    jest.config.js
    package.json
    rollup.config.js
    tsconfig.json
dev-env/  (9 files)
  basic/  (9 files)
    src/  (3 files)
      … 3 files under this directory
    .eslintrc
    .gitignore
    CHANGELOG.md
    README.md
    doczrc.js
    package.json
examples/  (354 files)
  basic/  (6 files)
    src/  (3 files)
      … 3 files under this directory
    .gitignore
    README.md
    package.json
  create-react-app/  (16 files)
    public/  (3 files)
      … 3 files under this directory
    src/  (10 files)
      … 10 files under this directory
    .gitignore
    README.md
    package.json
  create-react-app-ts/  (20 files)
    public/  (3 files)
      … 3 files under this directory
    src/  (12 files)
      … 12 files under this directory
    .gitignore
    README.md
    doczrc.js
    package.json
    tsconfig.json
  custom-base-path/  (7 files)
    src/  (3 files)
      … 3 files under this directory
    .gitignore
    README.md
    doczrc.js
    package.json
  custom-config-location/  (7 files)
    src/  (4 files)
      … 4 files under this directory
    .gitignore
    README.md
    package.json
  flow/  (11 files)
    src/  (5 files)
      … 5 files under this directory
    .babelrc
    .flowconfig
    .gitignore
    README.md
    gatsby-node.js
    package.json
  gatsby/  (11 files)
    src/  (6 files)
      … 6 files under this directory
    .gitignore
    README.md
    doczrc.js
    gatsby-config.js
    package.json
  images/  (6 files)
    src/  (2 files)
      … 2 files under this directory
    .gitignore
    README.md
    doczrc.js
    package.json
  less/  (9 files)
    src/  (4 files)
      … 4 files under this directory
    .gitignore
    README.md
    doczrc.js
    gatsby-config.js
    package.json
  logo-in-sidebar/  (8 files)
    src/  (5 files)
      … 5 files under this directory
    .gitignore
    README.md
    package.json
  material-ui/  (5 files)
    .gitignore
    README.md
    doczrc.js
    home.mdx
    package.json
  monorepo/  (10 files)
    packages/  (6 files)
      … 6 files under this directory
    .gitignore
    README.md
    lerna.json
    package.json
  monorepo-package/  (11 files)
    packages/  (7 files)
      … 7 files under this directory
    .gitignore
    README.md
    lerna.json
    package.json
  monorepo-separate-docs/  (23 files)
    packages/  (19 files)
      … 19 files under this directory
    .gitignore
    README.md
    lerna.json
    package.json
  now/  (10 files)
    src/  (5 files)
      … 5 files under this directory
    .gitignore
    README.md
    doczrc.js
    now.json
    package.json
  react-native/  (8 files)
    src/  (3 files)
      … 3 files under this directory
    .gitignore
    README.md
    doczrc.js
    gatsby-node.js
    package.json
  react-router/  (7 files)
    src/  (4 files)
      … 4 files under this directory
    .gitignore
    README.md
    package.json
  sass/  (9 files)
    src/  (4 files)
      … 4 files under this directory
    .gitignore
    README.md
    doczrc.js
    gatsby-config.js
    package.json
  shadowed-playground/  (8 files)
    src/  (4 files)
      … 4 files under this directory
    .gitignore
    README.md
    doczrc.js
    package.json
  styled-components/  (8 files)
    src/  (5 files)
      … 5 files under this directory
    .gitignore
    README.md
    package.json
  stylus/  (9 files)
    src/  (4 files)
      … 4 files under this directory
    .gitignore
    README.md
    doczrc.js
    gatsby-config.js
    package.json
  typescript/  (9 files)
    src/  (5 files)
      … 5 files under this directory
    README.md
    doczrc.js
    package.json
    tsconfig.json
  webpack-alias/  (8 files)
    src/  (3 files)
      … 3 files under this directory
    .gitignore
    README.md
    doczrc.js
    gatsby-node.js
    package.json
  with-algolia-search/  (31 files)
    src/  (26 files)
      … 26 files under this directory
    .env.example
    .gitignore
    README.md
    gatsby-config.js
    package.json
  with-custom-404-page/  (7 files)
    src/  (4 files)
      … 4 files under this directory
    .gitignore
    README.md
    package.json
  with-custom-docz-theme/  (11 files)
    gatsby-theme-docz-pink/  (3 files)
      … 3 files under this directory
    src/  (3 files)
      … 3 files under this directory
    .gitignore
    README.md
    doczrc.js
    gatsby-config.js
    package.json
  with-custom-links/  (5 files)
    src/  (2 files)
      … 2 files under this directory
    .gitignore
    README.md
    package.json
  with-decorators/  (10 files)
    src/  (4 files)
      … 4 files under this directory
    .gitignore
    README.md
    doczrc.js
    gatsby-node.js
    jsconfig.json
    package.json
  with-env-variables/  (9 files)
    src/  (3 files)
      … 3 files under this directory
    .gitignore
    README.md
    doczrc.js
    gatsby-config.js
    gatsby-node.js
    package.json
  with-favicon-and-metadata/  (7 files)
    src/  (4 files)
      … 4 files under this directory
    .gitignore
    README.md
    package.json
  with-gatsby-remark-vscode/  (8 files)
    src/  (4 files)
      … 4 files under this directory
    .gitignore
    README.md
    doczrc.js
    package.json
  with-styled-components-and-scoping/  (10 files)
    src/  (6 files)
      … 6 files under this directory
    .gitignore
    README.md
    doczrc.js
    package.json
  with-themes-dir/  (9 files)
    src/  (3 files)
      … 3 files under this directory
    theme/  (2 files)
      … 2 files under this directory
    .gitignore
    README.md
    doczrc.js
    package.json
  with-typescript-decorators/  (12 files)
    src/  (6 files)
      … 6 files under this directory
    .gitignore
    README.md
    doczrc.js
    gatsby-node.js
    package.json
    tsconfig.json
  wrapped-playground/  (8 files)
    src/  (4 files)
      … 4 files under this directory
    .gitignore
    README.md
    doczrc.js
    package.json
  .eslintrc
other-packages/  (59 files)
  babel-plugin-export-metadata/  (23 files)
    src/  (1 files)
      … 1 files under this directory
    tests/  (16 files)
      … 16 files under this directory
    .eslintrc.js
    .lintstagedrc
    CHANGELOG.md
    README.md
    jest.config.js
    package.json
  e2e-tests/  (8 files)
    __tests__/  (1 files)
      … 1 files under this directory
    .testcaferc.json
    CHANGELOG.md
    helpers.js
    index.js
    package.json
    testing-library.js
    verdaccio.yaml
  eslint-config-docz-js/  (4 files)
    CHANGELOG.md
    README.md
    index.js
    package.json
  eslint-config-docz-ts/  (4 files)
    CHANGELOG.md
    README.md
    index.js
    package.json
  load-cfg/  (10 files)
    src/  (2 files)
      … 2 files under this directory
    .eslintignore
    .eslintrc.js
    .lintstagedrc
    CHANGELOG.md
    README.md
    package.json
    rollup.config.js
    tsconfig.json
  react-docgen-actual-name-handler/  (10 files)
    src/  (2 files)
      … 2 files under this directory
    .eslintignore
    .eslintrc.js
    .lintstagedrc
    CHANGELOG.md
    README.md
    package.json
    rollup.config.js
    tsconfig.json
.all-contributorsrc
.commitlintrc.json
.editorconfig
.eslintignore
.gitignore
.huskyrc
.prettierignore
.prettierrc
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE.md
MIGRATION_GUIDE.md
README.md
lerna.json
package.json
tsconfig.json
```

## Entry points

- [core/docz-rollup/src/index.js](https://github.com/pedronauck/docz/blob/e0a53cb64fa8bb7a9e02f4f39eada7f74566dd3c/core/docz-rollup/src/index.js)
- [core/docz/bin/index.js](https://github.com/pedronauck/docz/blob/e0a53cb64fa8bb7a9e02f4f39eada7f74566dd3c/core/docz/bin/index.js)
- [examples/monorepo-separate-docs/packages/alert/index.js](https://github.com/pedronauck/docz/blob/e0a53cb64fa8bb7a9e02f4f39eada7f74566dd3c/examples/monorepo-separate-docs/packages/alert/index.js)
- [examples/with-custom-docz-theme/gatsby-theme-docz-pink/index.js](https://github.com/pedronauck/docz/blob/e0a53cb64fa8bb7a9e02f4f39eada7f74566dd3c/examples/with-custom-docz-theme/gatsby-theme-docz-pink/index.js)
- [other-packages/babel-plugin-export-metadata/src/index.js](https://github.com/pedronauck/docz/blob/e0a53cb64fa8bb7a9e02f4f39eada7f74566dd3c/other-packages/babel-plugin-export-metadata/src/index.js)
- [other-packages/e2e-tests/index.js](https://github.com/pedronauck/docz/blob/e0a53cb64fa8bb7a9e02f4f39eada7f74566dd3c/other-packages/e2e-tests/index.js)
- [other-packages/eslint-config-docz-js/index.js](https://github.com/pedronauck/docz/blob/e0a53cb64fa8bb7a9e02f4f39eada7f74566dd3c/other-packages/eslint-config-docz-js/index.js)
- [other-packages/eslint-config-docz-ts/index.js](https://github.com/pedronauck/docz/blob/e0a53cb64fa8bb7a9e02f4f39eada7f74566dd3c/other-packages/eslint-config-docz-ts/index.js)
- [core/docz-core/bin/index.js](https://github.com/pedronauck/docz/blob/e0a53cb64fa8bb7a9e02f4f39eada7f74566dd3c/core/docz-core/bin/index.js)
- [core/docz-core/src/index.ts](https://github.com/pedronauck/docz/blob/e0a53cb64fa8bb7a9e02f4f39eada7f74566dd3c/core/docz-core/src/index.ts)
- [core/docz-utils/src/index.ts](https://github.com/pedronauck/docz/blob/e0a53cb64fa8bb7a9e02f4f39eada7f74566dd3c/core/docz-utils/src/index.ts)
- [core/docz/src/index.ts](https://github.com/pedronauck/docz/blob/e0a53cb64fa8bb7a9e02f4f39eada7f74566dd3c/core/docz/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 31 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| dev-env package | library | Observed | Groups 2 file(s) under dev-env package (observed from repository paths and static analysis). |
| other-packages package | library | Observed | Groups 17 file(s) under other-packages package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 167 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 16 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.circleci/config.yml` (ci)
- `.commitlintrc.json` (config)
- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/stale.yml` (config)
- `.vscode/launch.json` (config)
- `.vscode/settings.json` (config)
- `core/docz-core/nodemon.json` (config)
- `core/docz-core/package.json` (manifest)
- `core/docz-core/tsconfig.json` (config)
- `core/docz-rollup/package.json` (manifest)
- `core/docz-utils/package.json` (manifest)
- `core/docz-utils/tsconfig.json` (config)
- `core/docz/package.json` (manifest)
- `core/docz/tsconfig.json` (config)
- `core/gatsby-theme-docz/package.json` (manifest)
- `core/rehype-docz/package.json` (manifest)
- `core/rehype-docz/tsconfig.json` (config)
- `core/remark-docz/package.json` (manifest)
- `core/remark-docz/tsconfig.json` (config)
- `dev-env/basic/package.json` (manifest)
- `examples/basic/package.json` (manifest)
- `examples/create-react-app-ts/package.json` (manifest)
- `examples/create-react-app-ts/public/manifest.json` (config)
- `examples/create-react-app-ts/tsconfig.json` (config)
- `examples/create-react-app/package.json` (manifest)
- `examples/create-react-app/public/manifest.json` (config)
- `examples/custom-base-path/package.json` (manifest)
- `examples/custom-config-location/package.json` (manifest)
- `examples/flow/package.json` (manifest)
- `examples/gatsby/package.json` (manifest)
- `examples/images/package.json` (manifest)
- `examples/less/package.json` (manifest)
- `examples/logo-in-sidebar/package.json` (manifest)
- `examples/material-ui/package.json` (manifest)
- `examples/monorepo-package/lerna.json` (config)
- `examples/monorepo-package/package.json` (manifest)
- `examples/monorepo-package/packages/basic/package.json` (manifest)
- `examples/monorepo-separate-docs/lerna.json` (config)
- `examples/monorepo-separate-docs/package.json` (manifest)
- `examples/monorepo-separate-docs/packages/alert-ts/package.json` (manifest)
- `examples/monorepo-separate-docs/packages/alert-ts/tsconfig.json` (config)
- `examples/monorepo-separate-docs/packages/alert/package.json` (manifest)
- `examples/monorepo-separate-docs/packages/docs/package.json` (manifest)
- `examples/monorepo-separate-docs/packages/docs/tsconfig.json` (config)
- `examples/monorepo/lerna.json` (config)
- `examples/monorepo/package.json` (manifest)
- `examples/monorepo/packages/basic/package.json` (manifest)
- `examples/now/now.json` (config)
- `examples/now/package.json` (manifest)
- `examples/react-native/package.json` (manifest)
- `examples/react-router/package.json` (manifest)
- `examples/sass/package.json` (manifest)
- `examples/shadowed-playground/package.json` (manifest)
- `examples/styled-components/package.json` (manifest)
- `examples/stylus/package.json` (manifest)
- `examples/typescript/package.json` (manifest)
- `examples/typescript/tsconfig.json` (config)
- `examples/webpack-alias/package.json` (manifest)
- `examples/with-algolia-search/.env.example` (config)
- `examples/with-algolia-search/package.json` (manifest)
- `examples/with-custom-404-page/package.json` (manifest)
- `examples/with-custom-docz-theme/gatsby-theme-docz-pink/package.json` (manifest)
- `examples/with-custom-docz-theme/package.json` (manifest)
- `examples/with-custom-links/package.json` (manifest)
- `examples/with-decorators/jsconfig.json` (config)
- `examples/with-decorators/package.json` (manifest)
- `examples/with-env-variables/package.json` (manifest)
- `examples/with-favicon-and-metadata/package.json` (manifest)
- `examples/with-gatsby-remark-vscode/package.json` (manifest)
- `examples/with-styled-components-and-scoping/package.json` (manifest)
- `examples/with-themes-dir/package.json` (manifest)
- `examples/with-typescript-decorators/package.json` (manifest)
- `examples/with-typescript-decorators/tsconfig.json` (config)
- `examples/wrapped-playground/package.json` (manifest)
- `lerna.json` (config)
- `other-packages/babel-plugin-export-metadata/package.json` (manifest)
- `other-packages/e2e-tests/.testcaferc.json` (config)
- `other-packages/e2e-tests/package.json` (manifest)
- `other-packages/e2e-tests/verdaccio.yaml` (config)
- `other-packages/eslint-config-docz-js/package.json` (manifest)
- `other-packages/eslint-config-docz-ts/package.json` (manifest)
- `other-packages/load-cfg/package.json` (manifest)
- `other-packages/load-cfg/tsconfig.json` (config)
- `other-packages/react-docgen-actual-name-handler/package.json` (manifest)
- `other-packages/react-docgen-actual-name-handler/tsconfig.json` (config)
- `package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `examples` — 354 analysed file(s)
- `core` — 227 analysed file(s)
- `other-packages` — 59 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `dev-env` — 9 analysed file(s)
- `.github` — 6 analysed file(s)
- `.vscode` — 2 analysed file(s)
- `.circleci` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `e0a53cb64fa8bb7a9e02f4f39eada7f74566dd3c` is the revision these paths and observations refer to.
