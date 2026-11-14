# Project structure: muratcankoylan/Agent-Skills-for-Context-Engineering

**Analysed commit:** `9ff0c99108b36d3b886defd825d8ac1f47dba374`

**Commit reference:** [9ff0c99108b36d3b886defd825d8ac1f47dba374](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/commit/9ff0c99108b36d3b886defd825d8ac1f47dba374)

**Tree at this commit:** [muratcankoylan/Agent-Skills-for-Context-Engineering@9ff0c99108b3](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/9ff0c99108b36d3b886defd825d8ac1f47dba374)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | muratcankoylan/Agent-Skills-for-Context-Engineering |
| Description | A comprehensive collection of Agent Skills for context engineering, multi-agent architectures, and production agent systems. Use when building, optimizing, or debugging agent systems that require effective context management. |
| Stars | 18345 |
| Forks | 1512 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `9ff0c99108b36d3b886defd825d8ac1f47dba374` |
| Retrieved at | 2026-11-14T19:08:24.830114+00:00 |
| Files in this snapshot | 486 |

## Directory tree

```text
.claude-plugin/  (1 files)
  marketplace.json
.github/  (3 files)
  PULL_REQUEST_TEMPLATE/  (1 files)
    constitution-amendment.md
  workflows/  (2 files)
    deploy-prompt-lab.yml
    validate.yml
.plugin/  (1 files)
  plugin.json
assets/  (4 files)
  release/  (4 files)
    v2.3.0/  (4 files)
      … 4 files under this directory
docs/  (18 files)
  decisions/  (5 files)
    0001-machine-testable-constitution.md
    0002-derived-corpus-inventory.md
    0003-allowlisted-public-projections.md
    0004-runtime-neutral-artifact-contracts.md
    README.md
  specs/  (4 files)
    SPEC-000-program-constitution.md
    SPEC-001-repository-reconciliation.md
    SPEC-002-public-private-boundary.md
    SPEC-003-schema-registry.md
  agentskills.md
  blogs.md
  claude_research.md
  compression.md
  gemini_research.md
  hncapsule.md
  netflix_context.md
  skills-improvement-analysis.md
  vercel_tool.md
examples/  (202 files)
  book-sft-pipeline/  (10 files)
    examples/  (4 files)
      … 4 files under this directory
    references/  (3 files)
      … 3 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    README.md
    SKILL.md
  digital-brain-skill/  (47 files)
    agents/  (5 files)
      … 5 files under this directory
    content/  (8 files)
      … 8 files under this directory
    examples/  (2 files)
      … 2 files under this directory
    identity/  (7 files)
      … 7 files under this directory
    knowledge/  (5 files)
      … 5 files under this directory
    network/  (5 files)
      … 5 files under this directory
    operations/  (6 files)
      … 6 files under this directory
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    .gitignore
    AGENT.md
    HOW-SKILLS-BUILT-THIS.md
    README.md
    SKILL.md
    SKILLS-MAPPING.md
    package.json
  interleaved-thinking/  (63 files)
    docs/  (3 files)
      … 3 files under this directory
    examples/  (3 files)
      … 3 files under this directory
    generated_skills/  (4 files)
      … 4 files under this directory
    optimization_artifacts/  (40 files)
      … 40 files under this directory
    reasoning_trace_optimizer/  (8 files)
      … 8 files under this directory
    tests/  (2 files)
      … 2 files under this directory
    README.md
    SKILL.md
    pyproject.toml
  llm-as-judge-skills/  (45 files)
    agents/  (4 files)
      … 4 files under this directory
    examples/  (4 files)
      … 4 files under this directory
    prompts/  (5 files)
      … 5 files under this directory
    skills/  (4 files)
      … 4 files under this directory
    src/  (8 files)
      … 8 files under this directory
    tests/  (3 files)
      … 3 files under this directory
    tools/  (7 files)
      … 7 files under this directory
    .gitignore
    .prettierrc
    CONTRIBUTING.md
    LICENSE
    README.md
    env.example
    eslint.config.js
    package.json
    tsconfig.json
    vitest.config.ts
  long-horizon-prompt-lab/  (34 files)
    data/  (1 files)
      … 1 files under this directory
    report/  (3 files)
      … 3 files under this directory
    scripts/  (7 files)
      … 7 files under this directory
    ui/  (20 files)
      … 20 files under this directory
    .gitignore
    README.md
    package.json
  x-to-book-system/  (3 files)
    PRD.md
    README.md
    SKILLS-MAPPING.md
governance/  (7 files)
  fixtures/  (1 files)
    authority-decisions.jsonl
  generated/  (1 files)
    authority-table.md
  README.md
  authority.schema.json
  constitution.yaml
  export-policy.schema.json
  export-policy.yaml
researcher/  (176 files)
  artifacts/  (1 files)
    README.md
  benchmarks/  (23 files)
    effectiveness/  (6 files)
      … 6 files under this directory
    goldens/  (1 files)
      … 1 files under this directory
    router/  (7 files)
      … 7 files under this directory
    scenarios/  (1 files)
      … 1 files under this directory
    sdk-runner/  (6 files)
      … 6 files under this directory
    PLAN.md
    README.md
  claims/  (2 files)
    README.md
    index.jsonl
  corpus/  (4 files)
    index.json
    inventory.json
    inventory.schema.json
    reconciliation-report.md
  discovery/  (1 files)
    manual-seed.jsonl
  exports/  (5 files)
    examples/  (3 files)
      … 3 files under this directory
    schemas/  (1 files)
      … 1 files under this directory
    README.md
  fixtures/  (7 files)
    export/  (3 files)
      … 3 files under this directory
    skill-proposals/  (1 files)
      … 1 files under this directory
    source-evaluations/  (2 files)
      … 2 files under this directory
    activation-cases.jsonl
  generated/  (1 files)
    corpus-summary.md
  insights/  (2 files)
    auto-research-experiment.md
    how-we-built-this.md
  mechanisms/  (4 files)
    ledgers/  (2 files)
      … 2 files under this directory
    README.md
    registry.jsonl
  orchestration/  (9 files)
    launchd/  (8 files)
      … 8 files under this directory
    config.json
  queue/  (1 files)
    README.md
  reports/  (1 files)
    benchmark-history.jsonl
  rubrics/  (4 files)
    content-curation.md
    harness-change.md
    pairwise-skill-revision.md
    skill-change.md
  runbooks/  (6 files)
    autonomous-research-loop.md
    continuous-operation.md
    governance-amendment.md
    pr-readiness.md
    public-export-correction.md
    schema-migration.md
  runs/  (11 files)
    20260515-035228-executable-autonomous-research-frameworks/  (10 files)
      … 10 files under this directory
    README.md
  schemas/  (54 files)
    fixtures/  (23 files)
      … 23 files under this directory
    generated/  (4 files)
      … 4 files under this directory
    typescript/  (12 files)
      … 12 files under this directory
    v1/  (11 files)
      … 11 files under this directory
    README.md
    public-legacy-sources.json
    registry.json
    registry.schema.json
  scripts/  (32 files)
    tests/  (7 files)
      … 7 files under this directory
    artifact_store.py
    build_inventory.py
    check_activation_cases.py
    compare_skill_revisions.py
    export_policy.py
    governance_policy.py
    loop_common.py
    loop_daily.py
    loop_discover.py
    loop_status.py
    loop_step.py
    migrate_legacy.py
    novelty_check.py
    render_router_report.py
    research_loop.py
    run_benchmarks.py
    schema_contract.py
    skill_frontmatter.py
    skill_health.py
    validate_export.py
    validate_governance.py
    validate_platform_compat.py
    validate_repo.py
    validate_run.py
    … 1 more files
  templates/  (4 files)
    mechanism-proposal.jsonl
    research-thread.md
    skill-proposal.md
    source-evaluation.json
  README.md
  example_output.md
  llm-as-a-judge.md
  source-registry.md
skills/  (61 files)
  advanced-evaluation/  (6 files)
    references/  (4 files)
      … 4 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    SKILL.md
  bdi-mental-states/  (5 files)
    references/  (4 files)
      … 4 files under this directory
    SKILL.md
  context-compression/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    tests/  (1 files)
      … 1 files under this directory
    SKILL.md
  context-degradation/  (3 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    SKILL.md
  context-fundamentals/  (3 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    SKILL.md
  context-optimization/  (3 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    SKILL.md
  evaluation/  (3 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    SKILL.md
  filesystem-context/  (3 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    SKILL.md
  harness-engineering/  (1 files)
    SKILL.md
  hosted-agents/  (3 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    SKILL.md
  latent-briefing/  (2 files)
    references/  (1 files)
      … 1 files under this directory
    SKILL.md
  long-horizon-prompting/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  memory-systems/  (3 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    SKILL.md
  multi-agent-patterns/  (3 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    SKILL.md
  project-development/  (4 files)
    references/  (2 files)
      … 2 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    SKILL.md
  self-improvement-loops/  (2 files)
    references/  (1 files)
      … 1 files under this directory
    SKILL.md
  self-managed-context/  (3 files)
    references/  (2 files)
      … 2 files under this directory
    SKILL.md
  tool-design/  (4 files)
    references/  (2 files)
      … 2 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    SKILL.md
template/  (3 files)
  references/  (2 files)
    reference-file.md
    topic-details.md
  SKILL.md
.cursorindexingignore
.gitignore
AGENTS.md
CHANGELOG.md
CLAUDE.md
CONTRIBUTING.md
LICENSE
README.md
SKILL.md
requirements-dev.txt
```

