# Project structure: zai-org/ChatGLM3

**Analysed commit:** `732294f42e2625509000daa87a9c3748d0bbb957`

**Commit reference:** [732294f42e2625509000daa87a9c3748d0bbb957](https://github.com/zai-org/ChatGLM3/commit/732294f42e2625509000daa87a9c3748d0bbb957)

**Tree at this commit:** [zai-org/ChatGLM3@732294f42e26](https://github.com/zai-org/ChatGLM3/tree/732294f42e2625509000daa87a9c3748d0bbb957)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | zai-org/ChatGLM3 |
| Description | ChatGLM3 series: Open Bilingual Chat LLMs | 开源双语对话语言模型 |
| Stars | 13628 |
| Forks | 1568 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `732294f42e2625509000daa87a9c3748d0bbb957` |
| Retrieved at | 2026-11-14T19:09:47.552816+00:00 |
| Files in this snapshot | 68 |

## Directory tree

```text
.github/  (3 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.yaml
    feature-request.yaml
  PULL_REQUEST_TEMPLATE/  (1 files)
    pr_template.md
Intel_device_demo/  (9 files)
  ipex_llm_cpu_demo/  (6 files)
    api_server.py
    chatglm3_infer.py
    chatglm3_web_demo.py
    generate.py
    openai_api_request.py
    utils.py
  openvino_demo/  (2 files)
    README.md
    openvino_cli_demo.py
  README.md
basic_demo/  (5 files)
  cli_batch_request_demo.py
  cli_demo.py
  cli_demo_bad_word_ids.py
  web_demo_gradio.py
  web_demo_streamlit.py
composite_demo/  (11 files)
  .streamlit/  (1 files)
    config.toml
  README.md
  README_en.md
  client.py
  conversation.py
  demo_chat.py
  demo_ci.py
  demo_tool.py
  main.py
  requirements.txt
  tool_registry.py
finetune_demo/  (11 files)
  configs/  (5 files)
    ds_zero_2.json
    ds_zero_3.json
    lora.yaml
    ptuning_v2.yaml
    sft.yaml
  README.md
  README_en.md
  finetune_hf.py
  inference_hf.py
  lora_finetune.ipynb
  requirements.txt
langchain_demo/  (5 files)
  tools/  (3 files)
    Calculator.py
    DistanceConversion.py
    Weather.py
  ChatGLM3.py
  main.py
openai_api_demo/  (5 files)
  api_server.py
  docker-compose.yml
  langchain_openai_api.py
  openai_api_request.py
  utils.py
resources/  (1 files)
  WECHAT.md
tensorrt_llm_demo/  (2 files)
  README.md
  tensorrt_llm_cli_demo.py
tools_using_demo/  (5 files)
  README.md
  README_en.md
  cli_demo_tool.py
  openai_api_demo.py
  tool_register.py
.gitignore
DEPLOYMENT.md
DEPLOYMENT_en.md
LICENSE
MODEL_LICENSE
PROMPT.md
PROMPT_en.md
README.md
README_en.md
requirements.txt
update_requirements.sh
```

## Entry points

- [Intel_device_demo/ipex_llm_cpu_demo/api_server.py:67](https://github.com/zai-org/ChatGLM3/blob/732294f42e2625509000daa87a9c3748d0bbb957/Intel_device_demo/ipex_llm_cpu_demo/api_server.py#L67)
- [Intel_device_demo/ipex_llm_cpu_demo/generate.py:14](https://github.com/zai-org/ChatGLM3/blob/732294f42e2625509000daa87a9c3748d0bbb957/Intel_device_demo/ipex_llm_cpu_demo/generate.py#L14)
- [Intel_device_demo/ipex_llm_cpu_demo/openai_api_request.py:87](https://github.com/zai-org/ChatGLM3/blob/732294f42e2625509000daa87a9c3748d0bbb957/Intel_device_demo/ipex_llm_cpu_demo/openai_api_request.py#L87)
- [Intel_device_demo/openvino_demo/openvino_cli_demo.py:55](https://github.com/zai-org/ChatGLM3/blob/732294f42e2625509000daa87a9c3748d0bbb957/Intel_device_demo/openvino_demo/openvino_cli_demo.py#L55)
- [basic_demo/cli_batch_request_demo.py:62](https://github.com/zai-org/ChatGLM3/blob/732294f42e2625509000daa87a9c3748d0bbb957/basic_demo/cli_batch_request_demo.py#L62)
- [basic_demo/cli_demo.py:56](https://github.com/zai-org/ChatGLM3/blob/732294f42e2625509000daa87a9c3748d0bbb957/basic_demo/cli_demo.py#L56)
- [basic_demo/cli_demo_bad_word_ids.py:86](https://github.com/zai-org/ChatGLM3/blob/732294f42e2625509000daa87a9c3748d0bbb957/basic_demo/cli_demo_bad_word_ids.py#L86)
- [composite_demo/tool_registry.py:136](https://github.com/zai-org/ChatGLM3/blob/732294f42e2625509000daa87a9c3748d0bbb957/composite_demo/tool_registry.py#L136)
- [finetune_demo/finetune_hf.py:39](https://github.com/zai-org/ChatGLM3/blob/732294f42e2625509000daa87a9c3748d0bbb957/finetune_demo/finetune_hf.py#L39)
- [finetune_demo/inference_hf.py:20](https://github.com/zai-org/ChatGLM3/blob/732294f42e2625509000daa87a9c3748d0bbb957/finetune_demo/inference_hf.py#L20)
- [langchain_demo/main.py:65](https://github.com/zai-org/ChatGLM3/blob/732294f42e2625509000daa87a9c3748d0bbb957/langchain_demo/main.py#L65)
- [openai_api_demo/api_server.py:69](https://github.com/zai-org/ChatGLM3/blob/732294f42e2625509000daa87a9c3748d0bbb957/openai_api_demo/api_server.py#L69)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| basic_demo package | library | Observed | Groups 2 file(s) under basic_demo package (observed from repository paths and static analysis). Observed top-level classes: StopOnTokens. Observed top-level functions: _resolve_path, get_model, load_model_and_tokenizer,… |
| composite_demo package | library | Observed | Groups 4 file(s) under composite_demo package (observed from repository paths and static analysis). Observed top-level classes: CodeKernel, Conversation, Role. Observed top-level functions: append_conversation, b64_2_im… |
| Configuration and deployment | config | Observed | Groups 10 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 19 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI, Typer. Observed routes: GET /health, POST /v1/embeddings, GET /v1/mo… |
| External integrations | external | Observed | Groups 1 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: Client, HFClient. Observed top-level functions: get_client, stream_chat. |
| Intel_device_demo package | library | Observed | Groups 3 file(s) under intel_device_demo package (observed from repository paths and static analysis). Observed top-level classes: InvalidScoreLogitsProcessor. Observed top-level functions: apply_stopping_strings, gener… |
| langchain_demo package | library | Observed | Groups 4 file(s) under langchain_demo package (observed from repository paths and static analysis). Observed top-level classes: Calculator, CalculatorInput, ChatGLM3, DistanceConversionInput, DistanceConverter, Weather. |
| openai_api_demo package | library | Observed | Groups 1 file(s) under openai_api_demo package (observed from repository paths and static analysis). Observed top-level classes: InvalidScoreLogitsProcessor. Observed top-level functions: apply_stopping_strings, generat… |

## Important files

- `.github/ISSUE_TEMPLATE/bug_report.yaml` (config)
- `.github/ISSUE_TEMPLATE/feature-request.yaml` (config)
- `composite_demo/.streamlit/config.toml` (config)
- `composite_demo/requirements.txt` (manifest)
- `finetune_demo/configs/ds_zero_2.json` (config)
- `finetune_demo/configs/ds_zero_3.json` (config)
- `finetune_demo/configs/lora.yaml` (config)
- `finetune_demo/configs/ptuning_v2.yaml` (config)
- `finetune_demo/configs/sft.yaml` (config)
- `finetune_demo/requirements.txt` (manifest)
- `openai_api_demo/docker-compose.yml` (container)
- `requirements.txt` (manifest)

## Top-level layout

- `(root files)` — 11 analysed file(s)
- `composite_demo` — 11 analysed file(s)
- `finetune_demo` — 11 analysed file(s)
- `Intel_device_demo` — 9 analysed file(s)
- `basic_demo` — 5 analysed file(s)
- `langchain_demo` — 5 analysed file(s)
- `openai_api_demo` — 5 analysed file(s)
- `tools_using_demo` — 5 analysed file(s)
- `.github` — 3 analysed file(s)
- `tensorrt_llm_demo` — 2 analysed file(s)
- `resources` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `732294f42e2625509000daa87a9c3748d0bbb957` is the revision these paths and observations refer to.
