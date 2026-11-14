# Project structure: xming521/WeClone

**Analysed commit:** `c9b346cf2a903a4112ff62bb415083497ba13f1d`

**Commit reference:** [c9b346cf2a903a4112ff62bb415083497ba13f1d](https://github.com/xming521/WeClone/commit/c9b346cf2a903a4112ff62bb415083497ba13f1d)

**Tree at this commit:** [xming521/WeClone@c9b346cf2a90](https://github.com/xming521/WeClone/tree/c9b346cf2a903a4112ff62bb415083497ba13f1d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | xming521/WeClone |
| Description | Build a portrait of your life. Assistants that know you better. Clones that sound more like you. |
| Stars | 18406 |
| Forks | 1553 |
| Licence | AGPL-3.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `c9b346cf2a903a4112ff62bb415083497ba13f1d` |
| Retrieved at | 2026-11-14T19:08:24.240737+00:00 |
| Files in this snapshot | 358 |

## Directory tree

```text
.cursor/  (1 files)
  rules/  (1 files)
    weclone-rules.mdc
.github/  (4 files)
  workflows/  (2 files)
    issue-labeler.yml
    tg_release_notification.yml
  issue-labeler.yml
  weclone-release-event.json
dataset/  (6 files)
  eval/  (3 files)
    test_data-en.json
    test_data-privacy.json
    test_data-zh.json
  media/  (1 files)
    images/  (1 files)
      … 1 files under this directory
  res_csv/  (1 files)
    sft/  (1 files)
      … 1 files under this directory
  telegram/  (1 files)
    .gitkeep
docs/  (14 files)
  en/  (6 files)
    chatbot.md
    data.md
    finetune.md
    installation.md
    profile.md
    security.md
  zh/  (7 files)
    chatbot.md
    data.md
    finetune.md
    installation.md
    profile.md
    security.md
    style.md
  CONTRIBUTING.md
scripts/  (6 files)
  check_private_llm_logs.py
  check_profile_paths.py
  check_profile_sources.py
  check_secure_storage.py
  check_web_security.py
  update_model_prices.py
tests/  (37 files)
  configs/  (2 files)
    Qwen2.5-VL.jsonc
    qwen2.5.jsonc
  tests_data/  (4 files)
    test_PII/  (1 files)
      … 1 files under this directory
    test_person/  (1 files)
      … 1 files under this directory
    distill_style_snapshot.json
    test_model_data.json
  __init__.py
  conftest.py
  fake_build.py
  profile_data.py
  test_PII.py
  test_assistant_mcp.py
  test_bot_access.py
  test_build_cost.py
  test_chat_snapshot.py
  test_chat_upload.py
  test_contacts.py
  test_deep_insights.py
  test_distill_cli.py
  test_distill_style.py
  test_distill_windows.py
  test_full_pipe.py
  test_jsonc_edit.py
  test_llm_cache.py
  test_llm_callers.py
  test_llm_inference.py
  test_llm_profile_hierarchy.py
  test_model_settings.py
  test_organize_memories.py
  test_profile_build.py
  … 7 more files
web/  (119 files)
  dev-data/  (1 files)
    .gitignore
  src/  (95 files)
    assets/  (3 files)
      … 3 files under this directory
    assistant/  (3 files)
      … 3 files under this directory
    atlas/  (24 files)
      … 24 files under this directory
    bots/  (3 files)
      … 3 files under this directory
    ds/  (2 files)
      … 2 files under this directory
    feedback/  (7 files)
      … 7 files under this directory
    i18n/  (6 files)
      … 6 files under this directory
    review/  (14 files)
      … 14 files under this directory
    settings/  (9 files)
      … 9 files under this directory
    style/  (6 files)
      … 6 files under this directory
    summary/  (3 files)
      … 3 files under this directory
    App.tsx
    Auth.tsx
    BrandMark.tsx
    Dropdown.tsx
    LanguageSwitch.tsx
    ModeSwitch.tsx
    api.ts
    base.css
    data.ts
    dropdown.css
    main.tsx
    shell.css
    store.ts
    style.css
    theme.ts
  tests/  (13 files)
    atlasFlow.test.ts
    atlasMetrics.test.ts
    buildCost.test.ts
    buildProgress.test.ts
    catalogs.test.ts
    chatUpload.test.ts
    data.test.ts
    entrance.test.ts
    graphLayout.test.ts
    graphTokens.test.ts
    modelLabels.ts
    nightIntro.test.ts
    summaryState.test.ts
  .gitignore
  .prettierignore
  .prettierrc.json
  README.md
  eslint.config.js
  i18next.config.ts
  index.html
  package.json
  tsconfig.json
  vite.config.ts
weclone/  (104 files)
  core/  (10 files)
    PII/  (2 files)
      … 2 files under this directory
    inference/  (8 files)
      … 8 files under this directory
  data/  (44 files)
    agent/  (35 files)
      … 35 files under this directory
    chat_parsers/  (1 files)
      … 1 files under this directory
    clean/  (2 files)
      … 2 files under this directory
    __init__.py
    chat_csv.py
    models.py
    qa_generator.py
    strategies.py
    utils.py
  eval/  (5 files)
    __init__.py
    cli_demo.py
    eval_model.py
    test_model.py
    web_demo.py
  prompts/  (8 files)
    __init__.py
    clean_data.py
    deep_insights.py
    distill_memory.py
    distill_style.py
    memory_organization.py
    profile_hierarchy.py
    profile_summary.py
  server/  (18 files)
    __init__.py
    api_service.py
    app.py
    assistant.py
    auth.py
    bots.py
    chat_upload.py
    client_access.py
    deep_insights.py
    errors.py
    mcp.py
    model_settings.py
    profile_build.py
    profile_intro.py
    profile_review.py
    profile_summary.py
    source_chat.py
    style_view.py
  train/  (5 files)
    __init__.py
    export_model.py
    security.py
    train_pt.py
    train_sft.py
  utils/  (11 files)
    __init__.py
    config.py
    config_models.py
    i18n.py
    jsonc_edit.py
    length_cdf.py
    log.py
    retry.py
    secure_storage.py
    token_counter.py
    tools.py
  web/  (1 files)
    __init__.py
  __init__.py
  cli.py
weclone-cloud/  (59 files)
  docs/  (7 files)
    architecture.md
    deploy.md
    install.md
    langbot.md
    maintenance.md
    providers.md
    runbook.md
  tests/  (8 files)
    __init__.py
    conftest.py
    test_api.py
    test_config.py
    test_dataset.py
    test_finetune.py
    test_scoring.py
    test_serve.py
  tools/  (9 files)
    fix_langbot_compose.py
    from_alpha.py
    inspect_data.py
    launch.py
    make_settings.py
    package_for_github.ps1
    patch_app.py
    prepare_langbot.ps1
    prepare_wechatpad.ps1
  weclone_cloud/  (11 files)
    web/  (1 files)
      … 1 files under this directory
    __init__.py
    api.py
    cli.py
    config.py
    dataset.py
    errors.py
    finetune.py
    prompts.py
    scoring.py
    serve.py
  .gitattributes
  .gitignore
  README.md
  bootstrap.ps1
  bootstrap.sh
  check-docker-link.cmd
  cloud.example.jsonc
  deploy.ps1
  langbot-demo.html
  package-to-desktop.cmd
  pyproject.toml
  secrets.example.cmd
  setup.cmd
  start-chat.cmd
  start-langbot-docker.cmd
  start-langbot.cmd
  start-persona-docker.cmd
  start-persona.cmd
  start-server.cmd
  start-wechat.cmd
  start-wechatpad.cmd
  stop-langbot-docker.cmd
  stop-server.cmd
  stop-wechatpad.cmd
.gitignore
.pre-commit-config.yaml
LICENSE
README.md
README_zh.md
ds_config.json
pyproject.toml
settings.template.jsonc
```

## Entry points

- [scripts/check_private_llm_logs.py:243](https://github.com/xming521/WeClone/blob/c9b346cf2a903a4112ff62bb415083497ba13f1d/scripts/check_private_llm_logs.py#L243)
- [scripts/check_profile_paths.py:151](https://github.com/xming521/WeClone/blob/c9b346cf2a903a4112ff62bb415083497ba13f1d/scripts/check_profile_paths.py#L151)
- [scripts/check_profile_sources.py:152](https://github.com/xming521/WeClone/blob/c9b346cf2a903a4112ff62bb415083497ba13f1d/scripts/check_profile_sources.py#L152)
- [scripts/check_secure_storage.py:488](https://github.com/xming521/WeClone/blob/c9b346cf2a903a4112ff62bb415083497ba13f1d/scripts/check_secure_storage.py#L488)
- [scripts/check_web_security.py:189](https://github.com/xming521/WeClone/blob/c9b346cf2a903a4112ff62bb415083497ba13f1d/scripts/check_web_security.py#L189)
- [scripts/update_model_prices.py:86](https://github.com/xming521/WeClone/blob/c9b346cf2a903a4112ff62bb415083497ba13f1d/scripts/update_model_prices.py#L86)
- [weclone-cloud/tools/fix_langbot_compose.py:53](https://github.com/xming521/WeClone/blob/c9b346cf2a903a4112ff62bb415083497ba13f1d/weclone-cloud/tools/fix_langbot_compose.py#L53)
- [weclone-cloud/tools/from_alpha.py:139](https://github.com/xming521/WeClone/blob/c9b346cf2a903a4112ff62bb415083497ba13f1d/weclone-cloud/tools/from_alpha.py#L139)
- [weclone-cloud/tools/inspect_data.py:304](https://github.com/xming521/WeClone/blob/c9b346cf2a903a4112ff62bb415083497ba13f1d/weclone-cloud/tools/inspect_data.py#L304)
- [weclone-cloud/tools/launch.py:298](https://github.com/xming521/WeClone/blob/c9b346cf2a903a4112ff62bb415083497ba13f1d/weclone-cloud/tools/launch.py#L298)
- [weclone-cloud/tools/make_settings.py:75](https://github.com/xming521/WeClone/blob/c9b346cf2a903a4112ff62bb415083497ba13f1d/weclone-cloud/tools/make_settings.py#L75)
- [weclone-cloud/tools/patch_app.py:61](https://github.com/xming521/WeClone/blob/c9b346cf2a903a4112ff62bb415083497ba13f1d/weclone-cloud/tools/patch_app.py#L61)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 18 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: ApiSettings, CloudConfig, FinetuneSettings, ScoringSettings, ServeSettings, _Section… |
| Data layer | data | Observed | Groups 37 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: BatchDispatcher, Build, BuildCancelled, ChatMessage, ChatSample, CleaningStrategy. Observed top-level… |
| Application entry point | entrypoint | Observed | Groups 36 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed top-level classes: DataProcessor, EmbeddingHTTPServer, Embe… |
| External integrations | external | Observed | Groups 1 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: BaseBatchMixin, CodexExecClient, LLMClient, LLMRequest, LLMResponse, OpenAICompatibleClient.… |
| Service / domain layer | service | Observed | Groups 8 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: ChinesePIIDetector, LLMAuditCall, LLMAuditLogger, Meter, PIIDetector, PIIResult. Observed t… |
| Tests | test | Observed | Groups 62 file(s) under tests (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed top-level classes: Assistant, Bot, FactPerGroupRunner, Failing, FakeClient, R… |
| web package | library | Observed | Groups 67 file(s) under web package (observed from repository paths and static analysis). |
| weclone package | library | Observed | Groups 35 file(s) under weclone package (observed from repository paths and static analysis). Observed top-level classes: AccessGrant, AccessStore, AgentDistillArgs, ApiError, ApiSettings, AssistantTools. Observed top-l… |
| weclone-cloud package | library | Observed | Groups 8 file(s) under weclone-cloud package (observed from repository paths and static analysis). Observed top-level classes: ApiError, ChatClient, CloudError, Completion, CompletionCache, ConfigError. Observed top-lev… |

## Important files

- `.github/issue-labeler.yml` (config)
- `.github/weclone-release-event.json` (config)
- `.github/workflows/issue-labeler.yml` (ci)
- `.github/workflows/tg_release_notification.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `dataset/res_csv/sft/dataset_info.json` (config)
- `ds_config.json` (config)
- `pyproject.toml` (manifest)
- `web/.prettierrc.json` (config)
- `web/package.json` (manifest)
- `web/src/i18n/locales/en/translation.json` (config)
- `web/src/i18n/locales/zh-CN/translation.json` (config)
- `web/tsconfig.json` (config)
- `weclone-cloud/pyproject.toml` (manifest)

## Top-level layout

- `web` — 119 analysed file(s)
- `weclone` — 104 analysed file(s)
- `weclone-cloud` — 59 analysed file(s)
- `tests` — 37 analysed file(s)
- `docs` — 14 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `dataset` — 6 analysed file(s)
- `scripts` — 6 analysed file(s)
- `.github` — 4 analysed file(s)
- `.cursor` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 21 file(s) were skipped during inventory (1 x lockfile excluded; 20 x vendored/generated directory excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `c9b346cf2a903a4112ff62bb415083497ba13f1d` is the revision these paths and observations refer to.
