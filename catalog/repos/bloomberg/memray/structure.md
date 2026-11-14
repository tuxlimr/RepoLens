# Project structure: bloomberg/memray

**Analysed commit:** `ec314a3288f5e00e0d45a84ce6bccf7a3140d069`

**Commit reference:** [ec314a3288f5e00e0d45a84ce6bccf7a3140d069](https://github.com/bloomberg/memray/commit/ec314a3288f5e00e0d45a84ce6bccf7a3140d069)

**Tree at this commit:** [bloomberg/memray@ec314a3288f5](https://github.com/bloomberg/memray/tree/ec314a3288f5e00e0d45a84ce6bccf7a3140d069)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | bloomberg/memray |
| Description | Memray is a memory profiler for Python |
| Stars | 15417 |
| Forks | 488 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `ec314a3288f5e00e0d45a84ce6bccf7a3140d069` |
| Retrieved at | 2026-11-14T19:09:04.363260+00:00 |
| Files in this snapshot | 358 |

## Directory tree

```text
.devcontainer/  (2 files)
  tutorials/  (1 files)
    devcontainer.json
  devcontainer.json
.github/  (12 files)
  ISSUE_TEMPLATE/  (3 files)
    ---bug-report.yaml
    ---feature-request.yaml
    config.yml
  workflows/  (8 files)
    build.yml
    build_wheels.yml
    coverage.yml
    docs.yml
    news-check.yml
    sanity-check.yml
    test_uv_python.yml
    zizmor.yml
  dependabot.yml
benchmarks/  (67 files)
  benchmarking/  (64 files)
    cases/  (62 files)
      … 62 files under this directory
    __main__.py
    plot.py
  __init__.py
  benchmarks.py
  requirements.txt
docs/  (56 files)
  _static/  (3 files)
    css/  (1 files)
      … 1 files under this directory
    flamegraphs/  (1 files)
      … 1 files under this directory
    js/  (1 files)
      … 1 files under this directory
  _templates/  (1 files)
    index.html
  examples/  (8 files)
    fibonacci/  (1 files)
      … 1 files under this directory
    mandelbrot/  (3 files)
      … 3 files under this directory
    nbody/  (2 files)
      … 2 files under this directory
    sqlite/  (1 files)
      … 1 files under this directory
    README.rst
  tutorials/  (20 files)
    exercise_1/  (2 files)
      … 2 files under this directory
    exercise_2/  (2 files)
      … 2 files under this directory
    exercise_3/  (2 files)
      … 2 files under this directory
    solutions/  (3 files)
      … 3 files under this directory
    tests/  (4 files)
      … 4 files under this directory
    1.rst
    2.rst
    3.rst
    Dockerfile
    additional_features.rst
    index.rst
    requirements-tutorial.txt
  Makefile
  api.rst
  attach.rst
  conf.py
  flamegraph.rst
  getting_started.rst
  index.rst
  jupyter_magic.rst
  licenses.rst
  live.rst
  manpage.rst
  memory.rst
  native_mode.rst
  overview.rst
  performance.rst
  python_allocators.rst
  run.rst
  stats.rst
  summary.rst
  supported_environments.rst
  table.rst
  temporary_allocations.rst
  transform.rst
  tree.rst
news/  (11 files)
  .gitignore
  1000.bugfix.rst
  1014.bugfix.rst
  1020.bugfix.rst
  1032.bugfix.rst
  1033.bugfix.rst
  1035.feature.rst
  1050.bugfix.rst
  943.feature.rst
  996.bugfix.rst
  faster-temporary-aggregation.feature.rst
src/  (120 files)
  memray/  (120 files)
    _ipython/  (2 files)
      … 2 files under this directory
    _memray/  (52 files)
      … 52 files under this directory
    commands/  (15 files)
      … 15 files under this directory
    reporters/  (35 files)
      … 35 files under this directory
    __init__.py
    __init__.pyi
    __main__.py
    _destination.py
    _errors.py
    _memray.pyi
    _memray.pyx
    _memray_test_utils.pyx
    _metadata.py
    _stats.py
    _stats.pyi
    _test.py
    _test_utils.pyi
    _thread_name_interceptor.py
    _version.py
    py.typed
tests/  (72 files)
  integration/  (29 files)
    misbehaving_extension/  (3 files)
      … 3 files under this directory
    multithreaded_extension/  (4 files)
      … 4 files under this directory
    native_extension/  (3 files)
      … 3 files under this directory
    rpath_extension/  (3 files)
      … 3 files under this directory
    __init__.py
    test_api.py
    test_attach.py
    test_extensions.py
    test_greenlet.py
    test_ipython.py
    test_main.py
    test_native_tracking.py
    test_object_tracking.py
    test_processes.py
    test_pyarrow.py
    test_record_writer.py
    test_socket.py
    test_threads.py
    test_tracing.py
    test_tracking.py
  unit/  (39 files)
    __snapshots__/  (20 files)
      … 20 files under this directory
    __init__.py
    conftest.py
    test_allocation_lifetime_aggregator.py
    test_attach.py
    test_cli.py
    test_flamegraph_reporter.py
    test_frame_tools.py
    test_high_water_mark_aggregator.py
    test_highwatermark_command.py
    test_module_tools.py
    test_reader.py
    test_stats_reporter.py
    test_summary_reporter.py
    test_table_reporter.py
    test_templates.py
    test_tracker.py
    test_transform_reporter.py
    test_tree_reporter.py
    test_tui_reporter.py
  __init__.py
  conftest.py
  test_utils.py
  utils.py
.babelrc
.bumpversion.cfg
.clang-format
.gitignore
.pre-commit-config.yaml
CMakeLists.txt
CONTRIBUTING.md
Dockerfile
KEYS
LICENSE
Makefile
NEWS.rst
README.md
asv.conf.json
package.json
pyproject.toml
valgrind.supp
webpack.config.js
```

## Entry points

- [src/memray/__main__.py](https://github.com/bloomberg/memray/blob/ec314a3288f5e00e0d45a84ce6bccf7a3140d069/src/memray/__main__.py)
- [benchmarks/benchmarking/__main__.py:186](https://github.com/bloomberg/memray/blob/ec314a3288f5e00e0d45a84ce6bccf7a3140d069/benchmarks/benchmarking/__main__.py#L186)
- [benchmarks/benchmarking/cases/async_tree_base.py:136](https://github.com/bloomberg/memray/blob/ec314a3288f5e00e0d45a84ce6bccf7a3140d069/benchmarks/benchmarking/cases/async_tree_base.py#L136)
- [benchmarks/benchmarking/cases/async_tree_memray.py:135](https://github.com/bloomberg/memray/blob/ec314a3288f5e00e0d45a84ce6bccf7a3140d069/benchmarks/benchmarking/cases/async_tree_memray.py#L135)
- [benchmarks/benchmarking/cases/deltablue_base.py:622](https://github.com/bloomberg/memray/blob/ec314a3288f5e00e0d45a84ce6bccf7a3140d069/benchmarks/benchmarking/cases/deltablue_base.py#L622)
- [benchmarks/benchmarking/cases/deltablue_memray.py:629](https://github.com/bloomberg/memray/blob/ec314a3288f5e00e0d45a84ce6bccf7a3140d069/benchmarks/benchmarking/cases/deltablue_memray.py#L629)
- [benchmarks/benchmarking/cases/docutils_html_base.py:58](https://github.com/bloomberg/memray/blob/ec314a3288f5e00e0d45a84ce6bccf7a3140d069/benchmarks/benchmarking/cases/docutils_html_base.py#L58)
- [benchmarks/benchmarking/cases/docutils_html_memray.py:53](https://github.com/bloomberg/memray/blob/ec314a3288f5e00e0d45a84ce6bccf7a3140d069/benchmarks/benchmarking/cases/docutils_html_memray.py#L53)
- [benchmarks/benchmarking/cases/fannkuch_base.py:53](https://github.com/bloomberg/memray/blob/ec314a3288f5e00e0d45a84ce6bccf7a3140d069/benchmarks/benchmarking/cases/fannkuch_base.py#L53)
- [benchmarks/benchmarking/cases/fannkuch_memray.py:57](https://github.com/bloomberg/memray/blob/ec314a3288f5e00e0d45a84ce6bccf7a3140d069/benchmarks/benchmarking/cases/fannkuch_memray.py#L57)
- [benchmarks/benchmarking/cases/go_base.py:462](https://github.com/bloomberg/memray/blob/ec314a3288f5e00e0d45a84ce6bccf7a3140d069/benchmarks/benchmarking/cases/go_base.py#L462)
- [benchmarks/benchmarking/cases/go_memray.py:463](https://github.com/bloomberg/memray/blob/ec314a3288f5e00e0d45a84ce6bccf7a3140d069/benchmarks/benchmarking/cases/go_memray.py#L463)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| benchmarks package | library | Observed | Groups 5 file(s) under benchmarks package (observed from repository paths and static analysis). Observed top-level classes: AllocatorBenchmarks, FileSizeBenchmarks, HighWatermarkBenchmarks, MacroBenchmarksBase, MacroBen… |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 44 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: AsyncTree, AvgLength, Battle, BenchmarkResult, BinaryConstraint, Board. Observed top-leve… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| memray package | library | Observed | Groups 81 file(s) under memray package (observed from repository paths and static analysis). Observed top-level classes: AllocationEntry, AllocationTable, AttachCommand, BaseReporter, Destination, DetachCommand. Observe… |
| Tests | test | Observed | Groups 77 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH memray.commands.run.os.getpid, PATCH memray.commands.run.subprocess.Popen, PATCH memray.commands.live.LiveComman… |

## Important files

- `.bumpversion.cfg` (config)
- `.devcontainer/devcontainer.json` (config)
- `.devcontainer/tutorials/devcontainer.json` (config)
- `.github/ISSUE_TEMPLATE/---bug-report.yaml` (config)
- `.github/ISSUE_TEMPLATE/---feature-request.yaml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/build.yml` (ci)
- `.github/workflows/build_wheels.yml` (ci)
- `.github/workflows/coverage.yml` (ci)
- `.github/workflows/docs.yml` (ci)
- `.github/workflows/news-check.yml` (ci)
- `.github/workflows/sanity-check.yml` (ci)
- `.github/workflows/test_uv_python.yml` (ci)
- `.github/workflows/zizmor.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `Dockerfile` (container)
- `asv.conf.json` (config)
- `benchmarks/requirements.txt` (manifest)
- `docs/examples/mandelbrot/requirements.txt` (manifest)
- `docs/examples/nbody/requirements.txt` (manifest)
- `docs/tutorials/Dockerfile` (container)
- `docs/tutorials/requirements-tutorial.txt` (manifest)
- `package.json` (manifest)
- `pyproject.toml` (manifest)

## Top-level layout

- `src` — 120 analysed file(s)
- `tests` — 72 analysed file(s)
- `benchmarks` — 67 analysed file(s)
- `docs` — 56 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `.github` — 12 analysed file(s)
- `news` — 11 analysed file(s)
- `.devcontainer` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 71 file(s) were skipped during inventory (71 x vendored/generated directory excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `ec314a3288f5e00e0d45a84ce6bccf7a3140d069` is the revision these paths and observations refer to.
