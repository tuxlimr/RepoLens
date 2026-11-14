# Project structure: huggingface/smolagents

**Analysed commit:** `96f33faaf028479119ec8d34507b47694cf14e34`

**Commit reference:** [96f33faaf028479119ec8d34507b47694cf14e34](https://github.com/huggingface/smolagents/commit/96f33faaf028479119ec8d34507b47694cf14e34)

**Tree at this commit:** [huggingface/smolagents@96f33faaf028](https://github.com/huggingface/smolagents/tree/96f33faaf028479119ec8d34507b47694cf14e34)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | huggingface/smolagents |
| Description | 🤗 smolagents: a barebones library for agents that think in code. |
| Stars | 30369 |
| Forks | 3216 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `96f33faaf028479119ec8d34507b47694cf14e34` |
| Retrieved at | 2026-11-14T19:07:09.658024+00:00 |
| Files in this snapshot | 184 |

## Directory tree

```text
.github/  (10 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    doc_improvement.md
    feature_request.md
  workflows/  (6 files)
    build_documentation.yml
    build_pr_documentation.yml
    quality.yml
    tests.yml
    trufflehog.yml
    upload_pr_documentation.yml
  dependabot.yml
docs/  (81 files)
  source/  (80 files)
    en/  (24 files)
      … 24 files under this directory
    es/  (4 files)
      … 4 files under this directory
    hi/  (15 files)
      … 15 files under this directory
    ko/  (19 files)
      … 19 files under this directory
    zh/  (18 files)
      … 18 files under this directory
  README.md
examples/  (34 files)
  async_agent/  (3 files)
    README.md
    main.py
    requirements.txt
  open_deep_research/  (15 files)
    scripts/  (8 files)
      … 8 files under this directory
    README.md
    analysis.ipynb
    app.py
    requirements.txt
    run.py
    run_gaia.py
    visual_vs_text_browser.ipynb
  plan_customization/  (2 files)
    README.md
    plan_customization.py
  server/  (2 files)
    README.md
    main.py
  smolagents_benchmark/  (2 files)
    run.py
    score.ipynb
  agent_from_any_llm.py
  gradio_ui.py
  inspect_multiagent_run.py
  multi_llm_agent.py
  multiple_tools.py
  rag.py
  rag_using_chromadb.py
  sandboxed_execution.py
  structured_output_tool.py
  text_to_sql.py
src/  (21 files)
  smolagents/  (21 files)
    prompts/  (3 files)
      … 3 files under this directory
    __init__.py
    _function_type_hints_utils.py
    agent_types.py
    agents.py
    cli.py
    default_tools.py
    gradio_ui.py
    local_python_executor.py
    mcp_client.py
    memory.py
    models.py
    monitoring.py
    remote_executors.py
    serialization.py
    tool_validation.py
    tools.py
    utils.py
    vision_web_browser.py
tests/  (27 files)
  fixtures/  (2 files)
    agents.py
    tools.py
  utils/  (1 files)
    markers.py
  __init__.py
  conftest.py
  test_agents.py
  test_all_docs.py
  test_cli.py
  test_default_tools.py
  test_final_answer.py
  test_function_type_hints_utils.py
  test_gradio_ui.py
  test_import.py
  test_local_python_executor.py
  test_mcp_client.py
  test_memory.py
  test_models.py
  test_monitoring.py
  test_remote_executors.py
  test_search.py
  test_serialization.py
  test_telemetry.py
  test_tool_validation.py
  test_tools.py
  test_types.py
  test_utils.py
  test_vision_web_browser.py
.gitignore
.pre-commit-config.yaml
AGENTS.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
Makefile
README.md
SECURITY.md
e2b.toml
pyproject.toml
```

## Entry points

- [src/smolagents/cli.py](https://github.com/huggingface/smolagents/blob/96f33faaf028479119ec8d34507b47694cf14e34/src/smolagents/cli.py)
- [src/smolagents/vision_web_browser.py](https://github.com/huggingface/smolagents/blob/96f33faaf028479119ec8d34507b47694cf14e34/src/smolagents/vision_web_browser.py)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AmazonBedrockModel, ApiModel, AzureOpenAIModel, ChatMessage, ChatMessageStreamDelta, ChatMessageToolCal… |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: _escape_xpath_string, close_popups, go_back, initialize_agent, initialize_driver, intera… |
| External integrations | external | Observed | Groups 1 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: MCPClient. |
| smolagents package | library | Observed | Groups 14 file(s) under smolagents package (observed from repository paths and static analysis). Observed top-level classes: ActionOutput, ActionStep, AgentAudio, AgentError, AgentExecutionError, AgentGenerationError. O… |
| Tests | test | Observed | Groups 27 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH huggingface_hub.InferenceClient, PATCH openai.OpenAI, PATCH openai.OpenAI, PATCH huggingface_hub.InferenceClient… |

## Important files

- `.github/dependabot.yml` (config)
- `.github/workflows/build_documentation.yml` (ci)
- `.github/workflows/build_pr_documentation.yml` (ci)
- `.github/workflows/quality.yml` (ci)
- `.github/workflows/tests.yml` (ci)
- `.github/workflows/trufflehog.yml` (ci)
- `.github/workflows/upload_pr_documentation.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `docs/source/en/_toctree.yml` (config)
- `docs/source/es/_toctree.yml` (config)
- `docs/source/hi/_toctree.yml` (config)
- `docs/source/ko/_toctree.yml` (config)
- `docs/source/zh/_toctree.yml` (config)
- `e2b.toml` (config)
- `examples/async_agent/requirements.txt` (manifest)
- `examples/open_deep_research/requirements.txt` (manifest)
- `pyproject.toml` (manifest)
- `src/smolagents/prompts/code_agent.yaml` (config)
- `src/smolagents/prompts/structured_code_agent.yaml` (config)
- `src/smolagents/prompts/toolcalling_agent.yaml` (config)

## Top-level layout

- `docs` — 81 analysed file(s)
- `examples` — 34 analysed file(s)
- `tests` — 27 analysed file(s)
- `src` — 21 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `.github` — 10 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `96f33faaf028479119ec8d34507b47694cf14e34` is the revision these paths and observations refer to.
