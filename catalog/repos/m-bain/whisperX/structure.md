# Project structure: m-bain/whisperX

**Analysed commit:** `b904f02b7e1f26fd10fb04840d655ff27e88e464`

**Commit reference:** [b904f02b7e1f26fd10fb04840d655ff27e88e464](https://github.com/m-bain/whisperX/commit/b904f02b7e1f26fd10fb04840d655ff27e88e464)

**Tree at this commit:** [m-bain/whisperX@b904f02b7e1f](https://github.com/m-bain/whisperX/tree/b904f02b7e1f26fd10fb04840d655ff27e88e464)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | m-bain/whisperX |
| Description | WhisperX:  Automatic Speech Recognition with Word-level Timestamps (& Diarization) |
| Stars | 25269 |
| Forks | 2548 |
| Licence | BSD-2-Clause |
| Language | Python |
| Default branch | main |
| Analysed commit | `b904f02b7e1f26fd10fb04840d655ff27e88e464` |
| Retrieved at | 2026-11-14T19:07:33.401967+00:00 |
| Files in this snapshot | 32 |

## Directory tree

```text
.github/  (5 files)
  workflows/  (4 files)
    build-and-release.yml
    python-compatibility.yml
    tests.yml
    zizmor.yml
  FUNDING.yml
tests/  (2 files)
  test_align_model_fallback.py
  test_word_timestamp_interpolation.py
whisperx/  (17 files)
  vads/  (4 files)
    __init__.py
    pyannote.py
    silero.py
    vad.py
  SubtitlesProcessor.py
  __init__.py
  __main__.py
  alignment.py
  asr.py
  audio.py
  conjunctions.py
  device_utils.py
  diarize.py
  log_utils.py
  schema.py
  transcribe.py
  utils.py
.gitignore
.python-version
CUDNN_TROUBLESHOOTING.md
EXAMPLES.md
LICENSE
MANIFEST.in
README.md
pyproject.toml
```

## Entry points

- [whisperx/__main__.py](https://github.com/m-bain/whisperX/blob/b904f02b7e1f26fd10fb04840d655ff27e88e464/whisperx/__main__.py)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: cli. |
| Tests | test | Observed | Groups 2 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: TestAlignWithWildcards, TestInterpolateNans. Observed top-level functions: _make_emission, _make_mock_model,… |
| whisperx package | library | Observed | Groups 16 file(s) under whisperx package (observed from repository paths and static analysis). Observed top-level classes: AlignedTranscriptionResult, Binarize, DiarizationPipeline, FasterWhisperPipeline, IntervalTree,… |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/workflows/build-and-release.yml` (ci)
- `.github/workflows/python-compatibility.yml` (ci)
- `.github/workflows/tests.yml` (ci)
- `.github/workflows/zizmor.yml` (ci)
- `MANIFEST.in` (manifest)
- `pyproject.toml` (manifest)

## Top-level layout

- `whisperx` — 17 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `.github` — 5 analysed file(s)
- `tests` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `b904f02b7e1f26fd10fb04840d655ff27e88e464` is the revision these paths and observations refer to.
