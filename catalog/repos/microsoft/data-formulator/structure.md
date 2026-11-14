# Project structure: microsoft/data-formulator

**Analysed commit:** `5477f0e236426dc8f74a498ec400414fba7fbc0f`

**Commit reference:** [5477f0e236426dc8f74a498ec400414fba7fbc0f](https://github.com/microsoft/data-formulator/commit/5477f0e236426dc8f74a498ec400414fba7fbc0f)

**Tree at this commit:** [microsoft/data-formulator@5477f0e23642](https://github.com/microsoft/data-formulator/tree/5477f0e236426dc8f74a498ec400414fba7fbc0f)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | microsoft/data-formulator |
| Description | 🪄 Data Formulator is an interactive AI-powered data analysis system makes it easy to connect, explore and visualize data. |
| Stars | 17682 |
| Forks | 1745 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `5477f0e236426dc8f74a498ec400414fba7fbc0f` |
| Retrieved at | 2026-11-14T19:08:32.721564+00:00 |
| Files in this snapshot | 642 |

## Directory tree

```text
.claude/  (1 files)
  settings.json
.cursor/  (17 files)
  rules/  (14 files)
    backend-test-conventions.mdc
    dataframe-serialization.mdc
    dev-guides-first.mdc
    error-response-safety.mdc
    frontend-test-conventions.mdc
    i18n-no-hardcoded-strings.mdc
    implementation-review-checklist.mdc
    incremental-development-cadence.mdc
    language-injection-conventions.mdc
    log-sanitization.mdc
    package-manager-conventions.mdc
    path-safety.mdc
    test-driven-workflow.mdc
    unified-error-protocol.mdc
  skills/  (3 files)
    error-handling/  (1 files)
      … 1 files under this directory
    language-injection/  (1 files)
      … 1 files under this directory
    path-safety/  (1 files)
      … 1 files under this directory
.devcontainer/  (1 files)
  devcontainer.json
.github/  (4 files)
  workflows/  (2 files)
    desktop-build.yml
    python-build.yml
  copilot-instructions.md
  dependabot.yml
.vscode/  (3 files)
  launch.json
  settings.json
  tasks.json
docs/  (23 files)
  dev-guides/  (15 files)
    1-streaming-protocol.md
    10-agent-knowledge-reasoning-log.md
    11-catalog-metadata-sync.md
    12-sandbox-session.md
    13-unified-row-limits.md
    14-model-capability-runtime-degradation.md
    15-dataframe-serialization.md
    2-log-sanitization.md
    3-data-loader-development.md
    4-authentication-oidc-tokenstore.md
    5-data-connector-api.md
    6-i18n-language-injection.md
    7-unified-error-handling.md
    8-path-safety.md
    9-workspace-storage-architecture.md
  docs-cn/  (7 files)
    config-examples/  (2 files)
      … 2 files under this directory
    1-data-source-connections.md
    5-datasource_plugin-development-guide.md
    5.1-superset-sso-oauth-config-guide.md
    6-credential-vault.md
    7-server-migration-guide.md
  desktop-portable.md
examples/  (2 files)
  plugins/  (2 files)
    README.md
    sqlite_data_loader.py
loops/  (1 files)
  model-evaluation/  (1 files)
    plan.md
packaging/  (2 files)
  data_formulator_desktop.py
  data_formulator_desktop.spec
public/  (4 files)
  demos/  (1 files)
    demos.yaml
  manifest.json
  pip-logo.svg
  robots.txt
py-src/  (149 files)
  data_formulator/  (149 files)
    agents/  (18 files)
      … 18 files under this directory
    analyst/  (20 files)
      … 20 files under this directory
    auth/  (16 files)
      … 16 files under this directory
    data_loader/  (37 files)
      … 37 files under this directory
    data_operations/  (6 files)
      … 6 files under this directory
    datalake/  (14 files)
      … 14 files under this directory
    knowledge/  (2 files)
      … 2 files under this directory
    routes/  (9 files)
      … 9 files under this directory
    sandbox/  (6 files)
      … 6 files under this directory
    security/  (6 files)
      … 6 files under this directory
    workflows/  (3 files)
      … 3 files under this directory
    __init__.py
    __main__.py
    _startup_spinner.py
    agent_config.py
    app.py
    data_connector.py
    desktop.py
    error_handler.py
    errors.py
    example_datasets_config.py
    model_registry.py
    workspace_factory.py
src/  (183 files)
  api/  (1 files)
    knowledgeApi.ts
  app/  (35 files)
    App.tsx
    AuthButton.tsx
    IdentityMigrationDialog.tsx
    LayoutProvider.tsx
    OidcCallback.tsx
    agentInteractionPolicy.ts
    apiClient.ts
    chartCache.ts
    chartRecommendation.ts
    clarification.ts
    connectorFormPersistence.ts
    connectorNames.ts
    dfSlice.tsx
    displayRowsCache.ts
    errorCodes.ts
    errorHandler.ts
    identity.ts
    inputTablePreviewCache.ts
    intentClassifier.ts
    layout.ts
    loadableState.ts
    oidcConfig.ts
    restyle.ts
    stateMigrations.ts
    … 11 more files
  assets/  (41 files)
    chart-icon-area.svg
    chart-icon-bar-table.svg
    chart-icon-box-plot.svg
    chart-icon-bullet.svg
    chart-icon-bump.svg
    chart-icon-candlestick.svg
    chart-icon-column-grouped.svg
    chart-icon-column-stacked.svg
    chart-icon-column.svg
    chart-icon-connected-scatter.svg
    chart-icon-custom-area.svg
    chart-icon-custom-bar.svg
    chart-icon-custom-line.svg
    chart-icon-custom-point.svg
    chart-icon-custom-rect.svg
    chart-icon-density.svg
    chart-icon-dot-plot-horizontal.svg
    chart-icon-dotted-line.svg
    chart-icon-ecdf.svg
    chart-icon-gantt.svg
    chart-icon-heat-map.svg
    chart-icon-histogram.svg
    chart-icon-kpi-card.svg
    chart-icon-line.svg
    … 17 more files
  components/  (17 files)
    AnvilLoader.tsx
    CatalogTree.tsx
    ChartTemplates.tsx
    ComponentType.tsx
    ConnectorFormCard.tsx
    ConnectorTablePreview.tsx
    DataOperationCard.tsx
    DndTypes.ts
    FunComponents.tsx
    LoadPlanCard.tsx
    MarkdownEditor.tsx
    ResizeHandle.tsx
    RotatingTextBlock.tsx
    ScrollFade.tsx
    TablePreviewRow.tsx
    VirtualizedCatalogTree.tsx
    filterFormat.ts
  data/  (4 files)
    column.ts
    table.ts
    types.ts
    utils.ts
  dataOperations/  (1 files)
    models.ts
  i18n/  (26 files)
    locales/  (23 files)
      … 23 files under this directory
    TRANSLATION_GUIDE.md
    index.ts
    vega-locale.ts
  scss/  (5 files)
    App.scss
    DataView.scss
    DraggableCard.scss
    EncodingShelf.scss
    VisualizationView.scss
  views/  (48 files)
    About.tsx
    AgentChatInput.tsx
    AgentPausePanel.tsx
    AgentRulesDialog.tsx
    AgentToyIcon.tsx
    ChartQuickConfig.tsx
    ChartRenderService.tsx
    ChartUtils.tsx
    ChartVariantStrip.tsx
    ChartifactDialog.tsx
    ChatDialog.tsx
    ColumnFilterPopover.tsx
    DBTableManager.tsx
    DataFormulator.tsx
    DataFrameTable.tsx
    DataLoadingChat.tsx
    DataSourceSidebar.tsx
    DataThread.tsx
    DataThreadCards.tsx
    DataView.tsx
    EncodingBox.tsx
    EncodingShelfCard.tsx
    EncodingShelfThread.tsx
    ExampleSessions.tsx
    … 24 more files
  icons.tsx
  index.css
  index.tsx
  mui.d.ts
  types.d.ts
tests/  (225 files)
  backend/  (134 files)
    agents/  (22 files)
      … 22 files under this directory
    auth/  (17 files)
      … 17 files under this directory
    benchmarks/  (2 files)
      … 2 files under this directory
    data/  (38 files)
      … 38 files under this directory
    data_loader/  (5 files)
      … 5 files under this directory
    data_operations/  (3 files)
      … 3 files under this directory
    errors/  (4 files)
      … 4 files under this directory
    fixtures/  (3 files)
      … 3 files under this directory
    knowledge/  (2 files)
      … 2 files under this directory
    routes/  (20 files)
      … 20 files under this directory
    security/  (14 files)
      … 14 files under this directory
    README.md
    test_desktop_single_instance.py
    test_model_endpoints.py
    test_startup_spinner.py
  database-dockers/  (41 files)
    bigquery/  (6 files)
      … 6 files under this directory
    cosmosdb/  (6 files)
      … 6 files under this directory
    mongodb/  (6 files)
      … 6 files under this directory
    mysql/  (7 files)
      … 7 files under this directory
    postgres/  (6 files)
      … 6 files under this directory
    superset/  (7 files)
      … 7 files under this directory
    README.md
    docker-compose.test.yml
    test-dbs.ps1
  frontend/  (47 files)
    unit/  (45 files)
      … 45 files under this directory
    README.md
    setup.ts
  README.md
  conftest.py
  test_plan.md
.dockerignore
.env.template
.gitignore
.python-version
CHANGELOG.md
CODESPACES.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
DEVELOPMENT.md
Dockerfile
LICENSE
MANIFEST.in
README.md
SECURITY.md
SUPPORT.md
docker-compose.yml
eslint.config.js
index.html
local_server.bat
local_server.sh
package.json
pyproject.toml
pytest.ini
requirements.txt
… 3 more files
```

## Entry points

- [py-src/data_formulator/__main__.py:3](https://github.com/microsoft/data-formulator/blob/5477f0e236426dc8f74a498ec400414fba7fbc0f/py-src/data_formulator/__main__.py#L3)
- [py-src/data_formulator/app.py:49](https://github.com/microsoft/data-formulator/blob/5477f0e236426dc8f74a498ec400414fba7fbc0f/py-src/data_formulator/app.py#L49)
- [py-src/data_formulator/desktop.py:296](https://github.com/microsoft/data-formulator/blob/5477f0e236426dc8f74a498ec400414fba7fbc0f/py-src/data_formulator/desktop.py#L296)
- [src/app/App.tsx](https://github.com/microsoft/data-formulator/blob/5477f0e236426dc8f74a498ec400414fba7fbc0f/src/app/App.tsx)
- [src/i18n/index.ts](https://github.com/microsoft/data-formulator/blob/5477f0e236426dc8f74a498ec400414fba7fbc0f/src/i18n/index.ts)
- [src/i18n/locales/index.ts](https://github.com/microsoft/data-formulator/blob/5477f0e236426dc8f74a498ec400414fba7fbc0f/src/i18n/locales/index.ts)
- [src/index.tsx](https://github.com/microsoft/data-formulator/blob/5477f0e236426dc8f74a498ec400414fba7fbc0f/src/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 62 file(s) under api layer (observed from repository paths and static analysis). Observed routes: ROUTE /login, ROUTE /callback, ROUTE /logout, ROUTE /login, ROUTE /callback. Observed top-level classes: DataConne… |
| app package | library | Observed | Groups 35 file(s) under app package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 17 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 46 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 5 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: ConnectorQueryStep, DataOperation, DataOperationPlan, DataOperationStatus, FailedOperationStep, LoadQue… |
| dataOperations package | library | Observed | Groups 1 file(s) under dataoperations package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 3 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Flask. Observed routes: ROUTE /, ROUTE /api/auth/info, ROUTE /api/app-config.… |
| External integrations | external | Observed | Groups 2 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: SupersetClient. |
| i18n package | library | Observed | Groups 5 file(s) under i18n package (observed from repository paths and static analysis). |
| icons.tsx package | library | Observed | Groups 1 file(s) under icons.tsx package (observed from repository paths and static analysis). |
| index.tsx package | library | Observed | Groups 1 file(s) under index.tsx package (observed from repository paths and static analysis). |
| mui.d.ts package | library | Observed | Groups 1 file(s) under mui.d.ts package (observed from repository paths and static analysis). |
| packaging package | library | Observed | Groups 1 file(s) under packaging package (observed from repository paths and static analysis). |
| py-src package | library | Observed | Groups 104 file(s) under py-src package (observed from repository paths and static analysis). Observed top-level classes: AgentDiagnostics, AnalystAgent, AppError, AthenaDataLoader, AuthProvider, AuthResult. Observed to… |
| Service / domain layer | service | Observed | Groups 2 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: CoreSkill. Observed top-level functions: get_skill. |
| Tests | test | Observed | Groups 214 file(s) under tests (observed from repository paths and static analysis). Observed application object created via Flask. Observed routes: PATCH data_formulator.agents.client_utils.litellm, PATCH data_formulat… |
| types.d.ts package | library | Observed | Groups 1 file(s) under types.d.ts package (observed from repository paths and static analysis). |

## Important files

- `.claude/settings.json` (config)
- `.devcontainer/devcontainer.json` (config)
- `.dockerignore` (container)
- `.env.template` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/desktop-build.yml` (ci)
- `.github/workflows/python-build.yml` (ci)
- `.vscode/launch.json` (config)
- `.vscode/settings.json` (config)
- `.vscode/tasks.json` (config)
- `Dockerfile` (container)
- `MANIFEST.in` (manifest)
- `docker-compose.yml` (container)
- `package.json` (manifest)
- `public/demos/demos.yaml` (config)
- `public/manifest.json` (config)
- `py-src/data_formulator/analyst/skills/core/tools.json` (config)
- `py-src/data_formulator/analyst/skills/data-loading/tools.json` (config)
- `py-src/data_formulator/analyst/skills/data_loading/tools.json` (config)
- `py-src/data_formulator/analyst/skills/report/tools.json` (config)
- `py-src/data_formulator/sandbox/Dockerfile.sandbox` (container)
- `pyproject.toml` (manifest)
- `pytest.ini` (config)
- `requirements.txt` (manifest)
- `src/i18n/locales/en/chart.json` (config)
- `src/i18n/locales/en/common.json` (config)
- `src/i18n/locales/en/dataLoading.json` (config)
- `src/i18n/locales/en/encoding.json` (config)
- `src/i18n/locales/en/errors.json` (config)
- `src/i18n/locales/en/loader.json` (config)
- `src/i18n/locales/en/messages.json` (config)
- `src/i18n/locales/en/model.json` (config)
- `src/i18n/locales/en/navigation.json` (config)
- `src/i18n/locales/en/upload.json` (config)
- `src/i18n/locales/zh/chart.json` (config)
- `src/i18n/locales/zh/common.json` (config)
- `src/i18n/locales/zh/dataLoading.json` (config)
- `src/i18n/locales/zh/encoding.json` (config)
- `src/i18n/locales/zh/errors.json` (config)
- `src/i18n/locales/zh/loader.json` (config)
- `src/i18n/locales/zh/messages.json` (config)
- `src/i18n/locales/zh/model.json` (config)
- `src/i18n/locales/zh/navigation.json` (config)
- `src/i18n/locales/zh/upload.json` (config)
- `tests/database-dockers/bigquery/Dockerfile` (container)
- `tests/database-dockers/bigquery/docker-compose.yml` (container)
- `tests/database-dockers/cosmosdb/Dockerfile` (container)
- `tests/database-dockers/cosmosdb/docker-compose.yml` (container)
- `tests/database-dockers/mongodb/Dockerfile` (container)
- `tests/database-dockers/mongodb/docker-compose.yml` (container)
- `tests/database-dockers/mysql/Dockerfile` (container)
- `tests/database-dockers/mysql/docker-compose.yml` (container)
- `tests/database-dockers/postgres/Dockerfile` (container)
- `tests/database-dockers/postgres/docker-compose.yml` (container)
- `tests/database-dockers/superset/docker-compose.yml` (container)
- `tsconfig.json` (config)

## Top-level layout

- `tests` — 225 analysed file(s)
- `src` — 183 analysed file(s)
- `py-src` — 149 analysed file(s)
- `(root files)` — 27 analysed file(s)
- `docs` — 23 analysed file(s)
- `.cursor` — 17 analysed file(s)
- `.github` — 4 analysed file(s)
- `public` — 4 analysed file(s)
- `.vscode` — 3 analysed file(s)
- `examples` — 2 analysed file(s)
- `packaging` — 2 analysed file(s)
- `.claude` — 1 analysed file(s)
- `.devcontainer` — 1 analysed file(s)
- `loops` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `5477f0e236426dc8f74a498ec400414fba7fbc0f` is the revision these paths and observations refer to.
