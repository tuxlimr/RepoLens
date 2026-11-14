# Project structure: vincentriemer/react-native-dom

**Analysed commit:** `235cae7e628fe1e4d89f662153e90da5ac5d0a9b`

**Commit reference:** [235cae7e628fe1e4d89f662153e90da5ac5d0a9b](https://github.com/vincentriemer/react-native-dom/commit/235cae7e628fe1e4d89f662153e90da5ac5d0a9b)

**Tree at this commit:** [vincentriemer/react-native-dom@235cae7e628f](https://github.com/vincentriemer/react-native-dom/tree/235cae7e628fe1e4d89f662153e90da5ac5d0a9b)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | vincentriemer/react-native-dom |
| Description | An experimental, comprehensive port of React Native to the web. |
| Stars | 3240 |
| Forks | 72 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `235cae7e628fe1e4d89f662153e90da5ac5d0a9b` |
| Retrieved at | 2026-11-14T19:15:27.263614+00:00 |
| Files in this snapshot | 300 |

## Directory tree

```text
.circleci/  (1 files)
  config.yml
.vscode/  (2 files)
  launch.json
  settings.json
Examples/  (1 files)
  index.html
docs/  (5 files)
  doc1.md
  doc2.md
  doc3.md
  exampledoc4.md
  exampledoc5.md
packages/  (254 files)
  react-native-dom/  (231 files)
    Examples/  (25 files)
      … 25 files under this directory
    Libraries/  (48 files)
      … 48 files under this directory
    ReactDom/  (111 files)
      … 111 files under this directory
    flow-typed/  (10 files)
      … 10 files under this directory
    jest/  (1 files)
      … 1 files under this directory
    local-cli/  (24 files)
      … 24 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    .babelrc
    .eslintrc.js
    .gitignore
    .npmignore
    CHANGELOG.md
    README.md
    RNTester.md
    metro.config.js
    now.json
    package.json
  rndom-redbox/  (9 files)
    public/  (2 files)
      … 2 files under this directory
    src/  (1 files)
      … 1 files under this directory
    .gitignore
    .npmignore
    CHANGELOG.md
    README.md
    package.json
    rollup.config.js
  rndom-switch/  (9 files)
    public/  (2 files)
      … 2 files under this directory
    src/  (1 files)
      … 1 files under this directory
    .gitignore
    .npmignore
    CHANGELOG.md
    README.md
    package.json
    rollup.config.js
  rnpm-plugin-dom/  (5 files)
    src/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    README.md
    index.js
    package.json
scripts/  (1 files)
  smoke.js
website/  (22 files)
  blog/  (5 files)
    2016-03-11-blog-post.md
    2017-04-10-blog-post-two.md
    2017-09-25-testing-rss.md
    2017-09-26-adding-rss.md
    2017-10-24-new-version-1.0.0.md
  core/  (1 files)
    Footer.js
  pages/  (3 files)
    en/  (3 files)
      … 3 files under this directory
  static/  (10 files)
    css/  (1 files)
      … 1 files under this directory
    img/  (9 files)
      … 9 files under this directory
  package.json
  sidebars.json
  siteConfig.js
.all-contributorsrc
.eslintignore
.eslintrc.js
.flowconfig
.gitignore
.gitmodules
.prettierignore
.prettierrc
CHANGELOG.md
CODE_OF_CONDUCT.md
LICENSE.md
README.md
lerna.json
package.json
```

## Entry points

- [packages/rnpm-plugin-dom/index.js](https://github.com/vincentriemer/react-native-dom/blob/235cae7e628fe1e4d89f662153e90da5ac5d0a9b/packages/rnpm-plugin-dom/index.js)
- [packages/react-native-dom/local-cli/index.js](https://github.com/vincentriemer/react-native-dom/blob/235cae7e628fe1e4d89f662153e90da5ac5d0a9b/packages/react-native-dom/local-cli/index.js)
- [website/pages/en/index.js](https://github.com/vincentriemer/react-native-dom/blob/235cae7e628fe1e4d89f662153e90da5ac5d0a9b/website/pages/en/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 36 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 15 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 174 file(s) under packages package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 6 file(s) under service / domain layer (observed from repository paths and static analysis). |
| website package | library | Observed | Groups 4 file(s) under website package (observed from repository paths and static analysis). |

## Important files

- `.circleci/config.yml` (ci)
- `.vscode/launch.json` (config)
- `.vscode/settings.json` (config)
- `lerna.json` (config)
- `package.json` (manifest)
- `packages/react-native-dom/Examples/AnimatedScrollView/package.json` (manifest)
- `packages/react-native-dom/Examples/Button/package.json` (manifest)
- `packages/react-native-dom/Examples/FlatList/package.json` (manifest)
- `packages/react-native-dom/Examples/LayoutAnimations/package.json` (manifest)
- `packages/react-native-dom/now.json` (config)
- `packages/react-native-dom/package.json` (manifest)
- `packages/rndom-redbox/package.json` (manifest)
- `packages/rndom-switch/package.json` (manifest)
- `packages/rnpm-plugin-dom/package.json` (manifest)
- `website/package.json` (manifest)
- `website/sidebars.json` (config)
- `website/static/img/favicon/manifest.json` (config)

## Top-level layout

- `packages` — 254 analysed file(s)
- `website` — 22 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `docs` — 5 analysed file(s)
- `.vscode` — 2 analysed file(s)
- `.circleci` — 1 analysed file(s)
- `Examples` — 1 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 4 file(s) were skipped during inventory (4 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `235cae7e628fe1e4d89f662153e90da5ac5d0a9b` is the revision these paths and observations refer to.
