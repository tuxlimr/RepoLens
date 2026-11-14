# Project structure: kyegomez/OpenMythos

**Analysed commit:** `155430a88d2a98322fc4c79b2a067792c3c9579a`

**Commit reference:** [155430a88d2a98322fc4c79b2a067792c3c9579a](https://github.com/kyegomez/OpenMythos/commit/155430a88d2a98322fc4c79b2a067792c3c9579a)

**Tree at this commit:** [kyegomez/OpenMythos@155430a88d2a](https://github.com/kyegomez/OpenMythos/tree/155430a88d2a98322fc4c79b2a067792c3c9579a)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | kyegomez/OpenMythos |
| Description | A theoretical reconstruction of the Claude Mythos architecture, built from first principles using the available research literature. |
| Stars | 14925 |
| Forks | 3267 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `155430a88d2a98322fc4c79b2a067792c3c9579a` |
| Retrieved at | 2026-11-14T19:09:11.089122+00:00 |
| Files in this snapshot | 23 |

## Directory tree

```text
docs/  (2 files)
  datasets.md
  open_mythos.md
examples/  (2 files)
  moda_example.py
  variants_example.py
open_mythos/  (5 files)
  __init__.py
  main.py
  moda.py
  tokenizer.py
  variants.py
tests/  (6 files)
  __init__.py
  bench_vs_transformer.py
  small_benchmark.py
  test_main.py
  test_rope_debug.py
  test_tokenizer.py
training/  (2 files)
  3b_fine_web_edu.py
  requirements.txt
.gitignore
LICENSE
README.md
example.py
pyproject.toml
requirements.txt
```

## Entry points

- [training/3b_fine_web_edu.py:550](https://github.com/kyegomez/OpenMythos/blob/155430a88d2a98322fc4c79b2a067792c3c9579a/training/3b_fine_web_edu.py#L550)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: ACTHalting, Expert, FineWebEduDataset, GQAttention, LTIInjection, LoRAAdapter. Observed to… |
| open_mythos package | library | Observed | Groups 4 file(s) under open_mythos package (observed from repository paths and static analysis). Observed top-level classes: DeepSeekExpert, DeepSeekGate, DeepSeekMoE, MoDAAttention, MoDABlock, MoDAConfig. Observed top-… |
| Tests | test | Observed | Groups 6 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: BaselineTransformer, Metrics, PackedLMDataset, ParamCounts, TestACTHalting, TestAttnTypeSwap. Observed top-l… |

## Important files

- `pyproject.toml` (manifest)
- `requirements.txt` (manifest)
- `training/requirements.txt` (manifest)

## Top-level layout

- `(root files)` — 6 analysed file(s)
- `tests` — 6 analysed file(s)
- `open_mythos` — 5 analysed file(s)
- `docs` — 2 analysed file(s)
- `examples` — 2 analysed file(s)
- `training` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `155430a88d2a98322fc4c79b2a067792c3c9579a` is the revision these paths and observations refer to.
