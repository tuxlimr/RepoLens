# Project structure: sansan0/TrendRadar

**Analysed commit:** `8a316628215c53ad34b7200ecb0fba76de3ef6c7`

**Commit reference:** [8a316628215c53ad34b7200ecb0fba76de3ef6c7](https://github.com/sansan0/TrendRadar/commit/8a316628215c53ad34b7200ecb0fba76de3ef6c7)

**Tree at this commit:** [sansan0/TrendRadar@8a316628215c](https://github.com/sansan0/TrendRadar/tree/8a316628215c53ad34b7200ecb0fba76de3ef6c7)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | sansan0/TrendRadar |
| Description | ⭐AI-driven public opinion & trend monitor with multi-platform aggregation, RSS, and smart alerts.🎯 告别信息过载，你的 AI 舆情监控助手与热点筛选工具！聚合多平台热点 +  RSS 订阅，支持关键词精准筛选。AI 智能筛选新闻 + AI 翻译 +  AI 分析简报直推手机，也支持接入 MCP 架构，赋能 AI 自然语言对话分析、情感洞察与趋势预测等。支持 Docker ，数据本地/云端自持。集成微信/飞书/钉钉/Telegram/邮件/ntfy/bark/slack 等渠道智能推送。 |
| Stars | 63634 |
| Forks | 24911 |
| Licence | GPL-3.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `8a316628215c53ad34b7200ecb0fba76de3ef6c7` |
| Retrieved at | 2026-11-14T19:06:21.322685+00:00 |
| Files in this snapshot | 129 |

## Directory tree

```text
.github/  (8 files)
  ISSUE_TEMPLATE/  (4 files)
    01-bug-report.yml
    02-feature-request.yml
    03-ai-and-config.yml
    config.yml
  workflows/  (4 files)
    clean-crawler.yml
    crawler.yml
    docker.yml
    issue-guard.yml
config/  (14 files)
  ai_filter/  (3 files)
    extract_prompt.txt
    prompt.txt
    update_tags_prompt.txt
  custom/  (2 files)
    ai/  (1 files)
      … 1 files under this directory
    keyword/  (1 files)
      … 1 files under this directory
  ai_analysis_prompt.txt
  ai_interests.txt
  ai_translation_prompt.txt
  config.en.yaml
  config.yaml
  frequency_words.en.txt
  frequency_words.txt
  timeline.en.yaml
  timeline.yaml
docker/  (6 files)
  Dockerfile
  Dockerfile.mcp
  docker-compose-build.yml
  docker-compose.yml
  entrypoint.sh
  manage.py
docs/  (3 files)
  assets/  (2 files)
    i18n.js
    style.css
  index.html
mcp_server/  (19 files)
  services/  (4 files)
    __init__.py
    cache_service.py
    data_service.py
    parser_service.py
  tools/  (9 files)
    __init__.py
    analytics.py
    article_reader.py
    config_mgmt.py
    data_query.py
    notification.py
    search_tools.py
    storage_sync.py
    system.py
  utils/  (4 files)
    __init__.py
    date_parser.py
    errors.py
    validators.py
  __init__.py
  server.py
tests/  (8 files)
  test_ai_analysis_response.py
  test_ai_extra_params.py
  test_config_serialization.py
  test_frequency.py
  test_mcp_stdio.py
  test_rss_total_count.py
  test_storage_sync.py
  test_time.py
trendradar/  (54 files)
  ai/  (8 files)
    __init__.py
    analyzer.py
    client.py
    filter.py
    filter_pipeline.py
    formatter.py
    prompt_loader.py
    translator.py
  commands/  (5 files)
    __init__.py
    doctor.py
    status.py
    test_notification.py
    version.py
  core/  (8 files)
    __init__.py
    analyzer.py
    cdn.py
    config.py
    data.py
    frequency.py
    loader.py
    scheduler.py
  crawler/  (5 files)
    rss/  (3 files)
      … 3 files under this directory
    __init__.py
    fetcher.py
  notification/  (7 files)
    __init__.py
    batch.py
    dispatcher.py
    formatters.py
    renderer.py
    senders.py
    splitter.py
  report/  (6 files)
    __init__.py
    formatter.py
    generator.py
    helpers.py
    html.py
    rss_html.py
  storage/  (9 files)
    __init__.py
    ai_filter_schema.sql
    base.py
    local.py
    manager.py
    remote.py
    rss_schema.sql
    schema.sql
    sqlite_mixin.py
  utils/  (3 files)
    __init__.py
    time.py
    url.py
  __init__.py
  __main__.py
  context.py
.dockerignore
LICENSE
README-Cherry-Studio.md
README-EN.md
README-MCP-FAQ-EN.md
README-MCP-FAQ.md
README.md
index.html
pyproject.toml
setup-mac.sh
setup-windows-en.bat
setup-windows.bat
start-http.bat
start-http.sh
version
version_configs
version_mcp
```

## Entry points

- [docker/manage.py:733](https://github.com/sansan0/TrendRadar/blob/8a316628215c53ad34b7200ecb0fba76de3ef6c7/docker/manage.py#L733)
- [mcp_server/server.py](https://github.com/sansan0/TrendRadar/blob/8a316628215c53ad34b7200ecb0fba76de3ef6c7/mcp_server/server.py)
- [trendradar/__main__.py](https://github.com/sansan0/TrendRadar/blob/8a316628215c53ad34b7200ecb0fba76de3ef6c7/trendradar/__main__.py)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 10 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: get_account_at_index, limit_accounts, parse_multi_account_config, validate_paired_… |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 6 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: LocalStorageBackend, NewsData, NewsItem, RSSData, RSSItem, RemoteStorageBackend. Observed top-level fun… |
| docker package | library | Observed | Groups 1 file(s) under docker package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 3 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: NewsAnalyzer. Observed top-level functions: _cleanup_stale_pid, _get_tools, _is_expected_w… |
| External integrations | external | Observed | Groups 1 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: AIClient. |
| mcp_server package | library | Observed | Groups 14 file(s) under mcp_server package (observed from repository paths and static analysis). Observed top-level classes: AnalyticsTools, ArticleReaderTools, ConfigManagementTools, ConfigResult, ConfigurationError, C… |
| Service / domain layer | service | Observed | Groups 11 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: CacheService, DataService, ParserService, ResolvedSchedule, Scheduler. Observed top-level… |
| Tests | test | Observed | Groups 9 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: AIExtraParamsTests, AnalysisResponseNormalizationTests, ConfigSerializationTests, GlobalFilterTests, MCPTran… |
| trendradar package | library | Observed | Groups 34 file(s) under trendradar package (observed from repository paths and static analysis). Observed top-level classes: AIAnalysisResult, AIAnalyzer, AIFilter, AIFilterPipeline, AIFilterResult, AITranslator. Observ… |

## Important files

- `.dockerignore` (container)
- `.github/ISSUE_TEMPLATE/01-bug-report.yml` (config)
- `.github/ISSUE_TEMPLATE/02-feature-request.yml` (config)
- `.github/ISSUE_TEMPLATE/03-ai-and-config.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/clean-crawler.yml` (ci)
- `.github/workflows/crawler.yml` (ci)
- `.github/workflows/docker.yml` (ci)
- `.github/workflows/issue-guard.yml` (ci)
- `config/config.en.yaml` (config)
- `config/config.yaml` (config)
- `config/timeline.en.yaml` (config)
- `config/timeline.yaml` (config)
- `docker/Dockerfile` (container)
- `docker/Dockerfile.mcp` (container)
- `docker/docker-compose-build.yml` (config)
- `docker/docker-compose.yml` (container)
- `pyproject.toml` (manifest)

## Top-level layout

- `trendradar` — 54 analysed file(s)
- `mcp_server` — 19 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `config` — 14 analysed file(s)
- `.github` — 8 analysed file(s)
- `tests` — 8 analysed file(s)
- `docker` — 6 analysed file(s)
- `docs` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `8a316628215c53ad34b7200ecb0fba76de3ef6c7` is the revision these paths and observations refer to.
