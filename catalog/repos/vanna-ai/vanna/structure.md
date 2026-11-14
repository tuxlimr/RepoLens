# Project structure: vanna-ai/vanna

**Analysed commit:** `365d0617c1a4567ffee1b19b40c27feb4206bfcf`

**Commit reference:** [365d0617c1a4567ffee1b19b40c27feb4206bfcf](https://github.com/vanna-ai/vanna/commit/365d0617c1a4567ffee1b19b40c27feb4206bfcf)

**Tree at this commit:** [vanna-ai/vanna@365d0617c1a4](https://github.com/vanna-ai/vanna/tree/365d0617c1a4567ffee1b19b40c27feb4206bfcf)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | vanna-ai/vanna |
| Description | 🤖 Chat with your SQL database 📊. Accurate Text-to-SQL Generation via LLMs using Agentic Retrieval 🔄. |
| Stars | 23800 |
| Forks | 2548 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `365d0617c1a4567ffee1b19b40c27feb4206bfcf` |
| Retrieved at | 2026-11-14T19:07:43.954403+00:00 |
| Files in this snapshot | 355 |

## Directory tree

```text
.github/  (4 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (2 files)
    python-publish.yaml
    tests.yml
examples/  (2 files)
  chromadb_gpu_example.py
  transform_args_example.py
frontends/  (36 files)
  webcomponent/  (36 files)
    .storybook/  (3 files)
      … 3 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    src/  (25 files)
      … 25 files under this directory
    TEST_README.md
    package.json
    requirements-test.txt
    test-comprehensive.html
    test_backend.py
    tsconfig.json
    vite.config.ts
img/  (1 files)
  vanna2.svg
notebooks/  (1 files)
  quickstart.ipynb
papers/  (1 files)
  ai-sql-accuracy-2023-08-17.md
src/  (285 files)
  evals/  (2 files)
    benchmarks/  (1 files)
      … 1 files under this directory
    datasets/  (1 files)
      … 1 files under this directory
  vanna/  (283 files)
    agents/  (1 files)
      … 1 files under this directory
    capabilities/  (10 files)
      … 10 files under this directory
    components/  (27 files)
      … 27 files under this directory
    core/  (58 files)
      … 58 files under this directory
    examples/  (22 files)
      … 22 files under this directory
    integrations/  (65 files)
      … 65 files under this directory
    legacy/  (75 files)
      … 75 files under this directory
    servers/  (15 files)
      … 15 files under this directory
    tools/  (6 files)
      … 6 files under this directory
    utils/  (1 files)
      … 1 files under this directory
    web_components/  (1 files)
      … 1 files under this directory
    __init__.py
    py.typed
tests/  (14 files)
  conftest.py
  test_agent_memory.py
  test_agent_memory_sanity.py
  test_agents.py
  test_azureopenai_llm.py
  test_chromadb_persistence_fix.py
  test_database_sanity.py
  test_gemini_integration.py
  test_legacy_adapter.py
  test_llm_context_enhancer.py
  test_memory_tools.py
  test_ollama_direct.py
  test_tool_permissions.py
  test_workflow.py
.gitattributes
.gitignore
.pre-commit-config.yaml
CONTRIBUTING.md
LICENSE
MIGRATION_GUIDE.md
README.md
README_LEGACY.md
pyproject.toml
setup.cfg
tox.ini
```

## Entry points

- [src/evals/benchmarks/llm_comparison.py:171](https://github.com/vanna-ai/vanna/blob/365d0617c1a4567ffee1b19b40c27feb4206bfcf/src/evals/benchmarks/llm_comparison.py#L171)
- [src/vanna/core/validation.py:145](https://github.com/vanna-ai/vanna/blob/365d0617c1a4567ffee1b19b40c27feb4206bfcf/src/vanna/core/validation.py#L145)
- [src/vanna/servers/__main__.py:7](https://github.com/vanna-ai/vanna/blob/365d0617c1a4567ffee1b19b40c27feb4206bfcf/src/vanna/servers/__main__.py#L7)
- [src/vanna/servers/cli/server_runner.py](https://github.com/vanna-ai/vanna/blob/365d0617c1a4567ffee1b19b40c27feb4206bfcf/src/vanna/servers/cli/server_runner.py)
- [src/vanna/servers/fastapi/app.py:38](https://github.com/vanna-ai/vanna/blob/365d0617c1a4567ffee1b19b40c27feb4206bfcf/src/vanna/servers/fastapi/app.py#L38)
- [src/vanna/servers/flask/app.py:40](https://github.com/vanna-ai/vanna/blob/365d0617c1a4567ffee1b19b40c27feb4206bfcf/src/vanna/servers/flask/app.py#L40)
- [frontends/webcomponent/.storybook/main.ts](https://github.com/vanna-ai/vanna/blob/365d0617c1a4567ffee1b19b40c27feb4206bfcf/frontends/webcomponent/.storybook/main.ts)
- [frontends/webcomponent/src/index.ts](https://github.com/vanna-ai/vanna/blob/365d0617c1a4567ffee1b19b40c27feb4206bfcf/frontends/webcomponent/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 8 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: AgentConfig, AuditConfig, UiFeature, UiFeatures. |
| Data layer | data | Observed | Groups 16 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AiResponseEvent, AuditEvent, AuditEventType, ChartComponent, ChatRequest, ChatResponse. |
| Application entry point | entrypoint | Observed | Groups 26 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI, Flask. Observed top-level classes: ArtifactDemoAgent, AuthArgs, Auth… |
| External integrations | external | Observed | Groups 65 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: AnthropicLlmService, AzureAISearchAgentMemory, AzureOpenAILlmService, BigQueryRunner, Chrom… |
| frontends package | library | Observed | Groups 28 file(s) under frontends package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 48 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: Agent, AgentError, AgentResult, AgentVariant, AuditLogger, ComparisonReport. |
| Tests | test | Observed | Groups 16 file(s) under tests (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed routes: POST /api/vanna/v2/chat_sse, GET /health, GET /, PATCH vanna.integrat… |
| vanna package | library | Observed | Groups 128 file(s) under vanna package (observed from repository paths and static analysis). Observed top-level classes: APIError, AccuracyStats, AgentMemory, Anthropic_Chat, ApiKey, ArtifactComponent. Observed top-leve… |

## Important files

- `.github/workflows/python-publish.yaml` (ci)
- `.github/workflows/tests.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `frontends/webcomponent/package.json` (manifest)
- `frontends/webcomponent/requirements-test.txt` (manifest)
- `frontends/webcomponent/tsconfig.json` (config)
- `pyproject.toml` (manifest)
- `setup.cfg` (manifest)
- `src/evals/datasets/sql_generation/basic.yaml` (config)
- `tox.ini` (config)

## Top-level layout

- `src` — 285 analysed file(s)
- `frontends` — 36 analysed file(s)
- `tests` — 14 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `.github` — 4 analysed file(s)
- `examples` — 2 analysed file(s)
- `img` — 1 analysed file(s)
- `notebooks` — 1 analysed file(s)
- `papers` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- The GitHub repository was marked archived at selection time.

Commit `365d0617c1a4567ffee1b19b40c27feb4206bfcf` is the revision these paths and observations refer to.
