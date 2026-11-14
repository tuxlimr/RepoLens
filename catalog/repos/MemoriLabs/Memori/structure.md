# Project structure: MemoriLabs/Memori

**Analysed commit:** `574b1ea3e876f100ef82c37817d603eb7e258e59`

**Commit reference:** [574b1ea3e876f100ef82c37817d603eb7e258e59](https://github.com/MemoriLabs/Memori/commit/574b1ea3e876f100ef82c37817d603eb7e258e59)

**Tree at this commit:** [MemoriLabs/Memori@574b1ea3e876](https://github.com/MemoriLabs/Memori/tree/574b1ea3e876f100ef82c37817d603eb7e258e59)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | MemoriLabs/Memori |
| Description | Memori is agent-native memory infrastructure. A LLM-agnostic layer that turns agent execution and conversation into structured, persistent state for production systems. Built for enterprise, Memori works with the data infrastructure you already run, no rip-and-replace, and deploys across managed cl… |
| Stars | 17575 |
| Forks | 3984 |
| Licence | Other |
| Language | Python |
| Default branch | main |
| Analysed commit | `574b1ea3e876f100ef82c37817d603eb7e258e59` |
| Retrieved at | 2026-11-14T19:08:31.035919+00:00 |
| Files in this snapshot | 658 |

## Directory tree

```text
.github/  (16 files)
  ISSUE_TEMPLATE/  (4 files)
    bug_report.yml
    config.yml
    feature_request.yml
    question.yml
  workflows/  (11 files)
    ci.yml
    core-ci.yml
    integration.yml
    publish-hermes.yml
    publish-npm.yml
    publish-openclaw-plugin.yml
    publish.yml
    python-cloud-integration.yml
    ts-ci.yml
    ts-cloud-integration.yml
    ts-openclaw-ci.yml
  pull_request_template.md
benchmarks/  (5 files)
  .env.example
  01_load_indexes.ipynb
  02_run_benchmark.ipynb
  README.md
  pyproject.toml
core/  (64 files)
  .cargo/  (1 files)
    config.toml
  bindings/  (10 files)
    node/  (8 files)
      … 8 files under this directory
    python/  (2 files)
      … 2 files under this directory
  docs/  (1 files)
    architecture.md
  src/  (42 files)
    augmentation/  (3 files)
      … 3 files under this directory
    embeddings/  (5 files)
      … 5 files under this directory
    network/  (3 files)
      … 3 files under this directory
    retrieval/  (3 files)
      … 3 files under this directory
    runtime/  (5 files)
      … 5 files under this directory
    search/  (5 files)
      … 5 files under this directory
    storage/  (15 files)
      … 15 files under this directory
    error.rs
    lib.rs
    models.rs
  tests/  (4 files)
    orchestrator_contract.rs
    retrieval_aa_contract.rs
    storage_sqlite_integration.rs
    worker_runtime_contract.rs
  .gitignore
  Cargo.toml
  Makefile
  README.md
  clippy.toml
  rust-toolchain.toml
docs/  (85 files)
  memori-byodb/  (39 files)
    concepts/  (8 files)
      … 8 files under this directory
    contribute/  (2 files)
      … 2 files under this directory
    dashboard/  (1 files)
      … 1 files under this directory
    databases/  (9 files)
      … 9 files under this directory
    getting-started/  (5 files)
      … 5 files under this directory
    llm/  (11 files)
      … 11 files under this directory
    support/  (2 files)
      … 2 files under this directory
    index.mdx
  memori-cloud/  (46 files)
    benchmark/  (3 files)
      … 3 files under this directory
    claude-code/  (3 files)
      … 3 files under this directory
    concepts/  (7 files)
      … 7 files under this directory
    dashboard/  (5 files)
      … 5 files under this directory
    getting-started/  (4 files)
      … 4 files under this directory
    hermes/  (3 files)
      … 3 files under this directory
    llm/  (11 files)
      … 11 files under this directory
    mcp/  (4 files)
      … 4 files under this directory
    openclaw/  (3 files)
      … 3 files under this directory
    support/  (2 files)
      … 2 files under this directory
    index.mdx
examples/  (38 files)
  agno/  (4 files)
    .env.example
    README.md
    main.py
    pyproject.toml
  cockroachdb/  (4 files)
    .env.example
    README.md
    main.py
    pyproject.toml
  digitalocean/  (4 files)
    .env.example
    README.md
    main.py
    pyproject.toml
  mongodb/  (4 files)
    .env.example
    README.md
    main.py
    pyproject.toml
  nebius/  (4 files)
    .env.example
    README.md
    main.py
    pyproject.toml
  neon/  (4 files)
    .env.example
    README.md
    main.py
    pyproject.toml
  oceanbase/  (2 files)
    README.md
    main.py
  postgres/  (4 files)
    .env.example
    README.md
    main.py
    pyproject.toml
  sqlite/  (5 files)
    .env.example
    README.md
    main.py
    pyproject.toml
    rust_core_main.py
  tidb/  (3 files)
    README.md
    main.py
    pyproject.toml
integrations/  (60 files)
  claude-code/  (4 files)
    .env.example
    README.md
    SKILL.md
    index.ts
  hermes/  (12 files)
    src/  (6 files)
      … 6 files under this directory
    tests/  (3 files)
      … 3 files under this directory
    README.md
    plugin.yaml
    pyproject.toml
  openclaw/  (44 files)
    skills/  (2 files)
      … 2 files under this directory
    src/  (21 files)
      … 21 files under this directory
    tests/  (14 files)
      … 14 files under this directory
    .prettierrc.json
    README.md
    eslint.config.js
    openclaw.plugin.json
    package.json
    tsconfig.json
    vitest.config.ts
memori/  (136 files)
  api/  (2 files)
    _quota.py
    _sign_up.py
  embeddings/  (7 files)
    __init__.py
    _api.py
    _chunking.py
    _format.py
    _tei.py
    _tei_embed.py
    _utils.py
  llm/  (33 files)
    adapters/  (10 files)
      … 10 files under this directory
    clients/  (3 files)
      … 3 files under this directory
    helpers/  (4 files)
      … 4 files under this directory
    invoke/  (5 files)
      … 5 files under this directory
    pipelines/  (4 files)
      … 4 files under this directory
    __init__.py
    _base.py
    _constants.py
    _providers.py
    _registry.py
    _utils.py
    _xai_wrappers.py
  memory/  (22 files)
    augmentation/  (16 files)
      … 16 files under this directory
    _collector.py
    _conversation_messages.py
    _manager.py
    _struct.py
    _writer.py
    recall.py
  native/  (6 files)
    __init__.py
    _adapter.py
    _embeddings.py
    _errors.py
    _loader.py
    _onnxruntime.py
  provisioning/  (8 files)
    providers/  (2 files)
      … 2 files under this directory
    __init__.py
    _cache.py
    _manager.py
    _models.py
    _registry.py
    _utils.py
  search/  (7 files)
    __init__.py
    _api.py
    _core.py
    _faiss.py
    _lexical.py
    _parsing.py
    _types.py
  storage/  (38 files)
    adapters/  (8 files)
      … 8 files under this directory
    cockroachdb/  (3 files)
      … 3 files under this directory
    drivers/  (14 files)
      … 14 files under this directory
    migrations/  (7 files)
      … 7 files under this directory
    __init__.py
    _base.py
    _builder.py
    _connection.py
    _manager.py
    _registry.py
  __init__.py
  __main__.py
  _cli.py
  _config.py
  _embedding_input.py
  _exceptions.py
  _logging.py
  _network.py
  _rust_core.py
  _setup.py
  _utils.py
  agent.py
  py.typed
memori-ts/  (90 files)
  examples/  (15 files)
    cloud/  (1 files)
      … 1 files under this directory
    cockroachdb/  (3 files)
      … 3 files under this directory
    mysql/  (3 files)
      … 3 files under this directory
    orm/  (1 files)
      … 1 files under this directory
    postgres/  (3 files)
      … 3 files under this directory
    sqlite/  (4 files)
      … 4 files under this directory
  scripts/  (2 files)
    bump-versions.js
    sync-native.js
  src/  (35 files)
    bin/  (1 files)
      … 1 files under this directory
    cli/  (5 files)
      … 5 files under this directory
    core/  (6 files)
      … 6 files under this directory
    engines/  (3 files)
      … 3 files under this directory
    integrations/  (3 files)
      … 3 files under this directory
    native/  (4 files)
      … 4 files under this directory
    storage/  (6 files)
      … 6 files under this directory
    types/  (3 files)
      … 3 files under this directory
    utils/  (1 files)
      … 1 files under this directory
    index.ts
    memori.ts
    version.ts
  tests/  (28 files)
    cli/  (6 files)
      … 6 files under this directory
    core/  (5 files)
      … 5 files under this directory
    engines/  (3 files)
      … 3 files under this directory
    integrations/  (6 files)
      … 6 files under this directory
    storage/  (5 files)
      … 5 files under this directory
    utils/  (1 files)
      … 1 files under this directory
    memori.test.ts
    setup.ts
  .gitignore
  .npmignore
  .prettierignore
  .prettierrc.json
  README.md
  eslint.config.js
  package.json
  tsconfig.build.json
  tsconfig.json
  vitest.config.ts
tests/  (147 files)
  database/  (2 files)
    core.py
    init_db.py
  embeddings/  (2 files)
    test_embedding_utils.py
    test_tei_chunking.py
  integration/  (19 files)
    cloud/  (7 files)
      … 7 files under this directory
    databases/  (3 files)
      … 3 files under this directory
    providers/  (6 files)
      … 6 files under this directory
    __init__.py
    conftest.py
    test_aa_payload.py
  integration_v2/  (6 files)
    cloud_v2/  (6 files)
      … 6 files under this directory
  llm/  (59 files)
    adapters/  (5 files)
      … 5 files under this directory
    clients/  (35 files)
      … 35 files under this directory
    helpers/  (2 files)
      … 2 files under this directory
    pipelines/  (3 files)
      … 3 files under this directory
    providers/  (5 files)
      … 5 files under this directory
    test_llm_base.py
    test_llm_clients.py
    test_llm_deprecation_warnings.py
    test_llm_embeddings.py
    test_llm_provider_sdk_version.py
    test_llm_registry.py
    test_llm_utils.py
    test_llm_xai_wrappers.py
    unit_test_objects.py
  memory/  (17 files)
    augmentation/  (9 files)
      … 9 files under this directory
    test_conversation_messages.py
    test_manager_enterprise_retry.py
    test_memory_augmentation_db_writer.py
    test_memory_struct.py
    test_memory_struct_triples.py
    test_memory_writer.py
    test_recall.py
    test_recall_eval_harness.py
  provisioning/  (7 files)
    test_memori_provision.py
    test_provisioning_cache.py
    test_provisioning_flow.py
    test_provisioning_models.py
    test_provisioning_registry.py
    test_provisioning_utils.py
    test_tidb_zero_provider.py
  storage/  (23 files)
    adapters/  (7 files)
      … 7 files under this directory
    cockroachdb/  (3 files)
      … 3 files under this directory
    drivers/  (7 files)
      … 7 files under this directory
    test_connection.py
    test_connection_factory.py
    test_storage_builder.py
    test_storage_init.py
    test_storage_manager.py
    test_storage_registry.py
  test_agent.py
  test_cli.py
  test_config.py
  test_init.py
  test_legacy_package_warning.py
  test_litellm_client.py
  test_llm_auto_registration.py
  test_network.py
  test_rust_core.py
  test_search.py
  test_typing_dx.py
  test_utils.py
.dockerignore
.env.example
.gitignore
.pre-commit-config.yaml
CHANGELOG.md
CONTRIBUTING.md
Dockerfile
LICENSE
MANIFEST.in
Makefile
README.md
SECURITY.md
conftest.py
docker-compose.yml
pyproject.toml
setup.cfg
setup.py
```

## Entry points

- [integrations/hermes/src/memori_hermes/install.py:187](https://github.com/MemoriLabs/Memori/blob/574b1ea3e876f100ef82c37817d603eb7e258e59/integrations/hermes/src/memori_hermes/install.py#L187)
- [memori/__main__.py:115](https://github.com/MemoriLabs/Memori/blob/574b1ea3e876f100ef82c37817d603eb7e258e59/memori/__main__.py#L115)
- [integrations/claude-code/index.ts](https://github.com/MemoriLabs/Memori/blob/574b1ea3e876f100ef82c37817d603eb7e258e59/integrations/claude-code/index.ts)
- [integrations/openclaw/src/index.ts](https://github.com/MemoriLabs/Memori/blob/574b1ea3e876f100ef82c37817d603eb7e258e59/integrations/openclaw/src/index.ts)
- [memori-ts/src/index.ts](https://github.com/MemoriLabs/Memori/blob/574b1ea3e876f100ef82c37817d603eb7e258e59/memori-ts/src/index.ts)
- [memori-ts/src/integrations/index.ts](https://github.com/MemoriLabs/Memori/blob/574b1ea3e876f100ef82c37817d603eb7e258e59/memori-ts/src/integrations/index.ts)
- [memori-ts/src/native/index.js](https://github.com/MemoriLabs/Memori/blob/574b1ea3e876f100ef82c37817d603eb7e258e59/memori-ts/src/native/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 3 file(s) under api layer (observed from repository paths and static analysis). Observed top-level classes: Manager. |
| Configuration and deployment | config | Observed | Groups 32 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 60 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: Adapter, AttributionData, AugmentationInputData, BaseConversation, BaseConversationMessage, BaseConver… |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: _PathsModule. Observed top-level functions: _ignore_copy_names, _load_direct_paths_module,… |
| External integrations | external | Observed | Groups 45 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: Adapter, Agno, Anthropic, Google, LangChain, LiteLLM. Observed top-level functions: _config… |
| memori package | library | Observed | Groups 78 file(s) under memori package (observed from repository paths and static analysis). Observed top-level classes: AdvancedAugmentation, Agent, Agno, Anthropic, Api, ApiSubdomain. Observed top-level functions: _ac… |
| memori-ts package | library | Observed | Groups 29 file(s) under memori-ts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 40 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 197 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH memori.llm.invoke.iterator.MemoryManager, PATCH memori.llm.invoke.iterator.format_payload, PATCH memori.llm.inv… |

## Important files

- `.dockerignore` (container)
- `.env.example` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/ISSUE_TEMPLATE/question.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/core-ci.yml` (ci)
- `.github/workflows/integration.yml` (ci)
- `.github/workflows/publish-hermes.yml` (ci)
- `.github/workflows/publish-npm.yml` (ci)
- `.github/workflows/publish-openclaw-plugin.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.github/workflows/python-cloud-integration.yml` (ci)
- `.github/workflows/ts-ci.yml` (ci)
- `.github/workflows/ts-cloud-integration.yml` (ci)
- `.github/workflows/ts-openclaw-ci.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `Dockerfile` (container)
- `MANIFEST.in` (manifest)
- `benchmarks/.env.example` (config)
- `benchmarks/pyproject.toml` (manifest)
- `core/.cargo/config.toml` (config)
- `core/Cargo.toml` (manifest)
- `core/bindings/node/Cargo.toml` (manifest)
- `core/bindings/node/package.json` (manifest)
- `core/bindings/python/Cargo.toml` (manifest)
- `core/clippy.toml` (config)
- `core/rust-toolchain.toml` (config)
- `docker-compose.yml` (container)
- `examples/agno/.env.example` (config)
- `examples/agno/pyproject.toml` (manifest)
- `examples/cockroachdb/.env.example` (config)
- `examples/cockroachdb/pyproject.toml` (manifest)
- `examples/digitalocean/.env.example` (config)
- `examples/digitalocean/pyproject.toml` (manifest)
- `examples/mongodb/.env.example` (config)
- `examples/mongodb/pyproject.toml` (manifest)
- `examples/nebius/.env.example` (config)
- `examples/nebius/pyproject.toml` (manifest)
- `examples/neon/.env.example` (config)
- `examples/neon/pyproject.toml` (manifest)
- `examples/postgres/.env.example` (config)
- `examples/postgres/pyproject.toml` (manifest)
- `examples/sqlite/.env.example` (config)
- `examples/sqlite/pyproject.toml` (manifest)
- `examples/tidb/pyproject.toml` (manifest)
- `integrations/claude-code/.env.example` (config)
- `integrations/hermes/plugin.yaml` (config)
- `integrations/hermes/pyproject.toml` (manifest)
- `integrations/hermes/src/memori_hermes/plugin.yaml` (config)
- `integrations/openclaw/.prettierrc.json` (config)
- `integrations/openclaw/openclaw.plugin.json` (config)
- `integrations/openclaw/package.json` (manifest)
- `integrations/openclaw/tsconfig.json` (config)
- `memori-ts/.prettierrc.json` (config)
- `memori-ts/examples/cockroachdb/.env.example` (config)
- `memori-ts/examples/mysql/.env.example` (config)
- `memori-ts/examples/postgres/.env.example` (config)
- `memori-ts/examples/sqlite/.env.example` (config)
- `memori-ts/package.json` (manifest)
- `memori-ts/src/native/package.json` (manifest)
- `memori-ts/tsconfig.build.json` (config)
- `memori-ts/tsconfig.json` (config)
- `pyproject.toml` (manifest)
- `setup.cfg` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `tests` — 147 analysed file(s)
- `memori` — 136 analysed file(s)
- `memori-ts` — 90 analysed file(s)
- `docs` — 85 analysed file(s)
- `core` — 64 analysed file(s)
- `integrations` — 60 analysed file(s)
- `examples` — 38 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `.github` — 16 analysed file(s)
- `benchmarks` — 5 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 8 file(s) were skipped during inventory (2 x lockfile excluded; 6 x vendored/generated directory excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `574b1ea3e876f100ef82c37817d603eb7e258e59` is the revision these paths and observations refer to.
