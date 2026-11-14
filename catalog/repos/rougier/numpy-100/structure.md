# Project structure: rougier/numpy-100

**Analysed commit:** `cf3b5a29749410758ccaab876302ed861bb94323`

**Commit reference:** [cf3b5a29749410758ccaab876302ed861bb94323](https://github.com/rougier/numpy-100/commit/cf3b5a29749410758ccaab876302ed861bb94323)

**Tree at this commit:** [rougier/numpy-100@cf3b5a297494](https://github.com/rougier/numpy-100/tree/cf3b5a29749410758ccaab876302ed861bb94323)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | rougier/numpy-100 |
| Description | 100 numpy exercises (with solutions) |
| Stars | 14692 |
| Forks | 6969 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `cf3b5a29749410758ccaab876302ed861bb94323` |
| Retrieved at | 2026-11-14T19:09:19.183565+00:00 |
| Files in this snapshot | 18 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (1 files)
    generate_solutions_files.yml
  FUNDING.yml
source/  (2 files)
  exercises100.ktx
  headers.ktx
.gitattributes
.gitignore
100_Numpy_exercises.ipynb
100_Numpy_exercises.md
100_Numpy_exercises_with_hints.md
100_Numpy_exercises_with_hints_with_solutions.md
100_Numpy_exercises_with_solutions.md
100_Numpy_random.ipynb
LICENSE.txt
README.md
generators.py
initialise.py
requirements.txt
runtime.txt
```

## Entry points

- [generators.py:131](https://github.com/rougier/numpy-100/blob/cf3b5a29749410758ccaab876302ed861bb94323/generators.py#L131)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). Observed top-level functions: answer, hint, pick, question. |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: create_jupyter_notebook, create_jupyter_notebook_random_question, create_markdown, creat… |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/workflows/generate_solutions_files.yml` (ci)
- `requirements.txt` (manifest)

## Top-level layout

- `(root files)` — 14 analysed file(s)
- `.github` — 2 analysed file(s)
- `source` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `cf3b5a29749410758ccaab876302ed861bb94323` is the revision these paths and observations refer to.
