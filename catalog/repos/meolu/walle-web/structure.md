# Project structure: meolu/walle-web

**Analysed commit:** `f96dc41ed882782d52ec62fddbe0213b8b9158ec`

**Commit reference:** [f96dc41ed882782d52ec62fddbe0213b8b9158ec](https://github.com/meolu/walle-web/commit/f96dc41ed882782d52ec62fddbe0213b8b9158ec)

**Tree at this commit:** [meolu/walle-web@f96dc41ed882](https://github.com/meolu/walle-web/tree/f96dc41ed882782d52ec62fddbe0213b8b9158ec)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | meolu/walle-web |
| Description | walle - 瓦力 Devops开源项目代码部署平台 |
| Stars | 11979 |
| Forks | 2736 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `f96dc41ed882782d52ec62fddbe0213b8b9158ec` |
| Retrieved at | 2026-11-14T19:10:19.455650+00:00 |
| Files in this snapshot | 160 |

## Directory tree

```text
.github/  (3 files)
  ISSUE_TEMPLATE/  (3 files)
    bug---.md
    fix----------------.md
    suggest----.md
fe/  (47 files)
  static/  (43 files)
    js/  (43 files)
      … 43 files under this directory
  .eslintignore
  .eslintrc
  .gitignore
  index.html
gateway/  (2 files)
  nginx/  (2 files)
    ssl/  (1 files)
      … 1 files under this directory
    default.conf
migrations/  (11 files)
  versions/  (7 files)
    00adfdca30bf_03_server.py
    0af33c7b8832_06_task_rollback.py
    2bca06a823a0_01_init_walle_database.py
    52a2df18b1d4_02_add_index.py
    5ff964e844a7_07_project_include.py
    91c4d13540c3_05_task_username.py
    9532a372b5aa_04_preject_remove_server.py
  README
  alembic.ini
  env.py
  script.py.mako
requirements/  (2 files)
  dev.txt
  prod.txt
tests/  (18 files)
  __init__.py
  conftest.py
  factories.py
  test_00_base.py
  test_00_login.py
  test_01_api_environment.py
  test_02_api_role.py
  test_03_api_user.py
  test_04_api_passport.py
  test_05_api_space.py
  test_06_api_server.py
  test_07_api_project.py
  test_08_api_task.py
  test_config.py
  test_forms.py
  test_functional.py
  test_models.py
  utils.py
walle/  (66 files)
  api/  (15 files)
    __init__.py
    access.py
    api.py
    deploy.py
    environment.py
    general.py
    group.py
    passport.py
    project.py
    repo.py
    role.py
    server.py
    space.py
    task.py
    user.py
  config/  (5 files)
    __init__.py
    settings.py
    settings_dev.py
    settings_prod.py
    settings_test.py
  form/  (10 files)
    __init__.py
    environment.py
    group.py
    project.py
    role.py
    server.py
    space.py
    tag.py
    task.py
    user.py
  model/  (13 files)
    __init__.py
    database.py
    environment.py
    member.py
    menu.py
    project.py
    record.py
    role.py
    server.py
    space.py
    tag.py
    task.py
    user.py
  service/  (19 files)
    git/  (2 files)
      … 2 files under this directory
    notice/  (3 files)
      … 3 files under this directory
    rbac/  (4 files)
      … 4 files under this directory
    __init__.py
    code.py
    deployer.py
    emails.py
    error.py
    extensions.py
    tokens.py
    utils.py
    waller.py
    websocket.py
  templates/  (1 files)
    socketio.html
  __init__.py
  app.py
  commands.py
.dockerignore
.editorconfig
.gitignore
.travis.yml
Dockerfile
LICENSE
README.md
admin.sh
docker-compose.yml
walle.env
waller.py
```

## Entry points

- [walle/app.py:42](https://github.com/meolu/walle-web/blob/f96dc41ed882782d52ec62fddbe0213b8b9158ec/walle/app.py#L42)
- [walle/commands.py:18](https://github.com/meolu/walle-web/blob/f96dc41ed882782d52ec62fddbe0213b8b9158ec/walle/commands.py#L18)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 14 file(s) under api layer (observed from repository paths and static analysis). Observed top-level classes: AccessAPI, ApiResource, Base, DeployAPI, EnvironmentAPI, GeneralAPI. |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: Config, DevConfig, ProdConfig. |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: CRUDMixin, Model, SurrogatePK. Observed top-level functions: parse_operator, reference_col. |
| Application entry point | entrypoint | Observed | Groups 4 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Flask. Observed top-level classes: InfoFilter, ServerAPI, ServerForm, ServerMo… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| fe package | library | Observed | Groups 43 file(s) under fe package (observed from repository paths and static analysis). |
| migrations package | library | Observed | Groups 8 file(s) under migrations package (observed from repository paths and static analysis). Observed top-level functions: create_environments, create_members, create_menus, create_projects, create_records, create_se… |
| Service / domain layer | service | Observed | Groups 19 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: Access, Code, Deployer, Dingding, Email, Notice. Observed top-level functions: _render_ema… |
| Tests | test | Observed | Groups 19 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: BaseFactory, TestAccess, TestApiBase, TestApiEnv, TestApiPassport, TestApiProject. Observed top-level funct… |
| walle package | library | Observed | Groups 22 file(s) under walle package (observed from repository paths and static analysis). Observed top-level classes: AnonymousUser, EnvironmentForm, EnvironmentModel, GroupForm, LoginForm, MemberModel. Observed top-l… |

## Important files

- `.dockerignore` (container)
- `.editorconfig` (config)
- `.travis.yml` (ci)
- `Dockerfile` (container)
- `docker-compose.yml` (container)
- `migrations/alembic.ini` (config)

## Top-level layout

- `walle` — 66 analysed file(s)
- `fe` — 47 analysed file(s)
- `tests` — 18 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `migrations` — 11 analysed file(s)
- `.github` — 3 analysed file(s)
- `gateway` — 2 analysed file(s)
- `requirements` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `f96dc41ed882782d52ec62fddbe0213b8b9158ec` is the revision these paths and observations refer to.
