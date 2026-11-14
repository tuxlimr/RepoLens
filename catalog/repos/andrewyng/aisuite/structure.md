# Project structure: andrewyng/aisuite

**Analysed commit:** `66c7890c2d68c2d67f41723bc848bb6713d82a9c`

**Commit reference:** [66c7890c2d68c2d67f41723bc848bb6713d82a9c](https://github.com/andrewyng/aisuite/commit/66c7890c2d68c2d67f41723bc848bb6713d82a9c)

**Tree at this commit:** [andrewyng/aisuite@66c7890c2d68](https://github.com/andrewyng/aisuite/tree/66c7890c2d68c2d67f41723bc848bb6713d82a9c)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | andrewyng/aisuite |
| Description | Simple, unified interface to multiple Generative AI providers  |
| Stars | 16400 |
| Forks | 1742 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `66c7890c2d68c2d67f41723bc848bb6713d82a9c` |
| Retrieved at | 2026-11-14T19:08:48.933265+00:00 |
| Files in this snapshot | 715 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (2 files)
    black.yml
    run_pytest.yml
aisuite/  (72 files)
  agents/  (12 files)
    __init__.py
    artifact_store.py
    artifacts.py
    context.py
    policies.py
    postgres_state_store.py
    runner.py
    state_store.py
    tools.py
    types.py
    utils.py
    viewer.py
  design-notes/  (1 files)
    asr-parameter-design-motivation.md
  framework/  (8 files)
    __init__.py
    asr_params.py
    chat_completion_chunk.py
    chat_completion_response.py
    choice.py
    message.py
    parameter_mapper.py
    provider_interface.py
  mcp/  (5 files)
    __init__.py
    client.py
    config.py
    schema_converter.py
    tool_wrapper.py
  providers/  (30 files)
    __init__.py
    anthropic_provider.py
    aws_provider.py
    azure_provider.py
    cerebras_provider.py
    cohere_provider.py
    crusoe_provider.py
    deepgram_provider.py
    deepseek_provider.py
    edenai_provider.py
    featherless_provider.py
    fireworks_provider.py
    gemini_provider.py
    google_provider.py
    groq_provider.py
    huggingface_provider.py
    inception_provider.py
    lmstudio_provider.py
    message_converter.py
    mistral_provider.py
    nebius_provider.py
    ollama_provider.py
    openai_provider.py
    openrouter_provider.py
    … 6 more files
  toolkits/  (4 files)
    __init__.py
    files.py
    git.py
    shell.py
  tracing/  (7 files)
    static/  (2 files)
      … 2 files under this directory
    __init__.py
    normalize.py
    sinks.py
    store.py
    viewer.py
  utils/  (2 files)
    tools.py
    utils.py
  __init__.py
  client.py
  provider.py
aisuite-js/  (79 files)
  examples/  (32 files)
    chat-app/  (23 files)
      … 23 files under this directory
    .env.example
    basic-usage.ts
    deepgram.ts
    groq.ts
    mistral.ts
    openai-asr.ts
    streaming.ts
    test-suite.ts
    tool-calling.ts
  src/  (35 files)
    asr-providers/  (5 files)
      … 5 files under this directory
    core/  (4 files)
      … 4 files under this directory
    providers/  (17 files)
      … 17 files under this directory
    types/  (6 files)
      … 6 files under this directory
    utils/  (1 files)
      … 1 files under this directory
    client.ts
    index.ts
  tests/  (8 files)
    providers/  (6 files)
      … 6 files under this directory
    utils/  (1 files)
      … 1 files under this directory
    client.test.ts
  README.md
  jest.config.ts
  package.json
  tsconfig.json
cli/  (10 files)
  py/  (10 files)
    aisuite-code-cli/  (10 files)
      … 10 files under this directory
docs/  (3 files)
  agents-quickstart.md
  chat-completions-quickstart.md
  openworker-quickstart.md
examples/  (29 files)
  agents/  (11 files)
    agent_api_quickstart.ipynb
    local_observability_demo.ipynb
    movie_buff_assistant.ipynb
    recipe_chef_assistant.ipynb
    simple_agent.py
    snake_game_generator.ipynb
    stock_dashboard.html
    stock_market_dashboard.html
    stock_market_mini_tracker.ipynb
    stock_market_tracker.ipynb
    world_weather_dashboard.ipynb
  chat-ui/  (4 files)
    .streamlit/  (1 files)
      … 1 files under this directory
    README.md
    chat.py
    config.yaml
  cli/  (2 files)
    create_demo_trace.py
    dev.py
  AISuiteDemo.ipynb
  DeepseekPost.ipynb
  QnA_with_pdf.ipynb
  aisuite_tool_abstraction.ipynb
  asr_example.ipynb
  client.ipynb
  llm_reasoning.ipynb
  mcp_config_dict_example.py
  mcp_http_example.py
  mcp_tools_example.ipynb
  simple_tool_calling.ipynb
  tool_calling_abstraction.ipynb
guides/  (23 files)
  README.md
  anthropic.md
  aws.md
  azure.md
  cerebras.md
  cohere.md
  crusoe.md
  deepseek.md
  edenai.md
  featherless.md
  gemini.md
  google.md
  groq.md
  huggingface.md
  lmstudio.md
  mistral.md
  nebius.md
  ollama.md
  openai.md
  sambanova.md
  tongyi.md
  watsonx.md
  xai.md
openworker-archive/  (402 files)
  abandoned-ux-mocks/  (3 files)
    index.html
    integrations.html
    session-view.html
  coworker/  (120 files)
    agents/  (7 files)
      … 7 files under this directory
    automation/  (5 files)
      … 5 files under this directory
    connectors/  (28 files)
      … 28 files under this directory
    mcp/  (5 files)
      … 5 files under this directory
    memory/  (4 files)
      … 4 files under this directory
    personas/  (5 files)
      … 5 files under this directory
    providers/  (10 files)
      … 10 files under this directory
    server/  (4 files)
      … 4 files under this directory
    skills/  (2 files)
      … 2 files under this directory
    testing/  (4 files)
      … 4 files under this directory
    tools/  (11 files)
      … 11 files under this directory
    tui/  (2 files)
      … 2 files under this directory
    web/  (4 files)
      … 4 files under this directory
    __init__.py
    agent.py
    attachments.py
    audit.py
    catalog.py
    cli.py
    cloud.py
    config.py
    connections.py
    conversations.py
    engine.py
    environment.py
    events.py
    inbox.py
    inbox_routing.py
    interactions.py
    mentions.py
    overrides.py
    pdf_support.py
    permissions.py
    project.py
    risk.py
    roots.py
    secrets.py
    … 5 more files
  docs/  (13 files)
    CONNECTORS-BATCH2-SPEC.md
    FAKE-SLACK-SPEC.md
    GDOCS-SHEETS-SPEC.md
    IMPLEMENTATION-LEDGER.md
    MESSAGING-AND-SESSIONS.md
    PERMISSIONS-AND-INBOX.md
    PERSONAS.md
    UI-REFRESH-KICKOFF.md
    UI-REFRESH-SPEC.md
    UI-REFRESH-VERIFICATION.md
    UX-DECISIONS.md
    config.example.toml
    email-connector-spec.md
  packaging/  (7 files)
    .gitignore
    build_dmg.sh
    build_windows.ps1
    coworker-server.spec
    make_update_manifest.py
    server_entry.py
    setup_dev_env.sh
  stt/  (3 files)
    src/  (1 files)
      … 1 files under this directory
    .gitignore
    Cargo.toml
  surfaces/  (171 files)
    gui/  (171 files)
      … 171 files under this directory
  tests/  (77 files)
    conftest.py
    test_accounts.py
    test_anthropic_provider.py
    test_attachments.py
    test_automation.py
    test_automation_create.py
    test_autotitle.py
    test_builtin_personas.py
    test_catalog.py
    test_cloud.py
    test_cloud_server.py
    test_code_tools.py
    test_config.py
    test_connections.py
    test_connector_registry.py
    test_connectors.py
    test_connectors_allowlist.py
    test_dm_routing.py
    test_durable_resume.py
    test_email_tools.py
    test_engine.py
    test_environment.py
    test_fake_slack.py
    test_gateway_inbox_reply.py
    … 53 more files
  ui-mocks/  (4 files)
    connectors-redesign.html
    redesign.html
    voice-input-composer-states.html
    voice-input-settings.html
  .gitignore
  README.md
  pyproject.toml
  release-workflow.yml
scripts/  (1 files)
  aisuite-code
tests/  (76 files)
  agents/  (17 files)
    __init__.py
    helpers.py
    test_agent.py
    test_agent_integration_flows.py
    test_artifact_store.py
    test_async_runner.py
    test_continuation.py
    test_openai_integration.py
    test_postgres_state_store.py
    test_runner.py
    test_state_store.py
    test_subagent_tool.py
    test_tool_metadata_policy.py
    test_tool_policy.py
    test_trace_output.py
    test_trace_sinks.py
    test_viewer.py
  cli/  (1 files)
    test_aisuite_code_cli.py
  client/  (6 files)
    __init__.py
    test_async_client.py
    test_client.py
    test_manual_tool_calling.py
    test_prerelease.py
    test_streaming.py
  examples/  (1 files)
    test_dev_cli.py
  framework/  (2 files)
    test_asr_models.py
    test_asr_params.py
  mcp/  (8 files)
    README.md
    __init__.py
    conftest.py
    test_client.py
    test_e2e.py
    test_http_llm_e2e.py
    test_http_transport.py
    test_llm_e2e.py
  providers/  (32 files)
    __init__.py
    test_anthropic_converter.py
    test_anthropic_images.py
    test_anthropic_streaming.py
    test_asr_parameter_passthrough.py
    test_async_provider.py
    test_aws_converter.py
    test_azure_provider.py
    test_cerebras_provider.py
    test_cohere_provider.py
    test_crusoe_provider.py
    test_deepgram_provider.py
    test_deepseek_provider.py
    test_edenai_provider.py
    test_featherless_provider.py
    test_gemini_provider.py
    test_google_converter.py
    test_google_provider.py
    test_groq_provider.py
    test_huggingface_provider.py
    test_inception_provider.py
    test_lmstudio_provider.py
    test_mistral_provider.py
    test_nebius_provider.py
    … 8 more files
  toolkits/  (3 files)
    test_files.py
    test_git.py
    test_shell.py
  utils/  (4 files)
    test_async_tools.py
    test_mcp_memory_integration.py
    test_tool_manager.py
    test_tools_mcp_schema.py
  __init__.py
  test_provider.py
viewer-ui/  (8 files)
  src/  (3 files)
    App.jsx
    index.css
    main.jsx
  index.html
  package.json
  postcss.config.js
  tailwind.config.js
  vite.config.js
.env.sample
.git-blame-ignore-revs
.gitignore
.pre-commit-config.yaml
.runtests.sh
CONTRIBUTING.md
LICENSE
README-alternative.md
README.md
pyproject.toml
```

## Entry points

- [aisuite/agents/viewer.py:3](https://github.com/andrewyng/aisuite/blob/66c7890c2d68c2d67f41723bc848bb6713d82a9c/aisuite/agents/viewer.py#L3)
- [aisuite/tracing/viewer.py:1677](https://github.com/andrewyng/aisuite/blob/66c7890c2d68c2d67f41723bc848bb6713d82a9c/aisuite/tracing/viewer.py#L1677)
- [cli/py/aisuite-code-cli/aisuite_code_cli/main.py:14](https://github.com/andrewyng/aisuite/blob/66c7890c2d68c2d67f41723bc848bb6713d82a9c/cli/py/aisuite-code-cli/aisuite_code_cli/main.py#L14)
- [openworker-archive/coworker/cli.py:69](https://github.com/andrewyng/aisuite/blob/66c7890c2d68c2d67f41723bc848bb6713d82a9c/openworker-archive/coworker/cli.py#L69)
- [openworker-archive/coworker/connectors/cli.py:109](https://github.com/andrewyng/aisuite/blob/66c7890c2d68c2d67f41723bc848bb6713d82a9c/openworker-archive/coworker/connectors/cli.py#L109)
- [openworker-archive/coworker/server/app.py:151](https://github.com/andrewyng/aisuite/blob/66c7890c2d68c2d67f41723bc848bb6713d82a9c/openworker-archive/coworker/server/app.py#L151)
- [openworker-archive/coworker/server/run.py:155](https://github.com/andrewyng/aisuite/blob/66c7890c2d68c2d67f41723bc848bb6713d82a9c/openworker-archive/coworker/server/run.py#L155)
- [openworker-archive/coworker/testing/fake_slack/__main__.py:68](https://github.com/andrewyng/aisuite/blob/66c7890c2d68c2d67f41723bc848bb6713d82a9c/openworker-archive/coworker/testing/fake_slack/__main__.py#L68)
- [openworker-archive/packaging/make_update_manifest.py:98](https://github.com/andrewyng/aisuite/blob/66c7890c2d68c2d67f41723bc848bb6713d82a9c/openworker-archive/packaging/make_update_manifest.py#L98)
- [openworker-archive/packaging/server_entry.py:9](https://github.com/andrewyng/aisuite/blob/66c7890c2d68c2d67f41723bc848bb6713d82a9c/openworker-archive/packaging/server_entry.py#L9)
- [aisuite-js/src/asr-providers/index.ts](https://github.com/andrewyng/aisuite/blob/66c7890c2d68c2d67f41723bc848bb6713d82a9c/aisuite-js/src/asr-providers/index.ts)
- [aisuite-js/src/index.ts](https://github.com/andrewyng/aisuite/blob/66c7890c2d68c2d67f41723bc848bb6713d82a9c/aisuite-js/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| aisuite package | library | Observed | Groups 64 file(s) under aisuite package (observed from repository paths and static analysis). Observed top-level classes: ASRError, ActiveRunContext, Agent, AllowAllToolPolicy, AllowToolsPolicy, Alternative. Observed to… |
| aisuite-js package | library | Observed | Groups 54 file(s) under aisuite-js package (observed from repository paths and static analysis). |
| cli package | library | Observed | Groups 4 file(s) under cli package (observed from repository paths and static analysis). Observed top-level classes: ApprovalController. Observed top-level functions: _approval_action, _approval_effect, _approval_previe… |
| Configuration and deployment | config | Observed | Groups 26 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: CliConfig, Config, ConnectorSettings, MCPConfig, MCPServerDef, TeamAuth. Observed to… |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: Schedule, ScheduledTask, TaskRun. Observed top-level functions: _human_time, _now, grant_entries, rule_… |
| Application entry point | entrypoint | Observed | Groups 13 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed top-level classes: ApprovalScreen, CodeCli, CoworkerApp, Fa… |
| External integrations | external | Observed | Groups 4 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: Audio, Chat, Client, Completions, MCPClient, MCPManager. Observed top-level functions: _resu… |
| openworker-archive package | library | Observed | Groups 250 file(s) under openworker-archive package (observed from repository paths and static analysis). Observed top-level classes: Agent, AgentContext, AnthropicProvider, ApprovalOutcome, AssistantTurn, AuditStore. O… |
| Service / domain layer | service | Observed | Groups 5 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 161 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH aisuite.provider.ProviderFactory.create_provider, PATCH aisuite.provider.ProviderFactory.create_provider, PATCH… |
| viewer-ui package | library | Observed | Groups 5 file(s) under viewer-ui package (observed from repository paths and static analysis). |

## Important files

- `.env.sample` (config)
- `.github/workflows/black.yml` (ci)
- `.github/workflows/run_pytest.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `aisuite-js/examples/.env.example` (config)
- `aisuite-js/examples/chat-app/package.json` (manifest)
- `aisuite-js/examples/chat-app/tsconfig.json` (config)
- `aisuite-js/examples/chat-app/tsconfig.node.json` (config)
- `aisuite-js/package.json` (manifest)
- `aisuite-js/tsconfig.json` (config)
- `cli/py/aisuite-code-cli/pyproject.toml` (manifest)
- `examples/chat-ui/.streamlit/config.toml` (config)
- `examples/chat-ui/config.yaml` (config)
- `openworker-archive/coworker/connectors/setup.py` (manifest)
- `openworker-archive/docs/config.example.toml` (config)
- `openworker-archive/pyproject.toml` (manifest)
- `openworker-archive/release-workflow.yml` (config)
- `openworker-archive/stt/Cargo.toml` (manifest)
- `openworker-archive/surfaces/gui/package.json` (manifest)
- `openworker-archive/surfaces/gui/src-tauri/Cargo.toml` (manifest)
- `openworker-archive/surfaces/gui/src-tauri/capabilities/default.json` (config)
- `openworker-archive/surfaces/gui/src-tauri/tauri.conf.json` (config)
- `openworker-archive/surfaces/gui/tsconfig.json` (config)
- `openworker-archive/surfaces/gui/tsconfig.node.json` (config)
- `pyproject.toml` (manifest)
- `viewer-ui/package.json` (manifest)

## Top-level layout

- `openworker-archive` — 402 analysed file(s)
- `aisuite-js` — 79 analysed file(s)
- `tests` — 76 analysed file(s)
- `aisuite` — 72 analysed file(s)
- `examples` — 29 analysed file(s)
- `guides` — 23 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `cli` — 10 analysed file(s)
- `viewer-ui` — 8 analysed file(s)
- `docs` — 3 analysed file(s)
- `.github` — 2 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 4 file(s) were skipped during inventory (4 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `66c7890c2d68c2d67f41723bc848bb6713d82a9c` is the revision these paths and observations refer to.
