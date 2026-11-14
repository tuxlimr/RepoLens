# Project structure: Rudrabha/Wav2Lip

**Analysed commit:** `bac9a81e63ecc153202353372e5724b83d9e6322`

**Commit reference:** [bac9a81e63ecc153202353372e5724b83d9e6322](https://github.com/Rudrabha/Wav2Lip/commit/bac9a81e63ecc153202353372e5724b83d9e6322)

**Tree at this commit:** [Rudrabha/Wav2Lip@bac9a81e63ec](https://github.com/Rudrabha/Wav2Lip/tree/bac9a81e63ecc153202353372e5724b83d9e6322)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Rudrabha/Wav2Lip |
| Description | This repository contains the codes of "A Lip Sync Expert Is All You Need for Speech to Lip Generation In the Wild", published at ACM Multimedia 2020. For HD commercial model, please try out Sync Labs  |
| Stars | 13276 |
| Forks | 2842 |
| Licence | Not detected |
| Language | Python |
| Default branch | master |
| Analysed commit | `bac9a81e63ecc153202353372e5724b83d9e6322` |
| Retrieved at | 2026-11-14T19:09:52.836550+00:00 |
| Files in this snapshot | 40 |

## Directory tree

```text
checkpoints/  (1 files)
  README.md
evaluation/  (10 files)
  scores_LSE/  (4 files)
    SyncNetInstance_calc_scores.py
    calculate_scores_LRS.py
    calculate_scores_real_videos.py
    calculate_scores_real_videos.sh
  test_filelists/  (3 files)
    ReSyncED/  (2 files)
      … 2 files under this directory
    README.md
  README.md
  gen_videos_from_filelist.py
  real_videos_inference.py
face_detection/  (12 files)
  detection/  (7 files)
    sfd/  (5 files)
      … 5 files under this directory
    __init__.py
    core.py
  README.md
  __init__.py
  api.py
  models.py
  utils.py
filelists/  (1 files)
  README.md
models/  (4 files)
  __init__.py
  conv.py
  syncnet.py
  wav2lip.py
results/  (1 files)
  README.md
temp/  (1 files)
  README.md
.gitignore
README.md
audio.py
color_syncnet_train.py
hparams.py
hq_wav2lip_train.py
inference.py
preprocess.py
requirements.txt
wav2lip_train.py
```

## Entry points

- [color_syncnet_train.py:246](https://github.com/Rudrabha/Wav2Lip/blob/bac9a81e63ecc153202353372e5724b83d9e6322/color_syncnet_train.py#L246)
- [evaluation/gen_videos_from_filelist.py:237](https://github.com/Rudrabha/Wav2Lip/blob/bac9a81e63ecc153202353372e5724b83d9e6322/evaluation/gen_videos_from_filelist.py#L237)
- [evaluation/real_videos_inference.py:304](https://github.com/Rudrabha/Wav2Lip/blob/bac9a81e63ecc153202353372e5724b83d9e6322/evaluation/real_videos_inference.py#L304)
- [hq_wav2lip_train.py:397](https://github.com/Rudrabha/Wav2Lip/blob/bac9a81e63ecc153202353372e5724b83d9e6322/hq_wav2lip_train.py#L397)
- [inference.py:279](https://github.com/Rudrabha/Wav2Lip/blob/bac9a81e63ecc153202353372e5724b83d9e6322/inference.py#L279)
- [preprocess.py:112](https://github.com/Rudrabha/Wav2Lip/blob/bac9a81e63ecc153202353372e5724b83d9e6322/preprocess.py#L112)
- [wav2lip_train.py:338](https://github.com/Rudrabha/Wav2Lip/blob/bac9a81e63ecc153202353372e5724b83d9e6322/wav2lip_train.py#L338)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). Observed top-level classes: HParams. Observed top-level functions: _amp_to_db, _build_mel_basis, _db_to_amp, _denormalize, _linea… |
| Data layer | data | Observed | Groups 5 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: Bottleneck, Conv2d, Conv2dTranspose, ConvBlock, FAN, HourGlass. Observed top-level functions: conv3x3. |
| Application entry point | entrypoint | Observed | Groups 7 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Dataset. Observed top-level functions: _load, cosine_loss, datagen, eval_model, face_detec… |
| evaluation package | library | Observed | Groups 4 file(s) under evaluation package (observed from repository paths and static analysis). Observed top-level classes: SyncNetInstance. Observed top-level functions: calc_pdist. |
| face_detection package | library | Observed | Groups 10 file(s) under face_detection package (observed from repository paths and static analysis). Observed top-level classes: FaceAlignment, FaceDetector, L2Norm, LandmarksType, NetworkSize, SFDDetector. Observed top… |

## Important files

- `requirements.txt` (manifest)

## Top-level layout

- `face_detection` — 12 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `evaluation` — 10 analysed file(s)
- `models` — 4 analysed file(s)
- `checkpoints` — 1 analysed file(s)
- `filelists` — 1 analysed file(s)
- `results` — 1 analysed file(s)
- `temp` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `bac9a81e63ecc153202353372e5724b83d9e6322` is the revision these paths and observations refer to.
