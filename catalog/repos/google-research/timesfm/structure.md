# Project structure: google-research/timesfm

**Analysed commit:** `918df02c9d366b2145bc5876135fa2131d3ed2a6`

**Commit reference:** [918df02c9d366b2145bc5876135fa2131d3ed2a6](https://github.com/google-research/timesfm/commit/918df02c9d366b2145bc5876135fa2131d3ed2a6)

**Tree at this commit:** [google-research/timesfm@918df02c9d36](https://github.com/google-research/timesfm/tree/918df02c9d366b2145bc5876135fa2131d3ed2a6)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | google-research/timesfm |
| Description | TimesFM (Time Series Foundation Model) is a pretrained time-series foundation model developed by Google Research for time-series forecasting. |
| Stars | 35493 |
| Forks | 3476 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `918df02c9d366b2145bc5876135fa2131d3ed2a6` |
| Retrieved at | 2026-11-14T19:06:56.420025+00:00 |
| Files in this snapshot | 164 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (2 files)
    main.yml
    manual_publish.yml
src/  (58 files)
  timesfm/  (17 files)
    flax/  (5 files)
      … 5 files under this directory
    timesfm_2p5/  (3 files)
      … 3 files under this directory
    torch/  (5 files)
      … 5 files under this directory
    utils/  (1 files)
      … 1 files under this directory
    __init__.py
    configs.py
    py.typed
  timesfm3/  (41 files)
    mlx/  (12 files)
      … 12 files under this directory
    torch/  (17 files)
      … 17 files under this directory
    __init__.py
    backward_compat_test.py
    configs.py
    cpm_revin_refine.py
    dense.py
    evaluator.py
    model.py
    normalization.py
    timesfm3_forecaster.py
    transformations.py
    transformer.py
    util.py
tests/  (21 files)
  __init__.py
  test_base_utils.py
  test_configs.py
  test_cpm_anchor_selection.py
  test_csv_time_grid.py
  test_force_flip_invariance.py
  test_forecast_inputs.py
  test_forecast_with_covariates.py
  test_forecaster_batch_horizon.py
  test_forecaster_output_ranks.py
  test_forecaster_query_validation.py
  test_input_normalization.py
  test_model_loading.py
  test_optional_backend_errors.py
  test_output_patch_gather.py
  test_running_stats_allocation.py
  test_stitch_output.py
  test_timesfm3_optional_backend_errors.py
  test_torch_layers.py
  test_torch_utils.py
  test_xreg_lib.py
timesfm-forecasting/  (25 files)
  examples/  (19 files)
    anomaly-detection/  (2 files)
      … 2 files under this directory
    covariates-forecasting/  (3 files)
      … 3 files under this directory
    finetuning/  (2 files)
      … 2 files under this directory
    global-temperature/  (12 files)
      … 12 files under this directory
  references/  (3 files)
    api_reference.md
    data_preparation.md
    system_requirements.md
  scripts/  (2 files)
    check_system.py
    forecast_csv.py
  SKILL.md
timesfm3-usage/  (13 files)
  benchmarks/  (12 files)
    fev_bench/  (4 files)
      … 4 files under this directory
    gift_eval/  (4 files)
      … 4 files under this directory
    time_bench/  (3 files)
      … 3 files under this directory
    README.md
  notebooks/  (1 files)
    promotion_and_synthetic_parity_demo.ipynb
v1/  (38 files)
  docs/  (1 files)
    contributing.md
  experiments/  (8 files)
    baselines/  (2 files)
      … 2 files under this directory
    extended_benchmarks/  (4 files)
      … 4 files under this directory
    long_horizon_benchmarks/  (2 files)
      … 2 files under this directory
  notebooks/  (3 files)
    covariates.ipynb
    finetuning.ipynb
    finetuning_torch.ipynb
  peft/  (4 files)
    README.md
    finetune.py
    finetune.sh
    usage.ipynb
  src/  (16 files)
    adapter/  (4 files)
      … 4 files under this directory
    finetuning/  (3 files)
      … 3 files under this directory
    timesfm/  (9 files)
      … 9 files under this directory
  tests/  (2 files)
    test_data_loader.py
    test_timesfm.py
  LICENSE
  README.md
  TROUBLESHOOTING.md
  pyproject.toml
.gitattributes
.gitignore
AGENTS.md
LICENSE
README.md
pyproject.toml
requirements.txt
```

## Entry points

- [src/timesfm3/backward_compat_test.py:68](https://github.com/google-research/timesfm/blob/918df02c9d366b2145bc5876135fa2131d3ed2a6/src/timesfm3/backward_compat_test.py#L68)
- [src/timesfm3/mlx/model_parity_test.py:434](https://github.com/google-research/timesfm/blob/918df02c9d366b2145bc5876135fa2131d3ed2a6/src/timesfm3/mlx/model_parity_test.py#L434)
- [src/timesfm3/mlx/timesfm3_forecaster_test.py:382](https://github.com/google-research/timesfm/blob/918df02c9d366b2145bc5876135fa2131d3ed2a6/src/timesfm3/mlx/timesfm3_forecaster_test.py#L382)
- [src/timesfm3/torch/cpm_revin_refine_test.py:121](https://github.com/google-research/timesfm/blob/918df02c9d366b2145bc5876135fa2131d3ed2a6/src/timesfm3/torch/cpm_revin_refine_test.py#L121)
- [src/timesfm3/torch/evaluator_test.py:383](https://github.com/google-research/timesfm/blob/918df02c9d366b2145bc5876135fa2131d3ed2a6/src/timesfm3/torch/evaluator_test.py#L383)
- [src/timesfm3/torch/model_test.py:222](https://github.com/google-research/timesfm/blob/918df02c9d366b2145bc5876135fa2131d3ed2a6/src/timesfm3/torch/model_test.py#L222)
- [src/timesfm3/torch/primitives_test.py:436](https://github.com/google-research/timesfm/blob/918df02c9d366b2145bc5876135fa2131d3ed2a6/src/timesfm3/torch/primitives_test.py#L436)
- [src/timesfm3/torch/timesfm3_forecaster_test.py:564](https://github.com/google-research/timesfm/blob/918df02c9d366b2145bc5876135fa2131d3ed2a6/src/timesfm3/torch/timesfm3_forecaster_test.py#L564)
- [src/timesfm3/torch/transformer_test.py:291](https://github.com/google-research/timesfm/blob/918df02c9d366b2145bc5876135fa2131d3ed2a6/src/timesfm3/torch/transformer_test.py#L291)
- [v1/src/finetuning/finetuning_example.py:402](https://github.com/google-research/timesfm/blob/918df02c9d366b2145bc5876135fa2131d3ed2a6/v1/src/finetuning/finetuning_example.py#L402)
- [timesfm-forecasting/scripts/check_system.py:752](https://github.com/google-research/timesfm/blob/918df02c9d366b2145bc5876135fa2131d3ed2a6/timesfm-forecasting/scripts/check_system.py#L752)
- [timesfm-forecasting/scripts/forecast_csv.py:272](https://github.com/google-research/timesfm/blob/918df02c9d366b2145bc5876135fa2131d3ed2a6/timesfm-forecasting/scripts/forecast_csv.py#L272)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 3 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: TimesFM3Mlx, TimesFM3Torch. |
| Application entry point | entrypoint | Observed | Groups 16 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: CheckResult, ExperimentHandler, SuppressGluonTSWarningFilter, SystemReport, TimeSeriesDat… |
| Tests | test | Observed | Groups 32 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: BackwardCompatImportTest, CpmRevinRefineTest, FakeModel, MaskTest, MixingTransformerTest, MultiHeadAttentio… |
| timesfm package | library | Observed | Groups 16 file(s) under timesfm package (observed from repository paths and static analysis). Observed top-level classes: BatchedInContextXRegBase, BatchedInContextXRegLinear, DecodeCache, ForecastConfig, LayerNorm, Mul… |
| timesfm3 package | library | Observed | Groups 29 file(s) under timesfm3 package (observed from repository paths and static analysis). Observed top-level classes: DecodeCache, ForecastOutput, MixingTransformer, MultiHeadAttention, PerDimScale, RMSNorm. Observ… |
| timesfm3-usage package | library | Observed | Groups 2 file(s) under timesfm3-usage package (observed from repository paths and static analysis). |
| timesfm-forecasting package | library | Observed | Groups 2 file(s) under timesfm-forecasting package (observed from repository paths and static analysis). |
| v1 package | library | Observed | Groups 18 file(s) under v1 package (observed from repository paths and static analysis). Observed top-level classes: BatchedInContextXRegBase, BatchedInContextXRegLinear, DistributedManager, DoraAttentionProjection, Dor… |

## Important files

- `.github/workflows/main.yml` (ci)
- `.github/workflows/manual_publish.yml` (ci)
- `pyproject.toml` (manifest)
- `requirements.txt` (manifest)
- `timesfm-forecasting/examples/anomaly-detection/output/anomaly_detection.json` (config)
- `timesfm-forecasting/examples/covariates-forecasting/output/covariates_metadata.json` (config)
- `timesfm-forecasting/examples/global-temperature/output/animation_data.json` (config)
- `timesfm-forecasting/examples/global-temperature/output/forecast_output.json` (config)
- `v1/pyproject.toml` (manifest)

## Top-level layout

- `src` — 58 analysed file(s)
- `v1` — 38 analysed file(s)
- `timesfm-forecasting` — 25 analysed file(s)
- `tests` — 21 analysed file(s)
- `timesfm3-usage` — 13 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `.github` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `918df02c9d366b2145bc5876135fa2131d3ed2a6` is the revision these paths and observations refer to.
