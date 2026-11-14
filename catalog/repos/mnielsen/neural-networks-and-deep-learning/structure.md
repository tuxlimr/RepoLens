# Project structure: mnielsen/neural-networks-and-deep-learning

**Analysed commit:** `72db53d750f571bef8804de4a52224e44dcab3a1`

**Commit reference:** [72db53d750f571bef8804de4a52224e44dcab3a1](https://github.com/mnielsen/neural-networks-and-deep-learning/commit/72db53d750f571bef8804de4a52224e44dcab3a1)

**Tree at this commit:** [mnielsen/neural-networks-and-deep-learning@72db53d750f5](https://github.com/mnielsen/neural-networks-and-deep-learning/tree/72db53d750f571bef8804de4a52224e44dcab3a1)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | mnielsen/neural-networks-and-deep-learning |
| Description | Code samples for my book "Neural Networks and Deep Learning" |
| Stars | 18067 |
| Forks | 7115 |
| Licence | Not detected |
| Language | Python |
| Default branch | master |
| Analysed commit | `72db53d750f571bef8804de4a52224e44dcab3a1` |
| Retrieved at | 2026-11-14T19:08:27.671555+00:00 |
| Files in this snapshot | 43 |

## Directory tree

```text
fig/  (32 files)
  replaced_by_d3/  (5 files)
    README.md
    relu.py
    sigmoid.py
    step.py
    tanh.py
  backprop_magnitude_nabla.py
  false_minima.py
  generate_gradient.py
  initial_gradient.json
  misleading_gradient.py
  misleading_gradient_contours.py
  mnist.py
  more_data.json
  more_data.py
  more_data_svm.json
  multiple_eta.json
  multiple_eta.py
  norms_during_training_2_layers.json
  norms_during_training_3_layers.json
  norms_during_training_4_layers.json
  overfitting.json
  overfitting.py
  overfitting_full.json
  pca_limitations.py
  regularized.json
  regularized_full.json
  serialize_images_to_json.py
  valley.py
  valley2.py
  … 3 more files
src/  (8 files)
  conv.py
  expand_mnist.py
  mnist_average_darkness.py
  mnist_loader.py
  mnist_svm.py
  network.py
  network2.py
  network3.py
.gitignore
README.md
requirements.txt
```

## Entry points

- [fig/mnist.py:233](https://github.com/mnielsen/neural-networks-and-deep-learning/blob/72db53d750f571bef8804de4a52224e44dcab3a1/fig/mnist.py#L233)
- [fig/overfitting.py:161](https://github.com/mnielsen/neural-networks-and-deep-learning/blob/72db53d750f571bef8804de4a52224e44dcab3a1/fig/overfitting.py#L161)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 14 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| conv.py package | library | Observed | Groups 1 file(s) under conv.py package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: get_images, load_data, main, make_plots, plot_10_by_10_images, plot_2_and_1. |
| expand_mnist.py package | library | Observed | Groups 1 file(s) under expand_mnist.py package (observed from repository paths and static analysis). |
| fig package | library | Observed | Groups 16 file(s) under fig package (observed from repository paths and static analysis). Observed top-level functions: make_data_integer. |
| mnist_average_darkness.py package | library | Observed | Groups 1 file(s) under mnist_average_darkness.py package (observed from repository paths and static analysis). |
| mnist_loader.py package | library | Observed | Groups 1 file(s) under mnist_loader.py package (observed from repository paths and static analysis). Observed top-level functions: load_data, load_data_wrapper, vectorized_result. |
| mnist_svm.py package | library | Observed | Groups 1 file(s) under mnist_svm.py package (observed from repository paths and static analysis). |
| network2.py package | library | Observed | Groups 1 file(s) under network2.py package (observed from repository paths and static analysis). |
| network3.py package | library | Observed | Groups 1 file(s) under network3.py package (observed from repository paths and static analysis). |
| network.py package | library | Observed | Groups 1 file(s) under network.py package (observed from repository paths and static analysis). |

## Important files

- `fig/initial_gradient.json` (config)
- `fig/more_data.json` (config)
- `fig/more_data_svm.json` (config)
- `fig/multiple_eta.json` (config)
- `fig/norms_during_training_2_layers.json` (config)
- `fig/norms_during_training_3_layers.json` (config)
- `fig/norms_during_training_4_layers.json` (config)
- `fig/overfitting.json` (config)
- `fig/overfitting_full.json` (config)
- `fig/regularized.json` (config)
- `fig/regularized_full.json` (config)
- `fig/weight_initialization_100.json` (config)
- `fig/weight_initialization_30.json` (config)
- `requirements.txt` (manifest)

## Top-level layout

- `fig` — 32 analysed file(s)
- `src` — 8 analysed file(s)
- `(root files)` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- File fig/generate_gradient.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File fig/more_data.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File fig/multiple_eta.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File fig/weight_initialization.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File src/conv.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File src/mnist_average_darkness.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File src/mnist_svm.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File src/network.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File src/network2.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File src/network3.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `72db53d750f571bef8804de4a52224e44dcab3a1` is the revision these paths and observations refer to.
