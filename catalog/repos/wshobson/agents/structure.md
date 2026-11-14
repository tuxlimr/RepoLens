# Project structure: wshobson/agents

**Analysed commit:** `9c61ab243def98f72da12abd41cfcf5bcd91af9d`

**Commit reference:** [9c61ab243def98f72da12abd41cfcf5bcd91af9d](https://github.com/wshobson/agents/commit/9c61ab243def98f72da12abd41cfcf5bcd91af9d)

**Tree at this commit:** [wshobson/agents@9c61ab243def](https://github.com/wshobson/agents/tree/9c61ab243def98f72da12abd41cfcf5bcd91af9d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | wshobson/agents |
| Description | Plugins, agents, skills, and commands for Claude Code, Codex CLI, Cursor, OpenCode, Antigravity CLI, GitHub Copilot, and Pi, written once in Markdown and adapted to each tool by generators with validation and evals. |
| Stars | 42510 |
| Forks | 4493 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `9c61ab243def98f72da12abd41cfcf5bcd91af9d` |
| Retrieved at | 2026-11-14T19:06:39.421372+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.agents/  (1 files)
  plugins/  (1 files)
    marketplace.json
.claude-plugin/  (1 files)
  marketplace.json
.cursor/  (3 files)
  rules/  (3 files)
    000-project-conventions.mdc
    010-python-tooling.mdc
    020-agent-skill-authoring.mdc
.cursor-plugin/  (94 files)
  plugins/  (92 files)
    accessibility-compliance.json
    agent-orchestration.json
    agent-teams.json
    api-scaffolding.json
    api-testing-observability.json
    application-performance.json
    arm-cortex-microcontrollers.json
    avoid-ai-writing.json
    backend-api-security.json
    backend-development.json
    before-you-build.json
    block-no-verify.json
    blockchain-web3.json
    brand-landingpage.json
    business-analytics.json
    c4-architecture.json
    cicd-automation.json
    cloud-infrastructure.json
    code-documentation.json
    code-refactoring.json
    codebase-cleanup.json
    comprehensive-review.json
    conductor.json
    content-marketing.json
    … 68 more files
  marketplace.json
  plugin.json
.github/  (16 files)
  ISSUE_TEMPLATE/  (5 files)
    bug_report.yml
    config.yml
    feature_request.yml
    moderation_report.yml
    new_subagent.yml
  workflows/  (6 files)
    claude-code-review.yml
    claude.yml
    code-quality.yml
    eval-report.yml
    mlops.yml
    validate.yml
  CODE_OF_CONDUCT.md
  CONTRIBUTING.md
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
docs/  (10 files)
  agent-skills.md
  agents.md
  architecture.md
  authoring.md
  harnesses.md
  mlops.md
  plugin-eval.md
  plugins.md
  round-trip-results.md
  usage.md
evals/  (2 files)
  README.md
  static-score-snapshot.json
plugins/  (665 files)
  accessibility-compliance/  (11 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    .codex-plugin/  (1 files)
      … 1 files under this directory
    agents/  (1 files)
      … 1 files under this directory
    commands/  (1 files)
      … 1 files under this directory
    skills/  (7 files)
      … 7 files under this directory
  agent-orchestration/  (4 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (1 files)
      … 1 files under this directory
    commands/  (2 files)
      … 2 files under this directory
  agent-teams/  (29 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    .codex-plugin/  (1 files)
      … 1 files under this directory
    agents/  (4 files)
      … 4 files under this directory
    commands/  (7 files)
      … 7 files under this directory
    skills/  (15 files)
      … 15 files under this directory
    README.md
  api-scaffolding/  (8 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    .codex-plugin/  (1 files)
      … 1 files under this directory
    agents/  (4 files)
      … 4 files under this directory
    skills/  (2 files)
      … 2 files under this directory
  api-testing-observability/  (3 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (1 files)
      … 1 files under this directory
    commands/  (1 files)
      … 1 files under this directory
  application-performance/  (5 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (3 files)
      … 3 files under this directory
    commands/  (1 files)
      … 1 files under this directory
  arm-cortex-microcontrollers/  (2 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (1 files)
      … 1 files under this directory
  avoid-ai-writing/  (7 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    .codex-plugin/  (1 files)
      … 1 files under this directory
    skills/  (4 files)
      … 4 files under this directory
    README.md
  backend-api-security/  (3 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (2 files)
      … 2 files under this directory
  backend-development/  (38 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    .codex-plugin/  (1 files)
      … 1 files under this directory
    agents/  (8 files)
      … 8 files under this directory
    commands/  (1 files)
      … 1 files under this directory
    skills/  (27 files)
      … 27 files under this directory
  before-you-build/  (5 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    .codex-plugin/  (1 files)
      … 1 files under this directory
    skills/  (2 files)
      … 2 files under this directory
    README.md
  block-no-verify/  (4 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    .codex-plugin/  (1 files)
      … 1 files under this directory
    commands/  (1 files)
      … 1 files under this directory
    skills/  (1 files)
      … 1 files under this directory
  blockchain-web3/  (11 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    .codex-plugin/  (1 files)
      … 1 files under this directory
    agents/  (1 files)
      … 1 files under this directory
    skills/  (8 files)
      … 8 files under this directory
  brand-landingpage/  (7 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    .codex-plugin/  (1 files)
      … 1 files under this directory
    skills/  (4 files)
      … 4 files under this directory
    README.md
  business-analytics/  (7 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    .codex-plugin/  (1 files)
      … 1 files under this directory
    agents/  (1 files)
      … 1 files under this directory
    skills/  (4 files)
      … 4 files under this directory
  c4-architecture/  (6 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (4 files)
      … 4 files under this directory
    commands/  (1 files)
      … 1 files under this directory
  cicd-automation/  (14 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    .codex-plugin/  (1 files)
      … 1 files under this directory
    agents/  (5 files)
      … 5 files under this directory
    commands/  (1 files)
      … 1 files under this directory
    skills/  (6 files)
      … 6 files under this directory
  cloud-infrastructure/  (25 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    .codex-plugin/  (1 files)
      … 1 files under this directory
    agents/  (7 files)
      … 7 files under this directory
    skills/  (16 files)
      … 16 files under this directory
  code-documentation/  (6 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (3 files)
      … 3 files under this directory
    commands/  (2 files)
      … 2 files under this directory
  code-refactoring/  (6 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (2 files)
      … 2 files under this directory
    commands/  (3 files)
      … 3 files under this directory
  codebase-cleanup/  (6 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (2 files)
      … 2 files under this directory
    commands/  (3 files)
      … 3 files under this directory
  comprehensive-review/  (6 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (3 files)
      … 3 files under this directory
    commands/  (2 files)
      … 2 files under this directory
  conductor/  (34 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    .codex-plugin/  (1 files)
      … 1 files under this directory
    agents/  (1 files)
      … 1 files under this directory
    commands/  (6 files)
      … 6 files under this directory
    skills/  (7 files)
      … 7 files under this directory
    templates/  (17 files)
      … 17 files under this directory
    README.md
  content-marketing/  (8 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    .codex-plugin/  (1 files)
      … 1 files under this directory
    agents/  (2 files)
      … 2 files under this directory
    skills/  (4 files)
      … 4 files under this directory
  context-management/  (4 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (1 files)
      … 1 files under this directory
    commands/  (2 files)
      … 2 files under this directory
  customer-sales-automation/  (3 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (2 files)
      … 2 files under this directory
  data-engineering/  (14 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    .codex-plugin/  (1 files)
      … 1 files under this directory
    agents/  (2 files)
      … 2 files under this directory
    commands/  (2 files)
      … 2 files under this directory
    skills/  (8 files)
      … 8 files under this directory
  data-validation-suite/  (2 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (1 files)
      … 1 files under this directory
  database-cloud-optimization/  (6 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (4 files)
      … 4 files under this directory
    commands/  (1 files)
      … 1 files under this directory
  database-design/  (6 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    .codex-plugin/  (1 files)
      … 1 files under this directory
    agents/  (2 files)
      … 2 files under this directory
    skills/  (2 files)
      … 2 files under this directory
  database-migrations/  (5 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (2 files)
      … 2 files under this directory
    commands/  (2 files)
      … 2 files under this directory
  debugging-toolkit/  (4 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (2 files)
      … 2 files under this directory
    commands/  (1 files)
      … 1 files under this directory
  dependency-management/  (3 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (1 files)
      … 1 files under this directory
    commands/  (1 files)
      … 1 files under this directory
  deployment-strategies/  (3 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (2 files)
      … 2 files under this directory
  deployment-validation/  (3 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (1 files)
      … 1 files under this directory
    commands/  (1 files)
      … 1 files under this directory
  developer-essentials/  (25 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    .codex-plugin/  (1 files)
      … 1 files under this directory
    agents/  (1 files)
      … 1 files under this directory
    skills/  (22 files)
      … 22 files under this directory
  dgx-spark-ops/  (13 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    .codex-plugin/  (1 files)
      … 1 files under this directory
    agents/  (1 files)
      … 1 files under this directory
    commands/  (1 files)
      … 1 files under this directory
    skills/  (9 files)
      … 9 files under this directory
  distributed-debugging/  (4 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (2 files)
      … 2 files under this directory
    commands/  (1 files)
      … 1 files under this directory
  documentation-generation/  (16 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    .codex-plugin/  (1 files)
      … 1 files under this directory
    agents/  (5 files)
      … 5 files under this directory
    commands/  (1 files)
      … 1 files under this directory
    skills/  (8 files)
      … 8 files under this directory
  documentation-standards/  (5 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    .codex-plugin/  (1 files)
      … 1 files under this directory
    skills/  (3 files)
      … 3 files under this directory
  dotnet-contribution/  (9 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    .codex-plugin/  (1 files)
      … 1 files under this directory
    agents/  (1 files)
      … 1 files under this directory
    skills/  (5 files)
      … 5 files under this directory
    README.md
  error-debugging/  (6 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (2 files)
      … 2 files under this directory
    commands/  (3 files)
      … 3 files under this directory
  error-diagnostics/  (6 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (2 files)
      … 2 files under this directory
    commands/  (3 files)
      … 3 files under this directory
  file-conversion/  (4 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    .codex-plugin/  (1 files)
      … 1 files under this directory
    skills/  (1 files)
      … 1 files under this directory
    README.md
  framework-migration/  (14 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    .codex-plugin/  (1 files)
      … 1 files under this directory
    agents/  (2 files)
      … 2 files under this directory
    commands/  (3 files)
      … 3 files under this directory
    skills/  (7 files)
      … 7 files under this directory
  frontend-mobile-development/  (14 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    .codex-plugin/  (1 files)
      … 1 files under this directory
    agents/  (2 files)
      … 2 files under this directory
    commands/  (1 files)
      … 1 files under this directory
    skills/  (9 files)
      … 9 files under this directory
  frontend-mobile-security/  (5 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (3 files)
      … 3 files under this directory
    commands/  (1 files)
      … 1 files under this directory
  full-stack-orchestration/  (6 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (4 files)
      … 4 files under this directory
    commands/  (1 files)
      … 1 files under this directory
  functional-programming/  (3 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (2 files)
      … 2 files under this directory
  game-development/  (9 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    .codex-plugin/  (1 files)
      … 1 files under this directory
    agents/  (2 files)
      … 2 files under this directory
    skills/  (5 files)
      … 5 files under this directory
  git-pr-workflows/  (5 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (1 files)
      … 1 files under this directory
    commands/  (3 files)
      … 3 files under this directory
  hermes-tweet/  (6 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    .codex-plugin/  (1 files)
      … 1 files under this directory
    skills/  (3 files)
      … 3 files under this directory
    README.md
  hr-legal-compliance/  (8 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    .codex-plugin/  (1 files)
      … 1 files under this directory
    agents/  (2 files)
      … 2 files under this directory
    skills/  (4 files)
      … 4 files under this directory
  incident-response/  (18 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    .codex-plugin/  (1 files)
      … 1 files under this directory
    agents/  (6 files)
      … 6 files under this directory
    commands/  (2 files)
      … 2 files under this directory
    skills/  (8 files)
      … 8 files under this directory
  javascript-typescript/  (15 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    .codex-plugin/  (1 files)
      … 1 files under this directory
    agents/  (2 files)
      … 2 files under this directory
    commands/  (1 files)
      … 1 files under this directory
    skills/  (10 files)
      … 10 files under this directory
  julia-development/  (2 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (1 files)
      … 1 files under this directory
  jvm-languages/  (4 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (3 files)
      … 3 files under this directory
  kubernetes-operations/  (22 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    .codex-plugin/  (1 files)
      … 1 files under this directory
    agents/  (1 files)
      … 1 files under this directory
    skills/  (19 files)
      … 19 files under this directory
  llm-application-dev/  (33 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    .codex-plugin/  (1 files)
      … 1 files under this directory
    agents/  (3 files)
      … 3 files under this directory
    commands/  (3 files)
      … 3 files under this directory
    skills/  (24 files)
      … 24 files under this directory
    README.md
  llm-finetuning/  (32 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    .codex-plugin/  (1 files)
      … 1 files under this directory
    agents/  (3 files)
      … 3 files under this directory
    commands/  (2 files)
      … 2 files under this directory
    skills/  (25 files)
      … 25 files under this directory
  machine-learning-ops/  (8 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    .codex-plugin/  (1 files)
      … 1 files under this directory
    agents/  (3 files)
      … 3 files under this directory
    commands/  (1 files)
      … 1 files under this directory
    skills/  (2 files)
      … 2 files under this directory
  meigen-ai-design/  (7 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (3 files)
      … 3 files under this directory
    commands/  (2 files)
      … 2 files under this directory
    README.md
  multi-platform-apps/  (8 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (6 files)
      … 6 files under this directory
    commands/  (1 files)
      … 1 files under this directory
  observability-monitoring/  (15 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    .codex-plugin/  (1 files)
      … 1 files under this directory
    agents/  (4 files)
      … 4 files under this directory
    commands/  (2 files)
      … 2 files under this directory
    skills/  (7 files)
      … 7 files under this directory
  operating-kit/  (6 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (5 files)
      … 5 files under this directory
  payment-processing/  (11 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    .codex-plugin/  (1 files)
      … 1 files under this directory
    agents/  (1 files)
      … 1 files under this directory
    skills/  (8 files)
      … 8 files under this directory
  performance-testing-review/  (5 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (2 files)
      … 2 files under this directory
    commands/  (2 files)
      … 2 files under this directory
  plugin-eval/  (13 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    .codex-plugin/  (1 files)
      … 1 files under this directory
    agents/  (2 files)
      … 2 files under this directory
    commands/  (3 files)
      … 3 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    skills/  (2 files)
      … 2 files under this directory
    .python-version
    README.md
    pyproject.toml
.gitignore
.markdownlint.json
AGENTS.md
ARCHITECTURE.md
CONTRIBUTING.md
LICENSE
Makefile
README.md
```

## Entry points

- [plugins/backend-development/skills/api-design-principles/assets/rest-api-template.py:15](https://github.com/wshobson/agents/blob/9c61ab243def98f72da12abd41cfcf5bcd91af9d/plugins/backend-development/skills/api-design-principles/assets/rest-api-template.py#L15)
- [plugins/llm-application-dev/skills/prompt-engineering-patterns/scripts/optimize-prompt.py:285](https://github.com/wshobson/agents/blob/9c61ab243def98f72da12abd41cfcf5bcd91af9d/plugins/llm-application-dev/skills/prompt-engineering-patterns/scripts/optimize-prompt.py#L285)
- [plugins/plugin-eval/scripts/eval_all.py:301](https://github.com/wshobson/agents/blob/9c61ab243def98f72da12abd41cfcf5bcd91af9d/plugins/plugin-eval/scripts/eval_all.py#L301)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 112 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 3 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed routes: GET /api/users, POST /api/users, GET /api/users/{use… |
| plugins package | library | Observed | Groups 5 file(s) under plugins package (observed from repository paths and static analysis). |

## Important files

- `.agents/plugins/marketplace.json` (config)
- `.claude-plugin/marketplace.json` (config)
- `.cursor-plugin/marketplace.json` (config)
- `.cursor-plugin/plugin.json` (config)
- `.cursor-plugin/plugins/accessibility-compliance.json` (config)
- `.cursor-plugin/plugins/agent-orchestration.json` (config)
- `.cursor-plugin/plugins/agent-teams.json` (config)
- `.cursor-plugin/plugins/api-scaffolding.json` (config)
- `.cursor-plugin/plugins/api-testing-observability.json` (config)
- `.cursor-plugin/plugins/application-performance.json` (config)
- `.cursor-plugin/plugins/arm-cortex-microcontrollers.json` (config)
- `.cursor-plugin/plugins/avoid-ai-writing.json` (config)
- `.cursor-plugin/plugins/backend-api-security.json` (config)
- `.cursor-plugin/plugins/backend-development.json` (config)
- `.cursor-plugin/plugins/before-you-build.json` (config)
- `.cursor-plugin/plugins/block-no-verify.json` (config)
- `.cursor-plugin/plugins/blockchain-web3.json` (config)
- `.cursor-plugin/plugins/brand-landingpage.json` (config)
- `.cursor-plugin/plugins/business-analytics.json` (config)
- `.cursor-plugin/plugins/c4-architecture.json` (config)
- `.cursor-plugin/plugins/cicd-automation.json` (config)
- `.cursor-plugin/plugins/cloud-infrastructure.json` (config)
- `.cursor-plugin/plugins/code-documentation.json` (config)
- `.cursor-plugin/plugins/code-refactoring.json` (config)
- `.cursor-plugin/plugins/codebase-cleanup.json` (config)
- `.cursor-plugin/plugins/comprehensive-review.json` (config)
- `.cursor-plugin/plugins/conductor.json` (config)
- `.cursor-plugin/plugins/content-marketing.json` (config)
- `.cursor-plugin/plugins/context-management.json` (config)
- `.cursor-plugin/plugins/customer-sales-automation.json` (config)
- `.cursor-plugin/plugins/data-engineering.json` (config)
- `.cursor-plugin/plugins/data-validation-suite.json` (config)
- `.cursor-plugin/plugins/database-cloud-optimization.json` (config)
- `.cursor-plugin/plugins/database-design.json` (config)
- `.cursor-plugin/plugins/database-migrations.json` (config)
- `.cursor-plugin/plugins/debugging-toolkit.json` (config)
- `.cursor-plugin/plugins/dependency-management.json` (config)
- `.cursor-plugin/plugins/deployment-strategies.json` (config)
- `.cursor-plugin/plugins/deployment-validation.json` (config)
- `.cursor-plugin/plugins/developer-essentials.json` (config)
- `.cursor-plugin/plugins/dgx-spark-ops.json` (config)
- `.cursor-plugin/plugins/distributed-debugging.json` (config)
- `.cursor-plugin/plugins/documentation-generation.json` (config)
- `.cursor-plugin/plugins/documentation-standards.json` (config)
- `.cursor-plugin/plugins/dotnet-contribution.json` (config)
- `.cursor-plugin/plugins/error-debugging.json` (config)
- `.cursor-plugin/plugins/error-diagnostics.json` (config)
- `.cursor-plugin/plugins/file-conversion.json` (config)
- `.cursor-plugin/plugins/framework-migration.json` (config)
- `.cursor-plugin/plugins/frontend-mobile-development.json` (config)
- `.cursor-plugin/plugins/frontend-mobile-security.json` (config)
- `.cursor-plugin/plugins/full-stack-orchestration.json` (config)
- `.cursor-plugin/plugins/functional-programming.json` (config)
- `.cursor-plugin/plugins/game-development.json` (config)
- `.cursor-plugin/plugins/git-pr-workflows.json` (config)
- `.cursor-plugin/plugins/hermes-tweet.json` (config)
- `.cursor-plugin/plugins/hr-legal-compliance.json` (config)
- `.cursor-plugin/plugins/incident-response.json` (config)
- `.cursor-plugin/plugins/javascript-typescript.json` (config)
- `.cursor-plugin/plugins/julia-development.json` (config)
- `.cursor-plugin/plugins/jvm-languages.json` (config)
- `.cursor-plugin/plugins/kubernetes-operations.json` (config)
- `.cursor-plugin/plugins/llm-application-dev.json` (config)
- `.cursor-plugin/plugins/llm-finetuning.json` (config)
- `.cursor-plugin/plugins/machine-learning-ops.json` (config)
- `.cursor-plugin/plugins/meigen-ai-design.json` (config)
- `.cursor-plugin/plugins/multi-platform-apps.json` (config)
- `.cursor-plugin/plugins/observability-monitoring.json` (config)
- `.cursor-plugin/plugins/operating-kit.json` (config)
- `.cursor-plugin/plugins/payment-processing.json` (config)
- `.cursor-plugin/plugins/performance-testing-review.json` (config)
- `.cursor-plugin/plugins/plugin-eval.json` (config)
- `.cursor-plugin/plugins/pptx-deck-creation.json` (config)
- `.cursor-plugin/plugins/protect-mcp.json` (config)
- `.cursor-plugin/plugins/python-development.json` (config)
- `.cursor-plugin/plugins/quantitative-trading.json` (config)
- `.cursor-plugin/plugins/reverse-engineering.json` (config)
- `.cursor-plugin/plugins/review-agent-governance.json` (config)
- `.cursor-plugin/plugins/security-compliance.json` (config)
- `.cursor-plugin/plugins/security-scanning.json` (config)
- `.cursor-plugin/plugins/seo-analysis-monitoring.json` (config)
- `.cursor-plugin/plugins/seo-content-creation.json` (config)
- `.cursor-plugin/plugins/seo-technical-optimization.json` (config)
- `.cursor-plugin/plugins/shell-scripting.json` (config)
- `.cursor-plugin/plugins/ship-mate.json` (config)
- `.cursor-plugin/plugins/signed-audit-trails.json` (config)
- `.cursor-plugin/plugins/skill-forge-essentials.json` (config)
- `.cursor-plugin/plugins/social-publishing.json` (config)
- `.cursor-plugin/plugins/startup-business-analyst.json` (config)
- `.cursor-plugin/plugins/superself.json` (config)
- `.cursor-plugin/plugins/systems-programming.json` (config)
- `.cursor-plugin/plugins/tdd-workflows.json` (config)
- `.cursor-plugin/plugins/team-collaboration.json` (config)
- `.cursor-plugin/plugins/ui-design.json` (config)
- `.cursor-plugin/plugins/unit-testing.json` (config)
- `.cursor-plugin/plugins/web-scripting.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/ISSUE_TEMPLATE/moderation_report.yml` (config)
- `.github/ISSUE_TEMPLATE/new_subagent.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/claude-code-review.yml` (ci)
- `.github/workflows/claude.yml` (ci)
- `.github/workflows/code-quality.yml` (ci)
- `.github/workflows/eval-report.yml` (ci)
- `.github/workflows/mlops.yml` (ci)
- `.github/workflows/validate.yml` (ci)
- `.markdownlint.json` (config)
- `evals/static-score-snapshot.json` (config)
- `plugins/accessibility-compliance/.claude-plugin/plugin.json` (config)
- `plugins/accessibility-compliance/.codex-plugin/plugin.json` (config)
- `plugins/agent-orchestration/.claude-plugin/plugin.json` (config)
- `plugins/agent-teams/.claude-plugin/plugin.json` (config)
- `plugins/agent-teams/.codex-plugin/plugin.json` (config)
- `plugins/api-scaffolding/.claude-plugin/plugin.json` (config)
- `plugins/api-scaffolding/.codex-plugin/plugin.json` (config)
- `plugins/api-testing-observability/.claude-plugin/plugin.json` (config)
- `plugins/application-performance/.claude-plugin/plugin.json` (config)
- `plugins/arm-cortex-microcontrollers/.claude-plugin/plugin.json` (config)
- `plugins/avoid-ai-writing/.claude-plugin/plugin.json` (config)
- `plugins/avoid-ai-writing/.codex-plugin/plugin.json` (config)
- `plugins/backend-api-security/.claude-plugin/plugin.json` (config)
- `plugins/backend-development/.claude-plugin/plugin.json` (config)
- `plugins/backend-development/.codex-plugin/plugin.json` (config)
- `plugins/before-you-build/.claude-plugin/plugin.json` (config)
- `plugins/before-you-build/.codex-plugin/plugin.json` (config)
- `plugins/block-no-verify/.claude-plugin/plugin.json` (config)
- `plugins/block-no-verify/.codex-plugin/plugin.json` (config)
- `plugins/blockchain-web3/.claude-plugin/plugin.json` (config)
- `plugins/blockchain-web3/.codex-plugin/plugin.json` (config)
- `plugins/brand-landingpage/.claude-plugin/plugin.json` (config)
- `plugins/brand-landingpage/.codex-plugin/plugin.json` (config)
- `plugins/business-analytics/.claude-plugin/plugin.json` (config)
- `plugins/business-analytics/.codex-plugin/plugin.json` (config)
- `plugins/c4-architecture/.claude-plugin/plugin.json` (config)
- `plugins/cicd-automation/.claude-plugin/plugin.json` (config)
- `plugins/cicd-automation/.codex-plugin/plugin.json` (config)
- `plugins/cloud-infrastructure/.claude-plugin/plugin.json` (config)
- `plugins/cloud-infrastructure/.codex-plugin/plugin.json` (config)
- `plugins/code-documentation/.claude-plugin/plugin.json` (config)
- `plugins/code-refactoring/.claude-plugin/plugin.json` (config)
- `plugins/codebase-cleanup/.claude-plugin/plugin.json` (config)
- `plugins/comprehensive-review/.claude-plugin/plugin.json` (config)
- `plugins/conductor/.claude-plugin/plugin.json` (config)
- `plugins/conductor/.codex-plugin/plugin.json` (config)
- `plugins/conductor/templates/track-metadata.json` (config)
- `plugins/content-marketing/.claude-plugin/plugin.json` (config)
- `plugins/content-marketing/.codex-plugin/plugin.json` (config)
- `plugins/context-management/.claude-plugin/plugin.json` (config)
- `plugins/customer-sales-automation/.claude-plugin/plugin.json` (config)
- `plugins/data-engineering/.claude-plugin/plugin.json` (config)
- `plugins/data-engineering/.codex-plugin/plugin.json` (config)
- `plugins/data-validation-suite/.claude-plugin/plugin.json` (config)
- `plugins/database-cloud-optimization/.claude-plugin/plugin.json` (config)
- `plugins/database-design/.claude-plugin/plugin.json` (config)
- `plugins/database-design/.codex-plugin/plugin.json` (config)
- `plugins/database-migrations/.claude-plugin/plugin.json` (config)
- `plugins/debugging-toolkit/.claude-plugin/plugin.json` (config)
- `plugins/dependency-management/.claude-plugin/plugin.json` (config)
- `plugins/deployment-strategies/.claude-plugin/plugin.json` (config)
- `plugins/deployment-validation/.claude-plugin/plugin.json` (config)
- `plugins/developer-essentials/.claude-plugin/plugin.json` (config)
- `plugins/developer-essentials/.codex-plugin/plugin.json` (config)
- `plugins/dgx-spark-ops/.claude-plugin/plugin.json` (config)
- `plugins/dgx-spark-ops/.codex-plugin/plugin.json` (config)
- `plugins/distributed-debugging/.claude-plugin/plugin.json` (config)
- `plugins/documentation-generation/.claude-plugin/plugin.json` (config)
- `plugins/documentation-generation/.codex-plugin/plugin.json` (config)
- `plugins/documentation-standards/.claude-plugin/plugin.json` (config)
- `plugins/documentation-standards/.codex-plugin/plugin.json` (config)
- `plugins/dotnet-contribution/.claude-plugin/plugin.json` (config)
- `plugins/dotnet-contribution/.codex-plugin/plugin.json` (config)
- `plugins/error-debugging/.claude-plugin/plugin.json` (config)
- `plugins/error-diagnostics/.claude-plugin/plugin.json` (config)
- `plugins/file-conversion/.claude-plugin/plugin.json` (config)
- `plugins/file-conversion/.codex-plugin/plugin.json` (config)
- `plugins/framework-migration/.claude-plugin/plugin.json` (config)
- `plugins/framework-migration/.codex-plugin/plugin.json` (config)
- `plugins/frontend-mobile-development/.claude-plugin/plugin.json` (config)
- `plugins/frontend-mobile-development/.codex-plugin/plugin.json` (config)
- `plugins/frontend-mobile-security/.claude-plugin/plugin.json` (config)
- `plugins/full-stack-orchestration/.claude-plugin/plugin.json` (config)
- `plugins/functional-programming/.claude-plugin/plugin.json` (config)
- `plugins/game-development/.claude-plugin/plugin.json` (config)
- `plugins/game-development/.codex-plugin/plugin.json` (config)
- `plugins/git-pr-workflows/.claude-plugin/plugin.json` (config)
- `plugins/hermes-tweet/.claude-plugin/plugin.json` (config)
- `plugins/hermes-tweet/.codex-plugin/plugin.json` (config)
- `plugins/hr-legal-compliance/.claude-plugin/plugin.json` (config)
- `plugins/hr-legal-compliance/.codex-plugin/plugin.json` (config)
- `plugins/incident-response/.claude-plugin/plugin.json` (config)
- `plugins/incident-response/.codex-plugin/plugin.json` (config)
- `plugins/javascript-typescript/.claude-plugin/plugin.json` (config)
- `plugins/javascript-typescript/.codex-plugin/plugin.json` (config)
- `plugins/julia-development/.claude-plugin/plugin.json` (config)
- `plugins/jvm-languages/.claude-plugin/plugin.json` (config)
- `plugins/kubernetes-operations/.claude-plugin/plugin.json` (config)
- `plugins/kubernetes-operations/.codex-plugin/plugin.json` (config)
- `plugins/kubernetes-operations/skills/k8s-manifest-generator/assets/configmap-template.yaml` (config)
- `plugins/kubernetes-operations/skills/k8s-manifest-generator/assets/deployment-template.yaml` (config)
- `plugins/kubernetes-operations/skills/k8s-manifest-generator/assets/service-template.yaml` (config)
- `plugins/kubernetes-operations/skills/k8s-security-policies/assets/network-policy-template.yaml` (config)
- `plugins/llm-application-dev/.claude-plugin/plugin.json` (config)
- `plugins/llm-application-dev/.codex-plugin/plugin.json` (config)
- `plugins/llm-application-dev/skills/prompt-engineering-patterns/assets/few-shot-examples.json` (config)
- `plugins/llm-finetuning/.claude-plugin/plugin.json` (config)
- `plugins/llm-finetuning/.codex-plugin/plugin.json` (config)
- `plugins/machine-learning-ops/.claude-plugin/plugin.json` (config)
- `plugins/machine-learning-ops/.codex-plugin/plugin.json` (config)
- `plugins/meigen-ai-design/.claude-plugin/plugin.json` (config)
- `plugins/multi-platform-apps/.claude-plugin/plugin.json` (config)
- `plugins/observability-monitoring/.claude-plugin/plugin.json` (config)
- `plugins/observability-monitoring/.codex-plugin/plugin.json` (config)
- `plugins/operating-kit/.claude-plugin/plugin.json` (config)
- `plugins/payment-processing/.claude-plugin/plugin.json` (config)
- `plugins/payment-processing/.codex-plugin/plugin.json` (config)
- `plugins/performance-testing-review/.claude-plugin/plugin.json` (config)
- `plugins/plugin-eval/.claude-plugin/plugin.json` (config)
- `plugins/plugin-eval/.codex-plugin/plugin.json` (config)
- `plugins/plugin-eval/pyproject.toml` (manifest)

## Top-level layout

- `plugins` — 665 analysed file(s)
- `.cursor-plugin` — 94 analysed file(s)
- `.github` — 16 analysed file(s)
- `docs` — 10 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `.cursor` — 3 analysed file(s)
- `evals` — 2 analysed file(s)
- `.agents` — 1 analysed file(s)
- `.claude-plugin` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `9c61ab243def98f72da12abd41cfcf5bcd91af9d` is the revision these paths and observations refer to.
