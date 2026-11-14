# Project structure: FareedKhan-dev/train-llm-from-scratch

**Analysed commit:** `bdd480a518094ca834e05ab32131dc126b522d3d`

**Commit reference:** [bdd480a518094ca834e05ab32131dc126b522d3d](https://github.com/FareedKhan-dev/train-llm-from-scratch/commit/bdd480a518094ca834e05ab32131dc126b522d3d)

**Tree at this commit:** [FareedKhan-dev/train-llm-from-scratch@bdd480a51809](https://github.com/FareedKhan-dev/train-llm-from-scratch/tree/bdd480a518094ca834e05ab32131dc126b522d3d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | FareedKhan-dev/train-llm-from-scratch |
| Description | A straightforward method for training your LLM, from downloading data to generating text. |
| Stars | 13222 |
| Forks | 1831 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `bdd480a518094ca834e05ab32131dc126b522d3d` |
| Retrieved at | 2026-11-14T19:09:54.768040+00:00 |
| Files in this snapshot | 243 |

## Directory tree

```text
.github/  (6 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.yml
    config.yml
    feature_request.yml
  workflows/  (2 files)
    ci.yml
    docs.yml
  pull_request_template.md
.streamlit/  (1 files)
  config.toml
config/  (7 files)
  __init__.py
  config.py
  loader.py
  paths.py
  post_training_config.py
  presets.py
  py.typed
configs/  (14 files)
  smoke/  (7 files)
    base.json
    dpo.json
    grpo.json
    ppo.json
    pretrain.json
    reward.json
    sft.json
  base.json
  dpo.json
  grpo.json
  ppo.json
  pretrain.json
  reward.json
  sft.json
data_loader/  (6 files)
  __init__.py
  data_loader.py
  preference_dataset.py
  prompt_dataset.py
  py.typed
  sft_dataset.py
docs/  (60 files)
  diagrams/  (23 files)
    src/  (21 files)
      … 21 files under this directory
    README.md
    make_plots.py
  foundations/  (9 files)
    README.md
    attention.md
    bpe.md
    generation.md
    objectives.md
    optimization.md
    scaling.md
    tokenization.md
    transformer.md
  howto/  (6 files)
    commands.md
    configs.md
    hardware.md
    train.md
    type_safety.md
    ui.md
  javascripts/  (1 files)
    mathjax.js
  modern/  (10 files)
    README.md
    attention.md
    blocks.md
    inference.md
    lora.md
    moe.md
    optimizers.md
    preference.md
    rl_reasoning.md
    rope.md
  student/  (1 files)
    README.md
  01_data_pipeline.md
  02_pretraining.md
  03_sft.md
  04_reward_model.md
  05_dpo.md
  06_ppo.md
  07_grpo.md
  08_evaluation.md
  09_inference.md
  README.md
images/  (20 files)
  00_pipeline.mmd
  01_data.mmd
  02_tokenization.mmd
  03_mlp.mmd
  04_attention_head.mmd
  05_multi_head_attention.mmd
  06_transformer_block.mmd
  07_transformer.mmd
  08_training_loop.mmd
  09_sft.mmd
  10_reward_model.mmd
  11_dpo.mmd
  12_ppo.mmd
  13_grpo.mmd
  14_evaluation.mmd
  15_inference.mmd
  make_diagrams.py
  mmdc.json
  plot_artifacts.py
  puppeteer.json
scripts/  (21 files)
  benchmark.py
  chat.py
  data_download.py
  data_preprocess.py
  eval_post_training.py
  generate_text.py
  model_report.py
  prepare_preference_data.py
  prepare_pretrain_data.py
  prepare_rl_prompts.py
  prepare_sft_data.py
  prepare_tiny_data.py
  pretrain_base.py
  render_diagrams.sh
  run_posttraining.sh
  train_dpo.py
  train_grpo.py
  train_ppo.py
  train_reward.py
  train_sft.py
  train_transformer.py
src/  (50 files)
  inference/  (4 files)
    __init__.py
    quantize.py
    sampling.py
    speculative.py
  models/  (17 files)
    modern/  (10 files)
      … 10 files under this directory
    __init__.py
    attention.py
    factory.py
    lora.py
    mlp.py
    transformer.py
    transformer_block.py
  optim/  (3 files)
    __init__.py
    muon.py
    schedules.py
  post_training/  (20 files)
    rewards/  (3 files)
      … 3 files under this directory
    __init__.py
    chat_template.py
    cli.py
    distributed.py
    dpo.py
    evaluation.py
    grpo.py
    inference.py
    logging_utils.py
    optim.py
    ppo.py
    reward_model.py
    reward_train.py
    rollout.py
    sft.py
    utils.py
    value_head.py
  tokenizer/  (2 files)
    __init__.py
    bpe.py
  __init__.py
  checkpoint.py
  device.py
  py.typed
tests/  (27 files)
  _typecheck.py
  conftest.py
  gpu_verify.sh
  grpo_live.py
  test_checkpoint_io.py
  test_checkpoint_resume.py
  test_classic_model.py
  test_config.py
  test_ddp_moe.py
  test_device.py
  test_factory.py
  test_inference.py
  test_lora.py
  test_model_report.py
  test_modern_model.py
  test_optim.py
  test_pipeline_e2e.py
  test_post_training_losses.py
  test_post_training_smoke.py
  test_preference_truncation.py
  test_rl_math.py
  test_sampling.py
  test_student_track.py
  test_tokenizer.py
  … 3 more files
ui/  (18 files)
  pages/  (9 files)
    1_Data.py
    2_Pretrain.py
    3_SFT.py
    4_Reward_Model.py
    5_DPO.py
    6_PPO.py
    7_GRPO.py
    8_Evaluate.py
    9_Chat.py
  __init__.py
  app.py
  config_forms.py
  docs_render.py
  jobs.py
  metrics.py
  stage_page.py
  stages.py
  theme.py
.gitattributes
.gitignore
.pre-commit-config.yaml
CHANGELOG.md
CONTRIBUTING.md
LICENSE
POST_TRAINING.md
README.md
mkdocs.yml
pyproject.toml
requirements-post.txt
requirements.txt
sft_rlhf_guide.ipynb
```

## Entry points

- [src/models/attention.py:104](https://github.com/FareedKhan-dev/train-llm-from-scratch/blob/bdd480a518094ca834e05ab32131dc126b522d3d/src/models/attention.py#L104)
- [src/models/mlp.py:69](https://github.com/FareedKhan-dev/train-llm-from-scratch/blob/bdd480a518094ca834e05ab32131dc126b522d3d/src/models/mlp.py#L69)
- [src/models/transformer.py:180](https://github.com/FareedKhan-dev/train-llm-from-scratch/blob/bdd480a518094ca834e05ab32131dc126b522d3d/src/models/transformer.py#L180)
- [src/models/transformer_block.py:63](https://github.com/FareedKhan-dev/train-llm-from-scratch/blob/bdd480a518094ca834e05ab32131dc126b522d3d/src/models/transformer_block.py#L63)
- [data_loader/data_loader.py:66](https://github.com/FareedKhan-dev/train-llm-from-scratch/blob/bdd480a518094ca834e05ab32131dc126b522d3d/data_loader/data_loader.py#L66)
- [images/make_diagrams.py:160](https://github.com/FareedKhan-dev/train-llm-from-scratch/blob/bdd480a518094ca834e05ab32131dc126b522d3d/images/make_diagrams.py#L160)
- [images/plot_artifacts.py:70](https://github.com/FareedKhan-dev/train-llm-from-scratch/blob/bdd480a518094ca834e05ab32131dc126b522d3d/images/plot_artifacts.py#L70)
- [scripts/benchmark.py:105](https://github.com/FareedKhan-dev/train-llm-from-scratch/blob/bdd480a518094ca834e05ab32131dc126b522d3d/scripts/benchmark.py#L105)
- [scripts/chat.py:74](https://github.com/FareedKhan-dev/train-llm-from-scratch/blob/bdd480a518094ca834e05ab32131dc126b522d3d/scripts/chat.py#L74)
- [scripts/data_download.py:79](https://github.com/FareedKhan-dev/train-llm-from-scratch/blob/bdd480a518094ca834e05ab32131dc126b522d3d/scripts/data_download.py#L79)
- [scripts/data_preprocess.py:116](https://github.com/FareedKhan-dev/train-llm-from-scratch/blob/bdd480a518094ca834e05ab32131dc126b522d3d/scripts/data_preprocess.py#L116)
- [scripts/eval_post_training.py:77](https://github.com/FareedKhan-dev/train-llm-from-scratch/blob/bdd480a518094ca834e05ab32131dc126b522d3d/scripts/eval_post_training.py#L77)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| checkpoint.py package | library | Observed | Groups 1 file(s) under checkpoint.py package (observed from repository paths and static analysis). Observed top-level functions: atomic_save, load_checkpoint, load_model_weights, model_config_from_checkpoint, model_stat… |
| Configuration and deployment | config | Observed | Groups 26 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: BaseModelConfig, ConfigError, DPOConfig, GRPOConfig, PPOConfig, PretrainConfig. Obse… |
| Data layer | data | Observed | Groups 13 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: GroupedQueryAttention, KVCache, LoRALinear, MoE, ModernBlock, ModernConfig. Observed top-level functio… |
| data_loader package | library | Observed | Groups 4 file(s) under data_loader package (observed from repository paths and static analysis). Observed top-level functions: _collate, _encode_response, _first_difference, encode_preference_pair, get_preference_iterat… |
| device.py package | library | Observed | Groups 1 file(s) under device.py package (observed from repository paths and static analysis). Observed top-level functions: _mps_available, _xla_available, autocast, configure_cpu_threads, describe_device, device_type. |
| Application entry point | entrypoint | Observed | Groups 28 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Block, Head, MLP, MultiHeadAttention, Transformer. Observed top-level functions: _build_p… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| inference package | library | Observed | Groups 4 file(s) under inference package (observed from repository paths and static analysis). Observed top-level classes: Int8Linear, SpeculativeStats. Observed top-level functions: _logits, _probs, filter_logits, mode… |
| __init__.py package | library | Observed | Groups 1 file(s) under __init__.py package (observed from repository paths and static analysis). |
| optim package | library | Observed | Groups 3 file(s) under optim package (observed from repository paths and static analysis). Observed top-level classes: Muon. Observed top-level functions: _warmup, adamw_param_groups, adjusted_lr, build_optimizer, cosin… |
| post_training package | library | Observed | Groups 19 file(s) under post_training package (observed from repository paths and static analysis). Observed top-level classes: DDPContext, MetricsLogger, RewardModel, RolloutBatch, TransformerWithValueHead. Observed to… |
| scripts package | library | Observed | Groups 2 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 27 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: _classic, _greedy, _json, _kept, _model, _modern. |
| tokenizer package | library | Observed | Groups 2 file(s) under tokenizer package (observed from repository paths and static analysis). Observed top-level classes: BPETokenizer, Tokenizer. Observed top-level functions: _merge, _tiktoken, safe_decode, tokenizer… |
| ui package | library | Observed | Groups 17 file(s) under ui package (observed from repository paths and static analysis). Observed top-level classes: Stage. Observed top-level functions: _alive, _alive_windows, _clean_markdown, _coerce_blank, _ensure_j… |

## Important files

- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/docs.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `.streamlit/config.toml` (config)
- `configs/base.json` (config)
- `configs/dpo.json` (config)
- `configs/grpo.json` (config)
- `configs/ppo.json` (config)
- `configs/pretrain.json` (config)
- `configs/reward.json` (config)
- `configs/sft.json` (config)
- `configs/smoke/base.json` (config)
- `configs/smoke/dpo.json` (config)
- `configs/smoke/grpo.json` (config)
- `configs/smoke/ppo.json` (config)
- `configs/smoke/pretrain.json` (config)
- `configs/smoke/reward.json` (config)
- `configs/smoke/sft.json` (config)
- `images/mmdc.json` (config)
- `images/puppeteer.json` (config)
- `mkdocs.yml` (config)
- `pyproject.toml` (manifest)
- `requirements-post.txt` (manifest)
- `requirements.txt` (manifest)

## Top-level layout

- `docs` — 60 analysed file(s)
- `src` — 50 analysed file(s)
- `tests` — 27 analysed file(s)
- `scripts` — 21 analysed file(s)
- `images` — 20 analysed file(s)
- `ui` — 18 analysed file(s)
- `configs` — 14 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `config` — 7 analysed file(s)
- `.github` — 6 analysed file(s)
- `data_loader` — 6 analysed file(s)
- `.streamlit` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `bdd480a518094ca834e05ab32131dc126b522d3d` is the revision these paths and observations refer to.
