# Project structure: MetaCubeX/mihomo

**Analysed commit:** `008b91bfe8c0e2daca0ab69061efd9ea1ad71bd2`

**Commit reference:** [008b91bfe8c0e2daca0ab69061efd9ea1ad71bd2](https://github.com/MetaCubeX/mihomo/commit/008b91bfe8c0e2daca0ab69061efd9ea1ad71bd2)

**Tree at this commit:** [MetaCubeX/mihomo@008b91bfe8c0](https://github.com/MetaCubeX/mihomo/tree/008b91bfe8c0e2daca0ab69061efd9ea1ad71bd2)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | MetaCubeX/mihomo |
| Description | A simple Python Pydantic model for Honkai: Star Rail parsed data from the Mihomo API. |
| Stars | 35765 |
| Forks | 4774 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `008b91bfe8c0e2daca0ab69061efd9ea1ad71bd2` |
| Retrieved at | 2026-11-14T19:06:54.845533+00:00 |
| Files in this snapshot | 30 |

## Directory tree

```text
.github/  (7 files)
  ISSUE_TEMPLATE/  (5 files)
    bug_report.yml
    bug_report_zh.yml
    config.yml
    feature_request.yml
    feature_request_zh.yml
  workflows/  (2 files)
    Delete.yml
    build.yml
examples/  (3 files)
  basic.py
  data_persistence.py
  merge_data.py
mihomo/  (16 files)
  models/  (12 files)
    v1/  (5 files)
      … 5 files under this directory
    __init__.py
    base.py
    character.py
    combat.py
    equipment.py
    player.py
    stat.py
  __init__.py
  client.py
  errors.py
  tools.py
.gitignore
LICENSE
README.md
pyproject.toml
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 12 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: Attribute, Avatar, Character, EidolonIcon, Element, ForgottenHall. |
| External integrations | external | Observed | Groups 1 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: Language, MihomoAPI. |
| mihomo package | library | Observed | Groups 3 file(s) under mihomo package (observed from repository paths and static analysis). Observed top-level classes: BaseException, HttpRequestError, InvalidParams, UserNotFound. Observed top-level functions: merge_c… |

## Important files

- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/bug_report_zh.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request_zh.yml` (config)
- `.github/workflows/Delete.yml` (ci)
- `.github/workflows/build.yml` (ci)
- `pyproject.toml` (manifest)

## Top-level layout

- `mihomo` — 16 analysed file(s)
- `.github` — 7 analysed file(s)
- `(root files)` — 4 analysed file(s)
- `examples` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `008b91bfe8c0e2daca0ab69061efd9ea1ad71bd2` is the revision these paths and observations refer to.
