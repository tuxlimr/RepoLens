# Project structure: yoheinakajima/babyagi

**Analysed commit:** `fa8930ebe72a82e5ad57b356e7cbec96290e5bb2`

**Commit reference:** [fa8930ebe72a82e5ad57b356e7cbec96290e5bb2](https://github.com/yoheinakajima/babyagi/commit/fa8930ebe72a82e5ad57b356e7cbec96290e5bb2)

**Tree at this commit:** [yoheinakajima/babyagi@fa8930ebe72a](https://github.com/yoheinakajima/babyagi/tree/fa8930ebe72a82e5ad57b356e7cbec96290e5bb2)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | yoheinakajima/babyagi |
| Description | Not provided |
| Stars | 22359 |
| Forks | 2831 |
| Licence | Not detected |
| Language | Python |
| Default branch | main |
| Analysed commit | `fa8930ebe72a82e5ad57b356e7cbec96290e5bb2` |
| Retrieved at | 2026-11-14T19:07:52.101741+00:00 |
| Files in this snapshot | 65 |

## Directory tree

```text
babyagi/  (49 files)
  api/  (1 files)
    __init__.py
  dashboard/  (17 files)
    static/  (6 files)
      … 6 files under this directory
    templates/  (10 files)
      … 10 files under this directory
    __init__.py
  functionz/  (30 files)
    core/  (4 files)
      … 4 files under this directory
    db/  (5 files)
      … 5 files under this directory
    packs/  (20 files)
      … 20 files under this directory
    __init__.py
  __init__.py
examples/  (6 files)
  custom_flask_example.py
  custom_route_example.py
  quickstart_example.py
  self_build_example.py
  simple_example.py
  trigger_example.py
.gitignore
.replit
CNAME
CODE_READINESS_ANALYSIS.md
MANIFEST.in
README.md
main.py
pyproject.toml
requirements.txt
setup.py
```

## Entry points

- [babyagi/__init__.py:20](https://github.com/yoheinakajima/babyagi/blob/fa8930ebe72a82e5ad57b356e7cbec96290e5bb2/babyagi/__init__.py#L20)
- [main.py:15](https://github.com/yoheinakajima/babyagi/blob/fa8930ebe72a82e5ad57b356e7cbec96290e5bb2/main.py#L15)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 1 file(s) under api layer (observed from repository paths and static analysis). Observed top-level functions: create_api_blueprint. |
| babyagi package | library | Observed | Groups 27 file(s) under babyagi package (observed from repository paths and static analysis). Observed top-level functions: activate_function_version_wrapper, add_function_to_database, add_key_wrapper, add_new_function,… |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: parse_requirements. |
| Data layer | data | Observed | Groups 5 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: BaseDB, DBRouter, Function, FunctionVersion, Import, ImportResult. Observed top-level functions: get_or… |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Flask. Observed routes: ROUTE /. Observed top-level functions: __getattr__, cr… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 4 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: FunctionExecutor, FunctionRegistrar, Functionz. |

## Important files

- `MANIFEST.in` (manifest)
- `pyproject.toml` (manifest)
- `requirements.txt` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `babyagi` — 49 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `examples` — 6 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- File babyagi/functionz/packs/drafts/user_db.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `fa8930ebe72a82e5ad57b356e7cbec96290e5bb2` is the revision these paths and observations refer to.
