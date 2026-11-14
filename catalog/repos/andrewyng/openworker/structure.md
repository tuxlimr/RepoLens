# Project structure: andrewyng/openworker

**Analysed commit:** `ecb445490fc054d52b8ea610d97ba947f57033d2`

**Commit reference:** [ecb445490fc054d52b8ea610d97ba947f57033d2](https://github.com/andrewyng/openworker/commit/ecb445490fc054d52b8ea610d97ba947f57033d2)

**Tree at this commit:** [andrewyng/openworker@ecb445490fc0](https://github.com/andrewyng/openworker/tree/ecb445490fc054d52b8ea610d97ba947f57033d2)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | andrewyng/openworker |
| Description | Not provided |
| Stars | 19195 |
| Forks | 2736 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `ecb445490fc054d52b8ea610d97ba947f57033d2` |
| Retrieved at | 2026-11-14T19:08:18.546271+00:00 |
| Files in this snapshot | 798 |

## Directory tree

```text
.claude/  (1 files)
  launch.json
.github/  (6 files)
  workflows/  (6 files)
    ci.yml
    harness-packages.yml
    image.yml
    release.yml
    rust-sdk.yml
    sdk-skills.yml
coworker/  (297 files)
  agents/  (7 files)
    __init__.py
    base.py
    chat.py
    code.py
    cowork.py
    myhelper.py
    registry.py
  automation/  (5 files)
    __init__.py
    models.py
    scheduler.py
    store.py
    tools.py
  connectors/  (32 files)
    experimental/  (1 files)
      … 1 files under this directory
    __init__.py
    accounts.py
    adapters.py
    attribution.py
    base.py
    browser_automation.py
    catalog_copy.py
    chat_tools.py
    cli.py
    config.py
    descriptors.py
    email_tools.py
    fake.py
    gateway.py
    gcal_accounts.py
    github_installs.py
    github_relay.py
    github_send.py
    gmail_accounts.py
    hubspot_portals.py
    integration_tools.py
    machine_poll.py
    origin.py
    parked.py
    … 7 more files
  headless/  (6 files)
    __init__.py
    prices.yaml
    pricing.py
    runner.py
    terminal.py
    trajectory.py
  mcp/  (5 files)
    __init__.py
    client.py
    config.py
    oauth.py
    tools.py
  memory/  (5 files)
    __init__.py
    base.py
    settings.py
    sqlite_store.py
    tools.py
  observability/  (21 files)
    __init__.py
    calculator.py
    canonical.py
    capture.py
    decision.py
    engine_hooks.py
    export.py
    export_spans.py
    gaps.py
    ids.py
    model_names.py
    provider_view.py
    read_api.py
    recorder.py
    rollups.py
    scopes.py
    signals.py
    signals.yaml
    stamps.py
    store.py
    usage_api.py
  personas/  (34 files)
    builtin/  (30 files)
      … 30 files under this directory
    __init__.py
    loading.py
    manifest.py
    registry.py
  providers/  (27 files)
    __init__.py
    anthropic_provider.py
    base.py
    bedrock_provider.py
    capabilities.py
    codex_auth.py
    codex_provider.py
    effort.py
    errors.py
    gemini_provider.py
    llamacpp_models.json
    llamacpp_setup.py
    local_machine.py
    local_server.py
    matrix.py
    model_controls.json
    model_controls.py
    ollama_context.py
    ollama_facts.py
    openai_provider.py
    openai_responses.py
    openrouter_auth.py
    recommended.py
    recommended_models.json
    … 3 more files
  remote/  (12 files)
    __init__.py
    acceptor.py
    audit.py
    audit_export.py
    channel.py
    cloudproxy.py
    identity.py
    joiner.py
    provision.py
    registry.py
    service.py
    stores.py
  sandbox/  (43 files)
    providers/  (9 files)
      … 9 files under this directory
    runner/  (13 files)
      … 13 files under this directory
    __init__.py
    bundle.py
    client.py
    credentials.py
    executor.py
    inside.py
    launch.py
    netproxy.py
    network_profiles.py
    proxy.py
    registry.py
    selection.py
    settings.py
    setup_cmd.py
    setup_job.py
    stages.py
    toolchains.py
    transport.py
    windows_wfp.py
    winsec.py
    workspace.py
  server/  (4 files)
    __init__.py
    app.py
    run.py
    ws_guard.py
  skills/  (3 files)
    __init__.py
    base.py
    store.py
  teams/  (15 files)
    __init__.py
    artifacts.py
    attachments.py
    chat.py
    cli.py
    dialect.py
    journal.py
    mcp_server.py
    model.py
    proposals.py
    registry.py
    store.py
    summary.py
    tokens.py
    tools.py
  testing/  (4 files)
    fake_slack/  (3 files)
      … 3 files under this directory
    __init__.py
  tools/  (15 files)
    __init__.py
    agent_tasks.py
    ask.py
    connreq.py
    directories.py
    files.py
    git.py
    network.py
    plan.py
    registry.py
    search.py
    shell.py
    subagent.py
    todo.py
    toolreq.py
  tui/  (2 files)
    __init__.py
    app.py
  web/  (5 files)
    __init__.py
    fetch.py
    guard.py
    providers.py
    tool.py
  __init__.py
  _psl_private.py
  agent.py
  attachment_workspace.py
  attachments.py
  audit.py
  basedir.py
  catalog.py
  cli.py
  clock.py
  cloud.py
  compaction.py
  config.py
  connections.py
  conversations.py
  decision_reviewer.py
  environment.py
  events.py
  git_settings.py
  inbox.py
  inbox_routing.py
  interactions.py
  mentions.py
  model_config.py
  … 28 more files
deploy/  (159 files)
  aws/  (34 files)
    fixtures/  (2 files)
      … 2 files under this directory
    README.md
    boundary-qualify.mjs
    capture-result.mjs
    cleanup.cjs
    cleanup.test.mjs
    client.mjs
    cost-preflight.mjs
    diagnose-database.mjs
    experiment.mjs
    finalize-qualification.mjs
    guard.mjs
    images.mjs
    inventory.mjs
    kubernetes.mjs
    live-model.mjs
    live-qualify.mjs
    preflight.mjs
    probe-network.mjs
    qualification-lib.mjs
    qualification.test.mjs
    qualify-current.mjs
    qualify-live.mjs
    qualify-operations.mjs
    qualify-restore.mjs
    … 8 more files
  containers/  (2 files)
    Dockerfile
    Dockerfile.dockerignore
  helm/  (17 files)
    openworker/  (10 files)
      … 10 files under this directory
    README.md
    chart.test.mjs
    load-images.mjs
    local.mjs
    openshell-local.yaml
    qualify.mjs
    version-drill.mjs
  local/  (7 files)
    README.md
    kind.yaml
    openshell-values.yaml
    probe-network.py
    runner.Dockerfile
    sandbox-policy.yaml
    versions.env
  recovery/  (4 files)
    README.md
    backup.mjs
    backup.test.mjs
    local.mjs
  reference/  (35 files)
    dashboards/  (2 files)
      … 2 files under this directory
    DRAINING.md
    Dockerfile.artifact-probe
    Dockerfile.artifact-probe.dockerignore
    Dockerfile.observability
    Dockerfile.observability.dockerignore
    LANGFUSE-LOCAL.md
    OPERATIONS.md
    README.md
    SIZING.md
    UPGRADES.md
    check-recorded-langfuse.mjs
    compose.yaml
    connection.example.json
    export-contract.mjs
    export-qualification-images.json
    langfuse-kubernetes-local.mjs
    observability-entrypoint.sh
    observability-local-views.mjs
    operations.mjs
    operations.test.mjs
    qualify-artifact-storage.mjs
    qualify-coding-limits.mjs
    qualify-coding-runner.mjs
    qualify-coding-service.mjs
    … 9 more files
  resilience/  (8 files)
    Dockerfile
    Dockerfile.dockerignore
    cluster.mjs
    contract.mjs
    contract.test.mjs
    postgres-workers.mjs
    prepare-local.mjs
    run.mjs
  service/  (51 files)
    bundle/  (2 files)
      … 2 files under this directory
    chart/  (8 files)
      … 8 files under this directory
    coding-bundle/  (2 files)
      … 2 files under this directory
    examples/  (4 files)
      … 4 files under this directory
    guard/  (2 files)
      … 2 files under this directory
    platform/  (2 files)
      … 2 files under this directory
    up/  (5 files)
      … 5 files under this directory
    Dockerfile
    Dockerfile.coding-runner
    Dockerfile.coding-service
    Dockerfile.coding-service.dockerignore
    Dockerfile.dockerignore
    README.md
    chart.test.mjs
    compose.yaml
    connection.example.json
    entrypoint.sh
    install.sh
    kubernetes-local.mjs
    local-drain.mjs
    local-drain.test.mjs
    local-values.mjs
    local-values.test.mjs
    local-views.mjs
    prepare-local-install.mjs
    probe-local-network.mjs
    proxy.test.mjs
    qualify-kubernetes.mjs
    qualify-local-install.mjs
    qualify-ui-kubernetes.mjs
    qualify.mjs
    … 2 more files
  teams/  (1 files)
    cluster.mjs
docs/  (65 files)
  assets/  (1 files)
    first-task.svg
  desktop/  (25 files)
    guides/  (22 files)
      … 22 files under this directory
    samples/  (3 files)
      … 3 files under this directory
  harness/  (27 files)
    assets/  (1 files)
      … 1 files under this directory
    guides/  (26 files)
      … 26 files under this directory
  approval-guidance.md
  config.example.toml
  desktop-models.md
  headless.md
  local-servers.md
  macos-sandbox.md
  model-settings.md
  openshell-inside.md
  openshell.md
  remote-machines.md
  team-board-evidence.md
  windows-sandbox.md
docs-site/  (41 files)
  scripts/  (12 files)
    code-tabs.mjs
    code-tabs.test.mjs
    hosting.test.mjs
    prepare-hosting.mjs
    prepare.mjs
    product.test.mjs
    render-guide.test.mjs
    site.test.mjs
    source-examples.mjs
    source-examples.test.mjs
    source-tree.test.mjs
    verify-built.py
  src/  (21 files)
    components/  (1 files)
      … 1 files under this directory
    layouts/  (2 files)
      … 2 files under this directory
    lib/  (5 files)
      … 5 files under this directory
    pages/  (3 files)
      … 3 files under this directory
    scripts/  (6 files)
      … 6 files under this directory
    styles/  (3 files)
      … 3 files under this directory
    content.config.ts
  .gitignore
  DESIGN-PREVIEWS.md
  README.md
  astro.config.mjs
  desktop-pages.json
  package.json
  pages.json
  product.mjs
harness/  (222 files)
  artifacts/  (10 files)
    examples/  (1 files)
      … 1 files under this directory
    src/  (4 files)
      … 4 files under this directory
    tests/  (2 files)
      … 2 files under this directory
    Cargo.toml
    LICENSE
    README.md
  compliance/  (5 files)
    src/  (2 files)
      … 2 files under this directory
    Cargo.toml
    LICENSE
    README.md
  console/  (7 files)
    public/  (3 files)
      … 3 files under this directory
    README.md
    browser-check.mjs
    server.mjs
    server.test.mjs
  desktop-starters/  (31 files)
    templates/  (23 files)
      … 23 files under this directory
    README.md
    create.mjs
    live-acceptance.mjs
    package.json
    qualify-electron.mjs
    recovery.test.mjs
    tauri-test-model.mjs
    test.mjs
  examples/  (165 files)
    arcade/  (150 files)
      … 150 files under this directory
    assistant/  (2 files)
      … 2 files under this directory
    computer-tools/  (4 files)
      … 4 files under this directory
    device-tools/  (3 files)
      … 3 files under this directory
    mixed/  (2 files)
      … 2 files under this directory
    direct-client.mjs
    grants-client.mjs
    long-session-client.mjs
    multi-client.mjs
  .gitignore
  Cargo.toml
  README.md
  WINDOWS.md
.dockerignore
.gitattributes
.gitignore
CONTRIBUTING.md
LICENSE
README.md
SECURITY.md
```

## Entry points

- [coworker/cli.py:163](https://github.com/andrewyng/openworker/blob/ecb445490fc054d52b8ea610d97ba947f57033d2/coworker/cli.py#L163)
- [coworker/connectors/cli.py:109](https://github.com/andrewyng/openworker/blob/ecb445490fc054d52b8ea610d97ba947f57033d2/coworker/connectors/cli.py#L109)
- [coworker/headless/runner.py:1606](https://github.com/andrewyng/openworker/blob/ecb445490fc054d52b8ea610d97ba947f57033d2/coworker/headless/runner.py#L1606)
- [coworker/remote/service.py:95](https://github.com/andrewyng/openworker/blob/ecb445490fc054d52b8ea610d97ba947f57033d2/coworker/remote/service.py#L95)
- [coworker/sandbox/runner/__main__.py:65](https://github.com/andrewyng/openworker/blob/ecb445490fc054d52b8ea610d97ba947f57033d2/coworker/sandbox/runner/__main__.py#L65)
- [coworker/sandbox/windows_wfp.py:401](https://github.com/andrewyng/openworker/blob/ecb445490fc054d52b8ea610d97ba947f57033d2/coworker/sandbox/windows_wfp.py#L401)
- [coworker/server/app.py:236](https://github.com/andrewyng/openworker/blob/ecb445490fc054d52b8ea610d97ba947f57033d2/coworker/server/app.py#L236)
- [coworker/server/run.py:250](https://github.com/andrewyng/openworker/blob/ecb445490fc054d52b8ea610d97ba947f57033d2/coworker/server/run.py#L250)
- [coworker/teams/cli.py:517](https://github.com/andrewyng/openworker/blob/ecb445490fc054d52b8ea610d97ba947f57033d2/coworker/teams/cli.py#L517)
- [coworker/testing/fake_slack/__main__.py:68](https://github.com/andrewyng/openworker/blob/ecb445490fc054d52b8ea610d97ba947f57033d2/coworker/testing/fake_slack/__main__.py#L68)
- [deploy/service/up/package.py:69](https://github.com/andrewyng/openworker/blob/ecb445490fc054d52b8ea610d97ba947f57033d2/deploy/service/up/package.py#L69)
- [harness/desktop-starters/create.mjs](https://github.com/andrewyng/openworker/blob/ecb445490fc054d52b8ea610d97ba947f57033d2/harness/desktop-starters/create.mjs)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 92 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: Config, ConnectorSettings, MCPServerDef, MemorySettingsStore, TeamAuth. Observed top… |
| coworker package | library | Observed | Groups 237 file(s) under coworker package (observed from repository paths and static analysis). Observed top-level classes: Agent, AgentContext, AgentTask, AgentTaskRegistry, AgentTaskStore, AllowListProxy. Observed top… |
| Data layer | data | Observed | Groups 2 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: Actor, AuthorityError, BoardError, BoardNotFoundError, ChainError, ItemState. Observed top-level functi… |
| deploy package | library | Observed | Groups 67 file(s) under deploy package (observed from repository paths and static analysis). Observed top-level functions: apply, kubectl, observe, policy. |
| docs-site package | library | Observed | Groups 26 file(s) under docs-site package (observed from repository paths and static analysis). Observed top-level classes: Page. |
| Application entry point | entrypoint | Observed | Groups 13 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed top-level classes: Answers, ApprovalScreen, CoworkerApp, En… |
| External integrations | external | Observed | Groups 5 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: MCPManager, RelayHub, RelayTransport, RunnerClient, SlackRelayAdapter, _Conn. Observed top-l… |
| harness package | library | Observed | Groups 102 file(s) under harness package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 21 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 35 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.claude/launch.json` (config)
- `.dockerignore` (container)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/harness-packages.yml` (ci)
- `.github/workflows/image.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/rust-sdk.yml` (ci)
- `.github/workflows/sdk-skills.yml` (ci)
- `coworker/connectors/setup.py` (manifest)
- `coworker/headless/prices.yaml` (config)
- `coworker/observability/signals.yaml` (config)
- `coworker/providers/llamacpp_models.json` (config)
- `coworker/providers/model_controls.json` (config)
- `coworker/providers/recommended_models.json` (config)
- `deploy/containers/Dockerfile` (container)
- `deploy/containers/Dockerfile.dockerignore` (container)
- `deploy/helm/openshell-local.yaml` (config)
- `deploy/helm/openworker/Chart.yaml` (config)
- `deploy/helm/openworker/templates/config.yaml` (config)
- `deploy/helm/openworker/templates/network.yaml` (config)
- `deploy/helm/openworker/templates/service.yaml` (config)
- `deploy/helm/openworker/templates/task-desk.yaml` (config)
- `deploy/helm/openworker/templates/workloads.yaml` (config)
- `deploy/helm/openworker/values.schema.json` (config)
- `deploy/helm/openworker/values.yaml` (config)
- `deploy/local/kind.yaml` (config)
- `deploy/local/openshell-values.yaml` (config)
- `deploy/local/sandbox-policy.yaml` (config)
- `deploy/reference/Dockerfile.artifact-probe` (container)
- `deploy/reference/Dockerfile.artifact-probe.dockerignore` (container)
- `deploy/reference/Dockerfile.observability` (container)
- `deploy/reference/Dockerfile.observability.dockerignore` (container)
- `deploy/reference/compose.yaml` (container)
- `deploy/reference/connection.example.json` (config)
- `deploy/reference/dashboards/dashboard.json` (config)
- `deploy/reference/dashboards/provider.yaml` (config)
- `deploy/reference/export-qualification-images.json` (config)
- `deploy/resilience/Dockerfile` (container)
- `deploy/resilience/Dockerfile.dockerignore` (container)
- `deploy/service/Dockerfile` (container)
- `deploy/service/Dockerfile.coding-runner` (container)
- `deploy/service/Dockerfile.coding-service` (container)
- `deploy/service/Dockerfile.coding-service.dockerignore` (container)
- `deploy/service/Dockerfile.dockerignore` (container)
- `deploy/service/bundle/tools.json` (config)
- `deploy/service/chart/Chart.yaml` (config)
- `deploy/service/chart/templates/bootstrap.yaml` (config)
- `deploy/service/chart/templates/config.yaml` (config)
- `deploy/service/chart/templates/management-ui.yaml` (config)
- `deploy/service/chart/templates/rbac.yaml` (config)
- `deploy/service/chart/templates/workloads.yaml` (config)
- `deploy/service/chart/values.yaml` (config)
- `deploy/service/coding-bundle/tools.json` (config)
- `deploy/service/compose.yaml` (container)
- `deploy/service/connection.example.json` (config)
- `deploy/service/examples/aws/deployment.yaml` (config)
- `deploy/service/examples/azure/deployment.yaml` (config)
- `deploy/service/examples/local-k8s/deployment.yaml` (config)
- `deploy/service/up/aws.yaml` (config)
- `deploy/service/up/azure.yaml` (config)
- `docs-site/desktop-pages.json` (config)
- `docs-site/package.json` (manifest)
- `docs-site/pages.json` (config)
- `docs/config.example.toml` (config)
- `harness/Cargo.toml` (manifest)
- `harness/artifacts/Cargo.toml` (manifest)
- `harness/compliance/Cargo.toml` (manifest)
- `harness/desktop-starters/package.json` (manifest)
- `harness/desktop-starters/templates/electron-game-builder/electron-builder.json` (config)
- `harness/desktop-starters/templates/electron-game-builder/package.json` (manifest)
- `harness/desktop-starters/templates/shared/tsconfig.json` (config)
- `harness/desktop-starters/templates/tauri-game-builder/package.json` (manifest)
- `harness/desktop-starters/templates/tauri-game-builder/src-tauri/Cargo.toml` (manifest)
- `harness/desktop-starters/templates/tauri-game-builder/src-tauri/tauri.conf.json` (config)
- `harness/examples/arcade/asset-library/catalog.json` (config)
- `harness/examples/arcade/electron-builder.json` (config)
- `harness/examples/arcade/package.json` (manifest)
- `harness/examples/arcade/starter-games/lumen-garden/manifest.json` (config)
- `harness/examples/arcade/starter-games/moonlight-rally/courses/neon.json` (config)
- `harness/examples/arcade/starter-games/moonlight-rally/courses/sunset.json` (config)
- `harness/examples/arcade/starter-games/moonlight-rally/credits.json` (config)
- `harness/examples/arcade/starter-games/moonlight-rally/manifest.json` (config)
- `harness/examples/arcade/starter-games/neon-drift/manifest.json` (config)
- `harness/examples/arcade/starter-games/orbit-runner/manifest.json` (config)
- `harness/examples/arcade/starter-games/pip-garden/art-credits.json` (config)
- `harness/examples/arcade/starter-games/pip-garden/generation.json` (config)
- `harness/examples/arcade/starter-games/pip-garden/manifest.json` (config)
- `harness/examples/arcade/starter-games/skybound-carrier/asset-credits.json` (config)
- `harness/examples/arcade/starter-games/skybound-carrier/config.json` (config)
- `harness/examples/arcade/starter-games/skybound-carrier/manifest.json` (config)
- `harness/examples/arcade/tsconfig.json` (config)
- `harness/examples/arcade/tsconfig.main.json` (config)
- `harness/examples/assistant/tools.json` (config)
- `harness/examples/computer-tools/Cargo.toml` (manifest)
- `harness/examples/device-tools/Cargo.toml` (manifest)
- `harness/examples/mixed/tools.json` (config)

## Top-level layout

- `coworker` — 297 analysed file(s)
- `harness` — 222 analysed file(s)
- `deploy` — 159 analysed file(s)
- `docs` — 65 analysed file(s)
- `docs-site` — 41 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `.github` — 6 analysed file(s)
- `.claude` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `ecb445490fc054d52b8ea610d97ba947f57033d2` is the revision these paths and observations refer to.
