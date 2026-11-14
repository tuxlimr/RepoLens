# Project structure: TencentARC/GFPGAN

**Analysed commit:** `7552a7791caad982045a7bbe5634bbf1cd5c8679`

**Commit reference:** [7552a7791caad982045a7bbe5634bbf1cd5c8679](https://github.com/TencentARC/GFPGAN/commit/7552a7791caad982045a7bbe5634bbf1cd5c8679)

**Tree at this commit:** [TencentARC/GFPGAN@7552a7791caa](https://github.com/TencentARC/GFPGAN/tree/7552a7791caad982045a7bbe5634bbf1cd5c8679)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | TencentARC/GFPGAN |
| Description | GFPGAN aims at developing Practical Algorithms for Real-world Face Restoration. |
| Stars | 37701 |
| Forks | 6279 |
| Licence | Other |
| Language | Python |
| Default branch | master |
| Analysed commit | `7552a7791caad982045a7bbe5634bbf1cd5c8679` |
| Retrieved at | 2026-11-14T19:06:47.867340+00:00 |
| Files in this snapshot | 51 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (3 files)
    publish-pip.yml
    pylint.yml
    release.yml
.vscode/  (1 files)
  settings.json
experiments/  (1 files)
  pretrained_models/  (1 files)
    README.md
gfpgan/  (16 files)
  archs/  (8 files)
    __init__.py
    arcface_arch.py
    gfpgan_bilinear_arch.py
    gfpganv1_arch.py
    gfpganv1_clean_arch.py
    restoreformer_arch.py
    stylegan2_bilinear_arch.py
    stylegan2_clean_arch.py
  data/  (2 files)
    __init__.py
    ffhq_degradation_dataset.py
  models/  (2 files)
    __init__.py
    gfpgan_model.py
  weights/  (1 files)
    README.md
  __init__.py
  train.py
  utils.py
options/  (2 files)
  train_gfpgan_v1.yml
  train_gfpgan_v1_simple.yml
scripts/  (2 files)
  convert_gfpganv_to_clean.py
  parse_landmark.py
tests/  (9 files)
  data/  (3 files)
    ffhq_gt.lmdb/  (1 files)
      … 1 files under this directory
    test_ffhq_degradation_dataset.yml
    test_gfpgan_model.yml
  test_arcface_arch.py
  test_ffhq_degradation_dataset.py
  test_gfpgan_arch.py
  test_gfpgan_model.py
  test_stylegan2_clean_arch.py
  test_utils.py
.gitignore
.pre-commit-config.yaml
CODE_OF_CONDUCT.md
Comparisons.md
FAQ.md
LICENSE
MANIFEST.in
PaperModel.md
README.md
README_CN.md
VERSION
cog.yaml
cog_predict.py
inference_gfpgan.py
requirements.txt
setup.cfg
setup.py
```

## Entry points

- [gfpgan/train.py:9](https://github.com/TencentARC/GFPGAN/blob/7552a7791caad982045a7bbe5634bbf1cd5c8679/gfpgan/train.py#L9)
- [inference_gfpgan.py:173](https://github.com/TencentARC/GFPGAN/blob/7552a7791caad982045a7bbe5634bbf1cd5c8679/inference_gfpgan.py#L173)
- [scripts/convert_gfpganv_to_clean.py:138](https://github.com/TencentARC/GFPGAN/blob/7552a7791caad982045a7bbe5634bbf1cd5c8679/scripts/convert_gfpganv_to_clean.py#L138)
- [setup.py:82](https://github.com/TencentARC/GFPGAN/blob/7552a7791caad982045a7bbe5634bbf1cd5c8679/setup.py#L82)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: get_git_hash, get_hash, get_requirements, get_version, readme, write_version_py. |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). Observed top-level classes: Predictor. Observed top-level functions: clean_folder. |
| Data layer | data | Observed | Groups 4 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: FFHQDegradationDataset, GFPGANModel. |
| Application entry point | entrypoint | Observed | Groups 3 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: main, modify_checkpoint. |
| gfpgan package | library | Observed | Groups 10 file(s) under gfpgan package (observed from repository paths and static analysis). Observed top-level classes: BasicBlock, Bottleneck, ConstantInput, ConvLayer, ConvUpLayer, Downsample. Observed top-level func… |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 9 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: test_basicblock, test_bottleneck, test_facialcomponentdiscriminator, test_ffhq_degradation_dataset, test_g… |

## Important files

- `.github/workflows/publish-pip.yml` (ci)
- `.github/workflows/pylint.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `.vscode/settings.json` (config)
- `MANIFEST.in` (manifest)
- `cog.yaml` (config)
- `options/train_gfpgan_v1.yml` (config)
- `options/train_gfpgan_v1_simple.yml` (config)
- `requirements.txt` (manifest)
- `setup.cfg` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `(root files)` — 17 analysed file(s)
- `gfpgan` — 16 analysed file(s)
- `tests` — 9 analysed file(s)
- `.github` — 3 analysed file(s)
- `options` — 2 analysed file(s)
- `scripts` — 2 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `experiments` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `7552a7791caad982045a7bbe5634bbf1cd5c8679` is the revision these paths and observations refer to.
