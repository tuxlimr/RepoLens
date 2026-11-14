# Project structure: haotian-liu/LLaVA

**Analysed commit:** `c121f0432da27facab705978f83c4ada465e46fd`

**Commit reference:** [c121f0432da27facab705978f83c4ada465e46fd](https://github.com/haotian-liu/LLaVA/commit/c121f0432da27facab705978f83c4ada465e46fd)

**Tree at this commit:** [haotian-liu/LLaVA@c121f0432da2](https://github.com/haotian-liu/LLaVA/tree/c121f0432da27facab705978f83c4ada465e46fd)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | haotian-liu/LLaVA |
| Description | [NeurIPS'23 Oral] Visual Instruction Tuning (LLaVA) built towards GPT-4V level capabilities and beyond. |
| Stars | 25077 |
| Forks | 2772 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `c121f0432da27facab705978f83c4ada465e46fd` |
| Retrieved at | 2026-11-14T19:07:34.190033+00:00 |
| Files in this snapshot | 163 |

## Directory tree

```text
.devcontainer/  (4 files)
  Dockerfile
  devcontainer.env
  devcontainer.json
  postCreateCommand.sh
.github/  (4 files)
  ISSUE_TEMPLATE/  (4 files)
    1-usage.yaml
    2-feature-request.yaml
    3-question.yaml
    4-discussion.yaml
docs/  (12 files)
  Customize_Component.md
  Data.md
  Evaluation.md
  Finetune_Custom_Data.md
  Intel.md
  LLaVA_Bench.md
  LLaVA_from_LLaMA2.md
  LoRA.md
  MODEL_ZOO.md
  ScienceQA.md
  Windows.md
  macOS.md
llava/  (70 files)
  eval/  (38 files)
    table/  (15 files)
      … 15 files under this directory
    webpage/  (5 files)
      … 5 files under this directory
    eval_gpt_review.py
    eval_gpt_review_bench.py
    eval_gpt_review_visual.py
    eval_pope.py
    eval_science_qa.py
    eval_science_qa_gpt4.py
    eval_science_qa_gpt4_requery.py
    eval_textvqa.py
    generate_webpage_data_from_table.py
    m4c_evaluator.py
    model_qa.py
    model_vqa.py
    model_vqa_loader.py
    model_vqa_mmbench.py
    model_vqa_science.py
    qa_baseline_gpt35.py
    run_llava.py
    summarize_gpt_review.py
  model/  (13 files)
    language_model/  (3 files)
      … 3 files under this directory
    multimodal_encoder/  (2 files)
      … 2 files under this directory
    multimodal_projector/  (1 files)
      … 1 files under this directory
    __init__.py
    apply_delta.py
    builder.py
    consolidate.py
    llava_arch.py
    make_delta.py
    utils.py
  serve/  (8 files)
    __init__.py
    cli.py
    controller.py
    gradio_web_server.py
    model_worker.py
    register_worker.py
    sglang_worker.py
    test_message.py
  train/  (6 files)
    llama_flash_attn_monkey_patch.py
    llama_xformers_attn_monkey_patch.py
    llava_trainer.py
    train.py
    train_mem.py
    train_xformers.py
  __init__.py
  constants.py
  conversation.py
  mm_utils.py
  utils.py
playground/  (22 files)
  data/  (22 files)
    coco2014_val_qa_eval/  (2 files)
      … 2 files under this directory
    prompts/  (19 files)
      … 19 files under this directory
    coco2014_val_gpt4_qa_30x3.jsonl
scripts/  (42 files)
  v1_5/  (19 files)
    eval/  (14 files)
      … 14 files under this directory
    finetune.sh
    finetune_lora.sh
    finetune_task.sh
    finetune_task_lora.sh
    pretrain.sh
  convert_gqa_for_eval.py
  convert_mmbench_for_submission.py
  convert_mmvet_for_eval.py
  convert_seed_for_submission.py
  convert_sqa_to_llava.py
  convert_sqa_to_llava_base_prompt.py
  convert_vizwiz_for_submission.py
  convert_vqav2_for_submission.py
  extract_mm_projector.py
  finetune.sh
  finetune_full_schedule.sh
  finetune_lora.sh
  finetune_qlora.sh
  finetune_sqa.sh
  merge_lora_weights.py
  pretrain.sh
  pretrain_xformers.sh
  sqa_eval_batch.sh
  sqa_eval_gather.sh
  upload_pypi.sh
  zero2.json
  zero3.json
  zero3_offload.json
.dockerignore
.editorconfig
.gitattributes
.gitignore
LICENSE
README.md
cog.yaml
predict.py
pyproject.toml
```

## Entry points

- [llava/conversation.py:395](https://github.com/haotian-liu/LLaVA/blob/c121f0432da27facab705978f83c4ada465e46fd/llava/conversation.py#L395)
- [llava/eval/eval_gpt_review.py:55](https://github.com/haotian-liu/LLaVA/blob/c121f0432da27facab705978f83c4ada465e46fd/llava/eval/eval_gpt_review.py#L55)
- [llava/eval/eval_gpt_review_bench.py:52](https://github.com/haotian-liu/LLaVA/blob/c121f0432da27facab705978f83c4ada465e46fd/llava/eval/eval_gpt_review_bench.py#L52)
- [llava/eval/eval_gpt_review_visual.py:52](https://github.com/haotian-liu/LLaVA/blob/c121f0432da27facab705978f83c4ada465e46fd/llava/eval/eval_gpt_review_visual.py#L52)
- [llava/eval/eval_pope.py:64](https://github.com/haotian-liu/LLaVA/blob/c121f0432da27facab705978f83c4ada465e46fd/llava/eval/eval_pope.py#L64)
- [llava/eval/eval_science_qa.py:39](https://github.com/haotian-liu/LLaVA/blob/c121f0432da27facab705978f83c4ada465e46fd/llava/eval/eval_science_qa.py#L39)
- [llava/eval/eval_science_qa_gpt4.py:38](https://github.com/haotian-liu/LLaVA/blob/c121f0432da27facab705978f83c4ada465e46fd/llava/eval/eval_science_qa_gpt4.py#L38)
- [llava/eval/eval_science_qa_gpt4_requery.py:40](https://github.com/haotian-liu/LLaVA/blob/c121f0432da27facab705978f83c4ada465e46fd/llava/eval/eval_science_qa_gpt4_requery.py#L40)
- [llava/eval/eval_textvqa.py:54](https://github.com/haotian-liu/LLaVA/blob/c121f0432da27facab705978f83c4ada465e46fd/llava/eval/eval_textvqa.py#L54)
- [llava/eval/generate_webpage_data_from_table.py:30](https://github.com/haotian-liu/LLaVA/blob/c121f0432da27facab705978f83c4ada465e46fd/llava/eval/generate_webpage_data_from_table.py#L30)
- [llava/eval/model_qa.py:57](https://github.com/haotian-liu/LLaVA/blob/c121f0432da27facab705978f83c4ada465e46fd/llava/eval/model_qa.py#L57)
- [llava/eval/model_vqa.py:86](https://github.com/haotian-liu/LLaVA/blob/c121f0432da27facab705978f83c4ada465e46fd/llava/eval/model_vqa.py#L86)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). Observed top-level classes: Predictor. Observed top-level functions: download_json, download_weights, load_image. |
| Application entry point | entrypoint | Observed | Groups 37 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed routes: POST /register_worker, POST /refresh_all_workers, P… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| llava package | library | Observed | Groups 20 file(s) under llava package (observed from repository paths and static analysis). Observed top-level classes: CLIPVisionTower, CLIPVisionTowerS2, EvalAIAnswerProcessor, IdentityMap, KeywordsStoppingCriteria, L… |
| scripts package | library | Observed | Groups 32 file(s) under scripts package (observed from repository paths and static analysis). Observed top-level functions: build_prompt, build_prompt_chatbot, build_prompt_gpt4, create_one_example, create_one_example_c… |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: main. |

## Important files

- `.devcontainer/Dockerfile` (container)
- `.devcontainer/devcontainer.json` (config)
- `.dockerignore` (container)
- `.editorconfig` (config)
- `.github/ISSUE_TEMPLATE/1-usage.yaml` (config)
- `.github/ISSUE_TEMPLATE/2-feature-request.yaml` (config)
- `.github/ISSUE_TEMPLATE/3-question.yaml` (config)
- `.github/ISSUE_TEMPLATE/4-discussion.yaml` (config)
- `cog.yaml` (config)
- `llava/eval/table/rule.json` (config)
- `pyproject.toml` (manifest)
- `scripts/zero2.json` (config)
- `scripts/zero3.json` (config)
- `scripts/zero3_offload.json` (config)

## Top-level layout

- `llava` — 70 analysed file(s)
- `scripts` — 42 analysed file(s)
- `playground` — 22 analysed file(s)
- `docs` — 12 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `.devcontainer` — 4 analysed file(s)
- `.github` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `c121f0432da27facab705978f83c4ada465e46fd` is the revision these paths and observations refer to.
