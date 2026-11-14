# Project structure: cupy/cupy

**Analysed commit:** `e41e2961f74ee2b1c2b50265f3104f0885e74623`

**Commit reference:** [e41e2961f74ee2b1c2b50265f3104f0885e74623](https://github.com/cupy/cupy/commit/e41e2961f74ee2b1c2b50265f3104f0885e74623)

**Tree at this commit:** [cupy/cupy@e41e2961f74e](https://github.com/cupy/cupy/tree/e41e2961f74ee2b1c2b50265f3104f0885e74623)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | cupy/cupy |
| Description | NumPy & SciPy for GPU |
| Stars | 12408 |
| Forks | 1164 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `e41e2961f74ee2b1c2b50265f3104f0885e74623` |
| Retrieved at | 2026-11-14T19:10:08.513123+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.github/  (31 files)
  ISSUE_TEMPLATE/  (4 files)
    bug.yml
    config.yml
    documentation.yml
    feature.yml
  actions/  (5 files)
    fetch_ctk/  (1 files)
      … 1 files under this directory
    free-disk-space/  (1 files)
      … 1 files under this directory
    install_unix_deps/  (1 files)
      … 1 files under this directory
    sccache-summary/  (1 files)
      … 1 files under this directory
    update-pip/  (1 files)
      … 1 files under this directory
  workflows/  (19 files)
    scripts/  (3 files)
      … 3 files under this directory
    auto-cc.yml
    backport-reminder.yml
    backport.yml
    build-sdist.yml
    build-wheel.yml
    ci-nightly.yml
    ci-trigger.yml
    ci.yml
    docker.yml
    docs.yml
    flexci.yml
    pr-project.yml
    pr-updated.yml
    pretest.yml
    publish.yml
    self-hosted-ci.yml
  CODEOWNERS
  CONTRIBUTING.md
  dependabot.yml
.pfnci/  (113 files)
  linux/  (97 files)
    tests/  (90 files)
      … 90 files under this directory
    README.md
    main-flexci-prep.sh
    main-flexci-stable.sh
    main-flexci.sh
    main-self-hosted-ci.sh
    run.sh
    update-cuda-driver.sh
  windows/  (4 files)
    _error_handler.ps1
    _flexci.ps1
    run.bat
    test.ps1
  .gitattributes
  BRANCH
  BRANCH_STABLE
  README.md
  config.pbtxt
  config.tags.json
  coverage.rst
  flexci_notify.py
  generate.py
  matrix.yaml
  schema.yaml
  trim_cupy_kernel_cache.py
ci/  (7 files)
  tools/  (6 files)
    ci-guard.sh
    env-vars
    fetch_ctk_redistrib.py
    prepare_sdist_build.py
    prepare_wheel_build.py
    wheel_configs.py
  versions.yml
cupy/  (272 files)
  _binary/  (3 files)
    __init__.py
    elementwise.py
    packing.py
  _core/  (107 files)
    include/  (39 files)
      … 39 files under this directory
    __init__.pxd
    __init__.py
    _accelerator.pxd
    _accelerator.pyx
    _carray.pxd
    _carray.pyx
    _codeblock.py
    _cub_reduction.pxd
    _cub_reduction.pyx
    _cuda_compute_common.pxd
    _cuda_compute_common.pyx
    _cuda_compute_histogram.py
    _cuda_compute_reduction.pxd
    _cuda_compute_reduction.pyx
    _cuda_compute_scan.pxd
    _cuda_compute_scan.pyx
    _dtype.pxd
    _dtype.pyx
    _fusion_interface.py
    _fusion_kernel.pyx
    _fusion_op.py
    _fusion_optimization.py
    _fusion_thread_local.pyx
    _fusion_trace.pyx
    … 44 more files
  _creation/  (5 files)
    __init__.py
    basic.py
    from_data.py
    matrix.py
    ranges.py
  _functional/  (3 files)
    __init__.py
    piecewise.py
    vectorize.py
  _indexing/  (5 files)
    __init__.py
    generate.py
    indexing.py
    insert.py
    iterate.py
  _io/  (4 files)
    __init__.py
    formatting.py
    npz.py
    text.py
  _logic/  (6 files)
    __init__.py
    comparison.py
    content.py
    ops.py
    truth.py
    type_testing.py
  _manipulation/  (11 files)
    __init__.py
    add_remove.py
    basic.py
    dims.py
    join.py
    kind.py
    rearrange.py
    shape.py
    split.py
    tiling.py
    transpose.py
  _math/  (13 files)
    __init__.py
    arithmetic.py
    explog.py
    floating.py
    hyperbolic.py
    misc.py
    rational.py
    rounding.py
    special.py
    sumprod.py
    trigonometric.py
    ufunc.py
    window.py
  _misc/  (4 files)
    __init__.py
    byte_bounds.py
    memory_ranges.py
    who.py
  _padding/  (2 files)
    __init__.py
    pad.py
  _sorting/  (4 files)
    __init__.py
    count.py
    search.py
    sort.py
  _statistics/  (5 files)
    __init__.py
    correlation.py
    histogram.py
    meanvar.py
    order.py
  cuda/  (44 files)
    memory_hooks/  (3 files)
      … 3 files under this directory
    __init__.pxd
    __init__.py
    _compiler_cache.py
    common.pxd
    common.pyx
    compiler.py
    cub.pxd
    cub.pyx
    cufft.pxd
    cufft.pyx
    cupy_cub.cu
    cupy_cub.h
    cupy_cufft.h
    cupy_cufftXt.cu
    cupy_cufftXt.h
    cupy_jitify.h
    cupy_thrust.cu
    cupy_thrust.h
    cutensor.py
    device.pxd
    device.pyx
    function.pxd
    function.pyx
    graph.pxd
    … 17 more files
  exceptions/  (1 files)
    __init__.py
  fft/  (6 files)
    __init__.pxd
    __init__.py
    _cache.pyx
    _callback.pyx
    _config.py
    _fft.py
  lib/  (5 files)
    __init__.py
    _polynomial.pyx
    _routines_poly.py
    _shape_base.py
    stride_tricks.py
  linalg/  (10 files)
    __init__.py
    _decomposition.py
    _eigenvalue.py
    _einsum.py
    _einsum_cutn.py
    _einsum_opt.py
    _norms.py
    _product.py
    _solve.py
    _util.py
  polynomial/  (3 files)
    __init__.py
    polynomial.py
    polyutils.py
  random/  (11 files)
    LICENSE
    __init__.py
    _bit_generator.pyx
    _distributions.py
    _generator.py
    _generator_api.pyx
    _kernels.py
    _permutations.py
    _sample.py
    cupy_distributions.cu
    cupy_distributions.cuh
  testing/  (12 files)
    __init__.py
    _array.py
    _attr.py
    _bundle.py
    _condition.py
    _helper.py
    _hypothesis.py
    _loops.py
    _parameterized.py
    _protocol_helpers.py
    _pytest_impl.py
    _random.py
  typing/  (2 files)
    __init__.py
    _types.py
  __init__.py
  _environment.py
  _util.pyi
  _util.pyx
  _version.py
  cublas.py
cupy_backends/  (75 files)
  cuda/  (48 files)
    api/  (15 files)
      … 15 files under this directory
    libs/  (19 files)
      … 19 files under this directory
    __init__.pxd
    __init__.py
    _softlink.pxd
    _softlink.pyx
    cupy_cublas.h
    cupy_cuda.h
    cupy_cuda_profiler_api.h
    cupy_cuda_runtime.h
    cupy_cusolver.h
    cupy_cusparse.h
    cupy_cutensor.h
    cupy_nccl.h
    stream.pxd
    stream.pyx
  hip/  (13 files)
    cupy_cuComplex.h
    cupy_cusparselt.h
    cupy_cutensor.h
    cupy_hip.h
    cupy_hip_common.h
    cupy_hip_runtime.h
    cupy_hipblas.h
    cupy_hiprand.h
    cupy_nvtx.h
    cupy_profiler.h
    cupy_rccl.h
    cupy_rocsolver.h
    cupy_roctx.h
  __init__.pxd
  __init__.py
  cupy_backend.h
  cupy_backend_runtime.h
  cupy_blas.h
  cupy_complex.h
  cupy_cusparselt.h
  cupy_cutensor.h
  cupy_lapack.h
  cupy_nccl.h
  cupy_profiler.h
  cupy_rand.h
  cupy_sparse.h
  cupy_tx.h
cupyx/  (217 files)
  distributed/  (16 files)
    array/  (9 files)
      … 9 files under this directory
    __init__.py
    _comm.py
    _init.py
    _klv_utils.py
    _nccl_comm.py
    _store.py
    _store_actions.py
  jit/  (10 files)
    __init__.py
    _builtin_funcs.py
    _compile.py
    _cuda_typerules.py
    _cuda_types.py
    _interface.py
    _internal_types.py
    cg.py
    cub.py
    thrust.py
  linalg/  (4 files)
    sparse/  (2 files)
      … 2 files under this directory
    __init__.py
    _solve.py
  optimizing/  (2 files)
    __init__.py
    _optimize.py
  profiler/  (4 files)
    __init__.py
    _time.py
    _time_range.py
    _timeit_magic.py
  scipy/  (153 files)
    _lib/  (2 files)
      … 2 files under this directory
    fft/  (5 files)
      … 5 files under this directory
    fftpack/  (2 files)
      … 2 files under this directory
    interpolate/  (12 files)
      … 12 files under this directory
    linalg/  (7 files)
      … 7 files under this directory
    ndimage/  (20 files)
      … 20 files under this directory
    signal/  (27 files)
      … 27 files under this directory
    sparse/  (23 files)
      … 23 files under this directory
    spatial/  (9 files)
      … 9 files under this directory
    special/  (40 files)
      … 40 files under this directory
    stats/  (5 files)
      … 5 files under this directory
    __init__.py
  signal/  (10 files)
    _acoustics/  (2 files)
      … 2 files under this directory
    _convolution/  (2 files)
      … 2 files under this directory
    _filtering/  (2 files)
      … 2 files under this directory
    _radartools/  (3 files)
      … 3 files under this directory
    __init__.py
  tools/  (3 files)
    __init__.py
    _generate_wheel_metadata.py
    install_library.py
  __init__.py
  _cusolver.pyx
  _cutensor.pyx
  _gufunc.py
  _pinned_array.py
  _rsqrt.py
  _runtime.py
  _scatter.py
  _texture.py
  _ufunc_config.py
  cusolver.py
  cusparse.py
  cutensor.py
  lapack.py
  time.py
docker/  (3 files)
  python3/  (1 files)
    Dockerfile
  rocm/  (2 files)
    Dockerfile
    README.md
docs/  (72 files)
  image/  (1 files)
    cupy_logo.svg
  source/  (68 files)
    _templates/  (1 files)
      … 1 files under this directory
    reference/  (54 files)
      … 54 files under this directory
    user_guide/  (3 files)
      … 3 files under this directory
    .gitignore
    _comparison_generator.py
    conf.py
    contribution.rst
    index.rst
    install.rst
    license.rst
    overview.rst
    spelling_wordlist.txt
    upgrade.rst
  Makefile
  make.bat
  requirements.txt
.gitignore
.gitmodules
.mergify.yml
.pre-commit-config.yaml
CITATION.bib
CODE_OF_CONDUCT.md
LICENSE
MANIFEST.in
README.md
codecov.yml
```

## Entry points

- [.github/workflows/scripts/backport_reminder.py:121](https://github.com/cupy/cupy/blob/e41e2961f74ee2b1c2b50265f3104f0885e74623/.github/workflows/scripts/backport_reminder.py#L121)
- [.github/workflows/scripts/flexci_dispatcher.py:309](https://github.com/cupy/cupy/blob/e41e2961f74ee2b1c2b50265f3104f0885e74623/.github/workflows/scripts/flexci_dispatcher.py#L309)
- [.pfnci/flexci_notify.py:54](https://github.com/cupy/cupy/blob/e41e2961f74ee2b1c2b50265f3104f0885e74623/.pfnci/flexci_notify.py#L54)
- [.pfnci/generate.py:773](https://github.com/cupy/cupy/blob/e41e2961f74ee2b1c2b50265f3104f0885e74623/.pfnci/generate.py#L773)
- [.pfnci/trim_cupy_kernel_cache.py:85](https://github.com/cupy/cupy/blob/e41e2961f74ee2b1c2b50265f3104f0885e74623/.pfnci/trim_cupy_kernel_cache.py#L85)
- [ci/tools/fetch_ctk_redistrib.py:170](https://github.com/cupy/cupy/blob/e41e2961f74ee2b1c2b50265f3104f0885e74623/ci/tools/fetch_ctk_redistrib.py#L170)
- [ci/tools/prepare_sdist_build.py:33](https://github.com/cupy/cupy/blob/e41e2961f74ee2b1c2b50265f3104f0885e74623/ci/tools/prepare_sdist_build.py#L33)
- [ci/tools/prepare_wheel_build.py:212](https://github.com/cupy/cupy/blob/e41e2961f74ee2b1c2b50265f3104f0885e74623/ci/tools/prepare_wheel_build.py#L212)
- [cupyx/tools/_generate_wheel_metadata.py:79](https://github.com/cupy/cupy/blob/e41e2961f74ee2b1c2b50265f3104f0885e74623/cupyx/tools/_generate_wheel_metadata.py#L79)
- [cupyx/tools/install_library.py:299](https://github.com/cupy/cupy/blob/e41e2961f74ee2b1c2b50265f3104f0885e74623/cupyx/tools/install_library.py#L299)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 1 file(s) under api layer (observed from repository paths and static analysis). |
| ci package | library | Observed | Groups 2 file(s) under ci package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| cupy package | library | Observed | Groups 159 file(s) under cupy package (observed from repository paths and static analysis). Observed top-level classes: AxisConcatenator, CClass, CodeBlock, CompileException, DebugPrintHook, DeviceSynchronized. Observed… |
| cupy_backends package | library | Observed | Groups 36 file(s) under cupy_backends package (observed from repository paths and static analysis). Observed top-level functions: __getattr__. |
| cupyx package | library | Observed | Groups 210 file(s) under cupyx package (observed from repository paths and static analysis). Observed top-level classes: ActTriMode, ActionError, Actions, Akima1DInterpolator, ArrayBase, AtomicOp. Observed top-level fun… |
| Application entry point | entrypoint | Observed | Groups 5 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: __make_cutensor_record, _apply_prefix, _generate_wheel_metadata, _get_records, _make_cut… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 90 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/ISSUE_TEMPLATE/bug.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/documentation.yml` (config)
- `.github/ISSUE_TEMPLATE/feature.yml` (config)
- `.github/actions/fetch_ctk/action.yml` (config)
- `.github/actions/free-disk-space/action.yml` (config)
- `.github/actions/install_unix_deps/action.yml` (config)
- `.github/actions/sccache-summary/action.yml` (config)
- `.github/actions/update-pip/action.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/auto-cc.yml` (ci)
- `.github/workflows/backport-reminder.yml` (ci)
- `.github/workflows/backport.yml` (ci)
- `.github/workflows/build-sdist.yml` (ci)
- `.github/workflows/build-wheel.yml` (ci)
- `.github/workflows/ci-nightly.yml` (ci)
- `.github/workflows/ci-trigger.yml` (ci)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/docker.yml` (ci)
- `.github/workflows/docs.yml` (ci)
- `.github/workflows/flexci.yml` (ci)
- `.github/workflows/pr-project.yml` (ci)
- `.github/workflows/pr-updated.yml` (ci)
- `.github/workflows/pretest.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.github/workflows/scripts/backport_reminder.py` (ci)
- `.github/workflows/scripts/flexci_dispatcher.py` (ci)
- `.github/workflows/scripts/pretest-rocm-test.sh` (ci)
- `.github/workflows/self-hosted-ci.yml` (ci)
- `.mergify.yml` (config)
- `.pfnci/config.tags.json` (config)
- `.pfnci/matrix.yaml` (config)
- `.pfnci/schema.yaml` (config)
- `.pre-commit-config.yaml` (config)
- `MANIFEST.in` (manifest)
- `ci/versions.yml` (config)
- `codecov.yml` (config)
- `docker/python3/Dockerfile` (container)
- `docker/rocm/Dockerfile` (container)
- `docs/requirements.txt` (manifest)

## Top-level layout

- `cupy` — 272 analysed file(s)
- `cupyx` — 217 analysed file(s)
- `.pfnci` — 113 analysed file(s)
- `cupy_backends` — 75 analysed file(s)
- `docs` — 72 analysed file(s)
- `.github` — 31 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `ci` — 7 analysed file(s)
- `docker` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `e41e2961f74ee2b1c2b50265f3104f0885e74623` is the revision these paths and observations refer to.
