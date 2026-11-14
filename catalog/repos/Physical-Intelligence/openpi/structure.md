# Project structure: Physical-Intelligence/openpi

**Analysed commit:** `215abfb217dbac7d5f1273282331b9b1866c0479`

**Commit reference:** [215abfb217dbac7d5f1273282331b9b1866c0479](https://github.com/Physical-Intelligence/openpi/commit/215abfb217dbac7d5f1273282331b9b1866c0479)

**Tree at this commit:** [Physical-Intelligence/openpi@215abfb217db](https://github.com/Physical-Intelligence/openpi/tree/215abfb217dbac7d5f1273282331b9b1866c0479)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Physical-Intelligence/openpi |
| Description | Not provided |
| Stars | 14648 |
| Forks | 2644 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `215abfb217dbac7d5f1273282331b9b1866c0479` |
| Retrieved at | 2026-11-14T19:09:21.987206+00:00 |
| Files in this snapshot | 139 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (2 files)
    pre-commit.yml
    test.yml
  CODEOWNERS
.vscode/  (1 files)
  settings.json
docs/  (3 files)
  docker.md
  norm_stats.md
  remote_inference.md
examples/  (42 files)
  aloha_real/  (12 files)
    Dockerfile
    README.md
    compose.yml
    constants.py
    convert_aloha_data_to_lerobot.py
    env.py
    main.py
    real_env.py
    requirements.in
    requirements.txt
    robot_utils.py
    video_display.py
  aloha_sim/  (8 files)
    Dockerfile
    README.md
    compose.yml
    env.py
    main.py
    requirements.in
    requirements.txt
    saver.py
  droid/  (5 files)
    README.md
    README_train.md
    compute_droid_nonidle_ranges.py
    convert_droid_data_to_lerobot.py
    main.py
  libero/  (7 files)
    Dockerfile
    README.md
    compose.yml
    convert_libero_data_to_lerobot.py
    main.py
    requirements.in
    requirements.txt
  simple_client/  (6 files)
    Dockerfile
    README.md
    compose.yml
    main.py
    requirements.in
    requirements.txt
  ur5/  (1 files)
    README.md
  convert_jax_model_to_pytorch.py
  inference.ipynb
  policy_records.ipynb
packages/  (14 files)
  openpi-client/  (14 files)
    src/  (13 files)
      … 13 files under this directory
    pyproject.toml
scripts/  (10 files)
  docker/  (4 files)
    compose.yml
    install_docker_ubuntu22.sh
    install_nvidia_container_toolkit.sh
    serve_policy.Dockerfile
  __init__.py
  compute_norm_stats.py
  serve_policy.py
  train.py
  train_pytorch.py
  train_test.py
src/  (56 files)
  openpi/  (56 files)
    models/  (16 files)
      … 16 files under this directory
    models_pytorch/  (8 files)
      … 8 files under this directory
    policies/  (6 files)
      … 6 files under this directory
    serving/  (1 files)
      … 1 files under this directory
    shared/  (9 files)
      … 9 files under this directory
    training/  (11 files)
      … 11 files under this directory
    __init__.py
    conftest.py
    py.typed
    transforms.py
    transforms_test.py
.dockerignore
.gitignore
.gitmodules
.pre-commit-config.yaml
.python-version
CONTRIBUTING.md
LICENSE
LICENSE_GEMMA.txt
README.md
pyproject.toml
```

## Entry points

- [src/openpi/training/config.py:259](https://github.com/Physical-Intelligence/openpi/blob/215abfb217dbac7d5f1273282331b9b1866c0479/src/openpi/training/config.py#L259)
- [scripts/compute_norm_stats.py:116](https://github.com/Physical-Intelligence/openpi/blob/215abfb217dbac7d5f1273282331b9b1866c0479/scripts/compute_norm_stats.py#L116)
- [scripts/serve_policy.py:120](https://github.com/Physical-Intelligence/openpi/blob/215abfb217dbac7d5f1273282331b9b1866c0479/scripts/serve_policy.py#L120)
- [scripts/train.py:279](https://github.com/Physical-Intelligence/openpi/blob/215abfb217dbac7d5f1273282331b9b1866c0479/scripts/train.py#L279)
- [scripts/train_pytorch.py:631](https://github.com/Physical-Intelligence/openpi/blob/215abfb217dbac7d5f1273282331b9b1866c0479/scripts/train_pytorch.py#L631)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 17 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AddPositionEmbs, Attention, BaseModel, BaseModelConfig, BinningTokenizer, Block. Observed top-level fu… |
| Application entry point | entrypoint | Observed | Groups 5 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Group. Observed top-level classes: Args, AssetsConfig, Checkpoint, DataConfig,… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| openpi package | library | Observed | Groups 26 file(s) under openpi package (observed from repository paths and static analysis). Observed top-level classes: AbsoluteActions, AdamW, AlohaInputs, AlohaOutputs, Callback, CallbackHandler. Observed top-level f… |
| packages package | library | Observed | Groups 11 file(s) under packages package (observed from repository paths and static analysis). Observed top-level classes: ActionChunkBroker, Agent, BasePolicy, Environment, PolicyAgent, Runtime. Observed top-level func… |
| scripts package | library | Observed | Groups 3 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 14 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: _check, _get_frozen_state, pytest_configure, set_jax_cpu_backend_if_no_gpu, set_openpi_data_home, test_ab… |

## Important files

- `.dockerignore` (container)
- `.github/workflows/pre-commit.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `.vscode/settings.json` (config)
- `examples/aloha_real/Dockerfile` (container)
- `examples/aloha_real/compose.yml` (container)
- `examples/aloha_real/requirements.txt` (manifest)
- `examples/aloha_sim/Dockerfile` (container)
- `examples/aloha_sim/compose.yml` (container)
- `examples/aloha_sim/requirements.txt` (manifest)
- `examples/libero/Dockerfile` (container)
- `examples/libero/compose.yml` (container)
- `examples/libero/requirements.txt` (manifest)
- `examples/simple_client/Dockerfile` (container)
- `examples/simple_client/compose.yml` (container)
- `examples/simple_client/requirements.txt` (manifest)
- `packages/openpi-client/pyproject.toml` (manifest)
- `pyproject.toml` (manifest)
- `scripts/docker/compose.yml` (container)

## Top-level layout

- `src` — 56 analysed file(s)
- `examples` — 42 analysed file(s)
- `packages` — 14 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `scripts` — 10 analysed file(s)
- `.github` — 3 analysed file(s)
- `docs` — 3 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `215abfb217dbac7d5f1273282331b9b1866c0479` is the revision these paths and observations refer to.
