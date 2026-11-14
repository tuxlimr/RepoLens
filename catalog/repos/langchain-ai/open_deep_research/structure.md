# Project structure: langchain-ai/open_deep_research

**Analysed commit:** `1b7d2e80db9faa586165c60e09096dbbfd483a64`

**Commit reference:** [1b7d2e80db9faa586165c60e09096dbbfd483a64](https://github.com/langchain-ai/open_deep_research/commit/1b7d2e80db9faa586165c60e09096dbbfd483a64)

**Tree at this commit:** [langchain-ai/open_deep_research@1b7d2e80db9f](https://github.com/langchain-ai/open_deep_research/tree/1b7d2e80db9faa586165c60e09096dbbfd483a64)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | langchain-ai/open_deep_research |
| Description | Not provided |
| Stars | 12677 |
| Forks | 1863 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `1b7d2e80db9faa586165c60e09096dbbfd483a64` |
| Retrieved at | 2026-11-14T19:10:02.656739+00:00 |
| Files in this snapshot | 41 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (2 files)
    claude-code-review.yml
    claude.yml
  dependabot.yml
examples/  (4 files)
  arxiv.md
  inference-market-gpt45.md
  inference-market.md
  pubmed.md
src/  (21 files)
  legacy/  (15 files)
    files/  (1 files)
      … 1 files under this directory
    tests/  (3 files)
      … 3 files under this directory
    CLAUDE.md
    __init__.py
    configuration.py
    graph.ipynb
    graph.py
    legacy.md
    multi_agent.ipynb
    multi_agent.py
    prompts.py
    state.py
    utils.py
  open_deep_research/  (5 files)
    configuration.py
    deep_researcher.py
    prompts.py
    state.py
    utils.py
  security/  (1 files)
    auth.py
tests/  (6 files)
  evaluators.py
  extract_langsmith_data.py
  pairwise_evaluation.py
  prompts.py
  run_evaluate.py
  supervisor_parallel_evaluation.py
.env.example
.gitignore
CLAUDE.md
LICENSE
README.md
langgraph.json
pyproject.toml
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| legacy package | library | Observed | Groups 7 file(s) under legacy package (observed from repository paths and static analysis). Observed top-level classes: Conclusion, Configuration, Feedback, FinishReport, FinishResearch, Introduction. Observed top-level… |
| open_deep_research package | library | Observed | Groups 5 file(s) under open_deep_research package (observed from repository paths and static analysis). Observed top-level classes: AgentInputState, AgentState, ClarifyWithUser, ConductResearch, Configuration, MCPConfig… |
| security package | library | Observed | Groups 1 file(s) under security package (observed from repository paths and static analysis). Observed top-level functions: authorize_store, get_current_user, on_assistants_create, on_assistants_read, on_thread_create,… |
| Tests | test | Observed | Groups 9 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: CompletenessScore, CorrectnessScore, CriteriaGrade, GroundednessClaim, GroundednessScore, HeadToHeadRanking.… |

## Important files

- `.env.example` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/claude-code-review.yml` (ci)
- `.github/workflows/claude.yml` (ci)
- `langgraph.json` (config)
- `pyproject.toml` (manifest)

## Top-level layout

- `src` — 21 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `tests` — 6 analysed file(s)
- `examples` — 4 analysed file(s)
- `.github` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- The GitHub repository was marked archived at selection time.

Commit `1b7d2e80db9faa586165c60e09096dbbfd483a64` is the revision these paths and observations refer to.
