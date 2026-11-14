# Project structure: xinntao/Real-ESRGAN

**Analysed commit:** `a4abfb2979a7bbff3f69f58f58ae324608821e27`

**Commit reference:** [a4abfb2979a7bbff3f69f58f58ae324608821e27](https://github.com/xinntao/Real-ESRGAN/commit/a4abfb2979a7bbff3f69f58f58ae324608821e27)

**Tree at this commit:** [xinntao/Real-ESRGAN@a4abfb2979a7](https://github.com/xinntao/Real-ESRGAN/tree/a4abfb2979a7bbff3f69f58f58ae324608821e27)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | xinntao/Real-ESRGAN |
| Description | Real-ESRGAN aims at developing Practical Algorithms for General Image/Video Restoration. |
| Stars | 37497 |
| Forks | 4536 |
| Licence | BSD-3-Clause |
| Language | Python |
| Default branch | master |
| Analysed commit | `a4abfb2979a7bbff3f69f58f58ae324608821e27` |
| Retrieved at | 2026-11-14T19:06:48.095120+00:00 |
| Files in this snapshot | 67 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (3 files)
    publish-pip.yml
    pylint.yml
    release.yml
.vscode/  (1 files)
  settings.json
docs/  (11 files)
  CONTRIBUTING.md
  FAQ.md
  Training.md
  Training_CN.md
  anime_comparisons.md
  anime_comparisons_CN.md
  anime_model.md
  anime_video_model.md
  feedback.md
  model_zoo.md
  ncnn_conversion.md
experiments/  (1 files)
  pretrained_models/  (1 files)
    README.md
options/  (6 files)
  finetune_realesrgan_x4plus.yml
  finetune_realesrgan_x4plus_pairdata.yml
  train_realesrgan_x2plus.yml
  train_realesrgan_x4plus.yml
  train_realesrnet_x2plus.yml
  train_realesrnet_x4plus.yml
realesrgan/  (12 files)
  archs/  (3 files)
    __init__.py
    discriminator_arch.py
    srvgg_arch.py
  data/  (3 files)
    __init__.py
    realesrgan_dataset.py
    realesrgan_paired_dataset.py
  models/  (3 files)
    __init__.py
    realesrgan_model.py
    realesrnet_model.py
  __init__.py
  train.py
  utils.py
scripts/  (5 files)
  extract_subimages.py
  generate_meta_info.py
  generate_meta_info_pairdata.py
  generate_multiscale_DF2K.py
  pytorch2onnx.py
tests/  (12 files)
  data/  (8 files)
    gt.lmdb/  (1 files)
      … 1 files under this directory
    lq.lmdb/  (1 files)
      … 1 files under this directory
    meta_info_gt.txt
    meta_info_pair.txt
    test_realesrgan_dataset.yml
    test_realesrgan_model.yml
    test_realesrgan_paired_dataset.yml
    test_realesrnet_model.yml
  test_dataset.py
  test_discriminator_arch.py
  test_model.py
  test_utils.py
weights/  (1 files)
  README.md
.gitignore
.pre-commit-config.yaml
CODE_OF_CONDUCT.md
LICENSE
MANIFEST.in
README.md
README_CN.md
VERSION
cog.yaml
cog_predict.py
inference_realesrgan.py
inference_realesrgan_video.py
requirements.txt
setup.cfg
setup.py
```

## Entry points

- [inference_realesrgan.py:165](https://github.com/xinntao/Real-ESRGAN/blob/a4abfb2979a7bbff3f69f58f58ae324608821e27/inference_realesrgan.py#L165)
- [inference_realesrgan_video.py:397](https://github.com/xinntao/Real-ESRGAN/blob/a4abfb2979a7bbff3f69f58f58ae324608821e27/inference_realesrgan_video.py#L397)
- [realesrgan/train.py:9](https://github.com/xinntao/Real-ESRGAN/blob/a4abfb2979a7bbff3f69f58f58ae324608821e27/realesrgan/train.py#L9)
- [scripts/extract_subimages.py:120](https://github.com/xinntao/Real-ESRGAN/blob/a4abfb2979a7bbff3f69f58f58ae324608821e27/scripts/extract_subimages.py#L120)
- [scripts/generate_meta_info.py:30](https://github.com/xinntao/Real-ESRGAN/blob/a4abfb2979a7bbff3f69f58f58ae324608821e27/scripts/generate_meta_info.py#L30)
- [scripts/generate_meta_info_pairdata.py:23](https://github.com/xinntao/Real-ESRGAN/blob/a4abfb2979a7bbff3f69f58f58ae324608821e27/scripts/generate_meta_info_pairdata.py#L23)
- [scripts/generate_multiscale_DF2K.py:38](https://github.com/xinntao/Real-ESRGAN/blob/a4abfb2979a7bbff3f69f58f58ae324608821e27/scripts/generate_multiscale_DF2K.py#L38)
- [scripts/pytorch2onnx.py:27](https://github.com/xinntao/Real-ESRGAN/blob/a4abfb2979a7bbff3f69f58f58ae324608821e27/scripts/pytorch2onnx.py#L27)
- [setup.py:82](https://github.com/xinntao/Real-ESRGAN/blob/a4abfb2979a7bbff3f69f58f58ae324608821e27/setup.py#L82)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 11 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: get_git_hash, get_hash, get_requirements, get_version, readme, write_version_py. |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). Observed top-level classes: Predictor. Observed top-level functions: clean_folder. |
| Data layer | data | Observed | Groups 6 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: RealESRGANDataset, RealESRGANModel, RealESRGANPairedDataset, RealESRNetModel. |
| Application entry point | entrypoint | Observed | Groups 8 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Reader, Writer. Observed top-level functions: extract_subimages, get_sub_video, get_video_… |
| realesrgan package | library | Observed | Groups 5 file(s) under realesrgan package (observed from repository paths and static analysis). Observed top-level classes: IOConsumer, PrefetchReader, RealESRGANer, SRVGGNetCompact, UNetDiscriminatorSN. |
| Tests | test | Observed | Groups 12 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: test_realesrgan_dataset, test_realesrgan_model, test_realesrgan_paired_dataset, test_realesrganer, test_r… |

## Important files

- `.github/workflows/publish-pip.yml` (ci)
- `.github/workflows/pylint.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `.vscode/settings.json` (config)
- `MANIFEST.in` (manifest)
- `cog.yaml` (config)
- `options/finetune_realesrgan_x4plus.yml` (config)
- `options/finetune_realesrgan_x4plus_pairdata.yml` (config)
- `options/train_realesrgan_x2plus.yml` (config)
- `options/train_realesrgan_x4plus.yml` (config)
- `options/train_realesrnet_x2plus.yml` (config)
- `options/train_realesrnet_x4plus.yml` (config)
- `requirements.txt` (manifest)
- `setup.cfg` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `(root files)` — 15 analysed file(s)
- `realesrgan` — 12 analysed file(s)
- `tests` — 12 analysed file(s)
- `docs` — 11 analysed file(s)
- `options` — 6 analysed file(s)
- `scripts` — 5 analysed file(s)
- `.github` — 3 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `experiments` — 1 analysed file(s)
- `weights` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `a4abfb2979a7bbff3f69f58f58ae324608821e27` is the revision these paths and observations refer to.
