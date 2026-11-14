# Project structure: Evil0ctal/Douyin_TikTok_Download_API

**Analysed commit:** `3c045e11aecd58ab076562f1246931b9dd5d909b`

**Commit reference:** [3c045e11aecd58ab076562f1246931b9dd5d909b](https://github.com/Evil0ctal/Douyin_TikTok_Download_API/commit/3c045e11aecd58ab076562f1246931b9dd5d909b)

**Tree at this commit:** [Evil0ctal/Douyin_TikTok_Download_API@3c045e11aecd](https://github.com/Evil0ctal/Douyin_TikTok_Download_API/tree/3c045e11aecd58ab076562f1246931b9dd5d909b)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Evil0ctal/Douyin_TikTok_Download_API |
| Description | 🚀 自托管的抖音、TikTok、B 站数据采集与无水印视频下载 API，支持 AI agent 通过 MCP 调用与离线语音转文字，Docker 一键部署。| Self-hosted TikTok, Douyin & Bilibili scraper and no-watermark video downloader — async REST API, MCP server for AI agents, CLI and web console, plus offline speech-to-text for downloaded videos. Self-healing identity p… |
| Stars | 21402 |
| Forks | 2968 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `3c045e11aecd58ab076562f1246931b9dd5d909b` |
| Retrieved at | 2026-11-14T19:07:58.608312+00:00 |
| Files in this snapshot | 584 |

## Directory tree

```text
.github/  (35 files)
  ISSUE_TEMPLATE/  (9 files)
    1-bug-en.yml
    1-bug-zh.yml
    2-endpoint-en.yml
    2-endpoint-zh.yml
    3-feature-en.yml
    3-feature-zh.yml
    4-docs-en.yml
    4-docs-zh.yml
    config.yml
  PULL_REQUEST_TEMPLATE/  (2 files)
    en.md
    zh.md
  workflows/  (3 files)
    ci.yml
    codeql.yml
    docker-publish.yml
  CODEOWNERS
  FUNDING.yml
  RELEASE_TEMPLATE.md
  RELEASE_v5.0.0.md
  RELEASE_v5.0.1.md
  RELEASE_v5.0.2.md
  RELEASE_v5.0.3.md
  RELEASE_v5.1.0.md
  RELEASE_v5.1.1.md
  RELEASE_v5.1.10.md
  RELEASE_v5.1.11.md
  RELEASE_v5.1.2.md
  RELEASE_v5.1.3.md
  RELEASE_v5.1.4.md
  RELEASE_v5.1.5.md
  RELEASE_v5.1.6.md
  RELEASE_v5.1.7.md
  RELEASE_v5.1.8.md
  RELEASE_v5.1.9.md
  dependabot.yml
  pull_request_template.md
docker/  (47 files)
  browser_rpc/  (21 files)
    backends/  (4 files)
      … 4 files under this directory
    tests/  (7 files)
      … 7 files under this directory
    __init__.py
    __main__.py
    errors.py
    geo.py
    main.py
    models.py
    requirements.txt
    service.py
    settings.py
    validation.py
  downloader/  (14 files)
    api.go
    api_test.go
    download.go
    download_test.go
    go.mod
    main.go
    progress.go
    progress_test.go
    queue.go
    resume_test.go
    safety.go
    safety_test.go
    store.go
    store_test.go
  transcriber/  (2 files)
    app.py
    requirements.txt
  Dockerfile
  Dockerfile.browser
  Dockerfile.downloader
  Dockerfile.transcriber
  README.md
  browser-entrypoint.sh
  compose.test.yml
  compose.yml
  entrypoint.sh
  package-mirrors.sh
documents/  (38 files)
  en/  (18 files)
    01-quickstart.md
    02-installation.md
    03-configuration.md
    04-concepts.md
    05-console-overview.md
    06-identities-and-proxies.md
    07-playground-and-tools.md
    08-downloads-and-library.md
    09-users-and-api-keys.md
    10-operations.md
    11-api.md
    12-mcp.md
    13-cli.md
    14-troubleshooting.md
    15-security.md
    16-contributing.md
    17-faq.md
    18-funasr-models.md
  zh/  (18 files)
    01-quickstart.md
    02-installation.md
    03-configuration.md
    04-concepts.md
    05-console-overview.md
    06-identities-and-proxies.md
    07-playground-and-tools.md
    08-downloads-and-library.md
    09-users-and-api-keys.md
    10-operations.md
    11-api.md
    12-mcp.md
    13-cli.md
    14-troubleshooting.md
    15-security.md
    16-contributing.md
    17-faq.md
    18-funasr-models.md
  README.md
  README.zh-CN.md
install/  (3 files)
  README.md
  install.sh
  install.zh.sh
logo/  (2 files)
  logo.svg
  logo.txt
screenshots/  (1 files)
  README.md
scripts/  (1 files)
  smoke.sh
src/  (230 files)
  dtk/  (230 files)
    api/  (42 files)
      … 42 files under this directory
    cli/  (12 files)
      … 12 files under this directory
    core/  (8 files)
      … 8 files under this directory
    db/  (24 files)
      … 24 files under this directory
    i18n/  (12 files)
      … 12 files under this directory
    identity/  (8 files)
      … 8 files under this directory
    mcp/  (9 files)
      … 9 files under this directory
    media/  (4 files)
      … 4 files under this directory
    models/  (2 files)
      … 2 files under this directory
    ops/  (14 files)
      … 14 files under this directory
    platforms/  (21 files)
      … 21 files under this directory
    scheduler/  (6 files)
      … 6 files under this directory
    services/  (15 files)
      … 15 files under this directory
    signing/  (16 files)
      … 16 files under this directory
    transport/  (6 files)
      … 6 files under this directory
    urls/  (5 files)
      … 5 files under this directory
    worker/  (24 files)
      … 24 files under this directory
    __init__.py
    transcriber.py
tests/  (209 files)
  contract/  (4 files)
    README.md
    __init__.py
    subjects.py
    test_live_endpoints.py
  fixtures/  (94 files)
    bilibili/  (35 files)
      … 35 files under this directory
    douyin/  (28 files)
      … 28 files under this directory
    signing/  (1 files)
      … 1 files under this directory
    tiktok/  (29 files)
      … 29 files under this directory
    README.md
  integration/  (39 files)
    __init__.py
    conftest.py
    test_api_admin.py
    test_api_auth.py
    test_api_backup.py
    test_api_capabilities.py
    test_api_collections.py
    test_api_content.py
    test_api_content_links.py
    test_api_cors_and_limits.py
    test_api_credential_roles.py
    test_api_demo.py
    test_api_discovery.py
    test_api_downloads.py
    test_api_identities_listing.py
    test_api_identities_paging.py
    test_api_identity_cookies.py
    test_api_identity_notes.py
    test_api_identity_pin.py
    test_api_identity_rotation.py
    test_api_logs.py
    test_api_setup.py
    test_api_support.py
    test_api_system.py
    … 15 more files
  replay/  (7 files)
    __init__.py
    support.py
    test_bilibili_parser.py
    test_discovery_parsers.py
    test_douyin_parser.py
    test_platform_contract.py
    test_tiktok_parser.py
  support/  (3 files)
    __init__.py
    marks.py
    shell_code.py
  unit/  (60 files)
    __init__.py
    test_absence_matrix.py
    test_admin_account_rules.py
    test_api_middleware.py
    test_archive.py
    test_bilibili.py
    test_bilibili_redaction.py
    test_capabilities_route.py
    test_capacity.py
    test_classify_status_keys.py
    test_cli.py
    test_client_profile.py
    test_console_api_seam.py
    test_console_notify_triggers.py
    test_console_reason_codes.py
    test_console_shell.py
    test_content_ids.py
    test_db_models.py
    test_db_pool.py
    test_demo.py
    test_discovery_absence.py
    test_discovery_params.py
    test_download_progress.py
    test_download_requests.py
    … 36 more files
  __init__.py
  conftest.py
web/  (3 files)
  src/  (2 files)
    components/  (1 files)
      … 1 files under this directory
    styles/  (1 files)
      … 1 files under this directory
  .gitignore
.dockerignore
.env.example
.gitattributes
.gitignore
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
Makefile
NOTICE
README.md
README.zh-CN.md
SECURITY.md
alembic.ini
llms.txt
pyproject.toml
```

## Entry points

- [src/dtk/api/app.py:147](https://github.com/Evil0ctal/Douyin_TikTok_Download_API/blob/3c045e11aecd58ab076562f1246931b9dd5d909b/src/dtk/api/app.py#L147)
- [src/dtk/cli/backup.py:36](https://github.com/Evil0ctal/Douyin_TikTok_Download_API/blob/3c045e11aecd58ab076562f1246931b9dd5d909b/src/dtk/cli/backup.py#L36)
- [src/dtk/cli/identities.py:33](https://github.com/Evil0ctal/Douyin_TikTok_Download_API/blob/3c045e11aecd58ab076562f1246931b9dd5d909b/src/dtk/cli/identities.py#L33)
- [src/dtk/cli/main.py](https://github.com/Evil0ctal/Douyin_TikTok_Download_API/blob/3c045e11aecd58ab076562f1246931b9dd5d909b/src/dtk/cli/main.py)
- [src/dtk/cli/proxies.py:33](https://github.com/Evil0ctal/Douyin_TikTok_Download_API/blob/3c045e11aecd58ab076562f1246931b9dd5d909b/src/dtk/cli/proxies.py#L33)
- [src/dtk/cli/settings_cmd.py:27](https://github.com/Evil0ctal/Douyin_TikTok_Download_API/blob/3c045e11aecd58ab076562f1246931b9dd5d909b/src/dtk/cli/settings_cmd.py#L27)
- [src/dtk/cli/users.py:37](https://github.com/Evil0ctal/Douyin_TikTok_Download_API/blob/3c045e11aecd58ab076562f1246931b9dd5d909b/src/dtk/cli/users.py#L37)
- [src/dtk/mcp/__main__.py:12](https://github.com/Evil0ctal/Douyin_TikTok_Download_API/blob/3c045e11aecd58ab076562f1246931b9dd5d909b/src/dtk/mcp/__main__.py#L12)
- [src/dtk/worker/__main__.py:9](https://github.com/Evil0ctal/Douyin_TikTok_Download_API/blob/3c045e11aecd58ab076562f1246931b9dd5d909b/src/dtk/worker/__main__.py#L9)
- [docker/browser_rpc/__main__.py:45](https://github.com/Evil0ctal/Douyin_TikTok_Download_API/blob/3c045e11aecd58ab076562f1246931b9dd5d909b/docker/browser_rpc/__main__.py#L45)
- [docker/browser_rpc/main.py:72](https://github.com/Evil0ctal/Douyin_TikTok_Download_API/blob/3c045e11aecd58ab076562f1246931b9dd5d909b/docker/browser_rpc/main.py#L72)
- [docker/transcriber/app.py:537](https://github.com/Evil0ctal/Douyin_TikTok_Download_API/blob/3c045e11aecd58ab076562f1246931b9dd5d909b/docker/transcriber/app.py#L537)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 39 file(s) under api layer (observed from repository paths and static analysis). Observed routes: GET /endpoints/access, GET (path not a literal), POST (path not a literal), PATCH /{key_id}, DELETE /{key_id}. Obs… |
| Configuration and deployment | config | Observed | Groups 21 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed routes: GET /status, POST /init. Observed top-level classes: BootstrapSettings, Config, Scope, SettingS… |
| Data layer | data | Observed | Groups 27 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AlbumImage, ApiKey, ApiKeyRepository, ArchivedAuthor, ArchivedContent, AuditLog. Observed top-level fu… |
| docker package | library | Observed | Groups 24 file(s) under docker package (observed from repository paths and static analysis). Observed top-level classes: BackendFailure, BackendInfo, BackendUnavailable, BrowserBackend, CloakBackend, CloakSigningContext… |
| dtk package | library | Observed | Groups 118 file(s) under dtk package (observed from repository paths and static analysis). Observed top-level classes: ABogus, ABogusComparator, Alerter, ApiKeyGuard, BackupError, BackupInfo. Observed top-level function… |
| Application entry point | entrypoint | Observed | Groups 14 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI, Typer. Observed top-level classes: Backend, DatabaseTaskStore, FunAS… |
| External integrations | external | Observed | Groups 2 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: BrowserRpcClient, BrowserRpcUnavailable, DownloaderBusy, DownloaderClient, DownloaderHealth,… |
| install package | library | Observed | Groups 2 file(s) under install package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 22 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: AlreadyInFlight, ArchiveFilter, Availability, BrowserFamily, BrowserRpcService, Cipher. Ob… |
| Tests | test | Observed | Groups 219 file(s) under tests (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed top-level classes: AdvancingClock, BothReadFirst, BrokenContext, Clock, Conc… |

## Important files

- `.dockerignore` (container)
- `.env.example` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/1-bug-en.yml` (config)
- `.github/ISSUE_TEMPLATE/1-bug-zh.yml` (config)
- `.github/ISSUE_TEMPLATE/2-endpoint-en.yml` (config)
- `.github/ISSUE_TEMPLATE/2-endpoint-zh.yml` (config)
- `.github/ISSUE_TEMPLATE/3-feature-en.yml` (config)
- `.github/ISSUE_TEMPLATE/3-feature-zh.yml` (config)
- `.github/ISSUE_TEMPLATE/4-docs-en.yml` (config)
- `.github/ISSUE_TEMPLATE/4-docs-zh.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/codeql.yml` (ci)
- `.github/workflows/docker-publish.yml` (ci)
- `alembic.ini` (config)
- `docker/Dockerfile` (container)
- `docker/Dockerfile.browser` (container)
- `docker/Dockerfile.downloader` (container)
- `docker/Dockerfile.transcriber` (container)
- `docker/browser_rpc/requirements.txt` (manifest)
- `docker/compose.test.yml` (config)
- `docker/compose.yml` (container)
- `docker/downloader/go.mod` (manifest)
- `docker/transcriber/requirements.txt` (manifest)
- `pyproject.toml` (manifest)
- `src/dtk/api/routes/data/ios_shortcut.json` (config)
- `src/dtk/api/routes/setup.py` (manifest)
- `src/dtk/i18n/locales/en.json` (config)
- `src/dtk/i18n/locales/errors.en.json` (config)
- `src/dtk/i18n/locales/errors.zh.json` (config)
- `src/dtk/i18n/locales/format.en.json` (config)
- `src/dtk/i18n/locales/format.zh.json` (config)
- `src/dtk/i18n/locales/zh.json` (config)

## Top-level layout

- `src` — 230 analysed file(s)
- `tests` — 209 analysed file(s)
- `docker` — 47 analysed file(s)
- `documents` — 38 analysed file(s)
- `.github` — 35 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `install` — 3 analysed file(s)
- `web` — 3 analysed file(s)
- `logo` — 2 analysed file(s)
- `screenshots` — 1 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `3c045e11aecd58ab076562f1246931b9dd5d909b` is the revision these paths and observations refer to.
