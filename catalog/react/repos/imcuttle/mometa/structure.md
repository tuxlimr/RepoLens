# Project structure: imcuttle/mometa

**Analysed commit:** `ddc44915377df7c9fdaeeefeaa460a36ece49734`

**Commit reference:** [ddc44915377df7c9fdaeeefeaa460a36ece49734](https://github.com/imcuttle/mometa/commit/ddc44915377df7c9fdaeeefeaa460a36ece49734)

**Tree at this commit:** [imcuttle/mometa@ddc44915377d](https://github.com/imcuttle/mometa/tree/ddc44915377df7c9fdaeeefeaa460a36ece49734)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | imcuttle/mometa |
| Description | 🛠 [Beta] 面向研发的低代码元编程，代码可视编辑，辅助编码工具 The coding tools which is visual code editing, auxiliary and Low-code metaprogramming for R&D |
| Stars | 4085 |
| Forks | 608 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `ddc44915377df7c9fdaeeefeaa460a36ece49734` |
| Retrieved at | 2026-11-14T19:14:54.111566+00:00 |
| Files in this snapshot | 484 |

## Directory tree

```text
.github/  (3 files)
  ISSUE_TEMPLATE/  (2 files)
    bug-report.md
    feature_request.md
  workflows/  (1 files)
    test.yml
docs/  (2 files)
  client-render.svg
  how-to-work.md
packages/  (461 files)
  __template/  (9 files)
    template/  (8 files)
      … 8 files under this directory
    index.js
  app/  (41 files)
    config/  (10 files)
      … 10 files under this directory
    public/  (3 files)
      … 3 files under this directory
    scripts/  (3 files)
      … 3 files under this directory
    src/  (19 files)
      … 19 files under this directory
    .gitignore
    CHANGELOG.md
    README.md
    mometa-material.config.js
    package.json
    tsconfig.json
  app-webpack4/  (36 files)
    config/  (13 files)
      … 13 files under this directory
    public/  (3 files)
      … 3 files under this directory
    scripts/  (3 files)
      … 3 files under this directory
    src/  (7 files)
      … 7 files under this directory
    .commitlintrc.js
    .gitignore
    .prettierrc.js
    .stylelintrc.js
    CHANGELOG.md
    README.md
    mometa-material.config.js
    package.json
    saber.yml
    tsconfig.json
  editor/  (137 files)
    __template/  (3 files)
      … 3 files under this directory
    __tests__/  (5 files)
      … 5 files under this directory
    babel/  (1 files)
      … 1 files under this directory
    example/  (39 files)
      … 39 files under this directory
    src/  (62 files)
      … 62 files under this directory
    webpack/  (20 files)
      … 20 files under this directory
    .gitignore
    CHANGELOG.md
    README.md
    jest.config.js
    package.json
    tsconfig.build.json
    tsconfig.json
  fs-handler/  (26 files)
    __tests__/  (9 files)
      … 9 files under this directory
    src/  (11 files)
      … 11 files under this directory
    CHANGELOG.md
    README.md
    const.js
    jest.config.js
    package.json
    tsconfig.json
  materials-generator/  (10 files)
    src/  (4 files)
      … 4 files under this directory
    CHANGELOG.md
    README.md
    jest.config.js
    package.json
    tsconfig.json
    types.js
  materials-resolver/  (20 files)
    __tests__/  (7 files)
      … 7 files under this directory
    src/  (8 files)
      … 8 files under this directory
    CHANGELOG.md
    README.md
    jest.config.js
    package.json
    tsconfig.json
  react-docgen-typescript/  (121 files)
    __tests__/  (3 files)
      … 3 files under this directory
    src/  (113 files)
      … 113 files under this directory
    CHANGELOG.md
    README.md
    jest.config.js
    package.json
    tsconfig.json
  react-refresh-webpack-plugin/  (61 files)
    client/  (7 files)
      … 7 files under this directory
    lib/  (16 files)
      … 16 files under this directory
    loader/  (8 files)
      … 8 files under this directory
    options/  (1 files)
      … 1 files under this directory
    overlay/  (12 files)
      … 12 files under this directory
    sockets/  (8 files)
      … 8 files under this directory
    types/  (3 files)
      … 3 files under this directory
    .gitignore
    CHANGELOG.md
    LICENSE
    README.md
    package.json
    tsconfig.json
scripts/  (5 files)
  run-build.js
  run-packlimit
  run-pkgxo
  run-test
  run.js
.editorconfig
.gitattributes
.gitignore
.prettierignore
.prettierrc.js
CHANGELOG.md
License
README.md
README_zh_CN.md
lerna.json
package.json
pnpm-workspace.yaml
tsconfig.json
```

## Entry points

- [packages/react-refresh-webpack-plugin/lib/index.js](https://github.com/imcuttle/mometa/blob/ddc44915377df7c9fdaeeefeaa460a36ece49734/packages/react-refresh-webpack-plugin/lib/index.js)
- [packages/__template/index.js](https://github.com/imcuttle/mometa/blob/ddc44915377df7c9fdaeeefeaa460a36ece49734/packages/__template/index.js)
- [packages/app-webpack4/src/app.tsx](https://github.com/imcuttle/mometa/blob/ddc44915377df7c9fdaeeefeaa460a36ece49734/packages/app-webpack4/src/app.tsx)
- [packages/app-webpack4/src/index.tsx](https://github.com/imcuttle/mometa/blob/ddc44915377df7c9fdaeeefeaa460a36ece49734/packages/app-webpack4/src/index.tsx)
- [packages/app/src/index.tsx](https://github.com/imcuttle/mometa/blob/ddc44915377df7c9fdaeeefeaa460a36ece49734/packages/app/src/index.tsx)
- [packages/editor/webpack/index.js](https://github.com/imcuttle/mometa/blob/ddc44915377df7c9fdaeeefeaa460a36ece49734/packages/editor/webpack/index.js)
- [packages/fs-handler/src/index.ts](https://github.com/imcuttle/mometa/blob/ddc44915377df7c9fdaeeefeaa460a36ece49734/packages/fs-handler/src/index.ts)
- [packages/materials-generator/src/index.ts](https://github.com/imcuttle/mometa/blob/ddc44915377df7c9fdaeeefeaa460a36ece49734/packages/materials-generator/src/index.ts)
- [packages/materials-resolver/src/index.ts](https://github.com/imcuttle/mometa/blob/ddc44915377df7c9fdaeeefeaa460a36ece49734/packages/materials-resolver/src/index.ts)
- [packages/react-docgen-typescript/src/index.ts](https://github.com/imcuttle/mometa/blob/ddc44915377df7c9fdaeeefeaa460a36ece49734/packages/react-docgen-typescript/src/index.ts)
- [packages/react-refresh-webpack-plugin/loader/index.js](https://github.com/imcuttle/mometa/blob/ddc44915377df7c9fdaeeefeaa460a36ece49734/packages/react-refresh-webpack-plugin/loader/index.js)
- [packages/react-refresh-webpack-plugin/options/index.js](https://github.com/imcuttle/mometa/blob/ddc44915377df7c9fdaeeefeaa460a36ece49734/packages/react-refresh-webpack-plugin/options/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 1 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 71 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 102 file(s) under data layer (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 6 file(s) under external integrations (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 219 file(s) under packages package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 2 file(s) under scripts package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/workflows/test.yml` (ci)
- `lerna.json` (config)
- `package.json` (manifest)
- `packages/app-webpack4/package.json` (manifest)
- `packages/app-webpack4/public/manifest.json` (config)
- `packages/app-webpack4/saber.yml` (config)
- `packages/app-webpack4/tsconfig.json` (config)
- `packages/app/package.json` (manifest)
- `packages/app/public/manifest.json` (config)
- `packages/app/tsconfig.json` (config)
- `packages/editor/example/package.json` (manifest)
- `packages/editor/example/tsconfig.json` (config)
- `packages/editor/package.json` (manifest)
- `packages/editor/tsconfig.build.json` (config)
- `packages/editor/tsconfig.json` (config)
- `packages/fs-handler/package.json` (manifest)
- `packages/fs-handler/tsconfig.json` (config)
- `packages/materials-generator/package.json` (manifest)
- `packages/materials-generator/tsconfig.json` (config)
- `packages/materials-resolver/__tests__/fixture/invalid-mat-lib/package.json` (manifest)
- `packages/materials-resolver/__tests__/fixture/mat-lib/package.json` (manifest)
- `packages/materials-resolver/package.json` (manifest)
- `packages/materials-resolver/tsconfig.json` (config)
- `packages/react-docgen-typescript/package.json` (manifest)
- `packages/react-docgen-typescript/src/__tests__/data/tsconfig.json` (config)
- `packages/react-docgen-typescript/tsconfig.json` (config)
- `packages/react-refresh-webpack-plugin/client/package.json` (manifest)
- `packages/react-refresh-webpack-plugin/lib/options.json` (config)
- `packages/react-refresh-webpack-plugin/loader/options.json` (config)
- `packages/react-refresh-webpack-plugin/overlay/package.json` (manifest)
- `packages/react-refresh-webpack-plugin/package.json` (manifest)
- `packages/react-refresh-webpack-plugin/sockets/package.json` (manifest)
- `packages/react-refresh-webpack-plugin/tsconfig.json` (config)
- `pnpm-workspace.yaml` (config)
- `tsconfig.json` (config)

## Top-level layout

- `packages` — 461 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `scripts` — 5 analysed file(s)
- `.github` — 3 analysed file(s)
- `docs` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 3 file(s) were skipped during inventory (3 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `ddc44915377df7c9fdaeeefeaa460a36ece49734` is the revision these paths and observations refer to.
