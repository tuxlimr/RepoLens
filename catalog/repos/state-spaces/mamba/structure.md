# Project structure: state-spaces/mamba

**Analysed commit:** `e9594ce1c732d97440f0332fdc43170a2294dbfa`

**Commit reference:** [e9594ce1c732d97440f0332fdc43170a2294dbfa](https://github.com/state-spaces/mamba/commit/e9594ce1c732d97440f0332fdc43170a2294dbfa)

**Tree at this commit:** [state-spaces/mamba@e9594ce1c732](https://github.com/state-spaces/mamba/tree/e9594ce1c732d97440f0332fdc43170a2294dbfa)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | state-spaces/mamba |
| Description | Mamba SSM architecture |
| Stars | 19005 |
| Forks | 1840 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `e9594ce1c732d97440f0332fdc43170a2294dbfa` |
| Retrieved at | 2026-11-14T19:08:19.692358+00:00 |
| Files in this snapshot | 104 |

## Directory tree

```text
.github/  (10 files)
  scripts/  (4 files)
    build.sh
    check_for_ngc_images.sh
    check_for_releases.sh
    test.sh
  workflows/  (6 files)
    _build.yml
    _build_in_container.yml
    build.yml
    build_in_container.yml
    build_in_container_scheduled.yml
    publish.yaml
benchmarks/  (1 files)
  benchmark_generation_mamba_simple.py
csrc/  (17 files)
  selective_scan/  (17 files)
    reverse_scan.cuh
    selective_scan.cpp
    selective_scan.h
    selective_scan_bwd_bf16_complex.cu
    selective_scan_bwd_bf16_real.cu
    selective_scan_bwd_fp16_complex.cu
    selective_scan_bwd_fp16_real.cu
    selective_scan_bwd_fp32_complex.cu
    selective_scan_bwd_fp32_real.cu
    selective_scan_bwd_kernel.cuh
    selective_scan_common.h
    selective_scan_fwd_bf16.cu
    selective_scan_fwd_fp16.cu
    selective_scan_fwd_fp32.cu
    selective_scan_fwd_kernel.cuh
    static_switch.h
    uninitialized_copy.cuh
evals/  (1 files)
  lm_harness_eval.py
mamba_ssm/  (54 files)
  distributed/  (3 files)
    __init__.py
    distributed_utils.py
    tensor_parallel.py
  models/  (3 files)
    __init__.py
    config_mamba.py
    mixer_seq_simple.py
  modules/  (9 files)
    __init__.py
    block.py
    mamba2.py
    mamba2_simple.py
    mamba3.py
    mamba_simple.py
    mha.py
    mlp.py
    ssd_minimal.py
  ops/  (33 files)
    cute/  (3 files)
      … 3 files under this directory
    tilelang/  (7 files)
      … 7 files under this directory
    triton/  (21 files)
      … 21 files under this directory
    __init__.py
    selective_scan_interface.py
  utils/  (5 files)
    __init__.py
    determinism.py
    generation.py
    hf.py
    torch.py
  __init__.py
rocm_patch/  (1 files)
  rocm6_0.patch
tests/  (11 files)
  modules/  (1 files)
    test_mamba3_varlen.py
  ops/  (7 files)
    cute/  (1 files)
      … 1 files under this directory
    tilelang/  (1 files)
      … 1 files under this directory
    triton/  (4 files)
      … 4 files under this directory
    test_selective_scan.py
  benchmark_determinism_kernels.py
  test_determinism.py
  test_generation.py
.gitignore
.gitmodules
AUTHORS
LICENSE
MANIFEST.in
README.md
pyproject.toml
setup.py
usage.md
```

## Entry points

- [evals/lm_harness_eval.py:38](https://github.com/state-spaces/mamba/blob/e9594ce1c732d97440f0332fdc43170a2294dbfa/evals/lm_harness_eval.py#L38)
- [mamba_ssm/ops/cute/mamba3/mamba3_step_fn.py:820](https://github.com/state-spaces/mamba/blob/e9594ce1c732d97440f0332fdc43170a2294dbfa/mamba_ssm/ops/cute/mamba3/mamba3_step_fn.py#L820)
- [mamba_ssm/ops/triton/mamba3/mamba3_mimo_rotary_step.py:396](https://github.com/state-spaces/mamba/blob/e9594ce1c732d97440f0332fdc43170a2294dbfa/mamba_ssm/ops/triton/mamba3/mamba3_mimo_rotary_step.py#L396)
- [mamba_ssm/ops/triton/mamba3/mamba3_mimo_utils.py:1847](https://github.com/state-spaces/mamba/blob/e9594ce1c732d97440f0332fdc43170a2294dbfa/mamba_ssm/ops/triton/mamba3/mamba3_mimo_utils.py#L1847)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| benchmarks package | library | Observed | Groups 1 file(s) under benchmarks package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: CachedWheelsCommand. Observed top-level functions: append_nvcc_threads, check_if_cuda… |
| csrc package | library | Observed | Groups 4 file(s) under csrc package (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 3 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: MambaConfig, MambaLMHeadModel, MixerModel. Observed top-level functions: _init_weights, create_block. |
| Application entry point | entrypoint | Observed | Groups 4 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Mamba3Step, MambaEvalWrapper. Observed top-level functions: _build_varlen_chunk_mapping, _… |
| mamba_ssm package | library | Observed | Groups 48 file(s) under mamba_ssm package (observed from repository paths and static analysis). Observed top-level classes: AllGatherFunc, AllReduceFunc, Block, ChunkScanFn, ChunkStateFn, ColumnParallelEmbedding. Observ… |
| Tests | test | Observed | Groups 11 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: InferenceParams, RunOutputs, VariantConfig. Observed top-level functions: _assert_close, _case_config, _cu_… |

## Important files

- `.github/workflows/_build.yml` (ci)
- `.github/workflows/_build_in_container.yml` (ci)
- `.github/workflows/build.yml` (ci)
- `.github/workflows/build_in_container.yml` (ci)
- `.github/workflows/build_in_container_scheduled.yml` (ci)
- `.github/workflows/publish.yaml` (ci)
- `MANIFEST.in` (manifest)
- `pyproject.toml` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `mamba_ssm` — 54 analysed file(s)
- `csrc` — 17 analysed file(s)
- `tests` — 11 analysed file(s)
- `.github` — 10 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `benchmarks` — 1 analysed file(s)
- `evals` — 1 analysed file(s)
- `rocm_patch` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `e9594ce1c732d97440f0332fdc43170a2294dbfa` is the revision these paths and observations refer to.
