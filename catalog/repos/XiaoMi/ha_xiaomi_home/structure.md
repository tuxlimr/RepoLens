# Project structure: XiaoMi/ha_xiaomi_home

**Analysed commit:** `75b3acb6325a3a8d295688b13904737d6738a6a5`

**Commit reference:** [75b3acb6325a3a8d295688b13904737d6738a6a5](https://github.com/XiaoMi/ha_xiaomi_home/commit/75b3acb6325a3a8d295688b13904737d6738a6a5)

**Tree at this commit:** [XiaoMi/ha_xiaomi_home@75b3acb6325a](https://github.com/XiaoMi/ha_xiaomi_home/tree/75b3acb6325a3a8d295688b13904737d6738a6a5)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | XiaoMi/ha_xiaomi_home |
| Description | Xiaomi Home Integration for Home Assistant |
| Stars | 22343 |
| Forks | 1204 |
| Licence | Other |
| Language | Python |
| Default branch | main |
| Analysed commit | `75b3acb6325a3a8d295688b13904737d6738a6a5` |
| Retrieved at | 2026-11-14T19:07:52.865978+00:00 |
| Files in this snapshot | 100 |

## Directory tree

```text
.github/  (5 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.yaml
    config.yml
  workflows/  (3 files)
    release.yaml
    test.yaml
    validate.yaml
custom_components/  (69 files)
  xiaomi_home/  (69 files)
    miot/  (35 files)
      … 35 files under this directory
    translations/  (13 files)
      … 13 files under this directory
    __init__.py
    binary_sensor.py
    button.py
    climate.py
    config_flow.py
    cover.py
    device_tracker.py
    event.py
    fan.py
    humidifier.py
    light.py
    manifest.json
    media_player.py
    notify.py
    number.py
    select.py
    sensor.py
    switch.py
    text.py
    vacuum.py
    water_heater.py
doc/  (2 files)
  CONTRIBUTING_zh.md
  README_zh.md
test/  (12 files)
  .gitignore
  check_rule_format.py
  conftest.py
  pytest.ini
  test_cloud.py
  test_common.py
  test_lan.py
  test_mdns.py
  test_mips.py
  test_network.py
  test_spec.py
  test_storage.py
tools/  (2 files)
  common.py
  update_lan_rule.py
.gitignore
.pylintrc
CHANGELOG.md
CLAUDE.md
CONTRIBUTING.md
LICENSE.md
LegalNotice.md
README.md
hacs.json
install.sh
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 34 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| custom_components package | library | Observed | Groups 34 file(s) under custom_components package (observed from repository paths and static analysis). Observed top-level classes: ActionText, AirConditioner, BinarySensor, Button, Cover, DeviceManufacturer. Observed t… |
| External integrations | external | Observed | Groups 1 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: CtrlMode, MIoTClient, MIoTClientSub. Observed top-level functions: get_miot_instance_async. |
| Tests | test | Observed | Groups 12 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: bool_trans, compare_dict_structure, dict_str_dict, dict_str_str, load_json_file, load_py_file. |
| tools package | library | Observed | Groups 2 file(s) under tools package (observed from repository paths and static analysis). Observed top-level functions: http_get, load_json_file, load_yaml_file, save_json_file, save_yaml_file, update_profile_model. |

## Important files

- `.github/ISSUE_TEMPLATE/bug_report.yaml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/release.yaml` (ci)
- `.github/workflows/test.yaml` (ci)
- `.github/workflows/validate.yaml` (ci)
- `custom_components/xiaomi_home/manifest.json` (config)
- `custom_components/xiaomi_home/miot/i18n/de.json` (config)
- `custom_components/xiaomi_home/miot/i18n/en.json` (config)
- `custom_components/xiaomi_home/miot/i18n/es.json` (config)
- `custom_components/xiaomi_home/miot/i18n/fr.json` (config)
- `custom_components/xiaomi_home/miot/i18n/it.json` (config)
- `custom_components/xiaomi_home/miot/i18n/ja.json` (config)
- `custom_components/xiaomi_home/miot/i18n/nl.json` (config)
- `custom_components/xiaomi_home/miot/i18n/pt-BR.json` (config)
- `custom_components/xiaomi_home/miot/i18n/pt.json` (config)
- `custom_components/xiaomi_home/miot/i18n/ru.json` (config)
- `custom_components/xiaomi_home/miot/i18n/tr.json` (config)
- `custom_components/xiaomi_home/miot/i18n/zh-Hans.json` (config)
- `custom_components/xiaomi_home/miot/i18n/zh-Hant.json` (config)
- `custom_components/xiaomi_home/miot/lan/profile_models.yaml` (config)
- `custom_components/xiaomi_home/miot/specs/bool_trans.yaml` (config)
- `custom_components/xiaomi_home/miot/specs/multi_lang.json` (config)
- `custom_components/xiaomi_home/miot/specs/spec_add.json` (config)
- `custom_components/xiaomi_home/miot/specs/spec_filter.yaml` (config)
- `custom_components/xiaomi_home/miot/specs/spec_modify.yaml` (config)
- `custom_components/xiaomi_home/translations/de.json` (config)
- `custom_components/xiaomi_home/translations/en.json` (config)
- `custom_components/xiaomi_home/translations/es.json` (config)
- `custom_components/xiaomi_home/translations/fr.json` (config)
- `custom_components/xiaomi_home/translations/it.json` (config)
- `custom_components/xiaomi_home/translations/ja.json` (config)
- `custom_components/xiaomi_home/translations/nl.json` (config)
- `custom_components/xiaomi_home/translations/pt-BR.json` (config)
- `custom_components/xiaomi_home/translations/pt.json` (config)
- `custom_components/xiaomi_home/translations/ru.json` (config)
- `custom_components/xiaomi_home/translations/tr.json` (config)
- `custom_components/xiaomi_home/translations/zh-Hans.json` (config)
- `custom_components/xiaomi_home/translations/zh-Hant.json` (config)
- `hacs.json` (config)

## Top-level layout

- `custom_components` — 69 analysed file(s)
- `test` — 12 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `.github` — 5 analysed file(s)
- `doc` — 2 analysed file(s)
- `tools` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `75b3acb6325a3a8d295688b13904737d6738a6a5` is the revision these paths and observations refer to.
