# Project structure: postmanlabs/httpbin

**Analysed commit:** `dfe140bc4b988e78ecff77f189abd2fc987f908b`

**Commit reference:** [dfe140bc4b988e78ecff77f189abd2fc987f908b](https://github.com/postmanlabs/httpbin/commit/dfe140bc4b988e78ecff77f189abd2fc987f908b)

**Tree at this commit:** [postmanlabs/httpbin@dfe140bc4b98](https://github.com/postmanlabs/httpbin/tree/dfe140bc4b988e78ecff77f189abd2fc987f908b)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | postmanlabs/httpbin |
| Description | HTTP Request & Response Service, written in Python + Flask. |
| Stars | 13636 |
| Forks | 1923 |
| Licence | ISC |
| Language | Python |
| Default branch | master |
| Analysed commit | `dfe140bc4b988e78ecff77f189abd2fc987f908b` |
| Retrieved at | 2026-11-14T19:09:46.201879+00:00 |
| Files in this snapshot | 42 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    test.yml
httpbin/  (24 files)
  static/  (6 files)
    swagger-ui/  (6 files)
      … 6 files under this directory
  templates/  (10 files)
    flasgger/  (1 files)
      … 1 files under this directory
    images/  (1 files)
      … 1 files under this directory
    UTF-8-demo.txt
    footer.html
    forms-post.html
    httpbin.1.html
    index.html
    moby.html
    sample.xml
    trackingscripts.html
  VERSION
  __init__.py
  core.py
  filters.py
  helpers.py
  redirect_targets.py
  structures.py
  utils.py
.dockerignore
.gitignore
AUTHORS
Dockerfile
LICENSE
MANIFEST.in
Procfile
README.md
app.json
docker-compose.yml
now.json
pyproject.toml
requirements-test.txt
requirements.txt
runtime.txt
test_httpbin.py
tox.ini
```

## Entry points

- [httpbin/core.py:116](https://github.com/postmanlabs/httpbin/blob/dfe140bc4b988e78ecff77f189abd2fc987f908b/httpbin/core.py#L116)
- [httpbin/filters.py:31](https://github.com/postmanlabs/httpbin/blob/dfe140bc4b988e78ecff77f189abd2fc987f908b/httpbin/filters.py#L31)
- [test_httpbin.py:1677](https://github.com/postmanlabs/httpbin/blob/dfe140bc4b988e78ecff77f189abd2fc987f908b/test_httpbin.py#L1677)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 9 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Flask. Observed routes: ROUTE /legacy, ROUTE /html, ROUTE /robots.txt, ROUTE /… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| httpbin package | library | Observed | Groups 5 file(s) under httpbin package (observed from repository paths and static analysis). Observed top-level classes: CaseInsensitiveDict. Observed top-level functions: H, HA1, HA2, __parse_request_range, _quality, a… |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: HttpbinTestCase, TargetClient, TargetResponse. Observed top-level functions: _hash, _make_digest_auth_header… |

## Important files

- `.dockerignore` (container)
- `.github/workflows/test.yml` (ci)
- `Dockerfile` (container)
- `MANIFEST.in` (manifest)
- `app.json` (config)
- `docker-compose.yml` (container)
- `now.json` (config)
- `pyproject.toml` (manifest)
- `requirements-test.txt` (manifest)
- `requirements.txt` (manifest)
- `tox.ini` (config)

## Top-level layout

- `httpbin` — 24 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `dfe140bc4b988e78ecff77f189abd2fc987f908b` is the revision these paths and observations refer to.
