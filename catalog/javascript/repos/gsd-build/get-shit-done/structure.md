# Project structure: gsd-build/get-shit-done

**Analysed commit:** `bdcaab2c752d9a33a1a1ca9acf3a3c81fb991815`

**Commit reference:** [bdcaab2c752d9a33a1a1ca9acf3a3c81fb991815](https://github.com/gsd-build/get-shit-done/commit/bdcaab2c752d9a33a1a1ca9acf3a3c81fb991815)

**Tree at this commit:** [gsd-build/get-shit-done@bdcaab2c752d](https://github.com/gsd-build/get-shit-done/tree/bdcaab2c752d9a33a1a1ca9acf3a3c81fb991815)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | gsd-build/get-shit-done |
| Description | A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code by TÂCHES. |
| Stars | 64136 |
| Forks | 5451 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `bdcaab2c752d9a33a1a1ca9acf3a3c81fb991815` |
| Retrieved at | 2026-11-14T19:10:35.227408+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.changeset/  (294 files)
  2937-statusline-context-position.md
  3033-sdk-flag-wired.md
  3095-quota-failure-classification.md
  3156-plan-phase-opencode-dispatch.md
  3166-graphify-inline-build.md
  3170-graphify-commit-staleness.md
  3195-quick-resurrection-guard.md
  3198-retrospective-canonical.md
  3210-fallow-structural-review.md
  3251-non-family-aliases.md
  3262-extract-scan-phase-plans.md
  3271-sdk-adr-structure.md
  3298-phase-dir-prefix-drift-workflows.md
  3312-sdk-first-architecture-seams.md
  3346-codex-aot-toml-key.md
  3347-graphify-auto-update-hook.md
  3409-phase-remove-force-position.md
  3450-shell-projection-merge-repair.md
  3488-decimal-phase-depends-on.md
  3489-complete-phase-idempotent.md
  3491-nested-git-detection.md
  3493-extract-milestone-generic-heading.md
  3517-phase-complete-state-staleness.md
  3537-phase-regex-fanout.md
  … 270 more files
.githooks/  (2 files)
  pre-commit
  pre-push
.github/  (33 files)
  ISSUE_TEMPLATE/  (6 files)
    bug_report.yml
    chore.yml
    config.yml
    docs_issue.yml
    enhancement.yml
    feature_request.yml
  PULL_REQUEST_TEMPLATE/  (3 files)
    enhancement.md
    feature.md
    fix.md
  workflows/  (20 files)
    auto-branch.yml
    auto-close-deprecated.yml
    auto-label-issues.yml
    branch-cleanup.yml
    branch-naming.yml
    canary.yml
    changeset-required.yml
    close-draft-prs.yml
    dismiss-unauthorized-pr-approvals.yml
    docs-required.yml
    hotfix.yml
    install-smoke.yml
    pr-gate.yml
    pr-template-format.yml
    release-sdk.yml
    release.yml
    require-issue-link.yml
    security-scan.yml
    stale.yml
    test.yml
  CODEOWNERS
  FUNDING.yml
  dependabot.yml
  pull_request_template.md
.out-of-scope/  (2 files)
  agent-template-rendering.md
  temporal-context.md
.plans/  (1 files)
  1755-install-audit-fix.md
agents/  (33 files)
  gsd-advisor-researcher.md
  gsd-ai-researcher.md
  gsd-assumptions-analyzer.md
  gsd-code-fixer.md
  gsd-code-reviewer.md
  gsd-codebase-mapper.md
  gsd-debug-session-manager.md
  gsd-debugger.md
  gsd-doc-classifier.md
  gsd-doc-synthesizer.md
  gsd-doc-verifier.md
  gsd-doc-writer.md
  gsd-domain-researcher.md
  gsd-eval-auditor.md
  gsd-eval-planner.md
  gsd-executor.md
  gsd-framework-selector.md
  gsd-integration-checker.md
  gsd-intel-updater.md
  gsd-nyquist-auditor.md
  gsd-pattern-mapper.md
  gsd-phase-researcher.md
  gsd-plan-checker.md
  gsd-planner.md
  … 9 more files
assets/  (3 files)
  gsd-logo-2000-transparent.svg
  gsd-logo-2000.svg
  terminal.svg
bin/  (2 files)
  lib/  (1 files)
    ui-safety-gate.cjs
  gsd-sdk.js
commands/  (67 files)
  gsd/  (67 files)
    add-tests.md
    ai-integration-phase.md
    audit-fix.md
    audit-milestone.md
    audit-uat.md
    autonomous.md
    capture.md
    cleanup.md
    code-review.md
    complete-milestone.md
    config.md
    debug.md
    discuss-phase.md
    docs-update.md
    eval-review.md
    execute-phase.md
    explore.md
    extract-learnings.md
    fast.md
    forensics.md
    graphify.md
    health.md
    help.md
    import.md
    … 43 more files
docs/  (115 files)
  adr/  (18 files)
    0001-dispatch-policy-module.md
    0002-command-contract-validation-module.md
    0003-model-catalog-module.md
    0004-worktree-workstream-seam-module.md
    0005-sdk-architecture-seam-map.md
    0006-planning-path-projection-module.md
    0007-sdk-package-seam-module.md
    0008-installer-migration-module.md
    0009-shell-command-projection-module.md
    0010-file-operation-engine-module.md
    0010-skill-surface-budget-module.md
    0011-review-default-reviewers-prd.md
    0011-review-default-reviewers.md
    0011-skill-surface-budget-module.md
    0012-command-routing-hub.md
    3524-cjs-sdk-hard-seam.md
    3660-runtime-artifact-layout-module.md
    README.md
  agents/  (4 files)
    cjs-sdk-seam.md
    domain.md
    issue-tracker.md
    triage-labels.md
  discussions/  (1 files)
    grok-build-support-2026-05.md
  ja-JP/  (12 files)
    superpowers/  (2 files)
      … 2 files under this directory
    AGENTS.md
    ARCHITECTURE.md
    CLI-TOOLS.md
    COMMANDS.md
    CONFIGURATION.md
    FEATURES.md
    README.md
    USER-GUIDE.md
    context-monitor.md
    workflow-discuss-mode.md
  ko-KR/  (12 files)
    superpowers/  (2 files)
      … 2 files under this directory
    AGENTS.md
    ARCHITECTURE.md
    CLI-TOOLS.md
    COMMANDS.md
    CONFIGURATION.md
    FEATURES.md
    README.md
    USER-GUIDE.md
    context-monitor.md
    workflow-discuss-mode.md
  prd/  (2 files)
    3524-cjs-sdk-hard-seam.md
    README.md
  pt-BR/  (13 files)
    superpowers/  (3 files)
      … 3 files under this directory
    AGENTS.md
    ARCHITECTURE.md
    CLI-TOOLS.md
    COMMANDS.md
    CONFIGURATION.md
    FEATURES.md
    README.md
    USER-GUIDE.md
    context-monitor.md
    workflow-discuss-mode.md
  research/  (3 files)
    data/  (1 files)
      … 1 files under this directory
    2026-05-12-skill-surface-budget.md
    provider-rate-limit-signals.md
  skills/  (1 files)
    discovery-contract.md
  superpowers/  (1 files)
    specs/  (1 files)
      … 1 files under this directory
  zh-CN/  (15 files)
    references/  (13 files)
      … 13 files under this directory
    README.md
    USER-GUIDE.md
  AGENTS.md
  ARCHITECTURE.md
  BETA.md
  CANARY.md
  CLI-TOOLS.md
  COMMANDS.md
  CONFIGURATION.md
  FEATURES.md
  INVENTORY-MANIFEST.json
  INVENTORY.md
  README.md
  RELEASE-v1.39.0-rc.4.md
  RELEASE-v1.39.0-rc.5.md
  RELEASE-v1.39.0-rc.6.md
  RELEASE-v1.39.0-rc.7.md
  RELEASE-v1.40.0-rc.1.md
  RELEASE-v1.41.0.md
  RELEASE-v1.42.0-rc.1.md
  RELEASE-v1.42.1.md
  RELEASE-v1.42.3.md
  RELEASE-v1.50.0-canary.1.md
  STATE-MD-LIFECYCLE.md
  TESTING-SUITES.md
  USER-GUIDE.md
  … 9 more files
get-shit-done/  (228 files)
  bin/  (80 files)
    lib/  (77 files)
      … 77 files under this directory
    check-latest-version.cjs
    gsd-tools.cjs
    verify-reapply-patches.cjs
  contexts/  (3 files)
    dev.md
    research.md
    review.md
  references/  (63 files)
    few-shot-examples/  (2 files)
      … 2 files under this directory
    agent-contracts.md
    ai-evals.md
    ai-frameworks.md
    artifact-types.md
    autonomous-smart-discuss.md
    checkpoints.md
    common-bug-patterns.md
    context-budget.md
    continuation-format.md
    debugger-philosophy.md
    decimal-phase-calculation.md
    doc-conflict-engine.md
    domain-probes.md
    execute-mvp-tdd.md
    executor-examples.md
    gate-prompts.md
    gates.md
    git-integration.md
    git-planning-commit.md
    ios-scaffold.md
    mandatory-initial-read.md
    model-profile-resolution.md
    model-profiles.md
    mvp-concepts.md
    … 37 more files
  templates/  (46 files)
    codebase/  (7 files)
      … 7 files under this directory
    research-project/  (5 files)
      … 5 files under this directory
    AI-SPEC.md
    DEBUG.md
    README.md
    SECURITY.md
    UAT.md
    UI-SPEC.md
    VALIDATION.md
    claude-md.md
    config.json
    context.md
    continue-here.md
    copilot-instructions.md
    debug-subagent-prompt.md
    dev-preferences.md
    discovery.md
    discussion-log.md
    milestone-archive.md
    milestone.md
    phase-prompt.md
    planner-subagent-prompt.md
    project.md
    requirements.md
    research.md
    retrospective.md
    … 10 more files
  workflows/  (36 files)
    discuss-phase/  (12 files)
      … 12 files under this directory
    add-backlog.md
    add-phase.md
    add-tests.md
    add-todo.md
    ai-integration-phase.md
    analyze-dependencies.md
    audit-fix.md
    audit-milestone.md
    audit-uat.md
    autonomous.md
    check-todos.md
    cleanup.md
    code-review-fix.md
    code-review.md
    complete-milestone.md
    debug.md
    diagnose-issues.md
    discovery-phase.md
    discuss-phase-assumptions.md
    discuss-phase-power.md
    discuss-phase.md
    do.md
    docs-update.md
    edit-phase.md
.base64scanignore
.clinerules
.coderabbit.yaml
.gitignore
.release-monitor.sh
.secretscanignore
AGENTS.md
CHANGELOG.md
CONTEXT.md
CONTRIBUTING.md
LICENSE
QUICK-WINS-CONFIRMED-BUGS.md
README.ja-JP.md
README.ko-KR.md
README.md
README.pt-BR.md
README.zh-CN.md
SECURITY.md
TEST-EXAMPLES.md
VERSIONING.md
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bin package | library | Observed | Groups 2 file(s) under bin package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| get-shit-done package | library | Observed | Groups 80 file(s) under get-shit-done package (observed from repository paths and static analysis). |

## Important files

- `.coderabbit.yaml` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/chore.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/docs_issue.yml` (config)
- `.github/ISSUE_TEMPLATE/enhancement.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/auto-branch.yml` (ci)
- `.github/workflows/auto-close-deprecated.yml` (ci)
- `.github/workflows/auto-label-issues.yml` (ci)
- `.github/workflows/branch-cleanup.yml` (ci)
- `.github/workflows/branch-naming.yml` (ci)
- `.github/workflows/canary.yml` (ci)
- `.github/workflows/changeset-required.yml` (ci)
- `.github/workflows/close-draft-prs.yml` (ci)
- `.github/workflows/dismiss-unauthorized-pr-approvals.yml` (ci)
- `.github/workflows/docs-required.yml` (ci)
- `.github/workflows/hotfix.yml` (ci)
- `.github/workflows/install-smoke.yml` (ci)
- `.github/workflows/pr-gate.yml` (ci)
- `.github/workflows/pr-template-format.yml` (ci)
- `.github/workflows/release-sdk.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/require-issue-link.yml` (ci)
- `.github/workflows/security-scan.yml` (ci)
- `.github/workflows/stale.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `docs/INVENTORY-MANIFEST.json` (config)
- `docs/research/data/2026-05-12-skill-audit.json` (config)
- `get-shit-done/templates/config.json` (config)
- `get-shit-done/workflows/discuss-phase/templates/checkpoint.json` (config)

## Top-level layout

- `.changeset` — 294 analysed file(s)
- `get-shit-done` — 228 analysed file(s)
- `docs` — 115 analysed file(s)
- `commands` — 67 analysed file(s)
- `.github` — 33 analysed file(s)
- `agents` — 33 analysed file(s)
- `(root files)` — 20 analysed file(s)
- `assets` — 3 analysed file(s)
- `.githooks` — 2 analysed file(s)
- `.out-of-scope` — 2 analysed file(s)
- `bin` — 2 analysed file(s)
- `.plans` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `bdcaab2c752d9a33a1a1ca9acf3a3c81fb991815` is the revision these paths and observations refer to.
