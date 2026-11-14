# Project structure: shareAI-lab/learn-claude-code

**Analysed commit:** `7226f555d48900076eba126acf37c9ed5f002b5d`

**Commit reference:** [7226f555d48900076eba126acf37c9ed5f002b5d](https://github.com/shareAI-lab/learn-claude-code/commit/7226f555d48900076eba126acf37c9ed5f002b5d)

**Tree at this commit:** [shareAI-lab/learn-claude-code@7226f555d489](https://github.com/shareAI-lab/learn-claude-code/tree/7226f555d48900076eba126acf37c9ed5f002b5d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | shareAI-lab/learn-claude-code |
| Description | Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1 |
| Stars | 80407 |
| Forks | 12856 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `7226f555d48900076eba126acf37c9ed5f002b5d` |
| Retrieved at | 2026-11-14T19:06:10.227932+00:00 |
| Files in this snapshot | 413 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (2 files)
    ci.yml
    test.yml
agents/  (14 files)
  __init__.py
  s01_agent_loop.py
  s02_tool_use.py
  s03_todo_write.py
  s04_subagent.py
  s05_skill_loading.py
  s06_context_compact.py
  s07_task_system.py
  s08_background_tasks.py
  s09_agent_teams.py
  s10_team_protocols.py
  s11_autonomous_agents.py
  s12_worktree_task_isolation.py
  s_full.py
docs/  (36 files)
  en/  (12 files)
    s01-the-agent-loop.md
    s02-tool-use.md
    s03-todo-write.md
    s04-subagent.md
    s05-skill-loading.md
    s06-context-compact.md
    s07-task-system.md
    s08-background-tasks.md
    s09-agent-teams.md
    s10-team-protocols.md
    s11-autonomous-agents.md
    s12-worktree-task-isolation.md
  ja/  (12 files)
    s01-the-agent-loop.md
    s02-tool-use.md
    s03-todo-write.md
    s04-subagent.md
    s05-skill-loading.md
    s06-context-compact.md
    s07-task-system.md
    s08-background-tasks.md
    s09-agent-teams.md
    s10-team-protocols.md
    s11-autonomous-agents.md
    s12-worktree-task-isolation.md
  zh/  (12 files)
    s01-the-agent-loop.md
    s02-tool-use.md
    s03-todo-write.md
    s04-subagent.md
    s05-skill-loading.md
    s06-context-compact.md
    s07-task-system.md
    s08-background-tasks.md
    s09-agent-teams.md
    s10-team-protocols.md
    s11-autonomous-agents.md
    s12-worktree-task-isolation.md
s01_agent_loop/  (7 files)
  images/  (3 files)
    agent-loop.en.svg
    agent-loop.ja.svg
    agent-loop.svg
  README.ja.md
  README.md
  README.zh.md
  code.py
s02_tool_use/  (7 files)
  images/  (3 files)
    tool-dispatch.en.svg
    tool-dispatch.ja.svg
    tool-dispatch.svg
  README.ja.md
  README.md
  README.zh.md
  code.py
s03_permission/  (10 files)
  images/  (6 files)
    permission-overview.en.svg
    permission-overview.ja.svg
    permission-overview.svg
    permission-pipeline.en.svg
    permission-pipeline.ja.svg
    permission-pipeline.svg
  README.ja.md
  README.md
  README.zh.md
  code.py
s04_hooks/  (7 files)
  images/  (3 files)
    hooks-overview.en.svg
    hooks-overview.ja.svg
    hooks-overview.svg
  README.ja.md
  README.md
  README.zh.md
  code.py
s05_todo_write/  (8 files)
  example/  (1 files)
    hello.py
  images/  (3 files)
    todo-overview.en.svg
    todo-overview.ja.svg
    todo-overview.svg
  README.ja.md
  README.md
  README.zh.md
  code.py
s06_subagent/  (7 files)
  images/  (3 files)
    subagent-overview.en.svg
    subagent-overview.ja.svg
    subagent-overview.svg
  README.ja.md
  README.md
  README.zh.md
  code.py
s07_skill_loading/  (7 files)
  images/  (3 files)
    skill-overview.en.svg
    skill-overview.ja.svg
    skill-overview.svg
  README.ja.md
  README.md
  README.zh.md
  code.py
s08_context_compact/  (19 files)
  images/  (15 files)
    auto-compact.en.svg
    auto-compact.ja.svg
    auto-compact.svg
    compact-overview.en.svg
    compact-overview.ja.svg
    compact-overview.svg
    compaction-layers.en.svg
    compaction-layers.ja.svg
    compaction-layers.svg
    layer1-budget.en.svg
    layer1-budget.ja.svg
    layer1-budget.svg
    micro-compact.en.svg
    micro-compact.ja.svg
    micro-compact.svg
  README.ja.md
  README.md
  README.zh.md
  code.py
s09_memory/  (10 files)
  images/  (6 files)
    memory-overview.en.svg
    memory-overview.ja.svg
    memory-overview.svg
    memory-subsystems.en.svg
    memory-subsystems.ja.svg
    memory-subsystems.svg
  README.ja.md
  README.md
  README.zh.md
  code.py
s10_task_system/  (10 files)
  images/  (6 files)
    task-dag.en.svg
    task-dag.ja.svg
    task-dag.svg
    task-system-overview.en.svg
    task-system-overview.ja.svg
    task-system-overview.svg
  README.ja.md
  README.md
  README.zh.md
  code.py
s11_background_tasks/  (7 files)
  images/  (3 files)
    background-tasks-overview.en.svg
    background-tasks-overview.ja.svg
    background-tasks-overview.svg
  README.ja.md
  README.md
  README.zh.md
  code.py
s12_cron_scheduler/  (7 files)
  images/  (3 files)
    cron-scheduler-overview.en.svg
    cron-scheduler-overview.ja.svg
    cron-scheduler-overview.svg
  README.ja.md
  README.md
  README.zh.md
  code.py
s13_agent_teams/  (13 files)
  images/  (9 files)
    agent-teams-overview.en.svg
    agent-teams-overview.ja.svg
    agent-teams-overview.svg
    team-protocols-overview.en.svg
    team-protocols-overview.ja.svg
    team-protocols-overview.svg
    team-topology.en.svg
    team-topology.ja.svg
    team-topology.svg
  README.ja.md
  README.md
  README.zh.md
  code.py
s14_mcp_plugin/  (7 files)
  images/  (3 files)
    mcp-architecture.en.svg
    mcp-architecture.ja.svg
    mcp-architecture.svg
  README.ja.md
  README.md
  README.zh.md
  code.py
s15_integrated_harness/  (7 files)
  images/  (3 files)
    system-architecture.en.svg
    system-architecture.ja.svg
    system-architecture.svg
  README.ja.md
  README.md
  README.zh.md
  code.py
s16_workflow_runtime/  (5 files)
  images/  (1 files)
    workflow-runtime-overview.svg
  README.ja.md
  README.md
  README.zh.md
  code.py
s17_goal_loop/  (5 files)
  images/  (1 files)
    goal-loop-overview.svg
  README.ja.md
  README.md
  README.zh.md
  code.py
skills/  (9 files)
  agent-builder/  (6 files)
    references/  (4 files)
      … 4 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    SKILL.md
  code-review/  (1 files)
    SKILL.md
  mcp-builder/  (1 files)
    SKILL.md
  pdf/  (1 files)
    SKILL.md
tests/  (21 files)
  test_agent_loop_boundaries.py
  test_agent_teams_runtime.py
  test_agents_smoke.py
  test_background_tasks.py
  test_chapter_readmes.py
  test_compaction_tool_pairs.py
  test_cron_scheduler.py
  test_goal_loop.py
  test_permission_command_words.py
  test_readline_prompts.py
  test_repl_quit_commands.py
  test_s06_subagent.py
  test_s08_context_compact.py
  test_s_full_background.py
  test_skill_loading.py
  test_subprocess_output_encoding.py
  test_task_system.py
  test_todo_write_string_input.py
  test_utf8_text_io.py
  test_web_scenarios.py
  test_workflow_goal_lessons.py
web/  (180 files)
  public/  (79 files)
    course-assets/  (74 files)
      … 74 files under this directory
    file.svg
    globe.svg
    next.svg
    vercel.svg
    window.svg
  scripts/  (1 files)
    extract-content.ts
  src/  (93 files)
    app/  (12 files)
      … 12 files under this directory
    components/  (35 files)
      … 35 files under this directory
    data/  (35 files)
      … 35 files under this directory
    hooks/  (3 files)
      … 3 files under this directory
    i18n/  (3 files)
      … 3 files under this directory
    lib/  (4 files)
      … 4 files under this directory
    types/  (1 files)
      … 1 files under this directory
  .gitignore
  README.md
  next.config.ts
  package.json
  postcss.config.mjs
  tsconfig.json
  vercel.json
.env.example
.gitignore
CONTRIBUTING.md
LICENSE
README-ja.md
README-zh.md
README.md
requirements.txt
```

## Entry points

- [agents/s01_agent_loop.py:104](https://github.com/shareAI-lab/learn-claude-code/blob/7226f555d48900076eba126acf37c9ed5f002b5d/agents/s01_agent_loop.py#L104)
- [agents/s02_tool_use.py:141](https://github.com/shareAI-lab/learn-claude-code/blob/7226f555d48900076eba126acf37c9ed5f002b5d/agents/s02_tool_use.py#L141)
- [agents/s03_todo_write.py:201](https://github.com/shareAI-lab/learn-claude-code/blob/7226f555d48900076eba126acf37c9ed5f002b5d/agents/s03_todo_write.py#L201)
- [agents/s04_subagent.py:177](https://github.com/shareAI-lab/learn-claude-code/blob/7226f555d48900076eba126acf37c9ed5f002b5d/agents/s04_subagent.py#L177)
- [agents/s05_skill_loading.py:217](https://github.com/shareAI-lab/learn-claude-code/blob/7226f555d48900076eba126acf37c9ed5f002b5d/agents/s05_skill_loading.py#L217)
- [agents/s06_context_compact.py:252](https://github.com/shareAI-lab/learn-claude-code/blob/7226f555d48900076eba126acf37c9ed5f002b5d/agents/s06_context_compact.py#L252)
- [agents/s07_task_system.py:233](https://github.com/shareAI-lab/learn-claude-code/blob/7226f555d48900076eba126acf37c9ed5f002b5d/agents/s07_task_system.py#L233)
- [agents/s08_background_tasks.py:251](https://github.com/shareAI-lab/learn-claude-code/blob/7226f555d48900076eba126acf37c9ed5f002b5d/agents/s08_background_tasks.py#L251)
- [agents/s09_agent_teams.py:388](https://github.com/shareAI-lab/learn-claude-code/blob/7226f555d48900076eba126acf37c9ed5f002b5d/agents/s09_agent_teams.py#L388)
- [agents/s10_team_protocols.py:469](https://github.com/shareAI-lab/learn-claude-code/blob/7226f555d48900076eba126acf37c9ed5f002b5d/agents/s10_team_protocols.py#L469)
- [agents/s11_autonomous_agents.py:561](https://github.com/shareAI-lab/learn-claude-code/blob/7226f555d48900076eba126acf37c9ed5f002b5d/agents/s11_autonomous_agents.py#L561)
- [agents/s12_worktree_task_isolation.py:768](https://github.com/shareAI-lab/learn-claude-code/blob/7226f555d48900076eba126acf37c9ed5f002b5d/agents/s12_worktree_task_isolation.py#L768)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| agents package | library | Observed | Groups 1 file(s) under agents package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 41 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 32 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: AgentSession, AnthropicAgentRunner, BackgroundManager, Budget, ConsoleBroker, ContextComp… |
| s05_todo_write package | library | Observed | Groups 1 file(s) under s05_todo_write package (observed from repository paths and static analysis). Observed top-level functions: greet. |
| skills package | library | Observed | Groups 2 file(s) under skills package (observed from repository paths and static analysis). Observed top-level functions: execute_tool, get_agent_descriptions, get_tools_for_agent, run_bash, run_edit_file, run_read_file. |
| Tests | test | Observed | Groups 21 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: AgentTeamsRuntimeTests, BackgroundManagerTests, CompactionToolPairTests, FakeClient, FakeMessages, FakeMess… |
| web package | library | Observed | Groups 56 file(s) under web package (observed from repository paths and static analysis). |

## Important files

- `.env.example` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `requirements.txt` (manifest)
- `web/package.json` (manifest)
- `web/src/data/annotations/s01.json` (config)
- `web/src/data/annotations/s02.json` (config)
- `web/src/data/annotations/s03.json` (config)
- `web/src/data/annotations/s04.json` (config)
- `web/src/data/annotations/s05.json` (config)
- `web/src/data/annotations/s06.json` (config)
- `web/src/data/annotations/s07.json` (config)
- `web/src/data/annotations/s08.json` (config)
- `web/src/data/annotations/s09.json` (config)
- `web/src/data/annotations/s10.json` (config)
- `web/src/data/annotations/s11.json` (config)
- `web/src/data/annotations/s12.json` (config)
- `web/src/data/annotations/s13.json` (config)
- `web/src/data/annotations/s14.json` (config)
- `web/src/data/annotations/s15.json` (config)
- `web/src/data/annotations/s16.json` (config)
- `web/src/data/annotations/s17.json` (config)
- `web/src/data/scenarios/s01.json` (config)
- `web/src/data/scenarios/s02.json` (config)
- `web/src/data/scenarios/s03.json` (config)
- `web/src/data/scenarios/s04.json` (config)
- `web/src/data/scenarios/s05.json` (config)
- `web/src/data/scenarios/s06.json` (config)
- `web/src/data/scenarios/s07.json` (config)
- `web/src/data/scenarios/s08.json` (config)
- `web/src/data/scenarios/s09.json` (config)
- `web/src/data/scenarios/s10.json` (config)
- `web/src/data/scenarios/s11.json` (config)
- `web/src/data/scenarios/s12.json` (config)
- `web/src/data/scenarios/s13.json` (config)
- `web/src/data/scenarios/s14.json` (config)
- `web/src/data/scenarios/s15.json` (config)
- `web/src/data/scenarios/s16.json` (config)
- `web/src/data/scenarios/s17.json` (config)
- `web/src/i18n/messages/en.json` (config)
- `web/src/i18n/messages/ja.json` (config)
- `web/src/i18n/messages/zh.json` (config)
- `web/tsconfig.json` (config)
- `web/vercel.json` (config)

## Top-level layout

- `web` — 180 analysed file(s)
- `docs` — 36 analysed file(s)
- `tests` — 21 analysed file(s)
- `s08_context_compact` — 19 analysed file(s)
- `agents` — 14 analysed file(s)
- `s13_agent_teams` — 13 analysed file(s)
- `s03_permission` — 10 analysed file(s)
- `s09_memory` — 10 analysed file(s)
- `s10_task_system` — 10 analysed file(s)
- `skills` — 9 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `s05_todo_write` — 8 analysed file(s)
- `s01_agent_loop` — 7 analysed file(s)
- `s02_tool_use` — 7 analysed file(s)
- `s04_hooks` — 7 analysed file(s)
- `s06_subagent` — 7 analysed file(s)
- `s07_skill_loading` — 7 analysed file(s)
- `s11_background_tasks` — 7 analysed file(s)
- `s12_cron_scheduler` — 7 analysed file(s)
- `s14_mcp_plugin` — 7 analysed file(s)
- `s15_integrated_harness` — 7 analysed file(s)
- `s16_workflow_runtime` — 5 analysed file(s)
- `s17_goal_loop` — 5 analysed file(s)
- `.github` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `7226f555d48900076eba126acf37c9ed5f002b5d` is the revision these paths and observations refer to.
