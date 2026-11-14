# Project structure: orval-labs/orval

**Analysed commit:** `4d82f9584ff687adcafd10f3acc1b66ac4e45520`

**Commit reference:** [4d82f9584ff687adcafd10f3acc1b66ac4e45520](https://github.com/orval-labs/orval/commit/4d82f9584ff687adcafd10f3acc1b66ac4e45520)

**Tree at this commit:** [orval-labs/orval@4d82f9584ff6](https://github.com/orval-labs/orval/tree/4d82f9584ff687adcafd10f3acc1b66ac4e45520)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | orval-labs/orval |
| Description | orval is able to generate client with appropriate type-signatures (TypeScript) from any valid OpenAPI v3 or Swagger v2 specification, either in yaml or json formats. 🍺 |
| Stars | 6614 |
| Forks | 711 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `4d82f9584ff687adcafd10f3acc1b66ac4e45520` |
| Retrieved at | 2026-11-14T19:14:04.276005+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.claude-plugin/  (1 files)
  marketplace.json
.devcontainer/  (3 files)
  Dockerfile
  devcontainer-lock.json
  devcontainer.json
.github/  (14 files)
  ISSUE_TEMPLATE/  (4 files)
    bug_report.yml
    config.yml
    feature_request.yml
    other.yml
  workflows/  (7 files)
    deploy-doc.yaml
    docker-publish.yaml
    issue-labeler.yaml
    pr-checks.yaml
    release-prepare.yaml
    release-publish.yaml
    stale.yaml
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
.vite-hooks/  (2 files)
  commit-msg
  pre-commit
.vscode/  (2 files)
  extensions.json
  settings.json
docs/  (130 files)
  content/  (86 files)
    docs/  (86 files)
      … 86 files under this directory
  plugins/  (1 files)
    generate-md-pages.ts
  public/  (3 files)
    images/  (3 files)
      … 3 files under this directory
  scripts/  (1 files)
    check-i18n-coverage.ts
  src/  (29 files)
    components/  (10 files)
      … 10 files under this directory
    lib/  (8 files)
      … 8 files under this directory
    routes/  (8 files)
      … 8 files under this directory
    styles/  (1 files)
      … 1 files under this directory
    routeTree.gen.ts
    router.tsx
  .gitignore
  README.md
  biome.json
  bun.lock
  package.json
  site.config.json
  source.config.ts
  tsconfig.json
  vite.config.ts
  wrangler.jsonc
logo/  (1 files)
  orval-logo-horizontal.svg
packages/  (512 files)
  angular/  (20 files)
    src/  (15 files)
      … 15 files under this directory
    README.md
    package.json
    tsconfig.build.json
    tsconfig.json
    vite.config.ts
  axios/  (7 files)
    src/  (2 files)
      … 2 files under this directory
    README.md
    package.json
    tsconfig.build.json
    tsconfig.json
    vite.config.ts
  core/  (248 files)
    src/  (243 files)
      … 243 files under this directory
    README.md
    package.json
    tsconfig.build.json
    tsconfig.json
    vite.config.ts
  effect/  (10 files)
    src/  (5 files)
      … 5 files under this directory
    README.md
    package.json
    tsconfig.build.json
    tsconfig.json
    vite.config.ts
  fetch/  (14 files)
    src/  (9 files)
      … 9 files under this directory
    README.md
    package.json
    tsconfig.build.json
    tsconfig.json
    vite.config.ts
  hono/  (14 files)
    src/  (9 files)
      … 9 files under this directory
    README.md
    package.json
    tsconfig.build.json
    tsconfig.json
    vite.config.ts
  mcp/  (7 files)
    src/  (2 files)
      … 2 files under this directory
    README.md
    package.json
    tsconfig.build.json
    tsconfig.json
    vite.config.ts
  mock/  (38 files)
    src/  (33 files)
      … 33 files under this directory
    README.md
    package.json
    tsconfig.build.json
    tsconfig.json
    vite.config.ts
  orval/  (46 files)
    src/  (41 files)
      … 41 files under this directory
    README.md
    package.json
    tsconfig.build.json
    tsconfig.json
    vite.config.ts
  pinia-colada/  (6 files)
    src/  (2 files)
      … 2 files under this directory
    package.json
    tsconfig.build.json
    tsconfig.json
    vite.config.ts
  query/  (33 files)
    src/  (27 files)
      … 27 files under this directory
    DEVELOPMENT.md
    README.md
    package.json
    tsconfig.build.json
    tsconfig.json
    vite.config.ts
  solid-start/  (8 files)
    src/  (3 files)
      … 3 files under this directory
    README.md
    package.json
    tsconfig.build.json
    tsconfig.json
    vite.config.ts
  swr/  (9 files)
    src/  (4 files)
      … 4 files under this directory
    README.md
    package.json
    tsconfig.build.json
    tsconfig.json
    vite.config.ts
  valibot/  (37 files)
    src/  (32 files)
      … 32 files under this directory
    README.md
    package.json
    tsconfig.build.json
    tsconfig.json
    vite.config.ts
  zod/  (14 files)
    src/  (9 files)
      … 9 files under this directory
    README.md
    package.json
    tsconfig.build.json
    tsconfig.json
    vite.config.ts
  vite.config.base.ts
samples/  (118 files)
  angular-app/  (117 files)
    __snapshots__/  (116 files)
      … 116 files under this directory
    .gitignore
  README.md
.coderabbit.yaml
.dockerignore
.gitattributes
.gitignore
.prettierrc.json
AGENTS.md
ARCHITECTURE.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
DEBUGGING.md
Dockerfile
LICENSE
README.md
SECURITY.md
bunfig.toml
commitlint.config.mjs
package.json
```

## Entry points

- [packages/angular/src/index.ts](https://github.com/orval-labs/orval/blob/4d82f9584ff687adcafd10f3acc1b66ac4e45520/packages/angular/src/index.ts)
- [packages/axios/src/index.ts](https://github.com/orval-labs/orval/blob/4d82f9584ff687adcafd10f3acc1b66ac4e45520/packages/axios/src/index.ts)
- [packages/core/src/index.ts](https://github.com/orval-labs/orval/blob/4d82f9584ff687adcafd10f3acc1b66ac4e45520/packages/core/src/index.ts)
- [packages/effect/src/index.ts](https://github.com/orval-labs/orval/blob/4d82f9584ff687adcafd10f3acc1b66ac4e45520/packages/effect/src/index.ts)
- [packages/fetch/src/index.ts](https://github.com/orval-labs/orval/blob/4d82f9584ff687adcafd10f3acc1b66ac4e45520/packages/fetch/src/index.ts)
- [packages/hono/src/index.ts](https://github.com/orval-labs/orval/blob/4d82f9584ff687adcafd10f3acc1b66ac4e45520/packages/hono/src/index.ts)
- [packages/mcp/src/index.ts](https://github.com/orval-labs/orval/blob/4d82f9584ff687adcafd10f3acc1b66ac4e45520/packages/mcp/src/index.ts)
- [packages/mock/src/index.ts](https://github.com/orval-labs/orval/blob/4d82f9584ff687adcafd10f3acc1b66ac4e45520/packages/mock/src/index.ts)
- [packages/orval/src/index.ts](https://github.com/orval-labs/orval/blob/4d82f9584ff687adcafd10f3acc1b66ac4e45520/packages/orval/src/index.ts)
- [packages/pinia-colada/src/index.ts](https://github.com/orval-labs/orval/blob/4d82f9584ff687adcafd10f3acc1b66ac4e45520/packages/pinia-colada/src/index.ts)
- [packages/query/src/index.ts](https://github.com/orval-labs/orval/blob/4d82f9584ff687adcafd10f3acc1b66ac4e45520/packages/query/src/index.ts)
- [packages/solid-start/src/index.ts](https://github.com/orval-labs/orval/blob/4d82f9584ff687adcafd10f3acc1b66ac4e45520/packages/solid-start/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 116 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 48 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 207 file(s) under packages package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 244 file(s) under service / domain layer (observed from repository paths and static analysis). |

## Important files

- `.claude-plugin/marketplace.json` (config)
- `.coderabbit.yaml` (config)
- `.devcontainer/Dockerfile` (container)
- `.devcontainer/devcontainer-lock.json` (config)
- `.devcontainer/devcontainer.json` (config)
- `.dockerignore` (container)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/ISSUE_TEMPLATE/other.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/deploy-doc.yaml` (ci)
- `.github/workflows/docker-publish.yaml` (ci)
- `.github/workflows/issue-labeler.yaml` (ci)
- `.github/workflows/pr-checks.yaml` (ci)
- `.github/workflows/release-prepare.yaml` (ci)
- `.github/workflows/release-publish.yaml` (ci)
- `.github/workflows/stale.yaml` (ci)
- `.prettierrc.json` (config)
- `.vscode/extensions.json` (config)
- `.vscode/settings.json` (config)
- `Dockerfile` (container)
- `bunfig.toml` (config)
- `docs/biome.json` (config)
- `docs/content/docs/guides/meta.json` (config)
- `docs/content/docs/meta.json` (config)
- `docs/content/docs/reference/configuration/meta.json` (config)
- `docs/content/docs/reference/meta.json` (config)
- `docs/content/docs/versions/meta.json` (config)
- `docs/content/docs/zh/guides/meta.json` (config)
- `docs/content/docs/zh/meta.json` (config)
- `docs/content/docs/zh/reference/configuration/meta.json` (config)
- `docs/content/docs/zh/reference/meta.json` (config)
- `docs/content/docs/zh/versions/meta.json` (config)
- `docs/package.json` (manifest)
- `docs/site.config.json` (config)
- `docs/tsconfig.json` (config)
- `package.json` (manifest)
- `packages/angular/package.json` (manifest)
- `packages/angular/tsconfig.build.json` (config)
- `packages/angular/tsconfig.json` (config)
- `packages/axios/package.json` (manifest)
- `packages/axios/tsconfig.build.json` (config)
- `packages/axios/tsconfig.json` (config)
- `packages/core/package.json` (manifest)
- `packages/core/tsconfig.build.json` (config)
- `packages/core/tsconfig.json` (config)
- `packages/effect/package.json` (manifest)
- `packages/effect/tsconfig.build.json` (config)
- `packages/effect/tsconfig.json` (config)
- `packages/fetch/package.json` (manifest)
- `packages/fetch/tsconfig.build.json` (config)
- `packages/fetch/tsconfig.json` (config)
- `packages/hono/package.json` (manifest)
- `packages/hono/tsconfig.build.json` (config)
- `packages/hono/tsconfig.json` (config)
- `packages/mcp/package.json` (manifest)
- `packages/mcp/tsconfig.build.json` (config)
- `packages/mcp/tsconfig.json` (config)
- `packages/mock/package.json` (manifest)
- `packages/mock/tsconfig.build.json` (config)
- `packages/mock/tsconfig.json` (config)
- `packages/orval/package.json` (manifest)
- `packages/orval/tsconfig.build.json` (config)
- `packages/orval/tsconfig.json` (config)
- `packages/pinia-colada/package.json` (manifest)
- `packages/pinia-colada/tsconfig.build.json` (config)
- `packages/pinia-colada/tsconfig.json` (config)
- `packages/query/package.json` (manifest)
- `packages/query/tsconfig.build.json` (config)
- `packages/query/tsconfig.json` (config)
- `packages/solid-start/package.json` (manifest)
- `packages/solid-start/tsconfig.build.json` (config)
- `packages/solid-start/tsconfig.json` (config)
- `packages/swr/package.json` (manifest)
- `packages/swr/tsconfig.build.json` (config)
- `packages/swr/tsconfig.json` (config)
- `packages/valibot/package.json` (manifest)
- `packages/valibot/tsconfig.build.json` (config)
- `packages/valibot/tsconfig.json` (config)
- `packages/zod/package.json` (manifest)
- `packages/zod/tsconfig.build.json` (config)
- `packages/zod/tsconfig.json` (config)

## Top-level layout

- `packages` — 512 analysed file(s)
- `docs` — 130 analysed file(s)
- `samples` — 118 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `.github` — 14 analysed file(s)
- `.devcontainer` — 3 analysed file(s)
- `.vite-hooks` — 2 analysed file(s)
- `.vscode` — 2 analysed file(s)
- `.claude-plugin` — 1 analysed file(s)
- `logo` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `4d82f9584ff687adcafd10f3acc1b66ac4e45520` is the revision these paths and observations refer to.
