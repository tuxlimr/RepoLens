# Project structure: AgriciDaniel/claude-seo

**Analysed commit:** `2e40a5fa6220fc846fcc56d666831fd1315bedc7`

**Commit reference:** [2e40a5fa6220fc846fcc56d666831fd1315bedc7](https://github.com/AgriciDaniel/claude-seo/commit/2e40a5fa6220fc846fcc56d666831fd1315bedc7)

**Tree at this commit:** [AgriciDaniel/claude-seo@2e40a5fa6220](https://github.com/AgriciDaniel/claude-seo/tree/2e40a5fa6220fc846fcc56d666831fd1315bedc7)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | AgriciDaniel/claude-seo |
| Description | Universal SEO skill for Claude Code. 26 sub-skills + 19 sub-agents covering technical SEO, E-E-A-T, schema, GEO/AEO, agent readiness (Lighthouse Agentic Browsing, WebMCP, llms.txt), backlinks, local SEO, e-commerce, international SEO, Google APIs, and PDF/Excel reporting. 9 optional extensions for… |
| Stars | 29294 |
| Forks | 3717 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `2e40a5fa6220fc846fcc56d666831fd1315bedc7` |
| Retrieved at | 2026-11-14T19:07:12.457887+00:00 |
| Files in this snapshot | 506 |

## Directory tree

```text
.claude-plugin/  (2 files)
  marketplace.json
  plugin.json
.devcontainer/  (1 files)
  devcontainer.json
.github/  (12 files)
  ISSUE_TEMPLATE/  (4 files)
    bug_report.yml
    config.yml
    feature_request.yml
    task.yml
  workflows/  (3 files)
    ci.yml
    v2.yml
    windows-smoke.yml
  CODEOWNERS
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
  release.yml
agents/  (19 files)
  seo-agentic.md
  seo-backlinks.md
  seo-cluster.md
  seo-content.md
  seo-dataforseo.md
  seo-drift.md
  seo-ecommerce.md
  seo-flow.md
  seo-geo.md
  seo-google.md
  seo-image-gen.md
  seo-local.md
  seo-maps.md
  seo-performance.md
  seo-schema.md
  seo-sitemap.md
  seo-sxo.md
  seo-technical.md
  seo-visual.md
assets/  (11 files)
  readme/  (7 files)
    v3/  (3 files)
      … 3 files under this directory
    btn-hub.svg
    btn-pro.svg
    btn-youtube.svg
    screen.svg
  cover.svg
  framework.svg
  signal-flow.svg
  sub-skills.svg
data/  (1 files)
  google-updates.json
docs/  (9 files)
  ARCHITECTURE.md
  COMMANDS.md
  COMMUNITY-INTEGRATIONS.md
  FINAL-VERIFICATION-v2.2.5-2026-08-26.md
  INSTALLATION.md
  MCP-INTEGRATION.md
  MIGRATION-v1-to-v2.md
  TROUBLESHOOTING.md
  WORKFLOW-public-private.md
extensions/  (74 files)
  ahrefs/  (5 files)
    docs/  (1 files)
      … 1 files under this directory
    skills/  (1 files)
      … 1 files under this directory
    install.ps1
    install.sh
    uninstall.sh
  banana/  (23 files)
    agents/  (1 files)
      … 1 files under this directory
    docs/  (1 files)
      … 1 files under this directory
    references/  (9 files)
      … 9 files under this directory
    scripts/  (7 files)
      … 7 files under this directory
    skills/  (2 files)
      … 2 files under this directory
    README.md
    install.sh
    uninstall.sh
  bing-webmaster/  (5 files)
    docs/  (1 files)
      … 1 files under this directory
    skills/  (1 files)
      … 1 files under this directory
    install.ps1
    install.sh
    uninstall.sh
  dataforseo/  (12 files)
    agents/  (1 files)
      … 1 files under this directory
    docs/  (1 files)
      … 1 files under this directory
    skills/  (4 files)
      … 4 files under this directory
    README.md
    field-config.json
    install.ps1
    install.sh
    uninstall.ps1
    uninstall.sh
  firecrawl/  (8 files)
    docs/  (1 files)
      … 1 files under this directory
    skills/  (2 files)
      … 2 files under this directory
    README.md
    install.ps1
    install.sh
    uninstall.ps1
    uninstall.sh
  matomo/  (6 files)
    agents/  (1 files)
      … 1 files under this directory
    docs/  (1 files)
      … 1 files under this directory
    skills/  (1 files)
      … 1 files under this directory
    install.ps1
    install.sh
    uninstall.sh
  profound/  (5 files)
    docs/  (1 files)
      … 1 files under this directory
    skills/  (1 files)
      … 1 files under this directory
    install.ps1
    install.sh
    uninstall.sh
  seranking/  (5 files)
    docs/  (1 files)
      … 1 files under this directory
    skills/  (1 files)
      … 1 files under this directory
    install.ps1
    install.sh
    uninstall.sh
  unlighthouse/  (5 files)
    docs/  (1 files)
      … 1 files under this directory
    skills/  (1 files)
      … 1 files under this directory
    install.ps1
    install.sh
    uninstall.sh
hooks/  (3 files)
  hooks.json
  run-python-hook.js
  validate-schema.py
schema/  (1 files)
  templates.json
scripts/  (66 files)
  agent_ux_check.py
  agentic_check.py
  agentic_fix.py
  analyze_visual.py
  backlinks_auth.py
  bing_webmaster.py
  browser_proxy.py
  capture_screenshot.py
  claude-seo
  commoncrawl_graph.py
  consistency_check.py
  content_humanize.py
  content_quality.py
  content_verify.py
  crux_history.py
  dataforseo_costs.py
  dataforseo_merchant.py
  dataforseo_normalize.py
  domain_history.py
  drift_baseline.py
  drift_compare.py
  drift_history.py
  drift_report.py
  fetch_page.py
  … 42 more files
skills/  (169 files)
  seo/  (19 files)
    references/  (17 files)
      … 17 files under this directory
    LICENSE.txt
    SKILL.md
  seo-agentic/  (8 files)
    references/  (6 files)
      … 6 files under this directory
    LICENSE.txt
    SKILL.md
  seo-audit/  (2 files)
    LICENSE.txt
    SKILL.md
  seo-backlinks/  (2 files)
    LICENSE.txt
    SKILL.md
  seo-cluster/  (5 files)
    references/  (3 files)
      … 3 files under this directory
    templates/  (1 files)
      … 1 files under this directory
    SKILL.md
  seo-competitor-pages/  (2 files)
    LICENSE.txt
    SKILL.md
  seo-content/  (2 files)
    LICENSE.txt
    SKILL.md
  seo-content-brief/  (5 files)
    references/  (3 files)
      … 3 files under this directory
    LICENSE.txt
    SKILL.md
  seo-dataforseo/  (4 files)
    references/  (2 files)
      … 2 files under this directory
    LICENSE.txt
    SKILL.md
  seo-drift/  (2 files)
    references/  (1 files)
      … 1 files under this directory
    SKILL.md
  seo-ecommerce/  (3 files)
    references/  (2 files)
      … 2 files under this directory
    SKILL.md
  seo-flow/  (46 files)
    references/  (45 files)
      … 45 files under this directory
    SKILL.md
  seo-geo/  (4 files)
    references/  (2 files)
      … 2 files under this directory
    LICENSE.txt
    SKILL.md
  seo-google/  (17 files)
    assets/  (3 files)
      … 3 files under this directory
    references/  (12 files)
      … 12 files under this directory
    LICENSE.txt
    SKILL.md
  seo-hreflang/  (6 files)
    references/  (4 files)
      … 4 files under this directory
    LICENSE.txt
    SKILL.md
  seo-image-gen/  (11 files)
    references/  (9 files)
      … 9 files under this directory
    LICENSE.txt
    SKILL.md
  seo-images/  (2 files)
    LICENSE.txt
    SKILL.md
  seo-local/  (2 files)
    LICENSE.txt
    SKILL.md
  seo-maps/  (2 files)
    LICENSE.txt
    SKILL.md
  seo-page/  (2 files)
    LICENSE.txt
    SKILL.md
  seo-plan/  (8 files)
    assets/  (6 files)
      … 6 files under this directory
    LICENSE.txt
    SKILL.md
  seo-programmatic/  (2 files)
    LICENSE.txt
    SKILL.md
  seo-schema/  (3 files)
    references/  (1 files)
      … 1 files under this directory
    LICENSE.txt
    SKILL.md
  seo-sitemap/  (2 files)
    LICENSE.txt
    SKILL.md
  seo-sxo/  (5 files)
    references/  (4 files)
      … 4 files under this directory
    SKILL.md
  seo-technical/  (3 files)
    references/  (1 files)
      … 1 files under this directory
    LICENSE.txt
    SKILL.md
tests/  (120 files)
  fixtures/  (2 files)
    dataforseo_mcp_2_8_10_tools.txt
    lighthouse_agentic_13_5_psi.json
  test_agent_mcp_permissions.py
  test_agent_untrusted_content.py
  test_agentic.py
  test_ai_crawler_claims.py
  test_audit_agent_turn_budget.py
  test_audit_instructions.py
  test_backlink_score_gate.py
  test_backlinks_auth_hardening.py
  test_banana_api_key_safety.py
  test_banana_cost_tracker.py
  test_banana_install_layout.py
  test_banana_key_masking.py
  test_banana_setup_mcp_atomic_write.py
  test_bing_webmaster.py
  test_browser_proxy.py
  test_canonical_facts.py
  test_capture_screenshot_hygiene.py
  test_capture_screenshot_paths.py
  test_cluster_map_escaping.py
  test_commoncrawl_graph.py
  test_consistency_check.py
  test_content_humanize.py
  test_content_quality.py
  test_contributors.py
  … 94 more files
.gitignore
AGENTS.md
CHANGELOG.md
CITATION.cff
CLAUDE.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
CONTRIBUTORS.md
LICENSE
PRIVACY.md
README.md
SECURITY.md
install.ps1
install.sh
pyproject.toml
requirements.txt
uninstall.ps1
uninstall.sh
```

## Entry points

- [extensions/banana/scripts/batch.py:97](https://github.com/AgriciDaniel/claude-seo/blob/2e40a5fa6220fc846fcc56d666831fd1315bedc7/extensions/banana/scripts/batch.py#L97)
- [extensions/banana/scripts/cost_tracker.py:338](https://github.com/AgriciDaniel/claude-seo/blob/2e40a5fa6220fc846fcc56d666831fd1315bedc7/extensions/banana/scripts/cost_tracker.py#L338)
- [extensions/banana/scripts/edit.py:169](https://github.com/AgriciDaniel/claude-seo/blob/2e40a5fa6220fc846fcc56d666831fd1315bedc7/extensions/banana/scripts/edit.py#L169)
- [extensions/banana/scripts/generate.py:177](https://github.com/AgriciDaniel/claude-seo/blob/2e40a5fa6220fc846fcc56d666831fd1315bedc7/extensions/banana/scripts/generate.py#L177)
- [extensions/banana/scripts/presets.py:152](https://github.com/AgriciDaniel/claude-seo/blob/2e40a5fa6220fc846fcc56d666831fd1315bedc7/extensions/banana/scripts/presets.py#L152)
- [extensions/banana/scripts/setup_mcp.py:167](https://github.com/AgriciDaniel/claude-seo/blob/2e40a5fa6220fc846fcc56d666831fd1315bedc7/extensions/banana/scripts/setup_mcp.py#L167)
- [extensions/banana/scripts/validate_setup.py:140](https://github.com/AgriciDaniel/claude-seo/blob/2e40a5fa6220fc846fcc56d666831fd1315bedc7/extensions/banana/scripts/validate_setup.py#L140)
- [hooks/validate-schema.py:370](https://github.com/AgriciDaniel/claude-seo/blob/2e40a5fa6220fc846fcc56d666831fd1315bedc7/hooks/validate-schema.py#L370)
- [scripts/agent_ux_check.py:299](https://github.com/AgriciDaniel/claude-seo/blob/2e40a5fa6220fc846fcc56d666831fd1315bedc7/scripts/agent_ux_check.py#L299)
- [scripts/agentic_check.py:1333](https://github.com/AgriciDaniel/claude-seo/blob/2e40a5fa6220fc846fcc56d666831fd1315bedc7/scripts/agentic_check.py#L1333)
- [scripts/agentic_fix.py:391](https://github.com/AgriciDaniel/claude-seo/blob/2e40a5fa6220fc846fcc56d666831fd1315bedc7/scripts/agentic_fix.py#L391)
- [scripts/analyze_visual.py:250](https://github.com/AgriciDaniel/claude-seo/blob/2e40a5fa6220fc846fcc56d666831fd1315bedc7/scripts/analyze_visual.py#L250)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 70 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: LedgerError, MatomoRequestRefused, ProxiedRequestRefused, SetupLock, URLSafetyError, _Bud… |
| extensions package | library | Observed | Groups 18 file(s) under extensions package (observed from repository paths and static analysis). |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 1 file(s) under hooks package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 3 file(s) under scripts package (observed from repository paths and static analysis). Observed top-level classes: ChromiumSandboxError, PageNotLoadedError, _GuardServer, _OriginReader, _ProxyHandler, _Rejected. O… |
| Tests | test | Observed | Groups 120 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: FakeExecute, FakeHeadResponse, FakeManager, FakePage, FakeRaw, FakeRawHeaders. Observed top-level function… |

## Important files

- `.claude-plugin/marketplace.json` (config)
- `.claude-plugin/plugin.json` (config)
- `.devcontainer/devcontainer.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/ISSUE_TEMPLATE/task.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/release.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/v2.yml` (ci)
- `.github/workflows/windows-smoke.yml` (ci)
- `data/google-updates.json` (config)
- `extensions/dataforseo/field-config.json` (config)
- `hooks/hooks.json` (config)
- `pyproject.toml` (manifest)
- `requirements.txt` (manifest)
- `schema/templates.json` (config)

## Top-level layout

- `skills` — 169 analysed file(s)
- `tests` — 120 analysed file(s)
- `extensions` — 74 analysed file(s)
- `scripts` — 66 analysed file(s)
- `agents` — 19 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `.github` — 12 analysed file(s)
- `assets` — 11 analysed file(s)
- `docs` — 9 analysed file(s)
- `hooks` — 3 analysed file(s)
- `.claude-plugin` — 2 analysed file(s)
- `.devcontainer` — 1 analysed file(s)
- `data` — 1 analysed file(s)
- `schema` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `2e40a5fa6220fc846fcc56d666831fd1315bedc7` is the revision these paths and observations refer to.
