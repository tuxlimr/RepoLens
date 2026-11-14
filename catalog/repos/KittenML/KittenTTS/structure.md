# Project structure: KittenML/KittenTTS

**Analysed commit:** `d13d8c978a8f17d441977d714b75853ae6bd4423`

**Commit reference:** [d13d8c978a8f17d441977d714b75853ae6bd4423](https://github.com/KittenML/KittenTTS/commit/d13d8c978a8f17d441977d714b75853ae6bd4423)

**Tree at this commit:** [KittenML/KittenTTS@d13d8c978a8f](https://github.com/KittenML/KittenTTS/tree/d13d8c978a8f17d441977d714b75853ae6bd4423)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | KittenML/KittenTTS |
| Description | Open-source State-of-the-art TTS model which runs on a CPU 😻  |
| Stars | 16873 |
| Forks | 1063 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `d13d8c978a8f17d441977d714b75853ae6bd4423` |
| Retrieved at | 2026-11-14T19:08:39.628105+00:00 |
| Files in this snapshot | 88 |

## Directory tree

```text
docs/  (11 files)
  README.md
  api.md
  architecture.md
  decoders.md
  docker.md
  kitten-tts-2-tiny.md
  mlx.md
  onnx-models.md
  text-normalization.md
  vllm.md
  voices-and-expression.md
kittenml/  (50 files)
  kittentts2/  (28 files)
    docker/  (2 files)
      … 2 files under this directory
    mlx/  (5 files)
      … 5 files under this directory
    vllm/  (7 files)
      … 7 files under this directory
    __init__.py
    logits.py
    model.py
    prompt.py
    s3gen.py
    speaker.py
    speaker_embedding.py
    student_flow.py
    ternary.py
    text.py
    tl2_emb4.py
    tokens.py
    vocoder.py
    weights.py
  kittentts2_tiny/  (15 files)
    frontend/  (6 files)
      … 6 files under this directory
    networks/  (6 files)
      … 6 files under this directory
    __init__.py
    model.py
    torch_model.py
  kittentts_legacy/  (3 files)
    __init__.py
    model.py
    onnx_model.py
  __init__.py
  get_model.py
  preprocess.py
  repo.py
tests/  (10 files)
  __init__.py
  conftest.py
  test_json_encoding.py
  test_kittentts2_tiny.py
  test_logits.py
  test_mlx.py
  test_small_gpu.py
  test_text_normalization.py
  test_vllm.py
  test_vllm_rocm.py
.gitignore
LICENSE
MANIFEST.in
README.md
example.py
example_advanced.py
example_cloning.py
example_expression.py
example_mlx.py
example_onnx_0.8.py
example_streaming.py
example_tiny.py
gradio_demo.py
pyproject.toml
requirements.txt
requirements_gpu.txt
setup.py
```

## Entry points

- [gradio_demo.py:701](https://github.com/KittenML/KittenTTS/blob/d13d8c978a8f17d441977d714b75853ae6bd4423/gradio_demo.py#L701)
- [kittenml/kittentts2/docker/server.py:116](https://github.com/KittenML/KittenTTS/blob/d13d8c978a8f17d441977d714b75853ae6bd4423/kittenml/kittentts2/docker/server.py#L116)
- [kittenml/kittentts2/s3gen.py:380](https://github.com/KittenML/KittenTTS/blob/d13d8c978a8f17d441977d714b75853ae6bd4423/kittenml/kittentts2/s3gen.py#L380)
- [kittenml/kittentts2_tiny/frontend/tts_norm.py:339](https://github.com/KittenML/KittenTTS/blob/d13d8c978a8f17d441977d714b75853ae6bd4423/kittenml/kittentts2_tiny/frontend/tts_norm.py#L339)
- [kittenml/preprocess.py:1268](https://github.com/KittenML/KittenTTS/blob/d13d8c978a8f17d441977d714b75853ae6bd4423/kittenml/preprocess.py#L1268)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 8 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 4 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: Attention, KVCache, KittenLM, KittenTTS2, KittenTTS2Tiny, KittenTTSOnnx. Observed top-level functions:… |
| Application entry point | entrypoint | Observed | Groups 5 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed routes: GET /health, POST /v1/audio/speech, POST /v1/audio/v… |
| kittenml package | library | Observed | Groups 41 file(s) under kittenml package (observed from repository paths and static analysis). Observed top-level classes: AdaIN1d, AdaINResBlock1, AdaLayerNorm, AdainResBlk1d, AttrDict, BASECFM. Observed top-level func… |
| Tests | test | Observed | Groups 10 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: FakeSession, TextNormalizationTests, Utf8JsonLoadingTests. Observed top-level functions: _amd, _apply, _bfl… |

## Important files

- `MANIFEST.in` (manifest)
- `kittenml/kittentts2/docker/Dockerfile` (container)
- `pyproject.toml` (manifest)
- `requirements.txt` (manifest)
- `requirements_gpu.txt` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `kittenml` — 50 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `docs` — 11 analysed file(s)
- `tests` — 10 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `d13d8c978a8f17d441977d714b75853ae6bd4423` is the revision these paths and observations refer to.
