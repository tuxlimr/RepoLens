# Project structure: ddbourgin/numpy-ml

**Analysed commit:** `b0359af5285fbf9699d64fd5ec059493228af03e`

**Commit reference:** [b0359af5285fbf9699d64fd5ec059493228af03e](https://github.com/ddbourgin/numpy-ml/commit/b0359af5285fbf9699d64fd5ec059493228af03e)

**Tree at this commit:** [ddbourgin/numpy-ml@b0359af5285f](https://github.com/ddbourgin/numpy-ml/tree/b0359af5285fbf9699d64fd5ec059493228af03e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | ddbourgin/numpy-ml |
| Description | Machine learning, in numpy |
| Stars | 16322 |
| Forks | 3730 |
| Licence | GPL-3.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `b0359af5285fbf9699d64fd5ec059493228af03e` |
| Retrieved at | 2026-11-14T19:08:49.653177+00:00 |
| Files in this snapshot | 195 |

## Directory tree

```text
.github/  (2 files)
  ISSUE_TEMPLATE/  (1 files)
    a--bug-performance-issue.md
  PULL_REQUEST_TEMPLATE.md
docs/  (61 files)
  _static/  (1 files)
    css/  (1 files)
      … 1 files under this directory
  Makefile
  README.md
  conf.py
  index.rst
  make.bat
  numpy_ml.bandits.bandits.rst
  numpy_ml.bandits.policies.rst
  numpy_ml.bandits.rst
  numpy_ml.bandits.trainer.rst
  numpy_ml.factorization.factors.rst
  numpy_ml.factorization.rst
  numpy_ml.gmm.gmm.rst
  numpy_ml.gmm.rst
  numpy_ml.hmm.MultinomialHMM.rst
  numpy_ml.hmm.rst
  numpy_ml.lda.lda.rst
  numpy_ml.lda.rst
  numpy_ml.lda.smoothed_lda.rst
  numpy_ml.linear_models.lm.rst
  numpy_ml.linear_models.rst
  numpy_ml.neural_nets.activations.rst
  numpy_ml.neural_nets.initializers.rst
  numpy_ml.neural_nets.layers.rst
  numpy_ml.neural_nets.losses.rst
  … 36 more files
numpy_ml/  (120 files)
  bandits/  (5 files)
    README.md
    __init__.py
    bandits.py
    policies.py
    trainer.py
  factorization/  (3 files)
    README.md
    __init__.py
    factors.py
  gmm/  (3 files)
    README.md
    __init__.py
    gmm.py
  hmm/  (3 files)
    README.md
    __init__.py
    hmm.py
  lda/  (4 files)
    README.md
    __init__.py
    lda.py
    lda_smoothed.py
  linear_models/  (8 files)
    README.md
    __init__.py
    bayesian_regression.py
    glm.py
    linear_regression.py
    logistic.py
    naive_bayes.py
    ridge.py
  neural_nets/  (34 files)
    activations/  (3 files)
      … 3 files under this directory
    initializers/  (3 files)
      … 3 files under this directory
    layers/  (3 files)
      … 3 files under this directory
    losses/  (3 files)
      … 3 files under this directory
    models/  (5 files)
      … 5 files under this directory
    modules/  (3 files)
      … 3 files under this directory
    optimizers/  (3 files)
      … 3 files under this directory
    schedulers/  (3 files)
      … 3 files under this directory
    utils/  (3 files)
      … 3 files under this directory
    wrappers/  (3 files)
      … 3 files under this directory
    README.md
    __init__.py
  ngram/  (3 files)
    README.md
    __init__.py
    ngram.py
  nonparametric/  (5 files)
    README.md
    __init__.py
    gp.py
    kernel_regression.py
    knn.py
  plots/  (11 files)
    bandit_plots.py
    gmm_plots.py
    hmm_plots.py
    lda_plots.py
    lm_plots.py
    ngram_plots.py
    nn_activations_plots.py
    nn_schedulers_plots.py
    nonparametric_plots.py
    rl_plots.py
    trees_plots.py
  preprocessing/  (5 files)
    README.md
    __init__.py
    dsp.py
    general.py
    nlp.py
  rl_models/  (7 files)
    tiles/  (2 files)
      … 2 files under this directory
    README.md
    __init__.py
    agents.py
    rl_utils.py
    trainer.py
  tests/  (12 files)
    __init__.py
    nn_torch_models.py
    test_glm.py
    test_linear_regression.py
    test_naive_bayes.py
    test_ngram.py
    test_nn.py
    test_nn_activations.py
    test_nonparametric.py
    test_preprocessing.py
    test_trees.py
    test_utils.py
  trees/  (6 files)
    README.md
    __init__.py
    dt.py
    gbdt.py
    losses.py
    rf.py
  utils/  (9 files)
    README.md
    __init__.py
    data_structures.py
    distance_metrics.py
    graphs.py
    kernels.py
    misc.py
    testing.py
    windows.py
  README.md
  __init__.py
.gitignore
.readthedocs.yml
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
MANIFEST.in
README.md
requirements-dev.txt
requirements-test.txt
requirements.txt
setup.py
tox.ini
```

## Entry points

- [numpy_ml/plots/nn_activations_plots.py:63](https://github.com/ddbourgin/numpy-ml/blob/b0359af5285fbf9699d64fd5ec059493228af03e/numpy_ml/plots/nn_activations_plots.py#L63)
- [numpy_ml/plots/nn_schedulers_plots.py:168](https://github.com/ddbourgin/numpy-ml/blob/b0359af5285fbf9699d64fd5ec059493228af03e/numpy_ml/plots/nn_schedulers_plots.py#L168)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 4 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: BernoulliVAE, WGAN_GP, Word2Vec. |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: king_loss_fn, plot_activations, plot_schedulers. |
| numpy_ml package | library | Observed | Groups 78 file(s) under numpy_ml package (observed from repository paths and static analysis). Observed top-level classes: ActivationBase, ActivationInitializer, AdaGrad, Adam, Add, AdditiveNGram. Observed top-level fun… |
| Tests | test | Observed | Groups 12 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: AdditiveGold, MLEGold, TorchAddLayer, TorchBatchNormLayer, TorchBidirectionalLSTM, TorchCausalConv1d. Obser… |

## Important files

- `.readthedocs.yml` (config)
- `MANIFEST.in` (manifest)
- `docs/requirements.txt` (manifest)
- `requirements-dev.txt` (manifest)
- `requirements-test.txt` (manifest)
- `requirements.txt` (manifest)
- `setup.py` (manifest)
- `tox.ini` (config)

## Top-level layout

- `numpy_ml` — 120 analysed file(s)
- `docs` — 61 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `.github` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `b0359af5285fbf9699d64fd5ec059493228af03e` is the revision these paths and observations refer to.
