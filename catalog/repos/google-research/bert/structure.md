# Project structure: google-research/bert

**Analysed commit:** `eedf5716ce1268e56f0a50264a88cafad334ac61`

**Commit reference:** [eedf5716ce1268e56f0a50264a88cafad334ac61](https://github.com/google-research/bert/commit/eedf5716ce1268e56f0a50264a88cafad334ac61)

**Tree at this commit:** [google-research/bert@eedf5716ce12](https://github.com/google-research/bert/tree/eedf5716ce1268e56f0a50264a88cafad334ac61)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | google-research/bert |
| Description | TensorFlow code and pre-trained models for BERT |
| Stars | 40029 |
| Forks | 9654 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `eedf5716ce1268e56f0a50264a88cafad334ac61` |
| Retrieved at | 2026-11-14T19:06:42.711315+00:00 |
| Files in this snapshot | 21 |

## Directory tree

```text
.gitignore
CONTRIBUTING.md
LICENSE
README.md
__init__.py
create_pretraining_data.py
extract_features.py
modeling.py
modeling_test.py
multilingual.md
optimization.py
optimization_test.py
predicting_movie_reviews_with_bert_on_tf_hub.ipynb
requirements.txt
run_classifier.py
run_classifier_with_tfhub.py
run_pretraining.py
run_squad.py
sample_text.txt
tokenization.py
tokenization_test.py
```

## Entry points

- [create_pretraining_data.py:465](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/create_pretraining_data.py#L465)
- [extract_features.py:413](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/extract_features.py#L413)
- [modeling_test.py:276](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/modeling_test.py#L276)
- [optimization_test.py:47](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/optimization_test.py#L47)
- [run_classifier.py:975](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/run_classifier.py#L975)
- [run_classifier_with_tfhub.py:309](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/run_classifier_with_tfhub.py#L309)
- [run_pretraining.py:489](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/run_pretraining.py#L489)
- [run_squad.py:1279](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/run_squad.py#L1279)
- [tokenization_test.py:136](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/tokenization_test.py#L136)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). Observed top-level classes: AdamWeightDecayOptimizer, BasicTokenizer, BertConfig, BertModel, FullTokenizer, WordpieceTokenizer. O… |
| Application entry point | entrypoint | Observed | Groups 6 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: ColaProcessor, DataProcessor, FeatureWriter, InputExample, InputFeatures, MnliProcessor. O… |
| Tests | test | Observed | Groups 3 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: BertModelTest, OptimizationTest, TokenizationTest. |

## Important files

- `requirements.txt` (manifest)

## Top-level layout

- `(root files)` — 21 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- The GitHub repository was marked archived at selection time.

Commit `eedf5716ce1268e56f0a50264a88cafad334ac61` is the revision these paths and observations refer to.
