# Project structure: openai/spinningup

**Analysed commit:** `038665d62d569055401d91856abb287263096178`

**Commit reference:** [038665d62d569055401d91856abb287263096178](https://github.com/openai/spinningup/commit/038665d62d569055401d91856abb287263096178)

**Tree at this commit:** [openai/spinningup@038665d62d56](https://github.com/openai/spinningup/tree/038665d62d569055401d91856abb287263096178)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | openai/spinningup |
| Description | An educational resource to help anyone learn deep reinforcement learning. |
| Stars | 12040 |
| Forks | 2460 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `038665d62d569055401d91856abb287263096178` |
| Retrieved at | 2026-11-14T19:10:16.909131+00:00 |
| Files in this snapshot | 151 |

## Directory tree

```text
docs/  (78 files)
  _static/  (1 files)
    css/  (1 files)
      … 1 files under this directory
  algorithms/  (6 files)
    ddpg.rst
    ppo.rst
    sac.rst
    td3.rst
    trpo.rst
    vpg.rst
  etc/  (2 files)
    acknowledgements.rst
    author.rst
  images/  (36 files)
    plots/  (30 files)
      … 30 files under this directory
    ex2-2_ddpg_bug.svg
    rl_algorithms.svg
    rl_algorithms.xml
    rl_algorithms_9_15.svg
    rl_algorithms_9_15.xml
    spinning-up-logo.svg
  spinningup/  (18 files)
    bench.rst
    bench_ddpg.rst
    bench_ppo.rst
    bench_sac.rst
    bench_td3.rst
    bench_vpg.rst
    exercise2_1_soln.rst
    exercise2_2_soln.rst
    exercises.rst
    extra_pg_proof1.rst
    extra_pg_proof2.rst
    extra_tf_pg_implementation.rst
    keypapers.rst
    rl_intro.rst
    rl_intro2.rst
    rl_intro3.rst
    rl_intro4.rst
    spinningup.rst
  user/  (6 files)
    algorithms.rst
    installation.rst
    introduction.rst
    plotting.rst
    running.rst
    saving_and_loading.rst
  utils/  (4 files)
    logger.rst
    mpi.rst
    plotter.rst
    run_utils.rst
  Makefile
  conf.py
  docs_requirements.txt
  index.rst
  make.bat
spinup/  (65 files)
  algos/  (30 files)
    pytorch/  (11 files)
      … 11 files under this directory
    tf1/  (18 files)
      … 18 files under this directory
    __init__.py
  examples/  (7 files)
    pytorch/  (3 files)
      … 3 files under this directory
    tf1/  (4 files)
      … 4 files under this directory
  exercises/  (14 files)
    pytorch/  (7 files)
      … 7 files under this directory
    tf1/  (6 files)
      … 6 files under this directory
    common.py
  utils/  (10 files)
    __init__.py
    logx.py
    mpi_pytorch.py
    mpi_tf.py
    mpi_tools.py
    plot.py
    run_entrypoint.py
    run_utils.py
    serialization_utils.py
    test_policy.py
  __init__.py
  run.py
  user_config.py
  version.py
test/  (1 files)
  test_ppo.py
.gitignore
.travis.yml
LICENSE
readme.md
readthedocs.yml
setup.py
travis_setup.sh
```

## Entry points

- [spinup/algos/pytorch/ddpg/ddpg.py:309](https://github.com/openai/spinningup/blob/038665d62d569055401d91856abb287263096178/spinup/algos/pytorch/ddpg/ddpg.py#L309)
- [spinup/algos/pytorch/ppo/ppo.py:356](https://github.com/openai/spinningup/blob/038665d62d569055401d91856abb287263096178/spinup/algos/pytorch/ppo/ppo.py#L356)
- [spinup/algos/pytorch/sac/sac.py:350](https://github.com/openai/spinningup/blob/038665d62d569055401d91856abb287263096178/spinup/algos/pytorch/sac/sac.py#L350)
- [spinup/algos/pytorch/td3/td3.py:350](https://github.com/openai/spinningup/blob/038665d62d569055401d91856abb287263096178/spinup/algos/pytorch/td3/td3.py#L350)
- [spinup/algos/pytorch/vpg/vpg.py:328](https://github.com/openai/spinningup/blob/038665d62d569055401d91856abb287263096178/spinup/algos/pytorch/vpg/vpg.py#L328)
- [spinup/algos/tf1/ddpg/ddpg.py:289](https://github.com/openai/spinningup/blob/038665d62d569055401d91856abb287263096178/spinup/algos/tf1/ddpg/ddpg.py#L289)
- [spinup/algos/tf1/ppo/ppo.py:303](https://github.com/openai/spinningup/blob/038665d62d569055401d91856abb287263096178/spinup/algos/tf1/ppo/ppo.py#L303)
- [spinup/algos/tf1/sac/sac.py:315](https://github.com/openai/spinningup/blob/038665d62d569055401d91856abb287263096178/spinup/algos/tf1/sac/sac.py#L315)
- [spinup/algos/tf1/td3/td3.py:315](https://github.com/openai/spinningup/blob/038665d62d569055401d91856abb287263096178/spinup/algos/tf1/td3/td3.py#L315)
- [spinup/algos/tf1/trpo/trpo.py:381](https://github.com/openai/spinningup/blob/038665d62d569055401d91856abb287263096178/spinup/algos/tf1/trpo/trpo.py#L381)
- [spinup/algos/tf1/vpg/vpg.py:278](https://github.com/openai/spinningup/blob/038665d62d569055401d91856abb287263096178/spinup/algos/tf1/vpg/vpg.py#L278)
- [spinup/exercises/pytorch/problem_set_1/exercise1_1.py:34](https://github.com/openai/spinningup/blob/038665d62d569055401d91856abb287263096178/spinup/exercises/pytorch/problem_set_1/exercise1_1.py#L34)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 29 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: BuggedMLPActor, BuggedMLPActorCritic, BuggedMLPQFunction, DiagonalGaussianDistribution, G… |
| spinup package | library | Observed | Groups 35 file(s) under spinup package (observed from repository paths and static analysis). Observed top-level classes: Actor, DiagonalGaussianDistribution, EpochLogger, ExerciseActorCritic, ExperimentGrid, Logger. Obs… |
| Tests | test | Observed | Groups 2 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: TestPPO. Observed top-level functions: load_policy_and_env, load_pytorch_policy, load_tf_policy, run_policy. |

## Important files

- `.travis.yml` (ci)
- `readthedocs.yml` (config)
- `setup.py` (manifest)

## Top-level layout

- `docs` — 78 analysed file(s)
- `spinup` — 65 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `test` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `038665d62d569055401d91856abb287263096178` is the revision these paths and observations refer to.
