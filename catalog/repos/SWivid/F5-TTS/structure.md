# Project structure: SWivid/F5-TTS

**Analysed commit:** `600e5fdfbf319f84735557aca80a7aaf60d487e6`

**Commit reference:** [600e5fdfbf319f84735557aca80a7aaf60d487e6](https://github.com/SWivid/F5-TTS/commit/600e5fdfbf319f84735557aca80a7aaf60d487e6)

**Tree at this commit:** [SWivid/F5-TTS@600e5fdfbf31](https://github.com/SWivid/F5-TTS/tree/600e5fdfbf319f84735557aca80a7aaf60d487e6)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | SWivid/F5-TTS |
| Description | Official code for "F5-TTS: A Fairytaler that Fakes Fluent and Faithful Speech with Flow Matching" |
| Stars | 15585 |
| Forks | 2279 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `600e5fdfbf319f84735557aca80a7aaf60d487e6` |
| Retrieved at | 2026-11-14T19:09:00.341298+00:00 |
| Files in this snapshot | 91 |

## Directory tree

```text
.github/  (8 files)
  ISSUE_TEMPLATE/  (5 files)
    bug_report.yml
    config.yml
    feature_request.yml
    help_wanted.yml
    question.yml
  workflows/  (3 files)
    pre-commit.yaml
    publish-docker-image.yaml
    publish-pypi.yaml
ckpts/  (1 files)
  README.md
data/  (1 files)
  Emilia_ZH_EN_pinyin/  (1 files)
    vocab.txt
src/  (73 files)
  f5_tts/  (73 files)
    configs/  (6 files)
      … 6 files under this directory
    eval/  (9 files)
      … 9 files under this directory
    infer/  (10 files)
      … 10 files under this directory
    model/  (10 files)
      … 10 files under this directory
    runtime/  (21 files)
      … 21 files under this directory
    scripts/  (3 files)
      … 3 files under this directory
    train/  (10 files)
      … 10 files under this directory
    api.py
    device_utils.py
    socket_client.py
    socket_server.py
.gitignore
.gitmodules
.pre-commit-config.yaml
Dockerfile
LICENSE
README.md
pyproject.toml
ruff.toml
```

## Entry points

- [src/f5_tts/api.py:143](https://github.com/SWivid/F5-TTS/blob/600e5fdfbf319f84735557aca80a7aaf60d487e6/src/f5_tts/api.py#L143)
- [src/f5_tts/eval/eval_infer_batch.py:220](https://github.com/SWivid/F5-TTS/blob/600e5fdfbf319f84735557aca80a7aaf60d487e6/src/f5_tts/eval/eval_infer_batch.py#L220)
- [src/f5_tts/eval/eval_librispeech_test_clean.py:104](https://github.com/SWivid/F5-TTS/blob/600e5fdfbf319f84735557aca80a7aaf60d487e6/src/f5_tts/eval/eval_librispeech_test_clean.py#L104)
- [src/f5_tts/eval/eval_seedtts_testset.py:103](https://github.com/SWivid/F5-TTS/blob/600e5fdfbf319f84735557aca80a7aaf60d487e6/src/f5_tts/eval/eval_seedtts_testset.py#L103)
- [src/f5_tts/eval/eval_utmos.py:43](https://github.com/SWivid/F5-TTS/blob/600e5fdfbf319f84735557aca80a7aaf60d487e6/src/f5_tts/eval/eval_utmos.py#L43)
- [src/f5_tts/infer/infer_cli.py](https://github.com/SWivid/F5-TTS/blob/600e5fdfbf319f84735557aca80a7aaf60d487e6/src/f5_tts/infer/infer_cli.py)
- [src/f5_tts/infer/infer_gradio.py](https://github.com/SWivid/F5-TTS/blob/600e5fdfbf319f84735557aca80a7aaf60d487e6/src/f5_tts/infer/infer_gradio.py)
- [src/f5_tts/runtime/triton_trtllm/benchmark.py:474](https://github.com/SWivid/F5-TTS/blob/600e5fdfbf319f84735557aca80a7aaf60d487e6/src/f5_tts/runtime/triton_trtllm/benchmark.py#L474)
- [src/f5_tts/runtime/triton_trtllm/client_grpc.py:458](https://github.com/SWivid/F5-TTS/blob/600e5fdfbf319f84735557aca80a7aaf60d487e6/src/f5_tts/runtime/triton_trtllm/client_grpc.py#L458)
- [src/f5_tts/runtime/triton_trtllm/client_http.py:123](https://github.com/SWivid/F5-TTS/blob/600e5fdfbf319f84735557aca80a7aaf60d487e6/src/f5_tts/runtime/triton_trtllm/client_http.py#L123)
- [src/f5_tts/runtime/triton_trtllm/scripts/convert_checkpoint.py:287](https://github.com/SWivid/F5-TTS/blob/600e5fdfbf319f84735557aca80a7aaf60d487e6/src/f5_tts/runtime/triton_trtllm/scripts/convert_checkpoint.py#L287)
- [src/f5_tts/runtime/triton_trtllm/scripts/export_vocoder_to_onnx.py:134](https://github.com/SWivid/F5-TTS/blob/600e5fdfbf319f84735557aca80a7aaf60d487e6/src/f5_tts/runtime/triton_trtllm/scripts/export_vocoder_to_onnx.py#L134)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 13 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 2 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: F5TTS, InputEmbedding, TritonPythonModel. Observed top-level functions: convert_char_to_pinyin, get_tok… |
| Application entry point | entrypoint | Observed | Groups 24 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: AudioFileWriterThread, F5TTS, ISTFTHead, Slicer, TTSStreamingProcessor, VocosTensorRT. Ob… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| f5_tts package | library | Observed | Groups 25 file(s) under f5_tts package (observed from repository paths and static analysis). Observed top-level classes: AdaLayerNorm, AdaLayerNormZero, AdaLayerNormZero_Final, AdaLayerNorm_Final, Attention, AttentiveSt… |

## Important files

- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/ISSUE_TEMPLATE/help_wanted.yml` (config)
- `.github/ISSUE_TEMPLATE/question.yml` (config)
- `.github/workflows/pre-commit.yaml` (ci)
- `.github/workflows/publish-docker-image.yaml` (ci)
- `.github/workflows/publish-pypi.yaml` (ci)
- `.pre-commit-config.yaml` (config)
- `Dockerfile` (container)
- `pyproject.toml` (manifest)
- `ruff.toml` (config)
- `src/f5_tts/configs/E2TTS_Base.yaml` (config)
- `src/f5_tts/configs/E2TTS_Small.yaml` (config)
- `src/f5_tts/configs/F5TTS_Base.yaml` (config)
- `src/f5_tts/configs/F5TTS_Small.yaml` (config)
- `src/f5_tts/configs/F5TTS_v1_Base.yaml` (config)
- `src/f5_tts/configs/F5TTS_v1_Small.yaml` (config)
- `src/f5_tts/infer/examples/basic/basic.toml` (config)
- `src/f5_tts/infer/examples/multi/story.toml` (config)
- `src/f5_tts/runtime/triton_trtllm/Dockerfile.server` (container)
- `src/f5_tts/runtime/triton_trtllm/docker-compose.yml` (container)

## Top-level layout

- `src` — 73 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `.github` — 8 analysed file(s)
- `ckpts` — 1 analysed file(s)
- `data` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `600e5fdfbf319f84735557aca80a7aaf60d487e6` is the revision these paths and observations refer to.
