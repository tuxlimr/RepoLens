# Project structure: karpathy/nanoGPT

**Analysed commit:** `3adf61e154c3fe3fca428ad6bc3818b27a3b8291`

**Commit reference:** [3adf61e154c3fe3fca428ad6bc3818b27a3b8291](https://github.com/karpathy/nanoGPT/commit/3adf61e154c3fe3fca428ad6bc3818b27a3b8291)

**Tree at this commit:** [karpathy/nanoGPT@3adf61e154c3](https://github.com/karpathy/nanoGPT/tree/3adf61e154c3fe3fca428ad6bc3818b27a3b8291)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | karpathy/nanoGPT |
| Description | The simplest, fastest repository for training/finetuning medium-sized GPTs. |
| Stars | 64748 |
| Forks | 11143 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `3adf61e154c3fe3fca428ad6bc3818b27a3b8291` |
| Retrieved at | 2026-11-14T19:06:20.025838+00:00 |
| Files in this snapshot | 23 |

## Directory tree

```text
config/  (7 files)
  eval_gpt2.py
  eval_gpt2_large.py
  eval_gpt2_medium.py
  eval_gpt2_xl.py
  finetune_shakespeare.py
  train_gpt2.py
  train_shakespeare_char.py
data/  (6 files)
  openwebtext/  (2 files)
    prepare.py
    readme.md
  shakespeare/  (2 files)
    prepare.py
    readme.md
  shakespeare_char/  (2 files)
    prepare.py
    readme.md
.gitattributes
.gitignore
LICENSE
README.md
bench.py
configurator.py
model.py
sample.py
train.py
transformer_sizing.ipynb
```

## Entry points

- [data/openwebtext/prepare.py:21](https://github.com/karpathy/nanoGPT/blob/3adf61e154c3fe3fca428ad6bc3818b27a3b8291/data/openwebtext/prepare.py#L21)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). Observed top-level functions: estimate_loss, get_batch, get_lr. |
| Data layer | data | Observed | Groups 3 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: Block, CausalSelfAttention, GPT, GPTConfig, LayerNorm, MLP. Observed top-level functions: decode, encod… |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |

## Important files

No manifest, config, CI, or container files were observed in the analysed set.

## Top-level layout

- `(root files)` — 10 analysed file(s)
- `config` — 7 analysed file(s)
- `data` — 6 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `3adf61e154c3fe3fca428ad6bc3818b27a3b8291` is the revision these paths and observations refer to.
