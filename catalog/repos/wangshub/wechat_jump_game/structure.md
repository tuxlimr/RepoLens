# Project structure: wangshub/wechat_jump_game

**Analysed commit:** `3cbbb07957901821542fcfc231a09b4f3c9318c9`

**Commit reference:** [3cbbb07957901821542fcfc231a09b4f3c9318c9](https://github.com/wangshub/wechat_jump_game/commit/3cbbb07957901821542fcfc231a09b4f3c9318c9)

**Tree at this commit:** [wangshub/wechat_jump_game@3cbbb0795790](https://github.com/wangshub/wechat_jump_game/tree/3cbbb07957901821542fcfc231a09b4f3c9318c9)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | wangshub/wechat_jump_game |
| Description | 微信《跳一跳》Python 辅助 |
| Stars | 13847 |
| Forks | 4211 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `3cbbb07957901821542fcfc231a09b4f3c9318c9` |
| Retrieved at | 2026-11-14T19:09:41.787845+00:00 |
| Files in this snapshot | 63 |

## Directory tree

```text
.github/  (3 files)
  CONTRIBUTING.md
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
Tools/  (1 files)
  README.md
common/  (7 files)
  UnicodeStreamFilter.py
  __init__.py
  ai.py
  auto_adb.py
  config.py
  debug.py
  screenshot.py
config/  (27 files)
  1280x720/  (1 files)
    config.json
  1440x720/  (1 files)
    config.json
  1800x1080/  (1 files)
    config.json
  1920x1080/  (1 files)
    config.json
  2160x1080/  (1 files)
    config.json
  2560x1440/  (1 files)
    config.json
  960x540/  (1 files)
    config.json
  huawei/  (2 files)
    honorV8
    honor_note8_config.json
  iPhone/  (5 files)
    6_config.json
    8P_7P_6sP_6P_config.json
    8_config.json
    SE_config.json
    X_config.json
  mi/  (7 files)
    max2_config.json
    mi5_config.json
    mi5s_config.json
    mi5x_config.json
    mi6_config.json
    mix2_config.json
    note2_config.json
  samsung/  (3 files)
    s7edge_config.json
    s8.json
    s8在设置里关闭曲面侧屏
  smartisan/  (1 files)
    pro2_config.json
  720x1280
  default.json
jump_bot/  (9 files)
  jumpbot/  (6 files)
    algos.py
    auto.py
    bot.py
    connector.py
    manual.py
    settings.py
  Makefile
  README.rst
  requirements.txt
resource/  (1 files)
  model/  (1 files)
    checkpoint
.gitignore
LICENSE
Makefile
README.md
README.rst
changelog.md
requirements.txt
wechat_jump.py
wechat_jump_auto.py
wechat_jump_auto_ai.py
wechat_jump_auto_curves.py
wechat_jump_auto_iOS.py
wechat_jump_auto_slim.py
wechat_jump_iOS_py3.py
wechat_jump_py3.py
```

## Entry points

- [jump_bot/jumpbot/bot.py:37](https://github.com/wangshub/wechat_jump_game/blob/3cbbb07957901821542fcfc231a09b4f3c9318c9/jump_bot/jumpbot/bot.py#L37)
- [wechat_jump_auto.py:254](https://github.com/wangshub/wechat_jump_game/blob/3cbbb07957901821542fcfc231a09b4f3c9318c9/wechat_jump_auto.py#L254)
- [wechat_jump_auto_ai.py:421](https://github.com/wangshub/wechat_jump_game/blob/3cbbb07957901821542fcfc231a09b4f3c9318c9/wechat_jump_auto_ai.py#L421)
- [wechat_jump_auto_curves.py:382](https://github.com/wangshub/wechat_jump_game/blob/3cbbb07957901821542fcfc231a09b4f3c9318c9/wechat_jump_auto_curves.py#L382)
- [wechat_jump_auto_iOS.py:208](https://github.com/wangshub/wechat_jump_game/blob/3cbbb07957901821542fcfc231a09b4f3c9318c9/wechat_jump_auto_iOS.py#L208)
- [wechat_jump_auto_slim.py:219](https://github.com/wangshub/wechat_jump_game/blob/3cbbb07957901821542fcfc231a09b4f3c9318c9/wechat_jump_auto_slim.py#L219)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| common package | library | Observed | Groups 6 file(s) under common package (observed from repository paths and static analysis). Observed top-level classes: auto_adb. Observed top-level functions: add_data, backup_screenshot, check_screenshot, computing_er… |
| Configuration and deployment | config | Observed | Groups 28 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: _get_screen_size, get_bot_params, open_accordant_config. |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). Observed top-level functions: jump, on_click, pull_screenshot, search, update_data, updatefig. |
| Application entry point | entrypoint | Observed | Groups 6 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: backup_screenshot, check_screenshot, config, find_piece, find_piece_and_board, hsv2rgb. |
| jump_bot package | library | Observed | Groups 4 file(s) under jump_bot package (observed from repository paths and static analysis). Observed top-level classes: AutoBot, Connector, ManualBot. Observed top-level functions: get_press_time. |

## Important files

- `config/1280x720/config.json` (config)
- `config/1440x720/config.json` (config)
- `config/1800x1080/config.json` (config)
- `config/1920x1080/config.json` (config)
- `config/2160x1080/config.json` (config)
- `config/2560x1440/config.json` (config)
- `config/960x540/config.json` (config)
- `config/default.json` (config)
- `config/huawei/honor_note8_config.json` (config)
- `config/iPhone/6_config.json` (config)
- `config/iPhone/8P_7P_6sP_6P_config.json` (config)
- `config/iPhone/8_config.json` (config)
- `config/iPhone/SE_config.json` (config)
- `config/iPhone/X_config.json` (config)
- `config/mi/max2_config.json` (config)
- `config/mi/mi5_config.json` (config)
- `config/mi/mi5s_config.json` (config)
- `config/mi/mi5x_config.json` (config)
- `config/mi/mi6_config.json` (config)
- `config/mi/mix2_config.json` (config)
- `config/mi/note2_config.json` (config)
- `config/samsung/s7edge_config.json` (config)
- `config/samsung/s8.json` (config)
- `config/smartisan/pro2_config.json` (config)
- `jump_bot/requirements.txt` (manifest)
- `requirements.txt` (manifest)

## Top-level layout

- `config` — 27 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `jump_bot` — 9 analysed file(s)
- `common` — 7 analysed file(s)
- `.github` — 3 analysed file(s)
- `Tools` — 1 analysed file(s)
- `resource` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `3cbbb07957901821542fcfc231a09b4f3c9318c9` is the revision these paths and observations refer to.
