# Project structure: Kludex/starlette

**Analysed commit:** `271c277da0ff64e2048a4d46ecc812b9d61db5f6`

**Commit reference:** [271c277da0ff64e2048a4d46ecc812b9d61db5f6](https://github.com/Kludex/starlette/commit/271c277da0ff64e2048a4d46ecc812b9d61db5f6)

**Tree at this commit:** [Kludex/starlette@271c277da0ff](https://github.com/Kludex/starlette/tree/271c277da0ff64e2048a4d46ecc812b9d61db5f6)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Kludex/starlette |
| Description | The little ASGI framework that shines. 🌟 |
| Stars | 12720 |
| Forks | 1445 |
| Licence | BSD-3-Clause |
| Language | Python |
| Default branch | main |
| Analysed commit | `271c277da0ff64e2048a4d46ecc812b9d61db5f6` |
| Retrieved at | 2026-11-14T19:10:01.546116+00:00 |
| Files in this snapshot | 145 |

## Directory tree

```text
.github/  (9 files)
  ISSUE_TEMPLATE/  (2 files)
    1-issue.md
    config.yml
  workflows/  (4 files)
    benchmark.yml
    main.yml
    publish.yml
    zizmor.yml
  FUNDING.yml
  dependabot.yml
  pull_request_template.md
benchmarks/  (14 files)
  README.md
  __init__.py
  _utils.py
  conftest.py
  file_response_benchmark.py
  gzip_benchmark.py
  json_benchmark.py
  multipart_benchmark.py
  request_benchmark.py
  response_benchmark.py
  routing_benchmark.py
  streaming_response_benchmark.py
  urlencoded_benchmark.py
  websocket_benchmark.py
docs/  (32 files)
  css/  (1 files)
    custom.css
  img/  (2 files)
    starlette.svg
    starlette_dark.svg
  overrides/  (3 files)
    partials/  (2 files)
      … 2 files under this directory
    main.html
  CNAME
  applications.md
  authentication.md
  background.md
  config.md
  contributing.md
  database.md
  early-hints.md
  endpoints.md
  exceptions.md
  graphql.md
  index.md
  lifespan.md
  middleware.md
  release-notes.md
  requests.md
  responses.md
  routing.md
  schemas.md
  server-push.md
  staticfiles.md
  templates.md
  testclient.md
  third-party-packages.md
  … 2 more files
scripts/  (8 files)
  README.md
  check
  coverage
  docs
  install
  lint
  sync-version
  test
starlette/  (37 files)
  middleware/  (13 files)
    __init__.py
    authentication.py
    base.py
    body_limit.py
    cors.py
    errors.py
    exceptions.py
    gzip.py
    httpsredirect.py
    opentelemetry.py
    sessions.py
    trustedhost.py
    wsgi.py
  __init__.py
  _exception_handler.py
  _utils.py
  applications.py
  authentication.py
  background.py
  concurrency.py
  config.py
  convertors.py
  datastructures.py
  endpoints.py
  exceptions.py
  formparsers.py
  py.typed
  requests.py
  responses.py
  routing.py
  schemas.py
  staticfiles.py
  status.py
  templating.py
  testclient.py
  types.py
  websockets.py
tests/  (36 files)
  middleware/  (12 files)
    __init__.py
    test_base.py
    test_body_limit.py
    test_cors.py
    test_errors.py
    test_gzip.py
    test_https_redirect.py
    test_middleware.py
    test_opentelemetry.py
    test_session.py
    test_trusted_host.py
    test_wsgi.py
  statics/  (1 files)
    example.txt
  __init__.py
  conftest.py
  test__utils.py
  test_applications.py
  test_authentication.py
  test_background.py
  test_concurrency.py
  test_config.py
  test_convertors.py
  test_datastructures.py
  test_endpoints.py
  test_exceptions.py
  test_formparsers.py
  test_requests.py
  test_responses.py
  test_routing.py
  test_schemas.py
  test_staticfiles.py
  test_status.py
  test_templates.py
  test_testclient.py
  test_websockets.py
  types.py
.gitignore
AGENTS.md
AI_POLICY.md
CITATION.cff
LICENSE.md
README.md
mkdocs.yml
pyproject.toml
wrangler.toml
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| benchmarks package | library | Observed | Groups 12 file(s) under benchmarks package (observed from repository paths and static analysis). Observed top-level classes: ASGIRunner, BenchmarkCase, BodyApp, BypassCase, BytesEchoApp, ChunkedReceive. Observed top-lev… |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: Config, Environ, EnvironError, undefined. |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: BaseSchemaGenerator, EndpointInfo, OpenAPIResponse, SchemaGenerator. |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: WSGIMiddleware, WSGIResponder. Observed top-level functions: build_environ. |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| starlette package | library | Observed | Groups 33 file(s) under starlette package (observed from repository paths and static analysis). Observed top-level classes: Address, AuthCredentials, AuthenticationBackend, AuthenticationError, AuthenticationMiddleware,… |
| Tests | test | Observed | Groups 38 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: AddHeadersMiddleware, BadBodyException, BasicAuth, CustomMiddleware, CustomMiddlewareUsingBaseHTTPMiddlewar… |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/benchmark.yml` (ci)
- `.github/workflows/main.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.github/workflows/zizmor.yml` (ci)
- `mkdocs.yml` (config)
- `pyproject.toml` (manifest)
- `wrangler.toml` (config)

## Top-level layout

- `starlette` — 37 analysed file(s)
- `tests` — 36 analysed file(s)
- `docs` — 32 analysed file(s)
- `benchmarks` — 14 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `.github` — 9 analysed file(s)
- `scripts` — 8 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `271c277da0ff64e2048a4d46ecc812b9d61db5f6` is the revision these paths and observations refer to.
