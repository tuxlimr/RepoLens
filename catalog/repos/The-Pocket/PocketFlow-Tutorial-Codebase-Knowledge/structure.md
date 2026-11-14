# Project structure: The-Pocket/PocketFlow-Tutorial-Codebase-Knowledge

**Analysed commit:** `05b24cbbb0fe409c5e23c9791f0342f07524ffdc`

**Commit reference:** [05b24cbbb0fe409c5e23c9791f0342f07524ffdc](https://github.com/The-Pocket/PocketFlow-Tutorial-Codebase-Knowledge/commit/05b24cbbb0fe409c5e23c9791f0342f07524ffdc)

**Tree at this commit:** [The-Pocket/PocketFlow-Tutorial-Codebase-Knowledge@05b24cbbb0fe](https://github.com/The-Pocket/PocketFlow-Tutorial-Codebase-Knowledge/tree/05b24cbbb0fe409c5e23c9791f0342f07524ffdc)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | The-Pocket/PocketFlow-Tutorial-Codebase-Knowledge |
| Description | Pocket Flow: Codebase to Tutorial |
| Stars | 12759 |
| Forks | 1437 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `05b24cbbb0fe409c5e23c9791f0342f07524ffdc` |
| Retrieved at | 2026-11-14T19:09:59.452235+00:00 |
| Files in this snapshot | 204 |

## Directory tree

```text
docs/  (187 files)
  AutoGen Core/  (9 files)
    01_agent.md
    02_messaging_system__topic___subscription_.md
    03_agentruntime.md
    04_tool.md
    05_chatcompletionclient.md
    06_chatcompletioncontext.md
    07_memory.md
    08_component.md
    index.md
  Browser Use/  (9 files)
    01_agent.md
    02_system_prompt.md
    03_browsercontext.md
    04_dom_representation.md
    05_action_controller___registry.md
    06_message_manager.md
    07_data_structures__views_.md
    08_telemetry_service.md
    index.md
  Celery/  (11 files)
    01_celery_app.md
    02_configuration.md
    03_task.md
    04_broker_connection__amqp_.md
    05_worker.md
    06_result_backend.md
    07_beat__scheduler_.md
    08_canvas__signatures___primitives_.md
    09_events.md
    10_bootsteps.md
    index.md
  Click/  (8 files)
    01_command___group.md
    02_decorators.md
    03_parameter__option___argument_.md
    04_paramtype.md
    05_context.md
    06_term_ui__terminal_user_interface_.md
    07_click_exceptions.md
    index.md
  Codex/  (9 files)
    01_terminal_ui__ink_components_.md
    02_input_handling__textbuffer_editor_.md
    03_agent_loop.md
    04_approval_policy___security.md
    05_response___tool_call_handling.md
    06_command_execution___sandboxing.md
    07_configuration_management.md
    08_single_pass_mode.md
    index.md
  Crawl4AI/  (11 files)
    01_asynccrawlerstrategy.md
    02_asyncwebcrawler.md
    03_crawlerrunconfig.md
    04_contentscrapingstrategy.md
    05_relevantcontentfilter.md
    06_extractionstrategy.md
    07_crawlresult.md
    08_deepcrawlstrategy.md
    09_cachecontext___cachemode.md
    10_basedispatcher.md
    index.md
  CrewAI/  (9 files)
    01_crew.md
    02_agent.md
    03_task.md
    04_tool.md
    05_process.md
    06_llm.md
    07_memory.md
    08_knowledge.md
    index.md
  DSPy/  (11 files)
    01_module___program.md
    02_signature.md
    03_example.md
    04_predict.md
    05_lm__language_model_client_.md
    06_rm__retrieval_model_client_.md
    07_evaluate.md
    08_teleprompter___optimizer.md
    09_adapter.md
    10_settings.md
    index.md
  FastAPI/  (9 files)
    01_fastapi_application___routing.md
    02_path_operations___parameter_declaration.md
    03_data_validation___serialization__pydantic_.md
    04_openapi___automatic_docs.md
    05_dependency_injection.md
    06_error_handling.md
    07_security_utilities.md
    08_background_tasks.md
    index.md
  Flask/  (9 files)
    01_application_object___flask__.md
    02_routing_system.md
    03_request_and_response_objects.md
    04_templating__jinja2_integration_.md
    05_context_globals___current_app____request____session____g__.md
    06_configuration___config__.md
    07_application_and_request_contexts.md
    08_blueprints.md
    index.md
  Google A2A/  (10 files)
    01_agent_card.md
    02_task.md
    03_a2a_protocol___core_types.md
    04_a2a_server_implementation.md
    05_a2a_client_implementation.md
    06_task_handling_logic__server_side_.md
    07_streaming_communication__sse_.md
    08_multi_agent_orchestration__host_agent_.md
    09_demo_ui_application___service.md
    index.md
  LangGraph/  (7 files)
    01_graph___stategraph.md
    02_nodes___pregelnode__.md
    03_channels.md
    04_control_flow_primitives___branch____send____interrupt__.md
    05_pregel_execution_engine.md
    06_checkpointer___basecheckpointsaver__.md
    index.md
  LevelDB/  (10 files)
    01_table___sstable___tablecache.md
    02_memtable.md
    03_write_ahead_log__wal____logwriter_logreader.md
    04_dbimpl.md
    05_writebatch.md
    06_version___versionset.md
    07_iterator.md
    08_compaction.md
    09_internalkey___dbformat.md
    index.md
  MCP Python SDK/  (10 files)
    01_cli___mcp__command_.md
    02_fastmcp_server___fastmcp__.md
    03_fastmcp_resources___resource____resourcemanager__.md
    04_fastmcp_tools___tool____toolmanager__.md
    05_fastmcp_prompts___prompt____promptmanager__.md
    06_fastmcp_context___context__.md
    07_mcp_protocol_types.md
    08_client_server_sessions___clientsession____serversession__.md
    09_communication_transports__stdio__sse__websocket__memory_.md
    index.md
  NumPy Core/  (9 files)
    01_ndarray__n_dimensional_array_.md
    02_dtype__data_type_object_.md
    03_ufunc__universal_function_.md
    04_numeric_types___numerictypes__.md
    05_array_printing___arrayprint__.md
    06_multiarray_module.md
    07_umath_module.md
    08___array_function___protocol___overrides___overrides__.md
    index.md
  OpenManus/  (10 files)
    01_llm.md
    02_message___memory.md
    03_baseagent.md
    04_tool___toolcollection.md
    05_baseflow.md
    06_schema.md
    07_configuration__config_.md
    08_dockersandbox.md
    09_mcp__model_context_protocol_.md
    index.md
  PocketFlow/  (8 files)
    01_shared_state___shared__dictionary__.md
    02_node___basenode____node____asyncnode___.md
    03_actions___transitions_.md
    04_flow___flow____asyncflow___.md
    05_asynchronous_processing___asyncnode____asyncflow___.md
    06_batch_processing___batchnode____batchflow____asyncparallelbatchnode___.md
    07_a2a__agent_to_agent__communication_framework_.md
    index.md
  Pydantic Core/  (7 files)
    01_basemodel.md
    02_fields__fieldinfo___field_function_.md
    03_configuration__configdict___configwrapper_.md
    04_custom_logic__decorators___annotated_helpers_.md
    05_core_schema___validation_serialization.md
    06_typeadapter.md
    index.md
  Requests/  (9 files)
    01_functional_api.md
    02_request___response_models.md
    03_session.md
    04_cookie_jar.md
    05_authentication_handlers.md
    06_exception_hierarchy.md
    07_transport_adapters.md
    08_hook_system.md
    index.md
  SmolaAgents/  (9 files)
    01_multistepagent.md
    02_model_interface.md
    03_tool.md
    04_agentmemory.md
    05_prompttemplates.md
    06_pythonexecutor.md
    07_agenttype.md
    08_agentlogger___monitor.md
    index.md
  _config.yml
  design.md
  index.md
utils/  (4 files)
  __init__.py
  call_llm.py
  crawl_github_files.py
  crawl_local_files.py
.clinerules
.cursorrules
.dockerignore
.env.sample
.gitignore
.windsurfrules
Dockerfile
LICENSE
README.md
flow.py
main.py
nodes.py
requirements.txt
```

## Entry points

- [main.py:110](https://github.com/The-Pocket/PocketFlow-Tutorial-Codebase-Knowledge/blob/05b24cbbb0fe409c5e23c9791f0342f07524ffdc/main.py#L110)
- [utils/call_llm.py:179](https://github.com/The-Pocket/PocketFlow-Tutorial-Codebase-Knowledge/blob/05b24cbbb0fe409c5e23c9791f0342f07524ffdc/utils/call_llm.py#L179)
- [utils/crawl_github_files.py:346](https://github.com/The-Pocket/PocketFlow-Tutorial-Codebase-Knowledge/blob/05b24cbbb0fe409c5e23c9791f0342f07524ffdc/utils/crawl_github_files.py#L346)
- [utils/crawl_local_files.py:132](https://github.com/The-Pocket/PocketFlow-Tutorial-Codebase-Knowledge/blob/05b24cbbb0fe409c5e23c9791f0342f07524ffdc/utils/crawl_local_files.py#L132)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). Observed top-level classes: AnalyzeRelationships, CombineTutorial, FetchRepo, IdentifyAbstractions, OrderChapters, WriteChapters.… |
| Application entry point | entrypoint | Observed | Groups 4 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: _call_llm_gemini, _call_llm_provider, call_llm, crawl_github_files, crawl_local_files, g… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 1 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.env.sample` (config)
- `Dockerfile` (container)
- `docs/_config.yml` (config)
- `requirements.txt` (manifest)

## Top-level layout

- `docs` — 187 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `utils` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `05b24cbbb0fe409c5e23c9791f0342f07524ffdc` is the revision these paths and observations refer to.
