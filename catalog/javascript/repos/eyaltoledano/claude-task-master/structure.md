# Project structure: eyaltoledano/claude-task-master

**Analysed commit:** `c0c98d367c55296bfe69e65680625b6db437af02`

**Commit reference:** [c0c98d367c55296bfe69e65680625b6db437af02](https://github.com/eyaltoledano/claude-task-master/commit/c0c98d367c55296bfe69e65680625b6db437af02)

**Tree at this commit:** [eyaltoledano/claude-task-master@c0c98d367c55](https://github.com/eyaltoledano/claude-task-master/tree/c0c98d367c55296bfe69e65680625b6db437af02)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | eyaltoledano/claude-task-master |
| Description | An AI-powered task-management system you can drop into Cursor, Lovable, Windsurf, Roo, and others. |
| Stars | 28357 |
| Forks | 2618 |
| Licence | Other |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `c0c98d367c55296bfe69e65680625b6db437af02` |
| Retrieved at | 2026-11-14T19:10:50.037642+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.changeset/  (3 files)
  README.md
  config.json
  fix-sync-readme-dead-url.md
.claude/  (5 files)
  commands/  (3 files)
    go/  (2 files)
      … 2 files under this directory
    dedupe.md
  TM_COMMANDS_GUIDE.md
  hamster.md
.claude-plugin/  (1 files)
  marketplace.json
.cursor/  (27 files)
  commands/  (1 files)
    goham.md
  rules/  (25 files)
    taskmaster/  (2 files)
      … 2 files under this directory
    ai_providers.mdc
    ai_services.mdc
    architecture.mdc
    changeset.mdc
    commands.mdc
    context_gathering.mdc
    cursor_rules.mdc
    dependencies.mdc
    dev_workflow.mdc
    git_workflow.mdc
    glossary.mdc
    hamster.mdc
    mcp.mdc
    new_features.mdc
    self_improve.mdc
    tags.mdc
    taskmaster.mdc
    tasks.mdc
    telemetry.mdc
    test_workflow.mdc
    tests.mdc
    ui.mdc
    utilities.mdc
  mcp.json
.github/  (33 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    enhancements---feature-requests.md
    feedback.md
  PULL_REQUEST_TEMPLATE/  (4 files)
    bugfix.md
    config.yml
    feature.md
    integration.md
  scripts/  (9 files)
    auto-close-duplicates.mjs
    backfill-duplicate-comments.mjs
    check-pre-release-mode.mjs
    parse-metrics.mjs
    release.mjs
    sync-manifest-version.mjs
    tag-extension.mjs
    utils.mjs
    validate-changesets.mjs
  workflows/  (16 files)
    auto-close-duplicates.yml
    backfill-duplicate-comments.yml
    ci.yml
    claude-dedupe-issues.yml
    claude-docs-trigger.yml
    claude-docs-updater.yml
    claude-issue-triage.yml
    claude.yml
    extension-ci.yml
    extension-release.yml
    forward-port.yml
    log-issue-events.yml
    release-check.yml
    release.yml
    update-models-md.yml
    weekly-metrics-discord.yml
  PULL_REQUEST_TEMPLATE.md
.kiro/  (13 files)
  hooks/  (7 files)
    tm-code-change-task-tracker.kiro.hook
    tm-complexity-analyzer.kiro.hook
    tm-daily-standup-assistant.kiro.hook
    tm-git-commit-task-linker.kiro.hook
    tm-pr-readiness-checker.kiro.hook
    tm-task-dependency-auto-progression.kiro.hook
    tm-test-success-task-completer.kiro.hook
  settings/  (1 files)
    mcp.json
  steering/  (5 files)
    dev_workflow.md
    kiro_rules.md
    self_improve.md
    taskmaster.md
    taskmaster_hooks_workflow.md
.taskmaster/  (43 files)
  docs/  (20 files)
    research/  (6 files)
      … 6 files under this directory
    MIGRATION-ROADMAP.md
    README.md
    autonomous-tdd-git-workflow.md
    loop-prd.md
    prd-tm-start.txt
    prd.txt
    task-template-importing-prd.txt
    tdd-workflow-phase-0-spike.md
    tdd-workflow-phase-1-core-rails.md
    tdd-workflow-phase-1-orchestrator.md
    tdd-workflow-phase-2-pr-resumability.md
    tdd-workflow-phase-3-extensibility-guardrails.md
    test-prd.txt
    tm-core-phase-1.txt
  reports/  (9 files)
    task-complexity-report.json
    task-complexity-report_autonomous-tdd-git-workflow.json
    task-complexity-report_cc-kiro-hooks.json
    task-complexity-report_loop.json
    task-complexity-report_tdd-phase-1-core-rails.json
    task-complexity-report_tdd-workflow-phase-0.json
    task-complexity-report_test-prd-tag.json
    task-complexity-report_tm-core-phase-1.json
    tm-core-complexity.json
  tasks/  (5 files)
    task_001_tm-start.txt
    task_002_tm-start.txt
    task_003_tm-start.txt
    task_004_tm-start.txt
    task_007_tm-start.txt
  templates/  (4 files)
    example_prd.md
    example_prd.txt
    example_prd_rpg.md
    example_prd_rpg.txt
  CLAUDE.md
  ascii-art (6).txt
  config.json
  loop-progress.txt
  state.json
.vscode/  (2 files)
  extensions.json
  settings.json
apps/  (258 files)
  cli/  (101 files)
    src/  (87 files)
      … 87 files under this directory
    tests/  (10 files)
      … 10 files under this directory
    CHANGELOG.md
    package.json
    tsconfig.json
    vitest.config.ts
  docs/  (45 files)
    archive/  (7 files)
      … 7 files under this directory
    best-practices/  (3 files)
      … 3 files under this directory
    capabilities/  (6 files)
      … 6 files under this directory
    getting-started/  (12 files)
      … 12 files under this directory
    logo/  (2 files)
      … 2 files under this directory
    providers/  (1 files)
      … 1 files under this directory
    tdd-workflow/  (2 files)
      … 2 files under this directory
    CHANGELOG.md
    README.md
    command-reference.mdx
    configuration.mdx
    docs.json
    favicon.svg
    introduction.mdx
    licensing.md
    package.json
    style.css
    vercel.json
    whats-new.mdx
  extension/  (88 files)
    assets/  (3 files)
      … 3 files under this directory
    docs/  (2 files)
      … 2 files under this directory
    src/  (73 files)
      … 73 files under this directory
    .vscodeignore
    CHANGELOG.md
    LICENSE
    README.md
    components.json
    esbuild.js
    package.json
    package.mjs
    package.publish.json
    tsconfig.json
  mcp/  (24 files)
    src/  (18 files)
      … 18 files under this directory
    tests/  (2 files)
      … 2 files under this directory
    CHANGELOG.md
    package.json
    tsconfig.json
    vitest.config.ts
assets/  (31 files)
  claude/  (1 files)
    TM_COMMANDS_GUIDE.md
  kiro-hooks/  (7 files)
    tm-code-change-task-tracker.kiro.hook
    tm-complexity-analyzer.kiro.hook
    tm-daily-standup-assistant.kiro.hook
    tm-git-commit-task-linker.kiro.hook
    tm-pr-readiness-checker.kiro.hook
    tm-task-dependency-auto-progression.kiro.hook
    tm-test-success-task-completer.kiro.hook
  roocode/  (7 files)
    .roo/  (6 files)
      … 6 files under this directory
    .roomodes
  rules/  (6 files)
    cursor_rules.mdc
    dev_workflow.mdc
    hamster.mdc
    self_improve.mdc
    taskmaster.mdc
    taskmaster_hooks_workflow.mdc
  .windsurfrules
  AGENTS.md
  GEMINI.md
  config.json
  env.example
  example_prd.txt
  example_prd_rpg.txt
  gitignore
  hamster-art.txt
  scripts_README.md
bin/  (1 files)
  task-master.js
context/  (6 files)
  chats/  (2 files)
    add-task-dependencies-1.md
    max-min-tokens.txt.md
  MCP_INTEGRATION.md
  fastmcp-core.txt
  fastmcp-docs.txt
  mcp-protocol-schema-03262025.json
docs/  (21 files)
  contributor-docs/  (2 files)
    testing-roo-integration.md
    worktree-setup.md
  examples/  (2 files)
    claude-code-usage.md
    codex-cli-usage.md
  providers/  (2 files)
    codex-cli.md
    gemini-cli.md
  scripts/  (1 files)
    models-json-to-markdown.js
  CLI-COMMANDER-PATTERN.md
  README.md
  claude-code-integration.md
  command-reference.md
  configuration.md
  cross-tag-task-movement.md
  examples.md
  licensing.md
  mcp-provider-guide.md
  mcp-provider.md
  migration-guide.md
  models.md
  task-structure.md
  tutorial.md
mcp-server/  (89 files)
  src/  (88 files)
    core/  (41 files)
      … 41 files under this directory
    custom-sdk/  (6 files)
      … 6 files under this directory
    providers/  (1 files)
      … 1 files under this directory
    tools/  (38 files)
      … 38 files under this directory
    index.js
    logger.js
  server.js
packages/  (242 files)
  ai-sdk-provider-grok-cli/  (15 files)
    src/  (11 files)
      … 11 files under this directory
    CHANGELOG.md
    README.md
    package.json
    tsconfig.json
  build-config/  (5 files)
    scripts/  (1 files)
      … 1 files under this directory
    src/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    package.json
    tsconfig.json
  claude-code-plugin/  (54 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (3 files)
      … 3 files under this directory
    commands/  (46 files)
      … 46 files under this directory
    .gitignore
    CHANGELOG.md
    mcp.json
    package.json
  tm-bridge/  (12 files)
    src/  (8 files)
      … 8 files under this directory
    CHANGELOG.md
    README.md
    package.json
    tsconfig.json
  tm-core/  (156 files)
    docs/  (1 files)
      … 1 files under this directory
    src/  (150 files)
      … 150 files under this directory
    .gitignore
    CHANGELOG.md
    POC-STATUS.md
    README.md
    package.json
.coderabbit.yaml
.cursorignore
.env.example
.gitignore
.manypkg.json
.mcp.json
.mcpbignore
.npmignore
.nvmrc
CLAUDE.md
CLAUDE_CODE_PLUGIN.md
CONTRIBUTING.md
LICENSE
README-task-master.md
README.md
biome.json
context7.json
index.js
jest.config.js
jest.resolver.cjs
llms-install.md
manifest.json
mcp-test.js
output.json
… 1 more files
```

## Entry points

- [index.js](https://github.com/eyaltoledano/claude-task-master/blob/c0c98d367c55296bfe69e65680625b6db437af02/index.js)
- [apps/cli/src/index.ts](https://github.com/eyaltoledano/claude-task-master/blob/c0c98d367c55296bfe69e65680625b6db437af02/apps/cli/src/index.ts)
- [apps/extension/src/index.ts](https://github.com/eyaltoledano/claude-task-master/blob/c0c98d367c55296bfe69e65680625b6db437af02/apps/extension/src/index.ts)
- [apps/mcp/src/index.ts](https://github.com/eyaltoledano/claude-task-master/blob/c0c98d367c55296bfe69e65680625b6db437af02/apps/mcp/src/index.ts)
- [mcp-server/server.js](https://github.com/eyaltoledano/claude-task-master/blob/c0c98d367c55296bfe69e65680625b6db437af02/mcp-server/server.js)
- [mcp-server/src/custom-sdk/index.js](https://github.com/eyaltoledano/claude-task-master/blob/c0c98d367c55296bfe69e65680625b6db437af02/mcp-server/src/custom-sdk/index.js)
- [mcp-server/src/index.js](https://github.com/eyaltoledano/claude-task-master/blob/c0c98d367c55296bfe69e65680625b6db437af02/mcp-server/src/index.js)
- [mcp-server/src/tools/index.js](https://github.com/eyaltoledano/claude-task-master/blob/c0c98d367c55296bfe69e65680625b6db437af02/mcp-server/src/tools/index.js)
- [packages/ai-sdk-provider-grok-cli/src/index.ts](https://github.com/eyaltoledano/claude-task-master/blob/c0c98d367c55296bfe69e65680625b6db437af02/packages/ai-sdk-provider-grok-cli/src/index.ts)
- [packages/tm-bridge/src/index.ts](https://github.com/eyaltoledano/claude-task-master/blob/c0c98d367c55296bfe69e65680625b6db437af02/packages/tm-bridge/src/index.ts)
- [packages/tm-core/src/index.ts](https://github.com/eyaltoledano/claude-task-master/blob/c0c98d367c55296bfe69e65680625b6db437af02/packages/tm-core/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| apps package | library | Observed | Groups 164 file(s) under apps package (observed from repository paths and static analysis). |
| bin package | library | Observed | Groups 1 file(s) under bin package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 41 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 21 file(s) under data layer (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 8 file(s) under external integrations (observed from repository paths and static analysis). |
| mcp-server package | library | Observed | Groups 47 file(s) under mcp-server package (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 104 file(s) under packages package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 80 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 14 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.claude-plugin/marketplace.json` (config)
- `.coderabbit.yaml` (config)
- `.cursor/mcp.json` (config)
- `.env.example` (config)
- `.github/PULL_REQUEST_TEMPLATE/config.yml` (config)
- `.github/workflows/auto-close-duplicates.yml` (ci)
- `.github/workflows/backfill-duplicate-comments.yml` (ci)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/claude-dedupe-issues.yml` (ci)
- `.github/workflows/claude-docs-trigger.yml` (ci)
- `.github/workflows/claude-docs-updater.yml` (ci)
- `.github/workflows/claude-issue-triage.yml` (ci)
- `.github/workflows/claude.yml` (ci)
- `.github/workflows/extension-ci.yml` (ci)
- `.github/workflows/extension-release.yml` (ci)
- `.github/workflows/forward-port.yml` (ci)
- `.github/workflows/log-issue-events.yml` (ci)
- `.github/workflows/release-check.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/update-models-md.yml` (ci)
- `.github/workflows/weekly-metrics-discord.yml` (ci)
- `.kiro/settings/mcp.json` (config)
- `.manypkg.json` (config)
- `.mcp.json` (config)
- `.taskmaster/config.json` (config)
- `.taskmaster/reports/task-complexity-report.json` (config)
- `.taskmaster/reports/task-complexity-report_autonomous-tdd-git-workflow.json` (config)
- `.taskmaster/reports/task-complexity-report_cc-kiro-hooks.json` (config)
- `.taskmaster/reports/task-complexity-report_loop.json` (config)
- `.taskmaster/reports/task-complexity-report_tdd-phase-1-core-rails.json` (config)
- `.taskmaster/reports/task-complexity-report_tdd-workflow-phase-0.json` (config)
- `.taskmaster/reports/task-complexity-report_test-prd-tag.json` (config)
- `.taskmaster/reports/task-complexity-report_tm-core-phase-1.json` (config)
- `.taskmaster/reports/tm-core-complexity.json` (config)
- `.taskmaster/state.json` (config)
- `.vscode/extensions.json` (config)
- `.vscode/settings.json` (config)
- `apps/cli/package.json` (manifest)
- `apps/cli/tsconfig.json` (config)
- `apps/docs/docs.json` (config)
- `apps/docs/package.json` (manifest)
- `apps/docs/vercel.json` (config)
- `apps/extension/components.json` (config)
- `apps/extension/package.json` (manifest)
- `apps/extension/package.publish.json` (config)
- `apps/extension/tsconfig.json` (config)
- `apps/mcp/package.json` (manifest)
- `apps/mcp/tsconfig.json` (config)
- `assets/config.json` (config)
- `biome.json` (config)
- `context/mcp-protocol-schema-03262025.json` (config)
- `context7.json` (config)
- `manifest.json` (config)
- `output.json` (config)
- `package.json` (manifest)
- `packages/ai-sdk-provider-grok-cli/package.json` (manifest)
- `packages/ai-sdk-provider-grok-cli/tsconfig.json` (config)
- `packages/build-config/package.json` (manifest)
- `packages/build-config/tsconfig.json` (config)
- `packages/claude-code-plugin/.claude-plugin/plugin.json` (config)
- `packages/claude-code-plugin/mcp.json` (config)
- `packages/claude-code-plugin/package.json` (manifest)
- `packages/tm-bridge/package.json` (manifest)
- `packages/tm-bridge/tsconfig.json` (config)
- `packages/tm-core/package.json` (manifest)

## Top-level layout

- `apps` — 258 analysed file(s)
- `packages` — 242 analysed file(s)
- `mcp-server` — 89 analysed file(s)
- `.taskmaster` — 43 analysed file(s)
- `.github` — 33 analysed file(s)
- `assets` — 31 analysed file(s)
- `.cursor` — 27 analysed file(s)
- `(root files)` — 25 analysed file(s)
- `docs` — 21 analysed file(s)
- `.kiro` — 13 analysed file(s)
- `context` — 6 analysed file(s)
- `.claude` — 5 analysed file(s)
- `.changeset` — 3 analysed file(s)
- `.vscode` — 2 analysed file(s)
- `.claude-plugin` — 1 analysed file(s)
- `bin` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `c0c98d367c55296bfe69e65680625b6db437af02` is the revision these paths and observations refer to.
