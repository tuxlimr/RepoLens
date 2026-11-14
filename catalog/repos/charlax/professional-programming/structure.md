# Project structure: charlax/professional-programming

**Analysed commit:** `2e9e51cb5f42c45a31c70ed59ce1fd9fb9618d5e`

**Commit reference:** [2e9e51cb5f42c45a31c70ed59ce1fd9fb9618d5e](https://github.com/charlax/professional-programming/commit/2e9e51cb5f42c45a31c70ed59ce1fd9fb9618d5e)

**Tree at this commit:** [charlax/professional-programming@2e9e51cb5f42](https://github.com/charlax/professional-programming/tree/2e9e51cb5f42c45a31c70ed59ce1fd9fb9618d5e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | charlax/professional-programming |
| Description | A collection of learning resources for curious software engineers |
| Stars | 51678 |
| Forks | 4034 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `2e9e51cb5f42c45a31c70ed59ce1fd9fb9618d5e` |
| Retrieved at | 2026-11-14T19:06:32.735537+00:00 |
| Files in this snapshot | 29 |

## Directory tree

```text
.github/  (1 files)
  pull_request_template.md
antipatterns/  (11 files)
  python-examples/  (2 files)
    reraise_exceptions_bad.py
    reraise_exceptions_good.py
  sqlalchemy-examples/  (1 files)
    exists.py
  README.md
  code-antipatterns.md
  database-antipatterns.md
  error-handling-antipatterns.md
  mvcs-antipatterns.md
  scalability-antipatterns.md
  sqlalchemy-antipatterns.md
  tests-antipatterns.md
list-of-links/  (1 files)
  List of AI and LLM learning resources 20260104144118.md
training/  (10 files)
  front-end/  (8 files)
    examples/  (1 files)
      … 1 files under this directory
    01-modern-javascript.md
    02-react.md
    03-typescript.md
    04-the-browser.md
    05-css-html-restart.md
    06-front-end-development-practices.md
    README.md
  learning-python/  (1 files)
    README.md
  web-dev/  (1 files)
    README.md
.pre-commit-config.yaml
CONTRIBUTING.md
LICENSE
README.md
feature-flags.md
glossary.md
```

## Entry points

- [antipatterns/sqlalchemy-examples/exists.py:37](https://github.com/charlax/professional-programming/blob/2e9e51cb5f42c45a31c70ed59ce1fd9fb9618d5e/antipatterns/sqlalchemy-examples/exists.py#L37)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| antipatterns package | library | Observed | Groups 2 file(s) under antipatterns package (observed from repository paths and static analysis). Observed top-level classes: ToastException. Observed top-level functions: put_in_toaster, toast. |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Toaster. Observed top-level functions: main, toaster_exists_bad, toaster_exists_good. |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |

## Important files

- `.pre-commit-config.yaml` (config)

## Top-level layout

- `antipatterns` — 11 analysed file(s)
- `training` — 10 analysed file(s)
- `(root files)` — 6 analysed file(s)
- `.github` — 1 analysed file(s)
- `list-of-links` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `2e9e51cb5f42c45a31c70ed59ce1fd9fb9618d5e` is the revision these paths and observations refer to.
