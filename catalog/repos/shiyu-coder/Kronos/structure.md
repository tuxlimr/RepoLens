# Project structure: shiyu-coder/Kronos

**Analysed commit:** `67b630e67f6a18c9e9be918d9b4337c960db1e9a`

**Commit reference:** [67b630e67f6a18c9e9be918d9b4337c960db1e9a](https://github.com/shiyu-coder/Kronos/commit/67b630e67f6a18c9e9be918d9b4337c960db1e9a)

**Tree at this commit:** [shiyu-coder/Kronos@67b630e67f6a](https://github.com/shiyu-coder/Kronos/tree/67b630e67f6a18c9e9be918d9b4337c960db1e9a)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | shiyu-coder/Kronos |
| Description | Kronos: A Foundation Model for the Language of Financial Markets |
| Stars | 47794 |
| Forks | 7907 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `67b630e67f6a18c9e9be918d9b4337c960db1e9a` |
| Retrieved at | 2026-11-14T19:06:34.718262+00:00 |
| Files in this snapshot | 78 |

## Directory tree

```text
examples/  (16 files)
  yuce/  (6 files)
    000021_comprehensive_analysis_report.json
    002354_comprehensive_analysis_report.json
    300207_comprehensive_analysis_report.json
    600580_comprehensive_analysis_report.json
    historical_backtest.py
    market_analysis_report.json
  get_akshare_date_2024-2025_x.py
  get_date_new.py
  prediction_akshare_2024-2025.py
  prediction_batch_example.py
  prediction_cn_markets_day.py
  prediction_example.py
  prediction_new.py
  prediction_new_GUI.py
  prediction_wo_vol_example.py
  run_backtest_kronos.py
finetune/  (8 files)
  utils/  (2 files)
    __init__.py
    training_utils.py
  config.py
  dataset.py
  qlib_data_preprocess.py
  qlib_test.py
  train_predictor.py
  train_tokenizer.py
finetune_csv/  (7 files)
  configs/  (1 files)
    config_ali09988_candle-5min.yaml
  README.md
  README_CN.md
  config_loader.py
  finetune_base_model.py
  finetune_tokenizer.py
  train_sequential.py
model/  (3 files)
  __init__.py
  kronos.py
  module.py
tests/  (5 files)
  data/  (4 files)
    generate_regression_output.py
    regression_input.csv
    regression_output_256.csv
    regression_output_512.csv
  test_kronos_regression.py
webui/  (35 files)
  prediction_results/  (29 files)
    prediction_20250826_163800.json
    prediction_20250826_164030.json
    prediction_20250826_164422.json
    prediction_20250826_170831.json
    prediction_20250826_171720.json
    prediction_20250826_171913.json
    prediction_20250826_172031.json
    prediction_20250826_172153.json
    prediction_20250826_172740.json
    prediction_20250826_173322.json
    prediction_20250826_173455.json
    prediction_20250826_174410.json
    prediction_20250826_174809.json
    prediction_20250826_175057.json
    prediction_20250826_175135.json
    prediction_20250826_175909.json
    prediction_20250826_180308.json
    prediction_20250826_180632.json
    prediction_20250826_180745.json
    prediction_20250826_180806.json
    prediction_20250826_181012.json
    prediction_20250826_181139.json
    prediction_20250826_181240.json
    prediction_20250826_181434.json
    … 5 more files
  templates/  (1 files)
    index.html
  README.md
  app.py
  requirements.txt
  run.py
  start.sh
.gitignore
LICENSE
README.md
requirements.txt
```

## Entry points

- [finetune/dataset.py:126](https://github.com/shiyu-coder/Kronos/blob/67b630e67f6a18c9e9be918d9b4337c960db1e9a/finetune/dataset.py#L126)
- [finetune/qlib_data_preprocess.py:124](https://github.com/shiyu-coder/Kronos/blob/67b630e67f6a18c9e9be918d9b4337c960db1e9a/finetune/qlib_data_preprocess.py#L124)
- [finetune/qlib_test.py:359](https://github.com/shiyu-coder/Kronos/blob/67b630e67f6a18c9e9be918d9b4337c960db1e9a/finetune/qlib_test.py#L359)
- [finetune/train_predictor.py:238](https://github.com/shiyu-coder/Kronos/blob/67b630e67f6a18c9e9be918d9b4337c960db1e9a/finetune/train_predictor.py#L238)
- [finetune/train_tokenizer.py:275](https://github.com/shiyu-coder/Kronos/blob/67b630e67f6a18c9e9be918d9b4337c960db1e9a/finetune/train_tokenizer.py#L275)
- [finetune_csv/finetune_base_model.py:467](https://github.com/shiyu-coder/Kronos/blob/67b630e67f6a18c9e9be918d9b4337c960db1e9a/finetune_csv/finetune_base_model.py#L467)
- [finetune_csv/finetune_tokenizer.py:357](https://github.com/shiyu-coder/Kronos/blob/67b630e67f6a18c9e9be918d9b4337c960db1e9a/finetune_csv/finetune_tokenizer.py#L357)
- [finetune_csv/train_sequential.py:360](https://github.com/shiyu-coder/Kronos/blob/67b630e67f6a18c9e9be918d9b4337c960db1e9a/finetune_csv/train_sequential.py#L360)
- [webui/app.py:24](https://github.com/shiyu-coder/Kronos/blob/67b630e67f6a18c9e9be918d9b4337c960db1e9a/webui/app.py#L24)
- [webui/run.py:88](https://github.com/shiyu-coder/Kronos/blob/67b630e67f6a18c9e9be918d9b4337c960db1e9a/webui/run.py#L88)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 33 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: Config. |
| Application entry point | entrypoint | Observed | Groups 9 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Flask. Observed routes: ROUTE /, ROUTE /api/data-files, ROUTE /api/load-data,… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| finetune package | library | Observed | Groups 2 file(s) under finetune package (observed from repository paths and static analysis). Observed top-level functions: cleanup_ddp, format_time, get_model_size, reduce_tensor, set_seed, setup_ddp. |
| finetune_csv package | library | Observed | Groups 1 file(s) under finetune_csv package (observed from repository paths and static analysis). Observed top-level classes: ConfigLoader, CustomFinetuneConfig. |
| model package | library | Observed | Groups 3 file(s) under model package (observed from repository paths and static analysis). Observed top-level classes: BSQuantizer, BinarySphericalQuantizer, DependencyAwareLayer, DifferentiableEntropyFunction, DualHead… |
| Tests | test | Observed | Groups 6 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: QlibBacktest, QlibTestDataset. Observed top-level functions: collate_fn_for_inference, generate_output, gene… |
| webui package | library | Observed | Groups 1 file(s) under webui package (observed from repository paths and static analysis). |

## Important files

- `examples/yuce/000021_comprehensive_analysis_report.json` (config)
- `examples/yuce/002354_comprehensive_analysis_report.json` (config)
- `examples/yuce/300207_comprehensive_analysis_report.json` (config)
- `examples/yuce/600580_comprehensive_analysis_report.json` (config)
- `examples/yuce/market_analysis_report.json` (config)
- `finetune_csv/configs/config_ali09988_candle-5min.yaml` (config)
- `requirements.txt` (manifest)
- `webui/prediction_results/prediction_20250826_163800.json` (config)
- `webui/prediction_results/prediction_20250826_164030.json` (config)
- `webui/prediction_results/prediction_20250826_164422.json` (config)
- `webui/prediction_results/prediction_20250826_170831.json` (config)
- `webui/prediction_results/prediction_20250826_171720.json` (config)
- `webui/prediction_results/prediction_20250826_171913.json` (config)
- `webui/prediction_results/prediction_20250826_172031.json` (config)
- `webui/prediction_results/prediction_20250826_172153.json` (config)
- `webui/prediction_results/prediction_20250826_172740.json` (config)
- `webui/prediction_results/prediction_20250826_173322.json` (config)
- `webui/prediction_results/prediction_20250826_173455.json` (config)
- `webui/prediction_results/prediction_20250826_174410.json` (config)
- `webui/prediction_results/prediction_20250826_174809.json` (config)
- `webui/prediction_results/prediction_20250826_175057.json` (config)
- `webui/prediction_results/prediction_20250826_175135.json` (config)
- `webui/prediction_results/prediction_20250826_175909.json` (config)
- `webui/prediction_results/prediction_20250826_180308.json` (config)
- `webui/prediction_results/prediction_20250826_180632.json` (config)
- `webui/prediction_results/prediction_20250826_180745.json` (config)
- `webui/prediction_results/prediction_20250826_180806.json` (config)
- `webui/prediction_results/prediction_20250826_181012.json` (config)
- `webui/prediction_results/prediction_20250826_181139.json` (config)
- `webui/prediction_results/prediction_20250826_181240.json` (config)
- `webui/prediction_results/prediction_20250826_181434.json` (config)
- `webui/prediction_results/prediction_20250826_181513.json` (config)
- `webui/prediction_results/prediction_20250826_181612.json` (config)
- `webui/prediction_results/prediction_20250826_181648.json` (config)
- `webui/prediction_results/prediction_20250826_181800.json` (config)
- `webui/prediction_results/prediction_20250826_181932.json` (config)
- `webui/requirements.txt` (manifest)

## Top-level layout

- `webui` — 35 analysed file(s)
- `examples` — 16 analysed file(s)
- `finetune` — 8 analysed file(s)
- `finetune_csv` — 7 analysed file(s)
- `tests` — 5 analysed file(s)
- `(root files)` — 4 analysed file(s)
- `model` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `67b630e67f6a18c9e9be918d9b4337c960db1e9a` is the revision these paths and observations refer to.
