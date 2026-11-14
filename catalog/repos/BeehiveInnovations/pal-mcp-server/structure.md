# Project structure: BeehiveInnovations/pal-mcp-server

**Analysed commit:** `7afc7c1cc96e23992c8f105f960132c657883bb1`

**Commit reference:** [7afc7c1cc96e23992c8f105f960132c657883bb1](https://github.com/BeehiveInnovations/pal-mcp-server/commit/7afc7c1cc96e23992c8f105f960132c657883bb1)

**Tree at this commit:** [BeehiveInnovations/pal-mcp-server@7afc7c1cc96e](https://github.com/BeehiveInnovations/pal-mcp-server/tree/7afc7c1cc96e23992c8f105f960132c657883bb1)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | BeehiveInnovations/pal-mcp-server |
| Description | The power of Claude Code / GeminiCLI / CodexCLI + [Gemini / OpenAI / OpenRouter / Azure / Grok / Ollama / Custom Model / All Of The Above] working as one. |
| Stars | 11838 |
| Forks | 1038 |
| Licence | Other |
| Language | Python |
| Default branch | main |
| Analysed commit | `7afc7c1cc96e23992c8f105f960132c657883bb1` |
| Retrieved at | 2026-11-14T19:10:22.056049+00:00 |
| Files in this snapshot | 361 |

## Directory tree

```text
.claude/  (2 files)
  commands/  (1 files)
    fix-github-issue.md
  settings.json
.github/  (12 files)
  ISSUE_TEMPLATE/  (5 files)
    bug_report.yml
    config.yml
    documentation.yml
    feature_request.yml
    tool_addition.yml
  workflows/  (5 files)
    docker-pr.yml
    docker-release.yml
    semantic-pr.yml
    semantic-release.yml
    test.yml
  FUNDING.yml
  pull_request_template.md
clink/  (14 files)
  agents/  (5 files)
    __init__.py
    base.py
    claude.py
    codex.py
    gemini.py
  parsers/  (5 files)
    __init__.py
    base.py
    claude.py
    codex.py
    gemini.py
  __init__.py
  constants.py
  models.py
  registry.py
conf/  (11 files)
  cli_clients/  (3 files)
    claude.json
    codex.json
    gemini.json
  __init__.py
  azure_models.json
  custom_models.json
  dial_models.json
  gemini_models.json
  openai_models.json
  openrouter_models.json
  xai_models.json
docker/  (6 files)
  scripts/  (5 files)
    build.ps1
    build.sh
    deploy.ps1
    deploy.sh
    healthcheck.py
  README.md
docs/  (40 files)
  tools/  (18 files)
    analyze.md
    apilookup.md
    challenge.md
    chat.md
    clink.md
    codereview.md
    consensus.md
    debug.md
    docgen.md
    listmodels.md
    planner.md
    precommit.md
    refactor.md
    secaudit.md
    testgen.md
    thinkdeep.md
    tracer.md
    version.md
  adding_providers.md
  adding_tools.md
  advanced-usage.md
  ai-collaboration.md
  ai_banter.md
  azure_openai.md
  configuration.md
  context-revival.md
  contributions.md
  custom_models.md
  docker-deployment.md
  gemini-setup.md
  getting-started.md
  index.md
  locale-configuration.md
  logging.md
  model_ranking.md
  name-change.md
  testing.md
  troubleshooting.md
  vcr-testing.md
  wsl-setup.md
examples/  (2 files)
  claude_config_macos.json
  claude_config_wsl.json
providers/  (26 files)
  registries/  (9 files)
    __init__.py
    azure.py
    base.py
    custom.py
    dial.py
    gemini.py
    openai.py
    openrouter.py
    xai.py
  shared/  (5 files)
    __init__.py
    model_capabilities.py
    model_response.py
    provider_type.py
    temperature.py
  __init__.py
  azure_openai.py
  base.py
  custom.py
  dial.py
  gemini.py
  openai.py
  openai_compatible.py
  openrouter.py
  registry.py
  registry_provider_mixin.py
  xai.py
scripts/  (1 files)
  sync_version.py
simulator_tests/  (38 files)
  __init__.py
  base_test.py
  conversation_base_test.py
  log_utils.py
  test_analyze_validation.py
  test_basic_conversation.py
  test_chat_simple_validation.py
  test_codereview_validation.py
  test_consensus_conversation.py
  test_consensus_three_models.py
  test_consensus_workflow_accurate.py
  test_content_validation.py
  test_conversation_chain_validation.py
  test_cross_tool_comprehensive.py
  test_cross_tool_continuation.py
  test_debug_certain_confidence.py
  test_debug_validation.py
  test_line_number_validation.py
  test_logs_validation.py
  test_model_thinking_config.py
  test_o3_model_selection.py
  test_o3_pro_expensive.py
  test_ollama_custom_url.py
  test_openrouter_fallback.py
  … 14 more files
systemprompts/  (19 files)
  clink/  (4 files)
    codex_codereviewer.txt
    default.txt
    default_codereviewer.txt
    default_planner.txt
  __init__.py
  analyze_prompt.py
  chat_prompt.py
  codereview_prompt.py
  consensus_prompt.py
  debug_prompt.py
  docgen_prompt.py
  generate_code_prompt.py
  planner_prompt.py
  precommit_prompt.py
  refactor_prompt.py
  secaudit_prompt.py
  testgen_prompt.py
  thinkdeep_prompt.py
  tracer_prompt.py
tests/  (118 files)
  gemini_cassettes/  (3 files)
    chat_codegen/  (1 files)
      … 1 files under this directory
    chat_cross/  (1 files)
      … 1 files under this directory
    consensus/  (1 files)
      … 1 files under this directory
  openai_cassettes/  (7 files)
    chat_cross_step2_gpt5_reminder.json
    chat_gpt5_continuation.json
    chat_gpt5_moon_distance.json
    consensus_step1_gpt51_for.json
    consensus_step1_gpt52_for.json
    consensus_step1_gpt5_for.json
    o3_pro_basic_math.json
  CASSETTE_MAINTENANCE.md
  __init__.py
  conftest.py
  http_transport_recorder.py
  mock_helpers.py
  pii_sanitizer.py
  sanitize_cassettes.py
  test_alias_target_restrictions.py
  test_auto_mode.py
  test_auto_mode_comprehensive.py
  test_auto_mode_custom_provider_only.py
  test_auto_mode_model_listing.py
  test_auto_mode_provider_selection.py
  test_auto_model_planner_fix.py
  test_azure_openai_provider.py
  test_buggy_behavior_prevention.py
  test_cassette_semantic_matching.py
  test_challenge.py
  test_chat_codegen_integration.py
  test_chat_cross_model_continuation.py
  test_chat_openai_integration.py
  test_chat_simple.py
  test_clink_claude_agent.py
  test_clink_claude_parser.py
  … 84 more files
tools/  (31 files)
  shared/  (5 files)
    __init__.py
    base_models.py
    base_tool.py
    exceptions.py
    schema_builders.py
  simple/  (2 files)
    __init__.py
    base.py
  workflow/  (4 files)
    __init__.py
    base.py
    schema_builders.py
    workflow_mixin.py
  __init__.py
  analyze.py
  apilookup.py
  challenge.py
  chat.py
  clink.py
  codereview.py
  consensus.py
  debug.py
  docgen.py
  listmodels.py
  models.py
  planner.py
  precommit.py
  refactor.py
  secaudit.py
  testgen.py
  thinkdeep.py
  tracer.py
  version.py
utils/  (12 files)
  __init__.py
  client_info.py
  conversation_memory.py
  env.py
  file_types.py
  file_utils.py
  image_utils.py
  model_context.py
  model_restrictions.py
  security_config.py
  storage_backend.py
  token_utils.py
.coveragerc
.dockerignore
.env.example
.gitattributes
.gitignore
.pre-commit-config.yaml
AGENTS.md
CHANGELOG.md
CLAUDE.md
Dockerfile
LICENSE
README.md
SECURITY.md
claude_config_example.json
code_quality_checks.ps1
code_quality_checks.sh
communication_simulator_test.py
config.py
docker-compose.yml
pal-mcp-server
pyproject.toml
pytest.ini
requirements-dev.txt
requirements.txt
… 5 more files
```

## Entry points

- [communication_simulator_test.py:555](https://github.com/BeehiveInnovations/pal-mcp-server/blob/7afc7c1cc96e23992c8f105f960132c657883bb1/communication_simulator_test.py#L555)
- [docker/scripts/healthcheck.py:114](https://github.com/BeehiveInnovations/pal-mcp-server/blob/7afc7c1cc96e23992c8f105f960132c657883bb1/docker/scripts/healthcheck.py#L114)
- [scripts/sync_version.py:37](https://github.com/BeehiveInnovations/pal-mcp-server/blob/7afc7c1cc96e23992c8f105f960132c657883bb1/scripts/sync_version.py#L37)
- [server.py](https://github.com/BeehiveInnovations/pal-mcp-server/blob/7afc7c1cc96e23992c8f105f960132c657883bb1/server.py)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| clink package | library | Observed | Groups 13 file(s) under clink package (observed from repository paths and static analysis). Observed top-level classes: AgentOutput, BaseCLIAgent, BaseParser, CLIAgentError, CLIInternalDefaults, ClaudeAgent. Observed to… |
| Configuration and deployment | config | Observed | Groups 19 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: _calculate_mcp_prompt_limit. |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 2 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: BranchingPoint, CLIClientConfig, CLIRoleConfig, CallPathStep, CodeTooLargeRequest, ContinuationOffer. |
| docker package | library | Observed | Groups 2 file(s) under docker package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 3 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: LocalTimeFormatter. Observed top-level functions: apply_tool_filter, check_environment, ch… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| providers package | library | Observed | Groups 26 file(s) under providers package (observed from repository paths and static analysis). Observed top-level classes: AzureModelRegistry, AzureOpenAIProvider, CapabilityModelRegistry, CustomEndpointModelRegistry,… |
| simulator_tests package | library | Observed | Groups 2 file(s) under simulator_tests package (observed from repository paths and static analysis). Observed top-level classes: LogUtils. |
| systemprompts package | library | Observed | Groups 15 file(s) under systemprompts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 155 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH config.DEFAULT_MODEL, PATCH providers.registry.ModelProviderRegistry.get_provider_for_model, PATCH server.DEFAU… |
| tools package | library | Observed | Groups 30 file(s) under tools package (observed from repository paths and static analysis). Observed top-level classes: AnalyzeTool, AnalyzeWorkflowRequest, BaseTool, BaseWorkflowMixin, BaseWorkflowRequest, CLinkRequest… |
| utils package | library | Observed | Groups 12 file(s) under utils package (observed from repository paths and static analysis). Observed top-level classes: ConversationTurn, InMemoryStorage, ModelContext, ModelRestrictionService, ThreadContext, TokenAlloc… |

## Important files

- `.claude/settings.json` (config)
- `.dockerignore` (container)
- `.env.example` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/documentation.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/ISSUE_TEMPLATE/tool_addition.yml` (config)
- `.github/workflows/docker-pr.yml` (ci)
- `.github/workflows/docker-release.yml` (ci)
- `.github/workflows/semantic-pr.yml` (ci)
- `.github/workflows/semantic-release.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `Dockerfile` (container)
- `claude_config_example.json` (config)
- `conf/azure_models.json` (config)
- `conf/cli_clients/claude.json` (config)
- `conf/cli_clients/codex.json` (config)
- `conf/cli_clients/gemini.json` (config)
- `conf/custom_models.json` (config)
- `conf/dial_models.json` (config)
- `conf/gemini_models.json` (config)
- `conf/openai_models.json` (config)
- `conf/openrouter_models.json` (config)
- `conf/xai_models.json` (config)
- `docker-compose.yml` (container)
- `examples/claude_config_macos.json` (config)
- `examples/claude_config_wsl.json` (config)
- `pyproject.toml` (manifest)
- `pytest.ini` (config)
- `requirements-dev.txt` (manifest)
- `requirements.txt` (manifest)

## Top-level layout

- `tests` — 118 analysed file(s)
- `docs` — 40 analysed file(s)
- `simulator_tests` — 38 analysed file(s)
- `tools` — 31 analysed file(s)
- `(root files)` — 29 analysed file(s)
- `providers` — 26 analysed file(s)
- `systemprompts` — 19 analysed file(s)
- `clink` — 14 analysed file(s)
- `.github` — 12 analysed file(s)
- `utils` — 12 analysed file(s)
- `conf` — 11 analysed file(s)
- `docker` — 6 analysed file(s)
- `.claude` — 2 analysed file(s)
- `examples` — 2 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `7afc7c1cc96e23992c8f105f960132c657883bb1` is the revision these paths and observations refer to.
