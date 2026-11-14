# Project structure: avgupta456/github-trends

**Analysed commit:** `7d1ec357a1033cd6828a6a194070167ccde20092`

**Commit reference:** [7d1ec357a1033cd6828a6a194070167ccde20092](https://github.com/avgupta456/github-trends/commit/7d1ec357a1033cd6828a6a194070167ccde20092)

**Tree at this commit:** [avgupta456/github-trends@7d1ec357a103](https://github.com/avgupta456/github-trends/tree/7d1ec357a1033cd6828a6a194070167ccde20092)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | avgupta456/github-trends |
| Description | 🚀 Level up your GitHub profile readme with customizable cards including LOC statistics! |
| Stars | 15926 |
| Forks | 117 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `7d1ec357a1033cd6828a6a194070167ccde20092` |
| Retrieved at | 2026-11-14T19:08:58.595504+00:00 |
| Files in this snapshot | 238 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (2 files)
    backend.yaml
    frontend.yaml
backend/  (141 files)
  deploy/  (3 files)
    app.yaml
    cloudbuild.yaml
    dispatch.yaml
  scripts/  (3 files)
    __init__.py
    delete_old_data.py
    local.py
  src/  (106 files)
    aggregation/  (11 files)
      … 11 files under this directory
    data/  (38 files)
      … 38 files under this directory
    models/  (15 files)
      … 15 files under this directory
    processing/  (13 files)
      … 13 files under this directory
    render/  (6 files)
      … 6 files under this directory
    routers/  (15 files)
      … 15 files under this directory
    utils/  (5 files)
      … 5 files under this directory
    __init__.py
    constants.py
    main.py
  tests/  (19 files)
    aggregation/  (4 files)
      … 4 files under this directory
    data/  (12 files)
      … 12 files under this directory
    utils/  (2 files)
      … 2 files under this directory
    __init__.py
  .coveragerc
  .env-template
  .flake8
  .gcloudignore
  .pre-commit-config.yaml
  README.md
  package.json
  pyproject.toml
  requirements.txt
  transfer_mongodb.bash
docs/  (4 files)
  API.md
  CONTRIBUTING.md
  FAQ.md
  THEME.md
frontend/  (87 files)
  deploy/  (1 files)
    Dockerfile
  public/  (5 files)
    _redirects
    manifest.json
    robots.txt
    trends.html
    wrapped.html
  src/  (73 files)
    api/  (3 files)
      … 3 files under this directory
    assets/  (1 files)
      … 1 files under this directory
    components/  (30 files)
      … 30 files under this directory
    pages/  (30 files)
      … 30 files under this directory
    redux/  (5 files)
      … 5 files under this directory
    constants.js
    index.css
    index.js
    utils.js
  .env-template
  .eslintrc.js
  .gitignore
  .prettierrc.js
  .yarnrc
  README.md
  package.json
  tailwind.config.js
.gitattributes
.gitignore
LICENSE
README.md
```

## Entry points

- [backend/src/main.py:27](https://github.com/avgupta456/github-trends/blob/7d1ec357a1033cd6828a6a194070167ccde20092/backend/src/main.py#L27)
- [backend/src/render/template.py:47](https://github.com/avgupta456/github-trends/blob/7d1ec357a1033cd6828a6a194070167ccde20092/backend/src/render/template.py#L47)
- [backend/scripts/delete_old_data.py:62](https://github.com/avgupta456/github-trends/blob/7d1ec357a1033cd6828a6a194070167ccde20092/backend/scripts/delete_old_data.py#L62)
- [backend/scripts/local.py:102](https://github.com/avgupta456/github-trends/blob/7d1ec357a1033cd6828a6a194070167ccde20092/backend/scripts/local.py#L102)
- [frontend/src/api/index.js](https://github.com/avgupta456/github-trends/blob/7d1ec357a1033cd6828a6a194070167ccde20092/frontend/src/api/index.js)
- [frontend/src/components/index.js](https://github.com/avgupta456/github-trends/blob/7d1ec357a1033cd6828a6a194070167ccde20092/frontend/src/components/index.js)
- [frontend/src/index.js](https://github.com/avgupta456/github-trends/blob/7d1ec357a1033cd6828a6a194070167ccde20092/frontend/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 16 file(s) under api layer (observed from repository paths and static analysis). Observed routes: GET /error, GET /stopwatch, GET /signup/public, GET /signup/private, GET /redirect. Observed top-level functions:… |
| backend package | library | Observed | Groups 36 file(s) under backend package (observed from repository paths and static analysis). Observed top-level classes: CommitLanguages, ContribsList, DateContainer, ListsContainer, StatsContainer. Observed top-level… |
| Configuration and deployment | config | Observed | Groups 13 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 48 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: CalendarData, CalendarDayDatum, CalendarLanguageDayDatum, ContribStats, ContributionDay, ContributionL… |
| Application entry point | entrypoint | Observed | Groups 11 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI, Group. Observed routes: GET /, GET /info, GET /{user_id}. Observed t… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| frontend package | library | Observed | Groups 68 file(s) under frontend package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 19 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: TestTemplate. |

## Important files

- `.github/workflows/backend.yaml` (ci)
- `.github/workflows/frontend.yaml` (ci)
- `backend/.pre-commit-config.yaml` (config)
- `backend/deploy/app.yaml` (config)
- `backend/deploy/cloudbuild.yaml` (config)
- `backend/deploy/dispatch.yaml` (config)
- `backend/package.json` (manifest)
- `backend/pyproject.toml` (manifest)
- `backend/requirements.txt` (manifest)
- `backend/src/data/github/extensions.json` (config)
- `frontend/deploy/Dockerfile` (container)
- `frontend/package.json` (manifest)
- `frontend/public/manifest.json` (config)

## Top-level layout

- `backend` — 141 analysed file(s)
- `frontend` — 87 analysed file(s)
- `(root files)` — 4 analysed file(s)
- `docs` — 4 analysed file(s)
- `.github` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- The GitHub repository was marked archived at selection time.

Commit `7d1ec357a1033cd6828a6a194070167ccde20092` is the revision these paths and observations refer to.
