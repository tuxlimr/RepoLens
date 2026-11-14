# Project structure: OpenEthan/SMSBoom

**Analysed commit:** `38ccbeccb05fab66442988b38b559062d7cf92d8`

**Commit reference:** [38ccbeccb05fab66442988b38b559062d7cf92d8](https://github.com/OpenEthan/SMSBoom/commit/38ccbeccb05fab66442988b38b559062d7cf92d8)

**Tree at this commit:** [OpenEthan/SMSBoom@38ccbeccb05f](https://github.com/OpenEthan/SMSBoom/tree/38ccbeccb05fab66442988b38b559062d7cf92d8)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | OpenEthan/SMSBoom |
| Description | SMSBoom - Deprecate: Due to judicial reasons, the repository has been suspended! |
| Stars | 15073 |
| Forks | 3527 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `38ccbeccb05fab66442988b38b559062d7cf92d8` |
| Retrieved at | 2026-11-14T19:09:10.171131+00:00 |
| Files in this snapshot | 21 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    run.yaml
debug/  (7 files)
  __init__.py
  api.js
  api_tou.json
  hz-web.json
  spider-api.py
  tou_api.py
  touapi.json
utils/  (5 files)
  __init__.py
  log.py
  models.py
  req.py
  sql.py
.gitignore
Dockerfile
GETAPI.json
LICENSE
README.md
api.json
smsboom.py
smsboom_GUI.py
```

## Entry points

- [debug/spider-api.py:175](https://github.com/OpenEthan/SMSBoom/blob/38ccbeccb05fab66442988b38b559062d7cf92d8/debug/spider-api.py#L175)
- [debug/tou_api.py:39](https://github.com/OpenEthan/SMSBoom/blob/38ccbeccb05fab66442988b38b559062d7cf92d8/debug/tou_api.py#L39)
- [smsboom.py:105](https://github.com/OpenEthan/SMSBoom/blob/38ccbeccb05fab66442988b38b559062d7cf92d8/smsboom.py#L105)
- [smsboom_GUI.py:51](https://github.com/OpenEthan/SMSBoom/blob/38ccbeccb05fab66442988b38b559062d7cf92d8/smsboom_GUI.py#L51)
- [utils/log.py:43](https://github.com/OpenEthan/SMSBoom/blob/38ccbeccb05fab66442988b38b559062d7cf92d8/utils/log.py#L43)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: API. |
| debug package | library | Observed | Groups 2 file(s) under debug package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 5 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: API, Application, InputWidget, SMS. Observed top-level functions: asyncRun, cli, load_api_… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 3 file(s) under utils package (observed from repository paths and static analysis). Observed top-level classes: Sql. Observed top-level functions: asyncReqs, callback, default_header_user_agent, reqAPI, reqFunc,… |

## Important files

- `.github/workflows/run.yaml` (ci)
- `Dockerfile` (container)
- `GETAPI.json` (config)
- `api.json` (config)
- `debug/api_tou.json` (config)
- `debug/hz-web.json` (config)
- `debug/touapi.json` (config)

## Top-level layout

- `(root files)` — 8 analysed file(s)
- `debug` — 7 analysed file(s)
- `utils` — 5 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- The GitHub repository was marked archived at selection time.

Commit `38ccbeccb05fab66442988b38b559062d7cf92d8` is the revision these paths and observations refer to.
