# Project structure: ValueCell-ai/valuecell

**Analysed commit:** `9793e9c0563fbf56fc096757d8bb80e209ac7aab`

**Commit reference:** [9793e9c0563fbf56fc096757d8bb80e209ac7aab](https://github.com/ValueCell-ai/valuecell/commit/9793e9c0563fbf56fc096757d8bb80e209ac7aab)

**Tree at this commit:** [ValueCell-ai/valuecell@9793e9c0563f](https://github.com/ValueCell-ai/valuecell/tree/9793e9c0563fbf56fc096757d8bb80e209ac7aab)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | ValueCell-ai/valuecell |
| Description | ValueCell is a community-driven, multi-agent platform for financial applications. |
| Stars | 11054 |
| Forks | 1806 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `9793e9c0563fbf56fc096757d8bb80e209ac7aab` |
| Retrieved at | 2026-11-14T19:13:27.436835+00:00 |
| Files in this snapshot | 523 |

## Directory tree

```text
.github/  (10 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    custom.md
    feature_request.md
  workflows/  (4 files)
    frontend.yml
    mac_build.yml
    python.yml
    win_build.yml
  CODE_OF_CONDUCT.md
  CONTRIBUTING.md
  PULL_REQUEST_TEMPLATE.md
.vscode/  (2 files)
  launch.json
  settings.json
docker/  (1 files)
  DockerFile
docs/  (3 files)
  CONFIGURATION_GUIDE.md
  CONTRIBUTE_AN_AGENT.md
  CORE_ARCHITECTURE.md
frontend/  (220 files)
  .vscode/  (1 files)
    settings.json
  public/  (1 files)
    logo.svg
  scripts/  (1 files)
    pre-build.sh
  src/  (193 files)
    api/  (6 files)
      … 6 files under this directory
    app/  (45 files)
      … 45 files under this directory
    assets/  (15 files)
      … 15 files under this directory
    components/  (85 files)
      … 85 files under this directory
    constants/  (5 files)
      … 5 files under this directory
    hooks/  (7 files)
      … 7 files under this directory
    i18n/  (5 files)
      … 5 files under this directory
    lib/  (6 files)
      … 6 files under this directory
    mock/  (1 files)
      … 1 files under this directory
    provider/  (2 files)
      … 2 files under this directory
    store/  (4 files)
      … 4 files under this directory
    types/  (8 files)
      … 8 files under this directory
    global.css
    root.tsx
    routes.ts
    vite-env.d.ts
  src-tauri/  (13 files)
    capabilities/  (2 files)
      … 2 files under this directory
    icons/  (2 files)
      … 2 files under this directory
    src/  (4 files)
      … 4 files under this directory
    .gitignore
    Cargo.toml
    build.rs
    hooks.nsh
    tauri.conf.json
  .env.example
  .gitignore
  README.md
  biome.json
  bun.lock
  components.json
  package.json
  react-router.config.ts
  tsconfig.json
  tsconfig.node.json
  vite.config.ts
python/  (274 files)
  configs/  (23 files)
    agent_cards/  (4 files)
      … 4 files under this directory
    agents/  (3 files)
      … 3 files under this directory
    locales/  (6 files)
      … 6 files under this directory
    providers/  (9 files)
      … 9 files under this directory
    config.yaml
  scripts/  (2 files)
    prepare_envs.ps1
    prepare_envs.sh
  valuecell/  (246 files)
    adapters/  (13 files)
      … 13 files under this directory
    agents/  (70 files)
      … 70 files under this directory
    config/  (4 files)
      … 4 files under this directory
    contrib/  (1 files)
      … 1 files under this directory
    core/  (78 files)
      … 78 files under this directory
    server/  (68 files)
      … 68 files under this directory
    tests/  (1 files)
      … 1 files under this directory
    utils/  (10 files)
      … 10 files under this directory
    __init__.py
  .python-version
  README.md
  pyproject.toml
.env.example
.gitignore
AGENTS.md
LICENSE
Makefile
README.ja.md
README.md
README.zh.md
README.zh_Hant.md
SECURITY.md
project.code-workspace
start.ps1
start.sh
```

## Entry points

- [python/valuecell/agents/news_agent/__main__.py:6](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/python/valuecell/agents/news_agent/__main__.py#L6)
- [python/valuecell/agents/prompt_strategy_agent/__main__.py:7](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/python/valuecell/agents/prompt_strategy_agent/__main__.py#L7)
- [python/valuecell/agents/research_agent/__main__.py:7](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/python/valuecell/agents/research_agent/__main__.py#L7)
- [python/valuecell/core/agent/listener.py:94](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/python/valuecell/core/agent/listener.py#L94)
- [python/valuecell/server/api/app.py:145](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/python/valuecell/server/api/app.py#L145)
- [python/valuecell/server/db/init_db.py:717](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/python/valuecell/server/db/init_db.py#L717)
- [python/valuecell/server/main.py:97](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/python/valuecell/server/main.py#L97)
- [frontend/src/i18n/index.ts](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/frontend/src/i18n/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 34 file(s) under api layer (observed from repository paths and static analysis). Observed top-level classes: APIException, AddAssetRequest, AddModelRequest, AgentCapabilities, AgentData, AgentEnableRequest. Obser… |
| Configuration and deployment | config | Observed | Groups 48 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: AgentConfig, AgentModelConfig, ConfigLoader, ConfigManager, I18nConfig, ProviderConf… |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 36 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AShareFilingMetadata, AShareFilingResult, Agent, Asset, AssetRepository, AzureProvider. Observed top-l… |
| Application entry point | entrypoint | Observed | Groups 7 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed top-level classes: DatabaseInitializer, NotificationListener… |
| External integrations | external | Observed | Groups 10 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: AKShareAdapter, AdapterCapability, AdapterManager, AgentClient, Asset, AssetI18nService. Ob… |
| frontend package | library | Observed | Groups 174 file(s) under frontend package (observed from repository paths and static analysis). |
| python package | library | Observed | Groups 68 file(s) under python package (observed from repository paths and static analysis). Observed top-level classes: BaseComposer, BaseDigestBuilder, BaseExecutionGateway, BaseFeaturesPipeline, BaseHistoryRecorder,… |
| Service / domain layer | service | Observed | Groups 48 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: AgentContext, AgentOrchestrator, AgentService, AgentServiceBundle, AgentStreamService, Ass… |
| Tests | test | Observed | Groups 40 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH valuecell.core.agent.card.get_agent_card_path, PATCH valuecell.core.agent.card.get_agent_card_path, PATCH valuec… |

## Important files

- `.env.example` (config)
- `.github/workflows/frontend.yml` (ci)
- `.github/workflows/mac_build.yml` (ci)
- `.github/workflows/python.yml` (ci)
- `.github/workflows/win_build.yml` (ci)
- `.vscode/launch.json` (config)
- `.vscode/settings.json` (config)
- `docker/DockerFile` (container)
- `frontend/.env.example` (config)
- `frontend/.vscode/settings.json` (config)
- `frontend/biome.json` (config)
- `frontend/components.json` (config)
- `frontend/package.json` (manifest)
- `frontend/src-tauri/Cargo.toml` (manifest)
- `frontend/src-tauri/capabilities/default.json` (config)
- `frontend/src-tauri/capabilities/desktop.json` (config)
- `frontend/src-tauri/tauri.conf.json` (config)
- `frontend/src/components/tradingview/tv-symbol-map.json` (config)
- `frontend/src/i18n/locales/en.json` (config)
- `frontend/src/i18n/locales/ja.json` (config)
- `frontend/src/i18n/locales/zh_CN.json` (config)
- `frontend/src/i18n/locales/zh_TW.json` (config)
- `frontend/tsconfig.json` (config)
- `frontend/tsconfig.node.json` (config)
- `python/configs/agent_cards/grid_agent.json` (config)
- `python/configs/agent_cards/investment_research_agent.json` (config)
- `python/configs/agent_cards/news_agent.json` (config)
- `python/configs/agent_cards/prompt_strategy_agent.json` (config)
- `python/configs/agents/news_agent.yaml` (config)
- `python/configs/agents/research_agent.yaml` (config)
- `python/configs/agents/super_agent.yaml` (config)
- `python/configs/config.yaml` (config)
- `python/configs/locales/en-GB.json` (config)
- `python/configs/locales/en-US.json` (config)
- `python/configs/locales/ja-JP.json` (config)
- `python/configs/locales/language_list.json` (config)
- `python/configs/locales/zh-Hans.json` (config)
- `python/configs/locales/zh-Hant.json` (config)
- `python/configs/providers/azure.yaml` (config)
- `python/configs/providers/dashscope.yaml` (config)
- `python/configs/providers/deepseek.yaml` (config)
- `python/configs/providers/google.yaml` (config)
- `python/configs/providers/ollama.yaml` (config)
- `python/configs/providers/openai-compatible.yaml` (config)
- `python/configs/providers/openai.yaml` (config)
- `python/configs/providers/openrouter.yaml` (config)
- `python/configs/providers/siliconflow.yaml` (config)
- `python/pyproject.toml` (manifest)

## Top-level layout

- `python` — 274 analysed file(s)
- `frontend` — 220 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `.github` — 10 analysed file(s)
- `docs` — 3 analysed file(s)
- `.vscode` — 2 analysed file(s)
- `docker` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `9793e9c0563fbf56fc096757d8bb80e209ac7aab` is the revision these paths and observations refer to.
