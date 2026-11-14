# Project structure: QwenLM/Qwen

**Analysed commit:** `2df8e8ac450fa185c421a08b0090ef81826caa6e`

**Commit reference:** [2df8e8ac450fa185c421a08b0090ef81826caa6e](https://github.com/QwenLM/Qwen/commit/2df8e8ac450fa185c421a08b0090ef81826caa6e)

**Tree at this commit:** [QwenLM/Qwen@2df8e8ac450f](https://github.com/QwenLM/Qwen/tree/2df8e8ac450fa185c421a08b0090ef81826caa6e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | QwenLM/Qwen |
| Description | The official repo of Qwen (通义千问) chat & pretrained large language model proposed by Alibaba Cloud. |
| Stars | 22028 |
| Forks | 2006 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `2df8e8ac450fa185c421a08b0090ef81826caa6e` |
| Retrieved at | 2026-11-14T19:07:56.891310+00:00 |
| Files in this snapshot | 114 |

## Directory tree

```text
.github/  (4 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.yaml
    config.yaml
    feature_request.yaml
  workflows/  (1 files)
    stale.yml
ascend-support/  (2 files)
  README.md
  docker_qwen.sh
dcu-support/  (12 files)
  package/  (5 files)
    fastllm_pytools/  (4 files)
      … 4 files under this directory
    setup.py
  README.md
  cli_demo.py
  cli_demo_batch.py
  model.properties
  qwen2flm.py
  requirements.txt
  web_demo.py
docker/  (6 files)
  Dockerfile
  Dockerfile-cu114
  Dockerfile-cu121
  docker_cli_demo.sh
  docker_openai_api.sh
  docker_web_demo.sh
eval/  (12 files)
  EVALUATION.md
  evaluate_ceval.py
  evaluate_chat_ceval.py
  evaluate_chat_gsm8k.py
  evaluate_chat_humaneval.py
  evaluate_chat_mmlu.py
  evaluate_cmmlu.py
  evaluate_gsm8k.py
  evaluate_humaneval.py
  evaluate_mmlu.py
  evaluate_plugin.py
  gsm8k_prompt.txt
examples/  (14 files)
  add_merges.py
  auto_comments.md
  auto_comments.py
  function_call_examples.py
  function_call_finetune_examples.py
  langchain_tooluse.ipynb
  qwen_extra.tiktoken
  qwen_extra_vocab.txt
  react_demo.py
  react_prompt.md
  system_prompt.md
  tokenizer_showcase.ipynb
  transformers_agent.md
  vllm_wrapper.py
finetune/  (7 files)
  ds_config_zero2.json
  ds_config_zero3.json
  finetune_ds.sh
  finetune_lora_ds.sh
  finetune_lora_single_gpu.sh
  finetune_qlora_ds.sh
  finetune_qlora_single_gpu.sh
recipes/  (31 files)
  applications/  (3 files)
    chatbot/  (1 files)
      … 1 files under this directory
    domain_finetune/  (1 files)
      … 1 files under this directory
    retrieval/  (1 files)
      … 1 files under this directory
  finetune/  (11 files)
    ascend/  (1 files)
      … 1 files under this directory
    deepspeed/  (8 files)
      … 8 files under this directory
    swift/  (2 files)
      … 2 files under this directory
  inference/  (8 files)
    dashscope/  (1 files)
      … 1 files under this directory
    hf_modelscope/  (1 files)
      … 1 files under this directory
    quantization/  (1 files)
      … 1 files under this directory
    tensorrt/  (2 files)
      … 2 files under this directory
    vllm/  (3 files)
      … 3 files under this directory
  quickstart/  (1 files)
    qwen.ipynb
  tests/  (8 files)
    assets/  (1 files)
      … 1 files under this directory
    test_finetune/  (1 files)
      … 1 files under this directory
    test_inference/  (2 files)
      … 2 files under this directory
    README.md
    __init__.py
    ut_config.py
    utils.py
.dockerignore
.gitignore
FAQ.md
FAQ_ja.md
FAQ_zh.md
LICENSE
NOTICE
README.md
README_CN.md
README_ES.md
README_FR.md
README_JA.md
Tongyi Qianwen LICENSE AGREEMENT
Tongyi Qianwen RESEARCH LICENSE AGREEMENT
cli_demo.py
finetune.py
openai_api.py
requirements.txt
requirements_web_demo.txt
run_gptq.py
tech_memo.md
tokenization_note.md
tokenization_note_ja.md
tokenization_note_zh.md
… 2 more files
```

## Entry points

- [cli_demo.py:209](https://github.com/QwenLM/Qwen/blob/2df8e8ac450fa185c421a08b0090ef81826caa6e/cli_demo.py#L209)
- [dcu-support/cli_demo.py:11](https://github.com/QwenLM/Qwen/blob/2df8e8ac450fa185c421a08b0090ef81826caa6e/dcu-support/cli_demo.py#L11)
- [dcu-support/cli_demo_batch.py:11](https://github.com/QwenLM/Qwen/blob/2df8e8ac450fa185c421a08b0090ef81826caa6e/dcu-support/cli_demo_batch.py#L11)
- [dcu-support/qwen2flm.py:6](https://github.com/QwenLM/Qwen/blob/2df8e8ac450fa185c421a08b0090ef81826caa6e/dcu-support/qwen2flm.py#L6)
- [eval/evaluate_ceval.py:415](https://github.com/QwenLM/Qwen/blob/2df8e8ac450fa185c421a08b0090ef81826caa6e/eval/evaluate_ceval.py#L415)
- [eval/evaluate_chat_ceval.py:431](https://github.com/QwenLM/Qwen/blob/2df8e8ac450fa185c421a08b0090ef81826caa6e/eval/evaluate_chat_ceval.py#L431)
- [eval/evaluate_chat_gsm8k.py:80](https://github.com/QwenLM/Qwen/blob/2df8e8ac450fa185c421a08b0090ef81826caa6e/eval/evaluate_chat_gsm8k.py#L80)
- [eval/evaluate_chat_humaneval.py:58](https://github.com/QwenLM/Qwen/blob/2df8e8ac450fa185c421a08b0090ef81826caa6e/eval/evaluate_chat_humaneval.py#L58)
- [eval/evaluate_chat_mmlu.py:288](https://github.com/QwenLM/Qwen/blob/2df8e8ac450fa185c421a08b0090ef81826caa6e/eval/evaluate_chat_mmlu.py#L288)
- [eval/evaluate_cmmlu.py:308](https://github.com/QwenLM/Qwen/blob/2df8e8ac450fa185c421a08b0090ef81826caa6e/eval/evaluate_cmmlu.py#L308)
- [eval/evaluate_gsm8k.py:74](https://github.com/QwenLM/Qwen/blob/2df8e8ac450fa185c421a08b0090ef81826caa6e/eval/evaluate_gsm8k.py#L74)
- [eval/evaluate_humaneval.py:40](https://github.com/QwenLM/Qwen/blob/2df8e8ac450fa185c421a08b0090ef81826caa6e/eval/evaluate_humaneval.py#L40)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| ascend-support package | library | Observed | Groups 1 file(s) under ascend-support package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 11 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). Observed top-level functions: _device_map, load_model_on_gpus. |
| dcu-support package | library | Observed | Groups 5 file(s) under dcu-support package (observed from repository paths and static analysis). Observed top-level classes: model. Observed top-level functions: create, from_hf, get_cpu_kvcache, get_cpu_low_mem, get_cp… |
| docker package | library | Observed | Groups 3 file(s) under docker package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 19 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed routes: GET /v1/models, POST /v1/chat/completions. Observed… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| finetune package | library | Observed | Groups 5 file(s) under finetune package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 8 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: TelnetPort, run_in_subprocess, simple_openai_api, test_finetune, test_inference_api, test_inference_vllm_f… |

## Important files

- `.dockerignore` (container)
- `.github/ISSUE_TEMPLATE/bug_report.yaml` (config)
- `.github/ISSUE_TEMPLATE/config.yaml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yaml` (config)
- `.github/workflows/stale.yml` (ci)
- `dcu-support/package/setup.py` (manifest)
- `dcu-support/requirements.txt` (manifest)
- `docker/Dockerfile` (container)
- `docker/Dockerfile-cu114` (container)
- `docker/Dockerfile-cu121` (container)
- `finetune/ds_config_zero2.json` (config)
- `finetune/ds_config_zero3.json` (config)
- `recipes/finetune/deepspeed/requirements.txt` (manifest)
- `recipes/inference/tensorrt/docker/Dockerfile` (container)
- `requirements.txt` (manifest)
- `requirements_web_demo.txt` (manifest)

## Top-level layout

- `recipes` — 31 analysed file(s)
- `(root files)` — 26 analysed file(s)
- `examples` — 14 analysed file(s)
- `dcu-support` — 12 analysed file(s)
- `eval` — 12 analysed file(s)
- `finetune` — 7 analysed file(s)
- `docker` — 6 analysed file(s)
- `.github` — 4 analysed file(s)
- `ascend-support` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `2df8e8ac450fa185c421a08b0090ef81826caa6e` is the revision these paths and observations refer to.
