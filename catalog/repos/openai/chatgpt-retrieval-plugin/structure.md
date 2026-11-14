# Project structure: openai/chatgpt-retrieval-plugin

**Analysed commit:** `b28ddce58474441da332d4e15c6dd60ddaa953ab`

**Commit reference:** [b28ddce58474441da332d4e15c6dd60ddaa953ab](https://github.com/openai/chatgpt-retrieval-plugin/commit/b28ddce58474441da332d4e15c6dd60ddaa953ab)

**Tree at this commit:** [openai/chatgpt-retrieval-plugin@b28ddce58474](https://github.com/openai/chatgpt-retrieval-plugin/tree/b28ddce58474441da332d4e15c6dd60ddaa953ab)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | openai/chatgpt-retrieval-plugin |
| Description | The ChatGPT Retrieval Plugin lets you easily find personal or work documents by asking questions in natural language. |
| Stars | 21282 |
| Forks | 3567 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `b28ddce58474441da332d4e15c6dd60ddaa953ab` |
| Retrieved at | 2026-11-14T19:08:00.580926+00:00 |
| Files in this snapshot | 116 |

## Directory tree

```text
.github/  (1 files)
  pull_request_template.md
.well-known/  (2 files)
  ai-plugin.json
  openapi.yaml
datastore/  (20 files)
  providers/  (17 files)
    __init__.py
    analyticdb_datastore.py
    azurecosmosdb_datastore.py
    azuresearch_datastore.py
    chroma_datastore.py
    elasticsearch_datastore.py
    llama_datastore.py
    milvus_datastore.py
    mongodb_atlas_datastore.py
    pgvector_datastore.py
    pinecone_datastore.py
    postgres_datastore.py
    qdrant_datastore.py
    redis_datastore.py
    supabase_datastore.py
    weaviate_datastore.py
    zilliz_datastore.py
  __init__.py
  datastore.py
  factory.py
docs/  (21 files)
  deployment/  (5 files)
    flyio.md
    heroku.md
    other-options.md
    removing-unused-dependencies.md
    render.md
  deprecated/  (1 files)
    plugins.md
  providers/  (15 files)
    analyticdb/  (1 files)
      … 1 files under this directory
    azurecosmosdb/  (1 files)
      … 1 files under this directory
    azuresearch/  (1 files)
      … 1 files under this directory
    chroma/  (1 files)
      … 1 files under this directory
    elasticsearch/  (1 files)
      … 1 files under this directory
    llama/  (1 files)
      … 1 files under this directory
    milvus/  (1 files)
      … 1 files under this directory
    mongodb/  (1 files)
      … 1 files under this directory
    pinecone/  (1 files)
      … 1 files under this directory
    postgres/  (1 files)
      … 1 files under this directory
    qdrant/  (1 files)
      … 1 files under this directory
    redis/  (1 files)
      … 1 files under this directory
    supabase/  (1 files)
      … 1 files under this directory
    weaviate/  (1 files)
      … 1 files under this directory
    zilliz/  (1 files)
      … 1 files under this directory
examples/  (27 files)
  authentication-methods/  (5 files)
    no-auth/  (2 files)
      … 2 files under this directory
    oauth/  (1 files)
      … 1 files under this directory
    service-http/  (1 files)
      … 1 files under this directory
    user-http/  (1 files)
      … 1 files under this directory
  docker/  (8 files)
    elasticsearch/  (2 files)
      … 2 files under this directory
    milvus/  (1 files)
      … 1 files under this directory
    qdrant/  (4 files)
      … 4 files under this directory
    redis/  (1 files)
      … 1 files under this directory
  function-calling/  (1 files)
    README.md
  memory/  (4 files)
    README.md
    ai-plugin.json
    main.py
    openapi.yaml
  providers/  (9 files)
    azurecosmosdb/  (1 files)
      … 1 files under this directory
    elasticsearch/  (1 files)
      … 1 files under this directory
    mongodb/  (1 files)
      … 1 files under this directory
    pinecone/  (1 files)
      … 1 files under this directory
    redis/  (1 files)
      … 1 files under this directory
    supabase/  (4 files)
      … 4 files under this directory
local_server/  (3 files)
  ai-plugin.json
  main.py
  openapi.yaml
models/  (2 files)
  api.py
  models.py
scripts/  (8 files)
  process_json/  (3 files)
    README.md
    example.json
    process_json.py
  process_jsonl/  (3 files)
    README.md
    example.jsonl
    process_jsonl.py
  process_zip/  (2 files)
    README.md
    process_zip.py
server/  (1 files)
  main.py
services/  (6 files)
  chunks.py
  date.py
  extract_metadata.py
  file.py
  openai.py
  pii_detection.py
tests/  (17 files)
  datastore/  (16 files)
    providers/  (16 files)
      … 16 files under this directory
  __init__.py
.dockerignore
.env.example
.gitignore
Dockerfile
LICENSE
Makefile
README.md
pyproject.toml
```

## Entry points

- [local_server/main.py:25](https://github.com/openai/chatgpt-retrieval-plugin/blob/b28ddce58474441da332d4e15c6dd60ddaa953ab/local_server/main.py#L25)
- [scripts/process_json/process_json.py:146](https://github.com/openai/chatgpt-retrieval-plugin/blob/b28ddce58474441da332d4e15c6dd60ddaa953ab/scripts/process_json/process_json.py#L146)
- [scripts/process_jsonl/process_jsonl.py:144](https://github.com/openai/chatgpt-retrieval-plugin/blob/b28ddce58474441da332d4e15c6dd60ddaa953ab/scripts/process_jsonl/process_jsonl.py#L144)
- [scripts/process_zip/process_zip.py:151](https://github.com/openai/chatgpt-retrieval-plugin/blob/b28ddce58474441da332d4e15c6dd60ddaa953ab/scripts/process_zip/process_zip.py#L151)
- [server/main.py:33](https://github.com/openai/chatgpt-retrieval-plugin/blob/b28ddce58474441da332d4e15c6dd60ddaa953ab/server/main.py#L33)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 2 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: DeleteRequest, DeleteResponse, Document, DocumentChunk, DocumentChunkMetadata, DocumentChunkWithScore. |
| datastore package | library | Observed | Groups 20 file(s) under datastore package (observed from repository paths and static analysis). Observed top-level classes: AnalyticDBDataStore, AzureCosmosDBDataStore, AzureCosmosDBStoreApi, AzureSearchDataStore, Chrom… |
| Application entry point | entrypoint | Observed | Groups 5 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed routes: ROUTE /.well-known/ai-plugin.json, ROUTE /.well-know… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 6 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level functions: create_document_chunks, extract_metadata_from_document, extract_text_from_file, extract_t… |
| Tests | test | Observed | Groups 16 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: _mongodb_datastore, analyticdb_datastore, assert_when_ready, azure_cosmos_db_settings_from_dot_env, azure… |

## Important files

- `.dockerignore` (container)
- `.env.example` (config)
- `.well-known/ai-plugin.json` (config)
- `.well-known/openapi.yaml` (config)
- `Dockerfile` (container)
- `examples/authentication-methods/no-auth/ai-plugin.json` (config)
- `examples/authentication-methods/oauth/ai-plugin.json` (config)
- `examples/authentication-methods/service-http/ai-plugin.json` (config)
- `examples/authentication-methods/user-http/ai-plugin.json` (config)
- `examples/docker/elasticsearch/docker-compose.yaml` (container)
- `examples/docker/milvus/docker-compose.yaml` (container)
- `examples/docker/qdrant/docker-compose.yaml` (container)
- `examples/docker/qdrant/documents.json` (config)
- `examples/docker/qdrant/queries.json` (config)
- `examples/docker/redis/docker-compose.yml` (container)
- `examples/memory/ai-plugin.json` (config)
- `examples/memory/openapi.yaml` (config)
- `examples/providers/supabase/config.toml` (config)
- `local_server/ai-plugin.json` (config)
- `local_server/openapi.yaml` (config)
- `pyproject.toml` (manifest)
- `scripts/process_json/example.json` (config)
- `tests/datastore/providers/weaviate/docker-compose.yml` (container)

## Top-level layout

- `examples` — 27 analysed file(s)
- `docs` — 21 analysed file(s)
- `datastore` — 20 analysed file(s)
- `tests` — 17 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `scripts` — 8 analysed file(s)
- `services` — 6 analysed file(s)
- `local_server` — 3 analysed file(s)
- `.well-known` — 2 analysed file(s)
- `models` — 2 analysed file(s)
- `.github` — 1 analysed file(s)
- `server` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- The GitHub repository was marked archived at selection time.

Commit `b28ddce58474441da332d4e15c6dd60ddaa953ab` is the revision these paths and observations refer to.
