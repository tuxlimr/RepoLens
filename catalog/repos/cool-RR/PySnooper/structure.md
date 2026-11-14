# Project structure: cool-RR/PySnooper

**Analysed commit:** `4be5c156ffc3315011c42ba521c4d8487052d289`

**Commit reference:** [4be5c156ffc3315011c42ba521c4d8487052d289](https://github.com/cool-RR/PySnooper/commit/4be5c156ffc3315011c42ba521c4d8487052d289)

**Tree at this commit:** [cool-RR/PySnooper@4be5c156ffc3](https://github.com/cool-RR/PySnooper/tree/4be5c156ffc3315011c42ba521c4d8487052d289)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | cool-RR/PySnooper |
| Description | Never use print for debugging again |
| Stars | 16576 |
| Forks | 971 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `4be5c156ffc3315011c42ba521c4d8487052d289` |
| Retrieved at | 2026-11-14T19:08:46.141684+00:00 |
| Files in this snapshot | 44 |

## Directory tree

```text
misc/  (2 files)
  IDE files/  (1 files)
    PySnooper.wpr
  generate_authors.py
pysnooper/  (5 files)
  __init__.py
  pycompat.py
  tracer.py
  utils.py
  variables.py
tests/  (22 files)
  mini_toolbox/  (3 files)
    __init__.py
    contextlib.py
    pathlib.py
  samples/  (4 files)
    __init__.py
    exception.py
    indentation.py
    recursion.py
  test_multiple_files/  (5 files)
    multiple_files/  (3 files)
      … 3 files under this directory
    __init__.py
    test_multiple_files.py
  test_utils/  (3 files)
    __init__.py
    test_ensure_tuple.py
    test_regex.py
  __init__.py
  test_chinese.py
  test_ended_by_exception.py
  test_mini_toolbox.py
  test_not_implemented.py
  test_pysnooper.py
  utils.py
.gitignore
.travis.yml
ADVANCED_USAGE.md
AUTHORS
CITATION.cff
LICENSE
MANIFEST.in
README.md
make_release.sh
pyproject.toml
requirements.in
requirements.txt
setup.cfg
setup.py
tox.ini
```

## Entry points

- [misc/generate_authors.py:57](https://github.com/cool-RR/PySnooper/blob/4be5c156ffc3315011c42ba521c4d8487052d289/misc/generate_authors.py#L57)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: read_file. |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: drop_recurrences, iterate_authors_by_chronological_order, print_authors. |
| pysnooper package | library | Observed | Groups 5 file(s) under pysnooper package (observed from repository paths and static analysis). Observed top-level classes: Attrs, BaseVariable, CommonVariable, Exploding, FileWriter, Indices. Observed top-level function… |
| Tests | test | Observed | Groups 22 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: CallEndedByExceptionEntry, CallEntry, ContextDecorator, ContextStack, ElapsedTimeEntry, ExceptionEntry. Obs… |

## Important files

- `.travis.yml` (ci)
- `MANIFEST.in` (manifest)
- `pyproject.toml` (manifest)
- `requirements.txt` (manifest)
- `setup.cfg` (manifest)
- `setup.py` (manifest)
- `tox.ini` (config)

## Top-level layout

- `tests` — 22 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `pysnooper` — 5 analysed file(s)
- `misc` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `4be5c156ffc3315011c42ba521c4d8487052d289` is the revision these paths and observations refer to.
