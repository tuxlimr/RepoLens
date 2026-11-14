# Project structure: jiji262/douyin-downloader

**Analysed commit:** `7c4b8b2252acbfe24728664cc77364bb75a24ecb`

**Commit reference:** [7c4b8b2252acbfe24728664cc77364bb75a24ecb](https://github.com/jiji262/douyin-downloader/commit/7c4b8b2252acbfe24728664cc77364bb75a24ecb)

**Tree at this commit:** [jiji262/douyin-downloader@7c4b8b2252ac](https://github.com/jiji262/douyin-downloader/tree/7c4b8b2252acbfe24728664cc77364bb75a24ecb)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | jiji262/douyin-downloader |
| Description | A practical Douyin downloader for both single-item and profile batch downloads, with progress display, retries, SQLite deduplication, and browser fallback support. 抖音批量下载工具，去水印，支持视频、图集、合集、音乐(原声)。 |
| Stars | 12611 |
| Forks | 1925 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `7c4b8b2252acbfe24728664cc77364bb75a24ecb` |
| Retrieved at | 2026-11-14T19:10:03.549963+00:00 |
| Files in this snapshot | 172 |

## Directory tree

```text
auth/  (5 files)
  AGENTS.md
  __init__.py
  cookie_manager.py
  ms_token_conf.py
  ms_token_manager.py
cli/  (6 files)
  AGENTS.md
  __init__.py
  login_flow.py
  main.py
  progress_display.py
  whisper_transcribe.py
config/  (4 files)
  AGENTS.md
  __init__.py
  config_loader.py
  default_config.py
control/  (5 files)
  AGENTS.md
  __init__.py
  queue_manager.py
  rate_limiter.py
  retry_handler.py
core/  (34 files)
  user_modes/  (11 files)
    AGENTS.md
    __init__.py
    base_strategy.py
    collect_mix_strategy.py
    collect_strategy.py
    like_strategy.py
    mix_routing.py
    mix_strategy.py
    music_strategy.py
    post_strategy.py
    post_time_boundary.py
  AGENTS.md
  __init__.py
  api_client.py
  audio_extraction.py
  comments_collector.py
  discovery.py
  downloader_base.py
  downloader_factory.py
  ffmpeg.py
  item_reasons.py
  live_downloader.py
  live_replay_downloader.py
  metadata.py
  mix_downloader.py
  music_downloader.py
  output_naming.py
  retry_executor.py
  silent_audio.py
  transcript_manager.py
  url_parser.py
  user_downloader.py
  user_mode_registry.py
  video_downloader.py
docs/  (6 files)
  superpowers/  (6 files)
    plans/  (3 files)
      … 3 files under this directory
    specs/  (3 files)
      … 3 files under this directory
server/  (3 files)
  __init__.py
  app.py
  jobs.py
storage/  (5 files)
  AGENTS.md
  __init__.py
  database.py
  file_manager.py
  metadata_handler.py
tests/  (75 files)
  fixtures/  (1 files)
    proxy_samples.json
  AGENTS.md
  test_api_client.py
  test_api_client_login_required.py
  test_api_client_risk_control.py
  test_audio_extraction.py
  test_cli_main.py
  test_comments_collector.py
  test_comments_download_behavior.py
  test_config_loader.py
  test_config_loader_save.py
  test_config_validation.py
  test_cookie_fetcher.py
  test_cookie_fetcher_fetch.py
  test_cookie_manager.py
  test_cookie_utils.py
  test_database.py
  test_database_history.py
  test_database_migration.py
  test_database_top_authors.py
  test_discovery.py
  test_download_progress_and_deadline.py
  test_download_proxy_passthrough.py
  test_download_slow_node_guard.py
  test_downloader_author_sec_uid.py
  … 50 more files
tools/  (3 files)
  AGENTS.md
  __init__.py
  cookie_fetcher.py
utils/  (12 files)
  AGENTS.md
  __init__.py
  abogus.py
  cookie_utils.py
  helpers.py
  logger.py
  naming.py
  naming_limits.py
  notifier.py
  paid_content.py
  validators.py
  xbogus.py
.dockerignore
.gitignore
AGENTS.md
CLAUDE.md
Dockerfile
LICENSE
PROJECT_SUMMARY.md
README.md
README.zh-CN.md
__init__.py
config.example.yml
pyproject.toml
requirements.txt
run.py
```

## Entry points

- [cli/main.py](https://github.com/jiji262/douyin-downloader/blob/7c4b8b2252acbfe24728664cc77364bb75a24ecb/cli/main.py)
- [cli/whisper_transcribe.py:532](https://github.com/jiji262/douyin-downloader/blob/7c4b8b2252acbfe24728664cc77364bb75a24ecb/cli/whisper_transcribe.py#L532)
- [run.py:10](https://github.com/jiji262/douyin-downloader/blob/7c4b8b2252acbfe24728664cc77364bb75a24ecb/run.py#L10)
- [server/app.py:152](https://github.com/jiji262/douyin-downloader/blob/7c4b8b2252acbfe24728664cc77364bb75a24ecb/server/app.py#L152)
- [tools/cookie_fetcher.py:389](https://github.com/jiji262/douyin-downloader/blob/7c4b8b2252acbfe24728664cc77364bb75a24ecb/tools/cookie_fetcher.py#L389)
- [utils/abogus.py:832](https://github.com/jiji262/douyin-downloader/blob/7c4b8b2252acbfe24728664cc77364bb75a24ecb/utils/abogus.py#L832)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| auth package | library | Observed | Groups 4 file(s) under auth package (observed from repository paths and static analysis). Observed top-level classes: CookieManager, MsTokenManager. |
| cli package | library | Observed | Groups 3 file(s) under cli package (observed from repository paths and static analysis). Observed top-level classes: ProgressDisplay. Observed top-level functions: can_interactive_login, interactive_relogin. |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: ConfigLoader. |
| control package | library | Observed | Groups 4 file(s) under control package (observed from repository paths and static analysis). Observed top-level classes: QueueManager, RateLimiter, RetryHandler. Observed top-level functions: _clamp_workers. |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 4 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: Database, FileManager, MetadataHandler, SlowDownloadError, _ThroughputGuard. Observed top-level functio… |
| Application entry point | entrypoint | Observed | Groups 6 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed top-level classes: ABogus, BrowserFingerprintGenerator, Cryp… |
| External integrations | external | Observed | Groups 1 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: DouyinAPIClient, FailedPayload, LoginRequiredError. Observed top-level functions: _consume_t… |
| server package | library | Observed | Groups 2 file(s) under server package (observed from repository paths and static analysis). Observed top-level classes: DownloadJob, JobManager, JobStatus. Observed top-level functions: _now_iso. |
| Service / domain layer | service | Observed | Groups 31 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: AudioExtractEmpty, AudioExtractError, BaseDownloader, BaseUserModeStrategy, CollectMixUser… |
| Tests | test | Observed | Groups 75 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: FakePage, RoutingAPI, SlowPage, TestOriginalPromotion, TestPickHighestQualityPlayAddr, TestPickPlayAddrByQu… |
| tools package | library | Observed | Groups 1 file(s) under tools package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 10 file(s) under utils package (observed from repository paths and static analysis). Observed top-level classes: BarkProvider, Notifier, PathLimits, TelegramProvider, TemplateValidationError, WebhookProvider. Obs… |

## Important files

- `.dockerignore` (container)
- `Dockerfile` (container)
- `config.example.yml` (config)
- `pyproject.toml` (manifest)
- `requirements.txt` (manifest)

## Top-level layout

- `tests` — 75 analysed file(s)
- `core` — 34 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `utils` — 12 analysed file(s)
- `cli` — 6 analysed file(s)
- `docs` — 6 analysed file(s)
- `auth` — 5 analysed file(s)
- `control` — 5 analysed file(s)
- `storage` — 5 analysed file(s)
- `config` — 4 analysed file(s)
- `server` — 3 analysed file(s)
- `tools` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `7c4b8b2252acbfe24728664cc77364bb75a24ecb` is the revision these paths and observations refer to.
