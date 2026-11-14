# Project structure: Usagi-org/ai-goofish-monitor

**Analysed commit:** `77f8d75869acd65f9dba72731b95c7c49ea67bdf`

**Commit reference:** [77f8d75869acd65f9dba72731b95c7c49ea67bdf](https://github.com/Usagi-org/ai-goofish-monitor/commit/77f8d75869acd65f9dba72731b95c7c49ea67bdf)

**Tree at this commit:** [Usagi-org/ai-goofish-monitor@77f8d75869ac](https://github.com/Usagi-org/ai-goofish-monitor/tree/77f8d75869acd65f9dba72731b95c7c49ea67bdf)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Usagi-org/ai-goofish-monitor |
| Description | 基于 Playwright 和AI实现的闲鱼多任务实时/定时监控与智能分析系统，配备了功能完善的后台管理UI。帮助用户从闲鱼海量商品中，找到心仪产品。 |
| Stars | 19922 |
| Forks | 3229 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `77f8d75869acd65f9dba72731b95c7c49ea67bdf` |
| Retrieved at | 2026-11-14T19:08:05.232739+00:00 |
| Files in this snapshot | 295 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (2 files)
    claude.yml
    docker-image.yml
chrome-extension/  (5 files)
  README.md
  background.js
  manifest.json
  popup.html
  popup.js
prompts/  (2 files)
  base_prompt.txt
  macbook_criteria.txt
src/  (77 files)
  api/  (12 files)
    routes/  (10 files)
      … 10 files under this directory
    __init__.py
    dependencies.py
  core/  (1 files)
    cron_utils.py
  domain/  (6 files)
    models/  (3 files)
      … 3 files under this directory
    repositories/  (2 files)
      … 2 files under this directory
    __init__.py
  infrastructure/  (22 files)
    config/  (3 files)
      … 3 files under this directory
    external/  (12 files)
      … 12 files under this directory
    persistence/  (6 files)
      … 6 files under this directory
    __init__.py
  services/  (24 files)
    __init__.py
    account_strategy_service.py
    ai_request_compat.py
    ai_response_parser.py
    ai_service.py
    dashboard_payloads.py
    dashboard_service.py
    item_analysis_dispatcher.py
    notification_config_service.py
    notification_service.py
    price_history_service.py
    process_service.py
    result_blacklist_service.py
    result_export_service.py
    result_file_service.py
    result_storage_service.py
    scheduler_service.py
    search_pagination.py
    seller_profile_cache.py
    task_generation_runner.py
    task_generation_service.py
    task_log_cleanup_service.py
    task_payloads.py
    task_service.py
  __init__.py
  ai_handler.py
  ai_message_builder.py
  app.py
  config.py
  failure_guard.py
  keyword_rule_engine.py
  parsers.py
  prompt_utils.py
  rotation.py
  scraper.py
  utils.py
tests/  (43 files)
  fixtures/  (6 files)
    config.sample.json
    ratings.json
    search_results.json
    state.sample.json
    user_head.json
    user_items.json
  integration/  (6 files)
    test_api_dashboard.py
    test_api_results.py
    test_api_settings.py
    test_api_tasks.py
    test_cli_spider.py
    test_pipeline_parse.py
  live/  (3 files)
    _support.py
    conftest.py
    test_live_smoke.py
  unit/  (23 files)
    test_ai_client.py
    test_ai_handler_analysis.py
    test_ai_handler_downloads.py
    test_ai_request_compat.py
    test_ai_response_parser.py
    test_app_lifespan.py
    test_cron_utils.py
    test_domain_task.py
    test_env_manager.py
    test_item_analysis_dispatcher.py
    test_keyword_rule_engine.py
    test_notification_service.py
    test_price_history_service.py
    test_process_service.py
    test_prompt_utils.py
    test_result_blacklist_service.py
    test_scraper_browser_channel.py
    test_scraper_extra_headers.py
    test_scraper_region_filter.py
    test_search_pagination.py
    test_seller_profile_cache.py
    test_task_log_cleanup_service.py
    test_utils.py
  README.md
  __init__.py
  conftest.py
  test_failure_guard.py
  test_frontend_build_paths.py
web-ui/  (142 files)
  .vscode/  (1 files)
    extensions.json
  public/  (1 files)
    vite.svg
  src/  (127 files)
    api/  (7 files)
      … 7 files under this directory
    assets/  (2 files)
      … 2 files under this directory
    components/  (84 files)
      … 84 files under this directory
    composables/  (9 files)
      … 9 files under this directory
    data/  (1 files)
      … 1 files under this directory
    i18n/  (5 files)
      … 5 files under this directory
    layouts/  (1 files)
      … 1 files under this directory
    lib/  (4 files)
      … 4 files under this directory
    router/  (1 files)
      … 1 files under this directory
    services/  (1 files)
      … 1 files under this directory
    types/  (3 files)
      … 3 files under this directory
    views/  (7 files)
      … 7 files under this directory
    App.vue
    main.ts
  .gitignore
  Dockerfile
  README.md
  components.json
  index.html
  nginx.conf
  package.json
  postcss.config.cjs
  tailwind.config.cjs
  tsconfig.app.json
  tsconfig.json
  tsconfig.node.json
  vite.config.ts
.dockerignore
.env.example
.gitignore
AGENTS.md
CLAUDE.md
DISCLAIMER.md
Dockerfile
Dockerfile.base
Dockerfile.release
LICENSE
README.md
README_EN.md
config.json
config.json.example
desktop_launcher.py
docker-compose.dev.yaml
docker-compose.yaml
pyproject.toml
requirements-runtime.txt
requirements.txt
run_live_smoke.sh
spider_v2.py
start.sh
xianyu-login-state-privacy.html
```

## Entry points

- [src/app.py:98](https://github.com/Usagi-org/ai-goofish-monitor/blob/77f8d75869acd65f9dba72731b95c7c49ea67bdf/src/app.py#L98)
- [desktop_launcher.py:45](https://github.com/Usagi-org/ai-goofish-monitor/blob/77f8d75869acd65f9dba72731b95c7c49ea67bdf/desktop_launcher.py#L45)
- [spider_v2.py:219](https://github.com/Usagi-org/ai-goofish-monitor/blob/77f8d75869acd65f9dba72731b95c7c49ea67bdf/spider_v2.py#L219)
- [web-ui/src/i18n/index.ts](https://github.com/Usagi-org/ai-goofish-monitor/blob/77f8d75869acd65f9dba72731b95c7c49ea67bdf/web-ui/src/i18n/index.ts)
- [web-ui/src/main.ts](https://github.com/Usagi-org/ai-goofish-monitor/blob/77f8d75869acd65f9dba72731b95c7c49ea67bdf/web-ui/src/main.ts)
- [web-ui/src/router/index.ts](https://github.com/Usagi-org/ai-goofish-monitor/blob/77f8d75869acd65f9dba72731b95c7c49ea67bdf/web-ui/src/router/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| ai_handler.py package | library | Observed | Groups 1 file(s) under ai_handler.py package (observed from repository paths and static analysis). Observed top-level functions: _build_debug_request_summary, _build_image_save_path, _download_single_image, _extract_mes… |
| ai_message_builder.py package | library | Observed | Groups 1 file(s) under ai_message_builder.py package (observed from repository paths and static analysis). Observed top-level functions: build_analysis_text_prompt, build_user_message_content. |
| API layer | api | Observed | Groups 26 file(s) under api layer (observed from repository paths and static analysis). Observed routes: GET (path not a literal), GET /{name}, POST (path not a literal), PUT /{name}, DELETE /{name}. Observed top-level… |
| chrome-extension package | library | Observed | Groups 2 file(s) under chrome-extension package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 24 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: AISettings, AppSettings, EnvManager, NotificationSettings, ScraperSettings. Observed… |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 11 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: JsonTaskRepository, SqliteTaskRepository, Task, TaskCreate, TaskGenerateRequest, TaskGenerationJob. Ob… |
| Application entry point | entrypoint | Observed | Groups 3 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed routes: GET /health, POST /auth/status, GET /, GET /{full_pa… |
| External integrations | external | Observed | Groups 12 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: AIClient, BarkClient, GotifyClient, NotificationClient, NotificationMessage, NtfyClient. Ob… |
| failure_guard.py package | library | Observed | Groups 1 file(s) under failure_guard.py package (observed from repository paths and static analysis). Observed top-level classes: FailureGuard, SkipDecision, _FileLock. Observed top-level functions: _as_int, _atomic_wri… |
| infrastructure package | library | Observed | Groups 1 file(s) under infrastructure package (observed from repository paths and static analysis). |
| __init__.py package | library | Observed | Groups 1 file(s) under __init__.py package (observed from repository paths and static analysis). |
| keyword_rule_engine.py package | library | Observed | Groups 1 file(s) under keyword_rule_engine.py package (observed from repository paths and static analysis). Observed top-level functions: _collect_text_fragments, _keyword_matches, _normalize_keywords, _uses_ascii_token… |
| parsers.py package | library | Observed | Groups 1 file(s) under parsers.py package (observed from repository paths and static analysis). Observed top-level functions: _parse_search_results_json, _parse_user_items_data, calculate_reputation_from_ratings, parse_… |
| prompt_utils.py package | library | Observed | Groups 1 file(s) under prompt_utils.py package (observed from repository paths and static analysis). Observed top-level functions: _close_ai_client, _read_reference_text, _report_progress, _request_generated_text, _stri… |
| rotation.py package | library | Observed | Groups 1 file(s) under rotation.py package (observed from repository paths and static analysis). Observed top-level classes: RotationItem, RotationPool. Observed top-level functions: load_state_files, parse_proxy_pool. |
| scraper.py package | library | Observed | Groups 1 file(s) under scraper.py package (observed from repository paths and static analysis). Observed top-level classes: LoginRequiredError, RiskControlError. Observed top-level functions: _as_bool, _as_int, _build_c… |
| Service / domain layer | service | Observed | Groups 27 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: AIAnalysisService, EmptyAIResponseError, ItemAnalysisDispatcher, ItemAnalysisJob, Notifica… |
| Tests | test | Observed | Groups 43 file(s) under tests (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed top-level classes: FakeLocator, FakePage, FakeProcess, FakeProcessService, Fa… |
| utils.py package | library | Observed | Groups 1 file(s) under utils.py package (observed from repository paths and static analysis). Observed top-level functions: build_task_log_path, convert_goofish_link, format_registration_days, get_link_unique_key, log_t… |
| web-ui package | library | Observed | Groups 110 file(s) under web-ui package (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.env.example` (config)
- `.github/workflows/claude.yml` (ci)
- `.github/workflows/docker-image.yml` (ci)
- `Dockerfile` (container)
- `Dockerfile.base` (container)
- `Dockerfile.release` (container)
- `chrome-extension/manifest.json` (config)
- `config.json` (config)
- `docker-compose.dev.yaml` (config)
- `docker-compose.yaml` (container)
- `pyproject.toml` (manifest)
- `requirements-runtime.txt` (manifest)
- `requirements.txt` (manifest)
- `web-ui/.vscode/extensions.json` (config)
- `web-ui/Dockerfile` (container)
- `web-ui/components.json` (config)
- `web-ui/package.json` (manifest)
- `web-ui/src/data/goofishRegions.json` (config)
- `web-ui/tsconfig.app.json` (config)
- `web-ui/tsconfig.json` (config)
- `web-ui/tsconfig.node.json` (config)

## Top-level layout

- `web-ui` — 142 analysed file(s)
- `src` — 77 analysed file(s)
- `tests` — 43 analysed file(s)
- `(root files)` — 24 analysed file(s)
- `chrome-extension` — 5 analysed file(s)
- `.github` — 2 analysed file(s)
- `prompts` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `77f8d75869acd65f9dba72731b95c7c49ea67bdf` is the revision these paths and observations refer to.
