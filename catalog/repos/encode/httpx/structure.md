# Project structure: encode/httpx

**Analysed commit:** `b5addb64f0161ff6bfe94c124ef76f6a1fba5254`

**Commit reference:** [b5addb64f0161ff6bfe94c124ef76f6a1fba5254](https://github.com/encode/httpx/commit/b5addb64f0161ff6bfe94c124ef76f6a1fba5254)

**Tree at this commit:** [encode/httpx@b5addb64f016](https://github.com/encode/httpx/tree/b5addb64f0161ff6bfe94c124ef76f6a1fba5254)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | encode/httpx |
| Description | A next generation HTTP client for Python. 🦋 |
| Stars | 15788 |
| Forks | 1878 |
| Licence | BSD-3-Clause |
| Language | Python |
| Default branch | master |
| Analysed commit | `b5addb64f0161ff6bfe94c124ef76f6a1fba5254` |
| Retrieved at | 2026-11-14T19:08:59.037446+00:00 |
| Files in this snapshot | 112 |

## Directory tree

```text
.github/  (8 files)
  ISSUE_TEMPLATE/  (2 files)
    1-issue.md
    config.yml
  workflows/  (2 files)
    publish.yml
    test-suite.yml
  CONTRIBUTING.md
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
docs/  (26 files)
  advanced/  (10 files)
    authentication.md
    clients.md
    event-hooks.md
    extensions.md
    proxies.md
    resource-limits.md
    ssl.md
    text-encodings.md
    timeouts.md
    transports.md
  css/  (1 files)
    custom.css
  overrides/  (1 files)
    partials/  (1 files)
      … 1 files under this directory
  CNAME
  api.md
  async.md
  code_of_conduct.md
  compatibility.md
  contributing.md
  environment_variables.md
  exceptions.md
  http2.md
  index.md
  logging.md
  quickstart.md
  third_party_packages.md
  troubleshooting.md
httpx/  (24 files)
  _transports/  (6 files)
    __init__.py
    asgi.py
    base.py
    default.py
    mock.py
    wsgi.py
  __init__.py
  __version__.py
  _api.py
  _auth.py
  _client.py
  _config.py
  _content.py
  _decoders.py
  _exceptions.py
  _main.py
  _models.py
  _multipart.py
  _status_codes.py
  _types.py
  _urlparse.py
  _urls.py
  _utils.py
  py.typed
scripts/  (9 files)
  check
  clean
  coverage
  docs
  install
  lint
  publish
  sync-version
  test
tests/  (38 files)
  client/  (11 files)
    __init__.py
    test_async_client.py
    test_auth.py
    test_client.py
    test_cookies.py
    test_event_hooks.py
    test_headers.py
    test_properties.py
    test_proxies.py
    test_queryparams.py
    test_redirects.py
  fixtures/  (1 files)
    .netrc-nopassword
  models/  (8 files)
    __init__.py
    test_cookies.py
    test_headers.py
    test_queryparams.py
    test_requests.py
    test_responses.py
    test_url.py
    test_whatwg.py
  __init__.py
  common.py
  concurrency.py
  conftest.py
  test_api.py
  test_asgi.py
  test_auth.py
  test_config.py
  test_content.py
  test_decoders.py
  test_exceptions.py
  test_exported_members.py
  test_main.py
  test_multipart.py
  test_status_codes.py
  test_timeouts.py
  test_utils.py
  test_wsgi.py
.gitignore
CHANGELOG.md
LICENSE.md
README.md
mkdocs.yml
pyproject.toml
requirements.txt
```

## Entry points

- [httpx/__init__.py](https://github.com/encode/httpx/blob/b5addb64f0161ff6bfe94c124ef76f6a1fba5254/httpx/__init__.py)
- [httpx/_main.py:452](https://github.com/encode/httpx/blob/b5addb64f0161ff6bfe94c124ef76f6a1fba5254/httpx/_main.py#L452)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: ASGIResponseStream, ASGITransport, WSGIByteStream, WSGITransport. Observed top-level funct… |
| External integrations | external | Observed | Groups 2 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: AsyncClient, BaseClient, BoundAsyncStream, BoundSyncStream, Client, ClientState. Observed to… |
| httpx package | library | Observed | Groups 19 file(s) under httpx package (observed from repository paths and static analysis). Observed top-level classes: AsyncBaseTransport, AsyncByteStream, AsyncHTTPTransport, AsyncIteratorByteStream, AsyncResponseStre… |
| Tests | test | Observed | Groups 39 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: App, ConsumeBodyTransport, DigestApp, RepeatAuth, ResponseBodyAuth, StreamingBody. Observed top-level funct… |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/publish.yml` (ci)
- `.github/workflows/test-suite.yml` (ci)
- `mkdocs.yml` (config)
- `pyproject.toml` (manifest)
- `requirements.txt` (manifest)

## Top-level layout

- `tests` — 38 analysed file(s)
- `docs` — 26 analysed file(s)
- `httpx` — 24 analysed file(s)
- `scripts` — 9 analysed file(s)
- `.github` — 8 analysed file(s)
- `(root files)` — 7 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (1 x likely secret file excluded; 1 x vendored/generated directory excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `b5addb64f0161ff6bfe94c124ef76f6a1fba5254` is the revision these paths and observations refer to.
