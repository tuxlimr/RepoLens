# Project structure: xai-org/grok-1

**Analysed commit:** `7050ed204b8206bb8645c7b7bbef7252f79561b0`

**Commit reference:** [7050ed204b8206bb8645c7b7bbef7252f79561b0](https://github.com/xai-org/grok-1/commit/7050ed204b8206bb8645c7b7bbef7252f79561b0)

**Tree at this commit:** [xai-org/grok-1@7050ed204b82](https://github.com/xai-org/grok-1/tree/7050ed204b8206bb8645c7b7bbef7252f79561b0)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | xai-org/grok-1 |
| Description | Grok open release |
| Stars | 52235 |
| Forks | 8534 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `7050ed204b8206bb8645c7b7bbef7252f79561b0` |
| Retrieved at | 2026-11-14T19:06:30.780498+00:00 |
| Files in this snapshot | 11 |

## Directory tree

```text
checkpoints/  (1 files)
  README.md
.gitignore
CODE_OF_CONDUCT.md
LICENSE.txt
README.md
checkpoint.py
model.py
pyproject.toml
requirements.txt
run.py
runners.py
```

## Entry points

- [run.py:70](https://github.com/xai-org/grok-1/blob/7050ed204b8206bb8645c7b7bbef7252f79561b0/run.py#L70)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). Observed top-level classes: InferenceRunner, ModelRunner, Request, SampleOutput, SampleSettings. Observed top-level functions: co… |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: DecoderLayer, DecoderOutput, DenseBlock, InOutEmbed, KVMemory, LanguageModel. Observed top-level functi… |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: main. |

## Important files

- `pyproject.toml` (manifest)
- `requirements.txt` (manifest)

## Top-level layout

- `(root files)` — 10 analysed file(s)
- `checkpoints` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `7050ed204b8206bb8645c7b7bbef7252f79561b0` is the revision these paths and observations refer to.
