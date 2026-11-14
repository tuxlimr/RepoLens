# Project structure: nari-labs/dia

**Analysed commit:** `876125e461a03b157ec905b0fe8b57a0f8b9e7a0`

**Commit reference:** [876125e461a03b157ec905b0fe8b57a0f8b9e7a0](https://github.com/nari-labs/dia/commit/876125e461a03b157ec905b0fe8b57a0f8b9e7a0)

**Tree at this commit:** [nari-labs/dia@876125e461a0](https://github.com/nari-labs/dia/tree/876125e461a03b157ec905b0fe8b57a0f8b9e7a0)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | nari-labs/dia |
| Description | A TTS model capable of generating ultra-realistic dialogue in one pass. |
| Stars | 19409 |
| Forks | 1693 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `876125e461a03b157ec905b0fe8b57a0f8b9e7a0` |
| Retrieved at | 2026-11-14T19:08:12.103651+00:00 |
| Files in this snapshot | 24 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    ci.yaml
dia/  (6 files)
  __init__.py
  audio.py
  config.py
  layers.py
  model.py
  state.py
docker/  (2 files)
  Dockerfile.cpu
  Dockerfile.gpu
example/  (7 files)
  benchmark.py
  simple-cpu.py
  simple-mac.py
  simple.py
  simple_batch.py
  voice_clone.py
  voice_clone_batch.py
.gitignore
.python-version
LICENSE
README.md
app.py
cli.py
hf.py
pyproject.toml
```

## Entry points

- [app.py:439](https://github.com/nari-labs/dia/blob/876125e461a03b157ec905b0fe8b57a0f8b9e7a0/app.py#L439)
- [cli.py:143](https://github.com/nari-labs/dia/blob/876125e461a03b157ec905b0fe8b57a0f8b9e7a0/cli.py#L143)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: DecoderConfig, DiaConfig, EncoderConfig. |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: ComputeDtype, Dia. Observed top-level functions: _get_default_device, _sample_next_token. |
| dia package | library | Observed | Groups 4 file(s) under dia package (observed from repository paths and static analysis). Observed top-level classes: CrossAttention, Decoder, DecoderInferenceState, DecoderLayer, DecoderOutput, DenseGeneral. Observed to… |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: main, run_inference, set_seed. |

## Important files

- `.github/workflows/ci.yaml` (ci)
- `docker/Dockerfile.cpu` (container)
- `docker/Dockerfile.gpu` (container)
- `pyproject.toml` (manifest)

## Top-level layout

- `(root files)` — 8 analysed file(s)
- `example` — 7 analysed file(s)
- `dia` — 6 analysed file(s)
- `docker` — 2 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `876125e461a03b157ec905b0fe8b57a0f8b9e7a0` is the revision these paths and observations refer to.
