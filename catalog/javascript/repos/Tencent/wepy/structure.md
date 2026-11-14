# Project structure: Tencent/wepy

**Analysed commit:** `253aa5bba394cf9efff90ab3a803a100a017b5cb`

**Commit reference:** [253aa5bba394cf9efff90ab3a803a100a017b5cb](https://github.com/Tencent/wepy/commit/253aa5bba394cf9efff90ab3a803a100a017b5cb)

**Tree at this commit:** [Tencent/wepy@253aa5bba394](https://github.com/Tencent/wepy/tree/253aa5bba394cf9efff90ab3a803a100a017b5cb)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Tencent/wepy |
| Description | 小程序组件化开发框架 - 已归档 |
| Stars | 22502 |
| Forks | 3004 |
| Licence | Other |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `253aa5bba394cf9efff90ab3a803a100a017b5cb` |
| Retrieved at | 2026-11-14T19:11:08.407674+00:00 |
| Files in this snapshot | 471 |

## Directory tree

```text
.github/  (5 files)
  workflows/  (2 files)
    ci.yml
    release.yml
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
  stale.yml
packages/  (427 files)
  babel-plugin-import-regenerator/  (10 files)
    test/  (5 files)
      … 5 files under this directory
    CHANGELOG.md
    README.md
    README_EN.md
    index.js
    package.json
  cli/  (125 files)
    bin/  (16 files)
      … 16 files under this directory
    core/  (56 files)
      … 56 files under this directory
    test/  (46 files)
      … 46 files under this directory
    util/  (1 files)
      … 1 files under this directory
    .gitignore
    .npmignore
    CHANGELOG.md
    README.md
    index.js
    package.json
  compiler-babel/  (9 files)
    test/  (4 files)
      … 4 files under this directory
    .npmignore
    CHANGELOG.md
    README.md
    index.js
    package.json
  compiler-less/  (34 files)
    test/  (28 files)
      … 28 files under this directory
    .npmignore
    CHANGELOG.md
    README.md
    createPlugin.js
    index.js
    package.json
  compiler-postcss/  (11 files)
    test/  (7 files)
      … 7 files under this directory
    CHANGELOG.md
    README.md
    index.js
    package.json
  compiler-sass/  (22 files)
    src/  (1 files)
      … 1 files under this directory
    test/  (14 files)
      … 14 files under this directory
    .npmignore
    CHANGELOG.md
    README.md
    importsToResolve.js
    index.js
    package.json
    resolveImporter.js
  compiler-stylus/  (32 files)
    test/  (26 files)
      … 26 files under this directory
    .npmignore
    CHANGELOG.md
    README.md
    createPlugin.js
    index.js
    package.json
  compiler-typescript/  (5 files)
    .npmignore
    CHANGELOG.md
    README.md
    index.js
    package.json
  core/  (107 files)
    ant/  (13 files)
      … 13 files under this directory
    shared/  (5 files)
      … 5 files under this directory
    src/  (3 files)
      … 3 files under this directory
    test/  (21 files)
      … 21 files under this directory
    types/  (18 files)
      … 18 files under this directory
    weapp/  (42 files)
      … 42 files under this directory
    .nycrc
    CHANGELOG.md
    index.ant.js
    index.js
    package.json
  plugin-define/  (12 files)
    test/  (6 files)
      … 6 files under this directory
    .npmignore
    CHANGELOG.md
    README.md
    README_EN.md
    index.js
    package.json
  plugin-eslint/  (6 files)
    test/  (1 files)
      … 1 files under this directory
    .npmignore
    CHANGELOG.md
    README.md
    index.js
    package.json
  plugin-uglifyjs/  (6 files)
    test/  (1 files)
      … 1 files under this directory
    .npmignore
    CHANGELOG.md
    README.md
    index.js
    package.json
  redux/  (7 files)
    CHANGELOG.md
    README.md
    README_EN.md
    helper.js
    index.js
    install.js
    package.json
  router/  (22 files)
    core/  (13 files)
      … 13 files under this directory
    doc/  (5 files)
      … 5 files under this directory
    README.md
    index.js
    install.js
    package.json
  use-intercept/  (7 files)
    test/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    README.md
    README_EN.md
    index.js
    install.js
    package.json
  use-promisify/  (7 files)
    test/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    README.md
    README_EN.md
    index.js
    install.js
    package.json
  x/  (5 files)
    CHANGELOG.md
    README.md
    README_EN.md
    index.js
    package.json
scripts/  (17 files)
  npm_publish/  (5 files)
    lib/  (4 files)
      … 4 files under this directory
    index.js
  bootstrap.sh
  build.js
  build.sh
  ci-release.js
  clean.js
  config.js
  install_dev.sh
  npm-ci-release.js
  npm-tags.js
  release.js
  test-build.sh
  unittest.js
test/  (5 files)
  build-cases/  (2 files)
    empty.sh
    standard.sh
  scripts/  (1 files)
    ci-release.test.js
  build.sh
  unit.js
.editorconfig
.eslintignore
.eslintrc
.gitignore
.npmignore
.nycrc
.prettierrc.yml
.travis.yml
CHANGELOG.md
CONTRIBUTING.md
CONTRIBUTING_COMMIT.md
LICENSE
README.md
README_EN.md
lerna.json
package.json
verpub.config.js
```

## Entry points

- [packages/babel-plugin-import-regenerator/index.js](https://github.com/Tencent/wepy/blob/253aa5bba394cf9efff90ab3a803a100a017b5cb/packages/babel-plugin-import-regenerator/index.js)
- [packages/cli/index.js](https://github.com/Tencent/wepy/blob/253aa5bba394cf9efff90ab3a803a100a017b5cb/packages/cli/index.js)
- [packages/cli/bin/wepy.js](https://github.com/Tencent/wepy/blob/253aa5bba394cf9efff90ab3a803a100a017b5cb/packages/cli/bin/wepy.js)
- [packages/compiler-babel/index.js](https://github.com/Tencent/wepy/blob/253aa5bba394cf9efff90ab3a803a100a017b5cb/packages/compiler-babel/index.js)
- [packages/compiler-less/index.js](https://github.com/Tencent/wepy/blob/253aa5bba394cf9efff90ab3a803a100a017b5cb/packages/compiler-less/index.js)
- [packages/compiler-postcss/index.js](https://github.com/Tencent/wepy/blob/253aa5bba394cf9efff90ab3a803a100a017b5cb/packages/compiler-postcss/index.js)
- [packages/compiler-sass/index.js](https://github.com/Tencent/wepy/blob/253aa5bba394cf9efff90ab3a803a100a017b5cb/packages/compiler-sass/index.js)
- [packages/compiler-stylus/index.js](https://github.com/Tencent/wepy/blob/253aa5bba394cf9efff90ab3a803a100a017b5cb/packages/compiler-stylus/index.js)
- [packages/compiler-typescript/index.js](https://github.com/Tencent/wepy/blob/253aa5bba394cf9efff90ab3a803a100a017b5cb/packages/compiler-typescript/index.js)
- [packages/plugin-define/index.js](https://github.com/Tencent/wepy/blob/253aa5bba394cf9efff90ab3a803a100a017b5cb/packages/plugin-define/index.js)
- [packages/plugin-eslint/index.js](https://github.com/Tencent/wepy/blob/253aa5bba394cf9efff90ab3a803a100a017b5cb/packages/plugin-eslint/index.js)
- [packages/plugin-uglifyjs/index.js](https://github.com/Tencent/wepy/blob/253aa5bba394cf9efff90ab3a803a100a017b5cb/packages/plugin-uglifyjs/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 21 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 43 file(s) under packages package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 17 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 145 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 171 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/stale.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.prettierrc.yml` (config)
- `.travis.yml` (ci)
- `lerna.json` (config)
- `package.json` (manifest)
- `packages/babel-plugin-import-regenerator/package.json` (manifest)
- `packages/cli/package.json` (manifest)
- `packages/compiler-babel/package.json` (manifest)
- `packages/compiler-less/package.json` (manifest)
- `packages/compiler-postcss/package.json` (manifest)
- `packages/compiler-sass/package.json` (manifest)
- `packages/compiler-stylus/package.json` (manifest)
- `packages/compiler-typescript/package.json` (manifest)
- `packages/core/package.json` (manifest)
- `packages/core/types/tsconfig.json` (config)
- `packages/core/types/typings.json` (config)
- `packages/plugin-define/package.json` (manifest)
- `packages/plugin-eslint/package.json` (manifest)
- `packages/plugin-uglifyjs/package.json` (manifest)
- `packages/redux/package.json` (manifest)
- `packages/router/package.json` (manifest)
- `packages/use-intercept/package.json` (manifest)
- `packages/use-promisify/package.json` (manifest)
- `packages/x/package.json` (manifest)

## Top-level layout

- `packages` — 427 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `scripts` — 17 analysed file(s)
- `.github` — 5 analysed file(s)
- `test` — 5 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 21 file(s) were skipped during inventory (10 x lockfile excluded; 11 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `253aa5bba394cf9efff90ab3a803a100a017b5cb` is the revision these paths and observations refer to.
