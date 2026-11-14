# Project structure: alibaba/formily

**Analysed commit:** `d9a46442a575aa5f0fc1bd945e34d9a85d191d0e`

**Commit reference:** [d9a46442a575aa5f0fc1bd945e34d9a85d191d0e](https://github.com/alibaba/formily/commit/d9a46442a575aa5f0fc1bd945e34d9a85d191d0e)

**Tree at this commit:** [alibaba/formily@d9a46442a575](https://github.com/alibaba/formily/tree/d9a46442a575aa5f0fc1bd945e34d9a85d191d0e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | alibaba/formily |
| Description | 📱🚀 🧩 Cross Device & High Performance Normal Form/Dynamic(JSON Schema) Form/Form Builder -- Support React/React Native/Vue 2/Vue 3 |
| Stars | 12596 |
| Forks | 1593 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | formily_next |
| Analysed commit | `d9a46442a575aa5f0fc1bd945e34d9a85d191d0e` |
| Retrieved at | 2026-11-14T19:13:20.019844+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.github/  (10 files)
  ISSUE_TEMPLATE/  (1 files)
    config.yml
  workflows/  (6 files)
    check-pr-title.yml
    ci.yml
    commitlint.yml
    issue-open-check.yml
    package-size.yml
    pr-welcome.yml
  CONTRIBUTING.md
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
.vscode/  (1 files)
  cspell.json
devtools/  (29 files)
  chrome-extension/  (28 files)
    assets/  (1 files)
      … 1 files under this directory
    config/  (3 files)
      … 3 files under this directory
    src/  (19 files)
      … 19 files under this directory
    .npmignore
    LICENSE.md
    package.json
    tsconfig.build.json
    tsconfig.json
  .eslintrc
docs/  (62 files)
  functions/  (2 files)
    contributors.ts
    npm-search.ts
  guide/  (51 files)
    advanced/  (21 files)
      … 21 files under this directory
    scenes/  (16 files)
      … 16 files under this directory
    contribution.md
    contribution.zh-CN.md
    form-builder.md
    form-builder.zh-CN.md
    index.md
    index.zh-CN.md
    issue-helper.md
    issue-helper.zh-CN.md
    learn-formily.md
    learn-formily.zh-CN.md
    quick-start.md
    quick-start.zh-CN.md
    upgrade.md
    upgrade.zh-CN.md
  site/  (7 files)
    Contributors.less
    Contributors.tsx
    QrCode.less
    QrCode.tsx
    Section.less
    Section.tsx
    styles.less
  index.md
  index.zh-CN.md
packages/  (680 files)
  antd/  (192 files)
    __tests__/  (2 files)
      … 2 files under this directory
    docs/  (72 files)
      … 72 files under this directory
    src/  (108 files)
      … 108 files under this directory
    .npmignore
    .umirc.js
    LICENSE.md
    README.md
    build-style.ts
    create-style.ts
    package.json
    rollup.config.js
    tsconfig.build.json
    tsconfig.json
  benchmark/  (12 files)
    src/  (1 files)
      … 1 files under this directory
    .npmignore
    .umirc.js
    LICENSE.md
    README.md
    package.json
    template.ejs
    tsconfig.build.json
    tsconfig.json
    webpack.base.ts
    webpack.dev.ts
    webpack.prod.ts
  core/  (85 files)
    docs/  (42 files)
      … 42 files under this directory
    src/  (35 files)
      … 35 files under this directory
    .npmignore
    .umirc.js
    LICENSE.md
    README.md
    package.json
    rollup.config.js
    tsconfig.build.json
    tsconfig.json
  element/  (252 files)
    docs/  (140 files)
      … 140 files under this directory
    src/  (103 files)
      … 103 files under this directory
    .npmignore
    README.md
    build-style.ts
    create-style.ts
    package.json
    rollup.config.js
    transformer.ts
    tsconfig.build.json
    tsconfig.json
  grid/  (9 files)
    src/  (2 files)
      … 2 files under this directory
    .npmignore
    LICENSE.md
    README.md
    package.json
    rollup.config.js
    tsconfig.build.json
    tsconfig.json
  json-schema/  (25 files)
    src/  (18 files)
      … 18 files under this directory
    .npmignore
    LICENSE.md
    README.md
    package.json
    rollup.config.js
    tsconfig.build.json
    tsconfig.json
  next/  (104 files)
    __tests__/  (2 files)
      … 2 files under this directory
    docs/  (74 files)
      … 74 files under this directory
    src/  (20 files)
      … 20 files under this directory
    .npmignore
    .umirc.js
    LESENCE.md
    README.md
    build-style.ts
    create-style.ts
    package.json
    rollup.config.js
  .eslintrc
.all-contributorsrc
.codecov.yml
.editorconfig
.eslintignore
.eslintrc
.gitignore
.prettierrc.js
.umirc.js
.yarnrc
CHANGELOG.md
LICENSE.md
README.md
README.zh-cn.md
commitlint.config.js
global.config.ts
jest.config.js
lerna.json
package.json
```

## Entry points

- [packages/antd/src/index.ts](https://github.com/alibaba/formily/blob/d9a46442a575aa5f0fc1bd945e34d9a85d191d0e/packages/antd/src/index.ts)
- [packages/benchmark/src/index.tsx](https://github.com/alibaba/formily/blob/d9a46442a575aa5f0fc1bd945e34d9a85d191d0e/packages/benchmark/src/index.tsx)
- [packages/core/src/index.ts](https://github.com/alibaba/formily/blob/d9a46442a575aa5f0fc1bd945e34d9a85d191d0e/packages/core/src/index.ts)
- [packages/element/src/index.ts](https://github.com/alibaba/formily/blob/d9a46442a575aa5f0fc1bd945e34d9a85d191d0e/packages/element/src/index.ts)
- [packages/grid/src/index.ts](https://github.com/alibaba/formily/blob/d9a46442a575aa5f0fc1bd945e34d9a85d191d0e/packages/grid/src/index.ts)
- [packages/json-schema/src/index.ts](https://github.com/alibaba/formily/blob/d9a46442a575aa5f0fc1bd945e34d9a85d191d0e/packages/json-schema/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 29 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 12 file(s) under data layer (observed from repository paths and static analysis). |
| devtools package | library | Observed | Groups 15 file(s) under devtools package (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 233 file(s) under packages package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 25 file(s) under service / domain layer (observed from repository paths and static analysis). |

## Important files

- `.codecov.yml` (config)
- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/check-pr-title.yml` (ci)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/commitlint.yml` (ci)
- `.github/workflows/issue-open-check.yml` (ci)
- `.github/workflows/package-size.yml` (ci)
- `.github/workflows/pr-welcome.yml` (ci)
- `.vscode/cspell.json` (config)
- `devtools/chrome-extension/package.json` (manifest)
- `devtools/chrome-extension/src/extension/manifest.json` (config)
- `devtools/chrome-extension/tsconfig.build.json` (config)
- `devtools/chrome-extension/tsconfig.json` (config)
- `lerna.json` (config)
- `package.json` (manifest)
- `packages/antd/package.json` (manifest)
- `packages/antd/tsconfig.build.json` (config)
- `packages/antd/tsconfig.json` (config)
- `packages/benchmark/package.json` (manifest)
- `packages/benchmark/tsconfig.build.json` (config)
- `packages/benchmark/tsconfig.json` (config)
- `packages/core/package.json` (manifest)
- `packages/core/tsconfig.build.json` (config)
- `packages/core/tsconfig.json` (config)
- `packages/element/package.json` (manifest)
- `packages/element/tsconfig.build.json` (config)
- `packages/element/tsconfig.json` (config)
- `packages/grid/package.json` (manifest)
- `packages/grid/tsconfig.build.json` (config)
- `packages/grid/tsconfig.json` (config)
- `packages/json-schema/package.json` (manifest)
- `packages/json-schema/tsconfig.build.json` (config)
- `packages/json-schema/tsconfig.json` (config)
- `packages/next/package.json` (manifest)

## Top-level layout

- `packages` — 680 analysed file(s)
- `docs` — 62 analysed file(s)
- `devtools` — 29 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `.github` — 10 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `d9a46442a575aa5f0fc1bd945e34d9a85d191d0e` is the revision these paths and observations refer to.
