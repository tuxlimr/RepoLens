# Project structure: waydroid/waydroid

**Analysed commit:** `db7294c4c2bd43157bab94cf8a3015e22d9f1ad8`

**Commit reference:** [db7294c4c2bd43157bab94cf8a3015e22d9f1ad8](https://github.com/waydroid/waydroid/commit/db7294c4c2bd43157bab94cf8a3015e22d9f1ad8)

**Tree at this commit:** [waydroid/waydroid@db7294c4c2bd](https://github.com/waydroid/waydroid/tree/db7294c4c2bd43157bab94cf8a3015e22d9f1ad8)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | waydroid/waydroid |
| Description | Waydroid uses a container-based approach to boot a full Android system on a regular GNU/Linux system like Ubuntu. |
| Stars | 12534 |
| Forks | 563 |
| Licence | GPL-3.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `db7294c4c2bd43157bab94cf8a3015e22d9f1ad8` |
| Retrieved at | 2026-11-14T19:10:05.277523+00:00 |
| Files in this snapshot | 81 |

## Directory tree

```text
.github/  (4 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.yml
    feature_request.yml
  workflows/  (1 files)
    check.yaml
  dependabot.yaml
data/  (16 files)
  configs/  (8 files)
    apparmor_profiles/  (3 files)
      … 3 files under this directory
    config_1
    config_3
    config_4
    config_base
    waydroid.seccomp
  scripts/  (2 files)
    waydroid-net.sh
    waydroid-post-stop.sh
  Waydroid.desktop
  id.waydro.waydroid.metainfo.xml
  waydroid.app.install.desktop
  waydroid.directory
  waydroid.market.desktop
  waydroid.menu
dbus/  (3 files)
  id.waydro.Container.conf
  id.waydro.Container.policy
  id.waydro.Container.service
debian/  (7 files)
  source/  (1 files)
    format
  changelog
  compat
  control
  copyright
  rules
  waydroid.postinst
systemd/  (1 files)
  waydroid-container.service
tools/  (42 files)
  actions/  (9 files)
    __init__.py
    app_manager.py
    bugreport.py
    container_manager.py
    initializer.py
    prop.py
    session_manager.py
    status.py
    upgrader.py
  config/  (3 files)
    __init__.py
    load.py
    save.py
  helpers/  (17 files)
    __init__.py
    arch.py
    arguments.py
    drivers.py
    gpu.py
    http.py
    images.py
    ipc.py
    logging.py
    lxc.py
    mount.py
    net.py
    props.py
    protocol.py
    run.py
    run_core.py
    version.py
  interfaces/  (7 files)
    IClipboard.py
    IHardware.py
    INotificationCallback.py
    INotifications.py
    IPlatform.py
    IStatusBarService.py
    IUserMonitor.py
  services/  (5 files)
    __init__.py
    clipboard_manager.py
    hardware_manager.py
    notification_manager.py
    user_manager.py
  __init__.py
.abstruse.yml
.gitignore
FUNDING.yml
LICENSE
Makefile
README.md
pyproject.toml
waydroid.py
```

## Entry points

- [tools/__init__.py:172](https://github.com/waydroid/waydroid/blob/db7294c4c2bd43157bab94cf8a3015e22d9f1ad8/tools/__init__.py#L172)
- [waydroid.py:9](https://github.com/waydroid/waydroid/blob/db7294c4c2bd43157bab94cf8a3015e22d9f1ad8/waydroid.py#L9)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: load, load_channels, save. |
| Data layer | data | Observed | Groups 2 file(s) under data layer (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 3 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: flat_cmd, main, prep_args, root, user. |
| Service / domain layer | service | Observed | Groups 5 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level functions: start, stop. |
| tools package | library | Observed | Groups 32 file(s) under tools package (observed from repository paths and static analysis). Observed top-level classes: Action, DbusContainerManager, DbusInitializer, DbusSessionManager, INotificationCallback, IPlatform… |

## Important files

- `.abstruse.yml` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/dependabot.yaml` (config)
- `.github/workflows/check.yaml` (ci)
- `FUNDING.yml` (config)
- `pyproject.toml` (manifest)

## Top-level layout

- `tools` — 42 analysed file(s)
- `data` — 16 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `debian` — 7 analysed file(s)
- `.github` — 4 analysed file(s)
- `dbus` — 3 analysed file(s)
- `systemd` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `db7294c4c2bd43157bab94cf8a3015e22d9f1ad8` is the revision these paths and observations refer to.
