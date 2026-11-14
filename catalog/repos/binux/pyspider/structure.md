# Project structure: binux/pyspider

**Analysed commit:** `897891cafb21ea5b4ac08e728ad2ea212879f7fa`

**Commit reference:** [897891cafb21ea5b4ac08e728ad2ea212879f7fa](https://github.com/binux/pyspider/commit/897891cafb21ea5b4ac08e728ad2ea212879f7fa)

**Tree at this commit:** [binux/pyspider@897891cafb21](https://github.com/binux/pyspider/tree/897891cafb21ea5b4ac08e728ad2ea212879f7fa)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | binux/pyspider |
| Description | A Powerful Spider(Web Crawler) System in Python. |
| Stars | 16744 |
| Forks | 3610 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `897891cafb21ea5b4ac08e728ad2ea212879f7fa` |
| Retrieved at | 2026-11-14T19:08:43.906149+00:00 |
| Files in this snapshot | 166 |

## Directory tree

```text
.github/  (1 files)
  ISSUE_TEMPLATE.md
data/  (1 files)
  .gitignore
docs/  (23 files)
  apis/  (6 files)
    @catch_status_code_error.md
    @every.md
    Response.md
    index.md
    self.crawl.md
    self.send_message.md
  tutorial/  (4 files)
    AJAX-and-more-HTTP.md
    HTML-and-CSS-Selector.md
    Render-with-PhantomJS.md
    index.md
  About-Projects.md
  About-Tasks.md
  Architecture.md
  Command-Line.md
  Deployment-demo.pyspider.org.md
  Deployment.md
  Frequently-Asked-Questions.md
  Quickstart.md
  Running-pyspider-with-Docker.md
  Script-Environment.md
  Working-with-Results.md
  conf.py
  index.md
pyspider/  (103 files)
  database/  (39 files)
    base/  (4 files)
      … 4 files under this directory
    couchdb/  (5 files)
      … 5 files under this directory
    elasticsearch/  (4 files)
      … 4 files under this directory
    local/  (2 files)
      … 2 files under this directory
    mongodb/  (5 files)
      … 5 files under this directory
    mysql/  (5 files)
      … 5 files under this directory
    redis/  (2 files)
      … 2 files under this directory
    sqlalchemy/  (5 files)
      … 5 files under this directory
    sqlite/  (5 files)
      … 5 files under this directory
    __init__.py
    basedb.py
  fetcher/  (6 files)
    __init__.py
    cookie_utils.py
    phantomjs_fetcher.js
    puppeteer_fetcher.js
    splash_fetcher.lua
    tornado_fetcher.py
  libs/  (15 files)
    ListIO.py
    __init__.py
    base_handler.py
    bench.py
    counter.py
    dataurl.py
    log.py
    multiprocessing_queue.py
    pprint.py
    response.py
    result_dump.py
    sample_handler.py
    url.py
    utils.py
    wsgi_xmlrpc.py
  message_queue/  (4 files)
    __init__.py
    kombu_queue.py
    rabbitmq.py
    redis_queue.py
  processor/  (3 files)
    __init__.py
    processor.py
    project_module.py
  result/  (2 files)
    __init__.py
    result_worker.py
  scheduler/  (4 files)
    __init__.py
    scheduler.py
    task_queue.py
    token_bucket.py
  webui/  (27 files)
    static/  (13 files)
      … 13 files under this directory
    templates/  (5 files)
      … 5 files under this directory
    __init__.py
    app.py
    bench_test.py
    debug.py
    index.py
    login.py
    result.py
    task.py
    webdav.py
  __init__.py
  logging.conf
  run.py
tests/  (23 files)
  __init__.py
  data_fetcher_processor_handler.py
  data_handler.py
  data_sample_handler.py
  data_test_webpage.py
  test_base_handler.py
  test_bench.py
  test_counter.py
  test_database.py
  test_fetcher.py
  test_fetcher_processor.py
  test_message_queue.py
  test_processor.py
  test_response.py
  test_result_dump.py
  test_result_worker.py
  test_run.py
  test_scheduler.py
  test_task_queue.py
  test_utils.py
  test_webdav.py
  test_webui.py
  test_xmlrpc.py
tools/  (1 files)
  migrate.py
.coveragerc
.gitignore
.travis.yml
Dockerfile
LICENSE
MANIFEST.in
README.md
config_example.json
docker-compose.yaml
mkdocs.yml
requirements.txt
run.py
setup.py
tox.ini
```

## Entry points

- [pyspider/database/basedb.py:135](https://github.com/binux/pyspider/blob/897891cafb21ea5b4ac08e728ad2ea212879f7fa/pyspider/database/basedb.py#L135)
- [pyspider/libs/pprint.py:377](https://github.com/binux/pyspider/blob/897891cafb21ea5b4ac08e728ad2ea212879f7fa/pyspider/libs/pprint.py#L377)
- [pyspider/run.py](https://github.com/binux/pyspider/blob/897891cafb21ea5b4ac08e728ad2ea212879f7fa/pyspider/run.py)
- [pyspider/scheduler/task_queue.py:289](https://github.com/binux/pyspider/blob/897891cafb21ea5b4ac08e728ad2ea212879f7fa/pyspider/scheduler/task_queue.py#L289)
- [run.py:10](https://github.com/binux/pyspider/blob/897891cafb21ea5b4ac08e728ad2ea212879f7fa/run.py#L10)
- [tools/migrate.py:43](https://github.com/binux/pyspider/blob/897891cafb21ea5b4ac08e728ad2ea212879f7fa/tools/migrate.py#L43)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 4 file(s) under api layer (observed from repository paths and static analysis). Observed routes: ROUTE /debug/<project>, ROUTE /debug/<project>/run, ROUTE /debug/<project>/save, ROUTE /debug/<project>/get, ROUTE… |
| Configuration and deployment | config | Observed | Groups 9 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 38 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: MySQLMixin, ProjectDB, ResultDB, SQLiteMixin, SplitTableMixin, TaskDB. Observed top-level functions: _… |
| Application entry point | entrypoint | Observed | Groups 7 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: AtomInt, BaseDB, InQueueTask, PrettyPrinter, PriorityTaskQueue, QuitableFlask. Observed to… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| pyspider package | library | Observed | Groups 40 file(s) under pyspider package (observed from repository paths and static analysis). Observed top-level classes: AmqpQueue, AnonymousUser, AverageWindowCounter, BaseCounter, BaseHandler, BaseHandlerMeta. Obser… |
| Tests | test | Observed | Groups 24 file(s) under tests (observed from repository paths and static analysis). Observed routes: ROUTE /bench, ROUTE /pyspider/test.html, ROUTE /pyspider/ajax.html, ROUTE /pyspider/ajax_click.html. Observed top-leve… |

## Important files

- `.travis.yml` (ci)
- `Dockerfile` (container)
- `MANIFEST.in` (manifest)
- `config_example.json` (config)
- `docker-compose.yaml` (container)
- `mkdocs.yml` (config)
- `pyspider/webui/static/package.json` (manifest)
- `requirements.txt` (manifest)
- `setup.py` (manifest)
- `tox.ini` (config)

## Top-level layout

- `pyspider` — 103 analysed file(s)
- `docs` — 23 analysed file(s)
- `tests` — 23 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `.github` — 1 analysed file(s)
- `data` — 1 analysed file(s)
- `tools` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 5 file(s) were skipped during inventory (5 x generated/minified file excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- The GitHub repository was marked archived at selection time.

Commit `897891cafb21ea5b4ac08e728ad2ea212879f7fa` is the revision these paths and observations refer to.
