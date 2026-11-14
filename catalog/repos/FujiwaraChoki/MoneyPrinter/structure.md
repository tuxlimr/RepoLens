# Project structure: FujiwaraChoki/MoneyPrinter

**Analysed commit:** `2a7c6bc6e8fab6e01fa740c4311d9e1e233b0262`

**Commit reference:** [2a7c6bc6e8fab6e01fa740c4311d9e1e233b0262](https://github.com/FujiwaraChoki/MoneyPrinter/commit/2a7c6bc6e8fab6e01fa740c4311d9e1e233b0262)

**Tree at this commit:** [FujiwaraChoki/MoneyPrinter@2a7c6bc6e8fa](https://github.com/FujiwaraChoki/MoneyPrinter/tree/2a7c6bc6e8fab6e01fa740c4311d9e1e233b0262)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | FujiwaraChoki/MoneyPrinter |
| Description | Automate Creation of YouTube Shorts using MoviePy. |
| Stars | 14198 |
| Forks | 1842 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `2a7c6bc6e8fab6e01fa740c4311d9e1e233b0262` |
| Retrieved at | 2026-11-14T19:09:31.278420+00:00 |
| Files in this snapshot | 41 |

## Directory tree

```text
.github/  (3 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  FUNDING.yml
Backend/  (13 files)
  db.py
  gpt.py
  logstream.py
  main.py
  models.py
  pipeline.py
  repository.py
  search.py
  tiktokvoice.py
  utils.py
  video.py
  worker.py
  youtube.py
Frontend/  (2 files)
  app.js
  index.html
docs/  (7 files)
  README.md
  architecture.md
  configuration.md
  docker.md
  quickstart.md
  testing.md
  troubleshooting.md
tests/  (6 files)
  conftest.py
  test_api_jobs.py
  test_api_misc.py
  test_repository.py
  test_utils.py
  test_worker.py
.env.example
.gitignore
AGENTS.md
CLAUDE.md
Dockerfile
LICENSE
README.md
docker-compose.yml
pyproject.toml
setup.sh
```

## Entry points

- [Backend/main.py:19](https://github.com/FujiwaraChoki/MoneyPrinter/blob/2a7c6bc6e8fab6e01fa740c4311d9e1e233b0262/Backend/main.py#L19)
- [Backend/worker.py:76](https://github.com/FujiwaraChoki/MoneyPrinter/blob/2a7c6bc6e8fab6e01fa740c4311d9e1e233b0262/Backend/worker.py#L76)
- [Frontend/app.js](https://github.com/FujiwaraChoki/MoneyPrinter/blob/2a7c6bc6e8fab6e01fa740c4311d9e1e233b0262/Frontend/app.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Backend package | library | Observed | Groups 9 file(s) under backend package (observed from repository paths and static analysis). Observed top-level classes: LogStream, PipelineCancelled. Observed top-level functions: __generate_subtitles_assemblyai, __gen… |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 2 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: Artifact, Base, GenerationEvent, GenerationJob, Project, Script. Observed top-level functions: _databas… |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Flask. Observed routes: ROUTE /api/models, ROUTE /api/generate, ROUTE /api/job… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| Frontend package | library | Observed | Groups 1 file(s) under frontend package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 6 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: _disable_cleanup, client, session, session_factory, test_cancel_job_endpoint_cancels_existing_job, test_ca… |

## Important files

- `.env.example` (config)
- `.github/FUNDING.yml` (config)
- `Dockerfile` (container)
- `docker-compose.yml` (container)
- `pyproject.toml` (manifest)

## Top-level layout

- `Backend` — 13 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `docs` — 7 analysed file(s)
- `tests` — 6 analysed file(s)
- `.github` — 3 analysed file(s)
- `Frontend` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `2a7c6bc6e8fab6e01fa740c4311d9e1e233b0262` is the revision these paths and observations refer to.
