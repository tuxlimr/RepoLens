# Project structure: Lightning-AI/litgpt

**Analysed commit:** `5341568a65e918a85cb284fac038de2157eebf3f`

**Commit reference:** [5341568a65e918a85cb284fac038de2157eebf3f](https://github.com/Lightning-AI/litgpt/commit/5341568a65e918a85cb284fac038de2157eebf3f)

**Tree at this commit:** [Lightning-AI/litgpt@5341568a65e9](https://github.com/Lightning-AI/litgpt/tree/5341568a65e918a85cb284fac038de2157eebf3f)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Lightning-AI/litgpt |
| Description | 20+ high-performance LLMs with recipes to pretrain, finetune and deploy at scale. |
| Stars | 13748 |
| Forks | 1548 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `5341568a65e918a85cb284fac038de2157eebf3f` |
| Retrieved at | 2026-11-14T19:09:42.506352+00:00 |
| Files in this snapshot | 237 |

## Directory tree

```text
.devcontainer/  (2 files)
  Dockerfile
  devcontainer.json
.github/  (9 files)
  ISSUE_TEMPLATE/  (3 files)
    ask-a-question.md
    bug-report.yaml
    feature-request.md
  workflows/  (4 files)
    check-links.yml
    cpu-tests.yml
    mkdocs-deploy.yml
    publish-pkg.yml
  CODEOWNERS
  dependabot.yml
.lightning/  (1 files)
  workflows/  (1 files)
    tests.yaml
config_hub/  (47 files)
  finetune/  (43 files)
    falcon-7b/  (2 files)
      … 2 files under this directory
    gemma-2b/  (3 files)
      … 3 files under this directory
    gemma-7b/  (2 files)
      … 2 files under this directory
    gemma2-2b/  (2 files)
      … 2 files under this directory
    gemma2-9b/  (2 files)
      … 2 files under this directory
    llama-2-7b/  (3 files)
      … 3 files under this directory
    llama-3-8b/  (3 files)
      … 3 files under this directory
    llama-3.1-8b/  (3 files)
      … 3 files under this directory
    llama-3.2-1B/  (3 files)
      … 3 files under this directory
    llama-3.2-3B/  (3 files)
      … 3 files under this directory
    mistral-7b/  (2 files)
      … 2 files under this directory
    mistral-7b-v0.2/  (2 files)
      … 2 files under this directory
    phi-2/  (3 files)
      … 3 files under this directory
    phi-3/  (3 files)
      … 3 files under this directory
    stablelm-base-alpha-3b/  (3 files)
      … 3 files under this directory
    tiny-llama/  (3 files)
      … 3 files under this directory
    README.md
  pretrain/  (4 files)
    debug.yaml
    microllama.yaml
    tinyllama.yaml
    tinystories.yaml
extensions/  (23 files)
  thunder/  (13 files)
    strategies/  (3 files)
      … 3 files under this directory
    unsloth/  (7 files)
      … 7 files under this directory
    README.md
    __init__.py
    pretrain.py
  xla/  (10 files)
    finetune/  (2 files)
      … 2 files under this directory
    generate/  (3 files)
      … 3 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    README.md
    __init__
    utils.py
litgpt/  (60 files)
  chat/  (2 files)
    __init__.py
    base.py
  data/  (18 files)
    __init__.py
    alpaca.py
    alpaca_2k.py
    alpaca_gpt4.py
    base.py
    deita.py
    flan.py
    json_data.py
    lima.py
    lit_data.py
    longform.py
    microllama.py
    openwebtext.py
    prepare_slimpajama.py
    prepare_starcoder.py
    text_files.py
    tinyllama.py
    tinystories.py
  deploy/  (2 files)
    __init__.py
    serve.py
  eval/  (1 files)
    evaluate.py
  finetune/  (6 files)
    __init__.py
    adapter.py
    adapter_v2.py
    full.py
    lora.py
    lora_legacy.py
  generate/  (8 files)
    __init__.py
    adapter.py
    adapter_v2.py
    base.py
    full.py
    sequentially.py
    speculative_decoding.py
    tp.py
  scripts/  (7 files)
    __init__.py
    convert_hf_checkpoint.py
    convert_lit_checkpoint.py
    convert_pretrained_checkpoint.py
    download.py
    merge_lora.py
    validate.py
  __init__.py
  __main__.py
  adapter.py
  adapter_v2.py
  api.py
  args.py
  config.py
  constants.py
  lora.py
  model.py
  parser_config.py
  pretrain.py
  prompts.py
  tokenizer.py
  types.py
  utils.py
tests/  (61 files)
  convert/  (4 files)
    __init__.py
    test_hf_checkpoint.py
    test_lit_checkpoint.py
    test_pretrained_checkpoint.py
  data/  (15 files)
    _fixtures/  (4 files)
      … 4 files under this directory
    __init__.py
    test_alpaca.py
    test_base.py
    test_deita.py
    test_json.py
    test_lit_data.py
    test_longform.py
    test_openwebtext.py
    test_textfiles.py
    test_tinyllama.py
    test_tinystories.py
  ext_thunder/  (5 files)
    __init__.py
    test_thunder_distributed.py
    test_thunder_networks.py
    test_thunder_pretrain.py
    test_unsloth_executor.py
  generate/  (6 files)
    __init__.py
    test_adapter.py
    test_main.py
    test_sequentially.py
    test_tp.py
    utils.py
  conftest.py
  test_adapter.py
  test_adapter_v2.py
  test_api.py
  test_args.py
  test_batch.py
  test_chat.py
  test_ci.py
  test_cli.py
  test_config.py
  test_config_hub.py
  test_deepseek_moe.py
  test_distributed.py
  test_evaluate.py
  test_full.py
  test_generate_speculatively.py
  test_lora.py
  test_merge_lora.py
  test_model.py
  test_multihead_latent_attention.py
  test_pretrain.py
  test_prompts.py
  test_readme.py
  test_rope.py
  … 7 more files
tutorials/  (26 files)
  developer-docs/  (3 files)
    README.md
    adding-models.md
    python-api.md
  examples/  (3 files)
    ptl-trainer/  (3 files)
      … 3 files under this directory
  0_to_litgpt.md
  convert_hf_checkpoint.md
  convert_lit_models.md
  deploy.md
  download_model_weights.md
  evaluation.md
  finetune.md
  finetune_adapter.md
  finetune_full.md
  finetune_lora.md
  full_finetune_example.py
  inference.md
  mkdocs.yml
  oom.md
  prepare_dataset.md
  pretrain.md
  pretrain_tinyllama.md
  python-api.md
  quantize.md
  resource-tables.md
.gitignore
.pre-commit-config.yaml
CITATION.cff
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE.md
README.md
pyproject.toml
```

## Entry points

- [extensions/thunder/pretrain.py:517](https://github.com/Lightning-AI/litgpt/blob/5341568a65e918a85cb284fac038de2157eebf3f/extensions/thunder/pretrain.py#L517)
- [extensions/xla/finetune/adapter.py:281](https://github.com/Lightning-AI/litgpt/blob/5341568a65e918a85cb284fac038de2157eebf3f/extensions/xla/finetune/adapter.py#L281)
- [extensions/xla/generate/adapter.py:129](https://github.com/Lightning-AI/litgpt/blob/5341568a65e918a85cb284fac038de2157eebf3f/extensions/xla/generate/adapter.py#L129)
- [extensions/xla/generate/base.py:181](https://github.com/Lightning-AI/litgpt/blob/5341568a65e918a85cb284fac038de2157eebf3f/extensions/xla/generate/base.py#L181)
- [extensions/xla/scripts/prepare_alpaca.py:145](https://github.com/Lightning-AI/litgpt/blob/5341568a65e918a85cb284fac038de2157eebf3f/extensions/xla/scripts/prepare_alpaca.py#L145)
- [litgpt/__main__.py](https://github.com/Lightning-AI/litgpt/blob/5341568a65e918a85cb284fac038de2157eebf3f/litgpt/__main__.py)
- [litgpt/data/prepare_slimpajama.py:62](https://github.com/Lightning-AI/litgpt/blob/5341568a65e918a85cb284fac038de2157eebf3f/litgpt/data/prepare_slimpajama.py#L62)
- [litgpt/data/prepare_starcoder.py:78](https://github.com/Lightning-AI/litgpt/blob/5341568a65e918a85cb284fac038de2157eebf3f/litgpt/data/prepare_starcoder.py#L78)
- [tutorials/full_finetune_example.py:114](https://github.com/Lightning-AI/litgpt/blob/5341568a65e918a85cb284fac038de2157eebf3f/tutorials/full_finetune_example.py#L114)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 49 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: Config. Observed top-level functions: check_indicator_and_length, find_multiple. |
| Data layer | data | Observed | Groups 17 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: Alpaca, Alpaca2k, AlpacaGPT4, Block, CausalSelfAttention, DataModule. Observed top-level functions: _s… |
| Application entry point | entrypoint | Observed | Groups 11 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: LitLLM, SlimPajamaDataRecipe, StarcoderDataRecipe. Observed top-level functions: _check_c… |
| extensions package | library | Observed | Groups 12 file(s) under extensions package (observed from repository paths and static analysis). Observed top-level classes: ThunderDDPStrategy, ThunderFSDPStrategy, ThunderLLaMAMLP, _SyncGradsContextManager, _ThunderDa… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| litgpt package | library | Observed | Groups 39 file(s) under litgpt package (observed from repository paths and static analysis). Observed top-level classes: AdapterV2Linear, Alpaca, BaseLitAPI, Block, CausalSelfAttention, ChatML. Observed top-level functi… |
| Tests | test | Observed | Groups 61 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH litgpt.data.deita.format_dataset, PATCH datasets.load_dataset, PATCH litgpt.data.lit_data.LitData._dataloader, P… |

## Important files

- `.devcontainer/Dockerfile` (container)
- `.devcontainer/devcontainer.json` (config)
- `.github/ISSUE_TEMPLATE/bug-report.yaml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/check-links.yml` (ci)
- `.github/workflows/cpu-tests.yml` (ci)
- `.github/workflows/mkdocs-deploy.yml` (ci)
- `.github/workflows/publish-pkg.yml` (ci)
- `.lightning/workflows/tests.yaml` (config)
- `.pre-commit-config.yaml` (config)
- `config_hub/finetune/falcon-7b/lora.yaml` (config)
- `config_hub/finetune/falcon-7b/qlora.yaml` (config)
- `config_hub/finetune/gemma-2b/full.yaml` (config)
- `config_hub/finetune/gemma-2b/lora.yaml` (config)
- `config_hub/finetune/gemma-2b/qlora.yaml` (config)
- `config_hub/finetune/gemma-7b/lora.yaml` (config)
- `config_hub/finetune/gemma-7b/qlora.yaml` (config)
- `config_hub/finetune/gemma2-2b/lora.yaml` (config)
- `config_hub/finetune/gemma2-2b/qlora.yaml` (config)
- `config_hub/finetune/gemma2-9b/lora.yaml` (config)
- `config_hub/finetune/gemma2-9b/qlora.yaml` (config)
- `config_hub/finetune/llama-2-7b/full.yaml` (config)
- `config_hub/finetune/llama-2-7b/lora.yaml` (config)
- `config_hub/finetune/llama-2-7b/qlora.yaml` (config)
- `config_hub/finetune/llama-3-8b/full.yaml` (config)
- `config_hub/finetune/llama-3-8b/lora.yaml` (config)
- `config_hub/finetune/llama-3-8b/qlora.yaml` (config)
- `config_hub/finetune/llama-3.1-8b/full.yaml` (config)
- `config_hub/finetune/llama-3.1-8b/lora.yaml` (config)
- `config_hub/finetune/llama-3.1-8b/qlora.yaml` (config)
- `config_hub/finetune/llama-3.2-1B/full.yaml` (config)
- `config_hub/finetune/llama-3.2-1B/lora.yaml` (config)
- `config_hub/finetune/llama-3.2-1B/qlora.yaml` (config)
- `config_hub/finetune/llama-3.2-3B/full.yaml` (config)
- `config_hub/finetune/llama-3.2-3B/lora.yaml` (config)
- `config_hub/finetune/llama-3.2-3B/qlora.yaml` (config)
- `config_hub/finetune/mistral-7b-v0.2/lora.yaml` (config)
- `config_hub/finetune/mistral-7b-v0.2/qlora.yaml` (config)
- `config_hub/finetune/mistral-7b/lora.yaml` (config)
- `config_hub/finetune/mistral-7b/qlora.yaml` (config)
- `config_hub/finetune/phi-2/full.yaml` (config)
- `config_hub/finetune/phi-2/lora.yaml` (config)
- `config_hub/finetune/phi-2/qlora.yaml` (config)
- `config_hub/finetune/phi-3/full.yaml` (config)
- `config_hub/finetune/phi-3/lora.yaml` (config)
- `config_hub/finetune/phi-3/qlora.yaml` (config)
- `config_hub/finetune/stablelm-base-alpha-3b/full.yaml` (config)
- `config_hub/finetune/stablelm-base-alpha-3b/lora.yaml` (config)
- `config_hub/finetune/stablelm-base-alpha-3b/qlora.yaml` (config)
- `config_hub/finetune/tiny-llama/full.yaml` (config)
- `config_hub/finetune/tiny-llama/lora.yaml` (config)
- `config_hub/finetune/tiny-llama/qlora.yaml` (config)
- `config_hub/pretrain/debug.yaml` (config)
- `config_hub/pretrain/microllama.yaml` (config)
- `config_hub/pretrain/tinyllama.yaml` (config)
- `config_hub/pretrain/tinystories.yaml` (config)
- `pyproject.toml` (manifest)
- `tutorials/mkdocs.yml` (config)

## Top-level layout

- `tests` — 61 analysed file(s)
- `litgpt` — 60 analysed file(s)
- `config_hub` — 47 analysed file(s)
- `tutorials` — 26 analysed file(s)
- `extensions` — 23 analysed file(s)
- `.github` — 9 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `.devcontainer` — 2 analysed file(s)
- `.lightning` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `5341568a65e918a85cb284fac038de2157eebf3f` is the revision these paths and observations refer to.
