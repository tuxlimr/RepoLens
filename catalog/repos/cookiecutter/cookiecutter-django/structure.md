# Project structure: cookiecutter/cookiecutter-django

**Analysed commit:** `adcbd39660c1fc5d40086ad8837099bdbc8b0b54`

**Commit reference:** [adcbd39660c1fc5d40086ad8837099bdbc8b0b54](https://github.com/cookiecutter/cookiecutter-django/commit/adcbd39660c1fc5d40086ad8837099bdbc8b0b54)

**Tree at this commit:** [cookiecutter/cookiecutter-django@adcbd39660c1](https://github.com/cookiecutter/cookiecutter-django/tree/adcbd39660c1fc5d40086ad8837099bdbc8b0b54)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | cookiecutter/cookiecutter-django |
| Description | Cookiecutter Django is a framework for jumpstarting production-ready Django projects quickly. |
| Stars | 13636 |
| Forks | 3069 |
| Licence | BSD-3-Clause |
| Language | Python |
| Default branch | main |
| Analysed commit | `adcbd39660c1fc5d40086ad8837099bdbc8b0b54` |
| Retrieved at | 2026-11-14T19:09:46.365076+00:00 |
| Files in this snapshot | 250 |

## Directory tree

```text
.github/  (18 files)
  ISSUE_TEMPLATE/  (4 files)
    bug.md
    feature.md
    paid-support.md
    question.md
  workflows/  (8 files)
    align-versions.yml
    ci.yml
    dependabot-uv-lock.yml
    django-issue-checker.yml
    issue-manager.yml
    pre-commit-autoupdate.yml
    update-changelog.yml
    update-contributors.yml
  CONTRIBUTORS-template.md
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
  changelog-template.md
  contributors.json
  dependabot.yml
docs/  (26 files)
  1-getting-started/  (2 files)
    project-generation-options.rst
    settings.rst
  2-local-development/  (3 files)
    developing-locally-docker.rst
    developing-locally.rst
    generate-project-block.rst
  3-deployment/  (4 files)
    cloud-storage.rst
    deployment-on-heroku.rst
    deployment-on-pythonanywhere.rst
    deployment-with-docker.rst
  4-guides/  (5 files)
    docker-postgres-backups.rst
    document.rst
    linters.rst
    testing.rst
    websocket.rst
  5-help/  (2 files)
    faq.rst
    troubleshooting.rst
  6-about/  (3 files)
    contributing.md
    generative-ai.md
    maintainer-guide.md
  _static/  (1 files)
    .gitkeep
  includes/  (1 files)
    mailgun.rst
  Makefile
  __init__.py
  conf.py
  index.rst
  make.bat
hooks/  (3 files)
  __init__.py
  post_gen_project.py
  pre_gen_project.py
scripts/  (6 files)
  __init__.py
  create_django_issue.py
  node_version.py
  python_dependency_version.py
  update_changelog.py
  update_contributors.py
tests/  (6 files)
  __init__.py
  test_bare.sh
  test_cookiecutter_generation.py
  test_docker.sh
  test_generate.ps1
  test_hooks.py
{{cookiecutter.project_slug}}/  (175 files)
  .devcontainer/  (3 files)
    bash_history
    bashrc.override.sh
    devcontainer.json
  .envs/  (4 files)
    .local/  (2 files)
      … 2 files under this directory
    .production/  (2 files)
      … 2 files under this directory
  .github/  (2 files)
    workflows/  (1 files)
      … 1 files under this directory
    dependabot.yml
  bin/  (1 files)
    post_compile
  compose/  (31 files)
    local/  (9 files)
      … 9 files under this directory
    production/  (22 files)
      … 22 files under this directory
  config/  (13 files)
    settings/  (5 files)
      … 5 files under this directory
    __init__.py
    api.py
    api_router.py
    asgi.py
    celery_app.py
    urls.py
    websocket.py
    wsgi.py
  docs/  (8 files)
    pycharm/  (1 files)
      … 1 files under this directory
    Makefile
    __init__.py
    conf.py
    howto.rst
    index.rst
    make.bat
    users.rst
  locale/  (4 files)
    en_US/  (1 files)
      … 1 files under this directory
    fr_FR/  (1 files)
      … 1 files under this directory
    pt_BR/  (1 files)
      … 1 files under this directory
    README.md
  requirements/  (3 files)
    base.txt
    local.txt
    production.txt
  tests/  (2 files)
    __init__.py
    test_merge_production_dotenvs_in_dotenv.py
  utility/  (13 files)
    install_os_dependencies.sh
    install_python_dependencies.sh
    requirements-bionic.apt
    requirements-bookworm.apt
    requirements-bullseye.apt
    requirements-buster.apt
    requirements-focal.apt
    requirements-jammy.apt
    requirements-jessie.apt
    requirements-noble.apt
    requirements-stretch.apt
    requirements-trusty.apt
    requirements-xenial.apt
  webpack/  (3 files)
    common.config.js
    dev.config.js
    prod.config.js
  {{cookiecutter.project_slug}}/  (64 files)
    contrib/  (7 files)
      … 7 files under this directory
    static/  (6 files)
      … 6 files under this directory
    templates/  (19 files)
      … 19 files under this directory
    users/  (30 files)
      … 30 files under this directory
    __init__.py
    conftest.py
  .dockerignore
  .drone.yml
  .editorconfig
  .gitattributes
  .gitignore
  .gitlab-ci.yml
  .pre-commit-config.yaml
  .python-version
  .readthedocs.yml
  .travis.yml
  CONTRIBUTORS.txt
  COPYING
  LICENSE
  Procfile
  README.md
  docker-compose.docs.yml
  docker-compose.local.yml
  docker-compose.production.yml
  gulpfile.mjs
  justfile
  manage.py
  merge_production_dotenvs_in_dotenv.py
  package.json
  pyproject.toml
.editorconfig
.gitattributes
.gitignore
.pre-commit-config.yaml
.pyup.yml
.readthedocs.yaml
AGENTS.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
CONTRIBUTORS.md
LICENSE
README.md
SECURITY.md
cookiecutter.json
pyproject.toml
tox.ini
```

## Entry points

- [hooks/post_gen_project.py:597](https://github.com/cookiecutter/cookiecutter-django/blob/adcbd39660c1fc5d40086ad8837099bdbc8b0b54/hooks/post_gen_project.py#L597)
- [scripts/create_django_issue.py:303](https://github.com/cookiecutter/cookiecutter-django/blob/adcbd39660c1fc5d40086ad8837099bdbc8b0b54/scripts/create_django_issue.py#L303)
- [scripts/node_version.py:57](https://github.com/cookiecutter/cookiecutter-django/blob/adcbd39660c1fc5d40086ad8837099bdbc8b0b54/scripts/node_version.py#L57)
- [scripts/python_dependency_version.py:72](https://github.com/cookiecutter/cookiecutter-django/blob/adcbd39660c1fc5d40086ad8837099bdbc8b0b54/scripts/python_dependency_version.py#L72)
- [scripts/update_changelog.py:163](https://github.com/cookiecutter/cookiecutter-django/blob/adcbd39660c1fc5d40086ad8837099bdbc8b0b54/scripts/update_changelog.py#L163)
- [scripts/update_contributors.py:99](https://github.com/cookiecutter/cookiecutter-django/blob/adcbd39660c1fc5d40086ad8837099bdbc8b0b54/scripts/update_contributors.py#L99)
- [{{cookiecutter.project_slug}}/config/celery_app.py:9](https://github.com/cookiecutter/cookiecutter-django/blob/adcbd39660c1fc5d40086ad8837099bdbc8b0b54/%7B%7Bcookiecutter.project_slug%7D%7D/config/celery_app.py#L9)
- [{{cookiecutter.project_slug}}/manage.py:30](https://github.com/cookiecutter/cookiecutter-django/blob/adcbd39660c1fc5d40086ad8837099bdbc8b0b54/%7B%7Bcookiecutter.project_slug%7D%7D/manage.py#L30)
- [{{cookiecutter.project_slug}}/merge_production_dotenvs_in_dotenv.py:29](https://github.com/cookiecutter/cookiecutter-django/blob/adcbd39660c1fc5d40086ad8837099bdbc8b0b54/%7B%7Bcookiecutter.project_slug%7D%7D/merge_production_dotenvs_in_dotenv.py#L29)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 4 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 38 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: websocket_application. |
| {{cookiecutter.project_slug}} package | library | Observed | Groups 35 file(s) under {{cookiecutter.project_slug}} package (observed from repository paths and static analysis). Observed top-level classes: Migration, UserManager, UsersConfig. Observed top-level functions: _update_… |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 11 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Celery. Observed top-level classes: ContributorsJSONFile, DjVersion, GitHubMa… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 2 file(s) under hooks package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 22 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: _fixture_id, build_files_list, check_paths, context, test_append_to_gitignore_file, test_django_upgrade_p… |

## Important files

- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/contributors.json` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/align-versions.yml` (ci)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/dependabot-uv-lock.yml` (ci)
- `.github/workflows/django-issue-checker.yml` (ci)
- `.github/workflows/issue-manager.yml` (ci)
- `.github/workflows/pre-commit-autoupdate.yml` (ci)
- `.github/workflows/update-changelog.yml` (ci)
- `.github/workflows/update-contributors.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `.pyup.yml` (config)
- `.readthedocs.yaml` (config)
- `cookiecutter.json` (config)
- `pyproject.toml` (manifest)
- `tox.ini` (config)
- `{{cookiecutter.project_slug}}/.devcontainer/devcontainer.json` (config)
- `{{cookiecutter.project_slug}}/.dockerignore` (container)
- `{{cookiecutter.project_slug}}/.drone.yml` (config)
- `{{cookiecutter.project_slug}}/.editorconfig` (config)
- `{{cookiecutter.project_slug}}/.github/dependabot.yml` (config)
- `{{cookiecutter.project_slug}}/.github/workflows/ci.yml` (ci)
- `{{cookiecutter.project_slug}}/.gitlab-ci.yml` (ci)
- `{{cookiecutter.project_slug}}/.pre-commit-config.yaml` (config)
- `{{cookiecutter.project_slug}}/.readthedocs.yml` (config)
- `{{cookiecutter.project_slug}}/.travis.yml` (ci)
- `{{cookiecutter.project_slug}}/compose/local/django/Dockerfile` (container)
- `{{cookiecutter.project_slug}}/compose/local/docs/Dockerfile` (container)
- `{{cookiecutter.project_slug}}/compose/local/node/Dockerfile` (container)
- `{{cookiecutter.project_slug}}/compose/local/uv/Dockerfile` (container)
- `{{cookiecutter.project_slug}}/compose/production/aws/Dockerfile` (container)
- `{{cookiecutter.project_slug}}/compose/production/django/Dockerfile` (container)
- `{{cookiecutter.project_slug}}/compose/production/nginx/Dockerfile` (container)
- `{{cookiecutter.project_slug}}/compose/production/postgres/Dockerfile` (container)
- `{{cookiecutter.project_slug}}/compose/production/traefik/Dockerfile` (container)
- `{{cookiecutter.project_slug}}/compose/production/traefik/traefik.yml` (config)
- `{{cookiecutter.project_slug}}/docker-compose.docs.yml` (config)
- `{{cookiecutter.project_slug}}/docker-compose.local.yml` (config)
- `{{cookiecutter.project_slug}}/docker-compose.production.yml` (config)
- `{{cookiecutter.project_slug}}/package.json` (manifest)
- `{{cookiecutter.project_slug}}/pyproject.toml` (manifest)

## Top-level layout

- `{{cookiecutter.project_slug}}` — 175 analysed file(s)
- `docs` — 26 analysed file(s)
- `.github` — 18 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `scripts` — 6 analysed file(s)
- `tests` — 6 analysed file(s)
- `hooks` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 16 file(s) were skipped during inventory (2 x lockfile excluded; 14 x vendored/generated directory excluded).
- File {{cookiecutter.project_slug}}/config/__init__.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File {{cookiecutter.project_slug}}/config/api_router.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File {{cookiecutter.project_slug}}/config/settings/base.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File {{cookiecutter.project_slug}}/config/settings/local.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File {{cookiecutter.project_slug}}/config/settings/production.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File {{cookiecutter.project_slug}}/config/settings/test.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File {{cookiecutter.project_slug}}/config/urls.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File {{cookiecutter.project_slug}}/docs/conf.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File {{cookiecutter.project_slug}}/{{cookiecutter.project_slug}}/conftest.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File {{cookiecutter.project_slug}}/{{cookiecutter.project_slug}}/users/adapters.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File {{cookiecutter.project_slug}}/{{cookiecutter.project_slug}}/users/admin.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File {{cookiecutter.project_slug}}/{{cookiecutter.project_slug}}/users/api/schema.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File {{cookiecutter.project_slug}}/{{cookiecutter.project_slug}}/users/api/serializers.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File {{cookiecutter.project_slug}}/{{cookiecutter.project_slug}}/users/api/views.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File {{cookiecutter.project_slug}}/{{cookiecutter.project_slug}}/users/forms.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File {{cookiecutter.project_slug}}/{{cookiecutter.project_slug}}/users/migrations/0001_initial.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File {{cookiecutter.project_slug}}/{{cookiecutter.project_slug}}/users/models.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File {{cookiecutter.project_slug}}/{{cookiecutter.project_slug}}/users/tests/api/test_openapi.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File {{cookiecutter.project_slug}}/{{cookiecutter.project_slug}}/users/tests/api/test_urls.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File {{cookiecutter.project_slug}}/{{cookiecutter.project_slug}}/users/tests/api/test_views.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File {{cookiecutter.project_slug}}/{{cookiecutter.project_slug}}/users/tests/factories.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File {{cookiecutter.project_slug}}/{{cookiecutter.project_slug}}/users/tests/test_admin.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File {{cookiecutter.project_slug}}/{{cookiecutter.project_slug}}/users/tests/test_forms.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File {{cookiecutter.project_slug}}/{{cookiecutter.project_slug}}/users/tests/test_managers.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File {{cookiecutter.project_slug}}/{{cookiecutter.project_slug}}/users/tests/test_models.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File {{cookiecutter.project_slug}}/{{cookiecutter.project_slug}}/users/tests/test_tasks.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File {{cookiecutter.project_slug}}/{{cookiecutter.project_slug}}/users/tests/test_urls.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File {{cookiecutter.project_slug}}/{{cookiecutter.project_slug}}/users/tests/test_views.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File {{cookiecutter.project_slug}}/{{cookiecutter.project_slug}}/users/urls.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File {{cookiecutter.project_slug}}/{{cookiecutter.project_slug}}/users/views.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `adcbd39660c1fc5d40086ad8837099bdbc8b0b54` is the revision these paths and observations refer to.
