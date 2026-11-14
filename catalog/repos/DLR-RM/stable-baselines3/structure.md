# Project structure: DLR-RM/stable-baselines3

**Analysed commit:** `0cdcd200deef06b9ad0af72f6ddfb07c06c6df39`

**Commit reference:** [0cdcd200deef06b9ad0af72f6ddfb07c06c6df39](https://github.com/DLR-RM/stable-baselines3/commit/0cdcd200deef06b9ad0af72f6ddfb07c06c6df39)

**Tree at this commit:** [DLR-RM/stable-baselines3@0cdcd200deef](https://github.com/DLR-RM/stable-baselines3/tree/0cdcd200deef06b9ad0af72f6ddfb07c06c6df39)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | DLR-RM/stable-baselines3 |
| Description | PyTorch version of Stable Baselines, reliable implementations of reinforcement learning algorithms.  |
| Stars | 14012 |
| Forks | 2183 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `0cdcd200deef06b9ad0af72f6ddfb07c06c6df39` |
| Retrieved at | 2026-11-14T19:09:35.343601+00:00 |
| Files in this snapshot | 173 |

## Directory tree

```text
.github/  (8 files)
  ISSUE_TEMPLATE/  (5 files)
    bug_report.yml
    custom_env.yml
    documentation.yml
    feature_request.yml
    question.yml
  workflows/  (2 files)
    ci.yml
    pypi-publish.yml
  PULL_REQUEST_TEMPLATE.md
docs/  (52 files)
  _static/  (3 files)
    css/  (1 files)
      … 1 files under this directory
    img/  (2 files)
      … 2 files under this directory
  common/  (10 files)
    atari_wrappers.md
    distributions.md
    env_checker.md
    env_util.md
    envs.md
    evaluation.md
    logger.md
    monitor.md
    noise.md
    utils.md
  guide/  (22 files)
    algos.md
    callbacks.md
    checking_nan.md
    custom_env.md
    custom_policy.md
    developer.md
    examples.md
    export.md
    imitation.md
    install.md
    integrations.md
    migration.md
    plotting.md
    quickstart.md
    rl.md
    rl_tips.md
    rl_zoo.md
    save_format.md
    sb3_contrib.md
    sbx.md
    tensorboard.md
    vec_envs.md
  misc/  (2 files)
    changelog.md
    projects.md
  modules/  (8 files)
    a2c.md
    base.md
    ddpg.md
    dqn.md
    her.md
    ppo.md
    sac.md
    td3.md
  Makefile
  README.md
  conda_env.yml
  conf.py
  index.rst
  make.bat
  spelling_wordlist.txt
scripts/  (4 files)
  build_docker.sh
  run_docker_cpu.sh
  run_docker_gpu.sh
  run_tests.sh
stable_baselines3/  (66 files)
  a2c/  (3 files)
    __init__.py
    a2c.py
    policies.py
  common/  (42 files)
    envs/  (4 files)
      … 4 files under this directory
    sb2_compat/  (2 files)
      … 2 files under this directory
    vec_env/  (14 files)
      … 14 files under this directory
    __init__.py
    atari_wrappers.py
    base_class.py
    buffers.py
    callbacks.py
    distributions.py
    env_checker.py
    env_util.py
    evaluation.py
    logger.py
    monitor.py
    noise.py
    off_policy_algorithm.py
    on_policy_algorithm.py
    policies.py
    preprocessing.py
    results_plotter.py
    running_mean_std.py
    save_util.py
    torch_layers.py
    type_aliases.py
    utils.py
  ddpg/  (3 files)
    __init__.py
    ddpg.py
    policies.py
  dqn/  (3 files)
    __init__.py
    dqn.py
    policies.py
  her/  (3 files)
    __init__.py
    goal_selection_strategy.py
    her_replay_buffer.py
  ppo/  (3 files)
    __init__.py
    policies.py
    ppo.py
  sac/  (3 files)
    __init__.py
    policies.py
    sac.py
  td3/  (3 files)
    __init__.py
    policies.py
    td3.py
  __init__.py
  py.typed
  version.txt
tests/  (31 files)
  __init__.py
  test_buffers.py
  test_callbacks.py
  test_cnn.py
  test_custom_policy.py
  test_deterministic.py
  test_dict_env.py
  test_distributions.py
  test_env_checker.py
  test_envs.py
  test_gae.py
  test_her.py
  test_identity.py
  test_logger.py
  test_monitor.py
  test_n_step_replay.py
  test_predict.py
  test_preprocessing.py
  test_run.py
  test_save_load.py
  test_sde.py
  test_spaces.py
  test_tensorboard.py
  test_train_eval_mode.py
  … 7 more files
.gitignore
.readthedocs.yml
CITATION.bib
CODE_OF_CONDUCT.md
CONTRIBUTING.md
Dockerfile
LICENSE
Makefile
NOTICE
README.md
pyproject.toml
setup.py
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 4 file(s) under scripts package (observed from repository paths and static analysis). |
| stable_baselines3 package | library | Observed | Groups 64 file(s) under stable_baselines3 package (observed from repository paths and static analysis). Observed top-level classes: A2C, ActionNoise, Actor, ActorCriticCnnPolicy, ActorCriticPolicy, AtariWrapper. Observe… |
| Tests | test | Observed | Groups 31 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: ActionDictTestEnv, AlwaysDoneWrapper, AlwaysFailCallback, CheckGAECallback, CustomEnv, CustomGymEnv. Observ… |

## Important files

- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/custom_env.yml` (config)
- `.github/ISSUE_TEMPLATE/documentation.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/ISSUE_TEMPLATE/question.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/pypi-publish.yml` (ci)
- `.readthedocs.yml` (config)
- `Dockerfile` (container)
- `docs/conda_env.yml` (config)
- `pyproject.toml` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `stable_baselines3` — 66 analysed file(s)
- `docs` — 52 analysed file(s)
- `tests` — 31 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `.github` — 8 analysed file(s)
- `scripts` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `0cdcd200deef06b9ad0af72f6ddfb07c06c6df39` is the revision these paths and observations refer to.
