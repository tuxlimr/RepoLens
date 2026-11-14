# Project structure: NVlabs/stylegan

**Analysed commit:** `1e0d5c781384ef12b50ef20a62fee5d78b38e88f`

**Commit reference:** [1e0d5c781384ef12b50ef20a62fee5d78b38e88f](https://github.com/NVlabs/stylegan/commit/1e0d5c781384ef12b50ef20a62fee5d78b38e88f)

**Tree at this commit:** [NVlabs/stylegan@1e0d5c781384](https://github.com/NVlabs/stylegan/tree/1e0d5c781384ef12b50ef20a62fee5d78b38e88f)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | NVlabs/stylegan |
| Description | StyleGAN - Official TensorFlow Implementation |
| Stars | 14411 |
| Forks | 3123 |
| Licence | Other |
| Language | Python |
| Default branch | master |
| Analysed commit | `1e0d5c781384ef12b50ef20a62fee5d78b38e88f` |
| Retrieved at | 2026-11-14T19:09:26.891881+00:00 |
| Files in this snapshot | 31 |

## Directory tree

```text
dnnlib/  (11 files)
  submission/  (4 files)
    _internal/  (1 files)
      … 1 files under this directory
    __init__.py
    run_context.py
    submit.py
  tflib/  (5 files)
    __init__.py
    autosummary.py
    network.py
    optimizer.py
    tfutil.py
  __init__.py
  util.py
metrics/  (5 files)
  __init__.py
  frechet_inception_distance.py
  linear_separability.py
  metric_base.py
  perceptual_path_length.py
training/  (7 files)
  __init__.py
  dataset.py
  loss.py
  misc.py
  networks_progan.py
  networks_stylegan.py
  training_loop.py
LICENSE.txt
README.md
config.py
dataset_tool.py
generate_figures.py
pretrained_example.py
run_metrics.py
train.py
```

## Entry points

- [dataset_tool.py:642](https://github.com/NVlabs/stylegan/blob/1e0d5c781384ef12b50ef20a62fee5d78b38e88f/dataset_tool.py#L642)
- [generate_figures.py:158](https://github.com/NVlabs/stylegan/blob/1e0d5c781384ef12b50ef20a62fee5d78b38e88f/generate_figures.py#L158)
- [pretrained_example.py:46](https://github.com/NVlabs/stylegan/blob/1e0d5c781384ef12b50ef20a62fee5d78b38e88f/pretrained_example.py#L46)
- [run_metrics.py:102](https://github.com/NVlabs/stylegan/blob/1e0d5c781384ef12b50ef20a62fee5d78b38e88f/run_metrics.py#L102)
- [train.py:189](https://github.com/NVlabs/stylegan/blob/1e0d5c781384ef12b50ef20a62fee5d78b38e88f/train.py#L189)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| dnnlib package | library | Observed | Groups 10 file(s) under dnnlib package (observed from repository paths and static analysis). Observed top-level classes: EasyDict, Logger, Optimizer, PathType, SubmitConfig, SubmitTarget. Observed top-level functions: _… |
| Application entry point | entrypoint | Observed | Groups 6 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: ExceptionInfo, TFRecordExporter, ThreadPool, WorkerThread. Observed top-level functions: c… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| metrics package | library | Observed | Groups 5 file(s) under metrics package (observed from repository paths and static analysis). Observed top-level classes: DummyMetric, FID, LS, MetricBase, MetricGroup, PPL. Observed top-level functions: conditional_entr… |
| training package | library | Observed | Groups 7 file(s) under training package (observed from repository paths and static analysis). Observed top-level classes: SyntheticDataset, TFRecordDataset. Observed top-level functions: D_hinge, D_hinge_gp, D_logistic,… |

## Important files

No manifest, config, CI, or container files were observed in the analysed set.

## Top-level layout

- `dnnlib` — 11 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `training` — 7 analysed file(s)
- `metrics` — 5 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- File dnnlib/__init__.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File dnnlib/submission/__init__.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File dnnlib/submission/_internal/run.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File dnnlib/submission/run_context.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File dnnlib/tflib/__init__.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File dnnlib/tflib/autosummary.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File dnnlib/tflib/network.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File dnnlib/tflib/tfutil.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File training/networks_stylegan.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `1e0d5c781384ef12b50ef20a62fee5d78b38e88f` is the revision these paths and observations refer to.
