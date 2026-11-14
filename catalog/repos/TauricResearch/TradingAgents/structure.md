# Project structure: TauricResearch/TradingAgents

**Analysed commit:** `9fa1196fffbcfd9de5146d2dd2869df84ab99838`

**Commit reference:** [9fa1196fffbcfd9de5146d2dd2869df84ab99838](https://github.com/TauricResearch/TradingAgents/commit/9fa1196fffbcfd9de5146d2dd2869df84ab99838)

**Tree at this commit:** [TauricResearch/TradingAgents@9fa1196fffbc](https://github.com/TauricResearch/TradingAgents/tree/9fa1196fffbcfd9de5146d2dd2869df84ab99838)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | TauricResearch/TradingAgents |
| Description | TradingAgents: Multi-Agents LLM Financial Trading Framework |
| Stars | 122565 |
| Forks | 23476 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `9fa1196fffbcfd9de5146d2dd2869df84ab99838` |
| Retrieved at | 2026-11-14T19:06:06.273132+00:00 |
| Files in this snapshot | 202 |

## Directory tree

```text
.github/  (6 files)
  ISSUE_TEMPLATE/  (4 files)
    bug-report.yml
    config.yml
    data-issue.yml
    feature-request.yml
  workflows/  (2 files)
    ci.yml
    release-assets.yml
cli/  (11 files)
  static/  (1 files)
    welcome.txt
  __init__.py
  display.py
  main.py
  models.py
  prefs.py
  prompts.py
  run.py
  selections.py
  stats_handler.py
  updates.py
tests/  (90 files)
  __init__.py
  conftest.py
  test_alpha_vantage_hardening.py
  test_analyst_execution.py
  test_anthropic_effort.py
  test_api_key_env.py
  test_azure_client.py
  test_backtest.py
  test_bedrock_provider.py
  test_cache_writes.py
  test_capabilities.py
  test_chatgpt_auth.py
  test_chatgpt_provider.py
  test_checkpoint_lifecycle.py
  test_checkpoint_resume.py
  test_cli_commands.py
  test_cli_config_precedence.py
  test_cli_display.py
  test_cli_env_skip.py
  test_cli_headless.py
  test_cli_memory_log.py
  test_cli_no_console.py
  test_cli_prefs.py
  test_cli_symbol_handling.py
  … 66 more files
tradingagents/  (84 files)
  agents/  (26 files)
    analysts/  (6 files)
      … 6 files under this directory
    managers/  (3 files)
      … 3 files under this directory
    researchers/  (3 files)
      … 3 files under this directory
    risk_mgmt/  (4 files)
      … 4 files under this directory
    trader/  (2 files)
      … 2 files under this directory
    __init__.py
    context.py
    post_screen.py
    rating.py
    schemas.py
    state.py
    structured.py
    tools.py
  assets/  (1 files)
    tauric-logo.svg
  dataflows/  (27 files)
    vendors/  (19 files)
      … 19 files under this directory
    __init__.py
    config.py
    date_window.py
    errors.py
    files.py
    net.py
    router.py
    symbols.py
  graph/  (7 files)
    __init__.py
    analyst_execution.py
    checkpointer.py
    conditional_logic.py
    propagation.py
    setup.py
    trading_graph.py
  llm_clients/  (13 files)
    __init__.py
    anthropic_client.py
    api_key_env.py
    azure_client.py
    base_client.py
    bedrock_client.py
    capabilities.py
    chatgpt_auth.py
    factory.py
    google_client.py
    model_catalog.py
    openai_client.py
    validators.py
  memory/  (4 files)
    __init__.py
    log.py
    reflection.py
    settlement.py
  __init__.py
  backtest.py
  default_config.py
  portfolio.py
  report_html.py
  reporting.py
.dockerignore
.env.example
.gitignore
CHANGELOG.md
Dockerfile
LICENSE
README.md
docker-compose.yml
main.py
pyproject.toml
requirements.txt
```

## Entry points

- [cli/main.py](https://github.com/TauricResearch/TradingAgents/blob/9fa1196fffbcfd9de5146d2dd2869df84ab99838/cli/main.py)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| cli package | library | Observed | Groups 7 file(s) under cli package (observed from repository paths and static analysis). Observed top-level classes: AnalystWallTimeTracker, MessageBuffer, StatsCallbackHandler. Observed top-level functions: _applies, _… |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: GraphSetup. Observed top-level functions: _analyst_graph, _merge, _tools_or_done, get… |
| Data layer | data | Observed | Groups 2 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AnalystType, AssetType, PortfolioDecision, PortfolioRating, ResearchPlan, SentimentBand. Observed top-l… |
| Application entry point | entrypoint | Observed | Groups 3 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Typer. Observed top-level functions: _announce_checkpoint_state, _build_run_co… |
| External integrations | external | Observed | Groups 6 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: AnthropicClient, AzureOpenAIClient, BaseLLMClient, BedrockClient, ChatGPTPlanChatOpenAI, Dee… |
| Tests | test | Observed | Groups 90 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH tradingagents.llm_clients.google_client.NormalizedChatGoogleGenerativeAI. Observed top-level classes: AnalystExe… |
| tradingagents package | library | Observed | Groups 74 file(s) under tradingagents package (observed from repository paths and static analysis). Observed top-level classes: AgentState, AlphaVantageNotConfiguredError, AlphaVantageRateLimitError, AnalystExecutionPla… |

## Important files

- `.dockerignore` (container)
- `.env.example` (config)
- `.github/ISSUE_TEMPLATE/bug-report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/data-issue.yml` (config)
- `.github/ISSUE_TEMPLATE/feature-request.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/release-assets.yml` (ci)
- `Dockerfile` (container)
- `docker-compose.yml` (container)
- `pyproject.toml` (manifest)
- `requirements.txt` (manifest)
- `tradingagents/graph/setup.py` (manifest)

## Top-level layout

- `tests` — 90 analysed file(s)
- `tradingagents` — 84 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `cli` — 11 analysed file(s)
- `.github` — 6 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `9fa1196fffbcfd9de5146d2dd2869df84ab99838` is the revision these paths and observations refer to.
