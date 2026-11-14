# Project structure: google/artemis

**Analysed commit:** `351ca8422f7b5b54e80a9c1ce03a222e02415b6b`

**Commit reference:** [351ca8422f7b5b54e80a9c1ce03a222e02415b6b](https://github.com/google/artemis/commit/351ca8422f7b5b54e80a9c1ce03a222e02415b6b)

**Tree at this commit:** [google/artemis@351ca8422f7b](https://github.com/google/artemis/tree/351ca8422f7b5b54e80a9c1ce03a222e02415b6b)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | google/artemis |
| Description | ARTEMIS turns natural-language instructions into reliable Android automation. It automates end-to-end workflows, captures logs, and integrates seamlessly with AI coding assistants such as Antigravity, Codex, and Claude Code.  It also achieves 99%+ success rate on AndroidWorld Benchmark. |
| Stars | 17445 |
| Forks | 1945 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `351ca8422f7b5b54e80a9c1ce03a222e02415b6b` |
| Retrieved at | 2026-11-14T19:08:35.047253+00:00 |
| Files in this snapshot | 785 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    ci.yml
apps/  (99 files)
  admin_console/  (31 files)
    core/  (4 files)
      … 4 files under this directory
    database/  (6 files)
      … 6 files under this directory
    routers/  (8 files)
      … 8 files under this directory
    schemas/  (2 files)
      … 2 files under this directory
    services/  (8 files)
      … 8 files under this directory
    __init__.py
    replay_manager.py
    server.py
  showcase_ui/  (67 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (59 files)
      … 59 files under this directory
    README.md
    angular.json
    package.json
    proxy.conf.json
    tsconfig.app.json
    tsconfig.json
    tsconfig.spec.json
  __init__.py
artemis/  (265 files)
  agents/  (67 files)
    checker/  (2 files)
      … 2 files under this directory
    diagnoser/  (2 files)
      … 2 files under this directory
    explorer/  (11 files)
      … 11 files under this directory
    flash/  (6 files)
      … 6 files under this directory
    history_analyzer/  (2 files)
      … 2 files under this directory
    image_processor/  (2 files)
      … 2 files under this directory
    log_analyzer/  (5 files)
      … 5 files under this directory
    object_detector/  (2 files)
      … 2 files under this directory
    operator/  (3 files)
      … 3 files under this directory
    outputter/  (2 files)
      … 2 files under this directory
    planner/  (2 files)
      … 2 files under this directory
    summarizer/  (1 files)
      … 1 files under this directory
    validator/  (9 files)
      … 9 files under this directory
    video_analyzer/  (16 files)
      … 16 files under this directory
    __init__.py
    prompt_assembly.py
  clients/  (2 files)
    accessibility_client.py
    screen_client_factory.py
  config/  (10 files)
    core/  (3 files)
      … 3 files under this directory
    __init__.py
    agent.py
    constants.py
    llm.py
    paths.py
    runtime.py
    settings.py
  controllers/  (5 files)
    __init__.py
    controller_factory.py
    device_controller.py
    types.py
    unified_controller.py
  core/  (18 files)
    diagnostics/  (15 files)
      … 15 files under this directory
    __init__.py
    tool_declaration.py
    tool_failure.py
  data_engine/  (6 files)
    context_vars.py
    engine.py
    history_reader.py
    models.py
    storage.py
    trace.py
  drivers/  (10 files)
    android/  (4 files)
      … 4 files under this directory
    cloud/  (1 files)
      … 1 files under this directory
    mock/  (1 files)
      … 1 files under this directory
    __init__.py
    base.py
    factory.py
    types.py
  graph/  (5 files)
    checkpoints.py
    graph.py
    perception.py
    state.py
    visibility.py
  interfaces/  (16 files)
    cli/  (13 files)
      … 13 files under this directory
    sdk/  (3 files)
      … 3 files under this directory
  llm/  (10 files)
    google/  (3 files)
      … 3 files under this directory
    __init__.py
    fake_model.py
    parser.py
    reliability.py
    router.py
    schemas.py
    structured.py
  mcp/  (15 files)
    actuators/  (4 files)
      … 4 files under this directory
    __init__.py
    action_executor.py
    action_manifest.py
    action_names.py
    action_server.py
    action_session.py
    action_specs.py
    action_types.py
    adb_server.py
    observation.py
    xml_search_server.py
  memory/  (6 files)
    __init__.py
    chunking.py
    context_policy.py
    step_capsule.md
    step_memory.py
    transcript.py
  platform/  (5 files)
    __init__.py
    base.py
    darwin.py
    linux.py
    windows.py
  resources/  (6 files)
    config/  (1 files)
      … 1 files under this directory
    showcase_ui/  (4 files)
      … 4 files under this directory
    __init__.py
  runtime/  (13 files)
    __init__.py
    adb_endpoint.py
    awake_lease.py
    awake_service.py
    cancel_requests.py
    daemon_client.py
    device_lock.py
    device_pool.py
    helper_manager.py
    process_probe.py
    server_lifecycle.py
    supervisor.py
    trace_store.py
  sdk/  (9 files)
    builders/  (2 files)
      … 2 files under this directory
    types/  (2 files)
      … 2 files under this directory
    __init__.py
    agent.py
    constants.py
    run_outcome.py
    utils.py
  services/  (2 files)
    llm.py
    token_meter.py
  telemetry/  (5 files)
    storage/  (1 files)
      … 1 files under this directory
    __init__.py
    models.py
    replay.py
    tracer.py
  toolchain/  (3 files)
    __init__.py
    descriptors.py
    resolver.py
  tools/  (26 files)
    history/  (4 files)
      … 4 files under this directory
    mobile/  (6 files)
      … 6 files under this directory
    system/  (1 files)
      … 1 files under this directory
    base.py
    command_tool.py
    committee_prompts.json
    committee_tool.py
    diagnoser_submit_answer_tool.py
    diagnostic_tool.py
    explorer_tool.py
    image_processor_tool.py
    index.py
    log_tool.py
    object_detection_tool.py
    scratchpad.py
    tool_wrapper.py
    video_tool.py
    wait_tool.py
  utils/  (19 files)
    app_launch_utils.py
    coordinates.py
    credentials_validator.py
    cv_canvas.py
    cython_compat.py
    element_hit_test.py
    image_diff.py
    image_hash.py
    notes.py
    ocr_api.py
    ocr_xml_fusion.py
    plan_grammar.py
    python_executor.py
    startup_progress.py
    task_tree.py
    text.py
    ui_filter.py
    video.py
    visualization.py
  __init__.py
  __main__.py
  _legacy_imports.py
  _version.py
  constants.py
  context.py
  main.py
config/  (1 files)
  artemis.jsonc
docs/  (4 files)
  assets/  (4 files)
    logo/  (2 files)
      … 2 files under this directory
    generate_banner.py
    generate_ui_showcase.py
mcp_server/  (25 files)
  background/  (2 files)
    __init__.py
    task_runner.py
  notifiers/  (8 files)
    __init__.py
    agentapi.py
    base.py
    composite.py
    desktop.py
    file.py
    script.py
    webhook.py
  tools/  (6 files)
    __init__.py
    device_state.py
    diagnose.py
    inspect_trace.py
    task_manager.py
    task_runner.py
  utils/  (3 files)
    __init__.py
    device_utils.py
    env_utils.py
  README.md
  __init__.py
  __main__.py
  base.py
  rules.md
  server.py
packages/  (31 files)
  artemis-accessibility-helper/  (19 files)
    app/  (13 files)
      … 13 files under this directory
    .gitignore
    build.gradle.kts
    build_apk.sh
    gradle.properties
    helper_manifest.json
    settings.gradle.kts
  artemis-client/  (12 files)
    examples/  (1 files)
      … 1 files under this directory
    src/  (6 files)
      … 6 files under this directory
    tests/  (2 files)
      … 2 files under this directory
    DESIGN.md
    README.md
    pyproject.toml
playground/  (47 files)
  artemis_container/  (5 files)
    .dockerignore
    Dockerfile
    README.md
    docker-compose.yml
    docker-entrypoint.sh
  backend_manager/  (25 files)
    app/  (21 files)
      … 21 files under this directory
    Dockerfile
    README.md
    docker-compose.yml
    requirements.txt
  nginx_container/  (16 files)
    certs/  (2 files)
      … 2 files under this directory
    conf/  (6 files)
      … 6 files under this directory
    html/  (3 files)
      … 3 files under this directory
    .dockerignore
    Dockerfile
    README.md
    docker-compose.yml
    docker-entrypoint.sh
  deploy_to_cos.sh
scripts/  (10 files)
  check_dependency_sources.py
  install_deps.ps1
  install_deps.sh
  quality_ratchet.py
  real_device_video_acceptance.py
  run_edge_case_part.py
  run_ui.py
  start.ps1
  test_all_edge_cases.py
  verify_concurrency_and_devices.py
tests/  (240 files)
  e2e/  (2 files)
    play_youtube.py
    test_multi_port_end_to_end.py
  fixtures/  (4 files)
    action_surfaces/  (4 files)
      … 4 files under this directory
  integration/  (16 files)
    agents/  (8 files)
      … 8 files under this directory
    test_artemis_login.py
    test_cloud_gateway.py
    test_flash_standalone_news.py
    test_flash_standalone_youtube.py
    test_ime.py
    test_physical_actions.py
    test_remote_adb.py
    test_thin_sdk_live.py
  tools/  (15 files)
    checker/  (1 files)
      … 1 files under this directory
    diagnoser/  (1 files)
      … 1 files under this directory
    explorer/  (1 files)
      … 1 files under this directory
    history_analyzer/  (1 files)
      … 1 files under this directory
    hopper/  (1 files)
      … 1 files under this directory
    image_processor/  (1 files)
      … 1 files under this directory
    log_analyzer/  (1 files)
      … 1 files under this directory
    object_detector/  (1 files)
      … 1 files under this directory
    operator/  (1 files)
      … 1 files under this directory
    outputter/  (1 files)
      … 1 files under this directory
    planner/  (1 files)
      … 1 files under this directory
    summarizer/  (1 files)
      … 1 files under this directory
    validator/  (1 files)
      … 1 files under this directory
    video_analyzer/  (1 files)
      … 1 files under this directory
    conftest.py
  unit/  (202 files)
    admin_console/  (18 files)
      … 18 files under this directory
    agents/  (40 files)
      … 40 files under this directory
    clients/  (2 files)
      … 2 files under this directory
    config/  (1 files)
      … 1 files under this directory
    core/  (9 files)
      … 9 files under this directory
    data_engine/  (8 files)
      … 8 files under this directory
    graph/  (6 files)
      … 6 files under this directory
    mcp/  (17 files)
      … 17 files under this directory
    memory/  (4 files)
      … 4 files under this directory
    runtime/  (12 files)
      … 12 files under this directory
    sdk/  (4 files)
      … 4 files under this directory
    services/  (1 files)
      … 1 files under this directory
    tools/  (34 files)
      … 34 files under this directory
    utils/  (15 files)
      … 15 files under this directory
    test_await.py
    test_bootstrap_scripts_encoding.py
    test_cli.py
    test_config_package.py
    test_context.py
    test_controller_factory.py
    test_credentials_validator.py
    test_drivers.py
    test_gemini_role.py
    test_google_provider.py
    test_google_usage.py
    test_hierarchy_backend_visibility.py
    test_hierarchy_fidelity.py
    test_install_paths.py
    test_llm_gateway.py
    test_llm_grounding.py
    test_llm_pause.py
    test_llm_reliability.py
    test_llm_structured.py
    test_main_entrypoint.py
    test_memory_config.py
    test_packaging_resources.py
    test_planner.py
    test_sdk.py
    … 7 more files
  conftest.py
third_party/  (46 files)
  mobile_use/  (46 files)
    agents/  (4 files)
      … 4 files under this directory
    clients/  (2 files)
      … 2 files under this directory
    config/  (3 files)
      … 3 files under this directory
    controllers/  (4 files)
      … 4 files under this directory
    sdk/  (10 files)
      … 10 files under this directory
    tools/  (5 files)
      … 5 files under this directory
    utils/  (9 files)
      … 9 files under this directory
    LICENSE
    METADATA
    NOTICE
    __init__.py
    context.py
    graph.py
    llm_service.py
    main.py
    testing.py
.dockerignore
.env.example
.gitignore
.pre-commit-config.yaml
.quality-baseline.json
CONTRIBUTING.md
Dockerfile
LICENSE
Makefile
README.md
README_CN.md
pyproject.toml
pyright-core.json
setup.py
start.bat
start.sh
```

## Entry points

- [apps/admin_console/server.py](https://github.com/google/artemis/blob/351ca8422f7b5b54e80a9c1ce03a222e02415b6b/apps/admin_console/server.py)
- [artemis/__main__.py:17](https://github.com/google/artemis/blob/351ca8422f7b5b54e80a9c1ce03a222e02415b6b/artemis/__main__.py#L17)
- [artemis/interfaces/cli/commands/helper.py:37](https://github.com/google/artemis/blob/351ca8422f7b5b54e80a9c1ce03a222e02415b6b/artemis/interfaces/cli/commands/helper.py#L37)
- [artemis/interfaces/cli/commands/server.py:35](https://github.com/google/artemis/blob/351ca8422f7b5b54e80a9c1ce03a222e02415b6b/artemis/interfaces/cli/commands/server.py#L35)
- [artemis/interfaces/cli/commands/trace.py:29](https://github.com/google/artemis/blob/351ca8422f7b5b54e80a9c1ce03a222e02415b6b/artemis/interfaces/cli/commands/trace.py#L29)
- [artemis/interfaces/cli/main.py](https://github.com/google/artemis/blob/351ca8422f7b5b54e80a9c1ce03a222e02415b6b/artemis/interfaces/cli/main.py)
- [artemis/main.py:57](https://github.com/google/artemis/blob/351ca8422f7b5b54e80a9c1ce03a222e02415b6b/artemis/main.py#L57)
- [artemis/mcp/adb_server.py:482](https://github.com/google/artemis/blob/351ca8422f7b5b54e80a9c1ce03a222e02415b6b/artemis/mcp/adb_server.py#L482)
- [artemis/mcp/xml_search_server.py:290](https://github.com/google/artemis/blob/351ca8422f7b5b54e80a9c1ce03a222e02415b6b/artemis/mcp/xml_search_server.py#L290)
- [mcp_server/__main__.py:19](https://github.com/google/artemis/blob/351ca8422f7b5b54e80a9c1ce03a222e02415b6b/mcp_server/__main__.py#L19)
- [mcp_server/background/task_runner.py:415](https://github.com/google/artemis/blob/351ca8422f7b5b54e80a9c1ce03a222e02415b6b/mcp_server/background/task_runner.py#L415)
- [mcp_server/server.py:105](https://github.com/google/artemis/blob/351ca8422f7b5b54e80a9c1ce03a222e02415b6b/mcp_server/server.py#L105)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 21 file(s) under api layer (observed from repository paths and static analysis). Observed routes: GET /admin, GET /debug, GET /images/{image_name}, GET /api/images/{image_name}, GET /videos/{video_path:path}. Obs… |
| apps package | library | Observed | Groups 33 file(s) under apps package (observed from repository paths and static analysis). Observed top-level classes: ReplayManager, ReplayRequest, RunRequest, StopRequest. |
| artemis package | library | Observed | Groups 185 file(s) under artemis package (observed from repository paths and static analysis). Observed top-level classes: AccessibilityHelperManager, ActionCode, ActionResult, ActionSession, ActionSpec, Actuator. Obser… |
| Configuration and deployment | config | Observed | Groups 45 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: AgentGlobalConfig, CascadingConfigEngine, CheckerConfig, CommitteeConfig, ExecutionC… |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 18 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: BackgroundTaskRecord, Capabilities, Device, FailedOutputRecord, HistoryChunkRecord, ImageRecord. Obser… |
| Application entry point | entrypoint | Observed | Groups 22 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI, Typer. Observed routes: GET /, GET /{full_path:path}, GET /. Observe… |
| External integrations | external | Observed | Groups 8 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: AccessibilityClient, ArtemisClient, DeviceOfflineError, FallbackScreenClient, HelperEmptyHie… |
| mcp_server package | library | Observed | Groups 20 file(s) under mcp_server package (observed from repository paths and static analysis). Observed top-level classes: AgentApiNotifier, BaseNotifier, CompositeNotifier, DesktopNotifier, FileNotifier, ScriptNotifi… |
| packages package | library | Observed | Groups 13 file(s) under packages package (observed from repository paths and static analysis). Observed top-level classes: ApiError, ArtemisClientError, AuthenticationError, ConflictError, JsonTransport, NetworkError. |
| playground package | library | Observed | Groups 11 file(s) under playground package (observed from repository paths and static analysis). Observed top-level classes: CreateSessionRequest, HeartbeatResponse, OTPRequest, OTPRequestResponse, OTPVerify, SessionLis… |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 44 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: AdbDeviceProbe, AdbKeyStatus, AdbServerConnectionManager, AppInfo, BaseProbe, BigQueryMapp… |
| Tests | test | Observed | Groups 244 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH urllib.request.urlopen, PATCH urllib.request.urlopen, PATCH urllib.request.urlopen, PATCH urllib.request.urlope… |
| third_party package | library | Observed | Groups 31 file(s) under third_party package (observed from repository paths and static analysis). Observed top-level classes: AgentBase, AgentConfigBase, AgentConfigBuilderBase, AgentError, AgentNotInitializedError, Age… |

## Important files

- `.dockerignore` (container)
- `.env.example` (config)
- `.github/workflows/ci.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `.quality-baseline.json` (config)
- `Dockerfile` (container)
- `apps/showcase_ui/angular.json` (config)
- `apps/showcase_ui/package.json` (manifest)
- `apps/showcase_ui/proxy.conf.json` (config)
- `apps/showcase_ui/tsconfig.app.json` (config)
- `apps/showcase_ui/tsconfig.json` (config)
- `apps/showcase_ui/tsconfig.spec.json` (config)
- `artemis/agents/checker/checker.json` (config)
- `artemis/agents/diagnoser/diagnoser.json` (config)
- `artemis/agents/explorer/explorer.json` (config)
- `artemis/agents/object_detector/object_detector.json` (config)
- `artemis/agents/operator/operator.json` (config)
- `artemis/agents/planner/planner.json` (config)
- `artemis/tools/committee_prompts.json` (config)
- `packages/artemis-accessibility-helper/helper_manifest.json` (config)
- `packages/artemis-client/pyproject.toml` (manifest)
- `playground/artemis_container/.dockerignore` (container)
- `playground/artemis_container/Dockerfile` (container)
- `playground/artemis_container/docker-compose.yml` (container)
- `playground/backend_manager/Dockerfile` (container)
- `playground/backend_manager/docker-compose.yml` (container)
- `playground/backend_manager/requirements.txt` (manifest)
- `playground/nginx_container/.dockerignore` (container)
- `playground/nginx_container/Dockerfile` (container)
- `playground/nginx_container/docker-compose.yml` (container)
- `playground/nginx_container/html/502.json` (config)
- `playground/nginx_container/html/504.json` (config)
- `pyproject.toml` (manifest)
- `pyright-core.json` (config)
- `setup.py` (manifest)

## Top-level layout

- `artemis` — 265 analysed file(s)
- `tests` — 240 analysed file(s)
- `apps` — 99 analysed file(s)
- `playground` — 47 analysed file(s)
- `third_party` — 46 analysed file(s)
- `packages` — 31 analysed file(s)
- `mcp_server` — 25 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `scripts` — 10 analysed file(s)
- `docs` — 4 analysed file(s)
- `.github` — 1 analysed file(s)
- `config` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `351ca8422f7b5b54e80a9c1ce03a222e02415b6b` is the revision these paths and observations refer to.
