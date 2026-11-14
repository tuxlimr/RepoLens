# Project structure: microsoft/qlib

**Analysed commit:** `54355232463878d2eebb91fe0ee5fa7fa1f5976c`

**Commit reference:** [54355232463878d2eebb91fe0ee5fa7fa1f5976c](https://github.com/microsoft/qlib/commit/54355232463878d2eebb91fe0ee5fa7fa1f5976c)

**Tree at this commit:** [microsoft/qlib@543552324638](https://github.com/microsoft/qlib/tree/54355232463878d2eebb91fe0ee5fa7fa1f5976c)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | microsoft/qlib |
| Description | Qlib is an AI-oriented Quant investment platform that aims to use AI tech to empower Quant Research, from exploring ideas to implementing productions. Qlib supports diverse ML modeling paradigms, including supervised learning, market dynamics modeling, and RL, and is now equipped with https://githu… |
| Stars | 50283 |
| Forks | 7932 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `54355232463878d2eebb91fe0ee5fa7fa1f5976c` |
| Retrieved at | 2026-11-14T19:06:32.078070+00:00 |
| Files in this snapshot | 600 |

## Directory tree

```text
.github/  (17 files)
  ISSUE_TEMPLATE/  (4 files)
    bug-report.md
    documentation.md
    feature-request.md
    question.md
  ci/  (3 files)
    README.md
    constraints.txt
    test-requirements.txt
  workflows/  (6 files)
    lint_title.yml
    release.yml
    stale.yml
    test_qlib_from_pip.yml
    test_qlib_from_source.yml
    test_qlib_from_source_slow.yml
  PULL_REQUEST_TEMPLATE.md
  brew_install.sh
  dependabot.yml
  release-drafter.yml
docs/  (42 files)
  FAQ/  (1 files)
    FAQ.rst
  _static/  (2 files)
    img/  (1 files)
      … 1 files under this directory
    demo.sh
  advanced/  (5 files)
    PIT.rst
    alpha.rst
    serial.rst
    server.rst
    task_management.rst
  changelog/  (1 files)
    changelog.rst
  component/  (14 files)
    rl/  (5 files)
      … 5 files under this directory
    data.rst
    highfreq.rst
    meta.rst
    model.rst
    online.rst
    recorder.rst
    report.rst
    strategy.rst
    workflow.rst
  developer/  (2 files)
    code_standard_and_dev_guide.rst
    how_to_build_image.rst
  hidden/  (3 files)
    client.rst
    online.rst
    tuner.rst
  introduction/  (2 files)
    introduction.rst
    quick.rst
  reference/  (1 files)
    api.rst
  start/  (6 files)
    artifact_migration.rst
    config_migration.rst
    getdata.rst
    initialization.rst
    installation.rst
    integration.rst
  Makefile
  conf.py
  index.rst
  make.bat
  requirements.txt
examples/  (187 files)
  benchmarks/  (131 files)
    ADARNN/  (3 files)
      … 3 files under this directory
    ADD/  (3 files)
      … 3 files under this directory
    ALSTM/  (4 files)
      … 4 files under this directory
    CatBoost/  (6 files)
      … 6 files under this directory
    DoubleEnsemble/  (7 files)
      … 7 files under this directory
    GATs/  (4 files)
      … 4 files under this directory
    GRU/  (4 files)
      … 4 files under this directory
    GeneralPtNN/  (4 files)
      … 4 files under this directory
    HIST/  (4 files)
      … 4 files under this directory
    IGMTF/  (3 files)
      … 3 files under this directory
    KRNN/  (3 files)
      … 3 files under this directory
    LSTM/  (4 files)
      … 4 files under this directory
    LightGBM/  (12 files)
      … 12 files under this directory
    Linear/  (4 files)
      … 4 files under this directory
    Localformer/  (4 files)
      … 4 files under this directory
    MLP/  (6 files)
      … 6 files under this directory
    SFM/  (3 files)
      … 3 files under this directory
    Sandwich/  (3 files)
      … 3 files under this directory
    TCN/  (4 files)
      … 4 files under this directory
    TCTS/  (3 files)
      … 3 files under this directory
    TFT/  (13 files)
      … 13 files under this directory
    TRA/  (17 files)
      … 17 files under this directory
    TabNet/  (4 files)
      … 4 files under this directory
    Transformer/  (4 files)
      … 4 files under this directory
    XGBoost/  (4 files)
      … 4 files under this directory
    README.md
  benchmarks_dynamic/  (10 files)
    DDG-DA/  (5 files)
      … 5 files under this directory
    baseline/  (4 files)
      … 4 files under this directory
    README.md
  data_demo/  (3 files)
    README.md
    data_cache_demo.py
    data_mem_resuse_demo.py
  highfreq/  (6 files)
    README.md
    highfreq_handler.py
    highfreq_ops.py
    highfreq_processor.py
    workflow.py
    workflow_config_High_Freq_Tree_Alpha158.yaml
  hyperparameter/  (4 files)
    LightGBM/  (4 files)
      … 4 files under this directory
  model_interpreter/  (1 files)
    feature.py
  model_rolling/  (2 files)
    requirements.txt
    task_manager_rolling.py
  nested_decision_execution/  (2 files)
    README.md
    workflow.py
  online_srv/  (3 files)
    online_management_simulate.py
    rolling_online_management.py
    update_online_pred.py
  orderbook_data/  (3 files)
    README.md
    create_dataset.py
    example.py
  portfolio/  (3 files)
    README.md
    config_enhanced_indexing.yaml
    prepare_riskdata.py
  rl/  (1 files)
    simple_example.ipynb
  rl_order_execution/  (10 files)
    exp_configs/  (5 files)
      … 5 files under this directory
    scripts/  (4 files)
      … 4 files under this directory
    README.md
  rolling_process_data/  (3 files)
    README.md
    rolling_handler.py
    workflow.py
  tutorial/  (1 files)
    detailed_workflow.ipynb
  README.md
  run_all_model.py
  workflow_by_code.ipynb
  workflow_by_code.py
qlib/  (235 files)
  backtest/  (12 files)
    __init__.py
    account.py
    backtest.py
    decision.py
    exchange.py
    executor.py
    high_performance_ds.py
    position.py
    profit_attribution.py
    report.py
    signal.py
    utils.py
  cli/  (3 files)
    __init__.py
    data.py
    run.py
  contrib/  (102 files)
    data/  (11 files)
      … 11 files under this directory
    eva/  (2 files)
      … 2 files under this directory
    meta/  (6 files)
      … 6 files under this directory
    model/  (35 files)
      … 35 files under this directory
    online/  (6 files)
      … 6 files under this directory
    ops/  (2 files)
      … 2 files under this directory
    report/  (15 files)
      … 15 files under this directory
    rolling/  (4 files)
      … 4 files under this directory
    strategy/  (9 files)
      … 9 files under this directory
    tuner/  (6 files)
      … 6 files under this directory
    workflow/  (2 files)
      … 2 files under this directory
    __init__.py
    evaluate.py
    evaluate_portfolio.py
    torch.py
  data/  (23 files)
    _libs/  (3 files)
      … 3 files under this directory
    dataset/  (7 files)
      … 7 files under this directory
    storage/  (3 files)
      … 3 files under this directory
    __init__.py
    base.py
    cache.py
    client.py
    data.py
    expression_parser.py
    filter.py
    inst_processor.py
    ops.py
    pit.py
  model/  (18 files)
    ens/  (3 files)
      … 3 files under this directory
    interpret/  (2 files)
      … 2 files under this directory
    meta/  (4 files)
      … 4 files under this directory
    riskmodel/  (5 files)
      … 5 files under this directory
    __init__.py
    base.py
    trainer.py
    utils.py
  rl/  (38 files)
    contrib/  (5 files)
      … 5 files under this directory
    data/  (5 files)
      … 5 files under this directory
    order_execution/  (10 files)
      … 10 files under this directory
    strategy/  (2 files)
      … 2 files under this directory
    trainer/  (5 files)
      … 5 files under this directory
    utils/  (5 files)
      … 5 files under this directory
    __init__.py
    aux_info.py
    interpreter.py
    reward.py
    seed.py
    simulator.py
  strategy/  (2 files)
    __init__.py
    base.py
  tests/  (4 files)
    __init__.py
    config.py
    data.py
    test_config_validation.py
  utils/  (12 files)
    __init__.py
    data.py
    exceptions.py
    file.py
    index_data.py
    mod.py
    objm.py
    paral.py
    pickle_utils.py
    resam.py
    serial.py
    time.py
  workflow/  (16 files)
    online/  (5 files)
      … 5 files under this directory
    task/  (5 files)
      … 5 files under this directory
    __init__.py
    exp.py
    expm.py
    record_temp.py
    recorder.py
    utils.py
  __init__.py
  config.py
  constant.py
  log.py
  typehint.py
scripts/  (43 files)
  data_collector/  (36 files)
    baostock_5min/  (3 files)
      … 3 files under this directory
    br_index/  (3 files)
      … 3 files under this directory
    cn_index/  (3 files)
      … 3 files under this directory
    contrib/  (6 files)
      … 6 files under this directory
    crowd_source/  (1 files)
      … 1 files under this directory
    crypto/  (3 files)
      … 3 files under this directory
    fund/  (3 files)
      … 3 files under this directory
    pit/  (3 files)
      … 3 files under this directory
    us_index/  (3 files)
      … 3 files under this directory
    yahoo/  (3 files)
      … 3 files under this directory
    README.md
    base.py
    future_calendar_collector.py
    index.py
    utils.py
  README.md
  check_data_health.py
  check_dump_bin.py
  collect_info.py
  dump_bin.py
  dump_pit.py
  get_data.py
tests/  (55 files)
  backtest/  (4 files)
    test_file_strategy.py
    test_high_freq_trading.py
    test_soft_topk_strategy.py
    test_soft_topk_strategy_cold_start.py
  data_mid_layer_tests/  (6 files)
    README.md
    test_dataloader.py
    test_dataset.py
    test_handler.py
    test_handler_storage.py
    test_processor.py
  dataset_tests/  (2 files)
    README.md
    test_datalayer.py
  dependency_tests/  (2 files)
    README.md
    test_mlflow.py
  misc/  (4 files)
    test_get_multi_proc.py
    test_index_data.py
    test_sepdf.py
    test_utils.py
  model/  (2 files)
    test_general_nn.py
    test_hist_workflow.py
  ops/  (3 files)
    test_elem_operator.py
    test_expression_compatibility.py
    test_special_ops.py
  rl/  (6 files)
    test_data_queue.py
    test_finite_env.py
    test_logger.py
    test_qlib_simulator.py
    test_saoe_simple.py
    test_trainer.py
  rolling_tests/  (2 files)
    test_ddgda.py
    test_update_pred.py
  security/  (10 files)
    test_artifact_reader_trust.py
    test_artifact_trust_api.py
    test_eval_registries.py
    test_expression_parser.py
    test_highfreq_artifact_paths.py
    test_hist_artifacts.py
    test_mlflow_artifacts.py
    test_module_loading.py
    test_pickle_utils.py
    test_workflow_artifact_trust.py
  storage_tests/  (1 files)
    test_storage.py
  conftest.py
  pytest.ini
  test_all_pipeline.py
  test_ci_configuration.py
  test_contrib_model.py
  test_contrib_workflow.py
  test_dump_data.py
  test_get_data.py
  test_pit.py
  test_register_ops.py
  test_structured_cov_estimator.py
  test_tra_example.py
  test_workflow.py
.commitlintrc.js
.deepsource.toml
.dockerignore
.gitignore
.mypy.ini
.pre-commit-config.yaml
.pylintrc
.readthedocs.yaml
CHANGELOG.md
CHANGES.rst
CODE_OF_CONDUCT.md
Dockerfile
LICENSE
MANIFEST.in
Makefile
README.md
SECURITY.md
build_docker_image.sh
package.json
pyproject.toml
setup.py
```

## Entry points

- [qlib/cli/data.py:7](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/cli/data.py#L7)
- [qlib/cli/run.py](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/cli/run.py)
- [qlib/contrib/data/utils/sepdf.py:207](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/contrib/data/utils/sepdf.py#L207)
- [qlib/contrib/evaluate.py:418](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/contrib/evaluate.py#L418)
- [qlib/contrib/model/catboost_model.py:99](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/contrib/model/catboost_model.py#L99)
- [qlib/contrib/online/operator.py:319](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/contrib/online/operator.py#L319)
- [qlib/contrib/rolling/__main__.py:6](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/contrib/rolling/__main__.py#L6)
- [qlib/contrib/rolling/base.py:262](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/contrib/rolling/base.py#L262)
- [qlib/rl/contrib/backtest.py:360](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/rl/contrib/backtest.py#L360)
- [qlib/rl/contrib/train_onpolicy.py:255](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/rl/contrib/train_onpolicy.py#L255)
- [qlib/utils/time.py:376](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/utils/time.py#L376)
- [qlib/workflow/task/manage.py:554](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/workflow/task/manage.py#L554)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 16 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: Config, MLflowSettings, OptimizationConfig, PipelineExperimentConfig, QSettings, Qli… |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 41 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: Abs, Add, Alpha158, Alpha158DL, Alpha158vwap, Alpha360. Observed top-level functions: _check_scalar, _… |
| Application entry point | entrypoint | Observed | Groups 30 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: BaostockCollectorHS3005min, BaostockNormalizeHS3005min, CSI100Index, CSI300Index, CSI500I… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| qlib package | library | Observed | Groups 174 file(s) under qlib package (observed from repository paths and static analysis). Observed top-level classes: ACRecordTemp, ACStrategy, ADARNN, ADD, ADDModel, ALSTM. Observed top-level functions: CORAL, _add_b… |
| scripts package | library | Observed | Groups 2 file(s) under scripts package (observed from repository paths and static analysis). Observed top-level classes: BaseCollector, BaseNormalize, BaseRun, IndexBase, Normalize. |
| Tests | test | Observed | Groups 59 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: AccReward, AnyPolicy, DataUtils, Diff, Distance, DoNothingTracker. Observed top-level functions: _assert_re… |

## Important files

- `.deepsource.toml` (config)
- `.dockerignore` (container)
- `.github/dependabot.yml` (config)
- `.github/release-drafter.yml` (config)
- `.github/workflows/lint_title.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/stale.yml` (ci)
- `.github/workflows/test_qlib_from_pip.yml` (ci)
- `.github/workflows/test_qlib_from_source.yml` (ci)
- `.github/workflows/test_qlib_from_source_slow.yml` (ci)
- `.mypy.ini` (config)
- `.pre-commit-config.yaml` (config)
- `.readthedocs.yaml` (config)
- `Dockerfile` (container)
- `MANIFEST.in` (manifest)
- `docs/requirements.txt` (manifest)
- `examples/benchmarks/ADARNN/requirements.txt` (manifest)
- `examples/benchmarks/ADARNN/workflow_config_adarnn_Alpha360.yaml` (config)
- `examples/benchmarks/ADD/requirements.txt` (manifest)
- `examples/benchmarks/ADD/workflow_config_add_Alpha360.yaml` (config)
- `examples/benchmarks/ALSTM/requirements.txt` (manifest)
- `examples/benchmarks/ALSTM/workflow_config_alstm_Alpha158.yaml` (config)
- `examples/benchmarks/ALSTM/workflow_config_alstm_Alpha360.yaml` (config)
- `examples/benchmarks/CatBoost/requirements.txt` (manifest)
- `examples/benchmarks/CatBoost/workflow_config_catboost_Alpha158.yaml` (config)
- `examples/benchmarks/CatBoost/workflow_config_catboost_Alpha158_csi500.yaml` (config)
- `examples/benchmarks/CatBoost/workflow_config_catboost_Alpha360.yaml` (config)
- `examples/benchmarks/CatBoost/workflow_config_catboost_Alpha360_csi500.yaml` (config)
- `examples/benchmarks/DoubleEnsemble/requirements.txt` (manifest)
- `examples/benchmarks/DoubleEnsemble/workflow_config_doubleensemble_Alpha158.yaml` (config)
- `examples/benchmarks/DoubleEnsemble/workflow_config_doubleensemble_Alpha158_csi500.yaml` (config)
- `examples/benchmarks/DoubleEnsemble/workflow_config_doubleensemble_Alpha360.yaml` (config)
- `examples/benchmarks/DoubleEnsemble/workflow_config_doubleensemble_Alpha360_csi500.yaml` (config)
- `examples/benchmarks/DoubleEnsemble/workflow_config_doubleensemble_early_stop_Alpha158.yaml` (config)
- `examples/benchmarks/GATs/requirements.txt` (manifest)
- `examples/benchmarks/GATs/workflow_config_gats_Alpha158.yaml` (config)
- `examples/benchmarks/GATs/workflow_config_gats_Alpha360.yaml` (config)
- `examples/benchmarks/GRU/requirements.txt` (manifest)
- `examples/benchmarks/GRU/workflow_config_gru_Alpha158.yaml` (config)
- `examples/benchmarks/GRU/workflow_config_gru_Alpha360.yaml` (config)
- `examples/benchmarks/GeneralPtNN/workflow_config_gru.yaml` (config)
- `examples/benchmarks/GeneralPtNN/workflow_config_gru2mlp.yaml` (config)
- `examples/benchmarks/GeneralPtNN/workflow_config_mlp.yaml` (config)
- `examples/benchmarks/HIST/qlib_csi300_stock_index.json` (config)
- `examples/benchmarks/HIST/requirements.txt` (manifest)
- `examples/benchmarks/HIST/workflow_config_hist_Alpha360.yaml` (config)
- `examples/benchmarks/IGMTF/requirements.txt` (manifest)
- `examples/benchmarks/IGMTF/workflow_config_igmtf_Alpha360.yaml` (config)
- `examples/benchmarks/KRNN/requirements.txt` (manifest)
- `examples/benchmarks/KRNN/workflow_config_krnn_Alpha360.yaml` (config)
- `examples/benchmarks/LSTM/requirements.txt` (manifest)
- `examples/benchmarks/LSTM/workflow_config_lstm_Alpha158.yaml` (config)
- `examples/benchmarks/LSTM/workflow_config_lstm_Alpha360.yaml` (config)
- `examples/benchmarks/LightGBM/requirements.txt` (manifest)
- `examples/benchmarks/LightGBM/workflow_config_lightgbm_Alpha158.yaml` (config)
- `examples/benchmarks/LightGBM/workflow_config_lightgbm_Alpha158_csi500.yaml` (config)
- `examples/benchmarks/LightGBM/workflow_config_lightgbm_Alpha158_multi_freq.yaml` (config)
- `examples/benchmarks/LightGBM/workflow_config_lightgbm_Alpha360.yaml` (config)
- `examples/benchmarks/LightGBM/workflow_config_lightgbm_Alpha360_csi500.yaml` (config)
- `examples/benchmarks/LightGBM/workflow_config_lightgbm_configurable_dataset.yaml` (config)
- `examples/benchmarks/LightGBM/workflow_config_lightgbm_multi_freq.yaml` (config)
- `examples/benchmarks/Linear/requirements.txt` (manifest)
- `examples/benchmarks/Linear/workflow_config_linear_Alpha158.yaml` (config)
- `examples/benchmarks/Linear/workflow_config_linear_Alpha158_csi500.yaml` (config)
- `examples/benchmarks/Linear/workflow_config_linear_Alpha158_multi_pass_bt.yaml` (config)
- `examples/benchmarks/Localformer/requirements.txt` (manifest)
- `examples/benchmarks/Localformer/workflow_config_localformer_Alpha158.yaml` (config)
- `examples/benchmarks/Localformer/workflow_config_localformer_Alpha360.yaml` (config)
- `examples/benchmarks/MLP/requirements.txt` (manifest)
- `examples/benchmarks/MLP/workflow_config_mlp_Alpha158.yaml` (config)
- `examples/benchmarks/MLP/workflow_config_mlp_Alpha158_csi500.yaml` (config)
- `examples/benchmarks/MLP/workflow_config_mlp_Alpha360.yaml` (config)
- `examples/benchmarks/MLP/workflow_config_mlp_Alpha360_csi500.yaml` (config)
- `examples/benchmarks/SFM/requirements.txt` (manifest)
- `examples/benchmarks/SFM/workflow_config_sfm_Alpha360.yaml` (config)
- `examples/benchmarks/Sandwich/requirements.txt` (manifest)
- `examples/benchmarks/Sandwich/workflow_config_sandwich_Alpha360.yaml` (config)
- `examples/benchmarks/TCN/requirements.txt` (manifest)
- `examples/benchmarks/TCN/workflow_config_tcn_Alpha158.yaml` (config)
- `examples/benchmarks/TCN/workflow_config_tcn_Alpha360.yaml` (config)
- `examples/benchmarks/TCTS/requirements.txt` (manifest)
- `examples/benchmarks/TCTS/workflow_config_tcts_Alpha360.yaml` (config)
- `examples/benchmarks/TFT/requirements.txt` (manifest)
- `examples/benchmarks/TFT/workflow_config_tft_Alpha158.yaml` (config)
- `examples/benchmarks/TRA/configs/config_alstm.yaml` (config)
- `examples/benchmarks/TRA/configs/config_alstm_tra.yaml` (config)
- `examples/benchmarks/TRA/configs/config_alstm_tra_init.yaml` (config)
- `examples/benchmarks/TRA/configs/config_transformer.yaml` (config)
- `examples/benchmarks/TRA/configs/config_transformer_tra.yaml` (config)
- `examples/benchmarks/TRA/configs/config_transformer_tra_init.yaml` (config)
- `examples/benchmarks/TRA/requirements.txt` (manifest)
- `examples/benchmarks/TRA/workflow_config_tra_Alpha158.yaml` (config)
- `examples/benchmarks/TRA/workflow_config_tra_Alpha158_full.yaml` (config)
- `examples/benchmarks/TRA/workflow_config_tra_Alpha360.yaml` (config)
- `examples/benchmarks/TabNet/requirements.txt` (manifest)
- `examples/benchmarks/TabNet/workflow_config_TabNet_Alpha158.yaml` (config)
- `examples/benchmarks/TabNet/workflow_config_TabNet_Alpha360.yaml` (config)
- `examples/benchmarks/Transformer/requirements.txt` (manifest)
- `examples/benchmarks/Transformer/workflow_config_transformer_Alpha158.yaml` (config)
- `examples/benchmarks/Transformer/workflow_config_transformer_Alpha360.yaml` (config)
- `examples/benchmarks/XGBoost/requirements.txt` (manifest)
- `examples/benchmarks/XGBoost/workflow_config_xgboost_Alpha158.yaml` (config)
- `examples/benchmarks/XGBoost/workflow_config_xgboost_Alpha360.yaml` (config)
- `examples/benchmarks_dynamic/DDG-DA/requirements.txt` (manifest)
- `examples/benchmarks_dynamic/baseline/workflow_config_lightgbm_Alpha158.yaml` (config)
- `examples/benchmarks_dynamic/baseline/workflow_config_linear_Alpha158.yaml` (config)
- `examples/highfreq/workflow_config_High_Freq_Tree_Alpha158.yaml` (config)
- `examples/hyperparameter/LightGBM/requirements.txt` (manifest)
- `examples/model_rolling/requirements.txt` (manifest)
- `examples/portfolio/config_enhanced_indexing.yaml` (config)
- `examples/rl_order_execution/exp_configs/backtest_opds.yml` (config)
- `examples/rl_order_execution/exp_configs/backtest_ppo.yml` (config)
- `examples/rl_order_execution/exp_configs/backtest_twap.yml` (config)
- `examples/rl_order_execution/exp_configs/train_opds.yml` (config)
- `examples/rl_order_execution/exp_configs/train_ppo.yml` (config)
- `examples/rl_order_execution/scripts/pickle_data_config.yml` (config)
- `package.json` (manifest)
- `pyproject.toml` (manifest)
- `scripts/data_collector/baostock_5min/requirements.txt` (manifest)
- `scripts/data_collector/br_index/requirements.txt` (manifest)
- `scripts/data_collector/cn_index/requirements.txt` (manifest)
- `scripts/data_collector/contrib/fill_cn_1min_data/requirements.txt` (manifest)
- `scripts/data_collector/contrib/future_trading_date_collector/requirements.txt` (manifest)
- `scripts/data_collector/fund/requirements.txt` (manifest)
- `scripts/data_collector/pit/requirements.txt` (manifest)
- `scripts/data_collector/us_index/requirements.txt` (manifest)
- `scripts/data_collector/yahoo/requirements.txt` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `qlib` — 235 analysed file(s)
- `examples` — 187 analysed file(s)
- `tests` — 55 analysed file(s)
- `scripts` — 43 analysed file(s)
- `docs` — 42 analysed file(s)
- `(root files)` — 21 analysed file(s)
- `.github` — 17 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `54355232463878d2eebb91fe0ee5fa7fa1f5976c` is the revision these paths and observations refer to.
