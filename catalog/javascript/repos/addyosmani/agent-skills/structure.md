# Project structure: addyosmani/agent-skills

**Analysed commit:** `39b723ceebf81474d0557c1fecd01eddab585563`

**Commit reference:** [39b723ceebf81474d0557c1fecd01eddab585563](https://github.com/addyosmani/agent-skills/commit/39b723ceebf81474d0557c1fecd01eddab585563)

**Tree at this commit:** [addyosmani/agent-skills@39b723ceebf8](https://github.com/addyosmani/agent-skills/tree/39b723ceebf81474d0557c1fecd01eddab585563)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | addyosmani/agent-skills |
| Description | Production-grade engineering skills for AI coding agents. |
| Stars | 117506 |
| Forks | 12287 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `39b723ceebf81474d0557c1fecd01eddab585563` |
| Retrieved at | 2026-11-14T19:10:32.065408+00:00 |
| Files in this snapshot | 251 |

## Directory tree

```text
.agents/  (1 files)
  plugins/  (1 files)
    marketplace.json
.claude/  (10 files)
  commands/  (9 files)
    build.md
    code-simplify.md
    constraints.md
    plan.md
    review.md
    ship.md
    spec.md
    test.md
    webperf.md
  rules/  (1 files)
    skills-contributing.md
.claude-plugin/  (2 files)
  marketplace.json
  plugin.json
.codex-plugin/  (1 files)
  plugin.json
.gemini/  (9 files)
  commands/  (9 files)
    build.toml
    code-simplify.toml
    constraints.toml
    planning.toml
    review.toml
    ship.toml
    spec.toml
    test.toml
    webperf.toml
.github/  (2 files)
  ISSUE_TEMPLATE/  (1 files)
    skill-gap.yml
  workflows/  (1 files)
    test-plugin-install.yml
agents/  (4 files)
  code-reviewer.md
  security-auditor.md
  test-engineer.md
  web-performance-auditor.md
commands/  (9 files)
  build.toml
  code-simplify.toml
  constraints.toml
  planning.toml
  review.toml
  ship.toml
  spec.toml
  test.toml
  webperf.toml
docs/  (17 files)
  adoption-guide.md
  advanced-per-agent-configuration.md
  agents.md
  antigravity-setup.md
  codex-setup.md
  commandcode-setup.md
  comparison.md
  copilot-cli-setup.md
  copilot-setup.md
  cursor-setup.md
  developer-onboarding.md
  gemini-cli-setup.md
  getting-started.md
  opencode-setup.md
  other-hosts.md
  skill-anatomy.md
  windsurf-setup.md
evals/  (121 files)
  cases/  (25 files)
    api-and-interface-design.json
    browser-testing-with-devtools.json
    ci-cd-and-automation.json
    code-review-and-quality.json
    code-simplification.json
    constraint-driven-development.json
    context-engineering.json
    debugging-and-error-recovery.json
    deprecation-and-migration.json
    documentation-and-adrs.json
    doubt-driven-development.json
    frontend-ui-engineering.json
    git-workflow-and-versioning.json
    idea-refine.json
    incremental-implementation.json
    interview-me.json
    observability-and-instrumentation.json
    performance-optimization.json
    planning-and-task-breakdown.json
    security-and-hardening.json
    shipping-and-launch.json
    source-driven-development.json
    spec-driven-development.json
    test-driven-development.json
    … 1 more files
  fixtures/  (61 files)
    api-and-interface-design/  (1 files)
      … 1 files under this directory
    browser-testing-with-devtools/  (3 files)
      … 3 files under this directory
    ci-cd-and-automation/  (3 files)
      … 3 files under this directory
    code-review-and-quality/  (1 files)
      … 1 files under this directory
    code-simplification/  (2 files)
      … 2 files under this directory
    context-budget/  (1 files)
      … 1 files under this directory
    context-engineering/  (1 files)
      … 1 files under this directory
    debugging-and-error-recovery/  (3 files)
      … 3 files under this directory
    deprecation-and-migration/  (1 files)
      … 1 files under this directory
    documentation-and-adrs/  (5 files)
      … 5 files under this directory
    doubt-driven-development/  (1 files)
      … 1 files under this directory
    frontend-ui-engineering/  (2 files)
      … 2 files under this directory
    git-workflow-and-versioning/  (3 files)
      … 3 files under this directory
    incremental-implementation/  (3 files)
      … 3 files under this directory
    incremental-implementation-pressure/  (2 files)
      … 2 files under this directory
    observability-and-instrumentation/  (2 files)
      … 2 files under this directory
    performance-optimization/  (2 files)
      … 2 files under this directory
    planning-and-task-breakdown/  (1 files)
      … 1 files under this directory
    review-evidence/  (4 files)
      … 4 files under this directory
    security-and-hardening/  (2 files)
      … 2 files under this directory
    shipping-and-launch/  (2 files)
      … 2 files under this directory
    source-driven-development/  (1 files)
      … 1 files under this directory
    spec-driven-development/  (1 files)
      … 1 files under this directory
    spec-driven-development-decomposition/  (1 files)
      … 1 files under this directory
    test-driven-development/  (5 files)
      … 5 files under this directory
    test-driven-development-ecosystem/  (3 files)
      … 3 files under this directory
    test-driven-development-persistence/  (4 files)
      … 4 files under this directory
    using-agent-skills/  (1 files)
      … 1 files under this directory
  plugin/  (33 files)
    code-review-fires/  (4 files)
      … 4 files under this directory
    code-review-fires-on-plain-request/  (2 files)
      … 2 files under this directory
    code-review-stays-quiet/  (3 files)
      … 3 files under this directory
    code-review-stays-quiet-on-commit-message/  (2 files)
      … 2 files under this directory
    debugging-fires-on-pasted-diff/  (3 files)
      … 3 files under this directory
    debugging-stays-quiet-on-review/  (2 files)
      … 2 files under this directory
    gitflow-fires-on-commit-message/  (3 files)
      … 3 files under this directory
    gitflow-stays-quiet-on-what-broke/  (2 files)
      … 2 files under this directory
    simplify-fires-on-pasted-function/  (3 files)
      … 3 files under this directory
    simplify-stays-quiet-on-make-it-fast/  (2 files)
      … 2 files under this directory
    tdd-fires-on-pasted-bug/  (3 files)
      … 3 files under this directory
    tdd-stays-quiet-on-debug/  (2 files)
      … 2 files under this directory
    tdd-stays-quiet-on-refactor/  (2 files)
      … 2 files under this directory
  README.md
  skill-impact.md
hooks/  (9 files)
  SDD-CACHE.md
  SIMPLIFY-IGNORE.md
  sdd-cache-post.sh
  sdd-cache-pre.sh
  sdd-cache-test.sh
  session-start-test.sh
  session-start.sh
  simplify-ignore-test.sh
  simplify-ignore.sh
references/  (7 files)
  accessibility-checklist.md
  definition-of-done.md
  observability-checklist.md
  orchestration-patterns.md
  performance-checklist.md
  security-checklist.md
  testing-patterns.md
scripts/  (18 files)
  lib/  (4 files)
    execution-status.js
    skill-lint-test.js
    skill-lint.js
    skill-resources.js
  floor-guard-reference-test.js
  quality-gate-test.js
  run-evals-test.js
  run-evals.js
  staged-secret-scan-test.js
  validate-artifact-paths-test.js
  validate-artifact-paths.js
  validate-commands-test.js
  validate-commands.js
  validate-reference-links-test.js
  validate-reference-links.js
  validate-skills.js
  validate-versions-test.js
  validate-versions.js
skills/  (33 files)
  api-and-interface-design/  (1 files)
    SKILL.md
  browser-testing-with-devtools/  (1 files)
    SKILL.md
  ci-cd-and-automation/  (1 files)
    SKILL.md
  code-review-and-quality/  (1 files)
    SKILL.md
  code-simplification/  (1 files)
    SKILL.md
  constraint-driven-development/  (3 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    SKILL.md
  context-engineering/  (1 files)
    SKILL.md
  debugging-and-error-recovery/  (1 files)
    SKILL.md
  deprecation-and-migration/  (1 files)
    SKILL.md
  documentation-and-adrs/  (1 files)
    SKILL.md
  doubt-driven-development/  (1 files)
    SKILL.md
  frontend-ui-engineering/  (1 files)
    SKILL.md
  git-workflow-and-versioning/  (1 files)
    SKILL.md
  idea-refine/  (5 files)
    scripts/  (1 files)
      … 1 files under this directory
    SKILL.md
    examples.md
    frameworks.md
    refinement-criteria.md
  incremental-implementation/  (1 files)
    SKILL.md
  interview-me/  (1 files)
    SKILL.md
  observability-and-instrumentation/  (1 files)
    SKILL.md
  performance-optimization/  (2 files)
    references/  (1 files)
      … 1 files under this directory
    SKILL.md
  planning-and-task-breakdown/  (1 files)
    SKILL.md
  security-and-hardening/  (2 files)
    references/  (1 files)
      … 1 files under this directory
    SKILL.md
  shipping-and-launch/  (1 files)
    SKILL.md
  source-driven-development/  (1 files)
    SKILL.md
  spec-driven-development/  (1 files)
    SKILL.md
  test-driven-development/  (1 files)
    SKILL.md
  using-agent-skills/  (1 files)
    SKILL.md
.gitattributes
.gitignore
AGENTS.md
CLAUDE.md
CONTRIBUTING.md
LICENSE
README.md
plugin.json
```

## Entry points

- [evals/fixtures/browser-testing-with-devtools/server.js](https://github.com/addyosmani/agent-skills/blob/39b723ceebf81474d0557c1fecd01eddab585563/evals/fixtures/browser-testing-with-devtools/server.js)
- [evals/fixtures/git-workflow-and-versioning/app.js](https://github.com/addyosmani/agent-skills/blob/39b723ceebf81474d0557c1fecd01eddab585563/evals/fixtures/git-workflow-and-versioning/app.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 37 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| evals package | library | Observed | Groups 25 file(s) under evals package (observed from repository paths and static analysis). Observed top-level functions: allowed, apply_entries, fee, initialize, lookup, replace_secret. |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 7 file(s) under hooks package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 18 file(s) under scripts package (observed from repository paths and static analysis). |
| skills package | library | Observed | Groups 2 file(s) under skills package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 4 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: ApplyEntriesTest, ReplaceSecretTest. |

## Important files

- `.agents/plugins/marketplace.json` (config)
- `.claude-plugin/marketplace.json` (config)
- `.claude-plugin/plugin.json` (config)
- `.codex-plugin/plugin.json` (config)
- `.gemini/commands/build.toml` (config)
- `.gemini/commands/code-simplify.toml` (config)
- `.gemini/commands/constraints.toml` (config)
- `.gemini/commands/planning.toml` (config)
- `.gemini/commands/review.toml` (config)
- `.gemini/commands/ship.toml` (config)
- `.gemini/commands/spec.toml` (config)
- `.gemini/commands/test.toml` (config)
- `.gemini/commands/webperf.toml` (config)
- `.github/ISSUE_TEMPLATE/skill-gap.yml` (config)
- `.github/workflows/test-plugin-install.yml` (ci)
- `commands/build.toml` (config)
- `commands/code-simplify.toml` (config)
- `commands/constraints.toml` (config)
- `commands/planning.toml` (config)
- `commands/review.toml` (config)
- `commands/ship.toml` (config)
- `commands/spec.toml` (config)
- `commands/test.toml` (config)
- `commands/webperf.toml` (config)
- `evals/cases/api-and-interface-design.json` (config)
- `evals/cases/browser-testing-with-devtools.json` (config)
- `evals/cases/ci-cd-and-automation.json` (config)
- `evals/cases/code-review-and-quality.json` (config)
- `evals/cases/code-simplification.json` (config)
- `evals/cases/constraint-driven-development.json` (config)
- `evals/cases/context-engineering.json` (config)
- `evals/cases/debugging-and-error-recovery.json` (config)
- `evals/cases/deprecation-and-migration.json` (config)
- `evals/cases/documentation-and-adrs.json` (config)
- `evals/cases/doubt-driven-development.json` (config)
- `evals/cases/frontend-ui-engineering.json` (config)
- `evals/cases/git-workflow-and-versioning.json` (config)
- `evals/cases/idea-refine.json` (config)
- `evals/cases/incremental-implementation.json` (config)
- `evals/cases/interview-me.json` (config)
- `evals/cases/observability-and-instrumentation.json` (config)
- `evals/cases/performance-optimization.json` (config)
- `evals/cases/planning-and-task-breakdown.json` (config)
- `evals/cases/security-and-hardening.json` (config)
- `evals/cases/shipping-and-launch.json` (config)
- `evals/cases/source-driven-development.json` (config)
- `evals/cases/spec-driven-development.json` (config)
- `evals/cases/test-driven-development.json` (config)
- `evals/cases/using-agent-skills.json` (config)
- `evals/fixtures/ci-cd-and-automation/package.json` (manifest)
- `evals/fixtures/test-driven-development/package.json` (manifest)
- `plugin.json` (config)

## Top-level layout

- `evals` — 121 analysed file(s)
- `skills` — 33 analysed file(s)
- `scripts` — 18 analysed file(s)
- `docs` — 17 analysed file(s)
- `.claude` — 10 analysed file(s)
- `.gemini` — 9 analysed file(s)
- `commands` — 9 analysed file(s)
- `hooks` — 9 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `references` — 7 analysed file(s)
- `agents` — 4 analysed file(s)
- `.claude-plugin` — 2 analysed file(s)
- `.github` — 2 analysed file(s)
- `.agents` — 1 analysed file(s)
- `.codex-plugin` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `39b723ceebf81474d0557c1fecd01eddab585563` is the revision these paths and observations refer to.
