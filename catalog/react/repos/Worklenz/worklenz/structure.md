# Project structure: Worklenz/worklenz

**Analysed commit:** `c0115ed217610a03b0b2da2fc28d17ec59d3e921`

**Commit reference:** [c0115ed217610a03b0b2da2fc28d17ec59d3e921](https://github.com/Worklenz/worklenz/commit/c0115ed217610a03b0b2da2fc28d17ec59d3e921)

**Tree at this commit:** [Worklenz/worklenz@c0115ed21761](https://github.com/Worklenz/worklenz/tree/c0115ed217610a03b0b2da2fc28d17ec59d3e921)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Worklenz/worklenz |
| Description | All in one project management tool for efficient teams |
| Stars | 3308 |
| Forks | 396 |
| Licence | AGPL-3.0 |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `c0115ed217610a03b0b2da2fc28d17ec59d3e921` |
| Retrieved at | 2026-11-14T19:15:25.309140+00:00 |
| Files in this snapshot | 798 |

## Directory tree

```text
.github/  (14 files)
  ISSUE_TEMPLATE/  (9 files)
    01_task.yml
    02_bug.yml
    03_user_request.yml
    04_hotfix.yml
    config.yml
    docs_issue.yml
    feature_request.yml
    feature_spec.yml
    security_issue.yml
  codeql/  (1 files)
    codeql-config.yml
  workflows/  (3 files)
    build-images.yaml
    ci.yaml
    codeql.yaml
  CODEOWNERS
addons/  (2 files)
  .gitignore
  README.md
docker/  (1 files)
  db-init-wrapper.sh
nginx/  (3 files)
  conf.d/  (1 files)
    worklenz.conf
  ssl/  (1 files)
    .gitkeep
  nginx.conf
scripts/  (12 files)
  oss-export/  (6 files)
    README.md
    allow.txt
    build-oss-tree.sh
    exclude.txt
    scan-secrets.sh
    scan-secrets.test.py
  add-short-weekdays.js
  add-util-keys.js
  check-i18n-translations.js
  db-init-wrapper.sh
  merge-schedule-translations.js
  test-e2e.js
security/  (11 files)
  phase1-emergency-mitigation/  (2 files)
    01-database-security.sql
    03-sql-injection-detector.ts
  phase2-sql-injection-fixes/  (9 files)
    01-tasks-controller-v2-example.ts
    02-tasks-controller-v2-getQuery-refactor.md
    03-reporting-projects-summary.md
    COMPLETION_SUMMARY.md
    DEPLOYMENT_CHECKLIST.md
    MIGRATION_GUIDE.md
    PHASE2_COMPLETE.md
    PROGRESS_REPORT.md
    README.md
worklenz-backend/  (728 files)
  cli/  (6 files)
    esbuild-patch
    generate-controller
    generate-validator
    inline-queries
    mkrelease
    swagger
  database/  (373 files)
    pg-migrations/  (353 files)
      … 353 files under this directory
    pg-migrations-support/  (1 files)
      … 1 files under this directory
    sql/  (12 files)
      … 12 files under this directory
    00_init.sh
    README-pg-migrations.md
    README.md
    apply-comment-migrations.sql
    create-test-client-user.sql
    fix-project-comment-function.sql
    project-comments-improvements.sql
  docs/  (1 files)
    security/  (1 files)
      … 1 files under this directory
  keys/  (1 files)
    .gitkeep
  release-notes/  (3 files)
    2026-08-15-example-release.md
    README.md
    v3.1.2-cloud.md
  scripts/  (12 files)
    build-addons.js
    compress.js
    convert-unmigrated-sql.js
    generate-pg-migrations.js
    migrate-addons.js
    migrate-bootstrap.js
    migrate.js
    populate-holidays.js
    reconcile-legacy-migration-ids.js
    run-holiday-population.sh
    validate-migration-ids.js
    verify-schedule-setup.js
  scss/  (1 files)
    style.scss
  src/  (312 files)
    __tests__/  (33 files)
      … 33 files under this directory
    addons/  (2 files)
      … 2 files under this directory
    bin/  (2 files)
      … 2 files under this directory
    config/  (4 files)
      … 4 files under this directory
    controllers/  (188 files)
      … 188 files under this directory
    cron_jobs/  (16 files)
      … 16 files under this directory
    data/  (1 files)
      … 1 files under this directory
    decorators/  (1 files)
      … 1 files under this directory
    docs/  (3 files)
      … 3 files under this directory
    interfaces/  (27 files)
      … 27 files under this directory
    jobs/  (1 files)
      … 1 files under this directory
    json_schemas/  (5 files)
      … 5 files under this directory
    middlewares/  (28 files)
      … 28 files under this directory
    app.ts
  .dockerignore
  .editorconfig
  .env.template
  .eslintrc.json
  .gitignore
  .gitmodules
  Dockerfile
  README.md
  apply-task-activity-migration.ps1
  apply-task-activity-migration.sh
  appspec.yml
  babel.config.js
  build.sh
  esbuild.js
  jest.config.js
  new
  package.json
  release
  sonar-project.properties
.coderabbit.yaml
.env.example
.gitattributes
.gitignore
.gitmodules
AGENTS.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
DEPLOYMENT_VERIFICATION_CHECKLIST.md
DESIGN.md
DOCKER_SETUP.md
LICENSE
README.md
SECURITY-REVIEW.md
SECURITY.md
SELF_HOSTING.md
SETUP_THE_PROJECT.md
backup.sh
deploy.sh
docker-compose.yml
manage.sh
quick-setup.sh
start.bat
start.sh
… 3 more files
```

## Entry points

- [scripts/oss-export/scan-secrets.test.py:64](https://github.com/Worklenz/worklenz/blob/c0115ed217610a03b0b2da2fc28d17ec59d3e921/scripts/oss-export/scan-secrets.test.py#L64)
- [worklenz-backend/src/app.ts](https://github.com/Worklenz/worklenz/blob/c0115ed217610a03b0b2da2fc28d17ec59d3e921/worklenz-backend/src/app.ts)
- [worklenz-backend/src/cron_jobs/index.ts](https://github.com/Worklenz/worklenz/blob/c0115ed217610a03b0b2da2fc28d17ec59d3e921/worklenz-backend/src/cron_jobs/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 186 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 14 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 7 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 355 file(s) under data layer (observed from repository paths and static analysis). |
| docker package | library | Observed | Groups 1 file(s) under docker package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: SecretScannerTest. |
| scripts package | library | Observed | Groups 8 file(s) under scripts package (observed from repository paths and static analysis). |
| security package | library | Observed | Groups 2 file(s) under security package (observed from repository paths and static analysis). |
| worklenz-backend package | library | Observed | Groups 131 file(s) under worklenz-backend package (observed from repository paths and static analysis). |

## Important files

- `.coderabbit.yaml` (config)
- `.env.example` (config)
- `.github/ISSUE_TEMPLATE/01_task.yml` (config)
- `.github/ISSUE_TEMPLATE/02_bug.yml` (config)
- `.github/ISSUE_TEMPLATE/03_user_request.yml` (config)
- `.github/ISSUE_TEMPLATE/04_hotfix.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/docs_issue.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_spec.yml` (config)
- `.github/ISSUE_TEMPLATE/security_issue.yml` (config)
- `.github/codeql/codeql-config.yml` (config)
- `.github/workflows/build-images.yaml` (ci)
- `.github/workflows/ci.yaml` (ci)
- `.github/workflows/codeql.yaml` (ci)
- `docker-compose.yml` (container)
- `worklenz-backend/.dockerignore` (container)
- `worklenz-backend/.editorconfig` (config)
- `worklenz-backend/.env.template` (config)
- `worklenz-backend/.eslintrc.json` (config)
- `worklenz-backend/Dockerfile` (container)
- `worklenz-backend/appspec.yml` (config)
- `worklenz-backend/package.json` (manifest)
- `worklenz-backend/src/data/sri-lankan-holidays.json` (config)
- `worklenz-backend/src/docs/openapi.yaml` (config)

## Top-level layout

- `worklenz-backend` — 728 analysed file(s)
- `(root files)` — 27 analysed file(s)
- `.github` — 14 analysed file(s)
- `scripts` — 12 analysed file(s)
- `security` — 11 analysed file(s)
- `nginx` — 3 analysed file(s)
- `addons` — 2 analysed file(s)
- `docker` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (1 x likely secret file excluded; 1 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `c0115ed217610a03b0b2da2fc28d17ec59d3e921` is the revision these paths and observations refer to.
