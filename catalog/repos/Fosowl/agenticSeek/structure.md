# Project structure: Fosowl/agenticSeek

**Analysed commit:** `4f5f924c1eb326b4163d3bf942954dcc7dd7875b`

**Commit reference:** [4f5f924c1eb326b4163d3bf942954dcc7dd7875b](https://github.com/Fosowl/agenticSeek/commit/4f5f924c1eb326b4163d3bf942954dcc7dd7875b)

**Tree at this commit:** [Fosowl/agenticSeek@4f5f924c1eb3](https://github.com/Fosowl/agenticSeek/tree/4f5f924c1eb326b4163d3bf942954dcc7dd7875b)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Fosowl/agenticSeek |
| Description | Fully Local Manus AI. No APIs, No $200 monthly bills. Enjoy an autonomous agent that thinks, browses the web, and code for the sole cost of electricity. |
| Stars | 27658 |
| Forks | 3111 |
| Licence | GPL-3.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `4f5f924c1eb326b4163d3bf942954dcc7dd7875b` |
| Retrieved at | 2026-11-14T19:07:20.502675+00:00 |
| Files in this snapshot | 164 |

## Directory tree

```text
.github/  (3 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  FUNDING.yml
docker/  (1 files)
  fonts.local.conf
docs/  (2 files)
  CODE_OF_CONDUCT.md
  CONTRIBUTING.md
frontend/  (30 files)
  agentic-seek-front/  (27 files)
    public/  (3 files)
      … 3 files under this directory
    src/  (22 files)
      … 22 files under this directory
    mock-backend.js
    package.json
  .gitignore
  Dockerfile.frontend
  README.md
llm_router/  (2 files)
  config.json
  dl_safetensors.sh
llm_server/  (9 files)
  sources/  (5 files)
    cache.py
    decorator.py
    generator.py
    llamacpp_handler.py
    ollama_handler.py
  Dockerfile
  app.py
  install.sh
  requirements.txt
prompts/  (12 files)
  base/  (6 files)
    browser_agent.txt
    casual_agent.txt
    coder_agent.txt
    file_agent.txt
    mcp_agent.txt
    planner_agent.txt
  jarvis/  (6 files)
    browser_agent.txt
    casual_agent.txt
    coder_agent.txt
    file_agent.txt
    mcp_agent.txt
    planner_agent.txt
scripts/  (4 files)
  docker_start.sh
  linux_install.sh
  macos_install.sh
  windows_install.bat
searxng/  (4 files)
  docker-compose.yml
  limiter.toml
  settings.yml
  setup_searxng.sh
sources/  (43 files)
  agents/  (8 files)
    __init__.py
    agent.py
    browser_agent.py
    casual_agent.py
    code_agent.py
    file_agent.py
    mcp_agent.py
    planner_agent.py
  tools/  (14 files)
    BashInterpreter.py
    C_Interpreter.py
    GoInterpreter.py
    JavaInterpreter.py
    PyInterpreter.py
    __init__.py
    fileFinder.py
    flightSearch.py
    mcpFinder.py
    safety.py
    sandbox.py
    searxSearch.py
    tools.py
    webSearch.py
  web_scripts/  (2 files)
    find_inputs.js
    spoofing.js
  api_auth.py
  browser.py
  browser_identity.py
  browser_session_import.py
  crx_utils.py
  echo_filter.py
  errors.py
  files_api.py
  interaction.py
  language.py
  llm_provider.py
  logger.py
  memory.py
  router.py
  schemas.py
  speech_to_text.py
  text_to_speech.py
  utility.py
  workspace.py
tests/  (27 files)
  test_agent_regressions.py
  test_api_auth.py
  test_browser_agent_parsing.py
  test_browser_identity.py
  test_browser_profile.py
  test_browser_realism.py
  test_browser_session_import.py
  test_chromedriver_update.py
  test_crx_utils.py
  test_deepseek_provider.py
  test_errors.py
  test_files_api.py
  test_interpreters.py
  test_litellm_provider.py
  test_logger.py
  test_memory.py
  test_minimax_provider.py
  test_planner_agent_parsing.py
  test_provider.py
  test_safe_mode.py
  test_safety.py
  test_sandbox.py
  test_searx_search.py
  test_spoofing_static.py
  … 3 more files
.dockerignore
.env.example
.gitignore
.pre-commit-config.yaml
.python-version
Dockerfile.backend
LICENSE
README.md
README_CHS.md
README_CHT.md
README_ES.md
README_FR.md
README_JP.md
README_PTBR.md
README_TR.md
SECURITY.md
api.py
cli.py
config.ini
docker-compose.yml
install.bat
install.sh
pyproject.toml
requirements.txt
… 3 more files
```

## Entry points

- [api.py:51](https://github.com/Fosowl/agenticSeek/blob/4f5f924c1eb326b4163d3bf942954dcc7dd7875b/api.py#L51)
- [cli.py:79](https://github.com/Fosowl/agenticSeek/blob/4f5f924c1eb326b4163d3bf942954dcc7dd7875b/cli.py#L79)
- [llm_server/app.py:15](https://github.com/Fosowl/agenticSeek/blob/4f5f924c1eb326b4163d3bf942954dcc7dd7875b/llm_server/app.py#L15)
- [llm_server/sources/generator.py:65](https://github.com/Fosowl/agenticSeek/blob/4f5f924c1eb326b4163d3bf942954dcc7dd7875b/llm_server/sources/generator.py#L65)
- [llm_server/sources/ollama_handler.py:49](https://github.com/Fosowl/agenticSeek/blob/4f5f924c1eb326b4163d3bf942954dcc7dd7875b/llm_server/sources/ollama_handler.py#L49)
- [sources/agents/browser_agent.py:447](https://github.com/Fosowl/agenticSeek/blob/4f5f924c1eb326b4163d3bf942954dcc7dd7875b/sources/agents/browser_agent.py#L447)
- [sources/agents/casual_agent.py:34](https://github.com/Fosowl/agenticSeek/blob/4f5f924c1eb326b4163d3bf942954dcc7dd7875b/sources/agents/casual_agent.py#L34)
- [sources/agents/code_agent.py:88](https://github.com/Fosowl/agenticSeek/blob/4f5f924c1eb326b4163d3bf942954dcc7dd7875b/sources/agents/code_agent.py#L88)
- [sources/agents/file_agent.py:89](https://github.com/Fosowl/agenticSeek/blob/4f5f924c1eb326b4163d3bf942954dcc7dd7875b/sources/agents/file_agent.py#L89)
- [sources/agents/mcp_agent.py:77](https://github.com/Fosowl/agenticSeek/blob/4f5f924c1eb326b4163d3bf942954dcc7dd7875b/sources/agents/mcp_agent.py#L77)
- [sources/api_auth.py:183](https://github.com/Fosowl/agenticSeek/blob/4f5f924c1eb326b4163d3bf942954dcc7dd7875b/sources/api_auth.py#L183)
- [sources/browser.py:1318](https://github.com/Fosowl/agenticSeek/blob/4f5f924c1eb326b4163d3bf942954dcc7dd7875b/sources/browser.py#L1318)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 15 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: QueryRequest, QueryResponse, executorResult. |
| Application entry point | entrypoint | Observed | Groups 35 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Celery, FastAPI, Flask. Observed routes: GET /screenshot, GET /health, GET /i… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| frontend package | library | Observed | Groups 18 file(s) under frontend package (observed from repository paths and static analysis). |
| llm_router package | library | Observed | Groups 1 file(s) under llm_router package (observed from repository paths and static analysis). |
| llm_server package | library | Observed | Groups 4 file(s) under llm_server package (observed from repository paths and static analysis). Observed top-level classes: Cache, LlamacppLLM. Observed top-level functions: timer_decorator. |
| scripts package | library | Observed | Groups 3 file(s) under scripts package (observed from repository paths and static analysis). |
| searxng package | library | Observed | Groups 1 file(s) under searxng package (observed from repository paths and static analysis). |
| sources package | library | Observed | Groups 12 file(s) under sources package (observed from repository paths and static analysis). Observed top-level classes: Agent, AgenticSeekError, BrowserIdentity, Interaction, PlannerAgent, ProviderContext. Observed to… |
| Tests | test | Observed | Groups 27 file(s) under tests (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed routes: PATCH sources.browser.subprocess.run, PATCH sources.browser.subproces… |

## Important files

- `.dockerignore` (container)
- `.env.example` (config)
- `.github/FUNDING.yml` (config)
- `.pre-commit-config.yaml` (config)
- `Dockerfile.backend` (container)
- `config.ini` (config)
- `docker-compose.yml` (container)
- `frontend/Dockerfile.frontend` (container)
- `frontend/agentic-seek-front/package.json` (manifest)
- `frontend/agentic-seek-front/public/manifest.json` (config)
- `llm_router/config.json` (config)
- `llm_server/Dockerfile` (container)
- `llm_server/requirements.txt` (manifest)
- `pyproject.toml` (manifest)
- `requirements.txt` (manifest)
- `searxng/docker-compose.yml` (container)
- `searxng/limiter.toml` (config)
- `searxng/settings.yml` (config)
- `setup.py` (manifest)

## Top-level layout

- `sources` — 43 analysed file(s)
- `frontend` — 30 analysed file(s)
- `(root files)` — 27 analysed file(s)
- `tests` — 27 analysed file(s)
- `prompts` — 12 analysed file(s)
- `llm_server` — 9 analysed file(s)
- `scripts` — 4 analysed file(s)
- `searxng` — 4 analysed file(s)
- `.github` — 3 analysed file(s)
- `docs` — 2 analysed file(s)
- `llm_router` — 2 analysed file(s)
- `docker` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `4f5f924c1eb326b4163d3bf942954dcc7dd7875b` is the revision these paths and observations refer to.
