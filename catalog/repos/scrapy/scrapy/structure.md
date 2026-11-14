# Project structure: scrapy/scrapy

**Analysed commit:** `e63a574c767d7a9438c21db158f605f1c44c6e6a`

**Commit reference:** [e63a574c767d7a9438c21db158f605f1c44c6e6a](https://github.com/scrapy/scrapy/commit/e63a574c767d7a9438c21db158f605f1c44c6e6a)

**Tree at this commit:** [scrapy/scrapy@e63a574c767d](https://github.com/scrapy/scrapy/tree/e63a574c767d7a9438c21db158f605f1c44c6e6a)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | scrapy/scrapy |
| Description | Scrapy, a fast high-level web crawling & scraping framework for Python. |
| Stars | 65389 |
| Forks | 12140 |
| Licence | BSD-3-Clause |
| Language | Python |
| Default branch | master |
| Analysed commit | `e63a574c767d7a9438c21db158f605f1c44c6e6a` |
| Retrieved at | 2026-11-14T19:06:18.601443+00:00 |
| Files in this snapshot | 708 |

## Directory tree

```text
.github/  (12 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    feature_request.md
    question.md
  workflows/  (7 files)
    ci.yml
    close-spam-prs.yml
    codspeed-walltime.yml
    codspeed.yml
    publish.yml
    tests-vcs-deps.yml
    upgrade-ci-pins.yml
  dependabot.yml
  pull_request_template.md
docs/  (72 files)
  _ext/  (2 files)
    scrapydocs.py
    scrapyfixautodoc.py
  _static/  (3 files)
    custom.css
    logo.svg
    selectors-sample1.html
  _templates/  (1 files)
    layout.html
  _tests/  (2 files)
    quotes.html
    quotes1.html
  intro/  (5 files)
    examples.rst
    getting-help.rst
    install.rst
    overview.rst
    tutorial.rst
  news/  (3 files)
    0.x.rst
    1.x.rst
    2.x.rst
  topics/  (47 files)
    addons.rst
    agents.rst
    api.rst
    architecture.rst
    asyncio.rst
    autothrottle.rst
    benchmarking.rst
    commands.rst
    components.rst
    concepts.rst
    contracts.rst
    cookies.rst
    coroutines.rst
    debug.rst
    deploy.rst
    developer-tools.rst
    djangoitem.rst
    download-handlers.rst
    downloader-middleware.rst
    dynamic-content.rst
    exceptions.rst
    exporters.rst
    extensions.rst
    extraction.rst
    … 23 more files
  utils/  (1 files)
    linkfix.py
  Makefile
  conf.py
  conftest.py
  contributing.rst
  faq.rst
  index.rst
  news.rst
  versioning.rst
extras/  (7 files)
  coverage-report.sh
  github-release-notes.py
  pre-bump.py
  qps-bench-server.py
  qpsclient.py
  scrapy.1
  upgrade-ci-pins.py
scrapy/  (213 files)
  _logging/  (1 files)
    __init__.py
  commands/  (17 files)
    __init__.py
    bench.py
    check.py
    complete.py
    crawl.py
    edit.py
    fetch.py
    genrequest.py
    genspider.py
    list.py
    parse.py
    runspider.py
    settings.py
    shell.py
    startproject.py
    version.py
    view.py
  contracts/  (2 files)
    __init__.py
    default.py
  core/  (28 files)
    _http2/  (4 files)
      … 4 files under this directory
    downloader/  (19 files)
      … 19 files under this directory
    __init__.py
    engine.py
    scheduler.py
    scraper.py
    spidermw.py
  downloadermiddlewares/  (16 files)
    __init__.py
    cookies.py
    defaultheaders.py
    downloadtimeout.py
    httpauth.py
    httpcache.py
    httpcompression.py
    httpproxy.py
    jsonvalidation.py
    offsite.py
    redirect.py
    retry.py
    robotstxt.py
    stats.py
    uriuserinfo.py
    useragent.py
  extensions/  (18 files)
    __init__.py
    closespider.py
    corestats.py
    debug.py
    event_loop_lag.py
    feedexport.py
    httpcache.py
    logcount.py
    logstats.py
    memdebug.py
    memusage.py
    periodic_log.py
    postprocessing.py
    remote_control.py
    spiderstate.py
    statsmailer.py
    telnet.py
    throttle.py
  http/  (13 files)
    request/  (4 files)
      … 4 files under this directory
    response/  (6 files)
      … 6 files under this directory
    __init__.py
    cookies.py
    headers.py
  linkextractors/  (2 files)
    __init__.py
    lxmlhtml.py
  loader/  (1 files)
    __init__.py
  pipelines/  (4 files)
    __init__.py
    files.py
    images.py
    media.py
  selector/  (2 files)
    __init__.py
    unified.py
  settings/  (2 files)
    __init__.py
    default_settings.py
  spidermiddlewares/  (9 files)
    __init__.py
    base.py
    depth.py
    httperror.py
    metacopy.py
    referer.py
    start.py
    stickymeta.py
    urllength.py
  spiders/  (4 files)
    __init__.py
    crawl.py
    feed.py
    sitemap.py
  templates/  (11 files)
    project/  (7 files)
      … 7 files under this directory
    spiders/  (4 files)
      … 4 files under this directory
  utils/  (55 files)
    __init__.py
    _benchserver.py
    _colorize.py
    _compression.py
    _datatypes.py
    _deps_compat.py
    _download_handlers.py
    _ftp.py
    _httpstatus.py
    _ossignals.py
    _remote_control.py
    _secrets.py
    _shell.py
    _sitemap.py
    _ssl.py
    _stopmode.py
    _template.py
    _versions.py
    asyncgen.py
    asyncio.py
    benchserver.py
    boto.py
    conf.py
    console.py
    … 31 more files
  VERSION
  __init__.py
  __main__.py
  addons.py
  cmdline.py
  crawler.py
  dupefilters.py
  exceptions.py
  exporters.py
  extension.py
  interfaces.py
  item.py
  link.py
  logformatter.py
  mail.py
  middleware.py
  mime.types
  pqueues.py
  py.typed
  resolver.py
  responsetypes.py
  robotstxt.py
  shell.py
  signalmanager.py
  … 4 more files
sep/  (21 files)
  README.rst
  sep-001.rst
  sep-002.rst
  sep-003.rst
  sep-004.rst
  sep-005.rst
  sep-006.rst
  sep-007.rst
  sep-008.rst
  sep-009.rst
  sep-010.rst
  sep-011.rst
  sep-012.rst
  sep-013.rst
  sep-014.rst
  sep-015.rst
  sep-016.rst
  sep-017.rst
  sep-018.rst
  sep-019.rst
  sep-020.rst
tests/  (361 files)
  AsyncCrawlerProcess/  (37 files)
    args_settings.py
    asyncio_custom_loop.py
    asyncio_custom_loop_custom_settings_different.py
    asyncio_custom_loop_custom_settings_same.py
    asyncio_deferred_signal.py
    asyncio_enabled_no_reactor.py
    asyncio_enabled_reactor.py
    asyncio_enabled_reactor_different_loop.py
    asyncio_enabled_reactor_loop_not_current.py
    asyncio_enabled_reactor_same_loop.py
    asyncio_enabled_reactor_same_loop_default.py
    caching_hostname_resolver.py
    caching_hostname_resolver_ipv6.py
    closespider_timeout_no_item.py
    default_name_resolver.py
    dns_resolver_deprecated.py
    multi.py
    reactor_default.py
    reactor_settings.py
    reactorless_custom_settings.py
    reactorless_datauri.py
    reactorless_import_hook.py
    reactorless_import_hook_multiple.py
    reactorless_import_hook_uninstall.py
    … 13 more files
  AsyncCrawlerRunner/  (12 files)
    custom_loop_different.py
    custom_loop_same.py
    multi_parallel.py
    multi_seq.py
    no_reactor.py
    reactorless_custom_settings.py
    reactorless_datauri.py
    reactorless_loop_not_running.py
    reactorless_reactor.py
    reactorless_simple.py
    simple.py
    simple_default_reactor.py
  CrawlerProcess/  (28 files)
    args_settings.py
    asyncio_custom_loop.py
    asyncio_deferred_signal.py
    asyncio_enabled_no_reactor.py
    asyncio_enabled_reactor.py
    asyncio_enabled_reactor_different_loop.py
    asyncio_enabled_reactor_loop_not_current.py
    asyncio_enabled_reactor_same_loop.py
    caching_hostname_resolver.py
    caching_hostname_resolver_ipv6.py
    default_name_resolver.py
    dns_resolver_deprecated.py
    multi.py
    reactor_default.py
    reactor_default_twisted_reactor_select.py
    reactor_select.py
    reactor_select_subclass_twisted_reactor_select.py
    reactor_select_twisted_reactor_select.py
    reactor_settings.py
    reactorless.py
    simple.py
    sleeping.py
    twisted_reactor_asyncio.py
    twisted_reactor_custom_settings.py
    … 4 more files
  CrawlerRunner/  (11 files)
    change_reactor.py
    custom_loop_different.py
    custom_loop_same.py
    explicit_default_reactor.py
    install_reactor_select.py
    ip_address.py
    multi_parallel.py
    multi_seq.py
    no_reactor.py
    reactorless.py
    simple.py
  benchmarks/  (8 files)
    __init__.py
    conftest.py
    test_crawl.py
    test_encoding.py
    test_exporters.py
    test_httpcompression.py
    test_urls.py
    urls.txt
  keys/  (6 files)
    __init__.py
    example-com.conf
    example-com.gen.README
    localhost-ip.gen.README
    localhost.gen.README
    localhost.ip.crt
  mocks/  (2 files)
    __init__.py
    dummydbm.py
  mockserver/  (13 files)
    __init__.py
    dns.py
    ftp.py
    http.py
    http_base.py
    http_resources.py
    mitm_proxy.py
    mitm_proxy_addon.py
    proxy_echo.py
    proxy_stalling.py
    raw_http.py
    simple_https.py
    utils.py
  sample_data/  (19 files)
    books/  (2 files)
      … 2 files under this directory
    compressed/  (2 files)
      … 2 files under this directory
    feeds/  (6 files)
      … 6 files under this directory
    link_extractor/  (4 files)
      … 4 files under this directory
    test_site/  (5 files)
      … 5 files under this directory
  test_cmdline/  (3 files)
    __init__.py
    extensions.py
    settings.py
  test_cmdline_crawl_with_pipeline/  (8 files)
    test_spider/  (6 files)
      … 6 files under this directory
    __init__.py
    scrapy.cfg
  test_settings/  (3 files)
    __init__.py
    default_settings.py
    test_secrets.py
  test_spiderloader/  (10 files)
    spiders_from_addons/  (2 files)
      … 2 files under this directory
    test_spiders/  (7 files)
      … 7 files under this directory
    __init__.py
  test_utils_misc/  (6 files)
    test_walk_modules/  (4 files)
      … 4 files under this directory
    __init__.py
    test_return_with_argument_inside_generator.py
  utils/  (19 files)
    bases/  (8 files)
      … 8 files under this directory
    __init__.py
    cloud.py
    cmdline.py
    crawl.py
    decorators.py
    downloader.py
    engine.py
    feedexport.py
    media_pipelines.py
    redirect.py
    robotstxt.py
  __init__.py
  ignores.txt
  pipelines.py
  spiders.py
  test_addons.py
  test_closespider.py
  test_command_check.py
  test_command_complete.py
  test_command_crawl.py
  test_command_fetch.py
  test_command_genrequest.py
  test_command_genspider.py
  test_command_parse.py
  test_command_runspider.py
  test_command_shell.py
  test_command_startproject.py
  test_command_version.py
  test_commands.py
  test_contracts.py
  test_core_downloader.py
  test_core_scraper.py
  test_crash.py
  test_crawl.py
  test_crawler.py
  … 152 more files
tests_typing/  (3 files)
  test_http_request.mypy-testing
  test_http_response.mypy-testing
  test_spiders.mypy-testing
.git-blame-ignore-revs
.gitattributes
.gitignore
.pre-commit-config.yaml
.readthedocs.yml
AGENTS.md
AUTHORS
CITATION.cff
CODE_OF_CONDUCT.md
CONTRIBUTING.md
INSTALL.md
LICENSE
NEWS
README.rst
SECURITY.md
codecov.yml
conftest.py
pyproject.toml
tox.ini
```

## Entry points

- [extras/github-release-notes.py:31](https://github.com/scrapy/scrapy/blob/e63a574c767d7a9438c21db158f605f1c44c6e6a/extras/github-release-notes.py#L31)
- [extras/pre-bump.py:56](https://github.com/scrapy/scrapy/blob/e63a574c767d7a9438c21db158f605f1c44c6e6a/extras/pre-bump.py#L56)
- [extras/upgrade-ci-pins.py:185](https://github.com/scrapy/scrapy/blob/e63a574c767d7a9438c21db158f605f1c44c6e6a/extras/upgrade-ci-pins.py#L185)
- [scrapy/__main__.py:4](https://github.com/scrapy/scrapy/blob/e63a574c767d7a9438c21db158f605f1c44c6e6a/scrapy/__main__.py#L4)
- [scrapy/cmdline.py](https://github.com/scrapy/scrapy/blob/e63a574c767d7a9438c21db158f605f1c44c6e6a/scrapy/cmdline.py)
- [scrapy/utils/_benchserver.py:55](https://github.com/scrapy/scrapy/blob/e63a574c767d7a9438c21db158f605f1c44c6e6a/scrapy/utils/_benchserver.py#L55)
- [scrapy/utils/benchserver.py:19](https://github.com/scrapy/scrapy/blob/e63a574c767d7a9438c21db158f605f1c44c6e6a/scrapy/utils/benchserver.py#L19)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 14 file(s) under api layer (observed from repository paths and static analysis). Observed top-level classes: AioftpDownloadHandler, AiohttpDownloadHandler, BaseDownloadHandler, BaseHttpDownloadHandler, BaseStream… |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: BaseSettings, Command, Settings, SettingsAttribute. Observed top-level functions: __g… |
| Application entry point | entrypoint | Observed | Groups 7 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Root, ScrapyArgumentParser. Observed top-level functions: _build_parser, _deps, _get_comma… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| extras package | library | Observed | Groups 3 file(s) under extras package (observed from repository paths and static analysis). Observed top-level classes: QPSSpider, Root. |
| scrapy package | library | Observed | Groups 166 file(s) under scrapy package (observed from repository paths and static analysis). Observed top-level classes: AddonManager, AsyncCrawlerProcess, AsyncCrawlerRunner, AsyncioLoopingCall, AutoThrottle, BaseDupe… |
| Service / domain layer | service | Observed | Groups 14 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: BaseScheduler, BaseSchedulerMeta, BrowserLikeContextFactory, Downloader, DownloaderMiddlew… |
| Tests | test | Observed | Groups 366 file(s) under tests (observed from repository paths and static analysis). Observed application object created via Command. Observed routes: PATCH scrapy.commands.check.ContractsManager, PATCH scrapy.commands.… |

## Important files

- `.github/dependabot.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/close-spam-prs.yml` (ci)
- `.github/workflows/codspeed-walltime.yml` (ci)
- `.github/workflows/codspeed.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.github/workflows/tests-vcs-deps.yml` (ci)
- `.github/workflows/upgrade-ci-pins.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `.readthedocs.yml` (config)
- `codecov.yml` (config)
- `pyproject.toml` (manifest)
- `scrapy/templates/project/scrapy.cfg` (config)
- `tox.ini` (config)

## Top-level layout

- `tests` — 361 analysed file(s)
- `scrapy` — 213 analysed file(s)
- `docs` — 72 analysed file(s)
- `sep` — 21 analysed file(s)
- `(root files)` — 19 analysed file(s)
- `.github` — 12 analysed file(s)
- `extras` — 7 analysed file(s)
- `tests_typing` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 5 file(s) were skipped during inventory (5 x likely secret file excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `e63a574c767d7a9438c21db158f605f1c44c6e6a` is the revision these paths and observations refer to.
