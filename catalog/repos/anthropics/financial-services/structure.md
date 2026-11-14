# Project structure: anthropics/financial-services

**Analysed commit:** `3e32c2287dcb637c184c01cc0ad82d6af7e9bb0f`

**Commit reference:** [3e32c2287dcb637c184c01cc0ad82d6af7e9bb0f](https://github.com/anthropics/financial-services/commit/3e32c2287dcb637c184c01cc0ad82d6af7e9bb0f)

**Tree at this commit:** [anthropics/financial-services@3e32c2287dcb](https://github.com/anthropics/financial-services/tree/3e32c2287dcb637c184c01cc0ad82d6af7e9bb0f)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | anthropics/financial-services |
| Description | Not provided |
| Stars | 41287 |
| Forks | 5753 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `3e32c2287dcb637c184c01cc0ad82d6af7e9bb0f` |
| Retrieved at | 2026-11-14T19:06:40.822197+00:00 |
| Files in this snapshot | 362 |

## Directory tree

```text
.claude-plugin/  (1 files)
  marketplace.json
.githooks/  (1 files)
  pre-commit
.github/  (2 files)
  workflows/  (2 files)
    plugin-validate.yml
    version-bump.yml
claude-for-msft-365-install/  (25 files)
  .claude/  (1 files)
    skills/  (1 files)
      … 1 files under this directory
  .claude-plugin/  (1 files)
    plugin.json
  commands/  (9 files)
    access-policies.md
    bootstrap.md
    consent.md
    debug.md
    entra-app.md
    export-data.md
    manifest.md
    setup.md
    update-user-attrs.md
  examples/  (6 files)
    python-bootstrap/  (6 files)
      … 6 files under this directory
  scripts/  (7 files)
    build-manifest.mjs
    clear-addin-cache.ps1
    clear-addin-cache.sh
    export-addin-data.ps1
    export-addin-data.sh
    sideload-addin.ps1
    sideload-addin.sh
  README.md
managed-agent-cookbooks/  (61 files)
  earnings-reviewer/  (6 files)
    subagents/  (3 files)
      … 3 files under this directory
    README.md
    agent.yaml
    steering-examples.json
  gl-reconciler/  (6 files)
    subagents/  (3 files)
      … 3 files under this directory
    README.md
    agent.yaml
    steering-examples.json
  kyc-screener/  (6 files)
    subagents/  (3 files)
      … 3 files under this directory
    README.md
    agent.yaml
    steering-examples.json
  market-researcher/  (6 files)
    subagents/  (3 files)
      … 3 files under this directory
    README.md
    agent.yaml
    steering-examples.json
  meeting-prep-agent/  (6 files)
    subagents/  (3 files)
      … 3 files under this directory
    README.md
    agent.yaml
    steering-examples.json
  model-builder/  (6 files)
    subagents/  (3 files)
      … 3 files under this directory
    README.md
    agent.yaml
    steering-examples.json
  month-end-closer/  (6 files)
    subagents/  (3 files)
      … 3 files under this directory
    README.md
    agent.yaml
    steering-examples.json
  pitch-agent/  (6 files)
    subagents/  (3 files)
      … 3 files under this directory
    README.md
    agent.yaml
    steering-examples.json
  statement-auditor/  (6 files)
    subagents/  (3 files)
      … 3 files under this directory
    README.md
    agent.yaml
    steering-examples.json
  valuation-reviewer/  (6 files)
    subagents/  (3 files)
      … 3 files under this directory
    README.md
    agent.yaml
    steering-examples.json
  README.md
plugins/  (261 files)
  agent-plugins/  (95 files)
    earnings-reviewer/  (11 files)
      … 11 files under this directory
    gl-reconciler/  (6 files)
      … 6 files under this directory
    kyc-screener/  (5 files)
      … 5 files under this directory
    market-researcher/  (9 files)
      … 9 files under this directory
    meeting-prep-agent/  (6 files)
      … 6 files under this directory
    model-builder/  (14 files)
      … 14 files under this directory
    month-end-closer/  (7 files)
      … 7 files under this directory
    pitch-agent/  (26 files)
      … 26 files under this directory
    statement-auditor/  (5 files)
      … 5 files under this directory
    valuation-reviewer/  (6 files)
      … 6 files under this directory
  partner-built/  (36 files)
    lseg/  (20 files)
      … 20 files under this directory
    spglobal/  (16 files)
      … 16 files under this directory
  vertical-plugins/  (130 files)
    equity-research/  (31 files)
      … 31 files under this directory
    financial-analysis/  (40 files)
      … 40 files under this directory
    fund-admin/  (7 files)
      … 7 files under this directory
    investment-banking/  (26 files)
      … 26 files under this directory
    operations/  (3 files)
      … 3 files under this directory
    private-equity/  (23 files)
      … 23 files under this directory
scripts/  (7 files)
  check.py
  deploy-managed-agent.sh
  orchestrate.py
  sync-agent-skills.py
  test-cookbooks.sh
  validate.py
  version_bump.py
.gitignore
CLAUDE.md
LICENSE
README.md
```

## Entry points

- [plugins/agent-plugins/model-builder/skills/dcf-model/scripts/validate_dcf.py:291](https://github.com/anthropics/financial-services/blob/3e32c2287dcb637c184c01cc0ad82d6af7e9bb0f/plugins/agent-plugins/model-builder/skills/dcf-model/scripts/validate_dcf.py#L291)
- [plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:291](https://github.com/anthropics/financial-services/blob/3e32c2287dcb637c184c01cc0ad82d6af7e9bb0f/plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py#L291)
- [plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:304](https://github.com/anthropics/financial-services/blob/3e32c2287dcb637c184c01cc0ad82d6af7e9bb0f/plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py#L304)
- [plugins/vertical-plugins/financial-analysis/skills/dcf-model/scripts/validate_dcf.py:291](https://github.com/anthropics/financial-services/blob/3e32c2287dcb637c184c01cc0ad82d6af7e9bb0f/plugins/vertical-plugins/financial-analysis/skills/dcf-model/scripts/validate_dcf.py#L291)
- [plugins/vertical-plugins/financial-analysis/skills/ib-check-deck/scripts/extract_numbers.py:304](https://github.com/anthropics/financial-services/blob/3e32c2287dcb637c184c01cc0ad82d6af7e9bb0f/plugins/vertical-plugins/financial-analysis/skills/ib-check-deck/scripts/extract_numbers.py#L304)
- [plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/init_skill.py:302](https://github.com/anthropics/financial-services/blob/3e32c2287dcb637c184c01cc0ad82d6af7e9bb0f/plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/init_skill.py#L302)
- [plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/package_skill.py:109](https://github.com/anthropics/financial-services/blob/3e32c2287dcb637c184c01cc0ad82d6af7e9bb0f/plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/package_skill.py#L109)
- [plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/quick_validate.py:88](https://github.com/anthropics/financial-services/blob/3e32c2287dcb637c184c01cc0ad82d6af7e9bb0f/plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/quick_validate.py#L88)
- [scripts/orchestrate.py:85](https://github.com/anthropics/financial-services/blob/3e32c2287dcb637c184c01cc0ad82d6af7e9bb0f/scripts/orchestrate.py#L85)
- [scripts/validate.py:41](https://github.com/anthropics/financial-services/blob/3e32c2287dcb637c184c01cc0ad82d6af7e9bb0f/scripts/validate.py#L41)
- [scripts/version_bump.py:208](https://github.com/anthropics/financial-services/blob/3e32c2287dcb637c184c01cc0ad82d6af7e9bb0f/scripts/version_bump.py#L208)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| claude-for-msft-365-install package | library | Observed | Groups 5 file(s) under claude-for-msft-365-install package (observed from repository paths and static analysis). Observed top-level functions: b64u. |
| Configuration and deployment | config | Observed | Groups 83 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: b64. |
| Application entry point | entrypoint | Observed | Groups 13 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed routes: GET /bootstrap. Observed top-level classes: DCFMode… |
| scripts package | library | Observed | Groups 4 file(s) under scripts package (observed from repository paths and static analysis). Observed top-level functions: check_refs, ensure_hooks_installed, err, rel. |

## Important files

- `.claude-plugin/marketplace.json` (config)
- `.github/workflows/plugin-validate.yml` (ci)
- `.github/workflows/version-bump.yml` (ci)
- `claude-for-msft-365-install/.claude-plugin/plugin.json` (config)
- `claude-for-msft-365-install/examples/python-bootstrap/requirements.txt` (manifest)
- `managed-agent-cookbooks/earnings-reviewer/agent.yaml` (config)
- `managed-agent-cookbooks/earnings-reviewer/steering-examples.json` (config)
- `managed-agent-cookbooks/earnings-reviewer/subagents/model-updater.yaml` (config)
- `managed-agent-cookbooks/earnings-reviewer/subagents/note-writer.yaml` (config)
- `managed-agent-cookbooks/earnings-reviewer/subagents/transcript-reader.yaml` (config)
- `managed-agent-cookbooks/gl-reconciler/agent.yaml` (config)
- `managed-agent-cookbooks/gl-reconciler/steering-examples.json` (config)
- `managed-agent-cookbooks/gl-reconciler/subagents/critic.yaml` (config)
- `managed-agent-cookbooks/gl-reconciler/subagents/reader.yaml` (config)
- `managed-agent-cookbooks/gl-reconciler/subagents/resolver.yaml` (config)
- `managed-agent-cookbooks/kyc-screener/agent.yaml` (config)
- `managed-agent-cookbooks/kyc-screener/steering-examples.json` (config)
- `managed-agent-cookbooks/kyc-screener/subagents/doc-reader.yaml` (config)
- `managed-agent-cookbooks/kyc-screener/subagents/escalator.yaml` (config)
- `managed-agent-cookbooks/kyc-screener/subagents/rules-engine.yaml` (config)
- `managed-agent-cookbooks/market-researcher/agent.yaml` (config)
- `managed-agent-cookbooks/market-researcher/steering-examples.json` (config)
- `managed-agent-cookbooks/market-researcher/subagents/comps-spreader.yaml` (config)
- `managed-agent-cookbooks/market-researcher/subagents/note-writer.yaml` (config)
- `managed-agent-cookbooks/market-researcher/subagents/sector-reader.yaml` (config)
- `managed-agent-cookbooks/meeting-prep-agent/agent.yaml` (config)
- `managed-agent-cookbooks/meeting-prep-agent/steering-examples.json` (config)
- `managed-agent-cookbooks/meeting-prep-agent/subagents/news-reader.yaml` (config)
- `managed-agent-cookbooks/meeting-prep-agent/subagents/pack-writer.yaml` (config)
- `managed-agent-cookbooks/meeting-prep-agent/subagents/profiler.yaml` (config)
- `managed-agent-cookbooks/model-builder/agent.yaml` (config)
- `managed-agent-cookbooks/model-builder/steering-examples.json` (config)
- `managed-agent-cookbooks/model-builder/subagents/auditor.yaml` (config)
- `managed-agent-cookbooks/model-builder/subagents/builder.yaml` (config)
- `managed-agent-cookbooks/model-builder/subagents/data-puller.yaml` (config)
- `managed-agent-cookbooks/month-end-closer/agent.yaml` (config)
- `managed-agent-cookbooks/month-end-closer/steering-examples.json` (config)
- `managed-agent-cookbooks/month-end-closer/subagents/ledger-reader.yaml` (config)
- `managed-agent-cookbooks/month-end-closer/subagents/poster.yaml` (config)
- `managed-agent-cookbooks/month-end-closer/subagents/rollforward.yaml` (config)
- `managed-agent-cookbooks/pitch-agent/agent.yaml` (config)
- `managed-agent-cookbooks/pitch-agent/steering-examples.json` (config)
- `managed-agent-cookbooks/pitch-agent/subagents/deck-writer.yaml` (config)
- `managed-agent-cookbooks/pitch-agent/subagents/modeler.yaml` (config)
- `managed-agent-cookbooks/pitch-agent/subagents/researcher.yaml` (config)
- `managed-agent-cookbooks/statement-auditor/agent.yaml` (config)
- `managed-agent-cookbooks/statement-auditor/steering-examples.json` (config)
- `managed-agent-cookbooks/statement-auditor/subagents/flagger.yaml` (config)
- `managed-agent-cookbooks/statement-auditor/subagents/reconciler.yaml` (config)
- `managed-agent-cookbooks/statement-auditor/subagents/statement-reader.yaml` (config)
- `managed-agent-cookbooks/valuation-reviewer/agent.yaml` (config)
- `managed-agent-cookbooks/valuation-reviewer/steering-examples.json` (config)
- `managed-agent-cookbooks/valuation-reviewer/subagents/package-reader.yaml` (config)
- `managed-agent-cookbooks/valuation-reviewer/subagents/publisher.yaml` (config)
- `managed-agent-cookbooks/valuation-reviewer/subagents/valuation-runner.yaml` (config)
- `plugins/agent-plugins/earnings-reviewer/.claude-plugin/plugin.json` (config)
- `plugins/agent-plugins/gl-reconciler/.claude-plugin/plugin.json` (config)
- `plugins/agent-plugins/kyc-screener/.claude-plugin/plugin.json` (config)
- `plugins/agent-plugins/market-researcher/.claude-plugin/plugin.json` (config)
- `plugins/agent-plugins/meeting-prep-agent/.claude-plugin/plugin.json` (config)
- `plugins/agent-plugins/model-builder/.claude-plugin/plugin.json` (config)
- `plugins/agent-plugins/model-builder/skills/dcf-model/requirements.txt` (manifest)
- `plugins/agent-plugins/month-end-closer/.claude-plugin/plugin.json` (config)
- `plugins/agent-plugins/pitch-agent/.claude-plugin/plugin.json` (config)
- `plugins/agent-plugins/pitch-agent/skills/dcf-model/requirements.txt` (manifest)
- `plugins/agent-plugins/statement-auditor/.claude-plugin/plugin.json` (config)
- `plugins/agent-plugins/valuation-reviewer/.claude-plugin/plugin.json` (config)
- `plugins/partner-built/lseg/.claude-plugin/plugin.json` (config)
- `plugins/partner-built/lseg/.mcp.json` (config)
- `plugins/partner-built/spglobal/.claude-plugin/plugin.json` (config)
- `plugins/partner-built/spglobal/.mcp.json` (config)
- `plugins/vertical-plugins/equity-research/.claude-plugin/plugin.json` (config)
- `plugins/vertical-plugins/equity-research/hooks/hooks.json` (config)
- `plugins/vertical-plugins/financial-analysis/.claude-plugin/plugin.json` (config)
- `plugins/vertical-plugins/financial-analysis/.mcp.json` (config)
- `plugins/vertical-plugins/financial-analysis/hooks/hooks.json` (config)
- `plugins/vertical-plugins/financial-analysis/skills/dcf-model/requirements.txt` (manifest)
- `plugins/vertical-plugins/fund-admin/.claude-plugin/plugin.json` (config)
- `plugins/vertical-plugins/investment-banking/.claude-plugin/plugin.json` (config)
- `plugins/vertical-plugins/investment-banking/.mcp.json` (config)
- `plugins/vertical-plugins/investment-banking/hooks/hooks.json` (config)
- `plugins/vertical-plugins/operations/.claude-plugin/plugin.json` (config)
- `plugins/vertical-plugins/private-equity/.claude-plugin/plugin.json` (config)
- `plugins/vertical-plugins/private-equity/.mcp.json` (config)
- `plugins/vertical-plugins/private-equity/hooks/hooks.json` (config)

## Top-level layout

- `plugins` — 261 analysed file(s)
- `managed-agent-cookbooks` — 61 analysed file(s)
- `claude-for-msft-365-install` — 25 analysed file(s)
- `scripts` — 7 analysed file(s)
- `(root files)` — 4 analysed file(s)
- `.github` — 2 analysed file(s)
- `.claude-plugin` — 1 analysed file(s)
- `.githooks` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `3e32c2287dcb637c184c01cc0ad82d6af7e9bb0f` is the revision these paths and observations refer to.
