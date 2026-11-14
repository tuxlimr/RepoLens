# Project structure: zai-org/ChatGLM-6B

**Analysed commit:** `401bf3a8a7dd8a26fba189551dccfc61a7079b4e`

**Commit reference:** [401bf3a8a7dd8a26fba189551dccfc61a7079b4e](https://github.com/zai-org/ChatGLM-6B/commit/401bf3a8a7dd8a26fba189551dccfc61a7079b4e)

**Tree at this commit:** [zai-org/ChatGLM-6B@401bf3a8a7dd](https://github.com/zai-org/ChatGLM-6B/tree/401bf3a8a7dd8a26fba189551dccfc61a7079b4e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | zai-org/ChatGLM-6B |
| Description | ChatGLM-6B: An Open Bilingual Dialogue Language Model | 开源双语对话语言模型 |
| Stars | 40847 |
| Forks | 5076 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `401bf3a8a7dd8a26fba189551dccfc61a7079b4e` |
| Retrieved at | 2026-11-14T19:06:42.143954+00:00 |
| Files in this snapshot | 37 |

## Directory tree

```text
.github/  (3 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.yaml
    config.yml
    feature_request.yml
improve/  (2 files)
  README.md
  data_sample.jsonl
ptuning/  (14 files)
  README.md
  README_en.md
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
.gitignore
FAQ.md
LICENSE
MODEL_LICENSE
PROJECT.md
README.md
README_en.md
UPDATE.md
api.py
cli_demo.py
cli_demo_vision.py
requirements.txt
utils.py
web_demo.py
web_demo2.py
web_demo_old.py
web_demo_vision.py
```

## Entry points

- [api.py:18](https://github.com/zai-org/ChatGLM-6B/blob/401bf3a8a7dd8a26fba189551dccfc61a7079b4e/api.py#L18)
- [cli_demo.py:57](https://github.com/zai-org/ChatGLM-6B/blob/401bf3a8a7dd8a26fba189551dccfc61a7079b4e/cli_demo.py#L57)
- [cli_demo_vision.py:63](https://github.com/zai-org/ChatGLM-6B/blob/401bf3a8a7dd8a26fba189551dccfc61a7079b4e/cli_demo_vision.py#L63)
- [ptuning/main.py:429](https://github.com/zai-org/ChatGLM-6B/blob/401bf3a8a7dd8a26fba189551dccfc61a7079b4e/ptuning/main.py#L429)
- [ptuning/web_demo.py:165](https://github.com/zai-org/ChatGLM-6B/blob/401bf3a8a7dd8a26fba189551dccfc61a7079b4e/ptuning/web_demo.py#L165)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 5 file(s) under core modules (observed from repository paths and static analysis). Observed top-level functions: auto_configure_device_map, get_model, load_model_on_gpus, parse_text, postprocess, predict. |
| Application entry point | entrypoint | Observed | Groups 5 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed routes: POST /. Observed top-level functions: _mp_fn, build_… |
| ptuning package | library | Observed | Groups 9 file(s) under ptuning package (observed from repository paths and static analysis). Observed top-level classes: DataTrainingArguments, ModelArguments, Seq2SeqTrainer, Trainer. |

## Important files

- `.github/ISSUE_TEMPLATE/bug_report.yaml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `ptuning/deepspeed.json` (config)
- `requirements.txt` (manifest)

## Top-level layout

- `(root files)` — 17 analysed file(s)
- `ptuning` — 14 analysed file(s)
- `.github` — 3 analysed file(s)
- `improve` — 2 analysed file(s)
- `resources` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `401bf3a8a7dd8a26fba189551dccfc61a7079b4e` is the revision these paths and observations refer to.
