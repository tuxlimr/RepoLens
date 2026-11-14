# Project structure: optuna/optuna

**Analysed commit:** `abf8914d48571120574469575d37c4b0929b7f0f`

**Commit reference:** [abf8914d48571120574469575d37c4b0929b7f0f](https://github.com/optuna/optuna/commit/abf8914d48571120574469575d37c4b0929b7f0f)

**Tree at this commit:** [optuna/optuna@abf8914d4857](https://github.com/optuna/optuna/tree/abf8914d48571120574469575d37c4b0929b7f0f)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | optuna/optuna |
| Description | A hyperparameter optimization framework |
| Stars | 15043 |
| Forks | 1465 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `abf8914d48571120574469575d37c4b0929b7f0f` |
| Retrieved at | 2026-11-14T19:09:09.209330+00:00 |
| Files in this snapshot | 471 |

## Directory tree

```text
.github/  (23 files)
  ISSUE_TEMPLATE/  (6 files)
    bug-report.yml
    code-fix.yml
    config.yml
    documentation.yml
    feature-request.yml
    questions-help-support.yml
  workflows/  (12 files)
    checks-optional.yaml
    checks.yml
    mac-tests.yml
    matplotlib-tests.yml
    pypi-publish.yml
    reviewdog.yml
    sphinx-build.yml
    stale.yml
    tests-storage.yml
    tests-with-minimum-versions.yml
    tests.yml
    windows-tests.yml
  CODEOWNERS
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
  release.yml
docs/  (71 files)
  source/  (43 files)
    _static/  (1 files)
      … 1 files under this directory
    _templates/  (4 files)
      … 4 files under this directory
    reference/  (30 files)
      … 30 files under this directory
    tutorial/  (1 files)
      … 1 files under this directory
    conf.py
    docutils.conf
    faq.rst
    index.rst
    installation.rst
    license_thirdparty.rst
    privacy.rst
  visualization_examples/  (13 files)
    GALLERY_HEADER.rst
    optuna.visualization.plot_contour.py
    optuna.visualization.plot_edf.py
    optuna.visualization.plot_hypervolume_history.py
    optuna.visualization.plot_intermediate_values.py
    optuna.visualization.plot_optimization_history.py
    optuna.visualization.plot_parallel_coordinate.py
    optuna.visualization.plot_param_importances.py
    optuna.visualization.plot_pareto_front.py
    optuna.visualization.plot_rank.py
    optuna.visualization.plot_slice.py
    optuna.visualization.plot_terminator_improvement.py
    optuna.visualization.plot_timeline.py
  visualization_matplotlib_examples/  (13 files)
    GALLERY_HEADER.rst
    optuna.visualization.matplotlib.contour.py
    optuna.visualization.matplotlib.edf.py
    optuna.visualization.matplotlib.hypervolume_history.py
    optuna.visualization.matplotlib.intermediate_values.py
    optuna.visualization.matplotlib.optimization_history.py
    optuna.visualization.matplotlib.parallel_coordinate.py
    optuna.visualization.matplotlib.param_importances.py
    optuna.visualization.matplotlib.pareto_front.py
    optuna.visualization.matplotlib.rank.py
    optuna.visualization.matplotlib.slice.py
    optuna.visualization.matplotlib.terminator_improvement.py
    optuna.visualization.matplotlib.timeline.py
  Makefile
  make.bat
optuna/  (225 files)
  _gp/  (10 files)
    __init__.py
    acqf.py
    batched_lbfgsb.py
    gp.py
    optim_mixed.py
    optim_sample.py
    prior.py
    qmc.py
    search_space.py
    thread_limiting.py
  _hypervolume/  (4 files)
    __init__.py
    box_decomposition.py
    hssp.py
    wfg.py
  artifacts/  (10 files)
    __init__.py
    _backoff.py
    _boto3.py
    _download.py
    _filesystem.py
    _gcs.py
    _list_artifact_meta.py
    _protocol.py
    _upload.py
    exceptions.py
  importance/  (10 files)
    _fanova/  (4 files)
      … 4 files under this directory
    _ped_anova/  (3 files)
      … 3 files under this directory
    __init__.py
    _base.py
    _mean_decrease_impurity.py
  integration/  (20 files)
    __init__.py
    botorch.py
    catboost.py
    cma.py
    dask.py
    fastaiv2.py
    keras.py
    lightgbm.py
    mlflow.py
    pytorch_distributed.py
    pytorch_ignite.py
    pytorch_lightning.py
    shap.py
    sklearn.py
    skorch.py
    tensorboard.py
    tensorflow.py
    tfkeras.py
    wandb.py
    xgboost.py
  pruners/  (10 files)
    __init__.py
    _base.py
    _hyperband.py
    _median.py
    _nop.py
    _patient.py
    _percentile.py
    _successive_halving.py
    _threshold.py
    _wilcoxon.py
  samplers/  (41 files)
    _ga/  (2 files)
      … 2 files under this directory
    _gp/  (2 files)
      … 2 files under this directory
    _nsgaiii/  (3 files)
      … 3 files under this directory
    _tpe/  (6 files)
      … 6 files under this directory
    nsgaii/  (19 files)
      … 19 files under this directory
    __init__.py
    _base.py
    _brute_force.py
    _cmaes.py
    _grid.py
    _lazy_random_state.py
    _partial_fixed.py
    _qmc.py
    _random.py
  search_space/  (3 files)
    __init__.py
    group_decomposed.py
    intersection.py
  storages/  (35 files)
    _grpc/  (8 files)
      … 8 files under this directory
    _rdb/  (16 files)
      … 16 files under this directory
    journal/  (5 files)
      … 5 files under this directory
    __init__.py
    _base.py
    _cached_storage.py
    _callbacks.py
    _heartbeat.py
    _in_memory.py
  study/  (10 files)
    __init__.py
    _constrained_optimization.py
    _dataframe.py
    _frozen.py
    _multi_objective.py
    _optimize.py
    _study_direction.py
    _study_summary.py
    _tell.py
    study.py
  terminator/  (8 files)
    improvement/  (3 files)
      … 3 files under this directory
    __init__.py
    callback.py
    erroreval.py
    median_erroreval.py
    terminator.py
  testing/  (12 files)
    __init__.py
    objectives.py
    pruners.py
    pytest_importance.py
    pytest_samplers.py
    pytest_storages.py
    samplers.py
    storages.py
    tempfile_pool.py
    threading.py
    trials.py
    visualization.py
  trial/  (6 files)
    __init__.py
    _base.py
    _fixed.py
    _frozen.py
    _state.py
    _trial.py
  visualization/  (30 files)
    matplotlib/  (15 files)
      … 15 files under this directory
    __init__.py
    _contour.py
    _edf.py
    _hypervolume_history.py
    _intermediate_values.py
    _optimization_history.py
    _parallel_coordinate.py
    _param_importances.py
    _pareto_front.py
    _plotly_imports.py
    _rank.py
    _slice.py
    _terminator_improvement.py
    _timeline.py
    _utils.py
  __init__.py
  _callbacks.py
  _convert_positional_args.py
  _deprecated.py
  _experimental.py
  _imports.py
  _transform.py
  _typing.py
  _warnings.py
  cli.py
  distributions.py
  exceptions.py
  logging.py
  progress_bar.py
  py.typed
  version.py
tests/  (118 files)
  artifacts_tests/  (9 files)
    __init__.py
    stubs.py
    test_backoff.py
    test_boto3.py
    test_download_artifact.py
    test_filesystem.py
    test_gcs.py
    test_list_artifact_meta.py
    test_upload_artifact.py
  gp_tests/  (4 files)
    test_acqf.py
    test_batched_lbfgsb.py
    test_gp.py
    test_search_space.py
  hypervolume_tests/  (4 files)
    __init__.py
    test_box_decomposition.py
    test_hssp.py
    test_wfg.py
  importance_tests/  (7 files)
    fanova_tests/  (2 files)
      … 2 files under this directory
    pedanova_tests/  (3 files)
      … 3 files under this directory
    __init__.py
    test_evaluator.py
  pruners_tests/  (9 files)
    __init__.py
    test_hyperband.py
    test_median.py
    test_nop.py
    test_patient.py
    test_percentile.py
    test_successive_halving.py
    test_threshold.py
    test_wilcoxon.py
  samplers_tests/  (18 files)
    tpe_tests/  (6 files)
      … 6 files under this directory
    __init__.py
    test_base_gasampler.py
    test_brute_force.py
    test_cmaes.py
    test_gp.py
    test_grid.py
    test_lazy_random_state.py
    test_nsgaii.py
    test_nsgaiii.py
    test_partial_fixed.py
    test_qmc.py
    test_samplers.py
  search_space_tests/  (3 files)
    __init__.py
    test_group_decomposed.py
    test_intersection.py
  storages_tests/  (16 files)
    journal_tests/  (5 files)
      … 5 files under this directory
    rdb_tests/  (4 files)
      … 4 files under this directory
    __init__.py
    test_cached_storage.py
    test_callbacks.py
    test_grpc.py
    test_heartbeat.py
    test_storages.py
    test_with_server.py
  study_tests/  (7 files)
    __init__.py
    test_constrained_optimization.py
    test_dataframe.py
    test_multi_objective.py
    test_optimize.py
    test_study.py
    test_study_summary.py
  terminator_tests/  (6 files)
    improvement_tests/  (2 files)
      … 2 files under this directory
    test_callback.py
    test_erroreval.py
    test_median_erroreval.py
    test_terminator.py
  trial_tests/  (5 files)
    __init__.py
    test_fixed.py
    test_frozen.py
    test_trial.py
    test_trials.py
  visualization_tests/  (18 files)
    matplotlib_tests/  (3 files)
      … 3 files under this directory
    __init__.py
    test_contour.py
    test_edf.py
    test_hypervolume_history.py
    test_intermediate_plot.py
    test_optimization_history.py
    test_parallel_coordinate.py
    test_param_importances.py
    test_pareto_front.py
    test_rank.py
    test_slice.py
    test_terminator_improvement.py
    test_timeline.py
    test_utils.py
    test_visualizations.py
  __init__.py
  conftest.py
  test_callbacks.py
  test_cli.py
  test_convert_positional_args.py
  test_deprecated.py
  test_distributions.py
  test_experimental.py
  test_imports.py
  test_logging.py
  test_multi_objective.py
  test_transform.py
tutorial/  (22 files)
  10_key_features/  (6 files)
    001_first.py
    002_configurations.py
    003_efficient_optimization_algorithms.py
    004_distributed.py
    005_visualization.py
    README.rst
  20_recipes/  (15 files)
    001_rdb.py
    002_multi_objective.py
    003_attributes.py
    004_cli.py
    005_user_defined_sampler.py
    006_user_defined_pruner.py
    007_optuna_callback.py
    008_specify_params.py
    009_ask_and_tell.py
    010_reuse_best_trial.py
    011_journal_storage.py
    012_artifact_tutorial.py
    013_wilcoxon_pruner.py
    014_ablation_study_by_optuna.py
    README.rst
  README.rst
.gitignore
.pre-commit-config.yaml
.readthedocs.yml
CITATION.cff
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
LICENSE_THIRD_PARTY
MANIFEST.in
README.md
SECURITY.md
pyproject.toml
```

## Entry points

- [optuna/cli.py](https://github.com/optuna/optuna/blob/abf8914d48571120574469575d37c4b0929b7f0f/optuna/cli.py)
- [tutorial/20_recipes/004_cli.py:37](https://github.com/optuna/optuna/blob/abf8914d48571120574469575d37c4b0929b7f0f/tutorial/20_recipes/004_cli.py#L37)
- [tutorial/20_recipes/012_artifact_tutorial.py:424](https://github.com/optuna/optuna/blob/abf8914d48571120574469575d37c4b0929b7f0f/tutorial/20_recipes/012_artifact_tutorial.py#L424)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: StudyDirectionModel, StudyModel, StudySystemAttributeModel, StudyUserAttributeModel, TrialHeartbeatMode… |
| Application entry point | entrypoint | Observed | Groups 4 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: CellValue, Objective, ValueType, _Ask, _BaseCommand, _BestTrial. Observed top-level functi… |
| External integrations | external | Observed | Groups 21 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: GrpcClientCache, GrpcClientCacheEntry, GrpcStorageProxy, _LightGBMModule. Observed top-leve… |
| optuna package | library | Observed | Groups 196 file(s) under optuna package (observed from repository paths and static analysis). Observed top-level classes: ArtifactMeta, ArtifactNotFound, ArtifactStore, BLXAlphaCrossover, Backoff, BaseAcquisitionFunc. O… |
| Tests | test | Observed | Groups 118 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH optuna.samplers.nsgaii._child_generation_strategy.perform_crossover, PATCH optuna.samplers.nsgaii._after_trial_… |
| tutorial package | library | Observed | Groups 17 file(s) under tutorial package (observed from repository paths and static analysis). Observed top-level classes: LastPlacePruner, SAOptions, SimulatedAnnealingSampler, StopWhenTrialKeepBeingPrunedCallback. Obs… |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/bug-report.yml` (config)
- `.github/ISSUE_TEMPLATE/code-fix.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/documentation.yml` (config)
- `.github/ISSUE_TEMPLATE/feature-request.yml` (config)
- `.github/ISSUE_TEMPLATE/questions-help-support.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/release.yml` (config)
- `.github/workflows/checks-optional.yaml` (ci)
- `.github/workflows/checks.yml` (ci)
- `.github/workflows/mac-tests.yml` (ci)
- `.github/workflows/matplotlib-tests.yml` (ci)
- `.github/workflows/pypi-publish.yml` (ci)
- `.github/workflows/reviewdog.yml` (ci)
- `.github/workflows/sphinx-build.yml` (ci)
- `.github/workflows/stale.yml` (ci)
- `.github/workflows/tests-storage.yml` (ci)
- `.github/workflows/tests-with-minimum-versions.yml` (ci)
- `.github/workflows/tests.yml` (ci)
- `.github/workflows/windows-tests.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `.readthedocs.yml` (config)
- `MANIFEST.in` (manifest)
- `optuna/storages/_rdb/alembic.ini` (config)
- `pyproject.toml` (manifest)

## Top-level layout

- `optuna` — 225 analysed file(s)
- `tests` — 118 analysed file(s)
- `docs` — 71 analysed file(s)
- `.github` — 23 analysed file(s)
- `tutorial` — 22 analysed file(s)
- `(root files)` — 12 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `abf8914d48571120574469575d37c4b0929b7f0f` is the revision these paths and observations refer to.
