# Project structure: stitionai/devika

**Analysed commit:** `80bb343cbe4a4e5f5a0ba08d2524920139baceb6`

**Commit reference:** [80bb343cbe4a4e5f5a0ba08d2524920139baceb6](https://github.com/stitionai/devika/commit/80bb343cbe4a4e5f5a0ba08d2524920139baceb6)

**Tree at this commit:** [stitionai/devika@80bb343cbe4a](https://github.com/stitionai/devika/tree/80bb343cbe4a4e5f5a0ba08d2524920139baceb6)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | stitionai/devika |
| Description | Devika is the first open-source implementation of an Agentic Software Engineer. Initially started as an open-source alternative to Devin. |
| Stars | 19546 |
| Forks | 2566 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `80bb343cbe4a4e5f5a0ba08d2524920139baceb6` |
| Retrieved at | 2026-11-14T19:08:10.566273+00:00 |
| Files in this snapshot | 155 |

## Directory tree

```text
.github/  (4 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    feature_request.md
    issue.md
  pull_request_template.md
benchmarks/  (2 files)
  BENCHMARKS.md
  SWE-bench.md
docs/  (5 files)
  Installation/  (2 files)
    ollama.md
    search_engine.md
  architecture/  (3 files)
    ARCHITECTURE.md
    README.md
    UNDER_THE_HOOD.md
src/  (83 files)
  agents/  (39 files)
    action/  (3 files)
      … 3 files under this directory
    answer/  (3 files)
      … 3 files under this directory
    coder/  (3 files)
      … 3 files under this directory
    decision/  (3 files)
      … 3 files under this directory
    feature/  (3 files)
      … 3 files under this directory
    formatter/  (3 files)
      … 3 files under this directory
    internal_monologue/  (3 files)
      … 3 files under this directory
    patcher/  (3 files)
      … 3 files under this directory
    planner/  (3 files)
      … 3 files under this directory
    reporter/  (3 files)
      … 3 files under this directory
    researcher/  (3 files)
      … 3 files under this directory
    runner/  (4 files)
      … 4 files under this directory
    __init__.py
    agent.py
  apis/  (1 files)
    project.py
  bert/  (1 files)
    sentence.py
  browser/  (4 files)
    __init__.py
    browser.py
    interaction.py
    search.py
  documenter/  (3 files)
    graphwiz.py
    pdf.py
    uml.py
  experts/  (8 files)
    __UNIMPLEMENTED__
    chemistry.py
    game-dev.py
    math.py
    medical.py
    physics.py
    stackoverflow.py
    web-design.py
  filesystem/  (2 files)
    __init__.py
    read_code.py
  llm/  (9 files)
    __init__.py
    claude_client.py
    gemini_client.py
    groq_client.py
    llm.py
    lm_studio_client.py
    mistral_client.py
    ollama_client.py
    openai_client.py
  memory/  (3 files)
    __init__.py
    knowledge_base.py
    rag.py
  sandbox/  (2 files)
    code_runner.py
    firejail.py
  services/  (5 files)
    __init__.py
    git.py
    github.py
    netlify.py
    utils.py
  config.py
  init.py
  logger.py
  project.py
  socket_instance.py
  state.py
ui/  (47 files)
  src/  (38 files)
    lib/  (31 files)
      … 31 files under this directory
    routes/  (5 files)
      … 5 files under this directory
    app.html
    app.pcss
  static/  (2 files)
    assets/  (2 files)
      … 2 files under this directory
  .gitignore
  components.json
  package.json
  postcss.config.cjs
  svelte.config.js
  tailwind.config.js
  vite.config.js
.gitignore
ARCHITECTURE.md
CONTRIBUTING.md
LICENSE
Makefile
README.md
ROADMAP.md
app.dockerfile
devika.dockerfile
devika.py
docker-compose.yaml
requirements.txt
sample.config.toml
setup.sh
```

## Entry points

- [devika.py:28](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/devika.py#L28)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| agents package | library | Observed | Groups 26 file(s) under agents package (observed from repository paths and static analysis). Observed top-level classes: Action, Agent, Answer, Coder, Decision, Feature. |
| API layer | api | Observed | Groups 6 file(s) under api layer (observed from repository paths and static analysis). Observed routes: ROUTE /api/get-project-files, ROUTE /api/create-project, ROUTE /api/delete-project, ROUTE /api/download-project, RO… |
| bert package | library | Observed | Groups 1 file(s) under bert package (observed from repository paths and static analysis). Observed top-level classes: SentenceBert. |
| browser package | library | Observed | Groups 4 file(s) under browser package (observed from repository paths and static analysis). Observed top-level classes: BingSearch, Browser, Crawler, DuckDuckGoSearch, GoogleSearch. Observed top-level functions: start_… |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: Config. |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| documenter package | library | Observed | Groups 3 file(s) under documenter package (observed from repository paths and static analysis). Observed top-level classes: PDF. |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Flask. Observed routes: ROUTE /api/data, ROUTE /api/messages, ROUTE /api/is-ag… |
| experts package | library | Observed | Groups 7 file(s) under experts package (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 7 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: Claude, Gemini, Groq, LMStudio, MistralAi, Ollama. |
| filesystem package | library | Observed | Groups 2 file(s) under filesystem package (observed from repository paths and static analysis). Observed top-level classes: ReadCode. |
| init.py package | library | Observed | Groups 1 file(s) under init.py package (observed from repository paths and static analysis). Observed top-level functions: init_devika. |
| llm package | library | Observed | Groups 2 file(s) under llm package (observed from repository paths and static analysis). Observed top-level classes: LLM. |
| logger.py package | library | Observed | Groups 1 file(s) under logger.py package (observed from repository paths and static analysis). Observed top-level classes: Logger. Observed top-level functions: route_logger. |
| memory package | library | Observed | Groups 3 file(s) under memory package (observed from repository paths and static analysis). Observed top-level classes: Knowledge, KnowledgeBase. |
| project.py package | library | Observed | Groups 1 file(s) under project.py package (observed from repository paths and static analysis). Observed top-level classes: ProjectManager, Projects. |
| sandbox package | library | Observed | Groups 2 file(s) under sandbox package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 5 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: Git, GitHub, InvalidResponseError, Netlify. Observed top-level functions: retry_wrapper, va… |
| socket_instance.py package | library | Observed | Groups 1 file(s) under socket_instance.py package (observed from repository paths and static analysis). Observed top-level functions: emit_agent. |
| state.py package | library | Observed | Groups 1 file(s) under state.py package (observed from repository paths and static analysis). Observed top-level classes: AgentState, AgentStateModel. |
| ui package | library | Observed | Groups 35 file(s) under ui package (observed from repository paths and static analysis). |

## Important files

- `docker-compose.yaml` (container)
- `requirements.txt` (manifest)
- `sample.config.toml` (config)
- `ui/components.json` (config)
- `ui/package.json` (manifest)

## Top-level layout

- `src` — 83 analysed file(s)
- `ui` — 47 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `docs` — 5 analysed file(s)
- `.github` — 4 analysed file(s)
- `benchmarks` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `80bb343cbe4a4e5f5a0ba08d2524920139baceb6` is the revision these paths and observations refer to.
