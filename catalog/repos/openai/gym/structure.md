# Project structure: openai/gym

**Analysed commit:** `bc212954b6713d5db303b3ead124de6cba66063e`

**Commit reference:** [bc212954b6713d5db303b3ead124de6cba66063e](https://github.com/openai/gym/commit/bc212954b6713d5db303b3ead124de6cba66063e)

**Tree at this commit:** [openai/gym@bc212954b671](https://github.com/openai/gym/tree/bc212954b6713d5db303b3ead124de6cba66063e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | openai/gym |
| Description | A toolkit for developing and comparing reinforcement learning algorithms. |
| Stars | 37236 |
| Forks | 8663 |
| Licence | Other |
| Language | Python |
| Default branch | master |
| Analysed commit | `bc212954b6713d5db303b3ead124de6cba66063e` |
| Retrieved at | 2026-11-14T19:06:54.203821+00:00 |
| Files in this snapshot | 219 |

## Directory tree

```text
.github/  (7 files)
  ISSUE_TEMPLATE/  (3 files)
    bug.md
    proposal.md
    question.md
  workflows/  (2 files)
    build.yml
    pre-commit.yml
  PULL_REQUEST_TEMPLATE.md
  stale.yml
bin/  (1 files)
  docker_entrypoint
gym/  (127 files)
  envs/  (63 files)
    box2d/  (5 files)
      … 5 files under this directory
    classic_control/  (7 files)
      … 7 files under this directory
    mujoco/  (43 files)
      … 43 files under this directory
    toy_text/  (6 files)
      … 6 files under this directory
    __init__.py
    registration.py
  spaces/  (12 files)
    __init__.py
    box.py
    dict.py
    discrete.py
    graph.py
    multi_binary.py
    multi_discrete.py
    sequence.py
    space.py
    text.py
    tuple.py
    utils.py
  utils/  (9 files)
    __init__.py
    colorize.py
    env_checker.py
    ezpickle.py
    passive_env_checker.py
    play.py
    save_video.py
    seeding.py
    step_api_compatibility.py
  vector/  (9 files)
    utils/  (5 files)
      … 5 files under this directory
    __init__.py
    async_vector_env.py
    sync_vector_env.py
    vector_env.py
  wrappers/  (28 files)
    monitoring/  (2 files)
      … 2 files under this directory
    README.md
    __init__.py
    atari_preprocessing.py
    autoreset.py
    clip_action.py
    compatibility.py
    env_checker.py
    filter_observation.py
    flatten_observation.py
    frame_stack.py
    gray_scale_observation.py
    human_rendering.py
    normalize.py
    order_enforcing.py
    pixel_observation.py
    record_episode_statistics.py
    record_video.py
    render_collection.py
    rescale_action.py
    resize_observation.py
    step_api_compatibility.py
    time_aware_observation.py
    time_limit.py
    transform_observation.py
    … 2 more files
  __init__.py
  core.py
  error.py
  logger.py
  py.typed
  version.py
tests/  (73 files)
  envs/  (11 files)
    __init__.py
    test_action_dim_check.py
    test_compatibility.py
    test_env_implementation.py
    test_envs.py
    test_make.py
    test_mujoco.py
    test_register.py
    test_spec.py
    utils.py
    utils_envs.py
  spaces/  (14 files)
    __init__.py
    test_box.py
    test_dict.py
    test_discrete.py
    test_graph.py
    test_multibinary.py
    test_multidiscrete.py
    test_sequence.py
    test_space.py
    test_spaces.py
    test_text.py
    test_tuple.py
    test_utils.py
    utils.py
  utils/  (7 files)
    __init__.py
    test_env_checker.py
    test_passive_env_checker.py
    test_play.py
    test_save_video.py
    test_seeding.py
    test_step_api_compatibility.py
  vector/  (11 files)
    __init__.py
    test_async_vector_env.py
    test_numpy_utils.py
    test_shared_memory.py
    test_spaces.py
    test_sync_vector_env.py
    test_vector_env.py
    test_vector_env_info.py
    test_vector_env_wrapper.py
    test_vector_make.py
    utils.py
  wrappers/  (27 files)
    __init__.py
    test_atari_preprocessing.py
    test_autoreset.py
    test_clip_action.py
    test_filter_observation.py
    test_flatten.py
    test_flatten_observation.py
    test_frame_stack.py
    test_gray_scale_observation.py
    test_human_rendering.py
    test_nested_dict.py
    test_normalize.py
    test_order_enforcing.py
    test_passive_env_checker.py
    test_pixel_observation.py
    test_record_episode_statistics.py
    test_record_video.py
    test_rescale_action.py
    test_resize_observation.py
    test_step_compatibility.py
    test_time_aware_observation.py
    test_time_limit.py
    test_transform_observation.py
    test_transform_reward.py
    … 3 more files
  __init__.py
  test_core.py
  testing_env.py
.gitignore
.pre-commit-config.yaml
CODE_OF_CONDUCT.rst
CONTRIBUTING.md
LICENSE.md
README.md
py.Dockerfile
pyproject.toml
requirements.txt
setup.py
test_requirements.txt
```

## Entry points

- [gym/envs/box2d/bipedal_walker.py:776](https://github.com/openai/gym/blob/bc212954b6713d5db303b3ead124de6cba66063e/gym/envs/box2d/bipedal_walker.py#L776)
- [gym/envs/box2d/car_racing.py:777](https://github.com/openai/gym/blob/bc212954b6713d5db303b3ead124de6cba66063e/gym/envs/box2d/car_racing.py#L777)
- [gym/envs/box2d/lunar_lander.py:816](https://github.com/openai/gym/blob/bc212954b6713d5db303b3ead124de6cba66063e/gym/envs/box2d/lunar_lander.py#L816)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 3 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: BipedalWalker, BipedalWalkerHardcore, CarRacing, ContactDetector, FrictionDetector, LunarL… |
| gym package | library | Observed | Groups 110 file(s) under gym package (observed from repository paths and static analysis). Observed top-level classes: APIConnectionError, APIError, AcrobotEnv, ActionWrapper, AlreadyPendingCallError, AntEnv. Observed t… |
| Tests | test | Observed | Groups 74 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: AleTesting, ArgumentEnv, AtariTestingEnv, BrokenRecordableEnv, CustomSpace, CustomSpaceEnv. Observed top-le… |

## Important files

- `.github/stale.yml` (config)
- `.github/workflows/build.yml` (ci)
- `.github/workflows/pre-commit.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `pyproject.toml` (manifest)
- `requirements.txt` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `gym` — 127 analysed file(s)
- `tests` — 73 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `.github` — 7 analysed file(s)
- `bin` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- The GitHub repository was marked archived at selection time.

Commit `bc212954b6713d5db303b3ead124de6cba66063e` is the revision these paths and observations refer to.
