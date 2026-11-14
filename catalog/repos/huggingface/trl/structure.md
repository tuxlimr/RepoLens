# Project structure: huggingface/trl

**Analysed commit:** `8ad18ec1b6493b85cf9fffbd87d376767ceb8611`

**Commit reference:** [8ad18ec1b6493b85cf9fffbd87d376767ceb8611](https://github.com/huggingface/trl/commit/8ad18ec1b6493b85cf9fffbd87d376767ceb8611)

**Tree at this commit:** [huggingface/trl@8ad18ec1b649](https://github.com/huggingface/trl/tree/8ad18ec1b6493b85cf9fffbd87d376767ceb8611)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | huggingface/trl |
| Description | Train transformer language models with reinforcement learning. |
| Stars | 19735 |
| Forks | 3145 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `8ad18ec1b6493b85cf9fffbd87d376767ceb8611` |
| Retrieved at | 2026-11-14T19:08:08.653245+00:00 |
| Files in this snapshot | 605 |

## Directory tree

```text
.agents/  (1 files)
  skills/  (1 files)
    update-paper-index/  (1 files)
      … 1 files under this directory
.ai/  (1 files)
  AGENTS.md
.github/  (29 files)
  ISSUE_TEMPLATE/  (3 files)
    bug-report.yml
    feature-request.yml
    new-trainer-addition.yml
  actions/  (1 files)
    post-slack/  (1 files)
      … 1 files under this directory
  codeql/  (1 files)
    custom-queries.qls
  workflows/  (20 files)
    build_documentation.yml
    build_pr_documentation.yml
    chat_templates_check.yml
    codeQL.yml
    docker-build-dev.yml
    docker-build.yml
    labeler.yml
    pr_template_check.yml
    publish.yml
    quality.yml
    sync-huggingface-skills.yml
    tests-experimental.yml
    tests.yml
    tests_latest.yml
    tests_python_versions.yml
    tests_transformers_branch.yml
    tests_vllm.yml
    trufflehog.yml
    upload_pr_documentation.yml
    version_check.yml
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
  labeler.yml
  release.yml
docker/  (2 files)
  trl/  (1 files)
    Dockerfile
  trl-dev/  (1 files)
    Dockerfile
docs/  (59 files)
  source/  (59 files)
    _redirects.yml
    _toctree.yml
    a2po_trainer.md
    amd_gpus.md
    async_distillation_trainer.md
    async_grpo_trainer.md
    aws_trainium.md
    bema_for_reference_model.md
    callbacks.md
    chat_template_utils.md
    chat_templates.md
    clis.md
    community_tutorials.md
    cpo_trainer.md
    customization.md
    data_utils.md
    dataset_formats.md
    deepspeed_integration.md
    distillation_trainer.md
    distributing_training.md
    dpo_trainer.md
    example_overview.md
    experimental_overview.md
    gkd_trainer.md
    … 35 more files
examples/  (105 files)
  async_distillation_math/  (1 files)
    async_distillation_math.py
  async_distillation_mopd/  (3 files)
    README.md
    async_distillation_mopd.py
    launcher.py
  async_grpo_harbor/  (3 files)
    README.md
    async_grpo_harbor.py
    launcher.py
  async_grpo_math/  (2 files)
    async_grpo_lora_math.py
    async_grpo_math.py
  datasets/  (11 files)
    chess_puzzles.py
    deepmath_103k.py
    hh-rlhf-helpful-base.py
    llava_instruct_mix.py
    lm-human-preferences-descriptiveness.py
    lm-human-preferences-sentiment.py
    rlaif-v.py
    tldr.py
    tldr_preference.py
    ultrafeedback-prompt.py
    ultrafeedback.py
  deepspeed_configs/  (3 files)
    zero1.json
    zero2.json
    zero3.json
  dpo_reduce_hallucinations/  (1 files)
    dpo_reduce_hallucinations.py
  fsdp_configs/  (1 files)
    fsdp2.json
  gold_chatbot_arena/  (1 files)
    gold_chatbot_arena.py
  gold_qwen3_vl/  (1 files)
    gold_qwen3_vl.py
  grpo_2048/  (1 files)
    grpo_2048.py
  grpo_browsergym/  (2 files)
    browsergym_llm.py
    grpo_browsergym.py
  grpo_carla/  (3 files)
    carla_vlm.py
    carla_vlm_gemma.py
    grpo_carla.py
  grpo_catch/  (1 files)
    grpo_catch.py
  grpo_continuous_batching/  (1 files)
    grpo_continuous_batching.py
  grpo_echo/  (1 files)
    grpo_echo.py
  grpo_harbor/  (12 files)
    harnesses/  (11 files)
      … 11 files under this directory
    grpo_harbor.py
  grpo_ministral3_vl/  (1 files)
    grpo_ministral3_vl.ipynb
  grpo_multi_env/  (1 files)
    grpo_multi_env.py
  grpo_qlora/  (1 files)
    grpo_qlora.ipynb
  grpo_qwen3_vl/  (1 files)
    grpo_qwen3_vl.ipynb
  grpo_rnj_1_instruct/  (1 files)
    grpo_rnj_1_instruct.ipynb
  grpo_seta/  (1 files)
    grpo_seta.py
  grpo_sql_agent/  (2 files)
    grpo_sql_agent.ipynb
    grpo_sql_agent.py
  grpo_sudoku/  (3 files)
    README.md
    grpo_sudoku.ipynb
    grpo_sudoku.py
  grpo_visual_math/  (1 files)
    grpo_visual_math.py
  grpo_wordle/  (2 files)
    grpo_wordle.ipynb
    grpo_wordle.py
  gspo_math/  (1 files)
    gspo_math.py
  gspo_visual_math/  (1 files)
    gspo_visual_math.py
  lfm2_5_moe_research_agent/  (5 files)
    1_sft.py
    2_evaluate.py
    3_grpo.py
    README.md
    wiki_library.py
  mpo_visual_preferences/  (1 files)
    mpo_visual_preferences.py
  online_dpo_visual_math/  (1 files)
    online_dpo_visual_math.py
  rloo_math/  (1 files)
    rloo_math.py
  rloo_visual_math/  (1 files)
    rloo_visual_math.py
  sdft_privileged_context/  (1 files)
    sdft_privileged_context.py
  sdpo_math/  (1 files)
    sdpo_math.py
  sft_agent_traces/  (4 files)
    README.md
    build_dataset.py
    rollouts.py
    sft.py
  sft_beam/  (2 files)
    sft_beam.py
    sft_beam.slurm
  sft_diffusion_gemma/  (1 files)
    sft_diffusion_gemma.py
  sft_gemma3/  (1 files)
    sft_gemma3.py
  sft_gemma3_vision/  (1 files)
    sft_gemma3_vision.py
  sft_gpt_oss_chess/  (3 files)
    README.md
    evaluate.py
    sft_gpt_oss_chess.py
  sft_mistral_large_4/  (2 files)
    sft_mistral_large_4.py
    sft_mistral_large_4.slurm
  sft_muse_spark_open/  (2 files)
    sft_muse_spark_open.py
    sft_muse_spark_open.slurm
  sft_nemotron_3/  (2 files)
    sft_nemotron_3.ipynb
    sft_nemotron_3.py
  sft_qlora/  (1 files)
    sft_qlora.ipynb
  sft_qwen3_8b_1m_context/  (1 files)
    sft_qwen3_8b_1m_context.py
  sft_tool_calling/  (3 files)
    sft_tiny_aya_tool_calling.py
    sft_tool_calling.ipynb
    tiny_aya_chat_template.jinja
  sft_visual_chat/  (1 files)
    sft_visual_chat.py
  tail_sft_gsm8k/  (1 files)
    tail_sft.py
  xtoken/  (4 files)
    build_projection_matrix.py
    reapply_exact_map.py
    sort_and_cut_projection_matrix.py
    xtoken.py
  README.md
scripts/  (88 files)
  generate_tiny_models/  (81 files)
    for_block_diffusion/  (2 files)
      … 2 files under this directory
    for_causal_lm/  (47 files)
      … 47 files under this directory
    for_conditional_generation/  (24 files)
      … 24 files under this directory
    for_sequence_classification/  (5 files)
      … 5 files under this directory
    README.md
    __init__.py
    _common.py
  add_copyrights.py
  check_chat_templates.py
  generate_harmony_dataset.py
  generate_toolcall_dataset.py
  generate_zen_dataset.py
  generate_zen_image_dataset.py
  generate_zen_multi_image_dataset.py
skills/  (1 files)
  trl-training/  (1 files)
    SKILL.md
tests/  (56 files)
  data/  (1 files)
    template.jinja
  distributed/  (5 files)
    data/  (3 files)
      … 3 files under this directory
    __init__.py
    test_distributed.py
  experimental/  (20 files)
    __init__.py
    _openreward_echo_env.py
    test_a2po_trainer.py
    test_async_distillation_trainer.py
    test_cpo_trainer.py
    test_gkd_trainer.py
    test_gmpo_trainer.py
    test_gold_trainer.py
    test_harbor.py
    test_iw_opd_trainer.py
    test_merge_model_callback.py
    test_online_dpo_trainer.py
    test_openenv_tito.py
    test_openreward.py
    test_orpo_trainer.py
    test_sdft_trainer.py
    test_sdpo_trainer.py
    test_self_distillation_trainer_behavior.py
    test_server_distillation_trainer.py
    test_utils.py
  invariant/  (6 files)
    references/  (3 files)
      … 3 files under this directory
    README.md
    __init__.py
    test_invariant.py
  __init__.py
  conftest.py
  test_activation_offloading.py
  test_callbacks.py
  test_chat_template_utils.py
  test_cli.py
  test_cli_utils.py
  test_data_utils.py
  test_distillation_trainer.py
  test_dpo_trainer.py
  test_examples_index.py
  test_kernels.py
  test_kto_trainer.py
  test_model_utils.py
  test_reward_trainer.py
  test_rewards.py
  test_rich_progress_callback.py
  test_rloo_trainer.py
  test_selective_activation_checkpointing.py
  test_sft_trainer.py
  test_utils.py
  test_vllm_client_server.py
  testing_constants.py
  testing_utils.py
trl/  (249 files)
  accelerate_configs/  (7 files)
    fsdp1.yaml
    fsdp2.yaml
    multi_gpu.yaml
    single_gpu.yaml
    zero1.yaml
    zero2.yaml
    zero3.yaml
  chat_templates/  (111 files)
    README.md
    cohere.jinja
    cohere2.jinja
    cohere2_training.jinja
    cohere_training.jinja
    deepseek_r1_distill.jinja
    deepseek_r1_distill_training.jinja
    deepseekv3.jinja
    deepseekv3_training.jinja
    deepseekv3_v2.jinja
    deepseekv3_v2_training.jinja
    deepseekv3_v3.jinja
    deepseekv3_v3_training.jinja
    deepseekv3_v4.jinja
    deepseekv3_v4_training.jinja
    diffusion_gemma.jinja
    diffusion_gemma_training.jinja
    gemma.jinja
    gemma3.jinja
    gemma3_training.jinja
    gemma4.jinja
    gemma4_v10.jinja
    gemma4_v2.jinja
    gemma4_v3.jinja
    … 87 more files
  cli/  (9 files)
    commands/  (5 files)
      … 5 files under this directory
    __init__.py
    accelerate_config.py
    accelerate_launcher.py
    main.py
  experimental/  (59 files)
    a2po/  (3 files)
      … 3 files under this directory
    async_distillation/  (6 files)
      … 6 files under this directory
    async_grpo/  (2 files)
      … 2 files under this directory
    bema_for_ref_model/  (3 files)
      … 3 files under this directory
    cpo/  (3 files)
      … 3 files under this directory
    distillation/  (1 files)
      … 1 files under this directory
    gkd/  (3 files)
      … 3 files under this directory
    gmpo/  (3 files)
      … 3 files under this directory
    gold/  (3 files)
      … 3 files under this directory
    harbor/  (3 files)
      … 3 files under this directory
    iw_opd/  (3 files)
      … 3 files under this directory
    kto/  (1 files)
      … 1 files under this directory
    online_dpo/  (3 files)
      … 3 files under this directory
    openreward/  (3 files)
      … 3 files under this directory
    orpo/  (3 files)
      … 3 files under this directory
    sdft/  (5 files)
      … 5 files under this directory
    sdpo/  (5 files)
      … 5 files under this directory
    server_distillation/  (3 files)
      … 3 files under this directory
    __init__.py
    merge_model_callback.py
    utils.py
  extras/  (2 files)
    __init__.py
    profiling.py
  generation/  (5 files)
    __init__.py
    async_vllm_client.py
    vllm_client.py
    vllm_generation.py
    weight_transfer.py
  kernels/  (5 files)
    __init__.py
    chunked_divergence.py
    chunked_logprob.py
    logprob_entropy.py
    tree_gated_delta_rule.py
  models/  (4 files)
    __init__.py
    activation_offloading.py
    selective_activation_checkpointing.py
    utils.py
  rewards/  (4 files)
    __init__.py
    accuracy_rewards.py
    format_rewards.py
    other_rewards.py
  scripts/  (12 files)
    __init__.py
    _hf_argparser.py
    distillation.py
    dpo.py
    env.py
    grpo.py
    kto.py
    reward.py
    rloo.py
    sft.py
    utils.py
    vllm_serve.py
  templates/  (3 files)
    completions_dataset_card.md
    lm_model_card.md
    rm_model_card.md
  trainer/  (20 files)
    __init__.py
    async_grpo_config.py
    base_config.py
    base_trainer.py
    callbacks.py
    distillation_config.py
    distillation_trainer.py
    dpo_config.py
    dpo_trainer.py
    grpo_config.py
    kto_config.py
    kto_trainer.py
    model_config.py
    reward_config.py
    reward_trainer.py
    rloo_config.py
    rloo_trainer.py
    sft_config.py
    sft_trainer.py
    utils.py
  __init__.py
  _compat.py
  _lazy_module.py
  chat_template_utils.py
  data_utils.py
  distributed.py
  import_utils.py
  py.typed
.gitignore
.pre-commit-config.yaml
CITATION.cff
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
MANIFEST.in
MIGRATION.md
Makefile
README.md
RELEASE.md
SECURITY.md
VERSION
pyproject.toml
```

## Entry points

- [scripts/add_copyrights.py:91](https://github.com/huggingface/trl/blob/8ad18ec1b6493b85cf9fffbd87d376767ceb8611/scripts/add_copyrights.py#L91)
- [scripts/check_chat_templates.py:141](https://github.com/huggingface/trl/blob/8ad18ec1b6493b85cf9fffbd87d376767ceb8611/scripts/check_chat_templates.py#L141)
- [scripts/generate_harmony_dataset.py:260](https://github.com/huggingface/trl/blob/8ad18ec1b6493b85cf9fffbd87d376767ceb8611/scripts/generate_harmony_dataset.py#L260)
- [scripts/generate_toolcall_dataset.py:337](https://github.com/huggingface/trl/blob/8ad18ec1b6493b85cf9fffbd87d376767ceb8611/scripts/generate_toolcall_dataset.py#L337)
- [scripts/generate_zen_dataset.py:589](https://github.com/huggingface/trl/blob/8ad18ec1b6493b85cf9fffbd87d376767ceb8611/scripts/generate_zen_dataset.py#L589)
- [scripts/generate_zen_image_dataset.py:343](https://github.com/huggingface/trl/blob/8ad18ec1b6493b85cf9fffbd87d376767ceb8611/scripts/generate_zen_image_dataset.py#L343)
- [scripts/generate_zen_multi_image_dataset.py:271](https://github.com/huggingface/trl/blob/8ad18ec1b6493b85cf9fffbd87d376767ceb8611/scripts/generate_zen_multi_image_dataset.py#L271)
- [trl/cli/__init__.py](https://github.com/huggingface/trl/blob/8ad18ec1b6493b85cf9fffbd87d376767ceb8611/trl/cli/__init__.py)
- [trl/cli/main.py:50](https://github.com/huggingface/trl/blob/8ad18ec1b6493b85cf9fffbd87d376767ceb8611/trl/cli/main.py#L50)
- [trl/generation/vllm_client.py:955](https://github.com/huggingface/trl/blob/8ad18ec1b6493b85cf9fffbd87d376767ceb8611/trl/generation/vllm_client.py#L955)
- [trl/scripts/distillation.py:154](https://github.com/huggingface/trl/blob/8ad18ec1b6493b85cf9fffbd87d376767ceb8611/trl/scripts/distillation.py#L154)
- [trl/scripts/dpo.py:148](https://github.com/huggingface/trl/blob/8ad18ec1b6493b85cf9fffbd87d376767ceb8611/trl/scripts/dpo.py#L148)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 11 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 4 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: NoOpManager, OffloadActivations, _ForwardRedirection. Observed top-level functions: _aten_attention_ops… |
| Application entry point | entrypoint | Observed | Groups 18 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: GRPOScriptArguments, RLOOScriptArguments, ScriptArguments, VLLMClient. Observed top-level… |
| External integrations | external | Observed | Groups 2 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: AsyncVLLMClient, VLLMClient. |
| scripts package | library | Observed | Groups 80 file(s) under scripts package (observed from repository paths and static analysis). Observed top-level classes: RemoteConfig, RemoteForCausalLM, RemoteForSequenceClassification, RemoteModel. Observed top-level… |
| Tests | test | Observed | Groups 56 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH sys.stdout, PATCH transformers.generation.utils.GenerationMixin.generate, PATCH sys.stdout, PATCH sys.stdout, PA… |
| trl package | library | Observed | Groups 110 file(s) under trl package (observed from repository paths and static analysis). Observed top-level classes: A2POConfig, A2POTrainer, AsyncDistillationConfig, AsyncDistillationTrainer, AsyncGRPOConfig, AsyncGR… |

## Important files

- `.github/ISSUE_TEMPLATE/bug-report.yml` (config)
- `.github/ISSUE_TEMPLATE/feature-request.yml` (config)
- `.github/ISSUE_TEMPLATE/new-trainer-addition.yml` (config)
- `.github/actions/post-slack/action.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/labeler.yml` (config)
- `.github/release.yml` (config)
- `.github/workflows/build_documentation.yml` (ci)
- `.github/workflows/build_pr_documentation.yml` (ci)
- `.github/workflows/chat_templates_check.yml` (ci)
- `.github/workflows/codeQL.yml` (ci)
- `.github/workflows/docker-build-dev.yml` (ci)
- `.github/workflows/docker-build.yml` (ci)
- `.github/workflows/labeler.yml` (ci)
- `.github/workflows/pr_template_check.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.github/workflows/quality.yml` (ci)
- `.github/workflows/sync-huggingface-skills.yml` (ci)
- `.github/workflows/tests-experimental.yml` (ci)
- `.github/workflows/tests.yml` (ci)
- `.github/workflows/tests_latest.yml` (ci)
- `.github/workflows/tests_python_versions.yml` (ci)
- `.github/workflows/tests_transformers_branch.yml` (ci)
- `.github/workflows/tests_vllm.yml` (ci)
- `.github/workflows/trufflehog.yml` (ci)
- `.github/workflows/upload_pr_documentation.yml` (ci)
- `.github/workflows/version_check.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `MANIFEST.in` (manifest)
- `docker/trl-dev/Dockerfile` (container)
- `docker/trl/Dockerfile` (container)
- `docs/source/_redirects.yml` (config)
- `docs/source/_toctree.yml` (config)
- `examples/deepspeed_configs/zero1.json` (config)
- `examples/deepspeed_configs/zero2.json` (config)
- `examples/deepspeed_configs/zero3.json` (config)
- `examples/fsdp_configs/fsdp2.json` (config)
- `pyproject.toml` (manifest)
- `trl/accelerate_configs/fsdp1.yaml` (config)
- `trl/accelerate_configs/fsdp2.yaml` (config)
- `trl/accelerate_configs/multi_gpu.yaml` (config)
- `trl/accelerate_configs/single_gpu.yaml` (config)
- `trl/accelerate_configs/zero1.yaml` (config)
- `trl/accelerate_configs/zero2.yaml` (config)
- `trl/accelerate_configs/zero3.yaml` (config)

## Top-level layout

- `trl` — 249 analysed file(s)
- `examples` — 105 analysed file(s)
- `scripts` — 88 analysed file(s)
- `docs` — 59 analysed file(s)
- `tests` — 56 analysed file(s)
- `.github` — 29 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `docker` — 2 analysed file(s)
- `.agents` — 1 analysed file(s)
- `.ai` — 1 analysed file(s)
- `skills` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `8ad18ec1b6493b85cf9fffbd87d376767ceb8611` is the revision these paths and observations refer to.
