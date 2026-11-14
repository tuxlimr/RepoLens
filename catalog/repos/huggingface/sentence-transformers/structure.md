# Project structure: huggingface/sentence-transformers

**Analysed commit:** `688fd663e7b242f41f3f62296d08c69937efeb00`

**Commit reference:** [688fd663e7b242f41f3f62296d08c69937efeb00](https://github.com/huggingface/sentence-transformers/commit/688fd663e7b242f41f3f62296d08c69937efeb00)

**Tree at this commit:** [huggingface/sentence-transformers@688fd663e7b2](https://github.com/huggingface/sentence-transformers/tree/688fd663e7b242f41f3f62296d08c69937efeb00)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | huggingface/sentence-transformers |
| Description | State-of-the-Art Embeddings, Retrieval, and Reranking |
| Stars | 19285 |
| Forks | 3022 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `688fd663e7b242f41f3f62296d08c69937efeb00` |
| Retrieved at | 2026-11-14T19:08:14.152887+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.github/  (5 files)
  workflows/  (4 files)
    min-versions.yml
    quality.yml
    sync-skills.yml
    tests.yml
  dependabot.yml
docs/  (111 files)
  _static/  (3 files)
    css/  (1 files)
      … 1 files under this directory
    html/  (1 files)
      … 1 files under this directory
    js/  (1 files)
      … 1 files under this directory
  _templates/  (1 files)
    layout.html
  cross_encoder/  (8 files)
    training/  (1 files)
      … 1 files under this directory
    usage/  (4 files)
      … 4 files under this directory
    loss_overview.md
    pretrained_models.md
    training_overview.md
  img/  (2 files)
    hf-logo.svg
    logo.svg
  multi_vector_encoder/  (8 files)
    training/  (1 files)
      … 1 files under this directory
    usage/  (4 files)
      … 4 files under this directory
    loss_overview.md
    pretrained_models.md
    training_overview.md
  package_reference/  (52 files)
    base/  (7 files)
      … 7 files under this directory
    cross_encoder/  (7 files)
      … 7 files under this directory
    multi_vector_encoder/  (9 files)
      … 9 files under this directory
    sentence_transformer/  (8 files)
      … 8 files under this directory
    sparse_encoder/  (9 files)
      … 9 files under this directory
    util/  (12 files)
      … 12 files under this directory
  pretrained-models/  (10 files)
    ce-msmarco.md
    dpr.md
    msmarco-v1.md
    msmarco-v2.md
    msmarco-v3.md
    msmarco-v5.md
    nli-models.md
    nq-v1.md
    sts-models.md
    wikipedia-sections-models.md
  sentence_transformer/  (12 files)
    training/  (2 files)
      … 2 files under this directory
    usage/  (6 files)
      … 6 files under this directory
    dataset_overview.md
    loss_overview.md
    pretrained_models.md
    training_overview.md
  sparse_encoder/  (7 files)
    training/  (1 files)
      … 1 files under this directory
    usage/  (3 files)
      … 3 files under this directory
    loss_overview.md
    pretrained_models.md
    training_overview.md
  .htaccess
  Makefile
  conf.py
  input_formats.rst
  installation.md
  migration_guide.md
  publications.md
  quickstart.rst
examples/  (254 files)
  cross_encoder/  (36 files)
    applications/  (3 files)
      … 3 files under this directory
    training/  (33 files)
      … 33 files under this directory
  multi_vector_encoder/  (29 files)
    applications/  (3 files)
      … 3 files under this directory
    compression/  (1 files)
      … 1 files under this directory
    evaluation/  (2 files)
      … 2 files under this directory
    interpretability/  (2 files)
      … 2 files under this directory
    training/  (21 files)
      … 21 files under this directory
  sentence_transformer/  (145 files)
    applications/  (38 files)
      … 38 files under this directory
    domain_adaptation/  (1 files)
      … 1 files under this directory
    evaluation/  (4 files)
      … 4 files under this directory
    training/  (76 files)
      … 76 files under this directory
    unsupervised_learning/  (25 files)
      … 25 files under this directory
    README.md
  sparse_encoder/  (44 files)
    applications/  (15 files)
      … 15 files under this directory
    evaluation/  (10 files)
      … 10 files under this directory
    training/  (19 files)
      … 19 files under this directory
sentence_transformers/  (222 files)
  backend/  (5 files)
    __init__.py
    load.py
    optimize.py
    quantize.py
    utils.py
  base/  (25 files)
    evaluation/  (3 files)
      … 3 files under this directory
    losses/  (3 files)
      … 3 files under this directory
    modules/  (7 files)
      … 7 files under this directory
    __init__.py
    data_collator.py
    merging.py
    modality.py
    modality_types.py
    model.py
    model_card.py
    model_card_template.md
    peft_mixin.py
    sampler.py
    trainer.py
    training_args.py
  cross_encoder/  (30 files)
    evaluation/  (6 files)
      … 6 files under this directory
    losses/  (13 files)
      … 13 files under this directory
    modules/  (2 files)
      … 2 files under this directory
    __init__.py
    data_collator.py
    fit_mixin.py
    model.py
    model_card.py
    model_card_template.md
    trainer.py
    training_args.py
    util.py
  multi_vector_encoder/  (28 files)
    evaluation/  (7 files)
      … 7 files under this directory
    losses/  (7 files)
      … 7 files under this directory
    modules/  (3 files)
      … 3 files under this directory
    scoring/  (3 files)
      … 3 files under this directory
    __init__.py
    data_collator.py
    interpretability.py
    model.py
    model_card.py
    model_card_template.md
    trainer.py
    training_args.py
  sentence_transformer/  (79 files)
    datasets/  (6 files)
      … 6 files under this directory
    evaluation/  (12 files)
      … 12 files under this directory
    losses/  (29 files)
      … 29 files under this directory
    modules/  (16 files)
      … 16 files under this directory
    readers/  (7 files)
      … 7 files under this directory
    __init__.py
    data_collator.py
    deprecated_model_card_templates.py
    fit_mixin.py
    model.py
    model_card.py
    model_card_template.md
    trainer.py
    training_args.py
  sparse_encoder/  (38 files)
    callbacks/  (2 files)
      … 2 files under this directory
    evaluation/  (10 files)
      … 10 files under this directory
    losses/  (13 files)
      … 13 files under this directory
    modules/  (5 files)
      … 5 files under this directory
    __init__.py
    data_collator.py
    model.py
    model_card.py
    model_card_template.md
    search_engines.py
    trainer.py
    training_args.py
  util/  (15 files)
    __init__.py
    dataset.py
    decorators.py
    deprecated_import.py
    distributed.py
    environment.py
    file_io.py
    hard_negatives.py
    kernels.py
    logging.py
    misc.py
    quantization.py
    retrieval.py
    similarity.py
    tensor.py
  __init__.py
  py.typed
skills/  (32 files)
  train-sentence-transformers/  (31 files)
    references/  (16 files)
      … 16 files under this directory
    scripts/  (14 files)
      … 14 files under this directory
    SKILL.md
  README.md
tests/  (165 files)
  backend/  (2 files)
    __init__.py
    test_utils.py
  base/  (31 files)
    evaluation/  (1 files)
      … 1 files under this directory
    modules/  (15 files)
      … 15 files under this directory
    samplers/  (4 files)
      … 4 files under this directory
    __init__.py
    test_data_collator.py
    test_distributed_evaluation.py
    test_gradcache_distributed.py
    test_modality.py
    test_model.py
    test_model_card.py
    test_model_type_subclass.py
    test_multi_process.py
    test_trainer.py
    test_training_args.py
  cross_encoder/  (17 files)
    evaluation/  (4 files)
      … 4 files under this directory
    losses/  (3 files)
      … 3 files under this directory
    __init__.py
    conftest.py
    test_backends.py
    test_data_collator.py
    test_model.py
    test_model_card.py
    test_multi_process.py
    test_pretrained.py
    test_train_stsb.py
    test_trainer.py
  multi_vector_encoder/  (21 files)
    evaluation/  (7 files)
      … 7 files under this directory
    losses/  (4 files)
      … 4 files under this directory
    modules/  (2 files)
      … 2 files under this directory
    __init__.py
    test_backends.py
    test_interpretability.py
    test_model.py
    test_model_card.py
    test_multi_process.py
    test_pretrained.py
    test_trainer.py
  sentence_transformer/  (53 files)
    evaluation/  (11 files)
      … 11 files under this directory
    losses/  (23 files)
      … 23 files under this directory
    modules/  (5 files)
      … 5 files under this directory
    __init__.py
    test_backends.py
    test_compute_embeddings.py
    test_custom_models.py
    test_image_embeddings.py
    test_model.py
    test_model_card.py
    test_model_card_data.py
    test_multi_process.py
    test_pretrained.py
    test_pretrained_stsb.py
    test_train_stsb.py
    test_trainer.py
    test_training_args.py
  sparse_encoder/  (28 files)
    evaluation/  (6 files)
      … 6 files under this directory
    losses/  (6 files)
      … 6 files under this directory
    modules/  (4 files)
      … 4 files under this directory
    __init__.py
    test_backends.py
    test_model.py
    test_model_card.py
    test_multi_process.py
    test_opensearch_models.py
    test_pretrained.py
    test_reciprocal_rank_fusion.py
    test_search_engines.py
    test_train_stsb.py
    test_trainer.py
    utils.py
  util/  (9 files)
    __init__.py
    test_backend.py
    test_dataset.py
    test_decorators.py
    test_deprecated_import.py
    test_environment.py
    test_file_io.py
    test_hard_negatives.py
    test_import.py
  __init__.py
  conftest.py
  test_kernels.py
  test_merging.py
.git-blame-ignore-revs
.gitignore
.pre-commit-config.yaml
CONTRIBUTING.md
LICENSE
Makefile
NOTICE.txt
README.md
SECURITY.md
index.rst
pyproject.toml
```

## Entry points

- [skills/train-sentence-transformers/scripts/mine_hard_negatives.py:198](https://github.com/huggingface/sentence-transformers/blob/688fd663e7b242f41f3f62296d08c69937efeb00/skills/train-sentence-transformers/scripts/mine_hard_negatives.py#L198)
- [skills/train-sentence-transformers/scripts/train_cross_encoder_distillation_example.py:253](https://github.com/huggingface/sentence-transformers/blob/688fd663e7b242f41f3f62296d08c69937efeb00/skills/train-sentence-transformers/scripts/train_cross_encoder_distillation_example.py#L253)
- [skills/train-sentence-transformers/scripts/train_cross_encoder_example.py:252](https://github.com/huggingface/sentence-transformers/blob/688fd663e7b242f41f3f62296d08c69937efeb00/skills/train-sentence-transformers/scripts/train_cross_encoder_example.py#L252)
- [skills/train-sentence-transformers/scripts/train_cross_encoder_listwise_example.py:281](https://github.com/huggingface/sentence-transformers/blob/688fd663e7b242f41f3f62296d08c69937efeb00/skills/train-sentence-transformers/scripts/train_cross_encoder_listwise_example.py#L281)
- [skills/train-sentence-transformers/scripts/train_multi_vector_encoder_example.py:239](https://github.com/huggingface/sentence-transformers/blob/688fd663e7b242f41f3f62296d08c69937efeb00/skills/train-sentence-transformers/scripts/train_multi_vector_encoder_example.py#L239)
- [skills/train-sentence-transformers/scripts/train_sentence_transformer_distillation_example.py:302](https://github.com/huggingface/sentence-transformers/blob/688fd663e7b242f41f3f62296d08c69937efeb00/skills/train-sentence-transformers/scripts/train_sentence_transformer_distillation_example.py#L302)
- [skills/train-sentence-transformers/scripts/train_sentence_transformer_example.py:226](https://github.com/huggingface/sentence-transformers/blob/688fd663e7b242f41f3f62296d08c69937efeb00/skills/train-sentence-transformers/scripts/train_sentence_transformer_example.py#L226)
- [skills/train-sentence-transformers/scripts/train_sentence_transformer_make_multilingual_example.py:307](https://github.com/huggingface/sentence-transformers/blob/688fd663e7b242f41f3f62296d08c69937efeb00/skills/train-sentence-transformers/scripts/train_sentence_transformer_make_multilingual_example.py#L307)
- [skills/train-sentence-transformers/scripts/train_sentence_transformer_matryoshka_example.py:211](https://github.com/huggingface/sentence-transformers/blob/688fd663e7b242f41f3f62296d08c69937efeb00/skills/train-sentence-transformers/scripts/train_sentence_transformer_matryoshka_example.py#L211)
- [skills/train-sentence-transformers/scripts/train_sentence_transformer_multi_dataset_example.py:257](https://github.com/huggingface/sentence-transformers/blob/688fd663e7b242f41f3f62296d08c69937efeb00/skills/train-sentence-transformers/scripts/train_sentence_transformer_multi_dataset_example.py#L257)
- [skills/train-sentence-transformers/scripts/train_sentence_transformer_static_embedding_example.py:272](https://github.com/huggingface/sentence-transformers/blob/688fd663e7b242f41f3f62296d08c69937efeb00/skills/train-sentence-transformers/scripts/train_sentence_transformer_static_embedding_example.py#L272)
- [skills/train-sentence-transformers/scripts/train_sentence_transformer_with_lora_example.py:274](https://github.com/huggingface/sentence-transformers/blob/688fd663e7b242f41f3f62296d08c69937efeb00/skills/train-sentence-transformers/scripts/train_sentence_transformer_with_lora_example.py#L274)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 5 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: BaseModel, CrossEncoder, MultiVectorEncoder, SentenceTransformer, SparseEncoder, _Float32Linear. |
| Application entry point | entrypoint | Observed | Groups 14 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: autocast_ctx, build_evaluator, build_parser, load_pair_dataset, load_parallel_data, loa… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| sentence_transformers package | library | Observed | Groups 211 file(s) under sentence_transformers package (observed from repository paths and static analysis). Observed top-level classes: ADRMSELoss, AdaptiveLayerLoss, AnglELoss, AudioDict, BaseDataCollator, BaseEvaluat… |
| Tests | test | Observed | Groups 165 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: BaseModelPreprocessTest, ControlledNegativeScoreModel, CustomNormalize, FakeProcessor, ForwardMethodWrappe… |

## Important files

- `.github/dependabot.yml` (config)
- `.github/workflows/min-versions.yml` (ci)
- `.github/workflows/quality.yml` (ci)
- `.github/workflows/sync-skills.yml` (ci)
- `.github/workflows/tests.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `pyproject.toml` (manifest)

## Top-level layout

- `examples` — 254 analysed file(s)
- `sentence_transformers` — 222 analysed file(s)
- `tests` — 165 analysed file(s)
- `docs` — 111 analysed file(s)
- `skills` — 32 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `.github` — 5 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `688fd663e7b242f41f3f62296d08c69937efeb00` is the revision these paths and observations refer to.