## Entry points

- [researcher/scripts/build_inventory.py:1224](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/9ff0c99108b36d3b886defd825d8ac1f47dba374/researcher/scripts/build_inventory.py#L1224)
- [researcher/scripts/check_activation_cases.py:144](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/9ff0c99108b36d3b886defd825d8ac1f47dba374/researcher/scripts/check_activation_cases.py#L144)
- [researcher/scripts/compare_skill_revisions.py:114](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/9ff0c99108b36d3b886defd825d8ac1f47dba374/researcher/scripts/compare_skill_revisions.py#L114)
- [researcher/scripts/loop_daily.py:217](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/9ff0c99108b36d3b886defd825d8ac1f47dba374/researcher/scripts/loop_daily.py#L217)
- [researcher/scripts/loop_discover.py:164](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/9ff0c99108b36d3b886defd825d8ac1f47dba374/researcher/scripts/loop_discover.py#L164)
- [researcher/scripts/loop_status.py:166](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/9ff0c99108b36d3b886defd825d8ac1f47dba374/researcher/scripts/loop_status.py#L166)
- [researcher/scripts/loop_step.py:423](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/9ff0c99108b36d3b886defd825d8ac1f47dba374/researcher/scripts/loop_step.py#L423)
- [researcher/scripts/migrate_legacy.py:454](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/9ff0c99108b36d3b886defd825d8ac1f47dba374/researcher/scripts/migrate_legacy.py#L454)
- [researcher/scripts/novelty_check.py:275](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/9ff0c99108b36d3b886defd825d8ac1f47dba374/researcher/scripts/novelty_check.py#L275)
- [researcher/scripts/render_router_report.py:402](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/9ff0c99108b36d3b886defd825d8ac1f47dba374/researcher/scripts/render_router_report.py#L402)
- [researcher/scripts/research_loop.py:696](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/9ff0c99108b36d3b886defd825d8ac1f47dba374/researcher/scripts/research_loop.py#L696)
- [researcher/scripts/run_benchmarks.py:141](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/9ff0c99108b36d3b886defd825d8ac1f47dba374/researcher/scripts/run_benchmarks.py#L141)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 67 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 31 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: AgentCommunication, AgentEvaluator, AgentFailureHandler, AgentMessage, AgentPlan, AgentSe… |
| researcher package | library | Observed | Groups 22 file(s) under researcher package (observed from repository paths and static analysis). Observed top-level classes: ArtifactAuthority, BlobRef, CandidateFreezer, Constitution, ConstitutionError, ContractError.… |
| Tests | test | Observed | Groups 16 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: ArtifactStoreTests, CandidateFreezeTests, CanonicalizationTests, CapabilityTests, CompressionEvaluatorTests… |

## Important files

- `.claude-plugin/marketplace.json` (config)
- `.github/workflows/deploy-prompt-lab.yml` (ci)
- `.github/workflows/validate.yml` (ci)
- `.plugin/plugin.json` (config)
- `examples/book-sft-pipeline/examples/gertrude-stein/training_config.json` (config)
- `examples/digital-brain-skill/identity/values.yaml` (config)
- `examples/digital-brain-skill/knowledge/learning.yaml` (config)
- `examples/digital-brain-skill/network/circles.yaml` (config)
- `examples/digital-brain-skill/operations/goals.yaml` (config)
- `examples/digital-brain-skill/package.json` (manifest)
- `examples/interleaved-thinking/generated_skills/comprehensive-research-agent/references/optimization_summary.json` (config)
- `examples/interleaved-thinking/generated_skills/comprehensive-research-agent/references/patterns_found.json` (config)
- `examples/interleaved-thinking/optimization_artifacts/summary.json` (config)
- `examples/interleaved-thinking/pyproject.toml` (manifest)
- `examples/llm-as-judge-skills/package.json` (manifest)
- `examples/llm-as-judge-skills/tsconfig.json` (config)
- `examples/long-horizon-prompt-lab/data/prompt-pairs.json` (config)
- `examples/long-horizon-prompt-lab/package.json` (manifest)
- `governance/authority.schema.json` (config)
- `governance/constitution.yaml` (config)
- `governance/export-policy.schema.json` (config)
- `governance/export-policy.yaml` (config)
- `requirements-dev.txt` (manifest)
- `researcher/benchmarks/effectiveness/tasks/001-filesystem-context-offload/metadata.json` (config)
- `researcher/benchmarks/goldens/adversarial-goldens.json` (config)
- `researcher/benchmarks/sdk-runner/package.json` (manifest)
- `researcher/benchmarks/sdk-runner/tsconfig.json` (config)
- `researcher/corpus/index.json` (config)
- `researcher/corpus/inventory.json` (config)
- `researcher/corpus/inventory.schema.json` (config)
- `researcher/exports/examples/restricted-citation-v1/citation/restricted-fixture.json` (config)
- `researcher/exports/examples/restricted-citation-v1/export-manifest.json` (config)
- `researcher/exports/schemas/export-records.schema.json` (config)
- `researcher/fixtures/export/private-root/restricted-source.json` (config)
- `researcher/fixtures/export/restricted-request.json` (config)
- `researcher/fixtures/source-evaluations/approved-harness-source.json` (config)
- `researcher/fixtures/source-evaluations/rejected-generic-source.json` (config)
- `researcher/orchestration/config.json` (config)
- `researcher/runs/20260515-035228-executable-autonomous-research-frameworks/reports/closure.json` (config)
- `researcher/runs/20260515-035228-executable-autonomous-research-frameworks/reports/validation-report.json` (config)
- `researcher/runs/20260515-035228-executable-autonomous-research-frameworks/run-state.json` (config)
- `researcher/runs/20260515-035228-executable-autonomous-research-frameworks/sources/evaluations/source-evaluation-draft.json` (config)
- `researcher/schemas/fixtures/canonicalization-v1.json` (config)
- `researcher/schemas/fixtures/editable-surface-policy-v1.json` (config)
- `researcher/schemas/fixtures/records/artifact-envelope.json` (config)
- `researcher/schemas/fixtures/records/artifact-ref.json` (config)
- `researcher/schemas/fixtures/records/candidate-artifact.json` (config)
- `researcher/schemas/fixtures/records/capability-grant-spec.json` (config)
- `researcher/schemas/fixtures/records/credential-ref.json` (config)
- `researcher/schemas/fixtures/records/export-approval.json` (config)
- `researcher/schemas/fixtures/records/export-correction.json` (config)
- `researcher/schemas/fixtures/records/export-manifest.json` (config)
- `researcher/schemas/fixtures/records/export-plan.json` (config)
- `researcher/schemas/fixtures/records/export-receipt.json` (config)
- `researcher/schemas/fixtures/records/export-render-receipt.json` (config)
- `researcher/schemas/fixtures/records/export-request.json` (config)
- `researcher/schemas/fixtures/records/export-validation.json` (config)
- `researcher/schemas/fixtures/records/freeze-receipt-utf16.json` (config)
- `researcher/schemas/fixtures/records/freeze-receipt.json` (config)
- `researcher/schemas/fixtures/records/legacy-claim.json` (config)
- `researcher/schemas/fixtures/records/legacy-mechanism.json` (config)
- `researcher/schemas/fixtures/records/legacy-queue-record.json` (config)
- `researcher/schemas/fixtures/records/legacy-run-state.json` (config)
- `researcher/schemas/fixtures/records/schema-registry.json` (config)
- `researcher/schemas/fixtures/records/storage-binding.json` (config)
- `researcher/schemas/generated/conformance-report.json` (config)
- `researcher/schemas/generated/current-artifacts-report.json` (config)
- `researcher/schemas/generated/migration-dry-run.json` (config)
- `researcher/schemas/public-legacy-sources.json` (config)
- `researcher/schemas/registry.json` (config)
- `researcher/schemas/registry.schema.json` (config)
- `researcher/schemas/typescript/package.json` (manifest)
- `researcher/schemas/typescript/tsconfig.json` (config)
- `researcher/schemas/v1/artifact-envelope.schema.json` (config)
- `researcher/schemas/v1/artifact-ref.schema.json` (config)
- `researcher/schemas/v1/candidate-artifact.schema.json` (config)
- `researcher/schemas/v1/capability-grant-spec.schema.json` (config)
- `researcher/schemas/v1/credential-ref.schema.json` (config)
- `researcher/schemas/v1/freeze-receipt.schema.json` (config)
- `researcher/schemas/v1/legacy-claim.schema.json` (config)
- `researcher/schemas/v1/legacy-mechanism.schema.json` (config)
- `researcher/schemas/v1/legacy-queue-record.schema.json` (config)
- `researcher/schemas/v1/legacy-run-state.schema.json` (config)
- `researcher/schemas/v1/storage-binding.schema.json` (config)
- `researcher/templates/source-evaluation.json` (config)

## Top-level layout

- `examples` — 202 analysed file(s)
- `researcher` — 176 analysed file(s)
- `skills` — 61 analysed file(s)
- `docs` — 18 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `governance` — 7 analysed file(s)
- `assets` — 4 analysed file(s)
- `.github` — 3 analysed file(s)
- `template` — 3 analysed file(s)
- `.claude-plugin` — 1 analysed file(s)
- `.plugin` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 3 file(s) were skipped during inventory (3 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `9ff0c99108b36d3b886defd825d8ac1f47dba374` is the revision these paths and observations refer to.
