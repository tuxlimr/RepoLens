# Project structure: jaredpalmer/razzle

**Analysed commit:** `54724b7bb810d06bb418951ada3f90ae3f135668`

**Commit reference:** [54724b7bb810d06bb418951ada3f90ae3f135668](https://github.com/jaredpalmer/razzle/commit/54724b7bb810d06bb418951ada3f90ae3f135668)

**Tree at this commit:** [jaredpalmer/razzle@54724b7bb810](https://github.com/jaredpalmer/razzle/tree/54724b7bb810d06bb418951ada3f90ae3f135668)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | jaredpalmer/razzle |
| Description | ✨ Create server-rendered universal JavaScript applications with no configuration |
| Stars | 11019 |
| Forks | 840 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `54724b7bb810d06bb418951ada3f90ae3f135668` |
| Retrieved at | 2026-11-14T19:13:28.398584+00:00 |
| Files in this snapshot | 788 |

## Directory tree

```text
.changeset/  (1 files)
  config.json
.github/  (15 files)
  ISSUE_TEMPLATE/  (4 files)
    Bug_report.md
    Documentation.md
    Feature_request.md
    Question.md
  workflows/  (6 files)
    examples.yml
    examples_node14.yml
    label.yml
    nodejs.yml
    release.yml
    test-examples.yml
  CODE_OF_CONDUCT.md
  CONTRIBUTING.md
  FUNDING.yml
  labels.yml
  stale.yml
examples/  (745 files)
  basic/  (11 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (6 files)
      … 6 files under this directory
    README.md
    gitignore
    package.json
    sandbox.config.json
  basic-server/  (11 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (5 files)
      … 5 files under this directory
    README.md
    gitignore
    package.json
    razzle.config.js
    sandbox.config.json
  basic-serverless/  (12 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (6 files)
      … 6 files under this directory
    README.md
    gitignore
    package.json
    razzle.config.js
    sandbox.config.json
  basic-spa/  (10 files)
    public/  (2 files)
      … 2 files under this directory
    src/  (4 files)
      … 4 files under this directory
    .gitignore
    README.md
    package.json
    razzle.config.js
  with-afterjs/  (1 files)
    README.md
  with-custom-babel-config/  (10 files)
    src/  (5 files)
      … 5 files under this directory
    .babelrc
    .gitignore
    README.md
    package.json
    razzle.config.js
  with-custom-devserver-options/  (9 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (4 files)
      … 4 files under this directory
    .gitignore
    README.md
    package.json
    razzle.config.js
  with-custom-environment-variables/  (8 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (4 files)
      … 4 files under this directory
    .gitignore
    README.md
    package.json
  with-custom-target-babel-config/  (11 files)
    src/  (5 files)
      … 5 files under this directory
    .babelrc.node
    .babelrc.web
    .gitignore
    README.md
    package.json
    razzle.config.js
  with-custom-webpack-config/  (9 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (4 files)
      … 4 files under this directory
    .gitignore
    README.md
    package.json
    razzle.config.js
  with-devcert-https/  (10 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (5 files)
      … 5 files under this directory
    .gitignore
    README.md
    package.json
    razzle.config.js
  with-development-build/  (11 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (6 files)
      … 6 files under this directory
    README.md
    gitignore
    package.json
    sandbox.config.json
  with-elm/  (11 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (5 files)
      … 5 files under this directory
    .gitignore
    README.md
    elm-package.json
    package.json
    razzle.config.js
  with-esbuild-loader/  (17 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (9 files)
      … 9 files under this directory
    typings/  (1 files)
      … 1 files under this directory
    .eslintrc.js
    .gitignore
    README.md
    package.json
    razzle.config.js
    tsconfig.json
  with-eslint/  (13 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (6 files)
      … 6 files under this directory
    .eslintrc.json
    .gitignore
    README.md
    package.json
    razzle.config.js
    sandbox.config.json
  with-experimental-refresh/  (12 files)
    src/  (9 files)
      … 9 files under this directory
    README.md
    package.json
    razzle.config.js
  with-fastify/  (16 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (10 files)
      … 10 files under this directory
    typings/  (1 files)
      … 1 files under this directory
    .gitignore
    README.md
    package.json
    tsconfig.json
  with-firebase-functions/  (14 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (6 files)
      … 6 files under this directory
    .firebaserc
    .gitignore
    README.md
    firebase.json
    index.js
    package.json
    razzle.config.js
  with-heroku/  (12 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (6 files)
      … 6 files under this directory
    .gitignore
    Procfile
    README.md
    package.json
    razzle.config.js
  with-hyperapp/  (14 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (9 files)
      … 9 files under this directory
    .babelrc
    .gitignore
    README.md
    package.json
  with-inferno/  (11 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (5 files)
      … 5 files under this directory
    .babelrc
    .eslintrc
    .gitignore
    README.md
    package.json
  with-jest-snapshots/  (13 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (9 files)
      … 9 files under this directory
    .gitignore
    README.md
    package.json
  with-jsconfig-paths/  (13 files)
    here-is-extra/  (1 files)
      … 1 files under this directory
    public/  (1 files)
      … 1 files under this directory
    src/  (6 files)
      … 6 files under this directory
    .gitignore
    README.md
    jsconfig.json
    package.json
    sandbox.config.json
  with-jsxstyle/  (12 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (8 files)
      … 8 files under this directory
    .gitignore
    README.md
    package.json
  with-koa/  (11 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (8 files)
      … 8 files under this directory
    README.md
    package.json
  with-less/  (12 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (7 files)
      … 7 files under this directory
    .gitignore
    README.md
    package.json
    razzle.config.js
  with-loadable-components/  (17 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (11 files)
      … 11 files under this directory
    .babelrc
    .gitignore
    README.md
    package.json
    razzle.config.js
  with-material-ui/  (10 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (7 files)
      … 7 files under this directory
    README.md
    package.json
  with-mdx/  (9 files)
    src/  (5 files)
      … 5 files under this directory
    .gitignore
    README.md
    package.json
    razzle.config.js
  with-module-federation/  (19 files)
    basic-1/  (8 files)
      … 8 files under this directory
    basic-2/  (8 files)
      … 8 files under this directory
    .gitignore
    README.md
    package.json
  with-monorepo/  (19 files)
    basic-1/  (8 files)
      … 8 files under this directory
    basic-2/  (8 files)
      … 8 files under this directory
    .gitignore
    README.md
    package.json
  with-monorepo-without-workspaces/  (17 files)
    basic-1/  (7 files)
      … 7 files under this directory
    basic-2/  (7 files)
      … 7 files under this directory
    .gitignore
    README.md
    package.json
  with-now/  (10 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (6 files)
      … 6 files under this directory
    .gitignore
    README.md
    package.json
  with-now-v2/  (11 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (6 files)
      … 6 files under this directory
    .gitignore
    README.md
    now.json
    package.json
  with-polka/  (10 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (6 files)
      … 6 files under this directory
    .gitignore
    README.md
    package.json
  with-preact/  (11 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (5 files)
      … 5 files under this directory
    .babelrc
    .gitignore
    README.md
    package.json
    razzle.config.js
  with-promise-config/  (9 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (4 files)
      … 4 files under this directory
    .gitignore
    README.md
    package.json
    razzle.config.js
  with-react-native-web/  (9 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (4 files)
      … 4 files under this directory
    .babelrc
    README.md
    package.json
    razzle.config.js
  with-react-router/  (13 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (9 files)
      … 9 files under this directory
    .gitignore
    README.md
    package.json
  with-react-server-components/  (53 files)
    notes/  (5 files)
      … 5 files under this directory
    plugin/  (13 files)
      … 13 files under this directory
    public/  (8 files)
      … 8 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    src/  (20 files)
      … 20 files under this directory
    .gitignore
    README.md
    babel.config.js
    package.json
    razzle.config.js
    sandbox.config.json
  with-reason-react/  (25 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (19 files)
      … 19 files under this directory
    .gitignore
    README.md
    bsconfig.json
    jsconfig.json
    package.json
  with-redux/  (14 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (10 files)
      … 10 files under this directory
    .gitignore
    README.md
    package.json
  with-scss/  (13 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (8 files)
      … 8 files under this directory
    .gitignore
    README.md
    package.json
    razzle.config.js
  with-scss-options/  (14 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (9 files)
      … 9 files under this directory
    .gitignore
    README.md
    package.json
    razzle.config.js
  with-single-exposed-port/  (9 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (4 files)
      … 4 files under this directory
    .gitignore
    README.md
    package.json
    razzle.config.js
  with-styled-components/  (10 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (6 files)
      … 6 files under this directory
    .gitignore
    README.md
    package.json
  with-svelte/  (12 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (6 files)
      … 6 files under this directory
    .gitignore
    README.md
    package.json
    razzle.config.js
    sandbox.config.json
  with-tailwindcss/  (12 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (6 files)
      … 6 files under this directory
    .gitignore
    README.md
    package.json
    razzle.config.js
    sandbox.config.json
  with-typeorm-graphql/  (28 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (19 files)
      … 19 files under this directory
    .babelrc
    .eslintrc.js
    .gitignore
    .prettierrc
    README.md
    package.json
    razzle.config.js
    tsconfig.json
  with-typescript/  (16 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (11 files)
      … 11 files under this directory
    .gitignore
    README.md
    package.json
    tsconfig.json
  with-typescript-plugin/  (17 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (9 files)
      … 9 files under this directory
    typings/  (1 files)
      … 1 files under this directory
    .eslintrc.js
    .gitignore
    README.md
    package.json
    razzle.config.js
    tsconfig.json
  with-vendor-bundle/  (9 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (4 files)
      … 4 files under this directory
    .gitignore
    README.md
    package.json
    razzle.config.js
  with-vue/  (12 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (6 files)
      … 6 files under this directory
    .eslintrc
    .gitignore
    README.md
    package.json
    razzle.config.js
  with-vue-router/  (16 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (10 files)
      … 10 files under this directory
    .eslintrc
    .gitignore
    README.md
    package.json
    razzle.config.js
  with-webpack-dev-server-v4/  (12 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (6 files)
      … 6 files under this directory
    README.md
    gitignore
    package.json
    razzle.config.js
    sandbox.config.json
  with-webpack-public-path/  (14 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (10 files)
      … 10 files under this directory
    README.md
    package.json
    sandbox.config.json
  .gitignore
packages/  (18 files)
  babel-preset-razzle/  (9 files)
    babel-plugins/  (4 files)
      … 4 files under this directory
    CHANGELOG.md
    LICENSE
    README.md
    index.js
    package.json
  create-razzle-app/  (9 files)
    bin/  (1 files)
      … 1 files under this directory
    lib/  (4 files)
      … 4 files under this directory
    .gitignore
    CHANGELOG.md
    README.md
    index.js
.all-contributorsrc
.eslintignore
.eslintrc
.gitignore
.prettierrc
LICENSE
lerna.json
package.json
package.meta.json
```

## Entry points

- [packages/babel-preset-razzle/index.js](https://github.com/jaredpalmer/razzle/blob/54724b7bb810d06bb418951ada3f90ae3f135668/packages/babel-preset-razzle/index.js)
- [packages/create-razzle-app/index.js](https://github.com/jaredpalmer/razzle/blob/54724b7bb810d06bb418951ada3f90ae3f135668/packages/create-razzle-app/index.js)
- [packages/create-razzle-app/lib/index.js](https://github.com/jaredpalmer/razzle/blob/54724b7bb810d06bb418951ada3f90ae3f135668/packages/create-razzle-app/lib/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Inferred | Groups 0 file(s) under data layer (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 10 file(s) under packages package (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/labels.yml` (config)
- `.github/stale.yml` (config)
- `.github/workflows/examples.yml` (ci)
- `.github/workflows/examples_node14.yml` (ci)
- `.github/workflows/label.yml` (ci)
- `.github/workflows/nodejs.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/test-examples.yml` (ci)
- `examples/basic-server/package.json` (manifest)
- `examples/basic-server/sandbox.config.json` (config)
- `examples/basic-serverless/package.json` (manifest)
- `examples/basic-serverless/sandbox.config.json` (config)
- `examples/basic-spa/package.json` (manifest)
- `examples/basic/package.json` (manifest)
- `examples/basic/sandbox.config.json` (config)
- `examples/with-custom-babel-config/package.json` (manifest)
- `examples/with-custom-devserver-options/package.json` (manifest)
- `examples/with-custom-environment-variables/package.json` (manifest)
- `examples/with-custom-target-babel-config/package.json` (manifest)
- `examples/with-custom-webpack-config/package.json` (manifest)
- `examples/with-devcert-https/package.json` (manifest)
- `examples/with-development-build/package.json` (manifest)
- `examples/with-development-build/sandbox.config.json` (config)
- `examples/with-elm/elm-package.json` (config)
- `examples/with-elm/package.json` (manifest)
- `examples/with-esbuild-loader/package.json` (manifest)
- `examples/with-esbuild-loader/tsconfig.json` (config)
- `examples/with-eslint/.eslintrc.json` (config)
- `examples/with-eslint/package.json` (manifest)
- `examples/with-eslint/sandbox.config.json` (config)
- `examples/with-experimental-refresh/package.json` (manifest)
- `examples/with-fastify/package.json` (manifest)
- `examples/with-fastify/tsconfig.json` (config)
- `examples/with-firebase-functions/firebase.json` (config)
- `examples/with-firebase-functions/package.json` (manifest)
- `examples/with-heroku/package.json` (manifest)
- `examples/with-hyperapp/package.json` (manifest)
- `examples/with-inferno/package.json` (manifest)
- `examples/with-jest-snapshots/package.json` (manifest)
- `examples/with-jsconfig-paths/jsconfig.json` (config)
- `examples/with-jsconfig-paths/package.json` (manifest)
- `examples/with-jsconfig-paths/sandbox.config.json` (config)
- `examples/with-jsxstyle/package.json` (manifest)
- `examples/with-koa/package.json` (manifest)
- `examples/with-less/package.json` (manifest)
- `examples/with-loadable-components/package.json` (manifest)
- `examples/with-material-ui/package.json` (manifest)
- `examples/with-mdx/package.json` (manifest)
- `examples/with-module-federation/basic-1/package.json` (manifest)
- `examples/with-module-federation/basic-2/package.json` (manifest)
- `examples/with-module-federation/package.json` (manifest)
- `examples/with-monorepo-without-workspaces/package.json` (manifest)
- `examples/with-monorepo/basic-1/package.json` (manifest)
- `examples/with-monorepo/basic-2/package.json` (manifest)
- `examples/with-monorepo/package.json` (manifest)
- `examples/with-now-v2/now.json` (config)
- `examples/with-now-v2/package.json` (manifest)
- `examples/with-now/package.json` (manifest)
- `examples/with-polka/package.json` (manifest)
- `examples/with-preact/package.json` (manifest)
- `examples/with-promise-config/package.json` (manifest)
- `examples/with-react-native-web/package.json` (manifest)
- `examples/with-react-router/package.json` (manifest)
- `examples/with-react-server-components/package.json` (manifest)
- `examples/with-react-server-components/plugin/__tests__/fixture/package.json` (manifest)
- `examples/with-react-server-components/sandbox.config.json` (config)
- `examples/with-reason-react/bsconfig.json` (config)
- `examples/with-reason-react/jsconfig.json` (config)
- `examples/with-reason-react/package.json` (manifest)
- `examples/with-redux/package.json` (manifest)
- `examples/with-scss-options/package.json` (manifest)
- `examples/with-scss/package.json` (manifest)
- `examples/with-single-exposed-port/package.json` (manifest)
- `examples/with-styled-components/package.json` (manifest)
- `examples/with-svelte/package.json` (manifest)
- `examples/with-svelte/sandbox.config.json` (config)
- `examples/with-tailwindcss/package.json` (manifest)
- `examples/with-tailwindcss/sandbox.config.json` (config)
- `examples/with-typeorm-graphql/package.json` (manifest)
- `examples/with-typeorm-graphql/tsconfig.json` (config)
- `examples/with-typescript-plugin/package.json` (manifest)
- `examples/with-typescript-plugin/tsconfig.json` (config)
- `examples/with-typescript/package.json` (manifest)
- `examples/with-typescript/tsconfig.json` (config)
- `examples/with-vendor-bundle/package.json` (manifest)
- `examples/with-vue-router/package.json` (manifest)
- `examples/with-vue/package.json` (manifest)
- `examples/with-webpack-dev-server-v4/package.json` (manifest)
- `examples/with-webpack-dev-server-v4/sandbox.config.json` (config)
- `examples/with-webpack-public-path/package.json` (manifest)
- `examples/with-webpack-public-path/sandbox.config.json` (config)
- `lerna.json` (config)
- `package.json` (manifest)
- `package.meta.json` (config)
- `packages/babel-preset-razzle/package.json` (manifest)

## Top-level layout

- `examples` — 745 analysed file(s)
- `packages` — 18 analysed file(s)
- `.github` — 15 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `.changeset` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 12 file(s) were skipped during inventory (12 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `54724b7bb810d06bb418951ada3f90ae3f135668` is the revision these paths and observations refer to.
