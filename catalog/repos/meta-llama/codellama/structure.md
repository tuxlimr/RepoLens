# Project structure: meta-llama/codellama

**Analysed commit:** `e81b597e44dbecc2a0dedb9949fdf84adfc22395`

**Commit reference:** [e81b597e44dbecc2a0dedb9949fdf84adfc22395](https://github.com/meta-llama/codellama/commit/e81b597e44dbecc2a0dedb9949fdf84adfc22395)

**Tree at this commit:** [meta-llama/codellama@e81b597e44db](https://github.com/meta-llama/codellama/tree/e81b597e44dbecc2a0dedb9949fdf84adfc22395)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | meta-llama/codellama |
| Description | Inference code for CodeLlama models |
| Stars | 16204 |
| Forks | 1925 |
| Licence | Other |
| Language | Python |
| Default branch | main |
| Analysed commit | `e81b597e44dbecc2a0dedb9949fdf84adfc22395` |
| Retrieved at | 2026-11-14T19:08:55.820522+00:00 |
| Files in this snapshot | 19 |

## Directory tree

```text
.circleci/  (1 files)
  config.yaml
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
USE_POLICY.md
dev-requirements.txt
download.sh
example_completion.py
example_infilling.py
example_instructions.py
requirements.txt
setup.py
```

## Entry points

- [example_completion.py:52](https://github.com/meta-llama/codellama/blob/e81b597e44dbecc2a0dedb9949fdf84adfc22395/example_completion.py#L52)
- [example_infilling.py:78](https://github.com/meta-llama/codellama/blob/e81b597e44dbecc2a0dedb9949fdf84adfc22395/example_infilling.py#L78)
- [example_instructions.py:67](https://github.com/meta-llama/codellama/blob/e81b597e44dbecc2a0dedb9949fdf84adfc22395/example_instructions.py#L67)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: get_requirements. |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: Attention, FeedForward, ModelArgs, RMSNorm, Transformer, TransformerBlock. Observed top-level functions… |
| Application entry point | entrypoint | Observed | Groups 3 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: main. |
| llama package | library | Observed | Groups 3 file(s) under llama package (observed from repository paths and static analysis). Observed top-level classes: ChatPrediction, CompletionPrediction, InfillingPrediction, Llama, Message, Tokenizer. Observed top-l… |

## Important files

- `.circleci/config.yaml` (ci)
- `requirements.txt` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `(root files)` — 14 analysed file(s)
- `llama` — 4 analysed file(s)
- `.circleci` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- The GitHub repository was marked archived at selection time.

Commit `e81b597e44dbecc2a0dedb9949fdf84adfc22395` is the revision these paths and observations refer to.
