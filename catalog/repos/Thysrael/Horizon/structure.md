# Project structure: Thysrael/Horizon

**Analysed commit:** `ae30765a45ea97f082f6913181289ddd49566eeb`

**Commit reference:** [ae30765a45ea97f082f6913181289ddd49566eeb](https://github.com/Thysrael/Horizon/commit/ae30765a45ea97f082f6913181289ddd49566eeb)

**Tree at this commit:** [Thysrael/Horizon@ae30765a45ea](https://github.com/Thysrael/Horizon/tree/ae30765a45ea97f082f6913181289ddd49566eeb)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Thysrael/Horizon |
| Description | 📡 Your own AI-powered news radar. Generates daily briefings in English & Chinese. | 用 AI 构建你专属的新闻雷达 |
| Stars | 14256 |
| Forks | 2061 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `ae30765a45ea97f082f6913181289ddd49566eeb` |
| Retrieved at | 2026-11-14T19:09:30.483669+00:00 |
| Files in this snapshot | 205 |

## Directory tree

```text
.github/  (4 files)
  ISSUE_TEMPLATE/  (1 files)
    feature_request.md
  workflows/  (2 files)
    daily-summary.yml.disabled
    deploy-docs.yml
  pull_request_template.md
data/  (3 files)
  config.example.json
  config.github.json
  presets.json
docs/  (19 files)
  _includes/  (1 files)
    head-custom.html
  assets/  (5 files)
    css/  (1 files)
      … 1 files under this directory
    js/  (1 files)
      … 1 files under this directory
    architecture.svg
    horizon-header.svg
    ofoxai-logo.svg
  _config.yml
  agent-skill.md
  chatgpt.md
  configuration.md
  extractors.md
  feed-en.xml
  feed-zh.xml
  horizon-hub-design.md
  index.md
  profiles.md
  scoring.md
  scrapers.md
  twitter-cookies.md
profiles/  (16 files)
  ai-creator/  (4 files)
    analysis.md
    enrichment.md
    match.md
    profile.json
  finance-news/  (4 files)
    analysis.md
    enrichment.md
    match.md
    profile.json
  tech-blog/  (4 files)
    analysis.md
    enrichment.md
    match.md
    profile.json
  tech-news/  (4 files)
    analysis.md
    enrichment.md
    match.md
    profile.json
scripts/  (2 files)
  check_mcp.py
  daily-run.sh
skills/  (5 files)
  horizon/  (5 files)
    evals/  (1 files)
      … 1 files under this directory
    references/  (2 files)
      … 2 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    SKILL.md
src/  (76 files)
  ai/  (19 files)
    prompting/  (6 files)
      … 6 files under this directory
    __init__.py
    analyzer.py
    chatgpt.py
    chatgpt_auth.py
    classifier.py
    client.py
    enricher.py
    errors.py
    localization.py
    markdown_utils.py
    summarizer.py
    tokens.py
    utils.py
  extractors/  (7 files)
    __init__.py
    base.py
    firecrawl.py
    outcrawl.py
    registry.py
    specstream.py
    trafilatura.py
  mcp/  (8 files)
    README.md
    __init__.py
    errors.py
    horizon_adapter.py
    integration.md
    run_store.py
    server.py
    service.py
  processing/  (5 files)
    __init__.py
    content.py
    history.py
    profiles.py
    tools.py
  scrapers/  (13 files)
    __init__.py
    base.py
    gdelt.py
    github.py
    google_news.py
    hackernews.py
    openbb.py
    ossinsight.py
    reddit.py
    rss.py
    telegram.py
    twitter.py
    twitter_playwright.py
  services/  (5 files)
    email.py
    webhook.py
    webhook_cli.py
    wechat.py
    wechat_cli.py
  setup/  (7 files)
    __init__.py
    ai_recommend.py
    chatgpt.py
    presets.py
    prompts.py
    tag_aliases.py
    wizard.py
  storage/  (2 files)
    __init__.py
    manager.py
  __init__.py
  _cli.py
  _file_utils.py
  collection_window.py
  console_icons.py
  logging_config.py
  main.py
  models.py
  orchestrator.py
  url_security.py
tests/  (67 files)
  conftest.py
  test_ai_parameter_compatibility.py
  test_ai_recommend.py
  test_analyzer.py
  test_azure_client.py
  test_balanced_digest.py
  test_category_wiring.py
  test_chained_client.py
  test_chatgpt_auth.py
  test_chatgpt_client.py
  test_classifier.py
  test_cli.py
  test_collection_windows.py
  test_console_icons.py
  test_content_selection.py
  test_cross_source_duplicates.py
  test_email.py
  test_enricher.py
  test_enrichment_publication.py
  test_extra_body.py
  test_extractors_firecrawl.py
  test_extractors_outcrawl.py
  test_extractors_registry.py
  test_extractors_specstream.py
  … 43 more files
.dockerignore
.env.example
.gitignore
CODE_OF_CONDUCT.md
CONTRIBUTING.md
Dockerfile
LICENSE
README.md
README_ja.md
README_zh.md
SECURITY.md
docker-compose.yml
pyproject.toml
```

## Entry points

- [src/main.py:135](https://github.com/Thysrael/Horizon/blob/ae30765a45ea97f082f6913181289ddd49566eeb/src/main.py#L135)
- [src/mcp/server.py:456](https://github.com/Thysrael/Horizon/blob/ae30765a45ea97f082f6913181289ddd49566eeb/src/mcp/server.py#L456)
- [src/services/webhook_cli.py:279](https://github.com/Thysrael/Horizon/blob/ae30765a45ea97f082f6913181289ddd49566eeb/src/services/webhook_cli.py#L279)
- [src/services/wechat_cli.py:217](https://github.com/Thysrael/Horizon/blob/ae30765a45ea97f082f6913181289ddd49566eeb/src/services/wechat_cli.py#L217)
- [src/setup/chatgpt.py:83](https://github.com/Thysrael/Horizon/blob/ae30765a45ea97f082f6913181289ddd49566eeb/src/setup/chatgpt.py#L83)
- [scripts/check_mcp.py:35](https://github.com/Thysrael/Horizon/blob/ae30765a45ea97f082f6913181289ddd49566eeb/scripts/check_mcp.py#L35)
- [skills/horizon/scripts/horizon_ops.py:118](https://github.com/Thysrael/Horizon/blob/ae30765a45ea97f082f6913181289ddd49566eeb/skills/horizon/scripts/horizon_ops.py#L118)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| ai package | library | Observed | Groups 18 file(s) under ai package (observed from repository paths and static analysis). Observed top-level classes: AIProviderUnavailableError, ChatGPTAuth, ChatGPTClient, ClassificationResponse, ContentAnalyzer, Conte… |
| _cli.py package | library | Observed | Groups 1 file(s) under _cli.py package (observed from repository paths and static analysis). Observed top-level functions: add_data_dir_arguments, add_log_level_argument. |
| collection_window.py package | library | Observed | Groups 1 file(s) under collection_window.py package (observed from repository paths and static analysis). Observed top-level functions: collection_hours. |
| Configuration and deployment | config | Observed | Groups 11 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| console_icons.py package | library | Observed | Groups 1 file(s) under console_icons.py package (observed from repository paths and static analysis). Observed top-level functions: get_icons. |
| Data layer | data | Observed | Groups 3 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AIConfig, AIProvider, ArtifactSource, CategoryGroupConfig, ClassificationResult, CollectionConfig. Obse… |
| Application entry point | entrypoint | Observed | Groups 7 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: _err, _hours_argument, _main, _make_test_items, _metrics_snapshot, _ok. |
| External integrations | external | Observed | Groups 1 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: AIClient, AnthropicClient, AzureOpenAIClient, ChainedAIClient, GeminiClient, OpenAIClient. O… |
| extractors package | library | Observed | Groups 7 file(s) under extractors package (observed from repository paths and static analysis). Observed top-level classes: BaseExtractor, ExtractorRegistry, FirecrawlExtractor, OutcrawlExtractor, SpecStreamExtractor, T… |
| _file_utils.py package | library | Observed | Groups 1 file(s) under _file_utils.py package (observed from repository paths and static analysis). Observed top-level functions: _atomic_write_text. |
| __init__.py package | library | Observed | Groups 1 file(s) under __init__.py package (observed from repository paths and static analysis). |
| logging_config.py package | library | Observed | Groups 1 file(s) under logging_config.py package (observed from repository paths and static analysis). Observed top-level functions: configure_logging. |
| mcp package | library | Observed | Groups 4 file(s) under mcp package (observed from repository paths and static analysis). Observed top-level classes: HorizonMcpError, RunStore. Observed top-level functions: _is_horizon_repo, _load_mcp_secrets, _resolve… |
| orchestrator.py package | library | Observed | Groups 1 file(s) under orchestrator.py package (observed from repository paths and static analysis). Observed top-level classes: BalancedDigestResult, FetchReport, FilteringPipelineResult, HorizonOrchestrator, SourceFet… |
| processing package | library | Observed | Groups 5 file(s) under processing package (observed from repository paths and static analysis). Observed top-level classes: ContentParts, HistoryEntry, HistorySearchTool, LoadedProfile, ProfileBlock, ProfileContent. Obs… |
| scrapers package | library | Observed | Groups 13 file(s) under scrapers package (observed from repository paths and static analysis). Observed top-level classes: BaseScraper, FetchResult, GDELTScraper, GitHubScraper, GoogleNewsScraper, HackerNewsScraper. Obs… |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 4 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: EmailManager, HorizonPipelineService, ILinkClient, ILinkError, PipelineContext, WeChatDeliv… |
| setup package | library | Observed | Groups 6 file(s) under setup package (observed from repository paths and static analysis). Observed top-level functions: _ai_recommendations_available, _count_sources, _gh_key, _matches_input_term, _merge_source_list, _… |
| Tests | test | Observed | Groups 67 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: FakeClient, FakeIMAP, FakeSMTP, FakeTools, LoginClient, OAuthServer. Observed top-level functions: _api_key… |
| url_security.py package | library | Observed | Groups 1 file(s) under url_security.py package (observed from repository paths and static analysis). Observed top-level classes: UnsafeURLError. Observed top-level functions: _resolve_hostname, safe_request, validate_ht… |

## Important files

- `.dockerignore` (container)
- `.env.example` (config)
- `.github/workflows/daily-summary.yml.disabled` (ci)
- `.github/workflows/deploy-docs.yml` (ci)
- `Dockerfile` (container)
- `data/config.example.json` (config)
- `data/config.github.json` (config)
- `data/presets.json` (config)
- `docker-compose.yml` (container)
- `docs/_config.yml` (config)
- `profiles/ai-creator/profile.json` (config)
- `profiles/finance-news/profile.json` (config)
- `profiles/tech-blog/profile.json` (config)
- `profiles/tech-news/profile.json` (config)
- `pyproject.toml` (manifest)
- `skills/horizon/evals/scenarios.json` (config)

## Top-level layout

- `src` — 76 analysed file(s)
- `tests` — 67 analysed file(s)
- `docs` — 19 analysed file(s)
- `profiles` — 16 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `skills` — 5 analysed file(s)
- `.github` — 4 analysed file(s)
- `data` — 3 analysed file(s)
- `scripts` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `ae30765a45ea97f082f6913181289ddd49566eeb` is the revision these paths and observations refer to.
