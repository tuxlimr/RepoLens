# Project structure: PKU-YuanGroup/Open-Sora-Plan

**Analysed commit:** `f7fa604f4e3a523d6b973e4c89a5620ed1aff65a`

**Commit reference:** [f7fa604f4e3a523d6b973e4c89a5620ed1aff65a](https://github.com/PKU-YuanGroup/Open-Sora-Plan/commit/f7fa604f4e3a523d6b973e4c89a5620ed1aff65a)

**Tree at this commit:** [PKU-YuanGroup/Open-Sora-Plan@f7fa604f4e3a](https://github.com/PKU-YuanGroup/Open-Sora-Plan/tree/f7fa604f4e3a523d6b973e4c89a5620ed1aff65a)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | PKU-YuanGroup/Open-Sora-Plan |
| Description | This project aim to reproduce Sora (Open AI T2V model), we wish the open source community contribute to this project. |
| Stars | 12199 |
| Forks | 1071 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `f7fa604f4e3a523d6b973e4c89a5620ed1aff65a` |
| Retrieved at | 2026-11-14T19:10:13.598947+00:00 |
| Files in this snapshot | 179 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    docker_build.yml
docs/  (10 files)
  Contribution_Guidelines.md
  Prompt_Refiner.md
  Report-v1.0.0-cn.md
  Report-v1.0.0.md
  Report-v1.1.0.md
  Report-v1.2.0.md
  Report-v1.3.0.md
  Report-v1.5.0.md
  Report-v1.5.0_cn.md
  VAE.md
examples/  (5 files)
  cond_pix_path.txt
  cond_prompt.txt
  rec_image.py
  rec_video.py
  sora.txt
opensora/  (128 files)
  acceleration/  (3 files)
    __init__.py
    communications.py
    parallel_states.py
  adaptor/  (7 files)
    __init__.py
    bf16_optimizer.py
    engine.py
    modules.py
    stage_1_and_2.py
    utils.py
    zp_manager.py
  dataset/  (5 files)
    __init__.py
    inpaint_dataset.py
    t2v_datasets.py
    transform.py
    virtual_disk.py
  models/  (86 files)
    causalvideovae/  (53 files)
      … 53 files under this directory
    diffusion/  (11 files)
      … 11 files under this directory
    frame_interpolation/  (15 files)
      … 15 files under this directory
    prompt_refiner/  (3 files)
      … 3 files under this directory
    text_encoder/  (3 files)
      … 3 files under this directory
    __init__.py
  sample/  (6 files)
    caption_refiner.py
    pipeline_inpaint.py
    pipeline_opensora.py
    rec_image.py
    rec_video.py
    sample.py
  serve/  (4 files)
    gradio_utils.py
    gradio_web_server.py
    gradio_web_server_i2v.py
    style.css
  train/  (3 files)
    train_causalvae.py
    train_inpaint.py
    train_t2v_diffusers.py
  utils/  (12 files)
    communications.py
    dataset_utils.py
    downloader.py
    ema.py
    ema_utils.py
    freeinit_utils.py
    lora_utils.py
    mask_utils.py
    parallel_states.py
    sample_utils.py
    taming_download.py
    utils.py
  __init__.py
  npu_config.py
scripts/  (31 files)
  accelerate_configs/  (14 files)
    ddp_config.yaml
    deepspeed_zero2_config.yaml
    deepspeed_zero2_offload_config.yaml
    deepspeed_zero3_config.yaml
    deepspeed_zero3_offload_config.yaml
    default_config.yaml
    hostfile
    multi_node_example.yaml
    multi_node_example_by_ddp.yaml
    zero2.json
    zero2_npu.json
    zero2_offload.json
    zero3.json
    zero3_offload.json
  causalvae/  (6 files)
    eval.sh
    prepare_eval.sh
    rec_image.sh
    rec_video.sh
    train.sh
    wfvae_4dim.json
  slurm/  (1 files)
    placeholder
  text_condition/  (8 files)
    gpu/  (4 files)
      … 4 files under this directory
    npu/  (4 files)
      … 4 files under this directory
  train_configs/  (1 files)
    mask_config.yaml
  train_data/  (1 files)
    merge_data.txt
.gitignore
LICENSE
README.md
pyproject.toml
```

## Entry points

- [opensora/dataset/__init__.py:57](https://github.com/PKU-YuanGroup/Open-Sora-Plan/blob/f7fa604f4e3a523d6b973e4c89a5620ed1aff65a/opensora/dataset/__init__.py#L57)
- [opensora/dataset/transform.py:843](https://github.com/PKU-YuanGroup/Open-Sora-Plan/blob/f7fa604f4e3a523d6b973e4c89a5620ed1aff65a/opensora/dataset/transform.py#L843)
- [opensora/models/causalvideovae/dataset/transform.py:521](https://github.com/PKU-YuanGroup/Open-Sora-Plan/blob/f7fa604f4e3a523d6b973e4c89a5620ed1aff65a/opensora/models/causalvideovae/dataset/transform.py#L521)
- [opensora/models/causalvideovae/eval/cal_fvd.py:84](https://github.com/PKU-YuanGroup/Open-Sora-Plan/blob/f7fa604f4e3a523d6b973e4c89a5620ed1aff65a/opensora/models/causalvideovae/eval/cal_fvd.py#L84)
- [opensora/models/causalvideovae/eval/cal_lpips.py:96](https://github.com/PKU-YuanGroup/Open-Sora-Plan/blob/f7fa604f4e3a523d6b973e4c89a5620ed1aff65a/opensora/models/causalvideovae/eval/cal_lpips.py#L96)
- [opensora/models/causalvideovae/eval/cal_psnr.py:96](https://github.com/PKU-YuanGroup/Open-Sora-Plan/blob/f7fa604f4e3a523d6b973e4c89a5620ed1aff65a/opensora/models/causalvideovae/eval/cal_psnr.py#L96)
- [opensora/models/causalvideovae/eval/cal_ssim.py:112](https://github.com/PKU-YuanGroup/Open-Sora-Plan/blob/f7fa604f4e3a523d6b973e4c89a5620ed1aff65a/opensora/models/causalvideovae/eval/cal_ssim.py#L112)
- [opensora/models/causalvideovae/eval/eval.py:185](https://github.com/PKU-YuanGroup/Open-Sora-Plan/blob/f7fa604f4e3a523d6b973e4c89a5620ed1aff65a/opensora/models/causalvideovae/eval/eval.py#L185)
- [opensora/models/causalvideovae/sample/rec_video_vae.py:87](https://github.com/PKU-YuanGroup/Open-Sora-Plan/blob/f7fa604f4e3a523d6b973e4c89a5620ed1aff65a/opensora/models/causalvideovae/sample/rec_video_vae.py#L87)
- [opensora/models/diffusion/opensora_v1_3/modeling_opensora.py:307](https://github.com/PKU-YuanGroup/Open-Sora-Plan/blob/f7fa604f4e3a523d6b973e4c89a5620ed1aff65a/opensora/models/diffusion/opensora_v1_3/modeling_opensora.py#L307)
- [opensora/models/frame_interpolation/interpolation.py:177](https://github.com/PKU-YuanGroup/Open-Sora-Plan/blob/f7fa604f4e3a523d6b973e4c89a5620ed1aff65a/opensora/models/frame_interpolation/interpolation.py#L177)
- [opensora/models/prompt_refiner/inference.py:34](https://github.com/PKU-YuanGroup/Open-Sora-Plan/blob/f7fa604f4e3a523d6b973e4c89a5620ed1aff65a/opensora/models/prompt_refiner/inference.py#L34)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 18 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 71 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: Attention, AttnBlock3D, AttnBlock3DFix, AverageMeter, AverageMeterGroups, BasicEncoder. Observed top-l… |
| Application entry point | entrypoint | Observed | Groups 21 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: BaseMaskGenerator, BaseNoiseAdder, CenterCropResizeVideo, CenterCropVideo, ClearMaskGener… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| opensora package | library | Observed | Groups 31 file(s) under opensora package (observed from repository paths and static analysis). Observed top-level classes: BF16_Optimizer, COMM_INFO, CheckOverflow, Collate, DataSetProg, DecordDecoder. Observed top-leve… |
| scripts package | library | Observed | Groups 13 file(s) under scripts package (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/docker_build.yml` (ci)
- `opensora/models/diffusion/curope/setup.py` (manifest)
- `opensora/models/frame_interpolation/cfgs/AMT-G.yaml` (config)
- `pyproject.toml` (manifest)
- `scripts/accelerate_configs/ddp_config.yaml` (config)
- `scripts/accelerate_configs/deepspeed_zero2_config.yaml` (config)
- `scripts/accelerate_configs/deepspeed_zero2_offload_config.yaml` (config)
- `scripts/accelerate_configs/deepspeed_zero3_config.yaml` (config)
- `scripts/accelerate_configs/deepspeed_zero3_offload_config.yaml` (config)
- `scripts/accelerate_configs/default_config.yaml` (config)
- `scripts/accelerate_configs/multi_node_example.yaml` (config)
- `scripts/accelerate_configs/multi_node_example_by_ddp.yaml` (config)
- `scripts/accelerate_configs/zero2.json` (config)
- `scripts/accelerate_configs/zero2_npu.json` (config)
- `scripts/accelerate_configs/zero2_offload.json` (config)
- `scripts/accelerate_configs/zero3.json` (config)
- `scripts/accelerate_configs/zero3_offload.json` (config)
- `scripts/causalvae/wfvae_4dim.json` (config)
- `scripts/train_configs/mask_config.yaml` (config)

## Top-level layout

- `opensora` — 128 analysed file(s)
- `scripts` — 31 analysed file(s)
- `docs` — 10 analysed file(s)
- `examples` — 5 analysed file(s)
- `(root files)` — 4 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `f7fa604f4e3a523d6b973e4c89a5620ed1aff65a` is the revision these paths and observations refer to.
