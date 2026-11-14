# Project structure: junyanz/pytorch-CycleGAN-and-pix2pix

**Analysed commit:** `2a7afba2895d52556dd5dfe07e8555ef657ced6f`

**Commit reference:** [2a7afba2895d52556dd5dfe07e8555ef657ced6f](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix/commit/2a7afba2895d52556dd5dfe07e8555ef657ced6f)

**Tree at this commit:** [junyanz/pytorch-CycleGAN-and-pix2pix@2a7afba2895d](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix/tree/2a7afba2895d52556dd5dfe07e8555ef657ced6f)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | junyanz/pytorch-CycleGAN-and-pix2pix |
| Description | Image-to-Image Translation in PyTorch |
| Stars | 25278 |
| Forks | 6554 |
| Licence | Other |
| Language | Python |
| Default branch | master |
| Analysed commit | `2a7afba2895d52556dd5dfe07e8555ef657ced6f` |
| Retrieved at | 2026-11-14T19:07:32.442861+00:00 |
| Files in this snapshot | 71 |

## Directory tree

```text
data/  (8 files)
  __init__.py
  aligned_dataset.py
  base_dataset.py
  colorization_dataset.py
  image_folder.py
  single_dataset.py
  template_dataset.py
  unaligned_dataset.py
datasets/  (10 files)
  bibtex/  (5 files)
    cityscapes.tex
    facades.tex
    handbags.tex
    shoes.tex
    transattr.tex
  combine_A_and_B.py
  download_cyclegan_dataset.sh
  download_pix2pix_dataset.sh
  make_dataset_aligned.py
  prepare_cityscapes_dataset.py
docs/  (7 files)
  Dockerfile
  README_es.md
  datasets.md
  docker.md
  overview.md
  qa.md
  tips.md
models/  (8 files)
  __init__.py
  base_model.py
  colorization_model.py
  cycle_gan_model.py
  networks.py
  pix2pix_model.py
  template_model.py
  test_model.py
options/  (4 files)
  __init__.py
  base_options.py
  test_options.py
  train_options.py
scripts/  (19 files)
  edges/  (2 files)
    PostprocessHED.m
    batch_hed.py
  eval_cityscapes/  (5 files)
    caffemodel/  (1 files)
      … 1 files under this directory
    cityscapes.py
    download_fcn8s.sh
    evaluate.py
    util.py
  conda_deps.sh
  download_cyclegan_model.sh
  download_pix2pix_model.sh
  install_deps.sh
  test_before_push.py
  test_colorization.sh
  test_cyclegan.sh
  test_pix2pix.sh
  test_single.sh
  train_colorization.sh
  train_cyclegan.sh
  train_pix2pix.sh
util/  (6 files)
  __init__.py
  get_data.py
  html.py
  image_pool.py
  util.py
  visualizer.py
.gitignore
.replit
CycleGAN.ipynb
LICENSE
README.md
environment.yml
pix2pix.ipynb
test.py
train.py
```

## Entry points

- [datasets/make_dataset_aligned.py:35](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix/blob/2a7afba2895d52556dd5dfe07e8555ef657ced6f/datasets/make_dataset_aligned.py#L35)
- [datasets/prepare_cityscapes_dataset.py:77](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix/blob/2a7afba2895d52556dd5dfe07e8555ef657ced6f/datasets/prepare_cityscapes_dataset.py#L77)
- [test.py:45](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix/blob/2a7afba2895d52556dd5dfe07e8555ef657ced6f/test.py#L45)
- [train.py:30](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix/blob/2a7afba2895d52556dd5dfe07e8555ef657ced6f/train.py#L30)
- [util/html.py:74](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix/blob/2a7afba2895d52556dd5dfe07e8555ef657ced6f/util/html.py#L74)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 15 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AlignedDataset, BaseDataset, BaseModel, ColorizationDataset, ColorizationModel, CustomDatasetDataLoade… |
| datasets package | library | Observed | Groups 3 file(s) under datasets package (observed from repository paths and static analysis). Observed top-level functions: image_write. |
| Application entry point | entrypoint | Observed | Groups 5 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: HTML. Observed top-level functions: align_images, check_matching_pair, get_file_paths, loa… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| options package | library | Observed | Groups 3 file(s) under options package (observed from repository paths and static analysis). Observed top-level classes: BaseOptions, TrainOptions. |
| scripts package | library | Observed | Groups 12 file(s) under scripts package (observed from repository paths and static analysis). Observed top-level classes: cityscapes. Observed top-level functions: fast_hist, feed_net, get_out_scoremap, get_scores, main… |
| Tests | test | Observed | Groups 7 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: TestBeforePush, TestModel, TestOptions. |
| util package | library | Observed | Groups 5 file(s) under util package (observed from repository paths and static analysis). Observed top-level classes: GetData, ImagePool, Visualizer. Observed top-level functions: cleanup_ddp, diagnose_network, init_ddp… |

## Important files

- `docs/Dockerfile` (container)
- `environment.yml` (manifest)

## Top-level layout

- `scripts` — 19 analysed file(s)
- `datasets` — 10 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `data` — 8 analysed file(s)
- `models` — 8 analysed file(s)
- `docs` — 7 analysed file(s)
- `util` — 6 analysed file(s)
- `options` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `2a7afba2895d52556dd5dfe07e8555ef657ced6f` is the revision these paths and observations refer to.
