# Project structure: 2noise/ChatTTS

**Analysed commit:** `77b89ee281cd479f5b1a787ada330dc975ca1f2a`

**Commit reference:** [77b89ee281cd479f5b1a787ada330dc975ca1f2a](https://github.com/2noise/ChatTTS/commit/77b89ee281cd479f5b1a787ada330dc975ca1f2a)

**Tree at this commit:** [2noise/ChatTTS@77b89ee281cd](https://github.com/2noise/ChatTTS/tree/77b89ee281cd479f5b1a787ada330dc975ca1f2a)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | 2noise/ChatTTS |
| Description | A generative speech model for daily dialogue. |
| Stars | 40006 |
| Forks | 4246 |
| Licence | AGPL-3.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `77b89ee281cd479f5b1a787ada330dc975ca1f2a` |
| Retrieved at | 2026-11-14T19:06:43.362411+00:00 |
| Files in this snapshot | 94 |

## Directory tree

```text
.github/  (6 files)
  workflows/  (6 files)
    checksum.yml
    close-issue.yml
    pull-format.yml
    push-format.yml
    unitest.yml
    upload-pypi.yml
ChatTTS/  (36 files)
  config/  (2 files)
    __init__.py
    config.py
  model/  (24 files)
    cuda/  (3 files)
      … 3 files under this directory
    velocity/  (14 files)
      … 14 files under this directory
    __init__.py
    dvae.py
    embed.py
    gpt.py
    processors.py
    speaker.py
    tokenizer.py
  res/  (2 files)
    __init__.py
    sha256_map.json
  utils/  (5 files)
    __init__.py
    dl.py
    gpu.py
    io.py
    log.py
  __init__.py
  core.py
  norm.py
docs/  (6 files)
  cn/  (1 files)
    README.md
  es/  (1 files)
    README.md
  fr/  (1 files)
    README.md
  jp/  (1 files)
    README.md
  kr/  (1 files)
    README.md
  ru/  (1 files)
    README.md
examples/  (19 files)
  api/  (6 files)
    README.md
    client.py
    main.py
    openai_api.py
    postScript.py
    requirements.txt
  cmd/  (2 files)
    run.py
    stream.py
  ipynb/  (2 files)
    colab.ipynb
    example.ipynb
  onnx/  (4 files)
    README.md
    exporter.py
    gpt.py
    modeling_llama.py
  web/  (4 files)
    __init__.py
    ex.py
    funcs.py
    webui.py
  __init__.py
tests/  (4 files)
  #511.py
  #588.py
  #655.py
  testall.sh
tools/  (17 files)
  audio/  (5 files)
    __init__.py
    av.py
    ffmpeg.py
    np.py
    pcm.py
  checksum/  (2 files)
    main.go
    tmpl.go
  llm/  (2 files)
    __init__.py
    llm.py
  logger/  (2 files)
    __init__.py
    log.py
  normalizer/  (3 files)
    __init__.py
    en.py
    zh.py
  seeder/  (2 files)
    __init__.py
    ctx.py
  __init__.py
.gitattributes
.gitignore
LICENSE
README.md
requirements.txt
setup.py
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| ChatTTS package | library | Observed | Groups 33 file(s) under chattts package (observed from repository paths and static analysis). Observed top-level classes: AllocStatus, AsyncEngineArgs, BlockAllocator, BlockSpaceManager, CUDAGraphRunner, CacheConfig. Ob… |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: Backbone, BackboneInitArgs, Config, DVAE, Decoder, Embed. |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 4 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: trim_tags. |
| tools package | library | Observed | Groups 17 file(s) under tools package (observed from repository paths and static analysis). Observed top-level classes: ChatOpenAI, Formatter, TorchSeedContext. Observed top-level functions: _pcm_to_wav_buffer, float_to… |

## Important files

- `.github/workflows/checksum.yml` (ci)
- `.github/workflows/close-issue.yml` (ci)
- `.github/workflows/pull-format.yml` (ci)
- `.github/workflows/push-format.yml` (ci)
- `.github/workflows/unitest.yml` (ci)
- `.github/workflows/upload-pypi.yml` (ci)
- `ChatTTS/res/sha256_map.json` (config)
- `examples/api/requirements.txt` (manifest)
- `requirements.txt` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `ChatTTS` — 36 analysed file(s)
- `examples` — 19 analysed file(s)
- `tools` — 17 analysed file(s)
- `(root files)` — 6 analysed file(s)
- `.github` — 6 analysed file(s)
- `docs` — 6 analysed file(s)
- `tests` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `77b89ee281cd479f5b1a787ada330dc975ca1f2a` is the revision these paths and observations refer to.
