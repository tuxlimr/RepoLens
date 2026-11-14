# Project structure: fabric/fabric

**Analysed commit:** `ded51893f02c33d2bc7c157624c44a039a952037`

**Commit reference:** [ded51893f02c33d2bc7c157624c44a039a952037](https://github.com/fabric/fabric/commit/ded51893f02c33d2bc7c157624c44a039a952037)

**Tree at this commit:** [fabric/fabric@ded51893f02c](https://github.com/fabric/fabric/tree/ded51893f02c33d2bc7c157624c44a039a952037)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | fabric/fabric |
| Description | Simple, Pythonic remote execution and deployment. |
| Stars | 15532 |
| Forks | 1954 |
| Licence | BSD-2-Clause |
| Language | Python |
| Default branch | main |
| Analysed commit | `ded51893f02c33d2bc7c157624c44a039a952037` |
| Retrieved at | 2026-11-14T19:09:01.353239+00:00 |
| Files in this snapshot | 110 |

## Directory tree

```text
.circleci/  (1 files)
  config.yml
.github/  (1 files)
  ISSUE_TEMPLATE/  (1 files)
    bug_report.md
fabric/  (18 files)
  testing/  (3 files)
    __init__.py
    base.py
    fixtures.py
  __init__.py
  __main__.py
  _version.py
  auth.py
  config.py
  connection.py
  exceptions.py
  executor.py
  group.py
  main.py
  runners.py
  tasks.py
  transfer.py
  tunnels.py
  util.py
integration/  (6 files)
  _support/  (2 files)
    file.txt
    funky-perms.txt
  concurrency.py
  connection.py
  group.py
  transfer.py
sites/  (35 files)
  docs/  (21 files)
    api/  (12 files)
      … 12 files under this directory
    concepts/  (3 files)
      … 3 files under this directory
    .readthedocs.yaml
    cli.rst
    conf.py
    getting-started.rst
    index.rst
    upgrading.rst
  www/  (13 files)
    .readthedocs.yaml
    changelog-v1.rst
    changelog.rst
    conf.py
    contact.rst
    development.rst
    faq.rst
    index.rst
    installing-1.x.rst
    installing.rst
    roadmap.rst
    troubleshooting.rst
    upgrading.rst
  shared_conf.py
tests/  (36 files)
  _support/  (22 files)
    json_conf/  (2 files)
      … 2 files under this directory
    py_conf/  (2 files)
      … 2 files under this directory
    ssh_config/  (10 files)
      … 10 files under this directory
    yaml_conf/  (2 files)
      … 2 files under this directory
    yml_conf/  (2 files)
      … 2 files under this directory
    config.yml
    fabfile.py
    prompting.py
    runtime_fabfile.py
  _util.py
  auth.py
  config.py
  conftest.py
  connection.py
  executor.py
  group.py
  init.py
  main.py
  runners.py
  task.py
  testing.py
  transfer.py
  util.py
.codecov.yml
.coveragerc
.flake8
.gitignore
LICENSE
MANIFEST.in
README.rst
SECURITY.md
codecov.yml
dev-requirements.txt
pytest.ini
setup.py
tasks.py
```

## Entry points

- [integration/group.py:9](https://github.com/fabric/fabric/blob/ded51893f02c33d2bc7c157624c44a039a952037/integration/group.py#L9)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: Config. |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). Observed top-level functions: coverage, integration, safety_test_v1_to_v2_shim. |
| Application entry point | entrypoint | Observed | Groups 3 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Group. Observed top-level classes: Fab, Group_. Observed top-level functions:… |
| External integrations | external | Observed | Groups 3 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: Connection_, Transfer_, concurrency. Observed top-level functions: _support, _worker, skip_o… |
| fabric package | library | Observed | Groups 15 file(s) under fabric package (observed from repository paths and static analysis). Observed top-level classes: Command, Connection, ConnectionCall, Executor, Group, GroupException. Observed top-level functions… |
| sites package | library | Observed | Groups 3 file(s) under sites package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 36 file(s) under tests (observed from repository paths and static analysis). Observed application object created via Group. Observed routes: PATCH fabric.auth.partial, PATCH fabric.config.os.path.exists, PATCH fa… |

## Important files

- `.circleci/config.yml` (ci)
- `.codecov.yml` (config)
- `MANIFEST.in` (manifest)
- `codecov.yml` (config)
- `pytest.ini` (config)
- `setup.py` (manifest)
- `sites/docs/.readthedocs.yaml` (config)
- `sites/www/.readthedocs.yaml` (config)

## Top-level layout

- `tests` — 36 analysed file(s)
- `sites` — 35 analysed file(s)
- `fabric` — 18 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `integration` — 6 analysed file(s)
- `.circleci` — 1 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `ded51893f02c33d2bc7c157624c44a039a952037` is the revision these paths and observations refer to.
