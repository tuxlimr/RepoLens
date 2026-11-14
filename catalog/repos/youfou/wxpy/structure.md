# Project structure: youfou/wxpy

**Analysed commit:** `ab63e12da822dc85615fa203e5be9fa28ae0b59f`

**Commit reference:** [ab63e12da822dc85615fa203e5be9fa28ae0b59f](https://github.com/youfou/wxpy/commit/ab63e12da822dc85615fa203e5be9fa28ae0b59f)

**Tree at this commit:** [youfou/wxpy@ab63e12da822](https://github.com/youfou/wxpy/tree/ab63e12da822dc85615fa203e5be9fa28ae0b59f)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | youfou/wxpy |
| Description | 微信机器人 / 可能是最优雅的微信个人号 API ✨✨ |
| Stars | 14252 |
| Forks | 2349 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `ab63e12da822dc85615fa203e5be9fa28ae0b59f` |
| Retrieved at | 2026-11-14T19:09:30.743422+00:00 |
| Files in this snapshot | 75 |

## Directory tree

```text
docs/  (13 files)
  Makefile
  bot.rst
  chats.rst
  conf.py
  console.rst
  faq.rst
  index.rst
  itchat.rst
  logging_with_wechat.rst
  make.bat
  messages.rst
  response_error.rst
  utils.rst
tests/  (18 files)
  api/  (13 files)
    chats/  (9 files)
      … 9 files under this directory
    messages/  (2 files)
      … 2 files under this directory
    __init__.py
    test_bot.py
  attachments/  (1 files)
    file.txt
  ext/  (1 files)
    __init__.py
  utils/  (1 files)
    __init__.py
  __init__.py
  conftest.py
wxpy/  (37 files)
  api/  (19 files)
    chats/  (9 files)
      … 9 files under this directory
    messages/  (7 files)
      … 7 files under this directory
    __init__.py
    bot.py
    consts.py
  compatible/  (2 files)
    __init__.py
    utils.py
  ext/  (6 files)
    __init__.py
    logging_with_wechat.py
    sync_message_in_groups.py
    talk_bot_utils.py
    tuling.py
    xiaoi.py
  utils/  (6 files)
    __init__.py
    base_request.py
    console.py
    misc.py
    puid_map.py
    tools.py
  __compat__.py
  __init__.py
  __main__.py
  exceptions.py
.gitignore
LICENSE
MANIFEST.in
README.rst
requirements.txt
setup.cfg
setup.py
```

## Entry points

- [wxpy/__main__.py:5](https://github.com/youfou/wxpy/blob/ab63e12da822dc85615fa203e5be9fa28ae0b59f/wxpy/__main__.py#L5)
- [wxpy/utils/__init__.py](https://github.com/youfou/wxpy/blob/ab63e12da822dc85615fa203e5be9fa28ae0b59f/wxpy/utils/__init__.py)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 19 file(s) under api layer (observed from repository paths and static analysis). Observed top-level classes: Article, Bot, Chat, Chats, Friend, Group. Observed top-level functions: wrapped_send. |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 18 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: TestBot, TestChat, TestChats, TestFriend, TestGroup, TestGroups. Observed top-level functions: base_dir, bo… |
| wxpy package | library | Observed | Groups 17 file(s) under wxpy package (observed from repository paths and static analysis). Observed top-level classes: BaseRequest, PuidMap, ResponseError, TemporaryDirectory, Tuling, TwoWayDict. Observed top-level func… |

## Important files

- `MANIFEST.in` (manifest)
- `requirements.txt` (manifest)
- `setup.cfg` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `wxpy` — 37 analysed file(s)
- `tests` — 18 analysed file(s)
- `docs` — 13 analysed file(s)
- `(root files)` — 7 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- The GitHub repository was marked archived at selection time.

Commit `ab63e12da822dc85615fa203e5be9fa28ae0b59f` is the revision these paths and observations refer to.
