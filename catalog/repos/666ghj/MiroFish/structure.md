# Project structure: 666ghj/MiroFish

**Analysed commit:** `7657031ac01184afe2cb220f5ee3545573b5e843`

**Commit reference:** [7657031ac01184afe2cb220f5ee3545573b5e843](https://github.com/666ghj/MiroFish/commit/7657031ac01184afe2cb220f5ee3545573b5e843)

**Tree at this commit:** [666ghj/MiroFish@7657031ac011](https://github.com/666ghj/MiroFish/tree/7657031ac01184afe2cb220f5ee3545573b5e843)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | 666ghj/MiroFish |
| Description | A Simple and Universal Swarm Intelligence Engine, Predicting Anything. 简洁通用的群体智能引擎，预测万物 |
| Stars | 85581 |
| Forks | 12985 |
| Licence | AGPL-3.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `7657031ac01184afe2cb220f5ee3545573b5e843` |
| Retrieved at | 2026-11-14T19:06:09.074224+00:00 |
| Files in this snapshot | 110 |

## Directory tree

```text
.github/  (4 files)
  star-history/  (2 files)
    THIRD_PARTY_NOTICES.md
    history.json
  workflows/  (2 files)
    docker-image.yml
    update-star-history.yml
backend/  (60 files)
  app/  (33 files)
    api/  (4 files)
      … 4 files under this directory
    models/  (3 files)
      … 3 files under this directory
    services/  (13 files)
      … 13 files under this directory
    utils/  (11 files)
      … 11 files under this directory
    __init__.py
    config.py
  scripts/  (6 files)
    action_logger.py
    run_parallel_simulation.py
    run_reddit_simulation.py
    run_twitter_simulation.py
    test_profile_format.py
    validate_zep_cloud_integration.py
  tests/  (18 files)
    test_llm_json_responses.py
    test_ontology_api_errors.py
    test_ontology_attributes.py
    test_ontology_generator.py
    test_openai_chat_compat.py
    test_platform_profiles.py
    test_profile_field_normalization.py
    test_report_tool_result_sanitizer.py
    test_simulation_prepare_failure.py
    test_zep_cloud_contracts.py
    test_zep_cloud_validation_script.py
    test_zep_edge_paging.py
    test_zep_entity_reader_edges.py
    test_zep_graph_lifecycle.py
    test_zep_graph_memory_updater.py
    test_zep_report_barrier.py
    test_zep_retry_and_client.py
    test_zep_simulation_barrier.py
  pyproject.toml
  requirements.txt
  run.py
frontend/  (28 files)
  src/  (24 files)
    api/  (4 files)
      … 4 files under this directory
    components/  (8 files)
      … 8 files under this directory
    i18n/  (1 files)
      … 1 files under this directory
    router/  (1 files)
      … 1 files under this directory
    store/  (1 files)
      … 1 files under this directory
    views/  (7 files)
      … 7 files under this directory
    App.vue
    main.js
  .gitignore
  index.html
  package.json
  vite.config.js
locales/  (3 files)
  en.json
  languages.json
  zh.json
scripts/  (2 files)
  fetch_star_count.py
  star_history.py
static/  (2 files)
  image/  (2 files)
    star-history-dark.svg
    star-history-light.svg
tests/  (2 files)
  test_local_star_count_fetch.py
  test_local_star_history.py
.dockerignore
.env.example
.gitignore
Dockerfile
LICENSE
README-ZH.md
README.md
docker-compose.yml
package.json
```

## Entry points

- [backend/app/__init__.py:21](https://github.com/666ghj/MiroFish/blob/7657031ac01184afe2cb220f5ee3545573b5e843/backend/app/__init__.py#L21)
- [backend/run.py:48](https://github.com/666ghj/MiroFish/blob/7657031ac01184afe2cb220f5ee3545573b5e843/backend/run.py#L48)
- [backend/scripts/run_parallel_simulation.py:1684](https://github.com/666ghj/MiroFish/blob/7657031ac01184afe2cb220f5ee3545573b5e843/backend/scripts/run_parallel_simulation.py#L1684)
- [backend/scripts/run_reddit_simulation.py:759](https://github.com/666ghj/MiroFish/blob/7657031ac01184afe2cb220f5ee3545573b5e843/backend/scripts/run_reddit_simulation.py#L759)
- [backend/scripts/run_twitter_simulation.py:771](https://github.com/666ghj/MiroFish/blob/7657031ac01184afe2cb220f5ee3545573b5e843/backend/scripts/run_twitter_simulation.py#L771)
- [backend/scripts/validate_zep_cloud_integration.py:903](https://github.com/666ghj/MiroFish/blob/7657031ac01184afe2cb220f5ee3545573b5e843/backend/scripts/validate_zep_cloud_integration.py#L903)
- [scripts/fetch_star_count.py:145](https://github.com/666ghj/MiroFish/blob/7657031ac01184afe2cb220f5ee3545573b5e843/scripts/fetch_star_count.py#L145)
- [scripts/star_history.py:1488](https://github.com/666ghj/MiroFish/blob/7657031ac01184afe2cb220f5ee3545573b5e843/scripts/star_history.py#L1488)
- [frontend/src/api/index.js](https://github.com/666ghj/MiroFish/blob/7657031ac01184afe2cb220f5ee3545573b5e843/frontend/src/api/index.js)
- [frontend/src/i18n/index.js](https://github.com/666ghj/MiroFish/blob/7657031ac01184afe2cb220f5ee3545573b5e843/frontend/src/i18n/index.js)
- [frontend/src/main.js](https://github.com/666ghj/MiroFish/blob/7657031ac01184afe2cb220f5ee3545573b5e843/frontend/src/main.js)
- [frontend/src/router/index.js](https://github.com/666ghj/MiroFish/blob/7657031ac01184afe2cb220f5ee3545573b5e843/frontend/src/router/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 15 file(s) under api layer (observed from repository paths and static analysis). Observed routes: ROUTE /project/<project_id>, ROUTE /project/list, ROUTE /project/<project_id>, ROUTE /project/<project_id>/reset,… |
| backend package | library | Observed | Groups 11 file(s) under backend package (observed from repository paths and static analysis). Observed top-level classes: ActionLogger, FileParser, PlatformActionLogger, RetryableAPIClient, SimulationLogManager. Observe… |
| Configuration and deployment | config | Observed | Groups 10 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: Config. |
| Data layer | data | Observed | Groups 3 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: Project, ProjectManager, ProjectStatus, Task, TaskManager, TaskStatus. |
| Application entry point | entrypoint | Observed | Groups 8 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Flask. Observed top-level classes: ChartPoint, Clock, CommandRunner, CommandTy… |
| External integrations | external | Observed | Groups 1 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: LLMClient, LLMResponseError. Observed top-level functions: _clean_chat_text, _contains_addit… |
| frontend package | library | Observed | Groups 14 file(s) under frontend package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 13 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: AgentAction, AgentActivity, AgentActivityConfig, AgentInterview, BatchSubmission, CommandS… |
| Tests | test | Observed | Groups 21 file(s) under tests (observed from repository paths and static analysis). Observed application object created via Flask. Observed top-level classes: CompletionRecorder, CompletionSequence, FakeGitHub, FakeRunn… |

## Important files

- `.dockerignore` (container)
- `.env.example` (config)
- `.github/star-history/history.json` (config)
- `.github/workflows/docker-image.yml` (ci)
- `.github/workflows/update-star-history.yml` (ci)
- `Dockerfile` (container)
- `backend/pyproject.toml` (manifest)
- `backend/requirements.txt` (manifest)
- `docker-compose.yml` (container)
- `frontend/package.json` (manifest)
- `locales/en.json` (config)
- `locales/languages.json` (config)
- `locales/zh.json` (config)
- `package.json` (manifest)

## Top-level layout

- `backend` — 60 analysed file(s)
- `frontend` — 28 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `.github` — 4 analysed file(s)
- `locales` — 3 analysed file(s)
- `scripts` — 2 analysed file(s)
- `static` — 2 analysed file(s)
- `tests` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `7657031ac01184afe2cb220f5ee3545573b5e843` is the revision these paths and observations refer to.
