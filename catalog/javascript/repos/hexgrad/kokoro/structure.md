# Project structure: hexgrad/kokoro

**Analysed commit:** `dfb907a02bba8152ca444717ca5d78747ccb4bec`

**Commit reference:** [dfb907a02bba8152ca444717ca5d78747ccb4bec](https://github.com/hexgrad/kokoro/commit/dfb907a02bba8152ca444717ca5d78747ccb4bec)

**Tree at this commit:** [hexgrad/kokoro@dfb907a02bba](https://github.com/hexgrad/kokoro/tree/dfb907a02bba8152ca444717ca5d78747ccb4bec)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | hexgrad/kokoro |
| Description | https://hf.co/hexgrad/Kokoro-82M |
| Stars | 10117 |
| Forks | 1133 |
| Licence | Apache-2.0 |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `dfb907a02bba8152ca444717ca5d78747ccb4bec` |
| Retrieved at | 2026-11-14T19:12:45.792593+00:00 |
| Files in this snapshot | 51 |

## Directory tree

```text
.github/  (1 files)
  FUNDING.yml
demo/  (7 files)
  README.md
  app.py
  en.txt
  frankenstein5k.md
  gatsby5k.md
  packages.txt
  requirements.txt
examples/  (4 files)
  device_examples.py
  export.py
  make_triton_compatible.py
  phoneme_example.py
kokoro/  (7 files)
  __init__.py
  __main__.py
  custom_stft.py
  istftnet.py
  model.py
  modules.py
  pipeline.py
kokoro.js/  (27 files)
  demo/  (15 files)
    public/  (2 files)
      … 2 files under this directory
    src/  (5 files)
      … 5 files under this directory
    .gitignore
    README.md
    eslint.config.js
    index.html
    package.json
    postcss.config.js
    tailwind.config.js
    vite.config.js
  src/  (4 files)
    kokoro.js
    phonemize.js
    splitter.js
    voices.js
  tests/  (2 files)
    phonemize.test.js
    splitting.test.js
  .gitignore
  .prettierignore
  README.md
  package.json
  rollup.config.js
  tsconfig.json
tests/  (1 files)
  test_custom_stft.py
.gitignore
LICENSE
README.md
pyproject.toml
```

## Entry points

- [demo/app.py:181](https://github.com/hexgrad/kokoro/blob/dfb907a02bba8152ca444717ca5d78747ccb4bec/demo/app.py#L181)
- [kokoro/__main__.py](https://github.com/hexgrad/kokoro/blob/dfb907a02bba8152ca444717ca5d78747ccb4bec/kokoro/__main__.py)
- [kokoro.js/demo/src/App.jsx](https://github.com/hexgrad/kokoro/blob/dfb907a02bba8152ca444717ca5d78747ccb4bec/kokoro.js/demo/src/App.jsx)
- [kokoro.js/demo/src/main.jsx](https://github.com/hexgrad/kokoro/blob/dfb907a02bba8152ca444717ca5d78747ccb4bec/kokoro.js/demo/src/main.jsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: KModel, KModelForONNX. |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: forward_gpu, generate_all, generate_and_save_audio, generate_audio, generate_first, get_… |
| kokoro package | library | Observed | Groups 5 file(s) under kokoro package (observed from repository paths and static analysis). Observed top-level classes: AdaIN1d, AdaINResBlock1, AdaLayerNorm, AdainResBlk1d, CustomAlbert, CustomSTFT. Observed top-level… |
| kokoro.js package | library | Observed | Groups 13 file(s) under kokoro.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 3 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: sample_audio, test_batch_processing, test_different_window_sizes, test_magnitude_phase_consistency, test_s… |

## Important files

- `.github/FUNDING.yml` (config)
- `demo/requirements.txt` (manifest)
- `kokoro.js/demo/package.json` (manifest)
- `kokoro.js/package.json` (manifest)
- `kokoro.js/tsconfig.json` (config)
- `pyproject.toml` (manifest)

## Top-level layout

- `kokoro.js` — 27 analysed file(s)
- `demo` — 7 analysed file(s)
- `kokoro` — 7 analysed file(s)
- `(root files)` — 4 analysed file(s)
- `examples` — 4 analysed file(s)
- `.github` — 1 analysed file(s)
- `tests` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `dfb907a02bba8152ca444717ca5d78747ccb4bec` is the revision these paths and observations refer to.
