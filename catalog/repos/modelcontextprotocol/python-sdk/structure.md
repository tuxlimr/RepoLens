# Project structure: modelcontextprotocol/python-sdk

**Analysed commit:** `77001c96f9507be0f4d009b83210a384a5e08bda`

**Commit reference:** [77001c96f9507be0f4d009b83210a384a5e08bda](https://github.com/modelcontextprotocol/python-sdk/commit/77001c96f9507be0f4d009b83210a384a5e08bda)

**Tree at this commit:** [modelcontextprotocol/python-sdk@77001c96f950](https://github.com/modelcontextprotocol/python-sdk/tree/77001c96f9507be0f4d009b83210a384a5e08bda)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | modelcontextprotocol/python-sdk |
| Description | The official Python SDK for Model Context Protocol servers and clients |
| Stars | 24861 |
| Forks | 4135 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `77001c96f9507be0f4d009b83210a384a5e08bda` |
| Retrieved at | 2026-11-14T19:07:35.647401+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.claude/  (2 files)
  commands/  (1 files)
    review-pr.md
  skills/  (1 files)
    test-quality/  (1 files)
      … 1 files under this directory
.github/  (27 files)
  ISSUE_TEMPLATE/  (5 files)
    bug.yaml
    config.yaml
    feature-request.yaml
    question.yaml
    v2-feedback.yaml
  actions/  (6 files)
    conformance/  (6 files)
      … 6 files under this directory
  scripts/  (4 files)
    docs_preview.js
    docs_preview.test.js
    pr_intake_gate.js
    pr_intake_gate.test.js
  workflows/  (10 files)
    claude.yml
    conformance.yml
    deploy-docs.yml
    docs-preview-cleanup.yml
    docs-preview.yml
    main.yml
    publish-pypi.yml
    require-linked-issue.yml
    shared.yml
    zizmor.yml
  dependabot.yml
  pull_request_template.md
docs/  (58 files)
  .overrides/  (1 files)
    .icons/  (1 files)
      … 1 files under this directory
  advanced/  (8 files)
    apps.md
    extensions.md
    header-parameters.md
    index.md
    low-level-server.md
    middleware.md
    pagination.md
    skills.md
  client/  (8 files)
    caching.md
    callbacks.md
    identity-assertion.md
    index.md
    oauth-clients.md
    session-groups.md
    subscriptions.md
    transports.md
  get-started/  (5 files)
    first-steps.md
    index.md
    installation.md
    real-host.md
    testing.md
  handlers/  (11 files)
    cancellation.md
    context.md
    dependencies.md
    elicitation.md
    index.md
    lifespan.md
    logging.md
    multi-round-trip.md
    progress.md
    sampling-and-roots.md
    subscriptions.md
  js/  (1 files)
    language-switch.js
  run/  (6 files)
    asgi.md
    authorization.md
    deploy.md
    index.md
    legacy-clients.md
    opentelemetry.md
  servers/  (9 files)
    completions.md
    handling-errors.md
    index.md
    media.md
    prompts.md
    resources.md
    structured-output.md
    tools.md
    uri-templates.md
  deprecated.md
  extra.css
  favicon.svg
  index.md
  migration.md
  protocol-versions.md
  translations.md
  troubleshooting.md
  whats-new.md
docs_src/  (218 files)
  apps/  (6 files)
    __init__.py
    report.html
    tutorial001.py
    tutorial001_client.py
    tutorial002.py
    tutorial003.py
  asgi/  (7 files)
    __init__.py
    tutorial001.py
    tutorial002.py
    tutorial003.py
    tutorial004.py
    tutorial005.py
    tutorial006.py
  authorization/  (3 files)
    __init__.py
    tutorial001.py
    tutorial002.py
  caching/  (4 files)
    __init__.py
    tutorial001.py
    tutorial002.py
    tutorial003.py
  cancellation/  (3 files)
    __init__.py
    tutorial001.py
    tutorial002.py
  client/  (9 files)
    __init__.py
    tutorial001.py
    tutorial001_client.py
    tutorial002.py
    tutorial003.py
    tutorial004.py
    tutorial005.py
    tutorial006.py
    tutorial007.py
  client_callbacks/  (5 files)
    __init__.py
    tutorial001.py
    tutorial002.py
    tutorial003.py
    tutorial004.py
  client_transports/  (6 files)
    __init__.py
    tutorial001.py
    tutorial002.py
    tutorial003.py
    tutorial004.py
    tutorial005.py
  completions/  (4 files)
    __init__.py
    tutorial001.py
    tutorial002.py
    tutorial003.py
  context/  (4 files)
    __init__.py
    tutorial001.py
    tutorial002.py
    tutorial003.py
  dependencies/  (5 files)
    __init__.py
    tutorial001.py
    tutorial002.py
    tutorial003.py
    tutorial004.py
  deploy/  (5 files)
    __init__.py
    tutorial001.py
    tutorial002.py
    tutorial003.py
    tutorial004.py
  elicitation/  (5 files)
    __init__.py
    tutorial001.py
    tutorial002.py
    tutorial003.py
    tutorial004.py
  extensions/  (12 files)
    __init__.py
    tutorial001.py
    tutorial002.py
    tutorial003.py
    tutorial003_client.py
    tutorial004.py
    tutorial004_client.py
    tutorial005.py
    tutorial006.py
    tutorial006_client.py
    tutorial007.py
    tutorial007_client.py
  first_steps/  (3 files)
    __init__.py
    tutorial001.py
    tutorial001_client.py
  handling_errors/  (5 files)
    __init__.py
    tutorial001.py
    tutorial002.py
    tutorial003.py
    tutorial004.py
  header_parameters/  (4 files)
    __init__.py
    tutorial001.py
    tutorial002.py
    tutorial003.py
  identity_assertion/  (3 files)
    __init__.py
    tutorial001.py
    tutorial002.py
  index/  (2 files)
    __init__.py
    tutorial001.py
  legacy_clients/  (5 files)
    __init__.py
    tutorial001.py
    tutorial001_client.py
    tutorial002.py
    tutorial003.py
  lifespan/  (3 files)
    __init__.py
    tutorial001.py
    tutorial002.py
  logging/  (2 files)
    __init__.py
    tutorial001.py
  lowlevel/  (8 files)
    __init__.py
    tutorial001.py
    tutorial002.py
    tutorial003.py
    tutorial004.py
    tutorial005.py
    tutorial006.py
    tutorial007.py
  media/  (6 files)
    __init__.py
    tutorial001.py
    tutorial002.py
    tutorial003.py
    tutorial004.py
    tutorial005.py
  middleware/  (3 files)
    __init__.py
    tutorial001.py
    tutorial002.py
  mrtr/  (6 files)
    __init__.py
    tutorial001.py
    tutorial002.py
    tutorial003.py
    tutorial004.py
    tutorial005.py
  oauth_clients/  (3 files)
    __init__.py
    tutorial001.py
    tutorial002.py
  opentelemetry/  (2 files)
    __init__.py
    tutorial001.py
  pagination/  (3 files)
    __init__.py
    tutorial001.py
    tutorial002.py
  progress/  (3 files)
    __init__.py
    tutorial001.py
    tutorial002.py
  prompts/  (7 files)
    __init__.py
    tutorial001.py
    tutorial002.py
    tutorial003.py
    tutorial004.py
    tutorial005.py
    tutorial006.py
  protocol_versions/  (5 files)
    __init__.py
    tutorial001.py
    tutorial002.py
    tutorial003.py
    tutorial004.py
  real_host/  (2 files)
    __init__.py
    tutorial001.py
  resources/  (4 files)
    __init__.py
    tutorial001.py
    tutorial002.py
    tutorial003.py
  run/  (4 files)
    __init__.py
    tutorial001.py
    tutorial002.py
    tutorial003.py
  sampling_and_roots/  (3 files)
    __init__.py
    tutorial001.py
    tutorial002.py
  session_groups/  (5 files)
    __init__.py
    tutorial001.py
    tutorial002.py
    tutorial003.py
    tutorial004.py
  skills/  (3 files)
    __init__.py
    tutorial001.py
    tutorial001_client.py
  structured_output/  (10 files)
    __init__.py
    tutorial001.py
    tutorial002.py
    tutorial003.py
    tutorial004.py
    tutorial005.py
    tutorial006.py
    tutorial007.py
    tutorial008.py
    tutorial009.py
  subscriptions/  (10 files)
    __init__.py
    tutorial001.py
    tutorial002.py
    tutorial003.py
    tutorial004_anyio.py
    tutorial004_asyncio.py
    tutorial004_trio.py
    tutorial005.py
    tutorial006.py
    tutorial007.py
  testing/  (2 files)
    __init__.py
    tutorial001.py
  tools/  (6 files)
    __init__.py
    tutorial001.py
    tutorial002.py
    tutorial003.py
    tutorial004.py
    tutorial005.py
  troubleshooting/  (9 files)
    __init__.py
    tutorial001.py
    tutorial002.py
    tutorial003.py
    tutorial004.py
    tutorial005.py
    tutorial006.py
    tutorial007.py
    tutorial008.py
  uri_templates/  (6 files)
    __init__.py
    tutorial001.py
    tutorial002.py
    tutorial003.py
    tutorial004.py
    tutorial005.py
  whats_new/  (2 files)
    __init__.py
    tutorial001.py
  __init__.py
examples/  (296 files)
  clients/  (14 files)
    simple-auth-client/  (4 files)
      … 4 files under this directory
    simple-chatbot/  (6 files)
      … 6 files under this directory
    sse-polling-client/  (4 files)
      … 4 files under this directory
  mcpserver/  (14 files)
    complex_inputs.py
    desktop.py
    direct_call_tool_result_return.py
    echo.py
    icons_demo.py
    logging_and_progress.py
    memory.py
    parameter_descriptions.py
    readme-quickstart.py
    screenshot.py
    simple_echo.py
    text_me.py
    unicode_example.py
    weather_structured.py
  servers/  (55 files)
    everything-server/  (5 files)
      … 5 files under this directory
    simple-auth/  (10 files)
      … 10 files under this directory
    simple-pagination/  (5 files)
      … 5 files under this directory
    simple-prompt/  (5 files)
      … 5 files under this directory
    simple-resource/  (5 files)
      … 5 files under this directory
    simple-streamablehttp/  (6 files)
      … 6 files under this directory
    simple-streamablehttp-stateless/  (5 files)
      … 5 files under this directory
    simple-tool/  (5 files)
      … 5 files under this directory
    sse-polling-demo/  (6 files)
      … 6 files under this directory
    structured-output-lowlevel/  (3 files)
      … 3 files under this directory
  snippets/  (40 files)
    clients/  (10 files)
      … 10 files under this directory
    servers/  (29 files)
      … 29 files under this directory
    pyproject.toml
  stories/  (171 files)
    _shared/  (2 files)
      … 2 files under this directory
    apps/  (4 files)
      … 4 files under this directory
    bearer_auth/  (5 files)
      … 5 files under this directory
    caching/  (1 files)
      … 1 files under this directory
    custom_methods/  (4 files)
      … 4 files under this directory
    dual_era/  (5 files)
      … 5 files under this directory
    error_handling/  (5 files)
      … 5 files under this directory
    events/  (1 files)
      … 1 files under this directory
    extensions/  (4 files)
      … 4 files under this directory
    identity_assertion/  (6 files)
      … 6 files under this directory
    json_response/  (5 files)
      … 5 files under this directory
    legacy_elicitation/  (5 files)
      … 5 files under this directory
    legacy_routing/  (5 files)
      … 5 files under this directory
    lifespan/  (5 files)
      … 5 files under this directory
    middleware/  (4 files)
      … 4 files under this directory
    mrtr/  (5 files)
      … 5 files under this directory
    oauth/  (5 files)
      … 5 files under this directory
    oauth_client_credentials/  (5 files)
      … 5 files under this directory
    pagination/  (5 files)
      … 5 files under this directory
    parallel_calls/  (5 files)
      … 5 files under this directory
    prompts/  (5 files)
      … 5 files under this directory
    reconnect/  (5 files)
      … 5 files under this directory
    refund_desk/  (4 files)
      … 4 files under this directory
    resources/  (5 files)
      … 5 files under this directory
    roots/  (5 files)
      … 5 files under this directory
    sampling/  (5 files)
      … 5 files under this directory
    schema_validators/  (5 files)
      … 5 files under this directory
    serve_one/  (4 files)
      … 4 files under this directory
    skills/  (1 files)
      … 1 files under this directory
    sse_polling/  (6 files)
      … 6 files under this directory
    standalone_get/  (5 files)
      … 5 files under this directory
    starlette_mount/  (4 files)
      … 4 files under this directory
    stateless_legacy/  (5 files)
      … 5 files under this directory
    stickynotes/  (5 files)
      … 5 files under this directory
    streaming/  (5 files)
      … 5 files under this directory
    subscriptions/  (5 files)
      … 5 files under this directory
    tasks/  (1 files)
      … 1 files under this directory
    tools/  (5 files)
      … 5 files under this directory
    README.md
    __init__.py
    _harness.py
    _hosting.py
    manifest.toml
  README.md
  pyproject.toml
i18n/  (184 files)
  de/  (55 files)
    pages/  (52 files)
      … 52 files under this directory
    glossary.json
    instructions.md
    notices.md
  es/  (55 files)
    pages/  (52 files)
      … 52 files under this directory
    glossary.json
    instructions.md
    notices.md
  fr/  (55 files)
    pages/  (52 files)
      … 52 files under this directory
    glossary.json
    instructions.md
    notices.md
  hi/  (17 files)
    pages/  (14 files)
      … 14 files under this directory
    glossary.json
    instructions.md
    notices.md
  README.md
  general-prompt.md
.git-blame-ignore-revs
.gitattributes
.gitignore
.pre-commit-config.yaml
AGENTS.md
CLAUDE.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
DEPENDENCY_POLICY.md
LICENSE
README.md
RELEASE.md
ROADMAP.md
SECURITY.md
VERSIONING.md
```

## Entry points

- [.github/actions/conformance/client.py:643](https://github.com/modelcontextprotocol/python-sdk/blob/77001c96f9507be0f4d009b83210a384a5e08bda/.github/actions/conformance/client.py#L643)
- [docs_src/apps/tutorial001_client.py:19](https://github.com/modelcontextprotocol/python-sdk/blob/77001c96f9507be0f4d009b83210a384a5e08bda/docs_src/apps/tutorial001_client.py#L19)
- [docs_src/caching/tutorial003.py:33](https://github.com/modelcontextprotocol/python-sdk/blob/77001c96f9507be0f4d009b83210a384a5e08bda/docs_src/caching/tutorial003.py#L33)
- [docs_src/client/tutorial001_client.py:14](https://github.com/modelcontextprotocol/python-sdk/blob/77001c96f9507be0f4d009b83210a384a5e08bda/docs_src/client/tutorial001_client.py#L14)
- [docs_src/client/tutorial002.py:16](https://github.com/modelcontextprotocol/python-sdk/blob/77001c96f9507be0f4d009b83210a384a5e08bda/docs_src/client/tutorial002.py#L16)
- [docs_src/client/tutorial003.py:19](https://github.com/modelcontextprotocol/python-sdk/blob/77001c96f9507be0f4d009b83210a384a5e08bda/docs_src/client/tutorial003.py#L19)
- [docs_src/client/tutorial004.py:21](https://github.com/modelcontextprotocol/python-sdk/blob/77001c96f9507be0f4d009b83210a384a5e08bda/docs_src/client/tutorial004.py#L21)
- [docs_src/client/tutorial005.py:16](https://github.com/modelcontextprotocol/python-sdk/blob/77001c96f9507be0f4d009b83210a384a5e08bda/docs_src/client/tutorial005.py#L16)
- [docs_src/client/tutorial006.py:16](https://github.com/modelcontextprotocol/python-sdk/blob/77001c96f9507be0f4d009b83210a384a5e08bda/docs_src/client/tutorial006.py#L16)
- [docs_src/client/tutorial007.py:24](https://github.com/modelcontextprotocol/python-sdk/blob/77001c96f9507be0f4d009b83210a384a5e08bda/docs_src/client/tutorial007.py#L24)
- [docs_src/extensions/tutorial003_client.py:15](https://github.com/modelcontextprotocol/python-sdk/blob/77001c96f9507be0f4d009b83210a384a5e08bda/docs_src/extensions/tutorial003_client.py#L15)
- [docs_src/extensions/tutorial004_client.py:34](https://github.com/modelcontextprotocol/python-sdk/blob/77001c96f9507be0f4d009b83210a384a5e08bda/docs_src/extensions/tutorial004_client.py#L34)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| docs_src package | library | Observed | Groups 185 file(s) under docs_src package (observed from repository paths and static analysis). Observed top-level classes: AlternativeDate, AppContext, AuditLog, Backorder, Book, CardHolder. Observed top-level function… |
| Application entry point | entrypoint | Observed | Groups 30 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Clock, JobParams, JobStatus, JobStatusRequest, ReceiptResult, Receipts. Observed top-leve… |
| External integrations | external | Observed | Groups 2 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: Book. Observed top-level functions: books_in_genre, complete_genre, genres, lookup_book, rec… |

## Important files

- `.github/ISSUE_TEMPLATE/bug.yaml` (config)
- `.github/ISSUE_TEMPLATE/config.yaml` (config)
- `.github/ISSUE_TEMPLATE/feature-request.yaml` (config)
- `.github/ISSUE_TEMPLATE/question.yaml` (config)
- `.github/ISSUE_TEMPLATE/v2-feedback.yaml` (config)
- `.github/actions/conformance/expected-failures.2025-11-25.yml` (config)
- `.github/actions/conformance/expected-failures.2026-07-28.yml` (config)
- `.github/actions/conformance/expected-failures.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/claude.yml` (ci)
- `.github/workflows/conformance.yml` (ci)
- `.github/workflows/deploy-docs.yml` (ci)
- `.github/workflows/docs-preview-cleanup.yml` (ci)
- `.github/workflows/docs-preview.yml` (ci)
- `.github/workflows/main.yml` (ci)
- `.github/workflows/publish-pypi.yml` (ci)
- `.github/workflows/require-linked-issue.yml` (ci)
- `.github/workflows/shared.yml` (ci)
- `.github/workflows/zizmor.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `examples/clients/simple-auth-client/pyproject.toml` (manifest)
- `examples/clients/simple-chatbot/mcp_simple_chatbot/.env.example` (config)
- `examples/clients/simple-chatbot/mcp_simple_chatbot/requirements.txt` (manifest)
- `examples/clients/simple-chatbot/mcp_simple_chatbot/servers_config.json` (config)
- `examples/clients/simple-chatbot/pyproject.toml` (manifest)
- `examples/clients/sse-polling-client/pyproject.toml` (manifest)
- `examples/pyproject.toml` (manifest)
- `examples/servers/everything-server/pyproject.toml` (manifest)
- `examples/servers/simple-auth/pyproject.toml` (manifest)
- `examples/servers/simple-pagination/pyproject.toml` (manifest)
- `examples/servers/simple-prompt/pyproject.toml` (manifest)
- `examples/servers/simple-resource/pyproject.toml` (manifest)
- `examples/servers/simple-streamablehttp-stateless/pyproject.toml` (manifest)
- `examples/servers/simple-streamablehttp/pyproject.toml` (manifest)
- `examples/servers/simple-tool/pyproject.toml` (manifest)
- `examples/servers/sse-polling-demo/pyproject.toml` (manifest)
- `examples/servers/structured-output-lowlevel/pyproject.toml` (manifest)
- `examples/snippets/pyproject.toml` (manifest)
- `examples/stories/manifest.toml` (config)
- `i18n/de/glossary.json` (config)
- `i18n/es/glossary.json` (config)
- `i18n/fr/glossary.json` (config)
- `i18n/hi/glossary.json` (config)

## Top-level layout

- `examples` — 296 analysed file(s)
- `docs_src` — 218 analysed file(s)
- `i18n` — 184 analysed file(s)
- `docs` — 58 analysed file(s)
- `.github` — 27 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `.claude` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `77001c96f9507be0f4d009b83210a384a5e08bda` is the revision these paths and observations refer to.
