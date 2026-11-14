# Project structure: tornadoweb/tornado

**Analysed commit:** `48f6645edfd0ae1fc2ef58902c98876f1f5a37b7`

**Commit reference:** [48f6645edfd0ae1fc2ef58902c98876f1f5a37b7](https://github.com/tornadoweb/tornado/commit/48f6645edfd0ae1fc2ef58902c98876f1f5a37b7)

**Tree at this commit:** [tornadoweb/tornado@48f6645edfd0](https://github.com/tornadoweb/tornado/tree/48f6645edfd0ae1fc2ef58902c98876f1f5a37b7)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | tornadoweb/tornado |
| Description | Tornado is a Python web framework and asynchronous networking library, originally developed at FriendFeed. |
| Stars | 22164 |
| Forks | 5607 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `48f6645edfd0ae1fc2ef58902c98876f1f5a37b7` |
| Retrieved at | 2026-11-14T19:07:54.605167+00:00 |
| Files in this snapshot | 330 |

## Directory tree

```text
.github/  (4 files)
  workflows/  (3 files)
    build.yml
    downstream.yml
    test.yml
  zizmor.yml
demos/  (42 files)
  blog/  (16 files)
    static/  (1 files)
      … 1 files under this directory
    templates/  (9 files)
      … 9 files under this directory
    Dockerfile
    README
    blog.py
    docker-compose.yml
    requirements.txt
    schema.sql
  chat/  (5 files)
    static/  (2 files)
      … 2 files under this directory
    templates/  (2 files)
      … 2 files under this directory
    chatdemo.py
  facebook/  (6 files)
    static/  (2 files)
      … 2 files under this directory
    templates/  (2 files)
      … 2 files under this directory
    README
    facebook.py
  file_upload/  (2 files)
    file_receiver.py
    file_uploader.py
  google_auth/  (2 files)
    .gitignore
    main.py
  helloworld/  (1 files)
    helloworld.py
  tcpecho/  (3 files)
    README.md
    client.py
    server.py
  websocket/  (5 files)
    static/  (2 files)
      … 2 files under this directory
    templates/  (2 files)
      … 2 files under this directory
    chatdemo.py
  webspider/  (1 files)
    webspider.py
  README.rst
docs/  (119 files)
  guide/  (8 files)
    async.rst
    coroutines.rst
    intro.rst
    queues.rst
    running.rst
    security.rst
    structure.rst
    templates.rst
  releases/  (69 files)
    v1.0.0.rst
    v1.0.1.rst
    v1.1.0.rst
    v1.1.1.rst
    v1.2.0.rst
    v1.2.1.rst
    v2.0.0.rst
    v2.1.0.rst
    v2.1.1.rst
    v2.2.0.rst
    v2.2.1.rst
    v2.3.0.rst
    v2.4.0.rst
    v2.4.1.rst
    v3.0.0.rst
    v3.0.1.rst
    v3.0.2.rst
    v3.1.0.rst
    v3.1.1.rst
    v3.2.0.rst
    v3.2.1.rst
    v3.2.2.rst
    v4.0.0.rst
    v4.0.1.rst
    … 45 more files
  Makefile
  asyncio.rst
  auth.rst
  autoreload.rst
  caresresolver.rst
  concurrent.rst
  conf.py
  coroutine.rst
  escape.rst
  faq.rst
  gen.rst
  guide.rst
  http.rst
  http1connection.rst
  httpclient.rst
  httpserver.rst
  httputil.rst
  index.rst
  integration.rst
  ioloop.rst
  iostream.rst
  locale.rst
  locks.rst
  log.rst
  … 18 more files
maint/  (54 files)
  benchmark/  (8 files)
    benchmark.py
    chunk_benchmark.py
    ci_benchmark.py
    compare_benchmarks.py
    dos_benchmark.py
    gen_benchmark.py
    parsing_benchmark.py
    template_benchmark.py
  scripts/  (8 files)
    custom_fixers/  (3 files)
      … 3 files under this directory
    pre_tag_checks.py
    run_autopep8.sh
    run_fixers.py
    runcog.sh
    test_resolvers.py
  test/  (23 files)
    cython/  (7 files)
      … 7 files under this directory
    mypy/  (4 files)
      … 4 files under this directory
    redbot/  (3 files)
      … 3 files under this directory
    websocket/  (8 files)
      … 8 files under this directory
    README
  vm/  (13 files)
    freebsd/  (3 files)
      … 3 files under this directory
    ubuntu12.04/  (3 files)
      … 3 files under this directory
    ubuntu14.04/  (3 files)
      … 3 files under this directory
    windows/  (2 files)
      … 2 files under this directory
    README
    shared-setup.sh
  README
  RELEASING.md
tornado/  (93 files)
  platform/  (4 files)
    __init__.py
    asyncio.py
    caresresolver.py
    twisted.py
  test/  (54 files)
    csv_translations/  (1 files)
      … 1 files under this directory
    gettext_translations/  (2 files)
      … 2 files under this directory
    static/  (3 files)
      … 3 files under this directory
    templates/  (1 files)
      … 1 files under this directory
    __init__.py
    __main__.py
    api.txt
    api_test.py
    asyncio_test.py
    auth_test.py
    autoreload_test.py
    circlerefs_test.py
    concurrent_test.py
    curl_httpclient_test.py
    escape_test.py
    gen_test.py
    http1connection_test.py
    httpclient_test.py
    httpserver_test.py
    httputil_test.py
    import_test.py
    ioloop_test.py
    iostream_test.py
    locale_test.py
    locks_test.py
    log_test.py
    netutil_test.py
    options_test.cfg
    … 23 more files
  __init__.py
  __init__.pyi
  _locale_data.py
  auth.py
  autoreload.py
  concurrent.py
  curl_httpclient.py
  escape.py
  gen.py
  http1connection.py
  httpclient.py
  httpserver.py
  httputil.py
  ioloop.py
  iostream.py
  locale.py
  locks.py
  log.py
  netutil.py
  options.py
  process.py
  py.typed
  queues.py
  routing.py
  … 11 more files
.coveragerc
.flake8
.gitattributes
.gitignore
.readthedocs.yaml
CONTRIBUTING.md
LICENSE
MANIFEST.in
README.rst
SECURITY.md
codecov.yml
pyproject.toml
requirements.in
requirements.txt
runtests.sh
setup.cfg
setup.py
tox.ini
```

## Entry points

- [demos/blog/blog.py:331](https://github.com/tornadoweb/tornado/blob/48f6645edfd0ae1fc2ef58902c98876f1f5a37b7/demos/blog/blog.py#L331)
- [demos/chat/chatdemo.py:141](https://github.com/tornadoweb/tornado/blob/48f6645edfd0ae1fc2ef58902c98876f1f5a37b7/demos/chat/chatdemo.py#L141)
- [demos/facebook/facebook.py:112](https://github.com/tornadoweb/tornado/blob/48f6645edfd0ae1fc2ef58902c98876f1f5a37b7/demos/facebook/facebook.py#L112)
- [demos/file_upload/file_receiver.py:58](https://github.com/tornadoweb/tornado/blob/48f6645edfd0ae1fc2ef58902c98876f1f5a37b7/demos/file_upload/file_receiver.py#L58)
- [demos/file_upload/file_uploader.py:100](https://github.com/tornadoweb/tornado/blob/48f6645edfd0ae1fc2ef58902c98876f1f5a37b7/demos/file_upload/file_uploader.py#L100)
- [demos/google_auth/main.py:113](https://github.com/tornadoweb/tornado/blob/48f6645edfd0ae1fc2ef58902c98876f1f5a37b7/demos/google_auth/main.py#L113)
- [demos/helloworld/helloworld.py:38](https://github.com/tornadoweb/tornado/blob/48f6645edfd0ae1fc2ef58902c98876f1f5a37b7/demos/helloworld/helloworld.py#L38)
- [demos/tcpecho/client.py:20](https://github.com/tornadoweb/tornado/blob/48f6645edfd0ae1fc2ef58902c98876f1f5a37b7/demos/tcpecho/client.py#L20)
- [demos/tcpecho/server.py:39](https://github.com/tornadoweb/tornado/blob/48f6645edfd0ae1fc2ef58902c98876f1f5a37b7/demos/tcpecho/server.py#L39)
- [demos/websocket/chatdemo.py:98](https://github.com/tornadoweb/tornado/blob/48f6645edfd0ae1fc2ef58902c98876f1f5a37b7/demos/websocket/chatdemo.py#L98)
- [demos/webspider/webspider.py:97](https://github.com/tornadoweb/tornado/blob/48f6645edfd0ae1fc2ef58902c98876f1f5a37b7/demos/webspider/webspider.py#L97)
- [maint/benchmark/benchmark.py:72](https://github.com/tornadoweb/tornado/blob/48f6645edfd0ae1fc2ef58902c98876f1f5a37b7/maint/benchmark/benchmark.py#L72)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 14 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| demos package | library | Observed | Groups 3 file(s) under demos package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 27 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Application, ArchiveHandler, AsyncHTTPClient, AsyncHTTPSTestCase, AsyncHTTPTestCase, Asyn… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| maint package | library | Observed | Groups 10 file(s) under maint package (observed from repository paths and static analysis). Observed top-level classes: FixFutureImports, FixUnicodeLiteral. Observed top-level functions: is_docstring. |
| Tests | test | Observed | Groups 78 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: APISnapshotTest, AcceptLanguageTest, AllHTTPMethodsTest, AllMethodsHandler, AnyThreadEventLoopPolicyTest, A… |
| tornado package | library | Observed | Groups 30 file(s) under tornado package (observed from repository paths and static analysis). Observed top-level classes: AddThreadSelectorEventLoop, AnyMatches, Application, ArgReplacer, AsyncIOLoop, AsyncIOMainLoop. O… |

## Important files

- `.github/workflows/build.yml` (ci)
- `.github/workflows/downstream.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `.github/zizmor.yml` (config)
- `.readthedocs.yaml` (config)
- `MANIFEST.in` (manifest)
- `codecov.yml` (config)
- `demos/blog/Dockerfile` (container)
- `demos/blog/docker-compose.yml` (container)
- `demos/blog/requirements.txt` (manifest)
- `maint/vm/freebsd/tox.ini` (config)
- `maint/vm/ubuntu12.04/tox.ini` (config)
- `maint/vm/ubuntu14.04/tox.ini` (config)
- `maint/vm/windows/tox.ini` (config)
- `pyproject.toml` (manifest)
- `requirements.txt` (manifest)
- `setup.cfg` (manifest)
- `setup.py` (manifest)
- `tox.ini` (config)

## Top-level layout

- `docs` — 119 analysed file(s)
- `tornado` — 93 analysed file(s)
- `maint` — 54 analysed file(s)
- `demos` — 42 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `.github` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `48f6645edfd0ae1fc2ef58902c98876f1f5a37b7` is the revision these paths and observations refer to.
