# Project structure: lm-sys/FastChat

**Analysed commit:** `587d5cfa1609a43d192cedb8441cac3c17db105d`

**Commit reference:** [587d5cfa1609a43d192cedb8441cac3c17db105d](https://github.com/lm-sys/FastChat/commit/587d5cfa1609a43d192cedb8441cac3c17db105d)

**Tree at this commit:** [lm-sys/FastChat@587d5cfa1609](https://github.com/lm-sys/FastChat/tree/587d5cfa1609a43d192cedb8441cac3c17db105d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | lm-sys/FastChat |
| Description | An open platform for training, serving, and evaluating large language models. Release repo for Vicuna and Chatbot Arena. |
| Stars | 39549 |
| Forks | 4772 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `587d5cfa1609a43d192cedb8441cac3c17db105d` |
| Retrieved at | 2026-11-14T19:06:44.944807+00:00 |
| Files in this snapshot | 209 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (1 files)
    python-package.yml
  PULL_REQUEST_TEMPLATE.md
docker/  (2 files)
  Dockerfile
  docker-compose.yml
docs/  (23 files)
  commands/  (6 files)
    conv_release.md
    data_cleaning.md
    leaderboard.md
    local_cluster.md
    pypi.md
    webserver.md
  arena.md
  awq.md
  dashinfer_integration.md
  dataset_release.md
  exllama_v2.md
  gptq.md
  langchain_integration.md
  lightllm_integration.md
  mlx_integration.md
  model_support.md
  openai_api.md
  server_arch.md
  third_party_ui.md
  training.md
  vicuna_weights_version.md
  vllm_integration.md
  xFasterTransformer.md
fastchat/  (150 files)
  data/  (17 files)
    __init__.py
    clean_sharegpt.py
    convert_alpaca.py
    extract_gpt4_only.py
    extract_single_round.py
    filter_wrong_format.py
    get_stats.py
    hardcoded_questions.py
    inspect_data.py
    merge.py
    optional_clean.py
    optional_replace.py
    prepare_all.py
    pretty_json.py
    sample.py
    split_long_conversation.py
    split_train_test.py
  llm_judge/  (15 files)
    data/  (5 files)
      … 5 files under this directory
    README.md
    clean_judgment.py
    common.py
    compute_agreement.py
    download_mt_bench_pregenerated.py
    gen_api_answer.py
    gen_judgment.py
    gen_model_answer.py
    qa_browser.py
    show_result.py
  model/  (19 files)
    __init__.py
    apply_delta.py
    apply_lora.py
    compression.py
    convert_fp16.py
    llama_condense_monkey_patch.py
    make_delta.py
    model_adapter.py
    model_chatglm.py
    model_cllm.py
    model_codet5p.py
    model_exllama.py
    model_falcon.py
    model_registry.py
    model_xfastertransformer.py
    model_yuan2.py
    monkey_patch_non_inplace.py
    rwkv_model.py
    upload_hub.py
  modules/  (5 files)
    __init__.py
    awq.py
    exllama.py
    gptq.py
    xfastertransformer.py
  protocol/  (2 files)
    api_protocol.py
    openai_api_protocol.py
  serve/  (76 files)
    gateway/  (2 files)
      … 2 files under this directory
    monitor/  (40 files)
      … 40 files under this directory
    vision/  (3 files)
      … 3 files under this directory
    __init__.py
    api_provider.py
    base_model_worker.py
    call_monitor.py
    cli.py
    controller.py
    dashinfer_worker.py
    gradio_block_arena_anony.py
    gradio_block_arena_named.py
    gradio_block_arena_vision.py
    gradio_block_arena_vision_anony.py
    gradio_block_arena_vision_named.py
    gradio_global_state.py
    gradio_web_server.py
    gradio_web_server_multi.py
    huggingface_api.py
    huggingface_api_worker.py
    inference.py
    launch_all_serve.py
    lightllm_worker.py
    mlx_worker.py
    model_worker.py
    multi_model_worker.py
    openai_api_server.py
    … 7 more files
  train/  (12 files)
    llama2_flash_attn_monkey_patch.py
    llama_flash_attn_monkey_patch.py
    llama_xformers_attn_monkey_patch.py
    train.py
    train_baichuan.py
    train_flant5.py
    train_lora.py
    train_lora_t5.py
    train_mem.py
    train_with_template.py
    train_xformers.py
    train_yuan2.py
  __init__.py
  constants.py
  conversation.py
  utils.py
playground/  (9 files)
  benchmark/  (1 files)
    benchmark_api_provider.py
  test_embedding/  (4 files)
    README.md
    test_classification.py
    test_semantic_search.py
    test_sentence_similarity.py
  FastChat_API_GoogleColab.ipynb
  __init__.py
  deepspeed_config_s2.json
  deepspeed_config_s3.json
scripts/  (6 files)
  build-api.sh
  test_readme_train.sh
  train_lora.sh
  train_vicuna_13b.sh
  train_vicuna_7b.sh
  upload_pypi.sh
tests/  (10 files)
  README.md
  killall_python.sh
  launch_openai_api_test_server.py
  load_test.py
  test_cli.py
  test_cli_inputs.txt
  test_image_utils.py
  test_openai_api.py
  test_openai_langchain.py
  test_openai_vision_api.py
.gitignore
.pylintrc
LICENSE
README.md
format.sh
pyproject.toml
theme.json
```

## Entry points

- [fastchat/conversation.py:2302](https://github.com/lm-sys/FastChat/blob/587d5cfa1609a43d192cedb8441cac3c17db105d/fastchat/conversation.py#L2302)
- [fastchat/data/clean_sharegpt.py:224](https://github.com/lm-sys/FastChat/blob/587d5cfa1609a43d192cedb8441cac3c17db105d/fastchat/data/clean_sharegpt.py#L224)
- [fastchat/data/convert_alpaca.py:14](https://github.com/lm-sys/FastChat/blob/587d5cfa1609a43d192cedb8441cac3c17db105d/fastchat/data/convert_alpaca.py#L14)
- [fastchat/data/extract_gpt4_only.py:10](https://github.com/lm-sys/FastChat/blob/587d5cfa1609a43d192cedb8441cac3c17db105d/fastchat/data/extract_gpt4_only.py#L10)
- [fastchat/data/extract_single_round.py:10](https://github.com/lm-sys/FastChat/blob/587d5cfa1609a43d192cedb8441cac3c17db105d/fastchat/data/extract_single_round.py#L10)
- [fastchat/data/filter_wrong_format.py:28](https://github.com/lm-sys/FastChat/blob/587d5cfa1609a43d192cedb8441cac3c17db105d/fastchat/data/filter_wrong_format.py#L28)
- [fastchat/data/get_stats.py:59](https://github.com/lm-sys/FastChat/blob/587d5cfa1609a43d192cedb8441cac3c17db105d/fastchat/data/get_stats.py#L59)
- [fastchat/data/hardcoded_questions.py:162](https://github.com/lm-sys/FastChat/blob/587d5cfa1609a43d192cedb8441cac3c17db105d/fastchat/data/hardcoded_questions.py#L162)
- [fastchat/data/inspect_data.py:10](https://github.com/lm-sys/FastChat/blob/587d5cfa1609a43d192cedb8441cac3c17db105d/fastchat/data/inspect_data.py#L10)
- [fastchat/data/merge.py:11](https://github.com/lm-sys/FastChat/blob/587d5cfa1609a43d192cedb8441cac3c17db105d/fastchat/data/merge.py#L11)
- [fastchat/data/optional_clean.py:47](https://github.com/lm-sys/FastChat/blob/587d5cfa1609a43d192cedb8441cac3c17db105d/fastchat/data/optional_clean.py#L47)
- [fastchat/data/optional_replace.py:53](https://github.com/lm-sys/FastChat/blob/587d5cfa1609a43d192cedb8441cac3c17db105d/fastchat/data/optional_replace.py#L53)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 8 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 86 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed routes: POST /worker_generate_stream, POST /worker_generate… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| fastchat package | library | Observed | Groups 48 file(s) under fastchat package (observed from repository paths and static analysis). Observed top-level classes: APIChatCompletionRequest, APITokenCheckRequest, APITokenCheckRequestItem, APITokenCheckResponse,… |
| playground package | library | Observed | Groups 1 file(s) under playground package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 5 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 17 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: ClaudeConversationResizesCorrectly, DontResizeIfLessThanMaxTest, DontResizeIfMaxImageSizeIsNone, OpenAIConv… |

## Important files

- `.github/workflows/python-package.yml` (ci)
- `docker/Dockerfile` (container)
- `docker/docker-compose.yml` (container)
- `fastchat/serve/monitor/classify/config.yaml` (config)
- `fastchat/serve/monitor/classify/vision_config.yaml` (config)
- `playground/deepspeed_config_s2.json` (config)
- `playground/deepspeed_config_s3.json` (config)
- `pyproject.toml` (manifest)
- `theme.json` (config)

## Top-level layout

- `fastchat` — 150 analysed file(s)
- `docs` — 23 analysed file(s)
- `tests` — 10 analysed file(s)
- `playground` — 9 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `scripts` — 6 analysed file(s)
- `.github` — 2 analysed file(s)
- `docker` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `587d5cfa1609a43d192cedb8441cac3c17db105d` is the revision these paths and observations refer to.
