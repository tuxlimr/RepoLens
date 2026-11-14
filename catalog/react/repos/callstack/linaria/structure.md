# Project structure: callstack/linaria

**Analysed commit:** `63a958afeebb0be3bb66cc8f31a0b1a54238b36e`

**Commit reference:** [63a958afeebb0be3bb66cc8f31a0b1a54238b36e](https://github.com/callstack/linaria/commit/63a958afeebb0be3bb66cc8f31a0b1a54238b36e)

**Tree at this commit:** [callstack/linaria@63a958afeebb](https://github.com/callstack/linaria/tree/63a958afeebb0be3bb66cc8f31a0b1a54238b36e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | callstack/linaria |
| Description | Zero-runtime CSS in JS library |
| Stars | 12351 |
| Forks | 414 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `63a958afeebb0be3bb66cc8f31a0b1a54238b36e` |
| Retrieved at | 2026-11-14T19:13:20.649586+00:00 |
| Files in this snapshot | 293 |

## Directory tree

```text
.changeset/  (2 files)
  README.md
  config.json
.github/  (10 files)
  ISSUE_TEMPLATE/  (4 files)
    bug_report.md
    config.yml
    enhancement_request.md
    feature_request.md
  workflows/  (4 files)
    check.yml
    main.yml
    release.yml
    site-deploy.yml
  PULL_REQUEST_TEMPLATE.md
  labels.json
.husky/  (2 files)
  commit-msg
  pre-commit
.vscode/  (1 files)
  settings.json
babel-plugins/  (1 files)
  transform-import-meta.cjs
docs/  (15 files)
  API.md
  ATOMIC_CSS.md
  BASICS.md
  BENEFITS.md
  BUNDLERS_INTEGRATION.md
  CLI.md
  CONFIGURATION.md
  CRITICAL_CSS.md
  DYNAMIC_STYLES.md
  FEATURE_FLAGS.md
  HOW_IT_WORKS.md
  LINTING.md
  MIGRATION_GUIDE.md
  THEMING.md
  TYPESCRIPT.md
examples/  (38 files)
  astro-solid/  (7 files)
    components/  (3 files)
      … 3 files under this directory
    pages/  (1 files)
      … 1 files under this directory
    astro.config.js
    package.json
    tsconfig.json
  esbuild/  (4 files)
    .gitignore
    app.js
    build.js
    package.json
  rollup/  (5 files)
    .gitignore
    app.js
    babel.config.js
    package.json
    rollup.config.mjs
  vite/  (5 files)
    .linariarc.mjs
    app.js
    index.html
    package.json
    vite.config.js
  vpssr-linaria-solid/  (13 files)
    pages/  (8 files)
      … 8 files under this directory
    check-vite-version.mjs
    package.json
    server.js
    tsconfig.json
    vite.config.js
  webpack5/  (4 files)
    app.js
    babel.config.js
    package.json
    webpack.config.js
packages/  (173 files)
  atomic/  (15 files)
    processors/  (3 files)
      … 3 files under this directory
    src/  (7 files)
      … 7 files under this directory
    CHANGELOG.md
    README.md
    babel.config.js
    package.json
    tsconfig.json
  core/  (18 files)
    __dtslint__/  (3 files)
      … 3 files under this directory
    __tests__/  (2 files)
      … 2 files under this directory
    processors/  (2 files)
      … 2 files under this directory
    src/  (5 files)
      … 5 files under this directory
    CHANGELOG.md
    README.md
    babel.config.js
    package.json
    tsconfig.json
    tstyche.json
  interop/  (8 files)
    __tests__/  (2 files)
      … 2 files under this directory
    src/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    README.md
    babel.config.js
    package.json
    tsconfig.json
  linaria/  (15 files)
    babel/  (1 files)
      … 1 files under this directory
    evaluators/  (1 files)
      … 1 files under this directory
    loader/  (1 files)
      … 1 files under this directory
    react/  (1 files)
      … 1 files under this directory
    rollup/  (1 files)
      … 1 files under this directory
    server/  (1 files)
      … 1 files under this directory
    src/  (3 files)
      … 3 files under this directory
    stylelint-config/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    README.md
    babel.config.js
    package.json
    tsconfig.json
  postcss-linaria/  (17 files)
    __tests__/  (6 files)
      … 6 files under this directory
    src/  (6 files)
      … 6 files under this directory
    CHANGELOG.md
    README.md
    babel.config.js
    package.json
    tsconfig.json
  react/  (24 files)
    __dtslint-react17__/  (5 files)
      … 5 files under this directory
    __dtslint__/  (4 files)
      … 4 files under this directory
    __tests__/  (3 files)
      … 3 files under this directory
    processors/  (2 files)
      … 2 files under this directory
    src/  (4 files)
      … 4 files under this directory
    CHANGELOG.md
    README.md
    babel.config.js
    package.json
    tsconfig.json
    tstyche.json
  server/  (9 files)
    __tests__/  (2 files)
      … 2 files under this directory
    src/  (2 files)
      … 2 files under this directory
    CHANGELOG.md
    README.md
    babel.config.js
    package.json
    tsconfig.json
  stylelint/  (7 files)
    src/  (2 files)
      … 2 files under this directory
    CHANGELOG.md
    README.md
    babel.config.js
    package.json
    tsconfig.json
  stylelint-config-standard-linaria/  (6 files)
    src/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    README.md
    babel.config.js
    package.json
    tsconfig.json
  testkit/  (54 files)
    src/  (51 files)
      … 51 files under this directory
    CHANGELOG.md
    package.json
    tsconfig.json
react/  (1 files)
  package.json
scripts/  (3 files)
  check-astro-solid-example.sh
  check-eslint-flat-config.sh
  typecheck-postcss-8-5.sh
website/  (24 files)
  assets/  (4 files)
    callstack-logo.svg
    linaria-logo.svg
    linaria-logomark.svg
    serverscom-logo-black.svg
  src/  (11 files)
    api/  (2 files)
      … 2 files under this directory
    components/  (5 files)
      … 5 files under this directory
    styles/  (2 files)
      … 2 files under this directory
    index.jsx
    server.jsx
  CHANGELOG.md
  babel.config.js
  babel.server-jsx.config.js
  index.html
  linaria.config.js
  package.json
  serve.config.js
  stylelint.config.js
  webpack.config.js
.all-contributorsrc
.codecov.yml
.editorconfig
.git-blame-ignore-revs
.gitignore
.prettierrc
.syncpackrc.js
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
babel.config.js
commitlint.config.mjs
eslint.config.js
greenkeeper.json
jest.config.js
link-wyw.sh
package.json
pnpm-workspace.yaml
tsconfig.eslint.json
tsconfig.json
tsconfig.prod.json
turbo.json
```

## Entry points

- [website/src/index.jsx](https://github.com/callstack/linaria/blob/63a958afeebb0be3bb66cc8f31a0b1a54238b36e/website/src/index.jsx)
- [packages/atomic/src/index.ts](https://github.com/callstack/linaria/blob/63a958afeebb0be3bb66cc8f31a0b1a54238b36e/packages/atomic/src/index.ts)
- [packages/core/src/index.ts](https://github.com/callstack/linaria/blob/63a958afeebb0be3bb66cc8f31a0b1a54238b36e/packages/core/src/index.ts)
- [packages/interop/src/index.ts](https://github.com/callstack/linaria/blob/63a958afeebb0be3bb66cc8f31a0b1a54238b36e/packages/interop/src/index.ts)
- [packages/linaria/src/server.ts](https://github.com/callstack/linaria/blob/63a958afeebb0be3bb66cc8f31a0b1a54238b36e/packages/linaria/src/server.ts)
- [packages/postcss-linaria/src/index.ts](https://github.com/callstack/linaria/blob/63a958afeebb0be3bb66cc8f31a0b1a54238b36e/packages/postcss-linaria/src/index.ts)
- [packages/react/src/index.ts](https://github.com/callstack/linaria/blob/63a958afeebb0be3bb66cc8f31a0b1a54238b36e/packages/react/src/index.ts)
- [packages/server/src/index.ts](https://github.com/callstack/linaria/blob/63a958afeebb0be3bb66cc8f31a0b1a54238b36e/packages/server/src/index.ts)
- [packages/stylelint-config-standard-linaria/src/index.js](https://github.com/callstack/linaria/blob/63a958afeebb0be3bb66cc8f31a0b1a54238b36e/packages/stylelint-config-standard-linaria/src/index.js)
- [packages/stylelint/src/index.ts](https://github.com/callstack/linaria/blob/63a958afeebb0be3bb66cc8f31a0b1a54238b36e/packages/stylelint/src/index.ts)
- [website/src/api/index.js](https://github.com/callstack/linaria/blob/63a958afeebb0be3bb66cc8f31a0b1a54238b36e/website/src/api/index.js)
- [website/src/components/App.jsx](https://github.com/callstack/linaria/blob/63a958afeebb0be3bb66cc8f31a0b1a54238b36e/website/src/components/App.jsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 2 file(s) under api layer (observed from repository paths and static analysis). |
| babel-plugins package | library | Observed | Groups 1 file(s) under babel-plugins package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 50 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 5 file(s) under core modules (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 98 file(s) under packages package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 3 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 10 file(s) under service / domain layer (observed from repository paths and static analysis). |
| website package | library | Observed | Groups 15 file(s) under website package (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.codecov.yml` (config)
- `.editorconfig` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/labels.json` (config)
- `.github/workflows/check.yml` (ci)
- `.github/workflows/main.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/site-deploy.yml` (ci)
- `.vscode/settings.json` (config)
- `examples/astro-solid/package.json` (manifest)
- `examples/astro-solid/tsconfig.json` (config)
- `examples/esbuild/package.json` (manifest)
- `examples/rollup/package.json` (manifest)
- `examples/vite/package.json` (manifest)
- `examples/vpssr-linaria-solid/package.json` (manifest)
- `examples/vpssr-linaria-solid/tsconfig.json` (config)
- `examples/webpack5/package.json` (manifest)
- `greenkeeper.json` (config)
- `package.json` (manifest)
- `packages/atomic/package.json` (manifest)
- `packages/atomic/processors/styled.processor.json` (config)
- `packages/atomic/tsconfig.json` (config)
- `packages/core/__dtslint__/tsconfig.eslint.json` (config)
- `packages/core/__dtslint__/tsconfig.json` (config)
- `packages/core/package.json` (manifest)
- `packages/core/processors/css.processor.json` (config)
- `packages/core/tsconfig.json` (config)
- `packages/core/tstyche.json` (config)
- `packages/interop/package.json` (manifest)
- `packages/interop/tsconfig.json` (config)
- `packages/linaria/babel/package.json` (manifest)
- `packages/linaria/evaluators/package.json` (manifest)
- `packages/linaria/loader/package.json` (manifest)
- `packages/linaria/package.json` (manifest)
- `packages/linaria/react/package.json` (manifest)
- `packages/linaria/rollup/package.json` (manifest)
- `packages/linaria/server/package.json` (manifest)
- `packages/linaria/stylelint-config/package.json` (manifest)
- `packages/linaria/tsconfig.json` (config)
- `packages/postcss-linaria/package.json` (manifest)
- `packages/postcss-linaria/tsconfig.json` (config)
- `packages/react/__dtslint-react17__/tsconfig.eslint.json` (config)
- `packages/react/__dtslint-react17__/tsconfig.json` (config)
- `packages/react/__dtslint__/tsconfig.eslint.json` (config)
- `packages/react/__dtslint__/tsconfig.json` (config)
- `packages/react/package.json` (manifest)
- `packages/react/processors/styled.processor.json` (config)
- `packages/react/tsconfig.json` (config)
- `packages/react/tstyche.json` (config)
- `packages/server/package.json` (manifest)
- `packages/server/tsconfig.json` (config)
- `packages/stylelint-config-standard-linaria/package.json` (manifest)
- `packages/stylelint-config-standard-linaria/tsconfig.json` (config)
- `packages/stylelint/package.json` (manifest)
- `packages/stylelint/tsconfig.json` (config)
- `packages/testkit/package.json` (manifest)
- `packages/testkit/src/__fixtures__/linaria-ui-library/package.json` (manifest)
- `packages/testkit/src/__fixtures__/non-linaria-ui-library/package.json` (manifest)
- `packages/testkit/src/__fixtures__/sample-data.json` (config)
- `packages/testkit/tsconfig.json` (config)
- `pnpm-workspace.yaml` (config)
- `react/package.json` (manifest)
- `tsconfig.eslint.json` (config)
- `tsconfig.json` (config)
- `tsconfig.prod.json` (config)
- `turbo.json` (config)
- `website/package.json` (manifest)

## Top-level layout

- `packages` — 173 analysed file(s)
- `examples` — 38 analysed file(s)
- `website` — 24 analysed file(s)
- `(root files)` — 23 analysed file(s)
- `docs` — 15 analysed file(s)
- `.github` — 10 analysed file(s)
- `scripts` — 3 analysed file(s)
- `.changeset` — 2 analysed file(s)
- `.husky` — 2 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `babel-plugins` — 1 analysed file(s)
- `react` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `63a958afeebb0be3bb66cc8f31a0b1a54238b36e` is the revision these paths and observations refer to.
