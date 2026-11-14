# Project structure: getzep/graphiti

**Analysed commit:** `ed23196506eba8806fae6da831d73fcd2ad714d8`

**Commit reference:** [ed23196506eba8806fae6da831d73fcd2ad714d8](https://github.com/getzep/graphiti/commit/ed23196506eba8806fae6da831d73fcd2ad714d8)

**Tree at this commit:** [getzep/graphiti@ed23196506eb](https://github.com/getzep/graphiti/tree/ed23196506eba8806fae6da831d73fcd2ad714d8)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | getzep/graphiti |
| Description | Build Real-Time Knowledge Graphs for AI Agents |
| Stars | 32808 |
| Forks | 3373 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `ed23196506eba8806fae6da831d73fcd2ad714d8` |
| Retrieved at | 2026-11-14T19:07:02.293765+00:00 |
| Files in this snapshot | 412 |

## Directory tree

```text
.github/  (37 files)
  ISSUE_TEMPLATE/  (5 files)
    01-bug.yml
    02-feature.yml
    03-docs.yml
    04-question.yml
    config.yml
  actions/  (3 files)
    openai-workload-identity/  (1 files)
      … 1 files under this directory
    setup-socket-firewall/  (2 files)
      … 2 files under this directory
  intake/  (10 files)
    templates/  (6 files)
      … 6 files under this directory
    README.md
    apply.py
    decide.py
    decision.schema.json
  scripts/  (1 files)
    setup-triage-labels.sh
  workflows/  (15 files)
    ai-moderator.yml
    cla.yml
    codeql.yml
    issue-intake.yml
    lint.yml
    mcp-server-tests.yml
    pr-intake.yml
    release-graphiti-core.yml
    release-mcp-server.yml
    release-server-container.yml
    server-tests.yml
    socket-firewall-connectivity.yml
    stale.yml
    typecheck.yml
    unit_tests.yml
  copilot-instructions.md
  dependabot.yml
  pull_request_template.md
examples/  (30 files)
  azure-openai/  (3 files)
    .env.example
    README.md
    azure_openai_neo4j.py
  data/  (1 files)
    manybirds_products.json
  ecommerce/  (1 files)
    runner.py
  gliner2/  (3 files)
    .env.example
    README.md
    gliner2_neo4j.py
  jev/  (3 files)
    .env.example
    README.md
    jev_dedupe_falkordb.py
  langgraph-agent/  (1 files)
    agent.ipynb
  openai_decisions/  (3 files)
    .env.example
    README.md
    openai_decisions_dedupe_falkordb.py
  opentelemetry/  (4 files)
    .env.example
    README.md
    otel_stdout_example.py
    pyproject.toml
  podcast/  (3 files)
    podcast_runner.py
    podcast_transcript.txt
    transcript_parser.py
  quickstart/  (6 files)
    README.md
    dense_vs_normal_ingestion.py
    quickstart_falkordb.py
    quickstart_neo4j.py
    quickstart_neptune.py
    requirements.txt
  wizard_of_oz/  (2 files)
    parser.py
    runner.py
graphiti_core/  (167 files)
  cross_encoder/  (5 files)
    __init__.py
    bge_reranker_client.py
    client.py
    gemini_reranker_client.py
    openai_reranker_client.py
  driver/  (77 files)
    falkordb/  (14 files)
      … 14 files under this directory
    graph_operations/  (1 files)
      … 1 files under this directory
    kuzu/  (14 files)
      … 14 files under this directory
    neo4j/  (13 files)
      … 13 files under this directory
    neptune/  (13 files)
      … 13 files under this directory
    operations/  (13 files)
      … 13 files under this directory
    search_interface/  (1 files)
      … 1 files under this directory
    __init__.py
    driver.py
    falkordb_driver.py
    kuzu_driver.py
    neo4j_driver.py
    neptune_driver.py
    query_executor.py
    record_parsers.py
  embedder/  (6 files)
    __init__.py
    azure_openai.py
    client.py
    gemini.py
    openai.py
    voyage.py
  llm_client/  (20 files)
    __init__.py
    anthropic_client.py
    azure_openai_client.py
    cache.py
    client.py
    config.py
    decision_prompts.py
    errors.py
    gemini_client.py
    gliner2_client.py
    groq_client.py
    jev_client.py
    llm_runtime.py
    openai_base_client.py
    openai_client.py
    openai_decisions_client.py
    openai_generic_client.py
    prompt_config.py
    token_tracker.py
    utils.py
  migrations/  (1 files)
    __init__.py
  models/  (5 files)
    edges/  (2 files)
      … 2 files under this directory
    nodes/  (2 files)
      … 2 files under this directory
    __init__.py
  namespaces/  (3 files)
    __init__.py
    edges.py
    nodes.py
  prompts/  (14 files)
    __init__.py
    dedupe_edges.py
    dedupe_nodes.py
    eval.py
    extract_edges.py
    extract_nodes.py
    extract_nodes_and_edges.py
    lib.py
    models.py
    names.py
    prompt_helpers.py
    snippets.py
    summarize_nodes.py
    summarize_sagas.py
  search/  (7 files)
    __init__.py
    search.py
    search_config.py
    search_config_recipes.py
    search_filters.py
    search_helpers.py
    search_utils.py
  telemetry/  (2 files)
    __init__.py
    telemetry.py
  utils/  (16 files)
    maintenance/  (10 files)
      … 10 files under this directory
    ontology_utils/  (1 files)
      … 1 files under this directory
    __init__.py
    bulk_utils.py
    content_chunking.py
    datetime_utils.py
    text_utils.py
  __init__.py
  decorators.py
  edges.py
  errors.py
  graph_queries.py
  graphiti.py
  graphiti_types.py
  helpers.py
  nodes.py
  py.typed
  tracer.py
images/  (1 files)
  simple_graph.svg
mcp_server/  (59 files)
  config/  (5 files)
    config-docker-falkordb-combined.yaml
    config-docker-falkordb.yaml
    config-docker-neo4j.yaml
    config.yaml
    mcp_config_stdio_example.json
  docker/  (10 files)
    Dockerfile
    Dockerfile.standalone
    README-falkordb-combined.md
    README.md
    build-standalone.sh
    build-with-version.sh
    docker-compose-falkordb.yml
    docker-compose-neo4j.yml
    docker-compose.yml
    github-actions-example.yml
  docs/  (1 files)
    cursor_rules.md
  src/  (15 files)
    config/  (2 files)
      … 2 files under this directory
    models/  (4 files)
      … 4 files under this directory
    services/  (3 files)
      … 3 files under this directory
    utils/  (4 files)
      … 4 files under this directory
    __init__.py
    graphiti_mcp_server.py
  tests/  (22 files)
    README.md
    __init__.py
    conftest.py
    pytest.ini
    run_tests.py
    test_async_operations.py
    test_comprehensive_integration.py
    test_configuration.py
    test_core_parity.py
    test_cross_encoder_factory.py
    test_factories.py
    test_falkordb_config.py
    test_falkordb_integration.py
    test_fixtures.py
    test_group_routing.py
    test_http_integration.py
    test_integration.py
    test_live_falkordb_int.py
    test_mcp_integration.py
    test_mcp_transports.py
    test_stdio_simple.py
    test_stress_load.py
  .env.example
  .python-version
  README.md
  main.py
  pyproject.toml
  pytest.ini
server/  (16 files)
  graph_service/  (11 files)
    dto/  (4 files)
      … 4 files under this directory
    routers/  (3 files)
      … 3 files under this directory
    __init__.py
    config.py
    main.py
    zep_graphiti.py
  tests/  (1 files)
    test_live_falkordb_int.py
  .env.example
  Makefile
  README.md
  pyproject.toml
signatures/  (1 files)
  version1/  (1 files)
    cla.json
spec/  (7 files)
  c2-default-extraction-prompt.md
  configurable-prompts-tests.yaml
  configurable-prompts.md
  driver-operations-redesign.md
  jev-decision-client.md
  llm-runtime.md
  openai-decisions-client.md
tests/  (74 files)
  cross_encoder/  (2 files)
    test_bge_reranker_client_int.py
    test_gemini_reranker_client.py
  driver/  (4 files)
    __init__.py
    test_falkordb_driver.py
    test_falkordb_ops_routing.py
    test_neo4j_driver_routing.py
  embedder/  (4 files)
    embedder_fixtures.py
    test_gemini.py
    test_openai.py
    test_voyage.py
  evals/  (5 files)
    data/  (1 files)
      … 1 files under this directory
    eval_cli.py
    eval_e2e_graph_building.py
    pytest.ini
    utils.py
  intake/  (3 files)
    test_apply.py
    test_decide.py
    test_workflows.py
  llm_client/  (15 files)
    decision_prompt_fixture.json
    test_anthropic_client.py
    test_anthropic_client_int.py
    test_azure_openai_client.py
    test_cache.py
    test_client.py
    test_errors.py
    test_gemini_client.py
    test_gliner2_delegation.py
    test_jev_client.py
    test_llm_runtime.py
    test_openai_client.py
    test_openai_decisions_client.py
    test_openai_generic_client.py
    test_token_tracker.py
  prompts/  (5 files)
    test_complete_prompt.py
    test_configurable_prompt_library.py
    test_legacy_prompt_compatibility.py
    test_prompt_exports.py
    test_prompt_names.py
  utils/  (19 files)
    maintenance/  (11 files)
      … 11 files under this directory
    search/  (6 files)
      … 6 files under this directory
    test_concatenate_episodes.py
    test_content_chunking.py
  e2e_prompt_library_ingest.py
  helpers_test.py
  test_add_triplet.py
  test_edge_db_queries.py
  test_edge_int.py
  test_entity_exclusion_int.py
  test_graphiti_configurable_prompts.py
  test_graphiti_int.py
  test_graphiti_mock.py
  test_handle_multiple_group_ids.py
  test_neptune_search_isolation.py
  test_node_int.py
  test_node_label_security.py
  test_request_scope_concurrency.py
  test_saga_refetch_episode_uuids.py
  test_saga_summary_budget.py
  test_text_utils.py
.env.example
.gitignore
AGENTS.md
CLAUDE.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
Dockerfile
LICENSE
Makefile
OTEL_TRACING.md
README.md
SECURITY.md
Zep-CLA.md
conftest.py
depot.json
docker-compose.test.yml
docker-compose.yml
py.typed
pyproject.toml
pytest.ini
```

## Entry points

- [mcp_server/src/graphiti_mcp_server.py:1378](https://github.com/getzep/graphiti/blob/ed23196506eba8806fae6da831d73fcd2ad714d8/mcp_server/src/graphiti_mcp_server.py#L1378)
- [.github/intake/apply.py:546](https://github.com/getzep/graphiti/blob/ed23196506eba8806fae6da831d73fcd2ad714d8/.github/intake/apply.py#L546)
- [.github/intake/decide.py:461](https://github.com/getzep/graphiti/blob/ed23196506eba8806fae6da831d73fcd2ad714d8/.github/intake/decide.py#L461)
- [mcp_server/main.py:22](https://github.com/getzep/graphiti/blob/ed23196506eba8806fae6da831d73fcd2ad714d8/mcp_server/main.py#L22)
- [server/graph_service/main.py:20](https://github.com/getzep/graphiti/blob/ed23196506eba8806fae6da831d73fcd2ad714d8/server/graph_service/main.py#L20)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 3 file(s) under api layer (observed from repository paths and static analysis). Observed routes: POST /messages, POST /entity-node, DELETE /entity-edge/{uuid}, DELETE /group/{group_id}, DELETE /episode/{uuid}. Ob… |
| Configuration and deployment | config | Observed | Groups 28 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: AnthropicProviderConfig, AzureOpenAIProviderConfig, DatabaseConfig, DatabaseProvider… |
| Data layer | data | Observed | Groups 10 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: BuildCommunitiesResponse, ChatPrompt, CommunityResult, Document, EdgeResult, EpisodeEntitiesResponse.… |
| Application entry point | entrypoint | Observed | Groups 3 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed routes: GET /healthcheck. Observed top-level classes: Graphi… |
| External integrations | external | Observed | Groups 16 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: AnthropicClient, AzureOpenAILLMClient, BGERerankerClient, BaseOpenAIClient, CrossEncoderCli… |
| graphiti_core package | library | Observed | Groups 143 file(s) under graphiti_core package (observed from repository paths and static analysis). Observed top-level classes: AddBulkEpisodeResults, AddEpisodeResults, AddTripletResults, AzureOpenAIEmbedderClient, Ba… |
| mcp_server package | library | Observed | Groups 7 file(s) under mcp_server package (observed from repository paths and static analysis). Observed top-level functions: _date_range_or_group, _doc_only_model, build_edge_type_map, build_edge_types, build_entity_ty… |
| server package | library | Observed | Groups 6 file(s) under server package (observed from repository paths and static analysis). Observed top-level classes: AddEntityNodeRequest, AddMessagesRequest, FactResult, GetMemoryRequest, GetMemoryResponse, Message.… |
| Service / domain layer | service | Observed | Groups 3 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: CrossEncoderFactory, DatabaseDriverFactory, EmbedderFactory, LLMClientFactory, QueueService… |
| Tests | test | Observed | Groups 98 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH google.genai.Client, PATCH google.genai.Client, PATCH google.genai.Client, PATCH google.genai.Client, PATCH goog… |

## Important files

- `.env.example` (config)
- `.github/ISSUE_TEMPLATE/01-bug.yml` (config)
- `.github/ISSUE_TEMPLATE/02-feature.yml` (config)
- `.github/ISSUE_TEMPLATE/03-docs.yml` (config)
- `.github/ISSUE_TEMPLATE/04-question.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/actions/openai-workload-identity/action.yml` (config)
- `.github/actions/setup-socket-firewall/action.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/intake/decision.schema.json` (config)
- `.github/workflows/ai-moderator.yml` (ci)
- `.github/workflows/cla.yml` (ci)
- `.github/workflows/codeql.yml` (ci)
- `.github/workflows/issue-intake.yml` (ci)
- `.github/workflows/lint.yml` (ci)
- `.github/workflows/mcp-server-tests.yml` (ci)
- `.github/workflows/pr-intake.yml` (ci)
- `.github/workflows/release-graphiti-core.yml` (ci)
- `.github/workflows/release-mcp-server.yml` (ci)
- `.github/workflows/release-server-container.yml` (ci)
- `.github/workflows/server-tests.yml` (ci)
- `.github/workflows/socket-firewall-connectivity.yml` (ci)
- `.github/workflows/stale.yml` (ci)
- `.github/workflows/typecheck.yml` (ci)
- `.github/workflows/unit_tests.yml` (ci)
- `Dockerfile` (container)
- `depot.json` (config)
- `docker-compose.test.yml` (config)
- `docker-compose.yml` (container)
- `examples/azure-openai/.env.example` (config)
- `examples/data/manybirds_products.json` (config)
- `examples/gliner2/.env.example` (config)
- `examples/jev/.env.example` (config)
- `examples/openai_decisions/.env.example` (config)
- `examples/opentelemetry/.env.example` (config)
- `examples/opentelemetry/pyproject.toml` (manifest)
- `examples/quickstart/requirements.txt` (manifest)
- `mcp_server/.env.example` (config)
- `mcp_server/config/config-docker-falkordb-combined.yaml` (config)
- `mcp_server/config/config-docker-falkordb.yaml` (config)
- `mcp_server/config/config-docker-neo4j.yaml` (config)
- `mcp_server/config/config.yaml` (config)
- `mcp_server/config/mcp_config_stdio_example.json` (config)
- `mcp_server/docker/Dockerfile` (container)
- `mcp_server/docker/Dockerfile.standalone` (container)
- `mcp_server/docker/docker-compose-falkordb.yml` (config)
- `mcp_server/docker/docker-compose-neo4j.yml` (config)
- `mcp_server/docker/docker-compose.yml` (container)
- `mcp_server/docker/github-actions-example.yml` (config)
- `mcp_server/pyproject.toml` (manifest)
- `mcp_server/pytest.ini` (config)
- `pyproject.toml` (manifest)
- `pytest.ini` (config)
- `server/.env.example` (config)
- `server/pyproject.toml` (manifest)
- `signatures/version1/cla.json` (config)
- `spec/configurable-prompts-tests.yaml` (config)

## Top-level layout

- `graphiti_core` — 167 analysed file(s)
- `tests` — 74 analysed file(s)
- `mcp_server` — 59 analysed file(s)
- `.github` — 37 analysed file(s)
- `examples` — 30 analysed file(s)
- `(root files)` — 20 analysed file(s)
- `server` — 16 analysed file(s)
- `spec` — 7 analysed file(s)
- `images` — 1 analysed file(s)
- `signatures` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (1 x likely secret file excluded; 1 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `ed23196506eba8806fae6da831d73fcd2ad714d8` is the revision these paths and observations refer to.
