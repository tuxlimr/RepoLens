# Project structure: karpathy/autoresearch

**Analysed commit:** `228791fb499afffb54b46200aca536f79142f117`

**Commit reference:** [228791fb499afffb54b46200aca536f79142f117](https://github.com/karpathy/autoresearch/commit/228791fb499afffb54b46200aca536f79142f117)

**Tree at this commit:** [karpathy/autoresearch@228791fb499a](https://github.com/karpathy/autoresearch/tree/228791fb499afffb54b46200aca536f79142f117)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | karpathy/autoresearch |
| Description | AI agents running research on single-GPU nanochat training automatically |
| Stars | 100043 |
| Forks | 13773 |
| Licence | Not detected |
| Language | Python |
| Default branch | master |
| Analysed commit | `228791fb499afffb54b46200aca536f79142f117` |
| Retrieved at | 2026-11-14T19:06:07.787749+00:00 |
| Files in this snapshot | 8 |

## Directory tree

```text
.gitignore
.python-version
README.md
analysis.ipynb
prepare.py
program.md
pyproject.toml
train.py
```

## Entry points

- [prepare.py:371](https://github.com/karpathy/autoresearch/blob/228791fb499afffb54b46200aca536f79142f117/prepare.py#L371)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). Observed top-level classes: Block, CausalSelfAttention, GPT, GPTConfig, MLP, MuonAdamW. Observed top-level functions: adamw_step_… |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Tokenizer. Observed top-level functions: _document_batches, download_data, download_single… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |

## Important files

- `pyproject.toml` (manifest)

## Top-level layout

- `(root files)` — 8 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `228791fb499afffb54b46200aca536f79142f117` is the revision these paths and observations refer to.
