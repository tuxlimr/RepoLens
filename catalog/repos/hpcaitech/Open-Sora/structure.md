# Project structure: hpcaitech/Open-Sora

**Analysed commit:** `7ad6a96a135feb81f755c84fb391818718f6beb2`

**Commit reference:** [7ad6a96a135feb81f755c84fb391818718f6beb2](https://github.com/hpcaitech/Open-Sora/commit/7ad6a96a135feb81f755c84fb391818718f6beb2)

**Tree at this commit:** [hpcaitech/Open-Sora@7ad6a96a135f](https://github.com/hpcaitech/Open-Sora/tree/7ad6a96a135feb81f755c84fb391818718f6beb2)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | hpcaitech/Open-Sora |
| Description | Open-Sora: Democratizing Efficient Video Production for All |
| Stars | 29935 |
| Forks | 3096 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `7ad6a96a135feb81f755c84fb391818718f6beb2` |
| Retrieved at | 2026-11-14T19:07:10.700983+00:00 |
| Files in this snapshot | 118 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (2 files)
    close_issue.yaml
    github_page.yaml
assets/  (3 files)
  texts/  (3 files)
    example.csv
    i2v.csv
    sora.csv
configs/  (20 files)
  diffusion/  (16 files)
    inference/  (9 files)
      … 9 files under this directory
    train/  (7 files)
      … 7 files under this directory
  vae/  (4 files)
    inference/  (2 files)
      … 2 files under this directory
    train/  (2 files)
      … 2 files under this directory
docs/  (11 files)
  zh_CN/  (4 files)
    report_v1.md
    report_v2.md
    report_v3.md
    report_v4.md
  ae.md
  hcae.md
  report_01.md
  report_02.md
  report_03.md
  report_04.md
  train.md
gradio/  (1 files)
  app.py
opensora/  (67 files)
  acceleration/  (9 files)
    shardformer/  (5 files)
      … 5 files under this directory
    __init__.py
    checkpoint.py
    communications.py
    parallel_states.py
  datasets/  (11 files)
    __init__.py
    aspect.py
    bucket.py
    dataloader.py
    datasets.py
    parallel.py
    pin_memory_cache.py
    read_video.py
    sampler.py
    utils.py
    video_transforms.py
  models/  (34 files)
    dc_ae/  (12 files)
      … 12 files under this directory
    hunyuan_vae/  (6 files)
      … 6 files under this directory
    mmdit/  (6 files)
      … 6 files under this directory
    text/  (2 files)
      … 2 files under this directory
    vae/  (7 files)
      … 7 files under this directory
    __init__.py
  utils/  (11 files)
    __init__.py
    cai.py
    ckpt.py
    config.py
    inference.py
    logger.py
    misc.py
    optimizer.py
    prompt_refine.py
    sampling.py
    train.py
  __init__.py
  registry.py
scripts/  (7 files)
  cnv/  (2 files)
    meta.py
    shard.py
  diffusion/  (2 files)
    inference.py
    train.py
  vae/  (3 files)
    inference.py
    stats.py
    train.py
.gitignore
.pre-commit-config.yaml
CONTRIBUTING.md
LICENSE
README.md
requirements.txt
setup.py
```

## Entry points

- [gradio/app.py:757](https://github.com/hpcaitech/Open-Sora/blob/7ad6a96a135feb81f755c84fb391818718f6beb2/gradio/app.py#L757)
- [opensora/datasets/dataloader.py:364](https://github.com/hpcaitech/Open-Sora/blob/7ad6a96a135feb81f755c84fb391818718f6beb2/opensora/datasets/dataloader.py#L364)
- [opensora/datasets/video_transforms.py:543](https://github.com/hpcaitech/Open-Sora/blob/7ad6a96a135feb81f755c84fb391818718f6beb2/opensora/datasets/video_transforms.py#L543)
- [opensora/models/dc_ae/models/nn/vo_ops.py:243](https://github.com/hpcaitech/Open-Sora/blob/7ad6a96a135feb81f755c84fb391818718f6beb2/opensora/models/dc_ae/models/nn/vo_ops.py#L243)
- [scripts/cnv/meta.py:69](https://github.com/hpcaitech/Open-Sora/blob/7ad6a96a135feb81f755c84fb391818718f6beb2/scripts/cnv/meta.py#L69)
- [scripts/cnv/shard.py:63](https://github.com/hpcaitech/Open-Sora/blob/7ad6a96a135feb81f755c84fb391818718f6beb2/scripts/cnv/shard.py#L63)
- [scripts/diffusion/inference.py:244](https://github.com/hpcaitech/Open-Sora/blob/7ad6a96a135feb81f755c84fb391818718f6beb2/scripts/diffusion/inference.py#L244)
- [scripts/diffusion/train.py:653](https://github.com/hpcaitech/Open-Sora/blob/7ad6a96a135feb81f755c84fb391818718f6beb2/scripts/diffusion/train.py#L653)
- [scripts/vae/inference.py:141](https://github.com/hpcaitech/Open-Sora/blob/7ad6a96a135feb81f755c84fb391818718f6beb2/scripts/vae/inference.py#L141)
- [scripts/vae/stats.py:117](https://github.com/hpcaitech/Open-Sora/blob/7ad6a96a135feb81f755c84fb391818718f6beb2/scripts/vae/stats.py#L117)
- [scripts/vae/train.py:596](https://github.com/hpcaitech/Open-Sora/blob/7ad6a96a135feb81f755c84fb391818718f6beb2/scripts/vae/train.py#L596)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 23 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: auto_convert, config_to_name, create_experiment_workspace, fetch_readme, fetch_req… |
| Data layer | data | Observed | Groups 33 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AttnBlock, AutoEncoder, AutoEncoder3DConfig, AutoEncoderConfig, AutoencoderKLCausal3D, CausalConv3d. O… |
| Application entry point | entrypoint | Observed | Groups 11 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: CenterCropResizeVideo, CenterCropVideo, DataloaderForVideo, KineticsRandomCropResizeVideo… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| opensora package | library | Observed | Groups 30 file(s) under opensora package (observed from repository paths and static analysis). Observed top-level classes: ActivationManager, BatchDistributedSampler, Bucket, CachedVideoTextDataset, CheckpointFunctionWi… |

## Important files

- `.github/workflows/close_issue.yaml` (ci)
- `.github/workflows/github_page.yaml` (ci)
- `.pre-commit-config.yaml` (config)
- `requirements.txt` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `opensora` — 67 analysed file(s)
- `configs` — 20 analysed file(s)
- `docs` — 11 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `scripts` — 7 analysed file(s)
- `assets` — 3 analysed file(s)
- `.github` — 2 analysed file(s)
- `gradio` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `7ad6a96a135feb81f755c84fb391818718f6beb2` is the revision these paths and observations refer to.
