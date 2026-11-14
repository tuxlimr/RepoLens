# Project structure: FlareSolverr/FlareSolverr

**Analysed commit:** `cc2224b21e31c09a713eb25690a8e8dcdf50d8d8`

**Commit reference:** [cc2224b21e31c09a713eb25690a8e8dcdf50d8d8](https://github.com/FlareSolverr/FlareSolverr/commit/cc2224b21e31c09a713eb25690a8e8dcdf50d8d8)

**Tree at this commit:** [FlareSolverr/FlareSolverr@cc2224b21e31](https://github.com/FlareSolverr/FlareSolverr/tree/cc2224b21e31c09a713eb25690a8e8dcdf50d8d8)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | FlareSolverr/FlareSolverr |
| Description | Proxy server to bypass Cloudflare protection |
| Stars | 16227 |
| Forks | 1304 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `cc2224b21e31c09a713eb25690a8e8dcdf50d8d8` |
| Retrieved at | 2026-11-14T19:08:52.593244+00:00 |
| Files in this snapshot | 43 |

## Directory tree

```text
.github/  (5 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.yml
    config.yml
  workflows/  (3 files)
    autotag.yml
    release-docker.yml
    release.yml
html_samples/  (4 files)
  cloudflare_captcha_hcaptcha_v1.html
  cloudflare_captcha_norobot_v1.html
  cloudflare_init_v1.html
  cloudflare_spinner_v1.html
resources/  (1 files)
  flaresolverr_logo.svg
src/  (21 files)
  bottle_plugins/  (4 files)
    __init__.py
    error_plugin.py
    logger_plugin.py
    prometheus_plugin.py
  undetected_chromedriver/  (8 files)
    __init__.py
    cdp.py
    devtool.py
    dprocess.py
    options.py
    patcher.py
    reactor.py
    webelement.py
  build_package.py
  dtos.py
  flaresolverr.py
  flaresolverr_service.py
  metrics.py
  sessions.py
  tests.py
  tests_sites.py
  utils.py
.dockerignore
.gitignore
CHANGELOG.md
Dockerfile
LICENSE
README.md
SECURITY.md
docker-compose.yml
flaresolverr.service
package.json
requirements.txt
test-requirements.txt
```

## Entry points

- [src/build_package.py:110](https://github.com/FlareSolverr/FlareSolverr/blob/cc2224b21e31c09a713eb25690a8e8dcdf50d8d8/src/build_package.py#L110)
- [src/flaresolverr.py:71](https://github.com/FlareSolverr/FlareSolverr/blob/cc2224b21e31c09a713eb25690a8e8dcdf50d8d8/src/flaresolverr.py#L71)
- [src/tests.py:654](https://github.com/FlareSolverr/FlareSolverr/blob/cc2224b21e31c09a713eb25690a8e8dcdf50d8d8/src/tests.py#L654)
- [src/tests_sites.py:101](https://github.com/FlareSolverr/FlareSolverr/blob/cc2224b21e31c09a713eb25690a8e8dcdf50d8d8/src/tests_sites.py#L101)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bottle_plugins package | library | Observed | Groups 4 file(s) under bottle_plugins package (observed from repository paths and static analysis). Observed top-level functions: error_plugin, logger_plugin, prometheus_plugin, setup. |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| dtos.py package | library | Observed | Groups 1 file(s) under dtos.py package (observed from repository paths and static analysis). Observed top-level classes: ChallengeResolutionResultT, ChallengeResolutionT, HealthResponse, IndexResponse, V1RequestBase, V1… |
| Application entry point | entrypoint | Observed | Groups 4 file(s) under application entry point (observed from repository paths and static analysis). Observed routes: ROUTE /, ROUTE /health, POST /v1. Observed top-level classes: JSONErrorBottle, TestFlareSolverr. Obse… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| metrics.py package | library | Observed | Groups 1 file(s) under metrics.py package (observed from repository paths and static analysis). Observed top-level functions: serve, start_metrics_http_server. |
| Service / domain layer | service | Observed | Groups 1 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level functions: _cmd_request_get, _cmd_request_post, _cmd_sessions_create, _cmd_sessions_destroy, _cmd_se… |
| sessions.py package | library | Observed | Groups 1 file(s) under sessions.py package (observed from repository paths and static analysis). Observed top-level classes: Session, SessionsStorage. |
| undetected_chromedriver package | library | Observed | Groups 8 file(s) under undetected_chromedriver package (observed from repository paths and static analysis). Observed top-level classes: CDP, CDPObject, Chrome, ChromeOptions, PageElement, Patcher. Observed top-level fu… |
| utils.py package | library | Observed | Groups 1 file(s) under utils.py package (observed from repository paths and static analysis). Observed top-level functions: create_proxy_extension, extract_version_nt_executable, extract_version_nt_folder, extract_versi… |

## Important files

- `.dockerignore` (container)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/autotag.yml` (ci)
- `.github/workflows/release-docker.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `Dockerfile` (container)
- `docker-compose.yml` (container)
- `package.json` (manifest)
- `requirements.txt` (manifest)

## Top-level layout

- `src` — 21 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `.github` — 5 analysed file(s)
- `html_samples` — 4 analysed file(s)
- `resources` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `cc2224b21e31c09a713eb25690a8e8dcdf50d8d8` is the revision these paths and observations refer to.
