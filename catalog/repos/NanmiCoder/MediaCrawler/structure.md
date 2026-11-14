# Project structure: NanmiCoder/MediaCrawler

**Analysed commit:** `306ab4ca26c0e44fb87ede0e40e98748752815a6`

**Commit reference:** [306ab4ca26c0e44fb87ede0e40e98748752815a6](https://github.com/NanmiCoder/MediaCrawler/commit/306ab4ca26c0e44fb87ede0e40e98748752815a6)

**Tree at this commit:** [NanmiCoder/MediaCrawler@306ab4ca26c0](https://github.com/NanmiCoder/MediaCrawler/tree/306ab4ca26c0e44fb87ede0e40e98748752815a6)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | NanmiCoder/MediaCrawler |
| Description | 小红书笔记 | 评论爬虫、抖音视频 | 评论爬虫、快手视频 | 评论爬虫、B 站视频 ｜ 评论爬虫、微博帖子 ｜ 评论爬虫、百度贴吧帖子 ｜ 百度贴吧评论回复爬虫  | 知乎问答文章｜评论爬虫 |
| Stars | 71120 |
| Forks | 13437 |
| Licence | Other |
| Language | Python |
| Default branch | main |
| Analysed commit | `306ab4ca26c0e44fb87ede0e40e98748752815a6` |
| Retrieved at | 2026-11-14T19:06:15.710040+00:00 |
| Files in this snapshot | 305 |

## Directory tree

```text
.github/  (5 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    quesiton.md
  workflows/  (1 files)
    deploy.yml
  CODEOWNERS
  FUNDING.yml
api/  (10 files)
  routers/  (4 files)
    __init__.py
    crawler.py
    data.py
    websocket.py
  schemas/  (2 files)
    __init__.py
    crawler.py
  services/  (2 files)
    __init__.py
    crawler_manager.py
  __init__.py
  main.py
base/  (2 files)
  __init__.py
  base_crawler.py
cache/  (5 files)
  __init__.py
  abs_cache.py
  cache_factory.py
  local_cache.py
  redis_cache.py
cmd_arg/  (2 files)
  __init__.py
  arg.py
config/  (10 files)
  __init__.py
  base_config.py
  bilibili_config.py
  db_config.py
  dy_config.py
  ks_config.py
  tieba_config.py
  weibo_config.py
  xhs_config.py
  zhihu_config.py
constant/  (3 files)
  __init__.py
  baidu_tieba.py
  zhihu.py
database/  (5 files)
  __init__.py
  db.py
  db_session.py
  models.py
  mongodb_store_base.py
docs/  (26 files)
  .vitepress/  (5 files)
    theme/  (4 files)
      … 4 files under this directory
    config.mjs
  proxylane/  (2 files)
    README.md
    README_en.md
  CDP模式使用指南.md
  data_storage_guide.md
  excel_export_guide.md
  hit_stopwords.txt
  index.md
  mediacrawlerpro订阅.md
  代理使用.md
  作者介绍.md
  原生环境管理文档.md
  常见问题.md
  微信交流群.md
  快代理使用文档.md
  手机号登录说明.md
  捐赠名单.md
  知识付费介绍.md
  词云图使用配置.md
  豌豆HTTP使用文档.md
  项目代码结构.md
  项目架构文档.md
libs/  (2 files)
  douyin.js
  zhihu.js
media_downloader/  (5 files)
  __init__.py
  downloader.py
  ffmpeg.py
  paths.py
  types.py
media_platform/  (67 files)
  bilibili/  (8 files)
    __init__.py
    client.py
    core.py
    exception.py
    field.py
    help.py
    login.py
    media.py
  douyin/  (8 files)
    __init__.py
    client.py
    core.py
    exception.py
    field.py
    help.py
    login.py
    media.py
  kuaishou/  (16 files)
    graphql/  (7 files)
      … 7 files under this directory
    __init__.py
    client.py
    core.py
    exception.py
    field.py
    graphql.py
    help.py
    login.py
    media.py
  tieba/  (8 files)
    test_data/  (2 files)
      … 2 files under this directory
    __init__.py
    client.py
    core.py
    field.py
    help.py
    login.py
  weibo/  (8 files)
    __init__.py
    client.py
    core.py
    exception.py
    field.py
    help.py
    login.py
    media.py
  xhs/  (11 files)
    __init__.py
    client.py
    core.py
    exception.py
    extractor.py
    field.py
    help.py
    login.py
    media.py
    playwright_sign.py
    xhs_sign.py
  zhihu/  (7 files)
    __init__.py
    client.py
    core.py
    exception.py
    field.py
    help.py
    login.py
  __init__.py
model/  (8 files)
  __init__.py
  m_baidu_tieba.py
  m_bilibili.py
  m_douyin.py
  m_kuaishou.py
  m_weibo.py
  m_xiaohongshu.py
  m_zhihu.py
proxy/  (9 files)
  providers/  (4 files)
    __init__.py
    jishu_http_proxy.py
    kuaidl_proxy.py
    wandou_http_proxy.py
  __init__.py
  base_proxy.py
  proxy_ip_pool.py
  proxy_mixin.py
  types.py
store/  (16 files)
  bilibili/  (2 files)
    __init__.py
    _store_impl.py
  douyin/  (2 files)
    __init__.py
    _store_impl.py
  kuaishou/  (2 files)
    __init__.py
    _store_impl.py
  tieba/  (2 files)
    __init__.py
    _store_impl.py
  weibo/  (2 files)
    __init__.py
    _store_impl.py
  xhs/  (2 files)
    __init__.py
    _store_impl.py
  zhihu/  (2 files)
    __init__.py
    _store_impl.py
  __init__.py
  excel_store_base.py
test/  (7 files)
  __init__.py
  test_db_sync.py
  test_expiring_local_cache.py
  test_mongodb_integration.py
  test_proxy_ip_pool.py
  test_redis_cache.py
  test_utils.py
tests/  (32 files)
  __init__.py
  conftest.py
  media_server.py
  test_api_limits.py
  test_bilibili_client_comments.py
  test_bilibili_login_state.py
  test_cdp_browser.py
  test_cdp_browser_timeout_hint.py
  test_cmd_arg_media.py
  test_cmd_arg_tieba.py
  test_douyin_argus_header.py
  test_douyin_aweme_detail_params.py
  test_douyin_no_user_info.py
  test_douyin_url_parse.py
  test_excel_store.py
  test_ip_cache.py
  test_kuaishou_no_user_info.py
  test_kuaishou_unavailable_video.py
  test_kuaishou_url_parse.py
  test_media_core_integration.py
  test_media_downloader.py
  test_media_e2e.py
  test_media_extractors.py
  test_media_ffmpeg.py
  … 8 more files
tools/  (14 files)
  __init__.py
  app_runner.py
  async_file_writer.py
  browser_launcher.py
  cdp_browser.py
  crawler_util.py
  easing.py
  file_header_manager.py
  httpx_util.py
  slider_util.py
  time_util.py
  user_hash.py
  utils.py
  words.py
webui/  (61 files)
  public/  (1 files)
    vite.svg
  src/  (52 files)
    components/  (27 files)
      … 27 files under this directory
    hooks/  (2 files)
      … 2 files under this directory
    i18n/  (13 files)
      … 13 files under this directory
    lib/  (3 files)
      … 3 files under this directory
    store/  (2 files)
      … 2 files under this directory
    types/  (1 files)
      … 1 files under this directory
    App.tsx
    index.css
    main.tsx
    vite-env.d.ts
  .gitignore
  LICENSE
  index.html
  package.json
  postcss.config.js
  tailwind.config.ts
  tsconfig.json
  vite.config.ts
.env.example
.gitattributes
.gitignore
.pre-commit-config.yaml
.python-version
LICENSE
README.md
README_en.md
README_es.md
main.py
mypy.ini
package.json
pyproject.toml
recv_sms.py
requirements.txt
var.py
```

## Entry points

- [api/main.py:40](https://github.com/NanmiCoder/MediaCrawler/blob/306ab4ca26c0e44fb87ede0e40e98748752815a6/api/main.py#L40)
- [cache/local_cache.py:131](https://github.com/NanmiCoder/MediaCrawler/blob/306ab4ca26c0e44fb87ede0e40e98748752815a6/cache/local_cache.py#L131)
- [cache/redis_cache.py:101](https://github.com/NanmiCoder/MediaCrawler/blob/306ab4ca26c0e44fb87ede0e40e98748752815a6/cache/redis_cache.py#L101)
- [cmd_arg/arg.py:157](https://github.com/NanmiCoder/MediaCrawler/blob/306ab4ca26c0e44fb87ede0e40e98748752815a6/cmd_arg/arg.py#L157)
- [main.py:145](https://github.com/NanmiCoder/MediaCrawler/blob/306ab4ca26c0e44fb87ede0e40e98748752815a6/main.py#L145)
- [media_platform/bilibili/help.py:134](https://github.com/NanmiCoder/MediaCrawler/blob/306ab4ca26c0e44fb87ede0e40e98748752815a6/media_platform/bilibili/help.py#L134)
- [media_platform/douyin/help.py:173](https://github.com/NanmiCoder/MediaCrawler/blob/306ab4ca26c0e44fb87ede0e40e98748752815a6/media_platform/douyin/help.py#L173)
- [media_platform/kuaishou/help.py:151](https://github.com/NanmiCoder/MediaCrawler/blob/306ab4ca26c0e44fb87ede0e40e98748752815a6/media_platform/kuaishou/help.py#L151)
- [media_platform/tieba/help.py:869](https://github.com/NanmiCoder/MediaCrawler/blob/306ab4ca26c0e44fb87ede0e40e98748752815a6/media_platform/tieba/help.py#L869)
- [media_platform/xhs/help.py:350](https://github.com/NanmiCoder/MediaCrawler/blob/306ab4ca26c0e44fb87ede0e40e98748752815a6/media_platform/xhs/help.py#L350)
- [proxy/proxy_ip_pool.py:221](https://github.com/NanmiCoder/MediaCrawler/blob/306ab4ca26c0e44fb87ede0e40e98748752815a6/proxy/proxy_ip_pool.py#L221)
- [recv_sms.py:33](https://github.com/NanmiCoder/MediaCrawler/blob/306ab4ca26c0e44fb87ede0e40e98748752815a6/recv_sms.py#L33)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 9 file(s) under api layer (observed from repository paths and static analysis). Observed routes: POST /start, POST /stop, GET /status, GET /logs, GET /files. Observed top-level classes: ConnectionManager, Crawler… |
| base package | library | Observed | Groups 2 file(s) under base package (observed from repository paths and static analysis). Observed top-level classes: AbstractApiClient, AbstractCrawler, AbstractLogin, AbstractStore. |
| cache package | library | Observed | Groups 3 file(s) under cache package (observed from repository paths and static analysis). Observed top-level classes: AbstractCache, CacheFactory. |
| cmd_arg package | library | Observed | Groups 1 file(s) under cmd_arg package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 30 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| constant package | library | Observed | Groups 3 file(s) under constant package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 10 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: BilibiliUpDynamic, BilibiliVideo, BilibiliVideoComment, DouyinAweme, DouyinAwemeComment, KuaishouVideo… |
| Application entry point | entrypoint | Observed | Groups 15 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI, Typer. Observed routes: GET /, GET /api/health, GET /api/env/check,… |
| External integrations | external | Observed | Groups 7 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: BaiduTieBaClient, BilibiliClient, DouYinClient, KuaiShouClient, WeiboClient, XiaoHongShuClie… |
| libs package | library | Observed | Groups 2 file(s) under libs package (observed from repository paths and static analysis). |
| media_downloader package | library | Observed | Groups 5 file(s) under media_downloader package (observed from repository paths and static analysis). Observed top-level classes: MediaDownloadError, MediaDownloader, MediaFatalError, MediaItem, MediaRetryableError, Med… |
| media_platform package | library | Observed | Groups 46 file(s) under media_platform package (observed from repository paths and static analysis). Observed top-level classes: BaiduTieBaLogin, BilibiliCrawler, BilibiliLogin, CommentOrderType, DataFetchError, DouYinC… |
| model package | library | Observed | Groups 8 file(s) under model package (observed from repository paths and static analysis). Observed top-level classes: CreatorUrlInfo, NoteUrlInfo, TiebaComment, TiebaCreator, TiebaNote, VideoUrlInfo. |
| proxy package | library | Observed | Groups 8 file(s) under proxy package (observed from repository paths and static analysis). Observed top-level classes: IpCache, IpGetError, IpInfoModel, JiSuHttpProxy, KuaiDaiLiProxy, KuaidailiProxyModel. Observed top-l… |
| store package | library | Observed | Groups 16 file(s) under store package (observed from repository paths and static analysis). Observed top-level classes: BiliCsvStoreImplement, BiliDbStoreImplement, BiliExcelStoreImplement, BiliJsonStoreImplement, BiliJ… |
| Tests | test | Observed | Groups 39 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH config.SAVE_DATA_OPTION, PATCH config.SAVE_DATA_OPTION, PATCH config.SAVE_DATA_OPTION, PATCH config.SAVE_DATA_OP… |
| tools package | library | Observed | Groups 11 file(s) under tools package (observed from repository paths and static analysis). Observed top-level classes: AsyncFileWriter, AsyncWordCloudGenerator, BrowserLauncher, CDPBrowserManager, Slide. Observed top-l… |
| webui package | library | Observed | Groups 35 file(s) under webui package (observed from repository paths and static analysis). |

## Important files

- `.env.example` (config)
- `.github/FUNDING.yml` (config)
- `.github/workflows/deploy.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `mypy.ini` (config)
- `package.json` (manifest)
- `pyproject.toml` (manifest)
- `requirements.txt` (manifest)
- `webui/package.json` (manifest)
- `webui/src/i18n/locales/en-US/common.json` (config)
- `webui/src/i18n/locales/en-US/config.json` (config)
- `webui/src/i18n/locales/en-US/data.json` (config)
- `webui/src/i18n/locales/en-US/env.json` (config)
- `webui/src/i18n/locales/en-US/license.json` (config)
- `webui/src/i18n/locales/en-US/terminal.json` (config)
- `webui/src/i18n/locales/zh-CN/common.json` (config)
- `webui/src/i18n/locales/zh-CN/config.json` (config)
- `webui/src/i18n/locales/zh-CN/data.json` (config)
- `webui/src/i18n/locales/zh-CN/env.json` (config)
- `webui/src/i18n/locales/zh-CN/license.json` (config)
- `webui/src/i18n/locales/zh-CN/terminal.json` (config)
- `webui/tsconfig.json` (config)

## Top-level layout

- `media_platform` — 67 analysed file(s)
- `webui` — 61 analysed file(s)
- `tests` — 32 analysed file(s)
- `docs` — 26 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `store` — 16 analysed file(s)
- `tools` — 14 analysed file(s)
- `api` — 10 analysed file(s)
- `config` — 10 analysed file(s)
- `proxy` — 9 analysed file(s)
- `model` — 8 analysed file(s)
- `test` — 7 analysed file(s)
- `.github` — 5 analysed file(s)
- `cache` — 5 analysed file(s)
- `database` — 5 analysed file(s)
- `media_downloader` — 5 analysed file(s)
- `constant` — 3 analysed file(s)
- `base` — 2 analysed file(s)
- `cmd_arg` — 2 analysed file(s)
- `libs` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `306ab4ca26c0e44fb87ede0e40e98748752815a6` is the revision these paths and observations refer to.
