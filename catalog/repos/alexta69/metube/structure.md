# Project structure: alexta69/metube

**Analysed commit:** `7594d26dc418ec0e24985d562e4f24e737e7c0fe`

**Commit reference:** [7594d26dc418ec0e24985d562e4f24e737e7c0fe](https://github.com/alexta69/metube/commit/7594d26dc418ec0e24985d562e4f24e737e7c0fe)

**Tree at this commit:** [alexta69/metube@7594d26dc418](https://github.com/alexta69/metube/tree/7594d26dc418ec0e24985d562e4f24e737e7c0fe)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | alexta69/metube |
| Description | Self-hosted video downloader for YouTube and other sites (web UI for yt-dlp) |
| Stars | 15263 |
| Forks | 1139 |
| Licence | AGPL-3.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `7594d26dc418ec0e24985d562e4f24e737e7c0fe` |
| Retrieved at | 2026-11-14T19:09:05.393169+00:00 |
| Files in this snapshot | 120 |

## Directory tree

```text
.github/  (10 files)
  DISCUSSION_TEMPLATE/  (3 files)
    general.yml
    ideas.yml
    q-a.yml
  ISSUE_TEMPLATE/  (3 files)
    bug_report.yml
    config.yml
    feature_request.yml
  workflows/  (3 files)
    main.yml
    readme-size.yml
    update-yt-dlp.yml
  dependabot.yml
.vscode/  (1 files)
  launch.json
app/  (26 files)
  tests/  (16 files)
    conftest.py
    test_api.py
    test_bg_tasks.py
    test_config.py
    test_dl_formats.py
    test_download_options.py
    test_download_queue.py
    test_format_catalog.py
    test_main_helpers.py
    test_music_metadata.py
    test_nightly_update.py
    test_persistent_queue.py
    test_state_store.py
    test_subscriptions.py
    test_url_guard.py
    test_ytdl_utils.py
  bg_tasks.py
  dl_formats.py
  download_options.py
  format_catalog.py
  main.py
  music_metadata.py
  state_store.py
  subscriptions.py
  url_guard.py
  ytdl.py
ui/  (72 files)
  src/  (63 files)
    app/  (55 files)
      … 55 files under this directory
    assets/  (3 files)
      … 3 files under this directory
    custom-service-worker.js
    index.html
    main.ts
    manifest.webmanifest
    styles.sass
  .editorconfig
  angular.json
  eslint.config.js
  ngsw-config.json
  package.json
  pnpm-workspace.yaml
  tsconfig.app.json
  tsconfig.json
  tsconfig.spec.json
.dockerignore
.editorconfig
.gitignore
AGENTS.md
CONTRIBUTING.md
Dockerfile
LICENSE
README.md
SECURITY.md
docker-entrypoint.sh
pyproject.toml
```

## Entry points

- [app/main.py:1603](https://github.com/alexta69/metube/blob/7594d26dc418ec0e24985d562e4f24e737e7c0fe/app/main.py#L1603)
- [ui/src/app/app.ts](https://github.com/alexta69/metube/blob/7594d26dc418ec0e24985d562e4f24e737e7c0fe/ui/src/app/app.ts)
- [ui/src/main.ts](https://github.com/alexta69/metube/blob/7594d26dc418ec0e24985d562e4f24e737e7c0fe/ui/src/main.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| app package | library | Observed | Groups 9 file(s) under app package (observed from repository paths and static analysis). Observed top-level classes: AtomicJsonStore, Download, DownloadInfo, DownloadOptions, DownloadQueue, DownloadQueueNotifier. Observ… |
| Configuration and deployment | config | Observed | Groups 10 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed routes: POST (path not a literal), GET (path not a literal), POST (path not a literal), GET (path not a liter… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 11 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 16 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: AddressResolutionTests, AlbumArtistPostProcessorTests, AlbumArtistRegistrationTests, AllowPrivateBypassTest… |
| ui package | library | Observed | Groups 38 file(s) under ui package (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.editorconfig` (config)
- `.github/DISCUSSION_TEMPLATE/general.yml` (config)
- `.github/DISCUSSION_TEMPLATE/ideas.yml` (config)
- `.github/DISCUSSION_TEMPLATE/q-a.yml` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/main.yml` (ci)
- `.github/workflows/readme-size.yml` (ci)
- `.github/workflows/update-yt-dlp.yml` (ci)
- `.vscode/launch.json` (config)
- `Dockerfile` (container)
- `pyproject.toml` (manifest)
- `ui/.editorconfig` (config)
- `ui/angular.json` (config)
- `ui/ngsw-config.json` (config)
- `ui/package.json` (manifest)
- `ui/pnpm-workspace.yaml` (config)
- `ui/tsconfig.app.json` (config)
- `ui/tsconfig.json` (config)
- `ui/tsconfig.spec.json` (config)

## Top-level layout

- `ui` — 72 analysed file(s)
- `app` — 26 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `.github` — 10 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x file exceeds per-file size limit (200000 bytes)).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `7594d26dc418ec0e24985d562e4f24e737e7c0fe` is the revision these paths and observations refer to.
