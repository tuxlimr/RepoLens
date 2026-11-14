# Project structure: meta-llama/llama3

**Analysed commit:** `a0940f9cf7065d45bb6675660f80d305c041a754`

**Commit reference:** [a0940f9cf7065d45bb6675660f80d305c041a754](https://github.com/meta-llama/llama3/commit/a0940f9cf7065d45bb6675660f80d305c041a754)

**Tree at this commit:** [meta-llama/llama3@a0940f9cf706](https://github.com/meta-llama/llama3/tree/a0940f9cf7065d45bb6675660f80d305c041a754)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | meta-llama/llama3 |
| Description | The official Meta Llama 3 GitHub site |
| Stars | 29145 |
| Forks | 3517 |
| Licence | Other |
| Language | Python |
| Default branch | main |
| Analysed commit | `a0940f9cf7065d45bb6675660f80d305c041a754` |
| Retrieved at | 2026-11-14T19:07:14.290131+00:00 |
| Files in this snapshot | 19 |

## Directory tree

```text
.github/  (1 files)
  ISSUE_TEMPLATE/  (1 files)
    bug_report.md
llama/  (5 files)
  __init__.py
  generation.py
  model.py
  test_tokenizer.py
  tokenizer.py
.gitignore
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
MODEL_CARD.md
README.md
USE_POLICY.md
download.sh
eval_details.md
example_chat_completion.py
example_text_completion.py
requirements.txt
setup.py
```

## Entry points

- [example_chat_completion.py:83](https://github.com/meta-llama/llama3/blob/a0940f9cf7065d45bb6675660f80d305c041a754/example_chat_completion.py#L83)
- [example_text_completion.py:63](https://github.com/meta-llama/llama3/blob/a0940f9cf7065d45bb6675660f80d305c041a754/example_text_completion.py#L63)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: get_requirements. |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: Attention, FeedForward, ModelArgs, RMSNorm, Transformer, TransformerBlock. Observed top-level functions… |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: main. |
| llama package | library | Observed | Groups 3 file(s) under llama package (observed from repository paths and static analysis). Observed top-level classes: ChatFormat, ChatPrediction, CompletionPrediction, Llama, Message, Tokenizer. Observed top-level func… |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: TokenizerTests. |

## Important files

- `requirements.txt` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `(root files)` — 13 analysed file(s)
- `llama` — 5 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- The GitHub repository was marked archived at selection time.

Commit `a0940f9cf7065d45bb6675660f80d305c041a754` is the revision these paths and observations refer to.
