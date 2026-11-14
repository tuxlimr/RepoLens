# Project structure: sapientinc/HRM

**Analysed commit:** `ac15626f8db096a63c775b84c9dc868776a6feda`

**Commit reference:** [ac15626f8db096a63c775b84c9dc868776a6feda](https://github.com/sapientinc/HRM/commit/ac15626f8db096a63c775b84c9dc868776a6feda)

**Tree at this commit:** [sapientinc/HRM@ac15626f8db0](https://github.com/sapientinc/HRM/tree/ac15626f8db096a63c775b84c9dc868776a6feda)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | sapientinc/HRM |
| Description | Hierarchical Reasoning Model Official Release |
| Stars | 12667 |
| Forks | 1806 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `ac15626f8db096a63c775b84c9dc868776a6feda` |
| Retrieved at | 2026-11-14T19:10:02.299348+00:00 |
| Files in this snapshot | 25 |

## Directory tree

```text
.vscode/  (2 files)
  launch.json
  settings.json
assets/  (1 files)
  npyjs.js
config/  (2 files)
  arch/  (1 files)
    hrm_v1.yaml
  cfg_pretrain.yaml
dataset/  (4 files)
  build_arc_dataset.py
  build_maze_dataset.py
  build_sudoku_dataset.py
  common.py
models/  (5 files)
  hrm/  (1 files)
    hrm_act_v1.py
  common.py
  layers.py
  losses.py
  sparse_embedding.py
utils/  (1 files)
  functions.py
.gitignore
.gitmodules
LICENSE
README.md
arc_eval.ipynb
evaluate.py
pretrain.py
puzzle_dataset.py
puzzle_visualizer.html
requirements.txt
```

## Entry points

- [dataset/build_arc_dataset.py:286](https://github.com/sapientinc/HRM/blob/ac15626f8db096a63c775b84c9dc868776a6feda/dataset/build_arc_dataset.py#L286)
- [dataset/build_maze_dataset.py:136](https://github.com/sapientinc/HRM/blob/ac15626f8db096a63c775b84c9dc868776a6feda/dataset/build_maze_dataset.py#L136)
- [dataset/build_sudoku_dataset.py:163](https://github.com/sapientinc/HRM/blob/ac15626f8db096a63c775b84c9dc868776a6feda/dataset/build_sudoku_dataset.py#L163)
- [evaluate.py:67](https://github.com/sapientinc/HRM/blob/ac15626f8db096a63c775b84c9dc868776a6feda/evaluate.py#L67)
- [pretrain.py:452](https://github.com/sapientinc/HRM/blob/ac15626f8db096a63c775b84c9dc868776a6feda/pretrain.py#L452)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| assets package | library | Observed | Groups 1 file(s) under assets package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). Observed top-level classes: PuzzleDataset, PuzzleDatasetConfig. Observed top-level functions: _sample_batch. |
| Data layer | data | Observed | Groups 5 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: ACTLossHead, Attention, CastedEmbedding, CastedLinear, CastedSparseEmbedding, CastedSparseEmbeddingSign… |
| dataset package | library | Observed | Groups 1 file(s) under dataset package (observed from repository paths and static analysis). Observed top-level classes: PuzzleDatasetMetadata. Observed top-level functions: dihedral_transform, inverse_dihedral_transfor… |
| Application entry point | entrypoint | Observed | Groups 5 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: ARCPuzzle, ArchConfig, DataProcessConfig, EvalConfig, LossConfig, PretrainConfig. Observed… |
| utils package | library | Observed | Groups 1 file(s) under utils package (observed from repository paths and static analysis). Observed top-level functions: get_model_source_path, load_model_class. |

## Important files

- `.vscode/launch.json` (config)
- `.vscode/settings.json` (config)
- `config/arch/hrm_v1.yaml` (config)
- `config/cfg_pretrain.yaml` (config)
- `requirements.txt` (manifest)

## Top-level layout

- `(root files)` — 10 analysed file(s)
- `models` — 5 analysed file(s)
- `dataset` — 4 analysed file(s)
- `.vscode` — 2 analysed file(s)
- `config` — 2 analysed file(s)
- `assets` — 1 analysed file(s)
- `utils` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `ac15626f8db096a63c775b84c9dc868776a6feda` is the revision these paths and observations refer to.
