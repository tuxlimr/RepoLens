# Project structure: karpathy/llm-council

**Analysed commit:** `92e1fccb1bdcf1bab7221aa9ed90f9dc72529131`

**Commit reference:** [92e1fccb1bdcf1bab7221aa9ed90f9dc72529131](https://github.com/karpathy/llm-council/commit/92e1fccb1bdcf1bab7221aa9ed90f9dc72529131)

**Tree at this commit:** [karpathy/llm-council@92e1fccb1bdc](https://github.com/karpathy/llm-council/tree/92e1fccb1bdcf1bab7221aa9ed90f9dc72529131)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | karpathy/llm-council |
| Description | LLM Council works together to answer your hardest questions |
| Stars | 26518 |
| Forks | 4529 |
| Licence | Not detected |
| Language | Python |
| Default branch | master |
| Analysed commit | `92e1fccb1bdcf1bab7221aa9ed90f9dc72529131` |
| Retrieved at | 2026-11-14T19:07:22.379664+00:00 |
| Files in this snapshot | 36 |

## Directory tree

```text
backend/  (6 files)
  __init__.py
  config.py
  council.py
  main.py
  openrouter.py
  storage.py
frontend/  (23 files)
  public/  (1 files)
    vite.svg
  src/  (16 files)
    assets/  (1 files)
      … 1 files under this directory
    components/  (10 files)
      … 10 files under this directory
    App.css
    App.jsx
    api.js
    index.css
    main.jsx
  .gitignore
  README.md
  eslint.config.js
  index.html
  package.json
  vite.config.js
.gitignore
.python-version
CLAUDE.md
README.md
main.py
pyproject.toml
start.sh
```

## Entry points

- [backend/main.py:15](https://github.com/karpathy/llm-council/blob/92e1fccb1bdcf1bab7221aa9ed90f9dc72529131/backend/main.py#L15)
- [main.py:5](https://github.com/karpathy/llm-council/blob/92e1fccb1bdcf1bab7221aa9ed90f9dc72529131/main.py#L5)
- [frontend/src/App.jsx](https://github.com/karpathy/llm-council/blob/92e1fccb1bdcf1bab7221aa9ed90f9dc72529131/frontend/src/App.jsx)
- [frontend/src/main.jsx](https://github.com/karpathy/llm-council/blob/92e1fccb1bdcf1bab7221aa9ed90f9dc72529131/frontend/src/main.jsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| backend package | library | Observed | Groups 4 file(s) under backend package (observed from repository paths and static analysis). Observed top-level functions: add_assistant_message, add_user_message, calculate_aggregate_rankings, create_conversation, ensu… |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed routes: GET /, GET /api/conversations, POST /api/conversatio… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| frontend package | library | Observed | Groups 10 file(s) under frontend package (observed from repository paths and static analysis). |

## Important files

- `frontend/package.json` (manifest)
- `pyproject.toml` (manifest)

## Top-level layout

- `frontend` — 23 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `backend` — 6 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `92e1fccb1bdcf1bab7221aa9ed90f9dc72529131` is the revision these paths and observations refer to.
