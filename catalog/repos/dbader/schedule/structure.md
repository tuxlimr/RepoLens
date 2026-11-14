# Project structure: dbader/schedule

**Analysed commit:** `82a43db1b938d8fdf60103bd41f329e06c8d3651`

**Commit reference:** [82a43db1b938d8fdf60103bd41f329e06c8d3651](https://github.com/dbader/schedule/commit/82a43db1b938d8fdf60103bd41f329e06c8d3651)

**Tree at this commit:** [dbader/schedule@82a43db1b938](https://github.com/dbader/schedule/tree/82a43db1b938d8fdf60103bd41f329e06c8d3651)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | dbader/schedule |
| Description | Python job scheduling for humans. |
| Stars | 12265 |
| Forks | 1024 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `82a43db1b938d8fdf60103bd41f329e06c8d3651` |
| Retrieved at | 2026-11-14T19:10:11.412081+00:00 |
| Files in this snapshot | 32 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    ci.yml
docs/  (17 files)
  _static/  (1 files)
    custom.css
  _templates/  (1 files)
    sidebarintro.html
  Makefile
  background-execution.rst
  changelog.rst
  conf.py
  development.rst
  examples.rst
  exception-handling.rst
  faq.rst
  index.rst
  installation.rst
  logging.rst
  multiple-schedulers.rst
  parallel-execution.rst
  reference.rst
  timezones.rst
schedule/  (2 files)
  __init__.py
  py.typed
.gitignore
AUTHORS.rst
HISTORY.rst
LICENSE.txt
MANIFEST.in
README.rst
pyproject.toml
requirements-dev.txt
setup.cfg
setup.py
test_schedule.py
tox.ini
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: read_file. |
| schedule package | library | Observed | Groups 1 file(s) under schedule package (observed from repository paths and static analysis). Observed top-level classes: CancelJob, IntervalError, Job, ScheduleError, ScheduleValueError, Scheduler. Observed top-level f… |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: SchedulerTests, mock_datetime. Observed top-level functions: make_mock_job. |

## Important files

- `.github/workflows/ci.yml` (ci)
- `MANIFEST.in` (manifest)
- `pyproject.toml` (manifest)
- `requirements-dev.txt` (manifest)
- `setup.cfg` (manifest)
- `setup.py` (manifest)
- `tox.ini` (config)

## Top-level layout

- `docs` — 17 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `schedule` — 2 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `82a43db1b938d8fdf60103bd41f329e06c8d3651` is the revision these paths and observations refer to.
