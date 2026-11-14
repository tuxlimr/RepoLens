# Project structure: ActivityWatch/activitywatch

**Analysed commit:** `b1dbd358ef6e284baa33aa075a885716538f1e1a`

**Commit reference:** [b1dbd358ef6e284baa33aa075a885716538f1e1a](https://github.com/ActivityWatch/activitywatch/commit/b1dbd358ef6e284baa33aa075a885716538f1e1a)

**Tree at this commit:** [ActivityWatch/activitywatch@b1dbd358ef6e](https://github.com/ActivityWatch/activitywatch/tree/b1dbd358ef6e284baa33aa075a885716538f1e1a)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | ActivityWatch/activitywatch |
| Description | The best free and open-source automated time tracker. Cross-platform, extensible, privacy-focused. |
| Stars | 19627 |
| Forks | 1078 |
| Licence | MPL-2.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `b1dbd358ef6e284baa33aa075a885716538f1e1a` |
| Retrieved at | 2026-11-14T19:08:10.115148+00:00 |
| Files in this snapshot | 111 |

## Directory tree

```text
.github/  (17 files)
  ISSUE_TEMPLATE/  (3 files)
    bug-report.yml
    config.yml
    everything-else.yml
  workflows/  (11 files)
    changelog-tests.yml
    codeql.yml
    dependabot-automerge.yml
    diagram.yml
    greetings.yml
    packaging-arch-tests.yml
    query-parity.yml
    release.yml
    research-feed-publisher-tests.yml
    test.yml
    winget.yml
  FUNDING.yml
  dependabot.yml
  stale.yml
scripts/  (80 files)
  chores/  (1 files)
    make-release.sh
  ci/  (7 files)
    enable_long_paths.bat
    import-macos-p12.sh
    install_node.ps1
    install_pyhook.ps1
    install_python.ps1
    run_with_env.cmd
    setup_venv_osx.sh
  package/  (22 files)
    deb/  (1 files)
      … 1 files under this directory
    README.txt
    RESEARCH_FEED.md
    UPDATER.md
    abi-gate.sh
    activitywatch-setup.iss
    app-entitlements.plist
    assert-windows-pe-arch.py
    aw-tauri.iss
    build_app_tauri.sh
    collect-setup.sh
    configure_tauri_release.py
    dmgbuild-settings.py
    entitlements.plist
    generate_latest_json.py
    get-arch.sh
    getversion.sh
    host-abi-gate.sh
    package-all.sh
    package-appimage.sh
    package-deb.sh
    publish_research_feed.py
  research_edition/  (2 files)
    export_sanitize.rs
    geography-free-default.toml
  tests/  (27 files)
    query_parity/  (13 files)
      … 13 files under this directory
    integration_tests.py
    test_assert_windows_pe_arch.py
    test_build_changelog.py
    test_check_tauri_server.py
    test_configure_tauri_release.py
    test_emit_research_category_preset.py
    test_generate_latest_json.py
    test_get_arch.py
    test_host_abi_gate.py
    test_patch_research_edition_config.py
    test_patch_research_edition_export.py
    test_patch_research_edition_profile.py
    test_publish_research_feed.py
    test_tauri_bundle_version.py
  build_changelog.py
  bump-submodules.sh
  changelog_contributors.csv
  changelog_contributors_twitter.csv
  check_tauri_server.py
  checkout-latest-tag.sh
  count_lines.sh
  emit_research_category_preset.py
  get_latest_release.sh
  logcrawler.py
  nop.sh
  notarize.sh
  patch_research_edition_awqt.py
  patch_research_edition_config.py
  patch_research_edition_export.py
  patch_research_edition_profile.py
  screenshots.py
  submodule-branch.sh
  symlink-systemd.sh
  uninstall.sh
  update-deps.sh
.gitattributes
.gitignore
.gitmodules
.tool-versions
CITATION.cff
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE.txt
Makefile
README.md
SECURITY.md
aw.spec
gptme.toml
pyproject.toml
```

## Entry points

- [scripts/build_changelog.py:870](https://github.com/ActivityWatch/activitywatch/blob/b1dbd358ef6e284baa33aa075a885716538f1e1a/scripts/build_changelog.py#L870)
- [scripts/check_tauri_server.py:279](https://github.com/ActivityWatch/activitywatch/blob/b1dbd358ef6e284baa33aa075a885716538f1e1a/scripts/check_tauri_server.py#L279)
- [scripts/emit_research_category_preset.py:262](https://github.com/ActivityWatch/activitywatch/blob/b1dbd358ef6e284baa33aa075a885716538f1e1a/scripts/emit_research_category_preset.py#L262)
- [scripts/logcrawler.py:79](https://github.com/ActivityWatch/activitywatch/blob/b1dbd358ef6e284baa33aa075a885716538f1e1a/scripts/logcrawler.py#L79)
- [scripts/package/assert-windows-pe-arch.py:116](https://github.com/ActivityWatch/activitywatch/blob/b1dbd358ef6e284baa33aa075a885716538f1e1a/scripts/package/assert-windows-pe-arch.py#L116)
- [scripts/package/configure_tauri_release.py:107](https://github.com/ActivityWatch/activitywatch/blob/b1dbd358ef6e284baa33aa075a885716538f1e1a/scripts/package/configure_tauri_release.py#L107)
- [scripts/package/generate_latest_json.py:181](https://github.com/ActivityWatch/activitywatch/blob/b1dbd358ef6e284baa33aa075a885716538f1e1a/scripts/package/generate_latest_json.py#L181)
- [scripts/package/publish_research_feed.py:283](https://github.com/ActivityWatch/activitywatch/blob/b1dbd358ef6e284baa33aa075a885716538f1e1a/scripts/package/publish_research_feed.py#L283)
- [scripts/patch_research_edition_awqt.py:51](https://github.com/ActivityWatch/activitywatch/blob/b1dbd358ef6e284baa33aa075a885716538f1e1a/scripts/patch_research_edition_awqt.py#L51)
- [scripts/patch_research_edition_config.py:824](https://github.com/ActivityWatch/activitywatch/blob/b1dbd358ef6e284baa33aa075a885716538f1e1a/scripts/patch_research_edition_config.py#L824)
- [scripts/patch_research_edition_export.py:395](https://github.com/ActivityWatch/activitywatch/blob/b1dbd358ef6e284baa33aa075a885716538f1e1a/scripts/patch_research_edition_export.py#L395)
- [scripts/patch_research_edition_profile.py:736](https://github.com/ActivityWatch/activitywatch/blob/b1dbd358ef6e284baa33aa075a885716538f1e1a/scripts/patch_research_edition_profile.py#L736)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 13 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Activity, Commit, CommitMsg, DayPlan, Device, Page. Observed top-level functions: _catego… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 24 file(s) under scripts package (observed from repository paths and static analysis). Observed top-level functions: icon_from_app. |
| Tests | test | Observed | Groups 27 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: Query, Scenario, Server. Observed top-level functions: _bind_servers, _case_id, _cases, _classify_event, _c… |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/bug-report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/everything-else.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/stale.yml` (config)
- `.github/workflows/changelog-tests.yml` (ci)
- `.github/workflows/codeql.yml` (ci)
- `.github/workflows/dependabot-automerge.yml` (ci)
- `.github/workflows/diagram.yml` (ci)
- `.github/workflows/greetings.yml` (ci)
- `.github/workflows/packaging-arch-tests.yml` (ci)
- `.github/workflows/query-parity.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/research-feed-publisher-tests.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `.github/workflows/winget.yml` (ci)
- `gptme.toml` (config)
- `pyproject.toml` (manifest)
- `scripts/research_edition/geography-free-default.toml` (config)

## Top-level layout

- `scripts` — 80 analysed file(s)
- `.github` — 17 analysed file(s)
- `(root files)` — 14 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `b1dbd358ef6e284baa33aa075a885716538f1e1a` is the revision these paths and observations refer to.
