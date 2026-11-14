# Project structure: deepseek-ai/DeepInfer

**Analysed commit:** `a679bb86ce36e883a98a97733492b686e5b9a08e`

**Commit reference:** [a679bb86ce36e883a98a97733492b686e5b9a08e](https://github.com/deepseek-ai/DeepInfer/commit/a679bb86ce36e883a98a97733492b686e5b9a08e)

**Tree at this commit:** [deepseek-ai/DeepInfer@a679bb86ce36](https://github.com/deepseek-ai/DeepInfer/tree/a679bb86ce36e883a98a97733492b686e5b9a08e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | deepseek-ai/DeepInfer |
| Description | DeepInfer: High-performance, large-scale inference framework for DeepSeek models |
| Stars | 26020 |
| Forks | 3194 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `a679bb86ce36e883a98a97733492b686e5b9a08e` |
| Retrieved at | 2026-11-14T19:07:27.619568+00:00 |
| Files in this snapshot | 336 |

## Directory tree

```text
csrc/  (33 files)
  engine/  (22 files)
    input_metadata/  (5 files)
      … 5 files under this directory
    block_manager.hpp
    flops_estimator.hpp
    mtp_varlen.hpp
    outputs.hpp
    prepare_sample.cpp
    prepare_sample.hpp
    process_output.hpp
    pybind.cpp
    pybind.hpp
    pybind_output.cpp
    pybind_scheduler.cpp
    pybind_sequence.cpp
    scheduler.hpp
    sequence.hpp
    utils.hpp
    zos.cpp
    zos.hpp
  graph_timer/  (4 files)
    graph_timer.hpp
    graph_timer_asc.cpp
    graph_timer_cuda.cpp
    pybind.cpp
  utils/  (3 files)
    lockable.hpp
    log.hpp
    object_pool.hpp
  asc_utils.cpp
  cuda_utils.cpp
  cuda_utils.hpp
  pybind.cpp
deep_cluster/  (8 files)
  hardware/  (5 files)
    __init__.py
    ascend.py
    cpu.py
    device.py
    nvidia.py
  topology/  (2 files)
    __init__.py
    bind.py
  __init__.py
deepinfer/  (223 files)
  _C/  (4 files)
    __init__.pyi
    cuda_utils.pyi
    engine.pyi
    graph_timer.pyi
  distributed/  (2 files)
    __init__.py
    shm_broadcast.py
  engine/  (6 files)
    __init__.py
    arg_utils.py
    engine_type.py
    llm_engine.py
    profile_server.py
    stats_logger.py
  entrypoints/  (2 files)
    __init__.py
    llm.py
  hugging_face/  (8 files)
    __init__.py
    config.py
    loading.py
    names.py
    parameters.py
    processor.py
    tokenizer.py
    weights.py
  model_executor/  (157 files)
    eplb/  (3 files)
      … 3 files under this directory
    input_metadata/  (5 files)
      … 5 files under this directory
    layers/  (102 files)
      … 102 files under this directory
    models/  (34 files)
      … 34 files under this directory
    parallel_utils/  (6 files)
      … 6 files under this directory
    __init__.py
    layer_utils.py
    model_loader.py
    model_metadata_utils.py
    model_output.py
    sampling_inputs.py
    utils.py
  npu_ops/  (4 files)
    __init__.py
    deep_select.py
    patch_imports.py
    vit_attn.py
  structure_output/  (5 files)
    __init__.py
    compiler.py
    mask.py
    matcher.py
    so_matcher_builder.py
  ve/  (9 files)
    processor/  (5 files)
      … 5 files under this directory
    __init__.py
    multimodal_processor.py
    prepare_tensor_input_vl.py
    schema.py
  worker/  (10 files)
    __init__.py
    base.py
    cache_engine.py
    cuda_graph_runner.py
    decode_perf_cache.py
    dflash_cuda_graph_runner.py
    model_runner.py
    runtime_config.py
    worker.py
    zos_status.py
  __init__.py
  attrdict.py
  config.py
  environ.py
  load_class.py
  logger.py
  model_config_loader.py
  multimodal_tokens.py
  platform.py
  py.typed
  sampling_params.py
  sequence.py
  shared_memory.py
  testing.py
  timer.py
  utils.py
doc/  (1 files)
  inference_deployment_qa.md
eval/  (17 files)
  aime/  (2 files)
    bench.py
    run.sh
  common/  (7 files)
    __init__.py
    encoder.py
    io.py
    judge.py
    loader.py
    passk.py
    paths.py
  gpqa/  (2 files)
    bench.py
    run.sh
  hle/  (2 files)
    bench.py
    run.sh
  .gitignore
  README.md
  run_eval.py
  score.py
examples/  (16 files)
  sweep/  (3 files)
    plot_pareto.py
    run_sweep.sh
    ve_sweep.py
  yoco/  (3 files)
    README.md
    run_yoco_equiv_l2.sh
    yoco_equiv.py
  README.md
  _config.py
  _launch.py
  _prompts.py
  _structured_output.py
  _trace.py
  _ve_helper.py
  benchmark.py
  offline_inference.py
  refresh_offline_decode_ppl.py
scripts/  (4 files)
  build.sh
  build_vendor.sh
  format_csrc.sh
  gen_stub.sh
tests/  (20 files)
  distributed/  (2 files)
    test_expert_shuffle.py
    test_shm_broadcast.py
  engine/  (3 files)
    test_flops_estimator.py
    test_mm_overwrite_prompt.py
    test_sequence.py
  models/  (9 files)
    _runner.py
    offline_decode_ppl.json
    test_batch_invariant.py
    test_eplb_policy.py
    test_kl.py
    test_offline_inference.py
    test_offline_inference_long.py
    test_sampler.py
    test_ve_batch_invariant.py
  ve/  (1 files)
    test_chunk_mm_metadata.py
  worker/  (2 files)
    test_state_cache_ops.py
    test_userbuffer.py
  __init__.py
  conftest.py
  test_cuda_sync_guards.py
.clang-format
.gitignore
.gitmodules
CONTRIBUTING.md
LICENSE
Makefile
README.md
build.sh
pyproject.toml
requirements-ascend.txt
requirements-dev.txt
requirements-nvidia.txt
requirements.txt
setup.py
```

## Entry points

- [deepinfer/engine/profile_server.py:182](https://github.com/deepseek-ai/DeepInfer/blob/a679bb86ce36e883a98a97733492b686e5b9a08e/deepinfer/engine/profile_server.py#L182)
- [eval/run_eval.py:308](https://github.com/deepseek-ai/DeepInfer/blob/a679bb86ce36e883a98a97733492b686e5b9a08e/eval/run_eval.py#L308)
- [eval/score.py:252](https://github.com/deepseek-ai/DeepInfer/blob/a679bb86ce36e883a98a97733492b686e5b9a08e/eval/score.py#L252)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 8 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: CacheConfig, ModelConfig, ParallelConfig, SchedulerConfig. Observed top-level functio… |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| csrc package | library | Observed | Groups 15 file(s) under csrc package (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 34 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AcceptRatePredictor, Attention, Block, ColumnParallelLora, CompressedTokenizer, CompressedVocabulary.… |
| deep_cluster package | library | Observed | Groups 8 file(s) under deep_cluster package (observed from repository paths and static analysis). Observed top-level classes: _Bitmask. Observed top-level functions: _device_node_indices, _entries, _libnuma, _npu_smi_nu… |
| deepinfer package | library | Observed | Groups 180 file(s) under deepinfer package (observed from repository paths and static analysis). Observed top-level classes: Aggregates, AttrDict, BaseInput, BaseProcessor, BaseTimer, BasicImageTransform. Observed top-l… |
| Application entry point | entrypoint | Observed | Groups 3 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed top-level classes: ProfileManager, _PendingTrace, _ProfileRe… |
| eval package | library | Observed | Groups 13 file(s) under eval package (observed from repository paths and static analysis). Observed top-level classes: LLMJudge, Problem. Observed top-level functions: _has_image, _hle_wording_verdict, _looks_like_repo,… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 4 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 21 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: Case, TestKVCacheLayoutCompressRatios, TestStateCacheOperationsBase, TestStateCacheOperationsWithExtraSizeZ… |

## Important files

- `pyproject.toml` (manifest)
- `requirements-ascend.txt` (manifest)
- `requirements-dev.txt` (manifest)
- `requirements-nvidia.txt` (manifest)
- `requirements.txt` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `deepinfer` — 223 analysed file(s)
- `csrc` — 33 analysed file(s)
- `tests` — 20 analysed file(s)
- `eval` — 17 analysed file(s)
- `examples` — 16 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `deep_cluster` — 8 analysed file(s)
- `scripts` — 4 analysed file(s)
- `doc` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `a679bb86ce36e883a98a97733492b686e5b9a08e` is the revision these paths and observations refer to.
