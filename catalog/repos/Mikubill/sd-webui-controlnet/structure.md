# Project structure: Mikubill/sd-webui-controlnet

**Analysed commit:** `56cec5b2958edf3b1807b7e7b2b1b5186dbd2f81`

**Commit reference:** [56cec5b2958edf3b1807b7e7b2b1b5186dbd2f81](https://github.com/Mikubill/sd-webui-controlnet/commit/56cec5b2958edf3b1807b7e7b2b1b5186dbd2f81)

**Tree at this commit:** [Mikubill/sd-webui-controlnet@56cec5b2958e](https://github.com/Mikubill/sd-webui-controlnet/tree/56cec5b2958edf3b1807b7e7b2b1b5186dbd2f81)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Mikubill/sd-webui-controlnet |
| Description | WebUI extension for ControlNet |
| Stars | 17797 |
| Forks | 1998 |
| Licence | GPL-3.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `56cec5b2958edf3b1807b7e7b2b1b5186dbd2f81` |
| Retrieved at | 2026-11-14T19:08:27.923498+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.github/  (4 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.yml
    config.yml
  workflows/  (2 files)
    lint.yaml
    tests.yml
annotator/  (793 files)
  anime_face_segment/  (2 files)
    LICENSE
    __init__.py
  binary/  (1 files)
    __init__.py
  canny/  (1 files)
    __init__.py
  clipvision/  (1 files)
    __init__.py
  color/  (1 files)
    __init__.py
  densepose/  (2 files)
    __init__.py
    densepose.py
  hed/  (1 files)
    __init__.py
  keypose/  (3 files)
    __init__.py
    faster_rcnn_r50_fpn_coco.py
    hrnet_w48_coco_256x192.py
  lama/  (33 files)
    saicinpainting/  (31 files)
      … 31 files under this directory
    __init__.py
    config.yaml
  leres/  (24 files)
    leres/  (7 files)
      … 7 files under this directory
    pix2pix/  (16 files)
      … 16 files under this directory
    __init__.py
  lineart/  (2 files)
    LICENSE
    __init__.py
  lineart_anime/  (2 files)
    LICENSE
    __init__.py
  manga_line/  (2 files)
    LICENSE
    __init__.py
  mediapipe_face/  (2 files)
    __init__.py
    mediapipe_face_common.py
  midas/  (12 files)
    midas/  (8 files)
      … 8 files under this directory
    LICENSE
    __init__.py
    api.py
    utils.py
  mlsd/  (5 files)
    models/  (2 files)
      … 2 files under this directory
    LICENSE
    __init__.py
    utils.py
  mmpkg/  (272 files)
    mmcv/  (173 files)
      … 173 files under this directory
    mmseg/  (99 files)
      … 99 files under this directory
  mobile_sam/  (1 files)
    __init__.py
  normalbae/  (35 files)
    models/  (33 files)
      … 33 files under this directory
    LICENSE
    __init__.py
  normaldsine/  (2 files)
    LICENSE
    __init__.py
  oneformer/  (255 files)
    configs/  (6 files)
      … 6 files under this directory
    detectron2/  (182 files)
      … 182 files under this directory
    oneformer/  (60 files)
      … 60 files under this directory
    pycocotools/  (4 files)
      … 4 files under this directory
    LICENSE
    __init__.py
    api.py
  openpose/  (12 files)
    LICENSE
    __init__.py
    animalpose.py
    body.py
    cv_ox_det.py
    cv_ox_pose.py
    face.py
    hand.py
    model.py
    types.py
    util.py
    wholebody.py
  pidinet/  (3 files)
    LICENSE
    __init__.py
    model.py
  shuffle/  (1 files)
    __init__.py
  teed/  (7 files)
    Fmish.py
    Fsmish.py
    LICENSE.txt
    Xmish.py
    Xsmish.py
    __init__.py
    ted.py
  uniformer/  (52 files)
    configs/  (45 files)
      … 45 files under this directory
    mmcv_custom/  (2 files)
      … 2 files under this directory
    LICENSE
    __init__.py
    inference.py
    uniformer.py
    upernet_global_small.py
  zoe/  (54 files)
    zoedepth/  (52 files)
      … 52 files under this directory
    LICENSE
    __init__.py
  __init__.py
  annotator_path.py
  depth_anything.py
  depth_anything_v2.py
  util.py
.gitignore
LICENSE
README.md
```

## Entry points

- [annotator/lama/saicinpainting/training/modules/spatial_transform.py:43](https://github.com/Mikubill/sd-webui-controlnet/blob/56cec5b2958edf3b1807b7e7b2b1b5186dbd2f81/annotator/lama/saicinpainting/training/modules/spatial_transform.py#L43)
- [annotator/leres/leres/network_auxi.py:411](https://github.com/Mikubill/sd-webui-controlnet/blob/56cec5b2958edf3b1807b7e7b2b1b5186dbd2f81/annotator/leres/leres/network_auxi.py#L411)
- [annotator/leres/pix2pix/util/html.py:76](https://github.com/Mikubill/sd-webui-controlnet/blob/56cec5b2958edf3b1807b7e7b2b1b5186dbd2f81/annotator/leres/pix2pix/util/html.py#L76)
- [annotator/mmpkg/mmseg/utils/collect_env.py:15](https://github.com/Mikubill/sd-webui-controlnet/blob/56cec5b2958edf3b1807b7e7b2b1b5186dbd2f81/annotator/mmpkg/mmseg/utils/collect_env.py#L15)
- [annotator/normalbae/models/baseline.py:81](https://github.com/Mikubill/sd-webui-controlnet/blob/56cec5b2958edf3b1807b7e7b2b1b5186dbd2f81/annotator/normalbae/models/baseline.py#L81)
- [annotator/normalbae/models/submodules/efficientnet_repo/caffe2_benchmark.py:64](https://github.com/Mikubill/sd-webui-controlnet/blob/56cec5b2958edf3b1807b7e7b2b1b5186dbd2f81/annotator/normalbae/models/submodules/efficientnet_repo/caffe2_benchmark.py#L64)
- [annotator/normalbae/models/submodules/efficientnet_repo/caffe2_validate.py:137](https://github.com/Mikubill/sd-webui-controlnet/blob/56cec5b2958edf3b1807b7e7b2b1b5186dbd2f81/annotator/normalbae/models/submodules/efficientnet_repo/caffe2_validate.py#L137)
- [annotator/normalbae/models/submodules/efficientnet_repo/onnx_export.py:119](https://github.com/Mikubill/sd-webui-controlnet/blob/56cec5b2958edf3b1807b7e7b2b1b5186dbd2f81/annotator/normalbae/models/submodules/efficientnet_repo/onnx_export.py#L119)
- [annotator/normalbae/models/submodules/efficientnet_repo/onnx_optimize.py:83](https://github.com/Mikubill/sd-webui-controlnet/blob/56cec5b2958edf3b1807b7e7b2b1b5186dbd2f81/annotator/normalbae/models/submodules/efficientnet_repo/onnx_optimize.py#L83)
- [annotator/normalbae/models/submodules/efficientnet_repo/onnx_to_caffe.py:26](https://github.com/Mikubill/sd-webui-controlnet/blob/56cec5b2958edf3b1807b7e7b2b1b5186dbd2f81/annotator/normalbae/models/submodules/efficientnet_repo/onnx_to_caffe.py#L26)
- [annotator/normalbae/models/submodules/efficientnet_repo/onnx_validate.py:111](https://github.com/Mikubill/sd-webui-controlnet/blob/56cec5b2958edf3b1807b7e7b2b1b5186dbd2f81/annotator/normalbae/models/submodules/efficientnet_repo/onnx_validate.py#L111)
- [annotator/normalbae/models/submodules/efficientnet_repo/validate.py:165](https://github.com/Mikubill/sd-webui-controlnet/blob/56cec5b2958edf3b1807b7e7b2b1b5186dbd2f81/annotator/normalbae/models/submodules/efficientnet_repo/validate.py#L165)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| annotator package | library | Observed | Groups 471 file(s) under annotator package (observed from repository paths and static analysis). Observed top-level classes: ADE20KDataset, AMPTrainer, ASPP, AddReadout, AdjustGamma, AlexNet. Observed top-level function… |
| API layer | api | Observed | Groups 5 file(s) under api layer (observed from repository paths and static analysis). Observed top-level classes: BaseFileHandler, JsonHandler, PickleHandler, YamlHandler. Observed top-level functions: set_default. |
| Configuration and deployment | config | Observed | Groups 40 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: CfgNode, Config, ConfigDict, ConverterV1, ConverterV2, DictAction. Observed top-leve… |
| Data layer | data | Observed | Groups 181 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: ACM, AFNB, ANNHead, APCHead, APNB, ASPPHead. Observed top-level functions: DPT_BEiT_B_384, DPT_BEiT_L… |
| Application entry point | entrypoint | Observed | Groups 32 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: AO, ATA, Body, COCOPanopticEvaluator, CoFusion, CoFusion2. Observed top-level functions:… |
| External integrations | external | Observed | Groups 2 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: BaseStorageBackend, COCOeval_opt, CephBackend, FileClient, HTTPBackend, HardDiskBackend. |
| Service / domain layer | service | Observed | Groups 12 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: BasePixelSampler, DistEvalHook, EvalHook, OHEMPixelSampler. Observed top-level functions:… |
| Tests | test | Observed | Groups 3 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: DatasetMapperTTA, GeneralizedRCNNWithTTA, MultiScaleFlipAug, TestOptions. |

## Important files

- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/lint.yaml` (ci)
- `.github/workflows/tests.yml` (ci)
- `annotator/lama/config.yaml` (config)
- `annotator/mmpkg/mmcv/model_zoo/deprecated.json` (config)
- `annotator/mmpkg/mmcv/model_zoo/mmcls.json` (config)
- `annotator/mmpkg/mmcv/model_zoo/open_mmlab.json` (config)
- `annotator/normalbae/models/submodules/efficientnet_repo/requirements.txt` (manifest)
- `annotator/normalbae/models/submodules/efficientnet_repo/setup.py` (manifest)
- `annotator/oneformer/configs/ade20k/Base-ADE20K-UnifiedSegmentation.yaml` (config)
- `annotator/oneformer/configs/ade20k/oneformer_R50_bs16_160k.yaml` (config)
- `annotator/oneformer/configs/ade20k/oneformer_swin_large_IN21k_384_bs16_160k.yaml` (config)
- `annotator/oneformer/configs/coco/Base-COCO-UnifiedSegmentation.yaml` (config)
- `annotator/oneformer/configs/coco/oneformer_R50_bs16_50ep.yaml` (config)
- `annotator/oneformer/configs/coco/oneformer_swin_large_IN21k_384_bs16_100ep.yaml` (config)
- `annotator/oneformer/oneformer/modeling/pixel_decoder/ops/setup.py` (manifest)
- `annotator/zoe/zoedepth/models/base_models/midas_repo/Dockerfile` (container)
- `annotator/zoe/zoedepth/models/base_models/midas_repo/environment.yaml` (config)

## Top-level layout

- `annotator` — 793 analysed file(s)
- `.github` — 4 analysed file(s)
- `(root files)` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `56cec5b2958edf3b1807b7e7b2b1b5186dbd2f81` is the revision these paths and observations refer to.
