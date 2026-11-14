# Project structure: maurosoria/dirsearch

**Analysed commit:** `461705af2688ab6644b1f2bf738c46c55ee4d3da`

**Commit reference:** [461705af2688ab6644b1f2bf738c46c55ee4d3da](https://github.com/maurosoria/dirsearch/commit/461705af2688ab6644b1f2bf738c46c55ee4d3da)

**Tree at this commit:** [maurosoria/dirsearch@461705af2688](https://github.com/maurosoria/dirsearch/tree/461705af2688ab6644b1f2bf738c46c55ee4d3da)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | maurosoria/dirsearch |
| Description | Web path scanner |
| Stars | 15078 |
| Forks | 2462 |
| Licence | Not detected |
| Language | Python |
| Default branch | master |
| Analysed commit | `461705af2688ab6644b1f2bf738c46c55ee4d3da` |
| Retrieved at | 2026-11-14T19:09:08.160609+00:00 |
| Files in this snapshot | 376 |

## Directory tree

```text
.github/  (16 files)
  ISSUE_TEMPLATE/  (3 files)
    ask_question.md
    bug_report.md
    feature_request.md
  workflows/  (11 files)
    ci.yml
    codeql-analysis.yml
    docker-image.yml
    portable-builds.yml
    pyinstaller-linux.yml
    pyinstaller-macos-intel.yml
    pyinstaller-macos-silicon.yml
    pyinstaller-release-draft.yml
    pyinstaller-windows.yml
    rust-security.yml
    semgrep-analysis.yml
  FUNDING.yml
  pull_request_template.md
db/  (49 files)
  categories/  (37 files)
    coldfusion/  (1 files)
      … 1 files under this directory
    dotnet/  (3 files)
      … 3 files under this directory
    infra/  (3 files)
      … 3 files under this directory
    java/  (3 files)
      … 3 files under this directory
    node/  (1 files)
      … 1 files under this directory
    php/  (12 files)
      … 12 files under this directory
    python/  (3 files)
      … 3 files under this directory
    aggressive.txt
    backups.txt
    common.txt
    conf.txt
    db.txt
    extensions.txt
    generate_wpscan_wordlists.py
    keys.txt
    logs.txt
    vcs.txt
    web.txt
  templates/  (7 files)
    admin.txt
    api.txt
    auth.txt
    backups.txt
    crud.txt
    db.txt
    logs.txt
  400_blacklist.txt
  403_blacklist.txt
  500_blacklist.txt
  dicc.txt
  user-agents.txt
docs/  (33 files)
  building.md
  calibration-word-ownership.md
  configuration.md
  controller-lifecycle.md
  discovery-configuration.md
  execution-configuration.md
  filter-configuration.md
  index.md
  installation.md
  invocation-options.md
  logging-ownership.md
  native-backend-benchmarks.md
  options.md
  python-api.md
  refactoring-backlog.md
  references.md
  release-notes-v0.5.0.md
  report-configuration.md
  request-configuration.md
  request-target-ownership.md
  result-configuration.md
  run-configuration.md
  run-metadata.md
  run-resources.md
  … 9 more files
lib/  (89 files)
  connection/  (8 files)
    __init__.py
    ip_overrides.py
    native.py
    proxy.py
    rate_limiter.py
    request_target.py
    requester.py
    response.py
  controller/  (7 files)
    __init__.py
    controller.py
    event_loop.py
    run_resources.py
    session.py
    session_options.py
    session_snapshot.py
  core/  (35 files)
    __init__.py
    api.py
    decorators.py
    dictionary.py
    discovery_config.py
    exceptions.py
    execution_config.py
    filter_config.py
    filter_state.py
    filters.py
    fuzzer.py
    log_config.py
    logger.py
    native_builder.py
    native_runtime.py
    option_defaults.py
    options.py
    report_config.py
    request_backend.py
    request_config.py
    result_config.py
    run_config.py
    run_metadata.py
    scan_run_state.py
    … 11 more files
  parse/  (7 files)
    __init__.py
    cmdline.py
    config.py
    headers.py
    nmap.py
    rawrequest.py
    url.py
  report/  (17 files)
    templates/  (1 files)
      … 1 files under this directory
    __init__.py
    csv_report.py
    directory_response_store.py
    factory.py
    html_report.py
    json_report.py
    jsonl_response_store.py
    manager.py
    markdown_report.py
    mysql_report.py
    plain_text_report.py
    postgresql_report.py
    response_store.py
    simple_report.py
    sqlite_report.py
    xml_report.py
  utils/  (11 files)
    __init__.py
    cli.py
    command.py
    common.py
    crawl.py
    diff.py
    file.py
    mimetype.py
    random.py
    safe_xml.py
    schemedet.py
  view/  (3 files)
    __init__.py
    colors.py
    terminal.py
  __init__.py
native/  (22 files)
  src/  (18 files)
    chunks.rs
    compression.rs
    engine.rs
    filters.rs
    lib.rs
    ntlm.rs
    pacing.rs
    proxy.rs
    raw_client.rs
    raw_http.rs
    request_target.rs
    result.rs
    routing.rs
    scan.rs
    session.rs
    tests.rs
    transport.rs
    wordlist.rs
  .gitignore
  Cargo.toml
  README.md
  pyproject.toml
pyinstaller/  (4 files)
  .gitignore
  README.md
  build.sh
  dirsearch.spec
requirements/  (2 files)
  db.txt
  runtime.txt
scripts/  (4 files)
  build_native.py
  build_portable.py
  configure_stack.py
  split_wordlists.py
sessions/  (1 files)
  .gitkeep
tests/  (140 files)
  connection/  (17 files)
    __init__.py
    proxy_server.py
    test_async_proxy_environment_cli.py
    test_dns.py
    test_logging_ownership.py
    test_macos_proxy.py
    test_native_backend.py
    test_native_engine.py
    test_native_response.py
    test_proxy.py
    test_proxy_integration.py
    test_rate_limiter.py
    test_request_config.py
    test_request_target_ownership.py
    test_requester.py
    test_requester_rate.py
    test_response.py
  controller/  (37 files)
    __init__.py
    test_async_controller.py
    test_backend_e2e_contract.py
    test_calibration_e2e_contract.py
    test_cli_interrupt_contract.py
    test_controller_lifecycle.py
    test_discovery_config.py
    test_engine_selection.py
    test_execution_config.py
    test_filter_config.py
    test_invocation_options.py
    test_logging_ownership.py
    test_native_controller.py
    test_pause_state.py
    test_process_isolation.py
    test_progress_ownership.py
    test_redirect_recursion.py
    test_replay_lifecycle.py
    test_report_config.py
    test_request_config.py
    test_result_config.py
    test_root_crawl.py
    test_run_config.py
    test_run_resources.py
    … 13 more files
  core/  (41 files)
    __init__.py
    test_advanced_filters.py
    test_async_fuzzer.py
    test_backup_discovery.py
    test_calibration_words.py
    test_cli_output_streams.py
    test_cli_run_metadata.py
    test_constant_tables.py
    test_dictionary_concurrency.py
    test_dictionary_templates.py
    test_discovery_config.py
    test_dynamic_dictionary.py
    test_execution_config.py
    test_filter_config.py
    test_fuzzer_filter_stacks.py
    test_fuzzer_lifecycle.py
    test_importable_api.py
    test_logger.py
    test_native_builder.py
    test_native_fuzzer.py
    test_native_runtime.py
    test_numeric_option_validation.py
    test_options.py
    test_options_config_merge.py
    … 17 more files
  parse/  (7 files)
    __init__.py
    test_cmdline.py
    test_config.py
    test_headers.py
    test_nmap.py
    test_rawrequest.py
    test_url.py
  report/  (13 files)
    __init__.py
    test_atomic_file_reports.py
    test_file_report_portability.py
    test_html_report_template.py
    test_mysql_report.py
    test_report_command_redaction.py
    test_report_locking.py
    test_report_manager.py
    test_response_store.py
    test_run_metadata.py
    test_sql_report.py
    test_streaming_file_reports.py
    test_structured_file_reports.py
  static/  (4 files)
    nmap.xml
    raw.txt
    targets.txt
    wordlist.txt
  utils/  (13 files)
    __init__.py
    test_cli_interrupts.py
    test_command.py
    test_common.py
    test_crawl.py
    test_diff.py
    test_file.py
    test_mimetype.py
    test_random.py
    test_safe_xml.py
    test_schemedet.py
    test_terminal.py
    test_terminal_ownership.py
  __init__.py
  check_packaged_install.py
  test_docker_workflow.py
  test_native_install_packaging.py
  test_optional_db_dependencies.py
  test_release_scripts.py
  test_report_exception_handling.py
  test_test_discovery.py
.dockerignore
.gitignore
AGENTS.md
CHANGELOG.md
CONTRIBUTORS.md
Dockerfile
README.md
__init__.py
__main__.py
config.ini
dirsearch.py
pyproject.toml
requirements.txt
setup.cfg
setup.py
testing.py
```

## Entry points

- [__main__.py:4](https://github.com/maurosoria/dirsearch/blob/461705af2688ab6644b1f2bf738c46c55ee4d3da/__main__.py#L4)
- [db/categories/generate_wpscan_wordlists.py:76](https://github.com/maurosoria/dirsearch/blob/461705af2688ab6644b1f2bf738c46c55ee4d3da/db/categories/generate_wpscan_wordlists.py#L76)
- [db/categories/php/generate_wpscan_wordlists.py:45](https://github.com/maurosoria/dirsearch/blob/461705af2688ab6644b1f2bf738c46c55ee4d3da/db/categories/php/generate_wpscan_wordlists.py#L45)
- [dirsearch.py:87](https://github.com/maurosoria/dirsearch/blob/461705af2688ab6644b1f2bf738c46c55ee4d3da/dirsearch.py#L87)
- [lib/core/native_builder.py:204](https://github.com/maurosoria/dirsearch/blob/461705af2688ab6644b1f2bf738c46c55ee4d3da/lib/core/native_builder.py#L204)
- [scripts/build_native.py:137](https://github.com/maurosoria/dirsearch/blob/461705af2688ab6644b1f2bf738c46c55ee4d3da/scripts/build_native.py#L137)
- [scripts/build_portable.py:262](https://github.com/maurosoria/dirsearch/blob/461705af2688ab6644b1f2bf738c46c55ee4d3da/scripts/build_portable.py#L262)
- [scripts/configure_stack.py:53](https://github.com/maurosoria/dirsearch/blob/461705af2688ab6644b1f2bf738c46c55ee4d3da/scripts/configure_stack.py#L53)
- [scripts/split_wordlists.py:191](https://github.com/maurosoria/dirsearch/blob/461705af2688ab6644b1f2bf738c46c55ee4d3da/scripts/split_wordlists.py#L191)
- [testing.py:40](https://github.com/maurosoria/dirsearch/blob/461705af2688ab6644b1f2bf738c46c55ee4d3da/testing.py#L40)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 10 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: ConfigParser. Observed top-level functions: _get_default_session_dir, package_files,… |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 11 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: archive_stage, build, build_native, build_native_engine, chmod_executable, clean_wheel_… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 51 file(s) under lib package (observed from repository paths and static analysis). Observed top-level classes: AsyncRequester, AsyncResponse, BaseReport, BaseRequester, BaseResponse, BaseResponseStore. Observed t… |
| native package | library | Observed | Groups 18 file(s) under native package (observed from repository paths and static analysis). |
| pyinstaller package | library | Observed | Groups 1 file(s) under pyinstaller package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 33 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: AsyncFuzzer, AsyncScanner, BaseFuzzer, BaseScanner, CannotConnectException, CaseInsensitiv… |
| Tests | test | Observed | Groups 140 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: APITestHandler, AlternatingRedirectRequester, AsyncCalibrationRequester, AsyncFixedResponseRequester, Asyn… |

## Important files

- `.dockerignore` (container)
- `.github/FUNDING.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/codeql-analysis.yml` (ci)
- `.github/workflows/docker-image.yml` (ci)
- `.github/workflows/portable-builds.yml` (ci)
- `.github/workflows/pyinstaller-linux.yml` (ci)
- `.github/workflows/pyinstaller-macos-intel.yml` (ci)
- `.github/workflows/pyinstaller-macos-silicon.yml` (ci)
- `.github/workflows/pyinstaller-release-draft.yml` (ci)
- `.github/workflows/pyinstaller-windows.yml` (ci)
- `.github/workflows/rust-security.yml` (ci)
- `.github/workflows/semgrep-analysis.yml` (ci)
- `Dockerfile` (container)
- `config.ini` (config)
- `native/Cargo.toml` (manifest)
- `native/pyproject.toml` (manifest)
- `pyproject.toml` (manifest)
- `requirements.txt` (manifest)
- `setup.cfg` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `tests` — 140 analysed file(s)
- `lib` — 89 analysed file(s)
- `db` — 49 analysed file(s)
- `docs` — 33 analysed file(s)
- `native` — 22 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `.github` — 16 analysed file(s)
- `pyinstaller` — 4 analysed file(s)
- `scripts` — 4 analysed file(s)
- `requirements` — 2 analysed file(s)
- `sessions` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `461705af2688ab6644b1f2bf738c46c55ee4d3da` is the revision these paths and observations refer to.
