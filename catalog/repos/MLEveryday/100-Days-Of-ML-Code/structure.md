# Project structure: MLEveryday/100-Days-Of-ML-Code

**Analysed commit:** `a6474a20a1cd8bb3fa3c7fab12ffadf70858810c`

**Commit reference:** [a6474a20a1cd8bb3fa3c7fab12ffadf70858810c](https://github.com/MLEveryday/100-Days-Of-ML-Code/commit/a6474a20a1cd8bb3fa3c7fab12ffadf70858810c)

**Tree at this commit:** [MLEveryday/100-Days-Of-ML-Code@a6474a20a1cd](https://github.com/MLEveryday/100-Days-Of-ML-Code/tree/a6474a20a1cd8bb3fa3c7fab12ffadf70858810c)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | MLEveryday/100-Days-Of-ML-Code |
| Description | 100-Days-Of-ML-Code中文版 |
| Stars | 22233 |
| Forks | 5449 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `a6474a20a1cd8bb3fa3c7fab12ffadf70858810c` |
| Retrieved at | 2026-11-14T19:07:55.327610+00:00 |
| Files in this snapshot | 187 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    course-checks.yml
Code/  (64 files)
  my/  (2 files)
    Data_age_salary.csv
    LinerTest.py
  Day 11_K-NN.ipynb
  Day 11_K-NN.md
  Day 11_k-NN.py
  Day 13_SVM.ipynb
  Day 13_SVM.md
  Day 13_SVM.py
  Day 14_SVM_Margin.ipynb
  Day 14_SVM_Margin.md
  Day 14_SVM_Margin.py
  Day 15_Naive_Bayes.ipynb
  Day 15_Naive_Bayes.md
  Day 15_Naive_Bayes.py
  Day 16_Kernel_SVM.ipynb
  Day 16_Kernel_SVM.md
  Day 16_Kernel_SVM.py
  Day 18_Numpy_Neural_Network.ipynb
  Day 18_Numpy_Neural_Network.md
  Day 18_Numpy_Neural_Network.py
  Day 1_Data_Preprocessing.ipynb
  Day 1_Data_Preprocessing.md
  Day 1_Data_Preprocessing.py
  Day 21_HTML_Data_Collection.ipynb
  Day 21_HTML_Data_Collection.md
  Day 21_HTML_Data_Collection.py
  … 38 more files
Other Docs/  (2 files)
  速查手册/  (1 files)
    README.md
  README.md
datasets/  (5 files)
  50_Startups.csv
  Data.csv
  Social_Network_Ads.csv
  readme.md
  studentscores.csv
docs/  (100 files)
  lessons/  (35 files)
    day-04.md
    day-05.md
    day-07.md
    day-08.md
    day-09.md
    day-10.md
    day-12.md
    day-17.md
    day-19.md
    day-20.md
    day-22.md
    day-23.md
    day-24.md
    day-26.md
    day-27.md
    day-28.md
    day-29.md
    day-30.md
    day-31.md
    day-32.md
    day-33.md
    day-35.md
    day-36.md
    day-37.md
    … 11 more files
  solutions/  (54 files)
    day-01.md
    day-02.md
    day-03.md
    day-04.md
    day-05.md
    day-06.md
    day-07.md
    day-08.md
    day-09.md
    day-10.md
    day-11.md
    day-12.md
    day-13.md
    day-14.md
    day-15.md
    day-16.md
    day-17.md
    day-18.md
    day-19.md
    day-20.md
    day-21.md
    day-22.md
    day-23.md
    day-24.md
    … 30 more files
  course-map.json
  curriculum.md
  day-by-day-review.md
  experiments.md
  learning-paths.md
  modernization.md
  original-roadmap.md
  readings.md
  review-handbook-checks.json
  review-link-checks.json
  setup.md
tests/  (4 files)
  test_course_guidance.py
  test_experiments.py
  test_learning_invariants.py
  test_pet_splits.py
tools/  (4 files)
  check_docs.py
  check_lessons.py
  course_guidance.py
  sync_lessons.py
.gitignore
FAQ.MD
LICENSE
README.md
Translation specification.MD
requirements-deep.txt
requirements.txt
```

## Entry points

- [tools/check_docs.py:63](https://github.com/MLEveryday/100-Days-Of-ML-Code/blob/a6474a20a1cd8bb3fa3c7fab12ffadf70858810c/tools/check_docs.py#L63)
- [tools/check_lessons.py:88](https://github.com/MLEveryday/100-Days-Of-ML-Code/blob/a6474a20a1cd8bb3fa3c7fab12ffadf70858810c/tools/check_lessons.py#L88)
- [tools/sync_lessons.py:60](https://github.com/MLEveryday/100-Days-Of-ML-Code/blob/a6474a20a1cd8bb3fa3c7fab12ffadf70858810c/tools/sync_lessons.py#L60)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Code package | library | Observed | Groups 25 file(s) under code package (observed from repository paths and static analysis). Observed top-level functions: array_dataset, bounded_dataset, build_model, classification_summary, configure, decision_plot. |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 3 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: fixtures, main, render. |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 4 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: CourseGuidance, ExperimentHistory, LearningInvariants, PetSplits. Observed top-level functions: run_lesson. |
| tools package | library | Observed | Groups 1 file(s) under tools package (observed from repository paths and static analysis). Observed top-level functions: link, navigation, theory_outputs. |

## Important files

- `.github/workflows/course-checks.yml` (ci)
- `docs/course-map.json` (config)
- `docs/review-handbook-checks.json` (config)
- `docs/review-link-checks.json` (config)
- `requirements-deep.txt` (manifest)
- `requirements.txt` (manifest)

## Top-level layout

- `docs` — 100 analysed file(s)
- `Code` — 64 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `datasets` — 5 analysed file(s)
- `tests` — 4 analysed file(s)
- `tools` — 4 analysed file(s)
- `Other Docs` — 2 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `a6474a20a1cd8bb3fa3c7fab12ffadf70858810c` is the revision these paths and observations refer to.
