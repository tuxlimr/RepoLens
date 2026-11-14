# Project structure: wistbean/learn_python3_spider

**Analysed commit:** `f5f43b62504d2f06f2a41746e955227aa017fec4`

**Commit reference:** [f5f43b62504d2f06f2a41746e955227aa017fec4](https://github.com/wistbean/learn_python3_spider/commit/f5f43b62504d2f06f2a41746e955227aa017fec4)

**Tree at this commit:** [wistbean/learn_python3_spider@f5f43b62504d](https://github.com/wistbean/learn_python3_spider/tree/f5f43b62504d2f06f2a41746e955227aa017fec4)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | wistbean/learn_python3_spider |
| Description | python爬虫教程系列、从0到1学习python爬虫，包括浏览器抓包，手机APP抓包，如 fiddler、mitmproxy，各种爬虫涉及的模块的使用，如：requests、beautifulSoup、selenium、appium、scrapy等，以及IP代理，验证码识别，Mysql，MongoDB数据库的python使用，多线程多进程爬虫的使用，css 爬虫加密逆向破解，JS爬虫逆向，分布式爬虫，爬虫项目实战实例等 |
| Stars | 22291 |
| Forks | 3922 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `f5f43b62504d2f06f2a41746e955227aa017fec4` |
| Retrieved at | 2026-11-14T19:07:56.247921+00:00 |
| Files in this snapshot | 64 |

## Directory tree

```text
GaoKao_Score/  (33 files)
  2006-2016浙江高考录取分数线.html
  2006-2016海南高考录取分数线.html
  2006-2017上海高考录取分数线.html
  2006-2017安徽高考录取分数线.html
  2006-2017山东高考录取分数线.html
  2006-2017山西高考录取分数线.html
  2006-2017新疆高考录取分数线.html
  2006-2017河南高考录取分数线.html
  2006-2017福建高考录取分数线.html
  2006-2017重庆高考录取分数线.html
  2006-2017黑龙江高考录取分数线.html
  2006-2018云南高考录取分数线.html
  2006-2018内蒙古高考录取分数线.html
  2006-2018北京高考录取分数线.html
  2006-2018吉林高考录取分数线.html
  2006-2018四川高考录取分数线.html
  2006-2018天津高考录取分数线.html
  2006-2018宁夏高考录取分数线.html
  2006-2018广东高考录取分数线.html
  2006-2018广西高考录取分数线.html
  2006-2018江西高考分数线.html
  2006-2018河北高考录取分数线.html
  2006-2018湖北高考录取分数线.html
  2006-2018湖南高考录取分数线.html
  … 9 more files
biaoqingbao/  (2 files)
  biaoqingbao.py
  search.py
qiushibaike/  (8 files)
  qiushibaike/  (7 files)
    spiders/  (2 files)
      … 2 files under this directory
    __init__.py
    items.py
    middlewares.py
    pipelines.py
    settings.py
  scrapy.cfg
stackoverflow/  (11 files)
  stackoverflow/  (10 files)
    middlewares/  (2 files)
      … 2 files under this directory
    spiders/  (2 files)
      … 2 files under this directory
    __init__.py
    items.py
    middlewares.py
    pipelines.py
    requirement.txt
    settings.py
  scrapy.cfg
.gitattributes
CloudCreat
LICENSE
README.md
dangdang_top_500.py
douban_top_250_books.py
douban_top_250_books_mul_process.py
fuck_bilibili_captcha.py
ikun_basketball.py
meizitu.py
```

## Entry points

- [biaoqingbao/biaoqingbao.py:50](https://github.com/wistbean/learn_python3_spider/blob/f5f43b62504d2f06f2a41746e955227aa017fec4/biaoqingbao/biaoqingbao.py#L50)
- [dangdang_top_500.py:47](https://github.com/wistbean/learn_python3_spider/blob/f5f43b62504d2f06f2a41746e955227aa017fec4/dangdang_top_500.py#L47)
- [douban_top_250_books_mul_process.py:44](https://github.com/wistbean/learn_python3_spider/blob/f5f43b62504d2f06f2a41746e955227aa017fec4/douban_top_250_books_mul_process.py#L44)
- [fuck_bilibili_captcha.py:193](https://github.com/wistbean/learn_python3_spider/blob/f5f43b62504d2f06f2a41746e955227aa017fec4/fuck_bilibili_captcha.py#L193)
- [ikun_basketball.py:122](https://github.com/wistbean/learn_python3_spider/blob/f5f43b62504d2f06f2a41746e955227aa017fec4/ikun_basketball.py#L122)
- [meizitu.py:88](https://github.com/wistbean/learn_python3_spider/blob/f5f43b62504d2f06f2a41746e955227aa017fec4/meizitu.py#L88)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| biaoqingbao package | library | Observed | Groups 1 file(s) under biaoqingbao package (observed from repository paths and static analysis). Observed top-level functions: searchImage, text_reply. |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 6 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: DownloadBiaoqingbao. Observed top-level functions: download, download_Pic, download_all_im… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| qiushibaike package | library | Observed | Groups 6 file(s) under qiushibaike package (observed from repository paths and static analysis). Observed top-level classes: QiushiSpider, QiushibaikeDownloaderMiddleware, QiushibaikeItem, QiushibaikePipeline, Qiushibai… |
| stackoverflow package | library | Observed | Groups 8 file(s) under stackoverflow package (observed from repository paths and static analysis). Observed top-level classes: HttpProxy, StackoverflowDownloaderMiddleware, StackoverflowPipeline, StackoverflowPythonItem… |

## Important files

- `qiushibaike/scrapy.cfg` (config)
- `stackoverflow/scrapy.cfg` (config)

## Top-level layout

- `GaoKao_Score` — 33 analysed file(s)
- `stackoverflow` — 11 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `qiushibaike` — 8 analysed file(s)
- `biaoqingbao` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 736 file(s) were skipped during inventory (736 x vendored/generated directory excluded).
- File douban_top_250_books.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `f5f43b62504d2f06f2a41746e955227aa017fec4` is the revision these paths and observations refer to.
