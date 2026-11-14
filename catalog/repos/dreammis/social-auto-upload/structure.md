# Project structure: dreammis/social-auto-upload

**Analysed commit:** `3847fff01f5434a8a32829833163cd6723cabc59`

**Commit reference:** [3847fff01f5434a8a32829833163cd6723cabc59](https://github.com/dreammis/social-auto-upload/commit/3847fff01f5434a8a32829833163cd6723cabc59)

**Tree at this commit:** [dreammis/social-auto-upload@3847fff01f54](https://github.com/dreammis/social-auto-upload/tree/3847fff01f5434a8a32829833163cd6723cabc59)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | dreammis/social-auto-upload |
| Description | 自动化上传视频到社交媒体：抖音、小红书、视频号、tiktok、youtube、bilibili |
| Stars | 16542 |
| Forks | 2807 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `3847fff01f5434a8a32829833163cd6723cabc59` |
| Retrieved at | 2026-11-14T19:08:46.500309+00:00 |
| Files in this snapshot | 262 |

## Directory tree

```text
.github/  (2 files)
  FUNDING.yml
  pull_request_template.md
db/  (1 files)
  createTable.py
docs/  (15 files)
  superpowers/  (5 files)
    plans/  (3 files)
      … 3 files under this directory
    specs/  (2 files)
      … 2 files under this directory
  CLI.md
  agent-bootstrap.md
  article.md
  dayu-article.md
  dayu.md
  install.md
  legacy-web.md
  skill-distribution.md
  update.md
  xueqiu.md
examples/  (23 files)
  __init__.py
  article.md
  dayu_article.html
  get_alipay_cookie.py
  get_baijiahao_cookie.py
  get_baijiahao_cookie_headless.py
  get_bilibili_cookie.py
  get_douyin_cookie.py
  get_kuaishou_cookie.py
  get_tencent_cookie.py
  get_tk_cookie.py
  get_xiaohongshu_cookie.py
  test_alipay_upload.py
  upload_to_douyin.py
  upload_to_kuaishou.py
  upload_video_to_baijiahao.py
  upload_video_to_bilibili.py
  upload_video_to_tencent.py
  upload_video_to_tiktok.py
  upload_video_to_xhs.py
  upload_video_to_xiaohongshu.py
  xueqiu_article.html
  xueqiu_article.md
myUtils/  (4 files)
  __init__.py
  auth.py
  login.py
  postVideo.py
sau_backend/  (1 files)
  README.md
sau_commands/  (19 files)
  __init__.py
  alipay.py
  arguments.py
  article.py
  baijiahao.py
  bilibili.py
  dayu.py
  douyin.py
  facebook.py
  facebook_page.py
  hupu.py
  instagram.py
  kuaishou.py
  tencent.py
  weibo.py
  xiaohongshu.py
  xueqiu.py
  youtube.py
  zhihu.py
sau_frontend/  (26 files)
  public/  (1 files)
    vite.svg
  src/  (21 files)
    api/  (4 files)
      … 4 files under this directory
    assets/  (1 files)
      … 1 files under this directory
    router/  (1 files)
      … 1 files under this directory
    stores/  (4 files)
      … 4 files under this directory
    styles/  (3 files)
      … 3 files under this directory
    utils/  (1 files)
      … 1 files under this directory
    views/  (5 files)
      … 5 files under this directory
    App.vue
    main.js
  README.md
  index.html
  package.json
  vite.config.js
skills/  (60 files)
  alipay-upload/  (1 files)
    SKILL.md
  baijiahao-upload/  (1 files)
    SKILL.md
  bilibili-upload/  (7 files)
    references/  (3 files)
      … 3 files under this directory
    scripts/  (3 files)
      … 3 files under this directory
    SKILL.md
  dayu-upload/  (4 files)
    scripts/  (3 files)
      … 3 files under this directory
    SKILL.md
  douyin-upload/  (7 files)
    references/  (3 files)
      … 3 files under this directory
    scripts/  (3 files)
      … 3 files under this directory
    SKILL.md
  facebook-upload/  (4 files)
    scripts/  (3 files)
      … 3 files under this directory
    SKILL.md
  hupu-upload/  (1 files)
    SKILL.md
  instagram-upload/  (4 files)
    scripts/  (3 files)
      … 3 files under this directory
    SKILL.md
  kuaishou-upload/  (7 files)
    references/  (3 files)
      … 3 files under this directory
    scripts/  (3 files)
      … 3 files under this directory
    SKILL.md
  meta-upload/  (4 files)
    scripts/  (3 files)
      … 3 files under this directory
    SKILL.md
  social-auto-upload/  (1 files)
    SKILL.md
  tencent-upload/  (1 files)
    SKILL.md
  tiktok-upload/  (1 files)
    SKILL.md
  weibo-upload/  (1 files)
    SKILL.md
  xiaohongshu-upload/  (7 files)
    references/  (3 files)
      … 3 files under this directory
    scripts/  (3 files)
      … 3 files under this directory
    SKILL.md
  xueqiu-upload/  (4 files)
    scripts/  (3 files)
      … 3 files under this directory
    SKILL.md
  youtube-upload/  (1 files)
    SKILL.md
  zhihu-upload/  (4 files)
    scripts/  (3 files)
      … 3 files under this directory
    SKILL.md
tests/  (18 files)
  __init__.py
  test_article_render.py
  test_bilibili_runtime.py
  test_dayu_article.py
  test_dayu_schedule.py
  test_dayu_uploader.py
  test_douyin_declaration.py
  test_facebook_posts.py
  test_facebook_uploader.py
  test_instagram_uploader.py
  test_kuaishou_publish_dialog.py
  test_meta_uploader.py
  test_sau_bilibili_cli.py
  test_sau_browser_cli.py
  test_tencent_verification_dialog.py
  test_xiaohongshu_uploader.py
  test_xueqiu_uploader.py
  test_zhihu_uploader.py
uploader/  (64 files)
  alipay_uploader/  (2 files)
    __init__.py
    main.py
  baijiahao_uploader/  (2 files)
    __init__.py
    main.py
  bilibili_uploader/  (2 files)
    __init__.py
    runtime.py
  dayu_uploader/  (10 files)
    __init__.py
    article.py
    article_content.py
    article_style.py
    constants.py
    main.py
    publication.py
    schedule.py
    session.py
    verification.py
  douyin_uploader/  (2 files)
    __init__.py
    main.py
  hupu_uploader/  (2 files)
    __init__.py
    main.py
  ks_uploader/  (2 files)
    __init__.py
    main.py
  meta_uploader/  (10 files)
    facebook_page_uploader/  (3 files)
      … 3 files under this directory
    facebook_uploader/  (3 files)
      … 3 files under this directory
    insgraph_uploader/  (3 files)
      … 3 files under this directory
    __init__.py
  tencent_uploader/  (2 files)
    __init__.py
    main.py
  tk_uploader/  (4 files)
    __init__.py
    main.py
    main_chrome.py
    tk_config.py
  weibo_uploader/  (2 files)
    __init__.py
    main.py
  xhs_uploader/  (4 files)
    __init__.py
    accounts.ini
    main.py
    xhs_login_qrcode.py
  xiaohongshu_uploader/  (2 files)
    __init__.py
    main.py
  xueqiu_uploader/  (6 files)
    __init__.py
    article.py
    constants.py
    content.py
    session.py
    verification.py
  youtube_uploader/  (2 files)
    __init__.py
    main.py
  zhihu_uploader/  (8 files)
    AUTOMATION.md
    __init__.py
    article.py
    constants.py
    schedule.py
    session.py
    verification.py
    video.py
  __init__.py
  base_video.py
utils/  (15 files)
  article_renderer/  (5 files)
    BAOYU-LICENSE
    DOOCS-LICENSE
    NOTICE.md
    package.json
    render.mjs
  __init__.py
  article_content.py
  article_render.py
  base_social_media.py
  browser_hook.py
  constant.py
  files_times.py
  log.py
  login_qrcode.py
  network.py
videos/  (1 files)
  demo.txt
.dockerignore
.gitignore
CHANGELOG.md
Dockerfile
LICENSE
README.md
__init__.py
conf.example.py
export_douyin_cookie.sh
pyproject.toml
sau_backend.py
sau_cli.py
start-win.bat
```

## Entry points

- [sau_backend.py:18](https://github.com/dreammis/social-auto-upload/blob/3847fff01f5434a8a32829833163cd6723cabc59/sau_backend.py#L18)
- [sau_cli.py](https://github.com/dreammis/social-auto-upload/blob/3847fff01f5434a8a32829833163cd6723cabc59/sau_cli.py)
- [uploader/xhs_uploader/xhs_login_qrcode.py:11](https://github.com/dreammis/social-auto-upload/blob/3847fff01f5434a8a32829833163cd6723cabc59/uploader/xhs_uploader/xhs_login_qrcode.py#L11)
- [sau_frontend/src/api/index.js](https://github.com/dreammis/social-auto-upload/blob/3847fff01f5434a8a32829833163cd6723cabc59/sau_frontend/src/api/index.js)
- [sau_frontend/src/main.js](https://github.com/dreammis/social-auto-upload/blob/3847fff01f5434a8a32829833163cd6723cabc59/sau_frontend/src/main.js)
- [sau_frontend/src/router/index.js](https://github.com/dreammis/social-auto-upload/blob/3847fff01f5434a8a32829833163cd6723cabc59/sau_frontend/src/router/index.js)
- [sau_frontend/src/stores/app.js](https://github.com/dreammis/social-auto-upload/blob/3847fff01f5434a8a32829833163cd6723cabc59/sau_frontend/src/stores/app.js)
- [sau_frontend/src/stores/index.js](https://github.com/dreammis/social-auto-upload/blob/3847fff01f5434a8a32829833163cd6723cabc59/sau_frontend/src/stores/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 9 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 22 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Flask. Observed routes: ROUTE /assets/<filename>, ROUTE /favicon.ico, ROUTE /… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| myUtils package | library | Observed | Groups 4 file(s) under myutils package (observed from repository paths and static analysis). Observed top-level functions: check_cookie, cookie_auth_douyin, cookie_auth_ks, cookie_auth_tencent, cookie_auth_xhs, douyin_c… |
| sau_commands package | library | Observed | Groups 19 file(s) under sau_commands package (observed from repository paths and static analysis). Observed top-level classes: AlipayVideoUploadRequest, BaijiahaoVideoUploadRequest, BilibiliVideoUploadRequest, DouyinNot… |
| sau_frontend package | library | Observed | Groups 9 file(s) under sau_frontend package (observed from repository paths and static analysis). |
| skills package | library | Observed | Groups 16 file(s) under skills package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 19 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH uploader.bilibili_uploader.runtime.fetch_latest_release, PATCH uploader.bilibili_uploader.runtime.fetch_latest_r… |
| uploader package | library | Observed | Groups 46 file(s) under uploader package (observed from repository paths and static analysis). Observed top-level classes: BaseVideoUploader, DayuArticle, TiktokVideo, Tk_Locator, XueqiuArticle, XueqiuHTML. Observed top… |
| utils package | library | Observed | Groups 11 file(s) under utils package (observed from repository paths and static analysis). Observed top-level classes: ArticleDocument, TencentZoneTypes, VideoZoneTypes. Observed top-level functions: _print_ascii_qrcod… |

## Important files

- `.dockerignore` (container)
- `.github/FUNDING.yml` (config)
- `Dockerfile` (container)
- `pyproject.toml` (manifest)
- `sau_frontend/package.json` (manifest)
- `uploader/xhs_uploader/accounts.ini` (config)
- `utils/article_renderer/package.json` (manifest)

## Top-level layout

- `uploader` — 64 analysed file(s)
- `skills` — 60 analysed file(s)
- `sau_frontend` — 26 analysed file(s)
- `examples` — 23 analysed file(s)
- `sau_commands` — 19 analysed file(s)
- `tests` — 18 analysed file(s)
- `docs` — 15 analysed file(s)
- `utils` — 15 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `myUtils` — 4 analysed file(s)
- `.github` — 2 analysed file(s)
- `db` — 1 analysed file(s)
- `sau_backend` — 1 analysed file(s)
- `videos` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 4 file(s) were skipped during inventory (2 x likely secret file excluded; 2 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `3847fff01f5434a8a32829833163cd6723cabc59` is the revision these paths and observations refer to.
