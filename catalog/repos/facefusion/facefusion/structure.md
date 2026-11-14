# Project structure: facefusion/facefusion

**Analysed commit:** `decc6c9d8f8e014878624452c6e8fe208726b4ec`

**Commit reference:** [decc6c9d8f8e014878624452c6e8fe208726b4ec](https://github.com/facefusion/facefusion/commit/decc6c9d8f8e014878624452c6e8fe208726b4ec)

**Tree at this commit:** [facefusion/facefusion@decc6c9d8f8e](https://github.com/facefusion/facefusion/tree/decc6c9d8f8e014878624452c6e8fe208726b4ec)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | facefusion/facefusion |
| Description | Industry leading face manipulation platform |
| Stars | 30672 |
| Forks | 5024 |
| Licence | Other |
| Language | Python |
| Default branch | master |
| Analysed commit | `decc6c9d8f8e014878624452c6e8fe208726b4ec` |
| Retrieved at | 2026-11-14T19:07:08.811815+00:00 |
| Files in this snapshot | 245 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (1 files)
    ci.yml
  FUNDING.yml
facefusion/  (184 files)
  jobs/  (6 files)
    __init__.py
    job_helper.py
    job_list.py
    job_manager.py
    job_runner.py
    job_store.py
  processors/  (61 files)
    modules/  (56 files)
      … 56 files under this directory
    __init__.py
    core.py
    live_portrait.py
    pixel_boost.py
    types.py
  uis/  (55 files)
    assets/  (1 files)
      … 1 files under this directory
    components/  (44 files)
      … 44 files under this directory
    layouts/  (4 files)
      … 4 files under this directory
    __init__.py
    choices.py
    core.py
    overrides.py
    types.py
    ui_helper.py
  workflows/  (6 files)
    __init__.py
    core.py
    image_to_image.py
    image_to_video.py
    to_image.py
    to_video.py
  __init__.py
  app_context.py
  args.py
  audio.py
  benchmarker.py
  camera_manager.py
  choices.py
  cli_helper.py
  common_helper.py
  conda.py
  config.py
  content_analyser.py
  core.py
  curl_builder.py
  download.py
  execution.py
  exit_helper.py
  face_classifier.py
  face_creator.py
  face_detector.py
  face_helper.py
  face_landmarker.py
  face_masker.py
  face_recognizer.py
  … 32 more files
tests/  (48 files)
  __init__.py
  helper.py
  test_audio.py
  test_cli_age_modifier.py
  test_cli_background_remover.py
  test_cli_batch_runner.py
  test_cli_expression_restorer.py
  test_cli_face_debugger.py
  test_cli_face_editor.py
  test_cli_face_enhancer.py
  test_cli_face_swapper.py
  test_cli_frame_colorizer.py
  test_cli_frame_enhancer.py
  test_cli_job_manager.py
  test_cli_job_runner.py
  test_cli_lip_syncer.py
  test_cli_output_fps.py
  test_cli_output_scale.py
  test_common_helper.py
  test_config.py
  test_curl_builder.py
  test_download.py
  test_execution.py
  test_face_creator.py
  … 24 more files
.coveragerc
.editorconfig
.flake8
.gitignore
LICENSE.md
README.md
facefusion.ini
facefusion.py
install.py
mypy.ini
requirements.txt
```

## Entry points

- [facefusion.py:9](https://github.com/facefusion/facefusion/blob/decc6c9d8f8e014878624452c6e8fe208726b4ec/facefusion.py#L9)
- [install.py:9](https://github.com/facefusion/facefusion/blob/decc6c9d8f8e014878624452c6e8fe208726b4ec/install.py#L9)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: get_bool_value, get_float_value, get_int_list, get_int_value, get_static_config_par… |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). |
| facefusion package | library | Observed | Groups 182 file(s) under facefusion package (observed from repository paths and static analysis). Observed top-level functions: __autoload__, add_step, adjust_inference_providers, analyse_frame, analyse_image, analyse_s… |
| Tests | test | Observed | Groups 48 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: adjust_module, before_all, before_each, clear_state, get_available_encoder_set, get_state. |

## Important files

- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `facefusion.ini` (config)
- `mypy.ini` (config)
- `requirements.txt` (manifest)

## Top-level layout

- `facefusion` — 184 analysed file(s)
- `tests` — 48 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `.github` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `decc6c9d8f8e014878624452c6e8fe208726b4ec` is the revision these paths and observations refer to.
