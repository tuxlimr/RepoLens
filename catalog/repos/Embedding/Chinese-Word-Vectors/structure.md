# Project structure: Embedding/Chinese-Word-Vectors

**Analysed commit:** `3096a475f79f218dde7b413dcc6b507d302b7f46`

**Commit reference:** [3096a475f79f218dde7b413dcc6b507d302b7f46](https://github.com/Embedding/Chinese-Word-Vectors/commit/3096a475f79f218dde7b413dcc6b507d302b7f46)

**Tree at this commit:** [Embedding/Chinese-Word-Vectors@3096a475f79f](https://github.com/Embedding/Chinese-Word-Vectors/tree/3096a475f79f218dde7b413dcc6b507d302b7f46)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Embedding/Chinese-Word-Vectors |
| Description | 100+ Chinese Word Vectors 上百种预训练中文词向量  |
| Stars | 12252 |
| Forks | 2320 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `3096a475f79f218dde7b413dcc6b507d302b7f46` |
| Retrieved at | 2026-11-14T19:10:12.378493+00:00 |
| Files in this snapshot | 7 |

## Directory tree

```text
evaluation/  (2 files)
  ana_eval_dense.py
  ana_eval_sparse.py
testsets/  (2 files)
  CA_translated/  (1 files)
    ca_translated.txt
  README.md
LICENSE
README.md
README_zh.md
```

## Entry points

- [evaluation/ana_eval_dense.py:162](https://github.com/Embedding/Chinese-Word-Vectors/blob/3096a475f79f218dde7b413dcc6b507d302b7f46/evaluation/ana_eval_dense.py#L162)
- [evaluation/ana_eval_sparse.py:168](https://github.com/Embedding/Chinese-Word-Vectors/blob/3096a475f79f218dde7b413dcc6b507d302b7f46/evaluation/ana_eval_sparse.py#L168)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: guess, load_matrix, load_vocabulary, main, normalize, read_analogy. |

## Important files

No manifest, config, CI, or container files were observed in the analysed set.

## Top-level layout

- `(root files)` — 3 analysed file(s)
- `evaluation` — 2 analysed file(s)
- `testsets` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `3096a475f79f218dde7b413dcc6b507d302b7f46` is the revision these paths and observations refer to.
