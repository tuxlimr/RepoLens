# Project structure: Zeyi-Lin/HivisionIDPhotos

**Analysed commit:** `5c191e2577f14755a69d9df6db415fab23aca484`

**Commit reference:** [5c191e2577f14755a69d9df6db415fab23aca484](https://github.com/Zeyi-Lin/HivisionIDPhotos/commit/5c191e2577f14755a69d9df6db415fab23aca484)

**Tree at this commit:** [Zeyi-Lin/HivisionIDPhotos@5c191e2577f1](https://github.com/Zeyi-Lin/HivisionIDPhotos/tree/5c191e2577f14755a69d9df6db415fab23aca484)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Zeyi-Lin/HivisionIDPhotos |
| Description | ⚡️HivisionIDPhotos: a lightweight and efficient AI ID photos tools. 一个轻量级的AI证件照制作算法。 |
| Stars | 21723 |
| Forks | 2532 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `5c191e2577f14755a69d9df6db415fab23aca484` |
| Retrieved at | 2026-11-14T19:07:57.934941+00:00 |
| Files in this snapshot | 69 |

## Directory tree

```text
.devcontainer/  (2 files)
  devcontainer.json
  start.sh
.github/  (1 files)
  workflows/  (1 files)
    build-image.yml
.vscode/  (2 files)
  extensions.json
  settings.json
demo/  (10 files)
  assets/  (5 files)
    color_list_CN.csv
    color_list_EN.csv
    size_list_CN.csv
    size_list_EN.csv
    title.md
  config.py
  locales.py
  processor.py
  ui.py
  utils.py
docs/  (4 files)
  api_CN.md
  api_EN.md
  face++_CN.md
  face++_EN.md
hivision/  (31 files)
  creator/  (17 files)
    retinaface/  (5 files)
      … 5 files under this directory
    weights/  (1 files)
      … 1 files under this directory
    __init__.py
    choose_handler.py
    context.py
    face_detector.py
    human_matting.py
    layout_calculator.py
    move_image.py
    photo_adjuster.py
    rotation_adjust.py
    tensor2numpy.py
    utils.py
  plugin/  (11 files)
    beauty/  (7 files)
      … 7 files under this directory
    font/  (1 files)
      … 1 files under this directory
    template/  (2 files)
      … 2 files under this directory
    watermark.py
  __init__.py
  error.py
  utils.py
scripts/  (2 files)
  build_pypi.py
  download_model.py
test/  (2 files)
  temp/  (1 files)
    .gitkeep
  create_id_photo.py
.gitignore
Dockerfile
LICENSE
README.md
README_EN.md
README_JP.md
README_KO.md
app.py
app.spec
deploy_api.py
docker-compose.yml
inference.py
requirements-app.txt
requirements-dev.txt
requirements.txt
```

## Entry points

- [app.py:43](https://github.com/Zeyi-Lin/HivisionIDPhotos/blob/5c191e2577f14755a69d9df6db415fab23aca484/app.py#L43)
- [deploy_api.py:28](https://github.com/Zeyi-Lin/HivisionIDPhotos/blob/5c191e2577f14755a69d9df6db415fab23aca484/deploy_api.py#L28)
- [hivision/creator/move_image.py:133](https://github.com/Zeyi-Lin/HivisionIDPhotos/blob/5c191e2577f14755a69d9df6db415fab23aca484/hivision/creator/move_image.py#L133)
- [hivision/creator/retinaface/inference.py:181](https://github.com/Zeyi-Lin/HivisionIDPhotos/blob/5c191e2577f14755a69d9df6db415fab23aca484/hivision/creator/retinaface/inference.py#L181)
- [hivision/plugin/beauty/base_adjust.py:114](https://github.com/Zeyi-Lin/HivisionIDPhotos/blob/5c191e2577f14755a69d9df6db415fab23aca484/hivision/plugin/beauty/base_adjust.py#L114)
- [hivision/plugin/beauty/grind_skin.py:115](https://github.com/Zeyi-Lin/HivisionIDPhotos/blob/5c191e2577f14755a69d9df6db415fab23aca484/hivision/plugin/beauty/grind_skin.py#L115)
- [hivision/plugin/beauty/whitening.py:80](https://github.com/Zeyi-Lin/HivisionIDPhotos/blob/5c191e2577f14755a69d9df6db415fab23aca484/hivision/plugin/beauty/whitening.py#L80)
- [hivision/plugin/watermark.py:212](https://github.com/Zeyi-Lin/HivisionIDPhotos/blob/5c191e2577f14755a69d9df6db415fab23aca484/hivision/plugin/watermark.py#L212)
- [scripts/download_model.py:107](https://github.com/Zeyi-Lin/HivisionIDPhotos/blob/5c191e2577f14755a69d9df6db415fab23aca484/scripts/download_model.py#L107)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: load_configuration. |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| demo package | library | Observed | Groups 4 file(s) under demo package (observed from repository paths and static analysis). Observed top-level classes: IDPhotoProcessor. Observed top-level functions: create_ui, csv_to_color_list, csv_to_size_list, load_… |
| Application entry point | entrypoint | Observed | Groups 9 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed routes: POST /idphoto, POST /human_matting, POST /add_backgr… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| hivision package | library | Observed | Groups 21 file(s) under hivision package (observed from repository paths and static analysis). Observed top-level classes: APIError, Context, FaceError, IDCreator, Params, PriorBox. Observed top-level functions: BeautyT… |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 2 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.devcontainer/devcontainer.json` (config)
- `.github/workflows/build-image.yml` (ci)
- `.vscode/extensions.json` (config)
- `.vscode/settings.json` (config)
- `Dockerfile` (container)
- `docker-compose.yml` (container)
- `hivision/plugin/template/assets/template_config.json` (config)
- `requirements-app.txt` (manifest)
- `requirements-dev.txt` (manifest)
- `requirements.txt` (manifest)

## Top-level layout

- `hivision` — 31 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `demo` — 10 analysed file(s)
- `docs` — 4 analysed file(s)
- `.devcontainer` — 2 analysed file(s)
- `.vscode` — 2 analysed file(s)
- `scripts` — 2 analysed file(s)
- `test` — 2 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `5c191e2577f14755a69d9df6db415fab23aca484` is the revision these paths and observations refer to.
