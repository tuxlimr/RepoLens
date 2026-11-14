# Project structure: deezer/spleeter

**Analysed commit:** `6f2c8a2e283914faa544631430f65b793f1b1218`

**Commit reference:** [6f2c8a2e283914faa544631430f65b793f1b1218](https://github.com/deezer/spleeter/commit/6f2c8a2e283914faa544631430f65b793f1b1218)

**Tree at this commit:** [deezer/spleeter@6f2c8a2e2839](https://github.com/deezer/spleeter/tree/6f2c8a2e283914faa544631430f65b793f1b1218)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | deezer/spleeter |
| Description | Deezer source separation library including pretrained models. |
| Stars | 28532 |
| Forks | 3048 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `6f2c8a2e283914faa544631430f65b793f1b1218` |
| Retrieved at | 2026-11-14T19:07:16.567607+00:00 |
| Files in this snapshot | 72 |

## Directory tree

```text
.github/  (11 files)
  ISSUE_TEMPLATE/  (4 files)
    bug.md
    config.yml
    discussion.md
    feature.md
  workflows/  (4 files)
    conda.yml
    docker.yml
    pypi.yml
    test.yml
  CODEOWNERS
  CONTRIBUTING.md
  PULL_REQUEST_TEMPLATE.md
conda/  (1 files)
  spleeter/  (1 files)
    meta.yaml
configs/  (6 files)
  2stems/  (1 files)
    base_config.json
  4stems/  (1 files)
    base_config.json
  5stems/  (1 files)
    base_config.json
  musdb_config.json
  musdb_train.csv
  musdb_validation.csv
docker/  (8 files)
  conda-entrypoint.sh
  conda.dockerfile
  cuda-10-0.dockerfile
  cuda-10-1.dockerfile
  cuda-9.2.dockerfile
  spleeter-conda.dockerfile
  spleeter-model.dockerfile
  spleeter.dockerfile
spleeter/  (30 files)
  audio/  (5 files)
    __init__.py
    adapter.py
    convertor.py
    ffmpeg.py
    spectrogram.py
  model/  (6 files)
    functions/  (3 files)
      … 3 files under this directory
    provider/  (2 files)
      … 2 files under this directory
    __init__.py
  resources/  (8 files)
    2stems-16kHz.json
    2stems.json
    4stems-16kHz.json
    4stems.json
    5stems-16kHz.json
    5stems.json
    __init__.py
    musdb.json
  utils/  (4 files)
    __init__.py
    configuration.py
    logging.py
    tensor.py
  __init__.py
  __main__.py
  dataset.py
  options.py
  py.typed
  separator.py
  types.py
tests/  (7 files)
  __init__.py
  test_command.py
  test_eval.py
  test_ffmpeg_adapter.py
  test_github_model_provider.py
  test_separator.py
  test_train.py
.flake8
.gitignore
CHANGELOG.md
LICENSE
README.md
paper.bib
paper.md
pyproject.toml
spleeter.ipynb
```

## Entry points

- [spleeter/__main__.py:272](https://github.com/deezer/spleeter/blob/6f2c8a2e283914faa544631430f65b793f1b1218/spleeter/__main__.py#L272)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 13 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| docker package | library | Observed | Groups 1 file(s) under docker package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: _compile_metrics, default, entrypoint, evaluate, separate, train. |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| spleeter package | library | Observed | Groups 21 file(s) under spleeter package (observed from repository paths and static analysis). Observed top-level classes: AudioAdapter, Codec, DatasetBuilder, EstimatorSpecBuilder, FFMPEGProcessAudioAdapter, GithubMode… |
| Tests | test | Observed | Groups 7 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: adapter, audio_data, generate_fake_eval_dataset, generate_fake_training_dataset, test_checksum, test_defau… |

## Important files

- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/conda.yml` (ci)
- `.github/workflows/docker.yml` (ci)
- `.github/workflows/pypi.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `conda/spleeter/meta.yaml` (config)
- `configs/2stems/base_config.json` (config)
- `configs/4stems/base_config.json` (config)
- `configs/5stems/base_config.json` (config)
- `configs/musdb_config.json` (config)
- `pyproject.toml` (manifest)
- `spleeter/resources/2stems-16kHz.json` (config)
- `spleeter/resources/2stems.json` (config)
- `spleeter/resources/4stems-16kHz.json` (config)
- `spleeter/resources/4stems.json` (config)
- `spleeter/resources/5stems-16kHz.json` (config)
- `spleeter/resources/5stems.json` (config)
- `spleeter/resources/musdb.json` (config)

## Top-level layout

- `spleeter` — 30 analysed file(s)
- `.github` — 11 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `docker` — 8 analysed file(s)
- `tests` — 7 analysed file(s)
- `configs` — 6 analysed file(s)
- `conda` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `6f2c8a2e283914faa544631430f65b793f1b1218` is the revision these paths and observations refer to.
