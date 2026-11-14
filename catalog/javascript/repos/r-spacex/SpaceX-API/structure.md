# Project structure: r-spacex/SpaceX-API

**Analysed commit:** `9f56af14a75ae410c26eb0317971d51ae1574f6a`

**Commit reference:** [9f56af14a75ae410c26eb0317971d51ae1574f6a](https://github.com/r-spacex/SpaceX-API/commit/9f56af14a75ae410c26eb0317971d51ae1574f6a)

**Tree at this commit:** [r-spacex/SpaceX-API@9f56af14a75a](https://github.com/r-spacex/SpaceX-API/tree/9f56af14a75ae410c26eb0317971d51ae1574f6a)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | r-spacex/SpaceX-API |
| Description | :rocket: Open Source REST API for SpaceX launch, rocket, core, capsule, starlink, launchpad, and landing pad data. |
| Stars | 10921 |
| Forks | 987 |
| Licence | Apache-2.0 |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `9f56af14a75ae410c26eb0317971d51ae1574f6a` |
| Retrieved at | 2026-11-14T19:12:28.115194+00:00 |
| Files in this snapshot | 161 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (2 files)
    codeql-analysis.yml
    deploy.yml
  dependabot.yml
docs/  (70 files)
  capsules/  (4 files)
    v4/  (4 files)
      … 4 files under this directory
  company/  (2 files)
    v4/  (2 files)
      … 2 files under this directory
  cores/  (4 files)
    v4/  (4 files)
      … 4 files under this directory
  crew/  (4 files)
    v4/  (4 files)
      … 4 files under this directory
  dragons/  (4 files)
    v4/  (4 files)
      … 4 files under this directory
  history/  (4 files)
    v4/  (4 files)
      … 4 files under this directory
  landpads/  (4 files)
    v4/  (4 files)
      … 4 files under this directory
  launches/  (17 files)
    v4/  (8 files)
      … 8 files under this directory
    v5/  (9 files)
      … 9 files under this directory
  launchpads/  (4 files)
    v4/  (4 files)
      … 4 files under this directory
  payloads/  (4 files)
    v4/  (4 files)
      … 4 files under this directory
  roadster/  (3 files)
    v4/  (3 files)
      … 3 files under this directory
  rockets/  (4 files)
    v4/  (4 files)
      … 4 files under this directory
  ships/  (4 files)
    v4/  (4 files)
      … 4 files under this directory
  starlink/  (4 files)
    v4/  (4 files)
      … 4 files under this directory
  README.md
  apps.md
  clients.md
  queries.md
jobs/  (12 files)
  capsules.js
  cores.js
  landpads.js
  launch-library.js
  launches.js
  launchpads.js
  payloads.js
  roadster.js
  starlink.js
  upcoming.js
  webcast.js
  worker.js
lib/  (6 files)
  healthchecks/  (4 files)
    fail.js
    index.js
    start.js
    success.js
  utils/  (1 files)
    healthcheck.js
  constants.js
middleware/  (7 files)
  auth.js
  authz.js
  cache.js
  errors.js
  index.js
  logger.js
  response-time.js
models/  (16 files)
  capsules.js
  company.js
  cores.js
  crew.js
  dragons.js
  history.js
  index.js
  landpads.js
  launches.js
  launchpads.js
  payloads.js
  roadster.js
  rockets.js
  ships.js
  starlink.js
  users.js
routes/  (36 files)
  admin/  (2 files)
    v4/  (1 files)
      … 1 files under this directory
    index.js
  capsules/  (2 files)
    v4/  (1 files)
      … 1 files under this directory
    index.js
  company/  (2 files)
    v4/  (1 files)
      … 1 files under this directory
    index.js
  cores/  (2 files)
    v4/  (1 files)
      … 1 files under this directory
    index.js
  crew/  (2 files)
    v4/  (1 files)
      … 1 files under this directory
    index.js
  dragons/  (2 files)
    v4/  (1 files)
      … 1 files under this directory
    index.js
  history/  (2 files)
    v4/  (1 files)
      … 1 files under this directory
    index.js
  landpads/  (2 files)
    v4/  (1 files)
      … 1 files under this directory
    index.js
  launches/  (5 files)
    v4/  (3 files)
      … 3 files under this directory
    v5/  (1 files)
      … 1 files under this directory
    index.js
  launchpads/  (2 files)
    v4/  (1 files)
      … 1 files under this directory
    index.js
  payloads/  (2 files)
    v4/  (1 files)
      … 1 files under this directory
    index.js
  roadster/  (2 files)
    v4/  (1 files)
      … 1 files under this directory
    index.js
  rockets/  (2 files)
    v4/  (1 files)
      … 1 files under this directory
    index.js
  ships/  (2 files)
    v4/  (1 files)
      … 1 files under this directory
    index.js
  starlink/  (2 files)
    v4/  (1 files)
      … 1 files under this directory
    index.js
  users/  (2 files)
    v4/  (1 files)
      … 1 files under this directory
    index.js
  index.js
tests/  (1 files)
  index.test.js
.dockerignore
.eslintrc.json
.gitignore
Dockerfile
LICENSE
README.md
app.js
package.json
server.js
start.sh
```

## Entry points

- [server.js](https://github.com/r-spacex/SpaceX-API/blob/9f56af14a75ae410c26eb0317971d51ae1574f6a/server.js)
- [app.js](https://github.com/r-spacex/SpaceX-API/blob/9f56af14a75ae410c26eb0317971d51ae1574f6a/app.js)
- [lib/healthchecks/index.js](https://github.com/r-spacex/SpaceX-API/blob/9f56af14a75ae410c26eb0317971d51ae1574f6a/lib/healthchecks/index.js)
- [middleware/index.js](https://github.com/r-spacex/SpaceX-API/blob/9f56af14a75ae410c26eb0317971d51ae1574f6a/middleware/index.js)
- [models/index.js](https://github.com/r-spacex/SpaceX-API/blob/9f56af14a75ae410c26eb0317971d51ae1574f6a/models/index.js)
- [routes/admin/index.js](https://github.com/r-spacex/SpaceX-API/blob/9f56af14a75ae410c26eb0317971d51ae1574f6a/routes/admin/index.js)
- [routes/admin/v4/index.js](https://github.com/r-spacex/SpaceX-API/blob/9f56af14a75ae410c26eb0317971d51ae1574f6a/routes/admin/v4/index.js)
- [routes/capsules/index.js](https://github.com/r-spacex/SpaceX-API/blob/9f56af14a75ae410c26eb0317971d51ae1574f6a/routes/capsules/index.js)
- [routes/capsules/v4/index.js](https://github.com/r-spacex/SpaceX-API/blob/9f56af14a75ae410c26eb0317971d51ae1574f6a/routes/capsules/v4/index.js)
- [routes/company/index.js](https://github.com/r-spacex/SpaceX-API/blob/9f56af14a75ae410c26eb0317971d51ae1574f6a/routes/company/index.js)
- [routes/company/v4/index.js](https://github.com/r-spacex/SpaceX-API/blob/9f56af14a75ae410c26eb0317971d51ae1574f6a/routes/company/v4/index.js)
- [routes/cores/index.js](https://github.com/r-spacex/SpaceX-API/blob/9f56af14a75ae410c26eb0317971d51ae1574f6a/routes/cores/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 36 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 16 file(s) under data layer (observed from repository paths and static analysis). |
| jobs package | library | Observed | Groups 12 file(s) under jobs package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 6 file(s) under lib package (observed from repository paths and static analysis). |
| middleware package | library | Observed | Groups 7 file(s) under middleware package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.eslintrc.json` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/codeql-analysis.yml` (ci)
- `.github/workflows/deploy.yml` (ci)
- `Dockerfile` (container)
- `package.json` (manifest)

## Top-level layout

- `docs` — 70 analysed file(s)
- `routes` — 36 analysed file(s)
- `models` — 16 analysed file(s)
- `jobs` — 12 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `middleware` — 7 analysed file(s)
- `lib` — 6 analysed file(s)
- `.github` — 3 analysed file(s)
- `tests` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `9f56af14a75ae410c26eb0317971d51ae1574f6a` is the revision these paths and observations refer to.
