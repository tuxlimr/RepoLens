# Project structure: meta-llama/llama

**Analysed commit:** `689c7f261b9c5514636ecc3c5fefefcbb3e6eed7`

**Commit reference:** [689c7f261b9c5514636ecc3c5fefefcbb3e6eed7](https://github.com/meta-llama/llama/commit/689c7f261b9c5514636ecc3c5fefefcbb3e6eed7)

**Tree at this commit:** [meta-llama/llama@689c7f261b9c](https://github.com/meta-llama/llama/tree/689c7f261b9c5514636ecc3c5fefefcbb3e6eed7)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | meta-llama/llama |
| Description | Inference code for Llama models |
| Stars | 59620 |
| Forks | 9762 |
| Licence | Other |
| Language | Python |
| Default branch | main |
| Analysed commit | `689c7f261b9c5514636ecc3c5fefefcbb3e6eed7` |
| Retrieved at | 2026-11-14T19:06:22.673504+00:00 |
| Files in this snapshot | 18 |

## Directory tree

```text
.github/  (1 files)
  ISSUE_TEMPLATE/  (1 files)
    bug_report.md
llama/  (4 files)
  __init__.py
  generation.py
  model.py
  tokenizer.py
.gitignore
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
MODEL_CARD.md
README.md
UPDATES.md
USE_POLICY.md
download.sh
example_chat_completion.py
example_text_completion.py
requirements.txt
setup.py
```

## Entry points

- [example_chat_completion.py:103](https://github.com/meta-llama/llama/blob/689c7f261b9c5514636ecc3c5fefefcbb3e6eed7/example_chat_completion.py#L103)
- [example_text_completion.py:68](https://github.com/meta-llama/llama/blob/689c7f261b9c5514636ecc3c5fefefcbb3e6eed7/example_text_completion.py#L68)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: get_requirements. |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: Attention, FeedForward, ModelArgs, RMSNorm, Transformer, TransformerBlock. Observed top-level functions… |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: main. |
| llama package | library | Observed | Groups 3 file(s) under llama package (observed from repository paths and static analysis). Observed top-level classes: ChatPrediction, CompletionPrediction, Llama, Message, Tokenizer. Observed top-level functions: sampl… |

## Important files

- `requirements.txt` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `(root files)` — 13 analysed file(s)
- `llama` — 4 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `689c7f261b9c5514636ecc3c5fefefcbb3e6eed7` is the revision these paths and observations refer to.
