# Project structure: usestrix/strix

**Analysed commit:** `4719329d1c3eb0db796714397551945c514a2301`

**Commit reference:** [4719329d1c3eb0db796714397551945c514a2301](https://github.com/usestrix/strix/commit/4719329d1c3eb0db796714397551945c514a2301)

**Tree at this commit:** [usestrix/strix@4719329d1c3e](https://github.com/usestrix/strix/tree/4719329d1c3eb0db796714397551945c514a2301)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | usestrix/strix |
| Description | Open-source AI penetration testing tool to find and fix your app’s vulnerabilities. |
| Stars | 75546 |
| Forks | 8538 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `4719329d1c3eb0db796714397551945c514a2301` |
| Retrieved at | 2026-11-14T19:06:11.506219+00:00 |
| Files in this snapshot | 538 |

## Directory tree

```text
.github/  (8 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  actions/  (1 files)
    setup-python-env/  (1 files)
      … 1 files under this directory
  workflows/  (4 files)
    binary.yml
    build-release.yml
    ci.yml
    workflows.yml
  dependabot.yml
benchmarks/  (1 files)
  README.md
containers/  (3 files)
  opengrep-rules/  (1 files)
    github-owned-action-not-pinned-to-commit-sha.yaml
  Dockerfile
  docker-entrypoint.sh
docs/  (32 files)
  advanced/  (2 files)
    configuration.mdx
    skills.mdx
  cloud/  (2 files)
    cli.mdx
    overview.mdx
  integrations/  (4 files)
    ci-cd.mdx
    coding-agents.mdx
    github-actions.mdx
    mcp.mdx
  llm-providers/  (10 files)
    anthropic.mdx
    azure.mdx
    bedrock.mdx
    local.mdx
    novita.mdx
    openai.mdx
    openrouter.mdx
    overview.mdx
    vercel-ai-gateway.mdx
    vertex.mdx
  tools/  (5 files)
    browser.mdx
    overview.mdx
    proxy.mdx
    sandbox.mdx
    terminal.mdx
  usage/  (4 files)
    cli.mdx
    instructions.mdx
    scan-modes.mdx
    viewer.mdx
  README.md
  contributing.mdx
  docs.json
  index.mdx
  quickstart.mdx
scripts/  (4 files)
  build.sh
  docker.sh
  install.sh
  tui_sidecar_hook.py
skills/  (9 files)
  api-security-testing/  (1 files)
    SKILL.md
  application-security-testing/  (1 files)
    SKILL.md
  ci-security-scanning-with-strix/  (1 files)
    SKILL.md
  find-security-vulnerabilities-in-code/  (1 files)
    SKILL.md
  fix-security-vulnerabilities-with-strix/  (1 files)
    SKILL.md
  managed-pentesting-with-strix/  (1 files)
    SKILL.md
  owasp-top-10-testing/  (1 files)
    SKILL.md
  penetration-testing-with-strix/  (1 files)
    SKILL.md
  web-app-penetration-testing/  (1 files)
    SKILL.md
strix/  (355 files)
  agents/  (5 files)
    prompts/  (2 files)
      … 2 files under this directory
    __init__.py
    factory.py
    prompt.py
  config/  (8 files)
    __init__.py
    codex.py
    loader.py
    models.py
    settings.py
    tool_call_arguments.py
    tool_call_ids.py
    tool_call_limits.py
  core/  (8 files)
    __init__.py
    agents.py
    execution.py
    hooks.py
    inputs.py
    paths.py
    runner.py
    sessions.py
  interface/  (177 files)
    cloud/  (12 files)
      … 12 files under this directory
    tui/  (71 files)
      … 71 files under this directory
    viewer/  (78 files)
      … 78 files under this directory
    __init__.py
    auth_cli.py
    cli.py
    cli_args.py
    completions.py
    environment.py
    interactive.py
    main.py
    platform_cli.py
    platform_identity.py
    resume_picker.py
    scan_setup.py
    terminal_text.py
    update_check.py
    url_safety.py
    utils.py
  llm/  (5 files)
    __init__.py
    compaction.py
    context_budget.py
    request_log.py
    warmup.py
  report/  (9 files)
    __init__.py
    coverage.py
    dedupe.py
    pricing.py
    runs.py
    sarif.py
    state.py
    usage.py
    writer.py
  runtime/  (9 files)
    __init__.py
    backends.py
    caido_bootstrap.py
    caido_handle.py
    deferred_session.py
    docker_client.py
    docker_connection.py
    session_manager.py
    status.py
  skills/  (81 files)
    analysis/  (4 files)
      … 4 files under this directory
    cloud/  (5 files)
      … 5 files under this directory
    coordination/  (2 files)
      … 2 files under this directory
    custom/  (5 files)
      … 5 files under this directory
    frameworks/  (4 files)
      … 4 files under this directory
    protocols/  (2 files)
      … 2 files under this directory
    reconnaissance/  (3 files)
      … 3 files under this directory
    scan_modes/  (4 files)
      … 4 files under this directory
    technologies/  (7 files)
      … 7 files under this directory
    tooling/  (13 files)
      … 13 files under this directory
    vulnerabilities/  (30 files)
      … 30 files under this directory
    README.md
    __init__.py
  telemetry/  (6 files)
    README.md
    __init__.py
    _common.py
    logging.py
    posthog.py
    scarf.py
  tools/  (42 files)
    agent_browser/  (1 files)
      … 1 files under this directory
    agents_graph/  (2 files)
      … 2 files under this directory
    apply_patch/  (1 files)
      … 1 files under this directory
    coverage/  (2 files)
      … 2 files under this directory
    finish/  (2 files)
      … 2 files under this directory
    load_skill/  (2 files)
      … 2 files under this directory
    mcp/  (10 files)
      … 10 files under this directory
    notes/  (2 files)
      … 2 files under this directory
    proxy/  (3 files)
      … 3 files under this directory
    reporting/  (2 files)
      … 2 files under this directory
    shell/  (1 files)
      … 1 files under this directory
    thinking/  (2 files)
      … 2 files under this directory
    threat_model/  (2 files)
      … 2 files under this directory
    todo/  (2 files)
      … 2 files under this directory
    view_image/  (1 files)
      … 1 files under this directory
    wait_for_user/  (2 files)
      … 2 files under this directory
    web_search/  (2 files)
      … 2 files under this directory
    __init__.py
    nullish.py
    output_store.py
  utils/  (4 files)
    __init__.py
    api_spec.py
    resource_paths.py
    secret_files.py
  __init__.py
tests/  (117 files)
  __init__.py
  conftest.py
  test_agent_factory_shell.py
  test_agent_factory_tool_arguments.py
  test_agent_graph_coordination.py
  test_agent_tool_registration.py
  test_api_spec.py
  test_api_spec_targets.py
  test_auth_cli.py
  test_budget_pause_policy.py
  test_caido_bootstrap.py
  test_caido_handle.py
  test_cli_fail_on.py
  test_cli_mcp_config.py
  test_cli_resume_picker.py
  test_cli_target_list.py
  test_cloud_cli.py
  test_cloud_cli_runtime.py
  test_cloud_idempotency.py
  test_cloud_payment_proxy.py
  test_cloud_session.py
  test_cloud_source_upload.py
  test_cloud_wallet.py
  test_codex_auth.py
  … 93 more files
.gitignore
.pre-commit-config.yaml
AGENTS.md
CONTRIBUTING.md
LICENSE
Makefile
README.md
pyproject.toml
strix.spec
```

## Entry points

- [strix/interface/main.py](https://github.com/usestrix/strix/blob/4719329d1c3eb0db796714397551945c514a2301/strix/interface/main.py)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 14 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: BearerAuth, CodexAuthError, CodexContentGuardrailError, ContextSettings, DedupeSetti… |
| containers package | library | Observed | Groups 1 file(s) under containers package (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 2 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: StrixProvider, _CodexResponsesModel, _CredentialedLitellmProvider, _NonStreamingModel, _TurnGuardModel.… |
| Application entry point | entrypoint | Observed | Groups 5 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: TuiBackendServer, _CollectionState, _MessageTooLargeError, _ViewerState. Observed top-leve… |
| External integrations | external | Observed | Groups 3 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: BuiltMcpServer, ConnectedMcpServer, StrixDockerSandboxClient, StrixDockerSandboxSession, _Qu… |
| scripts package | library | Observed | Groups 4 file(s) under scripts package (observed from repository paths and static analysis). Observed top-level classes: CustomBuildHook. |
| Service / domain layer | service | Observed | Groups 8 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: AgentCoordinator, AgentRuntime, BudgetExceededError, BudgetPausedError, ProviderRefusalErro… |
| strix package | library | Observed | Groups 234 file(s) under strix package (observed from repository paths and static analysis). Observed top-level classes: CaidoBootstrapHandle, CloudArgumentParser, CloudError, CloudTransportError, Cmd, DeferredSandboxCl… |
| Tests | test | Observed | Groups 117 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: ErroringMCPServer, FakeMCPServer, FakeResponse, FakeSession, MalformedJsonResponse, MultiBlockErrorServer.… |

## Important files

- `.github/actions/setup-python-env/action.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/binary.yml` (ci)
- `.github/workflows/build-release.yml` (ci)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/workflows.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `containers/Dockerfile` (container)
- `containers/opengrep-rules/github-owned-action-not-pinned-to-commit-sha.yaml` (config)
- `docs/docs.json` (config)
- `pyproject.toml` (manifest)
- `strix/interface/tui/go.mod` (manifest)
- `strix/interface/viewer/frontend/package.json` (manifest)
- `strix/interface/viewer/frontend/tsconfig.json` (config)

## Top-level layout

- `strix` — 355 analysed file(s)
- `tests` — 117 analysed file(s)
- `docs` — 32 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `skills` — 9 analysed file(s)
- `.github` — 8 analysed file(s)
- `scripts` — 4 analysed file(s)
- `containers` — 3 analysed file(s)
- `benchmarks` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (1 x likely secret file excluded; 1 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `4719329d1c3eb0db796714397551945c514a2301` is the revision these paths and observations refer to.
