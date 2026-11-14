# Project structure: alievk/avatarify-python

**Analysed commit:** `862182cfbca5bd8a7473bed9c5f69f92e8d5cc7b`

**Commit reference:** [862182cfbca5bd8a7473bed9c5f69f92e8d5cc7b](https://github.com/alievk/avatarify-python/commit/862182cfbca5bd8a7473bed9c5f69f92e8d5cc7b)

**Tree at this commit:** [alievk/avatarify-python@862182cfbca5](https://github.com/alievk/avatarify-python/tree/862182cfbca5bd8a7473bed9c5f69f92e8d5cc7b)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | alievk/avatarify-python |
| Description | Avatars for Zoom, Skype and other video-conferencing apps. |
| Stars | 16503 |
| Forks | 4290 |
| Licence | Other |
| Language | Python |
| Default branch | master |
| Analysed commit | `862182cfbca5bd8a7473bed9c5f69f92e8d5cc7b` |
| Retrieved at | 2026-11-14T19:08:49.927448+00:00 |
| Files in this snapshot | 37 |

## Directory tree

```text
.github/  (2 files)
  ISSUE_TEMPLATE/  (2 files)
    bug-report.md
    discussion.md
afy/  (9 files)
  arguments.py
  cam_fomm.py
  camera_selector.py
  networking.py
  predictor_local.py
  predictor_remote.py
  predictor_worker.py
  utils.py
  videocaptureasync.py
avatars/  (1 files)
  .geetkeep
docs/  (1 files)
  README.md
scripts/  (11 files)
  create_virtual_camera.sh
  download_data.sh
  get_ngrok.sh
  install.sh
  install_docker.sh
  install_mac.sh
  install_windows.bat
  open_tunnel_ngrok.sh
  open_tunnel_ssh.sh
  settings.sh
  settings_windows.bat
var/  (1 files)
  log/  (1 files)
    .geetkeep
.gitignore
.gitmodules
Dockerfile
LICENSE.md
README.md
avatarify.ipynb
config.yaml
requirements.txt
requirements_client.txt
run.sh
run_mac.sh
run_windows.bat
```

## Entry points

- [afy/cam_fomm.py:183](https://github.com/alievk/avatarify-python/blob/862182cfbca5bd8a7473bed9c5f69f92e8d5cc7b/afy/cam_fomm.py#L183)
- [afy/camera_selector.py:100](https://github.com/alievk/avatarify-python/blob/862182cfbca5bd8a7473bed9c5f69f92e8d5cc7b/afy/camera_selector.py#L100)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| afy package | library | Observed | Groups 7 file(s) under afy package (observed from repository paths and static analysis). Observed top-level classes: AccumDict, Logger, Once, PredictorLocal, PredictorRemote, PredictorWorker. Observed top-level function… |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: change_avatar, draw_calib_text, draw_face_landmarks, draw_fps, draw_landmark_text, draw_… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 9 file(s) under scripts package (observed from repository paths and static analysis). |

## Important files

- `Dockerfile` (container)
- `config.yaml` (config)
- `requirements.txt` (manifest)
- `requirements_client.txt` (manifest)

## Top-level layout

- `(root files)` — 12 analysed file(s)
- `scripts` — 11 analysed file(s)
- `afy` — 9 analysed file(s)
- `.github` — 2 analysed file(s)
- `avatars` — 1 analysed file(s)
- `docs` — 1 analysed file(s)
- `var` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `862182cfbca5bd8a7473bed9c5f69f92e8d5cc7b` is the revision these paths and observations refer to.
