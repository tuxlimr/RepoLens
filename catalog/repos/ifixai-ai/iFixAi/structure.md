# Project structure: ifixai-ai/iFixAi

**Analysed commit:** `8fe4e893f921cd48088fd959f2616d6989fabee5`

**Commit reference:** [8fe4e893f921cd48088fd959f2616d6989fabee5](https://github.com/ifixai-ai/iFixAi/commit/8fe4e893f921cd48088fd959f2616d6989fabee5)

**Tree at this commit:** [ifixai-ai/iFixAi@8fe4e893f921](https://github.com/ifixai-ai/iFixAi/tree/8fe4e893f921cd48088fd959f2616d6989fabee5)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | ifixai-ai/iFixAi |
| Description | Independent Auditing of AI Agents. Run by human or the agent itself, to answer the most crucial question in the AI Agent Economy. Is the agent doing what is supposed to do? With iFixAi you can have this answer in less than 120 seconds. |
| Stars | 45472 |
| Forks | 1794 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `8fe4e893f921cd48088fd959f2616d6989fabee5` |
| Retrieved at | 2026-11-14T19:06:38.027620+00:00 |
| Files in this snapshot | 782 |

## Directory tree

```text
.agents/  (1 files)
  plugins/  (1 files)
    marketplace.json
.claude-plugin/  (1 files)
  marketplace.json
.github/  (7 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (4 files)
    ci.yml
    release.yml
    self-check-smoke.yml
    traction.yaml
  CODEOWNERS
actions/  (1 files)
  self-check/  (1 files)
    action.yml
case_studies/  (4 files)
  aisi-cyber-range-containment/  (1 files)
    SCORECARD.md
  meta-instagram-support/  (1 files)
    SCORECARD.md
  openai-huggingface-containment/  (1 files)
    SCORECARD.md
  pizza-hut-dragontail/  (1 files)
    SCORECARD.md
ci/  (1 files)
  gitlab/  (1 files)
    ifixai-self-check.gitlab-ci.yml
docs/  (30 files)
  assets/  (13 files)
    brand/  (11 files)
      … 11 files under this directory
    pypi_stats_history.json
    runs_history.json
  README.md
  business-policy-lab.md
  cli.md
  fixture_authoring.md
  get-started.md
  inspections.md
  methodology.md
  python-api.md
  reproducibility.md
  scoring.md
  self-check.md
  testing-your-agent.md
  trace-intake.md
  traction.md
  trajectory-assurance.md
  what-we-test.md
  wind-tunnel.md
examples/  (2 files)
  business_policy_lab.py
  trajectory_assurance.py
ifixai/  (723 files)
  cli/  (25 files)
    __init__.py
    _branding.py
    audit.py
    author.py
    compare.py
    config_file.py
    init.py
    inspection_seeds.py
    judge_estimate.py
    list_cmd.py
    main.py
    model_catalog.py
    orchestrator.py
    policy_lab.py
    pro_offer.py
    reports.py
    run.py
    scaffold.py
    schemas.py
    setup_cmd.py
    traces.py
    trajectory.py
    ui.py
    validate.py
    … 1 more files
  core/  (14 files)
    __init__.py
    applicability.py
    concurrency.py
    connection.py
    context.py
    discovery.py
    fixture_loader.py
    governance_synthesis.py
    grounding.py
    profile.py
    refusal.py
    runner.py
    training_specification_screening.py
    types.py
  evaluation/  (15 files)
    __init__.py
    analytic_judge.py
    analytic_judge_schema.py
    atomic_claims.py
    checkpoint.py
    errors.py
    manifest.py
    normalizer.py
    pipeline.py
    proportion_ci.py
    purpose_check.py
    response_classifier.py
    run_stop.py
    schemas.py
    types.py
  fixtures/  (19 files)
    default/  (2 files)
      … 2 files under this directory
    examples/  (11 files)
      … 11 files under this directory
    governance/  (1 files)
      … 1 files under this directory
    reference/  (2 files)
      … 2 files under this directory
    README.md
    schema.json
    smoke_tiny.yaml
  harness/  (11 files)
    __init__.py
    adversarial_mutator.py
    base.py
    completeness.py
    consistency.py
    injection_corpus.py
    prompt_pool.py
    registry.py
    suites.py
    synonyms.yaml
    validator.py
  inspections/  (404 files)
    b01_tool_governance/  (4 files)
      … 4 files under this directory
    b02_non_llm_layer/  (4 files)
      … 4 files under this directory
    b03_auditability/  (4 files)
      … 4 files under this directory
    b04_deterministic_override/  (4 files)
      … 4 files under this directory
    b05_source_provenance/  (4 files)
      … 4 files under this directory
    b06_uncertainty_signalling/  (4 files)
      … 4 files under this directory
    b07_hallucination_rate/  (4 files)
      … 4 files under this directory
    b08_privilege_escalation/  (4 files)
      … 4 files under this directory
    b09_policy_violation/  (4 files)
      … 4 files under this directory
    b10_evaluation_drift/  (4 files)
      … 4 files under this directory
    b11_system_controllability/  (5 files)
      … 5 files under this directory
    b12_prompt_injection/  (5 files)
      … 5 files under this directory
    b13_plan_traceability/  (4 files)
      … 4 files under this directory
    b14_covert_side_task/  (5 files)
      … 5 files under this directory
    b15_long_horizon_drift/  (4 files)
      … 4 files under this directory
    b16_silent_failure/  (5 files)
      … 5 files under this directory
    b17_fact_consistency/  (4 files)
      … 4 files under this directory
    b18_goal_stability/  (6 files)
      … 6 files under this directory
    b19_context_accuracy/  (4 files)
      … 4 files under this directory
    b20_instruction_adherence/  (4 files)
      … 4 files under this directory
    b21_cross_turn_objective/  (5 files)
      … 5 files under this directory
    b22_decision_reproducibility/  (5 files)
      … 5 files under this directory
    b23_policy_version_trace/  (4 files)
      … 4 files under this directory
    b24_risk_scoring/  (4 files)
      … 4 files under this directory
    b25_regulatory_readiness/  (5 files)
      … 5 files under this directory
    b26_rate_limiting/  (4 files)
      … 4 files under this directory
    b27_session_integrity/  (4 files)
      … 4 files under this directory
    b28_rag_context_integrity/  (6 files)
      … 6 files under this directory
    b29_prompt_sensitivity/  (5 files)
      … 5 files under this directory
    b30_malicious_deployer_rules/  (5 files)
      … 5 files under this directory
    b31_escalation_correctness/  (4 files)
      … 4 files under this directory
    b32_off_topic_detection/  (6 files)
      … 6 files under this directory
    c02_low_confidence_abstention/  (4 files)
      … 4 files under this directory
    c05_human_fallback_routing/  (4 files)
      … 4 files under this directory
    c11_operational_outcome_conformance/  (4 files)
      … 4 files under this directory
    m02_standing_authority_revalidation/  (4 files)
      … 4 files under this directory
    m03_finetune_corpus_contamination/  (4 files)
      … 4 files under this directory
    m06_model_identity_attestation/  (4 files)
      … 4 files under this directory
    m07_cross_org_delegation_scope/  (6 files)
      … 6 files under this directory
    m12_end_user_dependency_cultivation/  (7 files)
      … 7 files under this directory
    p01_destruction_resistance/  (4 files)
      … 4 files under this directory
    p08_self_audit_trail_integrity/  (4 files)
      … 4 files under this directory
    p13_hidden_side_objective_persistence/  (5 files)
      … 5 files under this directory
    p19_honeypot_tool_restraint/  (5 files)
      … 5 files under this directory
    p22_goal_edit_acceptance/  (5 files)
      … 5 files under this directory
    p27_privilege_creep/  (5 files)
      … 5 files under this directory
    p32_emergent_systemic_harm/  (5 files)
      … 5 files under this directory
    s02_configurer_stakeholder_conflict/  (5 files)
      … 5 files under this directory
    v01_overcorrection_check/  (12 files)
      … 12 files under this directory
    v02_agreement_integrity/  (14 files)
      … 14 files under this directory
    v03_warranted_persistence/  (14 files)
      … 14 files under this directory
    v04_honesty_source_attribution/  (13 files)
      … 13 files under this directory
    v05_grader_independence/  (16 files)
      … 16 files under this directory
    v06_flattery_classification_validity/  (15 files)
      … 15 files under this directory
    v07_benchmark_contamination_check/  (18 files)
      … 18 files under this directory
    v08_training_misuse_guardrail/  (15 files)
      … 15 files under this directory
    v09_prompt_override_resistance/  (20 files)
      … 20 files under this directory
    v10_care_under_vulnerability/  (13 files)
      … 13 files under this directory
    v11_guilt_tripping/  (14 files)
      … 14 files under this directory
    x04_detection_performance_gate/  (4 files)
      … 4 files under this directory
    x11_pre_action_confirmation_gate/  (4 files)
      … 4 files under this directory
    __init__.py
    catalogue_guards.py
    conformance_probe.py
    dimension_majority.py
    dimension_reads.py
    fanout.py
    holdout_ids.py
    judge_consensus.py
    judge_probe.py
    policy_grounding.py
    probe_context.py
    probe_pack.py
    structural_probe.py
    user_selection.py
  judge/  (6 files)
    __init__.py
    config.py
    evaluator.py
    fallbacks.py
    judge_fallbacks.json
    preflight.py
  mappings/  (6 files)
    __init__.py
    eu_ai_act.yaml
    iso_42001.yaml
    loader.py
    nist_ai_rmf.yaml
    owasp_llm_top10.yaml
  observability/  (2 files)
    __init__.py
    logging.py
  policy_lab/  (7 files)
    __init__.py
    executor.py
    fixture.py
    integrity.py
    models.py
    repair.py
    search.py
  providers/  (25 files)
    __init__.py
    anthropic.py
    atlascloud.py
    azure.py
    base.py
    bedrock.py
    client_pool.py
    cloudflare.py
    gemini.py
    governance_fixture.py
    governance_mixin.py
    http.py
    huggingface.py
    langchain.py
    litellm.py
    minimax.py
    mock_governance.py
    openai.py
    openrouter.py
    orcarouter.py
    requesty.py
    resolver.py
    schemas.py
    secrets.py
    … 1 more files
  reporting/  (12 files)
    __init__.py
    artifact.py
    comparison.py
    gap_analysis.py
    grading.py
    health.py
    judge_votes.py
    policy_lab.py
    rates.py
    regulatory.py
    scorecard.py
    trajectory.py
  rules/  (2 files)
    __init__.py
    loader.py
  scaffold/  (1 files)
    playbook.md
  schemas/  (5 files)
    __init__.py
    corpus.schema.json
    definition.schema.json
    references.schema.json
    rubric.schema.json
  scoring/  (6 files)
    __init__.py
    category_weights.py
    engine.py
    mandatory_minimums.py
    schemas.py
    unscored_pass.py
  selfcheck/  (7 files)
    __init__.py
    comment.py
    explain.py
    mcp_server.py
    regressions.py
    result.py
    sarif.py
  shared/  (7 files)
    __init__.py
    authorized_scope.py
    coverage.py
    domain_scope.py
    evidence.py
    holdout.py
    template_vars.py
  tests/  (142 files)
    core/  (12 files)
      … 12 files under this directory
    evaluation/  (14 files)
      … 14 files under this directory
    fixtures/  (20 files)
      … 20 files under this directory
    policy_lab/  (11 files)
      … 11 files under this directory
    providers/  (15 files)
      … 15 files under this directory
    selfcheck/  (7 files)
      … 7 files under this directory
    trace_intake/  (1 files)
      … 1 files under this directory
    windtunnel/  (1 files)
      … 1 files under this directory
    test_added_artifact_legacy_resume.py
    test_analytic_judge_verdict_booleans.py
    test_anthropic_endpoint_capabilities.py
    test_anthropic_judge_cutoff_native.py
    test_anthropic_system_message_preservation.py
    test_anthropic_temperature_native.py
    test_anthropic_transient_backoff_native.py
    test_artifact_diff_unscored.py
    test_artifact_historical_unscored.py
    test_artifact_overall_summary.py
    test_artifact_private_fields.py
    test_atomic_budget_health.py
    test_atomic_claim_boolean_contract.py
    test_atomic_duplicate_claims.py
    test_atomic_judge_text_boolean_http.py
    test_author.py
    test_authorized_scope_explicit_deny.py
    test_authorized_scope_role_identity.py
    test_b01_evidence_floor_diagnostics.py
    test_b08_b17_ci_population.py
    test_b11_unanswered_prompt_inconclusive.py
    test_b12_replay_seed.py
    test_b13_timestamp_validation.py
    test_b14_user_identifiers.py
    … 37 more files
  utils/  (1 files)
    __init__.py
  __init__.py
  _version.py
  api.py
  py.typed
  quick_build.py
  telemetry.py
.gitattributes
.gitignore
.pre-commit-config.yaml
.pre-commit-hooks.yaml
CONTRIBUTING.md
LICENSE
README.ja.md
README.ko.md
README.md
README.zh-CN.md
SECURITY.md
conftest.py
```

## Entry points

- [ifixai/cli/audit.py:226](https://github.com/ifixai-ai/iFixAi/blob/8fe4e893f921cd48088fd959f2616d6989fabee5/ifixai/cli/audit.py#L226)
- [ifixai/cli/author.py:53](https://github.com/ifixai-ai/iFixAi/blob/8fe4e893f921cd48088fd959f2616d6989fabee5/ifixai/cli/author.py#L53)
- [ifixai/cli/compare.py:22](https://github.com/ifixai-ai/iFixAi/blob/8fe4e893f921cd48088fd959f2616d6989fabee5/ifixai/cli/compare.py#L22)
- [ifixai/cli/init.py:114](https://github.com/ifixai-ai/iFixAi/blob/8fe4e893f921cd48088fd959f2616d6989fabee5/ifixai/cli/init.py#L114)
- [ifixai/cli/list_cmd.py:16](https://github.com/ifixai-ai/iFixAi/blob/8fe4e893f921cd48088fd959f2616d6989fabee5/ifixai/cli/list_cmd.py#L16)
- [ifixai/cli/main.py:26](https://github.com/ifixai-ai/iFixAi/blob/8fe4e893f921cd48088fd959f2616d6989fabee5/ifixai/cli/main.py#L26)
- [ifixai/cli/policy_lab.py:87](https://github.com/ifixai-ai/iFixAi/blob/8fe4e893f921cd48088fd959f2616d6989fabee5/ifixai/cli/policy_lab.py#L87)
- [ifixai/cli/run.py:933](https://github.com/ifixai-ai/iFixAi/blob/8fe4e893f921cd48088fd959f2616d6989fabee5/ifixai/cli/run.py#L933)
- [ifixai/cli/scaffold.py:221](https://github.com/ifixai-ai/iFixAi/blob/8fe4e893f921cd48088fd959f2616d6989fabee5/ifixai/cli/scaffold.py#L221)
- [ifixai/cli/setup_cmd.py:142](https://github.com/ifixai-ai/iFixAi/blob/8fe4e893f921cd48088fd959f2616d6989fabee5/ifixai/cli/setup_cmd.py#L142)
- [ifixai/cli/traces.py:14](https://github.com/ifixai-ai/iFixAi/blob/8fe4e893f921cd48088fd959f2616d6989fabee5/ifixai/cli/traces.py#L14)
- [ifixai/cli/trajectory.py:41](https://github.com/ifixai-ai/iFixAi/blob/8fe4e893f921cd48088fd959f2616d6989fabee5/ifixai/cli/trajectory.py#L41)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 230 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: JudgeConfig, JudgeProviderSpec. |
| Data layer | data | Observed | Groups 7 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: ActionContract, Actor, ArmDecisions, BudgetRule, BusinessGoal, BusinessModel. Observed top-level functi… |
| Application entry point | entrypoint | Observed | Groups 3 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Group. Observed top-level classes: _CleanFormatter. Observed top-level functio… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| ifixai package | library | Observed | Groups 325 file(s) under ifixai package (observed from repository paths and static analysis). Observed top-level classes: ActionObservation, ActivationProbe, ActorTemplateVars, AdversarialMutatorError, AgentReply, Agent… |
| Service / domain layer | service | Observed | Groups 14 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: Abilities, ActionConfirmationRequest, ActivationAuthorityReport, ActivationAuthorityVerdic… |
| Tests | test | Observed | Groups 143 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: AcceptsAnyTemperature, AtomicJudge, BrowserRecorder, CallCounter, CancelledMenu, CannedReply. Observed top… |

## Important files

- `.agents/plugins/marketplace.json` (config)
- `.claude-plugin/marketplace.json` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/self-check-smoke.yml` (ci)
- `.github/workflows/traction.yaml` (ci)
- `.pre-commit-config.yaml` (config)
- `.pre-commit-hooks.yaml` (config)
- `actions/self-check/action.yml` (config)
- `ci/gitlab/ifixai-self-check.gitlab-ci.yml` (config)
- `docs/assets/pypi_stats_history.json` (config)
- `docs/assets/runs_history.json` (config)
- `ifixai/fixtures/default/fixture.yaml` (config)
- `ifixai/fixtures/examples/acme_legal.yaml` (config)
- `ifixai/fixtures/examples/customer_support.yaml` (config)
- `ifixai/fixtures/examples/healthcare.yaml` (config)
- `ifixai/fixtures/examples/helio_finance.yaml` (config)
- `ifixai/fixtures/examples/hermes_strict.yaml` (config)
- `ifixai/fixtures/examples/nimbusforge_it_infra.yaml` (config)
- `ifixai/fixtures/examples/openclaw_consolidated.yaml` (config)
- `ifixai/fixtures/examples/openclaw_moderate.yaml` (config)
- `ifixai/fixtures/examples/openclaw_strict.yaml` (config)
- `ifixai/fixtures/examples/openwebui.yaml` (config)
- `ifixai/fixtures/examples/software_engineering.yaml` (config)
- `ifixai/fixtures/governance/mock.yaml` (config)
- `ifixai/fixtures/reference/fixture.yaml` (config)
- `ifixai/fixtures/reference/profile.json` (config)
- `ifixai/fixtures/schema.json` (config)
- `ifixai/fixtures/smoke_tiny.yaml` (config)
- `ifixai/harness/synonyms.yaml` (config)
- `ifixai/inspections/b01_tool_governance/definition.yaml` (config)
- `ifixai/inspections/b01_tool_governance/probes.yaml` (config)
- `ifixai/inspections/b01_tool_governance/rubric.yaml` (config)
- `ifixai/inspections/b02_non_llm_layer/definition.yaml` (config)
- `ifixai/inspections/b02_non_llm_layer/probes.yaml` (config)
- `ifixai/inspections/b02_non_llm_layer/rubric.yaml` (config)
- `ifixai/inspections/b03_auditability/definition.yaml` (config)
- `ifixai/inspections/b03_auditability/references.yaml` (config)
- `ifixai/inspections/b03_auditability/rubric.yaml` (config)
- `ifixai/inspections/b04_deterministic_override/definition.yaml` (config)
- `ifixai/inspections/b04_deterministic_override/probes.yaml` (config)
- `ifixai/inspections/b04_deterministic_override/rubric.yaml` (config)
- `ifixai/inspections/b05_source_provenance/definition.yaml` (config)
- `ifixai/inspections/b05_source_provenance/references.yaml` (config)
- `ifixai/inspections/b05_source_provenance/rubric.yaml` (config)
- `ifixai/inspections/b06_uncertainty_signalling/definition.yaml` (config)
- `ifixai/inspections/b06_uncertainty_signalling/references.yaml` (config)
- `ifixai/inspections/b06_uncertainty_signalling/rubric.yaml` (config)
- `ifixai/inspections/b07_hallucination_rate/definition.yaml` (config)
- `ifixai/inspections/b07_hallucination_rate/references.yaml` (config)
- `ifixai/inspections/b07_hallucination_rate/rubric.yaml` (config)
- `ifixai/inspections/b08_privilege_escalation/definition.yaml` (config)
- `ifixai/inspections/b08_privilege_escalation/references.yaml` (config)
- `ifixai/inspections/b08_privilege_escalation/rubric.yaml` (config)
- `ifixai/inspections/b09_policy_violation/definition.yaml` (config)
- `ifixai/inspections/b09_policy_violation/references.yaml` (config)
- `ifixai/inspections/b09_policy_violation/rubric.yaml` (config)
- `ifixai/inspections/b10_evaluation_drift/definition.yaml` (config)
- `ifixai/inspections/b10_evaluation_drift/references.yaml` (config)
- `ifixai/inspections/b10_evaluation_drift/rubric.yaml` (config)
- `ifixai/inspections/b11_system_controllability/definition.yaml` (config)
- `ifixai/inspections/b11_system_controllability/references.yaml` (config)
- `ifixai/inspections/b11_system_controllability/rubric.yaml` (config)
- `ifixai/inspections/b12_prompt_injection/corpus.yaml` (config)
- `ifixai/inspections/b12_prompt_injection/definition.yaml` (config)
- `ifixai/inspections/b12_prompt_injection/references.yaml` (config)
- `ifixai/inspections/b12_prompt_injection/rubric.yaml` (config)
- `ifixai/inspections/b13_plan_traceability/definition.yaml` (config)
- `ifixai/inspections/b13_plan_traceability/references.yaml` (config)
- `ifixai/inspections/b13_plan_traceability/rubric.yaml` (config)
- `ifixai/inspections/b14_covert_side_task/corpus.yaml` (config)
- `ifixai/inspections/b14_covert_side_task/definition.yaml` (config)
- `ifixai/inspections/b14_covert_side_task/references.yaml` (config)
- `ifixai/inspections/b14_covert_side_task/rubric.yaml` (config)
- `ifixai/inspections/b15_long_horizon_drift/definition.yaml` (config)
- `ifixai/inspections/b15_long_horizon_drift/references.yaml` (config)
- `ifixai/inspections/b15_long_horizon_drift/rubric.yaml` (config)
- `ifixai/inspections/b16_silent_failure/definition.yaml` (config)
- `ifixai/inspections/b16_silent_failure/prompts.yaml` (config)
- `ifixai/inspections/b16_silent_failure/references.yaml` (config)
- `ifixai/inspections/b16_silent_failure/rubric.yaml` (config)
- `ifixai/inspections/b17_fact_consistency/definition.yaml` (config)
- `ifixai/inspections/b17_fact_consistency/references.yaml` (config)
- `ifixai/inspections/b17_fact_consistency/rubric.yaml` (config)
- `ifixai/inspections/b18_goal_stability/definition.yaml` (config)
- `ifixai/inspections/b18_goal_stability/references.yaml` (config)
- `ifixai/inspections/b18_goal_stability/rubric.yaml` (config)
- `ifixai/inspections/b18_goal_stability/rubric_comply.yaml` (config)
- `ifixai/inspections/b18_goal_stability/rubric_step1.yaml` (config)
- `ifixai/inspections/b19_context_accuracy/definition.yaml` (config)
- `ifixai/inspections/b19_context_accuracy/references.yaml` (config)
- `ifixai/inspections/b19_context_accuracy/rubric.yaml` (config)
- `ifixai/inspections/b20_instruction_adherence/definition.yaml` (config)
- `ifixai/inspections/b20_instruction_adherence/references.yaml` (config)
- `ifixai/inspections/b20_instruction_adherence/rubric.yaml` (config)
- `ifixai/inspections/b21_cross_turn_objective/definition.yaml` (config)
- `ifixai/inspections/b21_cross_turn_objective/references.yaml` (config)
- `ifixai/inspections/b21_cross_turn_objective/rubric.yaml` (config)
- `ifixai/inspections/b21_cross_turn_objective/rubric_step1.yaml` (config)
- `ifixai/inspections/b22_decision_reproducibility/definition.yaml` (config)
- `ifixai/inspections/b22_decision_reproducibility/references.yaml` (config)
- `ifixai/inspections/b22_decision_reproducibility/rubric.yaml` (config)
- `ifixai/inspections/b23_policy_version_trace/definition.yaml` (config)
- `ifixai/inspections/b23_policy_version_trace/probes.yaml` (config)
- `ifixai/inspections/b23_policy_version_trace/rubric.yaml` (config)
- `ifixai/inspections/b24_risk_scoring/definition.yaml` (config)
- `ifixai/inspections/b24_risk_scoring/references.yaml` (config)
- `ifixai/inspections/b24_risk_scoring/rubric.yaml` (config)
- `ifixai/inspections/b25_regulatory_readiness/definition.yaml` (config)
- `ifixai/inspections/b25_regulatory_readiness/references.yaml` (config)
- `ifixai/inspections/b25_regulatory_readiness/rubric.yaml` (config)
- `ifixai/inspections/b26_rate_limiting/definition.yaml` (config)
- `ifixai/inspections/b26_rate_limiting/references.yaml` (config)
- `ifixai/inspections/b26_rate_limiting/rubric.yaml` (config)
- `ifixai/inspections/b27_session_integrity/definition.yaml` (config)
- `ifixai/inspections/b27_session_integrity/references.yaml` (config)
- `ifixai/inspections/b27_session_integrity/rubric.yaml` (config)
- `ifixai/inspections/b28_rag_context_integrity/corpus.yaml` (config)
- `ifixai/inspections/b28_rag_context_integrity/definition.yaml` (config)
- `ifixai/inspections/b28_rag_context_integrity/references.yaml` (config)
- `ifixai/inspections/b28_rag_context_integrity/rubric.yaml` (config)
- `ifixai/inspections/b28_rag_context_integrity/rubric_comply.yaml` (config)
- `ifixai/inspections/b29_prompt_sensitivity/definition.yaml` (config)
- `ifixai/inspections/b29_prompt_sensitivity/prompts.yaml` (config)
- `ifixai/inspections/b29_prompt_sensitivity/references.yaml` (config)
- `ifixai/inspections/b29_prompt_sensitivity/rubric.yaml` (config)
- `ifixai/inspections/b30_malicious_deployer_rules/corpus.yaml` (config)
- `ifixai/inspections/b30_malicious_deployer_rules/definition.yaml` (config)
- `ifixai/inspections/b30_malicious_deployer_rules/references.yaml` (config)
- `ifixai/inspections/b30_malicious_deployer_rules/rubric.yaml` (config)
- `ifixai/inspections/b31_escalation_correctness/definition.yaml` (config)
- `ifixai/inspections/b31_escalation_correctness/references.yaml` (config)
- `ifixai/inspections/b31_escalation_correctness/rubric.yaml` (config)
- `ifixai/inspections/b32_off_topic_detection/definition.yaml` (config)
- `ifixai/inspections/b32_off_topic_detection/on_topic_prompts.yaml` (config)
- `ifixai/inspections/b32_off_topic_detection/prompts.yaml` (config)
- `ifixai/inspections/b32_off_topic_detection/references.yaml` (config)
- `ifixai/inspections/b32_off_topic_detection/rubric.yaml` (config)
- `ifixai/inspections/c02_low_confidence_abstention/definition.yaml` (config)
- `ifixai/inspections/c02_low_confidence_abstention/probes.yaml` (config)
- `ifixai/inspections/c02_low_confidence_abstention/rubric.yaml` (config)
- `ifixai/inspections/c05_human_fallback_routing/definition.yaml` (config)
- `ifixai/inspections/c05_human_fallback_routing/probes.yaml` (config)
- `ifixai/inspections/c05_human_fallback_routing/rubric.yaml` (config)
- `ifixai/inspections/c11_operational_outcome_conformance/definition.yaml` (config)
- `ifixai/inspections/c11_operational_outcome_conformance/probes.yaml` (config)
- `ifixai/inspections/c11_operational_outcome_conformance/rubric.yaml` (config)
- `ifixai/inspections/m02_standing_authority_revalidation/definition.yaml` (config)
- `ifixai/inspections/m02_standing_authority_revalidation/probes.yaml` (config)
- `ifixai/inspections/m02_standing_authority_revalidation/rubric.yaml` (config)
- `ifixai/inspections/m03_finetune_corpus_contamination/definition.yaml` (config)
- `ifixai/inspections/m03_finetune_corpus_contamination/probes.yaml` (config)
- `ifixai/inspections/m03_finetune_corpus_contamination/rubric.yaml` (config)
- `ifixai/inspections/m06_model_identity_attestation/definition.yaml` (config)
- `ifixai/inspections/m07_cross_org_delegation_scope/definition.yaml` (config)
- `ifixai/inspections/m07_cross_org_delegation_scope/probes.yaml` (config)
- `ifixai/inspections/m07_cross_org_delegation_scope/rubric.yaml` (config)
- `ifixai/inspections/m12_end_user_dependency_cultivation/definition.yaml` (config)
- `ifixai/inspections/m12_end_user_dependency_cultivation/references.yaml` (config)
- `ifixai/inspections/m12_end_user_dependency_cultivation/rubric.yaml` (config)
- `ifixai/inspections/p01_destruction_resistance/definition.yaml` (config)
- `ifixai/inspections/p01_destruction_resistance/probes.yaml` (config)
- `ifixai/inspections/p01_destruction_resistance/rubric.yaml` (config)
- `ifixai/inspections/p08_self_audit_trail_integrity/definition.yaml` (config)
- `ifixai/inspections/p08_self_audit_trail_integrity/probes.yaml` (config)
- `ifixai/inspections/p08_self_audit_trail_integrity/rubric_keep_record.yaml` (config)
- `ifixai/inspections/p13_hidden_side_objective_persistence/corpus.yaml` (config)
- `ifixai/inspections/p13_hidden_side_objective_persistence/definition.yaml` (config)
- `ifixai/inspections/p13_hidden_side_objective_persistence/references.yaml` (config)
- `ifixai/inspections/p13_hidden_side_objective_persistence/rubric.yaml` (config)
- `ifixai/inspections/p19_honeypot_tool_restraint/corpus.yaml` (config)
- `ifixai/inspections/p19_honeypot_tool_restraint/definition.yaml` (config)
- `ifixai/inspections/p19_honeypot_tool_restraint/references.yaml` (config)
- `ifixai/inspections/p19_honeypot_tool_restraint/rubric.yaml` (config)
- `ifixai/inspections/p22_goal_edit_acceptance/corpus.yaml` (config)
- `ifixai/inspections/p22_goal_edit_acceptance/definition.yaml` (config)
- `ifixai/inspections/p22_goal_edit_acceptance/references.yaml` (config)
- `ifixai/inspections/p22_goal_edit_acceptance/rubric.yaml` (config)
- `ifixai/inspections/p27_privilege_creep/corpus.yaml` (config)
- `ifixai/inspections/p27_privilege_creep/definition.yaml` (config)
- `ifixai/inspections/p27_privilege_creep/references.yaml` (config)
- `ifixai/inspections/p27_privilege_creep/rubric.yaml` (config)
- `ifixai/inspections/p32_emergent_systemic_harm/corpus.yaml` (config)
- `ifixai/inspections/p32_emergent_systemic_harm/definition.yaml` (config)
- `ifixai/inspections/p32_emergent_systemic_harm/references.yaml` (config)
- `ifixai/inspections/p32_emergent_systemic_harm/rubric.yaml` (config)
- `ifixai/inspections/s02_configurer_stakeholder_conflict/corpus.yaml` (config)
- `ifixai/inspections/s02_configurer_stakeholder_conflict/definition.yaml` (config)
- `ifixai/inspections/s02_configurer_stakeholder_conflict/references.yaml` (config)
- `ifixai/inspections/s02_configurer_stakeholder_conflict/rubric.yaml` (config)
- `ifixai/inspections/v01_overcorrection_check/definition.yaml` (config)
- `ifixai/inspections/v01_overcorrection_check/references.yaml` (config)
- `ifixai/inspections/v01_overcorrection_check/rubric.yaml` (config)
- `ifixai/inspections/v02_agreement_integrity/definition.yaml` (config)
- `ifixai/inspections/v02_agreement_integrity/references.yaml` (config)
- `ifixai/inspections/v02_agreement_integrity/rubric.yaml` (config)
- `ifixai/inspections/v03_warranted_persistence/definition.yaml` (config)
- `ifixai/inspections/v03_warranted_persistence/references.yaml` (config)
- `ifixai/inspections/v03_warranted_persistence/rubric.yaml` (config)
- `ifixai/inspections/v04_honesty_source_attribution/definition.yaml` (config)
- `ifixai/inspections/v04_honesty_source_attribution/references.yaml` (config)
- `ifixai/inspections/v04_honesty_source_attribution/rubric.yaml` (config)
- `ifixai/inspections/v05_grader_independence/definition.yaml` (config)
- `ifixai/inspections/v05_grader_independence/references.yaml` (config)
- `ifixai/inspections/v05_grader_independence/rubric.yaml` (config)
- `ifixai/inspections/v06_flattery_classification_validity/definition.yaml` (config)
- `ifixai/inspections/v06_flattery_classification_validity/references.yaml` (config)
- `ifixai/inspections/v06_flattery_classification_validity/rubric.yaml` (config)
- `ifixai/inspections/v07_benchmark_contamination_check/definition.yaml` (config)
- `ifixai/inspections/v07_benchmark_contamination_check/references.yaml` (config)
- `ifixai/inspections/v07_benchmark_contamination_check/rubric.yaml` (config)
- `ifixai/inspections/v08_training_misuse_guardrail/definition.yaml` (config)
- `ifixai/inspections/v08_training_misuse_guardrail/probes.yaml` (config)
- `ifixai/inspections/v08_training_misuse_guardrail/rubric.yaml` (config)
- `ifixai/inspections/v08_training_misuse_guardrail/rubric_refuse.yaml` (config)
- `ifixai/inspections/v09_prompt_override_resistance/definition.yaml` (config)
- `ifixai/inspections/v09_prompt_override_resistance/references.yaml` (config)
- `ifixai/inspections/v09_prompt_override_resistance/rubric.yaml` (config)
- `ifixai/inspections/v10_care_under_vulnerability/definition.yaml` (config)
- `ifixai/inspections/v10_care_under_vulnerability/references.yaml` (config)
- `ifixai/inspections/v10_care_under_vulnerability/rubric.yaml` (config)
- `ifixai/inspections/v11_guilt_tripping/definition.yaml` (config)
- `ifixai/inspections/v11_guilt_tripping/references.yaml` (config)
- `ifixai/inspections/v11_guilt_tripping/rubric.yaml` (config)
- `ifixai/inspections/x04_detection_performance_gate/definition.yaml` (config)
- `ifixai/inspections/x04_detection_performance_gate/probes.yaml` (config)
- `ifixai/inspections/x04_detection_performance_gate/rubric.yaml` (config)
- `ifixai/inspections/x11_pre_action_confirmation_gate/definition.yaml` (config)
- `ifixai/inspections/x11_pre_action_confirmation_gate/probes.yaml` (config)
- `ifixai/inspections/x11_pre_action_confirmation_gate/rubric.yaml` (config)
- `ifixai/judge/judge_fallbacks.json` (config)
- `ifixai/mappings/eu_ai_act.yaml` (config)
- `ifixai/mappings/iso_42001.yaml` (config)
- `ifixai/mappings/nist_ai_rmf.yaml` (config)
- `ifixai/mappings/owasp_llm_top10.yaml` (config)
- `ifixai/schemas/corpus.schema.json` (config)
- `ifixai/schemas/definition.schema.json` (config)
- `ifixai/schemas/references.schema.json` (config)
- `ifixai/schemas/rubric.schema.json` (config)

## Top-level layout

- `ifixai` — 723 analysed file(s)
- `docs` — 30 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `.github` — 7 analysed file(s)
- `case_studies` — 4 analysed file(s)
- `examples` — 2 analysed file(s)
- `.agents` — 1 analysed file(s)
- `.claude-plugin` — 1 analysed file(s)
- `actions` — 1 analysed file(s)
- `ci` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `8fe4e893f921cd48088fd959f2616d6989fabee5` is the revision these paths and observations refer to.
