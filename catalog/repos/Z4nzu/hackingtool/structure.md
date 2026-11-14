# Project structure: Z4nzu/hackingtool

**Analysed commit:** `c3a858990f1f772e5c59f10c51f1a7aeb888ef23`

**Commit reference:** [c3a858990f1f772e5c59f10c51f1a7aeb888ef23](https://github.com/Z4nzu/hackingtool/commit/c3a858990f1f772e5c59f10c51f1a7aeb888ef23)

**Tree at this commit:** [Z4nzu/hackingtool@c3a858990f1f](https://github.com/Z4nzu/hackingtool/tree/c3a858990f1f772e5c59f10c51f1a7aeb888ef23)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Z4nzu/hackingtool |
| Description | ALL IN ONE Hacking Tool For Hackers |
| Stars | 81911 |
| Forks | 9241 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `c3a858990f1f772e5c59f10c51f1a7aeb888ef23` |
| Retrieved at | 2026-11-14T19:06:09.382278+00:00 |
| Files in this snapshot | 174 |

## Directory tree

```text
.githooks/  (1 files)
  pre-push
.github/  (8 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    feature_request.md
    tool_request.md
  workflows/  (2 files)
    checks.yml
    release.yml
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
docs/  (2 files)
  HOW-TO-USE.md
  TOOLS.md
images/  (1 files)
  logo.svg
scripts/  (5 files)
  apply_archive.py
  audit_tools.py
  check.sh
  discover_tools.py
  gen_catalog_owners.py
src/  (106 files)
  hackingtool/  (106 files)
    catalog/  (22 files)
      … 22 files under this directory
    pipelines/  (1 files)
      … 1 files under this directory
    skill/  (2 files)
      … 2 files under this directory
    tools/  (33 files)
      … 33 files under this directory
    tui/  (19 files)
      … 19 files under this directory
    __init__.py
    __main__.py
    ai_command.py
    ai_goal.py
    ai_recommend.py
    ai_report.py
    ai_summary.py
    catalog_owners.py
    cli.py
    config.py
    config_ui.py
    constants.py
    core.py
    discover.py
    engagement.py
    findings.py
    orchestrator.py
    os_detect.py
    prompt.py
    registry.py
    repl.py
    report.py
    session.py
    skill.py
    … 5 more files
tests/  (38 files)
  test_ai_command.py
  test_ai_goal.py
  test_ai_recommend.py
  test_ai_report.py
  test_ai_summary.py
  test_cli.py
  test_config.py
  test_core.py
  test_discover.py
  test_engagement.py
  test_findings.py
  test_logo_version.py
  test_main_module.py
  test_orchestrator.py
  test_pr_fixes.py
  test_prompt.py
  test_registry.py
  test_repl.py
  test_report.py
  test_session.py
  test_skill.py
  test_sponsors.py
  test_tui_app.py
  test_tui_banner.py
  … 14 more files
.dockerignore
.gitignore
CODE_OF_CONDUCT.md
CONTRIBUTING.md
Dockerfile
LICENSE
Makefile
README.md
SECURITY.md
conftest.py
context7.json
docker-compose.yml
pyproject.toml
```

## Entry points

- [src/hackingtool/__main__.py:3](https://github.com/Z4nzu/hackingtool/blob/c3a858990f1f772e5c59f10c51f1a7aeb888ef23/src/hackingtool/__main__.py#L3)
- [src/hackingtool/ai_command.py:110](https://github.com/Z4nzu/hackingtool/blob/c3a858990f1f772e5c59f10c51f1a7aeb888ef23/src/hackingtool/ai_command.py#L110)
- [src/hackingtool/ai_goal.py:278](https://github.com/Z4nzu/hackingtool/blob/c3a858990f1f772e5c59f10c51f1a7aeb888ef23/src/hackingtool/ai_goal.py#L278)
- [src/hackingtool/ai_recommend.py:212](https://github.com/Z4nzu/hackingtool/blob/c3a858990f1f772e5c59f10c51f1a7aeb888ef23/src/hackingtool/ai_recommend.py#L212)
- [src/hackingtool/ai_report.py:152](https://github.com/Z4nzu/hackingtool/blob/c3a858990f1f772e5c59f10c51f1a7aeb888ef23/src/hackingtool/ai_report.py#L152)
- [src/hackingtool/ai_summary.py:58](https://github.com/Z4nzu/hackingtool/blob/c3a858990f1f772e5c59f10c51f1a7aeb888ef23/src/hackingtool/ai_summary.py#L58)
- [src/hackingtool/cli.py](https://github.com/Z4nzu/hackingtool/blob/c3a858990f1f772e5c59f10c51f1a7aeb888ef23/src/hackingtool/cli.py)
- [src/hackingtool/config_ui.py:267](https://github.com/Z4nzu/hackingtool/blob/c3a858990f1f772e5c59f10c51f1a7aeb888ef23/src/hackingtool/config_ui.py#L267)
- [src/hackingtool/prompt.py:411](https://github.com/Z4nzu/hackingtool/blob/c3a858990f1f772e5c59f10c51f1a7aeb888ef23/src/hackingtool/prompt.py#L411)
- [src/hackingtool/registry.py:225](https://github.com/Z4nzu/hackingtool/blob/c3a858990f1f772e5c59f10c51f1a7aeb888ef23/src/hackingtool/registry.py#L225)
- [src/hackingtool/skill.py:155](https://github.com/Z4nzu/hackingtool/blob/c3a858990f1f772e5c59f10c51f1a7aeb888ef23/src/hackingtool/skill.py#L155)
- [src/hackingtool/tags.py:66](https://github.com/Z4nzu/hackingtool/blob/c3a858990f1f772e5c59f10c51f1a7aeb888ef23/src/hackingtool/tags.py#L66)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 30 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: ConfigScreen. Observed top-level functions: _load_env, _resolve_key, ai_base_url, ai… |
| Application entry point | entrypoint | Observed | Groups 45 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: AdvPhishing, Airgeddon, AllTools, Amass, AndroGuard, AndroidAttackTools. Observed top-lev… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| hackingtool package | library | Observed | Groups 36 file(s) under hackingtool package (observed from repository paths and static analysis). Observed top-level classes: ActiveDirectoryTools, BloodHound, CatRow, CategoryScreen, Certipy, CloudSecurityTools. Observ… |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 39 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: _App, _Doc, _Fake, _FakeResp, _FakeTool, _Host. Observed top-level functions: _ansi, _assert_header, _cat_w… |

## Important files

- `.dockerignore` (container)
- `.github/FUNDING.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/checks.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `Dockerfile` (container)
- `context7.json` (config)
- `docker-compose.yml` (container)
- `pyproject.toml` (manifest)
- `src/hackingtool/catalog/active_directory.yaml` (config)
- `src/hackingtool/catalog/anonsurf.yaml` (config)
- `src/hackingtool/catalog/cloud_security.yaml` (config)
- `src/hackingtool/catalog/ddos.yaml` (config)
- `src/hackingtool/catalog/exploit_frameworks.yaml` (config)
- `src/hackingtool/catalog/forensics.yaml` (config)
- `src/hackingtool/catalog/hash_cracking.yaml` (config)
- `src/hackingtool/catalog/information_gathering.yaml` (config)
- `src/hackingtool/catalog/legacy_overlays.yaml` (config)
- `src/hackingtool/catalog/mobile_security.yaml` (config)
- `src/hackingtool/catalog/other_tools.yaml` (config)
- `src/hackingtool/catalog/payload_creator.yaml` (config)
- `src/hackingtool/catalog/phishing_attack.yaml` (config)
- `src/hackingtool/catalog/post_exploitation.yaml` (config)
- `src/hackingtool/catalog/remote_administration.yaml` (config)
- `src/hackingtool/catalog/reverse_engineering.yaml` (config)
- `src/hackingtool/catalog/sql_injection.yaml` (config)
- `src/hackingtool/catalog/steganography.yaml` (config)
- `src/hackingtool/catalog/web_attack.yaml` (config)
- `src/hackingtool/catalog/wireless_attack.yaml` (config)
- `src/hackingtool/catalog/wordlist_generator.yaml` (config)
- `src/hackingtool/catalog/xss_attack.yaml` (config)
- `src/hackingtool/pipelines/recon.yaml` (config)
- `src/hackingtool/sponsors.yaml` (config)

## Top-level layout

- `src` — 106 analysed file(s)
- `tests` — 38 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `.github` — 8 analysed file(s)
- `scripts` — 5 analysed file(s)
- `docs` — 2 analysed file(s)
- `.githooks` — 1 analysed file(s)
- `images` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `c3a858990f1f772e5c59f10c51f1a7aeb888ef23` is the revision these paths and observations refer to.
