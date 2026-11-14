# Project structure: JordanKnott/taskcafe

**Analysed commit:** `998db2a5da497a7902198a728ddc040fcacbacd6`

**Commit reference:** [998db2a5da497a7902198a728ddc040fcacbacd6](https://github.com/JordanKnott/taskcafe/commit/998db2a5da497a7902198a728ddc040fcacbacd6)

**Tree at this commit:** [JordanKnott/taskcafe@998db2a5da49](https://github.com/JordanKnott/taskcafe/tree/998db2a5da497a7902198a728ddc040fcacbacd6)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | JordanKnott/taskcafe |
| Description | An open source project management tool with Kanban boards |
| Stars | 5221 |
| Forks | 475 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `998db2a5da497a7902198a728ddc040fcacbacd6` |
| Retrieved at | 2026-11-14T19:14:23.651281+00:00 |
| Files in this snapshot | 491 |

## Directory tree

```text
.github/  (7 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    config.yml
  FUNDING.yml
  pull_request_template.md
  taskcafe-full.svg
  taskcafe.min.svg
  taskcafe.svg
cmd/  (2 files)
  mage/  (1 files)
    main.go
  taskcafe/  (1 files)
    main.go
conf/  (2 files)
  air.toml
  taskcafe.example.toml
frontend/  (285 files)
  .storybook/  (1 files)
    main.js
  public/  (3 files)
    index.html
    manifest.json
    robots.txt
  src/  (272 files)
    Admin/  (1 files)
      … 1 files under this directory
    App/  (12 files)
      … 12 files under this directory
    Auth/  (2 files)
      … 2 files under this directory
    Confirm/  (2 files)
      … 2 files under this directory
    Dashboard/  (1 files)
      … 1 files under this directory
    MyTasks/  (4 files)
      … 4 files under this directory
    Profile/  (1 files)
      … 1 files under this directory
    Projects/  (13 files)
      … 13 files under this directory
    Register/  (2 files)
      … 2 files under this directory
    Teams/  (4 files)
      … 4 files under this directory
    shared/  (223 files)
      … 223 files under this directory
    index.tsx
    outline.d.ts
    react-app-env.d.ts
    setupTests.ts
    styled.d.ts
    taskcafe.d.ts
    types.d.ts
  .editorconfig
  .eslintignore
  .eslintrc.json
  .gitignore
  .prettierrc.js
  Makefile
  codegen.yml
  package.json
  tsconfig.json
internal/  (98 files)
  commands/  (9 files)
    commands.go
    commands_prod.go
    job.go
    migrate.go
    reset_password.go
    seed.go
    token.go
    web.go
    worker.go
  config/  (1 files)
    config.go
  db/  (36 files)
    query/  (16 files)
      … 16 files under this directory
    db.go
    label_color.sql.go
    models.go
    notification.sql.go
    organization.sql.go
    project.sql.go
    project_label.sql.go
    querier.go
    repository.go
    system_options.sql.go
    task.sql.go
    task_activity.sql.go
    task_assigned.sql.go
    task_checklist.sql.go
    task_group.sql.go
    task_label.sql.go
    team.sql.go
    team_member.sql.go
    token.sql.go
    user_accounts.sql.go
  graph/  (37 files)
    schema/  (25 files)
      … 25 files under this directory
    graph.go
    helpers.go
    models_gen.go
    notification.resolvers.go
    project.resolvers.go
    resolver.go
    scalars.go
    schema.resolvers.go
    task.resolvers.go
    taskList.resolvers.go
    team.resolvers.go
    user.resolvers.go
  jobs/  (2 files)
    jobs.go
    logger.go
  logger/  (2 files)
    logger.go
    route_logger.go
  route/  (6 files)
    auth.go
    avatar.go
    log.go
    middleware.go
    route.go
    settings.go
  utils/  (5 files)
    context.go
    cursor.go
    mail.go
    redis.go
    version.go
migrations/  (72 files)
  0001_add-refresh-token-table.up.sql
  0002_add-user_account-table.up.sql
  0003_add-team-table.up.sql
  0004_add-project-table.up.sql
  0005_add-task-group-table.up.sql
  0006_add-task.up.sql
  0007_add-organization-table.up.sql
  0008_add-org-id-to-team-table.up.sql
  0009_add-task-assigned-table.up.sql
  0010_add-description-to-task-table.up.sql
  0011_add-label-color-table.up.sql
  0012_add-project-label-table.up.sql
  0013_add-due-date-to-task-table.up.sql
  0014_add-owner-column-to-project-table.up.sql
  0015_add-task-label-table.up.sql
  0016_add-profile_bg_color-column-to-user-account-table.up.sql
  0017_add-profile-bg-delete-cascade.up.sql
  0018_add-name-column-to-label-color.up.sql
  0019_add-unique-constraint-project-label-and-task-on-task-label.up.sql
  0020_add-full-name-column-to-user_account-table.up.sql
  0021_drop-first-name-column-from-user_account-table.up.sql
  0022_drop-last-name-column-from-user_account-table.up.sql
  0023_add-initials-column-to-user_account-table.up.sql
  0024_add-profile-avatar-url-column-to-user_account-table.up.sql
  … 48 more files
scripts/  (1 files)
  lint.sh
templates/  (1 files)
  mail/  (1 files)
    user/  (1 files)
      … 1 files under this directory
testing/  (2 files)
  docker-compose.dev.yml
  docker-compose.latest.yml
uploads/  (1 files)
  .keep
.cz.toml
.dockerignore
.gitignore
.pre-commit-config.yaml
.tmuxinator.yml
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
Dockerfile
LICENSE
Pipfile
README.md
docker-compose.dev.yml
docker-compose.migrate.yml
docker-compose.yml
go.mod
go.sum
gqlgen.yml
magefile.go
sqlc.yaml
```

## Entry points

- [frontend/.storybook/main.js](https://github.com/JordanKnott/taskcafe/blob/998db2a5da497a7902198a728ddc040fcacbacd6/frontend/.storybook/main.js)
- [frontend/src/Admin/index.tsx](https://github.com/JordanKnott/taskcafe/blob/998db2a5da497a7902198a728ddc040fcacbacd6/frontend/src/Admin/index.tsx)
- [frontend/src/App/index.tsx](https://github.com/JordanKnott/taskcafe/blob/998db2a5da497a7902198a728ddc040fcacbacd6/frontend/src/App/index.tsx)
- [frontend/src/Auth/index.tsx](https://github.com/JordanKnott/taskcafe/blob/998db2a5da497a7902198a728ddc040fcacbacd6/frontend/src/Auth/index.tsx)
- [frontend/src/Confirm/index.tsx](https://github.com/JordanKnott/taskcafe/blob/998db2a5da497a7902198a728ddc040fcacbacd6/frontend/src/Confirm/index.tsx)
- [frontend/src/Dashboard/index.tsx](https://github.com/JordanKnott/taskcafe/blob/998db2a5da497a7902198a728ddc040fcacbacd6/frontend/src/Dashboard/index.tsx)
- [frontend/src/MyTasks/index.tsx](https://github.com/JordanKnott/taskcafe/blob/998db2a5da497a7902198a728ddc040fcacbacd6/frontend/src/MyTasks/index.tsx)
- [frontend/src/Profile/index.tsx](https://github.com/JordanKnott/taskcafe/blob/998db2a5da497a7902198a728ddc040fcacbacd6/frontend/src/Profile/index.tsx)
- [frontend/src/Projects/index.tsx](https://github.com/JordanKnott/taskcafe/blob/998db2a5da497a7902198a728ddc040fcacbacd6/frontend/src/Projects/index.tsx)
- [frontend/src/Register/index.tsx](https://github.com/JordanKnott/taskcafe/blob/998db2a5da497a7902198a728ddc040fcacbacd6/frontend/src/Register/index.tsx)
- [frontend/src/Teams/index.tsx](https://github.com/JordanKnott/taskcafe/blob/998db2a5da497a7902198a728ddc040fcacbacd6/frontend/src/Teams/index.tsx)
- [frontend/src/index.tsx](https://github.com/JordanKnott/taskcafe/blob/998db2a5da497a7902198a728ddc040fcacbacd6/frontend/src/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| cmd package | library | Observed | Groups 2 file(s) under cmd package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 21 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 20 file(s) under data layer (observed from repository paths and static analysis). |
| frontend package | library | Observed | Groups 249 file(s) under frontend package (observed from repository paths and static analysis). |
| internal package | library | Observed | Groups 36 file(s) under internal package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |

## Important files

- `.cz.toml` (config)
- `.dockerignore` (container)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.pre-commit-config.yaml` (config)
- `.tmuxinator.yml` (config)
- `Dockerfile` (container)
- `Pipfile` (manifest)
- `conf/air.toml` (config)
- `conf/taskcafe.example.toml` (config)
- `docker-compose.dev.yml` (config)
- `docker-compose.migrate.yml` (config)
- `docker-compose.yml` (container)
- `frontend/.editorconfig` (config)
- `frontend/.eslintrc.json` (config)
- `frontend/codegen.yml` (config)
- `frontend/package.json` (manifest)
- `frontend/public/manifest.json` (config)
- `frontend/tsconfig.json` (config)
- `go.mod` (manifest)
- `gqlgen.yml` (config)
- `sqlc.yaml` (config)
- `testing/docker-compose.dev.yml` (config)
- `testing/docker-compose.latest.yml` (config)

## Top-level layout

- `frontend` — 285 analysed file(s)
- `internal` — 98 analysed file(s)
- `migrations` — 72 analysed file(s)
- `(root files)` — 20 analysed file(s)
- `.github` — 7 analysed file(s)
- `cmd` — 2 analysed file(s)
- `conf` — 2 analysed file(s)
- `testing` — 2 analysed file(s)
- `scripts` — 1 analysed file(s)
- `templates` — 1 analysed file(s)
- `uploads` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 3 file(s) were skipped during inventory (2 x likely secret file excluded; 1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `998db2a5da497a7902198a728ddc040fcacbacd6` is the revision these paths and observations refer to.
