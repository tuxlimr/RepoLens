# Project structure: bytedance/trae-agent

**Analysed commit:** `e839e559ac61bdd0e057c375dd1dee391fee797d`

**Commit reference:** [e839e559ac61bdd0e057c375dd1dee391fee797d](https://github.com/bytedance/trae-agent/commit/e839e559ac61bdd0e057c375dd1dee391fee797d)

**Tree at this commit:** [bytedance/trae-agent@e839e559ac61](https://github.com/bytedance/trae-agent/tree/e839e559ac61bdd0e057c375dd1dee391fee797d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | bytedance/trae-agent |
| Description | Trae Agent is an LLM-based agent for general purpose software engineering tasks. |
| Stars | 12202 |
| Forks | 1375 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `e839e559ac61bdd0e057c375dd1dee391fee797d` |
| Retrieved at | 2026-11-14T19:10:13.081405+00:00 |
| Files in this snapshot | 105 |

## Directory tree

```text
.github/  (8 files)
  ISSUE_TEMPLATE/  (5 files)
    bug-report.yml
    config.yml
    feature-request.yml
    proposal.yml
    question.yml
  workflows/  (2 files)
    pre-commit.yml
    unit-test.yml
  pull_request_template.md
.vscode/  (1 files)
  launch.template.json
docs/  (4 files)
  TRAJECTORY_RECORDING.md
  legacy_config.md
  roadmap.md
  tools.md
evaluation/  (20 files)
  patch_selection/  (15 files)
    example/  (1 files)
      … 1 files under this directory
    trae_selector/  (11 files)
      … 11 files under this directory
    README.md
    analysis.py
    selector.py
  README.md
  __init__.py
  run_evaluation.py
  setup.sh
  utils.py
server/  (1 files)
  Readme.md
tests/  (11 files)
  agent/  (1 files)
    test_trae_agent.py
  tools/  (4 files)
    test_bash_tool.py
    test_edit_tool.py
    test_json_edit_tool.py
    test_mcp_tool.py
  utils/  (5 files)
    test_config.py
    test_google_client.py
    test_mcp_client.py
    test_ollama_client_utils.py
    test_openrouter_client_utils.py
  test_cli.py
trae_agent/  (50 files)
  agent/  (6 files)
    __init__.py
    agent.py
    agent_basics.py
    base_agent.py
    docker_manager.py
    trae_agent.py
  prompt/  (2 files)
    __init__.py
    agent_prompt.py
  tools/  (15 files)
    ckg/  (2 files)
      … 2 files under this directory
    __init__.py
    base.py
    bash_tool.py
    ckg_tool.py
    docker_tool_executor.py
    edit_tool.py
    edit_tool_cli.py
    json_edit_tool.py
    json_edit_tool_cli.py
    mcp_tool.py
    run.py
    sequential_thinking_tool.py
    task_done_tool.py
  utils/  (25 files)
    cli/  (6 files)
      … 6 files under this directory
    llm_clients/  (13 files)
      … 13 files under this directory
    config.py
    constants.py
    lake_view.py
    legacy_config.py
    mcp_client.py
    trajectory_recorder.py
  __init__.py
  cli.py
.gitignore
.pre-commit-config.yaml
.python-version
CONTRIBUTING.md
LICENSE
Makefile
README.md
pyproject.toml
trae_config.json.example
trae_config.yaml.example
```

## Entry points

- [evaluation/patch_selection/analysis.py:154](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/evaluation/patch_selection/analysis.py#L154)
- [evaluation/patch_selection/selector.py:101](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/evaluation/patch_selection/selector.py#L101)
- [evaluation/patch_selection/trae_selector/tools/tools/execute_bash.py:30](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/evaluation/patch_selection/trae_selector/tools/tools/execute_bash.py#L30)
- [evaluation/patch_selection/trae_selector/tools/tools/execute_str_replace_editor.py:54](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/evaluation/patch_selection/trae_selector/tools/tools/execute_str_replace_editor.py#L54)
- [evaluation/run_evaluation.py:473](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/evaluation/run_evaluation.py#L473)
- [trae_agent/cli.py](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/trae_agent/cli.py)
- [trae_agent/tools/edit_tool_cli.py:476](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/trae_agent/tools/edit_tool_cli.py#L476)
- [trae_agent/tools/json_edit_tool_cli.py:281](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/trae_agent/tools/json_edit_tool_cli.py#L281)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: AgentConfig, Config, ConfigError, LakeviewConfig, MCPServerConfig, ModelConfig. Obser… |
| Application entry point | entrypoint | Observed | Groups 10 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: BenchmarkEvaluation, JSONEditTool, TextEditorTool, Tool, ToolError, ToolExecResult. Obser… |
| evaluation package | library | Observed | Groups 11 file(s) under evaluation package (observed from repository paths and static analysis). Observed top-level classes: BashTool, BenchmarkConfig, CLIResult, CandidatePatch, EditTool, Sandbox. Observed top-level fu… |
| External integrations | external | Observed | Groups 10 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: AnthropicClient, AzureClient, AzureProvider, BaseLLMClient, DoubaoClient, DoubaoProvider. |
| Tests | test | Observed | Groups 11 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH subprocess.check_output, PATCH os.chdir, PATCH os.path.isdir, PATCH trae_agent.cli.resolve_config_file, PATCH tr… |
| trae_agent package | library | Observed | Groups 33 file(s) under trae_agent package (observed from repository paths and static analysis). Observed top-level classes: Agent, AgentError, AgentExecution, AgentState, AgentStep, AgentStepState. Observed top-level f… |

## Important files

- `.github/ISSUE_TEMPLATE/bug-report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature-request.yml` (config)
- `.github/ISSUE_TEMPLATE/proposal.yml` (config)
- `.github/ISSUE_TEMPLATE/question.yml` (config)
- `.github/workflows/pre-commit.yml` (ci)
- `.github/workflows/unit-test.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `.vscode/launch.template.json` (config)
- `pyproject.toml` (manifest)

## Top-level layout

- `trae_agent` — 50 analysed file(s)
- `evaluation` — 20 analysed file(s)
- `tests` — 11 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `.github` — 8 analysed file(s)
- `docs` — 4 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `server` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `e839e559ac61bdd0e057c375dd1dee391fee797d` is the revision these paths and observations refer to.
