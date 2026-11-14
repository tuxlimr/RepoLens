# Project structure: borisdayma/dalle-mini

**Analysed commit:** `f0be4de610285a002052024a1e096126f9452cc4`

**Commit reference:** [f0be4de610285a002052024a1e096126f9452cc4](https://github.com/borisdayma/dalle-mini/commit/f0be4de610285a002052024a1e096126f9452cc4)

**Tree at this commit:** [borisdayma/dalle-mini@f0be4de61028](https://github.com/borisdayma/dalle-mini/tree/f0be4de610285a002052024a1e096126f9452cc4)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | borisdayma/dalle-mini |
| Description | DALL·E Mini - Generate images from a text prompt |
| Stars | 14710 |
| Forks | 1210 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `f0be4de610285a002052024a1e096126f9452cc4` |
| Retrieved at | 2026-11-14T19:09:18.603833+00:00 |
| Files in this snapshot | 48 |

## Directory tree

```text
.github/  (6 files)
  workflows/  (5 files)
    check_size.yml
    pypi_release.yml
    style.yml
    sync_to_hub.yml.backup
    sync_to_hub_debug.yml
  FUNDING.yml
Docker/  (3 files)
  Dockerfile
  README.md
  build_docker.sh
app/  (4 files)
  gradio/  (2 files)
    app.py
    backend.py
  streamlit/  (2 files)
    app.py
    backend.py
src/  (10 files)
  dalle_mini/  (10 files)
    model/  (8 files)
      … 8 files under this directory
    __init__.py
    data.py
tools/  (15 files)
  dataset/  (1 files)
    encode_dataset.ipynb
  inference/  (2 files)
    inference_pipeline.ipynb
    run_infer_notebook.sh
  train/  (12 files)
    config/  (4 files)
      … 4 files under this directory
    scalable_shampoo/  (5 files)
      … 5 files under this directory
    embeddings_retrain_preparation.ipynb
    sweep.yaml
    train.py
.gitattributes
.gitignore
CITATION.cff
LICENSE
Makefile
README.md
pyproject.toml
run_docker_image.sh
setup.cfg
setup.py
```

## Entry points

- [setup.py:3](https://github.com/borisdayma/dalle-mini/blob/f0be4de610285a002052024a1e096126f9452cc4/setup.py#L3)
- [tools/train/train.py:1739](https://github.com/borisdayma/dalle-mini/blob/f0be4de610285a002052024a1e096126f9452cc4/tools/train/train.py#L1739)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| app package | library | Observed | Groups 2 file(s) under app package (observed from repository paths and static analysis). Observed top-level classes: ServiceError. Observed top-level functions: get_images_from_backend, get_model_version. |
| Configuration and deployment | config | Observed | Groups 9 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| dalle_mini package | library | Observed | Groups 10 file(s) under dalle_mini package (observed from repository paths and static analysis). Observed top-level classes: DalleBart, DalleBartConfig, DalleBartProcessor, DalleBartProcessorBase, DalleBartTokenizer, Da… |
| Docker package | library | Observed | Groups 1 file(s) under docker package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 3 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: DataTrainingArguments, ModelArguments, TrainingArguments. Observed top-level functions: in… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| tools package | library | Observed | Groups 5 file(s) under tools package (observed from repository paths and static analysis). Observed top-level classes: BlockPartitioner, GlobalShardedParameterStats, GraftingType, InitFnState, LocalShardedParameterStats… |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/workflows/check_size.yml` (ci)
- `.github/workflows/pypi_release.yml` (ci)
- `.github/workflows/style.yml` (ci)
- `.github/workflows/sync_to_hub.yml.backup` (ci)
- `.github/workflows/sync_to_hub_debug.yml` (ci)
- `Docker/Dockerfile` (container)
- `pyproject.toml` (manifest)
- `setup.cfg` (manifest)
- `setup.py` (manifest)
- `tools/train/config/mega/config.json` (config)
- `tools/train/config/micro/config.json` (config)
- `tools/train/config/mini/config.json` (config)
- `tools/train/config/mini_glu/config.json` (config)
- `tools/train/sweep.yaml` (config)

## Top-level layout

- `tools` — 15 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `src` — 10 analysed file(s)
- `.github` — 6 analysed file(s)
- `app` — 4 analysed file(s)
- `Docker` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `f0be4de610285a002052024a1e096126f9452cc4` is the revision these paths and observations refer to.
