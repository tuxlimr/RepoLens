# Project structure: AykutSarac/jsoncrack.com

**Analysed commit:** `a46d0d0adb098e12e577a083e87ead7f61f90098`

**Commit reference:** [a46d0d0adb098e12e577a083e87ead7f61f90098](https://github.com/AykutSarac/jsoncrack.com/commit/a46d0d0adb098e12e577a083e87ead7f61f90098)

**Tree at this commit:** [AykutSarac/jsoncrack.com@a46d0d0adb09](https://github.com/AykutSarac/jsoncrack.com/tree/a46d0d0adb098e12e577a083e87ead7f61f90098)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | AykutSarac/jsoncrack.com |
| Description | ✨ Innovative and open-source visualization application that transforms various data formats, such as JSON, YAML, XML and CSV into interactive graphs. |
| Stars | 44595 |
| Forks | 3588 |
| Licence | Apache-2.0 |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `a46d0d0adb098e12e577a083e87ead7f61f90098` |
| Retrieved at | 2026-11-14T19:12:58.408759+00:00 |
| Files in this snapshot | 183 |

## Directory tree

```text
.github/  (5 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.yml
    feature_request.yml
  workflows/  (2 files)
    deploy.yml
    pull-request.yml
  pull_request_template.md
.vscode/  (2 files)
  launch.json
  tasks.json
apps/  (134 files)
  chrome-extension/  (12 files)
    public/  (2 files)
      … 2 files under this directory
    src/  (3 files)
      … 3 files under this directory
    .gitignore
    PRIVACY.md
    README.md
    package.json
    tsconfig.json
    vite.config.ts
    zip.sh
  vscode/  (21 files)
    assets/  (2 files)
      … 2 files under this directory
    ext-src/  (2 files)
      … 2 files under this directory
    src/  (5 files)
      … 5 files under this directory
    .gitignore
    .prettierignore
    .prettierrc
    .vscodeignore
    LICENSE.md
    README.md
    esbuild.config.mjs
    eslint.config.mjs
    index.html
    package.json
    tsconfig.json
    vite.config.ts
  www/  (101 files)
    public/  (8 files)
      … 8 files under this directory
    shims/  (1 files)
      … 1 files under this directory
    src/  (78 files)
      … 78 files under this directory
    .dockerignore
    .gitignore
    .prettierignore
    .prettierrc
    Dockerfile
    LICENSE.md
    docker-compose.yml
    eslint.config.mjs
    next-env.d.ts
    next-sitemap.config.js
    next.config.js
    nginx.conf
    package.json
    tsconfig.json
packages/  (34 files)
  jsoncrack-react/  (34 files)
    src/  (24 files)
      … 24 files under this directory
    .gitignore
    .prettierrc
    CHANGELOG.md
    LICENSE.md
    README.md
    eslint.config.mjs
    package.json
    tsconfig.build.json
    tsconfig.json
    vite.config.ts
.gitignore
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE.md
README.md
package.json
pnpm-workspace.yaml
turbo.json
```

## Entry points

- [apps/vscode/src/App.tsx](https://github.com/AykutSarac/jsoncrack.com/blob/a46d0d0adb098e12e577a083e87ead7f61f90098/apps/vscode/src/App.tsx)
- [apps/vscode/src/index.tsx](https://github.com/AykutSarac/jsoncrack.com/blob/a46d0d0adb098e12e577a083e87ead7f61f90098/apps/vscode/src/index.tsx)
- [packages/jsoncrack-react/src/index.ts](https://github.com/AykutSarac/jsoncrack.com/blob/a46d0d0adb098e12e577a083e87ead7f61f90098/packages/jsoncrack-react/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 11 file(s) under api layer (observed from repository paths and static analysis). |
| apps package | library | Observed | Groups 81 file(s) under apps package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 21 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 22 file(s) under packages package (observed from repository paths and static analysis). |

## Important files

- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/workflows/deploy.yml` (ci)
- `.github/workflows/pull-request.yml` (ci)
- `.vscode/launch.json` (config)
- `.vscode/tasks.json` (config)
- `apps/chrome-extension/package.json` (manifest)
- `apps/chrome-extension/public/manifest.json` (config)
- `apps/chrome-extension/tsconfig.json` (config)
- `apps/vscode/package.json` (manifest)
- `apps/vscode/tsconfig.json` (config)
- `apps/www/.dockerignore` (container)
- `apps/www/Dockerfile` (container)
- `apps/www/docker-compose.yml` (container)
- `apps/www/package.json` (manifest)
- `apps/www/public/manifest.json` (config)
- `apps/www/src/data/example.json` (config)
- `apps/www/src/data/faq.json` (config)
- `apps/www/src/data/privacy.json` (config)
- `apps/www/src/data/terms.json` (config)
- `apps/www/tsconfig.json` (config)
- `package.json` (manifest)
- `packages/jsoncrack-react/package.json` (manifest)
- `packages/jsoncrack-react/tsconfig.build.json` (config)
- `packages/jsoncrack-react/tsconfig.json` (config)
- `pnpm-workspace.yaml` (config)
- `turbo.json` (config)

## Top-level layout

- `apps` — 134 analysed file(s)
- `packages` — 34 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `.github` — 5 analysed file(s)
- `.vscode` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 3 file(s) were skipped during inventory (3 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `a46d0d0adb098e12e577a083e87ead7f61f90098` is the revision these paths and observations refer to.
