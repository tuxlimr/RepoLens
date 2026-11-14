# Project structure: eriklindernoren/ML-From-Scratch

**Analysed commit:** `a2806c6732eee8d27762edd6d864e0c179d8e9e8`

**Commit reference:** [a2806c6732eee8d27762edd6d864e0c179d8e9e8](https://github.com/eriklindernoren/ML-From-Scratch/commit/a2806c6732eee8d27762edd6d864e0c179d8e9e8)

**Tree at this commit:** [eriklindernoren/ML-From-Scratch@a2806c6732ee](https://github.com/eriklindernoren/ML-From-Scratch/tree/a2806c6732eee8d27762edd6d864e0c179d8e9e8)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | eriklindernoren/ML-From-Scratch |
| Description | Machine Learning From Scratch. Bare bones NumPy implementations of machine learning models and algorithms with a focus on accessibility. Aims to cover everything from linear regression to deep learning. |
| Stars | 33359 |
| Forks | 5546 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `a2806c6732eee8d27762edd6d864e0c179d8e9e8` |
| Retrieved at | 2026-11-14T19:07:01.164470+00:00 |
| Files in this snapshot | 89 |

## Directory tree

```text
mlfromscratch/  (82 files)
  data/  (1 files)
    TempLinkoping2016.txt
  deep_learning/  (6 files)
    __init__.py
    activation_functions.py
    layers.py
    loss_functions.py
    neural_network.py
    optimizers.py
  examples/  (36 files)
    adaboost.py
    apriori.py
    bayesian_regression.py
    convolutional_neural_network.py
    dbscan.py
    decision_tree_classifier.py
    decision_tree_regressor.py
    deep_q_network.py
    demo.py
    elastic_net.py
    fp_growth.py
    gaussian_mixture_model.py
    genetic_algorithm.py
    gradient_boosting_classifier.py
    gradient_boosting_regressor.py
    k_means.py
    k_nearest_neighbors.py
    lasso_regression.py
    linear_discriminant_analysis.py
    linear_regression.py
    logistic_regression.py
    multi_class_lda.py
    multilayer_perceptron.py
    naive_bayes.py
    … 12 more files
  reinforcement_learning/  (2 files)
    __init__.py
    deep_q_network.py
  supervised_learning/  (18 files)
    __init__.py
    adaboost.py
    bayesian_regression.py
    decision_tree.py
    gradient_boosting.py
    k_nearest_neighbors.py
    linear_discriminant_analysis.py
    logistic_regression.py
    multi_class_lda.py
    multilayer_perceptron.py
    naive_bayes.py
    neuroevolution.py
    particle_swarm_optimization.py
    perceptron.py
    random_forest.py
    regression.py
    support_vector_machine.py
    xgboost.py
  unsupervised_learning/  (13 files)
    __init__.py
    apriori.py
    autoencoder.py
    dbscan.py
    dcgan.py
    fp_growth.py
    gaussian_mixture_model.py
    generative_adversarial_network.py
    genetic_algorithm.py
    k_means.py
    partitioning_around_medoids.py
    principal_component_analysis.py
    restricted_boltzmann_machine.py
  utils/  (5 files)
    __init__.py
    data_manipulation.py
    data_operation.py
    kernels.py
    misc.py
  __init__.py
.gitignore
LICENSE
MANIFEST.in
README.md
requirements.txt
setup.cfg
setup.py
```

## Entry points

- [mlfromscratch/supervised_learning/adaboost.py:145](https://github.com/eriklindernoren/ML-From-Scratch/blob/a2806c6732eee8d27762edd6d864e0c179d8e9e8/mlfromscratch/supervised_learning/adaboost.py#L145)
- [mlfromscratch/supervised_learning/multilayer_perceptron.py:117](https://github.com/eriklindernoren/ML-From-Scratch/blob/a2806c6732eee8d27762edd6d864e0c179d8e9e8/mlfromscratch/supervised_learning/multilayer_perceptron.py#L117)
- [mlfromscratch/unsupervised_learning/autoencoder.py:116](https://github.com/eriklindernoren/ML-From-Scratch/blob/a2806c6732eee8d27762edd6d864e0c179d8e9e8/mlfromscratch/unsupervised_learning/autoencoder.py#L116)
- [mlfromscratch/unsupervised_learning/dcgan.py:169](https://github.com/eriklindernoren/ML-From-Scratch/blob/a2806c6732eee8d27762edd6d864e0c179d8e9e8/mlfromscratch/unsupervised_learning/dcgan.py#L169)
- [mlfromscratch/unsupervised_learning/generative_adversarial_network.py:164](https://github.com/eriklindernoren/ML-From-Scratch/blob/a2806c6732eee8d27762edd6d864e0c179d8e9e8/mlfromscratch/unsupervised_learning/generative_adversarial_network.py#L164)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 40 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Adaboost, Autoencoder, DCGAN, DecisionStump, GAN, MultilayerPerceptron. Observed top-leve… |
| mlfromscratch package | library | Observed | Groups 41 file(s) under mlfromscratch package (observed from repository paths and static analysis). Observed top-level classes: Activation, Adadelta, Adagrad, Adam, Apriori, AveragePooling2D. Observed top-level function… |

## Important files

- `MANIFEST.in` (manifest)
- `requirements.txt` (manifest)
- `setup.cfg` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `mlfromscratch` — 82 analysed file(s)
- `(root files)` — 7 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `a2806c6732eee8d27762edd6d864e0c179d8e9e8` is the revision these paths and observations refer to.
