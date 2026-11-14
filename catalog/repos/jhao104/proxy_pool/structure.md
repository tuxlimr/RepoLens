# Project structure: jhao104/proxy_pool

**Analysed commit:** `9cc0cad4c47e84e34aaec2eead099421960dcd07`

**Commit reference:** [9cc0cad4c47e84e34aaec2eead099421960dcd07](https://github.com/jhao104/proxy_pool/commit/9cc0cad4c47e84e34aaec2eead099421960dcd07)

**Tree at this commit:** [jhao104/proxy_pool@9cc0cad4c47e](https://github.com/jhao104/proxy_pool/tree/9cc0cad4c47e84e34aaec2eead099421960dcd07)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | jhao104/proxy_pool |
| Description | Python ProxyPool for web spider |
| Stars | 23793 |
| Forks | 5412 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `9cc0cad4c47e84e34aaec2eead099421960dcd07` |
| Retrieved at | 2026-11-14T19:07:43.806114+00:00 |
| Files in this snapshot | 91 |

## Directory tree

```text
.github/  (4 files)
  workflows/  (4 files)
    docker-image-latest.yml
    docker-image-tags.yml
    docs.yml
    test.yml
api/  (2 files)
  __init__.py
  proxyApi.py
db/  (4 files)
  __init__.py
  dbClient.py
  redisClient.py
  ssdbClient.py
docs/  (11 files)
  assets/  (1 files)
    logo.svg
  extending/  (2 files)
    fetcher.md
    validator.md
  stylesheets/  (1 files)
    extra.css
  api.md
  changelog.md
  configuration.md
  docker.md
  getting-started.md
  index.md
  project-structure.md
fetcher/  (17 files)
  sources/  (15 files)
    __init__.py
    daili66.py
    docip.py
    freevpnnode.py
    geonode.py
    goodips.py
    ihuan.py
    ip3366.py
    ip89.py
    kuaidaili.py
    kxdaili.py
    proxifly.py
    roundproxies.py
    scdn.py
    zdaye.py
  __init__.py
  baseFetcher.py
handler/  (4 files)
  __init__.py
  configHandler.py
  logHandler.py
  proxyHandler.py
helper/  (7 files)
  __init__.py
  check.py
  fetch.py
  launcher.py
  proxy.py
  scheduler.py
  validator.py
tests/  (22 files)
  api/  (2 files)
    __init__.py
    test_proxy_api.py
  integration/  (3 files)
    __init__.py
    test_redis_client.py
    test_ssdb_client.py
  unit/  (15 files)
    __init__.py
    test_base_fetcher.py
    test_check.py
    test_cli.py
    test_config.py
    test_db_client.py
    test_fetch.py
    test_fetcher_sources.py
    test_launcher.py
    test_log_handler.py
    test_proxy.py
    test_proxy_handler.py
    test_scheduler.py
    test_validator.py
    test_web_request.py
  __init__.py
  conftest.py
util/  (5 files)
  __init__.py
  lazyProperty.py
  singleton.py
  six.py
  webRequest.py
.gitignore
CLAUDE.md
Dockerfile
LICENSE
README.md
_config.yml
docker-compose.yml
mkdocs.yml
proxyPool.py
proxy_pool.sh
pyproject.toml
requirements-test.txt
requirements.txt
setting.py
tox.ini
```

## Entry points

- [api/proxyApi.py:28](https://github.com/jhao104/proxy_pool/blob/9cc0cad4c47e84e34aaec2eead099421960dcd07/api/proxyApi.py#L28)
- [fetcher/sources/daili66.py:40](https://github.com/jhao104/proxy_pool/blob/9cc0cad4c47e84e34aaec2eead099421960dcd07/fetcher/sources/daili66.py#L40)
- [fetcher/sources/docip.py:37](https://github.com/jhao104/proxy_pool/blob/9cc0cad4c47e84e34aaec2eead099421960dcd07/fetcher/sources/docip.py#L37)
- [fetcher/sources/freevpnnode.py:44](https://github.com/jhao104/proxy_pool/blob/9cc0cad4c47e84e34aaec2eead099421960dcd07/fetcher/sources/freevpnnode.py#L44)
- [fetcher/sources/geonode.py:47](https://github.com/jhao104/proxy_pool/blob/9cc0cad4c47e84e34aaec2eead099421960dcd07/fetcher/sources/geonode.py#L47)
- [fetcher/sources/goodips.py:35](https://github.com/jhao104/proxy_pool/blob/9cc0cad4c47e84e34aaec2eead099421960dcd07/fetcher/sources/goodips.py#L35)
- [fetcher/sources/ihuan.py:43](https://github.com/jhao104/proxy_pool/blob/9cc0cad4c47e84e34aaec2eead099421960dcd07/fetcher/sources/ihuan.py#L43)
- [fetcher/sources/ip3366.py:41](https://github.com/jhao104/proxy_pool/blob/9cc0cad4c47e84e34aaec2eead099421960dcd07/fetcher/sources/ip3366.py#L41)
- [fetcher/sources/ip89.py:36](https://github.com/jhao104/proxy_pool/blob/9cc0cad4c47e84e34aaec2eead099421960dcd07/fetcher/sources/ip89.py#L36)
- [fetcher/sources/kuaidaili.py:45](https://github.com/jhao104/proxy_pool/blob/9cc0cad4c47e84e34aaec2eead099421960dcd07/fetcher/sources/kuaidaili.py#L45)
- [fetcher/sources/kxdaili.py:38](https://github.com/jhao104/proxy_pool/blob/9cc0cad4c47e84e34aaec2eead099421960dcd07/fetcher/sources/kxdaili.py#L38)
- [fetcher/sources/proxifly.py:40](https://github.com/jhao104/proxy_pool/blob/9cc0cad4c47e84e34aaec2eead099421960dcd07/fetcher/sources/proxifly.py#L40)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 1 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 8 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 4 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: DbClient, RedisClient, SsdbClient. |
| Application entry point | entrypoint | Observed | Groups 18 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Flask. Observed routes: ROUTE /, ROUTE /get/, ROUTE /pop/, ROUTE /refresh/, R… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| fetcher package | library | Observed | Groups 3 file(s) under fetcher package (observed from repository paths and static analysis). Observed top-level classes: BaseFetcher. |
| handler package | library | Observed | Groups 3 file(s) under handler package (observed from repository paths and static analysis). Observed top-level classes: ConfigHandler, ProxyHandler. |
| helper package | library | Observed | Groups 6 file(s) under helper package (observed from repository paths and static analysis). Observed top-level classes: DoValidator, Fetcher, Proxy, ProxyValidator, _ThreadChecker, _ThreadFetcher. Observed top-level fun… |
| Tests | test | Observed | Groups 22 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH api.proxyApi.platform, PATCH api.proxyApi.app, PATCH helper.check.ConfigHandler, PATCH helper.check.ProxyValidat… |
| util package | library | Observed | Groups 5 file(s) under util package (observed from repository paths and static analysis). Observed top-level classes: LazyProperty, Singleton, WebRequest. Observed top-level functions: withMetaclass. |

## Important files

- `.github/workflows/docker-image-latest.yml` (ci)
- `.github/workflows/docker-image-tags.yml` (ci)
- `.github/workflows/docs.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `Dockerfile` (container)
- `_config.yml` (config)
- `docker-compose.yml` (container)
- `mkdocs.yml` (config)
- `pyproject.toml` (manifest)
- `requirements-test.txt` (manifest)
- `requirements.txt` (manifest)
- `tox.ini` (config)

## Top-level layout

- `tests` — 22 analysed file(s)
- `fetcher` — 17 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `docs` — 11 analysed file(s)
- `helper` — 7 analysed file(s)
- `util` — 5 analysed file(s)
- `.github` — 4 analysed file(s)
- `db` — 4 analysed file(s)
- `handler` — 4 analysed file(s)
- `api` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `9cc0cad4c47e84e34aaec2eead099421960dcd07` is the revision these paths and observations refer to.
