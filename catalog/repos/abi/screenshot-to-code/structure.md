# Project structure: abi/screenshot-to-code

**Analysed commit:** `0a77981c6eb4a4f4450690f21e4addc93522da9e`

**Commit reference:** [0a77981c6eb4a4f4450690f21e4addc93522da9e](https://github.com/abi/screenshot-to-code/commit/0a77981c6eb4a4f4450690f21e4addc93522da9e)

**Tree at this commit:** [abi/screenshot-to-code@0a77981c6eb4](https://github.com/abi/screenshot-to-code/tree/0a77981c6eb4a4f4450690f21e4addc93522da9e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | abi/screenshot-to-code |
| Description | Drop in a screenshot and convert it to clean code (HTML/Tailwind/React/Vue) |
| Stars | 81207 |
| Forks | 9948 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `0a77981c6eb4a4f4450690f21e4addc93522da9e` |
| Retrieved at | 2026-11-14T19:06:09.988136+00:00 |
| Files in this snapshot | 301 |

## Directory tree

```text
.claude/  (1 files)
  launch.json
.github/  (4 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    custom.md
    feature_request.md
  FUNDING.yml
.vscode/  (1 files)
  settings.json
.zed/  (1 files)
  tasks.json
backend/  (142 files)
  agent/  (21 files)
    providers/  (9 files)
      … 9 files under this directory
    tools/  (9 files)
      … 9 files under this directory
    engine.py
    runner.py
    state.py
  codegen/  (3 files)
    __init__.py
    test_utils.py
    utils.py
  costs/  (3 files)
    __init__.py
    pricing.py
    token_usage.py
  debug/  (2 files)
    DebugFileWriter.py
    __init__.py
  evals/  (8 files)
    __init__.py
    asset_extraction_benchmark.py
    config.py
    core.py
    runner.py
    sessions.py
    sets.py
    utils.py
  fs_logging/  (5 files)
    __init__.py
    agent_runs.py
    openai_input_compare.py
    openai_input_formatting.py
    prompt_reports.py
  image_generation/  (4 files)
    __init__.py
    core.py
    generation.py
    replicate.py
  preview_screenshot/  (4 files)
    __init__.py
    base.py
    playwright_backend.py
    registry.py
  prompts/  (16 files)
    create/  (4 files)
      … 4 files under this directory
    update/  (3 files)
      … 3 files under this directory
    __init__.py
    design_system.py
    message_builder.py
    pipeline.py
    plan.py
    policies.py
    prompt_types.py
    request_parsing.py
    system_prompt.py
  routes/  (11 files)
    agent_runs.py
    capabilities.py
    design_systems.py
    eval_sets.py
    evals.py
    export.py
    generate_code.py
    home.py
    model_choice_sets.py
    prompt_reports.py
    screenshot.py
  tests/  (40 files)
    __init__.py
    test_agent_engine.py
    test_agent_runs.py
    test_agent_tool_runtime.py
    test_agent_tools.py
    test_anthropic_many_image_limit.py
    test_anthropic_provider_config.py
    test_asset_extraction.py
    test_asset_extraction_benchmark.py
    test_babel_cdn.py
    test_batching.py
    test_capabilities.py
    test_codegen_utils.py
    test_design_systems.py
    test_eval_runner.py
    test_eval_sessions.py
    test_eval_sets.py
    test_evals_openai_input_compare.py
    test_export.py
    test_gemini_provider_config.py
    test_gemini_provider_session.py
    test_image_generation_replicate.py
    test_local_assets.py
    test_model_selection.py
    … 16 more files
  uploaded_assets/  (4 files)
    __init__.py
    prompts.py
    store.py
    tools.py
  video/  (2 files)
    __init__.py
    utils.py
  ws/  (2 files)
    __init__.py
    constants.py
  .gitignore
  .pre-commit-config.yaml
  Dockerfile
  README.md
  asset_extraction.py
  babel_cdn.py
  config.py
  custom_types.py
  llm.py
  main.py
  pyproject.toml
  pyrightconfig.json
  pytest.ini
  run_evals.py
  run_image_generation_evals.py
  start.py
  utils.py
blog/  (1 files)
  evaluating-claude.md
design-docs/  (7 files)
  agent-tool-calling-flow.md
  agentic-runner-refactor.md
  commits-and-variants.md
  general.md
  images-in-update-history.md
  prompt-history-refactor.md
  variant-system.md
frontend/  (131 files)
  public/  (1 files)
    legal/  (1 files)
      … 1 files under this directory
  src/  (117 files)
    components/  (89 files)
      … 89 files under this directory
    hooks/  (4 files)
      … 4 files under this directory
    lib/  (9 files)
      … 9 files under this directory
    store/  (3 files)
      … 3 files under this directory
    tests/  (2 files)
      … 2 files under this directory
    App.tsx
    config.ts
    constants.ts
    generateCode.ts
    index.css
    main.tsx
    setupTests.ts
    types.ts
    urls.ts
    vite-env.d.ts
  .env.example
  .eslintrc.cjs
  .gitignore
  Dockerfile
  components.json
  index.html
  jest.config.js
  package.json
  postcss.config.js
  tailwind.config.js
  tsconfig.json
  tsconfig.node.json
  vite.config.ts
scripts/  (1 files)
  cursor-cloud-install.sh
.gitattributes
.gitignore
AGENTS.md
Evaluation.md
LICENSE
QA.md
README.md
TESTING.md
Troubleshooting.md
docker-compose.yml
package.json
plan.md
```

## Entry points

- [backend/evals/asset_extraction_benchmark.py:864](https://github.com/abi/screenshot-to-code/blob/0a77981c6eb4a4f4450690f21e4addc93522da9e/backend/evals/asset_extraction_benchmark.py#L864)
- [backend/main.py:24](https://github.com/abi/screenshot-to-code/blob/0a77981c6eb4a4f4450690f21e4addc93522da9e/backend/main.py#L24)
- [backend/run_evals.py:14](https://github.com/abi/screenshot-to-code/blob/0a77981c6eb4a4f4450690f21e4addc93522da9e/backend/run_evals.py#L14)
- [backend/run_image_generation_evals.py:305](https://github.com/abi/screenshot-to-code/blob/0a77981c6eb4a4f4450690f21e4addc93522da9e/backend/run_image_generation_evals.py#L305)
- [backend/start.py:29](https://github.com/abi/screenshot-to-code/blob/0a77981c6eb4a4f4450690f21e4addc93522da9e/backend/start.py#L29)
- [frontend/src/App.tsx](https://github.com/abi/screenshot-to-code/blob/0a77981c6eb4a4f4450690f21e4addc93522da9e/frontend/src/App.tsx)
- [frontend/src/main.tsx](https://github.com/abi/screenshot-to-code/blob/0a77981c6eb4a4f4450690f21e4addc93522da9e/frontend/src/main.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 11 file(s) under api layer (observed from repository paths and static analysis). Observed routes: GET /agent-runs, GET /agent-runs/{run_id}, GET /agent-runs/{run_id}/output, GET /agent-runs/{run_id}/assets/{filen… |
| backend package | library | Observed | Groups 76 file(s) under backend package (observed from repository paths and static analysis). Observed top-level classes: Agent, AgentEngine, AgentFileState, AgentRunRecorder, AgentToolRuntime, AnthropicParseState. Obse… |
| Configuration and deployment | config | Observed | Groups 21 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 5 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed top-level classes: BenchmarkFixture, BenchmarkTarget, EvalRe… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| frontend package | library | Observed | Groups 109 file(s) under frontend package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 4 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 43 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: ExpectedResult, NoToolProviderSession, TestAccumulate, TestAnthropicExtract, TestCacheHitRate, TestCost. Ob… |

## Important files

- `.claude/launch.json` (config)
- `.github/FUNDING.yml` (config)
- `.vscode/settings.json` (config)
- `.zed/tasks.json` (config)
- `backend/.pre-commit-config.yaml` (config)
- `backend/Dockerfile` (container)
- `backend/pyproject.toml` (manifest)
- `backend/pyrightconfig.json` (config)
- `backend/pytest.ini` (config)
- `docker-compose.yml` (container)
- `frontend/.env.example` (config)
- `frontend/Dockerfile` (container)
- `frontend/components.json` (config)
- `frontend/package.json` (manifest)
- `frontend/tsconfig.json` (config)
- `frontend/tsconfig.node.json` (config)
- `package.json` (manifest)

## Top-level layout

- `backend` — 142 analysed file(s)
- `frontend` — 131 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `design-docs` — 7 analysed file(s)
- `.github` — 4 analysed file(s)
- `.claude` — 1 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `.zed` — 1 analysed file(s)
- `blog` — 1 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `0a77981c6eb4a4f4450690f21e4addc93522da9e` is the revision these paths and observations refer to.
