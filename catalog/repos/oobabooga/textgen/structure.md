# Project structure: oobabooga/textgen

**Analysed commit:** `c93f8871239550de2ccfe1e95d469aa82616f07e`

**Commit reference:** [c93f8871239550de2ccfe1e95d469aa82616f07e](https://github.com/oobabooga/textgen/commit/c93f8871239550de2ccfe1e95d469aa82616f07e)

**Tree at this commit:** [oobabooga/textgen@c93f88712395](https://github.com/oobabooga/textgen/tree/c93f8871239550de2ccfe1e95d469aa82616f07e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | oobabooga/textgen |
| Description | Open-source desktop app for local LLMs. Text, vision, tool-calling, OpenAI/Anthropic-compatible API. 100% private. |
| Stars | 47739 |
| Forks | 5972 |
| Licence | AGPL-3.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `c93f8871239550de2ccfe1e95d469aa82616f07e` |
| Retrieved at | 2026-11-14T19:06:36.416723+00:00 |
| Files in this snapshot | 244 |

## Directory tree

```text
.github/  (11 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report_template.yml
    feature_request.md
  workflows/  (7 files)
    build-everything-tgw.yml
    build-portable-release-cuda.yml
    build-portable-release-ik-cuda.yml
    build-portable-release-ik.yml
    build-portable-release-rocm.yml
    build-portable-release-vulkan.yml
    build-portable-release.yml
  dependabot.yml
  pull_request_template.md
css/  (10 files)
  NotoSans/  (1 files)
    stylesheet.css
  chat_style-Dark.css
  chat_style-TheEncrypted777.css
  chat_style-cai-chat-square.css
  chat_style-cai-chat.css
  chat_style-messenger.css
  chat_style-wpp.css
  html_instruct_style.css
  html_readable_style.css
  main.css
desktop/  (5 files)
  main.js
  package.json
  preload.js
  textgen.bat
  textgen.sh
docker/  (11 files)
  TensorRT-LLM/  (1 files)
    Dockerfile
  amd/  (2 files)
    Dockerfile
    docker-compose.yml
  cpu/  (2 files)
    Dockerfile
    docker-compose.yml
  intel/  (2 files)
    Dockerfile
    docker-compose.yml
  nvidia/  (2 files)
    Dockerfile
    docker-compose.yml
  .dockerignore
  .env.example
docs/  (17 files)
  01 - Chat Tab.md
  02 - Default and Notebook Tabs.md
  03 - Parameters Tab.md
  04 - Model Tab.md
  05 - Training Tab.md
  06 - Session Tab.md
  07 - Extensions.md
  08 - Additional Tips.md
  09 - Docker.md
  11 - AMD Setup.md
  12 - OpenAI API.md
  13 - Keyboard Shortcuts.md
  Image Generation Tutorial.md
  Multimodal Tutorial.md
  README.md
  Tool Calling Tutorial.md
  What Works.md
extensions/  (53 files)
  character_bias/  (1 files)
    script.py
  coqui_tts/  (5 files)
    harvard_sentences.txt
    languages.json
    requirements.txt
    script.py
    style.css
  example/  (1 files)
    script.py
  gallery/  (2 files)
    script.js
    script.py
  google_translate/  (2 files)
    requirements.txt
    script.py
  long_replies/  (1 files)
    script.py
  ngrok/  (3 files)
    README.md
    requirements.txt
    script.py
  perplexity_colors/  (1 files)
    script.py
  sd_api_pictures/  (3 files)
    README.MD
    script.py
    style.css
  send_pictures/  (1 files)
    script.py
  silero_tts/  (8 files)
    outputs/  (1 files)
      … 1 files under this directory
    harvard_sentences.txt
    languages.json
    requirements.txt
    script.py
    style.css
    test_tts.py
    tts_preprocessor.py
  superbooga/  (4 files)
    chromadb.py
    download_urls.py
    requirements.txt
    script.py
  superboogav2/  (17 files)
    benchmark_texts/  (1 files)
      … 1 files under this directory
    nltk_data/  (1 files)
      … 1 files under this directory
    README.md
    api.py
    benchmark.py
    chat_handler.py
    chromadb.py
    config.json
    data_preprocessor.py
    data_processor.py
    download_urls.py
    notebook_handler.py
    optimize.py
    parameters.py
    requirements.txt
    script.py
    utils.py
  whisper_stt/  (4 files)
    readme.md
    requirements.txt
    script.js
    script.py
js/  (8 files)
  katex/  (1 files)
    auto-render.js
  dark_theme.js
  global_scope_js.js
  main.js
  save_files.js
  show_controls.js
  switch_tabs.js
  update_big_picture.js
modules/  (60 files)
  api/  (14 files)
    __init__.py
    anthropic.py
    cache_embedding_model.py
    completions.py
    embeddings.py
    errors.py
    images.py
    logits.py
    models.py
    moderations.py
    script.py
    tokens.py
    typing.py
    utils.py
  grammar/  (3 files)
    __init__.py
    grammar_utils.py
    logits_process.py
  LoRA.py
  callbacks.py
  chat.py
  evaluate.py
  exllamav3.py
  exllamav3_hf.py
  extensions.py
  html_generator.py
  image_models.py
  image_utils.py
  llama_cpp_server.py
  loaders.py
  logging_colors.py
  logits.py
  metadata_gguf.py
  models.py
  models_settings.py
  paths.py
  presets.py
  prompts.py
  reasoning.py
  sampler_hijack.py
  sane_markdown_lists.py
  shared.py
  … 19 more files
requirements/  (17 files)
  full/  (6 files)
    requirements.txt
    requirements_amd.txt
    requirements_apple_intel.txt
    requirements_apple_silicon.txt
    requirements_cpu_only.txt
    requirements_nowheels.txt
  portable/  (11 files)
    requirements.txt
    requirements_amd.txt
    requirements_apple_intel.txt
    requirements_apple_silicon.txt
    requirements_cpu_only.txt
    requirements_cuda131.txt
    requirements_ik.txt
    requirements_ik_cpu_only.txt
    requirements_ik_cuda131.txt
    requirements_nowheels.txt
    requirements_vulkan.txt
user_data/  (35 files)
  characters/  (2 files)
    Assistant.yaml
    Example.yaml
  extensions/  (1 files)
    place-your-extensions-here.txt
  grammars/  (8 files)
    arithmetic.gbnf
    c.gbnf
    chess.gbnf
    json.gbnf
    json_w_trailing_space.gbnf
    list.gbnf
    roleplay.gbnf
    simple_arithmetic.gbnf
  image_models/  (1 files)
    place-your-models-here.txt
  instruction-templates/  (6 files)
    Alpaca.yaml
    ChatML.yaml
    Llama-v3.yaml
    Mistral.yaml
    Open Assistant.yaml
    Vicuna-v1.1.yaml
  loras/  (1 files)
    place-your-loras-here.txt
  mmproj/  (1 files)
    place-your-mmproj-here.txt
  models/  (1 files)
    place-your-models-here.txt
  presets/  (3 files)
    Creative.yaml
    Deterministic.yaml
    Top-P.yaml
  tools/  (5 files)
    calculate.py
    fetch_webpage.py
    get_datetime.py
    roll_dice.py
    web_search.py
  training/  (4 files)
    datasets/  (4 files)
      … 4 files under this directory
  users/  (1 files)
    Default.yaml
  CMD_FLAGS.txt
.gitignore
Colab-TextGen-GPU.ipynb
LICENSE
README.md
cmd_linux.sh
cmd_macos.sh
cmd_windows.bat
download-model.py
one_click.py
server.py
setup.cfg
start_linux.sh
start_macos.sh
start_windows.bat
update_wizard_linux.sh
update_wizard_macos.sh
update_wizard_windows.bat
```

## Entry points

- [download-model.py:381](https://github.com/oobabooga/textgen/blob/c93f8871239550de2ccfe1e95d469aa82616f07e/download-model.py#L381)
- [extensions/silero_tts/tts_preprocessor.py:198](https://github.com/oobabooga/textgen/blob/c93f8871239550de2ccfe1e95d469aa82616f07e/extensions/silero_tts/tts_preprocessor.py#L198)
- [modules/api/script.py:93](https://github.com/oobabooga/textgen/blob/c93f8871239550de2ccfe1e95d469aa82616f07e/modules/api/script.py#L93)
- [one_click.py:489](https://github.com/oobabooga/textgen/blob/c93f8871239550de2ccfe1e95d469aa82616f07e/one_click.py#L489)
- [server.py:249](https://github.com/oobabooga/textgen/blob/c93f8871239550de2ccfe1e95d469aa82616f07e/server.py#L249)
- [desktop/main.js](https://github.com/oobabooga/textgen/blob/c93f8871239550de2ccfe1e95d469aa82616f07e/desktop/main.js)
- [js/main.js](https://github.com/oobabooga/textgen/blob/c93f8871239550de2ccfe1e95d469aa82616f07e/js/main.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 13 file(s) under api layer (observed from repository paths and static analysis). Observed top-level classes: AnthropicRequest, AnthropicRequestParams, ChatCompletionRequest, ChatCompletionRequestParams, ChatCompl… |
| Configuration and deployment | config | Observed | Groups 56 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 6 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level functions: ExLlamav3_HF_loader, ExLlamav3_loader, TensorRT_LLM_loader, llama_cpp_server_loader, load_model, load… |
| desktop package | library | Observed | Groups 3 file(s) under desktop package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 5 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed routes: OPTIONS /, POST /v1/completions, POST /v1/chat/compl… |
| extensions package | library | Observed | Groups 29 file(s) under extensions package (observed from repository paths and static analysis). Observed top-level classes: APIManager, ChromaCollector, CustomThreadingHTTPServer, Handler, Info, MyLogits. Observed top-… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| js package | library | Observed | Groups 8 file(s) under js package (observed from repository paths and static analysis). |
| modules package | library | Observed | Groups 45 file(s) under modules package (observed from repository paths and static analysis). Observed top-level classes: AdaptivePLogitsWarper, ConcurrentGenerator, DRYLogitsProcessor, DynamicTemperatureLogitsWarper, E… |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: load_model, output_modifier, xmlesc. |
| user_data package | library | Observed | Groups 5 file(s) under user_data package (observed from repository paths and static analysis). Observed top-level functions: _eval, execute. |

## Important files

- `.github/ISSUE_TEMPLATE/bug_report_template.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/build-everything-tgw.yml` (ci)
- `.github/workflows/build-portable-release-cuda.yml` (ci)
- `.github/workflows/build-portable-release-ik-cuda.yml` (ci)
- `.github/workflows/build-portable-release-ik.yml` (ci)
- `.github/workflows/build-portable-release-rocm.yml` (ci)
- `.github/workflows/build-portable-release-vulkan.yml` (ci)
- `.github/workflows/build-portable-release.yml` (ci)
- `desktop/package.json` (manifest)
- `docker/.dockerignore` (container)
- `docker/.env.example` (config)
- `docker/TensorRT-LLM/Dockerfile` (container)
- `docker/amd/Dockerfile` (container)
- `docker/amd/docker-compose.yml` (container)
- `docker/cpu/Dockerfile` (container)
- `docker/cpu/docker-compose.yml` (container)
- `docker/intel/Dockerfile` (container)
- `docker/intel/docker-compose.yml` (container)
- `docker/nvidia/Dockerfile` (container)
- `docker/nvidia/docker-compose.yml` (container)
- `extensions/coqui_tts/languages.json` (config)
- `extensions/coqui_tts/requirements.txt` (manifest)
- `extensions/google_translate/requirements.txt` (manifest)
- `extensions/ngrok/requirements.txt` (manifest)
- `extensions/silero_tts/languages.json` (config)
- `extensions/silero_tts/requirements.txt` (manifest)
- `extensions/superbooga/requirements.txt` (manifest)
- `extensions/superboogav2/benchmark_texts/questions.json` (config)
- `extensions/superboogav2/config.json` (config)
- `extensions/superboogav2/requirements.txt` (manifest)
- `extensions/whisper_stt/requirements.txt` (manifest)
- `requirements/full/requirements.txt` (manifest)
- `requirements/full/requirements_amd.txt` (manifest)
- `requirements/full/requirements_apple_intel.txt` (manifest)
- `requirements/full/requirements_apple_silicon.txt` (manifest)
- `requirements/full/requirements_cpu_only.txt` (manifest)
- `requirements/full/requirements_nowheels.txt` (manifest)
- `requirements/portable/requirements.txt` (manifest)
- `requirements/portable/requirements_amd.txt` (manifest)
- `requirements/portable/requirements_apple_intel.txt` (manifest)
- `requirements/portable/requirements_apple_silicon.txt` (manifest)
- `requirements/portable/requirements_cpu_only.txt` (manifest)
- `requirements/portable/requirements_cuda131.txt` (manifest)
- `requirements/portable/requirements_ik.txt` (manifest)
- `requirements/portable/requirements_ik_cpu_only.txt` (manifest)
- `requirements/portable/requirements_ik_cuda131.txt` (manifest)
- `requirements/portable/requirements_nowheels.txt` (manifest)
- `requirements/portable/requirements_vulkan.txt` (manifest)
- `setup.cfg` (manifest)
- `user_data/characters/Assistant.yaml` (config)
- `user_data/characters/Example.yaml` (config)
- `user_data/instruction-templates/Alpaca.yaml` (config)
- `user_data/instruction-templates/ChatML.yaml` (config)
- `user_data/instruction-templates/Llama-v3.yaml` (config)
- `user_data/instruction-templates/Mistral.yaml` (config)
- `user_data/instruction-templates/Open Assistant.yaml` (config)
- `user_data/instruction-templates/Vicuna-v1.1.yaml` (config)
- `user_data/presets/Creative.yaml` (config)
- `user_data/presets/Deterministic.yaml` (config)
- `user_data/presets/Top-P.yaml` (config)
- `user_data/training/datasets/example_messages.json` (config)
- `user_data/training/datasets/example_sharegpt.json` (config)
- `user_data/training/datasets/example_text.json` (config)
- `user_data/users/Default.yaml` (config)

## Top-level layout

- `modules` — 60 analysed file(s)
- `extensions` — 53 analysed file(s)
- `user_data` — 35 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `docs` — 17 analysed file(s)
- `requirements` — 17 analysed file(s)
- `.github` — 11 analysed file(s)
- `docker` — 11 analysed file(s)
- `css` — 10 analysed file(s)
- `js` — 8 analysed file(s)
- `desktop` — 5 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 4 file(s) were skipped during inventory (4 x generated/minified file excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `c93f8871239550de2ccfe1e95d469aa82616f07e` is the revision these paths and observations refer to.
