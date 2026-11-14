# Project structure: FoundationAgents/OpenManus

**Analysed commit:** `3309bf4e416fb1c74b008f3e86494439a31bad53`

**Commit reference:** [3309bf4e416fb1c74b008f3e86494439a31bad53](https://github.com/FoundationAgents/OpenManus/commit/3309bf4e416fb1c74b008f3e86494439a31bad53)

**Tree at this commit:** [FoundationAgents/OpenManus@3309bf4e416f](https://github.com/FoundationAgents/OpenManus/tree/3309bf4e416fb1c74b008f3e86494439a31bad53)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | FoundationAgents/OpenManus |
| Description | No fortress, purely open ground.  OpenManus is Coming. |
| Stars | 58967 |
| Forks | 10249 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `3309bf4e416fb1c74b008f3e86494439a31bad53` |
| Retrieved at | 2026-11-14T19:06:23.032275+00:00 |
| Files in this snapshot | 140 |

## Directory tree

```text
.github/  (11 files)
  ISSUE_TEMPLATE/  (3 files)
    config.yml
    request_new_features.yaml
    show_me_the_bug.yaml
  workflows/  (6 files)
    build-package.yaml
    environment-corrupt-check.yaml
    pr-autodiff.yaml
    pre-commit.yaml
    stale.yaml
    top-issues.yaml
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
.vscode/  (2 files)
  extensions.json
  settings.json
app/  (81 files)
  agent/  (10 files)
    __init__.py
    base.py
    browser.py
    data_analysis.py
    manus.py
    mcp.py
    react.py
    sandbox_agent.py
    swe.py
    toolcall.py
  daytona/  (3 files)
    README.md
    sandbox.py
    tool_base.py
  flow/  (4 files)
    __init__.py
    base.py
    flow_factory.py
    planning.py
  mcp/  (2 files)
    __init__.py
    server.py
  prompt/  (8 files)
    __init__.py
    browser.py
    manus.py
    mcp.py
    planning.py
    swe.py
    toolcall.py
    visualization.py
  sandbox/  (6 files)
    core/  (4 files)
      … 4 files under this directory
    __init__.py
    client.py
  tool/  (38 files)
    chart_visualization/  (13 files)
      … 13 files under this directory
    sandbox/  (4 files)
      … 4 files under this directory
    search/  (6 files)
      … 6 files under this directory
    __init__.py
    ask_human.py
    base.py
    bash.py
    computer_use_tool.py
    crawl4ai.py
    create_chat_completion.py
    file_operators.py
    mcp.py
    planning.py
    python_execute.py
    str_replace_editor.py
    terminate.py
    tool_collection.py
    web_search.py
  utils/  (3 files)
    __init__.py
    files_utils.py
    logger.py
  __init__.py
  bedrock.py
  config.py
  exceptions.py
  llm.py
  logger.py
  schema.py
config/  (10 files)
  .gitignore
  config.example-daytona.toml
  config.example-model-anthropic.toml
  config.example-model-azure.toml
  config.example-model-google.toml
  config.example-model-jiekouai.toml
  config.example-model-ollama.toml
  config.example-model-ppio.toml
  config.example.toml
  mcp.example.json
examples/  (6 files)
  benchmarks/  (1 files)
    __init__.py
  use_case/  (5 files)
    japan-travel-plan/  (4 files)
      … 4 files under this directory
    readme.md
protocol/  (7 files)
  a2a/  (7 files)
    app/  (6 files)
      … 6 files under this directory
    __init__.py
tests/  (5 files)
  sandbox/  (4 files)
    test_client.py
    test_docker_terminal.py
    test_sandbox.py
    test_sandbox_manager.py
  tools/  (1 files)
    test_browser_use_mcp.py
workspace/  (1 files)
  example.txt
.gitattributes
.gitignore
.pre-commit-config.yaml
CODE_OF_CONDUCT.md
Dockerfile
LICENSE
README.md
README_ja.md
README_ko.md
README_zh.md
main.py
requirements.txt
run_flow.py
run_mcp.py
run_mcp_server.py
sandbox_main.py
setup.py
```

## Entry points

- [app/logger.py:32](https://github.com/FoundationAgents/OpenManus/blob/3309bf4e416fb1c74b008f3e86494439a31bad53/app/logger.py#L32)
- [app/mcp/server.py:170](https://github.com/FoundationAgents/OpenManus/blob/3309bf4e416fb1c74b008f3e86494439a31bad53/app/mcp/server.py#L170)
- [app/tool/bash.py:155](https://github.com/FoundationAgents/OpenManus/blob/3309bf4e416fb1c74b008f3e86494439a31bad53/app/tool/bash.py#L155)
- [app/tool/web_search.py:411](https://github.com/FoundationAgents/OpenManus/blob/3309bf4e416fb1c74b008f3e86494439a31bad53/app/tool/web_search.py#L411)
- [main.py](https://github.com/FoundationAgents/OpenManus/blob/3309bf4e416fb1c74b008f3e86494439a31bad53/main.py)
- [protocol/a2a/app/main.py:117](https://github.com/FoundationAgents/OpenManus/blob/3309bf4e416fb1c74b008f3e86494439a31bad53/protocol/a2a/app/main.py#L117)
- [run_flow.py:51](https://github.com/FoundationAgents/OpenManus/blob/3309bf4e416fb1c74b008f3e86494439a31bad53/run_flow.py#L51)
- [run_mcp.py:115](https://github.com/FoundationAgents/OpenManus/blob/3309bf4e416fb1c74b008f3e86494439a31bad53/run_mcp.py#L115)
- [run_mcp_server.py:6](https://github.com/FoundationAgents/OpenManus/blob/3309bf4e416fb1c74b008f3e86494439a31bad53/run_mcp_server.py#L6)
- [sandbox_main.py:35](https://github.com/FoundationAgents/OpenManus/blob/3309bf4e416fb1c74b008f3e86494439a31bad53/sandbox_main.py#L35)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| app package | library | Observed | Groups 62 file(s) under app package (observed from repository paths and static analysis). Observed top-level classes: AgentState, AskHuman, BaiduSearchEngine, BaseAgent, BaseFlow, BaseTool. Observed top-level functions:… |
| Configuration and deployment | config | Observed | Groups 15 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: AppConfig, BrowserSettings, Config, DaytonaSettings, LLMSettings, MCPServerConfig. O… |
| Application entry point | entrypoint | Observed | Groups 10 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Bash, MCPRunner, MCPServer, SearchMetadata, SearchResponse, SearchResult. Observed top-le… |
| External integrations | external | Observed | Groups 1 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: BaseSandboxClient, LocalSandboxClient, SandboxFileOperations. Observed top-level functions:… |
| protocol package | library | Observed | Groups 4 file(s) under protocol package (observed from repository paths and static analysis). Observed top-level classes: A2AManus, ManusExecutor, ResponseFormat. |
| Service / domain layer | service | Observed | Groups 4 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: AsyncDockerizedTerminal, DockerSandbox, DockerSession, SandboxError, SandboxManager, Sandbo… |
| Tests | test | Observed | Groups 7 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: FakeSession, ImageTool, TestAsyncDockerizedTerminal. Observed top-level functions: docker_client, docker_con… |

## Important files

- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/request_new_features.yaml` (config)
- `.github/ISSUE_TEMPLATE/show_me_the_bug.yaml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/build-package.yaml` (ci)
- `.github/workflows/environment-corrupt-check.yaml` (ci)
- `.github/workflows/pr-autodiff.yaml` (ci)
- `.github/workflows/pre-commit.yaml` (ci)
- `.github/workflows/stale.yaml` (ci)
- `.github/workflows/top-issues.yaml` (ci)
- `.pre-commit-config.yaml` (config)
- `.vscode/extensions.json` (config)
- `.vscode/settings.json` (config)
- `Dockerfile` (container)
- `app/tool/chart_visualization/package.json` (manifest)
- `app/tool/chart_visualization/tsconfig.json` (config)
- `config/config.example-daytona.toml` (config)
- `config/config.example-model-anthropic.toml` (config)
- `config/config.example-model-azure.toml` (config)
- `config/config.example-model-google.toml` (config)
- `config/config.example-model-jiekouai.toml` (config)
- `config/config.example-model-ollama.toml` (config)
- `config/config.example-model-ppio.toml` (config)
- `config/config.example.toml` (config)
- `config/mcp.example.json` (config)
- `requirements.txt` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `app` — 81 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `.github` — 11 analysed file(s)
- `config` — 10 analysed file(s)
- `protocol` — 7 analysed file(s)
- `examples` — 6 analysed file(s)
- `tests` — 5 analysed file(s)
- `.vscode` — 2 analysed file(s)
- `workspace` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `3309bf4e416fb1c74b008f3e86494439a31bad53` is the revision these paths and observations refer to.
