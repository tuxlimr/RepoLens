# Project structure: Jiayi-Pan/TinyZero

**Analysed commit:** `95df88f2dcb05f33bd18da546531b52d0954c18b`

**Commit reference:** [95df88f2dcb05f33bd18da546531b52d0954c18b](https://github.com/Jiayi-Pan/TinyZero/commit/95df88f2dcb05f33bd18da546531b52d0954c18b)

**Tree at this commit:** [Jiayi-Pan/TinyZero@95df88f2dcb0](https://github.com/Jiayi-Pan/TinyZero/tree/95df88f2dcb05f33bd18da546531b52d0954c18b)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Jiayi-Pan/TinyZero |
| Description | Minimal reproduction of DeepSeek R1-Zero |
| Stars | 13256 |
| Forks | 1571 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `95df88f2dcb05f33bd18da546531b52d0954c18b` |
| Retrieved at | 2026-11-14T19:09:53.279128+00:00 |
| Files in this snapshot | 304 |

## Directory tree

```text
.github/  (8 files)
  workflows/  (8 files)
    dataset.yml
    e2e_digit_completion.yml
    e2e_gsm8k.yml
    model.yml
    ray_test.yml
    sanity.yml
    vllm.yml
    yapf_format.yml
docker/  (2 files)
  Dockerfile.ngc.vllm
  Dockerfile.vemlp.vllm.te
docs/  (21 files)
  advance/  (4 files)
    dpo_extension.rst
    fsdp_extension.rst
    megatron_extension.rst
    placement.rst
  examples/  (3 files)
    config.rst
    gsm8k_example.rst
    ppo_code_architecture.rst
  experiment/  (1 files)
    ppo.rst
  faq/  (1 files)
    faq.rst
  preparation/  (2 files)
    prepare_data.rst
    reward_function.rst
  start/  (2 files)
    install.rst
    quickstart.rst
  workers/  (3 files)
    fsdp_workers.rst
    megatron_workers.rst
    ray_trainer.rst
  Makefile
  README.md
  conf.py
  index.rst
  requirements-docs.txt
examples/  (32 files)
  data_preprocess/  (7 files)
    arth.py
    countdown.py
    full_hh_rlhf.py
    gsm8k.py
    hellaswag.py
    math_dataset.py
    multiply.py
  generation/  (1 files)
    run_deepseek_v2_lite_math.sh
  grpo_trainer/  (4 files)
    run_deepseek7b_llm.sh
    run_deepseek7b_llm_seq_balance.sh
    run_qwen2-7b.sh
    run_qwen2-7b_seq_balance.sh
  ppo_trainer/  (11 files)
    run_deepseek7b_llm.sh
    run_deepseek7b_llm_sp2.sh
    run_deepseek_full_hh_rlhf.sh
    run_deepseek_math_gsm8k_megatron.sh
    run_deepseek_megatron.sh
    run_gemma.sh
    run_qwen2-7b.sh
    run_qwen2-7b_rm.sh
    run_qwen2-7b_rm_seq_balance.sh
    run_qwen2-7b_seq_balance.sh
    run_qwen2.5-32b.sh
  ray/  (1 files)
    tutorial.ipynb
  sft/  (3 files)
    gsm8k/  (3 files)
      … 3 files under this directory
  split_placement/  (5 files)
    config/  (1 files)
      … 1 files under this directory
    README.md
    main_ppo_split.py
    run_deepseek7b_llm.sh
    split_monkey_patch.py
patches/  (1 files)
  megatron_v4.patch
scripts/  (2 files)
  format.sh
  train_tiny_zero.sh
tests/  (50 files)
  e2e/  (22 files)
    arithmetic_sequence/  (8 files)
      … 8 files under this directory
    envs/  (4 files)
      … 4 files under this directory
    __init__.py
    check_results.py
    run_qwen_gsm8k_function_rm.sh
    run_qwen_gsm8k_function_rm_no_rmpad.sh
    run_qwen_gsm8k_model_rm.sh
    run_qwen_gsm8k_model_rm_no_rmpad.sh
    run_qwen_gsm8k_model_rm_seq_balance.sh
    run_qwen_gsm8k_model_rm_ulysses.sh
    run_ray_trainer.sh
    run_ray_trainer_rmpad.sh
  gpu_utility/  (3 files)
    test_memory_buffers.py
    test_ops.py
    test_torch_functional.py
  model/  (2 files)
    test_transformer.py
    test_transformers_ulysses.py
  ray/  (14 files)
    check_worker_alive/  (1 files)
      … 1 files under this directory
    detached_worker/  (4 files)
      … 4 files under this directory
    test_check_worker_alive.py
    test_colocated_workers.py
    test_data_transfer.py
    test_driverfunc_to_worker.py
    test_high_level_scheduling_api.py
    test_ray_local_envs.py
    test_rvdz.py
    test_worker_group_basics.py
    test_worker_group_torch.py
  rollout/  (2 files)
    run_fsdp_vllm.py
    test_vllm_hf_loader.py
  sanity/  (2 files)
    check_license.py
    test_import.py
  utility/  (1 files)
    test_tensor_dict_utilities.py
  verl/  (3 files)
    utils/  (3 files)
      … 3 files under this directory
  __init__.py
verl/  (178 files)
  models/  (20 files)
    llama/  (12 files)
      … 12 files under this directory
    transformers/  (4 files)
      … 4 files under this directory
    README.md
    __init__.py
    registry.py
    weight_loader_registry.py
  single_controller/  (14 files)
    base/  (9 files)
      … 9 files under this directory
    ray/  (3 files)
      … 3 files under this directory
    version/  (1 files)
      … 1 files under this directory
    __init__.py
  third_party/  (55 files)
    vllm/  (54 files)
      … 54 files under this directory
    __init__.py
  trainer/  (14 files)
    config/  (5 files)
      … 5 files under this directory
    ppo/  (3 files)
      … 3 files under this directory
    __init__.py
    fsdp_sft_trainer.py
    main_eval.py
    main_generation.py
    main_ppo.py
    runtime_env.yaml
  utils/  (44 files)
    dataset/  (5 files)
      … 5 files under this directory
    debug/  (3 files)
      … 3 files under this directory
    logger/  (2 files)
      … 2 files under this directory
    megatron/  (7 files)
      … 7 files under this directory
    rendezvous/  (2 files)
      … 2 files under this directory
    reward_score/  (5 files)
      … 5 files under this directory
    __init__.py
    config.py
    distributed.py
    flops_counter.py
    fs.py
    fsdp_utils.py
    hdfs_io.py
    import_utils.py
    logging_utils.py
    megatron_utils.py
    memory_buffer.py
    model.py
    py_functional.py
    ray_utils.py
    seqlen_balancing.py
    tokenizer.py
    torch_dtypes.py
    torch_functional.py
    tracking.py
    ulysses.py
  version/  (1 files)
    version
  workers/  (28 files)
    actor/  (4 files)
      … 4 files under this directory
    critic/  (4 files)
      … 4 files under this directory
    reward_model/  (4 files)
      … 4 files under this directory
    rollout/  (8 files)
      … 8 files under this directory
    sharding_manager/  (5 files)
      … 5 files under this directory
    __init__.py
    fsdp_workers.py
    megatron_workers.py
  __init__.py
  protocol.py
.gitignore
.readthedocs.yaml
.style.yapf
LICENSE
Notice.txt
OLD_README.md
README.md
pyproject.toml
requirements.txt
setup.py
```

## Entry points

- [verl/trainer/fsdp_sft_trainer.py:368](https://github.com/Jiayi-Pan/TinyZero/blob/95df88f2dcb05f33bd18da546531b52d0954c18b/verl/trainer/fsdp_sft_trainer.py#L368)
- [verl/trainer/main_eval.py:68](https://github.com/Jiayi-Pan/TinyZero/blob/95df88f2dcb05f33bd18da546531b52d0954c18b/verl/trainer/main_eval.py#L68)
- [verl/trainer/main_generation.py:136](https://github.com/Jiayi-Pan/TinyZero/blob/95df88f2dcb05f33bd18da546531b52d0954c18b/verl/trainer/main_generation.py#L136)
- [verl/trainer/main_ppo.py:192](https://github.com/Jiayi-Pan/TinyZero/blob/95df88f2dcb05f33bd18da546531b52d0954c18b/verl/trainer/main_ppo.py#L192)
- [verl/utils/debug/trajectory_tracker.py:88](https://github.com/Jiayi-Pan/TinyZero/blob/95df88f2dcb05f33bd18da546531b52d0954c18b/verl/utils/debug/trajectory_tracker.py#L88)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 16 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: CacheConfig, DeviceConfig, LoRAConfig, LoadConfig, LoadFormat, ModelConfig. Observed… |
| Data layer | data | Observed | Groups 20 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: LambdaLayer, LlamaDynamicNTKScalingRotaryEmbedding, LlamaLinearScalingRotaryEmbedding, LlamaRotaryEmbe… |
| Application entry point | entrypoint | Observed | Groups 5 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: FSDPSFTTrainer, RewardManager, TrajectoryTracker. Observed top-level functions: _select_rm… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 2 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 50 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: Actor, CharTokenizer, Critic, DigitCompletion, DummyWorker, HackSelf. Observed top-level functions: add_one… |
| verl package | library | Observed | Groups 138 file(s) under verl package (observed from repository paths and static analysis). Observed top-level classes: ActorRolloutRefWorker, AdaptiveKLController, AllGatherPPModel, AsyncEngineArgs, BasePPOActor, BaseP… |

## Important files

- `.github/workflows/dataset.yml` (ci)
- `.github/workflows/e2e_digit_completion.yml` (ci)
- `.github/workflows/e2e_gsm8k.yml` (ci)
- `.github/workflows/model.yml` (ci)
- `.github/workflows/ray_test.yml` (ci)
- `.github/workflows/sanity.yml` (ci)
- `.github/workflows/vllm.yml` (ci)
- `.github/workflows/yapf_format.yml` (ci)
- `.readthedocs.yaml` (config)
- `docker/Dockerfile.ngc.vllm` (container)
- `docker/Dockerfile.vemlp.vllm.te` (container)
- `docs/requirements-docs.txt` (manifest)
- `examples/split_placement/config/ppo_trainer_split.yaml` (config)
- `pyproject.toml` (manifest)
- `requirements.txt` (manifest)
- `setup.py` (manifest)
- `verl/trainer/config/evaluation.yaml` (config)
- `verl/trainer/config/generation.yaml` (config)
- `verl/trainer/config/ppo_megatron_trainer.yaml` (config)
- `verl/trainer/config/ppo_trainer.yaml` (config)
- `verl/trainer/config/sft_trainer.yaml` (config)
- `verl/trainer/runtime_env.yaml` (config)

## Top-level layout

- `verl` — 178 analysed file(s)
- `tests` — 50 analysed file(s)
- `examples` — 32 analysed file(s)
- `docs` — 21 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `.github` — 8 analysed file(s)
- `docker` — 2 analysed file(s)
- `scripts` — 2 analysed file(s)
- `patches` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- File examples/data_preprocess/multiply.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `95df88f2dcb05f33bd18da546531b52d0954c18b` is the revision these paths and observations refer to.
