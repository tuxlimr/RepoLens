# Project structure: mxrch/GHunt

**Analysed commit:** `5ee893929c51c7a8a665b199bbae04ce85a662b4`

**Commit reference:** [5ee893929c51c7a8a665b199bbae04ce85a662b4](https://github.com/mxrch/GHunt/commit/5ee893929c51c7a8a665b199bbae04ce85a662b4)

**Tree at this commit:** [mxrch/GHunt@5ee893929c51](https://github.com/mxrch/GHunt/tree/5ee893929c51c7a8a665b199bbae04ce85a662b4)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | mxrch/GHunt |
| Description | 🕵️‍♂️ Offensive Google framework. |
| Stars | 19849 |
| Forks | 1752 |
| Licence | Other |
| Language | Python |
| Default branch | master |
| Analysed commit | `5ee893929c51c7a8a665b199bbae04ce85a662b4` |
| Retrieved at | 2026-11-14T19:08:06.037245+00:00 |
| Files in this snapshot | 90 |

## Directory tree

```text
.github/  (3 files)
  ISSUE_TEMPLATE/  (1 files)
    bug_report.md
  workflows/  (1 files)
    sponsors.yml
  FUNDING.yml
examples/  (2 files)
  email_registered.py
  get_people_name.py
ghunt/  (80 files)
  apis/  (14 files)
    __init__.py
    accounts.py
    calendar.py
    clientauthconfig.py
    digitalassetslinks.py
    drive.py
    fireconsolepa.py
    geolocation.py
    identitytoolkit.py
    mobilesdk.py
    peoplepa.py
    playgames.py
    playgateway.py
    vision.py
  helpers/  (15 files)
    __init__.py
    auth.py
    banner.py
    calendar.py
    drive.py
    gcp.py
    gmail.py
    gmaps.py
    ia.py
    iam.py
    knowledge.py
    listener.py
    playgames.py
    playstore.py
    utils.py
  knowledge/  (7 files)
    __init__.py
    drive.py
    keys.py
    maps.py
    people.py
    services.py
    sig.py
  lib/  (2 files)
    __init__.py
    httpx.py
  modules/  (7 files)
    __init__.py
    drive.py
    email.py
    gaia.py
    geolocate.py
    login.py
    spiderdal.py
  objects/  (6 files)
    __init__.py
    apis.py
    base.py
    encoders.py
    session.py
    utils.py
  parsers/  (12 files)
    __init__.py
    calendar.py
    clientauthconfig.py
    digitalassetslinks.py
    drive.py
    geolocate.py
    identitytoolkit.py
    mobilesdk.py
    people.py
    playgames.py
    playgateway.py
    vision.py
  protos/  (10 files)
    playgatewaypa/  (9 files)
      … 9 files under this directory
    __init__.py
  __init__.py
  cli.py
  config.py
  errors.py
  ghunt.py
  globals.py
  version.py
.gitignore
LICENSE.md
README.md
main.py
pyproject.toml
```

## Entry points

- [main.py:1](https://github.com/mxrch/GHunt/blob/5ee893929c51c7a8a665b199bbae04ce85a662b4/main.py#L1)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: parse_and_run, process_args. |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| ghunt package | library | Observed | Groups 73 file(s) under ghunt package (observed from repository paths and static analysis). Observed top-level classes: Accounts, AndroidCreds, Asset, AsyncClient, CacBrand, CacBrandState. Observed top-level functions:… |
| Service / domain layer | service | Observed | Groups 1 file(s) under service / domain layer (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/workflows/sponsors.yml` (ci)
- `pyproject.toml` (manifest)

## Top-level layout

- `ghunt` — 80 analysed file(s)
- `(root files)` — 5 analysed file(s)
- `.github` — 3 analysed file(s)
- `examples` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `5ee893929c51c7a8a665b199bbae04ce85a662b4` is the revision these paths and observations refer to.
