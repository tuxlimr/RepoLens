# Project structure: resemble-ai/chatterbox

**Analysed commit:** `ab55923c27757c90cfcc407baa57dc25a7d25217`

**Commit reference:** [ab55923c27757c90cfcc407baa57dc25a7d25217](https://github.com/resemble-ai/chatterbox/commit/ab55923c27757c90cfcc407baa57dc25a7d25217)

**Tree at this commit:** [resemble-ai/chatterbox@ab55923c2775](https://github.com/resemble-ai/chatterbox/tree/ab55923c27757c90cfcc407baa57dc25a7d25217)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | resemble-ai/chatterbox |
| Description | SoTA open-source TTS |
| Stars | 27817 |
| Forks | 3745 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `ab55923c27757c90cfcc407baa57dc25a7d25217` |
| Retrieved at | 2026-11-14T19:07:18.304042+00:00 |
| Files in this snapshot | 64 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    install_check.yml
src/  (50 files)
  chatterbox/  (50 files)
    models/  (45 files)
      … 45 files under this directory
    __init__.py
    mtl_tts.py
    tts.py
    tts_turbo.py
    vc.py
.gitignore
LICENSE
README.md
example_for_mac.py
example_tts.py
example_tts_nano.py
example_tts_turbo.py
example_vc.py
gradio_tts_app.py
gradio_tts_turbo_app.py
gradio_vc_app.py
multilingual_app.py
pyproject.toml
```

## Entry points

- [src/chatterbox/models/s3gen/utils/intmeanflow.py:18](https://github.com/resemble-ai/chatterbox/blob/ab55923c27757c90cfcc407baa57dc25a7d25217/src/chatterbox/models/s3gen/utils/intmeanflow.py#L18)
- [gradio_tts_app.py:89](https://github.com/resemble-ai/chatterbox/blob/ab55923c27757c90cfcc407baa57dc25a7d25217/gradio_tts_app.py#L89)
- [gradio_tts_turbo_app.py:182](https://github.com/resemble-ai/chatterbox/blob/ab55923c27757c90cfcc407baa57dc25a7d25217/gradio_tts_turbo_app.py#L182)
- [gradio_vc_app.py:26](https://github.com/resemble-ai/chatterbox/blob/ab55923c27757c90cfcc407baa57dc25a7d25217/gradio_vc_app.py#L26)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| chatterbox package | library | Observed | Groups 5 file(s) under chatterbox package (observed from repository paths and static analysis). Observed top-level classes: ChatterboxMultilingualTTS, ChatterboxTTS, ChatterboxTurboTTS, ChatterboxVC, Conditionals. Obser… |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 6 file(s) under core modules (observed from repository paths and static analysis). Observed top-level functions: default_audio_for_ui, default_text_for_ui, generate_tts_audio, get_or_load_model, get_supported_lan… |
| Data layer | data | Observed | Groups 44 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AttentionBlock2, AttentionQKV, AttrDict, BASECFM, BaseSubsampling, BasicResBlock. Observed top-level f… |
| Application entry point | entrypoint | Observed | Groups 4 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: generate, get_intmeanflow_time_mixer, load_model, set_seed. |

## Important files

- `.github/workflows/install_check.yml` (ci)
- `pyproject.toml` (manifest)

## Top-level layout

- `src` — 50 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `ab55923c27757c90cfcc407baa57dc25a7d25217` is the revision these paths and observations refer to.
