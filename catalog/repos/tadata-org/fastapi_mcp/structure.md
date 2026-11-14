# Project structure: tadata-org/fastapi_mcp

**Analysed commit:** `e5cad13cabfc725bbcb047e526816d887d96da62`

**Commit reference:** [e5cad13cabfc725bbcb047e526816d887d96da62](https://github.com/tadata-org/fastapi_mcp/commit/e5cad13cabfc725bbcb047e526816d887d96da62)

**Tree at this commit:** [tadata-org/fastapi_mcp@e5cad13cabfc](https://github.com/tadata-org/fastapi_mcp/tree/e5cad13cabfc725bbcb047e526816d887d96da62)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | tadata-org/fastapi_mcp |
| Description | Expose your FastAPI endpoints as Model Context Protocol (MCP) tools, with Auth! |
| Stars | 12031 |
| Forks | 965 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `e5cad13cabfc725bbcb047e526816d887d96da62` |
| Retrieved at | 2026-11-14T19:10:16.597554+00:00 |
| Files in this snapshot | 80 |

## Directory tree

```text
.github/  (8 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    documentation.md
    feature_request.md
  workflows/  (2 files)
    ci.yml
    release.yml
  codecov.yml
  dependabot.yml
  pull_request_template.md
docs/  (13 files)
  advanced/  (5 files)
    asgi.mdx
    auth.mdx
    deploy.mdx
    refresh.mdx
    transport.mdx
  configurations/  (2 files)
    customization.mdx
    tool-naming.mdx
  getting-started/  (5 files)
    FAQ.mdx
    best-practices.mdx
    installation.mdx
    quickstart.mdx
    welcome.mdx
  docs.json
examples/  (16 files)
  shared/  (5 files)
    apps/  (2 files)
      … 2 files under this directory
    __init__.py
    auth.py
    setup.py
  01_basic_usage_example.py
  02_full_schema_description_example.py
  03_custom_exposed_endpoints_example.py
  04_separate_server_example.py
  05_reregister_tools_example.py
  06_custom_mcp_router_example.py
  07_configure_http_timeout_example.py
  08_auth_example_token_passthrough.py
  09_auth_example_auth0.py
  README.md
  __init__.py
fastapi_mcp/  (12 files)
  auth/  (2 files)
    __init__.py
    proxy.py
  openapi/  (3 files)
    __init__.py
    convert.py
    utils.py
  transport/  (3 files)
    __init__.py
    http.py
    sse.py
  utils/  (1 files)
    __init__.py
  __init__.py
  server.py
  types.py
tests/  (17 files)
  fixtures/  (5 files)
    complex_app.py
    conftest.py
    example_data.py
    simple_app.py
    types.py
  __init__.py
  conftest.py
  test_basic_functionality.py
  test_configuration.py
  test_http_real_transport.py
  test_mcp_complex_app.py
  test_mcp_execute_api_tool.py
  test_mcp_simple_app.py
  test_openapi_conversion.py
  test_sse_mock_transport.py
  test_sse_real_transport.py
  test_types_validation.py
.coveragerc
.cursorignore
.gitignore
.pre-commit-config.yaml
.python-version
CHANGELOG.md
CONTRIBUTING.md
LICENSE
MANIFEST.in
README.md
README_zh-CN.md
mypy.ini
pyproject.toml
pytest.ini
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: FastApiMCP. |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| fastapi_mcp package | library | Observed | Groups 11 file(s) under fastapi_mcp package (observed from repository paths and static analysis). Observed top-level classes: AuthConfig, BaseType, ClientRegistrationRequest, ClientRegistrationResponse, FastApiHttpSessi… |
| Tests | test | Observed | Groups 17 file(s) under tests (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed top-level classes: Address, Customer, CustomerTier, ErrorResponse, Item, Orde… |

## Important files

- `.github/codecov.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `MANIFEST.in` (manifest)
- `docs/docs.json` (config)
- `examples/shared/setup.py` (manifest)
- `mypy.ini` (config)
- `pyproject.toml` (manifest)
- `pytest.ini` (config)

## Top-level layout

- `tests` — 17 analysed file(s)
- `examples` — 16 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `docs` — 13 analysed file(s)
- `fastapi_mcp` — 12 analysed file(s)
- `.github` — 8 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `e5cad13cabfc725bbcb047e526816d887d96da62` is the revision these paths and observations refer to.
