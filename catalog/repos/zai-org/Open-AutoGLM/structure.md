# Project structure: zai-org/Open-AutoGLM

**Analysed commit:** `86f55382982fb054e8fc98ca80609dff8a2cdc3c`

**Commit reference:** [86f55382982fb054e8fc98ca80609dff8a2cdc3c](https://github.com/zai-org/Open-AutoGLM/commit/86f55382982fb054e8fc98ca80609dff8a2cdc3c)

**Tree at this commit:** [zai-org/Open-AutoGLM@86f55382982f](https://github.com/zai-org/Open-AutoGLM/tree/86f55382982fb054e8fc98ca80609dff8a2cdc3c)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | zai-org/Open-AutoGLM |
| Description | An Open Phone Agent Model & Framework. Unlocking the AI Phone for Everyone |
| Stars | 26592 |
| Forks | 4062 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `86f55382982fb054e8fc98ca80609dff8a2cdc3c` |
| Retrieved at | 2026-11-14T19:07:21.836686+00:00 |
| Files in this snapshot | 55 |

## Directory tree

```text
.github/  (3 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.yaml
    feature-request.yaml
  PULL_REQUEST_TEMPLATE.md
docs/  (1 files)
  ios_setup/  (1 files)
    ios_setup.md
examples/  (2 files)
  basic_usage.py
  demo_thinking.py
phone_agent/  (33 files)
  actions/  (3 files)
    __init__.py
    handler.py
    handler_ios.py
  adb/  (5 files)
    __init__.py
    connection.py
    device.py
    input.py
    screenshot.py
  config/  (9 files)
    __init__.py
    apps.py
    apps_harmonyos.py
    apps_ios.py
    i18n.py
    prompts.py
    prompts_en.py
    prompts_zh.py
    timing.py
  hdc/  (5 files)
    __init__.py
    connection.py
    device.py
    input.py
    screenshot.py
  model/  (2 files)
    __init__.py
    client.py
  xctest/  (5 files)
    __init__.py
    connection.py
    device.py
    input.py
    screenshot.py
  __init__.py
  agent.py
  agent_ios.py
  device_factory.py
resources/  (4 files)
  WECHAT.md
  logo.svg
  privacy_policy.txt
  privacy_policy_en.txt
scripts/  (2 files)
  check_deployment_cn.py
  check_deployment_en.py
.gitignore
.pre-commit-config.yaml
LICENSE
README.md
README_coding_agent.md
README_en.md
ios.py
main.py
requirements.txt
setup.py
```

## Entry points

- [ios.py:549](https://github.com/zai-org/Open-AutoGLM/blob/86f55382982fb054e8fc98ca80609dff8a2cdc3c/ios.py#L549)
- [main.py](https://github.com/zai-org/Open-AutoGLM/blob/86f55382982fb054e8fc98ca80609dff8a2cdc3c/main.py)
- [phone_agent/hdc/device.py:309](https://github.com/zai-org/Open-AutoGLM/blob/86f55382982fb054e8fc98ca80609dff8a2cdc3c/phone_agent/hdc/device.py#L309)
- [scripts/check_deployment_cn.py:7](https://github.com/zai-org/Open-AutoGLM/blob/86f55382982fb054e8fc98ca80609dff8a2cdc3c/scripts/check_deployment_cn.py#L7)
- [scripts/check_deployment_en.py:7](https://github.com/zai-org/Open-AutoGLM/blob/86f55382982fb054e8fc98ca80609dff8a2cdc3c/scripts/check_deployment_en.py#L7)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 11 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: ActionTimingConfig, ConnectionTimingConfig, DeviceTimingConfig, TimingConfig. Observ… |
| Application entry point | entrypoint | Observed | Groups 5 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: _get_hdc_prefix, back, check_model_api, check_system_requirements, double_tap, get_curre… |
| External integrations | external | Observed | Groups 1 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: MessageBuilder, ModelClient, ModelConfig, ModelResponse. |
| phone_agent package | library | Observed | Groups 22 file(s) under phone_agent package (observed from repository paths and static analysis). Observed top-level classes: ADBConnection, ActionHandler, ActionResult, AgentConfig, ConnectionType, DeviceFactory. Obser… |

## Important files

- `.github/ISSUE_TEMPLATE/bug_report.yaml` (config)
- `.github/ISSUE_TEMPLATE/feature-request.yaml` (config)
- `.pre-commit-config.yaml` (config)
- `requirements.txt` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `phone_agent` — 33 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `resources` — 4 analysed file(s)
- `.github` — 3 analysed file(s)
- `examples` — 2 analysed file(s)
- `scripts` — 2 analysed file(s)
- `docs` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `86f55382982fb054e8fc98ca80609dff8a2cdc3c` is the revision these paths and observations refer to.
