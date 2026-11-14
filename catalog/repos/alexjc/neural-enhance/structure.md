# Project structure: alexjc/neural-enhance

**Analysed commit:** `2fd67de7eddae3e8dc48f8abdc791ddbcc867112`

**Commit reference:** [2fd67de7eddae3e8dc48f8abdc791ddbcc867112](https://github.com/alexjc/neural-enhance/commit/2fd67de7eddae3e8dc48f8abdc791ddbcc867112)

**Tree at this commit:** [alexjc/neural-enhance@2fd67de7edda](https://github.com/alexjc/neural-enhance/tree/2fd67de7eddae3e8dc48f8abdc791ddbcc867112)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | alexjc/neural-enhance |
| Description | Super Resolution for images using deep learning. |
| Stars | 11853 |
| Forks | 1347 |
| Licence | AGPL-3.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `2fd67de7eddae3e8dc48f8abdc791ddbcc867112` |
| Retrieved at | 2026-11-14T19:10:21.644051+00:00 |
| Files in this snapshot | 9 |

## Directory tree

```text
train/  (2 files)
  ne1x-photo-repair.sh
  ne2x-photo-default.sh
.gitignore
LICENSE
README.rst
docker-cpu.df
docker-gpu.df
enhance.py
requirements.txt
```

## Entry points

- [enhance.py:574](https://github.com/alexjc/neural-enhance/blob/2fd67de7eddae3e8dc48f8abdc791ddbcc867112/enhance.py#L574)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: DataLoader, Model, NeuralEnhancer, SubpixelReshuffleLayer, ansi. Observed top-level functi… |
| train package | library | Observed | Groups 2 file(s) under train package (observed from repository paths and static analysis). |

## Important files

- `requirements.txt` (manifest)

## Top-level layout

- `(root files)` — 7 analysed file(s)
- `train` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- The GitHub repository was marked archived at selection time.

Commit `2fd67de7eddae3e8dc48f8abdc791ddbcc867112` is the revision these paths and observations refer to.
