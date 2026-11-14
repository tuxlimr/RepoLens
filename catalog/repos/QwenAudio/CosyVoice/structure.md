# Project structure: QwenAudio/CosyVoice

**Analysed commit:** `074ca6dc9e80a2f424f1f74b48bdd7d3fea531cc`

**Commit reference:** [074ca6dc9e80a2f424f1f74b48bdd7d3fea531cc](https://github.com/QwenAudio/CosyVoice/commit/074ca6dc9e80a2f424f1f74b48bdd7d3fea531cc)

**Tree at this commit:** [QwenAudio/CosyVoice@074ca6dc9e80](https://github.com/QwenAudio/CosyVoice/tree/074ca6dc9e80a2f424f1f74b48bdd7d3fea531cc)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | QwenAudio/CosyVoice |
| Description | Multi-lingual large voice generation model, providing inference, training and deployment full-stack ability. |
| Stars | 24403 |
| Forks | 2786 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `074ca6dc9e80a2f424f1f74b48bdd7d3fea531cc` |
| Retrieved at | 2026-11-14T19:07:37.280923+00:00 |
| Files in this snapshot | 152 |

## Directory tree

```text
.github/  (4 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (2 files)
    lint.yml
    stale-issues.yml
cosyvoice/  (49 files)
  bin/  (4 files)
    average_model.py
    export_jit.py
    export_onnx.py
    train.py
  cli/  (4 files)
    __init__.py
    cosyvoice.py
    frontend.py
    model.py
  dataset/  (3 files)
    __init__.py
    dataset.py
    processor.py
  flow/  (6 files)
    DiT/  (2 files)
      … 2 files under this directory
    decoder.py
    flow.py
    flow_matching.py
    length_regulator.py
  hifigan/  (4 files)
    discriminator.py
    f0_predictor.py
    generator.py
    hifigan.py
  llm/  (1 files)
    llm.py
  tokenizer/  (1 files)
    tokenizer.py
  transformer/  (13 files)
    __init__.py
    activation.py
    attention.py
    convolution.py
    decoder.py
    decoder_layer.py
    embedding.py
    encoder.py
    encoder_layer.py
    label_smoothing_loss.py
    positionwise_feed_forward.py
    subsampling.py
    upsample_encoder.py
  utils/  (11 files)
    __init__.py
    class_utils.py
    common.py
    executor.py
    file_utils.py
    frontend_utils.py
    losses.py
    mask.py
    onnx.py
    scheduler.py
    train_utils.py
  vllm/  (1 files)
    cosyvoice2.py
  __init__.py
docker/  (1 files)
  Dockerfile
examples/  (31 files)
  grpo/  (12 files)
    cosyvoice2/  (12 files)
      … 12 files under this directory
  libritts/  (15 files)
    cosyvoice/  (8 files)
      … 8 files under this directory
    cosyvoice2/  (4 files)
      … 4 files under this directory
    cosyvoice3/  (3 files)
      … 3 files under this directory
  magicdata-read/  (4 files)
    cosyvoice/  (4 files)
      … 4 files under this directory
runtime/  (54 files)
  python/  (6 files)
    fastapi/  (2 files)
      … 2 files under this directory
    grpc/  (3 files)
      … 3 files under this directory
    Dockerfile
  triton_trtllm/  (48 files)
    model_repo/  (15 files)
      … 15 files under this directory
    model_repo_cosyvoice3/  (10 files)
      … 10 files under this directory
    scripts/  (4 files)
      … 4 files under this directory
    Dockerfile.server
    README.Cosyvoice2.DiT.md
    README.Cosyvoice2.Unet.md
    README.Cosyvoice3.md
    README.md
    client_grpc.py
    client_http.py
    docker-compose.cosyvoice2.dit.yml
    docker-compose.cosyvoice2.unet.yml
    docker-compose.cosyvoice3.yml
    infer_cosyvoice3.py
    offline_inference.py
    requirements.txt
    run.sh
    run_cosyvoice3.sh
    run_stepaudio2_dit_token2wav.sh
    streaming_inference.py
    token2wav.py
    token2wav_cosyvoice3.py
tools/  (3 files)
  extract_embedding.py
  extract_speech_token.py
  make_parquet_list.py
.gitignore
.gitmodules
CODE_OF_CONDUCT.md
FAQ.md
LICENSE
README.md
example.py
requirements.txt
vllm_example.py
webui.py
```

## Entry points

- [cosyvoice/bin/average_model.py:92](https://github.com/QwenAudio/CosyVoice/blob/074ca6dc9e80a2f424f1f74b48bdd7d3fea531cc/cosyvoice/bin/average_model.py#L92)
- [cosyvoice/bin/export_jit.py:98](https://github.com/QwenAudio/CosyVoice/blob/074ca6dc9e80a2f424f1f74b48bdd7d3fea531cc/cosyvoice/bin/export_jit.py#L98)
- [cosyvoice/bin/export_onnx.py:113](https://github.com/QwenAudio/CosyVoice/blob/074ca6dc9e80a2f424f1f74b48bdd7d3fea531cc/cosyvoice/bin/export_onnx.py#L113)
- [cosyvoice/bin/train.py:194](https://github.com/QwenAudio/CosyVoice/blob/074ca6dc9e80a2f424f1f74b48bdd7d3fea531cc/cosyvoice/bin/train.py#L194)
- [cosyvoice/flow/flow.py:417](https://github.com/QwenAudio/CosyVoice/blob/074ca6dc9e80a2f424f1f74b48bdd7d3fea531cc/cosyvoice/flow/flow.py#L417)
- [cosyvoice/hifigan/generator.py:729](https://github.com/QwenAudio/CosyVoice/blob/074ca6dc9e80a2f424f1f74b48bdd7d3fea531cc/cosyvoice/hifigan/generator.py#L729)
- [example.py:111](https://github.com/QwenAudio/CosyVoice/blob/074ca6dc9e80a2f424f1f74b48bdd7d3fea531cc/example.py#L111)
- [runtime/python/fastapi/client.py:59](https://github.com/QwenAudio/CosyVoice/blob/074ca6dc9e80a2f424f1f74b48bdd7d3fea531cc/runtime/python/fastapi/client.py#L59)
- [runtime/python/fastapi/server.py:30](https://github.com/QwenAudio/CosyVoice/blob/074ca6dc9e80a2f424f1f74b48bdd7d3fea531cc/runtime/python/fastapi/server.py#L30)
- [runtime/python/grpc/client.py:73](https://github.com/QwenAudio/CosyVoice/blob/074ca6dc9e80a2f424f1f74b48bdd7d3fea531cc/runtime/python/grpc/client.py#L73)
- [runtime/python/grpc/server.py:77](https://github.com/QwenAudio/CosyVoice/blob/074ca6dc9e80a2f424f1f74b48bdd7d3fea531cc/runtime/python/grpc/server.py#L77)
- [runtime/triton_trtllm/client_grpc.py:914](https://github.com/QwenAudio/CosyVoice/blob/074ca6dc9e80a2f424f1f74b48bdd7d3fea531cc/runtime/triton_trtllm/client_grpc.py#L914)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 8 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| cosyvoice package | library | Observed | Groups 42 file(s) under cosyvoice package (observed from repository paths and static analysis). Observed top-level classes: AdaLayerNormZero, AdaLayerNormZero_Final, Attention, AttnProcessor, BaseEncoder, BaseSubsamplin… |
| Data layer | data | Observed | Groups 12 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: CosyVoice2, CosyVoice2Model, CosyVoice3Model, CosyVoiceModel, TritonPythonModel, TrtContextWrapper. Ob… |
| Application entry point | entrypoint | Observed | Groups 26 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed routes: GET /inference_sft, POST /inference_sft, GET /infer… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| runtime package | library | Observed | Groups 4 file(s) under runtime package (observed from repository paths and static analysis). Observed top-level classes: CosyVoice3_Token2Wav, TrtContextWrapper. Observed top-level functions: convert_onnx_to_trt. |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: main, parse_arguments, parse_input. |

## Important files

- `.github/workflows/lint.yml` (ci)
- `.github/workflows/stale-issues.yml` (ci)
- `docker/Dockerfile` (container)
- `examples/grpo/cosyvoice2/Dockerfile` (container)
- `examples/grpo/cosyvoice2/requirements.txt` (manifest)
- `examples/libritts/cosyvoice/conf/cosyvoice.yaml` (config)
- `examples/libritts/cosyvoice/conf/ds_stage2.json` (config)
- `examples/libritts/cosyvoice/tts_text.json` (config)
- `examples/libritts/cosyvoice2/conf/cosyvoice2.yaml` (config)
- `examples/libritts/cosyvoice2/conf/ds_stage2.json` (config)
- `examples/libritts/cosyvoice3/conf/cosyvoice3.yaml` (config)
- `examples/libritts/cosyvoice3/conf/ds_stage2.json` (config)
- `examples/magicdata-read/cosyvoice/tts_text.json` (config)
- `requirements.txt` (manifest)
- `runtime/python/Dockerfile` (container)
- `runtime/triton_trtllm/Dockerfile.server` (container)
- `runtime/triton_trtllm/docker-compose.cosyvoice2.dit.yml` (config)
- `runtime/triton_trtllm/docker-compose.cosyvoice2.unet.yml` (config)
- `runtime/triton_trtllm/docker-compose.cosyvoice3.yml` (config)
- `runtime/triton_trtllm/requirements.txt` (manifest)

## Top-level layout

- `runtime` — 54 analysed file(s)
- `cosyvoice` — 49 analysed file(s)
- `examples` — 31 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `.github` — 4 analysed file(s)
- `tools` — 3 analysed file(s)
- `docker` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `074ca6dc9e80a2f424f1f74b48bdd7d3fea531cc` is the revision these paths and observations refer to.
