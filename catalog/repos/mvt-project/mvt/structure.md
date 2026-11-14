# Project structure: mvt-project/mvt

**Analysed commit:** `c9190e05ef4c67df6407bc8b2adbd904954b9388`

**Commit reference:** [c9190e05ef4c67df6407bc8b2adbd904954b9388](https://github.com/mvt-project/mvt/commit/c9190e05ef4c67df6407bc8b2adbd904954b9388)

**Tree at this commit:** [mvt-project/mvt@c9190e05ef4c](https://github.com/mvt-project/mvt/tree/c9190e05ef4c67df6407bc8b2adbd904954b9388)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | mvt-project/mvt |
| Description | MVT (Mobile Verification Toolkit) helps with conducting forensics of mobile devices in order to find signs of a potential compromise. |
| Stars | 16039 |
| Forks | 1568 |
| Licence | Other |
| Language | Python |
| Default branch | main |
| Analysed commit | `c9190e05ef4c67df6407bc8b2adbd904954b9388` |
| Retrieved at | 2026-11-14T19:08:56.426171+00:00 |
| Files in this snapshot | 326 |

## Directory tree

```text
.github/  (9 files)
  workflows/  (8 files)
    scripts/  (1 files)
      … 1 files under this directory
    add-issue-to-project.yml
    mypy.yml
    publish-release-docker.yml
    release.yml
    ruff.yml
    tests.yml
    update-ios-data.yml
  dependabot.yml
docs/  (25 files)
  android/  (4 files)
    adb.md
    backup.md
    intrusion_logs.md
    methodology.md
  development/  (4 files)
    custom_commands.md
    index.md
    plugin_configuration.md
    plugins.md
  ios/  (10 files)
    backup/  (4 files)
      … 4 files under this directory
    filesystem/  (2 files)
      … 2 files under this directory
    install.md
    methodology.md
    records.md
    sysdiagnose.md
  command_completion.md
  docker.md
  index.md
  install.md
  introduction.md
  iocs.md
  license.md
src/  (157 files)
  mvt/  (157 files)
    android/  (70 files)
      … 70 files under this directory
    common/  (24 files)
      … 24 files under this directory
    ios/  (60 files)
      … 60 files under this directory
    __init__.py
    cli.py
    plugin.py
tests/  (120 files)
  android/  (26 files)
    __init__.py
    test_artifact.py
    test_artifact_dumpsys_accessibility.py
    test_artifact_dumpsys_accessibility_count.py
    test_artifact_dumpsys_accessibility_state.py
    test_artifact_dumpsys_adb.py
    test_artifact_dumpsys_appops.py
    test_artifact_dumpsys_battery_daily.py
    test_artifact_dumpsys_battery_history.py
    test_artifact_dumpsys_dbinfo.py
    test_artifact_dumpsys_package_activities.py
    test_artifact_dumpsys_packages.py
    test_artifact_dumpsys_platform_compat.py
    test_artifact_dumpsys_receivers.py
    test_artifact_getprop.py
    test_artifact_mounts.py
    test_artifact_processes.py
    test_artifact_settings.py
    test_artifact_tombstone_caused_by.py
    test_artifact_tombstones.py
    test_backup_module.py
    test_backup_parser.py
    test_bugreport_section_extraction.py
    test_check_backup_optional_failure.py
    … 2 more files
  android_adb/  (1 files)
    __init__.py
  android_androidqf/  (9 files)
    __init__.py
    test_files.py
    test_getprop.py
    test_mounts.py
    test_packages.py
    test_processes.py
    test_root_binaries.py
    test_settings.py
    test_tcc.py
  android_bugreport/  (2 files)
    __init__.py
    test_bugreport.py
  artifacts/  (26 files)
    android_backup/  (1 files)
      … 1 files under this directory
    android_data/  (15 files)
      … 15 files under this directory
    androidqf/  (7 files)
      … 7 files under this directory
    stix2/  (1 files)
      … 1 files under this directory
    .gitignore
    generate_stix.py
  common/  (16 files)
    __init__.py
    test_alerts.py
    test_cli_plugins.py
    test_cmd_check_iocs.py
    test_cmd_plugins.py
    test_command.py
    test_command_modules.py
    test_config.py
    test_indicators.py
    test_module_loader.py
    test_password.py
    test_plugin.py
    test_plugin_config.py
    test_plugin_updates.py
    test_url.py
    test_utils.py
  ios_backup/  (16 files)
    __init__.py
    test_backup_info.py
    test_calendar.py
    test_datausage.py
    test_decrypt.py
    test_global_preferences.py
    test_interactionc.py
    test_manifest.py
    test_safari_browserstate.py
    test_safari_history.py
    test_sms.py
    test_sqlite_handling.py
    test_tcc.py
    test_webkit_resource_load_statistics.py
    test_whatsapp.py
    test_whatsapp_contacts.py
  ios_fs/  (4 files)
    __init__.py
    test_cache_files.py
    test_filesystem.py
    test_shutdownlog.py
  ios_sysdiagnose/  (2 files)
    __init__.py
    test_sysdiagnose_info.py
  __init__.py
  conftest.py
  plugin_fixtures.py
  test_check_android_adb_removed.py
  test_check_android_androidqf.py
  test_check_android_backup.py
  test_check_android_bugreport.py
  test_check_ios_backup.py
  test_check_ios_sysdiagnose.py
  test_cli.py
  test_cli_entry_points.py
  test_cli_startup.py
  test_cli_verbose.py
  test_cmd_check_sysdiagnose.py
  test_completion.py
  test_custom_modules.py
  test_ios_versions.py
  utils.py
.gitignore
.python-version
.readthedocs.yaml
.safety-policy.yml
CONTRIBUTING.md
Dockerfile
Dockerfile.android
Dockerfile.ios
LICENSE
MANIFEST.in
Makefile
README.md
SECURITY.md
mkdocs.yml
pyproject.toml
```

## Entry points

- [src/mvt/android/__init__.py](https://github.com/mvt-project/mvt/blob/c9190e05ef4c67df6407bc8b2adbd904954b9388/src/mvt/android/__init__.py)
- [src/mvt/android/cli.py:94](https://github.com/mvt-project/mvt/blob/c9190e05ef4c67df6407bc8b2adbd904954b9388/src/mvt/android/cli.py#L94)
- [src/mvt/cli.py](https://github.com/mvt-project/mvt/blob/c9190e05ef4c67df6407bc8b2adbd904954b9388/src/mvt/cli.py)
- [src/mvt/common/cmd_plugins.py:138](https://github.com/mvt-project/mvt/blob/c9190e05ef4c67df6407bc8b2adbd904954b9388/src/mvt/common/cmd_plugins.py#L138)
- [src/mvt/common/completion.py:67](https://github.com/mvt-project/mvt/blob/c9190e05ef4c67df6407bc8b2adbd904954b9388/src/mvt/common/completion.py#L67)
- [src/mvt/ios/__init__.py](https://github.com/mvt-project/mvt/blob/c9190e05ef4c67df6407bc8b2adbd904954b9388/src/mvt/ios/__init__.py)
- [src/mvt/ios/cli.py:106](https://github.com/mvt-project/mvt/blob/c9190e05ef4c67df6407bc8b2adbd904954b9388/src/mvt/ios/cli.py#L106)
- [.github/workflows/scripts/update-ios-releases.py:95](https://github.com/mvt-project/mvt/blob/c9190e05ef4c67df6407bc8b2adbd904954b9388/.github/workflows/scripts/update-ios-releases.py#L95)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 11 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: MVTSettings, Settings. |
| Application entry point | entrypoint | Observed | Groups 3 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: _get_disable_flags, _get_verbose, _load_custom_modules, check_adb, check_androidqf, chec… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| mvt package | library | Observed | Groups 148 file(s) under mvt package (observed from repository paths and static analysis). Observed top-level classes: AQFFiles, AQFGetProp, AQFLogTimestamps, AQFPackages, AQFProcesses, AQFSettings. Observed top-level f… |
| Tests | test | Observed | Groups 120 file(s) under tests (observed from repository paths and static analysis). Observed application object created via Command, Group. Observed top-level classes: AnotherModule, BackupCheckerModule, BackupOnlyModu… |

## Important files

- `.github/dependabot.yml` (config)
- `.github/workflows/add-issue-to-project.yml` (ci)
- `.github/workflows/mypy.yml` (ci)
- `.github/workflows/publish-release-docker.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/ruff.yml` (ci)
- `.github/workflows/scripts/update-ios-releases.py` (ci)
- `.github/workflows/tests.yml` (ci)
- `.github/workflows/update-ios-data.yml` (ci)
- `.readthedocs.yaml` (config)
- `.safety-policy.yml` (config)
- `Dockerfile` (container)
- `Dockerfile.android` (container)
- `Dockerfile.ios` (container)
- `MANIFEST.in` (manifest)
- `mkdocs.yml` (config)
- `pyproject.toml` (manifest)
- `src/mvt/ios/data/ios_models.json` (config)
- `src/mvt/ios/data/ios_versions.json` (config)

## Top-level layout

- `src` — 157 analysed file(s)
- `tests` — 120 analysed file(s)
- `docs` — 25 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `.github` — 9 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `c9190e05ef4c67df6407bc8b2adbd904954b9388` is the revision these paths and observations refer to.
