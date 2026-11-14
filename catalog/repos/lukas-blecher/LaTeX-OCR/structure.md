# Project structure: lukas-blecher/LaTeX-OCR

**Analysed commit:** `5c1ac929bd19a7ecf86d5fb8d94771c8969fcb80`

**Commit reference:** [5c1ac929bd19a7ecf86d5fb8d94771c8969fcb80](https://github.com/lukas-blecher/LaTeX-OCR/commit/5c1ac929bd19a7ecf86d5fb8d94771c8969fcb80)

**Tree at this commit:** [lukas-blecher/LaTeX-OCR@5c1ac929bd19](https://github.com/lukas-blecher/LaTeX-OCR/tree/5c1ac929bd19a7ecf86d5fb8d94771c8969fcb80)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | lukas-blecher/LaTeX-OCR |
| Description | pix2tex: Using a ViT to convert images of equations into LaTeX code. |
| Stars | 16621 |
| Forks | 1301 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `5c1ac929bd19a7ecf86d5fb8d94771c8969fcb80` |
| Retrieved at | 2026-11-14T19:08:44.814396+00:00 |
| Files in this snapshot | 95 |

## Directory tree

```text
docker/  (2 files)
  api.dockerfile
  build-api.sh
docs/  (7 files)
  Makefile
  conf.py
  index.rst
  installation.md
  make.bat
  pix2tex.rst
  requirements.txt
notebooks/  (2 files)
  LaTeX_OCR_test.ipynb
  LaTeX_OCR_training.ipynb
pix2tex/  (77 files)
  api/  (4 files)
    __init__.py
    app.py
    run.py
    streamlit.py
  dataset/  (47 files)
    data/  (1 files)
      … 1 files under this directory
    preprocessing/  (35 files)
      … 35 files under this directory
    __init__.py
    arxiv.py
    dataset.py
    demacro-test.py
    demacro.py
    extract_latex.py
    latex2png.py
    postprocess.py
    render.py
    scraping.py
    transforms.py
  model/  (7 files)
    checkpoints/  (2 files)
      … 2 files under this directory
    dataset/  (1 files)
      … 1 files under this directory
    settings/  (3 files)
      … 3 files under this directory
    __init__.py
  models/  (5 files)
    __init__.py
    hybrid.py
    transformer.py
    utils.py
    vit.py
  resources/  (4 files)
    __init__.py
    icon.svg
    processing-icon-anim.svg
    resources.qrc
  utils/  (2 files)
    __init__.py
    utils.py
  __init__.py
  __main__.py
  cli.py
  eval.py
  gui.py
  setup_desktop.py
  train.py
  train_resizer.py
.gitignore
.readthedocs.yaml
LICENSE
MANIFEST.in
README.md
setup.cfg
setup.py
```

## Entry points

- [pix2tex/__main__.py](https://github.com/lukas-blecher/LaTeX-OCR/blob/5c1ac929bd19a7ecf86d5fb8d94771c8969fcb80/pix2tex/__main__.py)
- [pix2tex/__main__.py](https://github.com/lukas-blecher/LaTeX-OCR/blob/5c1ac929bd19a7ecf86d5fb8d94771c8969fcb80/pix2tex/__main__.py)
- [pix2tex/__main__.py](https://github.com/lukas-blecher/LaTeX-OCR/blob/5c1ac929bd19a7ecf86d5fb8d94771c8969fcb80/pix2tex/__main__.py)
- [pix2tex/__main__.py](https://github.com/lukas-blecher/LaTeX-OCR/blob/5c1ac929bd19a7ecf86d5fb8d94771c8969fcb80/pix2tex/__main__.py)
- [pix2tex/api/app.py:10](https://github.com/lukas-blecher/LaTeX-OCR/blob/5c1ac929bd19a7ecf86d5fb8d94771c8969fcb80/pix2tex/api/app.py#L10)
- [pix2tex/api/run.py:14](https://github.com/lukas-blecher/LaTeX-OCR/blob/5c1ac929bd19a7ecf86d5fb8d94771c8969fcb80/pix2tex/api/run.py#L14)
- [pix2tex/api/streamlit.py:16](https://github.com/lukas-blecher/LaTeX-OCR/blob/5c1ac929bd19a7ecf86d5fb8d94771c8969fcb80/pix2tex/api/streamlit.py#L16)
- [pix2tex/dataset/arxiv.py:112](https://github.com/lukas-blecher/LaTeX-OCR/blob/5c1ac929bd19a7ecf86d5fb8d94771c8969fcb80/pix2tex/dataset/arxiv.py#L112)
- [pix2tex/dataset/dataset.py:233](https://github.com/lukas-blecher/LaTeX-OCR/blob/5c1ac929bd19a7ecf86d5fb8d94771c8969fcb80/pix2tex/dataset/dataset.py#L233)
- [pix2tex/dataset/demacro-test.py:229](https://github.com/lukas-blecher/LaTeX-OCR/blob/5c1ac929bd19a7ecf86d5fb8d94771c8969fcb80/pix2tex/dataset/demacro-test.py#L229)
- [pix2tex/dataset/demacro.py:177](https://github.com/lukas-blecher/LaTeX-OCR/blob/5c1ac929bd19a7ecf86d5fb8d94771c8969fcb80/pix2tex/dataset/demacro.py#L177)
- [pix2tex/dataset/extract_latex.py:102](https://github.com/lukas-blecher/LaTeX-OCR/blob/5c1ac929bd19a7ecf86d5fb8d94771c8969fcb80/pix2tex/dataset/extract_latex.py#L102)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 1 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 9 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 5 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: CustomARWrapper, CustomVisionTransformer, Model, ViTransformerWrapper. Observed top-level functions: ge… |
| docker package | library | Observed | Groups 1 file(s) under docker package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 21 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed routes: GET /, POST /predict/, POST /bytes/. Observed top-l… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| pix2tex package | library | Observed | Groups 36 file(s) under pix2tex package (observed from repository paths and static analysis). Observed top-level classes: App, EmptyStepper, ModelThread, SnipWidget, WebView. Observed top-level functions: alternatives,… |

## Important files

- `.readthedocs.yaml` (config)
- `MANIFEST.in` (manifest)
- `docs/requirements.txt` (manifest)
- `pix2tex/dataset/preprocessing/third_party/katex/package.json` (manifest)
- `pix2tex/dataset/preprocessing/third_party/match-at/package.json` (manifest)
- `pix2tex/model/dataset/tokenizer.json` (config)
- `pix2tex/model/settings/config-vit.yaml` (config)
- `pix2tex/model/settings/config.yaml` (config)
- `pix2tex/model/settings/debug.yaml` (config)
- `setup.cfg` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `pix2tex` — 77 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `docs` — 7 analysed file(s)
- `docker` — 2 analysed file(s)
- `notebooks` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `5c1ac929bd19a7ecf86d5fb8d94771c8969fcb80` is the revision these paths and observations refer to.
