# Project structure: zhayujie/CowAgent

**Analysed commit:** `fd75a33d862fe7ea9dec2fa1c0a27f92f181985d`

**Commit reference:** [fd75a33d862fe7ea9dec2fa1c0a27f92f181985d](https://github.com/zhayujie/CowAgent/commit/fd75a33d862fe7ea9dec2fa1c0a27f92f181985d)

**Tree at this commit:** [zhayujie/CowAgent@fd75a33d862f](https://github.com/zhayujie/CowAgent/tree/fd75a33d862fe7ea9dec2fa1c0a27f92f181985d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | zhayujie/CowAgent |
| Description | Open-source personal AI assistant & Agent Harness. Plans tasks, runs tools and skills, self-evolves with memory and knowledge. Multi-agent, multi-model, multi-channel. Lightweight, extensible, one-line install. |
| Stars | 47931 |
| Forks | 10430 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `fd75a33d862fe7ea9dec2fa1c0a27f92f181985d` |
| Retrieved at | 2026-11-14T19:06:33.792964+00:00 |
| Files in this snapshot | 554 |

## Directory tree

```text
.github/  (14 files)
  ISSUE_TEMPLATE/  (3 files)
    1.bug.yml
    2.feature.yml
    config.yml
  scripts/  (1 files)
    register-releases.mjs
  workflows/  (9 files)
    deploy-image-arm.yml
    deploy-image.yml
    publish-feishu-vendor.yml
    release-overlay-win7.yml
    release-overlay.yml
    release-win7.yml
    release.yml
    test-windows-bash.yml
    test.yml
  PULL_REQUEST_TEMPLATE.md
agent/  (150 files)
  chat/  (4 files)
    __init__.py
    prompts.json
    service.py
    session_service.py
  evolution/  (7 files)
    __init__.py
    backup.py
    config.py
    executor.py
    prompts.py
    record.py
    trigger.py
  guest/  (11 files)
    __init__.py
    access.py
    actions.py
    branding.py
    paths.py
    policy.py
    profile.py
    runtime.py
    share.py
    store.py
    tools.py
  knowledge/  (2 files)
    __init__.py
    service.py
  memory/  (16 files)
    embedding/  (5 files)
      … 5 files under this directory
    __init__.py
    chunker.py
    config.py
    conversation_store.py
    manager.py
    rebuild_index.py
    reranker.py
    service.py
    storage.py
    summarizer.py
    vector_backend.py
  multiagent/  (3 files)
    __init__.py
    inbound.py
    transport.py
  permission/  (2 files)
    __init__.py
    policy.py
  prompt/  (4 files)
    __init__.py
    builder.py
    guest.py
    workspace.py
  protocol/  (12 files)
    __init__.py
    agent.py
    agent_stream.py
    artifact.py
    cancel.py
    context.py
    message_utils.py
    models.py
    result.py
    steer.py
    step_writer.py
    task.py
  skills/  (9 files)
    __init__.py
    archive.py
    config.py
    formatter.py
    frontmatter.py
    loader.py
    manager.py
    service.py
    types.py
  subagent/  (5 files)
    assets/  (2 files)
      … 2 files under this directory
    __init__.py
    runner.py
    templates.py
  tools/  (66 files)
    agent_delegate/  (2 files)
      … 2 files under this directory
    bash/  (5 files)
      … 5 files under this directory
    browser/  (5 files)
      … 5 files under this directory
    current_time/  (2 files)
      … 2 files under this directory
    edit/  (2 files)
      … 2 files under this directory
    env_config/  (2 files)
      … 2 files under this directory
    evolution_undo/  (2 files)
      … 2 files under this directory
    ls/  (2 files)
      … 2 files under this directory
    mcp/  (6 files)
      … 6 files under this directory
    memory/  (3 files)
      … 3 files under this directory
    read/  (2 files)
      … 2 files under this directory
    scheduler/  (8 files)
      … 8 files under this directory
    search_files/  (2 files)
      … 2 files under this directory
    send/  (2 files)
      … 2 files under this directory
    subagent/  (2 files)
      … 2 files under this directory
    utils/  (8 files)
      … 8 files under this directory
    vision/  (2 files)
      … 2 files under this directory
    web_fetch/  (2 files)
      … 2 files under this directory
    web_search/  (2 files)
      … 2 files under this directory
    write/  (2 files)
      … 2 files under this directory
    __init__.py
    base_tool.py
    tool_manager.py
  workspace/  (4 files)
    __init__.py
    project_store.py
    service.py
    session_prefs.py
  admin.py
  registry.py
  routing.py
  team.py
  team_addressing.py
bridge/  (6 files)
  agent_bridge.py
  agent_event_handler.py
  agent_initializer.py
  bridge.py
  context.py
  reply.py
channel/  (190 files)
  dingtalk/  (3 files)
    dingtalk_channel.py
    dingtalk_message.py
    dingtalk_stream_card.py
  discord/  (3 files)
    __init__.py
    discord_channel.py
    discord_message.py
  feishu/  (8 files)
    README.md
    domain.py
    feishu_channel.py
    feishu_message.py
    feishu_progress_card.py
    feishu_scheduler_card.py
    feishu_static_card.py
    lark_install.py
  qq/  (3 files)
    __init__.py
    qq_channel.py
    qq_message.py
  slack/  (3 files)
    __init__.py
    slack_channel.py
    slack_message.py
  telegram/  (4 files)
    __init__.py
    telegram_channel.py
    telegram_markdown.py
    telegram_message.py
  terminal/  (1 files)
    terminal_channel.py
  web/  (136 files)
    api/  (22 files)
      … 22 files under this directory
    core/  (6 files)
      … 6 files under this directory
    static/  (73 files)
      … 73 files under this directory
    templates/  (30 files)
      … 30 files under this directory
    tools/  (2 files)
      … 2 files under this directory
    README.md
    chat.html
    web_channel.py
  wechat_kf/  (4 files)
    README.md
    wechat_kf_channel.py
    wechat_kf_cursor_store.py
    wechat_kf_message.py
  wechatcom/  (4 files)
    README.md
    wechatcomapp_channel.py
    wechatcomapp_client.py
    wechatcomapp_message.py
  wechatmp/  (7 files)
    README.md
    active_reply.py
    common.py
    passive_reply.py
    wechatmp_channel.py
    wechatmp_client.py
    wechatmp_message.py
  wecom_bot/  (4 files)
    __init__.py
    wecom_bot_channel.py
    wecom_bot_crypt.py
    wecom_bot_message.py
  weixin/  (4 files)
    __init__.py
    weixin_api.py
    weixin_channel.py
    weixin_message.py
  channel.py
  channel_factory.py
  channel_instances.py
  chat_channel.py
  chat_message.py
  file_cache.py
cli/  (14 files)
  commands/  (7 files)
    __init__.py
    backup.py
    context.py
    install.py
    knowledge.py
    process.py
    skill.py
  VERSION
  __init__.py
  __main__.py
  cli.py
  config_json.py
  update_service.py
  utils.py
common/  (25 files)
  atomic_write.py
  channel_registry.py
  cloud_client.py
  const.py
  deployment.py
  dequeue.py
  directory_replace.py
  expired_dict.py
  i18n.py
  log.py
  markdown_fence.py
  media_download.py
  memory.py
  office_text.py
  package_manager.py
  runtime_identity.py
  singleton.py
  sorted_dict.py
  ssl_certs.py
  state_dir.py
  time_check.py
  tmp_dir.py
  token_bucket.py
  utils.py
  … 1 more files
desktop/  (125 files)
  scripts/  (1 files)
    apply-flavor.mjs
  src/  (116 files)
    main/  (9 files)
      … 9 files under this directory
    renderer/  (107 files)
      … 107 files under this directory
  .gitignore
  README.md
  electron-builder.js
  electron-builder.win.js
  package.json
  postcss.config.js
  tsconfig.json
  tsconfig.main.json
docker/  (1 files)
  build.latest.sh
models/  (4 files)
  deepseek/  (1 files)
    __init__.py
  doubao/  (1 files)
    __init__.py
  mimo/  (1 files)
    __init__.py
  qianfan/  (1 files)
    __init__.py
plugins/  (8 files)
  banwords/  (4 files)
    .gitignore
    __init__.py
    banwords.txt.template
    config.json.template
  cow_cli/  (1 files)
    __init__.py
  dungeon/  (1 files)
    __init__.py
  finish/  (1 files)
    __init__.py
  __init__.py
translate/  (3 files)
  baidu/  (1 files)
    __init__.py
  youdao/  (1 files)
    __init__.py
  __init__.py
voice/  (5 files)
  cowagent/  (1 files)
    __init__.py
  dashscope/  (1 files)
    __init__.py
  mimo/  (1 files)
    __init__.py
  minimax/  (1 files)
    __init__.py
  zhipuai/  (1 files)
    __init__.py
.gitignore
CONTRIBUTING.md
Dockerfile
LICENSE
README.md
SECURITY.md
app.py
config-template.json
config.py
```

## Entry points

- [agent/memory/embedding/rebuild.py:190](https://github.com/zhayujie/CowAgent/blob/fd75a33d862fe7ea9dec2fa1c0a27f92f181985d/agent/memory/embedding/rebuild.py#L190)
- [agent/memory/rebuild_index.py:11](https://github.com/zhayujie/CowAgent/blob/fd75a33d862fe7ea9dec2fa1c0a27f92f181985d/agent/memory/rebuild_index.py#L11)
- [app.py:870](https://github.com/zhayujie/CowAgent/blob/fd75a33d862fe7ea9dec2fa1c0a27f92f181985d/app.py#L870)
- [cli/cli.py:51](https://github.com/zhayujie/CowAgent/blob/fd75a33d862fe7ea9dec2fa1c0a27f92f181985d/cli/cli.py#L51)
- [cli/commands/backup.py:594](https://github.com/zhayujie/CowAgent/blob/fd75a33d862fe7ea9dec2fa1c0a27f92f181985d/cli/commands/backup.py#L594)
- [cli/commands/context.py:16](https://github.com/zhayujie/CowAgent/blob/fd75a33d862fe7ea9dec2fa1c0a27f92f181985d/cli/commands/context.py#L16)
- [cli/commands/install.py:451](https://github.com/zhayujie/CowAgent/blob/fd75a33d862fe7ea9dec2fa1c0a27f92f181985d/cli/commands/install.py#L451)
- [cli/commands/knowledge.py:27](https://github.com/zhayujie/CowAgent/blob/fd75a33d862fe7ea9dec2fa1c0a27f92f181985d/cli/commands/knowledge.py#L27)
- [cli/commands/process.py:119](https://github.com/zhayujie/CowAgent/blob/fd75a33d862fe7ea9dec2fa1c0a27f92f181985d/cli/commands/process.py#L119)
- [cli/commands/skill.py:743](https://github.com/zhayujie/CowAgent/blob/fd75a33d862fe7ea9dec2fa1c0a27f92f181985d/cli/commands/skill.py#L743)
- [cli/update_service.py:705](https://github.com/zhayujie/CowAgent/blob/fd75a33d862fe7ea9dec2fa1c0a27f92f181985d/cli/update_service.py#L705)
- [common/token_bucket.py:63](https://github.com/zhayujie/CowAgent/blob/fd75a33d862fe7ea9dec2fa1c0a27f92f181985d/common/token_bucket.py#L63)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| agent package | library | Observed | Groups 130 file(s) under agent package (observed from repository paths and static analysis). Observed top-level classes: Agent, AgentAction, AgentActionType, AgentAdminError, AgentAdminService, AgentCancelledError. Obse… |
| API layer | api | Observed | Groups 42 file(s) under api layer (observed from repository paths and static analysis). Observed top-level classes: AgentAvatarHandler, AgentCoreFileHandler, AgentsHandler, ArtifactAddHandler, ArtifactDeleteHandler, Art… |
| bridge package | library | Observed | Groups 6 file(s) under bridge package (observed from repository paths and static analysis). Observed top-level classes: AgentBridge, AgentEventHandler, AgentInitializer, AgentLLMModel, Bridge, Context. Observed top-leve… |
| channel package | library | Observed | Groups 66 file(s) under channel package (observed from repository paths and static analysis). Observed top-level classes: Channel, ChannelInstance, ChatChannel, ChatMessage, CursorStore, CustomAICardReplier. Observed to… |
| cli package | library | Observed | Groups 10 file(s) under cli package (observed from repository paths and static analysis). Observed top-level classes: InstallResult, SkillInstallError. Observed top-level functions: _apt_install, _atomic_copy, _batch_in… |
| common package | library | Observed | Groups 23 file(s) under common package (observed from repository paths and static analysis). Observed top-level classes: Dequeue, DownloadResult, ExpiredDict, MediaTooLargeError, RuntimeIdentity, SortedDict. Observed to… |
| Configuration and deployment | config | Observed | Groups 23 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: Config, EvolutionConfig, MemoryConfig. Observed top-level functions: _as_bool, _as_p… |
| Data layer | data | Observed | Groups 5 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: LLMModel, LLMRequest, ModelFactory. |
| desktop package | library | Observed | Groups 103 file(s) under desktop package (observed from repository paths and static analysis). |
| docker package | library | Observed | Groups 1 file(s) under docker package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 7 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: ChannelManager, CowCLI, InstallKind, RebuildResult, TokenBucket, UpdateError. Observed top… |
| External integrations | external | Observed | Groups 5 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: AgentRegistryUnavailable, CloudClient, McpClient, McpClientRegistry, McpHttpStatusError, Mcp… |
| plugins package | library | Observed | Groups 5 file(s) under plugins package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 27 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: BrowserService, ChatService, GuestPages, GuestRun, KnowledgeService, McpConfigError. Obser… |
| translate package | library | Observed | Groups 3 file(s) under translate package (observed from repository paths and static analysis). |
| voice package | library | Observed | Groups 5 file(s) under voice package (observed from repository paths and static analysis). |

## Important files

- `.github/ISSUE_TEMPLATE/1.bug.yml` (config)
- `.github/ISSUE_TEMPLATE/2.feature.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/deploy-image-arm.yml` (ci)
- `.github/workflows/deploy-image.yml` (ci)
- `.github/workflows/publish-feishu-vendor.yml` (ci)
- `.github/workflows/release-overlay-win7.yml` (ci)
- `.github/workflows/release-overlay.yml` (ci)
- `.github/workflows/release-win7.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/test-windows-bash.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `Dockerfile` (container)
- `agent/chat/prompts.json` (config)
- `config-template.json` (config)
- `desktop/package.json` (manifest)
- `desktop/tsconfig.json` (config)
- `desktop/tsconfig.main.json` (config)

## Top-level layout

- `channel` — 190 analysed file(s)
- `agent` — 150 analysed file(s)
- `desktop` — 125 analysed file(s)
- `common` — 25 analysed file(s)
- `.github` — 14 analysed file(s)
- `cli` — 14 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `plugins` — 8 analysed file(s)
- `bridge` — 6 analysed file(s)
- `voice` — 5 analysed file(s)
- `models` — 4 analysed file(s)
- `translate` — 3 analysed file(s)
- `docker` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 12 file(s) were skipped during inventory (12 x vendored/generated directory excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `fd75a33d862fe7ea9dec2fa1c0a27f92f181985d` is the revision these paths and observations refer to.
