# Project structure: openai/baselines

**Analysed commit:** `ea25b9e8b234e6ee1bca43083f8f3cf974143998`

**Commit reference:** [ea25b9e8b234e6ee1bca43083f8f3cf974143998](https://github.com/openai/baselines/commit/ea25b9e8b234e6ee1bca43083f8f3cf974143998)

**Tree at this commit:** [openai/baselines@ea25b9e8b234](https://github.com/openai/baselines/tree/ea25b9e8b234e6ee1bca43083f8f3cf974143998)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | openai/baselines |
| Description | OpenAI Baselines: high-quality implementations of reinforcement learning algorithms |
| Stars | 16780 |
| Forks | 4916 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `ea25b9e8b234e6ee1bca43083f8f3cf974143998` |
| Retrieved at | 2026-11-14T19:08:44.173915+00:00 |
| Files in this snapshot | 169 |

## Directory tree

```text
baselines/  (160 files)
  a2c/  (5 files)
    README.md
    __init__.py
    a2c.py
    runner.py
    utils.py
  acer/  (7 files)
    README.md
    __init__.py
    acer.py
    buffer.py
    defaults.py
    policies.py
    runner.py
  acktr/  (7 files)
    README.md
    __init__.py
    acktr.py
    defaults.py
    kfac.py
    kfac_utils.py
    utils.py
  bench/  (4 files)
    __init__.py
    benchmarks.py
    monitor.py
    test_monitor.py
  common/  (61 files)
    tests/  (20 files)
      … 20 files under this directory
    vec_env/  (13 files)
      … 13 files under this directory
    __init__.py
    atari_wrappers.py
    cg.py
    cmd_util.py
    console_util.py
    dataset.py
    distributions.py
    input.py
    math_util.py
    misc_util.py
    models.py
    mpi_adam.py
    mpi_adam_optimizer.py
    mpi_fork.py
    mpi_moments.py
    mpi_running_mean_std.py
    mpi_util.py
    plot_util.py
    policies.py
    retro_wrappers.py
    runners.py
    running_mean_std.py
    schedules.py
    segment_tree.py
    … 4 more files
  ddpg/  (8 files)
    README.md
    __init__.py
    ddpg.py
    ddpg_learner.py
    memory.py
    models.py
    noise.py
    test_smoke.py
  deepq/  (16 files)
    experiments/  (8 files)
      … 8 files under this directory
    README.md
    __init__.py
    build_graph.py
    deepq.py
    defaults.py
    models.py
    replay_buffer.py
    utils.py
  gail/  (12 files)
    dataset/  (2 files)
      … 2 files under this directory
    result/  (1 files)
      … 1 files under this directory
    README.md
    __init__.py
    adversary.py
    behavior_clone.py
    gail-eval.py
    mlp_policy.py
    run_mujoco.py
    statistics.py
    trpo_mpi.py
  her/  (15 files)
    experiment/  (5 files)
      … 5 files under this directory
    README.md
    __init__.py
    actor_critic.py
    ddpg.py
    her.py
    her_sampler.py
    normalizer.py
    replay_buffer.py
    rollout.py
    util.py
  ppo1/  (9 files)
    README.md
    __init__.py
    cnn_policy.py
    mlp_policy.py
    pposgd_simple.py
    run_atari.py
    run_humanoid.py
    run_mujoco.py
    run_robotics.py
  ppo2/  (8 files)
    README.md
    __init__.py
    defaults.py
    microbatched_model.py
    model.py
    ppo2.py
    runner.py
    test_microbatches.py
  trpo_mpi/  (4 files)
    README.md
    __init__.py
    defaults.py
    trpo_mpi.py
  __init__.py
  logger.py
  results_plotter.py
  run.py
.benchmark_pattern
.gitignore
.travis.yml
Dockerfile
LICENSE
README.md
benchmarks_mujoco1M.htm
setup.cfg
setup.py
```

## Entry points

- [baselines/common/mpi_adam.py:102](https://github.com/openai/baselines/blob/ea25b9e8b234e6ee1bca43083f8f3cf974143998/baselines/common/mpi_adam.py#L102)
- [baselines/common/mpi_running_mean_std.py:110](https://github.com/openai/baselines/blob/ea25b9e8b234e6ee1bca43083f8f3cf974143998/baselines/common/mpi_running_mean_std.py#L110)
- [baselines/common/running_mean_std.py:186](https://github.com/openai/baselines/blob/ea25b9e8b234e6ee1bca43083f8f3cf974143998/baselines/common/running_mean_std.py#L186)
- [baselines/deepq/experiments/custom_cartpole.py:25](https://github.com/openai/baselines/blob/ea25b9e8b234e6ee1bca43083f8f3cf974143998/baselines/deepq/experiments/custom_cartpole.py#L25)
- [baselines/deepq/experiments/enjoy_cartpole.py:20](https://github.com/openai/baselines/blob/ea25b9e8b234e6ee1bca43083f8f3cf974143998/baselines/deepq/experiments/enjoy_cartpole.py#L20)
- [baselines/deepq/experiments/enjoy_mountaincar.py:26](https://github.com/openai/baselines/blob/ea25b9e8b234e6ee1bca43083f8f3cf974143998/baselines/deepq/experiments/enjoy_mountaincar.py#L26)
- [baselines/deepq/experiments/enjoy_pong.py:27](https://github.com/openai/baselines/blob/ea25b9e8b234e6ee1bca43083f8f3cf974143998/baselines/deepq/experiments/enjoy_pong.py#L27)
- [baselines/deepq/experiments/train_cartpole.py:29](https://github.com/openai/baselines/blob/ea25b9e8b234e6ee1bca43083f8f3cf974143998/baselines/deepq/experiments/train_cartpole.py#L29)
- [baselines/deepq/experiments/train_mountaincar.py:25](https://github.com/openai/baselines/blob/ea25b9e8b234e6ee1bca43083f8f3cf974143998/baselines/deepq/experiments/train_mountaincar.py#L25)
- [baselines/deepq/experiments/train_pong.py:33](https://github.com/openai/baselines/blob/ea25b9e8b234e6ee1bca43083f8f3cf974143998/baselines/deepq/experiments/train_pong.py#L33)
- [baselines/gail/behavior_clone.py:122](https://github.com/openai/baselines/blob/ea25b9e8b234e6ee1bca43083f8f3cf974143998/baselines/gail/behavior_clone.py#L122)
- [baselines/gail/dataset/mujoco_dset.py:107](https://github.com/openai/baselines/blob/ea25b9e8b234e6ee1bca43083f8f3cf974143998/baselines/gail/dataset/mujoco_dset.py#L107)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| baselines package | library | Observed | Groups 94 file(s) under baselines package (observed from repository paths and static analysis). Observed top-level classes: AbstractEnvRunner, Acer, AcerCnnPolicy, AcerLstmPolicy, ActWrapper, ActionNoise. Observed top-l… |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: cached_make_env, configure_ddpg, configure_dims, configure_her, log_params, prepare… |
| Data layer | data | Observed | Groups 4 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: Actor, Critic, Model. Observed top-level functions: _normalize_clip_observation, build_impala_cnn, buil… |
| Application entry point | entrypoint | Observed | Groups 24 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: CSVOutputFormat, Dset, HumanOutputFormat, JSONOutputFormat, KVWriter, Logger. Observed to… |
| Tests | test | Observed | Groups 26 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: BoxIdentityEnv, DiscreteIdentityEnv, FixedSequenceEnv, IdentityEnv, MnistEnv, MultiDiscreteIdentityEnv. Obs… |

## Important files

- `.travis.yml` (ci)
- `Dockerfile` (container)
- `setup.cfg` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `baselines` — 160 analysed file(s)
- `(root files)` — 9 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `ea25b9e8b234e6ee1bca43083f8f3cf974143998` is the revision these paths and observations refer to.
