# Project structure: index-tts/index-tts

**Analysed commit:** `d9e41aac89fd00b3d71497fddb287b7f24613712`

**Commit reference:** [d9e41aac89fd00b3d71497fddb287b7f24613712](https://github.com/index-tts/index-tts/commit/d9e41aac89fd00b3d71497fddb287b7f24613712)

**Tree at this commit:** [index-tts/index-tts@d9e41aac89fd](https://github.com/index-tts/index-tts/tree/d9e41aac89fd00b3d71497fddb287b7f24613712)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | index-tts/index-tts |
| Description | An Industrial-Level Controllable and Efficient Zero-Shot Text-To-Speech System |
| Stars | 25091 |
| Forks | 2942 |
| Licence | Other |
| Language | Python |
| Default branch | main |
| Analysed commit | `d9e41aac89fd00b3d71497fddb287b7f24613712` |
| Retrieved at | 2026-11-14T19:07:34.903613+00:00 |
| Files in this snapshot | 323 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (2 files)
    ci.yml
    docker-publish.yml
  pull_request_template.md
archive/  (3 files)
  README_INDEXTTS_1_5.md
  README_INDEXTTS_2.md
  README_INDEXTTS_2_ZH.md
backends/  (49 files)
  trt/  (48 files)
    build_engines/  (9 files)
      … 9 files under this directory
    export/  (10 files)
      … 10 files under this directory
    pipeline/  (7 files)
      … 7 files under this directory
    runtime/  (3 files)
      … 3 files under this directory
    scripts/  (4 files)
      … 4 files under this directory
    serving/  (2 files)
      … 2 files under this directory
    trtllm/  (6 files)
      … 6 files under this directory
    .gitignore
    README.md
    __init__.py
    infer.py
    pyproject.toml
    run.sh
    utils.py
  __init__.py
checkpoints/  (1 files)
  pinyin.vocab
cli_tests/  (6 files)
  __init__.py
  test_cli_v2_batch.py
  test_cli_v2_check.py
  test_cli_v2_concat.py
  test_cli_v2_config.py
  test_cli_v2_download.py
docs/  (6 files)
  README2.5_ZH.md
  README_ar.md
  README_es.md
  README_ja.md
  README_zh.md
  cli_v2_usage.md
examples/  (6 files)
  batch/  (5 files)
    texts/  (1 files)
      … 1 files under this directory
    auto-output.jsonl
    batch-concat.jsonl
    concat-audio.jsonl
    demo.jsonl
  cases.jsonl
indextts/  (221 files)
  BigVGAN/  (27 files)
    alias_free_activation/  (13 files)
      … 13 files under this directory
    alias_free_torch/  (4 files)
      … 4 files under this directory
    nnet/  (4 files)
      … 4 files under this directory
    ECAPA_TDNN.py
    __init__.py
    activations.py
    bigvgan.py
    models.py
    utils.py
  accel/  (5 files)
    __init__.py
    accel_engine.py
    attention.py
    gpt2_accel.py
    kv_manager.py
  codec/  (9 files)
    amphion_codec/  (5 files)
      … 5 files under this directory
    kmeans/  (1 files)
      … 1 files under this directory
    __init__.py
    maskgct_codec.py
    models.py
  gpt/  (12 files)
    conformer/  (4 files)
      … 4 files under this directory
    __init__.py
    conformer_encoder.py
    model.py
    model_v2.py
    model_v2_5.py
    perceiver.py
    transformers_beam_search.py
    transformers_gpt2.py
  s2mel/  (81 files)
    dac/  (14 files)
      … 14 files under this directory
    modules/  (65 files)
      … 65 files under this directory
    optimizers.py
    wav2vecbert_extract.py
  utils/  (79 files)
    maskgct/  (60 files)
      … 60 files under this directory
    __init__.py
    arch_util.py
    checkpoint.py
    common.py
    examples_downloader.py
    feature_extractors.py
    front.py
    ja_g2p.py
    maskgct_utils.py
    model_download.py
    nemo_tn.py
    network_detection.py
    presets.py
    text_utils.py
    tokenizer.py
    typical_sampling.py
    utils.py
    webui_utils.py
    xtransformers.py
  vqvae/  (2 files)
    __init__.py
    xtts_dvae.py
  __init__.py
  cli.py
  cli_v2.py
  infer.py
  infer_v2.py
  infer_v2_5.py
tests/  (10 files)
  cases.jsonl
  conftest.py
  padding_test.py
  regression_test.py
  test_audio_save.py
  test_tail_fade.py
  test_v1.py
  test_v2.py
  test_webui_handlers.py
  test_webui_syntax.py
tools/  (8 files)
  i18n/  (7 files)
    locale/  (5 files)
      … 5 files under this directory
    i18n.py
    scan_i18n.py
  gpu_check.py
.gitattributes
.gitignore
.python-version
DISCLAIMER
LICENSE
LICENSE_ZH.txt
MANIFEST.in
README.md
pyproject.toml
webui.py
```

## Entry points

- [backends/trt/build_engines/build_bigvgan_trt.py:95](https://github.com/index-tts/index-tts/blob/d9e41aac89fd00b3d71497fddb287b7f24613712/backends/trt/build_engines/build_bigvgan_trt.py#L95)
- [backends/trt/build_engines/build_campplus_trt.py:95](https://github.com/index-tts/index-tts/blob/d9e41aac89fd00b3d71497fddb287b7f24613712/backends/trt/build_engines/build_campplus_trt.py#L95)
- [backends/trt/build_engines/build_dit_trt.py:120](https://github.com/index-tts/index-tts/blob/d9e41aac89fd00b3d71497fddb287b7f24613712/backends/trt/build_engines/build_dit_trt.py#L120)
- [backends/trt/build_engines/build_emotion_perceiver_conditioner_trt.py:100](https://github.com/index-tts/index-tts/blob/d9e41aac89fd00b3d71497fddb287b7f24613712/backends/trt/build_engines/build_emotion_perceiver_conditioner_trt.py#L100)
- [backends/trt/build_engines/build_latent_projector_trt.py:100](https://github.com/index-tts/index-tts/blob/d9e41aac89fd00b3d71497fddb287b7f24613712/backends/trt/build_engines/build_latent_projector_trt.py#L100)
- [backends/trt/build_engines/build_length_regulator_trt.py:106](https://github.com/index-tts/index-tts/blob/d9e41aac89fd00b3d71497fddb287b7f24613712/backends/trt/build_engines/build_length_regulator_trt.py#L106)
- [backends/trt/build_engines/build_semantic_codec_trt.py:95](https://github.com/index-tts/index-tts/blob/d9e41aac89fd00b3d71497fddb287b7f24613712/backends/trt/build_engines/build_semantic_codec_trt.py#L95)
- [backends/trt/build_engines/build_speaker_perceiver_conditioner_trt.py:127](https://github.com/index-tts/index-tts/blob/d9e41aac89fd00b3d71497fddb287b7f24613712/backends/trt/build_engines/build_speaker_perceiver_conditioner_trt.py#L127)
- [backends/trt/build_engines/build_speech_semantic_encoder_trt.py:100](https://github.com/index-tts/index-tts/blob/d9e41aac89fd00b3d71497fddb287b7f24613712/backends/trt/build_engines/build_speech_semantic_encoder_trt.py#L100)
- [backends/trt/export/export_bigvgan_onnx.py:95](https://github.com/index-tts/index-tts/blob/d9e41aac89fd00b3d71497fddb287b7f24613712/backends/trt/export/export_bigvgan_onnx.py#L95)
- [backends/trt/export/export_campplus_onnx.py:49](https://github.com/index-tts/index-tts/blob/d9e41aac89fd00b3d71497fddb287b7f24613712/backends/trt/export/export_campplus_onnx.py#L49)
- [backends/trt/export/export_dit_onnx.py:185](https://github.com/index-tts/index-tts/blob/d9e41aac89fd00b3d71497fddb287b7f24613712/backends/trt/export/export_dit_onnx.py#L185)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| backends package | library | Observed | Groups 21 file(s) under backends package (observed from repository paths and static analysis). Observed top-level classes: AudioChunk, BatchAudioChunk, FasterIndexTTS2, GPTTRTEngine, GenericTRTEngine, IndexTTS2GPTForCau… |
| cli_tests package | library | Observed | Groups 1 file(s) under cli_tests package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 11 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: TTSConfig. Observed top-level functions: load_config. |
| Data layer | data | Observed | Groups 61 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AMPBlock1, AMPBlock2, Activation1d, AdaLayerNorm, AdaptiveLayerNorm, Attention. Observed top-level fun… |
| Application entry point | entrypoint | Observed | Groups 50 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: ArithmeticCoder, ArithmeticDecoder, BatchFileError, ConcatExecutionError, ConcatFileError… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| indextts package | library | Observed | Groups 132 file(s) under indextts package (observed from repository paths and static analysis). Observed top-level classes: AMPBlock1, AMPBlock2, AbsolutePositionalEmbedding, AccelInferenceEngine, Activation1d, AdaLayer… |
| Tests | test | Observed | Groups 15 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: BatchCommandDryRunTests, BatchCommandExecutionTests, CheckCommandTests, ConcatCommandDryRunTests, ConfigCom… |

## Important files

- `.github/workflows/ci.yml` (ci)
- `.github/workflows/docker-publish.yml` (ci)
- `MANIFEST.in` (manifest)
- `backends/trt/pyproject.toml` (manifest)
- `indextts/s2mel/modules/bigvgan/config.json` (config)
- `indextts/s2mel/modules/openvoice/checkpoints_v2/converter/config.json` (config)
- `pyproject.toml` (manifest)
- `tools/i18n/locale/ar_SA.json` (config)
- `tools/i18n/locale/en_US.json` (config)
- `tools/i18n/locale/es_ES.json` (config)
- `tools/i18n/locale/ja_JP.json` (config)
- `tools/i18n/locale/zh_CN.json` (config)

## Top-level layout

- `indextts` — 221 analysed file(s)
- `backends` — 49 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `tests` — 10 analysed file(s)
- `tools` — 8 analysed file(s)
- `cli_tests` — 6 analysed file(s)
- `docs` — 6 analysed file(s)
- `examples` — 6 analysed file(s)
- `.github` — 3 analysed file(s)
- `archive` — 3 analysed file(s)
- `checkpoints` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `d9e41aac89fd00b3d71497fddb287b7f24613712` is the revision these paths and observations refer to.
