# Project structure: cleanlab/cleanlab

**Analysed commit:** `750625747de1b26d8530954f51f0530bd0b51d3c`

**Commit reference:** [750625747de1b26d8530954f51f0530bd0b51d3c](https://github.com/cleanlab/cleanlab/commit/750625747de1b26d8530954f51f0530bd0b51d3c)

**Tree at this commit:** [cleanlab/cleanlab@750625747de1](https://github.com/cleanlab/cleanlab/tree/750625747de1b26d8530954f51f0530bd0b51d3c)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | cleanlab/cleanlab |
| Description | Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels. |
| Stars | 11742 |
| Forks | 944 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `750625747de1b26d8530954f51f0530bd0b51d3c` |
| Retrieved at | 2026-11-14T19:10:26.590301+00:00 |
| Files in this snapshot | 304 |

## Directory tree

```text
.github/  (12 files)
  ISSUE_TEMPLATE/  (4 files)
    1-bug-report.md
    2-feature-request.md
    3-help.md
    4-other.md
  workflows/  (6 files)
    bleeding-edge.yml
    ci.yml
    gh-pages.yaml
    links.yml
    manual-testpypi.yml
    release-build-publish.yml
  get_min_dependencies.py
  pull_request_template.md
cleanlab/  (93 files)
  benchmarking/  (2 files)
    __init__.py
    noise_generation.py
  datalab/  (33 files)
    internal/  (31 files)
      … 31 files under this directory
    __init__.py
    datalab.py
  experimental/  (7 files)
    README.md
    __init__.py
    cifar_cnn.py
    coteaching.py
    label_issues_batched.py
    mnist_pytorch.py
    span_classification.py
  internal/  (19 files)
    neighbor/  (4 files)
      … 4 files under this directory
    __init__.py
    constants.py
    label_quality_utils.py
    latent_algebra.py
    multiannotator_utils.py
    multilabel_scorer.py
    multilabel_utils.py
    numerics.py
    object_detection_utils.py
    outlier.py
    regression_utils.py
    segmentation_utils.py
    token_classification_utils.py
    util.py
    validation.py
  models/  (2 files)
    README.md
    __init__.py
  multilabel_classification/  (4 files)
    __init__.py
    dataset.py
    filter.py
    rank.py
  object_detection/  (4 files)
    __init__.py
    filter.py
    rank.py
    summary.py
  regression/  (3 files)
    __init__.py
    learn.py
    rank.py
  segmentation/  (4 files)
    __init__.py
    filter.py
    rank.py
    summary.py
  token_classification/  (4 files)
    __init__.py
    filter.py
    rank.py
    summary.py
  __init__.py
  classification.py
  count.py
  data_valuation.py
  dataset.py
  filter.py
  multiannotator.py
  outlier.py
  rank.py
  typing.py
  version.py
docs/  (123 files)
  source/  (118 files)
    _static/  (2 files)
      … 2 files under this directory
    _templates/  (5 files)
      … 5 files under this directory
    cleanlab/  (84 files)
      … 84 files under this directory
    migrating/  (1 files)
      … 1 files under this directory
    tutorials/  (24 files)
      … 24 files under this directory
    conf.py
    index.rst
  .nojekyll
  Makefile
  README.md
  make.bat
  requirements.txt
tests/  (60 files)
  datalab/  (34 files)
    datalab/  (8 files)
      … 8 files under this directory
    issue_manager/  (16 files)
      … 16 files under this directory
    conftest.py
    test_cleanvision_integration.py
    test_data.py
    test_data_issues.py
    test_factory.py
    test_imagelab_adapter.py
    test_init.py
    test_issue_finder.py
    test_issue_manager.py
    test_report.py
  internal/  (3 files)
    neighbor/  (2 files)
      … 2 files under this directory
    test_numerics.py
  spurious_correlation/  (3 files)
    __init__.py
    test_correlation_visualizer.py
    test_spurious_correlation.py
  conftest.py
  test_classification.py
  test_data_valuation.py
  test_dataset.py
  test_filter_count.py
  test_frameworks.py
  test_latent_algebra.py
  test_model_pytorch_cnn.py
  test_multiannotator.py
  test_multilabel_classification.py
  test_noise_generation.py
  test_object_detection.py
  test_outlier.py
  test_rank.py
  test_regression.py
  test_segmentation.py
  test_span_classification.py
  test_token_classification.py
  test_util.py
  test_validation.py
.coveragerc
.editorconfig
.gitignore
.mypy.ini
.pre-commit-config.yaml
CODE_OF_CONDUCT.md
CONTRIBUTING.md
DEVELOPMENT.md
LICENSE
MANIFEST.in
README.md
pyproject.toml
requirements-dev.txt
requirements-test-core.txt
setup.cfg
setup.py
```

## Entry points

- [.github/get_min_dependencies.py:6](https://github.com/cleanlab/cleanlab/blob/750625747de1b26d8530954f51f0530bd0b51d3c/.github/get_min_dependencies.py#L6)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| cleanlab package | library | Observed | Groups 90 file(s) under cleanlab package (observed from repository paths and static analysis). Observed top-level classes: Aggregator, CNN, ClassImbalanceIssueManager, ClassLabelScorer, ClassificationRepresentation, Cle… |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: egg_info_ex. |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 60 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH cleanvision.utils.viz_manager.VizManager.individual_images, PATCH cleanvision.utils.viz_manager.VizManager.indiv… |

## Important files

- `.editorconfig` (config)
- `.github/workflows/bleeding-edge.yml` (ci)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/gh-pages.yaml` (ci)
- `.github/workflows/links.yml` (ci)
- `.github/workflows/manual-testpypi.yml` (ci)
- `.github/workflows/release-build-publish.yml` (ci)
- `.mypy.ini` (config)
- `.pre-commit-config.yaml` (config)
- `MANIFEST.in` (manifest)
- `docs/requirements.txt` (manifest)
- `pyproject.toml` (manifest)
- `requirements-dev.txt` (manifest)
- `requirements-test-core.txt` (manifest)
- `setup.cfg` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `docs` — 123 analysed file(s)
- `cleanlab` — 93 analysed file(s)
- `tests` — 60 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `.github` — 12 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `750625747de1b26d8530954f51f0530bd0b51d3c` is the revision these paths and observations refer to.
