# Project structure: AhmadHassan-BTed/AutoSwarm-Shadow-Adapter

**Analysed commit:** `8656e21ba4c6e1f18a820c3e0b5fb41db44a8da6`

**Commit reference:** [8656e21ba4c6e1f18a820c3e0b5fb41db44a8da6](https://github.com/AhmadHassan-BTed/AutoSwarm-Shadow-Adapter/commit/8656e21ba4c6e1f18a820c3e0b5fb41db44a8da6)

**Tree at this commit:** [AhmadHassan-BTed/AutoSwarm-Shadow-Adapter@8656e21ba4c6](https://github.com/AhmadHassan-BTed/AutoSwarm-Shadow-Adapter/tree/8656e21ba4c6e1f18a820c3e0b5fb41db44a8da6)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | AhmadHassan-BTed/AutoSwarm-Shadow-Adapter |
| Description | Zero-modification Human-in-the-Loop adapter for OpenOPC's agentic DAG runtime. |
| Stars | 5185 |
| Forks | 3 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `8656e21ba4c6e1f18a820c3e0b5fb41db44a8da6` |
| Retrieved at | 2026-11-14T19:14:25.390272+00:00 |
| Files in this snapshot | 76 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (2 files)
    ci.yml
    release.yml
docs/  (3 files)
  architecture.md
  execution_flow.md
  implementation_guide.md
shadow_adapter/  (44 files)
  api/  (6 files)
    __init__.py
    app.py
    dependencies.py
    routes_artifacts.py
    routes_auth.py
    routes_tasks.py
  frontend/  (20 files)
    src/  (14 files)
      … 14 files under this directory
    index.html
    package.json
    postcss.config.js
    tailwind.config.js
    tsconfig.json
    vite.config.ts
  repositories/  (3 files)
    __init__.py
    artifact_repo.py
    opc_resume_repo.py
  services/  (4 files)
    __init__.py
    auth_service.py
    handoff_service.py
    org_service.py
  __init__.py
  adapter.py
  brief_builder.py
  config.py
  exceptions.py
  models.py
  research.py
  security.py
  shadow_store.py
  upload.py
  worker.py
tests/  (18 files)
  __init__.py
  conftest.py
  mock_openopc_engine.py
  test_adapter.py
  test_api.py
  test_black_hole.py
  test_brain.py
  test_concurrency.py
  test_edge_cases.py
  test_fuzzing.py
  test_invariants.py
  test_opc_integration.py
  test_security.py
  test_services.py
  test_shadow_store.py
  test_symbiote_alignment.py
  test_worker.py
  test_worker_research.py
.env.example
.gitignore
CHANGELOG.md
CONTRIBUTING.md
LICENSE
README.md
example_usage.py
pyproject.toml
shadow_worker.py
```

## Entry points

- [example_usage.py:203](https://github.com/AhmadHassan-BTed/AutoSwarm-Shadow-Adapter/blob/8656e21ba4c6e1f18a820c3e0b5fb41db44a8da6/example_usage.py#L203)
- [shadow_adapter/api/app.py](https://github.com/AhmadHassan-BTed/AutoSwarm-Shadow-Adapter/blob/8656e21ba4c6e1f18a820c3e0b5fb41db44a8da6/shadow_adapter/api/app.py)
- [shadow_adapter/worker.py](https://github.com/AhmadHassan-BTed/AutoSwarm-Shadow-Adapter/blob/8656e21ba4c6e1f18a820c3e0b5fb41db44a8da6/shadow_adapter/worker.py)
- [shadow_worker.py:10](https://github.com/AhmadHassan-BTed/AutoSwarm-Shadow-Adapter/blob/8656e21ba4c6e1f18a820c3e0b5fb41db44a8da6/shadow_worker.py#L10)
- [shadow_adapter/frontend/src/App.tsx](https://github.com/AhmadHassan-BTed/AutoSwarm-Shadow-Adapter/blob/8656e21ba4c6e1f18a820c3e0b5fb41db44a8da6/shadow_adapter/frontend/src/App.tsx)
- [shadow_adapter/frontend/src/main.tsx](https://github.com/AhmadHassan-BTed/AutoSwarm-Shadow-Adapter/blob/8656e21ba4c6e1f18a820c3e0b5fb41db44a8da6/shadow_adapter/frontend/src/main.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 6 file(s) under api layer (observed from repository paths and static analysis). Observed routes: GET /{artifact_id}, GET /{artifact_id}/download, GET /context/{task_id}, POST /login, POST /register. Observed top-… |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: ShadowConfig. |
| Data layer | data | Observed | Groups 4 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: ContractorPublic, CorporateArtifact, CorporateArtifactsRepository, HealthResponse, JwtConfig, LoginRequ… |
| Application entry point | entrypoint | Observed | Groups 4 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed top-level classes: ShadowWorker. Observed top-level function… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 4 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: AuthService, HandoffService, OrgHierarchyService. |
| shadow_adapter package | library | Observed | Groups 23 file(s) under shadow_adapter package (observed from repository paths and static analysis). Observed top-level classes: ContractorAlreadyExistsError, ContractorNotFoundError, InvalidCredentialsError, SecureUplo… |
| Tests | test | Observed | Groups 18 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: MockOpenOPCEngine, MockTask, SyntheticMutatedTask. Observed top-level functions: admin_auth_headers, auth_h… |

## Important files

- `.env.example` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `pyproject.toml` (manifest)
- `shadow_adapter/frontend/package.json` (manifest)
- `shadow_adapter/frontend/tsconfig.json` (config)

## Top-level layout

- `shadow_adapter` — 44 analysed file(s)
- `tests` — 18 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `docs` — 3 analysed file(s)
- `.github` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `8656e21ba4c6e1f18a820c3e0b5fb41db44a8da6` is the revision these paths and observations refer to.
