# Project structure: volcengine/MineContext

**Analysed commit:** `171c7a9ea8091e326ddcf0f10718aa1b58c83c65`

**Commit reference:** [171c7a9ea8091e326ddcf0f10718aa1b58c83c65](https://github.com/volcengine/MineContext/commit/171c7a9ea8091e326ddcf0f10718aa1b58c83c65)

**Tree at this commit:** [volcengine/MineContext@171c7a9ea809](https://github.com/volcengine/MineContext/tree/171c7a9ea8091e326ddcf0f10718aa1b58c83c65)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | volcengine/MineContext |
| Description | MineContext is your proactive context-aware AI partner（Context-Engineering+ChatGPT Pulse） |
| Stars | 5547 |
| Forks | 414 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `171c7a9ea8091e326ddcf0f10718aa1b58c83c65` |
| Retrieved at | 2026-11-14T19:14:17.810317+00:00 |
| Files in this snapshot | 461 |

## Directory tree

```text
.github/  (6 files)
  ISSUE_TEMPLATE/  (4 files)
    01_bug_report.yml
    02_feature_request.yml
    03_docs_advice.yml
    config.yml
  workflows/  (1 files)
    release.yml
  PULL_REQUEST_TEMPLATE.md
config/  (4 files)
  config.yaml
  prompts_en.yaml
  prompts_zh.yaml
  quick_start_default.md
examples/  (8 files)
  .gitignore
  example_document_processor.py
  example_screenshot_processor.py
  example_screenshot_to_insights.py
  example_todo_deduplication.py
  example_weblink_processor.py
  regenerate_debug_file.py
  verify_folder_monitor.py
frontend/  (270 files)
  externals/  (8 files)
    python/  (8 files)
      … 8 files under this directory
  packages/  (12 files)
    shared/  (12 files)
      … 12 files under this directory
  resources/  (2 files)
    js/  (2 files)
      … 2 files under this directory
  scripts/  (2 files)
    copy-prebuilt-backend.js
    define-the-license-header.ts
  src/  (226 files)
    interface/  (3 files)
      … 3 files under this directory
    main/  (42 files)
      … 42 files under this directory
    preload/  (3 files)
      … 3 files under this directory
    renderer/  (178 files)
      … 178 files under this directory
  .editorconfig
  .env.example
  .gitignore
  .prettierignore
  .prettierrc
  .prettierrc.yaml
  README.md
  build-python.js
  build-python.sh
  components.json
  dev-app-update.yml
  electron-builder.yml
  electron.vite.config.ts
  eslint.config.mjs
  package.json
  start-dev.sh
  tailwind.config.js
  tsconfig.json
  tsconfig.node.json
  tsconfig.web.json
opencontext/  (157 files)
  config/  (4 files)
    __init__.py
    config_manager.py
    global_config.py
    prompt_manager.py
  context_capture/  (6 files)
    __init__.py
    base.py
    folder_monitor.py
    screenshot.py
    vault_document_monitor.py
    web_link_capture.py
  context_consumption/  (27 files)
    completion/  (3 files)
      … 3 files under this directory
    context_agent/  (17 files)
      … 17 files under this directory
    generation/  (6 files)
      … 6 files under this directory
    __init__.py
  context_processing/  (15 files)
    chunker/  (3 files)
      … 3 files under this directory
    merger/  (4 files)
      … 4 files under this directory
    processor/  (7 files)
      … 7 files under this directory
    __init__.py
  interfaces/  (4 files)
    __init__.py
    capture_interface.py
    processor_interface.py
    storage_interface.py
  llm/  (4 files)
    __init__.py
    global_embedding_client.py
    global_vlm_client.py
    llm_client.py
  managers/  (5 files)
    __init__.py
    capture_manager.py
    consumption_manager.py
    event_manager.py
    processor_manager.py
  models/  (3 files)
    __init__.py
    context.py
    enums.py
  monitoring/  (3 files)
    __init__.py
    metrics_collector.py
    monitor.py
  server/  (24 files)
    middleware/  (2 files)
      … 2 files under this directory
    routes/  (16 files)
      … 16 files under this directory
    __init__.py
    api.py
    component_initializer.py
    context_operations.py
    opencontext.py
    utils.py
  storage/  (8 files)
    backends/  (4 files)
      … 4 files under this directory
    __init__.py
    base_storage.py
    global_storage.py
    unified_storage.py
  tools/  (21 files)
    operation_tools/  (2 files)
      … 2 files under this directory
    profile_tools/  (2 files)
      … 2 files under this directory
    retrieval_tools/  (14 files)
      … 14 files under this directory
    base.py
    tool_definitions.py
    tools_executor.py
  utils/  (7 files)
    __init__.py
    file_utils.py
    image.py
    json_encoder.py
    json_parser.py
    logger.py
    logging_utils.py
  web/  (24 files)
    static/  (10 files)
      … 10 files under this directory
    templates/  (13 files)
      … 13 files under this directory
    __init__.py
  __init__.py
  cli.py
src/  (3 files)
  MineContext-Banner.svg
  architecture-overview-zh.md
  architecture-overview.md
.gitignore
.pre-commit-config.yaml
CONTRIBUTING.md
LICENSE
README.md
README_zh.md
SECURITY.md
build.bat
build.sh
hook-opencontext.py
opencontext.spec
package.json
pyproject.toml
```

## Entry points

- [opencontext/cli.py](https://github.com/volcengine/MineContext/blob/171c7a9ea8091e326ddcf0f10718aa1b58c83c65/opencontext/cli.py)
- [opencontext/server/opencontext.py:298](https://github.com/volcengine/MineContext/blob/171c7a9ea8091e326ddcf0f10718aa1b58c83c65/opencontext/server/opencontext.py#L298)
- [frontend/src/main/index.ts](https://github.com/volcengine/MineContext/blob/171c7a9ea8091e326ddcf0f10718aa1b58c83c65/frontend/src/main/index.ts)
- [frontend/src/preload/index.ts](https://github.com/volcengine/MineContext/blob/171c7a9ea8091e326ddcf0f10718aa1b58c83c65/frontend/src/preload/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 16 file(s) under api layer (observed from repository paths and static analysis). Observed routes: POST /chat, POST /chat/stream, POST /resume/{workflow_id}, GET /state/{workflow_id}, DELETE /cancel/{workflow_id}.… |
| Configuration and deployment | config | Observed | Groups 27 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: ConfigManager, GlobalConfig, PromptManager. Observed top-level functions: get_config… |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). Observed top-level functions: get_resource_path. |
| Data layer | data | Observed | Groups 17 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: ActionType, ChatMessage, ChromaDBBackend, Chunk, CompletionType, ContentFormat. Observed top-level fun… |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed top-level classes: OpenContext. Observed top-level functions… |
| External integrations | external | Observed | Groups 3 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: GlobalEmbeddingClient, GlobalVLMClient, LLMClient, LLMProvider, LLMType. Observed top-level… |
| frontend package | library | Observed | Groups 155 file(s) under frontend package (observed from repository paths and static analysis). |
| opencontext package | library | Observed | Groups 94 file(s) under opencontext package (observed from repository paths and static analysis). Observed top-level classes: ActivityContextStrategy, ActivityContextTool, ActivityInsight, ActivityPattern, ActivitySumma… |
| Service / domain layer | service | Observed | Groups 32 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: CompletionService, CompletionSuggestion, LLMContextStrategy, StateManager, StreamingManage… |

## Important files

- `.github/ISSUE_TEMPLATE/01_bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/02_feature_request.yml` (config)
- `.github/ISSUE_TEMPLATE/03_docs_advice.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/release.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `config/config.yaml` (config)
- `config/prompts_en.yaml` (config)
- `config/prompts_zh.yaml` (config)
- `frontend/.editorconfig` (config)
- `frontend/.env.example` (config)
- `frontend/.prettierrc.yaml` (config)
- `frontend/components.json` (config)
- `frontend/dev-app-update.yml` (config)
- `frontend/electron-builder.yml` (config)
- `frontend/externals/python/window_capture/requirements.txt` (manifest)
- `frontend/externals/python/window_inspector/requirements.txt` (manifest)
- `frontend/package.json` (manifest)
- `frontend/tsconfig.json` (config)
- `frontend/tsconfig.node.json` (config)
- `frontend/tsconfig.web.json` (config)
- `package.json` (manifest)
- `pyproject.toml` (manifest)

## Top-level layout

- `frontend` — 270 analysed file(s)
- `opencontext` — 157 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `examples` — 8 analysed file(s)
- `.github` — 6 analysed file(s)
- `config` — 4 analysed file(s)
- `src` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 5 file(s) were skipped during inventory (1 x likely secret file excluded; 1 x lockfile excluded; 3 x vendored/generated directory excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `171c7a9ea8091e326ddcf0f10718aa1b58c83c65` is the revision these paths and observations refer to.
