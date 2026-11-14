# Project structure: JoeanAmier/XHS-Downloader

**Analysed commit:** `dfad51b3d1aac55866802007544f9390ad21553f`

**Commit reference:** [dfad51b3d1aac55866802007544f9390ad21553f](https://github.com/JoeanAmier/XHS-Downloader/commit/dfad51b3d1aac55866802007544f9390ad21553f)

**Tree at this commit:** [JoeanAmier/XHS-Downloader@dfad51b3d1aa](https://github.com/JoeanAmier/XHS-Downloader/tree/dfad51b3d1aac55866802007544f9390ad21553f)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | JoeanAmier/XHS-Downloader |
| Description | 小红书（XiaoHongShu、RedNote）链接提取/作品采集工具 |
| Stars | 13295 |
| Forks | 1941 |
| Licence | GPL-3.0 |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `dfad51b3d1aac55866802007544f9390ad21553f` |
| Retrieved at | 2026-11-14T19:11:58.270824+00:00 |
| Files in this snapshot | 80 |

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
  xhs.pot
source/  (47 files)
  CLI/  (2 files)
    __init__.py
    main.py
  GUI/  (4 files)
    __init__.py
    backend.py
    launcher.py
    ui_strings.py
  TUI/  (10 files)
    __init__.py
    about.py
    app.py
    index.py
    loading.py
    monitor.py
    progress.py
    record.py
    setting.py
    update.py
  application/  (8 files)
    __init__.py
    app.py
    download.py
    explore.py
    image.py
    request.py
    user_posted.py
    video.py
  expansion/  (8 files)
    __init__.py
    browser.py
    cleaner.py
    converter.py
    error.py
    file_folder.py
    namespace.py
    truncate.py
  module/  (12 files)
    __init__.py
    auth.py
    extend.py
    manager.py
    mapping.py
    model.py
    note_info.py
    recorder.py
    script.py
    settings.py
    static.py
    tools.py
  translation/  (2 files)
    __init__.py
    translate.py
  __init__.py
static/  (7 files)
  GUI/  (3 files)
    app.js
    index.html
    styles.css
  other/  (1 files)
    自动滚动页面.js
  Release_Notes.md
  XHS-Downloader.js
  XHS-Downloader.tcss
.gitignore
.python-version
Dockerfile
LICENSE
README.md
README_EN.md
example.py
main.py
pyproject.toml
requirements.txt
setup.py
```

## Entry points

- [example.py:118](https://github.com/JoeanAmier/XHS-Downloader/blob/dfad51b3d1aac55866802007544f9390ad21553f/example.py#L118)
- [locale/po_to_mo.py:23](https://github.com/JoeanAmier/XHS-Downloader/blob/dfad51b3d1aac55866802007544f9390ad21553f/locale/po_to_mo.py#L23)
- [main.py:45](https://github.com/JoeanAmier/XHS-Downloader/blob/dfad51b3d1aac55866802007544f9390ad21553f/main.py#L45)
- [source/CLI/main.py:410](https://github.com/JoeanAmier/XHS-Downloader/blob/dfad51b3d1aac55866802007544f9390ad21553f/source/CLI/main.py#L410)
- [source/GUI/launcher.py:72](https://github.com/JoeanAmier/XHS-Downloader/blob/dfad51b3d1aac55866802007544f9390ad21553f/source/GUI/launcher.py#L72)
- [source/application/app.py:792](https://github.com/JoeanAmier/XHS-Downloader/blob/dfad51b3d1aac55866802007544f9390ad21553f/source/application/app.py#L792)
- [source/expansion/cleaner.py:112](https://github.com/JoeanAmier/XHS-Downloader/blob/dfad51b3d1aac55866802007544f9390ad21553f/source/expansion/cleaner.py#L112)
- [source/module/static.py:72](https://github.com/JoeanAmier/XHS-Downloader/blob/dfad51b3d1aac55866802007544f9390ad21553f/source/module/static.py#L72)
- [static/GUI/app.js](https://github.com/JoeanAmier/XHS-Downloader/blob/dfad51b3d1aac55866802007544f9390ad21553f/static/GUI/app.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: Settings. Observed top-level functions: include_distribution_metadata. |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: ExtractData, ExtractParams. |
| Application entry point | entrypoint | Observed | Groups 9 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed top-level classes: CLI, Cleaner, Print, XHS, XHSDownloader.… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| locale package | library | Observed | Groups 1 file(s) under locale package (observed from repository paths and static analysis). Observed top-level functions: find_python_files. |
| source package | library | Observed | Groups 39 file(s) under source package (observed from repository paths and static analysis). Observed top-level classes: About, Account, BrowserCookie, CacheError, Converter, DataRecorder. Observed top-level functions:… |
| static package | library | Observed | Groups 3 file(s) under static package (observed from repository paths and static analysis). |

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

- `source` — 47 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `.github` — 9 analysed file(s)
- `static` — 7 analysed file(s)
- `locale` — 6 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `dfad51b3d1aac55866802007544f9390ad21553f` is the revision these paths and observations refer to.
