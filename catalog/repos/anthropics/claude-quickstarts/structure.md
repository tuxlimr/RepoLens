# Project structure: anthropics/claude-quickstarts

**Analysed commit:** `4a4224bdf0e9cfb3332167b69c90457403813625`

**Commit reference:** [4a4224bdf0e9cfb3332167b69c90457403813625](https://github.com/anthropics/claude-quickstarts/commit/4a4224bdf0e9cfb3332167b69c90457403813625)

**Tree at this commit:** [anthropics/claude-quickstarts@4a4224bdf0e9](https://github.com/anthropics/claude-quickstarts/tree/4a4224bdf0e9cfb3332167b69c90457403813625)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | anthropics/claude-quickstarts |
| Description | A collection of projects designed to help developers quickly get started with building deployable applications using the Claude API |
| Stars | 20959 |
| Forks | 3495 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `4a4224bdf0e9cfb3332167b69c90457403813625` |
| Retrieved at | 2026-11-14T19:08:01.155435+00:00 |
| Files in this snapshot | 739 |

## Directory tree

```text
.github/  (5 files)
  workflows/  (4 files)
    build.yaml
    openshell-policy.yaml
    reusable_build_step.yaml
    tests.yaml
  pull_request_template.md
agents/  (18 files)
  tools/  (8 files)
    __init__.py
    base.py
    calculator_mcp.py
    code_execution.py
    file_tools.py
    mcp_tool.py
    think.py
    web_search.py
  utils/  (4 files)
    __init__.py
    connections.py
    history_util.py
    tool_util.py
  .gitignore
  README.md
  __init__.py
  agent.py
  agent_demo.ipynb
  test_message_params.py
autonomous-coding/  (13 files)
  prompts/  (3 files)
    app_spec.txt
    coding_prompt.md
    initializer_prompt.md
  .gitignore
  README.md
  agent.py
  autonomous_agent_demo.py
  client.py
  progress.py
  prompts.py
  requirements.txt
  security.py
  test_security.py
browser-toolset/  (11 files)
  python/  (4 files)
    cdp_browser.py
    exercise.py
    requirements.txt
    run.py
  typescript/  (5 files)
    cdp-browser.ts
    exercise.ts
    package.json
    run.ts
    tsconfig.json
  .gitignore
  README.md
browser-use-demo/  (52 files)
  browser_use_demo/  (18 files)
    browser_tool_utils/  (6 files)
      … 6 files under this directory
    tools/  (5 files)
      … 5 files under this directory
    __init__.py
    display_constants.py
    loop.py
    message_handler.py
    message_renderer.py
    requirements.txt
    streamlit.py
  image/  (14 files)
    .config/  (4 files)
      … 4 files under this directory
    static_content/  (1 files)
      … 1 files under this directory
    entrypoint.sh
    http_server.py
    index.html
    mutter_startup.sh
    novnc_startup.sh
    start_all.sh
    tint2_startup.sh
    x11vnc_startup.sh
    xvfb_startup.sh
  tests/  (7 files)
    README.md
    __init__.py
    conftest.py
    test_integration.py
    test_message_renderer.py
    test_sampling_loop.py
    test_streamlit_helpers.py
  .dockerignore
  .env.example
  .gitignore
  CHANGELOG.md
  Dockerfile
  NOTICE
  README.md
  build.sh
  docker-compose.yml
  pytest.ini
  setup.py
  test-requirements.txt
  validate_env.py
computer-toolset/  (11 files)
  python/  (4 files)
    exercise.py
    requirements.txt
    run.py
    vnc_computer.py
  typescript/  (5 files)
    exercise.ts
    package.json
    run.ts
    tsconfig.json
    vnc-computer.ts
  .gitignore
  README.md
computer-use-best-practices/  (57 files)
  .claude/  (1 files)
    skills/  (1 files)
      … 1 files under this directory
  .vscode/  (2 files)
    launch.json
    settings.json
  computer_use/  (17 files)
    tools/  (9 files)
      … 9 files under this directory
    __init__.py
    __main__.py
    formatters.py
    image.py
    loop.py
    preflight.py
    render.py
    trajectory.py
  dev_ui/  (11 files)
    assets/  (2 files)
      … 2 files under this directory
    localization_demo/  (3 files)
      … 3 files under this directory
    tool_panel/  (3 files)
      … 3 files under this directory
    trajectory_viewer/  (2 files)
      … 2 files under this directory
    __init__.py
  sandbox/  (1 files)
    default.sb
  tests/  (18 files)
    __init__.py
    test_advisor.py
    test_base.py
    test_batch.py
    test_build_tools.py
    test_compaction.py
    test_computer.py
    test_config.py
    test_constants.py
    test_editor.py
    test_formatters.py
    test_image.py
    test_loop.py
    test_loop_hosted.py
    test_preflight.py
    test_result.py
    test_shell.py
    test_zoom.py
  .env.example
  .gitignore
  README.md
  config.example.toml
  constants.py
  pyproject.toml
  requirements.txt
computer-use-demo/  (45 files)
  .claude/  (1 files)
    skills/  (1 files)
      … 1 files under this directory
  .zed/  (1 files)
    settings.json
  ca-store/  (1 files)
    distrust_ca_roots.sh
  computer_use_demo/  (12 files)
    tools/  (8 files)
      … 8 files under this directory
    __init__.py
    loop.py
    requirements.txt
    streamlit.py
  image/  (15 files)
    .config/  (4 files)
      … 4 files under this directory
    .streamlit/  (1 files)
      … 1 files under this directory
    static_content/  (1 files)
      … 1 files under this directory
    entrypoint.sh
    http_server.py
    index.html
    mutter_startup.sh
    novnc_startup.sh
    start_all.sh
    tint2_startup.sh
    x11vnc_startup.sh
    xvfb_startup.sh
  tests/  (6 files)
    tools/  (3 files)
      … 3 files under this directory
    conftest.py
    loop_test.py
    streamlit_test.py
  .gitignore
  CONTRIBUTING.md
  Dockerfile
  LICENSE
  README.md
  dev-requirements.txt
  pyproject.toml
  ruff.toml
  setup.sh
customer-support-agent/  (38 files)
  app/  (6 files)
    api/  (1 files)
      … 1 files under this directory
    lib/  (2 files)
      … 2 files under this directory
    globals.css
    layout.tsx
    page.tsx
  components/  (13 files)
    ui/  (7 files)
      … 7 files under this directory
    ChatArea.tsx
    FullSourceModal.tsx
    LeftSidebar.tsx
    RightSidebar.tsx
    TopNavBar.tsx
    theme-provider.tsx
  lib/  (1 files)
    utils.ts
  public/  (6 files)
    ant-logo.svg
    claude-icon.svg
    next.svg
    vercel.svg
    wordmark-dark.svg
    wordmark.svg
  styles/  (1 files)
    themes.js
  .eslintrc.json
  .gitignore
  README.md
  amplify.yml
  components.json
  config.ts
  next.config.mjs
  package.json
  postcss.config.mjs
  tailwind.config.ts
  tsconfig.json
financial-data-analyst/  (34 files)
  app/  (5 files)
    api/  (1 files)
      … 1 files under this directory
    finance/  (1 files)
      … 1 files under this directory
    globals.css
    layout.tsx
    page.tsx
  components/  (13 files)
    ui/  (9 files)
      … 9 files under this directory
    ChartRenderer.tsx
    FilePreview.tsx
    TopNavBar.tsx
    theme-provider.tsx
  hooks/  (1 files)
    use-toast.ts
  lib/  (1 files)
    utils.ts
  public/  (3 files)
    ant-logo.svg
    wordmark-dark.svg
    wordmark.svg
  types/  (1 files)
    chart.ts
  utils/  (1 files)
    fileHandling.ts
  .eslintrc.json
  .gitignore
  README.md
  components.json
  next.config.mjs
  package.json
  postcss.config.mjs
  tailwind.config.ts
  tsconfig.json
managed-agents/  (450 files)
  assistant-ui/  (78 files)
    agents/  (1 files)
      … 1 files under this directory
    app/  (15 files)
      … 15 files under this directory
    components/  (35 files)
      … 35 files under this directory
    environments/  (1 files)
      … 1 files under this directory
    hooks/  (1 files)
      … 1 files under this directory
    lib/  (13 files)
      … 13 files under this directory
    sample_data/  (1 files)
      … 1 files under this directory
    .env.example
    .gitignore
    CLAUDE.md
    README.md
    components.json
    eslint.config.mjs
    next.config.ts
    package.json
    postcss.config.mjs
    skill.md
    tsconfig.json
  chat-sdk/  (21 files)
    setup/  (3 files)
      … 3 files under this directory
    src/  (8 files)
      … 8 files under this directory
    web/  (3 files)
      … 3 files under this directory
    .env.example
    .gitignore
    CLAUDE.md
    README.md
    package.json
    skill.md
    tsconfig.json
  copilot-kit-ag-ui/  (30 files)
    .claude/  (1 files)
      … 1 files under this directory
    agents/  (1 files)
      … 1 files under this directory
    environments/  (1 files)
      … 1 files under this directory
    server/  (5 files)
      … 5 files under this directory
    web/  (17 files)
      … 17 files under this directory
    .env.example
    .gitignore
    CLAUDE.md
    README.md
    package.json
  daily-brief/  (17 files)
    agents/  (7 files)
      … 7 files under this directory
    scripts/  (4 files)
      … 4 files under this directory
    slack/  (1 files)
      … 1 files under this directory
    .env.example
    .gitignore
    CLAUDE.md
    README.md
    preferences.example.md
  knowledge-wiki/  (22 files)
    example_data/  (2 files)
      … 2 files under this directory
    prompts/  (4 files)
      … 4 files under this directory
    .gitignore
    CLAUDE.md
    README.md
    build_manifest.py
    distill_documents_into_knowledge_wiki.ipynb
    fetch_data_room.py
    fetch_real_deck.py
    make_analyst_docx.py
    manifest_core.json
    manifest_full.json
    manifest_mini.json
    manifest_quickstart.json
    manifest_standard.json
    requirements.txt
    skill.md
    utilities.py
  linear/  (15 files)
    agents/  (1 files)
      … 1 files under this directory
    environments/  (1 files)
      … 1 files under this directory
    src/  (6 files)
      … 6 files under this directory
    .env.example
    .gitignore
    CLAUDE.md
    README.md
    package.json
    skill.md
    tsconfig.json
  mcp-server-typescript/  (16 files)
    src/  (5 files)
      … 5 files under this directory
    .dockerignore
    .env.example
    .gitignore
    CLAUDE.md
    Dockerfile
    README.md
    bun.lock
    environment.yaml
    package.json
    skill.md
    tsconfig.json
  roadtrip-planner/  (30 files)
    agents/  (4 files)
      … 4 files under this directory
    environments/  (1 files)
      … 1 files under this directory
    src/  (16 files)
      … 16 files under this directory
    vaults/  (1 files)
      … 1 files under this directory
    .env.example
    .gitignore
    CLAUDE.md
    README.md
    next.config.ts
    package.json
    skill.md
    tsconfig.json
  self-hosted-sandboxes/  (159 files)
    archil/  (11 files)
      … 11 files under this directory
    cloudflare-containers/  (8 files)
      … 8 files under this directory
    cloudflare-worker/  (8 files)
      … 8 files under this directory
    daytona/  (4 files)
      … 4 files under this directory
    docker/  (8 files)
      … 8 files under this directory
    docker-memory/  (10 files)
      … 10 files under this directory
    modal/  (4 files)
      … 4 files under this directory
    openshell/  (10 files)
      … 10 files under this directory
    openshell-policy/  (82 files)
      … 82 files under this directory
    vercel/  (8 files)
      … 8 files under this directory
    webhook-demo/  (4 files)
      … 4 files under this directory
    CLAUDE.md
    README.md
  sentry/  (18 files)
    .claude/  (1 files)
      … 1 files under this directory
    agents/  (2 files)
      … 2 files under this directory
    environments/  (1 files)
      … 1 files under this directory
    vaults/  (1 files)
      … 1 files under this directory
    .env.example
    .gitignore
    CLAUDE.md
    README.md
    deploy.py
    managed_agents.py
    oauth_setup.py
    pyproject.toml
    run_now.py
    runs.py
    skill.md
    start.sh
    teardown.py
  sentry-autofix/  (28 files)
    .claude/  (1 files)
      … 1 files under this directory
    agents/  (4 files)
      … 4 files under this directory
    demo-app/  (7 files)
      … 7 files under this directory
    src/  (7 files)
      … 7 files under this directory
    test/  (2 files)
      … 2 files under this directory
    .env.example
    .gitignore
    CLAUDE.md
    README.md
    package.json
    start.sh
    tsconfig.json
  slack/  (15 files)
    agents/  (1 files)
      … 1 files under this directory
    environments/  (1 files)
      … 1 files under this directory
    src/  (6 files)
      … 6 files under this directory
    .env.example
    .gitignore
    CLAUDE.md
    README.md
    package.json
    skill.md
    tsconfig.json
  README.md
.pre-commit-config.yaml
CLAUDE.md
LICENSE
README.md
pyproject.toml
```

## Entry points

- [managed-agents/self-hosted-sandboxes/openshell-policy/src/agentpolicy/cli.py:678](https://github.com/anthropics/claude-quickstarts/blob/4a4224bdf0e9cfb3332167b69c90457403813625/managed-agents/self-hosted-sandboxes/openshell-policy/src/agentpolicy/cli.py#L678)
- [agents/tools/calculator_mcp.py:54](https://github.com/anthropics/claude-quickstarts/blob/4a4224bdf0e9cfb3332167b69c90457403813625/agents/tools/calculator_mcp.py#L54)
- [autonomous-coding/autonomous_agent_demo.py:115](https://github.com/anthropics/claude-quickstarts/blob/4a4224bdf0e9cfb3332167b69c90457403813625/autonomous-coding/autonomous_agent_demo.py#L115)
- [browser-toolset/python/exercise.py:142](https://github.com/anthropics/claude-quickstarts/blob/4a4224bdf0e9cfb3332167b69c90457403813625/browser-toolset/python/exercise.py#L142)
- [browser-toolset/python/run.py:92](https://github.com/anthropics/claude-quickstarts/blob/4a4224bdf0e9cfb3332167b69c90457403813625/browser-toolset/python/run.py#L92)
- [browser-use-demo/browser_use_demo/streamlit.py:739](https://github.com/anthropics/claude-quickstarts/blob/4a4224bdf0e9cfb3332167b69c90457403813625/browser-use-demo/browser_use_demo/streamlit.py#L739)
- [browser-use-demo/image/http_server.py:18](https://github.com/anthropics/claude-quickstarts/blob/4a4224bdf0e9cfb3332167b69c90457403813625/browser-use-demo/image/http_server.py#L18)
- [browser-use-demo/validate_env.py:52](https://github.com/anthropics/claude-quickstarts/blob/4a4224bdf0e9cfb3332167b69c90457403813625/browser-use-demo/validate_env.py#L52)
- [computer-toolset/python/exercise.py:126](https://github.com/anthropics/claude-quickstarts/blob/4a4224bdf0e9cfb3332167b69c90457403813625/computer-toolset/python/exercise.py#L126)
- [computer-toolset/python/run.py:67](https://github.com/anthropics/claude-quickstarts/blob/4a4224bdf0e9cfb3332167b69c90457403813625/computer-toolset/python/run.py#L67)
- [computer-use-best-practices/computer_use/__main__.py:105](https://github.com/anthropics/claude-quickstarts/blob/4a4224bdf0e9cfb3332167b69c90457403813625/computer-use-best-practices/computer_use/__main__.py#L105)
- [computer-use-best-practices/dev_ui/localization_demo/server.py:37](https://github.com/anthropics/claude-quickstarts/blob/4a4224bdf0e9cfb3332167b69c90457403813625/computer-use-best-practices/dev_ui/localization_demo/server.py#L37)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| agents package | library | Observed | Groups 13 file(s) under agents package (observed from repository paths and static analysis). Observed top-level classes: Agent, CodeExecutionServerTool, FileReadTool, FileWriteTool, MCPConnection, MCPConnectionSSE. Obse… |
| API layer | api | Observed | Groups 18 file(s) under api layer (observed from repository paths and static analysis). |
| autonomous-coding package | library | Observed | Groups 4 file(s) under autonomous-coding package (observed from repository paths and static analysis). Observed top-level functions: bash_security_hook, copy_spec_to_project, count_passing_tests, extract_commands, get_c… |
| browser-toolset package | library | Observed | Groups 4 file(s) under browser-toolset package (observed from repository paths and static analysis). Observed top-level classes: CdpBrowser. Observed top-level functions: find_chrome. |
| browser-use-demo package | library | Observed | Groups 24 file(s) under browser-use-demo package (observed from repository paths and static analysis). Observed top-level classes: APIProvider, BaseAnthropicTool, BrowserOptions, BrowserTool, CLIResult, CoordinateScaler… |
| computer-toolset package | library | Observed | Groups 4 file(s) under computer-toolset package (observed from repository paths and static analysis). Observed top-level classes: VncComputer. Observed top-level functions: keysym. |
| computer-use-best-practices package | library | Observed | Groups 21 file(s) under computer-use-best-practices package (observed from repository paths and static analysis). Observed top-level classes: BashTool, BrowserBatchTool, BrowserTool, ComputerBatchTool, ComputerTool, Con… |
| computer-use-demo package | library | Observed | Groups 18 file(s) under computer-use-demo package (observed from repository paths and static analysis). Observed top-level classes: APIProvider, BaseAnthropicTool, BaseComputerTool, BashTool20241022, BashTool20250124, C… |
| Configuration and deployment | config | Observed | Groups 138 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: BreakerSettings, ConfigMissing, GatewaySettings, ProfileSettings, ReviewSettings, S… |
| customer-support-agent package | library | Observed | Groups 22 file(s) under customer-support-agent package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 26 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed routes: GET /, GET /meta, POST /localize, GET /, GET /tools… |
| External integrations | external | Observed | Groups 1 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level functions: create_client. |
| financial-data-analyst package | library | Observed | Groups 23 file(s) under financial-data-analyst package (observed from repository paths and static analysis). |
| managed-agents package | library | Observed | Groups 184 file(s) under managed-agents package (observed from repository paths and static analysis). Observed top-level classes: Bindings, CeilingError, Check, ClaudeReviewer, CliProver, Collector. Observed top-level f… |
| Tests | test | Observed | Groups 51 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH streamlit.session_state, PATCH streamlit.chat_message, PATCH streamlit.markdown, PATCH streamlit.write, PATCH st… |

## Important files

- `.github/workflows/build.yaml` (ci)
- `.github/workflows/openshell-policy.yaml` (ci)
- `.github/workflows/reusable_build_step.yaml` (ci)
- `.github/workflows/tests.yaml` (ci)
- `.pre-commit-config.yaml` (config)
- `autonomous-coding/requirements.txt` (manifest)
- `browser-toolset/python/requirements.txt` (manifest)
- `browser-toolset/typescript/package.json` (manifest)
- `browser-toolset/typescript/tsconfig.json` (config)
- `browser-use-demo/.dockerignore` (container)
- `browser-use-demo/.env.example` (config)
- `browser-use-demo/Dockerfile` (container)
- `browser-use-demo/browser_use_demo/requirements.txt` (manifest)
- `browser-use-demo/docker-compose.yml` (container)
- `browser-use-demo/pytest.ini` (config)
- `browser-use-demo/setup.py` (manifest)
- `computer-toolset/python/requirements.txt` (manifest)
- `computer-toolset/typescript/package.json` (manifest)
- `computer-toolset/typescript/tsconfig.json` (config)
- `computer-use-best-practices/.env.example` (config)
- `computer-use-best-practices/.vscode/launch.json` (config)
- `computer-use-best-practices/.vscode/settings.json` (config)
- `computer-use-best-practices/config.example.toml` (config)
- `computer-use-best-practices/dev_ui/assets/streamlit_theme.toml` (config)
- `computer-use-best-practices/pyproject.toml` (manifest)
- `computer-use-best-practices/requirements.txt` (manifest)
- `computer-use-demo/.zed/settings.json` (config)
- `computer-use-demo/Dockerfile` (container)
- `computer-use-demo/computer_use_demo/requirements.txt` (manifest)
- `computer-use-demo/image/.streamlit/config.toml` (config)
- `computer-use-demo/pyproject.toml` (manifest)
- `computer-use-demo/ruff.toml` (config)
- `customer-support-agent/.eslintrc.json` (config)
- `customer-support-agent/amplify.yml` (config)
- `customer-support-agent/app/lib/customer_support_categories.json` (config)
- `customer-support-agent/components.json` (config)
- `customer-support-agent/package.json` (manifest)
- `customer-support-agent/tsconfig.json` (config)
- `financial-data-analyst/.eslintrc.json` (config)
- `financial-data-analyst/components.json` (config)
- `financial-data-analyst/package.json` (manifest)
- `financial-data-analyst/tsconfig.json` (config)
- `managed-agents/assistant-ui/.env.example` (config)
- `managed-agents/assistant-ui/components.json` (config)
- `managed-agents/assistant-ui/environments/spreadsheet-analyst.yaml` (config)
- `managed-agents/assistant-ui/package.json` (manifest)
- `managed-agents/assistant-ui/tsconfig.json` (config)
- `managed-agents/chat-sdk/.env.example` (config)
- `managed-agents/chat-sdk/package.json` (manifest)
- `managed-agents/chat-sdk/tsconfig.json` (config)
- `managed-agents/copilot-kit-ag-ui/.env.example` (config)
- `managed-agents/copilot-kit-ag-ui/environments/financial-assistant.yaml` (config)
- `managed-agents/copilot-kit-ag-ui/package.json` (manifest)
- `managed-agents/copilot-kit-ag-ui/server/package.json` (manifest)
- `managed-agents/copilot-kit-ag-ui/server/tsconfig.json` (config)
- `managed-agents/copilot-kit-ag-ui/web/package.json` (manifest)
- `managed-agents/copilot-kit-ag-ui/web/tsconfig.json` (config)
- `managed-agents/daily-brief/.env.example` (config)
- `managed-agents/daily-brief/agents/daily-brief/environment.yaml` (config)
- `managed-agents/daily-brief/agents/daily-brief/memory_store_preferences.yaml` (config)
- `managed-agents/daily-brief/agents/daily-brief/memory_store_state.yaml` (config)
- `managed-agents/daily-brief/agents/daily-brief/vault.yaml` (config)
- `managed-agents/daily-brief/slack/manifest.yaml` (config)
- `managed-agents/knowledge-wiki/manifest_core.json` (config)
- `managed-agents/knowledge-wiki/manifest_full.json` (config)
- `managed-agents/knowledge-wiki/manifest_mini.json` (config)
- `managed-agents/knowledge-wiki/manifest_quickstart.json` (config)
- `managed-agents/knowledge-wiki/manifest_standard.json` (config)
- `managed-agents/knowledge-wiki/requirements.txt` (manifest)
- `managed-agents/linear/.env.example` (config)
- `managed-agents/linear/environments/linear-assistant.yaml` (config)
- `managed-agents/linear/package.json` (manifest)
- `managed-agents/linear/tsconfig.json` (config)
- `managed-agents/mcp-server-typescript/.dockerignore` (container)
- `managed-agents/mcp-server-typescript/.env.example` (config)
- `managed-agents/mcp-server-typescript/Dockerfile` (container)
- `managed-agents/mcp-server-typescript/environment.yaml` (config)
- `managed-agents/mcp-server-typescript/package.json` (manifest)
- `managed-agents/mcp-server-typescript/tsconfig.json` (config)
- `managed-agents/roadtrip-planner/.env.example` (config)
- `managed-agents/roadtrip-planner/environments/roadtrip-planner.yaml` (config)
- `managed-agents/roadtrip-planner/package.json` (manifest)
- `managed-agents/roadtrip-planner/tsconfig.json` (config)
- `managed-agents/roadtrip-planner/vaults/roadtrip-planner.yaml` (config)
- `managed-agents/self-hosted-sandboxes/archil/.env.example` (config)
- `managed-agents/self-hosted-sandboxes/archil/environments/self-hosted.yaml` (config)
- `managed-agents/self-hosted-sandboxes/archil/requirements.txt` (manifest)
- `managed-agents/self-hosted-sandboxes/cloudflare-containers/container/Dockerfile` (container)
- `managed-agents/self-hosted-sandboxes/cloudflare-containers/package.json` (manifest)
- `managed-agents/self-hosted-sandboxes/cloudflare-containers/tsconfig.json` (config)
- `managed-agents/self-hosted-sandboxes/cloudflare-containers/wrangler.toml` (config)
- `managed-agents/self-hosted-sandboxes/cloudflare-worker/package.json` (manifest)
- `managed-agents/self-hosted-sandboxes/cloudflare-worker/tsconfig.json` (config)
- `managed-agents/self-hosted-sandboxes/cloudflare-worker/wrangler.toml` (config)
- `managed-agents/self-hosted-sandboxes/docker-memory/.env.example` (config)
- `managed-agents/self-hosted-sandboxes/docker-memory/Dockerfile` (container)
- `managed-agents/self-hosted-sandboxes/docker-memory/environments/self-hosted.yaml` (config)
- `managed-agents/self-hosted-sandboxes/docker-memory/memory_stores/user-preferences.yaml` (config)
- `managed-agents/self-hosted-sandboxes/docker/.env.example` (config)
- `managed-agents/self-hosted-sandboxes/docker/Dockerfile` (container)
- `managed-agents/self-hosted-sandboxes/docker/environments/self-hosted.yaml` (config)
- `managed-agents/self-hosted-sandboxes/openshell-policy/.env.example` (config)
- `managed-agents/self-hosted-sandboxes/openshell-policy/agentpolicy.yaml` (config)
- `managed-agents/self-hosted-sandboxes/openshell-policy/environments/reviewer.yaml` (config)
- `managed-agents/self-hosted-sandboxes/openshell-policy/environments/worker.yaml` (config)
- `managed-agents/self-hosted-sandboxes/openshell-policy/ops/Dockerfile` (container)
- `managed-agents/self-hosted-sandboxes/openshell-policy/ops/requirements.txt` (manifest)
- `managed-agents/self-hosted-sandboxes/openshell-policy/policy/base.yaml` (config)
- `managed-agents/self-hosted-sandboxes/openshell-policy/policy/profiles/hello/ceiling.yaml` (config)
- `managed-agents/self-hosted-sandboxes/openshell-policy/policy/profiles/hello/policy.yaml` (config)
- `managed-agents/self-hosted-sandboxes/openshell-policy/policy/signers.yaml` (config)
- `managed-agents/self-hosted-sandboxes/openshell-policy/pyproject.toml` (manifest)
- `managed-agents/self-hosted-sandboxes/openshell-policy/sandbox/Dockerfile` (container)
- `managed-agents/self-hosted-sandboxes/openshell-policy/stack/openshell/docker-compose.yml` (container)
- `managed-agents/self-hosted-sandboxes/openshell-policy/stack/openshell/gateway.toml` (config)
- `managed-agents/self-hosted-sandboxes/openshell/.env.example` (config)
- `managed-agents/self-hosted-sandboxes/openshell/Dockerfile` (container)
- `managed-agents/self-hosted-sandboxes/openshell/environments/self-hosted.yaml` (config)
- `managed-agents/self-hosted-sandboxes/openshell/policy.yaml` (config)
- `managed-agents/self-hosted-sandboxes/vercel/.env.example` (config)
- `managed-agents/self-hosted-sandboxes/vercel/package.json` (manifest)
- `managed-agents/self-hosted-sandboxes/vercel/tsconfig.json` (config)
- `managed-agents/self-hosted-sandboxes/vercel/vercel.json` (config)
- `managed-agents/self-hosted-sandboxes/webhook-demo/environments/webhook-demo.yaml` (config)
- `managed-agents/sentry-autofix/.claude/settings.json` (config)
- `managed-agents/sentry-autofix/.env.example` (config)
- `managed-agents/sentry-autofix/agents/issue-fixer/agent.yaml` (config)
- `managed-agents/sentry-autofix/agents/issue-fixer/environment.yaml` (config)
- `managed-agents/sentry-autofix/agents/issue-fixer/vault.yaml` (config)
- `managed-agents/sentry-autofix/demo-app/package.json` (manifest)
- `managed-agents/sentry-autofix/package.json` (manifest)
- `managed-agents/sentry-autofix/tsconfig.json` (config)
- `managed-agents/sentry/.claude/settings.json` (config)
- `managed-agents/sentry/.env.example` (config)
- `managed-agents/sentry/environments/sentry-triage.yaml` (config)
- `managed-agents/sentry/pyproject.toml` (manifest)
- `managed-agents/sentry/vaults/sentry-triage.yaml` (config)
- `managed-agents/slack/.env.example` (config)
- `managed-agents/slack/environments/slack-assistant.yaml` (config)
- `managed-agents/slack/package.json` (manifest)
- `managed-agents/slack/tsconfig.json` (config)
- `pyproject.toml` (manifest)

## Top-level layout

- `managed-agents` — 450 analysed file(s)
- `computer-use-best-practices` — 57 analysed file(s)
- `browser-use-demo` — 52 analysed file(s)
- `computer-use-demo` — 45 analysed file(s)
- `customer-support-agent` — 38 analysed file(s)
- `financial-data-analyst` — 34 analysed file(s)
- `agents` — 18 analysed file(s)
- `autonomous-coding` — 13 analysed file(s)
- `browser-toolset` — 11 analysed file(s)
- `computer-toolset` — 11 analysed file(s)
- `(root files)` — 5 analysed file(s)
- `.github` — 5 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `4a4224bdf0e9cfb3332167b69c90457403813625` is the revision these paths and observations refer to.
