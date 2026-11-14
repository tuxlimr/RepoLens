# Project structure: sherlock-project/sherlock

**Analysed commit:** `c588d7c8b476df9f9c84912a05d1430fb8cdcdae`

**Commit reference:** [c588d7c8b476df9f9c84912a05d1430fb8cdcdae](https://github.com/sherlock-project/sherlock/commit/c588d7c8b476df9f9c84912a05d1430fb8cdcdae)

**Tree at this commit:** [sherlock-project/sherlock@c588d7c8b476](https://github.com/sherlock-project/sherlock/tree/c588d7c8b476df9f9c84912a05d1430fb8cdcdae)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | sherlock-project/sherlock |
| Description | Hunt down social media accounts by username across social networks |
| Stars | 111684 |
| Forks | 12924 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `c588d7c8b476df9f9c84912a05d1430fb8cdcdae` |
| Retrieved at | 2026-11-14T19:06:07.117618+00:00 |
| Files in this snapshot | 51 |

## Directory tree

```text
.actor/  (6 files)
  Dockerfile
  README.md
  actor.json
  actor.sh
  dataset_schema.json
  input_schema.json
.github/  (13 files)
  ISSUE_TEMPLATE/  (6 files)
    bug-report.yml
    config.yml
    false-negative.yml
    false-positive.yml
    feature-request.yml
    site-request.yml
  workflows/  (4 files)
    exclusions.yml
    regression.yml
    update-site-list.yml
    validate_modified_targets.yml
  CODEOWNERS
  FUNDING.yml
  SECURITY.md
devel/  (2 files)
  site-list.py
  summarize_site_validation.py
docs/  (4 files)
  pyproject/  (1 files)
    README.md
  CODE_OF_CONDUCT.md
  README.md
  removed-sites.md
sherlock_project/  (9 files)
  resources/  (2 files)
    data.json
    data.schema.json
  __init__.py
  __main__.py
  notify.py
  py.typed
  result.py
  sherlock.py
  sites.py
tests/  (9 files)
  conftest.py
  few_test_basic.py
  sherlock_interactives.py
  test_manifest.py
  test_probes.py
  test_unicode.py
  test_ux.py
  test_validate_targets.py
  test_version.py
.dockerignore
.editorconfig
.gitignore
Dockerfile
LICENSE
pyproject.toml
pytest.ini
tox.ini
```

## Entry points

- [devel/summarize_site_validation.py:61](https://github.com/sherlock-project/sherlock/blob/c588d7c8b476df9f9c84912a05d1430fb8cdcdae/devel/summarize_site_validation.py#L61)
- [sherlock_project/__main__.py:13](https://github.com/sherlock-project/sherlock/blob/c588d7c8b476df9f9c84912a05d1430fb8cdcdae/sherlock_project/__main__.py#L13)
- [sherlock_project/sherlock.py:933](https://github.com/sherlock-project/sherlock/blob/c588d7c8b476df9f9c84912a05d1430fb8cdcdae/sherlock_project/sherlock.py#L933)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| devel package | library | Observed | Groups 1 file(s) under devel package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 3 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: SherlockFuturesSession. Observed top-level functions: check_for_parameter, get_response, h… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| sherlock_project package | library | Observed | Groups 4 file(s) under sherlock_project package (observed from repository paths and static analysis). Observed top-level classes: QueryNotify, QueryNotifyPrint, QueryResult, QueryStatus, SiteInformation, SitesInformatio… |
| Tests | test | Observed | Groups 9 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: Interactives, InteractivesSubprocessError, TestLiveTargets, Test_All_Targets. Observed top-level functions:… |

## Important files

- `.actor/Dockerfile` (container)
- `.actor/actor.json` (config)
- `.actor/dataset_schema.json` (config)
- `.actor/input_schema.json` (config)
- `.dockerignore` (container)
- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/bug-report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/false-negative.yml` (config)
- `.github/ISSUE_TEMPLATE/false-positive.yml` (config)
- `.github/ISSUE_TEMPLATE/feature-request.yml` (config)
- `.github/ISSUE_TEMPLATE/site-request.yml` (config)
- `.github/workflows/exclusions.yml` (ci)
- `.github/workflows/regression.yml` (ci)
- `.github/workflows/update-site-list.yml` (ci)
- `.github/workflows/validate_modified_targets.yml` (ci)
- `Dockerfile` (container)
- `pyproject.toml` (manifest)
- `pytest.ini` (config)
- `sherlock_project/resources/data.json` (config)
- `sherlock_project/resources/data.schema.json` (config)
- `tox.ini` (config)

## Top-level layout

- `.github` — 13 analysed file(s)
- `sherlock_project` — 9 analysed file(s)
- `tests` — 9 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `.actor` — 6 analysed file(s)
- `docs` — 4 analysed file(s)
- `devel` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `c588d7c8b476df9f9c84912a05d1430fb8cdcdae` is the revision these paths and observations refer to.
