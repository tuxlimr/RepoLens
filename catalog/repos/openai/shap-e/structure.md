# Project structure: openai/shap-e

**Analysed commit:** `50131012ee11c9d2617f3886c10f000d3c7a3b43`

**Commit reference:** [50131012ee11c9d2617f3886c10f000d3c7a3b43](https://github.com/openai/shap-e/commit/50131012ee11c9d2617f3886c10f000d3c7a3b43)

**Tree at this commit:** [openai/shap-e@50131012ee11](https://github.com/openai/shap-e/tree/50131012ee11c9d2617f3886c10f000d3c7a3b43)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | openai/shap-e |
| Description | Generate 3D objects conditioned on text or images |
| Stars | 12266 |
| Forks | 1076 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `50131012ee11c9d2617f3886c10f000d3c7a3b43` |
| Retrieved at | 2026-11-14T19:10:12.832090+00:00 |
| Files in this snapshot | 78 |

## Directory tree

```text
shap_e/  (72 files)
  diffusion/  (4 files)
    __init__.py
    gaussian_diffusion.py
    k_diffusion.py
    sample.py
  examples/  (4 files)
    example_data/  (1 files)
      … 1 files under this directory
    encode_model.ipynb
    sample_image_to_3d.ipynb
    sample_text_to_3d.ipynb
  models/  (38 files)
    generation/  (7 files)
      … 7 files under this directory
    nerf/  (4 files)
      … 4 files under this directory
    nerstf/  (2 files)
      … 2 files under this directory
    nn/  (8 files)
      … 8 files under this directory
    stf/  (4 files)
      … 4 files under this directory
    transmitter/  (7 files)
      … 7 files under this directory
    __init__.py
    configs.py
    download.py
    query.py
    renderer.py
    volume.py
  rendering/  (19 files)
    blender/  (5 files)
      … 5 files under this directory
    raycast/  (5 files)
      … 5 files under this directory
    __init__.py
    _mc_table.py
    mc.py
    mesh.py
    ply_util.py
    point_cloud.py
    pytorch3d_util.py
    torch_mesh.py
    view_data.py
  util/  (6 files)
    __init__.py
    collections.py
    data_util.py
    image_util.py
    io.py
    notebooks.py
  __init__.py
.gitignore
LICENSE
README.md
model-card.md
samples.md
setup.py
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 38 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: BoundingBoxVolume, CLIPImageGridPointDiffusionTransformer, CLIPImageGridUpsamplePointDiffusionTransfor… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| shap_e package | library | Observed | Groups 30 file(s) under shap_e package (observed from repository paths and static analysis). Observed top-level classes: AttrDict, BidirectionalLights, BlenderViewData, Camera, GaussianDiffusion, GaussianToKarrasDenoise… |

## Important files

- `setup.py` (manifest)

## Top-level layout

- `shap_e` — 72 analysed file(s)
- `(root files)` — 6 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `50131012ee11c9d2617f3886c10f000d3c7a3b43` is the revision these paths and observations refer to.
