# Project structure: fishaudio/fish-speech

**Analysed commit:** `0f8a12e8a651062fdee9c33a894bdccd3a8513f1`

**Commit reference:** [0f8a12e8a651062fdee9c33a894bdccd3a8513f1](https://github.com/fishaudio/fish-speech/commit/0f8a12e8a651062fdee9c33a894bdccd3a8513f1)

**Tree at this commit:** [fishaudio/fish-speech@0f8a12e8a651](https://github.com/fishaudio/fish-speech/tree/0f8a12e8a651062fdee9c33a894bdccd3a8513f1)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | fishaudio/fish-speech |
| Description | SOTA Open Source TTS |
| Stars | 33721 |
| Forks | 2936 |
| Licence | Other |
| Language | Python |
| Default branch | main |
| Analysed commit | `0f8a12e8a651062fdee9c33a894bdccd3a8513f1` |
| Retrieved at | 2026-11-14T19:07:01.035400+00:00 |
| Files in this snapshot | 132 |

## Directory tree

```text
.github/  (7 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.yml
    config.yml
    feature_request.yml
  workflows/  (3 files)
    build-docker-image.yml
    docs.yml
    stale.yml
  pull_request_template.md
awesome_webui/  (28 files)
  public/  (1 files)
    vite.svg
  src/  (18 files)
    assets/  (1 files)
      … 1 files under this directory
    components/  (13 files)
      … 13 files under this directory
    lib/  (1 files)
      … 1 files under this directory
    App.tsx
    index.css
    main.tsx
  .gitignore
  README.md
  eslint.config.js
  index.html
  package.json
  tsconfig.app.json
  tsconfig.json
  tsconfig.node.json
  vite.config.ts
docker/  (2 files)
  Dockerfile
  Dockerfile.rocm
docs/  (31 files)
  ar/  (3 files)
    index.md
    inference.md
    install.md
  assets/  (1 files)
    logo.svg
  en/  (3 files)
    index.md
    inference.md
    install.md
  es/  (3 files)
    index.md
    inference.md
    install.md
  ja/  (3 files)
    index.md
    inference.md
    install.md
  ko/  (3 files)
    index.md
    inference.md
    install.md
  pt/  (3 files)
    index.md
    inference.md
    install.md
  stylesheets/  (1 files)
    extra.css
  zh/  (3 files)
    index.md
    inference.md
    install.md
  CNAME
  README.ar.md
  README.es.md
  README.ja.md
  README.ko.md
  README.pt-BR.md
  README.zh.md
  requirements.txt
fish_speech/  (32 files)
  configs/  (1 files)
    modded_dac_vq.yaml
  inference_engine/  (4 files)
    __init__.py
    reference_loader.py
    utils.py
    vq_manager.py
  models/  (19 files)
    dac/  (4 files)
      … 4 files under this directory
    text2semantic/  (15 files)
      … 15 files under this directory
  utils/  (5 files)
    __init__.py
    context.py
    file.py
    schema.py
    utils.py
  content_sequence.py
  conversation.py
  tokenizer.py
tests/  (6 files)
  test_active_kv_attention.py
  test_drama3_chunking.py
  test_fish_omni_backbone.py
  test_fish_omni_generate.py
  test_server_drama3.py
  test_visualization.py
tools/  (10 files)
  server/  (6 files)
    api_utils.py
    exception_handler.py
    inference.py
    model_manager.py
    model_utils.py
    views.py
  api_client.py
  api_server.py
  drama3_ref_test.py
  tts_sample.py
.dockerignore
.gitignore
.pre-commit-config.yaml
.project-root
.readthedocs.yaml
API_FLAGS.txt
LICENSE
README.md
compose.base.yml
compose.rocm.yml
compose.yml
dockerfile.dev
inference.ipynb
mkdocs.yml
pyproject.toml
pyrightconfig.json
```

## Entry points

- [fish_speech/conversation.py:149](https://github.com/fishaudio/fish-speech/blob/0f8a12e8a651062fdee9c33a894bdccd3a8513f1/fish_speech/conversation.py#L149)
- [fish_speech/models/dac/inference.py:71](https://github.com/fishaudio/fish-speech/blob/0f8a12e8a651062fdee9c33a894bdccd3a8513f1/fish_speech/models/dac/inference.py#L71)
- [fish_speech/models/dac/modded_dac.py:999](https://github.com/fishaudio/fish-speech/blob/0f8a12e8a651062fdee9c33a894bdccd3a8513f1/fish_speech/models/dac/modded_dac.py#L999)
- [fish_speech/models/dac/rvq.py:374](https://github.com/fishaudio/fish-speech/blob/0f8a12e8a651062fdee9c33a894bdccd3a8513f1/fish_speech/models/dac/rvq.py#L374)
- [fish_speech/models/text2semantic/inference.py:1216](https://github.com/fishaudio/fish-speech/blob/0f8a12e8a651062fdee9c33a894bdccd3a8513f1/fish_speech/models/text2semantic/inference.py#L1216)
- [tools/api_client.py:161](https://github.com/fishaudio/fish-speech/blob/0f8a12e8a651062fdee9c33a894bdccd3a8513f1/tools/api_client.py#L161)
- [tools/api_server.py:129](https://github.com/fishaudio/fish-speech/blob/0f8a12e8a651062fdee9c33a894bdccd3a8513f1/tools/api_server.py#L129)
- [tools/drama3_ref_test.py:135](https://github.com/fishaudio/fish-speech/blob/0f8a12e8a651062fdee9c33a894bdccd3a8513f1/tools/drama3_ref_test.py#L135)
- [tools/tts_sample.py:95](https://github.com/fishaudio/fish-speech/blob/0f8a12e8a651062fdee9c33a894bdccd3a8513f1/tools/tts_sample.py#L95)
- [awesome_webui/src/App.tsx](https://github.com/fishaudio/fish-speech/blob/0f8a12e8a651062fdee9c33a894bdccd3a8513f1/awesome_webui/src/App.tsx)
- [awesome_webui/src/main.tsx](https://github.com/fishaudio/fish-speech/blob/0f8a12e8a651062fdee9c33a894bdccd3a8513f1/awesome_webui/src/main.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 1 file(s) under api layer (observed from repository paths and static analysis). Observed routes: GET /v1/tts/defaults, POST /v1/vqgan/encode, POST /v1/vqgan/decode, POST /v1/tts, POST /v1/references/add. Observed… |
| awesome_webui package | library | Observed | Groups 18 file(s) under awesome_webui package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 14 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 15 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: Attention, AudioDecoderConfig, BaseModelArgs, BaseTransformer, BaseTransformerForwardResult, DecoderLa… |
| Application entry point | entrypoint | Observed | Groups 8 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: API, Attention, CausalConvNet, CausalTransConvNet, ConvNeXtBlock, Conversation. Observed t… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| fish_speech package | library | Observed | Groups 11 file(s) under fish_speech package (observed from repository paths and static analysis). Observed top-level classes: AddReferenceRequest, AddReferenceResponse, AudioPart, BasePart, ContentSequence, DeleteRefere… |
| Tests | test | Observed | Groups 7 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: ActiveKVAttentionTest, ActiveKVAutoregressiveDecodeTest, ActiveKVProgressionTest, BackboneMatchesHuggingFace… |
| tools package | library | Observed | Groups 5 file(s) under tools package (observed from repository paths and static analysis). Observed top-level classes: ExceptionHandler, ModelManager, MsgPackRequest. Observed top-level functions: batch_encode, batch_vq… |

## Important files

- `.dockerignore` (container)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/workflows/build-docker-image.yml` (ci)
- `.github/workflows/docs.yml` (ci)
- `.github/workflows/stale.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `.readthedocs.yaml` (config)
- `awesome_webui/package.json` (manifest)
- `awesome_webui/tsconfig.app.json` (config)
- `awesome_webui/tsconfig.json` (config)
- `awesome_webui/tsconfig.node.json` (config)
- `compose.base.yml` (config)
- `compose.rocm.yml` (config)
- `compose.yml` (container)
- `docker/Dockerfile` (container)
- `docker/Dockerfile.rocm` (container)
- `dockerfile.dev` (container)
- `docs/requirements.txt` (manifest)
- `fish_speech/configs/modded_dac_vq.yaml` (config)
- `mkdocs.yml` (config)
- `pyproject.toml` (manifest)
- `pyrightconfig.json` (config)

## Top-level layout

- `fish_speech` — 32 analysed file(s)
- `docs` — 31 analysed file(s)
- `awesome_webui` — 28 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `tools` — 10 analysed file(s)
- `.github` — 7 analysed file(s)
- `tests` — 6 analysed file(s)
- `docker` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `0f8a12e8a651062fdee9c33a894bdccd3a8513f1` is the revision these paths and observations refer to.
