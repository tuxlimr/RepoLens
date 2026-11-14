# Project structure: gitalk/gitalk

**Analysed commit:** `b1b478e877fac68d6632b843b00c33d3f32c2dad`

**Commit reference:** [b1b478e877fac68d6632b843b00c33d3f32c2dad](https://github.com/gitalk/gitalk/commit/b1b478e877fac68d6632b843b00c33d3f32c2dad)

**Tree at this commit:** [gitalk/gitalk@b1b478e877fa](https://github.com/gitalk/gitalk/tree/b1b478e877fac68d6632b843b00c33d3f32c2dad)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | gitalk/gitalk |
| Description | Gitalk — a comment component based on GitHub Discussions (current, 2.x). The GitHub Issues based 1.x line is end-of-life. |
| Stars | 7154 |
| Forks | 614 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `b1b478e877fac68d6632b843b00c33d3f32c2dad` |
| Retrieved at | 2026-11-14T19:13:59.630771+00:00 |
| Files in this snapshot | 189 |

## Directory tree

```text
.github/  (6 files)
  workflows/  (4 files)
    ci.yml
    deploy-pages.yml
    publish-deploy-cli.yml
    publish.yml
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
apps/  (61 files)
  demo-react/  (11 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (6 files)
      … 6 files under this directory
    index.html
    package.json
    tsconfig.json
    vite.config.ts
  demo-vue/  (11 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (6 files)
      … 6 files under this directory
    index.html
    package.json
    tsconfig.json
    vite.config.ts
  landing/  (39 files)
    public/  (3 files)
      … 3 files under this directory
    src/  (31 files)
      … 31 files under this directory
    .gitignore
    index.html
    package.json
    tsconfig.json
    vite.config.ts
docs/  (5 files)
  guide.md
  handsoff.md
  tech-deploy.md
  tech.md
  upload-service.md
packages/  (103 files)
  core/  (65 files)
    src/  (61 files)
      … 61 files under this directory
    package.json
    tsconfig.types.json
    vite.config.ts
    vite.iife.config.ts
  gitalk-deploy/  (8 files)
    scripts/  (1 files)
      … 1 files under this directory
    src/  (4 files)
      … 4 files under this directory
    README-CN.md
    README.md
    package.json
  proxy-cloudbase/  (5 files)
    functions/  (1 files)
      … 1 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    cloudbaserc.json
    package.json
  proxy-core/  (6 files)
    src/  (5 files)
      … 5 files under this directory
    package.json
  proxy-node/  (3 files)
    src/  (1 files)
      … 1 files under this directory
    Dockerfile
    package.json
  proxy-worker/  (6 files)
    scripts/  (1 files)
      … 1 files under this directory
    src/  (1 files)
      … 1 files under this directory
    .env.example
    .gitignore
    package.json
    wrangler.toml
  react/  (5 files)
    src/  (1 files)
      … 1 files under this directory
    package.json
    tsconfig.json
    tsconfig.types.json
    vite.config.ts
  vue/  (5 files)
    src/  (1 files)
      … 1 files under this directory
    package.json
    tsconfig.json
    tsconfig.types.json
    vite.config.ts
prd/  (1 files)
  comment-translation.md
scripts/  (3 files)
  check-docs.mjs
  check-publishable.mjs
  next-beta-version.mjs
.editorconfig
.gitignore
LICENSE
package.json
pnpm-workspace.yaml
readme-cn.md
readme.md
scf_bootstrap
tsconfig.json
vitest.config.ts
```

## Entry points

- [packages/proxy-core/src/index.ts](https://github.com/gitalk/gitalk/blob/b1b478e877fac68d6632b843b00c33d3f32c2dad/packages/proxy-core/src/index.ts)
- [apps/demo-react/src/app.tsx](https://github.com/gitalk/gitalk/blob/b1b478e877fac68d6632b843b00c33d3f32c2dad/apps/demo-react/src/app.tsx)
- [apps/demo-react/src/main.tsx](https://github.com/gitalk/gitalk/blob/b1b478e877fac68d6632b843b00c33d3f32c2dad/apps/demo-react/src/main.tsx)
- [apps/demo-vue/src/main.ts](https://github.com/gitalk/gitalk/blob/b1b478e877fac68d6632b843b00c33d3f32c2dad/apps/demo-vue/src/main.ts)
- [apps/landing/src/app.tsx](https://github.com/gitalk/gitalk/blob/b1b478e877fac68d6632b843b00c33d3f32c2dad/apps/landing/src/app.tsx)
- [apps/landing/src/main.tsx](https://github.com/gitalk/gitalk/blob/b1b478e877fac68d6632b843b00c33d3f32c2dad/apps/landing/src/main.tsx)
- [packages/core/src/index.ts](https://github.com/gitalk/gitalk/blob/b1b478e877fac68d6632b843b00c33d3f32c2dad/packages/core/src/index.ts)
- [packages/proxy-node/src/server.ts](https://github.com/gitalk/gitalk/blob/b1b478e877fac68d6632b843b00c33d3f32c2dad/packages/proxy-node/src/server.ts)
- [packages/proxy-worker/src/index.ts](https://github.com/gitalk/gitalk/blob/b1b478e877fac68d6632b843b00c33d3f32c2dad/packages/proxy-worker/src/index.ts)
- [packages/react/src/index.tsx](https://github.com/gitalk/gitalk/blob/b1b478e877fac68d6632b843b00c33d3f32c2dad/packages/react/src/index.tsx)
- [packages/vue/src/index.ts](https://github.com/gitalk/gitalk/blob/b1b478e877fac68d6632b843b00c33d3f32c2dad/packages/vue/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 7 file(s) under api layer (observed from repository paths and static analysis). |
| apps package | library | Observed | Groups 43 file(s) under apps package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 26 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 19 file(s) under packages package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 3 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 55 file(s) under service / domain layer (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/deploy-pages.yml` (ci)
- `.github/workflows/publish-deploy-cli.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `apps/demo-react/package.json` (manifest)
- `apps/demo-react/tsconfig.json` (config)
- `apps/demo-vue/package.json` (manifest)
- `apps/demo-vue/tsconfig.json` (config)
- `apps/landing/package.json` (manifest)
- `apps/landing/tsconfig.json` (config)
- `package.json` (manifest)
- `packages/core/package.json` (manifest)
- `packages/core/tsconfig.types.json` (config)
- `packages/gitalk-deploy/package.json` (manifest)
- `packages/proxy-cloudbase/cloudbaserc.json` (config)
- `packages/proxy-cloudbase/package.json` (manifest)
- `packages/proxy-core/package.json` (manifest)
- `packages/proxy-node/Dockerfile` (container)
- `packages/proxy-node/package.json` (manifest)
- `packages/proxy-worker/.env.example` (config)
- `packages/proxy-worker/package.json` (manifest)
- `packages/proxy-worker/wrangler.toml` (config)
- `packages/react/package.json` (manifest)
- `packages/react/tsconfig.json` (config)
- `packages/react/tsconfig.types.json` (config)
- `packages/vue/package.json` (manifest)
- `packages/vue/tsconfig.json` (config)
- `packages/vue/tsconfig.types.json` (config)
- `pnpm-workspace.yaml` (config)
- `tsconfig.json` (config)

## Top-level layout

- `packages` — 103 analysed file(s)
- `apps` — 61 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `.github` — 6 analysed file(s)
- `docs` — 5 analysed file(s)
- `scripts` — 3 analysed file(s)
- `prd` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (1 x likely secret file excluded; 1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `b1b478e877fac68d6632b843b00c33d3f32c2dad` is the revision these paths and observations refer to.
