# Project structure: lss233/kirara-ai

**Analysed commit:** `36249e4a0aa8e3d8930acdfe4e14ec2be6484f63`

**Commit reference:** [36249e4a0aa8e3d8930acdfe4e14ec2be6484f63](https://github.com/lss233/kirara-ai/commit/36249e4a0aa8e3d8930acdfe4e14ec2be6484f63)

**Tree at this commit:** [lss233/kirara-ai@36249e4a0aa8](https://github.com/lss233/kirara-ai/tree/36249e4a0aa8e3d8930acdfe4e14ec2be6484f63)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | lss233/kirara-ai |
| Description | 🤖 可 DIY 的 多模态 AI 聊天机器人 | 🚀 快速接入 微信、 QQ、Telegram、等聊天平台 | 🦈支持DeepSeek、Grok、Claude、Ollama、Gemini、OpenAI | 工作流系统、网页搜索、AI画图、人设调教、虚拟女仆、语音对话 |  |
| Stars | 19293 |
| Forks | 1836 |
| Licence | AGPL-3.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `36249e4a0aa8e3d8930acdfe4e14ec2be6484f63` |
| Retrieved at | 2026-11-14T19:08:13.689509+00:00 |
| Files in this snapshot | 339 |

## Directory tree

```text
.cursor/  (1 files)
  rules/  (1 files)
    create-workflow.mdc
.github/  (11 files)
  ISSUE_TEMPLATE/  (2 files)
    bug-report.md
    feature-request.md
  quickstarts/  (1 files)
    windows/  (1 files)
      … 1 files under this directory
  workflows/  (7 files)
    docker-latest.yml
    docker-tag.yml
    pr_review.yml
    project_check.yml
    quickstart-windows.yml
    run-tests.yml
    stale.yml
  dependabot.yml
data/  (10 files)
  dispatch_rules/  (1 files)
    rules.yaml
  media/  (1 files)
    .gitignore
  memory/  (1 files)
    .gitignore
  web/  (1 files)
    .gitkeep
  workflows/  (5 files)
    chat/  (4 files)
      … 4 files under this directory
    .gitkeep
  .gitkeep
docker/  (1 files)
  start.sh
kirara_ai/  (234 files)
  alembic/  (4 files)
    versions/  (1 files)
      … 1 files under this directory
    README
    env.py
    script.py.mako
  config/  (3 files)
    __init__.py
    config_loader.py
    global_config.py
  database/  (2 files)
    __init__.py
    manager.py
  events/  (11 files)
    tracing/  (3 files)
      … 3 files under this directory
    __init__.py
    application.py
    event_bus.py
    im.py
    listen.py
    llm.py
    plugin.py
    workflow.py
  im/  (7 files)
    __init__.py
    adapter.py
    im_registry.py
    manager.py
    message.py
    profile.py
    sender.py
  ioc/  (3 files)
    __init__.py
    container.py
    inject.py
  llm/  (11 files)
    format/  (7 files)
      … 7 files under this directory
    adapter.py
    llm_manager.py
    llm_registry.py
    model_types.py
  mcp_module/  (4 files)
    __init__.py
    manager.py
    models.py
    server.py
  media/  (12 files)
    carrier/  (4 files)
      … 4 files under this directory
    types/  (2 files)
      … 2 files under this directory
    utils/  (2 files)
      … 2 files under this directory
    __init__.py
    manager.py
    media_object.py
    metadata.py
  memory/  (17 files)
    composes/  (6 files)
      … 6 files under this directory
    persistences/  (5 files)
      … 5 files under this directory
    scopes/  (3 files)
      … 3 files under this directory
    entry.py
    memory_manager.py
    registry.py
  plugin_manager/  (5 files)
    models.py
    plugin.py
    plugin_event_bus.py
    plugin_loader.py
    utils.py
  plugins/  (38 files)
    bundled_frpc/  (4 files)
      … 4 files under this directory
    im_http_legacy_adapter/  (4 files)
      … 4 files under this directory
    im_qqbot_adapter/  (4 files)
      … 4 files under this directory
    im_telegram_adapter/  (3 files)
      … 3 files under this directory
    im_wecom_adapter/  (4 files)
      … 4 files under this directory
    llm_preset_adapters/  (18 files)
      … 18 files under this directory
    .gitkeep
  system/  (2 files)
    __init__.py
    updater.py
  tracing/  (6 files)
    __init__.py
    core.py
    decorator.py
    llm_tracer.py
    manager.py
    models.py
  web/  (54 files)
    api/  (45 files)
      … 45 files under this directory
    auth/  (5 files)
      … 5 files under this directory
    README.md
    __init__.py
    app.py
    utils.py
  workflow/  (50 files)
    core/  (24 files)
      … 24 files under this directory
    implementations/  (25 files)
      … 25 files under this directory
    utils/  (1 files)
      … 1 files under this directory
  __init__.py
  __main__.py
  entry.py
  internal.py
  logger.py
tests/  (68 files)
  llm_adapters/  (14 files)
    mock_app/  (8 files)
      … 8 files under this directory
    __init__.py
    conftest.py
    test_gemini_adapter.py
    test_ollama_adapter.py
    test_openai_adapter.py
    test_voyage_adapter.py
  memory/  (7 files)
    __init__.py
    test_composer_decomposer.py
    test_composer_strategy.py
    test_decomposer_strategy.py
    test_memory_manager.py
    test_persistence.py
    test_scope.py
  resources/  (1 files)
    test_image.txt
  system_blocks/  (17 files)
    game/  (3 files)
      … 3 files under this directory
    im/  (3 files)
      … 3 files under this directory
    llm/  (4 files)
      … 4 files under this directory
    memory/  (3 files)
      … 3 files under this directory
    system/  (3 files)
      … 3 files under this directory
    __init__.py
  tracing/  (7 files)
    __init__.py
    test_base.py
    test_core.py
    test_decorator.py
    test_llm_tracer.py
    test_manager.py
    test_models.py
  utils/  (2 files)
    auth_test_utils.py
    test_block_registry.py
  web/  (7 files)
    api/  (6 files)
      … 6 files under this directory
    auth/  (1 files)
      … 1 files under this directory
  workflow_executor/  (4 files)
    test_block.py
    test_executor.py
    test_input_output.py
    test_workflow_basic.py
  __init__.py
  test_config_loader.py
  test_game_blocks.py
  test_mcp_server.py
  test_media.py
  test_media_element.py
  test_system_blocks.py
  test_workflow_builder.py
  test_workflow_factories.py
web/  (1 files)
  .gitkeep
.dockerignore
.editorconfig
.gitignore
.pre-commit-config.yaml
.pylintrc
Dockerfile
LICENSE
MANIFEST.in
README.md
alembic.ini
config.yaml.example
pyproject.toml
pytest.ini
```

## Entry points

- [kirara_ai/__main__.py](https://github.com/lss233/kirara-ai/blob/36249e4a0aa8e3d8930acdfe4e14ec2be6484f63/kirara_ai/__main__.py)
- [kirara_ai/web/app.py:109](https://github.com/lss233/kirara-ai/blob/36249e4a0aa8e3d8930acdfe4e14ec2be6484f63/kirara_ai/web/app.py#L109)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 38 file(s) under api layer (observed from repository paths and static analysis). Observed routes: ROUTE /status, ROUTE /config, ROUTE /start, ROUTE /stop, ROUTE /download. Observed top-level classes: BaseDiagnost… |
| Configuration and deployment | config | Observed | Groups 18 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: ConfigJsonSchema, ConfigLoader, DefaultConfig, FrpcConfig, GlobalConfig, IMConfig. O… |
| Data layer | data | Observed | Groups 8 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: ChangePasswordRequest, CombinedDispatchRule, DatabaseManager, FrpcConfigUpdate, FrpcDownloadProgress, F… |
| docker package | library | Observed | Groups 1 file(s) under docker package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 3 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed top-level classes: MCPServer, WebServer. Observed top-level… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| kirara_ai package | library | Observed | Groups 137 file(s) under kirara_ai package (observed from repository paths and static analysis). Observed top-level classes: AlibabaCloudAdapter, AlibabaCloudConfig, AppendIMMessage, ApplicationStarted, ApplicationStopp… |
| Service / domain layer | service | Observed | Groups 25 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: AuthService, Block, BlockConfig, BlockExecutionFailedException, BlockInput, BlockOutput. O… |
| Tests | test | Observed | Groups 70 file(s) under tests (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed routes: POST /models/{model}:generateContent, POST /models/{model}:batchEmbed… |

## Important files

- `.dockerignore` (container)
- `.editorconfig` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/docker-latest.yml` (ci)
- `.github/workflows/docker-tag.yml` (ci)
- `.github/workflows/pr_review.yml` (ci)
- `.github/workflows/project_check.yml` (ci)
- `.github/workflows/quickstart-windows.yml` (ci)
- `.github/workflows/run-tests.yml` (ci)
- `.github/workflows/stale.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `Dockerfile` (container)
- `MANIFEST.in` (manifest)
- `alembic.ini` (config)
- `data/dispatch_rules/rules.yaml` (config)
- `data/workflows/chat/dsr_thinking.yaml` (config)
- `data/workflows/chat/memory_store.yaml` (config)
- `data/workflows/chat/normal_multimodal.yaml` (config)
- `data/workflows/chat/talk_break.yaml` (config)
- `kirara_ai/plugins/im_http_legacy_adapter/setup.py` (manifest)
- `kirara_ai/plugins/im_qqbot_adapter/setup.py` (manifest)
- `kirara_ai/plugins/im_telegram_adapter/setup.py` (manifest)
- `kirara_ai/plugins/im_wecom_adapter/setup.py` (manifest)
- `kirara_ai/plugins/llm_preset_adapters/setup.py` (manifest)
- `pyproject.toml` (manifest)
- `pytest.ini` (config)

## Top-level layout

- `kirara_ai` — 234 analysed file(s)
- `tests` — 68 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `.github` — 11 analysed file(s)
- `data` — 10 analysed file(s)
- `.cursor` — 1 analysed file(s)
- `docker` — 1 analysed file(s)
- `web` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `36249e4a0aa8e3d8930acdfe4e14ec2be6484f63` is the revision these paths and observations refer to.
