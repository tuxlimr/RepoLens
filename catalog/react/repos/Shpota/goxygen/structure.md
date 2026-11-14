# Project structure: Shpota/goxygen

**Analysed commit:** `47ce691cfac7ecde991afb8c1eabe9a9206c3434`

**Commit reference:** [47ce691cfac7ecde991afb8c1eabe9a9206c3434](https://github.com/Shpota/goxygen/commit/47ce691cfac7ecde991afb8c1eabe9a9206c3434)

**Tree at this commit:** [Shpota/goxygen@47ce691cfac7](https://github.com/Shpota/goxygen/tree/47ce691cfac7ecde991afb8c1eabe9a9206c3434)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Shpota/goxygen |
| Description | Generate a modern Web project with Go and Angular, React, or Vue in seconds 🎲 |
| Stars | 3585 |
| Forks | 220 |
| Licence | Apache-2.0 |
| Language | Go |
| Default branch | main |
| Analysed commit | `47ce691cfac7ecde991afb8c1eabe9a9206c3434` |
| Retrieved at | 2026-11-14T19:15:14.562907+00:00 |
| Files in this snapshot | 113 |

## Directory tree

```text
.github/  (5 files)
  workflows/  (3 files)
    build.yml
    verify-all-committed.yml
    verify-templates.yml
  .golangci.yml
  FUNDING.yml
cli/  (2 files)
  cli.go
  cli_test.go
codegen/  (2 files)
  codegen.go
  codegen_test.go
docs/  (19 files)
  _includes/  (3 files)
    footer.html
    head.html
    header.html
  CNAME
  README.md
  README_by.md
  README_es.md
  README_fr.md
  README_he.md
  README_id.md
  README_jp.md
  README_ko.md
  README_pt-br.md
  README_tr.md
  README_ua.md
  README_zh.md
  _config.yml
  flag-by.svg
  logo.svg
templates/  (79 files)
  angular.webapp/  (25 files)
    .vscode/  (3 files)
      … 3 files under this directory
    src/  (15 files)
      … 15 files under this directory
    .editorconfig
    .gitignore
    angular.json
    package.json
    tsconfig.app.json
    tsconfig.json
    tsconfig.spec.json
  mongo.server/  (4 files)
    db/  (1 files)
      … 1 files under this directory
    go.mod
    go.sum
    server.go
  mysql.server/  (4 files)
    db/  (1 files)
      … 1 files under this directory
    go.mod
    go.sum
    server.go
  postgres.server/  (4 files)
    db/  (1 files)
      … 1 files under this directory
    go.mod
    go.sum
    server.go
  react.webapp/  (13 files)
    public/  (3 files)
      … 3 files under this directory
    src/  (9 files)
      … 9 files under this directory
    package.json
  server/  (3 files)
    model/  (1 files)
      … 1 files under this directory
    web/  (2 files)
      … 2 files under this directory
  vue.webapp/  (9 files)
    .vscode/  (1 files)
      … 1 files under this directory
    src/  (4 files)
      … 4 files under this directory
    .eslintrc.cjs
    index.html
    package.json
    vite.config.js
  .dockerignore
  .gitignore
  mongo.Dockerfile
  mongo.README.md
  mongo.docker-compose-dev.yml
  mongo.docker-compose.yml
  mongo.init-db.js
  mysql.Dockerfile
  mysql.README.md
  mysql.docker-compose-dev.yml
  mysql.docker-compose.yml
  mysql.init-db.sql
  postgres.Dockerfile
  postgres.README.md
  postgres.docker-compose-dev.yml
  postgres.docker-compose.yml
  postgres.init-db.sql
transform/  (3 files)
  go.mod
  transformer.go
  transformer_test.go
LICENSE
go.mod
main.go
```

## Entry points

- [templates/angular.webapp/src/main.ts](https://github.com/Shpota/goxygen/blob/47ce691cfac7ecde991afb8c1eabe9a9206c3434/templates/angular.webapp/src/main.ts)
- [templates/react.webapp/src/App.js](https://github.com/Shpota/goxygen/blob/47ce691cfac7ecde991afb8c1eabe9a9206c3434/templates/react.webapp/src/App.js)
- [templates/react.webapp/src/index.js](https://github.com/Shpota/goxygen/blob/47ce691cfac7ecde991afb8c1eabe9a9206c3434/templates/react.webapp/src/index.js)
- [templates/vue.webapp/src/main.js](https://github.com/Shpota/goxygen/blob/47ce691cfac7ecde991afb8c1eabe9a9206c3434/templates/vue.webapp/src/main.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| cli package | library | Observed | Groups 2 file(s) under cli package (observed from repository paths and static analysis). |
| codegen package | library | Observed | Groups 2 file(s) under codegen package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 25 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 3 file(s) under data layer (observed from repository paths and static analysis). |
| templates package | library | Observed | Groups 26 file(s) under templates package (observed from repository paths and static analysis). |
| transform package | library | Observed | Groups 2 file(s) under transform package (observed from repository paths and static analysis). |

## Important files

- `.github/.golangci.yml` (config)
- `.github/FUNDING.yml` (config)
- `.github/workflows/build.yml` (ci)
- `.github/workflows/verify-all-committed.yml` (ci)
- `.github/workflows/verify-templates.yml` (ci)
- `docs/_config.yml` (config)
- `go.mod` (manifest)
- `templates/.dockerignore` (container)
- `templates/angular.webapp/.editorconfig` (config)
- `templates/angular.webapp/.vscode/extensions.json` (config)
- `templates/angular.webapp/.vscode/launch.json` (config)
- `templates/angular.webapp/.vscode/tasks.json` (config)
- `templates/angular.webapp/angular.json` (config)
- `templates/angular.webapp/package.json` (manifest)
- `templates/angular.webapp/tsconfig.app.json` (config)
- `templates/angular.webapp/tsconfig.json` (config)
- `templates/angular.webapp/tsconfig.spec.json` (config)
- `templates/mongo.docker-compose-dev.yml` (config)
- `templates/mongo.docker-compose.yml` (config)
- `templates/mongo.server/go.mod` (manifest)
- `templates/mysql.docker-compose-dev.yml` (config)
- `templates/mysql.docker-compose.yml` (config)
- `templates/mysql.server/go.mod` (manifest)
- `templates/postgres.docker-compose-dev.yml` (config)
- `templates/postgres.docker-compose.yml` (config)
- `templates/postgres.server/go.mod` (manifest)
- `templates/react.webapp/package.json` (manifest)
- `templates/react.webapp/public/manifest.json` (config)
- `templates/vue.webapp/.vscode/extensions.json` (config)
- `templates/vue.webapp/package.json` (manifest)
- `transform/go.mod` (manifest)

## Top-level layout

- `templates` — 79 analysed file(s)
- `docs` — 19 analysed file(s)
- `.github` — 5 analysed file(s)
- `(root files)` — 3 analysed file(s)
- `transform` — 3 analysed file(s)
- `cli` — 2 analysed file(s)
- `codegen` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 4 file(s) were skipped during inventory (4 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `47ce691cfac7ecde991afb8c1eabe9a9206c3434` is the revision these paths and observations refer to.
