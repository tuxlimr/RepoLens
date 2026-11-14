# Project structure: JoeanAmier/TikTokDownloader

**Analysed commit:** `f766a6eff25b76fe4d737f10c27258e4da65df7d`

**Commit reference:** [f766a6eff25b76fe4d737f10c27258e4da65df7d](https://github.com/JoeanAmier/TikTokDownloader/commit/f766a6eff25b76fe4d737f10c27258e4da65df7d)

**Tree at this commit:** [JoeanAmier/TikTokDownloader@f766a6eff25b](https://github.com/JoeanAmier/TikTokDownloader/tree/f766a6eff25b76fe4d737f10c27258e4da65df7d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | JoeanAmier/TikTokDownloader |
| Description | 抖音 / TikTok 平台作品下载/数据采集工具 |
| Stars | 17492 |
| Forks | 2881 |
| Licence | GPL-3.0 |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `f766a6eff25b76fe4d737f10c27258e4da65df7d` |
| Retrieved at | 2026-11-14T19:11:27.830096+00:00 |
| Files in this snapshot | 157 |

## Directory tree

```text
.github/  (9 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.yml
    feature_request.yml
  workflows/  (6 files)
    Close_Stale_Issues_and_PRs.yaml
    Delete_untagged_images.yml
    Manually_build_executable_programs.yml
    Manually_docker_image.yml
    Release_build_executable_program.yml
    Release_docker_image.yml
  dependabot.yml
docs/  (3 files)
  Cookie获取教程.md
  DouK-Downloader文档.md
  Release_Notes.md
locale/  (6 files)
  en_US/  (1 files)
    LC_MESSAGES/  (1 files)
      … 1 files under this directory
  zh_CN/  (1 files)
    LC_MESSAGES/  (1 files)
      … 1 files under this directory
  README.md
  generate_path.py
  po_to_mo.py
  tk.pot
src/  (124 files)
  application/  (5 files)
    TikTokDownloader.py
    __init__.py
    main_monitor.py
    main_server.py
    main_terminal.py
  cli_edition/  (3 files)
    __init__.py
    main_cli.py
    write.py
  config/  (3 files)
    __init__.py
    parameter.py
    settings.py
  custom/  (4 files)
    __init__.py
    function.py
    internal.py
    static.py
  downloader/  (2 files)
    __init__.py
    download.py
  encrypt/  (15 files)
    __init__.py
    aBogus.py
    device_id.py
    douyin_params.py
    msToken.py
    params.py
    sm3.py
    tiktok_params.py
    tiktok_sign.py
    ttWid.py
    verifyFp.py
    webID.py
    websign.py
    xBogus.py
    xGnarly.py
  extract/  (2 files)
    __init__.py
    extractor.py
  gui_edition/  (1 files)
    __init__.py
  interface/  (21 files)
    __init__.py
    account.py
    account_tiktok.py
    collection.py
    collects.py
    comment.py
    comment_tiktok.py
    detail.py
    detail_tiktok.py
    hashtag.py
    hot.py
    info.py
    info_tiktok.py
    live.py
    live_tiktok.py
    mix.py
    mix_tiktok.py
    search.py
    slides.py
    template.py
    user.py
  link/  (3 files)
    __init__.py
    extractor.py
    requester.py
  manager/  (4 files)
    __init__.py
    cache.py
    database.py
    recorder.py
  models/  (12 files)
    __init__.py
    account.py
    base.py
    comment.py
    detail.py
    live.py
    mix.py
    reply.py
    response.py
    search.py
    settings.py
    share.py
  module/  (5 files)
    __init__.py
    cookie.py
    ffmpeg.py
    migrate_folder.py
    tiktok_unofficial.py
  record/  (3 files)
    __init__.py
    base.py
    logger.py
  storage/  (8 files)
    __init__.py
    csv.py
    manager.py
    mysql.py
    sql.py
    sqlite.py
    text.py
    xlsx.py
  testers/  (7 files)
    __init__.py
    logger.py
    params.py
    test_douyin_params.py
    test_format.py
    test_tiktok_params.py
    translate.py
  tools/  (20 files)
    __init__.py
    browser.py
    capture.py
    check_node.py
    choose.py
    cleaner.py
    console.py
    dynamic_import.py
    error.py
    file_folder.py
    format.py
    get_ua.py
    list_pop.py
    progress.py
    rename_compatible.py
    retry.py
    session.py
    temporary.py
    timer.py
    truncate.py
  translation/  (3 files)
    __init__.py
    static.py
    translate.py
  tui_edition/  (3 files)
    __init__.py
    app.py
    setting.py
static/  (4 files)
  js/  (4 files)
    X-Bogus.js
    a_bogus.js
    environment.js
    tiktok-web-params.js
.gitignore
.python-version
Dockerfile
README.md
README_EN.md
encipher_example.py
license
main.py
pyproject.toml
requirements.txt
setup.py
```

## Entry points

- [src/cli_edition/write.py:53](https://github.com/JoeanAmier/TikTokDownloader/blob/f766a6eff25b76fe4d737f10c27258e4da65df7d/src/cli_edition/write.py#L53)
- [src/custom/function.py:84](https://github.com/JoeanAmier/TikTokDownloader/blob/f766a6eff25b76fe4d737f10c27258e4da65df7d/src/custom/function.py#L84)
- [src/custom/internal.py:114](https://github.com/JoeanAmier/TikTokDownloader/blob/f766a6eff25b76fe4d737f10c27258e4da65df7d/src/custom/internal.py#L114)
- [src/encrypt/device_id.py:76](https://github.com/JoeanAmier/TikTokDownloader/blob/f766a6eff25b76fe4d737f10c27258e4da65df7d/src/encrypt/device_id.py#L76)
- [src/encrypt/msToken.py:260](https://github.com/JoeanAmier/TikTokDownloader/blob/f766a6eff25b76fe4d737f10c27258e4da65df7d/src/encrypt/msToken.py#L260)
- [src/encrypt/ttWid.py:111](https://github.com/JoeanAmier/TikTokDownloader/blob/f766a6eff25b76fe4d737f10c27258e4da65df7d/src/encrypt/ttWid.py#L111)
- [src/encrypt/verifyFp.py:64](https://github.com/JoeanAmier/TikTokDownloader/blob/f766a6eff25b76fe4d737f10c27258e4da65df7d/src/encrypt/verifyFp.py#L64)
- [src/encrypt/webID.py:53](https://github.com/JoeanAmier/TikTokDownloader/blob/f766a6eff25b76fe4d737f10c27258e4da65df7d/src/encrypt/webID.py#L53)
- [src/interface/account.py:282](https://github.com/JoeanAmier/TikTokDownloader/blob/f766a6eff25b76fe4d737f10c27258e4da65df7d/src/interface/account.py#L282)
- [src/interface/account_tiktok.py:151](https://github.com/JoeanAmier/TikTokDownloader/blob/f766a6eff25b76fe4d737f10c27258e4da65df7d/src/interface/account_tiktok.py#L151)
- [src/interface/collection.py:113](https://github.com/JoeanAmier/TikTokDownloader/blob/f766a6eff25b76fe4d737f10c27258e4da65df7d/src/interface/collection.py#L113)
- [src/interface/collects.py:327](https://github.com/JoeanAmier/TikTokDownloader/blob/f766a6eff25b76fe4d737f10c27258e4da65df7d/src/interface/collects.py#L327)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| application package | library | Observed | Groups 5 file(s) under application package (observed from repository paths and static analysis). Observed top-level classes: APIServer, ClipboardMonitor, PostMonitor, TikTok, TikTokDownloader. Observed top-level functio… |
| cli_edition package | library | Observed | Groups 2 file(s) under cli_edition package (observed from repository paths and static analysis). Observed top-level classes: Cli. Observed top-level functions: cli. |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: Parameter, Settings. |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). Observed top-level classes: DouYinParams, Params, TikTokParams. |
| custom package | library | Observed | Groups 2 file(s) under custom package (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 21 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: APIModel, Account, AccountTiktok, AccountUrl, BaseSQLLogger, BaseSearch. Observed top-level functions:… |
| downloader package | library | Observed | Groups 2 file(s) under downloader package (observed from repository paths and static analysis). Observed top-level classes: Downloader. |
| encrypt package | library | Observed | Groups 10 file(s) under encrypt package (observed from repository paths and static analysis). Observed top-level classes: ABogus, DigestChain, DouYinParams, Params, TikTokParams, XBogus. Observed top-level functions: _b… |
| Application entry point | entrypoint | Observed | Groups 39 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Account, AccountTikTok, App, Cleaner, Collection, Collects. Observed top-level functions:… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| extract package | library | Observed | Groups 2 file(s) under extract package (observed from repository paths and static analysis). Observed top-level classes: Extractor. |
| gui_edition package | library | Observed | Groups 1 file(s) under gui_edition package (observed from repository paths and static analysis). |
| interface package | library | Observed | Groups 2 file(s) under interface package (observed from repository paths and static analysis). Observed top-level classes: API, APITikTok. |
| link package | library | Observed | Groups 3 file(s) under link package (observed from repository paths and static analysis). Observed top-level classes: Extractor, ExtractorTikTok, Requester. |
| locale package | library | Observed | Groups 1 file(s) under locale package (observed from repository paths and static analysis). Observed top-level functions: find_python_files. |
| manager package | library | Observed | Groups 3 file(s) under manager package (observed from repository paths and static analysis). Observed top-level classes: Cache, DownloadRecorder, __DownloadRecorder. |
| module package | library | Observed | Groups 4 file(s) under module package (observed from repository paths and static analysis). Observed top-level classes: Cookie, FFMPEG, MigrateFolder. |
| record package | library | Observed | Groups 3 file(s) under record package (observed from repository paths and static analysis). Observed top-level classes: BaseLogger, LoggerManager. |
| static package | library | Observed | Groups 4 file(s) under static package (observed from repository paths and static analysis). |
| testers package | library | Observed | Groups 2 file(s) under testers package (observed from repository paths and static analysis). Observed top-level classes: Logger. |
| Tests | test | Observed | Groups 3 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: create_test_cookie_jar, test_cookie_dict_to_str, test_cookie_jar_to_dict, test_cookie_str_to_dict, test_co… |
| tools package | library | Observed | Groups 14 file(s) under tools package (observed from repository paths and static analysis). Observed top-level classes: Browser, CacheError, ColorfulConsole, DownloaderError, FakeProgress, RenameCompatible. Observed top… |
| translation package | library | Observed | Groups 3 file(s) under translation package (observed from repository paths and static analysis). Observed top-level classes: TranslationManager. Observed top-level functions: _translate, switch_language. |
| tui_edition package | library | Observed | Groups 2 file(s) under tui_edition package (observed from repository paths and static analysis). Observed top-level classes: Setting. |

## Important files

- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/Close_Stale_Issues_and_PRs.yaml` (ci)
- `.github/workflows/Delete_untagged_images.yml` (ci)
- `.github/workflows/Manually_build_executable_programs.yml` (ci)
- `.github/workflows/Manually_docker_image.yml` (ci)
- `.github/workflows/Release_build_executable_program.yml` (ci)
- `.github/workflows/Release_docker_image.yml` (ci)
- `Dockerfile` (container)
- `pyproject.toml` (manifest)
- `requirements.txt` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `src` — 124 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `.github` — 9 analysed file(s)
- `locale` — 6 analysed file(s)
- `static` — 4 analysed file(s)
- `docs` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `f766a6eff25b76fe4d737f10c27258e4da65df7d` is the revision these paths and observations refer to.
