# Project structure: Alishahryar1/free-claude-code

**Analysed commit:** `9aafa6f314a1067627be395d2bd384f208ca16bd`

**Commit reference:** [9aafa6f314a1067627be395d2bd384f208ca16bd](https://github.com/Alishahryar1/free-claude-code/commit/9aafa6f314a1067627be395d2bd384f208ca16bd)

**Tree at this commit:** [Alishahryar1/free-claude-code@9aafa6f314a1](https://github.com/Alishahryar1/free-claude-code/tree/9aafa6f314a1067627be395d2bd384f208ca16bd)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Alishahryar1/free-claude-code |
| Description | Use Claude Code, Codex, Antigravity, VSCode, Pi, and OpenCode (and 6 other harnesses) for free (1.3B+ free tokens) from your terminal, app, IDE, or phone, and now from the browser with native browser sessions (multi-harness + multi-model) like OpenClaw (voice supported + ToS friendly) |
| Stars | 70164 |
| Forks | 10888 |
| Licence | Other |
| Language | Python |
| Default branch | main |
| Analysed commit | `9aafa6f314a1067627be395d2bd384f208ca16bd` |
| Retrieved at | 2026-11-14T19:06:16.009964+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.github/  (10 files)
  ISSUE_TEMPLATE/  (4 files)
    bug-report.yml
    config.yml
    feature-request.yml
    installation-problem.yml
  actions/  (1 files)
    ci-environment/  (1 files)
      … 1 files under this directory
  workflows/  (4 files)
    post-merge.yml
    tests.yml
    validate-bug-report-version.yml
    version-policy.yml
  dependabot.yml
assets/  (4 files)
  free-claude-code-wordmark-dark.svg
  free-claude-code-wordmark-light.svg
  how-it-works.mmd
  package-manager-uv.svg
e2e/  (30 files)
  __init__.py
  artifacts.py
  code_support.py
  conftest.py
  form_support.py
  provider_support.py
  server_shutdown.py
  test_admin_apply.py
  test_admin_assets.py
  test_admin_integrations.py
  test_admin_models.py
  test_admin_providers.py
  test_admin_status_independence.py
  test_admin_vscode_chat.py
  test_antigravity_integration.py
  test_api_key_lists.py
  test_claude_desktop_integration.py
  test_code_sessions.py
  test_connected_accounts.py
  test_custom_providers.py
  test_dsh_desktop_integration.py
  test_fallback_key_controls.py
  test_integration_notices.py
  test_jetbrains_acp_integration.py
  … 6 more files
scripts/  (17 files)
  macos/  (1 files)
    launcher.m
  update/  (2 files)
    fcc-update
    fcc-update.cmd
  build_macos_launcher.py
  check_version_policy.py
  ci.ps1
  ci.sh
  ci_shards.py
  ci_timings.py
  install-muse.ps1
  install.ps1
  install.sh
  publish_release.py
  uninstall-muse.ps1
  uninstall.ps1
  uninstall.sh
  validate_release.py
smoke/  (70 files)
  desktop/  (7 files)
    conftest.py
    identity_probe.py
    lifecycle_probe.py
    rebuild_sdist.py
    support.py
    test_macos_launcher.py
    test_macos_lifecycle.py
  installers/  (13 files)
    fixtures/  (4 files)
      … 4 files under this directory
    AGENTS.md
    _pty_runner.py
    conftest.py
    test_antigravity_installers.py
    test_installer_release.py
    test_muse_windows_lifecycle.py
    test_powershell_cache.py
    test_uninstallers.py
    test_update_wrapper.py
  lib/  (15 files)
    __init__.py
    child_process.py
    claude_cli_matrix.py
    config.py
    dsh_desktop.cjs
    dsh_provider.py
    e2e.py
    http.py
    local_providers.py
    outcomes.py
    report.py
    report_summary.py
    server.py
    server_runtime.py
    skips.py
  prereq/  (10 files)
    __init__.py
    test_api_prereq_live.py
    test_auth_prereq_live.py
    test_cli_prereq_live.py
    test_client_shapes_prereq_live.py
    test_local_provider_endpoints_prereq_live.py
    test_messaging_prereq_live.py
    test_provider_prereq_live.py
    test_tools_prereq_live.py
    test_voice_prereq_live.py
  product/  (20 files)
    __init__.py
    test_antigravity_cli_live.py
    test_api_product_live.py
    test_auth_product_live.py
    test_cli_package_product_live.py
    test_client_product_live.py
    test_codex_modes_product_live.py
    test_config_extensibility_product_live.py
    test_dsh_desktop_live.py
    test_dsh_native_live.py
    test_live_platform_product_live.py
    test_local_provider_product_live.py
    test_messaging_product_live.py
    test_model_fallback_product_live.py
    test_nvidia_nim_cli_product_live.py
    test_nvidia_nim_vision_product_live.py
    test_openrouter_free_cli_product_live.py
    test_provider_product_live.py
    test_runtime_ownership_product_live.py
    test_voice_product_live.py
  README.md
  __init__.py
  capabilities.py
  conftest.py
  features.py
src/  (514 files)
  free_claude_code/  (514 files)
    api/  (87 files)
      … 87 files under this directory
    application/  (21 files)
      … 21 files under this directory
    assets/  (1 files)
      … 1 files under this directory
    cli/  (39 files)
      … 39 files under this directory
    config/  (27 files)
      … 27 files under this directory
    core/  (101 files)
      … 101 files under this directory
    harnesses/  (20 files)
      … 20 files under this directory
    messaging/  (52 files)
      … 52 files under this directory
    providers/  (132 files)
      … 132 files under this directory
    runtime/  (31 files)
      … 31 files under this directory
    updater/  (2 files)
      … 2 files under this directory
    __init__.py
tests/  (149 files)
  api/  (92 files)
    model_fallback_support.py
    support.py
    test_admin.py
    test_admin_configuration_io.py
    test_antigravity_routes.py
    test_api.py
    test_api_handlers.py
    test_api_key_lists.py
    test_app_lifespan_and_errors.py
    test_app_version.py
    test_auth.py
    test_chat_accounting_wire.py
    test_chat_protocol_matrix.py
    test_chat_tool_identity_api.py
    test_classifier_provider_compatibility.py
    test_classifier_response.py
    test_claude_desktop_integration.py
    test_claude_onboarding.py
    test_code_sessions_routes.py
    test_codex_integration_routes.py
    test_continuation_overlap.py
    test_cooldown_cleanup.py
    test_delivered_stream_recovery.py
    test_dependencies.py
    … 68 more files
  application/  (12 files)
    test_code_sessions.py
    test_code_sessions_state.py
    test_connected_accounts.py
    test_execution.py
    test_model_catalog.py
    test_model_metadata.py
    test_reasoning.py
    test_request_conversion.py
    test_response_collection.py
    test_routing.py
    test_session_events.py
    test_web_tools.py
  cli/  (42 files)
    conftest.py
    test_agy_launcher.py
    test_aider_config.py
    test_aider_launcher.py
    test_autostart_logging.py
    test_catalog_http.py
    test_claude_launcher.py
    test_cli.py
    test_cli_manager_edge_cases.py
    test_cli_ownership.py
    test_cline_launcher.py
    test_codex_launcher.py
    test_codex_model_catalog.py
    test_config_restart_lifecycle.py
    test_desktop.py
    test_desktop_assets.py
    test_doctor.py
    test_dsh_config.py
    test_dsh_launcher.py
    test_entrypoints.py
    test_grok_launcher.py
    test_hermes_config.py
    test_hermes_launcher.py
    test_launcher_checks.py
    … 18 more files
  config/  (1 files)
    credential_support.py
  __init__.py
  code_sessions_support.py
.gitattributes
.gitignore
CONTRIBUTING.md
LICENSE
README.md
pyproject.toml
```

## Entry points

- [src/free_claude_code/api/app.py:53](https://github.com/Alishahryar1/free-claude-code/blob/9aafa6f314a1067627be395d2bd384f208ca16bd/src/free_claude_code/api/app.py#L53)
- [src/free_claude_code/cli/entrypoints.py](https://github.com/Alishahryar1/free-claude-code/blob/9aafa6f314a1067627be395d2bd384f208ca16bd/src/free_claude_code/cli/entrypoints.py)
- [src/free_claude_code/cli/entrypoints.py](https://github.com/Alishahryar1/free-claude-code/blob/9aafa6f314a1067627be395d2bd384f208ca16bd/src/free_claude_code/cli/entrypoints.py)
- [src/free_claude_code/cli/launchers/agy.py](https://github.com/Alishahryar1/free-claude-code/blob/9aafa6f314a1067627be395d2bd384f208ca16bd/src/free_claude_code/cli/launchers/agy.py)
- [src/free_claude_code/cli/launchers/aider.py](https://github.com/Alishahryar1/free-claude-code/blob/9aafa6f314a1067627be395d2bd384f208ca16bd/src/free_claude_code/cli/launchers/aider.py)
- [src/free_claude_code/cli/launchers/claude.py](https://github.com/Alishahryar1/free-claude-code/blob/9aafa6f314a1067627be395d2bd384f208ca16bd/src/free_claude_code/cli/launchers/claude.py)
- [src/free_claude_code/cli/launchers/cline.py](https://github.com/Alishahryar1/free-claude-code/blob/9aafa6f314a1067627be395d2bd384f208ca16bd/src/free_claude_code/cli/launchers/cline.py)
- [src/free_claude_code/cli/launchers/codex.py](https://github.com/Alishahryar1/free-claude-code/blob/9aafa6f314a1067627be395d2bd384f208ca16bd/src/free_claude_code/cli/launchers/codex.py)
- [src/free_claude_code/cli/launchers/dsh.py](https://github.com/Alishahryar1/free-claude-code/blob/9aafa6f314a1067627be395d2bd384f208ca16bd/src/free_claude_code/cli/launchers/dsh.py)
- [src/free_claude_code/cli/launchers/grok.py](https://github.com/Alishahryar1/free-claude-code/blob/9aafa6f314a1067627be395d2bd384f208ca16bd/src/free_claude_code/cli/launchers/grok.py)
- [src/free_claude_code/cli/launchers/hermes.py](https://github.com/Alishahryar1/free-claude-code/blob/9aafa6f314a1067627be395d2bd384f208ca16bd/src/free_claude_code/cli/launchers/hermes.py)
- [src/free_claude_code/cli/launchers/muse.py](https://github.com/Alishahryar1/free-claude-code/blob/9aafa6f314a1067627be395d2bd384f208ca16bd/src/free_claude_code/cli/launchers/muse.py)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 34 file(s) under api layer (observed from repository paths and static analysis). Observed routes: GET /admin, GET /admin/model_config, GET /admin/messaging, GET /admin/integrations, GET /admin/assets/{version}/{f… |
| Configuration and deployment | config | Observed | Groups 30 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: ChatModelConfig, ConfigConflictError, ConfigFieldSpec, ConfigMigrationResult, Config… |
| Data layer | data | Observed | Groups 9 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AdmissionToken, AnthropicModelRecord, CodeCatalog, CodeConflictError, CodeDetail, CodeError. Observed t… |
| e2e package | library | Observed | Groups 7 file(s) under e2e package (observed from repository paths and static analysis). Observed top-level classes: CodeControl, FolderPickerControl. Observed top-level functions: _task_snapshot, api_key_input, assert_… |
| Application entry point | entrypoint | Observed | Groups 13 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed top-level classes: GitHub, Publisher, Run, RunningServer, R… |
| External integrations | external | Observed | Groups 14 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: AlibabaCloudProvider, CloudflareChatBehavior, CloudflareProvider, DeepSeekChatBehavior, Dee… |
| free_claude_code package | library | Observed | Groups 271 file(s) under free_claude_code package (observed from repository paths and static analysis). Observed top-level classes: AdmissionRejection, AiderConfig, AnthropicChatStreamOutput, AnthropicMessagesTransport,… |
| scripts package | library | Observed | Groups 3 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 100 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: AmbiguousToolCallIdentityError, AnthropicImageSourceError, AnthropicSSEDecoder, Anthropic… |
| smoke package | library | Observed | Groups 21 file(s) under smoke package (observed from repository paths and static analysis). Observed top-level classes: CapabilityContract, ClaudeCliRun, CliMatrixOutcome, ClientProtocolDriver, ConversationDriver, Conve… |
| Tests | test | Observed | Groups 211 file(s) under tests (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed top-level classes: Answer, ApiTestRuntime, ApplicationErrorValidationProvide… |

## Important files

- `.github/ISSUE_TEMPLATE/bug-report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature-request.yml` (config)
- `.github/ISSUE_TEMPLATE/installation-problem.yml` (config)
- `.github/actions/ci-environment/action.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/post-merge.yml` (ci)
- `.github/workflows/tests.yml` (ci)
- `.github/workflows/validate-bug-report-version.yml` (ci)
- `.github/workflows/version-policy.yml` (ci)
- `pyproject.toml` (manifest)

## Top-level layout

- `src` — 514 analysed file(s)
- `tests` — 149 analysed file(s)
- `smoke` — 70 analysed file(s)
- `e2e` — 30 analysed file(s)
- `scripts` — 17 analysed file(s)
- `.github` — 10 analysed file(s)
- `(root files)` — 6 analysed file(s)
- `assets` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `9aafa6f314a1067627be395d2bd384f208ca16bd` is the revision these paths and observations refer to.
