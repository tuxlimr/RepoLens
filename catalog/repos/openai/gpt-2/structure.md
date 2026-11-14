# Project structure: openai/gpt-2

**Analysed commit:** `9b63575ef42771a015060c964af2c3da4cf7c8ab`

**Commit reference:** [9b63575ef42771a015060c964af2c3da4cf7c8ab](https://github.com/openai/gpt-2/commit/9b63575ef42771a015060c964af2c3da4cf7c8ab)

**Tree at this commit:** [openai/gpt-2@9b63575ef427](https://github.com/openai/gpt-2/tree/9b63575ef42771a015060c964af2c3da4cf7c8ab)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | openai/gpt-2 |
| Description | Code for the paper "Language Models are Unsupervised Multitask Learners" |
| Stars | 25016 |
| Forks | 5958 |
| Licence | Other |
| Language | Python |
| Default branch | master |
| Analysed commit | `9b63575ef42771a015060c964af2c3da4cf7c8ab` |
| Retrieved at | 2026-11-14T19:07:34.704663+00:00 |
| Files in this snapshot | 17 |

## Directory tree

```text
src/  (5 files)
  encoder.py
  generate_unconditional_samples.py
  interactive_conditional_samples.py
  model.py
  sample.py
.gitattributes
.gitignore
CONTRIBUTORS.md
DEVELOPERS.md
Dockerfile.cpu
Dockerfile.gpu
LICENSE
README.md
domains.txt
download_model.py
model_card.md
requirements.txt
```

## Entry points

- [src/generate_unconditional_samples.py:78](https://github.com/openai/gpt-2/blob/9b63575ef42771a015060c964af2c3da4cf7c8ab/src/generate_unconditional_samples.py#L78)
- [src/interactive_conditional_samples.py:90](https://github.com/openai/gpt-2/blob/9b63575ef42771a015060c964af2c3da4cf7c8ab/src/interactive_conditional_samples.py#L90)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level functions: attention_mask, attn, block, conv1d, default_hparams, expand_tile. |
| encoder.py package | library | Observed | Groups 1 file(s) under encoder.py package (observed from repository paths and static analysis). Observed top-level classes: Encoder. Observed top-level functions: bytes_to_unicode, get_encoder, get_pairs. |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: interact_model, sample_model. |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| sample.py package | library | Observed | Groups 1 file(s) under sample.py package (observed from repository paths and static analysis). Observed top-level functions: sample_sequence, top_k_logits, top_p_logits. |

## Important files

- `Dockerfile.cpu` (container)
- `Dockerfile.gpu` (container)
- `requirements.txt` (manifest)

## Top-level layout

- `(root files)` — 12 analysed file(s)
- `src` — 5 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- The GitHub repository was marked archived at selection time.

Commit `9b63575ef42771a015060c964af2c3da4cf7c8ab` is the revision these paths and observations refer to.
