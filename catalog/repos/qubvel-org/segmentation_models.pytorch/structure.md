# Project structure: qubvel-org/segmentation_models.pytorch

**Analysed commit:** `5b8e53f0ebece38823477b656c442ea389b71669`

**Commit reference:** [5b8e53f0ebece38823477b656c442ea389b71669](https://github.com/qubvel-org/segmentation_models.pytorch/commit/5b8e53f0ebece38823477b656c442ea389b71669)

**Tree at this commit:** [qubvel-org/segmentation_models.pytorch@5b8e53f0ebec](https://github.com/qubvel-org/segmentation_models.pytorch/tree/5b8e53f0ebece38823477b656c442ea389b71669)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | qubvel-org/segmentation_models.pytorch |
| Description | Semantic segmentation models with 500+ pretrained convolutional and transformer-based backbones. |
| Stars | 11806 |
| Forks | 1854 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `5b8e53f0ebece38823477b656c442ea389b71669` |
| Retrieved at | 2026-11-14T19:10:24.087060+00:00 |
| Files in this snapshot | 167 |

## Directory tree

```text
.devcontainer/  (1 files)
  devcontainer.json
.github/  (6 files)
  workflows/  (3 files)
    pypi.yml
    stale.yaml
    tests.yml
  FUNDING.yml
  codecov.yml
  dependabot.yml
docs/  (14 files)
  Makefile
  conf.py
  encoders.rst
  encoders_dpt.rst
  encoders_timm.rst
  index.rst
  insights.rst
  install.rst
  losses.rst
  make.bat
  metrics.rst
  models.rst
  quickstart.rst
  save_load.rst
examples/  (3 files)
  binary_segmentation_buildings.py
  convert_to_onnx.ipynb
  save_load_model_and_share_with_hf_hub.ipynb
licenses/  (4 files)
  LICENSES.md
  LICENSE_apache.md
  LICENSE_apple.md
  LICENSE_nvidia.md
misc/  (3 files)
  generate_table.py
  generate_table_timm.py
  generate_test_models.py
requirements/  (4 files)
  docs.txt
  minimum.old
  required.txt
  test.txt
scripts/  (3 files)
  models-conversions/  (3 files)
    dpt-original-to-smp.py
    segformer-original-decoder-to-smp.py
    upernet-hf-to-smp.py
segmentation_models_pytorch/  (91 files)
  base/  (7 files)
    __init__.py
    heads.py
    hub_mixin.py
    initialization.py
    model.py
    modules.py
    utils.py
  datasets/  (2 files)
    __init__.py
    oxford_pet.py
  decoders/  (34 files)
    deeplabv3/  (3 files)
      … 3 files under this directory
    dpt/  (3 files)
      … 3 files under this directory
    fpn/  (3 files)
      … 3 files under this directory
    linknet/  (3 files)
      … 3 files under this directory
    manet/  (3 files)
      … 3 files under this directory
    pan/  (3 files)
      … 3 files under this directory
    pspnet/  (3 files)
      … 3 files under this directory
    segformer/  (3 files)
      … 3 files under this directory
    unet/  (3 files)
      … 3 files under this directory
    unetplusplus/  (3 files)
      … 3 files under this directory
    upernet/  (3 files)
      … 3 files under this directory
    __init__.py
  encoders/  (26 files)
    __init__.py
    _base.py
    _dpn.py
    _efficientnet.py
    _inceptionresnetv2.py
    _inceptionv4.py
    _preprocessing.py
    _senet.py
    _utils.py
    _xception.py
    densenet.py
    dpn.py
    efficientnet.py
    inceptionresnetv2.py
    inceptionv4.py
    mix_transformer.py
    mobilenet.py
    mobileone.py
    resnet.py
    senet.py
    timm_efficientnet.py
    timm_sknet.py
    timm_universal.py
    timm_vit.py
    … 2 more files
  losses/  (11 files)
    __init__.py
    _functional.py
    constants.py
    dice.py
    focal.py
    jaccard.py
    lovasz.py
    mcc.py
    soft_bce.py
    soft_ce.py
    tversky.py
  metrics/  (2 files)
    __init__.py
    functional.py
  utils/  (7 files)
    __init__.py
    base.py
    functional.py
    losses.py
    meter.py
    metrics.py
    train.py
  __init__.py
  __version__.py
tests/  (31 files)
  base/  (2 files)
    test_freeze_encoder.py
    test_modules.py
  encoders/  (10 files)
    __init__.py
    base.py
    test_batchnorm_deprecation.py
    test_common.py
    test_pretrainedmodels_encoders.py
    test_smp_encoders.py
    test_timm_ported_encoders.py
    test_timm_universal.py
    test_timm_vit_encoders.py
    test_torchvision_encoders.py
  models/  (13 files)
    __init__.py
    base.py
    test_deeplab.py
    test_dpt.py
    test_fpn.py
    test_linknet.py
    test_manet.py
    test_pan.py
    test_psp.py
    test_segformer.py
    test_unet.py
    test_unetplusplus.py
    test_upernet.py
  __init__.py
  conftest.py
  test_base.py
  test_losses.py
  test_preprocessing.py
  utils.py
.gitignore
.readthedocs.yaml
HALLOFFAME.md
LICENSE
Makefile
README.md
pyproject.toml
```

## Entry points

- [misc/generate_table_timm.py:87](https://github.com/qubvel-org/segmentation_models.pytorch/blob/5b8e53f0ebece38823477b656c442ea389b71669/misc/generate_table_timm.py#L87)
- [scripts/models-conversions/dpt-original-to-smp.py:33](https://github.com/qubvel-org/segmentation_models.pytorch/blob/5b8e53f0ebece38823477b656c442ea389b71669/scripts/models-conversions/dpt-original-to-smp.py#L33)
- [scripts/models-conversions/segformer-original-decoder-to-smp.py:138](https://github.com/qubvel-org/segmentation_models.pytorch/blob/5b8e53f0ebece38823477b656c442ea389b71669/scripts/models-conversions/segformer-original-decoder-to-smp.py#L138)
- [scripts/models-conversions/upernet-hf-to-smp.py:245](https://github.com/qubvel-org/segmentation_models.pytorch/blob/5b8e53f0ebece38823477b656c442ea389b71669/scripts/models-conversions/upernet-hf-to-smp.py#L245)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 12 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: DPT, DeepLabV3, DeepLabV3Plus, FPN, Linknet, MAnet. |
| Application entry point | entrypoint | Observed | Groups 4 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: check_features_and_reduction, convert_model, convert_old_keys_to_new_keys, convert_state… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| misc package | library | Observed | Groups 2 file(s) under misc package (observed from repository paths and static analysis). Observed top-level functions: save_and_push, wrap_row. |
| segmentation_models_pytorch package | library | Observed | Groups 79 file(s) under segmentation_models_pytorch package (observed from repository paths and static analysis). Observed top-level classes: ASPP, ASPPConv, ASPPPooling, ASPPSeparableConv, Accuracy, Activation. Observe… |
| Tests | test | Observed | Groups 31 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: BaseEncoderTester, BaseModelTester, TestDPNEncoder, TestDPTModel, TestDeeplabV3Model, TestDeeplabV3PlusMode… |

## Important files

- `.devcontainer/devcontainer.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/codecov.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/pypi.yml` (ci)
- `.github/workflows/stale.yaml` (ci)
- `.github/workflows/tests.yml` (ci)
- `.readthedocs.yaml` (config)
- `pyproject.toml` (manifest)

## Top-level layout

- `segmentation_models_pytorch` — 91 analysed file(s)
- `tests` — 31 analysed file(s)
- `docs` — 14 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `.github` — 6 analysed file(s)
- `licenses` — 4 analysed file(s)
- `requirements` — 4 analysed file(s)
- `examples` — 3 analysed file(s)
- `misc` — 3 analysed file(s)
- `scripts` — 3 analysed file(s)
- `.devcontainer` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `5b8e53f0ebece38823477b656c442ea389b71669` is the revision these paths and observations refer to.
