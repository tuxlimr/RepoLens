# Project structure: gotify/server

**Analysed commit:** `01086b95a8b69ee87383f6e8bcae601d8c33384b`

**Commit reference:** [01086b95a8b69ee87383f6e8bcae601d8c33384b](https://github.com/gotify/server/commit/01086b95a8b69ee87383f6e8bcae601d8c33384b)

**Tree at this commit:** [gotify/server@01086b95a8b6](https://github.com/gotify/server/tree/01086b95a8b69ee87383f6e8bcae601d8c33384b)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | gotify/server |
| Description | A simple server for sending and receiving messages in real-time per WebSocket. (Includes a sleek web-ui) |
| Stars | 16206 |
| Forks | 899 |
| Licence | Other |
| Language | Go |
| Default branch | master |
| Analysed commit | `01086b95a8b69ee87383f6e8bcae601d8c33384b` |
| Retrieved at | 2026-11-14T19:13:15.768046+00:00 |
| Files in this snapshot | 255 |

## Directory tree

```text
.github/  (5 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    feature_request.md
    questions.md
  workflows/  (1 files)
    build.yml
  FUNDING.yml
api/  (28 files)
  stream/  (5 files)
    client.go
    once.go
    once_test.go
    stream.go
    stream_test.go
  application.go
  application_test.go
  client.go
  client_test.go
  errorHandling.go
  errorHandling_test.go
  health.go
  health_test.go
  internalutil.go
  mcp.go
  mcp_test.go
  message.go
  message_test.go
  oidc.go
  oidc_test.go
  plugin.go
  plugin_test.go
  session.go
  session_test.go
  tokens.go
  tokens_test.go
  user.go
  user_test.go
auth/  (11 files)
  password/  (2 files)
    password.go
    password_test.go
  authentication.go
  authentication_test.go
  cookie.go
  cors.go
  cors_test.go
  token.go
  token_test.go
  util.go
  util_test.go
config/  (12 files)
  migrate/  (2 files)
    migrate.go
    migrate_test.go
  config.go
  config_test.go
  error.go
  file.go
  keys.go
  loglevel.go
  loglevel_test.go
  origin.go
  origin_test.go
  parse.go
database/  (15 files)
  application.go
  application_test.go
  client.go
  client_test.go
  database.go
  database_test.go
  message.go
  message_test.go
  migration_test.go
  ping.go
  ping_test.go
  plugin.go
  plugin_test.go
  user.go
  user_test.go
decaymap/  (2 files)
  decaymap.go
  decaymap_test.go
docker/  (1 files)
  Dockerfile
docs/  (6 files)
  package.go
  spec.json
  swagger.go
  swagger_test.go
  ui.go
  ui_test.go
error/  (4 files)
  handler.go
  handler_test.go
  notfound.go
  notfound_test.go
fracdex/  (2 files)
  fracdex.go
  fracdex_test.go
mode/  (2 files)
  mode.go
  mode_test.go
model/  (14 files)
  application.go
  client.go
  elevate.go
  elevate_test.go
  error.go
  gotifyinfo.go
  health.go
  message.go
  oidc.go
  paging.go
  pluginconf.go
  security.go
  user.go
  version.go
plugin/  (27 files)
  compat/  (9 files)
    instance.go
    plugin.go
    plugin_test.go
    v1.go
    v1_test.go
    wrap.go
    wrap_test.go
    wrap_test_norace.go
    wrap_test_race.go
  example/  (3 files)
    clock/  (1 files)
      … 1 files under this directory
    echo/  (1 files)
      … 1 files under this directory
    minimal/  (1 files)
      … 1 files under this directory
  testing/  (6 files)
    broken/  (5 files)
      … 5 files under this directory
    mock/  (1 files)
      … 1 files under this directory
  manager.go
  manager_test.go
  manager_test_norace.go
  manager_test_race.go
  messagehandler.go
  messagehandler_test.go
  pluginenabled.go
  pluginenabled_test.go
  storagehandler.go
router/  (3 files)
  mcp_test.go
  router.go
  router_test.go
runner/  (4 files)
  runner.go
  runner_test.go
  umask.go
  umask_fallback.go
test/  (18 files)
  assets/  (1 files)
    text.txt
  oidc/  (7 files)
    authelia/  (3 files)
      … 3 files under this directory
    dex/  (2 files)
      … 2 files under this directory
    .gitignore
    README.md
  testdb/  (2 files)
    database.go
    database_test.go
  asserts.go
  asserts_test.go
  auth.go
  auth_test.go
  filepath.go
  filepath_test.go
  tmpdir.go
  tmpdir_test.go
ui/  (83 files)
  public/  (1 files)
    manifest.json
  src/  (69 files)
    application/  (4 files)
      … 4 files under this directory
    client/  (5 files)
      … 5 files under this directory
    common/  (15 files)
      … 15 files under this directory
    layout/  (4 files)
      … 4 files under this directory
    message/  (6 files)
      … 6 files under this directory
    plugin/  (3 files)
      … 3 files under this directory
    snack/  (2 files)
      … 2 files under this directory
    tests/  (12 files)
      … 12 files under this directory
    typedef/  (1 files)
      … 1 files under this directory
    user/  (6 files)
      … 6 files under this directory
    CurrentUser.ts
    ElevateStore.ts
    apiAuth.ts
    clipboard.ts
    config.ts
    index.tsx
    react-app-env.d.ts
    reactions.ts
    registerServiceWorker.ts
    stores.tsx
    types.ts
  .gitignore
  .prettierrc
  .yarnrc
  eslint.config.mjs
  index.html
  package.json
  serve.go
  tsconfig.json
  tsconfig.prod.json
  tsconfig.test.json
  vite-env.d.ts
  vite.config.ts
  vitest.config.js
.dockerignore
.editorconfig
.gitignore
.golangci.yml
CODEOWNERS
CODE_OF_CONDUCT.md
CONTRIBUTING.md
GO_VERSION
LICENSE
Makefile
README.md
SECURITY.md
app.go
app_test.go
go.mod
go.sum
gotify-server.env.example
renovate.json
```

## Entry points

- [ui/src/index.tsx](https://github.com/gotify/server/blob/01086b95a8b69ee87383f6e8bcae601d8c33384b/ui/src/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 28 file(s) under api layer (observed from repository paths and static analysis). |
| auth package | library | Observed | Groups 11 file(s) under auth package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 22 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 15 file(s) under data layer (observed from repository paths and static analysis). |
| decaymap package | library | Observed | Groups 2 file(s) under decaymap package (observed from repository paths and static analysis). |
| error package | library | Observed | Groups 4 file(s) under error package (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 5 file(s) under external integrations (observed from repository paths and static analysis). |
| fracdex package | library | Observed | Groups 2 file(s) under fracdex package (observed from repository paths and static analysis). |
| mode package | library | Observed | Groups 2 file(s) under mode package (observed from repository paths and static analysis). |
| model package | library | Observed | Groups 14 file(s) under model package (observed from repository paths and static analysis). |
| plugin package | library | Observed | Groups 27 file(s) under plugin package (observed from repository paths and static analysis). |
| router package | library | Observed | Groups 3 file(s) under router package (observed from repository paths and static analysis). |
| runner package | library | Observed | Groups 4 file(s) under runner package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 28 file(s) under tests (observed from repository paths and static analysis). |
| ui package | library | Observed | Groups 57 file(s) under ui package (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/workflows/build.yml` (ci)
- `.golangci.yml` (config)
- `docker/Dockerfile` (container)
- `docs/spec.json` (config)
- `go.mod` (manifest)
- `renovate.json` (config)
- `test/oidc/authelia/docker-compose.yml` (container)
- `test/oidc/dex/docker-compose.yml` (container)
- `ui/package.json` (manifest)
- `ui/public/manifest.json` (config)
- `ui/tsconfig.json` (config)
- `ui/tsconfig.prod.json` (config)
- `ui/tsconfig.test.json` (config)

## Top-level layout

- `ui` — 83 analysed file(s)
- `api` — 28 analysed file(s)
- `plugin` — 27 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `test` — 18 analysed file(s)
- `database` — 15 analysed file(s)
- `model` — 14 analysed file(s)
- `config` — 12 analysed file(s)
- `auth` — 11 analysed file(s)
- `docs` — 6 analysed file(s)
- `.github` — 5 analysed file(s)
- `error` — 4 analysed file(s)
- `runner` — 4 analysed file(s)
- `router` — 3 analysed file(s)
- `decaymap` — 2 analysed file(s)
- `fracdex` — 2 analysed file(s)
- `mode` — 2 analysed file(s)
- `docker` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `01086b95a8b69ee87383f6e8bcae601d8c33384b` is the revision these paths and observations refer to.
