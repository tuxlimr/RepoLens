# Project structure: alibaba/designable

**Analysed commit:** `3e961de947011df6ac5cd092c1084140494f5fc2`

**Commit reference:** [3e961de947011df6ac5cd092c1084140494f5fc2](https://github.com/alibaba/designable/commit/3e961de947011df6ac5cd092c1084140494f5fc2)

**Tree at this commit:** [alibaba/designable@3e961de94701](https://github.com/alibaba/designable/tree/3e961de947011df6ac5cd092c1084140494f5fc2)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | alibaba/designable |
| Description | 🧩 Make everything designable 🧩  |
| Stars | 3522 |
| Forks | 728 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `3e961de947011df6ac5cd092c1084140494f5fc2` |
| Retrieved at | 2026-11-14T19:15:15.934912+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.github/  (11 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    config.yml
  workflows/  (5 files)
    check-pr-title.yml
    ci.yml
    commitlint.yml
    package-size.yml
    pr-welcome.yml
  CONTRIBUTING.md
  FUNDING.yml
  GIT_COMMIT_SPECIFIC.md
  PULL_REQUEST_TEMPLATE.md
.vscode/  (1 files)
  cspell.json
examples/  (52 files)
  basic/  (13 files)
    config/  (4 files)
      … 4 files under this directory
    src/  (3 files)
      … 3 files under this directory
    .npmignore
    LICENSE.md
    README.md
    package.json
    tsconfig.build.json
    tsconfig.json
  multi-workspace/  (12 files)
    config/  (4 files)
      … 4 files under this directory
    src/  (2 files)
      … 2 files under this directory
    .npmignore
    LICENSE.md
    README.md
    package.json
    tsconfig.build.json
    tsconfig.json
  sandbox/  (13 files)
    config/  (4 files)
      … 4 files under this directory
    src/  (3 files)
      … 3 files under this directory
    .npmignore
    LICENSE.md
    README.md
    package.json
    tsconfig.build.json
    tsconfig.json
  sandbox-multi-workspace/  (13 files)
    config/  (4 files)
      … 4 files under this directory
    src/  (3 files)
      … 3 files under this directory
    .npmignore
    LICENSE.md
    README.md
    package.json
    tsconfig.build.json
    tsconfig.json
  .eslintrc
formily/  (347 files)
  antd/  (153 files)
    playground/  (13 files)
      … 13 files under this directory
    src/  (132 files)
      … 132 files under this directory
    .npmignore
    .umirc.js
    LICENSE.md
    README.md
    copy.ts
    package.json
    tsconfig.build.json
    tsconfig.json
  next/  (154 files)
    playground/  (13 files)
      … 13 files under this directory
    src/  (133 files)
      … 133 files under this directory
    .npmignore
    .umirc.js
    LICENSE.md
    README.md
    copy.ts
    package.json
    tsconfig.build.json
    tsconfig.json
  setters/  (31 files)
    src/  (23 files)
      … 23 files under this directory
    .npmignore
    .umirc.js
    LICENSE.md
    README.md
    copy.ts
    package.json
    tsconfig.build.json
    tsconfig.json
  transformer/  (8 files)
    src/  (1 files)
      … 1 files under this directory
    .npmignore
    LICENSE.md
    README.md
    package.json
    rollup.config.js
    tsconfig.build.json
    tsconfig.json
  .eslintrc
packages/  (368 files)
  core/  (103 files)
    src/  (96 files)
      … 96 files under this directory
    .npmignore
    LICENSE.md
    README.md
    package.json
    rollup.config.js
    tsconfig.build.json
    tsconfig.json
  react/  (168 files)
    src/  (160 files)
      … 160 files under this directory
    .npmignore
    LICENSE.md
    README.md
    copy.ts
    package.json
    rollup.config.js
    tsconfig.build.json
    tsconfig.json
  react-sandbox/  (8 files)
    src/  (1 files)
      … 1 files under this directory
    .npmignore
    LICENSE.md
    README.md
    package.json
    rollup.config.js
    tsconfig.build.json
    tsconfig.json
  react-settings-form/  (63 files)
    src/  (55 files)
      … 55 files under this directory
    .npmignore
    LICENSE.md
    README.md
    copy.ts
    package.json
    rollup.config.js
    tsconfig.build.json
    tsconfig.json
  shared/  (25 files)
    src/  (18 files)
      … 18 files under this directory
    .npmignore
    LICENSE.md
    README.md
    package.json
    rollup.config.js
    tsconfig.build.json
    tsconfig.json
  .eslintrc
scripts/  (8 files)
  build-style/  (5 files)
    buildAllStyles.ts
    buildStyle.ts
    copy.ts
    helper.ts
    index.ts
  release/  (1 files)
    git.ts
  global.ts
  jest.base.js
.editorconfig
.eslintignore
.eslintrc
.gitignore
.prettierrc.js
.travis.yml
.yarnrc
CHANGELOG.md
LICENSE
README.md
jest.config.js
lerna.json
package.json
```

## Entry points

- [formily/antd/playground/main.tsx](https://github.com/alibaba/designable/blob/3e961de947011df6ac5cd092c1084140494f5fc2/formily/antd/playground/main.tsx)
- [formily/antd/src/index.ts](https://github.com/alibaba/designable/blob/3e961de947011df6ac5cd092c1084140494f5fc2/formily/antd/src/index.ts)
- [formily/next/playground/main.tsx](https://github.com/alibaba/designable/blob/3e961de947011df6ac5cd092c1084140494f5fc2/formily/next/playground/main.tsx)
- [formily/next/src/index.ts](https://github.com/alibaba/designable/blob/3e961de947011df6ac5cd092c1084140494f5fc2/formily/next/src/index.ts)
- [formily/setters/src/index.ts](https://github.com/alibaba/designable/blob/3e961de947011df6ac5cd092c1084140494f5fc2/formily/setters/src/index.ts)
- [formily/transformer/src/index.ts](https://github.com/alibaba/designable/blob/3e961de947011df6ac5cd092c1084140494f5fc2/formily/transformer/src/index.ts)
- [packages/core/src/index.ts](https://github.com/alibaba/designable/blob/3e961de947011df6ac5cd092c1084140494f5fc2/packages/core/src/index.ts)
- [packages/react-sandbox/src/index.ts](https://github.com/alibaba/designable/blob/3e961de947011df6ac5cd092c1084140494f5fc2/packages/react-sandbox/src/index.ts)
- [packages/react-settings-form/src/index.ts](https://github.com/alibaba/designable/blob/3e961de947011df6ac5cd092c1084140494f5fc2/packages/react-settings-form/src/index.ts)
- [packages/react/src/index.ts](https://github.com/alibaba/designable/blob/3e961de947011df6ac5cd092c1084140494f5fc2/packages/react/src/index.ts)
- [packages/shared/src/index.ts](https://github.com/alibaba/designable/blob/3e961de947011df6ac5cd092c1084140494f5fc2/packages/shared/src/index.ts)
- [scripts/build-style/index.ts](https://github.com/alibaba/designable/blob/3e961de947011df6ac5cd092c1084140494f5fc2/scripts/build-style/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 29 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 18 file(s) under data layer (observed from repository paths and static analysis). |
| formily package | library | Observed | Groups 302 file(s) under formily package (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 205 file(s) under packages package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 8 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 83 file(s) under service / domain layer (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/check-pr-title.yml` (ci)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/commitlint.yml` (ci)
- `.github/workflows/package-size.yml` (ci)
- `.github/workflows/pr-welcome.yml` (ci)
- `.travis.yml` (ci)
- `.vscode/cspell.json` (config)
- `examples/basic/package.json` (manifest)
- `examples/basic/tsconfig.build.json` (config)
- `examples/basic/tsconfig.json` (config)
- `examples/multi-workspace/package.json` (manifest)
- `examples/multi-workspace/tsconfig.build.json` (config)
- `examples/multi-workspace/tsconfig.json` (config)
- `examples/sandbox-multi-workspace/package.json` (manifest)
- `examples/sandbox-multi-workspace/tsconfig.build.json` (config)
- `examples/sandbox-multi-workspace/tsconfig.json` (config)
- `examples/sandbox/package.json` (manifest)
- `examples/sandbox/tsconfig.build.json` (config)
- `examples/sandbox/tsconfig.json` (config)
- `formily/antd/package.json` (manifest)
- `formily/antd/tsconfig.build.json` (config)
- `formily/antd/tsconfig.json` (config)
- `formily/next/package.json` (manifest)
- `formily/next/tsconfig.build.json` (config)
- `formily/next/tsconfig.json` (config)
- `formily/setters/package.json` (manifest)
- `formily/setters/tsconfig.build.json` (config)
- `formily/setters/tsconfig.json` (config)
- `formily/transformer/package.json` (manifest)
- `formily/transformer/tsconfig.build.json` (config)
- `formily/transformer/tsconfig.json` (config)
- `lerna.json` (config)
- `package.json` (manifest)
- `packages/core/package.json` (manifest)
- `packages/core/tsconfig.build.json` (config)
- `packages/core/tsconfig.json` (config)
- `packages/react-sandbox/package.json` (manifest)
- `packages/react-sandbox/tsconfig.build.json` (config)
- `packages/react-sandbox/tsconfig.json` (config)
- `packages/react-settings-form/package.json` (manifest)
- `packages/react-settings-form/tsconfig.build.json` (config)
- `packages/react-settings-form/tsconfig.json` (config)
- `packages/react/package.json` (manifest)
- `packages/react/tsconfig.build.json` (config)
- `packages/react/tsconfig.json` (config)
- `packages/shared/package.json` (manifest)
- `packages/shared/tsconfig.build.json` (config)
- `packages/shared/tsconfig.json` (config)

## Top-level layout

- `packages` — 368 analysed file(s)
- `formily` — 347 analysed file(s)
- `examples` — 52 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `.github` — 11 analysed file(s)
- `scripts` — 8 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `3e961de947011df6ac5cd092c1084140494f5fc2` is the revision these paths and observations refer to.
