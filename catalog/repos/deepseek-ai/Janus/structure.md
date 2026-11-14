# Project structure: deepseek-ai/Janus

**Analysed commit:** `1daa72fa409002d40931bd7b36a9280362469ead`

**Commit reference:** [1daa72fa409002d40931bd7b36a9280362469ead](https://github.com/deepseek-ai/Janus/commit/1daa72fa409002d40931bd7b36a9280362469ead)

**Tree at this commit:** [deepseek-ai/Janus@1daa72fa4090](https://github.com/deepseek-ai/Janus/tree/1daa72fa409002d40931bd7b36a9280362469ead)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | deepseek-ai/Janus |
| Description | Janus-Series: Unified Multimodal Understanding and Generation Models |
| Stars | 17766 |
| Forks | 2229 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `1daa72fa409002d40931bd7b36a9280362469ead` |
| Retrieved at | 2026-11-14T19:08:29.152810+00:00 |
| Files in this snapshot | 39 |

## Directory tree

```text
demo/  (6 files)
  Janus_colab_demo.ipynb
  app.py
  app_janusflow.py
  app_januspro.py
  fastapi_app.py
  fastapi_client.py
images/  (2 files)
  badge.svg
  logo.svg
janus/  (20 files)
  janusflow/  (8 files)
    models/  (7 files)
      … 7 files under this directory
    __init__.py
  models/  (8 files)
    __init__.py
    clip_encoder.py
    image_processing_vlm.py
    modeling_vlm.py
    processing_vlm.py
    projector.py
    siglip_vit.py
    vq_model.py
  utils/  (3 files)
    __init__.py
    conversation.py
    io.py
  __init__.py
.gitattributes
.gitignore
LICENSE-CODE
LICENSE-MODEL
Makefile
README.md
generation_inference.py
inference.py
interactivechat.py
pyproject.toml
requirements.txt
```

## Entry points

- [demo/fastapi_app.py:10](https://github.com/deepseek-ai/Janus/blob/1daa72fa409002d40931bd7b36a9280362469ead/demo/fastapi_app.py#L10)
- [demo/fastapi_client.py:73](https://github.com/deepseek-ai/Janus/blob/1daa72fa409002d40931bd7b36a9280362469ead/demo/fastapi_client.py#L73)
- [interactivechat.py:149](https://github.com/deepseek-ai/Janus/blob/1daa72fa409002d40931bd7b36a9280362469ead/interactivechat.py#L149)
- [janus/janusflow/models/image_processing_vlm.py:202](https://github.com/deepseek-ai/Janus/blob/1daa72fa409002d40931bd7b36a9280362469ead/janus/janusflow/models/image_processing_vlm.py#L202)
- [janus/models/image_processing_vlm.py:202](https://github.com/deepseek-ai/Janus/blob/1daa72fa409002d40931bd7b36a9280362469ead/janus/models/image_processing_vlm.py#L202)
- [janus/models/projector.py:89](https://github.com/deepseek-ai/Janus/blob/1daa72fa409002d40931bd7b36a9280362469ead/janus/models/projector.py#L89)
- [janus/utils/conversation.py:345](https://github.com/deepseek-ai/Janus/blob/1daa72fa409002d40931bd7b36a9280362469ead/janus/utils/conversation.py#L345)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). Observed top-level functions: generate. |
| Data layer | data | Observed | Groups 12 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AlignerConfig, Attention, AttnBlock, BatchedVLChatProcessorOutput, Block, CLIPVisionTower. Observed to… |
| demo package | library | Observed | Groups 2 file(s) under demo package (observed from repository paths and static analysis). Observed top-level functions: generate, generate_image, multimodal_understanding, unpack. |
| Application entry point | entrypoint | Observed | Groups 8 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed routes: POST /understand_image_and_question/, POST /generate… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| janus package | library | Observed | Groups 4 file(s) under janus package (observed from repository paths and static analysis). Observed top-level functions: load_json, load_pil_images, load_pretrained_model. |

## Important files

- `pyproject.toml` (manifest)
- `requirements.txt` (manifest)

## Top-level layout

- `janus` — 20 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `demo` — 6 analysed file(s)
- `images` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `1daa72fa409002d40931bd7b36a9280362469ead` is the revision these paths and observations refer to.
