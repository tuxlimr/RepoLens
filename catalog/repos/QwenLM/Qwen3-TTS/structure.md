# Project structure: QwenLM/Qwen3-TTS

**Analysed commit:** `022e286b98fbec7e1e916cb940cdf532cd9f488e`

**Commit reference:** [022e286b98fbec7e1e916cb940cdf532cd9f488e](https://github.com/QwenLM/Qwen3-TTS/commit/022e286b98fbec7e1e916cb940cdf532cd9f488e)

**Tree at this commit:** [QwenLM/Qwen3-TTS@022e286b98fb](https://github.com/QwenLM/Qwen3-TTS/tree/022e286b98fbec7e1e916cb940cdf532cd9f488e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | QwenLM/Qwen3-TTS |
| Description | Qwen3-TTS is an open-source series of TTS models developed by the Qwen team at Alibaba Cloud, supporting stable, expressive, and streaming speech generation, free-form voice design, and vivid voice cloning. |
| Stars | 14414 |
| Forks | 1860 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `022e286b98fbec7e1e916cb940cdf532cd9f488e` |
| Retrieved at | 2026-11-14T19:09:26.253574+00:00 |
| Files in this snapshot | 34 |

## Directory tree

```text
.github/  (4 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.yml
    config.yml
  workflows/  (2 files)
    inactive.yaml
    translate.yaml
examples/  (4 files)
  test_model_12hz_base.py
  test_model_12hz_custom_voice.py
  test_model_12hz_voice_design.py
  test_tokenizer_12hz.py
finetuning/  (4 files)
  README.md
  dataset.py
  prepare_data.py
  sft_12hz.py
qwen_tts/  (17 files)
  cli/  (1 files)
    demo.py
  core/  (12 files)
    models/  (4 files)
      … 4 files under this directory
    tokenizer_12hz/  (2 files)
      … 2 files under this directory
    tokenizer_25hz/  (5 files)
      … 5 files under this directory
    __init__.py
  inference/  (2 files)
    qwen3_tts_model.py
    qwen3_tts_tokenizer.py
  __init__.py
  __main__.py
.gitignore
LICENSE
MANIFEST.in
README.md
pyproject.toml
```

## Entry points

- [finetuning/prepare_data.py:70](https://github.com/QwenLM/Qwen3-TTS/blob/022e286b98fbec7e1e916cb940cdf532cd9f488e/finetuning/prepare_data.py#L70)
- [finetuning/sft_12hz.py:160](https://github.com/QwenLM/Qwen3-TTS/blob/022e286b98fbec7e1e916cb940cdf532cd9f488e/finetuning/sft_12hz.py#L160)
- [qwen_tts/__main__.py:23](https://github.com/QwenLM/Qwen3-TTS/blob/022e286b98fbec7e1e916cb940cdf532cd9f488e/qwen_tts/__main__.py#L23)
- [qwen_tts/cli/demo.py](https://github.com/QwenLM/Qwen3-TTS/blob/022e286b98fbec7e1e916cb940cdf532cd9f488e/qwen_tts/cli/demo.py)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 4 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AttentiveStatisticsPooling, Qwen3TTSAttention, Qwen3TTSConfig, Qwen3TTSDecoderLayer, Qwen3TTSForConditi… |
| Application entry point | entrypoint | Observed | Groups 4 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: _audio_to_tuple, _build_choices_and_map, _collect_gen_kwargs, _detect_model_kind, _dtype… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| finetuning package | library | Observed | Groups 1 file(s) under finetuning package (observed from repository paths and static analysis). Observed top-level classes: TTSDataset. |
| qwen_tts package | library | Observed | Groups 3 file(s) under qwen_tts package (observed from repository paths and static analysis). Observed top-level classes: Qwen3TTSModel, Qwen3TTSTokenizer, VoiceClonePromptItem. |
| Service / domain layer | service | Observed | Groups 8 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: AMPBlock, AdaLayerNormZero, AdaLayerNormZero_Final, AttentiveStatisticsPooling, CausalConv1… |
| Tests | test | Observed | Groups 4 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: ensure_dir, main, run_case. |

## Important files

- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/inactive.yaml` (ci)
- `.github/workflows/translate.yaml` (ci)
- `MANIFEST.in` (manifest)
- `pyproject.toml` (manifest)

## Top-level layout

- `qwen_tts` — 17 analysed file(s)
- `(root files)` — 5 analysed file(s)
- `.github` — 4 analysed file(s)
- `examples` — 4 analysed file(s)
- `finetuning` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `022e286b98fbec7e1e916cb940cdf532cd9f488e` is the revision these paths and observations refer to.
