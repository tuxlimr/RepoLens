# Project structure: ultralytics/yolov5

**Analysed commit:** `cb2f17fd5d790cfdd0c07c25351904df9affbe6e`

**Commit reference:** [cb2f17fd5d790cfdd0c07c25351904df9affbe6e](https://github.com/ultralytics/yolov5/commit/cb2f17fd5d790cfdd0c07c25351904df9affbe6e)

**Tree at this commit:** [ultralytics/yolov5@cb2f17fd5d79](https://github.com/ultralytics/yolov5/tree/cb2f17fd5d790cfdd0c07c25351904df9affbe6e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | ultralytics/yolov5 |
| Description | Ultralytics YOLOv5 in PyTorch for object detection, instance segmentation, classification, training, and export. |
| Stars | 58267 |
| Forks | 17432 |
| Licence | AGPL-3.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `cb2f17fd5d790cfdd0c07c25351904df9affbe6e` |
| Retrieved at | 2026-11-14T19:06:23.685003+00:00 |
| Files in this snapshot | 141 |

## Directory tree

```text
.github/  (12 files)
  ISSUE_TEMPLATE/  (4 files)
    bug-report.yml
    config.yml
    feature-request.yml
    question.yml
  workflows/  (7 files)
    ci-testing.yml
    cla.yml
    docker.yml
    format.yml
    links.yml
    merge-main-into-prs.yml
    stale.yml
  dependabot.yml
classify/  (4 files)
  predict.py
  train.py
  tutorial.ipynb
  val.py
data/  (27 files)
  hyps/  (6 files)
    hyp.Objects365.yaml
    hyp.VOC.yaml
    hyp.no-augmentation.yaml
    hyp.scratch-high.yaml
    hyp.scratch-low.yaml
    hyp.scratch-med.yaml
  scripts/  (7 files)
    download_weights.sh
    get_coco.sh
    get_coco128.sh
    get_imagenet.sh
    get_imagenet10.sh
    get_imagenet100.sh
    get_imagenet1000.sh
  Argoverse.yaml
  GlobalWheat2020.yaml
  ImageNet.yaml
  ImageNet10.yaml
  ImageNet100.yaml
  ImageNet1000.yaml
  Objects365.yaml
  SKU-110K.yaml
  VOC.yaml
  VisDrone.yaml
  coco.yaml
  coco128-seg.yaml
  coco128.yaml
  xView.yaml
models/  (34 files)
  hub/  (19 files)
    anchors.yaml
    yolov3-spp.yaml
    yolov3-tiny.yaml
    yolov3.yaml
    yolov5-bifpn.yaml
    yolov5-fpn.yaml
    yolov5-p2.yaml
    yolov5-p34.yaml
    yolov5-p6.yaml
    yolov5-p7.yaml
    yolov5-panet.yaml
    yolov5l6.yaml
    yolov5m6.yaml
    yolov5n6.yaml
    yolov5s-LeakyReLU.yaml
    yolov5s-ghost.yaml
    yolov5s-transformer.yaml
    yolov5s6.yaml
    yolov5x6.yaml
  segment/  (5 files)
    yolov5l-seg.yaml
    yolov5m-seg.yaml
    yolov5n-seg.yaml
    yolov5s-seg.yaml
    yolov5x-seg.yaml
  __init__.py
  common.py
  experimental.py
  tf.py
  yolo.py
  yolov5l.yaml
  yolov5m.yaml
  yolov5n.yaml
  yolov5s.yaml
  yolov5x.yaml
segment/  (4 files)
  predict.py
  train.py
  tutorial.ipynb
  val.py
tests/  (3 files)
  test_flask_rest_api.py
  test_invariant_common.py
  test_invariant_export.py
utils/  (39 files)
  docker/  (3 files)
    Dockerfile
    Dockerfile-arm64
    Dockerfile-cpu
  flask_rest_api/  (3 files)
    README.md
    example_request.py
    restapi.py
  loggers/  (12 files)
    clearml/  (4 files)
      … 4 files under this directory
    comet/  (5 files)
      … 5 files under this directory
    wandb/  (2 files)
      … 2 files under this directory
    __init__.py
  segment/  (7 files)
    __init__.py
    augmentations.py
    dataloaders.py
    general.py
    loss.py
    metrics.py
    plots.py
  __init__.py
  activations.py
  augmentations.py
  autoanchor.py
  autobatch.py
  callbacks.py
  dataloaders.py
  downloads.py
  general.py
  loss.py
  metrics.py
  plots.py
  torch_utils.py
  triton.py
.dockerignore
.gitattributes
.gitignore
AGENTS.md
CITATION.cff
CONTRIBUTING.md
LICENSE
README.md
README.zh-CN.md
benchmarks.py
detect.py
export.py
hubconf.py
pyproject.toml
requirements.txt
train.py
tutorial.ipynb
val.py
```

## Entry points

- [benchmarks.py:282](https://github.com/ultralytics/yolov5/blob/cb2f17fd5d790cfdd0c07c25351904df9affbe6e/benchmarks.py#L282)
- [classify/predict.py:239](https://github.com/ultralytics/yolov5/blob/cb2f17fd5d790cfdd0c07c25351904df9affbe6e/classify/predict.py#L239)
- [classify/train.py:381](https://github.com/ultralytics/yolov5/blob/cb2f17fd5d790cfdd0c07c25351904df9affbe6e/classify/train.py#L381)
- [classify/val.py:176](https://github.com/ultralytics/yolov5/blob/cb2f17fd5d790cfdd0c07c25351904df9affbe6e/classify/val.py#L176)
- [detect.py:437](https://github.com/ultralytics/yolov5/blob/cb2f17fd5d790cfdd0c07c25351904df9affbe6e/detect.py#L437)
- [export.py:1552](https://github.com/ultralytics/yolov5/blob/cb2f17fd5d790cfdd0c07c25351904df9affbe6e/export.py#L1552)
- [hubconf.py:469](https://github.com/ultralytics/yolov5/blob/cb2f17fd5d790cfdd0c07c25351904df9affbe6e/hubconf.py#L469)
- [models/tf.py:764](https://github.com/ultralytics/yolov5/blob/cb2f17fd5d790cfdd0c07c25351904df9affbe6e/models/tf.py#L764)
- [models/yolo.py:461](https://github.com/ultralytics/yolov5/blob/cb2f17fd5d790cfdd0c07c25351904df9affbe6e/models/yolo.py#L461)
- [segment/predict.py:295](https://github.com/ultralytics/yolov5/blob/cb2f17fd5d790cfdd0c07c25351904df9affbe6e/segment/predict.py#L295)
- [segment/train.py:748](https://github.com/ultralytics/yolov5/blob/cb2f17fd5d790cfdd0c07c25351904df9affbe6e/segment/train.py#L748)
- [segment/val.py:464](https://github.com/ultralytics/yolov5/blob/cb2f17fd5d790cfdd0c07c25351904df9affbe6e/segment/val.py#L464)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 55 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 10 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AutoShape, Bottleneck, BottleneckCSP, C3, C3Ghost, C3SPP. Observed top-level functions: _request_ssrf_… |
| Application entry point | entrypoint | Observed | Groups 16 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Flask. Observed routes: ROUTE (path not a literal). Observed top-level classe… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 3 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: DummyModel, DummyResults. Observed top-level functions: client, make_image_bytes, post_image, setup_model, t… |
| utils package | library | Observed | Groups 30 file(s) under utils package (observed from repository paths and static analysis). Observed top-level classes: AconC, Albumentations, BCEBlurWithLogitsLoss, Callbacks, CenterCrop, ClassificationDataset. Observe… |

## Important files

- `.dockerignore` (container)
- `.github/ISSUE_TEMPLATE/bug-report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature-request.yml` (config)
- `.github/ISSUE_TEMPLATE/question.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/ci-testing.yml` (ci)
- `.github/workflows/cla.yml` (ci)
- `.github/workflows/docker.yml` (ci)
- `.github/workflows/format.yml` (ci)
- `.github/workflows/links.yml` (ci)
- `.github/workflows/merge-main-into-prs.yml` (ci)
- `.github/workflows/stale.yml` (ci)
- `data/Argoverse.yaml` (config)
- `data/GlobalWheat2020.yaml` (config)
- `data/ImageNet.yaml` (config)
- `data/ImageNet10.yaml` (config)
- `data/ImageNet100.yaml` (config)
- `data/ImageNet1000.yaml` (config)
- `data/Objects365.yaml` (config)
- `data/SKU-110K.yaml` (config)
- `data/VOC.yaml` (config)
- `data/VisDrone.yaml` (config)
- `data/coco.yaml` (config)
- `data/coco128-seg.yaml` (config)
- `data/coco128.yaml` (config)
- `data/hyps/hyp.Objects365.yaml` (config)
- `data/hyps/hyp.VOC.yaml` (config)
- `data/hyps/hyp.no-augmentation.yaml` (config)
- `data/hyps/hyp.scratch-high.yaml` (config)
- `data/hyps/hyp.scratch-low.yaml` (config)
- `data/hyps/hyp.scratch-med.yaml` (config)
- `data/xView.yaml` (config)
- `models/hub/anchors.yaml` (config)
- `models/hub/yolov3-spp.yaml` (config)
- `models/hub/yolov3-tiny.yaml` (config)
- `models/hub/yolov3.yaml` (config)
- `models/hub/yolov5-bifpn.yaml` (config)
- `models/hub/yolov5-fpn.yaml` (config)
- `models/hub/yolov5-p2.yaml` (config)
- `models/hub/yolov5-p34.yaml` (config)
- `models/hub/yolov5-p6.yaml` (config)
- `models/hub/yolov5-p7.yaml` (config)
- `models/hub/yolov5-panet.yaml` (config)
- `models/hub/yolov5l6.yaml` (config)
- `models/hub/yolov5m6.yaml` (config)
- `models/hub/yolov5n6.yaml` (config)
- `models/hub/yolov5s-LeakyReLU.yaml` (config)
- `models/hub/yolov5s-ghost.yaml` (config)
- `models/hub/yolov5s-transformer.yaml` (config)
- `models/hub/yolov5s6.yaml` (config)
- `models/hub/yolov5x6.yaml` (config)
- `models/segment/yolov5l-seg.yaml` (config)
- `models/segment/yolov5m-seg.yaml` (config)
- `models/segment/yolov5n-seg.yaml` (config)
- `models/segment/yolov5s-seg.yaml` (config)
- `models/segment/yolov5x-seg.yaml` (config)
- `models/yolov5l.yaml` (config)
- `models/yolov5m.yaml` (config)
- `models/yolov5n.yaml` (config)
- `models/yolov5s.yaml` (config)
- `models/yolov5x.yaml` (config)
- `pyproject.toml` (manifest)
- `requirements.txt` (manifest)
- `utils/docker/Dockerfile` (container)
- `utils/docker/Dockerfile-arm64` (container)
- `utils/docker/Dockerfile-cpu` (container)
- `utils/loggers/comet/optimizer_config.json` (config)

## Top-level layout

- `utils` — 39 analysed file(s)
- `models` — 34 analysed file(s)
- `data` — 27 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `.github` — 12 analysed file(s)
- `classify` — 4 analysed file(s)
- `segment` — 4 analysed file(s)
- `tests` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `cb2f17fd5d790cfdd0c07c25351904df9affbe6e` is the revision these paths and observations refer to.
