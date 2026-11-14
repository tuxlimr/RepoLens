# Project structure: pacexy/flow

**Analysed commit:** `36f3cc7c4581f62ff6d72b75641c674020bb1e9f`

**Commit reference:** [36f3cc7c4581f62ff6d72b75641c674020bb1e9f](https://github.com/pacexy/flow/commit/36f3cc7c4581f62ff6d72b75641c674020bb1e9f)

**Tree at this commit:** [pacexy/flow@36f3cc7c4581](https://github.com/pacexy/flow/tree/36f3cc7c4581f62ff6d72b75641c674020bb1e9f)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | pacexy/flow |
| Description | Browser-based ePub reader |
| Stars | 3385 |
| Forks | 295 |
| Licence | AGPL-3.0 |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `36f3cc7c4581f62ff6d72b75641c674020bb1e9f` |
| Retrieved at | 2026-11-14T19:15:21.658900+00:00 |
| Files in this snapshot | 296 |

## Directory tree

```text
.github/  (1 files)
  FUNDING.yml
.husky/  (1 files)
  pre-commit
.vscode/  (1 files)
  settings.json
apps/  (116 files)
  reader/  (92 files)
    locales/  (5 files)
      … 5 files under this directory
    public/  (1 files)
      … 1 files under this directory
    src/  (74 files)
      … 74 files under this directory
    .eslintrc.js
    .gitignore
    netlify.toml
    next-env.d.ts
    next.config.js
    package.json
    postcss.config.js
    sentry.client.config.js
    sentry.properties
    sentry.server.config.js
    tailwind.config.js
    tsconfig.json
  website/  (24 files)
    locales/  (3 files)
      … 3 files under this directory
    plugins/  (1 files)
      … 1 files under this directory
    src/  (11 files)
      … 11 files under this directory
    .eslintrc.js
    i18n.js
    netlify.toml
    next-env.d.ts
    next.config.js
    package.json
    postcss.config.js
    tailwind.config.js
    tsconfig.json
packages/  (160 files)
  epubjs/  (150 files)
    documentation/  (1 files)
      … 1 files under this directory
    examples/  (30 files)
      … 30 files under this directory
    src/  (38 files)
      … 38 files under this directory
    test/  (30 files)
      … 30 files under this directory
    types/  (35 files)
      … 35 files under this directory
    .babelrc.json
    .eslintrc.js
    .gitignore
    .jshintrc
    .nojekyll
    .npmignore
    .travis.yml
    .watchmanconfig
    README.md
    bower.json
    documentation.yml
    karma.conf.js
    license
    package.json
    tsconfig.json
    webpack.config.js
  internal/  (4 files)
    src/  (2 files)
      … 2 files under this directory
    package.json
    tsconfig.json
  tailwind/  (6 files)
    src/  (5 files)
      … 5 files under this directory
    package.json
.dockerignore
.eslintrc.js
.gitattributes
.gitignore
AGENTS.md
Dockerfile
LICENSE
README.md
docker-compose.yml
package.json
pnpm-workspace.yaml
prettier.config.js
tsconfig.json
tsconfig.next.json
tsconfig.react.json
tsconfig.ts.json
turbo.json
```

## Entry points

- [packages/epubjs/src/index.js](https://github.com/pacexy/flow/blob/36f3cc7c4581f62ff6d72b75641c674020bb1e9f/packages/epubjs/src/index.js)
- [packages/internal/src/index.ts](https://github.com/pacexy/flow/blob/36f3cc7c4581f62ff6d72b75641c674020bb1e9f/packages/internal/src/index.ts)
- [packages/tailwind/src/index.js](https://github.com/pacexy/flow/blob/36f3cc7c4581f62ff6d72b75641c674020bb1e9f/packages/tailwind/src/index.js)
- [apps/reader/locales/index.ts](https://github.com/pacexy/flow/blob/36f3cc7c4581f62ff6d72b75641c674020bb1e9f/apps/reader/locales/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 5 file(s) under api layer (observed from repository paths and static analysis). |
| apps package | library | Observed | Groups 92 file(s) under apps package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 30 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 3 file(s) under data layer (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 80 file(s) under packages package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 30 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.github/FUNDING.yml` (config)
- `.vscode/settings.json` (config)
- `Dockerfile` (container)
- `apps/reader/netlify.toml` (config)
- `apps/reader/package.json` (manifest)
- `apps/reader/public/manifest.json` (config)
- `apps/reader/tsconfig.json` (config)
- `apps/website/locales/en-US.json` (config)
- `apps/website/locales/ja-JP.json` (config)
- `apps/website/locales/zh-CN.json` (config)
- `apps/website/netlify.toml` (config)
- `apps/website/package.json` (manifest)
- `apps/website/tsconfig.json` (config)
- `docker-compose.yml` (container)
- `package.json` (manifest)
- `packages/epubjs/.babelrc.json` (config)
- `packages/epubjs/.travis.yml` (ci)
- `packages/epubjs/bower.json` (config)
- `packages/epubjs/documentation.yml` (config)
- `packages/epubjs/package.json` (manifest)
- `packages/epubjs/tsconfig.json` (config)
- `packages/epubjs/types/tsconfig.json` (config)
- `packages/epubjs/types/tslint.json` (config)
- `packages/internal/package.json` (manifest)
- `packages/internal/tsconfig.json` (config)
- `packages/tailwind/package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `tsconfig.json` (config)
- `tsconfig.next.json` (config)
- `tsconfig.react.json` (config)
- `tsconfig.ts.json` (config)
- `turbo.json` (config)

## Top-level layout

- `packages` — 160 analysed file(s)
- `apps` — 116 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `.github` — 1 analysed file(s)
- `.husky` — 1 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 3 file(s) were skipped during inventory (3 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `36f3cc7c4581f62ff6d72b75641c674020bb1e9f` is the revision these paths and observations refer to.
