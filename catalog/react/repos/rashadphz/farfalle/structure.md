# Project structure: rashadphz/farfalle

**Analysed commit:** `a9dd4939d21f4da6bb3ef7de138caba0f2ffab13`

**Commit reference:** [a9dd4939d21f4da6bb3ef7de138caba0f2ffab13](https://github.com/rashadphz/farfalle/commit/a9dd4939d21f4da6bb3ef7de138caba0f2ffab13)

**Tree at this commit:** [rashadphz/farfalle@a9dd4939d21f](https://github.com/rashadphz/farfalle/tree/a9dd4939d21f4da6bb3ef7de138caba0f2ffab13)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | rashadphz/farfalle |
| Description | 🔍 AI search engine - self-host with local or cloud LLMs |
| Stars | 3541 |
| Forks | 316 |
| Licence | Apache-2.0 |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `a9dd4939d21f4da6bb3ef7de138caba0f2ffab13` |
| Retrieved at | 2026-11-14T19:15:15.727696+00:00 |
| Files in this snapshot | 143 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (2 files)
    build_and_push_docker.yml
    farfalle-backend-AutoDeployTrigger-3e5a49cd-d51c-45b9-93a5-6170d843a4cc.yml
docker-scripts/  (2 files)
  entrypoint.sh
  env-defaults
searxng/  (3 files)
  limiter.toml
  settings.yml
  uwsgi.ini
src/  (125 files)
  backend/  (30 files)
    alembic/  (6 files)
      … 6 files under this directory
    db/  (3 files)
      … 3 files under this directory
    llm/  (1 files)
      … 1 files under this directory
    search/  (8 files)
      … 8 files under this directory
    Dockerfile
    __init__.py
    agent_search.py
    alembic.ini
    chat.py
    constants.py
    main.py
    prompts.py
    related_queries.py
    schemas.py
    utils.py
    validators.py
  frontend/  (94 files)
    generated/  (24 files)
      … 24 files under this directory
    public/  (2 files)
      … 2 files under this directory
    src/  (56 files)
      … 56 files under this directory
    .eslintrc.json
    .gitignore
    Dockerfile
    README.md
    components.json
    next-env.d.ts
    next.config.mjs
    openapi-ts.config.ts
    package.json
    postcss.config.mjs
    tailwind.config.ts
    tsconfig.json
  __init__.py
.env-template
.gitignore
.pre-commit-config.yaml
.prettierignore
LICENSE
README.md
custom-setup-instructions.md
docker-compose.dev.yaml
pyproject.toml
render.yaml
standalone.Dockerfile
```

## Entry points

- [src/backend/main.py:86](https://github.com/rashadphz/farfalle/blob/a9dd4939d21f4da6bb3ef7de138caba0f2ffab13/src/backend/main.py#L86)
- [src/frontend/generated/index.ts](https://github.com/rashadphz/farfalle/blob/a9dd4939d21f4da6bb3ef7de138caba0f2ffab13/src/frontend/generated/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| backend package | library | Observed | Groups 20 file(s) under backend package (observed from repository paths and static analysis). Observed top-level classes: BaseLLM, BingSearchProvider, ChatModel, EveryLLM, QueryPlan, QueryPlanStep. Observed top-level fu… |
| Configuration and deployment | config | Observed | Groups 13 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 18 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AgentFinishStream, AgentQueryPlanStream, AgentReadResultsStream, AgentSearchFullResponse, AgentSearchF… |
| docker-scripts package | library | Observed | Groups 1 file(s) under docker-scripts package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed routes: POST /chat, GET /history, GET /thread/{thread_id}. O… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| frontend package | library | Observed | Groups 63 file(s) under frontend package (observed from repository paths and static analysis). |
| __init__.py package | library | Observed | Groups 1 file(s) under __init__.py package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 8 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level functions: get_bing_api_key, get_search_provider, get_searxng_base_url, get_serper_api_key, get_tavi… |

## Important files

- `.github/workflows/build_and_push_docker.yml` (ci)
- `.github/workflows/farfalle-backend-AutoDeployTrigger-3e5a49cd-d51c-45b9-93a5-6170d843a4cc.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `docker-compose.dev.yaml` (config)
- `pyproject.toml` (manifest)
- `render.yaml` (config)
- `searxng/limiter.toml` (config)
- `searxng/settings.yml` (config)
- `searxng/uwsgi.ini` (config)
- `src/backend/Dockerfile` (container)
- `src/backend/alembic.ini` (config)
- `src/frontend/.eslintrc.json` (config)
- `src/frontend/Dockerfile` (container)
- `src/frontend/components.json` (config)
- `src/frontend/package.json` (manifest)
- `src/frontend/tsconfig.json` (config)

## Top-level layout

- `src` — 125 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `searxng` — 3 analysed file(s)
- `.github` — 2 analysed file(s)
- `docker-scripts` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 3 file(s) were skipped during inventory (2 x likely secret file excluded; 1 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `a9dd4939d21f4da6bb3ef7de138caba0f2ffab13` is the revision these paths and observations refer to.
