# Project structure: Chainlit/chainlit

**Analysed commit:** `190ea74239d9e84b26e7c91bc2882dd038942564`

**Commit reference:** [190ea74239d9e84b26e7c91bc2882dd038942564](https://github.com/Chainlit/chainlit/commit/190ea74239d9e84b26e7c91bc2882dd038942564)

**Tree at this commit:** [Chainlit/chainlit@190ea74239d9](https://github.com/Chainlit/chainlit/tree/190ea74239d9e84b26e7c91bc2882dd038942564)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Chainlit/chainlit |
| Description | Build Conversational AI in minutes ⚡️ |
| Stars | 12504 |
| Forks | 1766 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `190ea74239d9e84b26e7c91bc2882dd038942564` |
| Retrieved at | 2026-11-14T19:10:07.294010+00:00 |
| Files in this snapshot | 632 |

## Directory tree

```text
.claude/  (1 files)
  settings.json
.cursor/  (1 files)
  settings.json
.github/  (15 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  actions/  (2 files)
    pnpm-node-install/  (1 files)
      … 1 files under this directory
    uv-python-install/  (1 files)
      … 1 files under this directory
  workflows/  (9 files)
    check-backend.yaml
    check-frontend.yaml
    ci.yaml
    close_stale.yml
    copilot-setup-steps.yaml
    e2e-tests.yaml
    publish-libs.yaml
    publish.yaml
    tests.yaml
  CODEOWNERS
  copilot-instructions.md
.husky/  (1 files)
  pre-commit
.serena/  (2 files)
  .gitignore
  project.yml
.shared/  (4 files)
  agents/  (1 files)
    .keep
  commands/  (1 files)
    .keep
  rules/  (1 files)
    .keep
  skills/  (1 files)
    karpathy-guidelines/  (1 files)
      … 1 files under this directory
backend/  (135 files)
  chainlit/  (90 files)
    auth/  (3 files)
      … 3 files under this directory
    cli/  (1 files)
      … 1 files under this directory
    data/  (14 files)
      … 14 files under this directory
    discord/  (2 files)
      … 2 files under this directory
    langchain/  (2 files)
      … 2 files under this directory
    langflow/  (1 files)
      … 1 files under this directory
    llama_index/  (2 files)
      … 2 files under this directory
    mistralai/  (1 files)
      … 1 files under this directory
    openai/  (1 files)
      … 1 files under this directory
    sample/  (2 files)
      … 2 files under this directory
    semantic_kernel/  (1 files)
      … 1 files under this directory
    slack/  (2 files)
      … 2 files under this directory
    teams/  (2 files)
      … 2 files under this directory
    translations/  (23 files)
      … 23 files under this directory
    __init__.py
    __main__.py
    _utils.py
    action.py
    cache.py
    callbacks.py
    chat_context.py
    chat_settings.py
    config.py
    context.py
    element.py
    emitter.py
    input_widget.py
    logger.py
    markdown.py
    mcp.py
    message.py
    mode.py
    oauth_providers.py
    py.typed
    secret.py
    server.py
    session.py
    sidebar.py
    … 9 more files
  tests/  (42 files)
    auth/  (2 files)
      … 2 files under this directory
    data/  (8 files)
      … 8 files under this directory
    langchain/  (4 files)
      … 4 files under this directory
    llama_index/  (1 files)
      … 1 files under this directory
    __init__.py
    conftest.py
    test_action.py
    test_cache.py
    test_callbacks.py
    test_chat_context.py
    test_chat_settings.py
    test_config.py
    test_context.py
    test_element.py
    test_emitter.py
    test_input_widget.py
    test_markdown.py
    test_mcp.py
    test_message.py
    test_modes.py
    test_oauth_providers.py
    test_server.py
    test_session.py
    test_sidebar.py
    test_slack_socket_mode.py
    test_socket.py
    test_step.py
    test_teams_adapter.py
    … 3 more files
  README.md
  build.py
  pyproject.toml
cypress/  (132 files)
  e2e/  (126 files)
    action/  (2 files)
      … 2 files under this directory
    ask_custom_element/  (3 files)
      … 3 files under this directory
    ask_file/  (2 files)
      … 2 files under this directory
    ask_multiple_files/  (2 files)
      … 2 files under this directory
    ask_user/  (2 files)
      … 2 files under this directory
    audio_element/  (2 files)
      … 2 files under this directory
    auth/  (2 files)
      … 2 files under this directory
    blinking_cursor/  (2 files)
      … 2 files under this directory
    chat_context/  (2 files)
      … 2 files under this directory
    chat_prefill/  (2 files)
      … 2 files under this directory
    chat_profiles/  (2 files)
      … 2 files under this directory
    chat_settings/  (2 files)
      … 2 files under this directory
    command/  (2 files)
      … 2 files under this directory
    config_overrides/  (2 files)
      … 2 files under this directory
    context/  (2 files)
      … 2 files under this directory
    copilot/  (2 files)
      … 2 files under this directory
    custom_build/  (5 files)
      … 5 files under this directory
    custom_data_layer/  (1 files)
      … 1 files under this directory
    custom_element/  (3 files)
      … 3 files under this directory
    custom_element_auth/  (3 files)
      … 3 files under this directory
    custom_element_command/  (3 files)
      … 3 files under this directory
    custom_theme/  (3 files)
      … 3 files under this directory
    data_layer/  (3 files)
      … 3 files under this directory
    dataframe/  (2 files)
      … 2 files under this directory
    edit_message/  (2 files)
      … 2 files under this directory
    elements/  (2 files)
      … 2 files under this directory
    error_handling/  (2 files)
      … 2 files under this directory
    file_element/  (2 files)
      … 2 files under this directory
    header_auth/  (2 files)
      … 2 files under this directory
    llama_index_cb/  (2 files)
      … 2 files under this directory
    modes/  (2 files)
      … 2 files under this directory
    oauth_auth/  (2 files)
      … 2 files under this directory
    on_chat_start/  (2 files)
      … 2 files under this directory
    password_auth/  (2 files)
      … 2 files under this directory
    pdf_viewer/  (2 files)
      … 2 files under this directory
    plotly/  (2 files)
      … 2 files under this directory
    pyplot/  (2 files)
      … 2 files under this directory
    readme/  (3 files)
      … 3 files under this directory
    remove_elements/  (2 files)
      … 2 files under this directory
    remove_step/  (2 files)
      … 2 files under this directory
    sidebar/  (2 files)
      … 2 files under this directory
    starters/  (2 files)
      … 2 files under this directory
    starters_categories/  (2 files)
      … 2 files under this directory
    step/  (5 files)
      … 5 files under this directory
    step_icon/  (2 files)
      … 2 files under this directory
    stop_task/  (5 files)
      … 5 files under this directory
    streaming/  (2 files)
      … 2 files under this directory
    tasklist/  (2 files)
      … 2 files under this directory
    thread_resume/  (2 files)
      … 2 files under this directory
    update_step/  (2 files)
      … 2 files under this directory
    upload_attachments/  (2 files)
      … 2 files under this directory
    user_env/  (4 files)
      … 4 files under this directory
    user_session/  (2 files)
      … 2 files under this directory
    window_message/  (3 files)
      … 3 files under this directory
  fixtures/  (3 files)
    hello.cpp
    hello.py
    state_of_the_union.txt
  support/  (3 files)
    e2e.ts
    run.ts
    testUtils.ts
docs/  (8 files)
  plans/  (2 files)
    2026-03-31-eslint-v9-migration.md
    2026-04-06-ci-cache-p2-react-client-build-cache.md
  research/  (3 files)
    ci-cache-optimization.md
    copilot-type-checking.md
    e2e-parallel-execution.md
  README.md
  context7.md
  security-advisory-2026-mcp.md
frontend/  (231 files)
  public/  (3 files)
    favicon.svg
    logo_dark.svg
    logo_light.svg
  src/  (211 files)
    api/  (1 files)
      … 1 files under this directory
    assets/  (2 files)
      … 2 files under this directory
    components/  (173 files)
      … 173 files under this directory
    contexts/  (1 files)
      … 1 files under this directory
    hooks/  (7 files)
      … 7 files under this directory
    i18n/  (2 files)
      … 2 files under this directory
    lib/  (3 files)
      … 3 files under this directory
    pages/  (7 files)
      … 7 files under this directory
    state/  (3 files)
      … 3 files under this directory
    types/  (5 files)
      … 5 files under this directory
    App.tsx
    AppWrapper.tsx
    index.css
    index.d.ts
    main.tsx
    router.tsx
    vite-env.d.ts
  tests/  (7 files)
    FavoriteButton.spec.tsx
    NewChat.spec.tsx
    content.spec.tsx
    displayModePrecedence.spec.ts
    icon.spec.tsx
    setup-tests.ts
    tsconfig.json
  .gitignore
  components.json
  index.html
  package.json
  postcss.config.js
  tailwind.config.js
  tsconfig.json
  tsconfig.node.json
  vite.config.ts
  vitest.config.ts
libs/  (78 files)
  copilot/  (30 files)
    .storybook/  (2 files)
      … 2 files under this directory
    src/  (18 files)
      … 18 files under this directory
    stories/  (1 files)
      … 1 files under this directory
    components.json
    index.tsx
    package.json
    postcss.config.js
    sonner.css
    tailwind.config.js
    tsconfig.json
    tsconfig.node.json
    vite.config.ts
  react-client/  (48 files)
    src/  (43 files)
      … 43 files under this directory
    README.md
    package.json
    tsconfig.build.json
    tsconfig.json
    vitest.config.ts
scripts/  (4 files)
  check-pnpm-overrides.mjs
  format.py
  lint.py
  type_check.py
.editorconfig
.gitattributes
.gitignore
.prettierignore
.prettierrc
AGENTS.md
CHANGELOG.md
CLAUDE.md
CONTRIBUTING.md
LICENSE
PRIVACY_POLICY.md
RELENG.md
SECURITY.md
cypress.config.ts
eslint.config.mjs
lint-staged.config.js
package.json
pnpm-workspace.yaml
pyproject.toml
tsconfig.json
```

## Entry points

- [backend/chainlit/__main__.py:3](https://github.com/Chainlit/chainlit/blob/190ea74239d9e84b26e7c91bc2882dd038942564/backend/chainlit/__main__.py#L3)
- [backend/chainlit/cli/__init__.py:53](https://github.com/Chainlit/chainlit/blob/190ea74239d9e84b26e7c91bc2882dd038942564/backend/chainlit/cli/__init__.py#L53)
- [backend/chainlit/server.py:228](https://github.com/Chainlit/chainlit/blob/190ea74239d9e84b26e7c91bc2882dd038942564/backend/chainlit/server.py#L228)
- [scripts/format.py:15](https://github.com/Chainlit/chainlit/blob/190ea74239d9e84b26e7c91bc2882dd038942564/scripts/format.py#L15)
- [scripts/lint.py:15](https://github.com/Chainlit/chainlit/blob/190ea74239d9e84b26e7c91bc2882dd038942564/scripts/lint.py#L15)
- [scripts/type_check.py:15](https://github.com/Chainlit/chainlit/blob/190ea74239d9e84b26e7c91bc2882dd038942564/scripts/type_check.py#L15)
- [frontend/src/App.tsx](https://github.com/Chainlit/chainlit/blob/190ea74239d9e84b26e7c91bc2882dd038942564/frontend/src/App.tsx)
- [frontend/src/api/index.ts](https://github.com/Chainlit/chainlit/blob/190ea74239d9e84b26e7c91bc2882dd038942564/frontend/src/api/index.ts)
- [frontend/src/i18n/index.ts](https://github.com/Chainlit/chainlit/blob/190ea74239d9e84b26e7c91bc2882dd038942564/frontend/src/i18n/index.ts)
- [frontend/src/main.tsx](https://github.com/Chainlit/chainlit/blob/190ea74239d9e84b26e7c91bc2882dd038942564/frontend/src/main.tsx)
- [frontend/src/pages/Page.tsx](https://github.com/Chainlit/chainlit/blob/190ea74239d9e84b26e7c91bc2882dd038942564/frontend/src/pages/Page.tsx)
- [frontend/src/types/index.ts](https://github.com/Chainlit/chainlit/blob/190ea74239d9e84b26e7c91bc2882dd038942564/frontend/src/types/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 9 file(s) under api layer (observed from repository paths and static analysis). |
| backend package | library | Observed | Groups 47 file(s) under backend package (observed from repository paths and static analysis). Observed top-level classes: AWSCognitoOAuthProvider, Action, ActionSpec, AskActionMessage, AskActionResponse, AskActionSpec.… |
| Configuration and deployment | config | Observed | Groups 43 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: AudioFeature, ChainlitConfig, ChainlitConfigOverrides, CodeSettings, FeaturesSetting… |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| cypress package | library | Observed | Groups 70 file(s) under cypress package (observed from repository paths and static analysis). Observed top-level functions: auth_callback, data_layer, handle_message, main, message, sync_function. |
| Data layer | data | Observed | Groups 14 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AzureBlobStorageClient, AzureStorageClient, BaseDataLayer, BaseStorageClient, ChainlitDataLayer, Dynam… |
| Application entry point | entrypoint | Observed | Groups 59 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed routes: GET /public/{filename:path}, GET /assets/{filename:… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| frontend package | library | Observed | Groups 211 file(s) under frontend package (observed from repository paths and static analysis). |
| libs package | library | Observed | Groups 60 file(s) under libs package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 49 file(s) under tests (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed top-level classes: TestAWSCognitoOAuthProvider, TestAction, TestAskActionMess… |

## Important files

- `.claude/settings.json` (config)
- `.cursor/settings.json` (config)
- `.editorconfig` (config)
- `.github/actions/pnpm-node-install/action.yaml` (config)
- `.github/actions/uv-python-install/action.yaml` (config)
- `.github/workflows/check-backend.yaml` (ci)
- `.github/workflows/check-frontend.yaml` (ci)
- `.github/workflows/ci.yaml` (ci)
- `.github/workflows/close_stale.yml` (ci)
- `.github/workflows/copilot-setup-steps.yaml` (ci)
- `.github/workflows/e2e-tests.yaml` (ci)
- `.github/workflows/publish-libs.yaml` (ci)
- `.github/workflows/publish.yaml` (ci)
- `.github/workflows/tests.yaml` (ci)
- `.serena/project.yml` (config)
- `backend/chainlit/translations/ar-SA.json` (config)
- `backend/chainlit/translations/bn.json` (config)
- `backend/chainlit/translations/da-DK.json` (config)
- `backend/chainlit/translations/de-DE.json` (config)
- `backend/chainlit/translations/el-GR.json` (config)
- `backend/chainlit/translations/en-US.json` (config)
- `backend/chainlit/translations/es.json` (config)
- `backend/chainlit/translations/fr-FR.json` (config)
- `backend/chainlit/translations/gu.json` (config)
- `backend/chainlit/translations/he-IL.json` (config)
- `backend/chainlit/translations/hi.json` (config)
- `backend/chainlit/translations/it.json` (config)
- `backend/chainlit/translations/ja.json` (config)
- `backend/chainlit/translations/kn.json` (config)
- `backend/chainlit/translations/ko.json` (config)
- `backend/chainlit/translations/ml.json` (config)
- `backend/chainlit/translations/mr.json` (config)
- `backend/chainlit/translations/nl.json` (config)
- `backend/chainlit/translations/pt-PT.json` (config)
- `backend/chainlit/translations/ta.json` (config)
- `backend/chainlit/translations/te.json` (config)
- `backend/chainlit/translations/zh-CN.json` (config)
- `backend/chainlit/translations/zh-TW.json` (config)
- `backend/pyproject.toml` (manifest)
- `cypress/e2e/custom_build/.chainlit/config.toml` (config)
- `cypress/e2e/custom_theme/public/theme.json` (config)
- `cypress/e2e/user_env/.chainlit/config.toml` (config)
- `frontend/components.json` (config)
- `frontend/package.json` (manifest)
- `frontend/tsconfig.json` (config)
- `frontend/tsconfig.node.json` (config)
- `libs/copilot/components.json` (config)
- `libs/copilot/package.json` (manifest)
- `libs/copilot/tsconfig.json` (config)
- `libs/copilot/tsconfig.node.json` (config)
- `libs/react-client/package.json` (manifest)
- `libs/react-client/tsconfig.build.json` (config)
- `libs/react-client/tsconfig.json` (config)
- `package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `pyproject.toml` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `frontend` — 231 analysed file(s)
- `backend` — 135 analysed file(s)
- `cypress` — 132 analysed file(s)
- `libs` — 78 analysed file(s)
- `(root files)` — 20 analysed file(s)
- `.github` — 15 analysed file(s)
- `docs` — 8 analysed file(s)
- `.shared` — 4 analysed file(s)
- `scripts` — 4 analysed file(s)
- `.serena` — 2 analysed file(s)
- `.claude` — 1 analysed file(s)
- `.cursor` — 1 analysed file(s)
- `.husky` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 6 file(s) were skipped during inventory (1 x likely secret file excluded; 3 x lockfile excluded; 2 x vendored/generated directory excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- The GitHub repository was marked archived at selection time.

Commit `190ea74239d9e84b26e7c91bc2882dd038942564` is the revision these paths and observations refer to.
