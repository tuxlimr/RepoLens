# Project structure: huggingface/peft

**Analysed commit:** `66a7c305bac9d7f8183b1f158280b77be971a3d4`

**Commit reference:** [66a7c305bac9d7f8183b1f158280b77be971a3d4](https://github.com/huggingface/peft/commit/66a7c305bac9d7f8183b1f158280b77be971a3d4)

**Tree at this commit:** [huggingface/peft@66a7c305bac9](https://github.com/huggingface/peft/tree/66a7c305bac9d7f8183b1f158280b77be971a3d4)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | huggingface/peft |
| Description | 🤗 PEFT: State-of-the-art Parameter-Efficient Fine-Tuning. |
| Stars | 21887 |
| Forks | 2668 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `66a7c305bac9d7f8183b1f158280b77be971a3d4` |
| Retrieved at | 2026-11-14T19:07:58.087912+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.ai/  (2 files)
  skills/  (1 files)
    peft-method-changes/  (1 files)
      … 1 files under this directory
  AGENTS.md
.github/  (22 files)
  ISSUE_TEMPLATE/  (2 files)
    bug-report.yml
    feature-request.yml
  workflows/  (17 files)
    build_docker_images.yml
    build_documentation.yml
    build_pr_documentation.yml
    deploy_method_comparison_app.yml
    deploy_peft_shop_app.yml
    integrations_tests.yml
    nightly.yml
    stale.yml
    test-docker-build.yml
    tests-main.yml
    tests.yml
    tests_macos.yml
    torch_compile_tests.yml
    triage_prs.yml
    trufflehog.yml
    upload_pr_documentation.yml
    zizmor.yaml
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
  zizmor.yml
docker/  (3 files)
  peft-cpu/  (1 files)
    Dockerfile
  peft-gpu/  (1 files)
    Dockerfile
  README.md
docs/  (87 files)
  source/  (85 files)
    accelerate/  (2 files)
      … 2 files under this directory
    developer_guides/  (10 files)
      … 10 files under this directory
    guides/  (2 files)
      … 2 files under this directory
    methods/  (1 files)
      … 1 files under this directory
    package_reference/  (64 files)
      … 64 files under this directory
    _config.py
    _redirects.yml
    _toctree.yml
    index.md
    install.md
    quicktour.md
  Makefile
  README.md
examples/  (227 files)
  KappaTune/  (2 files)
    README.md
    experiments_kappatune_peft.py
  adamss_finetuning/  (5 files)
    README.md
    glue_adamss_asa_example.py
    glue_adamss_asa_manual_example.py
    image_classification_adamss_asa.py
    test_adamss_quick.py
  alora_finetuning/  (2 files)
    README.md
    alora_finetuning.py
  arrow_multitask/  (2 files)
    arrow_phi3_mini.py
    requirements.txt
  astra_finetuning/  (4 files)
    README.md
    astra_finetuning.py
    datautils.py
    preprocess.py
  bdlora_finetuning/  (4 files)
    README.md
    bdlora_peft_demo.ipynb
    chat.py
    vllm_server.bash
  beft_finetuning/  (2 files)
    README.md
    beft_finetuning.py
  boft_controlnet/  (16 files)
    utils/  (7 files)
      … 7 files under this directory
    __init__.py
    boft_controlnet.md
    eval.py
    eval.sh
    requirements.txt
    test_controlnet.py
    test_controlnet.sh
    train_controlnet.py
    train_controlnet.sh
  boft_dreambooth/  (11 files)
    utils/  (4 files)
      … 4 files under this directory
    .gitignore
    __init__.py
    boft_dreambooth.md
    dreambooth_inference.ipynb
    requirements.txt
    train_dreambooth.py
    train_dreambooth.sh
  cartridge_self_study/  (6 files)
    README.md
    arxiv_synthesize.py
    arxiv_train.py
    requirements.txt
    synthesize.py
    train_distill.py
  causal_language_modeling/  (7 files)
    accelerate_ds_zero3_cpu_offload_config.yaml
    peft_ln_tuning_clm.ipynb
    peft_lora_clm_accelerate_ds_zero3_offload.py
    peft_lora_clm_with_additional_tokens.ipynb
    peft_prefix_tuning_clm.ipynb
    peft_prompt_tuning_clm.ipynb
    requirements.txt
  conditional_generation/  (11 files)
    accelerate_ds_zero3_cpu_offload_config.yaml
    multitask_prompt_tuning.ipynb
    peft_adalora_seq2seq.py
    peft_ia3_seq2seq.ipynb
    peft_lora_seq2seq.ipynb
    peft_lora_seq2seq_accelerate_ds_zero3_offload.py
    peft_lora_seq2seq_accelerate_fsdp.py
    peft_prefix_tuning_seq2seq.ipynb
    peft_prompt_tuning_seq2seq.ipynb
    peft_prompt_tuning_seq2seq_with_generate.ipynb
    requirements.txt
  corda_finetuning/  (4 files)
    README.md
    corda_finetuning.py
    datautils.py
    preprocess.py
  cpt_finetuning/  (2 files)
    README.md
    cpt_train_and_inference.ipynb
  deft_dreambooth/  (3 files)
    README.md
    deft_dreambooth_inference.ipynb
    train_dreambooth.py
  deft_finetuning/  (2 files)
    README.md
    deft_finetuning.py
  delora_finetuning/  (2 files)
    README.md
    delora_finetuning.py
  dna_language_models/  (1 files)
    dna_lm.ipynb
  dora_finetuning/  (3 files)
    README.md
    dora-caching.py
    dora_finetuning.py
  ephemeral_gpu_offloading/  (1 files)
    load_with_dora.py
  eva_finetuning/  (4 files)
    README.md
    eva_finetuning.py
    eva_finetuning_multi_accelerator.py
    utils.py
  evaluation/  (1 files)
    lora-lm-eval.ipynb
  feature_extraction/  (3 files)
    peft_lora_embedding_semantic_search.py
    peft_lora_embedding_semantic_similarity_inference.ipynb
    requirements.txt
  fp4_finetuning/  (1 files)
    finetune_fp4_opt_bnb_peft.py
  frod_finetuning/  (4 files)
    README.md
    frod_image_classification.py
    frod_text_classification.py
    requirements.txt
  glora_finetuning/  (2 files)
    README.md
    glora_finetuning.py
  gralora_finetuning/  (2 files)
    README.md
    gralora_finetuning.py
  hira_finetuning/  (2 files)
    README.md
    hira_finetuning.py
  hra_dreambooth/  (8 files)
    utils/  (4 files)
      … 4 files under this directory
    README.md
    requirements.txt
    train_dreambooth.py
    train_dreambooth.sh
  image_classification/  (1 files)
    README.md
  int8_training/  (5 files)
    config.yaml
    fine_tune_blip2_int8.py
    peft_adalora_whisper_large_training.py
    requirements.txt
    run_adalora_whisper_int8.sh
  kasa_finetuning/  (2 files)
    README.md
    kasa_finetuning.py
  lily_finetuning/  (2 files)
    README.md
    lily_finetuning.py
  loftq_finetuning/  (5 files)
    LoftQ_weight_replacement.ipynb
    README.md
    int8_correction.py
    quantize_save_load.py
    train_gsm8k_llama.py
  lora_dreambooth/  (5 files)
    colab_notebook.ipynb
    convert_kohya_ss_sd_lora_to_peft.py
    convert_peft_sd_lora_to_kohya_ss.py
    requirements.txt
    train_dreambooth.py
  lora_finetuning_transformer_engine/  (4 files)
    Dockerfile
    README.md
    lora_finetuning_te.py
    requirements.txt
  lora_ga_finetuning/  (2 files)
    README.md
    lora_ga_finetuning.py
  lorafa_finetune/  (2 files)
    README.md
    lorafa_finetuning.py
  mica_finetuning/  (2 files)
    README.md
    mica_finetuning.py
  miss_finetuning/  (2 files)
    README.md
    miss_finetuning.py
  monteclora_finetuning/  (1 files)
    sequence_classification_finetune_monteclora.py
  multi_adapter_examples/  (2 files)
    Lora_Merging.ipynb
    PEFT_Multi_LoRA_Inference.ipynb
  multilayer_perceptron/  (2 files)
    README.md
    multilayer_perceptron_lora.ipynb
  oft_dreambooth/  (1 files)
    train_dreambooth.py
  olora_finetuning/  (2 files)
    README.md
    olora_finetuning.py
  orthogonal_subspace_learning/  (3 files)
    README.md
    osf_continual_learning.py
    utils.py
  paca_finetuning/  (2 files)
    README.md
    paca_finetuning.py
  peanut_finetuning/  (2 files)
    README.md
    peanut_finetuning.py
  pissa_finetuning/  (3 files)
    README.md
    pissa_finetuning.py
    preprocess.py
  psoft_finetuning/  (2 files)
    README.md
    psoft_finetuning.py
  pvera/  (2 files)
    README.md
    confidence_interval_generation.py
  qalora_finetuning/  (2 files)
    README.md
    qalora_gptq_finetuning.py
  randlora_finetuning/  (2 files)
    README.md
    randlora_finetuning.py
  road_finetuning/  (2 files)
    README.md
    road_finetuning.py
  semantic_segmentation/  (1 files)
    README.md
  sequence_classification/  (14 files)
    C3A.ipynb
    FourierFT.ipynb
    LoRA-torchao-8bit-dynamic-activation.ipynb
    LoRA-torchao-8bit.ipynb
    LoRA.ipynb
    P_Tuning.ipynb
    Prompt_Tuning.ipynb
    VBLoRA.ipynb
    VeRA.ipynb
    peft_lora_relation_extraction.ipynb
    peft_lora_relation_extraction.py
    peft_no_lora_accelerate.py
    prefix_tuning.ipynb
    requirements.txt
  sft/  (18 files)
    configs/  (4 files)
      … 4 files under this directory
    README.md
    requirements.txt
    requirements_colab.txt
    requirements_xpu.txt
    run_peft.sh
    run_peft_deepspeed.sh
    run_peft_fsdp.sh
    run_peft_fsdp_gptq.sh
    run_peft_multigpu.sh
    run_peft_qlora_deepspeed_stage3.sh
    run_peft_qlora_fsdp.sh
    run_unsloth_peft.sh
    train.py
    utils.py
  shadow_finetuning/  (2 files)
    README.md
    shadow_finetuning.py
  shira_finetuning/  (2 files)
    README.md
    shira_finetuning.py
  stable_diffusion/  (3 files)
    convert_sd_adapter_to_peft.py
    inc_flux_lora_hpu.py
    train_dreambooth.py
  supertuning_finetuning/  (2 files)
    README.md
    supertuning_finetuning.py
  token_classification/  (2 files)
    peft_lora_ner.ipynb
    requirements.txt
  unilora_finetuning/  (2 files)
    README.md
    unilora_finetuning.py
  waveft_finetuning/  (2 files)
    README.md
    waveft_finetuning.py
  xlora/  (2 files)
    README.md
    xlora_inference_mistralrs.py
method_comparison/  (326 files)
  MetaMathQA/  (192 files)
    cancelled_results/  (1 files)
      … 1 files under this directory
    experiments/  (109 files)
      … 109 files under this directory
    results/  (73 files)
      … 73 files under this directory
    temporary_results/  (1 files)
      … 1 files under this directory
    Makefile
    README.md
    data.py
    default_training_params.json
    requirements.txt
    run.py
    run_with_jobs.py
    utils.py
  image-gen/  (111 files)
    cancelled_results/  (1 files)
      … 1 files under this directory
    experiments/  (58 files)
      … 58 files under this directory
    results/  (40 files)
      … 40 files under this directory
    sample-images/  (3 files)
      … 3 files under this directory
    temporary_results/  (1 files)
      … 1 files under this directory
    Makefile
    README.md
    data.py
    default_training_params.json
    evaluate.py
    requirements.txt
    run.py
    utils.py
  peft-shop/  (4 files)
    .gitignore
    README.md
    app.py
    requirements.txt
  text_generation_benchmark/  (11 files)
    cancelled_results/  (1 files)
      … 1 files under this directory
    configs/  (1 files)
      … 1 files under this directory
    experiments/  (1 files)
      … 1 files under this directory
    results/  (1 files)
      … 1 files under this directory
    temporary_results/  (1 files)
      … 1 files under this directory
    README.md
    data.py
    default_benchmark_params.json
    run.py
    run_base.py
    utils.py
  README.md
  __init__.py
  app.py
  app_embed.py
  processing.py
  requirements-app.txt
  sanitizer.py
  test_sanitizer.py
scripts/  (12 files)
  check_doc_coverage.py
  ci_clean_cache.py
  convert-bone-to-miss.py
  create-dummy-lora-for-hotswap.py
  evaluate-lora-conversion.py
  generate_method_capabilities.py
  launch_notebook_mp.py
  log_reports.py
  report_test_durations.py
  stale.py
  train_memory.py
  triage_prs.py
src/  (112 files)
  peft/  (112 files)
    optimizers/  (4 files)
      … 4 files under this directory
    tuners/  (97 files)
      … 97 files under this directory
    __init__.py
    auto.py
    config.py
    functional.py
    helpers.py
    import_utils.py
    mapping.py
    mapping_func.py
    mixed_model.py
    peft_model.py
    py.typed
.gitignore
.pre-commit-config.yaml
LICENSE
Makefile
README.md
SECURITY.md
pyproject.toml
requirements.txt
setup.py
```

## Entry points

- [method_comparison/MetaMathQA/run.py:532](https://github.com/huggingface/peft/blob/66a7c305bac9d7f8183b1f158280b77be971a3d4/method_comparison/MetaMathQA/run.py#L532)
- [method_comparison/image-gen/evaluate.py:265](https://github.com/huggingface/peft/blob/66a7c305bac9d7f8183b1f158280b77be971a3d4/method_comparison/image-gen/evaluate.py#L265)
- [method_comparison/image-gen/run.py:717](https://github.com/huggingface/peft/blob/66a7c305bac9d7f8183b1f158280b77be971a3d4/method_comparison/image-gen/run.py#L717)
- [method_comparison/peft-shop/app.py:1324](https://github.com/huggingface/peft/blob/66a7c305bac9d7f8183b1f158280b77be971a3d4/method_comparison/peft-shop/app.py#L1324)
- [method_comparison/text_generation_benchmark/run.py:357](https://github.com/huggingface/peft/blob/66a7c305bac9d7f8183b1f158280b77be971a3d4/method_comparison/text_generation_benchmark/run.py#L357)
- [method_comparison/text_generation_benchmark/run_base.py:185](https://github.com/huggingface/peft/blob/66a7c305bac9d7f8183b1f158280b77be971a3d4/method_comparison/text_generation_benchmark/run_base.py#L185)
- [scripts/check_doc_coverage.py:596](https://github.com/huggingface/peft/blob/66a7c305bac9d7f8183b1f158280b77be971a3d4/scripts/check_doc_coverage.py#L596)
- [scripts/ci_clean_cache.py:45](https://github.com/huggingface/peft/blob/66a7c305bac9d7f8183b1f158280b77be971a3d4/scripts/ci_clean_cache.py#L45)
- [scripts/convert-bone-to-miss.py:68](https://github.com/huggingface/peft/blob/66a7c305bac9d7f8183b1f158280b77be971a3d4/scripts/convert-bone-to-miss.py#L68)
- [scripts/create-dummy-lora-for-hotswap.py:58](https://github.com/huggingface/peft/blob/66a7c305bac9d7f8183b1f158280b77be971a3d4/scripts/create-dummy-lora-for-hotswap.py#L58)
- [scripts/evaluate-lora-conversion.py:135](https://github.com/huggingface/peft/blob/66a7c305bac9d7f8183b1f158280b77be971a3d4/scripts/evaluate-lora-conversion.py#L135)
- [scripts/generate_method_capabilities.py:768](https://github.com/huggingface/peft/blob/66a7c305bac9d7f8183b1f158280b77be971a3d4/scripts/generate_method_capabilities.py#L768)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 314 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: AdaLoraConfig, AdamssConfig, AdaptionPromptConfig, BOFTConfig, BeftConfig, C3AConfi… |
| Data layer | data | Observed | Groups 21 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AdaLoraModel, AdamssModel, AdaptionPromptModel, BOFTModel, BeftModel, C3AModel. Observed top-level fun… |
| Application entry point | entrypoint | Observed | Groups 19 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: AuxiliaryModulesTask, BenchmarkSpec, CategoryTask, Diagnostics, DummyGradScaler, ExtrasTa… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| method_comparison package | library | Observed | Groups 11 file(s) under method_comparison package (observed from repository paths and static analysis). Observed top-level classes: BenchmarkConfig, BenchmarkResult, BenchmarkStatus, BucketIterator, DummyScheduler, Meta… |
| peft package | library | Observed | Groups 67 file(s) under peft package (observed from repository paths and static analysis). Observed top-level classes: AdaLoraLayer, AdamssAsaCallback, AdamssLayer, AdaptedAttention, AdaptedAttentionGPT, AutoPeftModel.… |
| Tests | test | Observed | Groups 4 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: collate_fn, compute_metrics, df_products, main, preprocess_train, preprocess_val. |

## Important files

- `.github/ISSUE_TEMPLATE/bug-report.yml` (config)
- `.github/ISSUE_TEMPLATE/feature-request.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/build_docker_images.yml` (ci)
- `.github/workflows/build_documentation.yml` (ci)
- `.github/workflows/build_pr_documentation.yml` (ci)
- `.github/workflows/deploy_method_comparison_app.yml` (ci)
- `.github/workflows/deploy_peft_shop_app.yml` (ci)
- `.github/workflows/integrations_tests.yml` (ci)
- `.github/workflows/nightly.yml` (ci)
- `.github/workflows/stale.yml` (ci)
- `.github/workflows/test-docker-build.yml` (ci)
- `.github/workflows/tests-main.yml` (ci)
- `.github/workflows/tests.yml` (ci)
- `.github/workflows/tests_macos.yml` (ci)
- `.github/workflows/torch_compile_tests.yml` (ci)
- `.github/workflows/triage_prs.yml` (ci)
- `.github/workflows/trufflehog.yml` (ci)
- `.github/workflows/upload_pr_documentation.yml` (ci)
- `.github/workflows/zizmor.yaml` (ci)
- `.github/zizmor.yml` (config)
- `.pre-commit-config.yaml` (config)
- `docker/peft-cpu/Dockerfile` (container)
- `docker/peft-gpu/Dockerfile` (container)
- `docs/source/_redirects.yml` (config)
- `docs/source/_toctree.yml` (config)
- `examples/arrow_multitask/requirements.txt` (manifest)
- `examples/boft_controlnet/requirements.txt` (manifest)
- `examples/boft_dreambooth/requirements.txt` (manifest)
- `examples/cartridge_self_study/requirements.txt` (manifest)
- `examples/causal_language_modeling/accelerate_ds_zero3_cpu_offload_config.yaml` (config)
- `examples/causal_language_modeling/requirements.txt` (manifest)
- `examples/conditional_generation/accelerate_ds_zero3_cpu_offload_config.yaml` (config)
- `examples/conditional_generation/requirements.txt` (manifest)
- `examples/feature_extraction/requirements.txt` (manifest)
- `examples/frod_finetuning/requirements.txt` (manifest)
- `examples/hra_dreambooth/requirements.txt` (manifest)
- `examples/int8_training/config.yaml` (config)
- `examples/int8_training/requirements.txt` (manifest)
- `examples/lora_dreambooth/requirements.txt` (manifest)
- `examples/lora_finetuning_transformer_engine/Dockerfile` (container)
- `examples/lora_finetuning_transformer_engine/requirements.txt` (manifest)
- `examples/sequence_classification/requirements.txt` (manifest)
- `examples/sft/configs/deepspeed_config.yaml` (config)
- `examples/sft/configs/deepspeed_config_z3_qlora.yaml` (config)
- `examples/sft/configs/fsdp_config.yaml` (config)
- `examples/sft/configs/fsdp_config_qlora.yaml` (config)
- `examples/sft/requirements.txt` (manifest)
- `examples/sft/requirements_colab.txt` (manifest)
- `examples/sft/requirements_xpu.txt` (manifest)
- `examples/token_classification/requirements.txt` (manifest)
- `method_comparison/MetaMathQA/default_training_params.json` (config)
- `method_comparison/MetaMathQA/experiments/adalora/llama-3.2-3B-rank32/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/adamss/llama-3.2-3B-rank32/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/adamss/llama-3.2-3B-rank32/training_params.json` (config)
- `method_comparison/MetaMathQA/experiments/adaptionprompt/llama-3.2-3B-lr_0.0005/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/adaptionprompt/llama-3.2-3B-lr_0.0005/training_params.json` (config)
- `method_comparison/MetaMathQA/experiments/adaptionprompt/llama-3.2-3B-lr_5e-3/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/adaptionprompt/llama-3.2-3B-lr_5e-3/training_params.json` (config)
- `method_comparison/MetaMathQA/experiments/beft/llama-3.2-3B-target-v_proj/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/boft/llama-3.2-3B-default/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/c3a/llama-3.2-3B-default/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/c3a/llama-3.2-3B-default/training_params.json` (config)
- `method_comparison/MetaMathQA/experiments/deft/llama-3.2-3B-rank32-para/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/deft/llama-3.2-3B-rank32/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/delora/llama-3.2-3B-rank32/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/delora/llama-3.2-3B-rank32/training_params.json` (config)
- `method_comparison/MetaMathQA/experiments/fourierft/llama-3.2-3B-default/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/fourierft/llama-3.2-3B-n_frequency-5000/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/frod/llama-3.2-3B-default/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/frod/llama-3.2-3B-sparse0.02-lr_0.001/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/frod/llama-3.2-3B-sparse0.02-lr_0.001/training_params.json` (config)
- `method_comparison/MetaMathQA/experiments/full-finetuning/llama-3.2-3B-lr_0.00001/training_params.json` (config)
- `method_comparison/MetaMathQA/experiments/glora/llama-3.2-3B-default/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/glora/llama-3.2-3B-vector-paths/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/glora/llama-3.2-3B-vector-paths/training_params.json` (config)
- `method_comparison/MetaMathQA/experiments/gralora/llama-3.2-3B-rank32/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/gralora/llama-3.2-3B-rank32/training_params.json` (config)
- `method_comparison/MetaMathQA/experiments/hira/llama-3.2-3B-rank32-lr4.5e-3/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/hira/llama-3.2-3B-rank32-lr4.5e-3/training_params.json` (config)
- `method_comparison/MetaMathQA/experiments/hra/llama-3.2-3B-rank32/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/ia3/llama-3.2-3B-all-attn-5k-lr0.005/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/ia3/llama-3.2-3B-all-attn-5k-lr0.005/training_params.json` (config)
- `method_comparison/MetaMathQA/experiments/ia3/llama-3.2-3B-default/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/ia3/llama-3.2-3B-lr_0.001/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/ia3/llama-3.2-3B-lr_0.001/training_params.json` (config)
- `method_comparison/MetaMathQA/experiments/lily/llama-3.2-3B-rank140-mlp-a2-b2-s8.0/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/lily/llama-3.2-3B-rank896-a2-b2-s2.0/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/ln_tuning/llama-3.2-3B-default/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/loha/llama-3.2-3B-rank32/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/loha/llama-3.2-3B-rank32/training_params.json` (config)
- `method_comparison/MetaMathQA/experiments/lokr/llama-3.2-3B-rank32-factor4-lr0.003/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/lokr/llama-3.2-3B-rank32-factor4-lr0.003/training_params.json` (config)
- `method_comparison/MetaMathQA/experiments/lora/llama-3.2-3B-rank10-target-mlp-velora/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/lora/llama-3.2-3B-rank10-target-mlp/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/lora/llama-3.2-3B-rank14-target-mlp-bdlora/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/lora/llama-3.2-3B-rank32-dora/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/lora/llama-3.2-3B-rank32-kasa/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/lora/llama-3.2-3B-rank32-lorafa/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/lora/llama-3.2-3B-rank32-lorafa/training_params.json` (config)
- `method_comparison/MetaMathQA/experiments/lora/llama-3.2-3B-rank32-mica/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/lora/llama-3.2-3B-rank32-riemannian/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/lora/llama-3.2-3B-rank32-riemannian/training_params.json` (config)
- `method_comparison/MetaMathQA/experiments/lora/llama-3.2-3B-rank32/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/lora/llama-3.2-3B-rank64-rslora/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/lora/llama-3.2-3B-rank64/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/miss/llama-3.2-3B-bat/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/miss/llama-3.2-3B-default/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/miss/llama-3.2-3B-mini/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/oft/llama-3.2-3B-rank32/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/osf/llama-3.2-3B-rank128/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/osf/llama-3.2-3B-rank128/training_params.json` (config)
- `method_comparison/MetaMathQA/experiments/paca/llama-3.2-3B-rank32-all-linear-lr5e-4/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/paca/llama-3.2-3B-rank32-all-linear-lr5e-4/training_params.json` (config)
- `method_comparison/MetaMathQA/experiments/paca/llama-3.2-3B-rank80/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/peanut/llama-3.2-3B-rank1-relu-depth0-s32.0/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/peanut/llama-3.2-3B-rank32-relu-depth0-s2.0/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/prefixtuning/llama-3.2-3B-lr_0.001/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/prefixtuning/llama-3.2-3B-lr_0.001/training_params.json` (config)
- `method_comparison/MetaMathQA/experiments/prefixtuning/llama-3.2-3B-lr_0.005_zero_init/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/prefixtuning/llama-3.2-3B-lr_0.005_zero_init/training_params.json` (config)
- `method_comparison/MetaMathQA/experiments/prefixtuning/llama-3.2-3B-tokens50-init_prefix-lr_0.005/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/prefixtuning/llama-3.2-3B-tokens50-init_prefix-lr_0.005/training_params.json` (config)
- `method_comparison/MetaMathQA/experiments/prompt_tuning/llama-3.2-3B-default/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/prompt_tuning/llama-3.2-3B-lr_0.001/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/prompt_tuning/llama-3.2-3B-lr_0.001/training_params.json` (config)
- `method_comparison/MetaMathQA/experiments/prompt_tuning/llama-3.2-3B-sample_vocab-lr_0.001/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/prompt_tuning/llama-3.2-3B-sample_vocab-lr_0.001/training_params.json` (config)
- `method_comparison/MetaMathQA/experiments/psoft/llama-3.2-3B-default/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/psoft/llama-3.2-3B-fast/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/ptuning/llama-3.2-3B-default/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/pvera/llama-3.2-3B-default/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/pvera/llama-3.2-3B-default/training_params.json` (config)
- `method_comparison/MetaMathQA/experiments/pvera/llama-3.2-3B-rank64/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/pvera/llama-3.2-3B-rank64/training_params.json` (config)
- `method_comparison/MetaMathQA/experiments/randlora/llama-3.2-3B-default/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/road/llama-3.2-3B-lr_0.001/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/road/llama-3.2-3B-lr_0.001/training_params.json` (config)
- `method_comparison/MetaMathQA/experiments/shadow/llama-3.2-3B-mirror/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/shadow/llama-3.2-3B-mirror/training_params.json` (config)
- `method_comparison/MetaMathQA/experiments/shira/llama-3.2-3B-lr_0.0003-random_seed_42/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/shira/llama-3.2-3B-lr_0.0003-random_seed_42/training_params.json` (config)
- `method_comparison/MetaMathQA/experiments/supertuning/llama-3.2-3B-s974-topk/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/supertuning/llama-3.2-3B-s99-supra-r32/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/supertuning/llama-3.2-3B-s99-supra-r8/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/supertuning/llama-3.2-3B-s9935-bottomk/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/supertuning/llama-3.2-3B-s9935-topk/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/tinylora/llama-3.2-3B-default/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/tinylora/llama-3.2-3B-default/training_params.json` (config)
- `method_comparison/MetaMathQA/experiments/tinylora/llama-3.2-3B-weight-tying/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/tinylora/llama-3.2-3B-weight-tying/training_params.json` (config)
- `method_comparison/MetaMathQA/experiments/trainable_tokens/llama-3.2-3B-sos+eos/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/trainable_tokens/llama-3.2-3B-sos+eos/training_params.json` (config)
- `method_comparison/MetaMathQA/experiments/unilora/llama-3.2-3B-r4-td131072-lr0.002/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/unilora/llama-3.2-3B-r4-td131072-lr0.002/training_params.json` (config)
- `method_comparison/MetaMathQA/experiments/vblora/llama-3.2-3B-bank1024-lr5e4/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/vblora/llama-3.2-3B-bank1024-lr5e4/training_params.json` (config)
- `method_comparison/MetaMathQA/experiments/vblora/llama-3.2-3B-default/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/vera/llama-3.2-3B-default/adapter_config.json` (config)
- `method_comparison/MetaMathQA/experiments/vera/llama-3.2-3B-default/training_params.json` (config)
- `method_comparison/MetaMathQA/experiments/waveft/llama-3.2-3B-n_frequency-5000/adapter_config.json` (config)
- `method_comparison/MetaMathQA/requirements.txt` (manifest)
- `method_comparison/MetaMathQA/results/adalora--llama-3.2-3B-rank32.json` (config)
- `method_comparison/MetaMathQA/results/adamss--llama-3.2-3B-rank32.json` (config)
- `method_comparison/MetaMathQA/results/adaptionprompt--llama-3.2-3B-lr_0.0005.json` (config)
- `method_comparison/MetaMathQA/results/adaptionprompt--llama-3.2-3B-lr_5e-3.json` (config)
- `method_comparison/MetaMathQA/results/beft--llama-3.2-3B-target-v_proj.json` (config)
- `method_comparison/MetaMathQA/results/boft--llama-3.2-3B-default.json` (config)
- `method_comparison/MetaMathQA/results/c3a--llama-3.2-3B-default.json` (config)
- `method_comparison/MetaMathQA/results/deft--llama-3.2-3B-rank32-para.json` (config)
- `method_comparison/MetaMathQA/results/deft--llama-3.2-3B-rank32.json` (config)
- `method_comparison/MetaMathQA/results/delora--llama-3.2-3B-rank32.json` (config)
- `method_comparison/MetaMathQA/results/fourierft--llama-3.2-3B-default.json` (config)
- `method_comparison/MetaMathQA/results/fourierft--llama-3.2-3B-n_frequency-5000.json` (config)
- `method_comparison/MetaMathQA/results/frod--llama-3.2-3B-default.json` (config)
- `method_comparison/MetaMathQA/results/frod--llama-3.2-3B-sparse0.02-lr_0.001.json` (config)
- `method_comparison/MetaMathQA/results/full-finetuning--llama-3.2-3B-lr_0.00001.json` (config)
- `method_comparison/MetaMathQA/results/glora--llama-3.2-3B-default.json` (config)
- `method_comparison/MetaMathQA/results/glora--llama-3.2-3B-vector-paths.json` (config)
- `method_comparison/MetaMathQA/results/gralora--llama-3.2-3B-rank32.json` (config)
- `method_comparison/MetaMathQA/results/hira--llama-3.2-3B-rank32-lr4.5e-3.json` (config)
- `method_comparison/MetaMathQA/results/ia3--llama-3.2-3B-all-attn-5k-lr0.005.json` (config)
- `method_comparison/MetaMathQA/results/ia3--llama-3.2-3B-default.json` (config)
- `method_comparison/MetaMathQA/results/ia3--llama-3.2-3B-lr_0.001.json` (config)
- `method_comparison/MetaMathQA/results/lily--llama-3.2-3B-rank140-mlp-a2-b2-s8.0.json` (config)
- `method_comparison/MetaMathQA/results/lily--llama-3.2-3B-rank896-a2-b2-s2.0.json` (config)
- `method_comparison/MetaMathQA/results/ln_tuning--llama-3.2-3B-default.json` (config)
- `method_comparison/MetaMathQA/results/loha--llama-3.2-3B-rank32.json` (config)
- `method_comparison/MetaMathQA/results/lokr--llama-3.2-3B-rank32-factor4-lr0.003.json` (config)
- `method_comparison/MetaMathQA/results/lora--llama-3.2-3B-rank10-target-mlp.json` (config)
- `method_comparison/MetaMathQA/results/lora--llama-3.2-3B-rank14-target-mlp-bdlora.json` (config)
- `method_comparison/MetaMathQA/results/lora--llama-3.2-3B-rank32-dora.json` (config)
- `method_comparison/MetaMathQA/results/lora--llama-3.2-3B-rank32-kasa.json` (config)
- `method_comparison/MetaMathQA/results/lora--llama-3.2-3B-rank32-lorafa.json` (config)
- `method_comparison/MetaMathQA/results/lora--llama-3.2-3B-rank32-mica.json` (config)
- `method_comparison/MetaMathQA/results/lora--llama-3.2-3B-rank32-riemannian.json` (config)
- `method_comparison/MetaMathQA/results/lora--llama-3.2-3B-rank32.json` (config)
- `method_comparison/MetaMathQA/results/lora--llama-3.2-3B-rank64-rslora.json` (config)
- `method_comparison/MetaMathQA/results/lora--llama-3.2-3B-rank64.json` (config)
- `method_comparison/MetaMathQA/results/miss--llama-3.2-3B-bat.json` (config)
- `method_comparison/MetaMathQA/results/miss--llama-3.2-3B-default.json` (config)
- `method_comparison/MetaMathQA/results/miss--llama-3.2-3B-mini.json` (config)
- `method_comparison/MetaMathQA/results/oft--llama-3.2-3B-rank32.json` (config)
- `method_comparison/MetaMathQA/results/osf--llama-3.2-3B-rank128.json` (config)
- `method_comparison/MetaMathQA/results/peanut--llama-3.2-3B-rank1-relu-depth0-s32.0.json` (config)
- `method_comparison/MetaMathQA/results/peanut--llama-3.2-3B-rank32-relu-depth0-s2.0.json` (config)
- `method_comparison/MetaMathQA/results/prefixtuning--llama-3.2-3B-lr_0.001.json` (config)
- `method_comparison/MetaMathQA/results/prefixtuning--llama-3.2-3B-lr_0.005_zero_init.json` (config)
- `method_comparison/MetaMathQA/results/prefixtuning--llama-3.2-3B-tokens50-init_prefix-lr_0.005.json` (config)
- `method_comparison/MetaMathQA/results/prompt_tuning--llama-3.2-3B-default.json` (config)
- `method_comparison/MetaMathQA/results/prompt_tuning--llama-3.2-3B-lr_0.001.json` (config)
- `method_comparison/MetaMathQA/results/prompt_tuning--llama-3.2-3B-sample_vocab-lr_0.001.json` (config)
- `method_comparison/MetaMathQA/results/psoft--llama-3.2-3B-default.json` (config)
- `method_comparison/MetaMathQA/results/psoft--llama-3.2-3B-fast.json` (config)
- `method_comparison/MetaMathQA/results/ptuning--llama-3.2-3B-default.json` (config)
- `method_comparison/MetaMathQA/results/pvera--llama-3.2-3B-default.json` (config)
- `method_comparison/MetaMathQA/results/pvera--llama-3.2-3B-rank64.json` (config)
- `method_comparison/MetaMathQA/results/randlora--llama-3.2-3B-default.json` (config)
- `method_comparison/MetaMathQA/results/road--llama-3.2-3B-lr_0.001.json` (config)
- `method_comparison/MetaMathQA/results/shadow--llama-3.2-3B-mirror.json` (config)
- `method_comparison/MetaMathQA/results/shira--llama-3.2-3B-lr_0.0003-random_seed_42.json` (config)
- `method_comparison/MetaMathQA/results/supertuning--llama-3.2-3B-s974-topk.json` (config)
- `method_comparison/MetaMathQA/results/supertuning--llama-3.2-3B-s99-supra-r32.json` (config)
- `method_comparison/MetaMathQA/results/supertuning--llama-3.2-3B-s99-supra-r8.json` (config)
- `method_comparison/MetaMathQA/results/supertuning--llama-3.2-3B-s9935-bottomk.json` (config)
- `method_comparison/MetaMathQA/results/supertuning--llama-3.2-3B-s9935-topk.json` (config)
- `method_comparison/MetaMathQA/results/tinylora--llama-3.2-3B-default.json` (config)
- `method_comparison/MetaMathQA/results/tinylora--llama-3.2-3B-weight-tying.json` (config)
- `method_comparison/MetaMathQA/results/trainable_tokens--llama-3.2-3B-sos+eos.json` (config)
- `method_comparison/MetaMathQA/results/unilora--llama-3.2-3B-r4-td131072-lr0.002.json` (config)
- `method_comparison/MetaMathQA/results/vblora--llama-3.2-3B-bank1024-lr5e4.json` (config)
- `method_comparison/MetaMathQA/results/vblora--llama-3.2-3B-default.json` (config)
- `method_comparison/MetaMathQA/results/vera--llama-3.2-3B-default.json` (config)
- `method_comparison/MetaMathQA/results/waveft--llama-3.2-3B-n_frequency-5000.json` (config)
- `method_comparison/image-gen/default_training_params.json` (config)
- `method_comparison/image-gen/experiments/adalora/flux2-klein-default/adapter_config.json` (config)
- `method_comparison/image-gen/experiments/adamss/flux2-klein-default/adapter_config.json` (config)
- `method_comparison/image-gen/experiments/beft/flux2-klein-default/adapter_config.json` (config)
- `method_comparison/image-gen/experiments/boft/flux2-klein-default/adapter_config.json` (config)
- `method_comparison/image-gen/experiments/c3a/flux2-klein-default/adapter_config.json` (config)
- `method_comparison/image-gen/experiments/c3a/flux2-klein-default/training_params.json` (config)
- `method_comparison/image-gen/experiments/deft/flux2-klein-default/adapter_config.json` (config)
- `method_comparison/image-gen/experiments/deft/flux2-klein-para/adapter_config.json` (config)
- `method_comparison/image-gen/experiments/delora/flux2-klein-default/adapter_config.json` (config)
- `method_comparison/image-gen/experiments/delora/flux2-klein-default/training_params.json` (config)
- `method_comparison/image-gen/experiments/dora/flux2-klein-rank64/adapter_config.json` (config)
- `method_comparison/image-gen/experiments/fourierft/flux2-klein-default/adapter_config.json` (config)
- `method_comparison/image-gen/experiments/fourierft/flux2-klein-default/training_params.json` (config)
- `method_comparison/image-gen/experiments/frod/flux2-klein-default/adapter_config.json` (config)
- `method_comparison/image-gen/experiments/frod/flux2-klein-default/training_params.json` (config)
- `method_comparison/image-gen/experiments/full-finetuning/flux2-klein-default/training_params.json` (config)
- `method_comparison/image-gen/experiments/glora/flux2-klein-default/adapter_config.json` (config)
- `method_comparison/image-gen/experiments/gralora/flux2-klein-default/adapter_config.json` (config)
- `method_comparison/image-gen/experiments/hira/flux2-klein-default/adapter_config.json` (config)
- `method_comparison/image-gen/experiments/hira/flux2-klein-default/training_params.json` (config)
- `method_comparison/image-gen/experiments/hra/flux2-klein-default/adapter_config.json` (config)
- `method_comparison/image-gen/experiments/ia3/flux2-klein-default/adapter_config.json` (config)
- `method_comparison/image-gen/experiments/ia3/flux2-klein-default/training_params.json` (config)
- `method_comparison/image-gen/experiments/lily/flux2-klein-default/adapter_config.json` (config)
- `method_comparison/image-gen/experiments/ln_tuning/flux2-klein-default/adapter_config.json` (config)
- `method_comparison/image-gen/experiments/ln_tuning/flux2-klein-default/training_params.json` (config)
- `method_comparison/image-gen/experiments/loha/flux2-klein-default/adapter_config.json` (config)
- `method_comparison/image-gen/experiments/loha/flux2-klein-default/training_params.json` (config)
- `method_comparison/image-gen/experiments/lokr/flux2-klein-lr1e-3/adapter_config.json` (config)
- `method_comparison/image-gen/experiments/lokr/flux2-klein-lr1e-3/training_params.json` (config)
- `method_comparison/image-gen/experiments/lora/flux2-klein-bd-lora/adapter_config.json` (config)
- `method_comparison/image-gen/experiments/lora/flux2-klein-default/adapter_config.json` (config)
- `method_comparison/image-gen/experiments/lora/flux2-klein-monteclora/adapter_config.json` (config)
- `method_comparison/image-gen/experiments/lora/flux2-klein-rank64-kasa/adapter_config.json` (config)
- `method_comparison/image-gen/experiments/lora/flux2-klein-rank64/adapter_config.json` (config)
- `method_comparison/image-gen/experiments/lora/flux2-klein-velora/adapter_config.json` (config)
- `method_comparison/image-gen/experiments/miss/flux2-klein-default/adapter_config.json` (config)
- `method_comparison/image-gen/experiments/oft/flux2-klein-default/adapter_config.json` (config)
- `method_comparison/image-gen/experiments/osf/flux2-klein-default/adapter_config.json` (config)
- `method_comparison/image-gen/experiments/paca/flux2-klein-default/adapter_config.json` (config)
- `method_comparison/image-gen/experiments/peanut/flux2-klein-default/adapter_config.json` (config)
- `method_comparison/image-gen/experiments/psoft/flux2-klein-default/adapter_config.json` (config)
- `method_comparison/image-gen/experiments/pvera/flux2-klein-default/adapter_config.json` (config)
- `method_comparison/image-gen/experiments/pvera/flux2-klein-default/training_params.json` (config)
- `method_comparison/image-gen/experiments/randlora/flux2-klein-default/adapter_config.json` (config)
- `method_comparison/image-gen/experiments/road/flux2-klein-default/adapter_config.json` (config)
- `method_comparison/image-gen/experiments/road/flux2-klein-default/training_params.json` (config)
- `method_comparison/image-gen/experiments/shadow/flux2-klein-explicit/adapter_config.json` (config)
- `method_comparison/image-gen/experiments/shadow/flux2-klein-mirror/adapter_config.json` (config)
- `method_comparison/image-gen/experiments/shira/flux2-klein-default/adapter_config.json` (config)
- `method_comparison/image-gen/experiments/supertuning/flux2-klein-topk-lr3e-4/adapter_config.json` (config)
- `method_comparison/image-gen/experiments/supertuning/flux2-klein-topk-lr3e-4/training_params.json` (config)
- `method_comparison/image-gen/experiments/tinylora/flux2-klein-default/adapter_config.json` (config)
- `method_comparison/image-gen/experiments/unilora/flux2-klein-default/adapter_config.json` (config)
- `method_comparison/image-gen/experiments/vblora/flux2-klein-default/adapter_config.json` (config)
- `method_comparison/image-gen/experiments/vera/flux2-klein-default/adapter_config.json` (config)
- `method_comparison/image-gen/experiments/vera/flux2-klein-default/training_params.json` (config)
- `method_comparison/image-gen/experiments/waveft/flux2-klein-default/adapter_config.json` (config)
- `method_comparison/image-gen/requirements.txt` (manifest)
- `method_comparison/image-gen/results/adalora--flux2-klein-default.json` (config)
- `method_comparison/image-gen/results/adamss--flux2-klein-default.json` (config)
- `method_comparison/image-gen/results/beft--flux2-klein-default.json` (config)
- `method_comparison/image-gen/results/boft--flux2-klein-default.json` (config)
- `method_comparison/image-gen/results/c3a--flux2-klein-default.json` (config)
- `method_comparison/image-gen/results/deft--flux2-klein-default.json` (config)
- `method_comparison/image-gen/results/deft--flux2-klein-para.json` (config)
- `method_comparison/image-gen/results/delora--flux2-klein-default.json` (config)
- `method_comparison/image-gen/results/dora--flux2-klein-rank64.json` (config)
- `method_comparison/image-gen/results/fourierft--flux2-klein-default.json` (config)
- `method_comparison/image-gen/results/frod--flux2-klein-default.json` (config)
- `method_comparison/image-gen/results/full-finetuning--flux2-klein-default.json` (config)
- `method_comparison/image-gen/results/glora--flux2-klein-default.json` (config)
- `method_comparison/image-gen/results/gralora--flux2-klein-default.json` (config)
- `method_comparison/image-gen/results/hira--flux2-klein-default.json` (config)
- `method_comparison/image-gen/results/hra--flux2-klein-default.json` (config)
- `method_comparison/image-gen/results/ia3--flux2-klein-default.json` (config)
- `method_comparison/image-gen/results/lily--flux2-klein-default.json` (config)
- `method_comparison/image-gen/results/ln_tuning--flux2-klein-default.json` (config)
- `method_comparison/image-gen/results/loha--flux2-klein-default.json` (config)
- `method_comparison/image-gen/results/lokr--flux2-klein-lr1e-3.json` (config)
- `method_comparison/image-gen/results/lora--flux2-klein-default.json` (config)
- `method_comparison/image-gen/results/lora--flux2-klein-rank64-kasa.json` (config)
- `method_comparison/image-gen/results/lora--flux2-klein-rank64.json` (config)
- `method_comparison/image-gen/results/miss--flux2-klein-default.json` (config)
- `method_comparison/image-gen/results/oft--flux2-klein-default.json` (config)
- `method_comparison/image-gen/results/osf--flux2-klein-default.json` (config)
- `method_comparison/image-gen/results/peanut--flux2-klein-default.json` (config)
- `method_comparison/image-gen/results/psoft--flux2-klein-default.json` (config)
- `method_comparison/image-gen/results/pvera--flux2-klein-default.json` (config)
- `method_comparison/image-gen/results/randlora--flux2-klein-default.json` (config)
- `method_comparison/image-gen/results/road--flux2-klein-default.json` (config)
- `method_comparison/image-gen/results/shadow--flux2-klein-explicit.json` (config)
- `method_comparison/image-gen/results/shadow--flux2-klein-mirror.json` (config)
- `method_comparison/image-gen/results/shira--flux2-klein-default.json` (config)
- `method_comparison/image-gen/results/unilora--flux2-klein-default.json` (config)
- `method_comparison/image-gen/results/vblora--flux2-klein-default.json` (config)
- `method_comparison/image-gen/results/vera--flux2-klein-default.json` (config)
- `method_comparison/image-gen/results/waveft--flux2-klein-default.json` (config)
- `method_comparison/peft-shop/requirements.txt` (manifest)
- `method_comparison/requirements-app.txt` (manifest)
- `method_comparison/text_generation_benchmark/configs/prompts.json` (config)
- `method_comparison/text_generation_benchmark/default_benchmark_params.json` (config)
- `method_comparison/text_generation_benchmark/experiments/lora/lora_r8/adapter_config.json` (config)
- `pyproject.toml` (manifest)
- `requirements.txt` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `method_comparison` — 326 analysed file(s)
- `examples` — 227 analysed file(s)
- `src` — 112 analysed file(s)
- `docs` — 87 analysed file(s)
- `.github` — 22 analysed file(s)
- `scripts` — 12 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `docker` — 3 analysed file(s)
- `.ai` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `66a7c305bac9d7f8183b1f158280b77be971a3d4` is the revision these paths and observations refer to.
