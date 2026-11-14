# Project structure: HelloZeroNet/ZeroNet

**Analysed commit:** `454c0b2e7e000fda7000cba49027541fbf327b96`

**Commit reference:** [454c0b2e7e000fda7000cba49027541fbf327b96](https://github.com/HelloZeroNet/ZeroNet/commit/454c0b2e7e000fda7000cba49027541fbf327b96)

**Tree at this commit:** [HelloZeroNet/ZeroNet@454c0b2e7e00](https://github.com/HelloZeroNet/ZeroNet/tree/454c0b2e7e000fda7000cba49027541fbf327b96)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | HelloZeroNet/ZeroNet |
| Description | ZeroNet - Decentralized websites using Bitcoin crypto and BitTorrent network |
| Stars | 18777 |
| Forks | 2283 |
| Licence | Other |
| Language | JavaScript |
| Default branch | py3 |
| Analysed commit | `454c0b2e7e000fda7000cba49027541fbf327b96` |
| Retrieved at | 2026-11-14T19:11:20.078825+00:00 |
| Files in this snapshot | 532 |

## Directory tree

```text
.github/  (4 files)
  ISSUE_TEMPLATE/  (2 files)
    bug-report.md
    feature_request.md
  workflows/  (1 files)
    tests.yml
  FUNDING.yml
plugins/  (307 files)
  AnnounceBitTorrent/  (3 files)
    AnnounceBitTorrentPlugin.py
    __init__.py
    plugin_info.json
  AnnounceLocal/  (7 files)
    Test/  (3 files)
      … 3 files under this directory
    AnnounceLocalPlugin.py
    BroadcastServer.py
    __init__.py
    plugin_info.json
  AnnounceShare/  (6 files)
    Test/  (3 files)
      … 3 files under this directory
    AnnounceSharePlugin.py
    __init__.py
    plugin_info.json
  AnnounceZero/  (3 files)
    AnnounceZeroPlugin.py
    __init__.py
    plugin_info.json
  Benchmark/  (6 files)
    media/  (1 files)
      … 1 files under this directory
    BenchmarkDb.py
    BenchmarkPack.py
    BenchmarkPlugin.py
    __init__.py
    plugin_info.json
  Bigfile/  (6 files)
    Test/  (3 files)
      … 3 files under this directory
    BigfilePiecefield.py
    BigfilePlugin.py
    __init__.py
  Chart/  (5 files)
    ChartCollector.py
    ChartDb.py
    ChartPlugin.py
    __init__.py
    plugin_info.json
  ContentFilter/  (15 files)
    Test/  (3 files)
      … 3 files under this directory
    languages/  (6 files)
      … 6 files under this directory
    media/  (2 files)
      … 2 files under this directory
    ContentFilterPlugin.py
    ContentFilterStorage.py
    __init__.py
    plugin_info.json
  Cors/  (3 files)
    CorsPlugin.py
    __init__.py
    plugin_info.json
  CryptMessage/  (7 files)
    Test/  (3 files)
      … 3 files under this directory
    CryptMessage.py
    CryptMessagePlugin.py
    __init__.py
    plugin_info.json
  FilePack/  (3 files)
    FilePackPlugin.py
    __init__.py
    plugin_info.json
  MergerSite/  (11 files)
    languages/  (9 files)
      … 9 files under this directory
    MergerSitePlugin.py
    __init__.py
  Newsfeed/  (2 files)
    NewsfeedPlugin.py
    __init__.py
  OptionalManager/  (14 files)
    Test/  (3 files)
      … 3 files under this directory
    languages/  (7 files)
      … 7 files under this directory
    ContentDbPlugin.py
    OptionalManagerPlugin.py
    UiWebsocketPlugin.py
    __init__.py
  PeerDb/  (3 files)
    PeerDbPlugin.py
    __init__.py
    plugin_info.json
  Sidebar/  (35 files)
    languages/  (13 files)
      … 13 files under this directory
    media/  (14 files)
      … 14 files under this directory
    media_globe/  (3 files)
      … 3 files under this directory
    ConsolePlugin.py
    SidebarPlugin.py
    ZipStream.py
    __init__.py
    plugin_info.json
  Stats/  (3 files)
    StatsPlugin.py
    __init__.py
    plugin_info.json
  TranslateSite/  (3 files)
    TranslateSitePlugin.py
    __init__.py
    plugin_info.json
  Trayicon/  (16 files)
    languages/  (10 files)
      … 10 files under this directory
    lib/  (3 files)
      … 3 files under this directory
    TrayiconPlugin.py
    __init__.py
    plugin_info.json
  UiConfig/  (24 files)
    languages/  (5 files)
      … 5 files under this directory
    media/  (16 files)
      … 16 files under this directory
    UiConfigPlugin.py
    __init__.py
    plugin_info.json
  UiFileManager/  (82 files)
    languages/  (2 files)
      … 2 files under this directory
    media/  (78 files)
      … 78 files under this directory
    UiFileManagerPlugin.py
    __init__.py
  UiPluginManager/  (17 files)
    media/  (15 files)
      … 15 files under this directory
    UiPluginManagerPlugin.py
    __init__.py
  Zeroname/  (4 files)
    updater/  (1 files)
      … 1 files under this directory
    README.md
    SiteManagerPlugin.py
    __init__.py
  disabled-Bootstrapper/  (7 files)
    Test/  (3 files)
      … 3 files under this directory
    BootstrapperDb.py
    BootstrapperPlugin.py
    __init__.py
    plugin_info.json
  disabled-Dnschain/  (3 files)
    SiteManagerPlugin.py
    UiRequestPlugin.py
    __init__.py
  disabled-DonationMessage/  (2 files)
    DonationMessagePlugin.py
    __init__.py
  disabled-Multiuser/  (7 files)
    Test/  (3 files)
      … 3 files under this directory
    MultiuserPlugin.py
    UserPlugin.py
    __init__.py
    plugin_info.json
  disabled-StemPort/  (2 files)
    StemPortPlugin.py
    __init__.py
  disabled-UiPassword/  (4 files)
    UiPasswordPlugin.py
    __init__.py
    login.html
    plugin_info.json
  disabled-ZeronameLocal/  (3 files)
    SiteManagerPlugin.py
    UiRequestPlugin.py
    __init__.py
  __init__.py
src/  (202 files)
  Connection/  (3 files)
    Connection.py
    ConnectionServer.py
    __init__.py
  Content/  (4 files)
    ContentDb.py
    ContentDbDict.py
    ContentManager.py
    __init__.py
  Crypt/  (6 files)
    Crypt.py
    CryptBitcoin.py
    CryptConnection.py
    CryptHash.py
    CryptRsa.py
    __init__.py
  Db/  (4 files)
    Db.py
    DbCursor.py
    DbQuery.py
    __init__.py
  Debug/  (6 files)
    Debug.py
    DebugHook.py
    DebugLock.py
    DebugMedia.py
    DebugReloader.py
    __init__.py
  File/  (3 files)
    FileRequest.py
    FileServer.py
    __init__.py
  Peer/  (4 files)
    Peer.py
    PeerHashfield.py
    PeerPortchecker.py
    __init__.py
  Plugin/  (2 files)
    PluginManager.py
    __init__.py
  Site/  (5 files)
    Site.py
    SiteAnnouncer.py
    SiteManager.py
    SiteStorage.py
    __init__.py
  Test/  (55 files)
    testdata/  (17 files)
      … 17 files under this directory
    BenchmarkSsl.py
    Spy.py
    TestCached.py
    TestConfig.py
    TestConnectionServer.py
    TestContent.py
    TestContentUser.py
    TestCryptBitcoin.py
    TestCryptConnection.py
    TestCryptHash.py
    TestDb.py
    TestDbQuery.py
    TestDebug.py
    TestDiff.py
    TestEvent.py
    TestFileRequest.py
    TestFlag.py
    TestHelper.py
    TestMsgpack.py
    TestNoparallel.py
    TestPeer.py
    TestRateLimit.py
    TestSafeRe.py
    TestSite.py
    … 14 more files
  Tor/  (2 files)
    TorManager.py
    __init__.py
  Translate/  (19 files)
    languages/  (17 files)
      … 17 files under this directory
    Translate.py
    __init__.py
  Ui/  (24 files)
    media/  (18 files)
      … 18 files under this directory
    template/  (2 files)
      … 2 files under this directory
    UiRequest.py
    UiServer.py
    UiWebsocket.py
    __init__.py
  User/  (3 files)
    User.py
    UserManager.py
    __init__.py
  Worker/  (4 files)
    Worker.py
    WorkerManager.py
    WorkerTaskManager.py
    __init__.py
  lib/  (36 files)
    bencode_open/  (2 files)
      … 2 files under this directory
    cssvendor/  (2 files)
      … 2 files under this directory
    gevent_ws/  (1 files)
      … 1 files under this directory
    libsecp256k1message/  (2 files)
      … 2 files under this directory
    openssl/  (1 files)
      … 1 files under this directory
    pyaes/  (6 files)
      … 6 files under this directory
    sslcrypto/  (17 files)
      … 17 files under this directory
    subtl/  (4 files)
      … 4 files under this directory
    __init__.py
  util/  (19 files)
    Cached.py
    Diff.py
    Electrum.py
    Event.py
    Flag.py
    GreenletManager.py
    Msgpack.py
    Noparallel.py
    OpensslFindPatch.py
    Platform.py
    Pooled.py
    QueryJson.py
    RateLimit.py
    SafeRe.py
    SocksProxy.py
    ThreadPool.py
    UpnpPunch.py
    __init__.py
    helper.py
  Config.py
  __init__.py
  main.py
tools/  (3 files)
  coffee/  (3 files)
    README.md
    coffee.cmd
    coffee.wsf
.gitignore
.gitlab-ci.yml
.travis.yml
CHANGELOG.md
COPYING
Dockerfile
Dockerfile.arm64v8
LICENSE
README-ru.md
README-zh-cn.md
README.md
Vagrantfile
requirements.txt
start.py
update.py
zeronet.py
```

## Entry points

- [src/Content/ContentDbDict.py:124](https://github.com/HelloZeroNet/ZeroNet/blob/454c0b2e7e000fda7000cba49027541fbf327b96/src/Content/ContentDbDict.py#L124)
- [src/Db/Db.py:500](https://github.com/HelloZeroNet/ZeroNet/blob/454c0b2e7e000fda7000cba49027541fbf327b96/src/Db/Db.py#L500)
- [src/Debug/Debug.py:164](https://github.com/HelloZeroNet/ZeroNet/blob/454c0b2e7e000fda7000cba49027541fbf327b96/src/Debug/Debug.py#L164)
- [src/Debug/DebugHook.py:97](https://github.com/HelloZeroNet/ZeroNet/blob/454c0b2e7e000fda7000cba49027541fbf327b96/src/Debug/DebugHook.py#L97)
- [src/Debug/DebugMedia.py:131](https://github.com/HelloZeroNet/ZeroNet/blob/454c0b2e7e000fda7000cba49027541fbf327b96/src/Debug/DebugMedia.py#L131)
- [src/Peer/PeerHashfield.py:66](https://github.com/HelloZeroNet/ZeroNet/blob/454c0b2e7e000fda7000cba49027541fbf327b96/src/Peer/PeerHashfield.py#L66)
- [src/Plugin/PluginManager.py:270](https://github.com/HelloZeroNet/ZeroNet/blob/454c0b2e7e000fda7000cba49027541fbf327b96/src/Plugin/PluginManager.py#L270)
- [src/lib/cssvendor/cssvendor.py:24](https://github.com/HelloZeroNet/ZeroNet/blob/454c0b2e7e000fda7000cba49027541fbf327b96/src/lib/cssvendor/cssvendor.py#L24)
- [src/lib/libsecp256k1message/libsecp256k1message.py:146](https://github.com/HelloZeroNet/ZeroNet/blob/454c0b2e7e000fda7000cba49027541fbf327b96/src/lib/libsecp256k1message/libsecp256k1message.py#L146)
- [src/util/Cached.py:46](https://github.com/HelloZeroNet/ZeroNet/blob/454c0b2e7e000fda7000cba49027541fbf327b96/src/util/Cached.py#L46)
- [src/util/Event.py:28](https://github.com/HelloZeroNet/ZeroNet/blob/454c0b2e7e000fda7000cba49027541fbf327b96/src/util/Event.py#L28)
- [src/util/Noparallel.py:78](https://github.com/HelloZeroNet/ZeroNet/blob/454c0b2e7e000fda7000cba49027541fbf327b96/src/util/Noparallel.py#L78)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 92 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: Config, ErrorLogHandler. |
| Connection package | library | Observed | Groups 3 file(s) under connection package (observed from repository paths and static analysis). Observed top-level classes: Connection, ConnectionServer. |
| Content package | library | Observed | Groups 3 file(s) under content package (observed from repository paths and static analysis). Observed top-level classes: ContentDb, ContentManager, SignError, VerifyError. Observed top-level functions: getContentDb. |
| Crypt package | library | Observed | Groups 6 file(s) under crypt package (observed from repository paths and static analysis). Observed top-level classes: CryptConnectionManager, Sha512t. Observed top-level functions: hdPrivatekey, loadLib, newPrivatekey,… |
| Data layer | data | Observed | Groups 3 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: DbCursor, DbQuery. |
| Debug package | library | Observed | Groups 3 file(s) under debug package (observed from repository paths and static analysis). Observed top-level classes: DebugLock, DebugReloader. |
| Application entry point | entrypoint | Observed | Groups 24 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Actions, BigfilePiecefield, BigfilePiecefieldPacked, Cached, ContentDbDict, Db. Observed… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| File package | library | Observed | Groups 3 file(s) under file package (observed from repository paths and static analysis). Observed top-level classes: FileRequest, FileServer, RequestError. |
| __init__.py package | library | Observed | Groups 1 file(s) under __init__.py package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 27 file(s) under lib package (observed from repository paths and static analysis). Observed top-level classes: AES, AESBackend, AESBlockModeOfOperation, AESModeOfOperationCBC, AESModeOfOperationCFB, AESModeOfOper… |
| Peer package | library | Observed | Groups 3 file(s) under peer package (observed from repository paths and static analysis). Observed top-level classes: Peer, PeerPortchecker. |
| Plugin package | library | Observed | Groups 1 file(s) under plugin package (observed from repository paths and static analysis). |
| plugins package | library | Observed | Groups 135 file(s) under plugins package (observed from repository paths and static analysis). Observed top-level classes: ActionsPlugin, BigFile, BootstrapperDb, BroadcastServer, ChartCollector, ChartDb. Observed top-l… |
| Site package | library | Observed | Groups 5 file(s) under site package (observed from repository paths and static analysis). Observed top-level classes: AnnounceError, Site, SiteAnnouncer, SiteManager, SiteStorage. |
| Tests | test | Observed | Groups 79 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH util.UpnpPunch._get_local_ips, PATCH util.UpnpPunch._collect_idg_data, PATCH util.UpnpPunch._send_requests, PATC… |
| Tor package | library | Observed | Groups 2 file(s) under tor package (observed from repository paths and static analysis). Observed top-level classes: TorManager. |
| Translate package | library | Observed | Groups 2 file(s) under translate package (observed from repository paths and static analysis). Observed top-level classes: EscapeProxy, Translate. |
| Ui package | library | Observed | Groups 7 file(s) under ui package (observed from repository paths and static analysis). Observed top-level classes: SecurityError, UiRequest, UiServer, UiWSGIHandler, UiWebsocket. |
| User package | library | Observed | Groups 3 file(s) under user package (observed from repository paths and static analysis). Observed top-level classes: User, UserManager. |
| util package | library | Observed | Groups 12 file(s) under util package (observed from repository paths and static analysis). Observed top-level classes: Event, FilePart, Flag, GreenletManager, Lock, MainLoopCaller. Observed top-level functions: atomicWr… |
| Worker package | library | Observed | Groups 4 file(s) under worker package (observed from repository paths and static analysis). Observed top-level classes: CustomSortedList, Worker, WorkerDownloadError, WorkerIOError, WorkerManager, WorkerStop. |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/workflows/tests.yml` (ci)
- `.gitlab-ci.yml` (ci)
- `.travis.yml` (ci)
- `Dockerfile` (container)
- `Dockerfile.arm64v8` (container)
- `plugins/AnnounceBitTorrent/plugin_info.json` (config)
- `plugins/AnnounceLocal/plugin_info.json` (config)
- `plugins/AnnounceShare/plugin_info.json` (config)
- `plugins/AnnounceZero/plugin_info.json` (config)
- `plugins/Benchmark/plugin_info.json` (config)
- `plugins/Chart/plugin_info.json` (config)
- `plugins/ContentFilter/languages/hu.json` (config)
- `plugins/ContentFilter/languages/it.json` (config)
- `plugins/ContentFilter/languages/jp.json` (config)
- `plugins/ContentFilter/languages/pt-br.json` (config)
- `plugins/ContentFilter/languages/zh-tw.json` (config)
- `plugins/ContentFilter/languages/zh.json` (config)
- `plugins/ContentFilter/plugin_info.json` (config)
- `plugins/Cors/plugin_info.json` (config)
- `plugins/CryptMessage/plugin_info.json` (config)
- `plugins/FilePack/plugin_info.json` (config)
- `plugins/MergerSite/languages/es.json` (config)
- `plugins/MergerSite/languages/fr.json` (config)
- `plugins/MergerSite/languages/hu.json` (config)
- `plugins/MergerSite/languages/it.json` (config)
- `plugins/MergerSite/languages/jp.json` (config)
- `plugins/MergerSite/languages/pt-br.json` (config)
- `plugins/MergerSite/languages/tr.json` (config)
- `plugins/MergerSite/languages/zh-tw.json` (config)
- `plugins/MergerSite/languages/zh.json` (config)
- `plugins/OptionalManager/languages/es.json` (config)
- `plugins/OptionalManager/languages/fr.json` (config)
- `plugins/OptionalManager/languages/hu.json` (config)
- `plugins/OptionalManager/languages/jp.json` (config)
- `plugins/OptionalManager/languages/pt-br.json` (config)
- `plugins/OptionalManager/languages/zh-tw.json` (config)
- `plugins/OptionalManager/languages/zh.json` (config)
- `plugins/PeerDb/plugin_info.json` (config)
- `plugins/Sidebar/languages/da.json` (config)
- `plugins/Sidebar/languages/de.json` (config)
- `plugins/Sidebar/languages/es.json` (config)
- `plugins/Sidebar/languages/fr.json` (config)
- `plugins/Sidebar/languages/hu.json` (config)
- `plugins/Sidebar/languages/it.json` (config)
- `plugins/Sidebar/languages/jp.json` (config)
- `plugins/Sidebar/languages/pl.json` (config)
- `plugins/Sidebar/languages/pt-br.json` (config)
- `plugins/Sidebar/languages/ru.json` (config)
- `plugins/Sidebar/languages/tr.json` (config)
- `plugins/Sidebar/languages/zh-tw.json` (config)
- `plugins/Sidebar/languages/zh.json` (config)
- `plugins/Sidebar/plugin_info.json` (config)
- `plugins/Stats/plugin_info.json` (config)
- `plugins/TranslateSite/plugin_info.json` (config)
- `plugins/Trayicon/languages/es.json` (config)
- `plugins/Trayicon/languages/fr.json` (config)
- `plugins/Trayicon/languages/hu.json` (config)
- `plugins/Trayicon/languages/it.json` (config)
- `plugins/Trayicon/languages/jp.json` (config)
- `plugins/Trayicon/languages/pl.json` (config)
- `plugins/Trayicon/languages/pt-br.json` (config)
- `plugins/Trayicon/languages/tr.json` (config)
- `plugins/Trayicon/languages/zh-tw.json` (config)
- `plugins/Trayicon/languages/zh.json` (config)
- `plugins/Trayicon/plugin_info.json` (config)
- `plugins/UiConfig/languages/hu.json` (config)
- `plugins/UiConfig/languages/jp.json` (config)
- `plugins/UiConfig/languages/pl.json` (config)
- `plugins/UiConfig/languages/pt-br.json` (config)
- `plugins/UiConfig/languages/zh.json` (config)
- `plugins/UiConfig/plugin_info.json` (config)
- `plugins/UiFileManager/languages/hu.json` (config)
- `plugins/UiFileManager/languages/jp.json` (config)
- `plugins/disabled-Bootstrapper/plugin_info.json` (config)
- `plugins/disabled-Multiuser/plugin_info.json` (config)
- `plugins/disabled-UiPassword/plugin_info.json` (config)
- `requirements.txt` (manifest)
- `src/Translate/languages/da.json` (config)
- `src/Translate/languages/de.json` (config)
- `src/Translate/languages/es.json` (config)
- `src/Translate/languages/fa.json` (config)
- `src/Translate/languages/fr.json` (config)
- `src/Translate/languages/hu.json` (config)
- `src/Translate/languages/it.json` (config)
- `src/Translate/languages/jp.json` (config)
- `src/Translate/languages/nl.json` (config)
- `src/Translate/languages/pl.json` (config)
- `src/Translate/languages/pt-br.json` (config)
- `src/Translate/languages/ru.json` (config)
- `src/Translate/languages/sk.json` (config)
- `src/Translate/languages/sl.json` (config)
- `src/Translate/languages/tr.json` (config)
- `src/Translate/languages/zh-tw.json` (config)
- `src/Translate/languages/zh.json` (config)

## Top-level layout

- `plugins` — 307 analysed file(s)
- `src` — 202 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `.github` — 4 analysed file(s)
- `tools` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `454c0b2e7e000fda7000cba49027541fbf327b96` is the revision these paths and observations refer to.
