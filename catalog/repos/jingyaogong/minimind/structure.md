# Project structure: jingyaogong/minimind

**Analysed commit:** `233d00fa068ec2b8c0d4f07b703934d6391a5a73`

**Commit reference:** [233d00fa068ec2b8c0d4f07b703934d6391a5a73](https://github.com/jingyaogong/minimind/commit/233d00fa068ec2b8c0d4f07b703934d6391a5a73)

**Tree at this commit:** [jingyaogong/minimind@233d00fa068e](https://github.com/jingyaogong/minimind/tree/233d00fa068ec2b8c0d4f07b703934d6391a5a73)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | jingyaogong/minimind |
| Description | 🧠 Train a 64M-parameter LLM from scratch in just 2h! |
| Stars | 65229 |
| Forks | 8541 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `233d00fa068ec2b8c0d4f07b703934d6391a5a73` |
| Retrieved at | 2026-11-14T19:06:19.689503+00:00 |
| Files in this snapshot | 30 |

## Directory tree

```text
dataset/  (3 files)
  __init__.py
  dataset.md
  lm_dataset.py
model/  (4 files)
  __init__.py
  model_lora.py
  model_minimind.py
  tokenizer_config.json
scripts/  (5 files)
  chat_api.py
  convert_model.py
  eval_toolcall.py
  serve_openai_api.py
  web_demo.py
trainer/  (11 files)
  rollout_engine.py
  train_agent.py
  train_distillation.py
  train_dpo.py
  train_full_sft.py
  train_grpo.py
  train_lora.py
  train_ppo.py
  train_pretrain.py
  train_tokenizer.py
  trainer_utils.py
.gitignore
CODE_OF_CONDUCT.md
LICENSE
README.md
README_en.md
eval_llm.py
requirements.txt
```

## Entry points

- [dataset/lm_dataset.py:259](https://github.com/jingyaogong/minimind/blob/233d00fa068ec2b8c0d4f07b703934d6391a5a73/dataset/lm_dataset.py#L259)
- [eval_llm.py:95](https://github.com/jingyaogong/minimind/blob/233d00fa068ec2b8c0d4f07b703934d6391a5a73/eval_llm.py#L95)
- [scripts/convert_model.py:128](https://github.com/jingyaogong/minimind/blob/233d00fa068ec2b8c0d4f07b703934d6391a5a73/scripts/convert_model.py#L128)
- [scripts/eval_toolcall.py:239](https://github.com/jingyaogong/minimind/blob/233d00fa068ec2b8c0d4f07b703934d6391a5a73/scripts/eval_toolcall.py#L239)
- [scripts/serve_openai_api.py:25](https://github.com/jingyaogong/minimind/blob/233d00fa068ec2b8c0d4f07b703934d6391a5a73/scripts/serve_openai_api.py#L25)
- [scripts/web_demo.py:423](https://github.com/jingyaogong/minimind/blob/233d00fa068ec2b8c0d4f07b703934d6391a5a73/scripts/web_demo.py#L423)
- [trainer/train_agent.py:370](https://github.com/jingyaogong/minimind/blob/233d00fa068ec2b8c0d4f07b703934d6391a5a73/trainer/train_agent.py#L370)
- [trainer/train_distillation.py:137](https://github.com/jingyaogong/minimind/blob/233d00fa068ec2b8c0d4f07b703934d6391a5a73/trainer/train_distillation.py#L137)
- [trainer/train_dpo.py:122](https://github.com/jingyaogong/minimind/blob/233d00fa068ec2b8c0d4f07b703934d6391a5a73/trainer/train_dpo.py#L122)
- [trainer/train_full_sft.py:75](https://github.com/jingyaogong/minimind/blob/233d00fa068ec2b8c0d4f07b703934d6391a5a73/trainer/train_full_sft.py#L75)
- [trainer/train_grpo.py:199](https://github.com/jingyaogong/minimind/blob/233d00fa068ec2b8c0d4f07b703934d6391a5a73/trainer/train_grpo.py#L199)
- [trainer/train_lora.py:69](https://github.com/jingyaogong/minimind/blob/233d00fa068ec2b8c0d4f07b703934d6391a5a73/trainer/train_lora.py#L69)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| dataset package | library | Observed | Groups 1 file(s) under dataset package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 15 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed routes: POST /v1/chat/completions. Observed top-level class… |
| External integrations | external | Observed | Groups 1 file(s) under external integrations (observed from repository paths and static analysis). |
| model package | library | Observed | Groups 3 file(s) under model package (observed from repository paths and static analysis). Observed top-level classes: Attention, FeedForward, LoRA, MOEFeedForward, MiniMindBlock, MiniMindConfig. Observed top-level func… |
| trainer package | library | Observed | Groups 2 file(s) under trainer package (observed from repository paths and static analysis). Observed top-level classes: LMForRewardModel, RolloutEngine, RolloutResult, SGLangRolloutEngine, SkipBatchSampler, TorchRollou… |

## Important files

- `model/tokenizer_config.json` (config)
- `requirements.txt` (manifest)

## Top-level layout

- `trainer` — 11 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `scripts` — 5 analysed file(s)
- `model` — 4 analysed file(s)
- `dataset` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `233d00fa068ec2b8c0d4f07b703934d6391a5a73` is the revision these paths and observations refer to.
