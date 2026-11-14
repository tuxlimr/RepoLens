# Project structure: milesial/Pytorch-UNet

**Analysed commit:** `21d7850f2af30a9695bbeea75f3136aa538cfc4a`

**Commit reference:** [21d7850f2af30a9695bbeea75f3136aa538cfc4a](https://github.com/milesial/Pytorch-UNet/commit/21d7850f2af30a9695bbeea75f3136aa538cfc4a)

**Tree at this commit:** [milesial/Pytorch-UNet@21d7850f2af3](https://github.com/milesial/Pytorch-UNet/tree/21d7850f2af30a9695bbeea75f3136aa538cfc4a)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | milesial/Pytorch-UNet |
| Description | PyTorch implementation of the U-Net for image semantic segmentation with high quality images |
| Stars | 11764 |
| Forks | 2770 |
| Licence | GPL-3.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `21d7850f2af30a9695bbeea75f3136aa538cfc4a` |
| Retrieved at | 2026-11-14T19:10:25.262129+00:00 |
| Files in this snapshot | 21 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    main.yml
data/  (2 files)
  imgs/  (1 files)
    .keep
  masks/  (1 files)
    .keep
scripts/  (2 files)
  download_data.bat
  download_data.sh
unet/  (3 files)
  __init__.py
  unet_model.py
  unet_parts.py
utils/  (4 files)
  __init__.py
  data_loading.py
  dice_score.py
  utils.py
.gitignore
Dockerfile
LICENSE
README.md
evaluate.py
hubconf.py
predict.py
requirements.txt
train.py
```

## Entry points

- [predict.py:79](https://github.com/milesial/Pytorch-UNet/blob/21d7850f2af30a9695bbeea75f3136aa538cfc4a/predict.py#L79)
- [train.py:187](https://github.com/milesial/Pytorch-UNet/blob/21d7850f2af30a9695bbeea75f3136aa538cfc4a/train.py#L187)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). Observed top-level functions: evaluate, unet_carvana. |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: get_args, get_output_filenames, mask_to_image, predict_img, train_model. |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| unet package | library | Observed | Groups 3 file(s) under unet package (observed from repository paths and static analysis). Observed top-level classes: DoubleConv, Down, OutConv, UNet, Up. |
| utils package | library | Observed | Groups 4 file(s) under utils package (observed from repository paths and static analysis). Observed top-level classes: BasicDataset, CarvanaDataset. Observed top-level functions: dice_coeff, dice_loss, load_image, multi… |

## Important files

- `.github/workflows/main.yml` (ci)
- `Dockerfile` (container)
- `requirements.txt` (manifest)

## Top-level layout

- `(root files)` — 9 analysed file(s)
- `utils` — 4 analysed file(s)
- `unet` — 3 analysed file(s)
- `data` — 2 analysed file(s)
- `scripts` — 2 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `21d7850f2af30a9695bbeea75f3136aa538cfc4a` is the revision these paths and observations refer to.
