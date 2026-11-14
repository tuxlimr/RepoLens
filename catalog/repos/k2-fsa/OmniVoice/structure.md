# Project structure: k2-fsa/OmniVoice

**Analysed commit:** `08be0b4ccbac3e13e374e86fbfead4b4cac343e2`

**Commit reference:** [08be0b4ccbac3e13e374e86fbfead4b4cac343e2](https://github.com/k2-fsa/OmniVoice/commit/08be0b4ccbac3e13e374e86fbfead4b4cac343e2)

**Tree at this commit:** [k2-fsa/OmniVoice@08be0b4ccbac](https://github.com/k2-fsa/OmniVoice/tree/08be0b4ccbac3e13e374e86fbfead4b4cac343e2)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | k2-fsa/OmniVoice |
| Description | High-Quality Voice Cloning TTS for 600+ Languages |
| Stars | 16601 |
| Forks | 2442 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `08be0b4ccbac3e13e374e86fbfead4b4cac343e2` |
| Retrieved at | 2026-11-14T19:08:45.766335+00:00 |
| Files in this snapshot | 88 |

## Directory tree

```text
.github/  (7 files)
  ISSUE_TEMPLATE/  (5 files)
    bug_report.yml
    config.yml
    feature_request.yml
    help_wanted.yml
    question.yml
  workflows/  (2 files)
    publish.yml
    stale.yml
docs/  (12 files)
  OmniVoice.ipynb
  community-projects.md
  data_preparation.md
  data_preparation_advanced.md
  evaluation.md
  generation-parameters.md
  lang_id_name_map.tsv
  languages.md
  lora_finetuning.md
  tips.md
  training.md
  voice-design.md
examples/  (13 files)
  config/  (8 files)
    data_config_emilia.json
    data_config_finetune.json
    ds_config_zero2.json
    train_config_emilia.json
    train_config_finetune.json
    train_config_finetune_lora.json
    train_config_finetune_sdpa.json
    train_config_multilingual.json
  README.md
  run_emilia.sh
  run_eval.sh
  run_finetune.sh
  run_finetune_lora.sh
omnivoice/  (49 files)
  cli/  (6 files)
    __init__.py
    demo.py
    infer.py
    infer_batch.py
    merge_lora.py
    train.py
  data/  (5 files)
    __init__.py
    batching.py
    collator.py
    dataset.py
    processor.py
  eval/  (15 files)
    models/  (2 files)
      … 2 files under this directory
    mos/  (1 files)
      … 1 files under this directory
    speaker_similarity/  (1 files)
      … 1 files under this directory
    wer/  (9 files)
      … 9 files under this directory
    __init__.py
    utils.py
  models/  (3 files)
    __init__.py
    omnivoice.py
    omnivoice_flashinfer.py
  scripts/  (5 files)
    __init__.py
    denoise_audio.py
    extract_audio_tokens.py
    extract_audio_tokens_add_noise.py
    jsonl_to_webdataset.py
  training/  (5 files)
    __init__.py
    builder.py
    checkpoint.py
    config.py
    trainer.py
  utils/  (9 files)
    __init__.py
    audio.py
    common.py
    data_utils.py
    duration.py
    lang_map.py
    lora.py
    text.py
    voice_design.py
  __init__.py
tests/  (1 files)
  test_lora.py
.gitignore
.pre-commit-config.yaml
CONTRIBUTING.md
LICENSE
README.md
pyproject.toml
```

## Entry points

- [omnivoice/cli/demo.py](https://github.com/k2-fsa/OmniVoice/blob/08be0b4ccbac3e13e374e86fbfead4b4cac343e2/omnivoice/cli/demo.py)
- [omnivoice/cli/infer.py](https://github.com/k2-fsa/OmniVoice/blob/08be0b4ccbac3e13e374e86fbfead4b4cac343e2/omnivoice/cli/infer.py)
- [omnivoice/cli/infer_batch.py](https://github.com/k2-fsa/OmniVoice/blob/08be0b4ccbac3e13e374e86fbfead4b4cac343e2/omnivoice/cli/infer_batch.py)
- [omnivoice/cli/merge_lora.py](https://github.com/k2-fsa/OmniVoice/blob/08be0b4ccbac3e13e374e86fbfead4b4cac343e2/omnivoice/cli/merge_lora.py)
- [omnivoice/cli/train.py:73](https://github.com/k2-fsa/OmniVoice/blob/08be0b4ccbac3e13e374e86fbfead4b4cac343e2/omnivoice/cli/train.py#L73)
- [omnivoice/eval/mos/utmos.py:305](https://github.com/k2-fsa/OmniVoice/blob/08be0b4ccbac3e13e374e86fbfead4b4cac343e2/omnivoice/eval/mos/utmos.py#L305)
- [omnivoice/eval/speaker_similarity/sim.py:323](https://github.com/k2-fsa/OmniVoice/blob/08be0b4ccbac3e13e374e86fbfead4b4cac343e2/omnivoice/eval/speaker_similarity/sim.py#L323)
- [omnivoice/eval/wer/fleurs.py:516](https://github.com/k2-fsa/OmniVoice/blob/08be0b4ccbac3e13e374e86fbfead4b4cac343e2/omnivoice/eval/wer/fleurs.py#L516)
- [omnivoice/eval/wer/hubert.py:315](https://github.com/k2-fsa/OmniVoice/blob/08be0b4ccbac3e13e374e86fbfead4b4cac343e2/omnivoice/eval/wer/hubert.py#L315)
- [omnivoice/eval/wer/minimax.py:595](https://github.com/k2-fsa/OmniVoice/blob/08be0b4ccbac3e13e374e86fbfead4b4cac343e2/omnivoice/eval/wer/minimax.py#L595)
- [omnivoice/eval/wer/seedtts.py:410](https://github.com/k2-fsa/OmniVoice/blob/08be0b4ccbac3e13e374e86fbfead4b4cac343e2/omnivoice/eval/wer/seedtts.py#L410)
- [omnivoice/eval/wer/sensevoice.py:342](https://github.com/k2-fsa/OmniVoice/blob/08be0b4ccbac3e13e374e86fbfead4b4cac343e2/omnivoice/eval/wer/sensevoice.py#L342)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: TrainingConfig. |
| Data layer | data | Observed | Groups 10 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AttentiveStatsPool, Conv1dReluBn, ConvFeatureExtractionModel, ECAPA_TDNN_WAVLM, GenerationTask, Iterab… |
| Application entry point | entrypoint | Observed | Groups 17 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: CollateFunction, CollatedBatch, GPUWorkerPool, RuleDurationEstimator, SimpleWorkerSampler… |
| omnivoice package | library | Observed | Groups 20 file(s) under omnivoice package (observed from repository paths and static analysis). Observed top-level classes: OmniTrainer, TrainLogger. Observed top-level functions: _apply_lora, _apply_with_protection, _g… |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: _lora_config, test_build_model_with_lora_freezes_base_and_keeps_io_heads_trainable, test_build_model_witho… |

## Important files

- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/ISSUE_TEMPLATE/help_wanted.yml` (config)
- `.github/ISSUE_TEMPLATE/question.yml` (config)
- `.github/workflows/publish.yml` (ci)
- `.github/workflows/stale.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `examples/config/data_config_emilia.json` (config)
- `examples/config/data_config_finetune.json` (config)
- `examples/config/ds_config_zero2.json` (config)
- `examples/config/train_config_emilia.json` (config)
- `examples/config/train_config_finetune.json` (config)
- `examples/config/train_config_finetune_lora.json` (config)
- `examples/config/train_config_finetune_sdpa.json` (config)
- `examples/config/train_config_multilingual.json` (config)
- `pyproject.toml` (manifest)

## Top-level layout

- `omnivoice` — 49 analysed file(s)
- `examples` — 13 analysed file(s)
- `docs` — 12 analysed file(s)
- `.github` — 7 analysed file(s)
- `(root files)` — 6 analysed file(s)
- `tests` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `08be0b4ccbac3e13e374e86fbfead4b4cac343e2` is the revision these paths and observations refer to.
