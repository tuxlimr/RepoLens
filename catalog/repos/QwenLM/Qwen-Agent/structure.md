# Project structure: QwenLM/Qwen-Agent

**Analysed commit:** `31a4d36d123688581a9e9744427272b33ce940e0`

**Commit reference:** [31a4d36d123688581a9e9744427272b33ce940e0](https://github.com/QwenLM/Qwen-Agent/commit/31a4d36d123688581a9e9744427272b33ce940e0)

**Tree at this commit:** [QwenLM/Qwen-Agent@31a4d36d1236](https://github.com/QwenLM/Qwen-Agent/tree/31a4d36d123688581a9e9744427272b33ce940e0)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | QwenLM/Qwen-Agent |
| Description | Agent framework and applications built upon Qwen>=3.0, featuring Function Calling, MCP, Code Interpreter, RAG, Chrome extension, etc. |
| Stars | 17258 |
| Forks | 1768 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `31a4d36d123688581a9e9744427272b33ce940e0` |
| Retrieved at | 2026-11-14T19:08:36.966426+00:00 |
| Files in this snapshot | 304 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    deploy-docs.yml
benchmark/  (85 files)
  code_interpreter/  (25 files)
    metrics/  (4 files)
      … 4 files under this directory
    models/  (5 files)
      … 5 files under this directory
    parser/  (3 files)
      … 3 files under this directory
    prompt/  (5 files)
      … 5 files under this directory
    utils/  (3 files)
      … 3 files under this directory
    README.md
    code_interpreter.py
    config.py
    inference_and_execute.py
    requirements.txt
  deepplanning/  (60 files)
    shoppingplanning/  (29 files)
      … 29 files under this directory
    travelplanning/  (25 files)
      … 25 files under this directory
    README.md
    aggregate_results.py
    env.example
    models_config.json
    requirements.txt
    run_all.sh
browser_qwen/  (5 files)
  src/  (3 files)
    content.js
    popup.html
    popup.js
  background.js
  manifest.json
examples/  (34 files)
  resource/  (1 files)
    stock_prices.csv
  __init__.py
  assistant_add_custom_tool.py
  assistant_audio.py
  assistant_mcp_sqlite_bot.py
  assistant_omni.py
  assistant_qwen3.5.py
  assistant_qwen3.py
  assistant_qwen3_coder.py
  assistant_qwen3vl.py
  assistant_qwq.py
  assistant_rag.py
  assistant_weather_bot.py
  cookbook_database_manipulation.ipynb
  cookbook_drive_guide.ipynb
  cookbook_mind_map.ipynb
  function_calling.py
  function_calling_in_parallel.py
  gpt_mentions.py
  group_chat_chess.py
  group_chat_demo.py
  llm_quick_chat_oai.py
  llm_riddles.py
  llm_vl_mix_text.py
  long_dialogue.py
  … 9 more files
qwen-agent-docs/  (42 files)
  website/  (42 files)
    app/  (7 files)
      … 7 files under this directory
    content/  (20 files)
      … 20 files under this directory
    public/  (5 files)
      … 5 files under this directory
    src/  (3 files)
      … 3 files under this directory
    .gitignore
    mdx-components.tsx
    next-env.d.ts
    next.config.mjs
    package.json
    postcss.config.js
    tsconfig.json
qwen_agent/  (94 files)
  agents/  (32 files)
    doc_qa/  (5 files)
      … 5 files under this directory
    keygen_strategies/  (6 files)
      … 6 files under this directory
    writing/  (4 files)
      … 4 files under this directory
    __init__.py
    article_agent.py
    assistant.py
    dialogue_retrieval_agent.py
    dialogue_simulator.py
    fncall_agent.py
    group_chat.py
    group_chat_auto_router.py
    group_chat_creator.py
    human_simulator.py
    memo_assistant.py
    react_chat.py
    router.py
    tir_agent.py
    user_agent.py
    virtual_memory_agent.py
    write_from_scratch.py
  gui/  (7 files)
    assets/  (2 files)
      … 2 files under this directory
    __init__.py
    gradio_dep.py
    gradio_utils.py
    utils.py
    web_ui.py
  llm/  (18 files)
    fncall_prompts/  (4 files)
      … 4 files under this directory
    __init__.py
    azure.py
    base.py
    function_calling.py
    oai.py
    openvino.py
    qwen_dashscope.py
    qwenaudio_dashscope.py
    qwenomni_oai.py
    qwenvl_dashscope.py
    qwenvl_oai.py
    qwenvlo_dashscope.py
    schema.py
    transformers_llm.py
  memory/  (2 files)
    __init__.py
    memory.py
  tools/  (24 files)
    resource/  (2 files)
      … 2 files under this directory
    search_tools/  (6 files)
      … 6 files under this directory
    __init__.py
    amap_weather.py
    base.py
    code_interpreter.py
    doc_parser.py
    extract_doc_vocabulary.py
    image_gen.py
    image_search.py
    image_zoom_in_qwen3vl.py
    mcp_manager.py
    python_executor.py
    retrieval.py
    simple_doc_parser.py
    storage.py
    web_extractor.py
    web_search.py
  utils/  (6 files)
    __init__.py
    output_beautify.py
    parallel_executor.py
    str_processing.py
    tokenization_qwen.py
    utils.py
  __init__.py
  agent.py
  log.py
  multi_agent_hub.py
  settings.py
qwen_server/  (11 files)
  css/  (1 files)
    main.css
  js/  (1 files)
    main.js
  __init__.py
  add_qwen_libs.py
  assistant_server.py
  database_server.py
  output_beautify.py
  schema.py
  server_config.json
  utils.py
  workstation_server.py
tests/  (22 files)
  agents/  (7 files)
    test_article_agent.py
    test_assistant.py
    test_custom_tool_object.py
    test_doc_qa.py
    test_parallel_qa.py
    test_react_chat.py
    test_router.py
  examples/  (3 files)
    test_examples.py
    test_long_dialogue.py
    test_vm_qa.py
  llm/  (4 files)
    test_continue.py
    test_dashscope.py
    test_function_content.py
    test_oai.py
  memory/  (1 files)
    test_memory.py
  qwen_server/  (1 files)
    test_database_server.py
  tools/  (6 files)
    test_doc_parser.py
    test_hybrid_search.py
    test_keyword_search.py
    test_simple_doc_parser.py
    test_tools.py
    test_vector_search.py
.gitignore
.pre-commit-config.yaml
LICENSE
MANIFEST.in
README.md
README_CN.md
browser_qwen.md
browser_qwen_cn.md
run_server.py
setup.py
```

## Entry points

- [benchmark/code_interpreter/code_interpreter.py:243](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/benchmark/code_interpreter/code_interpreter.py#L243)
- [benchmark/code_interpreter/inference_and_execute.py:227](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/benchmark/code_interpreter/inference_and_execute.py#L227)
- [benchmark/deepplanning/aggregate_results.py:375](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/benchmark/deepplanning/aggregate_results.py#L375)
- [benchmark/deepplanning/shoppingplanning/agent/shopping_agent.py:513](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/benchmark/deepplanning/shoppingplanning/agent/shopping_agent.py#L513)
- [benchmark/deepplanning/shoppingplanning/evaluation/evaluation_pipeline.py:478](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/benchmark/deepplanning/shoppingplanning/evaluation/evaluation_pipeline.py#L478)
- [benchmark/deepplanning/shoppingplanning/evaluation/score_statistics.py:279](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/benchmark/deepplanning/shoppingplanning/evaluation/score_statistics.py#L279)
- [benchmark/deepplanning/shoppingplanning/run.py:170](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/benchmark/deepplanning/shoppingplanning/run.py#L170)
- [benchmark/deepplanning/travelplanning/agent/tools_fn_agent.py:549](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/benchmark/deepplanning/travelplanning/agent/tools_fn_agent.py#L549)
- [benchmark/deepplanning/travelplanning/evaluation/convert_report.py:363](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/benchmark/deepplanning/travelplanning/evaluation/convert_report.py#L363)
- [benchmark/deepplanning/travelplanning/evaluation/eval_converted.py:579](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/benchmark/deepplanning/travelplanning/evaluation/eval_converted.py#L579)
- [benchmark/deepplanning/travelplanning/run.py:502](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/benchmark/deepplanning/travelplanning/run.py#L502)
- [qwen_agent/tools/image_search.py:200](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/qwen_agent/tools/image_search.py#L200)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| benchmark package | library | Observed | Groups 53 file(s) under benchmark package (observed from repository paths and static analysis). Observed top-level classes: AddCouponToCartTool, AddProductToCartTool, AttractionDetailsQueryTool, AttractionRecommendTool,… |
| browser_qwen package | library | Observed | Groups 3 file(s) under browser_qwen package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 18 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: get_model, get_react_parser, get_react_prompt, get_version, read_description. |
| Data layer | data | Observed | Groups 5 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: HFModel, LLM, Qwen, QwenDashscopeVLModel, QwenVL. |
| Application entry point | entrypoint | Observed | Groups 15 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed routes: POST /endpoint. Observed top-level classes: ColorOb… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| qwen_agent package | library | Observed | Groups 88 file(s) under qwen_agent package (observed from repository paths and static analysis). Observed top-level classes: Agent, AmapWeather, AnyThreadEventLoopPolicy, ArticleAgent, Assistant, BaseChatModel. Observed… |
| qwen-agent-docs package | library | Observed | Groups 18 file(s) under qwen-agent-docs package (observed from repository paths and static analysis). |
| qwen_server package | library | Observed | Groups 8 file(s) under qwen_server package (observed from repository paths and static analysis). Observed top-level classes: GlobalConfig, PathConfig, ServerConfig. Observed top-level functions: add_file, add_text, bot,… |
| Tests | test | Observed | Groups 22 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: MyImageGen. Observed top-level functions: init_agent_service, test_amap_weather, test_article_agent_full_ar… |

## Important files

- `.github/workflows/deploy-docs.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `MANIFEST.in` (manifest)
- `benchmark/code_interpreter/requirements.txt` (manifest)
- `benchmark/deepplanning/models_config.json` (config)
- `benchmark/deepplanning/requirements.txt` (manifest)
- `benchmark/deepplanning/shoppingplanning/data/level_1_query_meta.json` (config)
- `benchmark/deepplanning/shoppingplanning/data/level_2_query_meta.json` (config)
- `benchmark/deepplanning/shoppingplanning/data/level_3_query_meta.json` (config)
- `benchmark/deepplanning/shoppingplanning/tools/shopping_tool_schema.json` (config)
- `benchmark/deepplanning/travelplanning/tools/tool_schema.json` (config)
- `benchmark/deepplanning/travelplanning/tools/tool_schema_en.json` (config)
- `benchmark/deepplanning/travelplanning/tools/tool_schema_zh.json` (config)
- `browser_qwen/manifest.json` (config)
- `qwen-agent-docs/website/package.json` (manifest)
- `qwen-agent-docs/website/tsconfig.json` (config)
- `qwen_server/server_config.json` (config)
- `setup.py` (manifest)

## Top-level layout

- `qwen_agent` — 94 analysed file(s)
- `benchmark` — 85 analysed file(s)
- `qwen-agent-docs` — 42 analysed file(s)
- `examples` — 34 analysed file(s)
- `tests` — 22 analysed file(s)
- `qwen_server` — 11 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `browser_qwen` — 5 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `31a4d36d123688581a9e9744427272b33ce940e0` is the revision these paths and observations refer to.
