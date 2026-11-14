# Project structure: thedevs-network/kutt

**Analysed commit:** `029da42b2459693681886665589fd9512d6b473c`

**Commit reference:** [029da42b2459693681886665589fd9512d6b473c](https://github.com/thedevs-network/kutt/commit/029da42b2459693681886665589fd9512d6b473c)

**Tree at this commit:** [thedevs-network/kutt@029da42b2459](https://github.com/thedevs-network/kutt/tree/029da42b2459693681886665589fd9512d6b473c)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | thedevs-network/kutt |
| Description | Free Modern URL Shortener. |
| Stars | 11206 |
| Forks | 1534 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `029da42b2459693681886665589fd9512d6b473c` |
| Retrieved at | 2026-11-14T19:12:24.075232+00:00 |
| Files in this snapshot | 209 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (3 files)
    docker-build-development.yaml
    docker-build-latest.yaml
    docker-build-release.yaml
custom/  (1 files)
  .gitkeep
db/  (1 files)
  .gitkeep
docs/  (2 files)
  api/  (2 files)
    api.js
    generate.js
server/  (184 files)
  handlers/  (8 files)
    auth.handler.js
    domains.handler.js
    helpers.handler.js
    links.handler.js
    locals.handler.js
    renders.handler.js
    users.handler.js
    validators.handler.js
  mail/  (6 files)
    index.js
    mail.js
    template-change-email.html
    template-reset.html
    template-verify.html
    text.js
  migrations/  (10 files)
    20200211220920_constraints.js
    20200510140704_domains.js
    20200718124944_description.js
    20200730203154_expire_in.js
    20200810195255_change_email.js
    20241103083933_user-roles.js
    20241223062111_indexes.js
    20241223103044_visits_user_id.js
    20241223155527_visits_user_id_index.js
    20250106070444_remove_cooldown.js
  models/  (7 files)
    domain.model.js
    host.model.js
    index.js
    ip.model.js
    link.model.js
    user.model.js
    visit.model.js
  queries/  (6 files)
    domain.queries.js
    host.queries.js
    index.js
    link.queries.js
    user.queries.js
    visit.queries.js
  queues/  (3 files)
    index.js
    queues.js
    visit.js
  routes/  (8 files)
    auth.routes.js
    domain.routes.js
    health.routes.js
    index.js
    link.routes.js
    renders.routes.js
    routes.js
    user.routes.js
  utils/  (5 files)
    asyncHandler.js
    index.js
    knex.js
    map.json
    utils.js
  views/  (124 files)
    partials/  (105 files)
      … 105 files under this directory
    404.hbs
    admin.hbs
    banned.hbs
    create_admin.hbs
    error.hbs
    homepage.hbs
    layout.hbs
    login.hbs
    logout.hbs
    protected.hbs
    report.hbs
    reset_password.hbs
    reset_password_set_new_password.hbs
    settings.hbs
    stats.hbs
    terms.hbs
    url_info.hbs
    verify.hbs
    verify_change_email.hbs
  consts.js
  cron.js
  env.js
  knex.js
  passport.js
  redis.js
  server.js
static/  (5 files)
  css/  (1 files)
    styles.css
  scripts/  (2 files)
    main.js
    stats.js
  manifest.webmanifest
  robots.txt
.dockerignore
.example.env
.gitignore
Dockerfile
LICENSE
README.md
docker-compose.mariadb.yml
docker-compose.postgres.yml
docker-compose.sqlite-redis.yml
docker-compose.yml
jsconfig.json
knexfile.js
package.json
```

## Entry points

- [server/server.js](https://github.com/thedevs-network/kutt/blob/029da42b2459693681886665589fd9512d6b473c/server/server.js)
- [server/mail/index.js](https://github.com/thedevs-network/kutt/blob/029da42b2459693681886665589fd9512d6b473c/server/mail/index.js)
- [server/models/index.js](https://github.com/thedevs-network/kutt/blob/029da42b2459693681886665589fd9512d6b473c/server/models/index.js)
- [server/queries/index.js](https://github.com/thedevs-network/kutt/blob/029da42b2459693681886665589fd9512d6b473c/server/queries/index.js)
- [server/queues/index.js](https://github.com/thedevs-network/kutt/blob/029da42b2459693681886665589fd9512d6b473c/server/queues/index.js)
- [server/routes/index.js](https://github.com/thedevs-network/kutt/blob/029da42b2459693681886665589fd9512d6b473c/server/routes/index.js)
- [server/utils/index.js](https://github.com/thedevs-network/kutt/blob/029da42b2459693681886665589fd9512d6b473c/server/utils/index.js)
- [static/scripts/main.js](https://github.com/thedevs-network/kutt/blob/029da42b2459693681886665589fd9512d6b473c/static/scripts/main.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 16 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 8 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 7 file(s) under data layer (observed from repository paths and static analysis). |
| server package | library | Observed | Groups 33 file(s) under server package (observed from repository paths and static analysis). |
| static package | library | Observed | Groups 2 file(s) under static package (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.github/workflows/docker-build-development.yaml` (ci)
- `.github/workflows/docker-build-latest.yaml` (ci)
- `.github/workflows/docker-build-release.yaml` (ci)
- `Dockerfile` (container)
- `docker-compose.mariadb.yml` (config)
- `docker-compose.postgres.yml` (config)
- `docker-compose.sqlite-redis.yml` (config)
- `docker-compose.yml` (container)
- `jsconfig.json` (config)
- `package.json` (manifest)
- `server/utils/map.json` (config)

## Top-level layout

- `server` — 184 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `static` — 5 analysed file(s)
- `.github` — 3 analysed file(s)
- `docs` — 2 analysed file(s)
- `custom` — 1 analysed file(s)
- `db` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `029da42b2459693681886665589fd9512d6b473c` is the revision these paths and observations refer to.
