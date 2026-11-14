# Project structure: oraios/serena

**Analysed commit:** `6b39542bb108ce77901072deac699d770b302d52`

**Commit reference:** [6b39542bb108ce77901072deac699d770b302d52](https://github.com/oraios/serena/commit/6b39542bb108ce77901072deac699d770b302d52)

**Tree at this commit:** [oraios/serena@6b39542bb108](https://github.com/oraios/serena/tree/6b39542bb108ce77901072deac699d770b302d52)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | oraios/serena |
| Description | A powerful MCP toolkit for coding, providing semantic retrieval and editing capabilities  - the IDE for your agent |
| Stars | 31377 |
| Forks | 2141 |
| Licence | Other |
| Language | Python |
| Default branch | main |
| Analysed commit | `6b39542bb108ce77901072deac699d770b302d52` |
| Retrieved at | 2026-11-14T19:07:08.171170+00:00 |
| Files in this snapshot | 796 |

## Directory tree

```text
.devcontainer/  (1 files)
  devcontainer.json
.github/  (15 files)
  ISSUE_TEMPLATE/  (3 files)
    config.yml
    feature_request.md
    issue--bug--performance-problem--question-.md
  workflows/  (9 files)
    codeql.yml
    codespell.yml
    create-release.yml
    docker.yml
    docs.yaml
    publish.yml
    pytest.yml
    python-versions.yml
    scorecard.yml
  FUNDING.yml
  copilot-instructions.md
  pull_request_template.md
.serena/  (10 files)
  memories/  (8 files)
    adding_new_language_support_guide.md
    creating_pull_requests.md
    critical_info.md
    memory_maintenance.md
    project_structure.md
    repl.md
    task_completion.md
    trusted_projects.md
  .gitignore
  project.yml
.vscode/  (1 files)
  settings.json
LICENSES/  (2 files)
  GPL-3.0-or-later.txt
  MIT.txt
docs/  (44 files)
  01-about/  (6 files)
    .gitignore
    020_programming-languages.md
    030_serena-in-action.md
    050_acknowledgements.md
    060_license.md
    070_privacy.md
  02-usage/  (12 files)
    000_intro.md
    010_installation.md
    020_running.md
    025_jetbrains_plugin.md
    030_clients.md
    040_workflow.md
    045_memories.md
    050_configuration.md
    060_dashboard.md
    065_logs.md
    070_security.md
    999_additional-usage.md
  03-special-guides/  (10 files)
    000_intro.md
    cpp_setup.md
    custom_agent.md
    external_language_server_registration.md
    godot_gdscript_setup_guide_for_serena.md
    groovy_setup_guide_for_serena.md
    ocaml_setup_guide_for_serena.md
    scala_setup_guide_for_serena.md
    serena_on_chatgpt.md
    unreal_engine_setup_guide_for_serena.md
  04-evaluation/  (11 files)
    020_prompts/  (3 files)
      … 3 files under this directory
    030_results/  (6 files)
      … 6 files under this directory
    000_evaluation-intro.md
    010_methodology.md
  .gitignore
  _config.yml
  autogen_docs.py
  create_toc.py
  index.md
news/  (14 files)
  20260111.html
  20260303.html
  20260321.html
  20260330.html
  20260404.html
  20260411.html
  20260414.html
  20260427.html
  20260512.html
  20260716.html
  20260718.html
  20260809.html
  20261013.html
  20261019.html
resources/  (1 files)
  serena-block-diagram.svg
scripts/  (21 files)
  add_spdx_headers.py
  agno_agent.py
  build_news_json.py
  bump_version.py
  demo_cli_call.py
  demo_diagnostics.py
  demo_find_defining_symbol.py
  demo_find_implementing_symbol.py
  demo_progressive_tool_shortening.py
  demo_run_tools.py
  gen_prompt_factory.py
  gen_tool_capabilities.py
  live_test_grok.py
  mcp_server.py
  memory_graph.py
  print_language_list.py
  print_mode_context_options.py
  print_tool_overview.py
  profile_search_text.py
  profile_tool_call.py
  update_downloaded_dependency_hashes.py
src/  (235 files)
  interprompt/  (8 files)
    util/  (2 files)
      … 2 files under this directory
    .syncCommitId.remote
    .syncCommitId.this
    __init__.py
    jinja_template.py
    multilang_prompt.py
    prompt_factory.py
  serena/  (117 files)
    config/  (5 files)
      … 5 files under this directory
    dashboard/  (3 files)
      … 3 files under this directory
    generated/  (2 files)
      … 2 files under this directory
    jetbrains/  (4 files)
      … 4 files under this directory
    lsp/  (2 files)
      … 2 files under this directory
    memories/  (2 files)
      … 2 files under this directory
    olb/  (1 files)
      … 1 files under this directory
    repl/  (12 files)
      … 12 files under this directory
    resources/  (38 files)
      … 38 files under this directory
    tools/  (11 files)
      … 11 files under this directory
    util/  (19 files)
      … 19 files under this directory
    __init__.py
    agent.py
    agno.py
    analytics.py
    cli.py
    code_editor.py
    constants.py
    gui_log_viewer.py
    hooks.py
    language_backend.py
    ls_manager.py
    mcp.py
    project.py
    project_server.py
    prompt_factory.py
    session.py
    symbol.py
    task_executor.py
  solidlsp/  (109 files)
    language_servers/  (88 files)
      … 88 files under this directory
    lsp_protocol_handler/  (3 files)
      … 3 files under this directory
    resources/  (1 files)
      … 1 files under this directory
    util/  (5 files)
      … 5 files under this directory
    .gitignore
    __init__.py
    dependency_provider.py
    initialize_params.py
    ls.py
    ls_config.py
    ls_exceptions.py
    ls_process.py
    ls_request.py
    ls_types.py
    ls_utils.py
    settings.py
  README.md
test/  (430 files)
  resources/  (428 files)
    repos/  (428 files)
      … 428 files under this directory
  __init__.py
  conftest.py
.dockerignore
.env.example
.gitattributes
.gitignore
AGENTS.md
CHANGELOG.md
CLA.md
CLAUDE.md
CONTRIBUTING.md
DOCKER.md
Dockerfile
LICENSE
README-dev.md
README.md
compose.yaml
docker_build_and_run.sh
flake.lock
flake.nix
pyproject.toml
repo_dir_sync.py
server.json
sync.py
```

## Entry points

- [src/serena/cli.py](https://github.com/oraios/serena/blob/6b39542bb108ce77901072deac699d770b302d52/src/serena/cli.py)
- [src/serena/cli.py](https://github.com/oraios/serena/blob/6b39542bb108ce77901072deac699d770b302d52/src/serena/cli.py)
- [src/serena/hooks.py](https://github.com/oraios/serena/blob/6b39542bb108ce77901072deac699d770b302d52/src/serena/hooks.py)
- [src/solidlsp/language_servers/msl_lsp_server.py:439](https://github.com/oraios/serena/blob/6b39542bb108ce77901072deac699d770b302d52/src/solidlsp/language_servers/msl_lsp_server.py#L439)
- [scripts/add_spdx_headers.py:94](https://github.com/oraios/serena/blob/6b39542bb108ce77901072deac699d770b302d52/scripts/add_spdx_headers.py#L94)
- [scripts/agno_agent.py:33](https://github.com/oraios/serena/blob/6b39542bb108ce77901072deac699d770b302d52/scripts/agno_agent.py#L33)
- [scripts/build_news_json.py:45](https://github.com/oraios/serena/blob/6b39542bb108ce77901072deac699d770b302d52/scripts/build_news_json.py#L45)
- [scripts/bump_version.py:38](https://github.com/oraios/serena/blob/6b39542bb108ce77901072deac699d770b302d52/scripts/bump_version.py#L38)
- [scripts/demo_cli_call.py:5](https://github.com/oraios/serena/blob/6b39542bb108ce77901072deac699d770b302d52/scripts/demo_cli_call.py#L5)
- [scripts/demo_diagnostics.py:79](https://github.com/oraios/serena/blob/6b39542bb108ce77901072deac699d770b302d52/scripts/demo_diagnostics.py#L79)
- [scripts/demo_find_defining_symbol.py:68](https://github.com/oraios/serena/blob/6b39542bb108ce77901072deac699d770b302d52/scripts/demo_find_defining_symbol.py#L68)
- [scripts/demo_find_implementing_symbol.py:53](https://github.com/oraios/serena/blob/6b39542bb108ce77901072deac699d770b302d52/scripts/demo_find_implementing_symbol.py#L53)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 8 file(s) under api layer (observed from repository paths and static analysis). Observed top-level classes: ConfigApi, DirectoryListing, DirectoryListingRenderer, EditApi, ExternalProjectContextManager, ExternalP… |
| Configuration and deployment | config | Observed | Groups 48 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: AgentInterface, ApiInclusionDefinition, ClientSetupHandler, ClientSetupHandlerClaude… |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). Observed top-level classes: LibRepo, OtherRepo. Observed top-level functions: call, execute, gitCommit, gitCommitWithMessageFromF… |
| Application entry point | entrypoint | Observed | Groups 24 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: AbortError, CheckResult, CommandResult, ContextCommands, GrokLiveTest, LSPError. Observed… |
| External integrations | external | Observed | Groups 2 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: APIError, ConnectionError, JetBrainsPluginClient, JetBrainsPluginClientManager, MatchedClien… |
| interprompt package | library | Observed | Groups 6 file(s) under interprompt package (observed from repository paths and static analysis). Observed top-level classes: JinjaTemplate, LanguageFallbackMode, MultiLangPromptCollection, MultiLangPromptList, MultiLang… |
| serena package | library | Observed | Groups 64 file(s) under serena package (observed from repository paths and static analysis). Observed top-level classes: ActivateProjectTool, ActiveModes, AnthropicTokenCount, ApiScope, ApplyMethodProtocol, AutoRegister… |
| solidlsp package | library | Observed | Groups 100 file(s) under solidlsp package (observed from repository paths and static analysis). Observed top-level classes: ALLanguageServer, AdaLanguageServer, AngularLanguageServer, AngularTypeScriptServer, AnsibleLan… |
| Tests | test | Observed | Groups 430 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: Auditable, BaseModel, BaseModule, BaseProcessor, BaseService, ClassWillBeOverwritten. Observed top-level f… |

## Important files

- `.devcontainer/devcontainer.json` (config)
- `.dockerignore` (container)
- `.env.example` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/codeql.yml` (ci)
- `.github/workflows/codespell.yml` (ci)
- `.github/workflows/create-release.yml` (ci)
- `.github/workflows/docker.yml` (ci)
- `.github/workflows/docs.yaml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.github/workflows/pytest.yml` (ci)
- `.github/workflows/python-versions.yml` (ci)
- `.github/workflows/scorecard.yml` (ci)
- `.serena/project.yml` (config)
- `.vscode/settings.json` (config)
- `Dockerfile` (container)
- `compose.yaml` (container)
- `docs/_config.yml` (config)
- `pyproject.toml` (manifest)
- `server.json` (config)
- `src/serena/resources/config/contexts/agent.yml` (config)
- `src/serena/resources/config/contexts/antigravity.yml` (config)
- `src/serena/resources/config/contexts/chatgpt.yml` (config)
- `src/serena/resources/config/contexts/claude-code.yml` (config)
- `src/serena/resources/config/contexts/codebuddy.yml` (config)
- `src/serena/resources/config/contexts/codex.yml` (config)
- `src/serena/resources/config/contexts/context.template.yml` (config)
- `src/serena/resources/config/contexts/copilot-cli.yml` (config)
- `src/serena/resources/config/contexts/desktop-app.yml` (config)
- `src/serena/resources/config/contexts/grok.yml` (config)
- `src/serena/resources/config/contexts/ide.yml` (config)
- `src/serena/resources/config/contexts/jb-ai-assistant.yml` (config)
- `src/serena/resources/config/contexts/jb-copilot-plugin.yml` (config)
- `src/serena/resources/config/contexts/junie.yml` (config)
- `src/serena/resources/config/contexts/oaicompat-agent.yml` (config)
- `src/serena/resources/config/contexts/vscode.yml` (config)
- `src/serena/resources/config/contexts/zcode.yml` (config)
- `src/serena/resources/config/internal_modes/jetbrains.yml` (config)
- `src/serena/resources/config/modes/benchmark.yml` (config)
- `src/serena/resources/config/modes/editing.yml` (config)
- `src/serena/resources/config/modes/interactive.yml` (config)
- `src/serena/resources/config/modes/mode.template.yml` (config)
- `src/serena/resources/config/modes/no-memories.yml` (config)
- `src/serena/resources/config/modes/no-onboarding.yml` (config)
- `src/serena/resources/config/modes/onboarding.yml` (config)
- `src/serena/resources/config/modes/one-shot.yml` (config)
- `src/serena/resources/config/modes/planning.yml` (config)
- `src/serena/resources/config/modes/query-projects.yml` (config)
- `src/serena/resources/config/prompt_templates/info_prompts.yml` (config)
- `src/serena/resources/config/prompt_templates/simple_tool_outputs.yml` (config)
- `src/serena/resources/config/prompt_templates/system_prompt.yml` (config)
- `src/serena/resources/project.local.template.yml` (config)
- `src/serena/resources/project.template.yml` (config)
- `src/serena/resources/serena_config.template.yml` (config)
- `src/solidlsp/language_servers/omnisharp/initialize_params.json` (config)
- `src/solidlsp/language_servers/omnisharp/runtime_dependencies.json` (config)
- `src/solidlsp/language_servers/omnisharp/workspace_did_change_configuration.json` (config)
- `src/solidlsp/resources/downloaded_dependency_hashes.json` (config)

## Top-level layout

- `test` — 430 analysed file(s)
- `src` — 235 analysed file(s)
- `docs` — 44 analysed file(s)
- `(root files)` — 22 analysed file(s)
- `scripts` — 21 analysed file(s)
- `.github` — 15 analysed file(s)
- `news` — 14 analysed file(s)
- `.serena` — 10 analysed file(s)
- `LICENSES` — 2 analysed file(s)
- `.devcontainer` — 1 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `resources` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 4 file(s) were skipped during inventory (4 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `6b39542bb108ce77901072deac699d770b302d52` is the revision these paths and observations refer to.
