# Project structure: QwenLM/Qwen3

**Analysed commit:** `7a2f61ffc7a20d47efcd2bf97f6f2bf52729042e`

**Commit reference:** [7a2f61ffc7a20d47efcd2bf97f6f2bf52729042e](https://github.com/QwenLM/Qwen3/commit/7a2f61ffc7a20d47efcd2bf97f6f2bf52729042e)

**Tree at this commit:** [QwenLM/Qwen3@7a2f61ffc7a2](https://github.com/QwenLM/Qwen3/tree/7a2f61ffc7a20d47efcd2bf97f6f2bf52729042e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | QwenLM/Qwen3 |
| Description | Qwen3 is the large language model series developed by Qwen team, Alibaba Cloud. |
| Stars | 27731 |
| Forks | 2105 |
| Licence | Not detected |
| Language | Python |
| Default branch | main |
| Analysed commit | `7a2f61ffc7a20d47efcd2bf97f6f2bf52729042e` |
| Retrieved at | 2026-11-14T19:07:19.470010+00:00 |
| Files in this snapshot | 98 |

## Directory tree

```text
.github/  (3 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.yml
    config.yml
  workflows/  (1 files)
    inactive.yml
docker/  (3 files)
  Dockerfile-cu121
  docker_cli_demo.sh
  docker_web_demo.sh
docs/  (65 files)
  locales/  (28 files)
    zh_CN/  (28 files)
      … 28 files under this directory
  source/  (33 files)
    _static/  (2 files)
      … 2 files under this directory
    assets/  (1 files)
      … 1 files under this directory
    deployment/  (6 files)
      … 6 files under this directory
    framework/  (4 files)
      … 4 files under this directory
    getting_started/  (5 files)
      … 5 files under this directory
    inference/  (1 files)
      … 1 files under this directory
    quantization/  (3 files)
      … 3 files under this directory
    run_locally/  (4 files)
      … 4 files under this directory
    training/  (5 files)
      … 5 files under this directory
    conf.py
    index.rst
  Makefile
  README.md
  make.bat
  requirements-docs.txt
eval/  (8 files)
  configs/  (1 files)
    ARCAGI-Qwen3-235B-A22B-Instruct-2507.yaml
  eval/  (2 files)
    arc_agi_1.py
    eval.py
  eval_res/  (1 files)
    ARCAGI-Qwen3-235B-A22B-Instruct-2507_eval_result.txt
  generate_api_answers/  (2 files)
    infer_multithread.py
    utils_vllm.py
  README.md
  requirements.txt
examples/  (16 files)
  demo/  (2 files)
    cli_demo.py
    web_demo.py
  gcu-support/  (2 files)
    README.md
    gcu_demo.py
  llama-factory/  (5 files)
    finetune-zh.md
    qwen2-7b-full-sft.yaml
    qwen2-7b-lora-sft.yaml
    qwen2-7b-merge-lora.yaml
    qwen2-7b-qlora-sft.yaml
  speed-benchmark/  (6 files)
    README.md
    README_zh.md
    requirements-perf-transformers.txt
    requirements-perf-vllm.txt
    speed_benchmark_transformers.py
    speed_benchmark_vllm.py
  README.md
.gitignore
.readthedocs.yaml
README.md
```

## Entry points

- [eval/eval/eval.py:86](https://github.com/QwenLM/Qwen3/blob/7a2f61ffc7a20d47efcd2bf97f6f2bf52729042e/eval/eval/eval.py#L86)
- [eval/generate_api_answers/infer_multithread.py:184](https://github.com/QwenLM/Qwen3/blob/7a2f61ffc7a20d47efcd2bf97f6f2bf52729042e/eval/generate_api_answers/infer_multithread.py#L184)
- [eval/generate_api_answers/utils_vllm.py:92](https://github.com/QwenLM/Qwen3/blob/7a2f61ffc7a20d47efcd2bf97f6f2bf52729042e/eval/generate_api_answers/utils_vllm.py#L92)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| docker package | library | Observed | Groups 2 file(s) under docker package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 3 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: ClientError. Observed top-level functions: count_completed_samples, get_after_think, get_c… |
| eval package | library | Observed | Groups 1 file(s) under eval package (observed from repository paths and static analysis). Observed top-level functions: compute_scores_arc_agi_1, parse_model_output, save_cache, solution_score. |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |

## Important files

- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/inactive.yml` (ci)
- `.readthedocs.yaml` (config)
- `docker/Dockerfile-cu121` (container)
- `docs/requirements-docs.txt` (manifest)
- `eval/configs/ARCAGI-Qwen3-235B-A22B-Instruct-2507.yaml` (config)
- `eval/requirements.txt` (manifest)
- `examples/llama-factory/qwen2-7b-full-sft.yaml` (config)
- `examples/llama-factory/qwen2-7b-lora-sft.yaml` (config)
- `examples/llama-factory/qwen2-7b-merge-lora.yaml` (config)
- `examples/llama-factory/qwen2-7b-qlora-sft.yaml` (config)
- `examples/speed-benchmark/requirements-perf-transformers.txt` (manifest)
- `examples/speed-benchmark/requirements-perf-vllm.txt` (manifest)

## Top-level layout

- `docs` — 65 analysed file(s)
- `examples` — 16 analysed file(s)
- `eval` — 8 analysed file(s)
- `(root files)` — 3 analysed file(s)
- `.github` — 3 analysed file(s)
- `docker` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `7a2f61ffc7a20d47efcd2bf97f6f2bf52729042e` is the revision these paths and observations refer to.
