# Project structure: karpathy/minGPT

**Analysed commit:** `37baab71b9abea1b76ab957409a1cc2fbfba8a26`

**Commit reference:** [37baab71b9abea1b76ab957409a1cc2fbfba8a26](https://github.com/karpathy/minGPT/commit/37baab71b9abea1b76ab957409a1cc2fbfba8a26)

**Tree at this commit:** [karpathy/minGPT@37baab71b9ab](https://github.com/karpathy/minGPT/tree/37baab71b9abea1b76ab957409a1cc2fbfba8a26)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | karpathy/minGPT |
| Description | A minimal PyTorch re-implementation of the OpenAI GPT (Generative Pretrained Transformer) training |
| Stars | 25024 |
| Forks | 3330 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `37baab71b9abea1b76ab957409a1cc2fbfba8a26` |
| Retrieved at | 2026-11-14T19:07:33.951251+00:00 |
| Files in this snapshot | 17 |

## Directory tree

```text
mingpt/  (5 files)
  __init__.py
  bpe.py
  model.py
  trainer.py
  utils.py
projects/  (5 files)
  adder/  (2 files)
    adder.py
    readme.md
  chargpt/  (2 files)
    chargpt.py
    readme.md
  readme.md
tests/  (1 files)
  test_huggingface_import.py
.gitignore
LICENSE
README.md
demo.ipynb
generate.ipynb
setup.py
```

## Entry points

- [mingpt/bpe.py:282](https://github.com/karpathy/minGPT/blob/37baab71b9abea1b76ab957409a1cc2fbfba8a26/mingpt/bpe.py#L282)
- [projects/adder/adder.py:123](https://github.com/karpathy/minGPT/blob/37baab71b9abea1b76ab957409a1cc2fbfba8a26/projects/adder/adder.py#L123)
- [projects/chargpt/chargpt.py:86](https://github.com/karpathy/minGPT/blob/37baab71b9abea1b76ab957409a1cc2fbfba8a26/projects/chargpt/chargpt.py#L86)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: Block, CausalSelfAttention, GPT, NewGELU. |
| Application entry point | entrypoint | Observed | Groups 3 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: AdditionDataset, BPETokenizer, CharDataset, Encoder. Observed top-level functions: bytes_t… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| mingpt package | library | Observed | Groups 3 file(s) under mingpt package (observed from repository paths and static analysis). Observed top-level classes: CfgNode, Trainer. Observed top-level functions: set_seed, setup_logging. |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: TestHuggingFaceImport. |

## Important files

- `setup.py` (manifest)

## Top-level layout

- `(root files)` — 6 analysed file(s)
- `mingpt` — 5 analysed file(s)
- `projects` — 5 analysed file(s)
- `tests` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `37baab71b9abea1b76ab957409a1cc2fbfba8a26` is the revision these paths and observations refer to.
