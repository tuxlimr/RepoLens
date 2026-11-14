# Project structure: NVIDIA/auto-ontology

**Analysed commit:** `8ff3060a29bb8cb7c301ecf3945fc0a5fab009eb`

**Commit reference:** [8ff3060a29bb8cb7c301ecf3945fc0a5fab009eb](https://github.com/NVIDIA/auto-ontology/commit/8ff3060a29bb8cb7c301ecf3945fc0a5fab009eb)

**Tree at this commit:** [NVIDIA/auto-ontology@8ff3060a29bb](https://github.com/NVIDIA/auto-ontology/tree/8ff3060a29bb8cb7c301ecf3945fc0a5fab009eb)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | NVIDIA/auto-ontology |
| Description | Auto Ontology is a Python framework for building semantic, graph-based reasoning layers over data. It enables deterministic query generation, better context retrieval, and more explainable AI for LLM and agent workflows. |
| Stars | 12796 |
| Forks | 1071 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `8ff3060a29bb8cb7c301ecf3945fc0a5fab009eb` |
| Retrieved at | 2026-11-14T19:09:59.592560+00:00 |
| Files in this snapshot | 799 |

## Directory tree

```text
.cursor/  (1 files)
  rules/  (1 files)
    frontend-formatting.md
.github/  (18 files)
  ISSUE_TEMPLATE/  (1 files)
    integration.yml
  actions/  (3 files)
    determine-release-version/  (1 files)
      … 1 files under this directory
    docker-login-ngc/  (1 files)
      … 1 files under this directory
    setup-docker-buildx/  (1 files)
      … 1 files under this directory
  workflows/  (13 files)
    ci-client.yml
    ci-mcp.yml
    ci-openapi.yml
    ci-python.yml
    publish-api-docs.yml
    release-all.yml
    release-docker.yml
    release-helm.yml
    request-nvskills-ci.yml
    staging-publish-chart.yml
    staging-publish-frontend.yml
    staging-publish-image.yml
    staging-publish-mcp.yml
  CODEOWNERS
.vscode/  (1 files)
  launch.json
alembic/  (13 files)
  versions/  (10 files)
    47ffb7499dfa_trigram_index_on_tag_name_for_global_.py
    6347ede6dac1_add_pii_processed_to_catalog_columns.py
    7d864cacef9c_add_term_families.py
    84dd4f50dbba_add_catalog_column_distinct_ratio.py
    99d4d343dd0b_add_semantic_fk_join_path_default.py
    b3aed65e49b7_add_pii_processed_to_attributes.py
    c778a7d94c20_create_the_auto_ontology_schema.py
    caee572fa81c_add_catalog_column_distinct_values.py
    e4850fd803d6_add_user_groups.py
    f3a91c0e5b27_add_owner_id.py
  README
  env.py
  script.py.mako
auto_ontology/  (454 files)
  catalog/  (38 files)
    model/  (4 files)
      … 4 files under this directory
    parsers/  (4 files)
      … 4 files under this directory
    services/  (2 files)
      … 2 files under this directory
    store/  (11 files)
      … 11 files under this directory
    tests/  (7 files)
      … 7 files under this directory
    __init__.py
    constants.py
    diff.py
    extract.py
    ingest.py
    normalize.py
    query_stats.py
    sql_parse.py
    table_filter.py
    write.py
  connectors/  (33 files)
    tests/  (16 files)
      … 16 files under this directory
    __init__.py
    base.py
    clickhouse.py
    connection_string_factory.py
    databricks.py
    databricks_oauth.py
    db_errors.py
    duckdb.py
    heavydb.py
    kyuubi.py
    mysql.py
    postgres.py
    registry.py
    snowflake.py
    sqlite.py
    trino.py
    vault.py
  dal/  (51 files)
    tests/  (26 files)
      … 26 files under this directory
    __init__.py
    attributes.py
    candidates.py
    connections.py
    custom_analyses.py
    datasources.py
    exploration.py
    groups.py
    model_interchange.py
    owners.py
    pii.py
    pql_analyses.py
    reset.py
    rules.py
    schema.py
    schema_version.py
    search.py
    session.py
    sql_attributes.py
    sql_fragments.py
    tags.py
    term_families.py
    terms.py
    users.py
    … 1 more files
  infra/  (5 files)
    tests/  (2 files)
      … 2 files under this directory
    __init__.py
    feature_flags.py
    postgres.py
  ingestion_service/  (16 files)
    tests/  (4 files)
      … 4 files under this directory
    __init__.py
    __main__.py
    config.py
    connections.py
    data_scheduler.py
    history.py
    ingest.py
    pii.py
    router.py
    rules.py
    scheduler.py
    semantic_scheduler.py
  pii_detection/  (7 files)
    tests/  (2 files)
      … 2 files under this directory
    __init__.py
    detector.py
    models.py
    rules.py
    service.py
  retrieval/  (137 files)
    data_access/  (10 files)
      … 10 files under this directory
    entity_coverage/  (9 files)
      … 9 files under this directory
    interactive/  (14 files)
      … 14 files under this directory
    kumo/  (20 files)
      … 20 files under this directory
    text_to_sql/  (83 files)
      … 83 files under this directory
    __init__.py
  semantic/  (41 files)
    prompts/  (2 files)
      … 2 files under this directory
    tests/  (17 files)
      … 17 files under this directory
    __init__.py
    __main__.py
    attribute_descriptions.py
    bridge_tables.py
    cancellation.py
    compile.py
    constants.py
    date_format.py
    deterministic.py
    domain.py
    embed.py
    fk_suggester.py
    fk_values.py
    loaders.py
    models.py
    pipeline.py
    semantic_fk.py
    sql_attribute_suggester.py
    term_extractor.py
    term_families.py
    unmatched_fks.py
    visit_enter.py
  server/  (87 files)
    chat/  (10 files)
      … 10 files under this directory
    connections/  (4 files)
      … 4 files under this directory
    custom_analyses/  (3 files)
      … 3 files under this directory
    datasources/  (4 files)
      … 4 files under this directory
    exploration/  (3 files)
      … 3 files under this directory
    health/  (3 files)
      … 3 files under this directory
    ingestion/  (2 files)
      … 2 files under this directory
    metadata/  (3 files)
      … 3 files under this directory
    model_interchange/  (6 files)
      … 6 files under this directory
    pql_analyses/  (2 files)
      … 2 files under this directory
    rules/  (5 files)
      … 5 files under this directory
    search/  (6 files)
      … 6 files under this directory
    semantic_compilation/  (2 files)
      … 2 files under this directory
    sql_attributes/  (4 files)
      … 4 files under this directory
    tags/  (3 files)
      … 3 files under this directory
    terms/  (4 files)
      … 4 files under this directory
    tests/  (3 files)
      … 3 files under this directory
    users/  (8 files)
      … 8 files under this directory
    zones/  (4 files)
      … 4 files under this directory
    __init__.py
    __main__.py
    identity.py
    models.py
    owners.py
    pagination.py
    responses.py
    sql_utils.py
  tests/  (11 files)
    interactive/  (4 files)
      … 4 files under this directory
    __init__.py
    conftest.py
    test_case_dirty_join_check.py
    test_empty_result_retry.py
    test_jsonb_path_check.py
    test_literal_check.py
    test_table_without_columns_validation.py
  utils/  (20 files)
    tests/  (9 files)
      … 9 files under this directory
    __init__.py
    catalog_reembed.py
    column_types.py
    embedding.py
    embedding_rows.py
    llm_invoke.py
    model_config.py
    rerank.py
    retriever.py
    sample_values.py
    sql_identifiers.py
  vdb/  (5 files)
    tests/  (2 files)
      … 2 files under this directory
    __init__.py
    postgres.py
    records.py
  __init__.py
  env.py
  version.py
dev_tools/  (22 files)
  fixtures/  (11 files)
    sql/  (3 files)
      … 3 files under this directory
    tests/  (2 files)
      … 2 files under this directory
    __init__.py
    build_sqlite_fixtures.py
    capture_dal_golden.py
    seed_fixtures.py
    seed_graph_fixture.py
    seed_local_postgres.py
  tests/  (3 files)
    __init__.py
    test_licensing.py
    test_packaging.py
  README.md
  __init__.py
  _add_spdx_headers.py
  generate_backend_openapi.py
  generate_permission_resource.py
  local_ingest.py
  release_helm_chart.py
  setup_env.sh
docs/  (6 files)
  openapi/  (2 files)
    README.md
    ingestion.json
  authentication.md
  connections.md
  conversation-api.md
  mcp.md
frontend/  (263 files)
  adapters/  (1 files)
    ui/  (1 files)
      … 1 files under this directory
  api/  (24 files)
    analyses.ts
    analytics.ts
    apiTokens.ts
    auth.ts
    chat.ts
    connections.ts
    conversations.ts
    datasources.ts
    exploration.ts
    groups.ts
    invitations.ts
    modelInterchange.ts
    owners.ts
    pqlAnalyses.ts
    requests.ts
    rules.ts
    search.ts
    settings.ts
    sqlAttributes.ts
    tags.ts
    terms.ts
    types.ts
    users.ts
    zones.ts
  app/  (161 files)
    .well-known/  (1 files)
      … 1 files under this directory
    account/  (2 files)
      … 2 files under this directory
    admin/  (1 files)
      … 1 files under this directory
    analysis/  (2 files)
      … 2 files under this directory
    analytics/  (2 files)
      … 2 files under this directory
    api/  (109 files)
      … 109 files under this directory
    chat/  (2 files)
      … 2 files under this directory
    data/  (2 files)
      … 2 files under this directory
    discovery/  (2 files)
      … 2 files under this directory
    exploration/  (1 files)
      … 1 files under this directory
    invite/  (2 files)
      … 2 files under this directory
    login/  (1 files)
      … 1 files under this directory
    oauth/  (3 files)
      … 3 files under this directory
    settings/  (27 files)
      … 27 files under this directory
    terms/  (1 files)
      … 1 files under this directory
    globals.css
    layout.tsx
    page.tsx
  assets/  (1 files)
    images/  (1 files)
      … 1 files under this directory
  auth/  (16 files)
    access.json
    api-token.ts
    auth-access.ts
    auth-client.ts
    auth-guards.ts
    auth.ts
    bearer.ts
    exact-admin.ts
    oauth-loopback.ts
    oauth-token.ts
    permissions.ts
    proxy-backend.ts
    resolve-user.ts
    seed-admin.ts
    sso-token.ts
    with-auth.ts
  common/  (45 files)
    Button/  (4 files)
      … 4 files under this directory
    DataTreeSelect/  (2 files)
      … 2 files under this directory
    EmptyState/  (2 files)
      … 2 files under this directory
    FileUpload/  (2 files)
      … 2 files under this directory
    ProgressBar/  (2 files)
      … 2 files under this directory
    Toggle/  (2 files)
      … 2 files under this directory
    AppTopBar.tsx
    BackPanelLayout.tsx
    Breadcrumbs.tsx
    CertificationBadge.tsx
    CertificationSelect.tsx
    DetailLinkButton.tsx
    GlobalSearch.tsx
    GlobalSearchResults.tsx
    GlobalSearchTabs.tsx
    InfiniteScroll.tsx
    Label.tsx
    NavRail.tsx
    OwnerLabel.tsx
    OwnersSelect.tsx
    Popover.tsx
    PopoverMenu.tsx
    PropertyRow.tsx
    RuleTagPopover.tsx
    SearchInput.tsx
    SidePanel.tsx
    SinglePageComposer.tsx
    SinglePageView.tsx
    Skeleton.tsx
    Spinner.tsx
    … 7 more files
  .dockerignore
  .eslintrc.json
  .gitignore
  .prettierignore
  .prettierrc
  .prettierrc.license
  AGENTS.md
  CLAUDE.md
  CONTAINER_THIRD_PARTY_NOTICES.md
  Dockerfile
  LICENSE
  OPEN_SOURCE_NOTICE
  OPEN_SOURCE_NOTICE.license
  README.md
  THIRD_PARTY_NOTICES.md
.coderabbit.yaml
.dockerignore
.env.example
.gitignore
.python-version
AGENTS.md
CLAUDE.md
CODE_OF_CONDUCT.md
CONTAINER_THIRD_PARTY_NOTICES.md
CONTRIBUTING.md
DEPLOYMENT.md
Dockerfile
LICENSE
Makefile
OPEN_SOURCE_NOTICE
OPEN_SOURCE_NOTICE.license
README.md
SECURITY.md
THIRD_PARTY_NOTICES.md
alembic.ini
docker-compose.yml
```

## Entry points

- [auto_ontology/ingestion_service/__main__.py:92](https://github.com/NVIDIA/auto-ontology/blob/8ff3060a29bb8cb7c301ecf3945fc0a5fab009eb/auto_ontology/ingestion_service/__main__.py#L92)
- [auto_ontology/semantic/__main__.py:48](https://github.com/NVIDIA/auto-ontology/blob/8ff3060a29bb8cb7c301ecf3945fc0a5fab009eb/auto_ontology/semantic/__main__.py#L48)
- [auto_ontology/server/__main__.py:81](https://github.com/NVIDIA/auto-ontology/blob/8ff3060a29bb8cb7c301ecf3945fc0a5fab009eb/auto_ontology/server/__main__.py#L81)
- [dev_tools/_add_spdx_headers.py:92](https://github.com/NVIDIA/auto-ontology/blob/8ff3060a29bb8cb7c301ecf3945fc0a5fab009eb/dev_tools/_add_spdx_headers.py#L92)
- [dev_tools/fixtures/build_sqlite_fixtures.py:88](https://github.com/NVIDIA/auto-ontology/blob/8ff3060a29bb8cb7c301ecf3945fc0a5fab009eb/dev_tools/fixtures/build_sqlite_fixtures.py#L88)
- [dev_tools/fixtures/capture_dal_golden.py:776](https://github.com/NVIDIA/auto-ontology/blob/8ff3060a29bb8cb7c301ecf3945fc0a5fab009eb/dev_tools/fixtures/capture_dal_golden.py#L776)
- [dev_tools/fixtures/seed_fixtures.py:39](https://github.com/NVIDIA/auto-ontology/blob/8ff3060a29bb8cb7c301ecf3945fc0a5fab009eb/dev_tools/fixtures/seed_fixtures.py#L39)
- [dev_tools/fixtures/seed_graph_fixture.py:552](https://github.com/NVIDIA/auto-ontology/blob/8ff3060a29bb8cb7c301ecf3945fc0a5fab009eb/dev_tools/fixtures/seed_graph_fixture.py#L552)
- [dev_tools/fixtures/seed_local_postgres.py:150](https://github.com/NVIDIA/auto-ontology/blob/8ff3060a29bb8cb7c301ecf3945fc0a5fab009eb/dev_tools/fixtures/seed_local_postgres.py#L150)
- [dev_tools/generate_backend_openapi.py:53](https://github.com/NVIDIA/auto-ontology/blob/8ff3060a29bb8cb7c301ecf3945fc0a5fab009eb/dev_tools/generate_backend_openapi.py#L53)
- [dev_tools/generate_permission_resource.py:27](https://github.com/NVIDIA/auto-ontology/blob/8ff3060a29bb8cb7c301ecf3945fc0a5fab009eb/dev_tools/generate_permission_resource.py#L27)
- [dev_tools/local_ingest.py:53](https://github.com/NVIDIA/auto-ontology/blob/8ff3060a29bb8cb7c301ecf3945fc0a5fab009eb/dev_tools/local_ingest.py#L53)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| alembic package | library | Observed | Groups 11 file(s) under alembic package (observed from repository paths and static analysis). Observed top-level functions: _configure, downgrade, include_object, run_migrations_offline, run_migrations_online, upgrade. |
| API layer | api | Observed | Groups 148 file(s) under api layer (observed from repository paths and static analysis). Observed routes: GET /health, GET /health/live, POST /ingest, POST /ingest/delete, POST /semantic/reset. Observed top-level classe… |
| auto_ontology package | library | Observed | Groups 238 file(s) under auto_ontology package (observed from repository paths and static analysis). Observed top-level classes: AgentExecutionError, AgentPayload, AgentState, AskUserAction, BaseAgent, Budget. Observed… |
| Configuration and deployment | config | Observed | Groups 38 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: _float_env, _int_env, is_db_probe_join_path_check, is_db_probe_jsonb_path_check, i… |
| Data layer | data | Observed | Groups 10 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AnchorColumnModel, ApiModel, AutoOntologyModelDocument, CandidateFilterModel, ColumnAttribute, ColumnA… |
| dev_tools package | library | Observed | Groups 4 file(s) under dev_tools package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 15 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed top-level classes: AgentRunError, Capture, Fixture, SqliteF… |
| External integrations | external | Observed | Groups 1 file(s) under external integrations (observed from repository paths and static analysis). |
| frontend package | library | Observed | Groups 83 file(s) under frontend package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 14 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: PiiPropagationResult, PiiTaggingResult, PredictionFlowError, SearchValidationError, _Prepa… |
| Tests | test | Observed | Groups 173 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH auto_ontology.retrieval.text_to_sql.agents.sql_parse_validation._JOINS_VALIDATED_ELSEWHERE, PATCH auto_ontology… |

## Important files

- `.coderabbit.yaml` (config)
- `.dockerignore` (container)
- `.env.example` (config)
- `.github/ISSUE_TEMPLATE/integration.yml` (config)
- `.github/actions/determine-release-version/action.yml` (config)
- `.github/actions/docker-login-ngc/action.yml` (config)
- `.github/actions/setup-docker-buildx/action.yml` (config)
- `.github/workflows/ci-client.yml` (ci)
- `.github/workflows/ci-mcp.yml` (ci)
- `.github/workflows/ci-openapi.yml` (ci)
- `.github/workflows/ci-python.yml` (ci)
- `.github/workflows/publish-api-docs.yml` (ci)
- `.github/workflows/release-all.yml` (ci)
- `.github/workflows/release-docker.yml` (ci)
- `.github/workflows/release-helm.yml` (ci)
- `.github/workflows/request-nvskills-ci.yml` (ci)
- `.github/workflows/staging-publish-chart.yml` (ci)
- `.github/workflows/staging-publish-frontend.yml` (ci)
- `.github/workflows/staging-publish-image.yml` (ci)
- `.github/workflows/staging-publish-mcp.yml` (ci)
- `.vscode/launch.json` (config)
- `Dockerfile` (container)
- `alembic.ini` (config)
- `auto_ontology/retrieval/text_to_sql/agents/calculation_subtypes.json` (config)
- `auto_ontology/server/users/access.json` (config)
- `docker-compose.yml` (container)
- `docs/openapi/ingestion.json` (config)
- `frontend/.dockerignore` (container)
- `frontend/.eslintrc.json` (config)
- `frontend/Dockerfile` (container)
- `frontend/auth/access.json` (config)

## Top-level layout

- `auto_ontology` — 454 analysed file(s)
- `frontend` — 263 analysed file(s)
- `dev_tools` — 22 analysed file(s)
- `(root files)` — 21 analysed file(s)
- `.github` — 18 analysed file(s)
- `alembic` — 13 analysed file(s)
- `docs` — 6 analysed file(s)
- `.cursor` — 1 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `8ff3060a29bb8cb7c301ecf3945fc0a5fab009eb` is the revision these paths and observations refer to.
