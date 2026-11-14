# Project structure: facebookresearch/detr

**Analysed commit:** `29901c51d7fe8712168b8d0d64351170bc0f83e0`

**Commit reference:** [29901c51d7fe8712168b8d0d64351170bc0f83e0](https://github.com/facebookresearch/detr/commit/29901c51d7fe8712168b8d0d64351170bc0f83e0)

**Tree at this commit:** [facebookresearch/detr@29901c51d7fe](https://github.com/facebookresearch/detr/tree/29901c51d7fe8712168b8d0d64351170bc0f83e0)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | facebookresearch/detr |
| Description | End-to-End Object Detection with Transformers |
| Stars | 15344 |
| Forks | 2678 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `29901c51d7fe8712168b8d0d64351170bc0f83e0` |
| Retrieved at | 2026-11-14T19:09:04.661149+00:00 |
| Files in this snapshot | 42 |

## Directory tree

```text
.github/  (5 files)
  ISSUE_TEMPLATE/  (3 files)
    bugs.md
    questions-help-support.md
    unexpected-problems-bugs.md
  CODE_OF_CONDUCT.md
  CONTRIBUTING.md
d2/  (9 files)
  configs/  (2 files)
    detr_256_6_6_torchvision.yaml
    detr_segm_256_6_6_torchvision.yaml
  detr/  (4 files)
    __init__.py
    config.py
    dataset_mapper.py
    detr.py
  README.md
  converter.py
  train_net.py
datasets/  (6 files)
  __init__.py
  coco.py
  coco_eval.py
  coco_panoptic.py
  panoptic_eval.py
  transforms.py
models/  (7 files)
  __init__.py
  backbone.py
  detr.py
  matcher.py
  position_encoding.py
  segmentation.py
  transformer.py
util/  (4 files)
  __init__.py
  box_ops.py
  misc.py
  plot_utils.py
.gitignore
Dockerfile
LICENSE
README.md
engine.py
hubconf.py
main.py
requirements.txt
run_with_submitit.py
test_all.py
tox.ini
```

## Entry points

- [d2/converter.py:68](https://github.com/facebookresearch/detr/blob/29901c51d7fe8712168b8d0d64351170bc0f83e0/d2/converter.py#L68)
- [d2/train_net.py:135](https://github.com/facebookresearch/detr/blob/29901c51d7fe8712168b8d0d64351170bc0f83e0/d2/train_net.py#L135)
- [main.py:243](https://github.com/facebookresearch/detr/blob/29901c51d7fe8712168b8d0d64351170bc0f83e0/main.py#L243)
- [run_with_submitit.py:110](https://github.com/facebookresearch/detr/blob/29901c51d7fe8712168b8d0d64351170bc0f83e0/run_with_submitit.py#L110)
- [test_all.py:208](https://github.com/facebookresearch/detr/blob/29901c51d7fe8712168b8d0d64351170bc0f83e0/test_all.py#L208)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: add_detr_config. |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). Observed top-level functions: _make_detr, detr_resnet101, detr_resnet101_dc5, detr_resnet101_panoptic, detr_resnet50, detr_resnet… |
| d2 package | library | Observed | Groups 3 file(s) under d2 package (observed from repository paths and static analysis). Observed top-level classes: Detr, DetrDatasetMapper, MaskedBackbone. Observed top-level functions: build_transform_gen. |
| Data layer | data | Observed | Groups 7 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: Backbone, BackboneBase, DETR, DETRsegm, FrozenBatchNorm2d, HungarianMatcher. Observed top-level functio… |
| datasets package | library | Observed | Groups 6 file(s) under datasets package (observed from repository paths and static analysis). Observed top-level classes: CenterCrop, CocoDetection, CocoEvaluator, CocoPanoptic, Compose, ConvertCocoPolysToMask. Observed… |
| Application entry point | entrypoint | Observed | Groups 4 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Trainer. Observed top-level functions: get_args_parser, get_init_file, get_shared_folder,… |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: ONNXExporterTester, Tester. |
| util package | library | Observed | Groups 4 file(s) under util package (observed from repository paths and static analysis). Observed top-level classes: MetricLogger, NestedTensor, SmoothedValue. Observed top-level functions: _max_by_axis, _onnx_nested_t… |

## Important files

- `Dockerfile` (container)
- `d2/configs/detr_256_6_6_torchvision.yaml` (config)
- `d2/configs/detr_segm_256_6_6_torchvision.yaml` (config)
- `requirements.txt` (manifest)
- `tox.ini` (config)

## Top-level layout

- `(root files)` — 11 analysed file(s)
- `d2` — 9 analysed file(s)
- `models` — 7 analysed file(s)
- `datasets` — 6 analysed file(s)
- `.github` — 5 analysed file(s)
- `util` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- The GitHub repository was marked archived at selection time.

Commit `29901c51d7fe8712168b8d0d64351170bc0f83e0` is the revision these paths and observations refer to.
