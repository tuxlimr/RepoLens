# Project structure: Cinnamon/kotaemon

**Analysed commit:** `9ad3e4e49aa35b8acddd235918a5d9753c1cfdf9`

**Commit reference:** [9ad3e4e49aa35b8acddd235918a5d9753c1cfdf9](https://github.com/Cinnamon/kotaemon/commit/9ad3e4e49aa35b8acddd235918a5d9753c1cfdf9)

**Tree at this commit:** [Cinnamon/kotaemon@9ad3e4e49aa3](https://github.com/Cinnamon/kotaemon/tree/9ad3e4e49aa35b8acddd235918a5d9753c1cfdf9)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Cinnamon/kotaemon |
| Description | An open-source RAG-based tool for chatting with your documents. |
| Stars | 25909 |
| Forks | 2169 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `9ad3e4e49aa35b8acddd235918a5d9753c1cfdf9` |
| Retrieved at | 2026-11-14T19:07:28.645739+00:00 |
| Files in this snapshot | 375 |

## Directory tree

```text
.github/  (9 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.yml
    config.yml
    feature_request.yml
  workflows/  (5 files)
    auto-bump-and-release.yaml
    build-push-docker.yaml
    pr-lint.yaml
    style-check.yaml
    unit-test.yaml
  PULL_REQUEST_TEMPLATE.md
docs/  (30 files)
  development/  (5 files)
    contributing.md
    create-a-component.md
    data-components.md
    index.md
    utilities.md
  extra/  (1 files)
    css/  (1 files)
      … 1 files under this directory
  integrations/  (2 files)
    docling.md
    paddle_ocr.md
  pages/  (7 files)
    app/  (7 files)
      … 7 files under this directory
  scripts/  (2 files)
    generate_examples_docs.py
    generate_reference_docs.py
  theme/  (8 files)
    assets/  (4 files)
      … 4 files under this directory
    partials/  (3 files)
      … 3 files under this directory
    main.html
  about.md
  index.md
  local_model.md
  online_install.md
  usage.md
libs/  (291 files)
  kotaemon/  (174 files)
    kotaemon/  (138 files)
      … 138 files under this directory
    tests/  (33 files)
      … 33 files under this directory
    README.md
    pyproject.toml
    pytest.ini
  ktem/  (117 files)
    ktem/  (103 files)
      … 103 files under this directory
    ktem_tests/  (5 files)
      … 5 files under this directory
    migrations/  (4 files)
      … 4 files under this directory
    .gitignore
    MANIFEST.in
    alembic.ini
    pyproject.toml
    requirements.txt
scripts/  (13 files)
  migrate/  (2 files)
    __init__.py
    migrate_chroma_db.py
  download_pdfjs.sh
  run_linux.sh
  run_macos.sh
  run_windows.bat
  serve_local.py
  server_llamacpp_linux.sh
  server_llamacpp_macos.sh
  server_llamacpp_windows.bat
  update_linux.sh
  update_macos.sh
  update_windows.bat
templates/  (10 files)
  component-default/  (1 files)
    README.md
  project-default/  (9 files)
    {{cookiecutter.project_name}}/  (8 files)
      … 8 files under this directory
    cookiecutter.json
.commitlintrc
.dockerignore
.env.example
.gitattributes
.gitignore
.pre-commit-config.yaml
.python-version
CODE_OF_CONDUCT.md
CONTRIBUTING.md
Dockerfile
LICENSE.txt
README.md
app.py
doc_env_reqs.txt
flowsettings.py
fly.toml
launch.sh
mkdocs.yml
pyproject.toml
settings.yaml.example
sso_app.py
sso_app_demo.py
```

## Entry points

- [libs/kotaemon/kotaemon/cli.py:20](https://github.com/Cinnamon/kotaemon/blob/9ad3e4e49aa35b8acddd235918a5d9753c1cfdf9/libs/kotaemon/kotaemon/cli.py#L20)
- [libs/kotaemon/kotaemon/llms/branching.py:157](https://github.com/Cinnamon/kotaemon/blob/9ad3e4e49aa35b8acddd235918a5d9753c1cfdf9/libs/kotaemon/kotaemon/llms/branching.py#L157)
- [libs/ktem/ktem/utils/conversation.py:97](https://github.com/Cinnamon/kotaemon/blob/9ad3e4e49aa35b8acddd235918a5d9753c1cfdf9/libs/ktem/ktem/utils/conversation.py#L97)
- [scripts/migrate/migrate_chroma_db.py:188](https://github.com/Cinnamon/kotaemon/blob/9ad3e4e49aa35b8acddd235918a5d9753c1cfdf9/scripts/migrate/migrate_chroma_db.py#L188)
- [scripts/serve_local.py:78](https://github.com/Cinnamon/kotaemon/blob/9ad3e4e49aa35b8acddd235918a5d9753c1cfdf9/scripts/serve_local.py#L78)
- [sso_app.py:33](https://github.com/Cinnamon/kotaemon/blob/9ad3e4e49aa35b8acddd235918a5d9753c1cfdf9/sso_app.py#L33)
- [sso_app_demo.py:51](https://github.com/Cinnamon/kotaemon/blob/9ad3e4e49aa35b8acddd235918a5d9753c1cfdf9/sso_app_demo.py#L51)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 18 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: BaseSettingGroup, SettingGroup, SettingIndexGroup, SettingIndexOption, SettingItem,… |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 9 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: Base, BaseConversation, BaseEmbeddingTable, BaseIssueReport, BaseLLMTable, BaseMCPTable. |
| Application entry point | entrypoint | Observed | Groups 11 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed routes: GET /favicon.ico, GET /, GET /favicon.ico, ROUTE /l… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| libs package | library | Observed | Groups 212 file(s) under libs package (observed from repository paths and static analysis). Observed top-level classes: AIMessage, AddQueryContextPipeline, AdobeReader, AgentAction, AgentFinish, AgentOutput. Observed to… |
| scripts package | library | Observed | Groups 8 file(s) under scripts package (observed from repository paths and static analysis). |
| templates package | library | Observed | Groups 2 file(s) under templates package (observed from repository paths and static analysis). Observed top-level classes: IndexingPipeline, QAResultLog, QuestionAnsweringPipeline. |
| Tests | test | Observed | Groups 37 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH openai.resources.chat.completions.Completions.create, PATCH openai.resources.chat.completions.Completions.create… |

## Important files

- `.dockerignore` (container)
- `.env.example` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/workflows/auto-bump-and-release.yaml` (ci)
- `.github/workflows/build-push-docker.yaml` (ci)
- `.github/workflows/pr-lint.yaml` (ci)
- `.github/workflows/style-check.yaml` (ci)
- `.github/workflows/unit-test.yaml` (ci)
- `.pre-commit-config.yaml` (config)
- `Dockerfile` (container)
- `fly.toml` (config)
- `libs/kotaemon/pyproject.toml` (manifest)
- `libs/kotaemon/pytest.ini` (config)
- `libs/ktem/MANIFEST.in` (manifest)
- `libs/ktem/alembic.ini` (config)
- `libs/ktem/ktem/pages/setup.py` (manifest)
- `libs/ktem/ktem_tests/resources/embedding_openai.json` (config)
- `libs/ktem/pyproject.toml` (manifest)
- `libs/ktem/requirements.txt` (manifest)
- `mkdocs.yml` (config)
- `pyproject.toml` (manifest)
- `templates/project-default/cookiecutter.json` (config)
- `templates/project-default/{{cookiecutter.project_name}}/.pre-commit-config.yaml` (config)
- `templates/project-default/{{cookiecutter.project_name}}/setup.py` (manifest)

## Top-level layout

- `libs` — 291 analysed file(s)
- `docs` — 30 analysed file(s)
- `(root files)` — 22 analysed file(s)
- `scripts` — 13 analysed file(s)
- `templates` — 10 analysed file(s)
- `.github` — 9 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `9ad3e4e49aa35b8acddd235918a5d9753c1cfdf9` is the revision these paths and observations refer to.
