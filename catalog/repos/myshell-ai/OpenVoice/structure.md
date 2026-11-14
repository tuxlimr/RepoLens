# Project structure: myshell-ai/OpenVoice

**Analysed commit:** `74a1d147b17a8c3092dd5430504bd83ef6c7eb23`

**Commit reference:** [74a1d147b17a8c3092dd5430504bd83ef6c7eb23](https://github.com/myshell-ai/OpenVoice/commit/74a1d147b17a8c3092dd5430504bd83ef6c7eb23)

**Tree at this commit:** [myshell-ai/OpenVoice@74a1d147b17a](https://github.com/myshell-ai/OpenVoice/tree/74a1d147b17a8c3092dd5430504bd83ef6c7eb23)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | myshell-ai/OpenVoice |
| Description | Instant voice cloning by MIT and MyShell. Audio foundation model. |
| Stars | 38245 |
| Forks | 4293 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `74a1d147b17a8c3092dd5430504bd83ef6c7eb23` |
| Retrieved at | 2026-11-14T19:06:46.659339+00:00 |
| Files in this snapshot | 26 |

## Directory tree

```text
docs/  (2 files)
  QA.md
  USAGE.md
openvoice/  (16 files)
  text/  (5 files)
    __init__.py
    cleaners.py
    english.py
    mandarin.py
    symbols.py
  __init__.py
  api.py
  attentions.py
  commons.py
  mel_processing.py
  models.py
  modules.py
  openvoice_app.py
  se_extractor.py
  transforms.py
  utils.py
.gitignore
LICENSE
README.md
demo_part1.ipynb
demo_part2.ipynb
demo_part3.ipynb
requirements.txt
setup.py
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: DurationPredictor, Generator, PosteriorEncoder, ReferenceEncoder, ResidualCouplingBlock, StochasticDura… |
| openvoice package | library | Observed | Groups 15 file(s) under openvoice package (observed from repository paths and static analysis). Observed top-level classes: BaseSpeakerTTS, ConvFlow, ConvReluNorm, DDSConv, Decoder, ElementwiseAffine. Observed top-level… |

## Important files

- `requirements.txt` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `openvoice` — 16 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `docs` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `74a1d147b17a8c3092dd5430504bd83ef6c7eb23` is the revision these paths and observations refer to.
