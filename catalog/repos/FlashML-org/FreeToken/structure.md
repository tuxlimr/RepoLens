# Project structure: FlashML-org/FreeToken

**Analysed commit:** `4b71d4d928e968c7036024c089f81050134a680b`

**Commit reference:** [4b71d4d928e968c7036024c089f81050134a680b](https://github.com/FlashML-org/FreeToken/commit/4b71d4d928e968c7036024c089f81050134a680b)

**Tree at this commit:** [FlashML-org/FreeToken@4b71d4d928e9](https://github.com/FlashML-org/FreeToken/tree/4b71d4d928e968c7036024c089f81050134a680b)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | FlashML-org/FreeToken |
| Description | FreeToken brings datacenter-scale model serving to your desktop. Run massive models locally, fast and efficiently. |
| Stars | 17188 |
| Forks | 1704 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `4b71d4d928e968c7036024c089f81050134a680b` |
| Retrieved at | 2026-11-14T19:08:37.402149+00:00 |
| Files in this snapshot | 794 |

## Directory tree

```text
.github/  (11 files)
  ISSUE_TEMPLATE/  (5 files)
    bug_desktop.yml
    bug_engine.yml
    config.yml
    feature_request.yml
    model_checkpoint.yml
  workflows/  (4 files)
    issue-labels.yml
    nightly-wheels.yml
    promote-beta.yml
    release.yml
  issue-labeler.yml
  issue-title-labeler.yml
assets/  (4 files)
  freetoken-icon.svg
  freetoken-logo-dark.svg
  freetoken-logo-light.svg
  freetoken-logo.svg
benchmarks/  (4 files)
  README.md
  bench_decode_moe.py
  bench_load_weight_generic.py
  bench_offload_cache_copy.py
docs/  (9 files)
  performance/  (2 files)
    decode.md
    prefill.md
  cli.md
  ftw-hotfix.md
  ggml-kernels.md
  install.md
  install_amd.md
  models.md
  quickstart.md
freetoken-kernel-cache/  (5 files)
  freetoken_kernel_cache/  (1 files)
    __init__.py
  README.md
  build_backend.py
  pyproject.toml
  setup.py
python/  (634 files)
  freetoken/  (634 files)
    attention/  (17 files)
      … 17 files under this directory
    benchmark/  (2 files)
      … 2 files under this directory
    checkpoint/  (4 files)
      … 4 files under this directory
    daemon/  (18 files)
      … 18 files under this directory
    distributed/  (3 files)
      … 3 files under this directory
    engine/  (7 files)
      … 7 files under this directory
    kernel/  (215 files)
      … 215 files under this directory
    kvcache/  (21 files)
      … 21 files under this directory
    layers/  (48 files)
      … 48 files under this directory
    llm/  (2 files)
      … 2 files under this directory
    message/  (5 files)
      … 5 files under this directory
    mm/  (12 files)
      … 12 files under this directory
    models/  (181 files)
      … 181 files under this directory
    moe/  (18 files)
      … 18 files under this directory
    scheduler/  (11 files)
      … 11 files under this directory
    server/  (20 files)
      … 20 files under this directory
    shell/  (5 files)
      … 5 files under this directory
    spec/  (13 files)
      … 13 files under this directory
    third_party/  (7 files)
      … 7 files under this directory
    tokenizer/  (6 files)
      … 6 files under this directory
    utils/  (9 files)
      … 9 files under this directory
    __init__.py
    __main__.py
    cache_report.py
    cli.py
    control_cli.py
    core.py
    env.py
    gpu_select.py
    launch.py
    version.py
scripts/  (19 files)
  checkpoint_diagnose/  (6 files)
    README.md
    ckpt_edit.py
    diagnose.py
    fetch_headers.py
    fix_config.py
    rename_tensors.py
  ci/  (3 files)
    fetch-nightly-pair.sh
    manylinux-build.sh
    retag-manylinux.py
  gguf_check/  (5 files)
    README.md
    check.py
    fetch_headers.py
    probe_kernels.py
    tok_compare.py
  build-release-wheels.sh
  ftw_hotfix.py
  make_token_map.py
  publish-wheels.sh
  sync-llama-cpp.sh
tests/  (98 files)
  attention/  (3 files)
    test_capture_rows_per_req.py
    test_dsa_kpool.py
    test_dsv41_backend.py
  checkpoint/  (2 files)
    test_ftw_hotfix_vision.py
    test_ftw_weights.py
  daemon/  (3 files)
    __init__.py
    test_daemon_import_safety.py
    test_daemon_serve_manager.py
  dsv4/  (1 files)
    test_dsv4_attn_backend.py
  e2e/  (3 files)
    __init__.py
    test_aime.py
    test_cache_rebuild.py
  engine/  (8 files)
    __init__.py
    test_attention_backend_arch.py
    test_attention_backend_matrix.py
    test_cache_budget.py
    test_graph.py
    test_mm_encoder.py
    test_mm_repeated_image.py
    test_moe_cpu_layers.py
  kernels/  (28 files)
    __init__.py
    test_dflash.py
    test_dsv41_indexer.py
    test_dsv41_pack.py
    test_dsv41_sparse_attn.py
    test_dsv41_topk.py
    test_dsv4_fp8_block_linear.py
    test_dsv4_indexer_decode.py
    test_dsv4_router_select.py
    test_dsv4_sparse_attn.py
    test_e4m3_compat.py
    test_fp8_blockscale_moe.py
    test_fp8_pertensor_linear.py
    test_gemma4_fused_ops.py
    test_ggml.py
    test_kda.py
    test_kernel_cache_version.py
    test_minimax_m3_sparse.py
    test_mrope.py
    test_mxfp8_linear.py
    test_nvfp4_w4a4_linear.py
    test_pinned_tensor.py
    test_rocm_launch_kwargs.py
    test_rotary.py
    … 4 more files
  kvcache/  (24 files)
    radix/  (10 files)
      … 10 files under this directory
    __init__.py
    test_bsa_pool.py
    test_cache_unit_bytes.py
    test_dsa_pool.py
    test_dsv41_pool.py
    test_dsv4_free_list.py
    test_dsv4_pool.py
    test_hybrid_linear_paged_pools.py
    test_hybrid_swa_kv_cache.py
    test_kv_cache_rebuild.py
    test_linear_state_pool_alloc.py
    test_pool_sizing_surface.py
    test_qsa_pool.py
    test_swa_paged_pool.py
  layers/  (2 files)
    test_gdn.py
    test_mhc.py
  mm/  (2 files)
    test_encoder_cache.py
    test_processor.py
  models/  (16 files)
    deepseek_v41/  (9 files)
      … 9 files under this directory
    dflash/  (1 files)
      … 1 files under this directory
    gemma4/  (1 files)
      … 1 files under this directory
    qwen4_exp/  (2 files)
      … 2 files under this directory
    ricursive/  (1 files)
      … 1 files under this directory
    __init__.py
    test_models_registry.py
  moe/  (1 files)
    __init__.py
  scheduler/  (1 files)
    __init__.py
  server/  (1 files)
    __init__.py
  tokenizer/  (1 files)
    __init__.py
  README.md
  conftest.py
.gitignore
AGENTS.md
CLAUDE.md
CONTRIBUTING.md
LICENSE
README.md
SECURITY.md
install.sh
pyproject.toml
setup.py
```

## Entry points

- [benchmarks/bench_decode_moe.py:452](https://github.com/FlashML-org/FreeToken/blob/4b71d4d928e968c7036024c089f81050134a680b/benchmarks/bench_decode_moe.py#L452)
- [benchmarks/bench_load_weight_generic.py:366](https://github.com/FlashML-org/FreeToken/blob/4b71d4d928e968c7036024c089f81050134a680b/benchmarks/bench_load_weight_generic.py#L366)
- [benchmarks/bench_offload_cache_copy.py:252](https://github.com/FlashML-org/FreeToken/blob/4b71d4d928e968c7036024c089f81050134a680b/benchmarks/bench_offload_cache_copy.py#L252)
- [python/freetoken/checkpoint/__main__.py:76](https://github.com/FlashML-org/FreeToken/blob/4b71d4d928e968c7036024c089f81050134a680b/python/freetoken/checkpoint/__main__.py#L76)
- [python/freetoken/cli.py:129](https://github.com/FlashML-org/FreeToken/blob/4b71d4d928e968c7036024c089f81050134a680b/python/freetoken/cli.py#L129)
- [python/freetoken/control_cli.py:507](https://github.com/FlashML-org/FreeToken/blob/4b71d4d928e968c7036024c089f81050134a680b/python/freetoken/control_cli.py#L507)
- [python/freetoken/daemon/app.py:135](https://github.com/FlashML-org/FreeToken/blob/4b71d4d928e968c7036024c089f81050134a680b/python/freetoken/daemon/app.py#L135)
- [python/freetoken/daemon/client.py:205](https://github.com/FlashML-org/FreeToken/blob/4b71d4d928e968c7036024c089f81050134a680b/python/freetoken/daemon/client.py#L205)
- [python/freetoken/launch.py:1108](https://github.com/FlashML-org/FreeToken/blob/4b71d4d928e968c7036024c089f81050134a680b/python/freetoken/launch.py#L1108)
- [python/freetoken/moe/benchbw.py:1146](https://github.com/FlashML-org/FreeToken/blob/4b71d4d928e968c7036024c089f81050134a680b/python/freetoken/moe/benchbw.py#L1146)
- [python/freetoken/server/api_server.py:470](https://github.com/FlashML-org/FreeToken/blob/4b71d4d928e968c7036024c089f81050134a680b/python/freetoken/server/api_server.py#L470)
- [python/freetoken/server/launch.py:227](https://github.com/FlashML-org/FreeToken/blob/4b71d4d928e968c7036024c089f81050134a680b/python/freetoken/server/launch.py#L227)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 15 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: BuildClib, BuildExt, CompressedTensorsConfig, EngineConfig, Fp8BlockConfig, GGUFConf… |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 181 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: Attention, BaseAttentionGroupConfig, BaseLLMModel, Block, BlockWeightStreamer, Compressor. Observed t… |
| Application entry point | entrypoint | Observed | Groups 30 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed routes: POST /v1/cache/rebuild, API_ROUTE /v1/cache/flush,… |
| External integrations | external | Observed | Groups 6 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: BenchOneResult, BenchmarkResult, BenchmarkTrace, Console, ContentDelta, Counter. Observed to… |
| freetoken-kernel-cache package | library | Observed | Groups 2 file(s) under freetoken-kernel-cache package (observed from repository paths and static analysis). Observed top-level functions: _build_jit_cache, _check_toolchain, _cuda_version_suffix, _ensure_freetoken_impor… |
| python package | library | Observed | Groups 351 file(s) under python package (observed from repository paths and static analysis). Observed top-level classes: AbortBackendMsg, AbortMsg, AccountingDrainError, AccountingError, AccountingOutbox, AccountingOut… |
| scripts package | library | Observed | Groups 6 file(s) under scripts package (observed from repository paths and static analysis). Observed top-level classes: Checkpoint. Observed top-level functions: _copy_range, _fsync_dir, _shared, check_out_dir, confirm… |
| Tests | test | Observed | Groups 98 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: Adapter, Aligner, Attention, Block, CacheSpec, EngramLayout. Observed top-level functions: _activation, _al… |

## Important files

- `.github/ISSUE_TEMPLATE/bug_desktop.yml` (config)
- `.github/ISSUE_TEMPLATE/bug_engine.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/ISSUE_TEMPLATE/model_checkpoint.yml` (config)
- `.github/issue-labeler.yml` (config)
- `.github/issue-title-labeler.yml` (config)
- `.github/workflows/issue-labels.yml` (ci)
- `.github/workflows/nightly-wheels.yml` (ci)
- `.github/workflows/promote-beta.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `freetoken-kernel-cache/pyproject.toml` (manifest)
- `freetoken-kernel-cache/setup.py` (manifest)
- `pyproject.toml` (manifest)
- `python/freetoken/moe/configs/triton_3_5_1/E=128,N=704,device_name=NVIDIA_H100_80GB_HBM3.json` (config)
- `setup.py` (manifest)

## Top-level layout

- `python` — 634 analysed file(s)
- `tests` — 98 analysed file(s)
- `scripts` — 19 analysed file(s)
- `.github` — 11 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `docs` — 9 analysed file(s)
- `freetoken-kernel-cache` — 5 analysed file(s)
- `assets` — 4 analysed file(s)
- `benchmarks` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `4b71d4d928e968c7036024c089f81050134a680b` is the revision these paths and observations refer to.
