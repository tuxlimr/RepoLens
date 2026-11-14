# Project structure: microsoft/Swin-Transformer

**Analysed commit:** `f82860bfb5225915aca09c3227159ee9e1df874d`

**Commit reference:** [f82860bfb5225915aca09c3227159ee9e1df874d](https://github.com/microsoft/Swin-Transformer/commit/f82860bfb5225915aca09c3227159ee9e1df874d)

**Tree at this commit:** [microsoft/Swin-Transformer@f82860bfb522](https://github.com/microsoft/Swin-Transformer/tree/f82860bfb5225915aca09c3227159ee9e1df874d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | microsoft/Swin-Transformer |
| Description | This is an official implementation for "Swin Transformer: Hierarchical Vision Transformer using Shifted Windows". |
| Stars | 16080 |
| Forks | 2212 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `f82860bfb5225915aca09c3227159ee9e1df874d` |
| Retrieved at | 2026-11-14T19:08:56.185863+00:00 |
| Files in this snapshot | 86 |

## Directory tree

```text
configs/  (46 files)
  simmim/  (4 files)
    simmim_finetune__swin_base__img224_window7__800ep.yaml
    simmim_finetune__swinv2_base__img224_window14__800ep.yaml
    simmim_pretrain__swin_base__img192_window6__800ep.yaml
    simmim_pretrain__swinv2_base__img192_window12__800ep.yaml
  swin/  (15 files)
    swin_base_patch4_window12_384_22kto1k_finetune.yaml
    swin_base_patch4_window12_384_finetune.yaml
    swin_base_patch4_window7_224.yaml
    swin_base_patch4_window7_224_22k.yaml
    swin_base_patch4_window7_224_22kto1k_finetune.yaml
    swin_large_patch4_window12_384_22kto1k_finetune.yaml
    swin_large_patch4_window7_224_22k.yaml
    swin_large_patch4_window7_224_22kto1k_finetune.yaml
    swin_small_patch4_window7_224.yaml
    swin_small_patch4_window7_224_22k.yaml
    swin_small_patch4_window7_224_22kto1k_finetune.yaml
    swin_tiny_c24_patch4_window8_256.yaml
    swin_tiny_patch4_window7_224.yaml
    swin_tiny_patch4_window7_224_22k.yaml
    swin_tiny_patch4_window7_224_22kto1k_finetune.yaml
  swinmlp/  (4 files)
    swin_mlp_base_patch4_window7_224.yaml
    swin_mlp_tiny_c12_patch4_window8_256.yaml
    swin_mlp_tiny_c24_patch4_window8_256.yaml
    swin_mlp_tiny_c6_patch4_window8_256.yaml
  swinmoe/  (11 files)
    swin_moe_base_patch4_window12_192_16expert_32gpu_22k.yaml
    swin_moe_base_patch4_window12_192_32expert_32gpu_22k.yaml
    swin_moe_base_patch4_window12_192_8expert_32gpu_22k.yaml
    swin_moe_base_patch4_window12_192_cosine_router_32expert_32gpu_22k.yaml
    swin_moe_base_patch4_window12_192_densebaseline_22k.yaml
    swin_moe_small_patch4_window12_192_16expert_32gpu_22k.yaml
    swin_moe_small_patch4_window12_192_32expert_32gpu_22k.yaml
    swin_moe_small_patch4_window12_192_64expert_64gpu_22k.yaml
    swin_moe_small_patch4_window12_192_8expert_32gpu_22k.yaml
    swin_moe_small_patch4_window12_192_cosine_router_32expert_32gpu_22k.yaml
    swin_moe_small_patch4_window12_192_densebaseline_22k.yaml
  swinv2/  (12 files)
    swinv2_base_patch4_window12_192_22k.yaml
    swinv2_base_patch4_window12to16_192to256_22kto1k_ft.yaml
    swinv2_base_patch4_window12to24_192to384_22kto1k_ft.yaml
    swinv2_base_patch4_window16_256.yaml
    swinv2_base_patch4_window8_256.yaml
    swinv2_large_patch4_window12_192_22k.yaml
    swinv2_large_patch4_window12to16_192to256_22kto1k_ft.yaml
    swinv2_large_patch4_window12to24_192to384_22kto1k_ft.yaml
    swinv2_small_patch4_window16_256.yaml
    swinv2_small_patch4_window8_256.yaml
    swinv2_tiny_patch4_window16_256.yaml
    swinv2_tiny_patch4_window8_256.yaml
data/  (9 files)
  __init__.py
  build.py
  cached_image_folder.py
  data_simmim_ft.py
  data_simmim_pt.py
  imagenet22k_dataset.py
  map22kto1k.txt
  samplers.py
  zipreader.py
kernels/  (5 files)
  window_process/  (5 files)
    setup.py
    swin_window_process.cpp
    swin_window_process_kernel.cu
    unit_test.py
    window_process.py
models/  (7 files)
  __init__.py
  build.py
  simmim.py
  swin_mlp.py
  swin_transformer.py
  swin_transformer_moe.py
  swin_transformer_v2.py
.gitignore
CODE_OF_CONDUCT.md
LICENSE
MODELHUB.md
README.md
SECURITY.md
SUPPORT.md
config.py
get_started.md
logger.py
lr_scheduler.py
main.py
main_moe.py
main_simmim_ft.py
main_simmim_pt.py
optimizer.py
utils.py
utils_moe.py
utils_simmim.py
```

## Entry points

- [kernels/window_process/unit_test.py:247](https://github.com/microsoft/Swin-Transformer/blob/f82860bfb5225915aca09c3227159ee9e1df874d/kernels/window_process/unit_test.py#L247)
- [main.py:302](https://github.com/microsoft/Swin-Transformer/blob/f82860bfb5225915aca09c3227159ee9e1df874d/main.py#L302)
- [main_moe.py:321](https://github.com/microsoft/Swin-Transformer/blob/f82860bfb5225915aca09c3227159ee9e1df874d/main_moe.py#L321)
- [main_simmim_ft.py:296](https://github.com/microsoft/Swin-Transformer/blob/f82860bfb5225915aca09c3227159ee9e1df874d/main_simmim_ft.py#L296)
- [main_simmim_pt.py:188](https://github.com/microsoft/Swin-Transformer/blob/f82860bfb5225915aca09c3227159ee9e1df874d/main_simmim_pt.py#L188)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 48 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: _update_config_from_file, get_config, update_config. |
| Core modules | core | Observed | Groups 6 file(s) under core modules (observed from repository paths and static analysis). Observed top-level classes: LinearLRScheduler, MultiStepLRScheduler, NativeScalerWithGradNormCount. Observed top-level functions:… |
| Data layer | data | Observed | Groups 15 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: BasicLayer, CachedImageFolder, DatasetFolder, IN22KDATASET, MaskGenerator, Mlp. Observed top-level fun… |
| Application entry point | entrypoint | Observed | Groups 4 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: main, parse_option, throughput, train_one_epoch, validate. |
| kernels package | library | Observed | Groups 2 file(s) under kernels package (observed from repository paths and static analysis). Observed top-level classes: WindowProcess, WindowProcessReverse. |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: Test_WindowProcess, WindowProcess, WindowProcessReverse. Observed top-level functions: copy_one_tensor, pyt_… |

## Important files

- `configs/simmim/simmim_finetune__swin_base__img224_window7__800ep.yaml` (config)
- `configs/simmim/simmim_finetune__swinv2_base__img224_window14__800ep.yaml` (config)
- `configs/simmim/simmim_pretrain__swin_base__img192_window6__800ep.yaml` (config)
- `configs/simmim/simmim_pretrain__swinv2_base__img192_window12__800ep.yaml` (config)
- `configs/swin/swin_base_patch4_window12_384_22kto1k_finetune.yaml` (config)
- `configs/swin/swin_base_patch4_window12_384_finetune.yaml` (config)
- `configs/swin/swin_base_patch4_window7_224.yaml` (config)
- `configs/swin/swin_base_patch4_window7_224_22k.yaml` (config)
- `configs/swin/swin_base_patch4_window7_224_22kto1k_finetune.yaml` (config)
- `configs/swin/swin_large_patch4_window12_384_22kto1k_finetune.yaml` (config)
- `configs/swin/swin_large_patch4_window7_224_22k.yaml` (config)
- `configs/swin/swin_large_patch4_window7_224_22kto1k_finetune.yaml` (config)
- `configs/swin/swin_small_patch4_window7_224.yaml` (config)
- `configs/swin/swin_small_patch4_window7_224_22k.yaml` (config)
- `configs/swin/swin_small_patch4_window7_224_22kto1k_finetune.yaml` (config)
- `configs/swin/swin_tiny_c24_patch4_window8_256.yaml` (config)
- `configs/swin/swin_tiny_patch4_window7_224.yaml` (config)
- `configs/swin/swin_tiny_patch4_window7_224_22k.yaml` (config)
- `configs/swin/swin_tiny_patch4_window7_224_22kto1k_finetune.yaml` (config)
- `configs/swinmlp/swin_mlp_base_patch4_window7_224.yaml` (config)
- `configs/swinmlp/swin_mlp_tiny_c12_patch4_window8_256.yaml` (config)
- `configs/swinmlp/swin_mlp_tiny_c24_patch4_window8_256.yaml` (config)
- `configs/swinmlp/swin_mlp_tiny_c6_patch4_window8_256.yaml` (config)
- `configs/swinmoe/swin_moe_base_patch4_window12_192_16expert_32gpu_22k.yaml` (config)
- `configs/swinmoe/swin_moe_base_patch4_window12_192_32expert_32gpu_22k.yaml` (config)
- `configs/swinmoe/swin_moe_base_patch4_window12_192_8expert_32gpu_22k.yaml` (config)
- `configs/swinmoe/swin_moe_base_patch4_window12_192_cosine_router_32expert_32gpu_22k.yaml` (config)
- `configs/swinmoe/swin_moe_base_patch4_window12_192_densebaseline_22k.yaml` (config)
- `configs/swinmoe/swin_moe_small_patch4_window12_192_16expert_32gpu_22k.yaml` (config)
- `configs/swinmoe/swin_moe_small_patch4_window12_192_32expert_32gpu_22k.yaml` (config)
- `configs/swinmoe/swin_moe_small_patch4_window12_192_64expert_64gpu_22k.yaml` (config)
- `configs/swinmoe/swin_moe_small_patch4_window12_192_8expert_32gpu_22k.yaml` (config)
- `configs/swinmoe/swin_moe_small_patch4_window12_192_cosine_router_32expert_32gpu_22k.yaml` (config)
- `configs/swinmoe/swin_moe_small_patch4_window12_192_densebaseline_22k.yaml` (config)
- `configs/swinv2/swinv2_base_patch4_window12_192_22k.yaml` (config)
- `configs/swinv2/swinv2_base_patch4_window12to16_192to256_22kto1k_ft.yaml` (config)
- `configs/swinv2/swinv2_base_patch4_window12to24_192to384_22kto1k_ft.yaml` (config)
- `configs/swinv2/swinv2_base_patch4_window16_256.yaml` (config)
- `configs/swinv2/swinv2_base_patch4_window8_256.yaml` (config)
- `configs/swinv2/swinv2_large_patch4_window12_192_22k.yaml` (config)
- `configs/swinv2/swinv2_large_patch4_window12to16_192to256_22kto1k_ft.yaml` (config)
- `configs/swinv2/swinv2_large_patch4_window12to24_192to384_22kto1k_ft.yaml` (config)
- `configs/swinv2/swinv2_small_patch4_window16_256.yaml` (config)
- `configs/swinv2/swinv2_small_patch4_window8_256.yaml` (config)
- `configs/swinv2/swinv2_tiny_patch4_window16_256.yaml` (config)
- `configs/swinv2/swinv2_tiny_patch4_window8_256.yaml` (config)
- `kernels/window_process/setup.py` (manifest)

## Top-level layout

- `configs` — 46 analysed file(s)
- `(root files)` — 19 analysed file(s)
- `data` — 9 analysed file(s)
- `models` — 7 analysed file(s)
- `kernels` — 5 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- The GitHub repository was marked archived at selection time.

Commit `f82860bfb5225915aca09c3227159ee9e1df874d` is the revision these paths and observations refer to.
