# Project structure: anthropics/knowledge-work-plugins

**Analysed commit:** `e91a134584eb798bac7fb0379358006a2b63b965`

**Commit reference:** [e91a134584eb798bac7fb0379358006a2b63b965](https://github.com/anthropics/knowledge-work-plugins/commit/e91a134584eb798bac7fb0379358006a2b63b965)

**Tree at this commit:** [anthropics/knowledge-work-plugins@e91a134584eb](https://github.com/anthropics/knowledge-work-plugins/tree/e91a134584eb798bac7fb0379358006a2b63b965)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | anthropics/knowledge-work-plugins |
| Description | Open source repository of plugins primarily intended for knowledge workers to use in Claude Cowork |
| Stars | 35776 |
| Forks | 3961 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `e91a134584eb798bac7fb0379358006a2b63b965` |
| Retrieved at | 2026-11-14T19:06:55.145133+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.claude-plugin/  (1 files)
  marketplace.json
.github/  (7 files)
  policy/  (2 files)
    prompt.md
    schema.json
  workflows/  (5 files)
    bump-plugin-shas.yml
    check-mcp-urls.yml
    close-external-prs.yml
    revert-failed-bumps.yml
    scan-plugins.yml
bio-research/  (78 files)
  .claude-plugin/  (1 files)
    plugin.json
  skills/  (73 files)
    instrument-data-to-allotrope/  (11 files)
      … 11 files under this directory
    nextflow-development/  (22 files)
      … 22 files under this directory
    scientific-problem-selection/  (11 files)
      … 11 files under this directory
    scvi-tools/  (22 files)
      … 22 files under this directory
    single-cell-rna-qc/  (6 files)
      … 6 files under this directory
    start/  (1 files)
      … 1 files under this directory
  .mcp.json
  CONNECTORS.md
  LICENSE
  README.md
cowork-plugin-management/  (10 files)
  .claude-plugin/  (1 files)
    plugin.json
  skills/  (8 files)
    cowork-plugin-customizer/  (5 files)
      … 5 files under this directory
    create-cowork-plugin/  (3 files)
      … 3 files under this directory
  LICENSE
customer-support/  (10 files)
  .claude-plugin/  (1 files)
    plugin.json
  skills/  (5 files)
    customer-escalation/  (1 files)
      … 1 files under this directory
    customer-research/  (1 files)
      … 1 files under this directory
    draft-response/  (1 files)
      … 1 files under this directory
    kb-article/  (1 files)
      … 1 files under this directory
    ticket-triage/  (1 files)
      … 1 files under this directory
  .mcp.json
  CONNECTORS.md
  LICENSE
  README.md
data/  (20 files)
  .claude-plugin/  (1 files)
    plugin.json
  skills/  (15 files)
    analyze/  (1 files)
      … 1 files under this directory
    build-dashboard/  (1 files)
      … 1 files under this directory
    create-viz/  (1 files)
      … 1 files under this directory
    data-context-extractor/  (6 files)
      … 6 files under this directory
    data-visualization/  (1 files)
      … 1 files under this directory
    explore-data/  (1 files)
      … 1 files under this directory
    sql-queries/  (1 files)
      … 1 files under this directory
    statistical-analysis/  (1 files)
      … 1 files under this directory
    validate-data/  (1 files)
      … 1 files under this directory
    write-query/  (1 files)
      … 1 files under this directory
  .mcp.json
  CONNECTORS.md
  LICENSE
  README.md
design/  (11 files)
  .claude-plugin/  (1 files)
    plugin.json
  skills/  (7 files)
    accessibility-review/  (1 files)
      … 1 files under this directory
    design-critique/  (1 files)
      … 1 files under this directory
    design-handoff/  (1 files)
      … 1 files under this directory
    design-system/  (1 files)
      … 1 files under this directory
    research-synthesis/  (1 files)
      … 1 files under this directory
    user-research/  (1 files)
      … 1 files under this directory
    ux-copy/  (1 files)
      … 1 files under this directory
  .mcp.json
  CONNECTORS.md
  README.md
engineering/  (14 files)
  .claude-plugin/  (1 files)
    plugin.json
  skills/  (10 files)
    architecture/  (1 files)
      … 1 files under this directory
    code-review/  (1 files)
      … 1 files under this directory
    debug/  (1 files)
      … 1 files under this directory
    deploy-checklist/  (1 files)
      … 1 files under this directory
    documentation/  (1 files)
      … 1 files under this directory
    incident-response/  (1 files)
      … 1 files under this directory
    standup/  (1 files)
      … 1 files under this directory
    system-design/  (1 files)
      … 1 files under this directory
    tech-debt/  (1 files)
      … 1 files under this directory
    testing-strategy/  (1 files)
      … 1 files under this directory
  .mcp.json
  CONNECTORS.md
  README.md
enterprise-search/  (10 files)
  .claude-plugin/  (1 files)
    plugin.json
  skills/  (5 files)
    digest/  (1 files)
      … 1 files under this directory
    knowledge-synthesis/  (1 files)
      … 1 files under this directory
    search/  (1 files)
      … 1 files under this directory
    search-strategy/  (1 files)
      … 1 files under this directory
    source-management/  (1 files)
      … 1 files under this directory
  .mcp.json
  CONNECTORS.md
  LICENSE
  README.md
finance/  (13 files)
  .claude-plugin/  (1 files)
    plugin.json
  skills/  (8 files)
    audit-support/  (1 files)
      … 1 files under this directory
    close-management/  (1 files)
      … 1 files under this directory
    financial-statements/  (1 files)
      … 1 files under this directory
    journal-entry/  (1 files)
      … 1 files under this directory
    journal-entry-prep/  (1 files)
      … 1 files under this directory
    reconciliation/  (1 files)
      … 1 files under this directory
    sox-testing/  (1 files)
      … 1 files under this directory
    variance-analysis/  (1 files)
      … 1 files under this directory
  .mcp.json
  CONNECTORS.md
  LICENSE
  README.md
human-resources/  (13 files)
  .claude-plugin/  (1 files)
    plugin.json
  skills/  (9 files)
    comp-analysis/  (1 files)
      … 1 files under this directory
    draft-offer/  (1 files)
      … 1 files under this directory
    interview-prep/  (1 files)
      … 1 files under this directory
    onboarding/  (1 files)
      … 1 files under this directory
    org-planning/  (1 files)
      … 1 files under this directory
    people-report/  (1 files)
      … 1 files under this directory
    performance-review/  (1 files)
      … 1 files under this directory
    policy-lookup/  (1 files)
      … 1 files under this directory
    recruiting-pipeline/  (1 files)
      … 1 files under this directory
  .mcp.json
  CONNECTORS.md
  README.md
legal/  (14 files)
  .claude-plugin/  (1 files)
    plugin.json
  skills/  (9 files)
    brief/  (1 files)
      … 1 files under this directory
    compliance-check/  (1 files)
      … 1 files under this directory
    legal-response/  (1 files)
      … 1 files under this directory
    legal-risk-assessment/  (1 files)
      … 1 files under this directory
    meeting-briefing/  (1 files)
      … 1 files under this directory
    review-contract/  (1 files)
      … 1 files under this directory
    signature-request/  (1 files)
      … 1 files under this directory
    triage-nda/  (1 files)
      … 1 files under this directory
    vendor-check/  (1 files)
      … 1 files under this directory
  .mcp.json
  CONNECTORS.md
  LICENSE
  README.md
marketing/  (13 files)
  .claude-plugin/  (1 files)
    plugin.json
  skills/  (8 files)
    brand-review/  (1 files)
      … 1 files under this directory
    campaign-plan/  (1 files)
      … 1 files under this directory
    competitive-brief/  (1 files)
      … 1 files under this directory
    content-creation/  (1 files)
      … 1 files under this directory
    draft-content/  (1 files)
      … 1 files under this directory
    email-sequence/  (1 files)
      … 1 files under this directory
    performance-report/  (1 files)
      … 1 files under this directory
    seo-audit/  (1 files)
      … 1 files under this directory
  .mcp.json
  CONNECTORS.md
  LICENSE
  README.md
operations/  (13 files)
  .claude-plugin/  (1 files)
    plugin.json
  skills/  (9 files)
    capacity-plan/  (1 files)
      … 1 files under this directory
    change-request/  (1 files)
      … 1 files under this directory
    compliance-tracking/  (1 files)
      … 1 files under this directory
    process-doc/  (1 files)
      … 1 files under this directory
    process-optimization/  (1 files)
      … 1 files under this directory
    risk-assessment/  (1 files)
      … 1 files under this directory
    runbook/  (1 files)
      … 1 files under this directory
    status-report/  (1 files)
      … 1 files under this directory
    vendor-review/  (1 files)
      … 1 files under this directory
  .mcp.json
  CONNECTORS.md
  README.md
partner-built/  (571 files)
  apollo/  (7 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    skills/  (3 files)
      … 3 files under this directory
    .mcp.json
    LICENSE
    README.md
  brand-voice/  (23 files)
    .claude-plugin/  (2 files)
      … 2 files under this directory
    agents/  (5 files)
      … 5 files under this directory
    commands/  (3 files)
      … 3 files under this directory
    settings/  (1 files)
      … 1 files under this directory
    skills/  (9 files)
      … 9 files under this directory
    .mcp.json
    LICENSE
    README.md
  common-room/  (21 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    commands/  (2 files)
      … 2 files under this directory
    references/  (2 files)
      … 2 files under this directory
    skills/  (12 files)
      … 12 files under this directory
    .mcp.json
    CONNECTORS.md
    LICENSE
    README.md
  slack/  (12 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    commands/  (5 files)
      … 5 files under this directory
    skills/  (2 files)
      … 2 files under this directory
    .mcp.json
    CLAUDE.md
    LICENSE
    README.md
  zoom-plugin/  (508 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    skills/  (500 files)
      … 500 files under this directory
    .mcp.json
    AGENTS.md
    CHANGELOG.md
    CONNECTORS.md
    CONTRIBUTING.md
    LICENSE
    README.md
LICENSE
README.md
```

## Entry points

- [bio-research/skills/instrument-data-to-allotrope/scripts/convert_to_asm.py:542](https://github.com/anthropics/knowledge-work-plugins/blob/e91a134584eb798bac7fb0379358006a2b63b965/bio-research/skills/instrument-data-to-allotrope/scripts/convert_to_asm.py#L542)
- [bio-research/skills/instrument-data-to-allotrope/scripts/export_parser.py:480](https://github.com/anthropics/knowledge-work-plugins/blob/e91a134584eb798bac7fb0379358006a2b63b965/bio-research/skills/instrument-data-to-allotrope/scripts/export_parser.py#L480)
- [bio-research/skills/instrument-data-to-allotrope/scripts/flatten_asm.py:253](https://github.com/anthropics/knowledge-work-plugins/blob/e91a134584eb798bac7fb0379358006a2b63b965/bio-research/skills/instrument-data-to-allotrope/scripts/flatten_asm.py#L253)
- [bio-research/skills/instrument-data-to-allotrope/scripts/validate_asm.py:1101](https://github.com/anthropics/knowledge-work-plugins/blob/e91a134584eb798bac7fb0379358006a2b63b965/bio-research/skills/instrument-data-to-allotrope/scripts/validate_asm.py#L1101)
- [bio-research/skills/nextflow-development/scripts/check_environment.py:451](https://github.com/anthropics/knowledge-work-plugins/blob/e91a134584eb798bac7fb0379358006a2b63b965/bio-research/skills/nextflow-development/scripts/check_environment.py#L451)
- [bio-research/skills/nextflow-development/scripts/detect_data_type.py:299](https://github.com/anthropics/knowledge-work-plugins/blob/e91a134584eb798bac7fb0379358006a2b63b965/bio-research/skills/nextflow-development/scripts/detect_data_type.py#L299)
- [bio-research/skills/nextflow-development/scripts/generate_samplesheet.py:454](https://github.com/anthropics/knowledge-work-plugins/blob/e91a134584eb798bac7fb0379358006a2b63b965/bio-research/skills/nextflow-development/scripts/generate_samplesheet.py#L454)
- [bio-research/skills/nextflow-development/scripts/manage_genomes.py:520](https://github.com/anthropics/knowledge-work-plugins/blob/e91a134584eb798bac7fb0379358006a2b63b965/bio-research/skills/nextflow-development/scripts/manage_genomes.py#L520)
- [bio-research/skills/nextflow-development/scripts/sra_geo_fetch.py:731](https://github.com/anthropics/knowledge-work-plugins/blob/e91a134584eb798bac7fb0379358006a2b63b965/bio-research/skills/nextflow-development/scripts/sra_geo_fetch.py#L731)
- [bio-research/skills/scvi-tools/scripts/cluster_embed.py:211](https://github.com/anthropics/knowledge-work-plugins/blob/e91a134584eb798bac7fb0379358006a2b63b965/bio-research/skills/scvi-tools/scripts/cluster_embed.py#L211)
- [bio-research/skills/scvi-tools/scripts/differential_expression.py:219](https://github.com/anthropics/knowledge-work-plugins/blob/e91a134584eb798bac7fb0379358006a2b63b965/bio-research/skills/scvi-tools/scripts/differential_expression.py#L219)
- [bio-research/skills/scvi-tools/scripts/integrate_datasets.py:236](https://github.com/anthropics/knowledge-work-plugins/blob/e91a134584eb798bac7fb0379358006a2b63b965/bio-research/skills/scvi-tools/scripts/integrate_datasets.py#L236)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bio-research package | library | Observed | Groups 8 file(s) under bio-research package (observed from repository paths and static analysis). Observed top-level classes: FileInfo, ValidationResult. Observed top-level functions: _format_gsm_range, _get_pattern_sco… |
| Configuration and deployment | config | Observed | Groups 40 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 18 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: CheckResult, EnvironmentReport, StudyInfo, ValidationResult. Observed top-level functions… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |

## Important files

- `.claude-plugin/marketplace.json` (config)
- `.github/policy/schema.json` (config)
- `.github/workflows/bump-plugin-shas.yml` (ci)
- `.github/workflows/check-mcp-urls.yml` (ci)
- `.github/workflows/close-external-prs.yml` (ci)
- `.github/workflows/revert-failed-bumps.yml` (ci)
- `.github/workflows/scan-plugins.yml` (ci)
- `bio-research/.claude-plugin/plugin.json` (config)
- `bio-research/.mcp.json` (config)
- `bio-research/skills/instrument-data-to-allotrope/requirements.txt` (manifest)
- `bio-research/skills/nextflow-development/scripts/config/genomes.yaml` (config)
- `bio-research/skills/nextflow-development/scripts/config/pipelines/atacseq.yaml` (config)
- `bio-research/skills/nextflow-development/scripts/config/pipelines/rnaseq.yaml` (config)
- `bio-research/skills/nextflow-development/scripts/config/pipelines/sarek.yaml` (config)
- `cowork-plugin-management/.claude-plugin/plugin.json` (config)
- `cowork-plugin-management/skills/cowork-plugin-customizer/examples/customized-mcp.json` (config)
- `customer-support/.claude-plugin/plugin.json` (config)
- `customer-support/.mcp.json` (config)
- `data/.claude-plugin/plugin.json` (config)
- `data/.mcp.json` (config)
- `design/.claude-plugin/plugin.json` (config)
- `design/.mcp.json` (config)
- `engineering/.claude-plugin/plugin.json` (config)
- `engineering/.mcp.json` (config)
- `enterprise-search/.claude-plugin/plugin.json` (config)
- `enterprise-search/.mcp.json` (config)
- `finance/.claude-plugin/plugin.json` (config)
- `finance/.mcp.json` (config)
- `human-resources/.claude-plugin/plugin.json` (config)
- `human-resources/.mcp.json` (config)
- `legal/.claude-plugin/plugin.json` (config)
- `legal/.mcp.json` (config)
- `marketing/.claude-plugin/plugin.json` (config)
- `marketing/.mcp.json` (config)
- `operations/.claude-plugin/plugin.json` (config)
- `operations/.mcp.json` (config)
- `partner-built/apollo/.claude-plugin/plugin.json` (config)
- `partner-built/apollo/.mcp.json` (config)
- `partner-built/brand-voice/.claude-plugin/marketplace.json` (config)
- `partner-built/brand-voice/.claude-plugin/plugin.json` (config)
- `partner-built/brand-voice/.mcp.json` (config)
- `partner-built/common-room/.claude-plugin/plugin.json` (config)
- `partner-built/common-room/.mcp.json` (config)
- `partner-built/slack/.claude-plugin/plugin.json` (config)
- `partner-built/slack/.mcp.json` (config)
- `partner-built/zoom-plugin/.claude-plugin/plugin.json` (config)
- `partner-built/zoom-plugin/.mcp.json` (config)

## Top-level layout

- `partner-built` — 571 analysed file(s)
- `bio-research` — 78 analysed file(s)
- `data` — 20 analysed file(s)
- `engineering` — 14 analysed file(s)
- `legal` — 14 analysed file(s)
- `finance` — 13 analysed file(s)
- `human-resources` — 13 analysed file(s)
- `marketing` — 13 analysed file(s)
- `operations` — 13 analysed file(s)
- `design` — 11 analysed file(s)
- `cowork-plugin-management` — 10 analysed file(s)
- `customer-support` — 10 analysed file(s)
- `enterprise-search` — 10 analysed file(s)
- `.github` — 7 analysed file(s)
- `(root files)` — 2 analysed file(s)
- `.claude-plugin` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `e91a134584eb798bac7fb0379358006a2b63b965` is the revision these paths and observations refer to.
