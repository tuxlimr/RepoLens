# Project structure: openai/tiktoken

**Analysed commit:** `79dc2c0533685b893616c78160b5d9e40876e724`

**Commit reference:** [79dc2c0533685b893616c78160b5d9e40876e724](https://github.com/openai/tiktoken/commit/79dc2c0533685b893616c78160b5d9e40876e724)

**Tree at this commit:** [openai/tiktoken@79dc2c053368](https://github.com/openai/tiktoken/tree/79dc2c0533685b893616c78160b5d9e40876e724)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | openai/tiktoken |
| Description | tiktoken is a fast BPE tokeniser for use with OpenAI's models. |
| Stars | 19664 |
| Forks | 1679 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `79dc2c0533685b893616c78160b5d9e40876e724` |
| Retrieved at | 2026-11-14T19:08:09.706007+00:00 |
| Files in this snapshot | 30 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    build_wheels.yml
scripts/  (3 files)
  benchmark.py
  redact.py
  wheel_download.py
src/  (2 files)
  lib.rs
  py.rs
tests/  (7 files)
  __init__.py
  test_encoding.py
  test_helpers.py
  test_misc.py
  test_offsets.py
  test_pickle.py
  test_simple_public.py
tiktoken/  (7 files)
  __init__.py
  _educational.py
  core.py
  load.py
  model.py
  py.typed
  registry.py
tiktoken_ext/  (1 files)
  openai_public.py
.gitignore
CHANGELOG.md
Cargo.toml
LICENSE
MANIFEST.in
README.md
perf.svg
pyproject.toml
setup.py
```

## Entry points

- [scripts/redact.py:66](https://github.com/openai/tiktoken/blob/79dc2c0533685b893616c78160b5d9e40876e724/scripts/redact.py#L66)
- [scripts/wheel_download.py:44](https://github.com/openai/tiktoken/blob/79dc2c0533685b893616c78160b5d9e40876e724/scripts/wheel_download.py#L44)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level functions: encoding_for_model, encoding_name_for_model. |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: download_artifacts, main, redact, redact_file. |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| lib.rs package | library | Observed | Groups 1 file(s) under lib.rs package (observed from repository paths and static analysis). |
| py.rs package | library | Observed | Groups 1 file(s) under py.rs package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). Observed top-level functions: benchmark_batch. |
| Tests | test | Observed | Groups 7 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: _common_prefix_len, _token_offsets_reference, test_basic_encode, test_basic_offsets, test_basic_roundtrip,… |
| tiktoken package | library | Observed | Groups 5 file(s) under tiktoken package (observed from repository paths and static analysis). Observed top-level classes: Encoding, SimpleBytePairEncoding. Observed top-level functions: _available_plugin_modules, _find_… |
| tiktoken_ext package | library | Observed | Groups 1 file(s) under tiktoken_ext package (observed from repository paths and static analysis). Observed top-level functions: cl100k_base, gpt2, o200k_base, o200k_harmony, p50k_base, p50k_edit. |

## Important files

- `.github/workflows/build_wheels.yml` (ci)
- `Cargo.toml` (manifest)
- `MANIFEST.in` (manifest)
- `pyproject.toml` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `(root files)` — 9 analysed file(s)
- `tests` — 7 analysed file(s)
- `tiktoken` — 7 analysed file(s)
- `scripts` — 3 analysed file(s)
- `src` — 2 analysed file(s)
- `.github` — 1 analysed file(s)
- `tiktoken_ext` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `79dc2c0533685b893616c78160b5d9e40876e724` is the revision these paths and observations refer to.
