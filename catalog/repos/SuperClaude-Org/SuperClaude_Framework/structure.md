# Project structure: SuperClaude-Org/SuperClaude_Framework

**Analysed commit:** `fe68862c8ed9e2afb8120c2d9e27d0c3a7ce73a2`

**Commit reference:** [fe68862c8ed9e2afb8120c2d9e27d0c3a7ce73a2](https://github.com/SuperClaude-Org/SuperClaude_Framework/commit/fe68862c8ed9e2afb8120c2d9e27d0c3a7ce73a2)

**Tree at this commit:** [SuperClaude-Org/SuperClaude_Framework@fe68862c8ed9](https://github.com/SuperClaude-Org/SuperClaude_Framework/tree/fe68862c8ed9e2afb8120c2d9e27d0c3a7ce73a2)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | SuperClaude-Org/SuperClaude_Framework |
| Description | A configuration framework that enhances Claude Code with specialized commands, cognitive personas, and development methodologies. |
| Stars | 23937 |
| Forks | 1983 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `fe68862c8ed9e2afb8120c2d9e27d0c3a7ce73a2` |
| Retrieved at | 2026-11-14T19:07:42.930256+00:00 |
| Files in this snapshot | 410 |

## Directory tree

```text
.claude/  (3 files)
  skills/  (2 files)
    confidence-check/  (2 files)
      … 2 files under this directory
  settings.json
.github/  (8 files)
  workflows/  (6 files)
    README.md
    publish-pypi.yml
    pull-sync-framework.yml
    quick-check.yml
    readme-quality-check.yml
    test.yml
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
docs/  (126 files)
  Development/  (10 files)
    tasks/  (1 files)
      … 1 files under this directory
    ARCHITECTURE.md
    PROJECT_STATUS.md
    ROADMAP.md
    TASKS.md
    hypothesis-pm-autonomous-enhancement-2025-10-14.md
    installation-flow-understanding.md
    pm-agent-ideal-workflow.md
    pm-agent-integration.md
    project-structure-understanding.md
  Templates/  (1 files)
    __init__.py
  agents/  (1 files)
    pm-agent-guide.md
  architecture/  (9 files)
    CONTEXT_WINDOW_ANALYSIS.md
    MIGRATION_TO_CLEAN_ARCHITECTURE.md
    PHASE_1_COMPLETE.md
    PHASE_2_COMPLETE.md
    PHASE_3_COMPLETE.md
    PM_AGENT_COMPARISON.md
    SKILLS_CLEANUP.md
    pm-agent-auto-activation.md
    pm-agent-responsibility-cleanup.md
  developer-guide/  (5 files)
    README.md
    contributing-code.md
    documentation-index.md
    technical-architecture.md
    testing-debugging.md
  getting-started/  (3 files)
    installation.md
    quick-start.md
    windows-installation.md
  mcp/  (2 files)
    mcp-integration-policy.md
    mcp-optional-design.md
  memory/  (10 files)
    README.md
    WORKFLOW_METRICS_SCHEMA.md
    last_session.md
    next_actions.md
    patterns_learned.jsonl
    pm_context.md
    reflexion.jsonl.example
    solutions_learned.jsonl
    token_efficiency_validation.md
    workflow_metrics.jsonl
  mistakes/  (9 files)
    test_database_connection-2025-11-11.md
    test_database_connection-2025-11-14.md
    test_database_connection-2026-03-22.md
    test_reflexion_with_real_exception-2025-11-11.md
    test_reflexion_with_real_exception-2025-11-14.md
    test_reflexion_with_real_exception-2026-03-22.md
    unknown-2025-11-11.md
    unknown-2025-11-14.md
    unknown-2026-03-22.md
  reference/  (15 files)
    README.md
    advanced-patterns.md
    advanced-workflows.md
    basic-examples.md
    claude-code-history-management.md
    commands-list.md
    common-issues.md
    comprehensive-features.md
    diagnostic-reference.md
    examples-cookbook.md
    integration-patterns.md
    mcp-server-guide.md
    pm-agent-autonomous-reflection.md
    suggested-commands.md
    troubleshooting.md
  research/  (24 files)
    complete-python-skills-migration.md
    intelligent-execution-architecture.md
    llm-agent-token-efficiency-2025.md
    markdown-to-python-migration-plan.md
    mcp-installer-fix-summary.md
    parallel-execution-complete-findings.md
    parallel-execution-findings.md
    phase1-implementation-strategy.md
    pm-mode-performance-analysis.md
    pm-mode-validation-methodology.md
    pm-skills-migration-results.md
    pm_agent_roi_analysis_2025-10-21.md
    python_src_layout_research_20251021.md
    reflexion-integration-2025.md
    repository-understanding-proposal.md
    research_git_branch_integration_2025.md
    research_installer_improvements_20251017.md
    research_oss_fork_workflow_2025.md
    research_python_directory_naming_20251015.md
    research_python_directory_naming_automation_2025.md
    research_repository_scoped_memory_2025-10-16.md
    research_serena_mcp_2025-01-16.md
    skills-migration-test.md
    task-tool-parallel-execution-results.md
  sessions/  (1 files)
    2025-10-14-summary.md
  testing/  (2 files)
    pm-workflow-test-results.md
    procedures.md
  troubleshooting/  (1 files)
    serena-installation.md
  user-guide/  (9 files)
    agents.md
    claude-code-integration.md
    commands.md
    flags.md
    mcp-installation.md
    mcp-servers.md
    memory-system.md
    modes.md
    session-management.md
  user-guide-jp/  (6 files)
    agents.md
    commands.md
    flags.md
    mcp-servers.md
    modes.md
    session-management.md
  user-guide-kr/  (6 files)
    agents.md
    commands.md
    flags.md
    mcp-servers.md
    modes.md
    session-management.md
  user-guide-zh/  (6 files)
    agents.md
    commands.md
    flags.md
    mcp-servers.md
    modes.md
    session-management.md
  PR_STRATEGY.md
  README.md
  capability-mapping-v5.md
  next-refactor-plan.md
  plugin-reorg.md
  pm-agent-implementation-status.md
plugins/  (93 files)
  superclaude/  (93 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (20 files)
      … 20 files under this directory
    commands/  (30 files)
      … 30 files under this directory
    core/  (6 files)
      … 6 files under this directory
    examples/  (1 files)
      … 1 files under this directory
    hooks/  (1 files)
      … 1 files under this directory
    mcp/  (16 files)
      … 16 files under this directory
    modes/  (7 files)
      … 7 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    skills/  (7 files)
      … 7 files under this directory
    .mcp.json
    README.md
scripts/  (8 files)
  README.md
  ab_test_workflows.py
  analyze_workflow_metrics.py
  build_superclaude_plugin.py
  cleanup.sh
  publish.sh
  sync_from_framework.py
  uninstall_legacy.sh
skills/  (2 files)
  confidence-check/  (2 files)
    SKILL.md
    confidence.ts
src/  (122 files)
  superclaude/  (122 files)
    agents/  (22 files)
      … 22 files under this directory
    cli/  (6 files)
      … 6 files under this directory
    commands/  (32 files)
      … 32 files under this directory
    core/  (7 files)
      … 7 files under this directory
    examples/  (2 files)
      … 2 files under this directory
    execution/  (4 files)
      … 4 files under this directory
    hooks/  (3 files)
      … 3 files under this directory
    mcp/  (22 files)
      … 22 files under this directory
    modes/  (8 files)
      … 8 files under this directory
    pm_agent/  (5 files)
      … 5 files under this directory
    scripts/  (4 files)
      … 4 files under this directory
    skills/  (4 files)
      … 4 files under this directory
    __init__.py
    __version__.py
    pytest_plugin.py
tests/  (15 files)
  integration/  (3 files)
    __init__.py
    test_execution_engine.py
    test_pytest_plugin.py
  unit/  (10 files)
    __init__.py
    test_cli_install.py
    test_confidence.py
    test_install_mcp_registry.py
    test_parallel.py
    test_reflection.py
    test_reflexion.py
    test_self_check.py
    test_self_correction.py
    test_token_budget.py
  __init__.py
  conftest.py
.env.example
.gitignore
.pre-commit-config.yaml
AGENTS.md
CHANGELOG.md
CLAUDE.md
CODEOWNERS
CODE_OF_CONDUCT.md
CONTRIBUTING.md
DELETION_RATIONALE.md
KNOWLEDGE.md
LICENSE
MANIFEST.in
Makefile
PARALLEL_INDEXING_PLAN.md
PLANNING.md
PLUGIN_INSTALL.md
PROJECT_INDEX.json
PROJECT_INDEX.md
PR_DOCUMENTATION.md
QUALITY_COMPARISON.md
README-ja.md
README-kr.md
README-zh.md
… 9 more files
```

## Entry points

- [src/superclaude/cli/main.py](https://github.com/SuperClaude-Org/SuperClaude_Framework/blob/fe68862c8ed9e2afb8120c2d9e27d0c3a7ce73a2/src/superclaude/cli/main.py)
- [src/superclaude/execution/parallel.py:334](https://github.com/SuperClaude-Org/SuperClaude_Framework/blob/fe68862c8ed9e2afb8120c2d9e27d0c3a7ce73a2/src/superclaude/execution/parallel.py#L334)
- [src/superclaude/scripts/clean_command_names.py:167](https://github.com/SuperClaude-Org/SuperClaude_Framework/blob/fe68862c8ed9e2afb8120c2d9e27d0c3a7ce73a2/src/superclaude/scripts/clean_command_names.py#L167)
- [plugins/superclaude/scripts/clean_command_names.py:166](https://github.com/SuperClaude-Org/SuperClaude_Framework/blob/fe68862c8ed9e2afb8120c2d9e27d0c3a7ce73a2/plugins/superclaude/scripts/clean_command_names.py#L166)
- [scripts/ab_test_workflows.py:309](https://github.com/SuperClaude-Org/SuperClaude_Framework/blob/fe68862c8ed9e2afb8120c2d9e27d0c3a7ce73a2/scripts/ab_test_workflows.py#L309)
- [scripts/analyze_workflow_metrics.py:330](https://github.com/SuperClaude-Org/SuperClaude_Framework/blob/fe68862c8ed9e2afb8120c2d9e27d0c3a7ce73a2/scripts/analyze_workflow_metrics.py#L330)
- [scripts/build_superclaude_plugin.py:96](https://github.com/SuperClaude-Org/SuperClaude_Framework/blob/fe68862c8ed9e2afb8120c2d9e27d0c3a7ce73a2/scripts/build_superclaude_plugin.py#L96)
- [scripts/sync_from_framework.py:958](https://github.com/SuperClaude-Org/SuperClaude_Framework/blob/fe68862c8ed9e2afb8120c2d9e27d0c3a7ce73a2/scripts/sync_from_framework.py#L958)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 28 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 8 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: ABTestAnalyzer, ContentTransformer, ExecutionPlan, FileSyncer, FrameworkSyncer, McpMerger.… |
| plugins package | library | Observed | Groups 2 file(s) under plugins package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 3 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 1 file(s) under service / domain layer (observed from repository paths and static analysis). |
| skills package | library | Observed | Groups 1 file(s) under skills package (observed from repository paths and static analysis). |
| superclaude package | library | Observed | Groups 27 file(s) under superclaude package (observed from repository paths and static analysis). Observed top-level classes: ConfidenceChecker, ConfidenceScore, FailureEntry, ReflectionEngine, ReflectionResult, Reflexi… |
| Tests | test | Observed | Groups 22 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: TestConfidenceChecker, TestConvenienceFunctions, TestFailureEntry, TestInstallCommands, TestInstallCommands… |

## Important files

- `.claude/settings.json` (config)
- `.env.example` (config)
- `.github/FUNDING.yml` (config)
- `.github/workflows/README.md` (ci)
- `.github/workflows/publish-pypi.yml` (ci)
- `.github/workflows/pull-sync-framework.yml` (ci)
- `.github/workflows/quick-check.yml` (ci)
- `.github/workflows/readme-quality-check.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `MANIFEST.in` (manifest)
- `PROJECT_INDEX.json` (config)
- `package.json` (manifest)
- `plugins/superclaude/.claude-plugin/plugin.json` (config)
- `plugins/superclaude/.mcp.json` (config)
- `plugins/superclaude/hooks/hooks.json` (config)
- `plugins/superclaude/mcp/configs/context7.json` (config)
- `plugins/superclaude/mcp/configs/magic.json` (config)
- `plugins/superclaude/mcp/configs/morphllm.json` (config)
- `plugins/superclaude/mcp/configs/playwright.json` (config)
- `plugins/superclaude/mcp/configs/sequential.json` (config)
- `plugins/superclaude/mcp/configs/serena-docker.json` (config)
- `plugins/superclaude/mcp/configs/serena.json` (config)
- `plugins/superclaude/mcp/configs/tavily.json` (config)
- `pyproject.toml` (manifest)
- `setup.py` (manifest)
- `src/superclaude/hooks/hooks.json` (config)
- `src/superclaude/mcp/configs/airis-agent.json` (config)
- `src/superclaude/mcp/configs/context7.json` (config)
- `src/superclaude/mcp/configs/magic.json` (config)
- `src/superclaude/mcp/configs/mindbase.json` (config)
- `src/superclaude/mcp/configs/morphllm.json` (config)
- `src/superclaude/mcp/configs/playwright.json` (config)
- `src/superclaude/mcp/configs/sequential.json` (config)
- `src/superclaude/mcp/configs/serena-docker.json` (config)
- `src/superclaude/mcp/configs/serena.json` (config)
- `src/superclaude/mcp/configs/tavily.json` (config)

## Top-level layout

- `docs` — 126 analysed file(s)
- `src` — 122 analysed file(s)
- `plugins` — 93 analysed file(s)
- `(root files)` — 33 analysed file(s)
- `tests` — 15 analysed file(s)
- `.github` — 8 analysed file(s)
- `scripts` — 8 analysed file(s)
- `.claude` — 3 analysed file(s)
- `skills` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `fe68862c8ed9e2afb8120c2d9e27d0c3a7ce73a2` is the revision these paths and observations refer to.
