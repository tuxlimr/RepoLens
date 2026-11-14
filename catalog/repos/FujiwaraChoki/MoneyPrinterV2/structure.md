# Project structure: FujiwaraChoki/MoneyPrinterV2

**Analysed commit:** `a734fa924adb9ffe5ab8472aa5526e469e42a8b5`

**Commit reference:** [a734fa924adb9ffe5ab8472aa5526e469e42a8b5](https://github.com/FujiwaraChoki/MoneyPrinterV2/commit/a734fa924adb9ffe5ab8472aa5526e469e42a8b5)

**Tree at this commit:** [FujiwaraChoki/MoneyPrinterV2@a734fa924adb](https://github.com/FujiwaraChoki/MoneyPrinterV2/tree/a734fa924adb9ffe5ab8472aa5526e469e42a8b5)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | FujiwaraChoki/MoneyPrinterV2 |
| Description | Automate the process of making money online. |
| Stars | 32426 |
| Forks | 3474 |
| Licence | AGPL-3.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `a734fa924adb9ffe5ab8472aa5526e469e42a8b5` |
| Retrieved at | 2026-11-14T19:07:03.224443+00:00 |
| Files in this snapshot | 42 |

## Directory tree

```text
.github/  (1 files)
  FUNDING.yml
assets/  (1 files)
  banner.txt
docs/  (6 files)
  AffiliateMarketing.md
  Configuration.md
  PostBridge.md
  Roadmap.md
  TwitterBot.md
  YouTube.md
scripts/  (3 files)
  preflight_local.py
  setup_local.sh
  upload_video.sh
src/  (16 files)
  classes/  (6 files)
    AFM.py
    Outreach.py
    PostBridge.py
    Tts.py
    Twitter.py
    YouTube.py
  art.py
  cache.py
  config.py
  constants.py
  cron.py
  llm_provider.py
  main.py
  post_bridge_integration.py
  status.py
  utils.py
tests/  (5 files)
  test_config.py
  test_cron_post_bridge.py
  test_post_bridge_client.py
  test_post_bridge_integration.py
  test_youtube_custom_topic.py
.gitignore
.python-version
AGENTS.md
CLAUDE.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
config.example.json
requirements.txt
```

## Entry points

- [src/cron.py:99](https://github.com/FujiwaraChoki/MoneyPrinterV2/blob/a734fa924adb9ffe5ab8472aa5526e469e42a8b5/src/cron.py#L99)
- [src/main.py:462](https://github.com/FujiwaraChoki/MoneyPrinterV2/blob/a734fa924adb9ffe5ab8472aa5526e469e42a8b5/src/main.py#L462)
- [scripts/preflight_local.py:123](https://github.com/FujiwaraChoki/MoneyPrinterV2/blob/a734fa924adb9ffe5ab8472aa5526e469e42a8b5/scripts/preflight_local.py#L123)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| art.py package | library | Observed | Groups 1 file(s) under art.py package (observed from repository paths and static analysis). Observed top-level functions: print_banner. |
| cache.py package | library | Observed | Groups 1 file(s) under cache.py package (observed from repository paths and static analysis). Observed top-level functions: add_account, add_product, get_accounts, get_afm_cache_path, get_cache_path, get_products. |
| classes package | library | Observed | Groups 6 file(s) under classes package (observed from repository paths and static analysis). Observed top-level classes: AffiliateMarketing, Outreach, PostBridge, PostBridgeClientError, TTS, Twitter. |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: assert_folder_structure, equalize_subtitles, get_assemblyai_api_key, get_email_cred… |
| constants.py package | library | Observed | Groups 1 file(s) under constants.py package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 3 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: check_url, fail, generate_and_upload_short, main, ok, warn. |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| llm_provider.py package | library | Observed | Groups 1 file(s) under llm_provider.py package (observed from repository paths and static analysis). Observed top-level functions: _client, generate_text, get_active_model, list_models, select_model. |
| post_bridge_integration.py package | library | Observed | Groups 1 file(s) under post_bridge_integration.py package (observed from repository paths and static analysis). Observed top-level functions: build_platform_configurations, maybe_crosspost_youtube_short, resolve_social_… |
| scripts package | library | Observed | Groups 2 file(s) under scripts package (observed from repository paths and static analysis). |
| status.py package | library | Observed | Groups 1 file(s) under status.py package (observed from repository paths and static analysis). Observed top-level functions: error, info, question, success, warning. |
| Tests | test | Observed | Groups 5 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH cron.maybe_crosspost_youtube_short, PATCH cron.YouTube, PATCH cron.TTS, PATCH cron.get_accounts, PATCH cron.selec… |
| utils.py package | library | Observed | Groups 1 file(s) under utils.py package (observed from repository paths and static analysis). Observed top-level functions: build_url, choose_random_song, close_running_selenium_instances, fetch_songs, rem_temp_files. |

## Important files

- `.github/FUNDING.yml` (config)
- `config.example.json` (config)
- `requirements.txt` (manifest)

## Top-level layout

- `src` — 16 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `docs` — 6 analysed file(s)
- `tests` — 5 analysed file(s)
- `scripts` — 3 analysed file(s)
- `.github` — 1 analysed file(s)
- `assets` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `a734fa924adb9ffe5ab8472aa5526e469e42a8b5` is the revision these paths and observations refer to.
