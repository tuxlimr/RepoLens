# Project structure: psf/requests

**Analysed commit:** `3c7baaa05ab4aa49cc819ce3a819d260de19c157`

**Commit reference:** [3c7baaa05ab4aa49cc819ce3a819d260de19c157](https://github.com/psf/requests/commit/3c7baaa05ab4aa49cc819ce3a819d260de19c157)

**Tree at this commit:** [psf/requests@3c7baaa05ab4](https://github.com/psf/requests/tree/3c7baaa05ab4aa49cc819ce3a819d260de19c157)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | psf/requests |
| Description | A simple, yet elegant, HTTP library. |
| Stars | 54700 |
| Forks | 10778 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `3c7baaa05ab4aa49cc819ce3a819d260de19c157` |
| Retrieved at | 2026-11-14T19:06:29.576577+00:00 |
| Files in this snapshot | 114 |

## Directory tree

```text
.github/  (19 files)
  ISSUE_TEMPLATE/  (3 files)
    Bug_report.md
    Custom.md
    Feature_request.md
  workflows/  (8 files)
    close-issues.yml
    codeql-analysis.yml
    lint.yml
    lock-issues.yml
    publish.yml
    run-tests.yml
    typecheck.yml
    zizmor.yml
  AI_POLICY.md
  CODEOWNERS
  CODE_OF_CONDUCT.md
  CONTRIBUTING.md
  FUNDING.yml
  ISSUE_TEMPLATE.md
  SECURITY.md
  dependabot.yml
docs/  (25 files)
  _static/  (1 files)
    custom.css
  _templates/  (1 files)
    sidebar.html
  _themes/  (3 files)
    .gitignore
    LICENSE
    flask_theme_support.py
  community/  (7 files)
    faq.rst
    out-there.rst
    recommended.rst
    release-process.rst
    support.rst
    updates.rst
    vulnerabilities.rst
  dev/  (2 files)
    authors.rst
    contributing.rst
  user/  (4 files)
    advanced.rst
    authentication.rst
    install.rst
    quickstart.rst
  .nojekyll
  Makefile
  api.rst
  conf.py
  index.rst
  make.bat
  requirements.txt
ext/  (1 files)
  LICENSE
src/  (20 files)
  requests/  (20 files)
    __init__.py
    __version__.py
    _internal_utils.py
    _types.py
    adapters.py
    api.py
    auth.py
    certs.py
    compat.py
    cookies.py
    exceptions.py
    help.py
    hooks.py
    models.py
    packages.py
    py.typed
    sessions.py
    status_codes.py
    structures.py
    utils.py
tests/  (33 files)
  certs/  (18 files)
    expired/  (9 files)
      … 9 files under this directory
    mtls/  (5 files)
      … 5 files under this directory
    valid/  (3 files)
      … 3 files under this directory
    README.md
  testserver/  (2 files)
    __init__.py
    server.py
  __init__.py
  compat.py
  conftest.py
  test_adapters.py
  test_help.py
  test_hooks.py
  test_lowlevel.py
  test_packages.py
  test_requests.py
  test_structures.py
  test_testserver.py
  test_utils.py
  utils.py
.coveragerc
.git-blame-ignore-revs
.gitignore
.pre-commit-config.yaml
.readthedocs.yaml
AUTHORS.rst
HISTORY.md
LICENSE
MANIFEST.in
Makefile
NOTICE
README.md
pyproject.toml
requirements-dev.txt
setup.py
tox.ini
```

## Entry points

- [src/requests/certs.py:17](https://github.com/psf/requests/blob/3c7baaa05ab4aa49cc819ce3a819d260de19c157/src/requests/certs.py#L17)
- [src/requests/help.py:131](https://github.com/psf/requests/blob/3c7baaa05ab4aa49cc819ce3a819d260de19c157/src/requests/help.py#L131)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: PreparedRequest, Request, RequestEncodingMixin, RequestHooksMixin, Response. |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: _implementation, info, main. |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| requests package | library | Observed | Groups 16 file(s) under requests package (observed from repository paths and static analysis). Observed top-level classes: AuthBase, BaseAdapter, CaseInsensitiveDict, ChunkedEncodingError, ConnectTimeout, ConnectionErro… |
| Tests | test | Observed | Groups 33 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: RedirectSession, Server, TLSServer, TestAddressInNetwork, TestCaseInsensitiveDict, TestContentEncodingDetec… |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/close-issues.yml` (ci)
- `.github/workflows/codeql-analysis.yml` (ci)
- `.github/workflows/lint.yml` (ci)
- `.github/workflows/lock-issues.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.github/workflows/run-tests.yml` (ci)
- `.github/workflows/typecheck.yml` (ci)
- `.github/workflows/zizmor.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `.readthedocs.yaml` (config)
- `MANIFEST.in` (manifest)
- `docs/requirements.txt` (manifest)
- `pyproject.toml` (manifest)
- `requirements-dev.txt` (manifest)
- `setup.py` (manifest)
- `tox.ini` (config)

## Top-level layout

- `tests` — 33 analysed file(s)
- `docs` — 25 analysed file(s)
- `src` — 20 analysed file(s)
- `.github` — 19 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `ext` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 7 file(s) were skipped during inventory (7 x likely secret file excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `3c7baaa05ab4aa49cc819ce3a819d260de19c157` is the revision these paths and observations refer to.
