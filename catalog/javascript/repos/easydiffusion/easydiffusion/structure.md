# Project structure: easydiffusion/easydiffusion

**Analysed commit:** `7caaf64acd47b6bc40ba2379571d48ea4cc29a6a`

**Commit reference:** [7caaf64acd47b6bc40ba2379571d48ea4cc29a6a](https://github.com/easydiffusion/easydiffusion/commit/7caaf64acd47b6bc40ba2379571d48ea4cc29a6a)

**Tree at this commit:** [easydiffusion/easydiffusion@7caaf64acd47](https://github.com/easydiffusion/easydiffusion/tree/7caaf64acd47b6bc40ba2379571d48ea4cc29a6a)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | easydiffusion/easydiffusion |
| Description | An easy 1-click way to create beautiful artwork on your PC using AI, with no tech knowledge. Provides a browser UI for generating images from text prompts and images. Just enter your text prompt, and see the generated image. |
| Stars | 10479 |
| Forks | 860 |
| Licence | Other |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `7caaf64acd47b6bc40ba2379571d48ea4cc29a6a` |
| Retrieved at | 2026-11-14T19:12:39.557536+00:00 |
| Files in this snapshot | 145 |

## Directory tree

```text
.github/  (3 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  FUNDING.yml
NSIS/  (3 files)
  .gitignore
  README.md
  sdui.nsi
kb/  (13 files)
  README.md
  architecture.md
  backend-engines.md
  configuration.md
  development.md
  features.md
  frontend.md
  install-and-startup.md
  models.md
  release-process.md
  task-lifecycle.md
  testing.md
  v4.md
scripts/  (21 files)
  Developer Console.cmd
  Start Stable Diffusion UI.cmd
  bootstrap.bat
  bootstrap.sh
  check_modules.py
  config.yaml.sample
  developer_console.sh
  ensure_torchruntime.py
  functions.sh
  get_config.py
  install_status.txt
  on_env_start.bat
  on_env_start.sh
  on_sd_start.bat
  on_sd_start.sh
  start.sh
  test_backend_config_overrides.py
  test_webui_alternate_field_names.py
  test_webui_face_filters.py
  webui_console.py
  win_enable_long_filepaths.ps1
ui/  (85 files)
  easydiffusion/  (31 files)
    backends/  (7 files)
      … 7 files under this directory
    easydb/  (4 files)
      … 4 files under this directory
    model_manager/  (2 files)
      … 2 files under this directory
    tasks/  (4 files)
      … 4 files under this directory
    utils/  (4 files)
      … 4 files under this directory
    __init__.py
    app.py
    backend_manager.py
    bucket_manager.py
    device_manager.py
    package_manager.py
    runtime.py
    server.py
    task_manager.py
    types.py
  media/  (32 files)
    css/  (11 files)
      … 11 files under this directory
    images/  (4 files)
      … 4 files under this directory
    js/  (16 files)
      … 16 files under this directory
    manifest.webmanifest
  plugins/  (19 files)
    ui/  (19 files)
      … 19 files under this directory
  index.html
  main.py
  modifiers.json
.gitignore
.prettierignore
.prettierrc.json
3rd-PARTY-LICENSES
CHANGES.md
CONTRIBUTING.md
CreativeML Open RAIL-M License
How to install and run.txt
LICENSE
PRIVACY.md
README BEFORE YOU RUN THIS.txt
README.md
announcement_log.md
announcement_log.txt
build.bat
build.sh
environment.yaml
event_log.md
event_log.txt
package.json
```

## Entry points

- [scripts/check_modules.py:400](https://github.com/easydiffusion/easydiffusion/blob/7caaf64acd47b6bc40ba2379571d48ea4cc29a6a/scripts/check_modules.py#L400)
- [scripts/webui_console.py:96](https://github.com/easydiffusion/easydiffusion/blob/7caaf64acd47b6bc40ba2379571d48ea4cc29a6a/scripts/webui_console.py#L96)
- [ui/easydiffusion/backends/webui.py:155](https://github.com/easydiffusion/easydiffusion/blob/7caaf64acd47b6bc40ba2379571d48ea4cc29a6a/ui/easydiffusion/backends/webui.py#L155)
- [ui/easydiffusion/server.py:36](https://github.com/easydiffusion/easydiffusion/blob/7caaf64acd47b6bc40ba2379571d48ea4cc29a6a/ui/easydiffusion/server.py#L36)
- [ui/easydiffusion/utils/model_identifier.py:411](https://github.com/easydiffusion/easydiffusion/blob/7caaf64acd47b6bc40ba2379571d48ea4cc29a6a/ui/easydiffusion/utils/model_identifier.py#L411)
- [ui/media/js/main.js](https://github.com/easydiffusion/easydiffusion/blob/7caaf64acd47b6bc40ba2379571d48ea4cc29a6a/ui/media/js/main.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 3 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: Bucket, BucketBase, BucketCreate, BucketFile, BucketFileBase, BucketFileCreate. |
| Application entry point | entrypoint | Observed | Groups 7 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed top-level classes: CloudflareTunnel, NoCacheStaticFiles, Set… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 8 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 3 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: TestBackendConfigEnvOverrides, TestTerminologyConsistency, TestWebuiFaceFilterPayloads, _FakeResponse. Obser… |
| ui package | library | Observed | Groups 56 file(s) under ui package (observed from repository paths and static analysis). Observed top-level classes: DataCache, FilterImageRequest, FilterImageResponse, FilterTask, GenerateImageRequest, GenerateImageRes… |

## Important files

- `.github/FUNDING.yml` (config)
- `.prettierrc.json` (config)
- `environment.yaml` (config)
- `package.json` (manifest)
- `ui/modifiers.json` (config)

## Top-level layout

- `ui` — 85 analysed file(s)
- `scripts` — 21 analysed file(s)
- `(root files)` — 20 analysed file(s)
- `kb` — 13 analysed file(s)
- `.github` — 3 analysed file(s)
- `NSIS` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x generated/minified file excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `7caaf64acd47b6bc40ba2379571d48ea4cc29a6a` is the revision these paths and observations refer to.
