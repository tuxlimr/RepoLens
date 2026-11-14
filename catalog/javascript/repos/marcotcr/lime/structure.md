# Project structure: marcotcr/lime

**Analysed commit:** `fd7eb2e6f760619c29fca0187c07b82157601b32`

**Commit reference:** [fd7eb2e6f760619c29fca0187c07b82157601b32](https://github.com/marcotcr/lime/commit/fd7eb2e6f760619c29fca0187c07b82157601b32)

**Tree at this commit:** [marcotcr/lime@fd7eb2e6f760](https://github.com/marcotcr/lime/tree/fd7eb2e6f760619c29fca0187c07b82157601b32)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | marcotcr/lime |
| Description | Lime: Explaining the predictions of any machine learning classifier |
| Stars | 12170 |
| Forks | 1851 |
| Licence | BSD-2-Clause |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `fd7eb2e6f760619c29fca0187c07b82157601b32` |
| Retrieved at | 2026-11-14T19:12:09.458040+00:00 |
| Files in this snapshot | 49 |

## Directory tree

```text
benchmark/  (3 files)
  __init__.py
  table_perf.py
  text_perf.py
binder/  (1 files)
  environment.yml
doc/  (8 files)
  notebooks/  (4 files)
    data/  (2 files)
      … 2 files under this directory
    Submodular Pick examples.ipynb
    Tutorial - MNIST and RF.ipynb
  blog_post.md
  conf.py
  index.rst
  lime.rst
lime/  (28 files)
  js/  (5 files)
    bar_chart.js
    explanation.js
    main.js
    predict_proba.js
    predicted_value.js
  tests/  (6 files)
    __init__.py
    test_discretize.py
    test_generic_utils.py
    test_lime_tabular.py
    test_lime_text.py
    test_scikit_image.py
  utils/  (2 files)
    __init__.py
    generic_utils.py
  wrappers/  (2 files)
    __init__.py
    scikit_image.py
  __init__.py
  discretize.py
  exceptions.py
  explanation.py
  lime_base.py
  lime_image.py
  lime_tabular.py
  lime_text.py
  package.json
  style.css
  submodular_pick.py
  test_table.html
  webpack.config.js
.gitignore
.travis.yml
CONTRIBUTING.md
LICENSE
MANIFEST.in
README.md
citation.bib
setup.cfg
setup.py
```

## Entry points

- [benchmark/table_perf.py:25](https://github.com/marcotcr/lime/blob/fd7eb2e6f760619c29fca0187c07b82157601b32/benchmark/table_perf.py#L25)
- [benchmark/text_perf.py:22](https://github.com/marcotcr/lime/blob/fd7eb2e6f760619c29fca0187c07b82157601b32/benchmark/text_perf.py#L22)
- [lime/js/main.js](https://github.com/marcotcr/lime/blob/fd7eb2e6f760619c29fca0187c07b82157601b32/lime/js/main.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| benchmark package | library | Observed | Groups 1 file(s) under benchmark package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: interpret_data. |
| lime package | library | Observed | Groups 19 file(s) under lime package (observed from repository paths and static analysis). Observed top-level classes: BaseDiscretizer, BaseWrapper, DecileDiscretizer, DomainMapper, EntropyDiscretizer, Explanation. Obse… |
| Tests | test | Observed | Groups 7 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: TestBaseWrapper, TestDiscretize, TestGenericUtils, TestLimeTabular, TestLimeText, TestSegmentationAlgorithm. |

## Important files

- `.travis.yml` (ci)
- `MANIFEST.in` (manifest)
- `binder/environment.yml` (manifest)
- `doc/notebooks/data/imagenet_class_index.json` (config)
- `lime/package.json` (manifest)
- `setup.cfg` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `lime` — 28 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `doc` — 8 analysed file(s)
- `benchmark` — 3 analysed file(s)
- `binder` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `fd7eb2e6f760619c29fca0187c07b82157601b32` is the revision these paths and observations refer to.
