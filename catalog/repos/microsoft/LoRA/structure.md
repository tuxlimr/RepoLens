# Project structure: microsoft/LoRA

**Analysed commit:** `c4593f060e6a368d7bb5af5273b8e42810cdef90`

**Commit reference:** [c4593f060e6a368d7bb5af5273b8e42810cdef90](https://github.com/microsoft/LoRA/commit/c4593f060e6a368d7bb5af5273b8e42810cdef90)

**Tree at this commit:** [microsoft/LoRA@c4593f060e6a](https://github.com/microsoft/LoRA/tree/c4593f060e6a368d7bb5af5273b8e42810cdef90)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | microsoft/LoRA |
| Description | Code for loralib, an implementation of "LoRA: Low-Rank Adaptation of Large Language Models" |
| Stars | 13923 |
| Forks | 937 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `c4593f060e6a368d7bb5af5273b8e42810cdef90` |
| Retrieved at | 2026-11-14T19:09:39.264095+00:00 |
| Files in this snapshot | 680 |

## Directory tree

```text
examples/  (676 files)
  NLG/  (24 files)
    eval/  (3 files)
      … 3 files under this directory
    src/  (13 files)
      … 13 files under this directory
    vocab/  (1 files)
      … 1 files under this directory
    CODE_OF_CONDUCT.md
    LICENSE
    README.md
    SECURITY.md
    create_datasets.sh
    download_pretrained_checkpoints.sh
    requirement.txt
  NLU/  (652 files)
    docker/  (10 files)
      … 10 files under this directory
    docs/  (102 files)
      … 102 files under this directory
    examples/  (265 files)
      … 265 files under this directory
    model_cards/  (2 files)
      … 2 files under this directory
    notebooks/  (5 files)
      … 5 files under this directory
    scripts/  (18 files)
      … 18 files under this directory
    src/  (204 files)
      … 204 files under this directory
    templates/  (1 files)
      … 1 files under this directory
    tests/  (4 files)
      … 4 files under this directory
    CODE_OF_CONDUCT.md
    CONTRIBUTING.md
    ISSUES.md
    LICENSE
    MANIFEST.in
    Makefile
    README.md
    adapter_houlsby_roberta_large_mnli.sh
    adapter_pfeiffer_roberta_large_mnli.sh
    deberta_v2_xxlarge_cola.sh
    deberta_v2_xxlarge_mnli.sh
    deberta_v2_xxlarge_mrpc.sh
    deberta_v2_xxlarge_qnli.sh
    deberta_v2_xxlarge_qqp.sh
    deberta_v2_xxlarge_rte.sh
    deberta_v2_xxlarge_sst2.sh
    deberta_v2_xxlarge_stsb.sh
    ds_config.json
    environment.yml
    hubconf.py
    mnli.cutoff.sh
    mnli.rdrop.sh
    pyproject.toml
    roberta_base_cola.sh
    … 17 more files
.gitignore
LICENSE.md
README.md
SECURITY.md
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 15 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: DeeBertTests, ExamplesTests, GenerationUtilsTest, PabeeTests, RagRetrieverTest, SummarizationDataProcessing… |

## Important files

- `examples/NLG/vocab/config.json` (config)
- `examples/NLU/MANIFEST.in` (manifest)
- `examples/NLU/docker/transformers-cpu/Dockerfile` (container)
- `examples/NLU/docker/transformers-gpu/Dockerfile` (container)
- `examples/NLU/docker/transformers-pytorch-cpu/Dockerfile` (container)
- `examples/NLU/docker/transformers-pytorch-gpu/Dockerfile` (container)
- `examples/NLU/docker/transformers-pytorch-tpu/Dockerfile` (container)
- `examples/NLU/docker/transformers-pytorch-tpu/dataset.yaml` (config)
- `examples/NLU/docker/transformers-tensorflow-cpu/Dockerfile` (container)
- `examples/NLU/docker/transformers-tensorflow-gpu/Dockerfile` (container)
- `examples/NLU/ds_config.json` (config)
- `examples/NLU/environment.yml` (manifest)
- `examples/NLU/examples/benchmarking/requirements.txt` (manifest)
- `examples/NLU/examples/language-modeling/requirements.txt` (manifest)
- `examples/NLU/examples/legacy/pytorch-lightning/requirements.txt` (manifest)
- `examples/NLU/examples/legacy/seq2seq/requirements.txt` (manifest)
- `examples/NLU/examples/legacy/seq2seq/test_data/fsmt/fsmt_val_data.json` (config)
- `examples/NLU/examples/multiple-choice/requirements.txt` (manifest)
- `examples/NLU/examples/question-answering/requirements.txt` (manifest)
- `examples/NLU/examples/research_projects/adversarial/requirements.txt` (manifest)
- `examples/NLU/examples/research_projects/bert-loses-patience/requirements.txt` (manifest)
- `examples/NLU/examples/research_projects/bertabs/requirements.txt` (manifest)
- `examples/NLU/examples/research_projects/bertology/requirements.txt` (manifest)
- `examples/NLU/examples/research_projects/deebert/requirements.txt` (manifest)
- `examples/NLU/examples/research_projects/distillation/requirements.txt` (manifest)
- `examples/NLU/examples/research_projects/distillation/training_configs/distilbert-base-cased.json` (config)
- `examples/NLU/examples/research_projects/distillation/training_configs/distilbert-base-multilingual-cased.json` (config)
- `examples/NLU/examples/research_projects/distillation/training_configs/distilbert-base-uncased.json` (config)
- `examples/NLU/examples/research_projects/distillation/training_configs/distilgpt2.json` (config)
- `examples/NLU/examples/research_projects/distillation/training_configs/distilroberta-base.json` (config)
- `examples/NLU/examples/research_projects/longform-qa/requirements.txt` (manifest)
- `examples/NLU/examples/research_projects/lxmert/requirements.txt` (manifest)
- `examples/NLU/examples/research_projects/mlm_wwm/requirements.txt` (manifest)
- `examples/NLU/examples/research_projects/movement-pruning/requirements.txt` (manifest)
- `examples/NLU/examples/research_projects/pplm/requirements.txt` (manifest)
- `examples/NLU/examples/research_projects/rag/requirements.txt` (manifest)
- `examples/NLU/examples/research_projects/seq2seq-distillation/requirements.txt` (manifest)
- `examples/NLU/examples/research_projects/wav2vec2/requirements.txt` (manifest)
- `examples/NLU/examples/seq2seq/requirements.txt` (manifest)
- `examples/NLU/examples/test_data/wmt_en_ro/test.json` (config)
- `examples/NLU/examples/test_data/wmt_en_ro/train.json` (config)
- `examples/NLU/examples/test_data/wmt_en_ro/val.json` (config)
- `examples/NLU/examples/text-classification/requirements.txt` (manifest)
- `examples/NLU/examples/text-generation/requirements.txt` (manifest)
- `examples/NLU/examples/token-classification/requirements.txt` (manifest)
- `examples/NLU/pyproject.toml` (manifest)
- `examples/NLU/setup.cfg` (manifest)
- `examples/NLU/setup.py` (manifest)

## Top-level layout

- `examples` — 676 analysed file(s)
- `(root files)` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `c4593f060e6a368d7bb5af5273b8e42810cdef90` is the revision these paths and observations refer to.
