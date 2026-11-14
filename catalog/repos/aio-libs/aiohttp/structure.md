# Project structure: aio-libs/aiohttp

**Analysed commit:** `fe099491d275ef2c21bf683e024e34d51ac05d43`

**Commit reference:** [fe099491d275ef2c21bf683e024e34d51ac05d43](https://github.com/aio-libs/aiohttp/commit/fe099491d275ef2c21bf683e024e34d51ac05d43)

**Tree at this commit:** [aio-libs/aiohttp@fe099491d275](https://github.com/aio-libs/aiohttp/tree/fe099491d275ef2c21bf683e024e34d51ac05d43)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | aio-libs/aiohttp |
| Description | Asynchronous HTTP client/server framework for asyncio and Python |
| Stars | 16607 |
| Forks | 2524 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `fe099491d275ef2c21bf683e024e34d51ac05d43` |
| Retrieved at | 2026-11-14T19:08:44.946563+00:00 |
| Files in this snapshot | 502 |

## Directory tree

```text
.claude/  (1 files)
  skills/  (1 files)
    backport-failed/  (1 files)
      … 1 files under this directory
.github/  (21 files)
  ISSUE_TEMPLATE/  (3 files)
    bug-report.yml
    config.yml
    feature-request.yml
  workflows/  (10 files)
    actions.lock
    agent-scan.yml
    auto-merge.yml
    ci-cd.yml
    codeql.yml
    dependency-submission.yml
    label-remove.yml
    labels.yml
    reusable-cibuildwheel.yml
    stale.yml
  CODEOWNERS
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
  codeql.yml
  config.yml
  dependabot.yml
  egress-firewall.yaml
  lock.yml
CHANGES/  (174 files)
  .TEMPLATE.rst
  .gitignore
  10468.doc.rst
  10549.misc.rst
  10611.bugfix.rst
  10762.breaking.rst
  10890.misc.rst
  11012.breaking.rst
  11268.feature.rst
  11776.misc.rst
  11876.misc.rst
  12088.bugfix.rst
  12111.breaking.rst
  12296.bugfix.rst
  12425.misc.rst
  12501.breaking.rst
  12540.bugfix.rst
  12561.misc.rst
  12573.contrib.rst
  12580.contrib.rst
  12584.contrib.rst
  12588.contrib.rst
  12596.contrib.rst
  12600.contrib.rst
  … 150 more files
aiohttp/  (61 files)
  _websocket/  (9 files)
    __init__.py
    helpers.py
    mask.pxd
    mask.pyx
    models.py
    reader.py
    reader_c.pxd
    reader_py.py
    writer.py
  __init__.py
  _cookie_helpers.py
  _cparser.pxd
  _find_header.h
  _find_header.pxd
  _http_parser.pyx
  _http_writer.pyx
  abc.py
  base_protocol.py
  client.py
  client_exceptions.py
  client_middleware_digest_auth.py
  client_middlewares.py
  client_proto.py
  client_reqrep.py
  client_ws.py
  compression_utils.py
  connector.py
  cookiejar.py
  formdata.py
  hdrs.py
  helpers.py
  http.py
  http_exceptions.py
  … 28 more files
docs/  (53 files)
  _static/  (5 files)
    css/  (1 files)
      … 1 files under this directory
    img/  (4 files)
      … 4 files under this directory
  code/  (1 files)
    client_middleware_cookbook.py
  Makefile
  abc.rst
  aiohttp-icon.svg
  aiohttp-plain.svg
  built_with.rst
  changes.rst
  client.rst
  client_advanced.rst
  client_middleware_cookbook.rst
  client_quickstart.rst
  client_reference.rst
  conf.py
  contributing-admins.rst
  contributing.rst
  deployment.rst
  essays.rst
  external.rst
  faq.rst
  glossary.rst
  http_request_lifecycle.rst
  index.rst
  logging.rst
  make.bat
  migration_to_2xx.rst
  … 23 more files
examples/  (26 files)
  background_tasks.py
  basic_auth_middleware.py
  cli_app.py
  client_auth.py
  client_json.py
  client_ws.py
  combined_middleware.py
  curl.py
  digest_auth_qop_auth.py
  fake_server.py
  logging_middleware.py
  lowlevel_srv.py
  retry_middleware.py
  server.crt
  server.csr
  server_simple.py
  static_files.py
  token_refresh_middleware.py
  web_classview.py
  web_cookies.py
  web_rewrite_headers_middleware.py
  web_srv.py
  web_srv_route_deco.py
  web_srv_route_table.py
  … 2 more files
fuzzers/  (7 files)
  http_parser.py
  http_payload_parser.py
  multipart.py
  no_extensions.txt
  payload_url.py
  set_cookie.py
  web_request.py
requirements/  (31 files)
  base-ft.in
  base-ft.txt
  base.in
  base.txt
  constraints.in
  constraints.txt
  cython.in
  cython.txt
  dev.in
  dev.txt
  doc-spelling.in
  doc-spelling.txt
  doc.in
  doc.txt
  lint.in
  lint.txt
  multidict.in
  multidict.txt
  runtime-deps.in
  runtime-deps.txt
  sync-direct-runtime-deps.py
  test-common-base.in
  test-common-base.txt
  test-common.in
  … 7 more files
tests/  (90 files)
  autobahn/  (7 files)
    client/  (2 files)
      … 2 files under this directory
    server/  (2 files)
      … 2 files under this directory
    Dockerfile.aiohttp
    Dockerfile.autobahn
    test_autobahn.py
  isolated/  (2 files)
    check_for_client_response_leak.py
    check_for_request_leak.py
  conftest.py
  data.unknown_mime_type
  data.zero_bytes
  github-urls.json
  sample.txt
  test_base_protocol.py
  test_benchmarks_client.py
  test_benchmarks_client_request.py
  test_benchmarks_client_response.py
  test_benchmarks_client_ws.py
  test_benchmarks_cookie_helpers.py
  test_benchmarks_cookiejar.py
  test_benchmarks_helpers.py
  test_benchmarks_http_websocket.py
  test_benchmarks_http_writer.py
  test_benchmarks_multipart.py
  test_benchmarks_web_fileresponse.py
  test_benchmarks_web_middleware.py
  test_benchmarks_web_request.py
  test_benchmarks_web_response.py
  test_benchmarks_web_urldispatcher.py
  test_circular_imports.py
  test_classbasedview.py
  test_client_connection.py
  … 57 more files
tools/  (9 files)
  testing/  (3 files)
    Dockerfile
    Dockerfile.dockerignore
    entrypoint.sh
  bench-asyncio-write.py
  check_changes.py
  check_sum.py
  cleanup_changes.py
  drop_merged_branches.sh
  gen.py
.cherry_picker.toml
.codecov.yml
.coveragerc-cython.toml
.coveragerc.toml
.editorconfig
.git-blame-ignore-revs
.gitattributes
.gitignore
.gitmodules
.lgtm.yml
.mypy.ini
.pip-tools.toml
.pre-commit-config.yaml
.readthedocs.yml
AGENTS.md
CLAUDE.md
CODE_OF_CONDUCT.md
CONTRIBUTING.rst
CONTRIBUTORS.txt
LICENSE.txt
MANIFEST.in
Makefile
README.rst
SECURITY_EXTRA.md
… 5 more files
```

## Entry points

- [aiohttp/web.py:578](https://github.com/aio-libs/aiohttp/blob/fe099491d275ef2c21bf683e024e34d51ac05d43/aiohttp/web.py#L578)
- [fuzzers/http_parser.py:41](https://github.com/aio-libs/aiohttp/blob/fe099491d275ef2c21bf683e024e34d51ac05d43/fuzzers/http_parser.py#L41)
- [fuzzers/http_payload_parser.py:42](https://github.com/aio-libs/aiohttp/blob/fe099491d275ef2c21bf683e024e34d51ac05d43/fuzzers/http_payload_parser.py#L42)
- [fuzzers/multipart.py:67](https://github.com/aio-libs/aiohttp/blob/fe099491d275ef2c21bf683e024e34d51ac05d43/fuzzers/multipart.py#L67)
- [fuzzers/payload_url.py:39](https://github.com/aio-libs/aiohttp/blob/fe099491d275ef2c21bf683e024e34d51ac05d43/fuzzers/payload_url.py#L39)
- [fuzzers/set_cookie.py:49](https://github.com/aio-libs/aiohttp/blob/fe099491d275ef2c21bf683e024e34d51ac05d43/fuzzers/set_cookie.py#L49)
- [fuzzers/web_request.py:54](https://github.com/aio-libs/aiohttp/blob/fe099491d275ef2c21bf683e024e34d51ac05d43/fuzzers/web_request.py#L54)
- [tools/check_changes.py:58](https://github.com/aio-libs/aiohttp/blob/fe099491d275ef2c21bf683e024e34d51ac05d43/tools/check_changes.py#L58)
- [tools/check_sum.py:49](https://github.com/aio-libs/aiohttp/blob/fe099491d275ef2c21bf683e024e34d51ac05d43/tools/check_sum.py#L49)
- [tools/cleanup_changes.py:44](https://github.com/aio-libs/aiohttp/blob/fe099491d275ef2c21bf683e024e34d51ac05d43/tools/cleanup_changes.py#L44)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| aiohttp package | library | Observed | Groups 49 file(s) under aiohttp package (observed from repository paths and static analysis). Observed top-level classes: AbstractAccessLogger, AbstractAsyncAccessLogger, AbstractCookieJar, AbstractMatchInfo, AbstractRe… |
| Configuration and deployment | config | Observed | Groups 9 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: ParallelBuildExt. |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: WSCloseCode, WSHandshakeError, WSMessageBinary, WSMessageClose, WSMessageClosed, WSMessageClosing. |
| Application entry point | entrypoint | Observed | Groups 10 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: FuzzStream. Observed top-level functions: TestOneInput, _cancel_tasks, _run_app, fuzz_bod… |
| External integrations | external | Observed | Groups 1 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: ClientSession, _BaseRequestContextManager, _RequestOptions, _SessionOptions, _SessionRequest… |
| requirements package | library | Observed | Groups 1 file(s) under requirements package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 89 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH aiohttp.connector.ClientRequestBase, PATCH aiohttp.connector.aiohappyeyeballs.start_connection, PATCH aiohttp.co… |
| tools package | library | Observed | Groups 4 file(s) under tools package (observed from repository paths and static analysis). Observed top-level functions: _job, build, calc_headers, factory, fm_size, fm_time. |

## Important files

- `.cherry_picker.toml` (config)
- `.codecov.yml` (config)
- `.coveragerc-cython.toml` (config)
- `.coveragerc.toml` (config)
- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/bug-report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature-request.yml` (config)
- `.github/codeql.yml` (config)
- `.github/config.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/egress-firewall.yaml` (config)
- `.github/lock.yml` (config)
- `.github/workflows/actions.lock` (ci)
- `.github/workflows/agent-scan.yml` (ci)
- `.github/workflows/auto-merge.yml` (ci)
- `.github/workflows/ci-cd.yml` (ci)
- `.github/workflows/codeql.yml` (ci)
- `.github/workflows/dependency-submission.yml` (ci)
- `.github/workflows/label-remove.yml` (ci)
- `.github/workflows/labels.yml` (ci)
- `.github/workflows/reusable-cibuildwheel.yml` (ci)
- `.github/workflows/stale.yml` (ci)
- `.lgtm.yml` (config)
- `.mypy.ini` (config)
- `.pip-tools.toml` (config)
- `.pre-commit-config.yaml` (config)
- `.readthedocs.yml` (config)
- `MANIFEST.in` (manifest)
- `pyproject.toml` (manifest)
- `pytest.ini` (config)
- `setup.cfg` (manifest)
- `setup.py` (manifest)
- `tests/autobahn/Dockerfile.aiohttp` (container)
- `tests/autobahn/Dockerfile.autobahn` (container)
- `tools/testing/Dockerfile` (container)
- `tools/testing/Dockerfile.dockerignore` (container)

## Top-level layout

- `CHANGES` — 174 analysed file(s)
- `tests` — 90 analysed file(s)
- `aiohttp` — 61 analysed file(s)
- `docs` — 53 analysed file(s)
- `requirements` — 31 analysed file(s)
- `(root files)` — 29 analysed file(s)
- `examples` — 26 analysed file(s)
- `.github` — 21 analysed file(s)
- `tools` — 9 analysed file(s)
- `fuzzers` — 7 analysed file(s)
- `.claude` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (1 x likely secret file excluded; 1 x vendored/generated directory excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `fe099491d275ef2c21bf683e024e34d51ac05d43` is the revision these paths and observations refer to.
