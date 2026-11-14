# Project structure: neutrinojs/neutrino

**Analysed commit:** `f9d476446983684225545159f58bbed2a93ca824`

**Commit reference:** [f9d476446983684225545159f58bbed2a93ca824](https://github.com/neutrinojs/neutrino/commit/f9d476446983684225545159f58bbed2a93ca824)

**Tree at this commit:** [neutrinojs/neutrino@f9d476446983](https://github.com/neutrinojs/neutrino/tree/f9d476446983684225545159f58bbed2a93ca824)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | neutrinojs/neutrino |
| Description | Create and build modern JavaScript projects with zero initial configuration. |
| Stars | 3903 |
| Forks | 208 |
| Licence | MPL-2.0 |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `f9d476446983684225545159f58bbed2a93ca824` |
| Retrieved at | 2026-11-14T19:14:58.814177+00:00 |
| Files in this snapshot | 244 |

## Directory tree

```text
.github/  (5 files)
  workflows/  (1 files)
    ci.yml
  CODE_OF_CONDUCT.md
  CONTRIBUTING.md
  ISSUE_TEMPLATE.md
  SUPPORT.md
docs/  (18 files)
  contributing/  (3 files)
    code-of-conduct.md
    development.md
    index.md
  installation/  (1 files)
    index.md
  api.md
  creating-presets.md
  customization.md
  faq.md
  index.md
  learning-resources.md
  middleware.md
  migration-guide.md
  presets.md
  project-layout.md
  requirements.txt
  runtime.txt
  usage.md
  webpack-chain.md
packages/  (201 files)
  airbnb/  (6 files)
    test/  (1 files)
      … 1 files under this directory
    .npmignore
    README.md
    eslintrc.js
    index.js
    package.json
  airbnb-base/  (6 files)
    test/  (1 files)
      … 1 files under this directory
    .npmignore
    README.md
    eslintrc.js
    index.js
    package.json
  banner/  (5 files)
    test/  (1 files)
      … 1 files under this directory
    .npmignore
    README.md
    index.js
    package.json
  clean/  (5 files)
    test/  (1 files)
      … 1 files under this directory
    .npmignore
    README.md
    index.js
    package.json
  compile-loader/  (5 files)
    test/  (1 files)
      … 1 files under this directory
    .npmignore
    README.md
    index.js
    package.json
  copy/  (5 files)
    test/  (1 files)
      … 1 files under this directory
    .npmignore
    README.md
    index.js
    package.json
  create-project/  (39 files)
    bin/  (1 files)
      … 1 files under this directory
    commands/  (34 files)
      … 34 files under this directory
    test/  (1 files)
      … 1 files under this directory
    .npmignore
    README.md
    package.json
  dev-server/  (5 files)
    test/  (1 files)
      … 1 files under this directory
    .npmignore
    README.md
    index.js
    package.json
  eslint/  (6 files)
    test/  (1 files)
      … 1 files under this directory
    .npmignore
    README.md
    eslintrc.js
    index.js
    package.json
  font-loader/  (5 files)
    test/  (1 files)
      … 1 files under this directory
    .npmignore
    README.md
    index.js
    package.json
  html-loader/  (5 files)
    test/  (1 files)
      … 1 files under this directory
    .npmignore
    README.md
    index.js
    package.json
  html-template/  (6 files)
    test/  (1 files)
      … 1 files under this directory
    .npmignore
    README.md
    index.js
    package.json
    template.ejs
  image-loader/  (5 files)
    test/  (1 files)
      … 1 files under this directory
    .npmignore
    README.md
    index.js
    package.json
  jest/  (8 files)
    src/  (4 files)
      … 4 files under this directory
    test/  (1 files)
      … 1 files under this directory
    .npmignore
    README.md
    package.json
  karma/  (5 files)
    test/  (1 files)
      … 1 files under this directory
    .npmignore
    README.md
    index.js
    package.json
  library/  (5 files)
    test/  (1 files)
      … 1 files under this directory
    .npmignore
    README.md
    index.js
    package.json
  migrate/  (8 files)
    bin/  (1 files)
      … 1 files under this directory
    test/  (3 files)
      … 3 files under this directory
    transforms/  (1 files)
      … 1 files under this directory
    .npmignore
    README.md
    package.json
  mocha/  (6 files)
    src/  (2 files)
      … 2 files under this directory
    test/  (1 files)
      … 1 files under this directory
    .npmignore
    README.md
    package.json
  neutrino/  (14 files)
    bin/  (1 files)
      … 1 files under this directory
    test/  (5 files)
      … 5 files under this directory
    .npmignore
    Neutrino.js
    README.md
    errors.js
    extensions.js
    handlers.js
    index.js
    package.json
  node/  (5 files)
    test/  (1 files)
      … 1 files under this directory
    .npmignore
    README.md
    index.js
    package.json
  preact/  (5 files)
    test/  (1 files)
      … 1 files under this directory
    .npmignore
    README.md
    index.js
    package.json
  react/  (5 files)
    test/  (1 files)
      … 1 files under this directory
    .npmignore
    README.md
    index.js
    package.json
  react-components/  (6 files)
    test/  (2 files)
      … 2 files under this directory
    .npmignore
    README.md
    index.js
    package.json
  standardjs/  (6 files)
    test/  (1 files)
      … 1 files under this directory
    .npmignore
    README.md
    eslintrc.js
    index.js
    package.json
  start-server/  (5 files)
    test/  (1 files)
      … 1 files under this directory
    .npmignore
    README.md
    index.js
    package.json
  style-loader/  (5 files)
    test/  (1 files)
      … 1 files under this directory
    .npmignore
    README.md
    index.js
    package.json
  style-minify/  (5 files)
    test/  (1 files)
      … 1 files under this directory
    .npmignore
    README.md
    index.js
    package.json
  vue/  (5 files)
    test/  (1 files)
      … 1 files under this directory
    .npmignore
    README.md
    index.js
    package.json
  web/  (5 files)
    test/  (1 files)
      … 1 files under this directory
    .npmignore
    README.md
    index.js
    package.json
scripts/  (2 files)
  build-docs.sh
  test-create-project-ci.sh
.auto-changelog
.eslintignore
.eslintrc.js
.gitignore
.huskyrc.js
.lintstagedrc.js
.neutrinorc.js
.prettierrc.js
CHANGELOG.md
LICENSE
README.md
lerna.json
mkdocs.yml
netlify.toml
package.json
renovate.json
verdaccio.npm.yml
verdaccio.yarn.yml
```

## Entry points

- [packages/airbnb-base/index.js](https://github.com/neutrinojs/neutrino/blob/f9d476446983684225545159f58bbed2a93ca824/packages/airbnb-base/index.js)
- [packages/airbnb/index.js](https://github.com/neutrinojs/neutrino/blob/f9d476446983684225545159f58bbed2a93ca824/packages/airbnb/index.js)
- [packages/banner/index.js](https://github.com/neutrinojs/neutrino/blob/f9d476446983684225545159f58bbed2a93ca824/packages/banner/index.js)
- [packages/clean/index.js](https://github.com/neutrinojs/neutrino/blob/f9d476446983684225545159f58bbed2a93ca824/packages/clean/index.js)
- [packages/compile-loader/index.js](https://github.com/neutrinojs/neutrino/blob/f9d476446983684225545159f58bbed2a93ca824/packages/compile-loader/index.js)
- [packages/copy/index.js](https://github.com/neutrinojs/neutrino/blob/f9d476446983684225545159f58bbed2a93ca824/packages/copy/index.js)
- [packages/create-project/bin/create-project.js](https://github.com/neutrinojs/neutrino/blob/f9d476446983684225545159f58bbed2a93ca824/packages/create-project/bin/create-project.js)
- [packages/dev-server/index.js](https://github.com/neutrinojs/neutrino/blob/f9d476446983684225545159f58bbed2a93ca824/packages/dev-server/index.js)
- [packages/eslint/index.js](https://github.com/neutrinojs/neutrino/blob/f9d476446983684225545159f58bbed2a93ca824/packages/eslint/index.js)
- [packages/font-loader/index.js](https://github.com/neutrinojs/neutrino/blob/f9d476446983684225545159f58bbed2a93ca824/packages/font-loader/index.js)
- [packages/html-loader/index.js](https://github.com/neutrinojs/neutrino/blob/f9d476446983684225545159f58bbed2a93ca824/packages/html-loader/index.js)
- [packages/html-template/index.js](https://github.com/neutrinojs/neutrino/blob/f9d476446983684225545159f58bbed2a93ca824/packages/html-template/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 36 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 71 file(s) under packages package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 2 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 39 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/ci.yml` (ci)
- `docs/requirements.txt` (manifest)
- `lerna.json` (config)
- `mkdocs.yml` (config)
- `netlify.toml` (config)
- `package.json` (manifest)
- `packages/airbnb-base/package.json` (manifest)
- `packages/airbnb/package.json` (manifest)
- `packages/banner/package.json` (manifest)
- `packages/clean/package.json` (manifest)
- `packages/compile-loader/package.json` (manifest)
- `packages/copy/package.json` (manifest)
- `packages/create-project/package.json` (manifest)
- `packages/dev-server/package.json` (manifest)
- `packages/eslint/package.json` (manifest)
- `packages/font-loader/package.json` (manifest)
- `packages/html-loader/package.json` (manifest)
- `packages/html-template/package.json` (manifest)
- `packages/image-loader/package.json` (manifest)
- `packages/jest/package.json` (manifest)
- `packages/karma/package.json` (manifest)
- `packages/library/package.json` (manifest)
- `packages/migrate/package.json` (manifest)
- `packages/mocha/package.json` (manifest)
- `packages/neutrino/package.json` (manifest)
- `packages/node/package.json` (manifest)
- `packages/preact/package.json` (manifest)
- `packages/react-components/package.json` (manifest)
- `packages/react/package.json` (manifest)
- `packages/standardjs/package.json` (manifest)
- `packages/start-server/package.json` (manifest)
- `packages/style-loader/package.json` (manifest)
- `packages/style-minify/package.json` (manifest)
- `packages/vue/package.json` (manifest)
- `packages/web/package.json` (manifest)
- `renovate.json` (config)
- `verdaccio.npm.yml` (config)
- `verdaccio.yarn.yml` (config)

## Top-level layout

- `packages` — 201 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `docs` — 18 analysed file(s)
- `.github` — 5 analysed file(s)
- `scripts` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `f9d476446983684225545159f58bbed2a93ca824` is the revision these paths and observations refer to.
