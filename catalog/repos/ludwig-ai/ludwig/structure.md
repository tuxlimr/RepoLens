# Project structure: ludwig-ai/ludwig

**Analysed commit:** `b16404c1e985a23f2b7c0246228c4fc85b7cf406`

**Commit reference:** [b16404c1e985a23f2b7c0246228c4fc85b7cf406](https://github.com/ludwig-ai/ludwig/commit/b16404c1e985a23f2b7c0246228c4fc85b7cf406)

**Tree at this commit:** [ludwig-ai/ludwig@b16404c1e985](https://github.com/ludwig-ai/ludwig/tree/b16404c1e985a23f2b7c0246228c4fc85b7cf406)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | ludwig-ai/ludwig |
| Description | Low-code framework for building custom LLMs, neural networks, and other AI models |
| Stars | 11790 |
| Forks | 1213 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `b16404c1e985a23f2b7c0246228c4fc85b7cf406` |
| Retrieved at | 2026-11-14T19:10:25.005041+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.claude/  (3 files)
  commands/  (1 files)
    ludwig_review.md
  scheduled_tasks.lock
  settings.json
.devcontainer/  (2 files)
  Dockerfile
  devcontainer.json
.github/  (9 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (6 files)
    docker.yml
    pytest.yml
    pytest_slow.yml
    schema.yml
    test-results.yml
    upload-pypi.yml
  pull_request_template.md
.vscode/  (1 files)
  settings.json
docker/  (6 files)
  ludwig/  (1 files)
    Dockerfile
  ludwig-gpu/  (1 files)
    Dockerfile
  ludwig-ray/  (1 files)
    Dockerfile
  ludwig-ray-gpu/  (1 files)
    Dockerfile
  README.md
  build_and_push.sh
docs/  (1 files)
  developer_guide/  (1 files)
    adding_a_feature_type.md
examples/  (190 files)
  alignment/  (9 files)
    README.md
    alignment_dpo.ipynb
    config_dpo.yaml
    config_grpo.yaml
    config_kto.yaml
    config_orpo.yaml
    prepare_dataset.py
    train_dpo.py
    train_grpo.py
  anomaly_detection/  (6 files)
    README.md
    anomaly_detection.ipynb
    config_deep_sad.yaml
    config_deep_svdd.yaml
    config_drocc.yaml
    train.py
  calibration/  (3 files)
    README.md
    train_forest_cover_calibrated.py
    train_mushroom_edibility_calibrated.py
  class_imbalance/  (5 files)
    README.md
    balanced_model_config.yaml
    model_training.py
    model_training_results.ipynb
    standard_model_config.yaml
  forecasting/  (2 files)
    README.md
    config.yaml
  getting_started/  (2 files)
    rotten_tomatoes.yaml
    run.sh
  hypernetwork/  (5 files)
    README.md
    config_concat.yaml
    config_hypernetwork.yaml
    hypernetwork.ipynb
    train_hypernetwork.py
  hyperopt/  (5 files)
    README.md
    README_optuna.md
    config_optuna.yaml
    optuna_executor.ipynb
    optuna_executor.py
  image_encoders/  (8 files)
    README.md
    compare_encoders.py
    config_clip.yaml
    config_dinov2_finetuned.yaml
    config_dinov2_linear_probe.yaml
    config_siglip.yaml
    config_stacked_cnn.yaml
    image_encoders.ipynb
  insurance_lite/  (2 files)
    config.yaml
    train.py
  kfold_cv/  (5 files)
    README.md
    display_kfold_cv_results.py
    k-fold_cv_classification.sh
    prepare_classification_data_set.py
    regression_example.ipynb
  lbfgs/  (2 files)
    config.yaml
    model.py
  llama2_7b_finetuning_4bit/  (4 files)
    README.md
    llama2_7b_4bit.yaml
    run_train.sh
    train_alpaca.py
  llm_base_model_dequantization/  (2 files)
    README.md
    phi_2_dequantization.py
  llm_config_generation/  (4 files)
    README.md
    example_description.txt
    generate_and_train.py
    llm_config_generation.ipynb
  llm_few_shot_learning/  (1 files)
    simple_model_training.py
  llm_finetuning/  (6 files)
    README.md
    imdb_deepspeed_zero3.yaml
    imdb_deepspeed_zero3_ray.yaml
    run_train_dsz3.sh
    run_train_dsz3_ray.sh
    train_imdb_ray.py
  llm_instruction_tuning/  (1 files)
    train_alpaca_ray.py
  llm_structured_output/  (5 files)
    README.md
    config_constrained.yaml
    config_json_schema.yaml
    run_structured.py
    structured_output.ipynb
  llm_text_generation/  (1 files)
    simple_model_training.py
  llm_zero_shot_learning/  (1 files)
    simple_model_training.py
  mamba_encoders/  (3 files)
    README.md
    jamba_sequence.yaml
    mamba2_text_classification.yaml
  mnist/  (5 files)
    README.md
    advanced_model_training.py
    assess_model_performance.py
    config.yaml
    simple_model_training.py
  multi_task/  (8 files)
    README.md
    compare_balancers.py
    config_famo.yaml
    config_nash_mtl.yaml
    config_no_balancing.yaml
    config_uncertainty.yaml
    multi_task.ipynb
    train_multi_task.py
  open_set_recognition/  (9 files)
    README.md
    config_baseline.yaml
    config_baseline_mnist.yaml
    config_entropic.yaml
    config_entropic_mnist.yaml
    config_objectosphere.yaml
    config_objectosphere_mnist.yaml
    open_set_mnist.ipynb
    train_open_set.py
  optimizers/  (8 files)
    README.md
    config_adafactor.yaml
    config_adamw.yaml
    config_muon.yaml
    config_radam.yaml
    config_schedule_free_adamw.yaml
    optimizer_comparison.ipynb
    optimizer_comparison.py
  peft_advanced/  (11 files)
    README.md
    compare_adapters.py
    corda_lora.yaml
    eva_lora.yaml
    ln_tuning_llm.yaml
    loftq_lora.yaml
    oft_llm.yaml
    pissa_lora.yaml
    tinylora_llm.yaml
    train_example.py
    vblora_llm.yaml
  ray/  (15 files)
    job_submission/  (4 files)
      … 4 files under this directory
    kubernetes/  (11 files)
      … 11 files under this directory
  regex_freezing/  (2 files)
    ecd_freezing_with_regex_training.py
    llm_freezing_with_regex_training.py
  semantic_segmentation/  (8 files)
    README.md
    camseq.py
    config_camseq.yaml
    config_fpn.yaml
    config_segformer.yaml
    config_unet_depth.yaml
    semantic_segmentation.ipynb
    unet_depth_sweep.py
  serve/  (7 files)
    prometheus_monitoring/  (3 files)
      … 3 files under this directory
    README.md
    client_program.py
    vllm_client.py
    vllm_serving.ipynb
  serving/  (4 files)
    kserve/  (2 files)
      … 2 files under this directory
    ray_serve/  (2 files)
      … 2 files under this directory
  synthetic/  (1 files)
    train.py
  tabnet/  (4 files)
    higgs/  (4 files)
      … 4 files under this directory
  timeseries_forecasting/  (2 files)
    nbeats_example.yaml
    patchtst_example.yaml
  titanic/  (6 files)
    README.md
    model1_config.yaml
    model2_config.yaml
    model_training_results.ipynb
    multiple_model_training.py
    simple_model_training.py
  twitter_bots/  (3 files)
    README.md
    train_twitter_bots.py
    train_twitter_bots_text_only.py
  uncertainty/  (6 files)
    README.md
    config_baseline.yaml
    config_calibrated.yaml
    config_mc_dropout.yaml
    train.py
    uncertainty.ipynb
  vlm_finetuning/  (3 files)
    README.md
    run.py
    vlm_config.yaml
  wine_quality/  (2 files)
    README.md
    model_defaults_example.ipynb
  wmt15/  (3 files)
    config_large.yaml
    config_small.yaml
    train_nmt.py
  README.md
ludwig/  (569 files)
  accounting/  (2 files)
    __init__.py
    used_tokens.py
  automl/  (17 files)
    defaults/  (8 files)
      … 8 files under this directory
    __init__.py
    auto_tune_config.py
    automl.py
    base_config.py
    config_enumerator.py
    config_sampler.py
    config_validator.py
    search_space.py
    target_detection.py
  backend/  (6 files)
    utils/  (2 files)
      … 2 files under this directory
    __init__.py
    base.py
    datasource.py
    ray.py
  benchmarking/  (34 files)
    configs/  (21 files)
      … 21 files under this directory
    examples/  (2 files)
      … 2 files under this directory
    README.md
    __init__.py
    artifacts.py
    benchmark.py
    profiler.py
    profiler_callbacks.py
    profiler_dataclasses.py
    reporting.py
    summarize.py
    summary_dataclasses.py
    utils.py
  callbacks/  (2 files)
    __init__.py
    studio.py
  combiners/  (3 files)
    __init__.py
    combiners.py
    tabpfn_v2_combiner.py
  config_sampling/  (3 files)
    __init__.py
    explore_schema.py
    parameter_sampling.py
  config_validation/  (4 files)
    __init__.py
    checks.py
    preprocessing.py
    validation.py
  contribs/  (7 files)
    mlflow/  (3 files)
      … 3 files under this directory
    __init__.py
    aim.py
    comet.py
    wandb.py
  data/  (37 files)
    batcher/  (6 files)
      … 6 files under this directory
    cache/  (4 files)
      … 4 files under this directory
    dataframe/  (5 files)
      … 5 files under this directory
    dataset/  (4 files)
      … 4 files under this directory
    __init__.py
    concatenate_datasets.py
    dataset_synthesizer.py
    format_registry.py
    lazy_utils.py
    multimodal_collator.py
    negative_sampling.py
    postprocessing.py
    preprocessing.py
    preprocessing_progress.py
    prompt.py
    sampler.py
    split.py
    split_dataset.py
    split_utils.py
    statistics.py
    types.py
    utils.py
  datasets/  (444 files)
    configs/  (441 files)
      … 441 files under this directory
    README.md
    __init__.py
    archives.py
  __init__.py
  api.py
  api_annotations.py
  api_types.py
  check.py
  cli.py
  collect.py
  config_generation.py
  constants.py
  contrib.py
.actrc
.deepsource.toml
.flake8
.gitignore
.nojekyll
.plan
.plan-lazy-preprocessing.md
.pre-commit-config.yaml
.protolint.yaml
CODEOWNERS
CODE_OF_CONDUCT.md
CONTRIBUTING.md
IMPROVEMENT_PLAN.md
LICENSE
NOTICE
README.md
README_KR.md
RELEASES.md
SECURITY.md
```

## Entry points

- [ludwig/benchmarking/summarize.py:95](https://github.com/ludwig-ai/ludwig/blob/b16404c1e985a23f2b7c0246228c4fc85b7cf406/ludwig/benchmarking/summarize.py#L95)
- [ludwig/cli.py:200](https://github.com/ludwig-ai/ludwig/blob/b16404c1e985a23f2b7c0246228c4fc85b7cf406/ludwig/cli.py#L200)
- [ludwig/collect.py:446](https://github.com/ludwig-ai/ludwig/blob/b16404c1e985a23f2b7c0246228c4fc85b7cf406/ludwig/collect.py#L446)
- [ludwig/data/concatenate_datasets.py:91](https://github.com/ludwig-ai/ludwig/blob/b16404c1e985a23f2b7c0246228c4fc85b7cf406/ludwig/data/concatenate_datasets.py#L91)
- [ludwig/data/dataset_synthesizer.py:640](https://github.com/ludwig-ai/ludwig/blob/b16404c1e985a23f2b7c0246228c4fc85b7cf406/ludwig/data/dataset_synthesizer.py#L640)
- [ludwig/data/split_dataset.py:38](https://github.com/ludwig-ai/ludwig/blob/b16404c1e985a23f2b7c0246228c4fc85b7cf406/ludwig/data/split_dataset.py#L38)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 475 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 34 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AudioMetadata, Batcher, BinaryMetadata, BucketedBatcher, CacheableDataframe, CacheableDataset. Observe… |
| docker package | library | Observed | Groups 1 file(s) under docker package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 6 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: CLI. Observed top-level functions: _get_feature_encoder_or_decoder, assign_vocab, build_fe… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| ludwig package | library | Observed | Groups 55 file(s) under ludwig package (observed from repository paths and static analysis). Observed top-level classes: AimCallback, AimLoader, ArchiveType, AutoTrainResults, Backend, BackendCapabilities. Observed top-… |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: test_pandas_batcher_use_all_samples, test_pandas_size. |

## Important files

- `.claude/settings.json` (config)
- `.deepsource.toml` (config)
- `.devcontainer/Dockerfile` (container)
- `.devcontainer/devcontainer.json` (config)
- `.github/workflows/docker.yml` (ci)
- `.github/workflows/pytest.yml` (ci)
- `.github/workflows/pytest_slow.yml` (ci)
- `.github/workflows/schema.yml` (ci)
- `.github/workflows/test-results.yml` (ci)
- `.github/workflows/upload-pypi.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `.protolint.yaml` (config)
- `.vscode/settings.json` (config)
- `docker/ludwig-gpu/Dockerfile` (container)
- `docker/ludwig-ray-gpu/Dockerfile` (container)
- `docker/ludwig-ray/Dockerfile` (container)
- `docker/ludwig/Dockerfile` (container)
- `examples/alignment/config_dpo.yaml` (config)
- `examples/alignment/config_grpo.yaml` (config)
- `examples/alignment/config_kto.yaml` (config)
- `examples/alignment/config_orpo.yaml` (config)
- `examples/anomaly_detection/config_deep_sad.yaml` (config)
- `examples/anomaly_detection/config_deep_svdd.yaml` (config)
- `examples/anomaly_detection/config_drocc.yaml` (config)
- `examples/class_imbalance/balanced_model_config.yaml` (config)
- `examples/class_imbalance/standard_model_config.yaml` (config)
- `examples/forecasting/config.yaml` (config)
- `examples/getting_started/rotten_tomatoes.yaml` (config)
- `examples/hypernetwork/config_concat.yaml` (config)
- `examples/hypernetwork/config_hypernetwork.yaml` (config)
- `examples/hyperopt/config_optuna.yaml` (config)
- `examples/image_encoders/config_clip.yaml` (config)
- `examples/image_encoders/config_dinov2_finetuned.yaml` (config)
- `examples/image_encoders/config_dinov2_linear_probe.yaml` (config)
- `examples/image_encoders/config_siglip.yaml` (config)
- `examples/image_encoders/config_stacked_cnn.yaml` (config)
- `examples/insurance_lite/config.yaml` (config)
- `examples/lbfgs/config.yaml` (config)
- `examples/llama2_7b_finetuning_4bit/llama2_7b_4bit.yaml` (config)
- `examples/llm_finetuning/imdb_deepspeed_zero3.yaml` (config)
- `examples/llm_finetuning/imdb_deepspeed_zero3_ray.yaml` (config)
- `examples/llm_structured_output/config_constrained.yaml` (config)
- `examples/llm_structured_output/config_json_schema.yaml` (config)
- `examples/mamba_encoders/jamba_sequence.yaml` (config)
- `examples/mamba_encoders/mamba2_text_classification.yaml` (config)
- `examples/mnist/config.yaml` (config)
- `examples/multi_task/config_famo.yaml` (config)
- `examples/multi_task/config_nash_mtl.yaml` (config)
- `examples/multi_task/config_no_balancing.yaml` (config)
- `examples/multi_task/config_uncertainty.yaml` (config)
- `examples/open_set_recognition/config_baseline.yaml` (config)
- `examples/open_set_recognition/config_baseline_mnist.yaml` (config)
- `examples/open_set_recognition/config_entropic.yaml` (config)
- `examples/open_set_recognition/config_entropic_mnist.yaml` (config)
- `examples/open_set_recognition/config_objectosphere.yaml` (config)
- `examples/open_set_recognition/config_objectosphere_mnist.yaml` (config)
- `examples/optimizers/config_adafactor.yaml` (config)
- `examples/optimizers/config_adamw.yaml` (config)
- `examples/optimizers/config_muon.yaml` (config)
- `examples/optimizers/config_radam.yaml` (config)
- `examples/optimizers/config_schedule_free_adamw.yaml` (config)
- `examples/peft_advanced/corda_lora.yaml` (config)
- `examples/peft_advanced/eva_lora.yaml` (config)
- `examples/peft_advanced/ln_tuning_llm.yaml` (config)
- `examples/peft_advanced/loftq_lora.yaml` (config)
- `examples/peft_advanced/oft_llm.yaml` (config)
- `examples/peft_advanced/pissa_lora.yaml` (config)
- `examples/peft_advanced/tinylora_llm.yaml` (config)
- `examples/peft_advanced/vblora_llm.yaml` (config)
- `examples/ray/job_submission/config.yaml` (config)
- `examples/ray/kubernetes/clusters/ludwig-ray-cpu-cluster.yaml` (config)
- `examples/ray/kubernetes/clusters/ludwig-ray-gpu-cluster.yaml` (config)
- `examples/semantic_segmentation/config_camseq.yaml` (config)
- `examples/semantic_segmentation/config_fpn.yaml` (config)
- `examples/semantic_segmentation/config_segformer.yaml` (config)
- `examples/semantic_segmentation/config_unet_depth.yaml` (config)
- `examples/serve/prometheus_monitoring/docker-compose.yml` (container)
- `examples/serve/prometheus_monitoring/prometheus.yml` (config)
- `examples/serving/kserve/serving_config.yaml` (config)
- `examples/tabnet/higgs/medium_config.yaml` (config)
- `examples/tabnet/higgs/small_config.yaml` (config)
- `examples/timeseries_forecasting/nbeats_example.yaml` (config)
- `examples/timeseries_forecasting/patchtst_example.yaml` (config)
- `examples/titanic/model1_config.yaml` (config)
- `examples/titanic/model2_config.yaml` (config)
- `examples/uncertainty/config_baseline.yaml` (config)
- `examples/uncertainty/config_calibrated.yaml` (config)
- `examples/uncertainty/config_mc_dropout.yaml` (config)
- `examples/vlm_finetuning/vlm_config.yaml` (config)
- `examples/wmt15/config_large.yaml` (config)
- `examples/wmt15/config_small.yaml` (config)
- `ludwig/automl/defaults/base_automl_config.yaml` (config)
- `ludwig/automl/defaults/combiner/concat_config.yaml` (config)
- `ludwig/automl/defaults/combiner/ft_transformer_config.yaml` (config)
- `ludwig/automl/defaults/combiner/tabnet_config.yaml` (config)
- `ludwig/automl/defaults/combiner/tabtransformer_config.yaml` (config)
- `ludwig/automl/defaults/combiner/transformer_config.yaml` (config)
- `ludwig/automl/defaults/reference_configs.yaml` (config)
- `ludwig/automl/defaults/text/bert_config.yaml` (config)
- `ludwig/benchmarking/configs/allstate_claims_severity.yaml` (config)
- `ludwig/benchmarking/configs/amazon_review_polarity.yaml` (config)
- `ludwig/benchmarking/configs/amazon_reviews.yaml` (config)
- `ludwig/benchmarking/configs/ames_housing.yaml` (config)
- `ludwig/benchmarking/configs/bnp_claims_management.yaml` (config)
- `ludwig/benchmarking/configs/connect4.yaml` (config)
- `ludwig/benchmarking/configs/goemotions.yaml` (config)
- `ludwig/benchmarking/configs/higgs.yaml` (config)
- `ludwig/benchmarking/configs/ieee_fraud.yaml` (config)
- `ludwig/benchmarking/configs/imbalanced_insurance.yaml` (config)
- `ludwig/benchmarking/configs/mercedes_benz_greener.yaml` (config)
- `ludwig/benchmarking/configs/otto_group_product.yaml` (config)
- `ludwig/benchmarking/configs/porto_seguro_safe_driver.yaml` (config)
- `ludwig/benchmarking/configs/protein.yaml` (config)
- `ludwig/benchmarking/configs/santander_customer_satisfaction.yaml` (config)
- `ludwig/benchmarking/configs/santander_customer_transaction.yaml` (config)
- `ludwig/benchmarking/configs/sst2.yaml` (config)
- `ludwig/benchmarking/configs/sst3.yaml` (config)
- `ludwig/benchmarking/configs/sst5.yaml` (config)
- `ludwig/benchmarking/configs/titanic.yaml` (config)
- `ludwig/benchmarking/configs/yelp_reviews.yaml` (config)
- `ludwig/benchmarking/examples/benchmarking_config.yaml` (config)
- `ludwig/datasets/configs/abjad_kids.yaml` (config)
- `ludwig/datasets/configs/acronym_identification.yaml` (config)
- `ludwig/datasets/configs/adult_census_income.yaml` (config)
- `ludwig/datasets/configs/adult_income_hf.yaml` (config)
- `ludwig/datasets/configs/ae_price_prediction.yaml` (config)
- `ludwig/datasets/configs/aegis_safety.yaml` (config)
- `ludwig/datasets/configs/aeslc.yaml` (config)
- `ludwig/datasets/configs/ag_news_hf.yaml` (config)
- `ludwig/datasets/configs/agnews.yaml` (config)
- `ludwig/datasets/configs/ai2d_diagrams.yaml` (config)
- `ludwig/datasets/configs/ai_generated_ecommerce.yaml` (config)
- `ludwig/datasets/configs/allocine.yaml` (config)
- `ludwig/datasets/configs/allstate_claims_severity.yaml` (config)
- `ludwig/datasets/configs/alpaca.yaml` (config)
- `ludwig/datasets/configs/alpaca_cleaned.yaml` (config)
- `ludwig/datasets/configs/alpaca_gpt4.yaml` (config)
- `ludwig/datasets/configs/alpaca_gpt4_zh.yaml` (config)
- `ludwig/datasets/configs/amazon_employee_access_challenge.yaml` (config)
- `ludwig/datasets/configs/amazon_massive_intent.yaml` (config)
- `ludwig/datasets/configs/amazon_massive_scenario.yaml` (config)
- `ludwig/datasets/configs/amazon_polarity.yaml` (config)
- `ludwig/datasets/configs/amazon_review_polarity.yaml` (config)
- `ludwig/datasets/configs/amazon_reviews.yaml` (config)
- `ludwig/datasets/configs/amazon_reviews_2023.yaml` (config)
- `ludwig/datasets/configs/amazon_science_massive.yaml` (config)
- `ludwig/datasets/configs/ambig_qa.yaml` (config)
- `ludwig/datasets/configs/ames_housing.yaml` (config)
- `ludwig/datasets/configs/ami_asr.yaml` (config)
- `ludwig/datasets/configs/anli.yaml` (config)
- `ludwig/datasets/configs/app_reviews.yaml` (config)
- `ludwig/datasets/configs/aqua_rat.yaml` (config)
- `ludwig/datasets/configs/arc_challenge.yaml` (config)
- `ludwig/datasets/configs/arc_easy.yaml` (config)
- `ludwig/datasets/configs/arxiv_abstracts_2021.yaml` (config)
- `ludwig/datasets/configs/arxiv_summarization.yaml` (config)
- `ludwig/datasets/configs/audioset_balanced.yaml` (config)
- `ludwig/datasets/configs/banking77.yaml` (config)
- `ludwig/datasets/configs/banking77_legacy.yaml` (config)
- `ludwig/datasets/configs/bbcnews.yaml` (config)
- `ludwig/datasets/configs/bbh.yaml` (config)
- `ludwig/datasets/configs/beans.yaml` (config)
- `ludwig/datasets/configs/beavertails.yaml` (config)
- `ludwig/datasets/configs/belebele.yaml` (config)
- `ludwig/datasets/configs/belebele_fr.yaml` (config)
- `ludwig/datasets/configs/big_patent.yaml` (config)
- `ludwig/datasets/configs/bigbench.yaml` (config)
- `ludwig/datasets/configs/billsum.yaml` (config)
- `ludwig/datasets/configs/bitext_customer_intent.yaml` (config)
- `ludwig/datasets/configs/bitext_customer_support.yaml` (config)
- `ludwig/datasets/configs/blimp.yaml` (config)
- `ludwig/datasets/configs/bnp_claims_management.yaml` (config)
- `ludwig/datasets/configs/bookprice_prediction.yaml` (config)
- `ludwig/datasets/configs/boolq.yaml` (config)
- `ludwig/datasets/configs/boolq_standalone.yaml` (config)
- `ludwig/datasets/configs/bornholm_bitext.yaml` (config)
- `ludwig/datasets/configs/brazilian_toxic_tweets.yaml` (config)
- `ludwig/datasets/configs/california_house_price.yaml` (config)
- `ludwig/datasets/configs/california_housing.yaml` (config)
- `ludwig/datasets/configs/camseq.yaml` (config)
- `ludwig/datasets/configs/cantonese_asr.yaml` (config)
- `ludwig/datasets/configs/ccnews.yaml` (config)
- `ludwig/datasets/configs/cifar10.yaml` (config)
- `ludwig/datasets/configs/cifar100.yaml` (config)
- `ludwig/datasets/configs/civil_comments.yaml` (config)
- `ludwig/datasets/configs/climate_fever.yaml` (config)
- `ludwig/datasets/configs/climate_sentiment.yaml` (config)
- `ludwig/datasets/configs/clinc_oos.yaml` (config)
- `ludwig/datasets/configs/clue_afqmc.yaml` (config)
- `ludwig/datasets/configs/cmrc2018.yaml` (config)
- `ludwig/datasets/configs/cnn_dailymail.yaml` (config)
- `ludwig/datasets/configs/cnn_dm_hf.yaml` (config)
- `ludwig/datasets/configs/code_alpaca.yaml` (config)
- `ludwig/datasets/configs/code_contests.yaml` (config)
- `ludwig/datasets/configs/code_defect_detection.yaml` (config)
- `ludwig/datasets/configs/code_search_net.yaml` (config)
- `ludwig/datasets/configs/codex_thinking.yaml` (config)
- `ludwig/datasets/configs/codexglue_code_to_text.yaml` (config)
- `ludwig/datasets/configs/coig_cqia.yaml` (config)
- `ludwig/datasets/configs/cola.yaml` (config)
- `ludwig/datasets/configs/commitment_bank.yaml` (config)
- `ludwig/datasets/configs/commonsense_qa.yaml` (config)
- `ludwig/datasets/configs/compas_recidivism.yaml` (config)
- `ludwig/datasets/configs/connect4.yaml` (config)
- `ludwig/datasets/configs/consumer_complaints.yaml` (config)
- `ludwig/datasets/configs/copa.yaml` (config)
- `ludwig/datasets/configs/cord_v2.yaml` (config)
- `ludwig/datasets/configs/credit_card_default.yaml` (config)
- `ludwig/datasets/configs/creditcard_fraud.yaml` (config)
- `ludwig/datasets/configs/customer_churn_prediction.yaml` (config)
- `ludwig/datasets/configs/customer_reviews.yaml` (config)
- `ludwig/datasets/configs/dair_emotion.yaml` (config)
- `ludwig/datasets/configs/data_scientist_salary.yaml` (config)
- `ludwig/datasets/configs/databench_qa.yaml` (config)
- `ludwig/datasets/configs/databricks_dolly_15k.yaml` (config)
- `ludwig/datasets/configs/dbpedia.yaml` (config)
- `ludwig/datasets/configs/dbpedia_14.yaml` (config)
- `ludwig/datasets/configs/diabetes_readmission.yaml` (config)
- `ludwig/datasets/configs/dialogsum.yaml` (config)
- `ludwig/datasets/configs/docvqa.yaml` (config)
- `ludwig/datasets/configs/dolly_15k.yaml` (config)
- `ludwig/datasets/configs/drop.yaml` (config)
- `ludwig/datasets/configs/duorc.yaml` (config)
- `ludwig/datasets/configs/electricity.yaml` (config)
- `ludwig/datasets/configs/electricity_tabular.yaml` (config)
- `ludwig/datasets/configs/emodb.yaml` (config)
- `ludwig/datasets/configs/emotion.yaml` (config)
- `ludwig/datasets/configs/enron_spam.yaml` (config)
- `ludwig/datasets/configs/esc50.yaml` (config)
- `ludwig/datasets/configs/europarl_bg_cs.yaml` (config)
- `ludwig/datasets/configs/europarl_bg_en.yaml` (config)
- `ludwig/datasets/configs/europarl_cs_en.yaml` (config)
- `ludwig/datasets/configs/europarl_da_en.yaml` (config)
- `ludwig/datasets/configs/europarl_de_en.yaml` (config)
- `ludwig/datasets/configs/europarl_el_en.yaml` (config)
- `ludwig/datasets/configs/europarl_en_es.yaml` (config)
- `ludwig/datasets/configs/europarl_en_fr.yaml` (config)
- `ludwig/datasets/configs/europarl_en_it.yaml` (config)
- `ludwig/datasets/configs/europarl_en_nl.yaml` (config)
- `ludwig/datasets/configs/europarl_en_pl.yaml` (config)
- `ludwig/datasets/configs/europarl_en_pt.yaml` (config)
- `ludwig/datasets/configs/europarl_en_ro.yaml` (config)
- `ludwig/datasets/configs/europarl_en_sv.yaml` (config)
- `ludwig/datasets/configs/eurosat.yaml` (config)
- `ludwig/datasets/configs/eurosat_rgb.yaml` (config)
- `ludwig/datasets/configs/factcheck.yaml` (config)
- `ludwig/datasets/configs/fake_job_postings2.yaml` (config)
- `ludwig/datasets/configs/fake_news_detection.yaml` (config)
- `ludwig/datasets/configs/farstail_nli.yaml` (config)
- `ludwig/datasets/configs/fashion_mnist.yaml` (config)
- `ludwig/datasets/configs/fever.yaml` (config)
- `ludwig/datasets/configs/fever_gold.yaml` (config)
- `ludwig/datasets/configs/few_nerd.yaml` (config)
- `ludwig/datasets/configs/financial_phrasebank.yaml` (config)
- `ludwig/datasets/configs/fineweb_edu.yaml` (config)
- `ludwig/datasets/configs/flashrag_2wikimultihop.yaml` (config)
- `ludwig/datasets/configs/flickr8k.yaml` (config)
- `ludwig/datasets/configs/flores_101.yaml` (config)
- `ludwig/datasets/configs/food101.yaml` (config)
- `ludwig/datasets/configs/forest_cover.yaml` (config)
- `ludwig/datasets/configs/gaia_cepheids.yaml` (config)
- `ludwig/datasets/configs/gaia_rrlyrae.yaml` (config)
- `ludwig/datasets/configs/gaia_spectroscopic_binaries.yaml` (config)
- `ludwig/datasets/configs/gaia_young_stellar_objects.yaml` (config)
- `ludwig/datasets/configs/gaiasky_qa.yaml` (config)
- `ludwig/datasets/configs/germeval18.yaml` (config)
- `ludwig/datasets/configs/go_emotions.yaml` (config)
- `ludwig/datasets/configs/go_emotions_multiclass.yaml` (config)
- `ludwig/datasets/configs/goemotions.yaml` (config)
- `ludwig/datasets/configs/goodbooks_books.yaml` (config)
- `ludwig/datasets/configs/google_qa_answer_type_reason_explanation.yaml` (config)
- `ludwig/datasets/configs/google_qa_question_type_reason_explanation.yaml` (config)
- `ludwig/datasets/configs/google_quest_qa.yaml` (config)
- `ludwig/datasets/configs/govreport_summarization.yaml` (config)
- `ludwig/datasets/configs/graid_bdd.yaml` (config)
- `ludwig/datasets/configs/gsm8k.yaml` (config)
- `ludwig/datasets/configs/gsm8k_openai.yaml` (config)
- `ludwig/datasets/configs/gtsrb.yaml` (config)
- `ludwig/datasets/configs/handwritten_crossouts.yaml` (config)
- `ludwig/datasets/configs/hate_speech18.yaml` (config)
- `ludwig/datasets/configs/hatespeech_offensive.yaml` (config)
- `ludwig/datasets/configs/hc3.yaml` (config)
- `ludwig/datasets/configs/hc3_chinese.yaml` (config)
- `ludwig/datasets/configs/heart_failure.yaml` (config)
- `ludwig/datasets/configs/hellaswag.yaml` (config)
- `ludwig/datasets/configs/helpsteer2.yaml` (config)
- `ludwig/datasets/configs/hermes_function_calling.yaml` (config)
- `ludwig/datasets/configs/hh_rlhf.yaml` (config)
- `ludwig/datasets/configs/higgs.yaml` (config)
- `ludwig/datasets/configs/hotpot_qa.yaml` (config)
- `ludwig/datasets/configs/hugging_face.yaml` (config)
- `ludwig/datasets/configs/ieee_fraud.yaml` (config)
- `ludwig/datasets/configs/imagenet_100.yaml` (config)
- `ludwig/datasets/configs/imbalanced_insurance.yaml` (config)
- `ludwig/datasets/configs/imdb.yaml` (config)
- `ludwig/datasets/configs/imdb_genre_prediction.yaml` (config)
- `ludwig/datasets/configs/imdb_mteb.yaml` (config)
- `ludwig/datasets/configs/imdb_sentiment.yaml` (config)
- `ludwig/datasets/configs/indic_glue.yaml` (config)
- `ludwig/datasets/configs/insurance_lite.yaml` (config)
- `ludwig/datasets/configs/intuitive_physics.yaml` (config)
- `ludwig/datasets/configs/invoice_data.yaml` (config)
- `ludwig/datasets/configs/iris.yaml` (config)
- `ludwig/datasets/configs/iris_sklearn.yaml` (config)
- `ludwig/datasets/configs/irony.yaml` (config)
- `ludwig/datasets/configs/jc_penney_products.yaml` (config)
- `ludwig/datasets/configs/jigsaw_unintended_bias.yaml` (config)
- `ludwig/datasets/configs/jigsaw_unintended_bias100k.yaml` (config)
- `ludwig/datasets/configs/kdd_appetency.yaml` (config)
- `ludwig/datasets/configs/kdd_churn.yaml` (config)
- `ludwig/datasets/configs/kdd_upselling.yaml` (config)
- `ludwig/datasets/configs/kick_starter_funding.yaml` (config)
- `ludwig/datasets/configs/kilt_nq.yaml` (config)
- `ludwig/datasets/configs/klue_sts.yaml` (config)
- `ludwig/datasets/configs/klue_topic.yaml` (config)
- `ludwig/datasets/configs/kmmlu.yaml` (config)
- `ludwig/datasets/configs/kvasir_vqa.yaml` (config)
- `ludwig/datasets/configs/language_identification.yaml` (config)
- `ludwig/datasets/configs/lex_glue_ecthr.yaml` (config)
- `ludwig/datasets/configs/lex_glue_eurlex.yaml` (config)
- `ludwig/datasets/configs/librispeech.yaml` (config)
- `ludwig/datasets/configs/lmsys_arena.yaml` (config)
- `ludwig/datasets/configs/m3cot.yaml` (config)
- `ludwig/datasets/configs/m_mmlu.yaml` (config)
- `ludwig/datasets/configs/map_trace.yaml` (config)
- `ludwig/datasets/configs/math500.yaml` (config)
- `ludwig/datasets/configs/mathvista.yaml` (config)
- `ludwig/datasets/configs/mbpp.yaml` (config)
- `ludwig/datasets/configs/measuring_hate_speech.yaml` (config)
- `ludwig/datasets/configs/medical_flashcards.yaml` (config)
- `ludwig/datasets/configs/medmcqa.yaml` (config)
- `ludwig/datasets/configs/melbourne_airbnb.yaml` (config)
- `ludwig/datasets/configs/mercari_price_suggestion.yaml` (config)
- `ludwig/datasets/configs/mercari_price_suggestion100K.yaml` (config)
- `ludwig/datasets/configs/mercedes_benz_greener.yaml` (config)
- `ludwig/datasets/configs/merit.yaml` (config)
- `ludwig/datasets/configs/minds14.yaml` (config)
- `ludwig/datasets/configs/mini_imagenet.yaml` (config)
- `ludwig/datasets/configs/mls_german.yaml` (config)
- `ludwig/datasets/configs/mmlu.yaml` (config)
- `ludwig/datasets/configs/mmlu_lighteval.yaml` (config)
- `ludwig/datasets/configs/mmlu_pro.yaml` (config)
- `ludwig/datasets/configs/mmsulab.yaml` (config)
- `ludwig/datasets/configs/mnist.yaml` (config)
- `ludwig/datasets/configs/mnist_ylecun.yaml` (config)
- `ludwig/datasets/configs/mnli.yaml` (config)
- `ludwig/datasets/configs/mobile_mold.yaml` (config)
- `ludwig/datasets/configs/moral_stories.yaml` (config)
- `ludwig/datasets/configs/mrpc.yaml` (config)
- `ludwig/datasets/configs/msmarco_passage.yaml` (config)
- `ludwig/datasets/configs/mteb_amazon_polarity.yaml` (config)
- `ludwig/datasets/configs/mteb_amazon_reviews_class_de.yaml` (config)
- `ludwig/datasets/configs/mteb_amazon_reviews_class_en.yaml` (config)
- `ludwig/datasets/configs/mteb_amazon_reviews_class_es.yaml` (config)
- `ludwig/datasets/configs/mteb_amazon_reviews_class_fr.yaml` (config)
- `ludwig/datasets/configs/mteb_amazon_reviews_class_ja.yaml` (config)
- `ludwig/datasets/configs/mteb_amazon_reviews_class_zh.yaml` (config)
- `ludwig/datasets/configs/mteb_biosses.yaml` (config)
- `ludwig/datasets/configs/mteb_cyrillic_turkic.yaml` (config)
- `ludwig/datasets/configs/mteb_emotion.yaml` (config)
- `ludwig/datasets/configs/mteb_financial_phrasebank.yaml` (config)
- `ludwig/datasets/configs/mteb_frenk_en.yaml` (config)
- `ludwig/datasets/configs/mteb_frenk_hr.yaml` (config)
- `ludwig/datasets/configs/mteb_frenk_sl.yaml` (config)
- `ludwig/datasets/configs/mteb_georeview.yaml` (config)
- `ludwig/datasets/configs/mteb_greek_legal.yaml` (config)
- `ludwig/datasets/configs/mteb_imdb.yaml` (config)
- `ludwig/datasets/configs/mteb_ita_casehold.yaml` (config)
- `ludwig/datasets/configs/mteb_jd_review.yaml` (config)
- `ludwig/datasets/configs/mteb_kor_sarcasm.yaml` (config)
- `ludwig/datasets/configs/mteb_language_class.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_af.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_am.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_ar.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_az.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_bn.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_cy.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_da.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_de.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_el.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_en.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_es.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_fa.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_fi.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_fr.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_he.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_hi.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_hu.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_hy.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_id.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_is.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_it.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_ja.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_jv.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_ka.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_km.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_kn.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_ko.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_lv.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_ml.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_mn.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_ms.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_my.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_nb.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_nl.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_pl.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_pt.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_ro.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_ru.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_sl.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_sq.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_sv.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_sw.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_ta.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_te.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_th.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_tl.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_tr.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_ur.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_vi.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_zh_cn.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_intent_zh_tw.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_af.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_am.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_ar.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_az.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_bn.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_cy.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_da.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_de.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_el.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_en.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_es.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_fa.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_fi.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_fr.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_he.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_hi.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_hu.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_hy.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_id.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_is.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_it.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_ja.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_jv.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_ka.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_km.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_kn.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_ko.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_lv.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_ml.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_mn.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_ms.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_my.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_nb.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_nl.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_pl.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_pt.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_ro.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_ru.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_sl.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_sq.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_sv.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_sw.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_ta.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_te.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_th.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_tl.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_tr.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_ur.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_vi.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_zh_cn.yaml` (config)
- `ludwig/datasets/configs/mteb_massive_scenario_zh_tw.yaml` (config)
- `ludwig/datasets/configs/mteb_mtop_domain_de.yaml` (config)
- `ludwig/datasets/configs/mteb_mtop_domain_en.yaml` (config)
- `ludwig/datasets/configs/mteb_mtop_domain_es.yaml` (config)
- `ludwig/datasets/configs/mteb_mtop_domain_fr.yaml` (config)
- `ludwig/datasets/configs/mteb_mtop_domain_hi.yaml` (config)
- `ludwig/datasets/configs/mteb_mtop_domain_th.yaml` (config)
- `ludwig/datasets/configs/mteb_mtop_intent_de2.yaml` (config)
- `ludwig/datasets/configs/mteb_mtop_intent_en.yaml` (config)
- `ludwig/datasets/configs/mteb_mtop_intent_es2.yaml` (config)
- `ludwig/datasets/configs/mteb_mtop_intent_fr2.yaml` (config)
- `ludwig/datasets/configs/mteb_mtop_intent_hi2.yaml` (config)
- `ludwig/datasets/configs/mteb_mtop_intent_th2.yaml` (config)
- `ludwig/datasets/configs/mteb_multilingual_sentiment.yaml` (config)
- `ludwig/datasets/configs/mteb_naija_senti_hau.yaml` (config)
- `ludwig/datasets/configs/mteb_naija_senti_ibo.yaml` (config)
- `ludwig/datasets/configs/mteb_naija_senti_pcm.yaml` (config)
- `ludwig/datasets/configs/mteb_naija_senti_yor.yaml` (config)
- `ludwig/datasets/configs/mteb_nepali_news.yaml` (config)
- `ludwig/datasets/configs/mteb_nordic_lang.yaml` (config)
- `ludwig/datasets/configs/mteb_online_shopping.yaml` (config)
- `ludwig/datasets/configs/mteb_poem_sentiment.yaml` (config)
- `ludwig/datasets/configs/mteb_sensitive_topics.yaml` (config)
- `ludwig/datasets/configs/mteb_sentiment_hindi.yaml` (config)
- `ludwig/datasets/configs/mteb_sts17_ar.yaml` (config)
- `ludwig/datasets/configs/mteb_sts17_de.yaml` (config)
- `ludwig/datasets/configs/mteb_sts17_en.yaml` (config)
- `ludwig/datasets/configs/mteb_sts17_es.yaml` (config)
- `ludwig/datasets/configs/mteb_sts17_fr.yaml` (config)
- `ludwig/datasets/configs/mteb_sts22_ar.yaml` (config)
- `ludwig/datasets/configs/mteb_sts22_de.yaml` (config)
- `ludwig/datasets/configs/mteb_sts22_de_en.yaml` (config)
- `ludwig/datasets/configs/mteb_sts22_de_fr.yaml` (config)
- `ludwig/datasets/configs/mteb_sts22_en.yaml` (config)
- `ludwig/datasets/configs/mteb_sts22_es.yaml` (config)
- `ludwig/datasets/configs/mteb_sts22_es_en.yaml` (config)
- `ludwig/datasets/configs/mteb_sts22_es_it.yaml` (config)
- `ludwig/datasets/configs/mteb_sts22_fr.yaml` (config)
- `ludwig/datasets/configs/mteb_sts22_it.yaml` (config)
- `ludwig/datasets/configs/mteb_sts22_pl.yaml` (config)
- `ludwig/datasets/configs/mteb_sts22_pl_en.yaml` (config)
- `ludwig/datasets/configs/mteb_sts22_ru.yaml` (config)
- `ludwig/datasets/configs/mteb_sts22_tr.yaml` (config)
- `ludwig/datasets/configs/mteb_sts22_zh.yaml` (config)
- `ludwig/datasets/configs/mteb_sts22_zh_en.yaml` (config)
- `ludwig/datasets/configs/mteb_stsbenchmark.yaml` (config)
- `ludwig/datasets/configs/mteb_swiss_judgement_de.yaml` (config)
- `ludwig/datasets/configs/mteb_swiss_judgement_fr.yaml` (config)
- `ludwig/datasets/configs/mteb_swiss_judgement_it.yaml` (config)
- `ludwig/datasets/configs/mteb_tnews.yaml` (config)
- `ludwig/datasets/configs/mteb_toxic_convo.yaml` (config)
- `ludwig/datasets/configs/mteb_turkish_product.yaml` (config)
- `ludwig/datasets/configs/mteb_tweet_sentiment.yaml` (config)
- `ludwig/datasets/configs/mteb_tweet_topic.yaml` (config)
- `ludwig/datasets/configs/mteb_waimai.yaml` (config)
- `ludwig/datasets/configs/mteb_yahoo_answers.yaml` (config)
- `ludwig/datasets/configs/multi30k.yaml` (config)
- `ludwig/datasets/configs/multi_nli.yaml` (config)
- `ludwig/datasets/configs/multinerd.yaml` (config)
- `ludwig/datasets/configs/multirc.yaml` (config)
- `ludwig/datasets/configs/multiun_ar_en.yaml` (config)
- `ludwig/datasets/configs/mushroom_edibility.yaml` (config)
- `ludwig/datasets/configs/natural_questions.yaml` (config)
- `ludwig/datasets/configs/natural_questions_hard_negatives.yaml` (config)
- `ludwig/datasets/configs/naturelm_audio.yaml` (config)
- `ludwig/datasets/configs/naval.yaml` (config)
- `ludwig/datasets/configs/naver_news_summary.yaml` (config)
- `ludwig/datasets/configs/nemotron_pii.yaml` (config)
- `ludwig/datasets/configs/nemotron_safety.yaml` (config)
- `ludwig/datasets/configs/news_category.yaml` (config)
- `ludwig/datasets/configs/news_channel.yaml` (config)
- `ludwig/datasets/configs/news_popularity2.yaml` (config)
- `ludwig/datasets/configs/newyorker_caption_contest.yaml` (config)
- `ludwig/datasets/configs/nli_zh_all.yaml` (config)
- `ludwig/datasets/configs/no_robots.yaml` (config)
- `ludwig/datasets/configs/noshow_appointments.yaml` (config)
- `ludwig/datasets/configs/nq_open.yaml` (config)
- `ludwig/datasets/configs/numerai28pt6.yaml` (config)
- `ludwig/datasets/configs/numinamath.yaml` (config)
- `ludwig/datasets/configs/oasst1.yaml` (config)
- `ludwig/datasets/configs/ohsumed_7400.yaml` (config)
- `ludwig/datasets/configs/ohsumed_cmu.yaml` (config)
- `ludwig/datasets/configs/openbookqa.yaml` (config)
- `ludwig/datasets/configs/openfake.yaml` (config)
- `ludwig/datasets/configs/opus100_en_es.yaml` (config)
- `ludwig/datasets/configs/opus100_en_fr.yaml` (config)
- `ludwig/datasets/configs/opus_books_en_fr.yaml` (config)
- `ludwig/datasets/configs/or_bench.yaml` (config)
- `ludwig/datasets/configs/orca_dpo_pairs.yaml` (config)

## Top-level layout

- `ludwig` — 569 analysed file(s)
- `examples` — 190 analysed file(s)
- `(root files)` — 19 analysed file(s)
- `.github` — 9 analysed file(s)
- `docker` — 6 analysed file(s)
- `.claude` — 3 analysed file(s)
- `.devcontainer` — 2 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `docs` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `b16404c1e985a23f2b7c0246228c4fc85b7cf406` is the revision these paths and observations refer to.
