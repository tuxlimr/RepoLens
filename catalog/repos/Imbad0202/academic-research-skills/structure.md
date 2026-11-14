# Project structure: Imbad0202/academic-research-skills

**Analysed commit:** `ac42fc3a8635e143a6c3363f5c7132df1b6b0567`

**Commit reference:** [ac42fc3a8635e143a6c3363f5c7132df1b6b0567](https://github.com/Imbad0202/academic-research-skills/commit/ac42fc3a8635e143a6c3363f5c7132df1b6b0567)

**Tree at this commit:** [Imbad0202/academic-research-skills@ac42fc3a8635](https://github.com/Imbad0202/academic-research-skills/tree/ac42fc3a8635e143a6c3363f5c7132df1b6b0567)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Imbad0202/academic-research-skills |
| Description | Academic Research Skills for Claude Code: research → write → review → revise → finalize |
| Stars | 56882 |
| Forks | 4338 |
| Licence | Other |
| Language | Python |
| Default branch | main |
| Analysed commit | `ac42fc3a8635e143a6c3363f5c7132df1b6b0567` |
| Retrieved at | 2026-11-14T19:06:29.065569+00:00 |
| Files in this snapshot | 384 |

## Directory tree

```text
.claude/  (2 files)
  CHANGELOG.md
  CLAUDE.md
.claude-plugin/  (2 files)
  marketplace.json
  plugin.json
.github/  (17 files)
  workflows/  (14 files)
    changelog-covers-merges.yml
    command-invariants.yml
    defer-label-gate.yml
    eval-harness.yml
    freshness-check.yml
    harness-retirement-monthly.yml
    platform-port-reminder.yml
    pr-closes-issue.yml
    pytest.yml
    release-cooldown.yml
    repository-hygiene.yml
    spec-consistency.yml
    tag-version-match.yml
    test-count-monotonic.yml
  FUNDING.yml
  copilot-instructions.md
  pull_request_template.md
academic-paper/  (63 files)
  agents/  (12 files)
    abstract_bilingual_agent.md
    argument_builder_agent.md
    citation_compliance_agent.md
    draft_writer_agent.md
    formatter_agent.md
    intake_agent.md
    literature_strategist_agent.md
    peer_reviewer_agent.md
    revision_coach_agent.md
    socratic_mentor_agent.md
    structure_architect_agent.md
    visualization_agent.md
  examples/  (10 files)
    chinese_paper_example.md
    clinical_citation_verification_checklist.md
    clinical_epistemic_status_example.md
    commitment_ledger_example.md
    imrad_hei_example.md
    literature_review_example.md
    plan_mode_guided_writing.md
    revision_mode_example.md
    revision_recovery_example.md
    version_family_reconciliation_example.md
  references/  (29 files)
    abstract_writing_guide.md
    academic_writing_style.md
    anti_leakage_protocol.md
    apa7_chinese_citation_guide.md
    apa7_extended_guide.md
    changelog.md
    citation_format_switcher.md
    committee_correspondence_protocol.md
    credit_authorship_guide.md
    disclosure_mode_protocol.md
    domain_evidence_profiles.md
    failure_paths.md
    funding_statement_guide.md
    hei_domain_glossary.md
    intro_title_rhetoric_guide.md
    journal_submission_guide.md
    latex_template_reference.md
    mode_selection_guide.md
    paper_structure_patterns.md
    plan_mode_protocol.md
    policy_anchor_disclosure_protocol.md
    policy_anchor_table.md
    revision_patch_protocol.md
    statistical_visualization_standards.md
    … 5 more files
  templates/  (11 files)
    bilingual_abstract_template.md
    case_study_template.md
    conference_paper_template.md
    credit_statement_template.md
    funding_statement_template.md
    imrad_template.md
    latex_article_template.tex
    literature_review_template.md
    policy_brief_template.md
    revision_tracking_template.md
    theoretical_paper_template.md
  SKILL.md
academic-paper-reviewer/  (29 files)
  agents/  (7 files)
    devils_advocate_reviewer_agent.md
    domain_reviewer_agent.md
    editorial_synthesizer_agent.md
    eic_agent.md
    field_analyst_agent.md
    methodology_reviewer_agent.md
    perspective_reviewer_agent.md
  examples/  (3 files)
    hei_paper_review_example.md
    interdisciplinary_review_example.md
    subclaim_decomposition_example.md
  references/  (14 files)
    calibration_mode_protocol.md
    changelog.md
    editorial_decision_standards.md
    guided_mode_protocol.md
    integration_guide.md
    quality_rubrics.md
    re_review_mode_protocol.md
    review_criteria_framework.md
    review_panel_provenance_protocol.md
    review_quality_thinking.md
    reviewer_sprint_prompt_source.md
    sprint_contract_protocol.md
    statistical_reporting_standards.md
    top_journals_by_field.md
  templates/  (4 files)
    author_letter_template.md
    editorial_decision_template.md
    peer_review_report_template.md
    revision_response_template.md
  SKILL.md
academic-pipeline/  (30 files)
  agents/  (5 files)
    claim_ref_alignment_audit_agent.md
    collaboration_depth_agent.md
    integrity_verification_agent.md
    pipeline_orchestrator_agent.md
    state_tracker_agent.md
  examples/  (3 files)
    full_pipeline_example.md
    integrity_failure_recovery.md
    mid_entry_example.md
  references/  (20 files)
    adapters/  (2 files)
      … 2 files under this directory
    ai_research_failure_modes.md
    changelog.md
    claim_audit_calibration_protocol.md
    claim_verification_protocol.md
    external_review_protocol.md
    integrity_review_protocol.md
    literature_corpus_consumers.md
    mode_advisor.md
    passport_as_reset_boundary.md
    pipeline_state_machine.md
    plagiarism_detection_protocol.md
    process_summary_protocol.md
    progress_dashboard_template.md
    reinforcement_content.md
    reproducibility_audit.md
    score_trajectory_protocol.md
    team_collaboration_protocol.md
    two_stage_review_protocol.md
  templates/  (1 files)
    pipeline_status_template.md
  SKILL.md
agents/  (4 files)
  report_compiler_agent.md
  research_architect_agent.md
  screening_reviewer_agent.md
  synthesis_agent.md
audits/  (18 files)
  575-scope-closure-audit-2026-08-24.md
  575-source-backed-proving-set-2026-08-24.md
  684-expert-readiness-2026-08-24.md
  ars-researcher-blindspot-audit-2026-06-10.md
  bakeoff-gpt-5-6-sol-codex-2026-08-19.md
  external-contribution-audit-prompt.md
  harness-retirement-2026-06-10.md
  harness-retirement-2026-07-04.md
  harness-retirement-2026-07.md
  harness-retirement-2026-08.md
  harness-retirement-2026-09-model-update.md
  harness-retirement-2026-09-opus-5-5.md
  harness-retirement-2026-09.md
  harness-retirement-2026-11-fable-5-2.md
  harness-retirement-2026-11.md
  iso42001-spirit-gap-assessment-2026-08-17.md
  rq-advisory-505-exemption-sharpening-2026-07-11.md
  rq-advisory-heldout-measurement-2026-07-11.md
commands/  (16 files)
  ars-3w.md
  ars-abstract.md
  ars-cache-invalidate.md
  ars-citation-check.md
  ars-disclosure.md
  ars-format-convert.md
  ars-full.md
  ars-lit-review.md
  ars-mark-read.md
  ars-outline.md
  ars-plan.md
  ars-rebuttal-audit.md
  ars-reviewer.md
  ars-revision-coach.md
  ars-revision.md
  ars-unmark-read.md
deep-research/  (53 files)
  agents/  (14 files)
    bibliography_agent.md
    devils_advocate_agent.md
    editor_in_chief_agent.md
    ethics_review_agent.md
    meta_analysis_agent.md
    monitoring_agent.md
    report_compiler_agent.md
    research_architect_agent.md
    research_question_agent.md
    risk_of_bias_agent.md
    socratic_mentor_agent.md
    source_verification_agent.md
    synthesis_agent.md
    timeline_extraction_agent.md
  examples/  (8 files)
    exploratory_research.md
    fact_check_mode.md
    handoff_to_paper.md
    idea_diversity_coverage_gap_advisory.md
    policy_analysis.md
    review_mode.md
    socratic_guided_research.md
    systematic_review.md
  references/  (24 files)
    apa7_style_guide.md
    argumentation_reasoning_framework.md
    arxiv_api_protocol.md
    changelog.md
    chinese_literature_api_protocol.md
    cross_agent_quality_definitions.md
    crossref_api_protocol.md
    equator_reporting_guidelines.md
    ethics_checklist.md
    failure_paths.md
    interdisciplinary_bridges.md
    irb_decision_tree.md
    literature_monitoring_strategies.md
    logical_fallacies.md
    methodology_patterns.md
    mode_selection_guide.md
    openalex_api_protocol.md
    preregistration_guide.md
    semantic_scholar_api_protocol.md
    socratic_mode_protocol.md
    socratic_questioning_framework.md
    source_quality_hierarchy.md
    systematic_review_protocol.md
    systematic_review_toolkit.md
  templates/  (6 files)
    evidence_assessment_template.md
    literature_matrix_template.md
    preregistration_template.md
    prisma_protocol_template.md
    prisma_report_template.md
    research_brief_template.md
  SKILL.md
docs/  (119 files)
  changelog-archive/  (5 files)
    es-ES.md
    ja-JP.md
    ko-KR.md
    zh-CN.md
    zh-TW.md
  design/  (102 files)
    snapshots/  (1 files)
      … 1 files under this directory
    2026-04-20-v3.4-prisma-trAIce-raise-readcheck-design.md
    2026-04-22-ars-v3.7.3-reading-check-probe-design.md
    2026-04-23-ars-v3.6.2-sprint-contract-design.md
    2026-04-23-ars-v3.6.4-literature-corpus-adapters-design.md
    2026-04-23-ars-v3.6.4-literature-corpus-adapters-plan.md
    2026-04-26-ars-v3.6.5-consumer-integration-design.md
    2026-04-27-ars-v3.6.5.1-setup-fix-implementation-brief.md
    2026-04-27-ars-v3.6.5.2-claude-ai-method-4a-scope-implementation-brief.md
    2026-04-27-ars-v3.6.6-generator-evaluator-contract-design.md
    2026-04-29-ars-v3.6.7-downstream-agent-pattern-protection-spec.md
    2026-04-30-ars-v3.6.8-trust-provenance-and-drift-transparency-spec.md
    2026-04-30-ars-v3.7.0-plugin-packaging-roadmap.md
    2026-05-05-phase-6.6-scoping-note.md
    2026-05-10-ars-v3.7.2-trust-provenance-hardening-spec.md
    2026-05-12-ars-v3.7.3-claim-faithfulness-and-contaminated-source-spec.md
    2026-05-13-ai-disclosure-schema-discovery.md
    2026-05-14-ai-disclosure-impl-spec.md
    2026-05-14-ai-disclosure-schema-decision.md
    2026-05-15-issue-103-claim-alignment-audit-decision.md
    2026-05-15-issue-103-claim-alignment-audit-spec.md
    2026-05-15-issue-105-contamination-signals-backfill-design.md
    2026-05-15-issue-111-slr-lineage-emission-design.md
    2026-05-17-ars-v3.9.0-cross-index-triangulation-measurement-spec.md
    2026-05-18-ars-v3.9.2-agent-phase-classification.md
    … 77 more files
  ARCHITECTURE.md
  CONTROL_AVAILABILITY.md
  DATA_FLOWS.md
  PERFORMANCE.md
  PERFORMANCE.zh-TW.md
  RISK_REGISTER.md
  ROADMAP-v3.11.md
  ROADMAP-v3.20.1-v3.22.md
  SETUP.md
  SETUP.zh-TW.md
  STAGE_CAPABILITY_MATRIX.md
  cross-paper-workflow.md
evals/  (6 files)
  gold/  (1 files)
    citation_extraction/  (1 files)
      … 1 files under this directory
  heldout/  (4 files)
    reviewer_calibration/  (2 files)
      … 2 files under this directory
    reviewer_seeded_defects/  (2 files)
      … 2 files under this directory
  README.md
scripts/  (3 files)
  adapters/  (3 files)
    examples/  (2 files)
      … 2 files under this directory
    tests/  (1 files)
      … 1 files under this directory
.command-invariants.toml
.gitattributes
.gitignore
.gitleaks.toml
.gitleaksignore
CITATION.cff
CONTRIBUTING.md
GOVERNANCE.md
LICENSE
MODE_REGISTRY.md
NOTICE.md
POSITIONING.md
QUICKSTART.md
README.es-ES.md
README.ja-JP.md
README.ko-KR.md
README.md
README.pt-BR.md
README.zh-CN.md
README.zh-TW.md
SECURITY.md
THIRD_PARTY.md
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.claude-plugin/marketplace.json` (config)
- `.claude-plugin/plugin.json` (config)
- `.command-invariants.toml` (config)
- `.github/FUNDING.yml` (config)
- `.github/workflows/changelog-covers-merges.yml` (ci)
- `.github/workflows/command-invariants.yml` (ci)
- `.github/workflows/defer-label-gate.yml` (ci)
- `.github/workflows/eval-harness.yml` (ci)
- `.github/workflows/freshness-check.yml` (ci)
- `.github/workflows/harness-retirement-monthly.yml` (ci)
- `.github/workflows/platform-port-reminder.yml` (ci)
- `.github/workflows/pr-closes-issue.yml` (ci)
- `.github/workflows/pytest.yml` (ci)
- `.github/workflows/release-cooldown.yml` (ci)
- `.github/workflows/repository-hygiene.yml` (ci)
- `.github/workflows/spec-consistency.yml` (ci)
- `.github/workflows/tag-version-match.yml` (ci)
- `.github/workflows/test-count-monotonic.yml` (ci)
- `.gitleaks.toml` (config)
- `docs/design/snapshots/2026-05-13-ai-disclosure-discovery/manifest.yaml` (config)
- `evals/gold/citation_extraction/manifest.yaml` (config)
- `evals/heldout/reviewer_calibration/runs/raw/contamination_probe/probe_AOUa1Ae9qg.json` (config)

## Top-level layout

- `docs` — 119 analysed file(s)
- `academic-paper` — 63 analysed file(s)
- `deep-research` — 53 analysed file(s)
- `academic-pipeline` — 30 analysed file(s)
- `academic-paper-reviewer` — 29 analysed file(s)
- `(root files)` — 22 analysed file(s)
- `audits` — 18 analysed file(s)
- `.github` — 17 analysed file(s)
- `commands` — 16 analysed file(s)
- `evals` — 6 analysed file(s)
- `agents` — 4 analysed file(s)
- `scripts` — 3 analysed file(s)
- `.claude` — 2 analysed file(s)
- `.claude-plugin` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `ac42fc3a8635e143a6c3363f5c7132df1b6b0567` is the revision these paths and observations refer to.
