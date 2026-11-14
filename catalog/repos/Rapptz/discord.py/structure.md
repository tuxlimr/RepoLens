# Project structure: Rapptz/discord.py

**Analysed commit:** `65232c38702be5844cf2ce865a4777eb1928b5d0`

**Commit reference:** [65232c38702be5844cf2ce865a4777eb1928b5d0](https://github.com/Rapptz/discord.py/commit/65232c38702be5844cf2ce865a4777eb1928b5d0)

**Tree at this commit:** [Rapptz/discord.py@65232c38702b](https://github.com/Rapptz/discord.py/tree/65232c38702be5844cf2ce865a4777eb1928b5d0)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Rapptz/discord.py |
| Description | An API wrapper for Discord written in Python. |
| Stars | 16210 |
| Forks | 3898 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `65232c38702be5844cf2ce865a4777eb1928b5d0` |
| Retrieved at | 2026-11-14T19:08:54.839374+00:00 |
| Files in this snapshot | 279 |

## Directory tree

```text
.github/  (12 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.yml
    config.yml
    feature_request.yml
  workflows/  (6 files)
    scripts/  (1 files)
      … 1 files under this directory
    build.yml
    crowdin_download.yml
    crowdin_upload.yml
    lint.yml
    test.yml
  CONTRIBUTING.md
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
discord/  (146 files)
  app_commands/  (10 files)
    __init__.py
    checks.py
    commands.py
    errors.py
    installs.py
    models.py
    namespace.py
    transformers.py
    translator.py
    tree.py
  bin/  (1 files)
    COPYING
  ext/  (15 files)
    commands/  (14 files)
      … 14 files under this directory
    tasks/  (1 files)
      … 1 files under this directory
  types/  (34 files)
    __init__.py
    activity.py
    appinfo.py
    audit_log.py
    automod.py
    channel.py
    command.py
    components.py
    embed.py
    emoji.py
    gateway.py
    guild.py
    integration.py
    interactions.py
    invite.py
    member.py
    message.py
    onboarding.py
    poll.py
    role.py
    scheduled_event.py
    sku.py
    snowflake.py
    soundboard.py
    … 10 more files
  ui/  (20 files)
    __init__.py
    action_row.py
    button.py
    checkbox.py
    container.py
    dynamic.py
    file.py
    file_upload.py
    item.py
    label.py
    media_gallery.py
    modal.py
    radio.py
    section.py
    select.py
    separator.py
    text_display.py
    text_input.py
    thumbnail.py
    view.py
  webhook/  (3 files)
    __init__.py
    async_.py
    sync.py
  __init__.py
  __main__.py
  _types.py
  abc.py
  activity.py
  appinfo.py
  asset.py
  audit_logs.py
  automod.py
  backoff.py
  channel.py
  client.py
  collectible.py
  colour.py
  components.py
  context_managers.py
  embeds.py
  emoji.py
  enums.py
  errors.py
  file.py
  flags.py
  gateway.py
  guild.py
  … 39 more files
docs/  (63 files)
  _static/  (9 files)
    codeblocks.css
    copy.js
    custom.js
    drop_down_icon.svg
    icons.css
    scorer.js
    settings.js
    sidebar.js
    style.css
  _templates/  (4 files)
    gettext/  (1 files)
      … 1 files under this directory
    genindex.html
    layout.html
    relations.html
  ext/  (6 files)
    commands/  (5 files)
      … 5 files under this directory
    tasks/  (1 files)
      … 1 files under this directory
  extensions/  (7 files)
    attributetable.py
    builder.py
    colour_preview.py
    details.py
    exception_hierarchy.py
    nitpick_file_ignorer.py
    resourcelinks.py
  images/  (2 files)
    snake.svg
    snake_dark.svg
  interactions/  (1 files)
    api.rst
  locale/  (17 files)
    ja/  (17 files)
      … 17 files under this directory
  Makefile
  api.rst
  conf.py
  crowdin.yml
  discord.rst
  faq.rst
  index.rst
  intents.rst
  intro.rst
  logging.rst
  make.bat
  migrating.rst
  migrating_to_async.rst
  migrating_to_v1.rst
  quickstart.rst
  version_guarantees.rst
  whats_new.rst
examples/  (30 files)
  app_commands/  (2 files)
    basic.py
    transformers.py
  modals/  (3 files)
    basic.py
    label.py
    report.py
  views/  (11 files)
    confirm.py
    counter.py
    dropdown.py
    dynamic_counter.py
    embed_like.py
    ephemeral.py
    layout.py
    link.py
    persistent.py
    settings.py
    tic_tac_toe.py
  advanced_startup.py
  background_task.py
  background_task_asyncio.py
  basic_bot.py
  basic_voice.py
  converters.py
  custom_context.py
  deleted.py
  edits.py
  guessing_game.py
  new_member.py
  reaction_roles.py
  reply.py
  secret.py
tests/  (18 files)
  test_annotated_annotation.py
  test_app_commands_autocomplete.py
  test_app_commands_description.py
  test_app_commands_group.py
  test_app_commands_invoke.py
  test_colour.py
  test_embed.py
  test_ext_commands_cog.py
  test_ext_commands_description.py
  test_ext_tasks.py
  test_files.py
  test_http.py
  test_permissions_all.py
  test_ui_buttons.py
  test_ui_modals.py
  test_ui_selects.py
  test_ui_view.py
  test_utils.py
.git-blame-ignore-revs
.gitignore
.readthedocs.yml
LICENSE
MANIFEST.in
README.ja.rst
README.rst
pyproject.toml
requirements.txt
setup.py
```

## Entry points

- [discord/__main__.py:364](https://github.com/Rapptz/discord.py/blob/65232c38702be5844cf2ce865a4777eb1928b5d0/discord/__main__.py#L364)
- [discord/app_commands/commands.py:2013](https://github.com/Rapptz/discord.py/blob/65232c38702be5844cf2ce865a4777eb1928b5d0/discord/app_commands/commands.py#L2013)
- [discord/app_commands/tree.py:922](https://github.com/Rapptz/discord.py/blob/65232c38702be5844cf2ce865a4777eb1928b5d0/discord/app_commands/tree.py#L922)
- [discord/ext/commands/cog.py:315](https://github.com/Rapptz/discord.py/blob/65232c38702be5844cf2ce865a4777eb1928b5d0/discord/ext/commands/cog.py#L315)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: derive_version. |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AllChannels, AppCommand, AppCommandChannel, AppCommandGroup, AppCommandPermissions, AppCommandThread. O… |
| discord package | library | Observed | Groups 137 file(s) under discord package (observed from repository paths and static analysis). Observed top-level classes: ActionRow, Activity, ActivityAssets, ActivityEmoji, ActivityParty, ActivitySecrets. Observed top… |
| Application entry point | entrypoint | Observed | Groups 4 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Command, Group. Observed top-level classes: Cog, CogMeta, Command, CommandTree… |
| External integrations | external | Observed | Groups 2 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: Client, VoiceClient, VoiceProtocol, _LoopSentinel. |
| Tests | test | Observed | Groups 18 file(s) under tests (observed from repository paths and static analysis). Observed application object created via Group. Observed top-level classes: ClassBased, DynamicButton, MockCommandInteraction, MockTree,… |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/workflows/build.yml` (ci)
- `.github/workflows/crowdin_download.yml` (ci)
- `.github/workflows/crowdin_upload.yml` (ci)
- `.github/workflows/lint.yml` (ci)
- `.github/workflows/scripts/close_and_reopen_pr.js` (ci)
- `.github/workflows/test.yml` (ci)
- `.readthedocs.yml` (config)
- `MANIFEST.in` (manifest)
- `docs/crowdin.yml` (config)
- `pyproject.toml` (manifest)
- `requirements.txt` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `discord` — 146 analysed file(s)
- `docs` — 63 analysed file(s)
- `examples` — 30 analysed file(s)
- `tests` — 18 analysed file(s)
- `.github` — 12 analysed file(s)
- `(root files)` — 10 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `65232c38702be5844cf2ce865a4777eb1928b5d0` is the revision these paths and observations refer to.
