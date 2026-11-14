# Project structure: pjialin/py12306

**Analysed commit:** `52ccae8b206b828624f185bf8178e1057c6b5fb9`

**Commit reference:** [52ccae8b206b828624f185bf8178e1057c6b5fb9](https://github.com/pjialin/py12306/commit/52ccae8b206b828624f185bf8178e1057c6b5fb9)

**Tree at this commit:** [pjialin/py12306@52ccae8b206b](https://github.com/pjialin/py12306/tree/52ccae8b206b828624f185bf8178e1057c6b5fb9)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | pjialin/py12306 |
| Description | 🚂 12306 购票助手，支持集群，多账号，多任务购票以及 Web 页面管理  |
| Stars | 14970 |
| Forks | 3564 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `52ccae8b206b828624f185bf8178e1057c6b5fb9` |
| Retrieved at | 2026-11-14T19:09:10.590130+00:00 |
| Files in this snapshot | 68 |

## Directory tree

```text
data/  (2 files)
  cdn.txt
  stations.txt
py12306/  (51 files)
  cluster/  (3 files)
    __init__.py
    cluster.py
    redis.py
  exceptions/  (1 files)
    __init__.py
  helpers/  (12 files)
    OCR.py
    __init__.py
    api.py
    auth_code.py
    cdn.py
    event.py
    func.py
    notification.py
    qrcode.py
    request.py
    station.py
    type.py
  log/  (8 files)
    __init__.py
    base.py
    cluster_log.py
    common_log.py
    order_log.py
    query_log.py
    redis_log.py
    user_log.py
  order/  (1 files)
    order.py
  query/  (3 files)
    __init__.py
    job.py
    query.py
  user/  (3 files)
    __init__.py
    job.py
    user.py
  vender/  (1 files)
    ruokuai/  (1 files)
      … 1 files under this directory
  web/  (16 files)
    handler/  (6 files)
      … 6 files under this directory
    static/  (8 files)
      … 8 files under this directory
    __init__.py
    web.py
  __init__.py
  app.py
  config.py
runtime/  (3 files)
  query/  (1 files)
    .gitignore
  user/  (1 files)
    .gitignore
  .gitignore
.gitignore
.gitpod.yml
Dockerfile
LICENSE
README.md
depdencies.txt
docker-compose.yml.example
env.docker.py.example
env.py.example
env.slave.py.example
main.py
requirements.txt
```

## Entry points

- [main.py:63](https://github.com/pjialin/py12306/blob/52ccae8b206b828624f185bf8178e1057c6b5fb9/main.py#L63)
- [py12306/helpers/OCR.py:74](https://github.com/pjialin/py12306/blob/52ccae8b206b828624f185bf8178e1057c6b5fb9/py12306/helpers/OCR.py#L74)
- [py12306/helpers/auth_code.py:84](https://github.com/pjialin/py12306/blob/52ccae8b206b828624f185bf8178e1057c6b5fb9/py12306/helpers/auth_code.py#L84)
- [py12306/helpers/cdn.py:230](https://github.com/pjialin/py12306/blob/52ccae8b206b828624f185bf8178e1057c6b5fb9/py12306/helpers/cdn.py#L230)
- [py12306/helpers/notification.py:240](https://github.com/pjialin/py12306/blob/52ccae8b206b828624f185bf8178e1057c6b5fb9/py12306/helpers/notification.py#L240)
- [py12306/vender/ruokuai/main.py:50](https://github.com/pjialin/py12306/blob/52ccae8b206b828624f185bf8178e1057c6b5fb9/py12306/vender/ruokuai/main.py#L50)
- [py12306/web/web.py:61](https://github.com/pjialin/py12306/blob/52ccae8b206b828624f185bf8178e1057c6b5fb9/py12306/web/web.py#L61)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 4 file(s) under api layer (observed from repository paths and static analysis). Observed routes: ROUTE /log/output, ROUTE /query, ROUTE /stat/dashboard, ROUTE /stat/cluster, ROUTE /login. Observed top-level funct… |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: Config, EnvLoader. |
| Application entry point | entrypoint | Observed | Groups 9 file(s) under application entry point (observed from repository paths and static analysis). Observed routes: ROUTE /, ROUTE /app/menus, ROUTE /app/actions. Observed top-level classes: App, AuthCode, Cdn, Dict,… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| py12306 package | library | Observed | Groups 35 file(s) under py12306 package (observed from repository paths and static analysis). Observed top-level classes: BaseLog, Browser, Cluster, ClusterLog, CommonLog, Const. Observed top-level functions: array_dict… |

## Important files

- `.gitpod.yml` (config)
- `Dockerfile` (container)
- `requirements.txt` (manifest)

## Top-level layout

- `py12306` — 51 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `runtime` — 3 analysed file(s)
- `data` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `52ccae8b206b828624f185bf8178e1057c6b5fb9` is the revision these paths and observations refer to.
