# Project structure: huggingface/open-r1

**Analysed commit:** `5b6ff22b3fb7aa069c54866e517f39dfc3160e09`

**Commit reference:** [5b6ff22b3fb7aa069c54866e517f39dfc3160e09](https://github.com/huggingface/open-r1/commit/5b6ff22b3fb7aa069c54866e517f39dfc3160e09)

**Tree at this commit:** [huggingface/open-r1@5b6ff22b3fb7](https://github.com/huggingface/open-r1/tree/5b6ff22b3fb7aa069c54866e517f39dfc3160e09)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | huggingface/open-r1 |
| Description | Fully open reproduction of DeepSeek-R1 |
| Stars | 26480 |
| Forks | 2454 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `5b6ff22b3fb7aa069c54866e517f39dfc3160e09` |
| Retrieved at | 2026-11-14T19:07:22.704789+00:00 |
| Files in this snapshot | 78 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (1 files)
    tests.yml
  dependabot.yml
logs/  (1 files)
  .gitkeep
recipes/  (16 files)
  DeepSeek-R1-Distill-Qwen-1.5B/  (1 files)
    grpo/  (1 files)
      … 1 files under this directory
  OlympicCoder-32B/  (1 files)
    sft/  (1 files)
      … 1 files under this directory
  OlympicCoder-7B/  (1 files)
    sft/  (1 files)
      … 1 files under this directory
  OpenR1-Distill-7B/  (1 files)
    sft/  (1 files)
      … 1 files under this directory
  Qwen2.5-1.5B-Instruct/  (3 files)
    grpo/  (3 files)
      … 3 files under this directory
  Qwen2.5-Coder-7B-Instruct/  (1 files)
    grpo/  (1 files)
      … 1 files under this directory
  accelerate_configs/  (4 files)
    ddp.yaml
    fsdp.yaml
    zero2.yaml
    zero3.yaml
  dataset_filtering/  (3 files)
    config_demo.yaml
    filter_dapo.yaml
    filter_python.yaml
  README.md
scripts/  (11 files)
  pass_rate_filtering/  (3 files)
    README.md
    compute_pass_rate.py
    launch_filtering.sh
  benchmark_e2b.py
  decontaminate.py
  e2b_router.py
  generate_reasoning.py
  get_tensor_parallel_size.py
  morph_router.py
  run_benchmarks.py
  upload_details.py
slurm/  (13 files)
  experimental/  (1 files)
    serve_r1_vllm.slurm
  piston/  (3 files)
    README.md
    launch_piston_workers.sh
    launch_single_piston.sh
  README.md
  compute_pass_rate.slurm
  e2b_router.slurm
  evaluate.slurm
  generate.slurm
  morph_router.slurm
  serve_r1.slurm
  serve_router.slurm
  train.slurm
src/  (25 files)
  open_r1/  (25 files)
    utils/  (19 files)
      … 19 files under this directory
    __init__.py
    configs.py
    generate.py
    grpo.py
    rewards.py
    sft.py
tests/  (4 files)
  slow/  (1 files)
    test_code_reward.py
  utils/  (1 files)
    test_data.py
  __init__.py
  test_rewards.py
.gitignore
LICENSE
Makefile
README.md
setup.cfg
setup.py
```

## Entry points

- [src/open_r1/generate.py:66](https://github.com/huggingface/open-r1/blob/5b6ff22b3fb7aa069c54866e517f39dfc3160e09/src/open_r1/generate.py#L66)
- [src/open_r1/grpo.py:178](https://github.com/huggingface/open-r1/blob/5b6ff22b3fb7aa069c54866e517f39dfc3160e09/src/open_r1/grpo.py#L178)
- [src/open_r1/sft.py:166](https://github.com/huggingface/open-r1/blob/5b6ff22b3fb7aa069c54866e517f39dfc3160e09/src/open_r1/sft.py#L166)
- [src/open_r1/utils/competitive_programming/code_patcher.py:119](https://github.com/huggingface/open-r1/blob/5b6ff22b3fb7aa069c54866e517f39dfc3160e09/src/open_r1/utils/competitive_programming/code_patcher.py#L119)
- [src/open_r1/utils/routed_sandbox.py:103](https://github.com/huggingface/open-r1/blob/5b6ff22b3fb7aa069c54866e517f39dfc3160e09/src/open_r1/utils/routed_sandbox.py#L103)
- [scripts/benchmark_e2b.py:43](https://github.com/huggingface/open-r1/blob/5b6ff22b3fb7aa069c54866e517f39dfc3160e09/scripts/benchmark_e2b.py#L43)
- [scripts/decontaminate.py:71](https://github.com/huggingface/open-r1/blob/5b6ff22b3fb7aa069c54866e517f39dfc3160e09/scripts/decontaminate.py#L71)
- [scripts/e2b_router.py:93](https://github.com/huggingface/open-r1/blob/5b6ff22b3fb7aa069c54866e517f39dfc3160e09/scripts/e2b_router.py#L93)
- [scripts/generate_reasoning.py:172](https://github.com/huggingface/open-r1/blob/5b6ff22b3fb7aa069c54866e517f39dfc3160e09/scripts/generate_reasoning.py#L172)
- [scripts/get_tensor_parallel_size.py:19](https://github.com/huggingface/open-r1/blob/5b6ff22b3fb7aa069c54866e517f39dfc3160e09/scripts/get_tensor_parallel_size.py#L19)
- [scripts/morph_router.py:71](https://github.com/huggingface/open-r1/blob/5b6ff22b3fb7aa069c54866e517f39dfc3160e09/scripts/morph_router.py#L71)
- [scripts/pass_rate_filtering/compute_pass_rate.py:202](https://github.com/huggingface/open-r1/blob/5b6ff22b3fb7aa069c54866e517f39dfc3160e09/scripts/pass_rate_filtering/compute_pass_rate.py#L202)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 17 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: deps_list. |
| Application entry point | entrypoint | Observed | Groups 14 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed top-level classes: BatchRequest, PassRateScriptArguments, R… |
| External integrations | external | Observed | Groups 2 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: MorphCloudError, MorphCloudExecutionClient, PistonClient, PistonError. Observed top-level fu… |
| open_r1 package | library | Observed | Groups 18 file(s) under open_r1 package (observed from repository paths and static analysis). Observed top-level classes: CodeExecutionProvider, DatasetConfig, DatasetMixtureConfig, DummyConfig, E2BProvider, GRPOConfig.… |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| slurm package | library | Observed | Groups 2 file(s) under slurm package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 4 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: TestCodeFormat, TestCodeRewards, TestGetDataset, TestGetRewardFuncs, TestRepetitionPenaltyReward, TestReward… |

## Important files

- `.github/dependabot.yml` (config)
- `.github/workflows/tests.yml` (ci)
- `recipes/DeepSeek-R1-Distill-Qwen-1.5B/grpo/config_demo.yaml` (config)
- `recipes/OlympicCoder-32B/sft/config_v00.00.yaml` (config)
- `recipes/OlympicCoder-7B/sft/config_v00.00.yaml` (config)
- `recipes/OpenR1-Distill-7B/sft/config_distill.yaml` (config)
- `recipes/Qwen2.5-1.5B-Instruct/grpo/config_demo.yaml` (config)
- `recipes/Qwen2.5-1.5B-Instruct/grpo/config_demo_code.yaml` (config)
- `recipes/Qwen2.5-1.5B-Instruct/grpo/config_demo_code_ioi.yaml` (config)
- `recipes/Qwen2.5-Coder-7B-Instruct/grpo/config_codeforces.yaml` (config)
- `recipes/accelerate_configs/ddp.yaml` (config)
- `recipes/accelerate_configs/fsdp.yaml` (config)
- `recipes/accelerate_configs/zero2.yaml` (config)
- `recipes/accelerate_configs/zero3.yaml` (config)
- `recipes/dataset_filtering/config_demo.yaml` (config)
- `recipes/dataset_filtering/filter_dapo.yaml` (config)
- `recipes/dataset_filtering/filter_python.yaml` (config)
- `setup.cfg` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `src` — 25 analysed file(s)
- `recipes` — 16 analysed file(s)
- `slurm` — 13 analysed file(s)
- `scripts` — 11 analysed file(s)
- `(root files)` — 6 analysed file(s)
- `tests` — 4 analysed file(s)
- `.github` — 2 analysed file(s)
- `logs` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `5b6ff22b3fb7aa069c54866e517f39dfc3160e09` is the revision these paths and observations refer to.
