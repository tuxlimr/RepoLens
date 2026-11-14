# Project structure: Datalux/Osintgram

**Analysed commit:** `a560498be79a3bf40d7f3b203ad174661b8e81e7`

**Commit reference:** [a560498be79a3bf40d7f3b203ad174661b8e81e7](https://github.com/Datalux/Osintgram/commit/a560498be79a3bf40d7f3b203ad174661b8e81e7)

**Tree at this commit:** [Datalux/Osintgram@a560498be79a](https://github.com/Datalux/Osintgram/tree/a560498be79a3bf40d7f3b203ad174661b8e81e7)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Datalux/Osintgram |
| Description | Osintgram is a OSINT tool on Instagram. It offers an interactive shell to perform analysis on Instagram account of any users by its nickname |
| Stars | 15628 |
| Forks | 3282 |
| Licence | GPL-3.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `a560498be79a3bf40d7f3b203ad174661b8e81e7` |
| Retrieved at | 2026-11-14T19:09:00.137825+00:00 |
| Files in this snapshot | 39 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    tests.yml
config/  (1 files)
  credentials.ini.example
doc/  (2 files)
  CHANGELOG.md
  web-ui.md
scripts/  (2 files)
  instagrapi_login.py
  set_session.py
src/  (12 files)
  web/  (9 files)
    static/  (1 files)
      … 1 files under this directory
    __init__.py
    app.py
    cost.py
    dossier.py
    download.py
    history.py
    request_cache.py
    tools.py
  artwork.py
  instagrapi_backend.py
  osint_service.py
tests/  (10 files)
  conftest.py
  test_app_endpoints.py
  test_cost.py
  test_docs.py
  test_dossier.py
  test_download.py
  test_instagrapi_backend.py
  test_osint_service.py
  test_request_cache.py
  test_token_endpoint.py
.dockerignore
.gitignore
Dockerfile
LICENSE
Makefile
README.md
SECURITY.md
docker-compose.yml
pytest.ini
requirements-dev.txt
requirements.txt
```

## Entry points

- [src/web/app.py:217](https://github.com/Datalux/Osintgram/blob/a560498be79a3bf40d7f3b203ad174661b8e81e7/src/web/app.py#L217)
- [scripts/instagrapi_login.py:56](https://github.com/Datalux/Osintgram/blob/a560498be79a3bf40d7f3b203ad174661b8e81e7/scripts/instagrapi_login.py#L56)
- [scripts/set_session.py:36](https://github.com/Datalux/Osintgram/blob/a560498be79a3bf40d7f3b203ad174661b8e81e7/scripts/set_session.py#L36)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| artwork.py package | library | Observed | Groups 1 file(s) under artwork.py package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 3 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed routes: GET /api/about, GET /api/balance, DELETE /api/cache,… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| instagrapi_backend.py package | library | Observed | Groups 1 file(s) under instagrapi_backend.py package (observed from repository paths and static analysis). Observed top-level classes: InstagrapiBackendError, InstagrapiClient. Observed top-level functions: resolve_inst… |
| Service / domain layer | service | Observed | Groups 1 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: HikerAPIError, OsintServiceError, OsintgramService, PrivateProfileError, QueryCancelledErro… |
| Tests | test | Observed | Groups 10 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: FakeHiker, FakeInstagrapi, SearchClient, _Flaky. Observed top-level functions: _client, _comment_page, _fak… |
| web package | library | Observed | Groups 7 file(s) under web package (observed from repository paths and static analysis). Observed top-level classes: DownloadError, History, PersistentRequestCache. Observed top-level functions: _capped, _coerce_int, _d… |

## Important files

- `.dockerignore` (container)
- `.github/workflows/tests.yml` (ci)
- `Dockerfile` (container)
- `docker-compose.yml` (container)
- `pytest.ini` (config)
- `requirements-dev.txt` (manifest)
- `requirements.txt` (manifest)

## Top-level layout

- `src` — 12 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `tests` — 10 analysed file(s)
- `doc` — 2 analysed file(s)
- `scripts` — 2 analysed file(s)
- `.github` — 1 analysed file(s)
- `config` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `a560498be79a3bf40d7f3b203ad174661b8e81e7` is the revision these paths and observations refer to.
