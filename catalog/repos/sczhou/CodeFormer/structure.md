# Project structure: sczhou/CodeFormer

**Analysed commit:** `b33cc7d639d6545bfcccc7e0bc6ae51f24e79c2b`

**Commit reference:** [b33cc7d639d6545bfcccc7e0bc6ae51f24e79c2b](https://github.com/sczhou/CodeFormer/commit/b33cc7d639d6545bfcccc7e0bc6ae51f24e79c2b)

**Tree at this commit:** [sczhou/CodeFormer@b33cc7d639d6](https://github.com/sczhou/CodeFormer/tree/b33cc7d639d6545bfcccc7e0bc6ae51f24e79c2b)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | sczhou/CodeFormer |
| Description | [NeurIPS 2022] Towards Robust Blind Face Restoration with Codebook Lookup Transformer |
| Stars | 18228 |
| Forks | 3718 |
| Licence | Other |
| Language | Python |
| Default branch | master |
| Analysed commit | `b33cc7d639d6545bfcccc7e0bc6ae51f24e79c2b` |
| Retrieved at | 2026-11-14T19:08:26.727734+00:00 |
| Files in this snapshot | 115 |

## Directory tree

```text
basicsr/  (61 files)
  archs/  (7 files)
    __init__.py
    arcface_arch.py
    arch_util.py
    codeformer_arch.py
    rrdbnet_arch.py
    vgg_arch.py
    vqgan_arch.py
  data/  (9 files)
    __init__.py
    data_sampler.py
    data_util.py
    ffhq_blind_dataset.py
    ffhq_blind_joint_dataset.py
    gaussian_kernels.py
    paired_image_dataset.py
    prefetch_dataloader.py
    transforms.py
  losses/  (3 files)
    __init__.py
    loss_util.py
    losses.py
  metrics/  (3 files)
    __init__.py
    metric_util.py
    psnr_ssim.py
  models/  (8 files)
    __init__.py
    base_model.py
    codeformer_idx_model.py
    codeformer_joint_model.py
    codeformer_model.py
    lr_scheduler.py
    sr_model.py
    vqgan_model.py
  ops/  (14 files)
    dcn/  (5 files)
      … 5 files under this directory
    fused_act/  (4 files)
      … 4 files under this directory
    upfirdn2d/  (4 files)
      … 4 files under this directory
    __init__.py
  utils/  (13 files)
    __init__.py
    dist_util.py
    download_util.py
    file_client.py
    img_util.py
    lmdb_util.py
    logger.py
    matlab_functions.py
    misc.py
    options.py
    realesrgan_utils.py
    registry.py
    video_util.py
  VERSION
  __init__.py
  setup.py
  train.py
docs/  (3 files)
  history_changelog.md
  train.md
  train_CN.md
facelib/  (28 files)
  detection/  (20 files)
    retinaface/  (3 files)
      … 3 files under this directory
    yolov5face/  (14 files)
      … 14 files under this directory
    __init__.py
    align_trans.py
    matlab_cp2tform.py
  parsing/  (4 files)
    __init__.py
    bisenet.py
    parsenet.py
    resnet.py
  utils/  (4 files)
    __init__.py
    face_restoration_helper.py
    face_utils.py
    misc.py
options/  (5 files)
  CodeFormer_colorization.yml
  CodeFormer_inpainting.yml
  CodeFormer_stage2.yml
  CodeFormer_stage3.yml
  VQGAN_512_ds32_nearest_stage1.yml
scripts/  (5 files)
  crop_align_face.py
  download_pretrained_models.py
  download_pretrained_models_from_gdrive.py
  generate_latent_gt.py
  inference_vqgan.py
web-demos/  (3 files)
  hugging_face/  (1 files)
    app.py
  replicate/  (2 files)
    cog.yaml
    predict.py
weights/  (3 files)
  CodeFormer/  (1 files)
    .gitkeep
  facelib/  (1 files)
    .gitkeep
  README.md
.gitignore
LICENSE
README.md
inference_codeformer.py
inference_colorization.py
inference_inpainting.py
requirements.txt
```

## Entry points

- [basicsr/setup.py:117](https://github.com/sczhou/CodeFormer/blob/b33cc7d639d6545bfcccc7e0bc6ae51f24e79c2b/basicsr/setup.py#L117)
- [basicsr/train.py:223](https://github.com/sczhou/CodeFormer/blob/b33cc7d639d6545bfcccc7e0bc6ae51f24e79c2b/basicsr/train.py#L223)
- [facelib/detection/matlab_cp2tform.py:235](https://github.com/sczhou/CodeFormer/blob/b33cc7d639d6545bfcccc7e0bc6ae51f24e79c2b/facelib/detection/matlab_cp2tform.py#L235)
- [facelib/utils/face_utils.py:211](https://github.com/sczhou/CodeFormer/blob/b33cc7d639d6545bfcccc7e0bc6ae51f24e79c2b/facelib/utils/face_utils.py#L211)
- [inference_codeformer.py:55](https://github.com/sczhou/CodeFormer/blob/b33cc7d639d6545bfcccc7e0bc6ae51f24e79c2b/inference_codeformer.py#L55)
- [inference_colorization.py:14](https://github.com/sczhou/CodeFormer/blob/b33cc7d639d6545bfcccc7e0bc6ae51f24e79c2b/inference_colorization.py#L14)
- [inference_inpainting.py:14](https://github.com/sczhou/CodeFormer/blob/b33cc7d639d6545bfcccc7e0bc6ae51f24e79c2b/inference_inpainting.py#L14)
- [scripts/crop_align_face.py:186](https://github.com/sczhou/CodeFormer/blob/b33cc7d639d6545bfcccc7e0bc6ae51f24e79c2b/scripts/crop_align_face.py#L186)
- [scripts/download_pretrained_models.py:18](https://github.com/sczhou/CodeFormer/blob/b33cc7d639d6545bfcccc7e0bc6ae51f24e79c2b/scripts/download_pretrained_models.py#L18)
- [scripts/download_pretrained_models_from_gdrive.py:31](https://github.com/sczhou/CodeFormer/blob/b33cc7d639d6545bfcccc7e0bc6ae51f24e79c2b/scripts/download_pretrained_models_from_gdrive.py#L31)
- [scripts/generate_latent_gt.py:12](https://github.com/sczhou/CodeFormer/blob/b33cc7d639d6545bfcccc7e0bc6ae51f24e79c2b/scripts/generate_latent_gt.py#L12)
- [scripts/inference_vqgan.py:12](https://github.com/sczhou/CodeFormer/blob/b33cc7d639d6545bfcccc7e0bc6ae51f24e79c2b/scripts/inference_vqgan.py#L12)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| basicsr package | library | Observed | Groups 37 file(s) under basicsr package (observed from repository paths and static analysis). Observed top-level classes: AttnBlock, BasicBlock, Bottleneck, CharbonnierLoss, CodeFormer, DCNv2Pack. Observed top-level fun… |
| Configuration and deployment | config | Observed | Groups 10 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: get_git_hash, get_hash, get_requirements, get_version, make_cuda_ext, readme. |
| Data layer | data | Observed | Groups 21 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AutoShape, BaseModel, Bottleneck, BottleneckCSP, C3, CPUPrefetcher. Observed top-level functions: DWCo… |
| Application entry point | entrypoint | Observed | Groups 12 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: MatlabCp2tormException. Observed top-level functions: align_crop_face_landmarks, align_fa… |
| External integrations | external | Observed | Groups 1 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: BaseStorageBackend, FileClient, HardDiskBackend, LmdbBackend, MemcachedBackend. |
| facelib package | library | Observed | Groups 20 file(s) under facelib package (observed from repository paths and static analysis). Observed top-level classes: AttentionRefinementModule, BasicBlock, BboxHead, BiSeNet, BiSeNetOutput, ClassHead. Observed top-… |
| web-demos package | library | Observed | Groups 1 file(s) under web-demos package (observed from repository paths and static analysis). Observed top-level classes: Predictor. Observed top-level functions: imread, set_realesrgan. |

## Important files

- `basicsr/setup.py` (manifest)
- `facelib/detection/yolov5face/models/yolov5l.yaml` (config)
- `facelib/detection/yolov5face/models/yolov5n.yaml` (config)
- `options/CodeFormer_colorization.yml` (config)
- `options/CodeFormer_inpainting.yml` (config)
- `options/CodeFormer_stage2.yml` (config)
- `options/CodeFormer_stage3.yml` (config)
- `options/VQGAN_512_ds32_nearest_stage1.yml` (config)
- `requirements.txt` (manifest)
- `web-demos/replicate/cog.yaml` (config)

## Top-level layout

- `basicsr` — 61 analysed file(s)
- `facelib` — 28 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `options` — 5 analysed file(s)
- `scripts` — 5 analysed file(s)
- `docs` — 3 analysed file(s)
- `web-demos` — 3 analysed file(s)
- `weights` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `b33cc7d639d6545bfcccc7e0bc6ae51f24e79c2b` is the revision these paths and observations refer to.
