# Project structure: plasma-umass/scalene

**Analysed commit:** `37951a9611f772b8b400e4b6f4964d0baf69a35e`

**Commit reference:** [37951a9611f772b8b400e4b6f4964d0baf69a35e](https://github.com/plasma-umass/scalene/commit/37951a9611f772b8b400e4b6f4964d0baf69a35e)

**Tree at this commit:** [plasma-umass/scalene@37951a9611f7](https://github.com/plasma-umass/scalene/tree/37951a9611f772b8b400e4b6f4964d0baf69a35e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | plasma-umass/scalene |
| Description | Scalene: a high-performance, high-precision CPU, GPU, and memory profiler for Python with AI-powered optimization proposals |
| Stars | 13560 |
| Forks | 448 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `37951a9611f772b8b400e4b6f4964d0baf69a35e` |
| Retrieved at | 2026-11-14T19:09:47.780475+00:00 |
| Files in this snapshot | 511 |

## Directory tree

```text
.github/  (10 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (7 files)
    build-and-upload.yml
    build-wheels.yml
    codeql.yml
    run-linters.yml
    test-smoketests.yml
    tests.yml
    update-models.yml
  FUNDING.yml
.vscode/  (1 files)
  c_cpp_properties.json
agents/  (1 files)
  windows-memory-profiling-port.md
benchmarks/  (6 files)
  bench_torch_memory.py
  benchmark.py
  julia1_nopil.py
  measure_profiler_memory.py
  new_benchmark.py
  pystone.py
docs/  (1 files)
  scalene-demo.ipynb
formal/  (32 files)
  extract/  (2 files)
    ScaleneExtract.lean
    scalene_verified_core.py
  lean/  (22 files)
    Scalene/  (17 files)
      … 17 files under this directory
    .gitignore
    Scalene.lean
    lake-manifest.json
    lakefile.toml
    lean-toolchain
  tla/  (5 files)
    Deadlock.cfg
    Deadlock.tla
    SignalSafety.tla
    SignalSafety_Bug.cfg
    SignalSafety_Fix.cfg
  HANDOFF.md
  README.md
  STATUS.md
scalene/  (96 files)
  scalene-gui/  (29 files)
    README.md
    TODO-TypeScript.md
    amazon.ts
    anthropic.ts
    azure.ts
    gemini.ts
    gui-elements.ts
    index.html
    index.html.template
    list-amazon-models.py
    model-recovery.ts
    models.ts
    ollama.ts
    openai.ts
    optimizations.ts
    package.json
    persistence.ts
    prism.css
    prism.d.ts
    prism.js
    profile.json
    profiler.html
    scalene-demo.ts
    scalene-fetch.ts
    … 5 more files
  README.md
  __init__.py
  __main__.py
  adaptive.py
  find_browser.py
  get_module_details.py
  hyperloglog.py
  launchbrowser.py
  merge_scalene_neuron_profiles.py
  profile.py
  redirect_python.py
  replacement_asyncio.py
  replacement_exec.py
  replacement_exit.py
  replacement_fork.py
  replacement_get_context.py
  replacement_lock.py
  replacement_mp_lock.py
  replacement_pjoin.py
  replacement_poll_selector.py
  replacement_sem_lock.py
  replacement_signal_fns.py
  replacement_thread_join.py
  replacement_thread_start.py
  … 43 more files
scripts/  (1 files)
  update_models.mjs
src/  (25 files)
  include/  (19 files)
    common.hpp
    common_win.hpp
    eintr_retry.hpp
    lowdiscrepancy.hpp
    mallocrecursionguard.hpp
    mallocrecursionguard_win.hpp
    memcpysampler.hpp
    poissonsampler.hpp
    pyptr.h
    pywhere.hpp
    samplefile.hpp
    samplefile_win.hpp
    sampleheap.hpp
    sampleheap_win.hpp
    sampler.hpp
    scaleneheader.hpp
    sharded_size_map.hpp
    thresholdsampler.hpp
    traceconfig.hpp
  source/  (6 files)
    get_line_atomic.cpp
    libscalene.cpp
    libscalene_windows.cpp
    native_unwind.cpp
    pywhere.cpp
    traceconfig.cpp
test/  (146 files)
  automatic/  (7 files)
    dataframe/  (3 files)
      … 3 files under this directory
    svm/  (3 files)
      … 3 files under this directory
    README.md
  expensive_benchmarks/  (66 files)
    docutils_data/  (58 files)
      … 58 files under this directory
    README.md
    bm_async_tree_io.py
    bm_docutils.py
    bm_fannukh.py
    bm_mdp.py
    bm_pprint.py
    bm_raytrace.py
    bm_sympy.py
  issues/  (14 files)
    test-issue124.py
    test-issue126.py
    test-issue130.py
    test-issue156.py
    test-issue167.py
    test-issue193.py
    test-issue244.py
    test-issue256.py
    test-issue266.py
    test-issue31.py
    test-issue379.py
    test-issue691.py
    test-issue74.py
    test-issue914.py
  line_attribution_tests/  (12 files)
    arithmetic_smear.py
    bigmem_driver.py
    line_after_final_alloc.py
    loop_below_threshold.py
    loop_with_multiple_lines.py
    loop_with_one_alloc.py
    loop_with_two_allocs.py
    mt_gil_release_worker.py
    mt_two_workers.py
    nested_allocator.py
    st_python_vs_c.py
    st_two_allocators.py
  optimized/  (5 files)
    bm_pyflate.py
    bm_raytrace.py
    bm_richards.py
    bm_scimark.py
    bm_spectral_norm.py
  original/  (7 files)
    bm_mdp.py
    bm_pyflate.py
    bm_raytrace.py
    bm_richards.py
    bm_scimark.py
    bm_spectral_norm.py
    bm_sympy.py
  issue_659_workload.py
  multiprocessing_test.py
  native_thread_alloc.c
  new_mp_test.py
  pool-test.py
  pool_spawn_test.py
  profile_annotation_test.py
  signal_test.py
  small_mp_test.py
  smoketest.py
  smoketest_issue_1022.py
  smoketest_issue_659.py
  smoketest_line_invalidation.py
  smoketest_pool_spawn.py
  smoketest_profile_decorator.py
  test-martinheinz.py
  test-memory.py
  test-native-thread-alloc-ctypes.py
  test-native-thread-alloc.py
  test-pprofile.py
  test-size.py
  test-torch-thread-alloc.py
  test_async_demo.py
  test_freethreaded_parity.py
  … 11 more files
tests/  (167 files)
  _scalene_subprocess.py
  conftest.py
  test_async_profiling.py
  test_child_cmdline.py
  test_classifier_soundness.py
  test_cli_leak_velocity_zero_elapsed.py
  test_combined_stacks_gui.py
  test_coverup_1.py
  test_coverup_106.py
  test_coverup_107.py
  test_coverup_109.py
  test_coverup_11.py
  test_coverup_110.py
  test_coverup_112.py
  test_coverup_113.py
  test_coverup_115.py
  test_coverup_116.py
  test_coverup_117.py
  test_coverup_118.py
  test_coverup_12.py
  test_coverup_121.py
  test_coverup_122.py
  test_coverup_123.py
  test_coverup_125.py
  … 143 more files
.gitignore
.readthedocs.yaml
CITATION.cff
CLAUDE.md
CMakeLists.txt
CODE_OF_CONDUCT.md
GNUmakefile
LICENSE
MANIFEST.in
Makefile
Pipfile
README.md
Scalene-Agents.md
Scalene-Debugging.md
Scalene-GUI.md
demo_torch_jit.py
index.rst
mypy.ini
pyproject.toml
pyrightconfig.json
pytest.ini
refactoring_todo.md
requirements.txt
ruff.toml
… 1 more files
```

## Entry points

- [benchmarks/bench_torch_memory.py:63](https://github.com/plasma-umass/scalene/blob/37951a9611f772b8b400e4b6f4964d0baf69a35e/benchmarks/bench_torch_memory.py#L63)
- [benchmarks/julia1_nopil.py:92](https://github.com/plasma-umass/scalene/blob/37951a9611f772b8b400e4b6f4964d0baf69a35e/benchmarks/julia1_nopil.py#L92)
- [benchmarks/measure_profiler_memory.py:214](https://github.com/plasma-umass/scalene/blob/37951a9611f772b8b400e4b6f4964d0baf69a35e/benchmarks/measure_profiler_memory.py#L214)
- [benchmarks/new_benchmark.py:110](https://github.com/plasma-umass/scalene/blob/37951a9611f772b8b400e4b6f4964d0baf69a35e/benchmarks/new_benchmark.py#L110)
- [benchmarks/pystone.py:272](https://github.com/plasma-umass/scalene/blob/37951a9611f772b8b400e4b6f4964d0baf69a35e/benchmarks/pystone.py#L272)
- [demo_torch_jit.py:31](https://github.com/plasma-umass/scalene/blob/37951a9611f772b8b400e4b6f4964d0baf69a35e/demo_torch_jit.py#L31)
- [scalene/__main__.py](https://github.com/plasma-umass/scalene/blob/37951a9611f772b8b400e4b6f4964d0baf69a35e/scalene/__main__.py)
- [scalene/launchbrowser.py:282](https://github.com/plasma-umass/scalene/blob/37951a9611f772b8b400e4b6f4964d0baf69a35e/scalene/launchbrowser.py#L282)
- [scalene/merge_scalene_neuron_profiles.py:356](https://github.com/plasma-umass/scalene/blob/37951a9611f772b8b400e4b6f4964d0baf69a35e/scalene/merge_scalene_neuron_profiles.py#L356)
- [scalene/scalene_apple_gpu.py:235](https://github.com/plasma-umass/scalene/blob/37951a9611f772b8b400e4b6f4964d0baf69a35e/scalene/scalene_apple_gpu.py#L235)
- [scalene/scalene_neuron.py:200](https://github.com/plasma-umass/scalene/blob/37951a9611f772b8b400e4b6f4964d0baf69a35e/scalene/scalene_neuron.py#L200)
- [scalene/scalene_profiler.py:2221](https://github.com/plasma-umass/scalene/blob/37951a9611f772b8b400e4b6f4964d0baf69a35e/scalene/scalene_profiler.py#L2221)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| benchmarks package | library | Observed | Groups 1 file(s) under benchmarks package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 17 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: BuildExtCommand, EggInfoCommand. Observed top-level functions: bdist_wheel_options,… |
| Application entry point | entrypoint | Observed | Groups 13 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: CustomHandler, NeuronMonitor, RSSMonitor, Record, Scalene, ScaleneAppleGPU. Observed top-… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| formal package | library | Observed | Groups 1 file(s) under formal package (observed from repository paths and static analysis). Observed top-level classes: List_cons, List_nil, isFalse, isTrue. Observed top-level functions: bump, c_time_ns, drop_first_wit… |
| include package | library | Observed | Groups 1 file(s) under include package (observed from repository paths and static analysis). |
| scalene package | library | Observed | Groups 78 file(s) under scalene package (observed from repository paths and static analysis). Observed top-level classes: Adaptive, AsyncStatistics, CPUStatistics, ChildArgSpec, ChromeTraceProfiler, CombinedStackFrame.… |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| source package | library | Observed | Groups 6 file(s) under source package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 313 file(s) under tests (observed from repository paths and static analysis). Observed application object created via Flask. Observed routes: ROUTE /<page>, PATCH scalene.scalene_profiler.ScaleneMapFile. Observed… |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/workflows/build-and-upload.yml` (ci)
- `.github/workflows/build-wheels.yml` (ci)
- `.github/workflows/codeql.yml` (ci)
- `.github/workflows/run-linters.yml` (ci)
- `.github/workflows/test-smoketests.yml` (ci)
- `.github/workflows/tests.yml` (ci)
- `.github/workflows/update-models.yml` (ci)
- `.readthedocs.yaml` (config)
- `.vscode/c_cpp_properties.json` (config)
- `MANIFEST.in` (manifest)
- `Pipfile` (manifest)
- `formal/lean/lake-manifest.json` (config)
- `formal/lean/lakefile.toml` (config)
- `formal/tla/Deadlock.cfg` (config)
- `formal/tla/SignalSafety_Bug.cfg` (config)
- `formal/tla/SignalSafety_Fix.cfg` (config)
- `mypy.ini` (config)
- `pyproject.toml` (manifest)
- `pyrightconfig.json` (config)
- `pytest.ini` (config)
- `requirements.txt` (manifest)
- `ruff.toml` (config)
- `scalene/scalene-gui/package.json` (manifest)
- `scalene/scalene-gui/profile.json` (config)
- `scalene/scalene-gui/tsconfig.json` (config)
- `setup.py` (manifest)

## Top-level layout

- `tests` — 167 analysed file(s)
- `test` — 146 analysed file(s)
- `scalene` — 96 analysed file(s)
- `formal` — 32 analysed file(s)
- `(root files)` — 25 analysed file(s)
- `src` — 25 analysed file(s)
- `.github` — 10 analysed file(s)
- `benchmarks` — 6 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `agents` — 1 analysed file(s)
- `docs` — 1 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 3 file(s) were skipped during inventory (1 x generated/minified file excluded; 2 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `37951a9611f772b8b400e4b6f4964d0baf69a35e` is the revision these paths and observations refer to.
