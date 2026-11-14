# Project structure: SYSTRAN/faster-whisper

**Analysed commit:** `6cb639e70786aea42b9233006ae60eaf07190bdb`

**Commit reference:** [6cb639e70786aea42b9233006ae60eaf07190bdb](https://github.com/SYSTRAN/faster-whisper/commit/6cb639e70786aea42b9233006ae60eaf07190bdb)

**Tree at this commit:** [SYSTRAN/faster-whisper@6cb639e70786](https://github.com/SYSTRAN/faster-whisper/tree/6cb639e70786aea42b9233006ae60eaf07190bdb)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | SYSTRAN/faster-whisper |
| Description | Faster Whisper transcription with CTranslate2 |
| Stars | 26751 |
| Forks | 2244 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `6cb639e70786aea42b9233006ae60eaf07190bdb` |
| Retrieved at | 2026-11-14T19:07:22.646424+00:00 |
| Files in this snapshot | 32 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    ci.yml
benchmark/  (7 files)
  evaluate_yt_commons.py
  memory_benchmark.py
  normalizer.json
  requirements.benchmark.txt
  speed_benchmark.py
  utils.py
  wer_benchmark.py
docker/  (2 files)
  Dockerfile
  infer.py
faster_whisper/  (9 files)
  assets/  (1 files)
    __init__.py
  __init__.py
  audio.py
  feature_extractor.py
  tokenizer.py
  transcribe.py
  utils.py
  vad.py
  version.py
tests/  (4 files)
  conftest.py
  test_tokenizer.py
  test_transcribe.py
  test_utils.py
.gitignore
CONTRIBUTING.md
LICENSE
MANIFEST.in
README.md
requirements.conversion.txt
requirements.txt
setup.cfg
setup.py
```

## Entry points

- [benchmark/memory_benchmark.py:93](https://github.com/SYSTRAN/faster-whisper/blob/6cb639e70786aea42b9233006ae60eaf07190bdb/benchmark/memory_benchmark.py#L93)
- [benchmark/speed_benchmark.py:30](https://github.com/SYSTRAN/faster-whisper/blob/6cb639e70786aea42b9233006ae60eaf07190bdb/benchmark/speed_benchmark.py#L30)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| benchmark package | library | Observed | Groups 3 file(s) under benchmark package (observed from repository paths and static analysis). Observed top-level classes: MyThread. Observed top-level functions: get_logger, inference, url_to_audio. |
| Configuration and deployment | config | Observed | Groups 8 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: get_long_description, get_project_version, get_requirements. |
| docker package | library | Observed | Groups 1 file(s) under docker package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: measure_memory, measure_speed. |
| faster_whisper package | library | Observed | Groups 9 file(s) under faster_whisper package (observed from repository paths and static analysis). Observed top-level classes: BatchedInferencePipeline, FeatureExtractor, Segment, SileroVADModel, SpeechTimestampsMap, T… |
| Tests | test | Observed | Groups 4 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: data_dir, jfk_path, physcisworks_path, test_available_models, test_batched_transcribe, test_cliptimestamps… |

## Important files

- `.github/workflows/ci.yml` (ci)
- `MANIFEST.in` (manifest)
- `benchmark/normalizer.json` (config)
- `benchmark/requirements.benchmark.txt` (manifest)
- `docker/Dockerfile` (container)
- `requirements.conversion.txt` (manifest)
- `requirements.txt` (manifest)
- `setup.cfg` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `(root files)` — 9 analysed file(s)
- `faster_whisper` — 9 analysed file(s)
- `benchmark` — 7 analysed file(s)
- `tests` — 4 analysed file(s)
- `docker` — 2 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `6cb639e70786aea42b9233006ae60eaf07190bdb` is the revision these paths and observations refer to.
