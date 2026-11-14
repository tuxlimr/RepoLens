# Project structure: nikopueringer/CorridorKey

**Analysed commit:** `97e55a453060745bead1befd293f6e523c4b845c`

**Commit reference:** [97e55a453060745bead1befd293f6e523c4b845c](https://github.com/nikopueringer/CorridorKey/commit/97e55a453060745bead1befd293f6e523c4b845c)

**Tree at this commit:** [nikopueringer/CorridorKey@97e55a453060](https://github.com/nikopueringer/CorridorKey/tree/97e55a453060745bead1befd293f6e523c4b845c)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | nikopueringer/CorridorKey |
| Description | Perfect Green Screen Keys |
| Stars | 15038 |
| Forks | 908 |
| Licence | Other |
| Language | Python |
| Default branch | main |
| Analysed commit | `97e55a453060745bead1befd293f6e523c4b845c` |
| Retrieved at | 2026-11-14T19:09:09.033514+00:00 |
| Files in this snapshot | 96 |

## Directory tree

```text
.github/  (4 files)
  ISSUE_TEMPLATE/  (1 files)
    bug_report.yml
  workflows/  (2 files)
    ci.yml
    docs.yml
  pull_request_template.md
BiRefNetModule/  (2 files)
  checkpoints/  (1 files)
    .gitkeep
  wrapper.py
ClipsForInference/  (1 files)
  .gitkeep
CorridorKeyModule/  (9 files)
  IgnoredCheckpoints/  (1 files)
    .gitkeep
  checkpoints/  (1 files)
    .gitkeep
  core/  (3 files)
    __init__.py
    color_utils.py
    model_transformer.py
  README.md
  __init__.py
  backend.py
  inference_engine.py
IgnoredClips/  (1 files)
  .gitkeep
Output/  (1 files)
  .gitkeep
VideoMaMaInferenceModule/  (6 files)
  checkpoints/  (1 files)
    .gitkeep
  LICENSE.md
  README.md
  __init__.py
  inference.py
  pipeline.py
backend/  (10 files)
  __init__.py
  clip_state.py
  errors.py
  ffmpeg_tools.py
  frame_io.py
  job_queue.py
  natural_sort.py
  project.py
  service.py
  validators.py
docs/  (2 files)
  LLM_HANDOVER.md
  index.md
gvm_core/  (11 files)
  gvm/  (6 files)
    models/  (2 files)
      … 2 files under this directory
    pipelines/  (1 files)
      … 1 files under this directory
    utils/  (2 files)
      … 2 files under this directory
    __init__.py
  weights/  (1 files)
    .gitkeep
  LICENSE.md
  README.md
  __init__.py
  wrapper.py
scripts/  (1 files)
  convert_pth_to_safetensors.py
tests/  (21 files)
  __init__.py
  conftest.py
  test_backend.py
  test_cli.py
  test_clip_manager.py
  test_color_utils.py
  test_convert_pth_to_safetensors.py
  test_device_utils.py
  test_e2e_workflow.py
  test_exr_gamma_bug_condition.py
  test_exr_gamma_preservation.py
  test_frame_io.py
  test_gamma_consistency.py
  test_imports.py
  test_inference_engine.py
  test_mlx_smoke.py
  test_pbt_auto_download.py
  test_pbt_backend_resolution.py
  test_pbt_dep_preservation.py
  test_pyproject_structure.py
  test_service.py
.dockerignore
.git-blame-ignore-revs
.gitignore
.python-version
CONTRIBUTING.md
CorridorKey_DRAG_CLIPS_HERE_local.bat
CorridorKey_DRAG_CLIPS_HERE_local.sh
Dockerfile
Install_CorridorKey_Linux_Mac.sh
Install_CorridorKey_Windows.bat
Install_GVM_Linux_Mac.sh
Install_GVM_Windows.bat
Install_VideoMaMa_Linux_Mac.sh
Install_VideoMaMa_Windows.bat
LICENSE
README.md
RunGVMOnly.sh
RunInferenceOnly.sh
clip_manager.py
corridorkey_cli.py
device_utils.py
docker-compose.yml
pyproject.toml
renovate.json
… 3 more files
```

## Entry points

- [clip_manager.py:1148](https://github.com/nikopueringer/CorridorKey/blob/97e55a453060745bead1befd293f6e523c4b845c/clip_manager.py#L1148)
- [corridorkey_cli.py](https://github.com/nikopueringer/CorridorKey/blob/97e55a453060745bead1befd293f6e523c4b845c/corridorkey_cli.py)
- [scripts/convert_pth_to_safetensors.py:91](https://github.com/nikopueringer/CorridorKey/blob/97e55a453060745bead1befd293f6e523c4b845c/scripts/convert_pth_to_safetensors.py#L91)
- [test_outputs.py:142](https://github.com/nikopueringer/CorridorKey/blob/97e55a453060745bead1befd293f6e523c4b845c/test_outputs.py#L142)
- [test_vram.py:58](https://github.com/nikopueringer/CorridorKey/blob/97e55a453060745bead1befd293f6e523c4b845c/test_vram.py#L58)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| backend package | library | Observed | Groups 9 file(s) under backend package (observed from repository paths and static analysis). Observed top-level classes: ClipAsset, ClipEntry, ClipScanError, ClipState, CorridorKeyError, ExtractionError. Observed top-le… |
| BiRefNetModule package | library | Observed | Groups 1 file(s) under birefnetmodule package (observed from repository paths and static analysis). Observed top-level classes: BiRefNetHandler, ImagePreprocessor. |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 7 file(s) under core modules (observed from repository paths and static analysis). Observed top-level classes: GPUInfo. Observed top-level functions: _enumerate_amd, _enumerate_nvidia, clear_device_cache, detect_… |
| CorridorKeyModule package | library | Observed | Groups 3 file(s) under corridorkeymodule package (observed from repository paths and static analysis). Observed top-level classes: CorridorKeyEngine, _MLXEngineAdapter. Observed top-level functions: _auto_detect_backend… |
| Data layer | data | Observed | Groups 2 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: UNetSpatioTemporalConditionModel. |
| Application entry point | entrypoint | Observed | Groups 3 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Typer. Observed top-level classes: ClipAsset, ClipEntry, InferenceSettings, Pr… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| gvm_core package | library | Observed | Groups 6 file(s) under gvm_core package (observed from repository paths and static analysis). Observed top-level classes: GVMLoraLoader, GVMOutput, GVMPipeline, GVMProcessor, ImageSequenceReader, ImageSequenceWriter. Ob… |
| Service / domain layer | service | Observed | Groups 4 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: CNNRefinerModule, CorridorKeyService, DecoderHead, FrameResult, GreenFormer, InferenceParam… |
| Tests | test | Observed | Groups 23 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH corridorkey_cli.scan_clips, PATCH corridorkey_cli.run_inference, PATCH corridorkey_cli._prompt_inference_setting… |
| VideoMaMaInferenceModule package | library | Observed | Groups 3 file(s) under videomamainferencemodule package (observed from repository paths and static analysis). Observed top-level classes: StableVideoDiffusionPipelineOnestepWithMask, StableVideoDiffusionPipelineOutput,… |

## Important files

- `.dockerignore` (container)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/docs.yml` (ci)
- `Dockerfile` (container)
- `docker-compose.yml` (container)
- `pyproject.toml` (manifest)
- `renovate.json` (config)
- `zensical.toml` (config)

## Top-level layout

- `(root files)` — 27 analysed file(s)
- `tests` — 21 analysed file(s)
- `gvm_core` — 11 analysed file(s)
- `backend` — 10 analysed file(s)
- `CorridorKeyModule` — 9 analysed file(s)
- `VideoMaMaInferenceModule` — 6 analysed file(s)
- `.github` — 4 analysed file(s)
- `BiRefNetModule` — 2 analysed file(s)
- `docs` — 2 analysed file(s)
- `ClipsForInference` — 1 analysed file(s)
- `IgnoredClips` — 1 analysed file(s)
- `Output` — 1 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `97e55a453060745bead1befd293f6e523c4b845c` is the revision these paths and observations refer to.
