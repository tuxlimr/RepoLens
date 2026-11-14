# Project structure: dilanx/craco

**Analysed commit:** `56840ceaedaa5f71cc580099e72f0048fafcc44f`

**Commit reference:** [56840ceaedaa5f71cc580099e72f0048fafcc44f](https://github.com/dilanx/craco/commit/56840ceaedaa5f71cc580099e72f0048fafcc44f)

**Tree at this commit:** [dilanx/craco@56840ceaedaa](https://github.com/dilanx/craco/tree/56840ceaedaa5f71cc580099e72f0048fafcc44f)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | dilanx/craco |
| Description | Create React App Configuration Override, an easy and comprehensible configuration layer for Create React App. |
| Stars | 7404 |
| Forks | 481 |
| Licence | Apache-2.0 |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `56840ceaedaa5f71cc580099e72f0048fafcc44f` |
| Retrieved at | 2026-11-14T19:13:51.013745+00:00 |
| Files in this snapshot | 167 |

## Directory tree

```text
.github/  (7 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (3 files)
    run-tests.yml
    website-deploy.yml
    website-test-deploy.yml
  CODEOWNERS
  FUNDING.yml
.vscode/  (1 files)
  extensions.json
packages/  (54 files)
  craco/  (44 files)
    src/  (40 files)
      … 40 files under this directory
    LICENSE
    README.md
    package.json
    tsconfig.json
  craco-types/  (10 files)
    src/  (7 files)
      … 7 files under this directory
    README.md
    package.json
    tsconfig.json
recipes/  (1 files)
  README.md
test/  (40 files)
  integration/  (14 files)
    fixtures/  (11 files)
      … 11 files under this directory
    jest.config.js
    setup.js
    teardown.js
  unit/  (25 files)
    merging-tests/  (24 files)
      … 24 files under this directory
    jest.config.js
  README.md
website/  (55 files)
  docs/  (18 files)
    configuration/  (9 files)
      … 9 files under this directory
    plugin-api/  (6 files)
      … 6 files under this directory
    configuration-api.md
    getting-started.md
    welcome.md
  plugins/  (1 files)
    plugins.md
  recipes/  (21 files)
    add-autoprefixer-options.md
    add-postcss-features.md
    add-stylelint.md
    add-webpack-alias-to-jest.md
    extends-postcss-plugins.md
    set-css-loader-locals-convention.md
    use-a-jest-config-file.md
    use-a-postcss-config-file.md
    use-an-eslint-config-file.md
    use-an-https-dev-server.md
    use-ant-design.md
    use-babel-plugin-react-css-modules.md
    use-dart-sass.md
    use-html-loader.md
    use-less-loader.md
    use-linaria.md
    use-markdown-loader.md
    use-mobx.md
    use-preact.md
    use-purescript.md
    use-ts-loader.md
  src/  (4 files)
    components/  (2 files)
      … 2 files under this directory
    css/  (1 files)
      … 1 files under this directory
    pages/  (1 files)
      … 1 files under this directory
  static/  (4 files)
    img/  (2 files)
      … 2 files under this directory
    .nojekyll
    CNAME
  .gitignore
  README.md
  babel.config.js
  docusaurus.config.js
  package.json
  sidebars.js
  sidebarsRecipes.js
.eslintrc.json
.gitattributes
.gitignore
.prettierignore
LICENSE
README.md
lerna.json
package.json
tsconfig.json
```

## Entry points

- [packages/craco-types/src/index.ts](https://github.com/dilanx/craco/blob/56840ceaedaa5f71cc580099e72f0048fafcc44f/packages/craco-types/src/index.ts)
- [packages/craco/src/index.ts](https://github.com/dilanx/craco/blob/56840ceaedaa5f71cc580099e72f0048fafcc44f/packages/craco/src/index.ts)
- [website/src/pages/index.js](https://github.com/dilanx/craco/blob/56840ceaedaa5f71cc580099e72f0048fafcc44f/website/src/pages/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 8 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 47 file(s) under packages package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 40 file(s) under tests (observed from repository paths and static analysis). |
| website package | library | Observed | Groups 6 file(s) under website package (observed from repository paths and static analysis). |

## Important files

- `.eslintrc.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/workflows/run-tests.yml` (ci)
- `.github/workflows/website-deploy.yml` (ci)
- `.github/workflows/website-test-deploy.yml` (ci)
- `.vscode/extensions.json` (config)
- `lerna.json` (config)
- `package.json` (manifest)
- `packages/craco-types/package.json` (manifest)
- `packages/craco-types/tsconfig.json` (config)
- `packages/craco/package.json` (manifest)
- `packages/craco/tsconfig.json` (config)
- `tsconfig.json` (config)
- `website/package.json` (manifest)

## Top-level layout

- `website` — 55 analysed file(s)
- `packages` — 54 analysed file(s)
- `test` — 40 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `.github` — 7 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `recipes` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `56840ceaedaa5f71cc580099e72f0048fafcc44f` is the revision these paths and observations refer to.
