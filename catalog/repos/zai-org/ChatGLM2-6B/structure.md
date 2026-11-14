# Project structure: zai-org/ChatGLM2-6B

**Analysed commit:** `cb8e8b43c0951b32614f25c03e1ab593a0603a1c`

**Commit reference:** [cb8e8b43c0951b32614f25c03e1ab593a0603a1c](https://github.com/zai-org/ChatGLM2-6B/commit/cb8e8b43c0951b32614f25c03e1ab593a0603a1c)

**Tree at this commit:** [zai-org/ChatGLM2-6B@cb8e8b43c095](https://github.com/zai-org/ChatGLM2-6B/tree/cb8e8b43c0951b32614f25c03e1ab593a0603a1c)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | zai-org/ChatGLM2-6B |
| Description | ChatGLM2-6B: An Open Bilingual Chat LLM | 开源双语对话语言模型 |
| Stars | 15475 |
| Forks | 1775 |
| Licence | Other |
| Language | Python |
| Default branch | main |
| Analysed commit | `cb8e8b43c0951b32614f25c03e1ab593a0603a1c` |
| Retrieved at | 2026-11-14T19:09:02.410523+00:00 |
| Files in this snapshot | 30 |

## Directory tree

```text
.github/  (3 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.yaml
    config.yml
    feature_request.yml
evaluation/  (2 files)
  README.md
  evaluate_ceval.py
ptuning/  (13 files)
  README.md
  arguments.py
  deepspeed.json
  ds_train_finetune.sh
  evaluate.sh
  evaluate_finetune.sh
  main.py
  train.sh
  train_chat.sh
  trainer.py
  trainer_seq2seq.py
  web_demo.py
  web_demo.sh
resources/  (1 files)
  WECHAT.md
FAQ.md
MODEL_LICENSE
README.md
README_EN.md
api.py
cli_demo.py
openai_api.py
requirements.txt
utils.py
web_demo.py
web_demo2.py
```

## Entry points

- [api.py:18](https://github.com/zai-org/ChatGLM2-6B/blob/cb8e8b43c0951b32614f25c03e1ab593a0603a1c/api.py#L18)
- [cli_demo.py:59](https://github.com/zai-org/ChatGLM2-6B/blob/cb8e8b43c0951b32614f25c03e1ab593a0603a1c/cli_demo.py#L59)
- [openai_api.py:27](https://github.com/zai-org/ChatGLM2-6B/blob/cb8e8b43c0951b32614f25c03e1ab593a0603a1c/openai_api.py#L27)
- [ptuning/main.py:410](https://github.com/zai-org/ChatGLM2-6B/blob/cb8e8b43c0951b32614f25c03e1ab593a0603a1c/ptuning/main.py#L410)
- [ptuning/web_demo.py:166](https://github.com/zai-org/ChatGLM2-6B/blob/cb8e8b43c0951b32614f25c03e1ab593a0603a1c/ptuning/web_demo.py#L166)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). Observed top-level functions: auto_configure_device_map, get_model, load_model_on_gpus, parse_text, postprocess, predict. |
| Application entry point | entrypoint | Observed | Groups 5 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed routes: POST /, GET /v1/models, POST /v1/chat/completions. O… |
| evaluation package | library | Observed | Groups 1 file(s) under evaluation package (observed from repository paths and static analysis). Observed top-level functions: build_prompt. |
| ptuning package | library | Observed | Groups 9 file(s) under ptuning package (observed from repository paths and static analysis). Observed top-level classes: DataTrainingArguments, ModelArguments, PrefixTrainer, Seq2SeqTrainer. |

## Important files

- `.github/ISSUE_TEMPLATE/bug_report.yaml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `ptuning/deepspeed.json` (config)
- `requirements.txt` (manifest)

## Top-level layout

- `ptuning` — 13 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `.github` — 3 analysed file(s)
- `evaluation` — 2 analysed file(s)
- `resources` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `cb8e8b43c0951b32614f25c03e1ab593a0603a1c` is the revision these paths and observations refer to.
