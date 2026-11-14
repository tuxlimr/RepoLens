# Project structure: fastapi/full-stack-fastapi-template

**Analysed commit:** `aabb90126964a164e02aff39e7c385bb0598236d`

**Commit reference:** [aabb90126964a164e02aff39e7c385bb0598236d](https://github.com/fastapi/full-stack-fastapi-template/commit/aabb90126964a164e02aff39e7c385bb0598236d)

**Tree at this commit:** [fastapi/full-stack-fastapi-template@aabb90126964](https://github.com/fastapi/full-stack-fastapi-template/tree/aabb90126964a164e02aff39e7c385bb0598236d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | fastapi/full-stack-fastapi-template |
| Description | Full-stack web application template with FastAPI, React, SQLModel, PostgreSQL, Vite, Tailwind CSS, shadcn/ui, FastAPI Cloud, and Docker Compose. |
| Stars | 46250 |
| Forks | 9220 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `aabb90126964a164e02aff39e7c385bb0598236d` |
| Retrieved at | 2026-11-14T19:12:57.711074+00:00 |
| Files in this snapshot | 236 |

## Directory tree

```text
.agents/  (2 files)
  skills/  (2 files)
    library-skills/  (2 files)
      … 2 files under this directory
.claude/  (2 files)
  skills/  (2 files)
    library-skills/  (2 files)
      … 2 files under this directory
.github/  (19 files)
  workflows/  (15 files)
    add-to-project.yml
    bump-pre-commit-hooks.yml
    create-draft-release.yml
    deploy-docker-compose.yml
    deploy.yml
    detect-conflicts.yml
    guard-dependencies.yml
    issue-manager.yml
    playwright.yml
    pre-commit.yml
    prepare-release.yml
    smokeshow.yml
    test-backend.yml
    test-docker-compose.yml
    zizmor.yml
  dependabot.yml
  latest-changes.yml
  pr-push.yml
  pr-submit.yml
.vscode/  (2 files)
  extensions.json
  launch.json
backend/  (57 files)
  app/  (31 files)
    alembic/  (9 files)
      … 9 files under this directory
    api/  (9 files)
      … 9 files under this directory
    core/  (4 files)
      … 4 files under this directory
    email-templates/  (3 files)
      … 3 files under this directory
    __init__.py
    crud.py
    initial_data.py
    main.py
    models.py
    utils.py
  scripts/  (5 files)
    format.sh
    lint.sh
    prestart.sh
    test.sh
    tests-start.sh
  tests/  (15 files)
    api/  (6 files)
      … 6 files under this directory
    crud/  (2 files)
      … 2 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    utils/  (4 files)
      … 4 files under this directory
    __init__.py
    conftest.py
  .dockerignore
  .gitignore
  Dockerfile
  README.md
  alembic.ini
  pyproject.toml
frontend/  (117 files)
  public/  (4 files)
    assets/  (4 files)
      … 4 files under this directory
  src/  (87 files)
    client/  (16 files)
      … 16 files under this directory
    components/  (51 files)
      … 51 files under this directory
    hooks/  (4 files)
      … 4 files under this directory
    lib/  (1 files)
      … 1 files under this directory
    routes/  (10 files)
      … 10 files under this directory
    index.css
    main.tsx
    routeTree.gen.ts
    utils.ts
    vite-env.d.ts
  tests/  (12 files)
    utils/  (4 files)
      … 4 files under this directory
    admin.spec.ts
    auth.setup.ts
    config.ts
    items.spec.ts
    login.spec.ts
    reset-password.spec.ts
    sign-up.spec.ts
    user-settings.spec.ts
  .dockerignore
  .gitignore
  Dockerfile.playwright
  README.md
  biome.json
  components.json
  index.html
  openapi-ts.config.ts
  package.json
  playwright.config.ts
  tsconfig.build.json
  tsconfig.json
  tsconfig.node.json
  vite.config.ts
hooks/  (1 files)
  post_gen_project.py
img/  (1 files)
  github-social-preview.svg
packages/  (11 files)
  react-email/  (11 files)
    emails/  (3 files)
      … 3 files under this directory
    ui/  (5 files)
      … 5 files under this directory
    biome.json
    package.json
    tsconfig.json
scripts/  (5 files)
  add_latest_release_date.py
  generate-client.sh
  prepare_release.py
  test-local.sh
  test.sh
.dockerignore
.fastapicloudignore
.gitattributes
.gitignore
.pre-commit-config.yaml
.python-version
CONTRIBUTING.md
LICENSE
README.md
bun.lock
compose.deploy.yml
compose.override.yml
compose.yml
deployment-docker-compose.md
deployment.md
development.md
package.json
pyproject.toml
release-notes.md
```

## Entry points

- [backend/app/initial_data.py:22](https://github.com/fastapi/full-stack-fastapi-template/blob/aabb90126964a164e02aff39e7c385bb0598236d/backend/app/initial_data.py#L22)
- [backend/app/main.py:21](https://github.com/fastapi/full-stack-fastapi-template/blob/aabb90126964a164e02aff39e7c385bb0598236d/backend/app/main.py#L21)
- [scripts/add_latest_release_date.py:39](https://github.com/fastapi/full-stack-fastapi-template/blob/aabb90126964a164e02aff39e7c385bb0598236d/scripts/add_latest_release_date.py#L39)
- [scripts/prepare_release.py:16](https://github.com/fastapi/full-stack-fastapi-template/blob/aabb90126964a164e02aff39e7c385bb0598236d/scripts/prepare_release.py#L16)
- [frontend/src/client/index.ts](https://github.com/fastapi/full-stack-fastapi-template/blob/aabb90126964a164e02aff39e7c385bb0598236d/frontend/src/client/index.ts)
- [frontend/src/main.tsx](https://github.com/fastapi/full-stack-fastapi-template/blob/aabb90126964a164e02aff39e7c385bb0598236d/frontend/src/main.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 18 file(s) under api layer (observed from repository paths and static analysis). Observed routes: GET /, GET /{id}, POST /, PUT /{id}, DELETE /{id}. Observed top-level classes: PrivateUserCreate. Observed top-lev… |
| backend package | library | Observed | Groups 14 file(s) under backend package (observed from repository paths and static analysis). Observed top-level classes: EmailData. Observed top-level functions: authenticate, create_item, create_user, downgrade, gener… |
| Configuration and deployment | config | Observed | Groups 21 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: Settings. |
| Data layer | data | Observed | Groups 2 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: Item, ItemBase, ItemCreate, ItemPublic, ItemUpdate, ItemsPublic. Observed top-level functions: get_date… |
| Application entry point | entrypoint | Observed | Groups 5 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI, Typer. Observed top-level functions: bump_version, current_version, c… |
| External integrations | external | Observed | Groups 16 file(s) under external integrations (observed from repository paths and static analysis). |
| frontend package | library | Observed | Groups 63 file(s) under frontend package (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 1 file(s) under hooks package (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 7 file(s) under packages package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 3 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 2 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level functions: create_access_token, get_password_hash, verify_password. |
| Tests | test | Observed | Groups 29 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: authentication_token_from_email, client, create_random_item, create_random_user, db, get_superuser_token_… |

## Important files

- `.agents/skills/library-skills/.library-skills.json` (config)
- `.claude/skills/library-skills/.library-skills.json` (config)
- `.dockerignore` (container)
- `.github/dependabot.yml` (config)
- `.github/latest-changes.yml` (config)
- `.github/pr-push.yml` (config)
- `.github/pr-submit.yml` (config)
- `.github/workflows/add-to-project.yml` (ci)
- `.github/workflows/bump-pre-commit-hooks.yml` (ci)
- `.github/workflows/create-draft-release.yml` (ci)
- `.github/workflows/deploy-docker-compose.yml` (ci)
- `.github/workflows/deploy.yml` (ci)
- `.github/workflows/detect-conflicts.yml` (ci)
- `.github/workflows/guard-dependencies.yml` (ci)
- `.github/workflows/issue-manager.yml` (ci)
- `.github/workflows/playwright.yml` (ci)
- `.github/workflows/pre-commit.yml` (ci)
- `.github/workflows/prepare-release.yml` (ci)
- `.github/workflows/smokeshow.yml` (ci)
- `.github/workflows/test-backend.yml` (ci)
- `.github/workflows/test-docker-compose.yml` (ci)
- `.github/workflows/zizmor.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `.vscode/extensions.json` (config)
- `.vscode/launch.json` (config)
- `backend/.dockerignore` (container)
- `backend/Dockerfile` (container)
- `backend/alembic.ini` (config)
- `backend/pyproject.toml` (manifest)
- `compose.deploy.yml` (config)
- `compose.override.yml` (config)
- `compose.yml` (container)
- `frontend/.dockerignore` (container)
- `frontend/Dockerfile.playwright` (container)
- `frontend/biome.json` (config)
- `frontend/components.json` (config)
- `frontend/package.json` (manifest)
- `frontend/tsconfig.build.json` (config)
- `frontend/tsconfig.json` (config)
- `frontend/tsconfig.node.json` (config)
- `package.json` (manifest)
- `packages/react-email/biome.json` (config)
- `packages/react-email/package.json` (manifest)
- `packages/react-email/tsconfig.json` (config)
- `pyproject.toml` (manifest)

## Top-level layout

- `frontend` — 117 analysed file(s)
- `backend` — 57 analysed file(s)
- `(root files)` — 19 analysed file(s)
- `.github` — 19 analysed file(s)
- `packages` — 11 analysed file(s)
- `scripts` — 5 analysed file(s)
- `.agents` — 2 analysed file(s)
- `.claude` — 2 analysed file(s)
- `.vscode` — 2 analysed file(s)
- `hooks` — 1 analysed file(s)
- `img` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x likely secret file excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `aabb90126964a164e02aff39e7c385bb0598236d` is the revision these paths and observations refer to.
