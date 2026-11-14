# Project structure: Dao-AILab/flash-attention

**Analysed commit:** `f63c472c4dc19237c0635d6a629df065ff64796e`

**Commit reference:** [f63c472c4dc19237c0635d6a629df065ff64796e](https://github.com/Dao-AILab/flash-attention/commit/f63c472c4dc19237c0635d6a629df065ff64796e)

**Tree at this commit:** [Dao-AILab/flash-attention@f63c472c4dc1](https://github.com/Dao-AILab/flash-attention/tree/f63c472c4dc19237c0635d6a629df065ff64796e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Dao-AILab/flash-attention |
| Description | Fast and memory-efficient exact attention |
| Stars | 25293 |
| Forks | 3229 |
| Licence | BSD-3-Clause |
| Language | Python |
| Default branch | main |
| Analysed commit | `f63c472c4dc19237c0635d6a629df065ff64796e` |
| Retrieved at | 2026-11-14T19:07:31.514120+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.github/  (10 files)
  actions/  (1 files)
    gpu-test/  (1 files)
      … 1 files under this directory
  scripts/  (2 files)
    bump_beta_tag.py
    test_ci_local.sh
  workflows/  (7 files)
    README.md
    _build.yml
    build.yml
    ci.yml
    pre-commit.yaml
    publish-fa4.yml
    publish.yml
AI/  (16 files)
  CLC_TRACE_DEBUG.md
  DEBUG_2CTA.md
  DEBUG_METHODOLOGY.md
  RACECHECK_TMA_HAZARD.md
  SASS_MMA_ANALYSIS.md
  SM90_BLOCK_SIZE_TUNING.md
  SM90_R2P_MASKING_SASS.md
  SPARSE_MLA_1CTA.md
  SPARSE_MLA_64H.md
  SPARSE_MLA_DPSUM_PRECISION.md
  SPARSE_MLA_EXACT_SOFTMAX_MAX.md
  SPARSE_MLA_RECOMPUTE_P.md
  VARLEN_PREPROCESS_TILE_BUG.md
  parse_clc_log.py
  racecheck_repro_1d_bulk.py
  racecheck_repro_1d_tensor.py
benchmarks/  (13 files)
  configs/  (1 files)
    clc.yaml
  bench_sm90.py
  benchmark_alibi.py
  benchmark_attn.py
  benchmark_causal.py
  benchmark_decode_sm100.py
  benchmark_flash_attention.py
  benchmark_gemm.py
  benchmark_mla_paged_kv.py
  benchmark_sparse_mla_fwd.py
  benchmark_varlen_sched.py
  clc_bench.py
  fwd_config_bench.py
csrc/  (197 files)
  flash_attn/  (117 files)
    src/  (116 files)
      … 116 files under this directory
    flash_api.cpp
  flash_attn_ck/  (9 files)
    flash_api.cpp
    flash_common.cpp
    flash_common.hpp
    mha_bwd.cpp
    mha_fwd.cpp
    mha_fwd_head_grouping_utils.hpp
    mha_fwd_kvcache.cpp
    mha_varlen_bwd.cpp
    mha_varlen_fwd.cpp
  fused_dense_lib/  (4 files)
    README.md
    fused_dense.cpp
    fused_dense_cuda.cu
    setup.py
  layer_norm/  (67 files)
    README.md
    ln.h
    ln_api.cpp
    ln_bwd_1024.cu
    ln_bwd_1280.cu
    ln_bwd_1536.cu
    ln_bwd_2048.cu
    ln_bwd_256.cu
    ln_bwd_2560.cu
    ln_bwd_3072.cu
    ln_bwd_4096.cu
    ln_bwd_512.cu
    ln_bwd_5120.cu
    ln_bwd_6144.cu
    ln_bwd_7168.cu
    ln_bwd_768.cu
    ln_bwd_8192.cu
    ln_bwd_kernels.cuh
    ln_fwd_1024.cu
    ln_fwd_1280.cu
    ln_fwd_1536.cu
    ln_fwd_2048.cu
    ln_fwd_256.cu
    ln_fwd_2560.cu
    … 43 more files
examples/  (1 files)
  inference/  (1 files)
    README.md
flash_attn/  (113 files)
  cute/  (63 files)
    .flake8
    AUTHORS
    LICENSE
    MANIFEST.in
    README.md
    __init__.py
    ampere_helpers.py
    autotune.py
    barrier.py
    bench_utils.py
    benchmark.py
    benchmark_flash_attention_fp8.py
    blackwell_helpers.py
    block_info.py
    block_sparse_utils.py
    block_sparsity.py
    blockscaled_utils.py
    bwd_accum_tile.py
    cache_utils.py
    compat.py
    compute_block_sparsity.py
    config.py
    copy_utils.py
    cu_blocks_kernel.py
    … 39 more files
  layers/  (3 files)
    __init__.py
    patch_embed.py
    rotary.py
  losses/  (2 files)
    __init__.py
    cross_entropy.py
  models/  (12 files)
    __init__.py
    baichuan.py
    bert.py
    bigcode.py
    btlm.py
    falcon.py
    gpt.py
    gpt_neox.py
    gptj.py
    llama.py
    opt.py
    vit.py
  modules/  (5 files)
    __init__.py
    block.py
    embedding.py
    mha.py
    mlp.py
  ops/  (12 files)
    triton/  (7 files)
      … 7 files under this directory
    __init__.py
    activations.py
    fused_dense.py
    layer_norm.py
    rms_norm.py
  utils/  (8 files)
    __init__.py
    benchmark.py
    distributed.py
    generation.py
    library.py
    pretrained.py
    testing.py
    torch.py
  __init__.py
  bert_padding.py
  flash_attn_interface.py
  flash_attn_triton.py
  flash_attn_triton_og.py
  flash_blocksparse_attention.py
  flash_blocksparse_attn_interface.py
  pyproject.toml
hopper/  (441 files)
  flash_attn_3/  (3 files)
    __init__.py
    flash_attn_config.py
    flash_attn_interface.py
  instantiations/  (410 files)
    flash_bwd_hdim128_bf16_sm80.cu
    flash_bwd_hdim128_bf16_sm90.cu
    flash_bwd_hdim128_bf16_softcap_sm80.cu
    flash_bwd_hdim128_bf16_softcap_sm90.cu
    flash_bwd_hdim128_bf16_softcapall_sm90.cu
    flash_bwd_hdim128_fp16_sm80.cu
    flash_bwd_hdim128_fp16_sm90.cu
    flash_bwd_hdim128_fp16_softcap_sm80.cu
    flash_bwd_hdim128_fp16_softcap_sm90.cu
    flash_bwd_hdim128_fp16_softcapall_sm90.cu
    flash_bwd_hdim192_bf16_sm80.cu
    flash_bwd_hdim192_bf16_sm90.cu
    flash_bwd_hdim192_bf16_softcap_sm80.cu
    flash_bwd_hdim192_bf16_softcap_sm90.cu
    flash_bwd_hdim192_bf16_softcapall_sm90.cu
    flash_bwd_hdim192_fp16_sm80.cu
    flash_bwd_hdim192_fp16_sm90.cu
    flash_bwd_hdim192_fp16_softcap_sm80.cu
    flash_bwd_hdim192_fp16_softcap_sm90.cu
    flash_bwd_hdim192_fp16_softcapall_sm90.cu
    flash_bwd_hdim256_bf16_sm80.cu
    flash_bwd_hdim256_bf16_sm90.cu
    flash_bwd_hdim256_bf16_softcap_sm80.cu
    flash_bwd_hdim256_bf16_softcap_sm90.cu
    … 386 more files
  __init__.py
  benchmark_attn.py
  benchmark_flash_attention_fp8.py
  benchmark_mla_decode.py
  benchmark_split_kv.py
  block.h
  copy_sm90_bulk_reduce.hpp
  cuda_check.h
  epilogue_bwd.hpp
  epilogue_fwd.hpp
  flash.h
  flash_api.cpp
  flash_api_stable.cpp
  flash_attn_interface.py
  flash_bwd_kernel_sm80.h
  flash_bwd_kernel_sm90.h
  flash_bwd_launch_template.h
  flash_bwd_postprocess_kernel.h
  flash_bwd_preprocess_kernel.h
  flash_fwd_combine.cu
  flash_fwd_combine_kernel.h
  flash_fwd_combine_launch_template.h
  flash_fwd_kernel_sm80.h
  flash_fwd_kernel_sm90.h
  … 4 more files
.gitignore
.gitmodules
.pre-commit-config.yaml
AUTHORS
CLAUDE.md
LICENSE
MANIFEST.in
Makefile
README.md
```

## Entry points

- [csrc/flash_attn/src/generate_kernels.py:112](https://github.com/Dao-AILab/flash-attention/blob/f63c472c4dc19237c0635d6a629df065ff64796e/csrc/flash_attn/src/generate_kernels.py#L112)
- [.github/scripts/bump_beta_tag.py:95](https://github.com/Dao-AILab/flash-attention/blob/f63c472c4dc19237c0635d6a629df065ff64796e/.github/scripts/bump_beta_tag.py#L95)
- [AI/parse_clc_log.py:395](https://github.com/Dao-AILab/flash-attention/blob/f63c472c4dc19237c0635d6a629df065ff64796e/AI/parse_clc_log.py#L395)
- [AI/racecheck_repro_1d_bulk.py:67](https://github.com/Dao-AILab/flash-attention/blob/f63c472c4dc19237c0635d6a629df065ff64796e/AI/racecheck_repro_1d_bulk.py#L67)
- [AI/racecheck_repro_1d_tensor.py:77](https://github.com/Dao-AILab/flash-attention/blob/f63c472c4dc19237c0635d6a629df065ff64796e/AI/racecheck_repro_1d_tensor.py#L77)
- [benchmarks/bench_sm90.py:535](https://github.com/Dao-AILab/flash-attention/blob/f63c472c4dc19237c0635d6a629df065ff64796e/benchmarks/bench_sm90.py#L535)
- [benchmarks/benchmark_attn.py:580](https://github.com/Dao-AILab/flash-attention/blob/f63c472c4dc19237c0635d6a629df065ff64796e/benchmarks/benchmark_attn.py#L580)
- [benchmarks/benchmark_decode_sm100.py:343](https://github.com/Dao-AILab/flash-attention/blob/f63c472c4dc19237c0635d6a629df065ff64796e/benchmarks/benchmark_decode_sm100.py#L343)
- [benchmarks/benchmark_sparse_mla_fwd.py:171](https://github.com/Dao-AILab/flash-attention/blob/f63c472c4dc19237c0635d6a629df065ff64796e/benchmarks/benchmark_sparse_mla_fwd.py#L171)
- [benchmarks/benchmark_varlen_sched.py:566](https://github.com/Dao-AILab/flash-attention/blob/f63c472c4dc19237c0635d6a629df065ff64796e/benchmarks/benchmark_varlen_sched.py#L566)
- [benchmarks/clc_bench.py:887](https://github.com/Dao-AILab/flash-attention/blob/f63c472c4dc19237c0635d6a629df065ff64796e/benchmarks/clc_bench.py#L887)
- [benchmarks/fwd_config_bench.py:126](https://github.com/Dao-AILab/flash-attention/blob/f63c472c4dc19237c0635d6a629df065ff64796e/benchmarks/fwd_config_bench.py#L126)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| benchmarks package | library | Observed | Groups 5 file(s) under benchmarks package (observed from repository paths and static analysis). Observed top-level functions: attention_pytorch, attn_bias_from_alibi_slopes, benchmark_forward, efficiency, flash_rotary,… |
| Configuration and deployment | config | Observed | Groups 8 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: BwdConfig, BwdFold, BwdHeuristicInputs, FwdConfig, FwdHeuristicInputs, MlaFwdConfig.… |
| csrc package | library | Observed | Groups 30 file(s) under csrc package (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 12 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: BertEncoder, BertForPreTraining, BertLMPredictionHead, BertModel, BertPooler, BertPreTrainedModel. Obs… |
| Application entry point | entrypoint | Observed | Groups 15 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: BlockSparseSweep, Case, DenseSweep, Kernel, TraceRow, VarlenSweep. Observed top-level fun… |
| flash_attn package | library | Observed | Groups 91 file(s) under flash_attn package (observed from repository paths and static analysis). Observed top-level classes: AccumTileOrder, Activation, AllGatherFunc, AllReduceFunc, ApplyRotaryEmb, ApplyRotaryEmbKV_. O… |
| hopper package | library | Observed | Groups 24 file(s) under hopper package (observed from repository paths and static analysis). Observed top-level classes: FlashAttnFunc, FlashAttnQKVPackedFunc, FlashAttnVarlenFunc. Observed top-level functions: _backwar… |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/actions/gpu-test/action.yml` (config)
- `.github/workflows/README.md` (ci)
- `.github/workflows/_build.yml` (ci)
- `.github/workflows/build.yml` (ci)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/pre-commit.yaml` (ci)
- `.github/workflows/publish-fa4.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `MANIFEST.in` (manifest)
- `benchmarks/configs/clc.yaml` (config)
- `csrc/fused_dense_lib/setup.py` (manifest)
- `csrc/layer_norm/setup.py` (manifest)
- `flash_attn/cute/MANIFEST.in` (manifest)
- `flash_attn/cute/pyproject.toml` (manifest)
- `flash_attn/pyproject.toml` (manifest)

## Top-level layout

- `hopper` — 441 analysed file(s)
- `csrc` — 197 analysed file(s)
- `flash_attn` — 113 analysed file(s)
- `AI` — 16 analysed file(s)
- `benchmarks` — 13 analysed file(s)
- `.github` — 10 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `examples` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `f63c472c4dc19237c0635d6a629df065ff64796e` is the revision these paths and observations refer to.
