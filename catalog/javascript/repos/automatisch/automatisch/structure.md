# Project structure: automatisch/automatisch

**Analysed commit:** `41f3c56a163103cae761bb44f03638cb84e859ee`

**Commit reference:** [41f3c56a163103cae761bb44f03638cb84e859ee](https://github.com/automatisch/automatisch/commit/41f3c56a163103cae761bb44f03638cb84e859ee)

**Tree at this commit:** [automatisch/automatisch@41f3c56a1631](https://github.com/automatisch/automatisch/tree/41f3c56a163103cae761bb44f03638cb84e859ee)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | automatisch/automatisch |
| Description | The open source Zapier alternative. Build workflow automation without spending time and money. |
| Stars | 14021 |
| Forks | 1063 |
| Licence | Other |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `41f3c56a163103cae761bb44f03638cb84e859ee` |
| Retrieved at | 2026-11-14T19:11:47.592776+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.devcontainer/  (4 files)
  Dockerfile
  boot.sh
  devcontainer.json
  docker-compose.yml
.github/  (6 files)
  workflows/  (5 files)
    backend.yml
    ci.yml
    docs-change.yml
    playwright.yml
    release.yml
  FUNDING.yml
.vscode/  (2 files)
  launch.json
  settings.json
docker/  (4 files)
  Dockerfile
  Dockerfile.compose
  compose-entrypoint.sh
  entrypoint.sh
packages/  (771 files)
  backend/  (771 files)
    bin/  (5 files)
      … 5 files under this directory
    src/  (757 files)
      … 757 files under this directory
    .env-example
    .env-example.test
    .eslintignore
    .eslintrc.json
    README.md
    alias-loader.mjs
    jsconfig.json
    knexfile.js
    package.json
.dockerignore
.gitignore
.node-version
.nvmrc
.prettierrc.js
.yarnrc
CODE_OF_CONDUCT.md
CONTRIBUTOR_LICENSE_AGREEMENT.md
LICENSE
LICENSE.agpl
LICENSE.enterprise
README.md
docker-compose.yml
```

## Entry points

- [packages/backend/src/app.js](https://github.com/automatisch/automatisch/blob/41f3c56a163103cae761bb44f03638cb84e859ee/packages/backend/src/app.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 5 file(s) under data layer (observed from repository paths and static analysis). |
| docker package | library | Observed | Groups 2 file(s) under docker package (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 711 file(s) under packages package (observed from repository paths and static analysis). |

## Important files

- `.devcontainer/Dockerfile` (container)
- `.devcontainer/devcontainer.json` (config)
- `.devcontainer/docker-compose.yml` (container)
- `.dockerignore` (container)
- `.github/FUNDING.yml` (config)
- `.github/workflows/backend.yml` (ci)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/docs-change.yml` (ci)
- `.github/workflows/playwright.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.vscode/launch.json` (config)
- `.vscode/settings.json` (config)
- `docker-compose.yml` (container)
- `docker/Dockerfile` (container)
- `docker/Dockerfile.compose` (container)
- `packages/backend/.eslintrc.json` (config)
- `packages/backend/jsconfig.json` (config)
- `packages/backend/package.json` (manifest)

## Top-level layout

- `packages` — 771 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `.github` — 6 analysed file(s)
- `.devcontainer` — 4 analysed file(s)
- `docker` — 4 analysed file(s)
- `.vscode` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `41f3c56a163103cae761bb44f03638cb84e859ee` is the revision these paths and observations refer to.
