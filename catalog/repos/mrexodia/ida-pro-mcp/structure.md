# Project structure: mrexodia/ida-pro-mcp

**Analysed commit:** `13e480cb1198f923154b63669e8cb2faee5deaea`

**Commit reference:** [13e480cb1198f923154b63669e8cb2faee5deaea](https://github.com/mrexodia/ida-pro-mcp/commit/13e480cb1198f923154b63669e8cb2faee5deaea)

**Tree at this commit:** [mrexodia/ida-pro-mcp@13e480cb1198](https://github.com/mrexodia/ida-pro-mcp/tree/13e480cb1198f923154b63669e8cb2faee5deaea)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | mrexodia/ida-pro-mcp |
| Description | AI-powered reverse engineering assistant that bridges IDA Pro with language models through MCP. |
| Stars | 13476 |
| Forks | 1649 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `13e480cb1198f923154b63669e8cb2faee5deaea` |
| Retrieved at | 2026-11-14T19:09:49.064810+00:00 |
| Files in this snapshot | 206 |

## Directory tree

```text
.claude-plugin/  (1 files)
  plugin.json
.codex-plugin/  (2 files)
  mcp.json
  plugin.json
.github/  (2 files)
  workflows/  (1 files)
    idalib-tests.yml
  FUNDING.yml
.kimi-plugin/  (1 files)
  plugin.json
devdocs/  (1 files)
  test-framework.md
profiles/  (2 files)
  readonly.txt
  triage.txt
scripts/  (1 files)
  stress_search_cancellation.py
skills/  (102 files)
  idapython/  (102 files)
    docs/  (101 files)
      … 101 files under this directory
    SKILL.md
src/  (65 files)
  ida_pro_mcp/  (65 files)
    ida_mcp/  (52 files)
      … 52 files under this directory
    __init__.py
    __main__.py
    ida_mcp.py
    idalib_server.py
    idalib_session_manager.py
    idalib_supervisor.py
    installer.py
    installer_data.py
    installer_tui.py
    server.py
    test.py
    trace_dump.py
    worker_lifecycle.py
tests/  (20 files)
  _mcp_spec_support.py
  binary_info.py
  test_browser_transport_guards.py
  test_discovery_wildcard_host.py
  test_idalib_session_manager.py
  test_idalib_supervisor.py
  test_installer_scope_messages.py
  test_jsonrpc_union_params.py
  test_mainthread_pump.py
  test_mcp_spec_endpoints.py
  test_mcp_spec_envelope.py
  test_mcp_spec_http_e2e.py
  test_mcp_spec_schema_generation.py
  test_mcp_spec_tools_list.py
  test_mcp_spec_truncation.py
  test_no_protocol_stdout_prints.py
  test_output_schema.py
  test_server_transport.py
  test_worker_lifecycle.py
  typed_fixture.c
.editorconfig
.gitignore
.python-version
CLAUDE.md
LICENSE
README.md
ida-plugin.json
pyproject.toml
uv-package.sh
```

## Entry points

- [src/ida_pro_mcp/__main__.py:4](https://github.com/mrexodia/ida-pro-mcp/blob/13e480cb1198f923154b63669e8cb2faee5deaea/src/ida_pro_mcp/__main__.py#L4)
- [src/ida_pro_mcp/idalib_server.py:352](https://github.com/mrexodia/ida-pro-mcp/blob/13e480cb1198f923154b63669e8cb2faee5deaea/src/ida_pro_mcp/idalib_server.py#L352)
- [src/ida_pro_mcp/idalib_supervisor.py](https://github.com/mrexodia/ida-pro-mcp/blob/13e480cb1198f923154b63669e8cb2faee5deaea/src/ida_pro_mcp/idalib_supervisor.py)
- [src/ida_pro_mcp/server.py](https://github.com/mrexodia/ida-pro-mcp/blob/13e480cb1198f923154b63669e8cb2faee5deaea/src/ida_pro_mcp/server.py)
- [src/ida_pro_mcp/test.py](https://github.com/mrexodia/ida-pro-mcp/blob/13e480cb1198f923154b63669e8cb2faee5deaea/src/ida_pro_mcp/test.py)
- [src/ida_pro_mcp/trace_dump.py](https://github.com/mrexodia/ida-pro-mcp/blob/13e480cb1198f923154b63669e8cb2faee5deaea/src/ida_pro_mcp/trace_dump.py)
- [scripts/stress_search_cancellation.py:530](https://github.com/mrexodia/ida-pro-mcp/blob/13e480cb1198f923154b63669e8cb2faee5deaea/scripts/stress_search_cancellation.py#L530)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 7 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Ctx, IdalibCloseResult, IdalibListResult, IdalibOpenResult, IdalibSessionInfo, IdalibSessi… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| ida_pro_mcp package | library | Observed | Groups 34 file(s) under ida_pro_mcp package (observed from repository paths and static analysis). Observed top-level classes: AnalyzeBatchDetails, AnalyzeBatchDisasm, AnalyzeBatchQuery, AnalyzeBatchResult, AnalyzeCompon… |
| Tests | test | Observed | Groups 45 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: BrowserTransportGuardTests, ConnectableHostTests, DictOfInner, DiscoverWildcardInstanceTests, DispatchProxy… |

## Important files

- `.claude-plugin/plugin.json` (config)
- `.codex-plugin/mcp.json` (config)
- `.codex-plugin/plugin.json` (config)
- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/workflows/idalib-tests.yml` (ci)
- `.kimi-plugin/plugin.json` (config)
- `ida-plugin.json` (config)
- `pyproject.toml` (manifest)

## Top-level layout

- `skills` — 102 analysed file(s)
- `src` — 65 analysed file(s)
- `tests` — 20 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `.codex-plugin` — 2 analysed file(s)
- `.github` — 2 analysed file(s)
- `profiles` — 2 analysed file(s)
- `.claude-plugin` — 1 analysed file(s)
- `.kimi-plugin` — 1 analysed file(s)
- `devdocs` — 1 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `13e480cb1198f923154b63669e8cb2faee5deaea` is the revision these paths and observations refer to.
