# Project structure: alirezarezvani/claude-skills

**Analysed commit:** `08cd8a9fc86cc370e2c0d448e8171fbcfdbc5a30`

**Commit reference:** [08cd8a9fc86cc370e2c0d448e8171fbcfdbc5a30](https://github.com/alirezarezvani/claude-skills/commit/08cd8a9fc86cc370e2c0d448e8171fbcfdbc5a30)

**Tree at this commit:** [alirezarezvani/claude-skills@08cd8a9fc86c](https://github.com/alirezarezvani/claude-skills/tree/08cd8a9fc86cc370e2c0d448e8171fbcfdbc5a30)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | alirezarezvani/claude-skills |
| Description | 410 Claude Code skills & agent skills & plugins (120+ Agents, custom commands, 410+ skills, customizable references, scripts)for Claude Code, Codex, Gemini CLI, Cursor, and 8 more coding agents — engineering, marketing, product, compliance, C-level advisory, research, business operations, commercia… |
| Stars | 29802 |
| Forks | 4135 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `08cd8a9fc86cc370e2c0d448e8171fbcfdbc5a30` |
| Retrieved at | 2026-11-14T19:07:13.242201+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.claude/  (13 files)
  claudex/  (1 files)
    log
  commands/  (10 files)
    git/  (4 files)
      … 4 files under this directory
    focused-fix.md
    plugin-audit.md
    quality-gate.md
    security-scan.md
    seo-auditor.md
    update-docs.md
  COMMANDS.md
  settings.json
.claude-plugin/  (1 files)
  marketplace.json
.codex/  (1 files)
  skills-index.json
.codex-plugin/  (1 files)
  plugin.json
.gemini/  (1 files)
  skills-index.json
.github/  (30 files)
  ISSUE_TEMPLATE/  (4 files)
    bug_report.md
    documentation.md
    feature_request.md
    skill_improvement.md
  workflows/  (18 files)
    ci-quality-gate.yml
    claude-code-review.yml
    claude.yml
    docs-preview.yml
    enforce-pr-target.yml
    harness-compat.yml
    hero-sync.yml
    pr-issue-auto-close.yml
    release.yml
    skill-evals.yml
    skill-quality-review.yml
    skill-security-audit.yml
    smart-sync.yml
    static.yml
    sync-codex-skills.yml
    traffic-snapshot.yml
    trigger-gate.yml
    virustotal-scan.yml
  AUTOMATION_SETUP.md
  AUTOMATION_TEST.md
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
  TRIAGE_POLICY.md
  WORKFLOW_KILLSWITCH
  branch-protection-config.json
  commit-template.txt
.hermes/  (1 files)
  skills/  (1 files)
    claude-skills/  (1 files)
      … 1 files under this directory
.vibe/  (1 files)
  skills/  (1 files)
    claude-skills/  (1 files)
      … 1 files under this directory
agent-launcher/  (60 files)
  .claude-plugin/  (2 files)
    authoring-notes.json
    plugin.json
  agents/  (4 files)
    cs-agent-deployer.md
    cs-agent-grader.md
    cs-agent-interviewer.md
    cs-agent-launcher-orchestrator.md
  assets/  (4 files)
    NEXT-DIRECTIONS.template.md
    agent-overview.template.html
    build-sheet.schema.json
    example-build-sheet.json
  commands/  (8 files)
    cs-goal.md
    cs-grade.md
    cs-grill-agent-launcher.md
    cs-interview.md
    cs-launch.md
    cs-run-without-you.md
    cs-stage-launch.md
    cs-wrap-up.md
  hooks/  (3 files)
    hooks.json
    session_end.py
    session_start.py
  references/  (5 files)
    cma-primitives.md
    examples-bank.md
    interview-to-config.md
    loops-and-workflows.md
    session-goal-model.md
  skills/  (30 files)
    agent-launcher-orchestrator/  (5 files)
      … 5 files under this directory
    grade-iterate/  (5 files)
      … 5 files under this directory
    interview/  (5 files)
      … 5 files under this directory
    run-without-you/  (5 files)
      … 5 files under this directory
    stage-launch/  (5 files)
      … 5 files under this directory
    wrap-up/  (5 files)
      … 5 files under this directory
  CLAUDE.md
  PUBLISH-CLAWHUB.md
  README.md
  SPEC.md
agents/  (38 files)
  business-growth/  (1 files)
    cs-growth-strategist.md
  c-level/  (3 files)
    .gitkeep
    cs-ceo-advisor.md
    cs-cto-advisor.md
  engineering/  (8 files)
    cs-backend-engineer.md
    cs-frontend-engineer.md
    cs-fullstack-engineer.md
    cs-karpathy-reviewer.md
    cs-senior-engineer.md
    cs-wiki-ingestor.md
    cs-wiki-librarian.md
    cs-wiki-linter.md
  engineering-team/  (2 files)
    cs-engineering-lead.md
    cs-workspace-admin.md
  finance/  (1 files)
    cs-financial-analyst.md
  marketing/  (5 files)
    .gitkeep
    cs-aeo.md
    cs-content-creator.md
    cs-demand-gen-specialist.md
    cs-webinar-marketer.md
  personas/  (9 files)
    README.md
    TEMPLATE.md
    content-strategist.md
    devops-engineer.md
    finance-lead.md
    growth-marketer.md
    product-manager.md
    solo-founder.md
    startup-cto.md
  product/  (6 files)
    .gitkeep
    cs-agile-product-owner.md
    cs-product-analyst.md
    cs-product-manager.md
    cs-product-strategist.md
    cs-ux-researcher.md
  project-management/  (1 files)
    cs-project-manager.md
  ra-qm-team/  (1 files)
    cs-quality-regulatory.md
  CLAUDE.md
audit/  (34 files)
  engineering-agentic-2026-07/  (6 files)
    00-MASTER.md
    RUBRIC.md
    engineering-team.md
    engineering.md
    improvement-fields.md
    research-digest.md
  human-review-2026-08/  (1 files)
    AUDIT.md
  newgen-2026-06/  (12 files)
    00-MASTER.md
    RUBRIC.md
    bizops-commercial-finance.md
    c-level-advisor.md
    compliance.md
    cross-cutting.md
    engineering-team.md
    engineering.md
    marketing.md
    product-pm.md
    productivity-markdown-html.md
    research.md
  pm-product-agentic-2026-07/  (6 files)
    00-MASTER.md
    RUBRIC.md
    improvement-fields.md
    product-team.md
    project-management.md
    research-digest.md
  pr-stream-2026-08/  (6 files)
    00-MASTER.md
    closures.md
    fix-series-governance.md
    fix-series-small.md
    maintainer-drafts.md
    new-skills.md
  productivity-2026-07/  (1 files)
    00-MASTER.md
  silent-skill-triggers-2026-11/  (1 files)
    README.md
  verified-tier/  (1 files)
    trigger_results.json
business-growth/  (44 files)
  .claude-plugin/  (1 files)
    plugin.json
  .codex/  (1 files)
    instructions.md
  skills/  (41 files)
    business-growth-skills/  (1 files)
      … 1 files under this directory
    contract-and-proposal-writer/  (1 files)
      … 1 files under this directory
    customer-success-manager/  (13 files)
      … 13 files under this directory
    revenue-operations/  (14 files)
      … 14 files under this directory
    sales-engineer/  (12 files)
      … 12 files under this directory
  CLAUDE.md
business-operations/  (63 files)
  .claude-plugin/  (2 files)
    authoring-notes.json
    plugin.json
  agents/  (1 files)
    cs-bizops-orchestrator.md
  commands/  (8 files)
    cs-bizops.md
    cs-capacity-plan.md
    cs-grill-bizops.md
    cs-internal-comms.md
    cs-knowledge-ops.md
    cs-process-map.md
    cs-procurement.md
    cs-vendor-review.md
  skills/  (50 files)
    business-operations-skills/  (1 files)
      … 1 files under this directory
    capacity-planner/  (8 files)
      … 8 files under this directory
    internal-comms/  (8 files)
      … 8 files under this directory
    knowledge-ops/  (9 files)
      … 9 files under this directory
    process-mapper/  (8 files)
      … 8 files under this directory
    procurement-optimizer/  (8 files)
      … 8 files under this directory
    vendor-management/  (8 files)
      … 8 files under this directory
  CLAUDE.md
  README.md
c-level-advisor/  (249 files)
  .claude-plugin/  (1 files)
    plugin.json
  .codex/  (1 files)
    instructions.md
  arquiteto-de-empresa/  (19 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (1 files)
      … 1 files under this directory
    commands/  (1 files)
      … 1 files under this directory
    skills/  (15 files)
      … 15 files under this directory
    README.md
  chief-ai-officer-advisor/  (10 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    skills/  (8 files)
      … 8 files under this directory
    README.md
  chief-customer-officer-advisor/  (10 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    skills/  (8 files)
      … 8 files under this directory
    README.md
  chief-data-officer-advisor/  (10 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    skills/  (8 files)
      … 8 files under this directory
    README.md
  executive-mentor/  (13 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (1 files)
      … 1 files under this directory
    skills/  (11 files)
      … 11 files under this directory
  general-counsel-advisor/  (8 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    skills/  (6 files)
      … 6 files under this directory
    README.md
  hooks/  (3 files)
    hooks.json
    skill_router.py
    skill_routes.json
  skills/  (161 files)
    agent-protocol/  (2 files)
      … 2 files under this directory
    arquiteto-de-empresa/  (15 files)
      … 15 files under this directory
    board-deck-builder/  (3 files)
      … 3 files under this directory
    board-meeting/  (4 files)
      … 4 files under this directory
    c-level-skills/  (1 files)
      … 1 files under this directory
    ceo-advisor/  (6 files)
      … 6 files under this directory
    cfo-advisor/  (7 files)
      … 7 files under this directory
    change-management/  (2 files)
      … 2 files under this directory
    chief-ai-officer-advisor/  (8 files)
      … 8 files under this directory
    chief-customer-officer-advisor/  (8 files)
      … 8 files under this directory
    chief-data-officer-advisor/  (8 files)
      … 8 files under this directory
    chief-of-staff/  (3 files)
      … 3 files under this directory
    chro-advisor/  (6 files)
      … 6 files under this directory
    ciso-advisor/  (6 files)
      … 6 files under this directory
    cmo-advisor/  (6 files)
      … 6 files under this directory
    company-os/  (3 files)
      … 3 files under this directory
    competitive-intel/  (3 files)
      … 3 files under this directory
    context-engine/  (2 files)
      … 2 files under this directory
    coo-advisor/  (6 files)
      … 6 files under this directory
    cpo-advisor/  (6 files)
      … 6 files under this directory
    cro-advisor/  (6 files)
      … 6 files under this directory
    cs-onboard/  (3 files)
      … 3 files under this directory
    cto-advisor/  (6 files)
      … 6 files under this directory
    culture-architect/  (3 files)
      … 3 files under this directory
    decision-logger/  (3 files)
      … 3 files under this directory
    founder-coach/  (3 files)
      … 3 files under this directory
    general-counsel-advisor/  (6 files)
      … 6 files under this directory
    internal-narrative/  (3 files)
      … 3 files under this directory
    intl-expansion/  (3 files)
      … 3 files under this directory
    ma-playbook/  (3 files)
      … 3 files under this directory
    org-health-diagnostic/  (3 files)
      … 3 files under this directory
    scenario-war-room/  (3 files)
      … 3 files under this directory
    strategic-alignment/  (3 files)
      … 3 files under this directory
    vpe-advisor/  (8 files)
      … 8 files under this directory
  vpe-advisor/  (10 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    skills/  (8 files)
      … 8 files under this directory
    README.md
  CLAUDE.md
  README.md
  c_level_leadership_skills_overview.md
c-level-agents/  (39 files)
  .claude-plugin/  (1 files)
    plugin.json
  agents/  (13 files)
    cs-caio-advisor.md
    cs-cco-advisor.md
    cs-cdo-advisor.md
    cs-cfo-advisor.md
    cs-chief-of-staff.md
    cs-chro-advisor.md
    cs-ciso-advisor.md
    cs-cmo-advisor.md
    cs-coo-advisor.md
    cs-cpo-advisor.md
    cs-cro-advisor.md
    cs-general-counsel-advisor.md
    cs-vpe-advisor.md
  references/  (2 files)
    llm-wiki-bridge.md
    persona-voices.md
  skills/  (22 files)
    boardroom/  (1 files)
      … 1 files under this directory
    brief/  (1 files)
      … 1 files under this directory
    c-level-agents/  (1 files)
      … 1 files under this directory
    caio-review/  (1 files)
      … 1 files under this directory
    cco-review/  (1 files)
      … 1 files under this directory
    cdo-review/  (1 files)
      … 1 files under this directory
    cfo-review/  (1 files)
      … 1 files under this directory
    ciso-review/  (1 files)
      … 1 files under this directory
    cmo-review/  (1 files)
      … 1 files under this directory
    cpo-review/  (1 files)
      … 1 files under this directory
    cro-review/  (1 files)
      … 1 files under this directory
    cross-eval/  (1 files)
      … 1 files under this directory
    cto-review/  (1 files)
      … 1 files under this directory
    decide/  (1 files)
      … 1 files under this directory
    execute/  (1 files)
      … 1 files under this directory
    founder-mode/  (1 files)
      … 1 files under this directory
    freeze/  (1 files)
      … 1 files under this directory
    gc-review/  (1 files)
      … 1 files under this directory
    office-hours/  (1 files)
      … 1 files under this directory
    onboard/  (1 files)
      … 1 files under this directory
    post-mortem/  (1 files)
      … 1 files under this directory
    vpe-review/  (1 files)
      … 1 files under this directory
  README.md
commands/  (40 files)
  .gitkeep
  a11y-audit.md
  changelog.md
  chaos-experiment.md
  code-to-prd.md
  competitive-matrix.md
  cs-aeo.md
  cs-backend-review.md
  cs-engineer-grill.md
  cs-frontend-review.md
  cs-fullstack-review.md
  cs-webinar.md
  financial-health.md
  flag-cleanup.md
  focused-fix.md
  google-workspace.md
  karpathy-check.md
  okr.md
  operator-audit.md
  persona.md
  pipeline.md
  plugin-audit.md
  prd.md
  project-health.md
  … 16 more files
commercial/  (71 files)
  .claude-plugin/  (2 files)
    authoring-notes.json
    plugin.json
  agents/  (1 files)
    cs-commercial-orchestrator.md
  commands/  (9 files)
    cs-channel-econ.md
    cs-commercial-forecast.md
    cs-commercial-policy.md
    cs-commercial.md
    cs-deal-review.md
    cs-grill-commercial.md
    cs-partner-tier.md
    cs-pricing-strategy.md
    cs-rfp-respond.md
  skills/  (57 files)
    channel-economics/  (8 files)
      … 8 files under this directory
    commercial-forecaster/  (8 files)
      … 8 files under this directory
    commercial-policy/  (8 files)
      … 8 files under this directory
    commercial-skills/  (1 files)
      … 1 files under this directory
    deal-desk/  (8 files)
      … 8 files under this directory
    partnerships-architect/  (8 files)
      … 8 files under this directory
    pricing-strategist/  (8 files)
      … 8 files under this directory
    rfp-responder/  (8 files)
      … 8 files under this directory
  CLAUDE.md
  README.md
compliance-os/  (32 files)
  .claude-plugin/  (1 files)
    plugin.json
  agents/  (8 files)
    cs-ai-act-compliance.md
    cs-aims-iso42001.md
    cs-ciso-iso27001.md
    cs-compliance-officer.md
    cs-cqm-iso13485.md
    cs-dpo-gdpr.md
    cs-fda-qsr-auditor.md
    cs-soc2-auditor.md
  skills/  (22 files)
    ai-act-readiness/  (1 files)
      … 1 files under this directory
    aims-audit/  (1 files)
      … 1 files under this directory
    compliance-os/  (14 files)
      … 14 files under this directory
    compliance-readiness/  (1 files)
      … 1 files under this directory
    fda-qsr-audit-prep/  (1 files)
      … 1 files under this directory
    gdpr-audit-prep/  (1 files)
      … 1 files under this directory
    iso13485-audit-prep/  (1 files)
      … 1 files under this directory
    iso27001-audit-prep/  (1 files)
      … 1 files under this directory
    soc2-audit-prep/  (1 files)
      … 1 files under this directory
  README.md
custom-gpt/  (1 files)
  README.md
docs/  (29 files)
  guides/  (7 files)
    agent-skills-for-codex.md
    best-claude-code-plugins.md
    cursor-skills-guide.md
    gemini-cli-skills-guide.md
    hermes-agent-skills-guide.md
    mistral-vibe-skills-guide.md
    openclaw-skills-guide.md
  overrides/  (5 files)
    partials/  (2 files)
      … 2 files under this directory
    .gitkeep
    404.html
    main.html
  personas/  (4 files)
    growth-marketer.md
    index.md
    solo-founder.md
    startup-cto.md
  plugins/  (1 files)
    index.md
  skills/  (1 files)
    index.md
  stylesheets/  (1 files)
    extra.css
  custom-gpts.md
  getting-started.md
  googlec3db22c96191d971.html
  index.md
  integrations.md
  llms-full.txt
  llms.txt
  orchestration.md
  robots.txt
  whats-new.md
engineering-team/  (35 files)
  .claude-plugin/  (1 files)
    plugin.json
  .codex/  (1 files)
    instructions.md
  a11y-audit/  (19 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    skills/  (16 files)
      … 16 files under this directory
    README.md
    settings.json
  google-workspace-cli/  (10 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    skills/  (8 files)
      … 8 files under this directory
    .gitignore
  CLAUDE.md
  README.md
  START_HERE.md
  TEAM_STRUCTURE_GUIDE.md
.gitignore
.mcp.json
.yamllintignore
CLAUDE.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
CONVENTIONS.md
GEMINI.md
INSTALLATION.md
LICENSE
README.md
SECURITY.md
SKILL-AUTHORING-STANDARD.md
SKILL_PIPELINE.md
STORE.md
VERIFIED.md
```

## Entry points

- [agent-launcher/hooks/session_end.py:56](https://github.com/alirezarezvani/claude-skills/blob/08cd8a9fc86cc370e2c0d448e8171fbcfdbc5a30/agent-launcher/hooks/session_end.py#L56)
- [agent-launcher/hooks/session_start.py:82](https://github.com/alirezarezvani/claude-skills/blob/08cd8a9fc86cc370e2c0d448e8171fbcfdbc5a30/agent-launcher/hooks/session_start.py#L82)
- [agent-launcher/skills/agent-launcher-orchestrator/scripts/goal_router.py:170](https://github.com/alirezarezvani/claude-skills/blob/08cd8a9fc86cc370e2c0d448e8171fbcfdbc5a30/agent-launcher/skills/agent-launcher-orchestrator/scripts/goal_router.py#L170)
- [agent-launcher/skills/agent-launcher-orchestrator/scripts/goal_state.py:222](https://github.com/alirezarezvani/claude-skills/blob/08cd8a9fc86cc370e2c0d448e8171fbcfdbc5a30/agent-launcher/skills/agent-launcher-orchestrator/scripts/goal_state.py#L222)
- [agent-launcher/skills/agent-launcher-orchestrator/scripts/loop_compiler.py:183](https://github.com/alirezarezvani/claude-skills/blob/08cd8a9fc86cc370e2c0d448e8171fbcfdbc5a30/agent-launcher/skills/agent-launcher-orchestrator/scripts/loop_compiler.py#L183)
- [agent-launcher/skills/grade-iterate/scripts/eval_scaffold.py:91](https://github.com/alirezarezvani/claude-skills/blob/08cd8a9fc86cc370e2c0d448e8171fbcfdbc5a30/agent-launcher/skills/grade-iterate/scripts/eval_scaffold.py#L91)
- [agent-launcher/skills/grade-iterate/scripts/outcome_builder.py:101](https://github.com/alirezarezvani/claude-skills/blob/08cd8a9fc86cc370e2c0d448e8171fbcfdbc5a30/agent-launcher/skills/grade-iterate/scripts/outcome_builder.py#L101)
- [agent-launcher/skills/grade-iterate/scripts/verdict_reader.py:108](https://github.com/alirezarezvani/claude-skills/blob/08cd8a9fc86cc370e2c0d448e8171fbcfdbc5a30/agent-launcher/skills/grade-iterate/scripts/verdict_reader.py#L108)
- [agent-launcher/skills/interview/scripts/build_sheet_builder.py:94](https://github.com/alirezarezvani/claude-skills/blob/08cd8a9fc86cc370e2c0d448e8171fbcfdbc5a30/agent-launcher/skills/interview/scripts/build_sheet_builder.py#L94)
- [agent-launcher/skills/interview/scripts/interview_planner.py:200](https://github.com/alirezarezvani/claude-skills/blob/08cd8a9fc86cc370e2c0d448e8171fbcfdbc5a30/agent-launcher/skills/interview/scripts/interview_planner.py#L200)
- [agent-launcher/skills/interview/scripts/primitives_validator.py:177](https://github.com/alirezarezvani/claude-skills/blob/08cd8a9fc86cc370e2c0d448e8171fbcfdbc5a30/agent-launcher/skills/interview/scripts/primitives_validator.py#L177)
- [agent-launcher/skills/run-without-you/scripts/cron_validator.py:133](https://github.com/alirezarezvani/claude-skills/blob/08cd8a9fc86cc370e2c0d448e8171fbcfdbc5a30/agent-launcher/skills/run-without-you/scripts/cron_validator.py#L133)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 40 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| engineering-team package | library | Observed | Groups 1 file(s) under engineering-team package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 136 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: ActionItem, Announcement, AuditResult, BandDefinition, CalendarReport, CalendarTouchpoin… |

## Important files

- `.claude-plugin/marketplace.json` (config)
- `.claude/settings.json` (config)
- `.codex-plugin/plugin.json` (config)
- `.codex/skills-index.json` (config)
- `.gemini/skills-index.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/branch-protection-config.json` (config)
- `.github/workflows/ci-quality-gate.yml` (ci)
- `.github/workflows/claude-code-review.yml` (ci)
- `.github/workflows/claude.yml` (ci)
- `.github/workflows/docs-preview.yml` (ci)
- `.github/workflows/enforce-pr-target.yml` (ci)
- `.github/workflows/harness-compat.yml` (ci)
- `.github/workflows/hero-sync.yml` (ci)
- `.github/workflows/pr-issue-auto-close.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/skill-evals.yml` (ci)
- `.github/workflows/skill-quality-review.yml` (ci)
- `.github/workflows/skill-security-audit.yml` (ci)
- `.github/workflows/smart-sync.yml` (ci)
- `.github/workflows/static.yml` (ci)
- `.github/workflows/sync-codex-skills.yml` (ci)
- `.github/workflows/traffic-snapshot.yml` (ci)
- `.github/workflows/trigger-gate.yml` (ci)
- `.github/workflows/virustotal-scan.yml` (ci)
- `.hermes/skills/claude-skills/skills-index.json` (config)
- `.mcp.json` (config)
- `.vibe/skills/claude-skills/skills-index.json` (config)
- `agent-launcher/.claude-plugin/authoring-notes.json` (config)
- `agent-launcher/.claude-plugin/plugin.json` (config)
- `agent-launcher/assets/build-sheet.schema.json` (config)
- `agent-launcher/assets/example-build-sheet.json` (config)
- `agent-launcher/hooks/hooks.json` (config)
- `audit/verified-tier/trigger_results.json` (config)
- `business-growth/.claude-plugin/plugin.json` (config)
- `business-growth/skills/customer-success-manager/assets/expected_output.json` (config)
- `business-growth/skills/customer-success-manager/assets/sample_customer_data.json` (config)
- `business-growth/skills/revenue-operations/assets/expected_output.json` (config)
- `business-growth/skills/revenue-operations/assets/sample_forecast_data.json` (config)
- `business-growth/skills/revenue-operations/assets/sample_gtm_data.json` (config)
- `business-growth/skills/revenue-operations/assets/sample_pipeline_data.json` (config)
- `business-growth/skills/sales-engineer/assets/expected_output.json` (config)
- `business-growth/skills/sales-engineer/assets/sample_rfp_data.json` (config)
- `business-operations/.claude-plugin/authoring-notes.json` (config)
- `business-operations/.claude-plugin/plugin.json` (config)
- `c-level-advisor/.claude-plugin/plugin.json` (config)
- `c-level-advisor/arquiteto-de-empresa/.claude-plugin/plugin.json` (config)
- `c-level-advisor/chief-ai-officer-advisor/.claude-plugin/plugin.json` (config)
- `c-level-advisor/chief-customer-officer-advisor/.claude-plugin/plugin.json` (config)
- `c-level-advisor/chief-data-officer-advisor/.claude-plugin/plugin.json` (config)
- `c-level-advisor/executive-mentor/.claude-plugin/plugin.json` (config)
- `c-level-advisor/general-counsel-advisor/.claude-plugin/plugin.json` (config)
- `c-level-advisor/hooks/hooks.json` (config)
- `c-level-advisor/hooks/skill_routes.json` (config)
- `c-level-advisor/vpe-advisor/.claude-plugin/plugin.json` (config)
- `c-level-agents/.claude-plugin/plugin.json` (config)
- `commercial/.claude-plugin/authoring-notes.json` (config)
- `commercial/.claude-plugin/plugin.json` (config)
- `compliance-os/.claude-plugin/plugin.json` (config)
- `compliance-os/skills/compliance-os/assets/company_profile_template.json` (config)
- `compliance-os/skills/compliance-os/assets/control_library_template.json` (config)
- `compliance-os/skills/compliance-os/assets/mock_audit_library.json` (config)
- `engineering-team/.claude-plugin/plugin.json` (config)
- `engineering-team/a11y-audit/.claude-plugin/plugin.json` (config)
- `engineering-team/a11y-audit/settings.json` (config)
- `engineering-team/a11y-audit/skills/a11y-audit/expected_outputs/sample-scan-output.json` (config)
- `engineering-team/google-workspace-cli/.claude-plugin/plugin.json` (config)
- `engineering-team/google-workspace-cli/skills/google-workspace-cli/assets/workspace-config.json` (config)

## Top-level layout

- `c-level-advisor` — 249 analysed file(s)
- `commercial` — 71 analysed file(s)
- `business-operations` — 63 analysed file(s)
- `agent-launcher` — 60 analysed file(s)
- `business-growth` — 44 analysed file(s)
- `commands` — 40 analysed file(s)
- `c-level-agents` — 39 analysed file(s)
- `agents` — 38 analysed file(s)
- `engineering-team` — 35 analysed file(s)
- `audit` — 34 analysed file(s)
- `compliance-os` — 32 analysed file(s)
- `.github` — 30 analysed file(s)
- `docs` — 29 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `.claude` — 13 analysed file(s)
- `.claude-plugin` — 1 analysed file(s)
- `.codex` — 1 analysed file(s)
- `.codex-plugin` — 1 analysed file(s)
- `.gemini` — 1 analysed file(s)
- `.hermes` — 1 analysed file(s)
- `.vibe` — 1 analysed file(s)
- `custom-gpt` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `08cd8a9fc86cc370e2c0d448e8171fbcfdbc5a30` is the revision these paths and observations refer to.
