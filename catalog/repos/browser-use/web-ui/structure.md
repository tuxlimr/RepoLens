# Project structure: browser-use/web-ui

**Analysed commit:** `61962296c38a0d064e0ba02c827192b7a81d1819`

**Commit reference:** [61962296c38a0d064e0ba02c827192b7a81d1819](https://github.com/browser-use/web-ui/commit/61962296c38a0d064e0ba02c827192b7a81d1819)

**Tree at this commit:** [browser-use/web-ui@61962296c38a](https://github.com/browser-use/web-ui/tree/61962296c38a0d064e0ba02c827192b7a81d1819)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | browser-use/web-ui |
| Description | 🖥️ Run AI Agent in your browser. |
| Stars | 16653 |
| Forks | 2758 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `61962296c38a0d064e0ba02c827192b7a81d1819` |
| Retrieved at | 2026-11-14T19:08:44.594567+00:00 |
| Files in this snapshot | 40 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    build.yml
.vscode/  (1 files)
  settings.json
src/  (23 files)
  agent/  (3 files)
    browser_use/  (1 files)
      … 1 files under this directory
    deep_research/  (1 files)
      … 1 files under this directory
    __init__.py
  browser/  (3 files)
    __init__.py
    custom_browser.py
    custom_context.py
  controller/  (2 files)
    __init__.py
    custom_controller.py
  utils/  (5 files)
    __init__.py
    config.py
    llm_provider.py
    mcp_client.py
    utils.py
  webui/  (9 files)
    components/  (6 files)
      … 6 files under this directory
    __init__.py
    interface.py
    webui_manager.py
  __init__.py
tests/  (4 files)
  test_agents.py
  test_controller.py
  test_llm_api.py
  test_playwright.py
.dockerignore
.env.example
.gitignore
Dockerfile
LICENSE
README.md
SECURITY.md
docker-compose.yml
requirements.txt
supervisord.conf
webui.py
```

## Entry points

- [webui.py:18](https://github.com/browser-use/web-ui/blob/61962296c38a0d064e0ba02c827192b7a81d1819/webui.py#L18)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| agent package | library | Observed | Groups 3 file(s) under agent package (observed from repository paths and static analysis). Observed top-level classes: BrowserSearchInput, BrowserUseAgent, DeepResearchAgent, DeepResearchState, ResearchCategoryItem, Res… |
| browser package | library | Observed | Groups 3 file(s) under browser package (observed from repository paths and static analysis). Observed top-level classes: CustomBrowser, CustomBrowserContext. |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| controller package | library | Observed | Groups 2 file(s) under controller package (observed from repository paths and static analysis). Observed top-level classes: CustomController. |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: main. |
| External integrations | external | Observed | Groups 1 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level functions: create_tool_param_model, resolve_type, setup_mcp_client_and_tools. |
| __init__.py package | library | Observed | Groups 1 file(s) under __init__.py package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 4 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: LLMConfig. Observed top-level functions: create_message_content, get_env_value, test_azure_openai_model, tes… |
| utils package | library | Observed | Groups 3 file(s) under utils package (observed from repository paths and static analysis). Observed top-level classes: DeepSeekR1ChatOllama, DeepSeekR1ChatOpenAI. Observed top-level functions: encode_image, get_latest_f… |
| webui package | library | Observed | Groups 9 file(s) under webui package (observed from repository paths and static analysis). Observed top-level classes: WebuiManager. Observed top-level functions: _ask_assistant_callback, _format_agent_output, _get_conf… |

## Important files

- `.dockerignore` (container)
- `.env.example` (config)
- `.github/workflows/build.yml` (ci)
- `.vscode/settings.json` (config)
- `Dockerfile` (container)
- `docker-compose.yml` (container)
- `requirements.txt` (manifest)

## Top-level layout

- `src` — 23 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `tests` — 4 analysed file(s)
- `.github` — 1 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `61962296c38a0d064e0ba02c827192b7a81d1819` is the revision these paths and observations refer to.
