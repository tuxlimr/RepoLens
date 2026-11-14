# Project structure: Delgan/loguru

**Analysed commit:** `28349be3cd740867bc947eef741c69370ca45735`

**Commit reference:** [28349be3cd740867bc947eef741c69370ca45735](https://github.com/Delgan/loguru/commit/28349be3cd740867bc947eef741c69370ca45735)

**Tree at this commit:** [Delgan/loguru@28349be3cd74](https://github.com/Delgan/loguru/tree/28349be3cd740867bc947eef741c69370ca45735)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Delgan/loguru |
| Description | Python logging made (stupidly) simple |
| Stars | 24157 |
| Forks | 835 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `28349be3cd740867bc947eef741c69370ca45735` |
| Retrieved at | 2026-11-14T19:07:42.127679+00:00 |
| Files in this snapshot | 313 |

## Directory tree

```text
.github/  (7 files)
  workflows/  (5 files)
    codeql-analysis.yml
    docs.yml
    lint.yml
    packaging.yml
    tests.yml
  SECURITY.md
  dependabot.yml
docs/  (22 files)
  _static/  (4 files)
    css/  (1 files)
      … 1 files under this directory
    img/  (2 files)
      … 2 files under this directory
    js/  (1 files)
      … 1 files under this directory
  _templates/  (2 files)
    breadcrumbs.html
    layout.html
  api/  (3 files)
    logger.rst
    type_hints.rst
    type_hints_source.rst
  project/  (3 files)
    changelog.rst
    contributing.rst
    license.rst
  resources/  (3 files)
    migration.rst
    recipes.rst
    troubleshooting.rst
  Makefile
  api.rst
  conf.py
  index.rst
  overview.rst
  project.rst
  resources.rst
loguru/  (21 files)
  __init__.py
  __init__.pyi
  _asyncio_loop.py
  _better_exceptions.py
  _colorama.py
  _colorizer.py
  _contextvars.py
  _ctime_functions.py
  _datetime.py
  _defaults.py
  _error_interceptor.py
  _file_sink.py
  _filters.py
  _get_frame.py
  _handler.py
  _locks_machinery.py
  _logger.py
  _recattrs.py
  _simple_sinks.py
  _string_parsers.py
  py.typed
tests/  (253 files)
  exceptions/  (200 files)
    output/  (99 files)
      … 99 files under this directory
    source/  (101 files)
      … 101 files under this directory
  typesafety/  (1 files)
    test_logger.yml
  __init__.py
  conftest.py
  test_activation.py
  test_add_option_backtrace.py
  test_add_option_catch.py
  test_add_option_colorize.py
  test_add_option_context.py
  test_add_option_diagnose.py
  test_add_option_enqueue.py
  test_add_option_filter.py
  test_add_option_format.py
  test_add_option_kwargs.py
  test_add_option_level.py
  test_add_option_serialize.py
  test_add_sinks.py
  test_ansimarkup_basic.py
  test_ansimarkup_extended.py
  test_bind.py
  test_colorama.py
  test_configure.py
  test_contextualize.py
  test_coroutine_sink.py
  test_datetime.py
  test_deepcopy.py
  … 28 more files
.codecov.yml
.gitignore
.pre-commit-config.yaml
.readthedocs.yml
CHANGELOG.rst
CONTRIBUTING.rst
LICENSE
README.md
pyproject.toml
tox.ini
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| loguru package | library | Observed | Groups 19 file(s) under loguru package (observed from repository paths and static analysis). Observed top-level classes: AnsiParser, AsyncSink, Back, CallableSink, ColoredFormat, ColoredMessage. Observed top-level funct… |
| Tests | test | Observed | Groups 253 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: A, AsyncWriter, Bar, CyclicReference, Foo, HandlerIdSubclass. Observed top-level functions: _deep, _expect… |

## Important files

- `.codecov.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/codeql-analysis.yml` (ci)
- `.github/workflows/docs.yml` (ci)
- `.github/workflows/lint.yml` (ci)
- `.github/workflows/packaging.yml` (ci)
- `.github/workflows/tests.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `.readthedocs.yml` (config)
- `pyproject.toml` (manifest)
- `tox.ini` (config)

## Top-level layout

- `tests` — 253 analysed file(s)
- `docs` — 22 analysed file(s)
- `loguru` — 21 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `.github` — 7 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `28349be3cd740867bc947eef741c69370ca45735` is the revision these paths and observations refer to.
