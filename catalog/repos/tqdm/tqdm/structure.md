# Project structure: tqdm/tqdm

**Analysed commit:** `9cf5a12b1f955468a17f0ba3c59092b23e4258ac`

**Commit reference:** [9cf5a12b1f955468a17f0ba3c59092b23e4258ac](https://github.com/tqdm/tqdm/commit/9cf5a12b1f955468a17f0ba3c59092b23e4258ac)

**Tree at this commit:** [tqdm/tqdm@9cf5a12b1f95](https://github.com/tqdm/tqdm/tree/9cf5a12b1f955468a17f0ba3c59092b23e4258ac)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | tqdm/tqdm |
| Description | :zap: A Fast, Extensible Progress Bar for Python and CLI |
| Stars | 31383 |
| Forks | 1993 |
| Licence | Other |
| Language | Python |
| Default branch | master |
| Analysed commit | `9cf5a12b1f955468a17f0ba3c59092b23e4258ac` |
| Retrieved at | 2026-11-14T19:07:07.812528+00:00 |
| Files in this snapshot | 79 |

## Directory tree

```text
examples/  (13 files)
  7zx.py
  async_coroutines.py
  coroutine_pipe.py
  include_no_requirements.py
  pandas_progress_apply.py
  paper.bib
  paper.md
  parallel_bars.py
  redirect_print.py
  simple_examples.py
  tqdm_requests.py
  tqdm_wget.py
  wrapping_generators.py
tests/  (21 files)
  __init__.py
  conftest.py
  tests_asyncio.py
  tests_concurrent.py
  tests_contrib.py
  tests_contrib_logging.py
  tests_dask.py
  tests_gui.py
  tests_itertools.py
  tests_keras.py
  tests_main.py
  tests_notebook.py
  tests_pandas.py
  tests_perf.py
  tests_rich.py
  tests_rlock.py
  tests_synchronisation.py
  tests_tk.py
  tests_tqdm.py
  tests_utils.py
  tests_version.py
tqdm/  (33 files)
  contrib/  (9 files)
    __init__.py
    bells.py
    concurrent.py
    discord.py
    itertools.py
    logging.py
    slack.py
    telegram.py
    utils_worker.py
  __init__.py
  __main__.py
  _main.py
  _monitor.py
  _tqdm.py
  _tqdm_gui.py
  _tqdm_notebook.py
  _tqdm_pandas.py
  _utils.py
  asyncio.py
  auto.py
  autonotebook.py
  cli.py
  completion.sh
  dask.py
  gui.py
  keras.py
  notebook.py
  rich.py
  std.py
  tk.py
  tqdm.1
  utils.py
  version.py
.pre-commit-config.yaml
.prospector.yml
.zenodo.json
CODE_OF_CONDUCT.md
CONTRIBUTING.md
DEMO.ipynb
LICENCE
Makefile
README.rst
environment.yml
pyproject.toml
tests_notebook.ipynb
```

## Entry points

- [tqdm/cli.py](https://github.com/tqdm/tqdm/blob/9cf5a12b1f955468a17f0ba3c59092b23e4258ac/tqdm/cli.py)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: cast, main, posix_pipe. |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 21 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: AIterable, AIterator, CustomTqdm, DiscreteTimer, ErrorRaisingTqdm, FakeEvent. Observed top-level functions:… |
| tqdm package | library | Observed | Groups 30 file(s) under tqdm package (observed from repository paths and static analysis). Observed top-level classes: Bar, CallbackIOWrapper, Comparable, DisableOnWriteError, DiscordIO, DummyTqdmFile. Observed top-leve… |

## Important files

- `.pre-commit-config.yaml` (config)
- `.prospector.yml` (config)
- `.zenodo.json` (config)
- `environment.yml` (manifest)
- `pyproject.toml` (manifest)

## Top-level layout

- `tqdm` — 33 analysed file(s)
- `tests` — 21 analysed file(s)
- `examples` — 13 analysed file(s)
- `(root files)` — 12 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `9cf5a12b1f955468a17f0ba3c59092b23e4258ac` is the revision these paths and observations refer to.
