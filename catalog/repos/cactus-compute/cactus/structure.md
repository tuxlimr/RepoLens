# Project structure: cactus-compute/cactus

**Analysed commit:** `44f8e0ec1ec71dddf028e7c37635cce01b3cdcc5`

**Commit reference:** [44f8e0ec1ec71dddf028e7c37635cce01b3cdcc5](https://github.com/cactus-compute/cactus/commit/44f8e0ec1ec71dddf028e7c37635cce01b3cdcc5)

**Tree at this commit:** [cactus-compute/cactus@44f8e0ec1ec7](https://github.com/cactus-compute/cactus/tree/44f8e0ec1ec71dddf028e7c37635cce01b3cdcc5)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | cactus-compute/cactus |
| Description | Sub-50mb agentic, voice and vision intelligence for consumer devices. |
| Stars | 14734 |
| Forks | 1035 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `44f8e0ec1ec71dddf028e7c37635cce01b3cdcc5` |
| Retrieved at | 2026-11-14T19:09:18.430541+00:00 |
| Files in this snapshot | 122 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (3 files)
    publish-component.yaml
    release.yaml
    verify.yaml
assets/  (1 files)
  banner.svg
cactus/  (76 files)
  agent/  (9 files)
    __init__.py
    audio.py
    fetch.py
    grounding.py
    mirage.py
    runtime.py
    text.py
    tools.py
    whistle.py
  cli/  (6 files)
    __init__.py
    download.py
    logging.py
    parser.py
    speech.py
    vision.py
  environments/  (8 files)
    __init__.py
    _harness.py
    data_capture.py
    kitchen_appliance.py
    media_player.py
    productivity.py
    smart_home.py
    wearable.py
  mlx/  (29 files)
    kernels/  (8 files)
      … 8 files under this directory
    models/  (8 files)
      … 8 files under this directory
    NOTICE
    __init__.py
    _environment.py
    bench_decode.py
    checkpoint.py
    cli.py
    generate.py
    generation.py
    ops.py
    reference.py
    runtime.py
    server.py
    vision.py
  model/  (14 files)
    __init__.py
    architecture.py
    architecture_mlx.py
    build.py
    checkpoints.py
    config.py
    export.py
    finetune.py
    quantize.py
    quantize_mlx.py
    run.py
    tokenizer.py
    whistle.py
    whistle_finetune.py
  playground/  (5 files)
    __init__.py
    app.js
    index.html
    server.py
    style.css
  __init__.py
  __main__.py
  _telemetry.py
  _worker.py
  platform.py
scripts/  (1 files)
  smoke.py
tests/  (31 files)
  mlx_inference/  (7 files)
    __init__.py
    test_checkpoint.py
    test_embedding.py
    test_fused_activation.py
    test_mtp.py
    test_runtime.py
    test_vision.py
  conftest.py
  test_build.py
  test_environments.py
  test_fetch.py
  test_finetune.py
  test_generate.py
  test_grounding.py
  test_inference.py
  test_lora.py
  test_mirage.py
  test_mlx.py
  test_mlx_entrypoint.py
  test_packaging.py
  test_platform.py
  test_playground.py
  test_quantize_mlx.py
  test_release.py
  test_render.py
  test_run.py
  test_tools.py
  test_weights.py
  test_whistle.py
  test_whistle_finetune.py
  test_worker.py
.gitignore
LICENSE
MANIFEST.in
README.md
llms.txt
pyproject.toml
requirements-train.txt
requirements.txt
setup
setup.bat
```

## Entry points

- [cactus/_worker.py:294](https://github.com/cactus-compute/cactus/blob/44f8e0ec1ec71dddf028e7c37635cce01b3cdcc5/cactus/_worker.py#L294)
- [cactus/cli/__init__.py](https://github.com/cactus-compute/cactus/blob/44f8e0ec1ec71dddf028e7c37635cce01b3cdcc5/cactus/cli/__init__.py)
- [cactus/environments/data_capture.py:131](https://github.com/cactus-compute/cactus/blob/44f8e0ec1ec71dddf028e7c37635cce01b3cdcc5/cactus/environments/data_capture.py#L131)
- [cactus/environments/kitchen_appliance.py:120](https://github.com/cactus-compute/cactus/blob/44f8e0ec1ec71dddf028e7c37635cce01b3cdcc5/cactus/environments/kitchen_appliance.py#L120)
- [cactus/environments/media_player.py:103](https://github.com/cactus-compute/cactus/blob/44f8e0ec1ec71dddf028e7c37635cce01b3cdcc5/cactus/environments/media_player.py#L103)
- [cactus/environments/productivity.py:132](https://github.com/cactus-compute/cactus/blob/44f8e0ec1ec71dddf028e7c37635cce01b3cdcc5/cactus/environments/productivity.py#L132)
- [cactus/environments/smart_home.py:138](https://github.com/cactus-compute/cactus/blob/44f8e0ec1ec71dddf028e7c37635cce01b3cdcc5/cactus/environments/smart_home.py#L138)
- [cactus/environments/wearable.py:110](https://github.com/cactus-compute/cactus/blob/44f8e0ec1ec71dddf028e7c37635cce01b3cdcc5/cactus/environments/wearable.py#L110)
- [cactus/mlx/bench_decode.py:132](https://github.com/cactus-compute/cactus/blob/44f8e0ec1ec71dddf028e7c37635cce01b3cdcc5/cactus/mlx/bench_decode.py#L132)
- [cactus/mlx/cli.py](https://github.com/cactus-compute/cactus/blob/44f8e0ec1ec71dddf028e7c37635cce01b3cdcc5/cactus/mlx/cli.py)
- [cactus/mlx/generate.py:136](https://github.com/cactus-compute/cactus/blob/44f8e0ec1ec71dddf028e7c37635cce01b3cdcc5/cactus/mlx/generate.py#L136)
- [cactus/mlx/models/nemotron_validate.py:102](https://github.com/cactus-compute/cactus/blob/44f8e0ec1ec71dddf028e7c37635cce01b3cdcc5/cactus/mlx/models/nemotron_validate.py#L102)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| cactus package | library | Observed | Groups 42 file(s) under cactus package (observed from repository paths and static analysis). Observed top-level classes: Block, Book, CQEmbedding, CQExperts, CQLinear, Cactus. Observed top-level functions: __dir__, __ge… |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: TransformerConfig. Observed top-level functions: _hada_blocks, _ladder_layer_order, _… |
| Data layer | data | Observed | Groups 7 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: CQModel, DecodeGraph, MTPDecoder, MTPHead, VerificationState, VerifyGraph. Observed top-level functions… |
| Application entry point | entrypoint | Observed | Groups 15 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: CQModelProvider, Engine, FineTuneWorker, _Handler. Observed top-level functions: __getatt… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). Observed top-level functions: check_text, set_thermostat. |
| Tests | test | Observed | Groups 31 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: Engine, FakePlatform, Invoice, LineItem, Order, Shipment. Observed top-level functions: _build_args, _call,… |

## Important files

- `.github/workflows/publish-component.yaml` (ci)
- `.github/workflows/release.yaml` (ci)
- `.github/workflows/verify.yaml` (ci)
- `MANIFEST.in` (manifest)
- `pyproject.toml` (manifest)
- `requirements-train.txt` (manifest)
- `requirements.txt` (manifest)

## Top-level layout

- `cactus` — 76 analysed file(s)
- `tests` — 31 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `.github` — 3 analysed file(s)
- `assets` — 1 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `44f8e0ec1ec71dddf028e7c37635cce01b3cdcc5` is the revision these paths and observations refer to.
