# Project structure: coleam00/context-engineering-intro

**Analysed commit:** `a2d84b021cee1e2f4e77ba854bba0be8cb319035`

**Commit reference:** [a2d84b021cee1e2f4e77ba854bba0be8cb319035](https://github.com/coleam00/context-engineering-intro/commit/a2d84b021cee1e2f4e77ba854bba0be8cb319035)

**Tree at this commit:** [coleam00/context-engineering-intro@a2d84b021cee](https://github.com/coleam00/context-engineering-intro/tree/a2d84b021cee1e2f4e77ba854bba0be8cb319035)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | coleam00/context-engineering-intro |
| Description | Context engineering is the new vibe coding - it's the way to actually make AI coding assistants work. Claude Code is the best for this so that's what this repo is centered around, but you can apply this strategy with any AI coding assistant! |
| Stars | 13913 |
| Forks | 2704 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `a2d84b021cee1e2f4e77ba854bba0be8cb319035` |
| Retrieved at | 2026-11-14T19:09:38.894609+00:00 |
| Files in this snapshot | 242 |

## Directory tree

```text
.claude/  (3 files)
  commands/  (2 files)
    execute-prp.md
    generate-prp.md
  settings.local.json
PRPs/  (2 files)
  templates/  (1 files)
    prp_base.md
  EXAMPLE_multi_agent_prp.md
claude-code-full-guide/  (21 files)
  .claude/  (12 files)
    agents/  (2 files)
      … 2 files under this directory
    commands/  (6 files)
      … 6 files under this directory
    hooks/  (3 files)
      … 3 files under this directory
    settings.local.json
  .devcontainer/  (3 files)
    Dockerfile
    devcontainer.json
    init-firewall.sh
  PRPs/  (2 files)
    templates/  (1 files)
      … 1 files under this directory
    EXAMPLE_multi_agent_prp.md
  CLAUDE.md
  INITIAL.md
  README.md
  install_claude_code_windows.md
examples/  (1 files)
  .gitkeep
use-cases/  (205 files)
  agent-factory-with-subagents/  (104 files)
    .claude/  (6 files)
      … 6 files under this directory
    PRPs/  (2 files)
      … 2 files under this directory
    agents/  (51 files)
      … 51 files under this directory
    examples/  (41 files)
      … 41 files under this directory
    .gitignore
    CLAUDE.md
    README.md
    SAMPLE_PROMPT.md
  ai-coding-wisc-framework/  (23 files)
    .claude/  (22 files)
      … 22 files under this directory
    README.md
  ai-coding-workflows-foundation/  (6 files)
    agents/  (2 files)
      … 2 files under this directory
    commands/  (3 files)
      … 3 files under this directory
    README.md
  build-with-agent-team/  (3 files)
    example-plan/  (1 files)
      … 1 files under this directory
    README.md
    SKILL.md
  mcp-server/  (41 files)
    .claude/  (3 files)
      … 3 files under this directory
    PRPs/  (5 files)
      … 5 files under this directory
    examples/  (2 files)
      … 2 files under this directory
    src/  (9 files)
      … 9 files under this directory
    tests/  (12 files)
      … 12 files under this directory
    .dev.vars.example
    .gitignore
    .prettierrc
    CLAUDE.md
    README.md
    copy_template.py
    package.json
    tsconfig.json
    vitest.config.js
    wrangler.jsonc
  pydantic-ai/  (19 files)
    .claude/  (2 files)
      … 2 files under this directory
    PRPs/  (2 files)
      … 2 files under this directory
    examples/  (12 files)
      … 12 files under this directory
    CLAUDE.md
    README.md
    copy_template.py
  template-generator/  (9 files)
    .claude/  (3 files)
      … 3 files under this directory
    PRPs/  (4 files)
      … 4 files under this directory
    CLAUDE.md
    README.md
validation/  (3 files)
  README.md
  example-validate.md
  ultimate_validate_command.md
.gitattributes
.gitignore
CLAUDE.md
INITIAL.md
INITIAL_EXAMPLE.md
LICENSE
README.md
```

## Entry points

- [use-cases/agent-factory-with-subagents/agents/rag_agent/cli.py:288](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/use-cases/agent-factory-with-subagents/agents/rag_agent/cli.py#L288)
- [use-cases/agent-factory-with-subagents/agents/rag_agent/ingestion/chunker.py:517](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/use-cases/agent-factory-with-subagents/agents/rag_agent/ingestion/chunker.py#L517)
- [use-cases/agent-factory-with-subagents/agents/rag_agent/ingestion/embedder.py:417](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/use-cases/agent-factory-with-subagents/agents/rag_agent/ingestion/embedder.py#L417)
- [use-cases/agent-factory-with-subagents/agents/rag_agent/ingestion/ingest.py:433](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/use-cases/agent-factory-with-subagents/agents/rag_agent/ingestion/ingest.py#L433)
- [use-cases/mcp-server/copy_template.py:361](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/use-cases/mcp-server/copy_template.py#L361)
- [use-cases/pydantic-ai/copy_template.py:290](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/use-cases/pydantic-ai/copy_template.py#L290)
- [use-cases/mcp-server/src/index.ts](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/use-cases/mcp-server/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| claude-code-full-guide package | library | Observed | Groups 2 file(s) under claude-code-full-guide package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 17 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: Settings. Observed top-level functions: load_settings. |
| Data layer | data | Observed | Groups 7 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AgentContext, AgentDependencies, AgentResponse, BraveSearchResult, ChatMessage, ChatResponse. |
| Application entry point | entrypoint | Observed | Groups 17 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: AnalysisDependencies, ChunkingConfig, ConversationContext, DataAnalysisReport, DataInsigh… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 22 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: TestAgentBasicFunctionality, TestAgentBasics, TestAgentDependencies, TestAgentErrorHandling, TestAgentError… |
| use-cases package | library | Observed | Groups 27 file(s) under use-cases package (observed from repository paths and static analysis). Observed top-level classes: AgentDependencies, DatabasePool, ResearchAgentDependencies, SearchResult. Observed top-level fu… |

## Important files

- `.claude/settings.local.json` (config)
- `claude-code-full-guide/.claude/hooks/example-hook-config.json` (config)
- `claude-code-full-guide/.claude/settings.local.json` (config)
- `claude-code-full-guide/.devcontainer/Dockerfile` (container)
- `claude-code-full-guide/.devcontainer/devcontainer.json` (config)
- `use-cases/agent-factory-with-subagents/.claude/settings.local.json` (config)
- `use-cases/agent-factory-with-subagents/agents/rag_agent/.env.example` (config)
- `use-cases/agent-factory-with-subagents/examples/main_agent_reference/.env.example` (config)
- `use-cases/agent-factory-with-subagents/examples/testing_examples/pytest.ini` (config)
- `use-cases/mcp-server/.claude/settings.local.json` (config)
- `use-cases/mcp-server/package.json` (manifest)
- `use-cases/mcp-server/tsconfig.json` (config)
- `use-cases/pydantic-ai/examples/main_agent_reference/.env.example` (config)
- `use-cases/pydantic-ai/examples/testing_examples/pytest.ini` (config)
- `use-cases/template-generator/.claude/settings.local.json` (config)

## Top-level layout

- `use-cases` — 205 analysed file(s)
- `claude-code-full-guide` — 21 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `.claude` — 3 analysed file(s)
- `validation` — 3 analysed file(s)
- `PRPs` — 2 analysed file(s)
- `examples` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `a2d84b021cee1e2f4e77ba854bba0be8cb319035` is the revision these paths and observations refer to.
