# Project structure: datalab-to/chandra

**Analysed commit:** `b20d54d94e53b32211c98408620edef63e99a4ec`

**Commit reference:** [b20d54d94e53b32211c98408620edef63e99a4ec](https://github.com/datalab-to/chandra/commit/b20d54d94e53b32211c98408620edef63e99a4ec)

**Tree at this commit:** [datalab-to/chandra@b20d54d94e53](https://github.com/datalab-to/chandra/tree/b20d54d94e53b32211c98408620edef63e99a4ec)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | datalab-to/chandra |
| Description | OCR model that handles complex tables, forms, handwriting with full layout. |
| Stars | 12724 |
| Forks | 1271 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `b20d54d94e53b32211c98408620edef63e99a4ec` |
| Retrieved at | 2026-11-14T19:10:01.801192+00:00 |
| Files in this snapshot | 33 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (2 files)
    integration.yml
    publish.yml
chandra/  (20 files)
  model/  (5 files)
    __init__.py
    hf.py
    schema.py
    util.py
    vllm.py
  scripts/  (9 files)
    templates/  (1 files)
      … 1 files under this directory
    OLMOCR_BENCH.md
    __init__.py
    app.py
    cli.py
    olmocr_bench.py
    run_app.py
    screenshot_app.py
    vllm.py
  __init__.py
  input.py
  output.py
  prompts.py
  settings.py
  util.py
tests/  (2 files)
  integration/  (1 files)
    test_image_inference.py
  conftest.py
.gitignore
.pre-commit-config.yaml
.python-version
FULL_BENCHMARKS.md
LICENSE
MODEL_LICENSE
README.md
pyproject.toml
pytest.ini
```

## Entry points

- [chandra/prompts.py:110](https://github.com/datalab-to/chandra/blob/b20d54d94e53b32211c98408620edef63e99a4ec/chandra/prompts.py#L110)
- [chandra/scripts/cli.py](https://github.com/datalab-to/chandra/blob/b20d54d94e53b32211c98408620edef63e99a4ec/chandra/scripts/cli.py)
- [chandra/scripts/olmocr_bench.py:259](https://github.com/datalab-to/chandra/blob/b20d54d94e53b32211c98408620edef63e99a4ec/chandra/scripts/olmocr_bench.py#L259)
- [chandra/scripts/run_app.py](https://github.com/datalab-to/chandra/blob/b20d54d94e53b32211c98408620edef63e99a4ec/chandra/scripts/run_app.py)
- [chandra/scripts/screenshot_app.py](https://github.com/datalab-to/chandra/blob/b20d54d94e53b32211c98408620edef63e99a4ec/chandra/scripts/screenshot_app.py)
- [chandra/scripts/vllm.py](https://github.com/datalab-to/chandra/blob/b20d54d94e53b32211c98408620edef63e99a4ec/chandra/scripts/vllm.py)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| chandra package | library | Observed | Groups 10 file(s) under chandra package (observed from repository paths and static analysis). Observed top-level classes: BatchInputItem, BatchOutputItem, GenerationResult, InferenceManager, LayoutBlock, Markdownify. Ob… |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: Settings. |
| Application entry point | entrypoint | Observed | Groups 7 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Flask. Observed routes: ROUTE /, ROUTE /process. Observed top-level functions:… |
| Tests | test | Observed | Groups 2 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: simple_text_image, test_inference_image. |

## Important files

- `.github/workflows/integration.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `pyproject.toml` (manifest)
- `pytest.ini` (config)

## Top-level layout

- `chandra` — 20 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `.github` — 2 analysed file(s)
- `tests` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `b20d54d94e53b32211c98408620edef63e99a4ec` is the revision these paths and observations refer to.
