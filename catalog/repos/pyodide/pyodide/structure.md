# Project structure: pyodide/pyodide

**Analysed commit:** `ebb528e4e7ddf8758764c10091d6613e5ce4f1c8`

**Commit reference:** [ebb528e4e7ddf8758764c10091d6613e5ce4f1c8](https://github.com/pyodide/pyodide/commit/ebb528e4e7ddf8758764c10091d6613e5ce4f1c8)

**Tree at this commit:** [pyodide/pyodide@ebb528e4e7dd](https://github.com/pyodide/pyodide/tree/ebb528e4e7ddf8758764c10091d6613e5ce4f1c8)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | pyodide/pyodide |
| Description | Pyodide is a Python distribution for the browser and Node.js based on WebAssembly |
| Stars | 14939 |
| Forks | 1062 |
| Licence | MPL-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `ebb528e4e7ddf8758764c10091d6613e5ce4f1c8` |
| Retrieved at | 2026-11-14T19:09:11.172776+00:00 |
| Files in this snapshot | 549 |

## Directory tree

```text
.circleci/  (2 files)
  config.yml
  s3-website-config.json
.devcontainer/  (4 files)
  conda/  (1 files)
    devcontainer.json
  devcontainer.json
  onCreate-conda.sh
  onCreate-docker.sh
.github/  (14 files)
  ISSUE_TEMPLATE/  (5 files)
    bug_report.md
    config.yml
    documentation.md
    feature_request.md
    improvement.md
  workflows/  (5 files)
    deploy_release.yml
    docker_image.yml
    main.yml
    pages.yml
    update_cross_build_releases.yml
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
  codecov.yml
  dependabot.yml
benchmark/  (50 files)
  benchmarks/  (36 files)
    numpy_benchmarks/  (34 files)
      … 34 files under this directory
    pystone_benchmarks/  (1 files)
      … 1 files under this directory
    README.md
  node/  (11 files)
    helpers/  (4 files)
      … 4 files under this directory
    suites/  (6 files)
      … 6 files under this directory
    run.mjs
  benchmark.py
  plot_benchmark.py
  stack_usage.py
cpython/  (14 files)
  patches/  (10 files)
    0001-Public-pymain_run_python.patch
    0002-Fix-LONG_BIT-constant-to-be-always-32bit.patch
    0003-Add-call-to-JsProxy_GetMethod-to-help-remove-tempora.patch
    0004-Make-from-x-import-aware-of-jsproxy-modules.patch
    0005-Remove-JSPI-related-parts-in-emscripten_syscalls.c.patch
    0006-Teach-json-encoder.py-to-encode-jsnull.patch
    0007-Warn-if-ZoneInfo-is-imported-without-tzdata.patch
    0008-Export-_Py_emscripten_signal_clock-and-_Py_emscripte.patch
    0009-Fix-Emscripten-trampoline-with-emcc-4.0.19.patch
    0010-Remove-iOS-guard-for-wasm-gc-trampoline.patch
  Makefile
  README.md
  Setup.local
  adjust_sysconfig.py
docs/  (74 files)
  _static/  (3 files)
    css/  (1 files)
      … 1 files under this directory
    img/  (2 files)
      … 2 files under this directory
  _templates/  (1 files)
    layout.html
  development/  (13 files)
    abi/  (5 files)
      … 5 files under this directory
    abi.md
    building-from-sources.md
    building-packages.md
    contributing.md
    core.md
    debugging.md
    maintainers.md
    testing.md
  project/  (8 files)
    release-notes/  (1 files)
      … 1 files under this directory
    about.md
    changelog.md
    code-of-conduct.md
    deprecation-timeline.md
    governance.md
    related-projects.md
    roadmap.md
  sphinx_pyodide/  (8 files)
    sphinx_pyodide/  (7 files)
      … 7 files under this directory
    README.md
  usage/  (35 files)
    api/  (9 files)
      … 9 files under this directory
    examples/  (5 files)
      … 5 files under this directory
    accessing-files.md
    api-reference.md
    cli.md
    downloading-and-deploying.md
    examples.md
    faq.md
    file-system.md
    index.md
    keyboard-interrupts.md
    loading-custom-python-code.md
    loading-packages.md
    packages-in-pyodide.md
    quickstart.md
    sdl.md
    service-worker.md
    socket.md
    streams.md
    type-conversions.md
    wasm-constraints.md
    webworker.md
    working-with-bundlers.md
  Makefile
  conf.py
  expected_js_docs.txt
  index.rst
  make.bat
  requirements-doc.txt
emsdk/  (6 files)
  patches/  (5 files)
    0001-Add-useful-error-when-symbol-resolution-fails.patch
    0002-Fix-promise-order.patch
    0003-dylink-Normalize-library-paths-to-prevent-duplicate-loading.patch
    0004-Append-pic-directory-when-SIDE_MODULE.patch
    0005-Don-t-bundle-the-LLVM-profile-runtime-into-libcompil.patch
  Makefile
metadata/  (3 files)
  pyodide-cross-build-environments-debug-v2.json
  pyodide-cross-build-environments-v1.json
  pyodide-cross-build-environments-v2.json
packages/  (118 files)
  _tests/  (1 files)
    test_packages_common.py
  cffi/  (2 files)
    meta.yaml
    test_cffi.py
  coverage/  (1 files)
    meta.yaml
  iniconfig/  (1 files)
    meta.yaml
  libboost/  (1 files)
    meta.yaml
  libf2c/  (9 files)
    extras/  (1 files)
      … 1 files under this directory
    patches/  (7 files)
      … 7 files under this directory
    meta.yaml
  libopenblas/  (4 files)
    patches/  (3 files)
      … 3 files under this directory
    meta.yaml
  libopenssl/  (1 files)
    meta.yaml
  micropip/  (2 files)
    meta.yaml
    test_micropip.py
  numpy/  (2 files)
    meta.yaml
    test_numpy.py
  packaging/  (3 files)
    patches/  (1 files)
      … 1 files under this directory
    meta.yaml
    test_packaging.py
  pluggy/  (1 files)
    meta.yaml
  pycparser/  (1 files)
    meta.yaml
  pydoc_data/  (3 files)
    src/  (1 files)
      … 1 files under this directory
    meta.yaml
    test_pydoc.py
  pyodide-tblib/  (1 files)
    meta.yaml
  pytest/  (2 files)
    meta.yaml
    test_pytest.py
  pytest-asyncio/  (3 files)
    inner_test_pytest_asyncio.py
    meta.yaml
    test_pytest_asyncio.py
  scipy/  (11 files)
    patches/  (5 files)
      … 5 files under this directory
    cmdline_test_file.py
    info.md
    meta.yaml
    scipy-conftest.py
    scipy-pytest.js
    test_scipy.py
  test/  (3 files)
    src/  (1 files)
      … 1 files under this directory
    meta.yaml
    test_test.py
  test-buffer/  (4 files)
    buffer-test/  (2 files)
      … 2 files under this directory
    meta.yaml
    test_buffer.py
  test-cpp-exceptions/  (4 files)
    src/  (2 files)
      … 2 files under this directory
    meta.yaml
    test_cpp_exceptions.py
  test-cpp-exceptions2/  (4 files)
    src/  (3 files)
      … 3 files under this directory
    meta.yaml
  test-dummy/  (3 files)
    src/  (2 files)
      … 2 files under this directory
    meta.yaml
  test-dummy-nonpure/  (3 files)
    src/  (2 files)
      … 2 files under this directory
    meta.yaml
  test-dummy-unNormalized/  (3 files)
    src/  (2 files)
      … 2 files under this directory
    meta.yaml
  test-dummy-unvendoring/  (4 files)
    src/  (3 files)
      … 3 files under this directory
    meta.yaml
  test-fpcast/  (4 files)
    fpcast-test/  (2 files)
      … 2 files under this directory
    meta.yaml
    test_fpcast_test.py
  test-pybind11/  (5 files)
    src/  (3 files)
      … 3 files under this directory
    meta.yaml
    test_pybind11.py
  test-rust-abi/  (6 files)
    src/  (4 files)
      … 4 files under this directory
    meta.yaml
    test_rust_abi.py
  test-rust-panic/  (6 files)
    src/  (4 files)
      … 4 files under this directory
    meta.yaml
    test_rust_panic.py
  test-sharedlib/  (5 files)
    src/  (4 files)
      … 4 files under this directory
    meta.yaml
  test-sharedlib-py/  (4 files)
    src/  (2 files)
      … 2 files under this directory
    meta.yaml
    test_sharedlib.py
  test-simd/  (9 files)
    src/  (7 files)
      … 7 files under this directory
    meta.yaml
    test_simd.py
  Makefile
  README.md
src/  (198 files)
  core/  (47 files)
    stack_switching/  (7 files)
      … 7 files under this directory
    README.md
    _pyodide_core.c
    docstring.c
    docstring.h
    error_handling.c
    error_handling.h
    error_handling.ts
    hiwire.c
    js2python.c
    js2python.h
    js2python.js
    jsbind.c
    jsbind.h
    jslib.c
    jslib.h
    jsmemops.h
    jsproxy.c
    jsproxy.h
    jsproxy_call.c
    jsproxy_call.h
    jsverror.ts
    jsverror.wat
    libjsverror.js
    main.c
    … 16 more files
  js/  (56 files)
    common/  (7 files)
      … 7 files under this directory
    fs/  (3 files)
      … 3 files under this directory
    test/  (15 files)
      … 15 files under this directory
    .gitignore
    README.md
    api.ts
    canvas.ts
    compat.ts
    constants.ts
    dynload.ts
    emscripten-settings.ts
    environments.ts
    esbuild.config.inner.mjs
    esbuild.config.outer.mjs
    esbuild.config.shared.mjs
    ffi.ts
    generated_struct_info32.json.d.ts
    installer.ts
    load-package.ts
    memory-limit.ts
    nativefs.ts
    package.json
    packaging-utils.ts
    playwright.config.ts
    pyodide.ts
    pyodide.umd.ts
    scheduler.ts
    … 7 more files
  py/  (32 files)
    _pyodide/  (9 files)
      … 9 files under this directory
    pyodide/  (17 files)
      … 17 files under this directory
    README.md
    _ssl.py
    js.pyi
    pyproject.toml
    ssl.py
    webbrowser.py
  templates/  (11 files)
    console-v2.html
    console.html
    makesnap.mjs
    module_static_import_test.html
    module_test.html
    python
    python.bat
    python_cli_entry.mjs
    python_exe.go
    test.html
    test_csp.html
  test-bun/  (2 files)
    package.json
    smoke-test.js
  test-deno/  (4 files)
    README.md
    deno.json
    deno.lock
    smoke-test.ts
  test-js/  (4 files)
    index.d.ts
    index.test-d.ts
    package.json
    tsconfig.json
  tests/  (42 files)
    html_templates/  (1 files)
      … 1 files under this directory
    test_data/  (4 files)
      … 4 files under this directory
    test_pkg/  (2 files)
      … 2 files under this directory
    __init__.py
    blns.base64.json
    python_tests.yaml
    test_asyncio.py
    test_browser_apis.py
    test_bz2.py
    test_canvas.py
    test_cmdline_runner.py
    test_common.py
    test_compat.py
    test_console.py
    test_core_python.py
    test_database_driver.py
    test_filesystem.py
    test_filesystem_mounting.py
    test_filesystem_webworker.py
    test_jsproxy.py
    test_package_loading.py
    test_pyodide.py
    test_pyodide_http.py
    test_pyproxy.py
    test_pytest_wrapper.py
    test_python.py
    test_python_esm.py
    … 11 more files
tools/  (42 files)
  cmdline_runner_test/  (2 files)
    run
    run.bat
  tests/  (13 files)
    testdata/  (2 files)
      … 2 files under this directory
    test_backport.py
    test_bump_version.py
    test_create_lockfile_diff.py
    test_create_xbuildenv.py
    test_create_zipfile.py
    test_cross_build_environments_metadata.py
    test_deploy_s3.py
    test_make_ghr_release.py
    test_make_test_list.py
    test_run_docker.py
    test_update_cross_build_releases.py
  backport.py
  bump_version.py
  calculate_build_cache_key.py
  check_build_trigger.sh
  check_ccache.py
  check_compressed_size.py
  check_documented_functions.py
  codespell_ignore_words.txt
  common.py
  constraints.txt
  create_lockfile_diff.py
  create_xbuildenv.py
  create_zipfile.py
  d8-test.mjs
  d8-test.sh
  dependency-check.sh
  deploy_s3.py
  deploy_to_npm.sh
  docker_image_tag.py
  fixup-type-definitions.py
  make_ghr_release.py
  make_test_list.py
  pytest_wrapper.py
  release_nightly_xbuildenv.py
  … 3 more files
.clang-format
.codecov.yml
.dockerignore
.editorconfig
.gitignore
.gitmodules
.pre-commit-config.yaml
.readthedocs.yml
AGENTS.md
CODE-OF-CONDUCT.md
Dockerfile
LICENSE
Makefile
Makefile.envs
README.md
biome.json
conftest.py
environment.yml
pyodide_env.sh
pyproject.toml
repository-structure.md
requirements-deploy.txt
requirements.txt
run_docker
```

## Entry points

- [benchmark/benchmark.py:227](https://github.com/pyodide/pyodide/blob/ebb528e4e7ddf8758764c10091d6613e5ce4f1c8/benchmark/benchmark.py#L227)
- [benchmark/node/helpers/pyperformance_native.py:72](https://github.com/pyodide/pyodide/blob/ebb528e4e7ddf8758764c10091d6613e5ce4f1c8/benchmark/node/helpers/pyperformance_native.py#L72)
- [cpython/adjust_sysconfig.py:76](https://github.com/pyodide/pyodide/blob/ebb528e4e7ddf8758764c10091d6613e5ce4f1c8/cpython/adjust_sysconfig.py#L76)
- [tools/backport.py:855](https://github.com/pyodide/pyodide/blob/ebb528e4e7ddf8758764c10091d6613e5ce4f1c8/tools/backport.py#L855)
- [tools/bump_version.py:368](https://github.com/pyodide/pyodide/blob/ebb528e4e7ddf8758764c10091d6613e5ce4f1c8/tools/bump_version.py#L368)
- [tools/calculate_build_cache_key.py:55](https://github.com/pyodide/pyodide/blob/ebb528e4e7ddf8758764c10091d6613e5ce4f1c8/tools/calculate_build_cache_key.py#L55)
- [tools/check_ccache.py:25](https://github.com/pyodide/pyodide/blob/ebb528e4e7ddf8758764c10091d6613e5ce4f1c8/tools/check_ccache.py#L25)
- [tools/check_compressed_size.py:62](https://github.com/pyodide/pyodide/blob/ebb528e4e7ddf8758764c10091d6613e5ce4f1c8/tools/check_compressed_size.py#L62)
- [tools/check_documented_functions.py:91](https://github.com/pyodide/pyodide/blob/ebb528e4e7ddf8758764c10091d6613e5ce4f1c8/tools/check_documented_functions.py#L91)
- [tools/create_lockfile_diff.py:242](https://github.com/pyodide/pyodide/blob/ebb528e4e7ddf8758764c10091d6613e5ce4f1c8/tools/create_lockfile_diff.py#L242)
- [tools/create_xbuildenv.py:284](https://github.com/pyodide/pyodide/blob/ebb528e4e7ddf8758764c10091d6613e5ce4f1c8/tools/create_xbuildenv.py#L284)
- [tools/create_zipfile.py:174](https://github.com/pyodide/pyodide/blob/ebb528e4e7ddf8758764c10091d6613e5ce4f1c8/tools/create_zipfile.py#L174)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| benchmark package | library | Observed | Groups 47 file(s) under benchmark package (observed from repository paths and static analysis). Observed top-level classes: Record. Observed top-level functions: Func1, Func2, Func3, Proc0, Proc1, Proc2. |
| Configuration and deployment | config | Observed | Groups 68 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 21 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Typer. Observed top-level classes: App, Changelog, ChangelogEntry, ChangelogP… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| js package | library | Observed | Groups 35 file(s) under js package (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 28 file(s) under packages package (observed from repository paths and static analysis). Observed top-level functions: async_coro, dummy, pytest_collection_modifyitems, pytest_configure, pytest_sessionfinish, test… |
| py package | library | Observed | Groups 27 file(s) under py package (observed from repository paths and static analysis). Observed top-level classes: AbortError, BaseBrowser, BindClass, BodyUsedError, CodeRunner, Console. Observed top-level functions:… |
| Service / domain layer | service | Observed | Groups 44 file(s) under service / domain layer (observed from repository paths and static analysis). |
| templates package | library | Observed | Groups 3 file(s) under templates package (observed from repository paths and static analysis). |
| test-bun package | library | Observed | Groups 1 file(s) under test-bun package (observed from repository paths and static analysis). |
| test-deno package | library | Observed | Groups 1 file(s) under test-deno package (observed from repository paths and static analysis). |
| test-js package | library | Observed | Groups 2 file(s) under test-js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 93 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: DummyDistribution, ImportTestCase, NoHypothesisUnpickler, TestPyxhr. Observed top-level functions: _check_s… |
| tools package | library | Observed | Groups 7 file(s) under tools package (observed from repository paths and static analysis). Observed top-level functions: get_makefile_envs. |

## Important files

- `.circleci/config.yml` (ci)
- `.circleci/s3-website-config.json` (ci)
- `.codecov.yml` (config)
- `.devcontainer/conda/devcontainer.json` (config)
- `.devcontainer/devcontainer.json` (config)
- `.dockerignore` (container)
- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/codecov.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/deploy_release.yml` (ci)
- `.github/workflows/docker_image.yml` (ci)
- `.github/workflows/main.yml` (ci)
- `.github/workflows/pages.yml` (ci)
- `.github/workflows/update_cross_build_releases.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `.readthedocs.yml` (config)
- `Dockerfile` (container)
- `biome.json` (config)
- `docs/requirements-doc.txt` (manifest)
- `environment.yml` (manifest)
- `metadata/pyodide-cross-build-environments-debug-v2.json` (config)
- `metadata/pyodide-cross-build-environments-v1.json` (config)
- `metadata/pyodide-cross-build-environments-v2.json` (config)
- `packages/cffi/meta.yaml` (config)
- `packages/coverage/meta.yaml` (config)
- `packages/iniconfig/meta.yaml` (config)
- `packages/libboost/meta.yaml` (config)
- `packages/libf2c/meta.yaml` (config)
- `packages/libopenblas/meta.yaml` (config)
- `packages/libopenssl/meta.yaml` (config)
- `packages/micropip/meta.yaml` (config)
- `packages/numpy/meta.yaml` (config)
- `packages/packaging/meta.yaml` (config)
- `packages/pluggy/meta.yaml` (config)
- `packages/pycparser/meta.yaml` (config)
- `packages/pydoc_data/meta.yaml` (config)
- `packages/pydoc_data/src/pyproject.toml` (manifest)
- `packages/pyodide-tblib/meta.yaml` (config)
- `packages/pytest-asyncio/meta.yaml` (config)
- `packages/pytest/meta.yaml` (config)
- `packages/scipy/meta.yaml` (config)
- `packages/test-buffer/buffer-test/setup.py` (manifest)
- `packages/test-buffer/meta.yaml` (config)
- `packages/test-cpp-exceptions/meta.yaml` (config)
- `packages/test-cpp-exceptions2/meta.yaml` (config)
- `packages/test-cpp-exceptions2/src/setup.py` (manifest)
- `packages/test-dummy-nonpure/meta.yaml` (config)
- `packages/test-dummy-nonpure/src/setup.py` (manifest)
- `packages/test-dummy-unNormalized/meta.yaml` (config)
- `packages/test-dummy-unNormalized/src/pyproject.toml` (manifest)
- `packages/test-dummy-unvendoring/meta.yaml` (config)
- `packages/test-dummy-unvendoring/src/pyproject.toml` (manifest)
- `packages/test-dummy/meta.yaml` (config)
- `packages/test-dummy/src/pyproject.toml` (manifest)
- `packages/test-fpcast/fpcast-test/setup.py` (manifest)
- `packages/test-fpcast/meta.yaml` (config)
- `packages/test-pybind11/meta.yaml` (config)
- `packages/test-pybind11/src/pyproject.toml` (manifest)
- `packages/test-pybind11/src/setup.py` (manifest)
- `packages/test-rust-abi/meta.yaml` (config)
- `packages/test-rust-abi/src/Cargo.toml` (manifest)
- `packages/test-rust-abi/src/pyproject.toml` (manifest)
- `packages/test-rust-abi/src/setup.py` (manifest)
- `packages/test-rust-panic/meta.yaml` (config)
- `packages/test-rust-panic/src/Cargo.toml` (manifest)
- `packages/test-rust-panic/src/pyproject.toml` (manifest)
- `packages/test-rust-panic/src/setup.py` (manifest)
- `packages/test-sharedlib-py/meta.yaml` (config)
- `packages/test-sharedlib-py/src/setup.py` (manifest)
- `packages/test-sharedlib/meta.yaml` (config)
- `packages/test-simd/meta.yaml` (config)
- `packages/test-simd/src/setup.py` (manifest)
- `pyproject.toml` (manifest)
- `requirements-deploy.txt` (manifest)
- `requirements.txt` (manifest)
- `src/core/tsconfig.json` (config)
- `src/js/package.json` (manifest)
- `src/js/struct_info_generated.json` (config)
- `src/js/tsconfig.json` (config)
- `src/js/tsdoc.json` (config)
- `src/py/pyproject.toml` (manifest)
- `src/test-bun/package.json` (manifest)
- `src/test-deno/deno.json` (config)
- `src/test-js/package.json` (manifest)
- `src/test-js/tsconfig.json` (config)

## Top-level layout

- `src` — 198 analysed file(s)
- `packages` — 118 analysed file(s)
- `docs` — 74 analysed file(s)
- `benchmark` — 50 analysed file(s)
- `tools` — 42 analysed file(s)
- `(root files)` — 24 analysed file(s)
- `.github` — 14 analysed file(s)
- `cpython` — 14 analysed file(s)
- `emsdk` — 6 analysed file(s)
- `.devcontainer` — 4 analysed file(s)
- `metadata` — 3 analysed file(s)
- `.circleci` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 4 file(s) were skipped during inventory (1 x lockfile excluded; 3 x vendored/generated directory excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `ebb528e4e7ddf8758764c10091d6613e5ce4f1c8` is the revision these paths and observations refer to.
