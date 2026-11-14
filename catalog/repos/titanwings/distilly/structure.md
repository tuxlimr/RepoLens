# Project structure: titanwings/distilly

**Analysed commit:** `0afc45c29c360ba7bc8260f1bb0bf34e9155f4fa`

**Commit reference:** [0afc45c29c360ba7bc8260f1bb0bf34e9155f4fa](https://github.com/titanwings/distilly/commit/0afc45c29c360ba7bc8260f1bb0bf34e9155f4fa)

**Tree at this commit:** [titanwings/distilly@0afc45c29c36](https://github.com/titanwings/distilly/tree/0afc45c29c360ba7bc8260f1bb0bf34e9155f4fa)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | titanwings/distilly |
| Description | Distilly — Distill how they think into reusable Skills for any Agent or Bot. Formerly Colleague Skill（原同事 Skill）. |
| Stars | 26575 |
| Forks | 2266 |
| Licence | MIT |
| Language | Python |
| Default branch | dot-skill |
| Analysed commit | `0afc45c29c360ba7bc8260f1bb0bf34e9155f4fa` |
| Retrieved at | 2026-11-14T19:07:21.977098+00:00 |
| Files in this snapshot | 122 |

## Directory tree

```text
.github/  (7 files)
  ISSUE_TEMPLATE/  (4 files)
    bug_report.md
    config.yml
    feature_request.md
    question.md
  workflows/  (2 files)
    ci.yml
    publish-package.yml
  PULL_REQUEST_TEMPLATE.md
bin/  (1 files)
  distilly.mjs
docs/  (23 files)
  assets/  (16 files)
    hosts/  (13 files)
      … 13 files under this directory
    sources/  (3 files)
      … 3 files under this directory
  lang/  (7 files)
    README_DE.md
    README_ES.md
    README_JA.md
    README_KO.md
    README_PT.md
    README_RU.md
    README_ZH.md
prompts/  (31 files)
  celebrity/  (12 files)
    budget_unfriendly/  (7 files)
      … 7 files under this directory
    intake.md
    merger.md
    persona_analyzer.md
    persona_builder.md
    research.md
  colleague/  (4 files)
    intake.md
    merger.md
    persona_analyzer.md
    persona_builder.md
  flows/  (6 files)
    celebrity_research.md
    create.md
    evolve.md
    manage.md
    owner.md
    sources.md
  owner/  (2 files)
    intake.md
    profile_builder.md
  relationship/  (4 files)
    intake.md
    merger.md
    persona_analyzer.md
    persona_builder.md
  shared/  (3 files)
    correction_handler.md
    work_analyzer.md
    work_builder.md
tests/  (20 files)
  e2e/  (5 files)
    owner_discovery/  (5 files)
      … 5 files under this directory
  _paths.py
  test_cli_lifecycle.py
  test_config_migration.py
  test_credentials.py
  test_install_claude_generated_skill.py
  test_install_distilly.py
  test_install_generated_skill.py
  test_install_openclaw_and_codex.py
  test_owner_profile.py
  test_owner_sources.py
  test_research_tools.py
  test_skill_entrypoint_docs.py
  test_skill_writer.py
  test_translation_sync.py
  test_xquik_public_posts.py
tools/  (27 files)
  research/  (7 files)
    __init__.py
    download_subtitles.sh
    merge_research.py
    quality_check.py
    srt_to_transcript.py
    transcribe_audio.py
    xquik_public_posts.py
  credentials.py
  dingtalk_auto_collector.py
  email_parser.py
  feishu_auto_collector.py
  feishu_browser.py
  feishu_mcp_client.py
  feishu_parser.py
  hosts.json
  hosts.py
  install_claude_generated_skill.py
  install_distilly.py
  install_generated_skill.py
  install_generated_skill_common.py
  owner_profile.py
  owner_sources.py
  skill_presets.py
  skill_schema.py
  skill_writer.py
  slack_auto_collector.py
  version_manager.py
.gitignore
CITATION.cff
CONTRIBUTING.md
INSTALL.md
INSTALL_EN.md
LICENSE
README.md
ROADMAP.md
SKILL.md
package.json
requirements-optional.txt
requirements.txt
ruff.toml
```

## Entry points

- [tools/dingtalk_auto_collector.py:805](https://github.com/titanwings/distilly/blob/0afc45c29c360ba7bc8260f1bb0bf34e9155f4fa/tools/dingtalk_auto_collector.py#L805)
- [tools/email_parser.py:338](https://github.com/titanwings/distilly/blob/0afc45c29c360ba7bc8260f1bb0bf34e9155f4fa/tools/email_parser.py#L338)
- [tools/feishu_auto_collector.py:1060](https://github.com/titanwings/distilly/blob/0afc45c29c360ba7bc8260f1bb0bf34e9155f4fa/tools/feishu_auto_collector.py#L1060)
- [tools/feishu_browser.py:372](https://github.com/titanwings/distilly/blob/0afc45c29c360ba7bc8260f1bb0bf34e9155f4fa/tools/feishu_browser.py#L372)
- [tools/feishu_mcp_client.py:329](https://github.com/titanwings/distilly/blob/0afc45c29c360ba7bc8260f1bb0bf34e9155f4fa/tools/feishu_mcp_client.py#L329)
- [tools/feishu_parser.py:249](https://github.com/titanwings/distilly/blob/0afc45c29c360ba7bc8260f1bb0bf34e9155f4fa/tools/feishu_parser.py#L249)
- [tools/install_claude_generated_skill.py:108](https://github.com/titanwings/distilly/blob/0afc45c29c360ba7bc8260f1bb0bf34e9155f4fa/tools/install_claude_generated_skill.py#L108)
- [tools/install_distilly.py:92](https://github.com/titanwings/distilly/blob/0afc45c29c360ba7bc8260f1bb0bf34e9155f4fa/tools/install_distilly.py#L92)
- [tools/install_generated_skill.py:46](https://github.com/titanwings/distilly/blob/0afc45c29c360ba7bc8260f1bb0bf34e9155f4fa/tools/install_generated_skill.py#L46)
- [tools/owner_profile.py:296](https://github.com/titanwings/distilly/blob/0afc45c29c360ba7bc8260f1bb0bf34e9155f4fa/tools/owner_profile.py#L296)
- [tools/owner_sources.py:318](https://github.com/titanwings/distilly/blob/0afc45c29c360ba7bc8260f1bb0bf34e9155f4fa/tools/owner_sources.py#L318)
- [tools/research/merge_research.py:276](https://github.com/titanwings/distilly/blob/0afc45c29c360ba7bc8260f1bb0bf34e9155f4fa/tools/research/merge_research.py#L276)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bin package | library | Observed | Groups 1 file(s) under bin package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 19 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: CollectorError, HTMLTextExtractor, RateLimitedClient, SlackAuthError, SlackCollectorError… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 20 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: ClassifyTest, ClaudeGeneratedSkillInstallTest, CliLifecycleTest, CollectionTest, ConfigMigrationTest, Crede… |
| tools package | library | Observed | Groups 7 file(s) under tools package (observed from repository paths and static analysis). Observed top-level functions: _keyring, _keyring_get, _keyring_set, _lookup, _resolve, ask. |

## Important files

- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/publish-package.yml` (ci)
- `package.json` (manifest)
- `requirements-optional.txt` (manifest)
- `requirements.txt` (manifest)
- `ruff.toml` (config)
- `tools/hosts.json` (config)

## Top-level layout

- `prompts` — 31 analysed file(s)
- `tools` — 27 analysed file(s)
- `docs` — 23 analysed file(s)
- `tests` — 20 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `.github` — 7 analysed file(s)
- `bin` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `0afc45c29c360ba7bc8260f1bb0bf34e9155f4fa` is the revision these paths and observations refer to.
