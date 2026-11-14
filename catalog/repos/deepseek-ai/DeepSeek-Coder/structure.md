# Project structure: deepseek-ai/DeepSeek-Coder

**Analysed commit:** `2f9fd85927c669dae3c0fbb2d607274023af243e`

**Commit reference:** [2f9fd85927c669dae3c0fbb2d607274023af243e](https://github.com/deepseek-ai/DeepSeek-Coder/commit/2f9fd85927c669dae3c0fbb2d607274023af243e)

**Tree at this commit:** [deepseek-ai/DeepSeek-Coder@2f9fd85927c6](https://github.com/deepseek-ai/DeepSeek-Coder/tree/2f9fd85927c669dae3c0fbb2d607274023af243e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | deepseek-ai/DeepSeek-Coder |
| Description | DeepSeek Coder: Let the Code Write Itself |
| Stars | 24371 |
| Forks | 2956 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `2f9fd85927c669dae3c0fbb2d607274023af243e` |
| Retrieved at | 2026-11-14T19:07:40.442618+00:00 |
| Files in this snapshot | 57 |

## Directory tree

```text
Evaluation/  (45 files)
  DS-1000/  (1 files)
    README.md
  HumanEval/  (13 files)
    human_eval/  (5 files)
      … 5 files under this directory
    utils/  (2 files)
      … 2 files under this directory
    README.md
    eval.sh
    eval_instruct.py
    eval_pal.py
    humaneval.py
    test_config.yaml
  LeetCode/  (7 files)
    human_eval/  (4 files)
      … 4 files under this directory
    evaluate_leetcode.py
    readme.md
    vllm_inference.py
  MBPP/  (13 files)
    human_eval/  (5 files)
      … 5 files under this directory
    utils/  (2 files)
      … 2 files under this directory
    README.md
    eval.sh
    eval_instruct.py
    eval_pal.py
    mbpp.py
    test_config.yaml
  PAL-Math/  (11 files)
    datasets/  (4 files)
      … 4 files under this directory
    prompts/  (2 files)
      … 2 files under this directory
    utils/  (3 files)
      … 3 files under this directory
    README.md
    run.py
demo/  (3 files)
  app.py
  requirement.txt
  style.css
finetune/  (4 files)
  configs/  (1 files)
    ds_config_zero3.json
  README.md
  finetune_deepseekcoder.py
  requirements.txt
.gitignore
LICENSE-CODE
LICENSE-MODEL
README.md
requirements.txt
```

## Entry points

- [Evaluation/HumanEval/eval_instruct.py:119](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/Evaluation/HumanEval/eval_instruct.py#L119)
- [Evaluation/HumanEval/eval_pal.py:17](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/Evaluation/HumanEval/eval_pal.py#L17)
- [Evaluation/LeetCode/evaluate_leetcode.py:74](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/Evaluation/LeetCode/evaluate_leetcode.py#L74)
- [Evaluation/LeetCode/vllm_inference.py:69](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/Evaluation/LeetCode/vllm_inference.py#L69)
- [Evaluation/MBPP/eval_instruct.py:131](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/Evaluation/MBPP/eval_instruct.py#L131)
- [Evaluation/MBPP/eval_pal.py:17](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/Evaluation/MBPP/eval_pal.py#L17)
- [Evaluation/PAL-Math/run.py:179](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/Evaluation/PAL-Math/run.py#L179)
- [Evaluation/PAL-Math/utils/grader.py:150](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/Evaluation/PAL-Math/utils/grader.py#L150)
- [Evaluation/PAL-Math/utils/python_executor.py:179](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/Evaluation/PAL-Math/utils/python_executor.py#L179)
- [demo/app.py:128](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/demo/app.py#L128)
- [finetune/finetune_deepseekcoder.py:192](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/finetune/finetune_deepseekcoder.py#L192)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 11 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: ColorObjectRuntime, CustomDict, DataArguments, DataCollatorForSupervisedDataset, DateRunt… |
| Evaluation package | library | Observed | Groups 23 file(s) under evaluation package (observed from repository paths and static analysis). Observed top-level classes: HumanEval, HumanEvalDataset, KeywordsStoppingCriteria, MBPP, MBPPDataset, TimeoutException. Ob… |
| Tests | test | Observed | Groups 2 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `finetune/configs/ds_config_zero3.json` (config)
- `finetune/requirements.txt` (manifest)
- `requirements.txt` (manifest)

## Top-level layout

- `Evaluation` — 45 analysed file(s)
- `(root files)` — 5 analysed file(s)
- `finetune` — 4 analysed file(s)
- `demo` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `2f9fd85927c669dae3c0fbb2d607274023af243e` is the revision these paths and observations refer to.
