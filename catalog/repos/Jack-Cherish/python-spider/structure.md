# Project structure: Jack-Cherish/python-spider

**Analysed commit:** `60b7ed839713ccf00bb30fe2b203a6b45d7459aa`

**Commit reference:** [60b7ed839713ccf00bb30fe2b203a6b45d7459aa](https://github.com/Jack-Cherish/python-spider/commit/60b7ed839713ccf00bb30fe2b203a6b45d7459aa)

**Tree at this commit:** [Jack-Cherish/python-spider@60b7ed839713](https://github.com/Jack-Cherish/python-spider/tree/60b7ed839713ccf00bb30fe2b203a6b45d7459aa)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Jack-Cherish/python-spider |
| Description | :rainbow:Python3网络爬虫实战：淘宝、京东、网易云、B站、12306、抖音、笔趣阁、漫画小说下载、音乐电影下载等 |
| Stars | 19859 |
| Forks | 5927 |
| Licence | Not detected |
| Language | Python |
| Default branch | master |
| Analysed commit | `60b7ed839713ccf00bb30fe2b203a6b45d7459aa` |
| Retrieved at | 2026-11-14T19:08:05.856867+00:00 |
| Files in this snapshot | 68 |

## Directory tree

```text
2020/  (8 files)
  api/  (1 files)
    api.py
  bilibili/  (2 files)
    download.py
    xml2ass.py
  dmzj/  (1 files)
    cartoon.py
  taobao/  (1 files)
    taobao_login.py
  xbqg/  (1 files)
    xbqg_spider.py
  zycjw/  (1 files)
    video_download.py
  README.md
Netease/  (2 files)
  Netease.py
  music_list.txt
baiwan/  (5 files)
  app.js
  baiwan.py
  file.txt
  index.html
  question.txt
bilibili/  (3 files)
  README.md
  bilibili.py
  xml2ass.py
bilibili_luckyman/  (2 files)
  README.md
  bilibili_luckyman.py
cartoon/  (8 files)
  cartoon/  (7 files)
    spiders/  (2 files)
      … 2 files under this directory
    __init__.py
    items.py
    middlewares.py
    pipelines.py
    settings.py
  scrapy.cfg
dingdong/  (2 files)
  README.md
  jd.py
douyin/  (3 files)
  README.md
  douyin.py
  fuck-byted-acrawler.js
one_hour_spider/  (5 files)
  biquge20180731.py
  biqukan.py
  unsplash.py
  unsplash20180731.py
  vidoe_downloader.py
video_downloader/  (13 files)
  MyQR/  (11 files)
    mylibs/  (8 files)
      … 8 files under this directory
    __init__.py
    myqr.py
    terminal.py
  requirements.txt
  video_downloader.py
zhengfang_system_spider/  (4 files)
  README.md
  requirements.txt
  spider.py
  zhengfang.txt
12306.py
README.md
baiduwenku.py
baiduwenku_pro_1.py
biqukan.py
daili.py
douyin.py
douyin_pro.py
downloader.py
financical.py
geetest.py
hero.py
shuaia.py
```

## Entry points

- [12306.py:122](https://github.com/Jack-Cherish/python-spider/blob/60b7ed839713ccf00bb30fe2b203a6b45d7459aa/12306.py#L122)
- [2020/bilibili/xml2ass.py:801](https://github.com/Jack-Cherish/python-spider/blob/60b7ed839713ccf00bb30fe2b203a6b45d7459aa/2020/bilibili/xml2ass.py#L801)
- [2020/taobao/taobao_login.py:93](https://github.com/Jack-Cherish/python-spider/blob/60b7ed839713ccf00bb30fe2b203a6b45d7459aa/2020/taobao/taobao_login.py#L93)
- [2020/xbqg/xbqg_spider.py:22](https://github.com/Jack-Cherish/python-spider/blob/60b7ed839713ccf00bb30fe2b203a6b45d7459aa/2020/xbqg/xbqg_spider.py#L22)
- [Netease/Netease.py:222](https://github.com/Jack-Cherish/python-spider/blob/60b7ed839713ccf00bb30fe2b203a6b45d7459aa/Netease/Netease.py#L222)
- [baiduwenku.py:7](https://github.com/Jack-Cherish/python-spider/blob/60b7ed839713ccf00bb30fe2b203a6b45d7459aa/baiduwenku.py#L7)
- [baiduwenku_pro_1.py:100](https://github.com/Jack-Cherish/python-spider/blob/60b7ed839713ccf00bb30fe2b203a6b45d7459aa/baiduwenku_pro_1.py#L100)
- [baiwan/baiwan.py:167](https://github.com/Jack-Cherish/python-spider/blob/60b7ed839713ccf00bb30fe2b203a6b45d7459aa/baiwan/baiwan.py#L167)
- [bilibili/bilibili.py:198](https://github.com/Jack-Cherish/python-spider/blob/60b7ed839713ccf00bb30fe2b203a6b45d7459aa/bilibili/bilibili.py#L198)
- [bilibili/xml2ass.py:801](https://github.com/Jack-Cherish/python-spider/blob/60b7ed839713ccf00bb30fe2b203a6b45d7459aa/bilibili/xml2ass.py#L801)
- [bilibili_luckyman/bilibili_luckyman.py:58](https://github.com/Jack-Cherish/python-spider/blob/60b7ed839713ccf00bb30fe2b203a6b45d7459aa/bilibili_luckyman/bilibili_luckyman.py#L58)
- [biqukan.py:118](https://github.com/Jack-Cherish/python-spider/blob/60b7ed839713ccf00bb30fe2b203a6b45d7459aa/biqukan.py#L118)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 1 file(s) under api layer (observed from repository paths and static analysis). |
| baiwan package | library | Observed | Groups 1 file(s) under baiwan package (observed from repository paths and static analysis). |
| 2020 package | library | Observed | Groups 3 file(s) under 2020 package (observed from repository paths and static analysis). Observed top-level functions: addTasktoXunlei, downVideo, get_download_url. |
| cartoon package | library | Observed | Groups 6 file(s) under cartoon package (observed from repository paths and static analysis). Observed top-level classes: CartoonSpiderMiddleware, ComicImgDownloadPipeline, ComicItem, ComicSpider. |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| douyin package | library | Observed | Groups 1 file(s) under douyin package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 29 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: APP, BaiWan, BiliBili, Crack, Crawler, DouYin. Observed top-level functions: ASSEscape, C… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| one_hour_spider package | library | Observed | Groups 1 file(s) under one_hour_spider package (observed from repository paths and static analysis). |
| video_downloader package | library | Observed | Groups 10 file(s) under video_downloader package (observed from repository paths and static analysis). Observed top-level functions: XOR, add_alignment, add_an_alignment, add_dark_and_reserving, add_finder_and_separator… |

## Important files

- `cartoon/scrapy.cfg` (config)
- `video_downloader/requirements.txt` (manifest)
- `zhengfang_system_spider/requirements.txt` (manifest)

## Top-level layout

- `(root files)` — 13 analysed file(s)
- `video_downloader` — 13 analysed file(s)
- `2020` — 8 analysed file(s)
- `cartoon` — 8 analysed file(s)
- `baiwan` — 5 analysed file(s)
- `one_hour_spider` — 5 analysed file(s)
- `zhengfang_system_spider` — 4 analysed file(s)
- `bilibili` — 3 analysed file(s)
- `douyin` — 3 analysed file(s)
- `Netease` — 2 analysed file(s)
- `bilibili_luckyman` — 2 analysed file(s)
- `dingdong` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- File 2020/api/api.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `60b7ed839713ccf00bb30fe2b203a6b45d7459aa` is the revision these paths and observations refer to.
