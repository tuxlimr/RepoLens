# Project structure: Yooooomi/your_spotify

**Analysed commit:** `fdd81ef89119159eac375fa2422d83e1765cff5e`

**Commit reference:** [fdd81ef89119159eac375fa2422d83e1765cff5e](https://github.com/Yooooomi/your_spotify/commit/fdd81ef89119159eac375fa2422d83e1765cff5e)

**Tree at this commit:** [Yooooomi/your_spotify@fdd81ef89119](https://github.com/Yooooomi/your_spotify/tree/fdd81ef89119159eac375fa2422d83e1765cff5e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Yooooomi/your_spotify |
| Description | Self hosted Spotify tracking dashboard |
| Stars | 4630 |
| Forks | 219 |
| Licence | GPL-3.0 |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `fdd81ef89119159eac375fa2422d83e1765cff5e` |
| Retrieved at | 2026-11-14T19:14:40.321404+00:00 |
| Files in this snapshot | 515 |

## Directory tree

```text
.github/  (4 files)
  ISSUE_TEMPLATE/  (1 files)
    bug_report.md
  workflows/  (2 files)
    nightly.yml
    release.yml
  FUNDING.yml
apps/  (494 files)
  client/  (400 files)
    public/  (7 files)
      … 7 files under this directory
    scripts/  (5 files)
      … 5 files under this directory
    src/  (383 files)
      … 383 files under this directory
    .gitignore
    css.js
    package.json
    rsbuild.config.ts
    tsconfig.json
  dev/  (4 files)
    .oxfmtrc.json
    .oxlintrc.json
    package.json
    tsconfig.json
  server/  (90 files)
    scripts/  (3 files)
      … 3 files under this directory
    src/  (81 files)
      … 81 files under this directory
    .dockerignore
    .gitignore
    README.md
    package.json
    rsbuild.config.ts
    tsconfig.json
.gitignore
Dockerfile.client
Dockerfile.client.production
Dockerfile.server
Dockerfile.server.production
LICENSE
LOCAL_INSTALL.md
README.md
build.sh
dev.sh
docker-compose-dev.yml
docker-compose-example.yml
docker-compose-prod.yml
monorepo.code-workspace
package.json
pnpm-workspace.yaml
prod.sh
```

## Entry points

- [apps/client/src/App.tsx](https://github.com/Yooooomi/your_spotify/blob/fdd81ef89119159eac375fa2422d83e1765cff5e/apps/client/src/App.tsx)
- [apps/client/src/index.tsx](https://github.com/Yooooomi/your_spotify/blob/fdd81ef89119159eac375fa2422d83e1765cff5e/apps/client/src/index.tsx)
- [apps/server/src/app.ts](https://github.com/Yooooomi/your_spotify/blob/fdd81ef89119159eac375fa2422d83e1765cff5e/apps/server/src/app.ts)
- [apps/server/src/index.ts](https://github.com/Yooooomi/your_spotify/blob/fdd81ef89119159eac375fa2422d83e1765cff5e/apps/server/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 10 file(s) under api layer (observed from repository paths and static analysis). |
| apps package | library | Observed | Groups 50 file(s) under apps package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 20 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 25 file(s) under data layer (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 309 file(s) under external integrations (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/workflows/nightly.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `Dockerfile.client` (container)
- `Dockerfile.client.production` (container)
- `Dockerfile.server` (container)
- `Dockerfile.server.production` (container)
- `apps/client/package.json` (manifest)
- `apps/client/public/manifest.json` (config)
- `apps/client/scripts/run/serve.json` (config)
- `apps/client/tsconfig.json` (config)
- `apps/dev/.oxfmtrc.json` (config)
- `apps/dev/.oxlintrc.json` (config)
- `apps/dev/package.json` (manifest)
- `apps/dev/tsconfig.json` (config)
- `apps/server/.dockerignore` (container)
- `apps/server/package.json` (manifest)
- `apps/server/tsconfig.json` (config)
- `docker-compose-dev.yml` (config)
- `docker-compose-example.yml` (config)
- `docker-compose-prod.yml` (config)
- `package.json` (manifest)
- `pnpm-workspace.yaml` (config)

## Top-level layout

- `apps` — 494 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `.github` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (1 x lockfile excluded; 1 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `fdd81ef89119159eac375fa2422d83e1765cff5e` is the revision these paths and observations refer to.
