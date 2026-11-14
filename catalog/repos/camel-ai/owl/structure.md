# Project structure: camel-ai/owl

**Analysed commit:** `5dbabd348c87278060a9885ae3080e3d312eac84`

**Commit reference:** [5dbabd348c87278060a9885ae3080e3d312eac84](https://github.com/camel-ai/owl/commit/5dbabd348c87278060a9885ae3080e3d312eac84)

**Tree at this commit:** [camel-ai/owl@5dbabd348c87](https://github.com/camel-ai/owl/tree/5dbabd348c87278060a9885ae3080e3d312eac84)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | camel-ai/owl |
| Description | 🦉 OWL: Optimized Workforce Learning for General Multi-Agent Assistance in Real-World Task Automation |
| Stars | 20193 |
| Forks | 2287 |
| Licence | Not detected |
| Language | Python |
| Default branch | main |
| Analysed commit | `5dbabd348c87278060a9885ae3080e3d312eac84` |
| Retrieved at | 2026-11-14T19:08:03.945858+00:00 |
| Files in this snapshot | 131 |

## Directory tree

```text
.container/  (11 files)
  .dockerignore
  DOCKER_README.md
  DOCKER_README_en.md
  Dockerfile
  build_docker.bat
  build_docker.sh
  check_docker.bat
  check_docker.sh
  docker-compose.yml
  run_in_docker.bat
  run_in_docker.sh
.github/  (2 files)
  workflows/  (2 files)
    codespell.yml
    docker-build.yml
community_usecase/  (88 files)
  Airbnb-MCP/  (3 files)
    Airbnb_MCP.py
    README.md
    mcp_servers_config.json
  Mcp_use_case/  (3 files)
    Content_curator.py
    Readme.md
    mcp_servers_config.json
  Notion-MCP/  (3 files)
    README.md
    mcp_servers_config.json
    notion_manager.py
  OWL Interview Preparation Assistant/  (9 files)
    config/  (1 files)
      … 1 files under this directory
    .env.template
    .gitignore
    PROJECT_DESCRIPTION.md
    README.md
    app.py
    logging_utils.py
    main.py
    requirements.txt
  PHI_Sanitization_Summarization_and_Article_Writing/  (2 files)
    project.py
    readme.md
  Puppeteer MCP/  (4 files)
    README.md
    demo.py
    mcp_servers_config.json
    requirements.txt
  Whatsapp-MCP/  (3 files)
    README.md
    app.py
    mcp_servers_config.json
  a_share_investment_agent_camel/  (28 files)
    src/  (22 files)
      … 22 files under this directory
    .env.example
    Dockerfile
    LICENSE
    README.md
    README_EN.md
    requirements.txt
  cooking-assistant/  (2 files)
    README.md
    run_gpt4o.py
  excel_analyzer/  (4 files)
    README.md
    README_zh.md
    data_analyzer_en.py
    data_analyzer_zh.py
  learning-assistant/  (2 files)
    README.md
    run_gpt4o.py
  qwen3_mcp/  (3 files)
    README.md
    mcp_sse_config.json
    run_mcp_qwen3.py
  resume-analysis-assistant/  (4 files)
    README.md
    mcp_servers_config.json
    resume_analysis.md
    run_mcp.py
  stock-analysis/  (15 files)
    agent/  (1 files)
      … 1 files under this directory
    example/  (6 files)
      … 6 files under this directory
    tools/  (1 files)
      … 1 files under this directory
    .env.template
    .gitignore
    README-zh.md
    README.md
    prompts.py
    requirements.txt
    run.py
  virtual_fitting_room/  (2 files)
    readme.md
    run_gpt4o.py
  COMMUNITY_CALL_FOR_USE_CASES.md
examples/  (8 files)
  __init__.py
  run.py
  run_claude.py
  run_deepseek.py
  run_gemini.py
  run_groq.py
  run_qwen.py
  run_vllm.py
licenses/  (3 files)
  LICENSE
  license_template.txt
  update_license.py
owl/  (10 files)
  utils/  (5 files)
    __init__.py
    common.py
    document_toolkit.py
    enhanced_role_playing.py
    gaia.py
  .env_template
  webapp.py
  webapp_backup.py
  webapp_jp.py
  webapp_zh.py
.gitignore
.pre-commit-config.yaml
CITATION.cff
README.md
README_ja.md
README_zh.md
community_challenges.md
pyproject.toml
requirements.txt
```

## Entry points

- [community_usecase/a_share_investment_agent_camel/src/main.py:318](https://github.com/camel-ai/owl/blob/5dbabd348c87278060a9885ae3080e3d312eac84/community_usecase/a_share_investment_agent_camel/src/main.py#L318)
- [community_usecase/Airbnb-MCP/Airbnb_MCP.py:116](https://github.com/camel-ai/owl/blob/5dbabd348c87278060a9885ae3080e3d312eac84/community_usecase/Airbnb-MCP/Airbnb_MCP.py#L116)
- [community_usecase/Mcp_use_case/Content_curator.py:131](https://github.com/camel-ai/owl/blob/5dbabd348c87278060a9885ae3080e3d312eac84/community_usecase/Mcp_use_case/Content_curator.py#L131)
- [community_usecase/Notion-MCP/notion_manager.py:126](https://github.com/camel-ai/owl/blob/5dbabd348c87278060a9885ae3080e3d312eac84/community_usecase/Notion-MCP/notion_manager.py#L126)
- [community_usecase/OWL Interview Preparation Assistant/app.py:454](https://github.com/camel-ai/owl/blob/5dbabd348c87278060a9885ae3080e3d312eac84/community_usecase/OWL%20Interview%20Preparation%20Assistant/app.py#L454)
- [community_usecase/OWL Interview Preparation Assistant/main.py:328](https://github.com/camel-ai/owl/blob/5dbabd348c87278060a9885ae3080e3d312eac84/community_usecase/OWL%20Interview%20Preparation%20Assistant/main.py#L328)
- [community_usecase/PHI_Sanitization_Summarization_and_Article_Writing/project.py:150](https://github.com/camel-ai/owl/blob/5dbabd348c87278060a9885ae3080e3d312eac84/community_usecase/PHI_Sanitization_Summarization_and_Article_Writing/project.py#L150)
- [community_usecase/Puppeteer MCP/demo.py:111](https://github.com/camel-ai/owl/blob/5dbabd348c87278060a9885ae3080e3d312eac84/community_usecase/Puppeteer%20MCP/demo.py#L111)
- [community_usecase/Whatsapp-MCP/app.py:171](https://github.com/camel-ai/owl/blob/5dbabd348c87278060a9885ae3080e3d312eac84/community_usecase/Whatsapp-MCP/app.py#L171)
- [community_usecase/cooking-assistant/run_gpt4o.py:175](https://github.com/camel-ai/owl/blob/5dbabd348c87278060a9885ae3080e3d312eac84/community_usecase/cooking-assistant/run_gpt4o.py#L175)
- [community_usecase/excel_analyzer/data_analyzer_en.py:263](https://github.com/camel-ai/owl/blob/5dbabd348c87278060a9885ae3080e3d312eac84/community_usecase/excel_analyzer/data_analyzer_en.py#L263)
- [community_usecase/excel_analyzer/data_analyzer_zh.py:308](https://github.com/camel-ai/owl/blob/5dbabd348c87278060a9885ae3080e3d312eac84/community_usecase/excel_analyzer/data_analyzer_zh.py#L308)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| community_usecase package | library | Observed | Groups 22 file(s) under community_usecase package (observed from repository paths and static analysis). Observed top-level classes: BaseAgent, DebateRoomAgent, EnhancedStreamlitLogHandler, FundamentalsAnalystAgent, Inve… |
| Configuration and deployment | config | Observed | Groups 21 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: get_company_research_prompt, get_preparation_plan_prompt, get_question_generator_p… |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AnalysisSignal, DateTimeEncoder, Portfolio, ResearchReport, RiskAnalysis, StockData. |
| Application entry point | entrypoint | Observed | Groups 24 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: ExcelRolePalying, SECToolkit, StreamlitLogHandler. Observed top-level functions: add_env_… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| owl package | library | Observed | Groups 5 file(s) under owl package (observed from repository paths and static analysis). Observed top-level classes: DocumentProcessingToolkit, GAIABenchmark, OwlGAIARolePlaying, OwlRolePlaying. Observed top-level funct… |

## Important files

- `.container/.dockerignore` (container)
- `.container/Dockerfile` (container)
- `.container/docker-compose.yml` (container)
- `.github/workflows/codespell.yml` (ci)
- `.github/workflows/docker-build.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `community_usecase/Airbnb-MCP/mcp_servers_config.json` (config)
- `community_usecase/Mcp_use_case/mcp_servers_config.json` (config)
- `community_usecase/Notion-MCP/mcp_servers_config.json` (config)
- `community_usecase/OWL Interview Preparation Assistant/.env.template` (config)
- `community_usecase/OWL Interview Preparation Assistant/requirements.txt` (manifest)
- `community_usecase/Puppeteer MCP/mcp_servers_config.json` (config)
- `community_usecase/Puppeteer MCP/requirements.txt` (manifest)
- `community_usecase/Whatsapp-MCP/mcp_servers_config.json` (config)
- `community_usecase/a_share_investment_agent_camel/.env.example` (config)
- `community_usecase/a_share_investment_agent_camel/Dockerfile` (container)
- `community_usecase/a_share_investment_agent_camel/requirements.txt` (manifest)
- `community_usecase/qwen3_mcp/mcp_sse_config.json` (config)
- `community_usecase/resume-analysis-assistant/mcp_servers_config.json` (config)
- `community_usecase/stock-analysis/.env.template` (config)
- `community_usecase/stock-analysis/example/Alibaba/Alibaba_chat_history.json` (config)
- `community_usecase/stock-analysis/example/Apple/Apple_chat_history.json` (config)
- `community_usecase/stock-analysis/example/Google/Google_chat_history.json` (config)
- `community_usecase/stock-analysis/requirements.txt` (manifest)
- `pyproject.toml` (manifest)
- `requirements.txt` (manifest)

## Top-level layout

- `community_usecase` — 88 analysed file(s)
- `.container` — 11 analysed file(s)
- `owl` — 10 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `examples` — 8 analysed file(s)
- `licenses` — 3 analysed file(s)
- `.github` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `5dbabd348c87278060a9885ae3080e3d312eac84` is the revision these paths and observations refer to.
