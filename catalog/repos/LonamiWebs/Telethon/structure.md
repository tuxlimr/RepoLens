# Project structure: LonamiWebs/Telethon

**Analysed commit:** `dab6bc4d4fc0c7815f6f19c6f643d9f75d2d930c`

**Commit reference:** [dab6bc4d4fc0c7815f6f19c6f643d9f75d2d930c](https://github.com/LonamiWebs/Telethon/commit/dab6bc4d4fc0c7815f6f19c6f643d9f75d2d930c)

**Tree at this commit:** [LonamiWebs/Telethon@dab6bc4d4fc0](https://github.com/LonamiWebs/Telethon/tree/dab6bc4d4fc0c7815f6f19c6f643d9f75d2d930c)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | LonamiWebs/Telethon |
| Description | Pure Python 3 MTProto API Telegram client library, for bots too! |
| Stars | 12066 |
| Forks | 1661 |
| Licence | MIT |
| Language | Python |
| Default branch | v1 |
| Analysed commit | `dab6bc4d4fc0c7815f6f19c6f643d9f75d2d930c` |
| Retrieved at | 2026-11-14T19:10:15.112061+00:00 |
| Files in this snapshot | 225 |

## Directory tree

```text
.github/  (6 files)
  ISSUE_TEMPLATE/  (4 files)
    bug-report.yml
    config.yml
    documentation-issue.yml
    feature-request.yml
  workflows.disabled/  (1 files)
    python.yml
  pull_request_template.md
readthedocs/  (46 files)
  basic/  (5 files)
    installation.rst
    next-steps.rst
    quick-start.rst
    signing-in.rst
    updates.rst
  concepts/  (9 files)
    asyncio.rst
    botapi-vs-mtproto.rst
    chats-vs-channels.rst
    entities.rst
    errors.rst
    full-api.rst
    sessions.rst
    strings.rst
    updates.rst
  developing/  (8 files)
    coding-style.rst
    philosophy.rst
    project-structure.rst
    telegram-api-in-other-languages.rst
    test-servers.rst
    testing.rst
    tips-for-porting-the-project.rst
    understanding-the-type-language.rst
  examples/  (4 files)
    chats-and-channels.rst
    users.rst
    word-of-warning.rst
    working-with-messages.rst
  misc/  (2 files)
    changelog.rst
    compatibility-and-convenience.rst
  modules/  (8 files)
    client.rst
    custom.rst
    errors.rst
    events.rst
    helpers.rst
    network.rst
    sessions.rst
    utils.rst
  quick-references/  (4 files)
    client-reference.rst
    events-reference.rst
    faq.rst
    objects-reference.rst
  Makefile
  conf.py
  custom_roles.py
  index.rst
  make.bat
  requirements.txt
telethon/  (103 files)
  _updates/  (4 files)
    __init__.py
    entitycache.py
    messagebox.py
    session.py
  client/  (15 files)
    __init__.py
    account.py
    auth.py
    bots.py
    buttons.py
    chats.py
    dialogs.py
    downloads.py
    messageparse.py
    messages.py
    telegrambaseclient.py
    telegramclient.py
    updates.py
    uploads.py
    users.py
  crypto/  (8 files)
    __init__.py
    aes.py
    aesctr.py
    authkey.py
    cdndecrypter.py
    factorization.py
    libssl.py
    rsa.py
  errors/  (3 files)
    __init__.py
    common.py
    rpcbaseerrors.py
  events/  (12 files)
    __init__.py
    album.py
    callbackquery.py
    chataction.py
    common.py
    inlinequery.py
    messagedeleted.py
    messageedited.py
    messageread.py
    newmessage.py
    raw.py
    userupdate.py
  extensions/  (5 files)
    __init__.py
    binaryreader.py
    html.py
    markdown.py
    messagepacker.py
  network/  (14 files)
    connection/  (8 files)
      … 8 files under this directory
    __init__.py
    authenticator.py
    mtprotoplainsender.py
    mtprotosender.py
    mtprotostate.py
    requeststate.py
  sessions/  (5 files)
    __init__.py
    abstract.py
    memory.py
    sqlite.py
    string.py
  tl/  (26 files)
    core/  (5 files)
      … 5 files under this directory
    custom/  (18 files)
      … 18 files under this directory
    patched/  (1 files)
      … 1 files under this directory
    __init__.py
    tlobject.py
  __init__.py
  custom.py
  functions.py
  helpers.py
  hints.py
  password.py
  requestiter.py
  sync.py
  types.py
  utils.py
  version.py
telethon_examples/  (10 files)
  LICENSE
  README.md
  assistant.py
  gui.py
  interactive_telegram_client.py
  payment.py
  print_messages.py
  print_updates.py
  quart_login.py
  replier.py
telethon_generator/  (27 files)
  data/  (11 files)
    html/  (7 files)
      … 7 files under this directory
    errors.csv
    friendly.csv
    methods.csv
    mtproto.tl
  generators/  (4 files)
    __init__.py
    docs.py
    errors.py
    tlobject.py
  parsers/  (7 files)
    tlobject/  (4 files)
      … 4 files under this directory
    __init__.py
    errors.py
    methods.py
  __init__.py
  docswriter.py
  sourcebuilder.py
  syncerrors.py
  utils.py
tests/  (20 files)
  readthedocs/  (4 files)
    quick_references/  (2 files)
      … 2 files under this directory
    __init__.py
    conftest.py
  telethon/  (15 files)
    client/  (2 files)
      … 2 files under this directory
    crypto/  (2 files)
      … 2 files under this directory
    events/  (2 files)
      … 2 files under this directory
    extensions/  (3 files)
      … 3 files under this directory
    tl/  (2 files)
      … 2 files under this directory
    __init__.py
    test_helpers.py
    test_pickle.py
    test_utils.py
  __init__.py
.coveragerc
.gitignore
.pre-commit-config.yaml
.readthedocs.yaml
LICENSE
README.rst
dev-requirements.txt
logo.svg
optional-requirements.txt
pyproject.toml
requirements.txt
setup.py
update-docs.sh
```

## Entry points

- [setup.py:262](https://github.com/LonamiWebs/Telethon/blob/dab6bc4d4fc0c7815f6f19c6f643d9f75d2d930c/setup.py#L262)
- [telethon_examples/assistant.py:69](https://github.com/LonamiWebs/Telethon/blob/dab6bc4d4fc0c7815f6f19c6f643d9f75d2d930c/telethon_examples/assistant.py#L69)
- [telethon_examples/gui.py:371](https://github.com/LonamiWebs/Telethon/blob/dab6bc4d4fc0c7815f6f19c6f643d9f75d2d930c/telethon_examples/gui.py#L371)
- [telethon_examples/interactive_telegram_client.py:402](https://github.com/LonamiWebs/Telethon/blob/dab6bc4d4fc0c7815f6f19c6f643d9f75d2d930c/telethon_examples/interactive_telegram_client.py#L402)
- [telethon_examples/payment.py:177](https://github.com/LonamiWebs/Telethon/blob/dab6bc4d4fc0c7815f6f19c6f643d9f75d2d930c/telethon_examples/payment.py#L177)
- [telethon_examples/quart_login.py:139](https://github.com/LonamiWebs/Telethon/blob/dab6bc4d4fc0c7815f6f19c6f643d9f75d2d930c/telethon_examples/quart_login.py#L139)
- [telethon_generator/syncerrors.py:54](https://github.com/LonamiWebs/Telethon/blob/dab6bc4d4fc0c7815f6f19c6f643d9f75d2d930c/telethon_generator/syncerrors.py#L54)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: TempWorkDir. Observed top-level functions: generate, main. |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 6 file(s) under application entry point (observed from repository paths and static analysis). Observed routes: ROUTE /. Observed top-level classes: App, InteractiveTelegramClient. Observed top-level functions: al… |
| External integrations | external | Observed | Groups 15 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: AccountMethods, AuthMethods, BotMethods, ButtonMethods, ChatMethods, DialogMethods. Observe… |
| readthedocs package | library | Observed | Groups 2 file(s) under readthedocs package (observed from repository paths and static analysis). Observed top-level functions: make_link_node, setup, skip, tl_role. |
| Service / domain layer | service | Observed | Groups 5 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: GzipPacked, MessageContainer, RpcResult, TLMessage. |
| telethon package | library | Observed | Groups 83 file(s) under telethon package (observed from repository paths and static analysis). Observed top-level classes: AES, AESModeCTR, AbridgedPacketCodec, AdminLogEvent, Album, AlbumHack. Observed top-level functi… |
| telethon_examples package | library | Observed | Groups 3 file(s) under telethon_examples package (observed from repository paths and static analysis). Observed top-level functions: can_react, get_env, handler. |
| telethon_generator package | library | Observed | Groups 15 file(s) under telethon_generator package (observed from repository paths and static analysis). Observed top-level classes: DocsWriter, Error, MethodInfo, SourceBuilder, TLArg, TLObject. Observed top-level func… |
| Tests | test | Observed | Groups 20 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: TestMessageMethods, TestSyncifyAsyncContext. Observed top-level functions: _assert_equality, docs_dir, get_… |

## Important files

- `.github/ISSUE_TEMPLATE/bug-report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/documentation-issue.yml` (config)
- `.github/ISSUE_TEMPLATE/feature-request.yml` (config)
- `.github/workflows.disabled/python.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `.readthedocs.yaml` (config)
- `pyproject.toml` (manifest)
- `readthedocs/requirements.txt` (manifest)
- `requirements.txt` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `telethon` — 103 analysed file(s)
- `readthedocs` — 46 analysed file(s)
- `telethon_generator` — 27 analysed file(s)
- `tests` — 20 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `telethon_examples` — 10 analysed file(s)
- `.github` — 6 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- The GitHub repository was marked archived at selection time.

Commit `dab6bc4d4fc0c7815f6f19c6f643d9f75d2d930c` is the revision these paths and observations refer to.
