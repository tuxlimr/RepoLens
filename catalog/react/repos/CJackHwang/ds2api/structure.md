# Project structure: CJackHwang/ds2api

**Analysed commit:** `8316cf8a0352e900e03ce600b792083f590d80e2`

**Commit reference:** [8316cf8a0352e900e03ce600b792083f590d80e2](https://github.com/CJackHwang/ds2api/commit/8316cf8a0352e900e03ce600b792083f590d80e2)

**Tree at this commit:** [CJackHwang/ds2api@8316cf8a0352](https://github.com/CJackHwang/ds2api/tree/8316cf8a0352e900e03ce600b792083f590d80e2)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | CJackHwang/ds2api |
| Description | DeepSeek-Compatible Middleware Interface: A technical exploration project in Go, focusing on high-concurrency protocol adaptation. It serves as a reference implementation for converting diverse web protocols into standardized formats. |
| Stars | 4705 |
| Forks | 1627 |
| Licence | AGPL-3.0 |
| Language | Go |
| Default branch | main |
| Analysed commit | `8316cf8a0352e900e03ce600b792083f590d80e2` |
| Retrieved at | 2026-11-14T19:14:38.641613+00:00 |
| Files in this snapshot | 544 |

## Directory tree

```text
.github/  (7 files)
  ISSUE_TEMPLATE/  (2 files)
    1_bug_report.yml
    2_feature_request.yml
  workflows/  (4 files)
    quality-gates.yml
    release-artifacts.yml
    release-dockerhub.yml
    release.yml
  PULL_REQUEST_TEMPLATE.md
api/  (2 files)
  chat-stream.js
  index.go
app/  (1 files)
  handler.go
cmd/  (2 files)
  ds2api/  (1 files)
    main.go
  ds2api-tests/  (1 files)
    main.go
docs/  (13 files)
  ARCHITECTURE.en.md
  ARCHITECTURE.md
  CONTRIBUTING.en.md
  CONTRIBUTING.md
  DEPLOY.en.md
  DEPLOY.md
  DEVELOPMENT.md
  DeepSeekSSE行为结构说明-2026-04-05.md
  README.md
  TESTING.md
  project-value.md
  prompt-compatibility.md
  toolcall-semantics.md
internal/  (384 files)
  account/  (6 files)
    pool_acquire.go
    pool_core.go
    pool_edge_test.go
    pool_limits.go
    pool_test.go
    pool_waiters.go
  assistantturn/  (3 files)
    stream.go
    turn.go
    turn_test.go
  auth/  (5 files)
    admin.go
    admin_test.go
    auth_edge_test.go
    request.go
    request_test.go
  chathistory/  (2 files)
    store.go
    store_test.go
  claudeconv/  (1 files)
    convert.go
  compat/  (1 files)
    go_compat_test.go
  completionruntime/  (4 files)
    nonstream.go
    nonstream_test.go
    stream_retry.go
    stream_retry_test.go
  config/  (22 files)
    account.go
    codec.go
    config.go
    config_edge_test.go
    config_test.go
    credentials.go
    dotenv.go
    dotenv_test.go
    logger.go
    mobile.go
    mobile_test.go
    model_alias_test.go
    models.go
    paths.go
    paths_test.go
    store.go
    store_accessors.go
    store_accessors_test.go
    store_env_writeback.go
    store_index.go
    validation.go
    validation_test.go
  deepseek/  (29 files)
    client/  (23 files)
      … 23 files under this directory
    protocol/  (5 files)
      … 5 files under this directory
    transport/  (1 files)
      … 1 files under this directory
  devcapture/  (2 files)
    store.go
    store_test.go
  format/  (7 files)
    claude/  (2 files)
      … 2 files under this directory
    openai/  (5 files)
      … 5 files under this directory
  httpapi/  (166 files)
    admin/  (60 files)
      … 60 files under this directory
    claude/  (26 files)
      … 26 files under this directory
    gemini/  (14 files)
      … 14 files under this directory
    ollama/  (2 files)
      … 2 files under this directory
    openai/  (62 files)
      … 62 files under this directory
    requestbody/  (2 files)
      … 2 files under this directory
  js/  (23 files)
    chat-stream/  (13 files)
      … 13 files under this directory
    helpers/  (9 files)
      … 9 files under this directory
    shared/  (1 files)
      … 1 files under this directory
  prompt/  (4 files)
    messages.go
    messages_test.go
    tool_calls.go
    tool_calls_test.go
  promptcompat/  (15 files)
    file_refs.go
    history_transcript.go
    message_normalize.go
    message_normalize_test.go
    prompt_build.go
    prompt_build_test.go
    request_normalize.go
    responses_input_items.go
    responses_input_items_test.go
    responses_input_normalize.go
    standard_request.go
    standard_request_test.go
    thinking_injection.go
    thinking_injection_test.go
    tool_prompt.go
  rawsample/  (3 files)
    rawsample.go
    rawsample_test.go
    visible_text.go
  responsehistory/  (1 files)
    session.go
  server/  (6 files)
    router.go
    router_cors_test.go
    router_health_test.go
    router_log_test.go
    router_routes_test.go
    router_utf8_test.go
  sse/  (16 files)
    citation_links.go
    consumer.go
    consumer_edge_test.go
    consumer_test.go
    content_filter_leak.go
    dedupe.go
    dedupe_test.go
    line.go
    line_edge_test.go
    line_test.go
    parser.go
    parser_edge_test.go
    parser_test.go
    stream.go
    stream_edge_test.go
    stream_test.go
  stream/  (2 files)
    engine.go
    engine_test.go
  testsuite/  (16 files)
    edge_cases.go
    edge_cases_abort.go
    edge_cases_error_contract.go
    runner_cases_admin.go
    runner_cases_claude.go
    runner_cases_openai.go
    runner_cases_openai_advanced.go
    runner_core.go
    runner_defaults.go
    runner_env.go
    runner_env_test.go
    runner_http.go
    runner_registry.go
    runner_registry_test.go
    runner_summary.go
    runner_utils.go
  textclean/  (1 files)
    reference_markers.go
  toolcall/  (19 files)
    fence_edge_test.go
    regression_test.go
    tool_prompt.go
    tool_prompt_test.go
    toolcall_edge_test.go
    toolcalls_array_parse.go
    toolcalls_candidates.go
    toolcalls_dsml.go
    toolcalls_format.go
    toolcalls_input_parse.go
    toolcalls_json_repair.go
    toolcalls_markup.go
    toolcalls_parse.go
    toolcalls_parse_markup.go
    toolcalls_scan.go
    toolcalls_schema_normalize.go
    toolcalls_schema_normalize_test.go
    toolcalls_test.go
    toolcalls_xml.go
  toolstream/  (8 files)
    complex_edge_test.go
    fence_edge_sieve_test.go
    tool_sieve_core.go
    tool_sieve_jsonscan.go
    tool_sieve_state.go
    tool_sieve_xml.go
    tool_sieve_xml_scan.go
    tool_sieve_xml_test.go
  translatorcliproxy/  (4 files)
    bridge.go
    bridge_test.go
    stream_writer.go
    stream_writer_test.go
  util/  (13 files)
    helpers.go
    messages.go
    messages_test.go
    render.go
    render_test.go
    text.go
    thinking.go
    thinking_test.go
    token_count.go
    token_count_heuristic.go
    token_count_tiktoken.go
    token_count_tiktoken_test.go
    util_edge_test.go
  version/  (2 files)
    version.go
    version_test.go
  webui/  (3 files)
    build.go
    handler.go
    handler_test.go
pow/  (4 files)
  README.md
  deepseek_hash.go
  deepseek_pow.go
  deepseek_pow_test.go
scripts/  (4 files)
  build-release-archives.sh
  build-webui.sh
  lint.sh
  release-targets.sh
tests/  (45 files)
  compat/  (16 files)
    expected/  (8 files)
      … 8 files under this directory
    fixtures/  (8 files)
      … 8 files under this directory
  node/  (4 files)
    chat-history-utils.test.js
    chat-stream.test.js
    js_compat_test.js
    stream-tool-sieve.test.js
  raw_stream_samples/  (11 files)
    continue-thinking-snapshot-replay-20260405/  (1 files)
      … 1 files under this directory
    longtext-deepseek-v4-flash-20260429/  (2 files)
      … 2 files under this directory
    longtext-deepseek-v4-pro-20260429/  (2 files)
      … 2 files under this directory
    markdown-format-example-20260405/  (2 files)
      … 2 files under this directory
    markdown-format-example-20260405-spacefix/  (2 files)
      … 2 files under this directory
    README.md
    manifest.json
  scripts/  (11 files)
    capture-raw-stream-sample.sh
    check-cross-build.sh
    check-node-split-syntax.sh
    check-refactor-line-gate.sh
    check-stage6-manual-smoke.sh
    compare-raw-stream-sample.sh
    run-live.sh
    run-raw-stream-sim.sh
    run-unit-all.sh
    run-unit-go.sh
    run-unit-node.sh
  tools/  (1 files)
    deepseek-sse-simulator.mjs
  repair_json_tool.go
  复杂场合测试.json
webui/  (59 files)
  public/  (1 files)
    ds2api-favicon.svg
  src/  (53 files)
    app/  (3 files)
      … 3 files under this directory
    components/  (4 files)
      … 4 files under this directory
    features/  (36 files)
      … 36 files under this directory
    layout/  (1 files)
      … 1 files under this directory
    locales/  (2 files)
      … 2 files under this directory
    utils/  (3 files)
      … 3 files under this directory
    App.jsx
    i18n.jsx
    main.jsx
    styles.css
  index.html
  package.json
  postcss.config.js
  tailwind.config.js
  vite.config.js
.dockerignore
.env.example
.gitignore
.golangci.yml
.releaserc.json
AGENTS.md
API.en.md
API.md
CODE_OF_CONDUCT.md
Dockerfile
LICENSE
README.MD
README.en.md
SECURITY.md
VERSION
config.example.json
docker-compose.dev.yml
docker-compose.yml
go.mod
go.sum
start.mjs
vercel.json
zeabur.yaml
```

## Entry points

- [internal/js/chat-stream/index.js](https://github.com/CJackHwang/ds2api/blob/8316cf8a0352e900e03ce600b792083f590d80e2/internal/js/chat-stream/index.js)
- [webui/src/App.jsx](https://github.com/CJackHwang/ds2api/blob/8316cf8a0352e900e03ce600b792083f590d80e2/webui/src/App.jsx)
- [webui/src/main.jsx](https://github.com/CJackHwang/ds2api/blob/8316cf8a0352e900e03ce600b792083f590d80e2/webui/src/main.jsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 2 file(s) under api layer (observed from repository paths and static analysis). |
| app package | library | Observed | Groups 1 file(s) under app package (observed from repository paths and static analysis). |
| cmd package | library | Observed | Groups 2 file(s) under cmd package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 49 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 23 file(s) under external integrations (observed from repository paths and static analysis). |
| internal package | library | Observed | Groups 325 file(s) under internal package (observed from repository paths and static analysis). |
| pow package | library | Observed | Groups 3 file(s) under pow package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 4 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 52 file(s) under tests (observed from repository paths and static analysis). |
| webui package | library | Observed | Groups 43 file(s) under webui package (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.env.example` (config)
- `.github/ISSUE_TEMPLATE/1_bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/2_feature_request.yml` (config)
- `.github/workflows/quality-gates.yml` (ci)
- `.github/workflows/release-artifacts.yml` (ci)
- `.github/workflows/release-dockerhub.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.golangci.yml` (config)
- `.releaserc.json` (config)
- `Dockerfile` (container)
- `config.example.json` (config)
- `docker-compose.dev.yml` (config)
- `docker-compose.yml` (container)
- `go.mod` (manifest)
- `internal/deepseek/protocol/constants_shared.json` (config)
- `vercel.json` (config)
- `webui/package.json` (manifest)
- `webui/src/locales/en.json` (config)
- `webui/src/locales/zh.json` (config)
- `zeabur.yaml` (config)

## Top-level layout

- `internal` — 384 analysed file(s)
- `webui` — 59 analysed file(s)
- `tests` — 45 analysed file(s)
- `(root files)` — 23 analysed file(s)
- `docs` — 13 analysed file(s)
- `.github` — 7 analysed file(s)
- `pow` — 4 analysed file(s)
- `scripts` — 4 analysed file(s)
- `api` — 2 analysed file(s)
- `cmd` — 2 analysed file(s)
- `app` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `8316cf8a0352e900e03ce600b792083f590d80e2` is the revision these paths and observations refer to.
