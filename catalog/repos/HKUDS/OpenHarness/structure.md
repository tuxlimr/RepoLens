# Project structure: HKUDS/OpenHarness

**Analysed commit:** `9b2efd795c6aa09f88b0c257d269a9e518da6ae7`

**Commit reference:** [9b2efd795c6aa09f88b0c257d269a9e518da6ae7](https://github.com/HKUDS/OpenHarness/commit/9b2efd795c6aa09f88b0c257d269a9e518da6ae7)

**Tree at this commit:** [HKUDS/OpenHarness@9b2efd795c6a](https://github.com/HKUDS/OpenHarness/tree/9b2efd795c6aa09f88b0c257d269a9e518da6ae7)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | HKUDS/OpenHarness |
| Description | "OpenHarness: Open Agent Harness with a Built-in Personal Agent--Ohmo!" |
| Stars | 16210 |
| Forks | 2612 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `9b2efd795c6aa09f88b0c257d269a9e518da6ae7` |
| Retrieved at | 2026-11-14T19:08:53.975227+00:00 |
| Files in this snapshot | 465 |

## Directory tree

```text
.claude/  (5 files)
  skills/  (5 files)
    harness-eval/  (3 files)
      … 3 files under this directory
    pr-merge/  (2 files)
      … 2 files under this directory
.github/  (8 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.yml
    config.yml
    feature_request.yml
  workflows/  (4 files)
    autopilot-pages.yml
    autopilot-run-next.yml
    autopilot-scan.yml
    ci.yml
  PULL_REQUEST_TEMPLATE.md
autopilot-dashboard/  (14 files)
  public/  (1 files)
    snapshot.json
  src/  (7 files)
    components/  (2 files)
      … 2 files under this directory
    App.tsx
    index.css
    main.tsx
    types.ts
    vite-env.d.ts
  .gitignore
  index.html
  package.json
  tsconfig.app.json
  tsconfig.json
  vite.config.ts
docs/  (5 files)
  autopilot/  (4 files)
    assets/  (1 files)
      … 1 files under this directory
    .nojekyll
    index.html
    snapshot.json
  SHOWCASE.md
frontend/  (29 files)
  terminal/  (29 files)
    src/  (27 files)
      … 27 files under this directory
    package.json
    tsconfig.json
ohmo/  (19 files)
  gateway/  (10 files)
    __init__.py
    bridge.py
    config.py
    group_tool.py
    models.py
    notify.py
    provider_commands.py
    router.py
    runtime.py
    service.py
  __init__.py
  __main__.py
  cli.py
  group_registry.py
  memory.py
  prompts.py
  runtime.py
  session_storage.py
  workspace.py
scripts/  (15 files)
  e2e_smoke.py
  install.ps1
  install.sh
  install_dev.sh
  local_system_scenarios.py
  migrate_memory.py
  react_tui_e2e.py
  sync_nanobot_channels.sh
  test_cli_flags.py
  test_docker_sandbox_e2e.py
  test_harness_features.py
  test_headless_rendering.py
  test_react_tui_redesign.py
  test_real_skills_plugins.py
  test_tui_interactions.py
src/  (240 files)
  openharness/  (239 files)
    api/  (10 files)
      … 10 files under this directory
    auth/  (5 files)
      … 5 files under this directory
    autopilot/  (3 files)
      … 3 files under this directory
    bridge/  (5 files)
      … 5 files under this directory
    channels/  (19 files)
      … 19 files under this directory
    commands/  (2 files)
      … 2 files under this directory
    config/  (4 files)
      … 4 files under this directory
    coordinator/  (3 files)
      … 3 files under this directory
    engine/  (6 files)
      … 6 files under this directory
    hooks/  (7 files)
      … 7 files under this directory
    keybindings/  (5 files)
      … 5 files under this directory
    mcp/  (4 files)
      … 4 files under this directory
    memory/  (13 files)
      … 13 files under this directory
    output_styles/  (2 files)
      … 2 files under this directory
    permissions/  (3 files)
      … 3 files under this directory
    personalization/  (4 files)
      … 4 files under this directory
    plugins/  (6 files)
      … 6 files under this directory
    prompts/  (5 files)
      … 5 files under this directory
    sandbox/  (7 files)
      … 7 files under this directory
    services/  (17 files)
      … 17 files under this directory
    skills/  (14 files)
      … 14 files under this directory
    state/  (3 files)
      … 3 files under this directory
    swarm/  (11 files)
      … 11 files under this directory
    tasks/  (6 files)
      … 6 files under this directory
    themes/  (4 files)
      … 4 files under this directory
    tools/  (44 files)
      … 44 files under this directory
    ui/  (11 files)
      … 11 files under this directory
    utils/  (6 files)
      … 6 files under this directory
    vim/  (2 files)
      … 2 files under this directory
    voice/  (4 files)
      … 4 files under this directory
    __init__.py
    __main__.py
    cli.py
    platforms.py
  __init__.py
tests/  (121 files)
  fixtures/  (1 files)
    fake_mcp_server.py
  test_api/  (6 files)
    __init__.py
    test_client.py
    test_codex_client.py
    test_copilot_auth.py
    test_copilot_client.py
    test_openai_client.py
  test_auth/  (2 files)
    test_external.py
    test_flows.py
  test_autopilot/  (2 files)
    __init__.py
    test_verification.py
  test_bridge/  (2 files)
    test_core.py
    test_session_flow.py
  test_channels/  (3 files)
    test_base.py
    test_feishu_security.py
    test_telegram_security.py
  test_commands/  (4 files)
    __init__.py
    test_cli.py
    test_command_flows.py
    test_registry.py
  test_config/  (5 files)
    __init__.py
    test_output_styles_loader.py
    test_paths.py
    test_schema.py
    test_settings.py
  test_coordinator/  (3 files)
    test_agent_definitions.py
    test_coordinator_mode.py
    test_registry.py
  test_engine/  (3 files)
    __init__.py
    test_messages.py
    test_query_engine.py
  test_entrypoints/  (2 files)
    test_config_cli.py
    test_no_stdlib_types_shadowing.py
  test_hooks/  (3 files)
    __init__.py
    test_executor.py
    test_priority.py
  test_install/  (1 files)
    test_windows_alias.py
  test_logging/  (1 files)
    test_format_strings.py
  test_mcp/  (5 files)
    __init__.py
    test_client_errors.py
    test_http_flow.py
    test_integration.py
    test_stdio_flow.py
  test_memory/  (3 files)
    __init__.py
    test_claude_runtime_memory.py
    test_memdir.py
  test_ohmo/  (6 files)
    test_cli.py
    test_gateway.py
    test_loading.py
    test_ohmo_session_storage.py
    test_prompts.py
    test_workspace.py
  test_permissions/  (2 files)
    __init__.py
    test_checker.py
  test_personalization/  (2 files)
    __init__.py
    test_extractor.py
  test_plugins/  (3 files)
    __init__.py
    test_lifecycle_flow.py
    test_loader.py
  test_prompts/  (4 files)
    __init__.py
    test_claudemd.py
    test_environment.py
    test_system_prompt.py
  test_sandbox/  (4 files)
    test_adapter.py
    test_docker_backend.py
    test_docker_image.py
    test_path_validator.py
  test_services/  (6 files)
    test_autodream.py
    test_autopilot.py
    test_compact.py
    test_cron.py
    test_cron_scheduler.py
    test_session_storage.py
  test_skills/  (1 files)
    test_loader.py
  test_swarm/  (12 files)
    __init__.py
    test_imports.py
    test_in_process.py
    test_lockfile.py
    test_mailbox.py
    test_permission_sync.py
    test_registry.py
    test_spawn_utils.py
    test_subprocess_backend.py
    test_team_lifecycle.py
    test_types.py
    test_worktree.py
  test_tasks/  (1 files)
    test_manager.py
  test_tools/  (11 files)
    __init__.py
    test_bash_tool.py
    test_core_tools.py
    test_grep_tool.py
    test_image_generation_tool.py
    test_image_to_text_tool.py
    test_integration_flows.py
    test_mcp_auth_tool.py
    test_mcp_tool.py
    test_task_tools.py
    test_web_fetch_tool.py
  test_ui/  (12 files)
    __init__.py
    test_coordinator_drain.py
    test_modes.py
    test_project_plugin_security.py
    test_react_backend.py
    test_react_launcher.py
    test_runtime_api_key.py
    test_runtime_close.py
    test_runtime_plan_mode.py
    test_runtime_plugin_tools.py
    test_textual_app.py
    test_tui_exit_sequence.py
  test_utils/  (4 files)
    test_fs.py
    test_helpers.py
    test_network_guard.py
    test_shell.py
  __init__.py
  conftest.py
  test_hooks_skills_plugins_real.py
  test_merged_prs_on_autoagent.py
  test_platforms.py
  test_real_large_tasks.py
  test_untested_features.py
.gitignore
CHANGELOG.md
CONTRIBUTING.md
LICENSE
README.md
README.zh-CN.md
RELEASE_NOTES_v0.1.8.md
RELEASE_NOTES_v0.1.9.md
pyproject.toml
```

## Entry points

- [src/openharness/__main__.py:5](https://github.com/HKUDS/OpenHarness/blob/9b2efd795c6aa09f88b0c257d269a9e518da6ae7/src/openharness/__main__.py#L5)
- [src/openharness/cli.py](https://github.com/HKUDS/OpenHarness/blob/9b2efd795c6aa09f88b0c257d269a9e518da6ae7/src/openharness/cli.py)
- [src/openharness/cli.py](https://github.com/HKUDS/OpenHarness/blob/9b2efd795c6aa09f88b0c257d269a9e518da6ae7/src/openharness/cli.py)
- [src/openharness/cli.py](https://github.com/HKUDS/OpenHarness/blob/9b2efd795c6aa09f88b0c257d269a9e518da6ae7/src/openharness/cli.py)
- [src/openharness/memory/migrate.py:136](https://github.com/HKUDS/OpenHarness/blob/9b2efd795c6aa09f88b0c257d269a9e518da6ae7/src/openharness/memory/migrate.py#L136)
- [src/openharness/services/cron_scheduler.py:594](https://github.com/HKUDS/OpenHarness/blob/9b2efd795c6aa09f88b0c257d269a9e518da6ae7/src/openharness/services/cron_scheduler.py#L594)
- [ohmo/__main__.py:6](https://github.com/HKUDS/OpenHarness/blob/9b2efd795c6aa09f88b0c257d269a9e518da6ae7/ohmo/__main__.py#L6)
- [ohmo/cli.py](https://github.com/HKUDS/OpenHarness/blob/9b2efd795c6aa09f88b0c257d269a9e518da6ae7/ohmo/cli.py)
- [scripts/e2e_smoke.py:806](https://github.com/HKUDS/OpenHarness/blob/9b2efd795c6aa09f88b0c257d269a9e518da6ae7/scripts/e2e_smoke.py#L806)
- [scripts/local_system_scenarios.py:247](https://github.com/HKUDS/OpenHarness/blob/9b2efd795c6aa09f88b0c257d269a9e518da6ae7/scripts/local_system_scenarios.py#L247)
- [scripts/migrate_memory.py:13](https://github.com/HKUDS/OpenHarness/blob/9b2efd795c6aa09f88b0c257d269a9e518da6ae7/scripts/migrate_memory.py#L13)
- [scripts/react_tui_e2e.py:160](https://github.com/HKUDS/OpenHarness/blob/9b2efd795c6aa09f88b0c257d269a9e518da6ae7/scripts/react_tui_e2e.py#L160)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 10 file(s) under api layer (observed from repository paths and static analysis). Observed top-level classes: AnthropicApiClient, ApiMessageCompleteEvent, ApiMessageRequest, ApiRetryEvent, ApiTextDeltaEvent, Authe… |
| autopilot-dashboard package | library | Observed | Groups 7 file(s) under autopilot-dashboard package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 14 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: BaseChannelConfig, ChannelConfigs, Config, DingTalkConfig, DiscordConfig, DockerSand… |
| Data layer | data | Observed | Groups 3 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AgentHookDefinition, CommandHookDefinition, GatewayConfig, GatewayState, HttpHookDefinition, PluginMani… |
| Application entry point | entrypoint | Observed | Groups 11 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Typer. Observed top-level classes: FakeApiClient, MigrationSummary, Scenario.… |
| External integrations | external | Observed | Groups 1 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: McpClientManager, McpServerNotConnectedError. |
| frontend package | library | Observed | Groups 27 file(s) under frontend package (observed from repository paths and static analysis). |
| __init__.py package | library | Observed | Groups 1 file(s) under __init__.py package (observed from repository paths and static analysis). |
| ohmo package | library | Observed | Groups 14 file(s) under ohmo package (observed from repository paths and static analysis). Observed top-level classes: GatewayStreamUpdate, ManagedGroupRecord, OhmoCreateFeishuGroupInput, OhmoCreateFeishuGroupTool, Ohmo… |
| openharness package | library | Observed | Groups 189 file(s) under openharness package (observed from repository paths and static analysis). Observed top-level classes: AgentDefinition, AgentTool, AgentToolInput, AggregatedHookResult, AllowedPath, ApiKeyFlow. O… |
| scripts package | library | Observed | Groups 3 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 18 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: AutoCompactState, CompactAttachment, CompactionResult, ExtractionRecord, ExtractionResult,… |
| Tests | test | Observed | Groups 128 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: CapturingApiClient, CoordinatorLoopApiClient, EmptyAssistantApiClient, FailingApiClient, FakeApiClient, Fa… |

## Important files

- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/workflows/autopilot-pages.yml` (ci)
- `.github/workflows/autopilot-run-next.yml` (ci)
- `.github/workflows/autopilot-scan.yml` (ci)
- `.github/workflows/ci.yml` (ci)
- `autopilot-dashboard/package.json` (manifest)
- `autopilot-dashboard/public/snapshot.json` (config)
- `autopilot-dashboard/tsconfig.app.json` (config)
- `autopilot-dashboard/tsconfig.json` (config)
- `docs/autopilot/snapshot.json` (config)
- `frontend/terminal/package.json` (manifest)
- `frontend/terminal/tsconfig.json` (config)
- `pyproject.toml` (manifest)
- `src/openharness/sandbox/Dockerfile` (container)

## Top-level layout

- `src` — 240 analysed file(s)
- `tests` — 121 analysed file(s)
- `frontend` — 29 analysed file(s)
- `ohmo` — 19 analysed file(s)
- `scripts` — 15 analysed file(s)
- `autopilot-dashboard` — 14 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `.github` — 8 analysed file(s)
- `.claude` — 5 analysed file(s)
- `docs` — 5 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `9b2efd795c6aa09f88b0c257d269a9e518da6ae7` is the revision these paths and observations refer to.
