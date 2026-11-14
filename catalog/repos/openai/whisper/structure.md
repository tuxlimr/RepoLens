# Project structure: openai/whisper

**Analysed commit:** `86098128c0b4f24f0e2aa2994de830614b474227`

**Commit reference:** [86098128c0b4f24f0e2aa2994de830614b474227](https://github.com/openai/whisper/commit/86098128c0b4f24f0e2aa2994de830614b474227)

**Tree at this commit:** [openai/whisper@86098128c0b4](https://github.com/openai/whisper/tree/86098128c0b4f24f0e2aa2994de830614b474227)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | openai/whisper |
| Description | Robust Speech Recognition via Large-Scale Weak Supervision |
| Stars | 112698 |
| Forks | 13668 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `86098128c0b4f24f0e2aa2994de830614b474227` |
| Retrieved at | 2026-11-14T19:06:07.235001+00:00 |
| Files in this snapshot | 38 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (2 files)
    python-publish.yml
    test.yml
  dependabot.yml
data/  (2 files)
  README.md
  meanwhile.json
notebooks/  (1 files)
  LibriSpeech.ipynb
tests/  (6 files)
  conftest.py
  test_audio.py
  test_normalizer.py
  test_timing.py
  test_tokenizer.py
  test_transcribe.py
whisper/  (15 files)
  normalizers/  (4 files)
    __init__.py
    basic.py
    english.json
    english.py
  __init__.py
  __main__.py
  audio.py
  decoding.py
  model.py
  timing.py
  tokenizer.py
  transcribe.py
  triton_ops.py
  utils.py
  version.py
.flake8
.gitattributes
.gitignore
.pre-commit-config.yaml
CHANGELOG.md
LICENSE
MANIFEST.in
README.md
model-card.md
pyproject.toml
requirements.txt
```

## Entry points

- [whisper/transcribe.py](https://github.com/openai/whisper/blob/86098128c0b4f24f0e2aa2994de830614b474227/whisper/transcribe.py)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AudioEncoder, Conv1d, LayerNorm, Linear, ModelDimensions, MultiHeadAttention. Observed top-level functi… |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: cli, transcribe. |
| Tests | test | Observed | Groups 6 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: pytest_configure, random, test_audio, test_dtw, test_dtw_cuda_equivalence, test_median_filter. |
| whisper package | library | Observed | Groups 11 file(s) under whisper package (observed from repository paths and static analysis). Observed top-level classes: ApplyTimestampRules, BasicTextNormalizer, BeamSearchDecoder, DecodingOptions, DecodingResult, Dec… |

## Important files

- `.github/dependabot.yml` (config)
- `.github/workflows/python-publish.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `MANIFEST.in` (manifest)
- `data/meanwhile.json` (config)
- `pyproject.toml` (manifest)
- `requirements.txt` (manifest)
- `whisper/normalizers/english.json` (config)

## Top-level layout

- `whisper` — 15 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `tests` — 6 analysed file(s)
- `.github` — 3 analysed file(s)
- `data` — 2 analysed file(s)
- `notebooks` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `86098128c0b4f24f0e2aa2994de830614b474227` is the revision these paths and observations refer to.
