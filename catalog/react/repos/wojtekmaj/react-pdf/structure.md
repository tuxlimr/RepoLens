# Project structure: wojtekmaj/react-pdf

**Analysed commit:** `f435d0bdc1fa8bc9658aa3d9d2c9e1f8da5eb219`

**Commit reference:** [f435d0bdc1fa8bc9658aa3d9d2c9e1f8da5eb219](https://github.com/wojtekmaj/react-pdf/commit/f435d0bdc1fa8bc9658aa3d9d2c9e1f8da5eb219)

**Tree at this commit:** [wojtekmaj/react-pdf@f435d0bdc1fa](https://github.com/wojtekmaj/react-pdf/tree/f435d0bdc1fa8bc9658aa3d9d2c9e1f8da5eb219)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | wojtekmaj/react-pdf |
| Description | Display PDFs in your React app as easily as if they were images. |
| Stars | 11200 |
| Forks | 1003 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `f435d0bdc1fa8bc9658aa3d9d2c9e1f8da5eb219` |
| Retrieved at | 2026-11-14T19:13:26.555827+00:00 |
| Files in this snapshot | 142 |

## Directory tree

```text
.github/  (7 files)
  ISSUE_TEMPLATE/  (3 files)
    Bug_report.yml
    Feature_request.yml
    config.yml
  workflows/  (3 files)
    ci.yml
    close-stale-issues.yml
    publish.yml
  FUNDING.yml
.husky/  (1 files)
  pre-commit
.vscode/  (2 files)
  extensions.json
  settings.json
.yarn/  (1 files)
  plugins/  (1 files)
    @yarnpkg/  (1 files)
      … 1 files under this directory
__mocks__/  (3 files)
  _failing_page.ts
  _failing_pdf.ts
  _silently_failing_pdf.ts
packages/  (56 files)
  react-pdf/  (56 files)
    src/  (49 files)
      … 49 files under this directory
    LICENSE
    README.md
    package.json
    tsconfig.build.json
    tsconfig.json
    vitest.config.ts
    vitest.setup.ts
sample/  (46 files)
  next-app/  (9 files)
    app/  (4 files)
      … 4 files under this directory
    .gitignore
    next-env.d.ts
    next.config.ts
    package.json
    tsconfig.json
  next-pages/  (10 files)
    pages/  (4 files)
      … 4 files under this directory
    .gitignore
    empty-module.ts
    next-env.d.ts
    next.config.ts
    package.json
    tsconfig.json
  parcel2/  (10 files)
    scripts/  (3 files)
      … 3 files under this directory
    .gitignore
    Sample.css
    Sample.tsx
    index.html
    index.tsx
    package.json
    tsconfig.json
  vite/  (8 files)
    .gitignore
    Sample.css
    Sample.tsx
    index.html
    index.tsx
    package.json
    tsconfig.json
    vite.config.ts
  webpack5/  (9 files)
    .babelrc
    .gitignore
    Sample.css
    Sample.tsx
    index.html
    index.tsx
    package.json
    tsconfig.json
    webpack.config.ts
test/  (18 files)
  shared/  (2 files)
    types.ts
    utils.ts
  .gitignore
  AnnotationOptions.tsx
  CustomRenderer.tsx
  LayerOptions.tsx
  LoadingOptions.tsx
  PassingOptions.tsx
  RenderingOptions.tsx
  Test.css
  Test.tsx
  ViewOptions.tsx
  global.d.ts
  index.html
  index.tsx
  package.json
  tsconfig.json
  vite.config.ts
.gitattributes
.gitignore
.mailmap
.yarnrc.yml
LICENSE
biome.json
package.json
test-utils.ts
```

## Entry points

- [packages/react-pdf/src/Page.tsx](https://github.com/wojtekmaj/react-pdf/blob/f435d0bdc1fa8bc9658aa3d9d2c9e1f8da5eb219/packages/react-pdf/src/Page.tsx)
- [packages/react-pdf/src/index.ts](https://github.com/wojtekmaj/react-pdf/blob/f435d0bdc1fa8bc9658aa3d9d2c9e1f8da5eb219/packages/react-pdf/src/index.ts)
- [sample/next-app/app/page.tsx](https://github.com/wojtekmaj/react-pdf/blob/f435d0bdc1fa8bc9658aa3d9d2c9e1f8da5eb219/sample/next-app/app/page.tsx)
- [sample/next-pages/pages/index.tsx](https://github.com/wojtekmaj/react-pdf/blob/f435d0bdc1fa8bc9658aa3d9d2c9e1f8da5eb219/sample/next-pages/pages/index.tsx)
- [sample/parcel2/index.tsx](https://github.com/wojtekmaj/react-pdf/blob/f435d0bdc1fa8bc9658aa3d9d2c9e1f8da5eb219/sample/parcel2/index.tsx)
- [sample/vite/index.tsx](https://github.com/wojtekmaj/react-pdf/blob/f435d0bdc1fa8bc9658aa3d9d2c9e1f8da5eb219/sample/vite/index.tsx)
- [sample/webpack5/index.tsx](https://github.com/wojtekmaj/react-pdf/blob/f435d0bdc1fa8bc9658aa3d9d2c9e1f8da5eb219/sample/webpack5/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 15 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| __mocks__ package | library | Observed | Groups 3 file(s) under __mocks__ package (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 49 file(s) under packages package (observed from repository paths and static analysis). |
| sample package | library | Observed | Groups 22 file(s) under sample package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 18 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/Bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/Feature_request.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/close-stale-issues.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.vscode/extensions.json` (config)
- `.vscode/settings.json` (config)
- `.yarnrc.yml` (config)
- `biome.json` (config)
- `package.json` (manifest)
- `packages/react-pdf/package.json` (manifest)
- `packages/react-pdf/tsconfig.build.json` (config)
- `packages/react-pdf/tsconfig.json` (config)
- `sample/next-app/package.json` (manifest)
- `sample/next-app/tsconfig.json` (config)
- `sample/next-pages/package.json` (manifest)
- `sample/next-pages/tsconfig.json` (config)
- `sample/parcel2/package.json` (manifest)
- `sample/parcel2/tsconfig.json` (config)
- `sample/vite/package.json` (manifest)
- `sample/vite/tsconfig.json` (config)
- `sample/webpack5/package.json` (manifest)
- `sample/webpack5/tsconfig.json` (config)

## Top-level layout

- `packages` — 56 analysed file(s)
- `sample` — 46 analysed file(s)
- `test` — 18 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `.github` — 7 analysed file(s)
- `__mocks__` — 3 analysed file(s)
- `.vscode` — 2 analysed file(s)
- `.husky` — 1 analysed file(s)
- `.yarn` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 5 file(s) were skipped during inventory (5 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `f435d0bdc1fa8bc9658aa3d9d2c9e1f8da5eb219` is the revision these paths and observations refer to.
