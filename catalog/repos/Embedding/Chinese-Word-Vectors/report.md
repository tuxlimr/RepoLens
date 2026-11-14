# Architecture report: Embedding/Chinese-Word-Vectors

> Automated static analysis. **Observed** = directly seen in files/imports/AST; **Inferred** = interpretation from that evidence. Repository code was not executed.

## 1. Repository at a glance

| Item | Value |
| --- | --- |
| Repository | Embedding/Chinese-Word-Vectors |
| Description | 100+ Chinese Word Vectors 上百种预训练中文词向量  |
| Language | Python |
| Stars | 12252 |
| Licence | Apache-2.0 |
| Analysed commit / branch | 3096a475f79f218dde7b413dcc6b507d302b7f46 / master |
| Framework(s) | None detected |
| Files analysed | 7 |
| Components | 1 |

## 2. Architecture in one minute

Embedding/Chinese-Word-Vectors - 100+ Chinese Word Vectors 上百种预训练中文词向量 . This repository was analysed statically from 7 file(s) (2 Python). Detected technologies (observed from imports/manifests): NumPy. Files are grouped into 1 component(s): Application entry point. Observed entry point(s): evaluation/ana_eval_dense.py, evaluation/ana_eval_sparse.py. Findings below distinguish observed facts from inferred interpretation.

## 3. High-level block diagram

```mermaid
flowchart TD
    entrypoint["Application entry point"]
```

## 4. Main components

### Application entry point (`entrypoint`)

- **Kind:** entrypoint
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: guess, load_matrix, load_vocabulary, main, normalize, read_analogy.
- **Paths:** `evaluation/ana_eval_dense.py`, `evaluation/ana_eval_sparse.py`
- **Evidence:** [evaluation/ana_eval_dense.py:10](https://github.com/Embedding/Chinese-Word-Vectors/blob/3096a475f79f218dde7b413dcc6b507d302b7f46/evaluation/ana_eval_dense.py#L10); [evaluation/ana_eval_sparse.py:11](https://github.com/Embedding/Chinese-Word-Vectors/blob/3096a475f79f218dde7b413dcc6b507d302b7f46/evaluation/ana_eval_sparse.py#L11)

## 5. Execution flow

**Observed** entry point(s):

- [evaluation/ana_eval_dense.py:162](https://github.com/Embedding/Chinese-Word-Vectors/blob/3096a475f79f218dde7b413dcc6b507d302b7f46/evaluation/ana_eval_dense.py#L162)
- [evaluation/ana_eval_sparse.py:168](https://github.com/Embedding/Chinese-Word-Vectors/blob/3096a475f79f218dde7b413dcc6b507d302b7f46/evaluation/ana_eval_sparse.py#L168)

Representative flow (derived from observed entry points and the import graph; steps beyond the entry point are **Inferred**):

1. Execution starts at an observed entry point listed above, if present.
2. No internal import relationships between components were observed.

## 6. Project structure

### `(root)`

- `LICENSE` - docs (11357 bytes)
- `README.md` - docs (22132 bytes)
- `README_zh.md` - docs (21513 bytes)

### `evaluation`

- `evaluation/ana_eval_dense.py` - source, Python (6635 bytes)
- `evaluation/ana_eval_sparse.py` - source, Python (6652 bytes)

### `testsets`

- `testsets/CA_translated/ca_translated.txt` - docs (31539 bytes)
- `testsets/README.md` - docs (15147 bytes)

## 7. Key dependencies and integrations

| Name | Category | Status | Confidence | Evidence |
| --- | --- | --- | --- | --- |
| NumPy | library | Observed | 0.95 | [evaluation/ana_eval_dense.py:5](https://github.com/Embedding/Chinese-Word-Vectors/blob/3096a475f79f218dde7b413dcc6b507d302b7f46/evaluation/ana_eval_dense.py#L5); [evaluation/ana_eval_sparse.py:5](https://github.com/Embedding/Chinese-Word-Vectors/blob/3096a475f79f218dde7b413dcc6b507d302b7f46/evaluation/ana_eval_sparse.py#L5) |

## 8. Data and state

No database, cache, queue, or persistent-state usage was observed in the analysed files. State handling, if any, may be in-memory or in files that were not analysed.

## 9. Configuration and deployment clues

No configuration, manifest, CI, or container files were observed.

## 10. Design observations

- An entry/API layer is separated from other code (Inferred from paths and decorators).
- The analysed code appears small or monolithic; few component boundaries were observed.

These observations are interpretations (**Inferred**) of the observed structure, not guarantees about runtime design.

## 11. Limitations and unknowns

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

## 12. Source references

- [evaluation/ana_eval_dense.py:5](https://github.com/Embedding/Chinese-Word-Vectors/blob/3096a475f79f218dde7b413dcc6b507d302b7f46/evaluation/ana_eval_dense.py#L5)
- [evaluation/ana_eval_dense.py:10](https://github.com/Embedding/Chinese-Word-Vectors/blob/3096a475f79f218dde7b413dcc6b507d302b7f46/evaluation/ana_eval_dense.py#L10)
- [evaluation/ana_eval_dense.py:162](https://github.com/Embedding/Chinese-Word-Vectors/blob/3096a475f79f218dde7b413dcc6b507d302b7f46/evaluation/ana_eval_dense.py#L162)
- [evaluation/ana_eval_sparse.py:5](https://github.com/Embedding/Chinese-Word-Vectors/blob/3096a475f79f218dde7b413dcc6b507d302b7f46/evaluation/ana_eval_sparse.py#L5)
- [evaluation/ana_eval_sparse.py:11](https://github.com/Embedding/Chinese-Word-Vectors/blob/3096a475f79f218dde7b413dcc6b507d302b7f46/evaluation/ana_eval_sparse.py#L11)
- [evaluation/ana_eval_sparse.py:168](https://github.com/Embedding/Chinese-Word-Vectors/blob/3096a475f79f218dde7b413dcc6b507d302b7f46/evaluation/ana_eval_sparse.py#L168)
