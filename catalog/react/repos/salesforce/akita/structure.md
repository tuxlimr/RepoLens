# Project structure: salesforce/akita

**Analysed commit:** `9997049301febe22b4e9cdd2a3637bada2356aaf`

**Commit reference:** [9997049301febe22b4e9cdd2a3637bada2356aaf](https://github.com/salesforce/akita/commit/9997049301febe22b4e9cdd2a3637bada2356aaf)

**Tree at this commit:** [salesforce/akita@9997049301fe](https://github.com/salesforce/akita/tree/9997049301febe22b4e9cdd2a3637bada2356aaf)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | salesforce/akita |
| Description | 🚀 State Management Tailored-Made for JS Applications |
| Stars | 3661 |
| Forks | 333 |
| Licence | Apache-2.0 |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `9997049301febe22b4e9cdd2a3637bada2356aaf` |
| Retrieved at | 2026-11-14T19:15:10.767302+00:00 |
| Files in this snapshot | 378 |

## Directory tree

```text
.github/  (7 files)
  ISSUE_TEMPLATE/  (3 files)
    1-bug-report.yaml
    2-feature-request.yaml
    3-support-request.md
  workflows/  (3 files)
    ci.yml
    deploy-sample-app.yml
    docs.yml
  PULL_REQUEST_TEMPLATE.md
.husky/  (2 files)
  .gitignore
  commit-msg
.vscode/  (2 files)
  extensions.json
  settings.json
docs/  (49 files)
  docs/  (36 files)
    additional/  (10 files)
      … 10 files under this directory
    angular/  (7 files)
      … 7 files under this directory
    enhancers/  (4 files)
      … 4 files under this directory
    entities/  (4 files)
      … 4 files under this directory
    plugins/  (3 files)
      … 3 files under this directory
    best-practices.mdx
    config.mdx
    immer.mdx
    installation.mdx
    query.mdx
    store.mdx
    transactions.mdx
    ui.mdx
  src/  (6 files)
    components/  (2 files)
      … 2 files under this directory
    css/  (1 files)
      … 1 files under this directory
    pages/  (3 files)
      … 3 files under this directory
  static/  (2 files)
    img/  (1 files)
      … 1 files under this directory
    .nojekyll
  .gitignore
  README.md
  docusaurus.config.js
  package.json
  sidebars.js
packages/  (293 files)
  akita/  (143 files)
    src/  (133 files)
      … 133 files under this directory
    .babelrc
    .eslintrc.json
    CHANGELOG.md
    README.md
    jest.config.ts
    package.json
    project.json
    tsconfig.json
    tsconfig.lib.json
    tsconfig.spec.json
  ng-entity-service/  (22 files)
    src/  (11 files)
      … 11 files under this directory
    .eslintrc.json
    CHANGELOG.md
    README.md
    jest.config.js
    ng-package.json
    package.json
    project.json
    tsconfig.json
    tsconfig.lib.json
    tsconfig.lib.prod.json
    tsconfig.spec.json
  ng-playground/  (109 files)
    src/  (102 files)
      … 102 files under this directory
    .eslintrc.json
    jest.config.ts
    project.json
    tsconfig.app.json
    tsconfig.editor.json
    tsconfig.json
    tsconfig.spec.json
  ng-router-store/  (18 files)
    src/  (7 files)
      … 7 files under this directory
    .eslintrc.json
    CHANGELOG.md
    README.md
    jest.config.ts
    ng-package.json
    package.json
    project.json
    tsconfig.json
    tsconfig.lib.json
    tsconfig.lib.prod.json
    tsconfig.spec.json
  .gitkeep
tools/  (2 files)
  generators/  (1 files)
    .gitkeep
  tsconfig.tools.json
.commitlintrc.json
.editorconfig
.eslintrc.json
.gitattributes
.gitignore
.prettierignore
.prettierrc
BREAKING_CHANGES.md
CODEOWNERS
CODE_OF_CONDUCT.md
CONTRIBUTING-ARCHIVED.md
CONTRIBUTING.md
LICENSE
README.md
SECURITY.md
changelog.config.js
jest.config.ts
jest.preset.js
migrations.json
nx.json
package.json
tsconfig.base.json
workspace.json
```

## Entry points

- [packages/akita/src/index.ts](https://github.com/salesforce/akita/blob/9997049301febe22b4e9cdd2a3637bada2356aaf/packages/akita/src/index.ts)
- [packages/ng-entity-service/src/index.ts](https://github.com/salesforce/akita/blob/9997049301febe22b4e9cdd2a3637bada2356aaf/packages/ng-entity-service/src/index.ts)
- [packages/ng-playground/src/main.ts](https://github.com/salesforce/akita/blob/9997049301febe22b4e9cdd2a3637bada2356aaf/packages/ng-playground/src/main.ts)
- [packages/ng-router-store/src/index.ts](https://github.com/salesforce/akita/blob/9997049301febe22b4e9cdd2a3637bada2356aaf/packages/ng-router-store/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 34 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 236 file(s) under packages package (observed from repository paths and static analysis). |

## Important files

- `.commitlintrc.json` (config)
- `.editorconfig` (config)
- `.eslintrc.json` (config)
- `.github/ISSUE_TEMPLATE/1-bug-report.yaml` (config)
- `.github/ISSUE_TEMPLATE/2-feature-request.yaml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/deploy-sample-app.yml` (ci)
- `.github/workflows/docs.yml` (ci)
- `.vscode/extensions.json` (config)
- `.vscode/settings.json` (config)
- `docs/package.json` (manifest)
- `migrations.json` (config)
- `nx.json` (config)
- `package.json` (manifest)
- `packages/akita/.eslintrc.json` (config)
- `packages/akita/package.json` (manifest)
- `packages/akita/project.json` (config)
- `packages/akita/tsconfig.json` (config)
- `packages/akita/tsconfig.lib.json` (config)
- `packages/akita/tsconfig.spec.json` (config)
- `packages/ng-entity-service/.eslintrc.json` (config)
- `packages/ng-entity-service/ng-package.json` (config)
- `packages/ng-entity-service/package.json` (manifest)
- `packages/ng-entity-service/project.json` (config)
- `packages/ng-entity-service/tsconfig.json` (config)
- `packages/ng-entity-service/tsconfig.lib.json` (config)
- `packages/ng-entity-service/tsconfig.lib.prod.json` (config)
- `packages/ng-entity-service/tsconfig.spec.json` (config)
- `packages/ng-playground/.eslintrc.json` (config)
- `packages/ng-playground/project.json` (config)
- `packages/ng-playground/tsconfig.app.json` (config)
- `packages/ng-playground/tsconfig.editor.json` (config)
- `packages/ng-playground/tsconfig.json` (config)
- `packages/ng-playground/tsconfig.spec.json` (config)
- `packages/ng-router-store/.eslintrc.json` (config)
- `packages/ng-router-store/ng-package.json` (config)
- `packages/ng-router-store/package.json` (manifest)
- `packages/ng-router-store/project.json` (config)
- `packages/ng-router-store/tsconfig.json` (config)
- `packages/ng-router-store/tsconfig.lib.json` (config)
- `packages/ng-router-store/tsconfig.lib.prod.json` (config)
- `packages/ng-router-store/tsconfig.spec.json` (config)
- `tools/tsconfig.tools.json` (config)
- `tsconfig.base.json` (config)
- `workspace.json` (config)

## Top-level layout

- `packages` — 293 analysed file(s)
- `docs` — 49 analysed file(s)
- `(root files)` — 23 analysed file(s)
- `.github` — 7 analysed file(s)
- `.husky` — 2 analysed file(s)
- `.vscode` — 2 analysed file(s)
- `tools` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `9997049301febe22b4e9cdd2a3637bada2356aaf` is the revision these paths and observations refer to.
