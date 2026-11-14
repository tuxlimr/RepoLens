# Project structure: jindongwang/transferlearning

**Analysed commit:** `d77ef50a2e7ecdd4f3354148205666970ba809b6`

**Commit reference:** [d77ef50a2e7ecdd4f3354148205666970ba809b6](https://github.com/jindongwang/transferlearning/commit/d77ef50a2e7ecdd4f3354148205666970ba809b6)

**Tree at this commit:** [jindongwang/transferlearning@d77ef50a2e7e](https://github.com/jindongwang/transferlearning/tree/d77ef50a2e7ecdd4f3354148205666970ba809b6)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | jindongwang/transferlearning |
| Description | Transfer learning / domain adaptation / domain generalization / multi-task learning etc. Papers, codes, datasets, applications, tutorials.-迁移学习 |
| Stars | 14387 |
| Forks | 3823 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `d77ef50a2e7ecdd4f3354148205666970ba809b6` |
| Retrieved at | 2026-11-14T19:09:26.988625+00:00 |
| Files in this snapshot | 458 |

## Directory tree

```text
.github/  (2 files)
  ISSUE_TEMPLATE/  (1 files)
    bug_report.md
  FUNDING.yml
code/  (437 files)
  ASR/  (24 files)
    Adapter/  (10 files)
      … 10 files under this directory
    CMatch/  (13 files)
      … 13 files under this directory
    readme.md
  BDA/  (1 files)
    readme.md
  DeepDA/  (32 files)
    BNM/  (3 files)
      … 3 files under this directory
    DAAN/  (2 files)
      … 2 files under this directory
    DAN/  (3 files)
      … 3 files under this directory
    DANN/  (3 files)
      … 3 files under this directory
    DSAN/  (3 files)
      … 3 files under this directory
    DeepCoral/  (3 files)
      … 3 files under this directory
    loss_funcs/  (7 files)
      … 7 files under this directory
    README.md
    backbones.py
    data_loader.py
    main.py
    models.py
    requirements.txt
    transfer_losses.py
    utils.py
  DeepDG/  (30 files)
    alg/  (15 files)
      … 15 files under this directory
    datautil/  (5 files)
      … 5 files under this directory
    network/  (4 files)
      … 4 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    utils/  (1 files)
      … 1 files under this directory
    readme.md
    requirements.txt
    train.py
  clip/  (11 files)
    data/  (3 files)
      … 3 files under this directory
    log/  (1 files)
      … 1 files under this directory
    README.md
    __init__.py
    clip_model.py
    main.py
    requirements.txt
    test_clip.py
    utils.py
  deep/  (265 files)
    B-JMMD/  (33 files)
      … 33 files under this directory
    CSG/  (43 files)
      … 43 files under this directory
    DAAN/  (8 files)
      … 8 files under this directory
    DAN/  (1 files)
      … 1 files under this directory
    DANN(RevGrad)/  (2 files)
      … 2 files under this directory
    DDC_DeepCoral/  (1 files)
      … 1 files under this directory
    DSAN/  (1 files)
      … 1 files under this directory
    DaNN/  (5 files)
      … 5 files under this directory
    DeepCoral/  (1 files)
      … 1 files under this directory
    DeepMEDA/  (8 files)
      … 8 files under this directory
    Learning-to-Match/  (1 files)
      … 1 files under this directory
    MRAN/  (5 files)
      … 5 files under this directory
    ReMoS/  (95 files)
      … 95 files under this directory
    TCP/  (6 files)
      … 6 files under this directory
    adarnn/  (32 files)
      … 32 files under this directory
    finetune_AlexNet_ResNet/  (4 files)
      … 4 files under this directory
    fixed/  (18 files)
      … 18 files under this directory
    README.md
  distance/  (5 files)
    coral_pytorch.py
    mmd_matlab.m
    mmd_numpy_sklearn.py
    mmd_pytorch.py
    proxy_a_distance.py
  feature_extractor/  (8 files)
    for_digit_data/  (3 files)
      … 3 files under this directory
    for_image_data/  (4 files)
      … 4 files under this directory
    readme.md
  traditional/  (57 files)
    BDA/  (4 files)
      … 4 files under this directory
    CORAL/  (4 files)
      … 4 files under this directory
    EasyTL/  (8 files)
      … 8 files under this directory
    GFK/  (4 files)
      … 4 files under this directory
    JDA/  (3 files)
      … 3 files under this directory
    MEDA/  (8 files)
      … 8 files under this directory
    TCA/  (3 files)
      … 3 files under this directory
    pyEasyTL/  (12 files)
      … 12 files under this directory
    sot/  (3 files)
      … 3 files under this directory
    KMM.py
    MyTJM.m
    SA_SVM.m
    SCL.py
    SFA.py
    SVM.m
    TrAdaBoost.py
    readme.md
  utils/  (2 files)
    feature_vis.py
    grl.py
  Integrated sensing and communication (LSTM and VGG 16 model for digit and image classification, will be used for sensing and communication in 6G networks)
  README.md
data/  (3 files)
  benchmark.md
  dataset.md
  readme.md
doc/  (6 files)
  awesome_paper_date.md
  domain_adaptation.md
  scholar_TL.md
  transfer_learning_application.md
  venues.md
  迁移学习简介.md
docs/  (3 files)
  CNAME
  _config.yml
  index.md
notebooks/  (2 files)
  deep_transfer_tutorial.ipynb
  traditional_transfer_learning.ipynb
.gitattributes
.gitignore
CONTRIBUTING.md
LICENSE
README.md
```

## Entry points

- [code/ASR/Adapter/train.py:317](https://github.com/jindongwang/transferlearning/blob/d77ef50a2e7ecdd4f3354148205666970ba809b6/code/ASR/Adapter/train.py#L317)
- [code/ASR/CMatch/train.py:212](https://github.com/jindongwang/transferlearning/blob/d77ef50a2e7ecdd4f3354148205666970ba809b6/code/ASR/CMatch/train.py#L212)
- [code/DeepDA/main.py:193](https://github.com/jindongwang/transferlearning/blob/d77ef50a2e7ecdd4f3354148205666970ba809b6/code/DeepDA/main.py#L193)
- [code/DeepDG/train.py:102](https://github.com/jindongwang/transferlearning/blob/d77ef50a2e7ecdd4f3354148205666970ba809b6/code/DeepDG/train.py#L102)
- [code/clip/clip_model.py:163](https://github.com/jindongwang/transferlearning/blob/d77ef50a2e7ecdd4f3354148205666970ba809b6/code/clip/clip_model.py#L163)
- [code/clip/data/data_loader.py:96](https://github.com/jindongwang/transferlearning/blob/d77ef50a2e7ecdd4f3354148205666970ba809b6/code/clip/data/data_loader.py#L96)
- [code/clip/data/download_data.py:261](https://github.com/jindongwang/transferlearning/blob/d77ef50a2e7ecdd4f3354148205666970ba809b6/code/clip/data/download_data.py#L261)
- [code/clip/data/download_data_azcopy.py:26](https://github.com/jindongwang/transferlearning/blob/d77ef50a2e7ecdd4f3354148205666970ba809b6/code/clip/data/download_data_azcopy.py#L26)
- [code/clip/main.py:103](https://github.com/jindongwang/transferlearning/blob/d77ef50a2e7ecdd4f3354148205666970ba809b6/code/clip/main.py#L103)
- [code/deep/CSG/a-domainbed/main.py:30](https://github.com/jindongwang/transferlearning/blob/d77ef50a2e7ecdd4f3354148205666970ba809b6/code/deep/CSG/a-domainbed/main.py#L30)
- [code/deep/CSG/a-domainbed/visual.py:214](https://github.com/jindongwang/transferlearning/blob/d77ef50a2e7ecdd4f3354148205666970ba809b6/code/deep/CSG/a-domainbed/visual.py#L214)
- [code/deep/CSG/a-imageclef/main.py:13](https://github.com/jindongwang/transferlearning/blob/d77ef50a2e7ecdd4f3354148205666970ba809b6/code/deep/CSG/a-imageclef/main.py#L13)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| code package | library | Observed | Groups 235 file(s) under code package (observed from repository paths and static analysis). Observed top-level classes: ANDMask, ActList, ActNetwork, AdaRNN, Adapter, AdaptiveDecoder. Observed top-level functions: BNM,… |
| Configuration and deployment | config | Observed | Groups 23 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 2 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: Network, TransferNet. |
| Application entry point | entrypoint | Observed | Groups 65 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: BDA, CORAL, CUB200Data, ClipModel, DANNet, FeatureExtractor. Observed top-level functions… |
| Tests | test | Observed | Groups 6 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: classify_imagenetr, gather_res, get_args, get_max_values, load_data, load_model. |

## Important files

- `.github/FUNDING.yml` (config)
- `code/ASR/Adapter/config/adapter_example.yaml` (config)
- `code/ASR/Adapter/config/adapterfusion_example.yaml` (config)
- `code/ASR/Adapter/config/finetune_meta_adapter_example.yaml` (config)
- `code/ASR/Adapter/config/meta_adapter_example.yaml` (config)
- `code/ASR/CMatch/config/adv_example.yaml` (config)
- `code/ASR/CMatch/config/ctc_align_example.yaml` (config)
- `code/ASR/CMatch/config/frame_average_example.yaml` (config)
- `code/ASR/CMatch/config/mmd_example.yaml` (config)
- `code/ASR/CMatch/config/pseudo_ctc_pred_example.yaml` (config)
- `code/ASR/CMatch/config/train.yaml` (config)
- `code/DeepDA/BNM/BNM.yaml` (config)
- `code/DeepDA/DAAN/DAAN.yaml` (config)
- `code/DeepDA/DAN/DAN.yaml` (config)
- `code/DeepDA/DANN/DANN.yaml` (config)
- `code/DeepDA/DSAN/DSAN.yaml` (config)
- `code/DeepDA/DeepCoral/DeepCoral.yaml` (config)
- `code/DeepDA/requirements.txt` (manifest)
- `code/DeepDG/requirements.txt` (manifest)
- `code/clip/requirements.txt` (manifest)
- `code/deep/CSG/arch/mlpstru.json` (config)
- `code/deep/CSG/requirements.txt` (manifest)
- `code/deep/adarnn/requirements.txt` (manifest)
- `code/deep/fixed/requirements.txt` (manifest)
- `docs/_config.yml` (config)

## Top-level layout

- `code` — 437 analysed file(s)
- `doc` — 6 analysed file(s)
- `(root files)` — 5 analysed file(s)
- `data` — 3 analysed file(s)
- `docs` — 3 analysed file(s)
- `.github` — 2 analysed file(s)
- `notebooks` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `d77ef50a2e7ecdd4f3354148205666970ba809b6` is the revision these paths and observations refer to.
