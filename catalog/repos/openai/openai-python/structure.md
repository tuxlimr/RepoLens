# Project structure: openai/openai-python

**Analysed commit:** `3dae6090cc31cc64a437fe0bcee740b6d81ed2cc`

**Commit reference:** [3dae6090cc31cc64a437fe0bcee740b6d81ed2cc](https://github.com/openai/openai-python/commit/3dae6090cc31cc64a437fe0bcee740b6d81ed2cc)

**Tree at this commit:** [openai/openai-python@3dae6090cc31](https://github.com/openai/openai-python/tree/3dae6090cc31cc64a437fe0bcee740b6d81ed2cc)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | openai/openai-python |
| Description | The official Python library for the OpenAI API |
| Stars | 32158 |
| Forks | 5883 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `3dae6090cc31cc64a437fe0bcee740b6d81ed2cc` |
| Retrieved at | 2026-11-14T19:07:05.825373+00:00 |
| Files in this snapshot | 798 |

## Directory tree

```text
.devcontainer/  (2 files)
  Dockerfile
  devcontainer.json
.github/  (16 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.yml
    config.yml
    feature_request.yml
  actions/  (1 files)
    setup-node-tooling/  (1 files)
      … 1 files under this directory
  codex/  (2 files)
    prompts/  (1 files)
      … 1 files under this directory
    python-version-review-config.toml
  scripts/  (1 files)
    setup-playwright-sandbox.sh
  workflows/  (6 files)
    ci.yml
    codeql.yml
    create-releases.yml
    detect-breaking-changes.yml
    publish-pypi.yml
    python-version-review.yml
  CODEOWNERS
  dependabot.yml
  pull_request_template.md
.inline-snapshot/  (1 files)
  external/  (1 files)
    .gitignore
.vscode/  (1 files)
  settings.json
api_reference/  (1 files)
  .gitattributes
docs/  (9 files)
  architecture/  (1 files)
    security-model.md
  beta-realtime-api.md
  browser-forms.md
  browser-navigation.md
  browser-providers.md
  browser.md
  castiron-generated-code-transition.md
  castiron-polling-runtime-preparation.md
  realtime-translation.md
examples/  (89 files)
  browser/  (4 files)
    README_read_only.md
    exercise_read_only.py
    read_only.py
    reader-site.json
  browser-use-demo/  (9 files)
    README.md
    booking.py
    exercise.py
    exercise_ui.py
    fixture.html
    index.html
    runner.py
    server.py
    tasks.json
  computer-desktop/  (26 files)
    guest/  (18 files)
      … 18 files under this directory
    README.md
    container_runtime.py
    desktop.py
    exercise.py
    exercise_container.py
    exercise_helper_env.py
    guest.py
    run.py
  live/  (3 files)
    audio_transcript.py
    transcript_grouper.md
    transcript_grouper.py
  realtime/  (5 files)
    audio_util.py
    azure_realtime.py
    push_to_talk_app.py
    realtime.py
    test_push_to_talk_app.py
  responses/  (12 files)
    __init__.py
    background.py
    background_async.py
    background_streaming.py
    background_streaming_async.py
    multi_agent_streaming.py
    multi_agent_websocket.py
    streaming.py
    streaming_tools.py
    structured_outputs.py
    structured_outputs_tools.py
    websocket.py
  .keep
  async_demo.py
  audio.py
  azure.py
  azure_ad.py
  bedrock.py
  bedrock_runtime.py
  demo.py
  generate_file.sh
  httpx2_client.py
  image_stream.py
  module_client.py
  mtls_httpx.py
  mtls_httpx2.py
  mtls_httpx2_async.py
  mtls_httpx_async.py
  parsing.py
  parsing_stream.py
  parsing_tools.py
  parsing_tools_stream.py
  picture.py
  responses_input_tokens.py
  responses_websocket.py
  speech_to_text.py
  … 6 more files
scripts/  (31 files)
  fixtures/  (1 files)
    computer_use_smoke.py
  steady/  (8 files)
    install
    manifest.json
    publication.test.cjs
    publish.cjs
    settings
    source-sha256.cjs
    test.cjs
    update.cjs
  utils/  (6 files)
    node-tooling.cjs
    ruffen-docs.py
    validate-bedrock-wheel.py
    validate-httpx2-wheel.py
    validate-python-version-wheel.py
    validate-vertex-wheel.py
  bootstrap
  bootstrap-node
  check-dependency-security.py
  check-example-security.py
  check-python-version-policy.py
  detect-breaking-changes
  detect-breaking-changes.py
  format
  hatch_metadata.py
  lint
  mock
  pyrightconfig.breaking-changes.json
  run-pyright
  run-steady
  test
  test-pydantic-v1
src/  (628 files)
  openai/  (628 files)
    _extras/  (5 files)
      … 5 files under this directory
    _utils/  (14 files)
      … 14 files under this directory
    _vendor/  (7 files)
      … 7 files under this directory
    auth/  (3 files)
      … 3 files under this directory
    helpers/  (3 files)
      … 3 files under this directory
    lib/  (72 files)
      … 72 files under this directory
    providers/  (3 files)
      … 3 files under this directory
    resources/  (179 files)
      … 179 files under this directory
    types/  (316 files)
      … 316 files under this directory
    __init__.py
    _base_client.py
    _client.py
    _compat.py
    _constants.py
    _data_residency.py
    _event_handler.py
    _exceptions.py
    _files.py
    _httpx2.py
    _legacy_response.py
    _models.py
    _module_client.py
    _multipart.py
    _provider.py
    _qs.py
    _resource.py
    _response.py
    _send_queue.py
    _streaming.py
    _streaming_cleanup.py
    _types.py
    _version.py
    _websocket_connection.py
    … 2 more files
.castiron.stats.yml
.gitignore
.node-version
.python-version
.release-please-manifest.json
AGENTS.md
Brewfile
CONTRIBUTING.md
LICENSE
PYTHON_VERSION_POLICY.md
README.md
SECURITY.md
api.md
bedrock.md
helpers.md
httpx2.md
package.json
pnpm-workspace.yaml
pyproject.toml
release-please-config.json
```

## Entry points

- [scripts/check-example-security.py:66](https://github.com/openai/openai-python/blob/3dae6090cc31cc64a437fe0bcee740b6d81ed2cc/scripts/check-example-security.py#L66)
- [scripts/check-python-version-policy.py:145](https://github.com/openai/openai-python/blob/3dae6090cc31cc64a437fe0bcee740b6d81ed2cc/scripts/check-python-version-policy.py#L145)
- [scripts/detect-breaking-changes.py:84](https://github.com/openai/openai-python/blob/3dae6090cc31cc64a437fe0bcee740b6d81ed2cc/scripts/detect-breaking-changes.py#L84)
- [scripts/fixtures/computer_use_smoke.py:197](https://github.com/openai/openai-python/blob/3dae6090cc31cc64a437fe0bcee740b6d81ed2cc/scripts/fixtures/computer_use_smoke.py#L197)
- [scripts/utils/ruffen-docs.py:166](https://github.com/openai/openai-python/blob/3dae6090cc31cc64a437fe0bcee740b6d81ed2cc/scripts/utils/ruffen-docs.py#L166)
- [scripts/utils/validate-bedrock-wheel.py:139](https://github.com/openai/openai-python/blob/3dae6090cc31cc64a437fe0bcee740b6d81ed2cc/scripts/utils/validate-bedrock-wheel.py#L139)
- [scripts/utils/validate-httpx2-wheel.py:128](https://github.com/openai/openai-python/blob/3dae6090cc31cc64a437fe0bcee740b6d81ed2cc/scripts/utils/validate-httpx2-wheel.py#L128)
- [scripts/utils/validate-python-version-wheel.py:98](https://github.com/openai/openai-python/blob/3dae6090cc31cc64a437fe0bcee740b6d81ed2cc/scripts/utils/validate-python-version-wheel.py#L98)
- [scripts/utils/validate-vertex-wheel.py:76](https://github.com/openai/openai-python/blob/3dae6090cc31cc64a437fe0bcee740b6d81ed2cc/scripts/utils/validate-vertex-wheel.py#L76)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AsyncModels, AsyncModelsWithRawResponse, AsyncModelsWithStreamingResponse, Models, ModelsWithRawRespons… |
| Application entry point | entrypoint | Observed | Groups 9 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: CodeBlockError. Observed top-level functions: assert_python_39_rejected, check_installed,… |
| External integrations | external | Observed | Groups 5 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: APIRemovedInV1, APIRemovedInV1Proxy, AdminProxy, AsyncAPIClient, AsyncHttpxClientWrapper, As… |
| openai package | library | Observed | Groups 610 file(s) under openai package (observed from repository paths and static analysis). Observed top-level classes: APIConnectionError, APIError, APIKey, APIKeyCreateParams, APIKeyCreateResponse, APIKeyCreated. Ob… |
| scripts package | library | Observed | Groups 8 file(s) under scripts package (observed from repository paths and static analysis). Observed top-level functions: allows_published_release, audience_covers, canonical, covers_transitive_security_release, depend… |
| Tests | test | Observed | Groups 4 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: ActionAdmissionTests, ReceiptTests. Observed top-level functions: app_module, changed_build, guest_process,… |

## Important files

- `.castiron.stats.yml` (config)
- `.devcontainer/Dockerfile` (container)
- `.devcontainer/devcontainer.json` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/actions/setup-node-tooling/action.yml` (config)
- `.github/codex/python-version-review-config.toml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/codeql.yml` (ci)
- `.github/workflows/create-releases.yml` (ci)
- `.github/workflows/detect-breaking-changes.yml` (ci)
- `.github/workflows/publish-pypi.yml` (ci)
- `.github/workflows/python-version-review.yml` (ci)
- `.release-please-manifest.json` (config)
- `.vscode/settings.json` (config)
- `examples/browser-use-demo/tasks.json` (config)
- `examples/browser/reader-site.json` (config)
- `examples/computer-desktop/guest/container/Dockerfile` (container)
- `examples/computer-desktop/guest/container/seccomp.json` (config)
- `examples/computer-desktop/guest/preseed.cfg` (config)
- `examples/computer-desktop/guest/setup.py` (manifest)
- `package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `pyproject.toml` (manifest)
- `release-please-config.json` (config)
- `scripts/pyrightconfig.breaking-changes.json` (config)
- `scripts/steady/manifest.json` (config)

## Top-level layout

- `src` — 628 analysed file(s)
- `examples` — 89 analysed file(s)
- `scripts` — 31 analysed file(s)
- `(root files)` — 20 analysed file(s)
- `.github` — 16 analysed file(s)
- `docs` — 9 analysed file(s)
- `.devcontainer` — 2 analysed file(s)
- `.inline-snapshot` — 1 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `api_reference` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (1 x lockfile excluded; 1 x vendored/generated directory excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `3dae6090cc31cc64a437fe0bcee740b6d81ed2cc` is the revision these paths and observations refer to.
