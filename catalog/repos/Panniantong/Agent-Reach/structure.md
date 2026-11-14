# Project structure: Panniantong/Agent-Reach

**Analysed commit:** `c70ae6da5d39bc90e09ad2ae0575ccc89f31e284`

**Commit reference:** [c70ae6da5d39bc90e09ad2ae0575ccc89f31e284](https://github.com/Panniantong/Agent-Reach/commit/c70ae6da5d39bc90e09ad2ae0575ccc89f31e284)

**Tree at this commit:** [Panniantong/Agent-Reach@c70ae6da5d39](https://github.com/Panniantong/Agent-Reach/tree/c70ae6da5d39bc90e09ad2ae0575ccc89f31e284)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Panniantong/Agent-Reach |
| Description | Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees. |
| Stars | 111765 |
| Forks | 10022 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `c70ae6da5d39bc90e09ad2ae0575ccc89f31e284` |
| Retrieved at | 2026-11-14T19:06:06.901229+00:00 |
| Files in this snapshot | 117 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (2 files)
    pytest.yml
    release.yml
  release-acceptance.json
agent_reach/  (55 files)
  backends/  (4 files)
    __init__.py
    boss_native.py
    cloak.py
    opencli.py
  channels/  (17 files)
    __init__.py
    _opencli_site.py
    base.py
    bilibili.py
    boss.py
    facebook.py
    github.py
    instagram.py
    linkedin.py
    reddit.py
    twitter.py
    v2ex.py
    web.py
    xiaohongshu.py
    xiaoyuzhou.py
    xueqiu.py
    youtube.py
  runtime/  (20 files)
    __init__.py
    bridge.py
    browser.py
    browser_binding.py
    browser_watcher.py
    cdp.py
    cli.py
    clock.py
    dispatch.py
    legacy.py
    manage.py
    onboarding.py
    public_web.py
    result.py
    run.py
    session_reuse.py
    sessions.py
    state.py
    tools.py
    update_notice.py
  scripts/  (1 files)
    transcribe_xiaoyuzhou.sh
  skill/  (5 files)
    references/  (3 files)
      … 3 files under this directory
    SKILL.md
    SKILL_en.md
  utils/  (4 files)
    paths.py
    process.py
    text.py
    url.py
  __init__.py
  cli.py
  config.py
  transcribe.py
docs/  (11 files)
  assets/  (4 files)
    sponsors/  (1 files)
      … 1 files under this directory
    logo-1.svg
    logo-2.svg
    logo-3.svg
  plans/  (2 files)
    2026-10-20-release-policy-guards.md
    2026-10-20-shared-cloak-browser.md
  README_en.md
  cloakbrowser.md
  install.md
  troubleshooting.md
  update.md
scripts/  (3 files)
  accept-search.py
  check_release_acceptance.py
  record_release_acceptance.py
tests/  (35 files)
  conftest.py
  test_auth_guidance_policy.py
  test_bilibili_login.py
  test_boss_channel.py
  test_browser.py
  test_browser_slots.py
  test_channel_contracts.py
  test_channels.py
  test_cli_encoding.py
  test_config.py
  test_config_shape.py
  test_dispatch_public_fallback.py
  test_integration_script.py
  test_manage.py
  test_native_access_errors.py
  test_private_file_writes.py
  test_process.py
  test_public_first.py
  test_reddit_channel.py
  test_release_policy.py
  test_run_windows.py
  test_scrub_credentials.py
  test_search_harness.py
  test_session_onboarding.py
  … 11 more files
.gitignore
CHANGELOG.md
CONTRIBUTING.md
LICENSE
README.md
SECURITY.md
constraints.txt
llms.txt
pyproject.toml
test.sh
```

## Entry points

- [agent_reach/backends/boss_native.py:74](https://github.com/Panniantong/Agent-Reach/blob/c70ae6da5d39bc90e09ad2ae0575ccc89f31e284/agent_reach/backends/boss_native.py#L74)
- [agent_reach/backends/cloak.py:36](https://github.com/Panniantong/Agent-Reach/blob/c70ae6da5d39bc90e09ad2ae0575ccc89f31e284/agent_reach/backends/cloak.py#L36)
- [agent_reach/cli.py](https://github.com/Panniantong/Agent-Reach/blob/c70ae6da5d39bc90e09ad2ae0575ccc89f31e284/agent_reach/cli.py)
- [agent_reach/runtime/browser_watcher.py:193](https://github.com/Panniantong/Agent-Reach/blob/c70ae6da5d39bc90e09ad2ae0575ccc89f31e284/agent_reach/runtime/browser_watcher.py#L193)
- [scripts/check_release_acceptance.py:89](https://github.com/Panniantong/Agent-Reach/blob/c70ae6da5d39bc90e09ad2ae0575ccc89f31e284/scripts/check_release_acceptance.py#L89)
- [scripts/record_release_acceptance.py:138](https://github.com/Panniantong/Agent-Reach/blob/c70ae6da5d39bc90e09ad2ae0575ccc89f31e284/scripts/record_release_acceptance.py#L138)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| agent_reach package | library | Observed | Groups 42 file(s) under agent_reach package (observed from repository paths and static analysis). Observed top-level classes: Action, BilibiliChannel, BossChannel, Channel, Clock, FacebookChannel. Observed top-level fun… |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: Config, ConfigError, ConfigReadOnlyError, ConfigSecurityError. Observed top-level fun… |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 9 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: CommandFailed, _ArgError, _Parser. Observed top-level functions: _agent_for, _apply_saved_… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 35 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: Bili, Bili2, Broken, FakeChannel, FakeResponse, Linky. Observed top-level functions: _actions, _added_reddi… |

## Important files

- `.github/release-acceptance.json` (config)
- `.github/workflows/pytest.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `pyproject.toml` (manifest)

## Top-level layout

- `agent_reach` — 55 analysed file(s)
- `tests` — 35 analysed file(s)
- `docs` — 11 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `.github` — 3 analysed file(s)
- `scripts` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `c70ae6da5d39bc90e09ad2ae0575ccc89f31e284` is the revision these paths and observations refer to.
