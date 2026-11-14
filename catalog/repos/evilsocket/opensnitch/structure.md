# Project structure: evilsocket/opensnitch

**Analysed commit:** `a1353848ba1b660320e90cefea782c3fba272c00`

**Commit reference:** [a1353848ba1b660320e90cefea782c3fba272c00](https://github.com/evilsocket/opensnitch/commit/a1353848ba1b660320e90cefea782c3fba272c00)

**Tree at this commit:** [evilsocket/opensnitch@a1353848ba1b](https://github.com/evilsocket/opensnitch/tree/a1353848ba1b660320e90cefea782c3fba272c00)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | evilsocket/opensnitch |
| Description | OpenSnitch is a GNU/Linux interactive application firewall inspired by Little Snitch. |
| Stars | 14298 |
| Forks | 688 |
| Licence | GPL-3.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `a1353848ba1b660320e90cefea782c3fba272c00` |
| Retrieved at | 2026-11-14T19:09:28.666900+00:00 |
| Files in this snapshot | 546 |

## Directory tree

```text
.github/  (7 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    config.yml
    feature-request.md
  workflows/  (3 files)
    build_ebpf_modules.yml
    generic_validations.yml
    go.yml
  FUNDING.yml
daemon/  (201 files)
  conman/  (2 files)
    connection.go
    connection_test.go
  core/  (5 files)
    core.go
    ebpf.go
    gzip.go
    system.go
    version.go
  data/  (9 files)
    init/  (3 files)
      … 3 files under this directory
    rules/  (2 files)
      … 2 files under this directory
    tasks/  (1 files)
      … 1 files under this directory
    default-config.json
    network_aliases.json
    system-fw.json
  dns/  (4 files)
    systemd/  (1 files)
      … 1 files under this directory
    ebpfhook.go
    parse.go
    track.go
  firewall/  (56 files)
    common/  (1 files)
      … 1 files under this directory
    config/  (2 files)
      … 2 files under this directory
    iptables/  (4 files)
      … 4 files under this directory
    nftables/  (48 files)
      … 48 files under this directory
    rules.go
  internal/  (1 files)
    testutil/  (1 files)
      … 1 files under this directory
  log/  (10 files)
    formats/  (5 files)
      … 5 files under this directory
    loggers/  (4 files)
      … 4 files under this directory
    log.go
  netfilter/  (5 files)
    netfilter_test.go
    packet.go
    queue.c
    queue.go
    queue.h
  netlink/  (7 files)
    procmon/  (1 files)
      … 1 files under this directory
    ifaces.go
    socket.go
    socket_linux.go
    socket_packet.go
    socket_test.go
    socket_xdp.go
  netstat/  (4 files)
    entry.go
    find.go
    parse.go
    parse_packet.go
  procmon/  (24 files)
    audit/  (3 files)
      … 3 files under this directory
    ebpf/  (9 files)
      … 9 files under this directory
    monitor/  (1 files)
      … 1 files under this directory
    activepids.go
    cache.go
    cache_events.go
    cache_events_test.go
    cache_test.go
    details.go
    find.go
    find_test.go
    parse.go
    process.go
    process_test.go
  rule/  (22 files)
    testdata/  (14 files)
      … 14 files under this directory
    loader.go
    loader_test.go
    operator.go
    operator_aliases.go
    operator_lists.go
    operator_test.go
    rule.go
    rule_test.go
  statistics/  (2 files)
    event.go
    stats.go
  tasks/  (32 files)
    base/  (1 files)
      … 1 files under this directory
    config/  (3 files)
      … 3 files under this directory
    downloader/  (5 files)
      … 5 files under this directory
    iocscanner/  (9 files)
      … 9 files under this directory
    looptask/  (1 files)
      … 1 files under this directory
    nodemonitor/  (2 files)
      … 2 files under this directory
    pidmonitor/  (2 files)
      … 2 files under this directory
    scheduler/  (2 files)
      … 2 files under this directory
    socketsmonitor/  (3 files)
      … 3 files under this directory
    doc.go
    load.go
    main.go
    main_test.go
  ui/  (12 files)
    auth/  (1 files)
      … 1 files under this directory
    config/  (1 files)
      … 1 files under this directory
    protocol/  (1 files)
      … 1 files under this directory
    testdata/  (3 files)
      … 3 files under this directory
    alerts.go
    client.go
    client_test.go
    config_utils.go
    notifications.go
    notifications_tasks.go
  .gitignore
  Gopkg.toml
  Makefile
  go.mod
  go.sum
  main.go
ebpf_prog/  (12 files)
  bpf_headers/  (4 files)
    bpf_core_read.h
    bpf_helper_defs.h
    bpf_helpers.h
    bpf_tracing.h
  Makefile
  README
  arm-clang-asm-fix.patch
  common.h
  common_defs.h
  opensnitch-dns.c
  opensnitch-procs.c
  opensnitch.c
proto/  (3 files)
  .gitignore
  Makefile
  ui.proto
ui/  (287 files)
  bin/  (1 files)
    opensnitch-ui
  i18n/  (21 files)
    locales/  (17 files)
      … 17 files under this directory
    Makefile
    README.md
    generate_i18n.sh
    opensnitch_i18n.pro
  opensnitch/  (248 files)
    actions/  (4 files)
      … 4 files under this directory
    auth/  (1 files)
      … 1 files under this directory
    customwidgets/  (10 files)
      … 10 files under this directory
    database/  (5 files)
      … 5 files under this directory
    dialogs/  (46 files)
      … 46 files under this directory
    firewall/  (7 files)
      … 7 files under this directory
    plugins/  (85 files)
      … 85 files under this directory
    proto/  (6 files)
      … 6 files under this directory
    res/  (59 files)
      … 59 files under this directory
    themes/  (2 files)
      … 2 files under this directory
    utils/  (15 files)
      … 15 files under this directory
    __init__.py
    config.py
    desktop_parser.py
    nodes.py
    notifications.py
    rules.py
    service.py
    version.py
  resources/  (4 files)
    icons/  (1 files)
      … 1 files under this directory
    io.github.evilsocket.opensnitch.appdata.xml
    kcm_opensnitch.desktop
    opensnitch_ui.desktop
  tests/  (7 files)
    dialogs/  (3 files)
      … 3 files under this directory
    README.md
    __init__.py
    conftest.py
    test_nodes.py
  .gitignore
  LICENSE
  MANIFEST.in
  Makefile
  requirements.txt
  setup.py
utils/  (31 files)
  legacy/  (1 files)
    make_ads_rules.py
  packaging/  (25 files)
    daemon/  (14 files)
      … 14 files under this directory
    ui/  (10 files)
      … 10 files under this directory
    build_modules.sh
  scripts/  (5 files)
    ads/  (1 files)
      … 1 files under this directory
    debug-ebpf-maps.sh
    ipasn_db_sync.sh
    ipasn_db_update.sh
    restart-opensnitch-onsleep.sh
.gitignore
LICENSE
Makefile
README.md
release.sh
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 27 file(s) under api layer (observed from repository paths and static analysis). Observed top-level classes: ActionFileController, AttachedRulesDialog, AttachedRulesIndex, BulkEditController, BulkEditDialog, Cont… |
| Configuration and deployment | config | Observed | Groups 43 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: Config, ConfigManager. Observed top-level functions: build_node_config, load, save,… |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| daemon package | library | Observed | Groups 153 file(s) under daemon package (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 10 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AlertFields, ConnFields, Database, GlobalDefaults, ListMetadata, MutableActionConfig. Observed top-lev… |
| ebpf_prog package | library | Observed | Groups 9 file(s) under ebpf_prog package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: ColorizedQSqlQueryModel, ConnectionsTableModel, ConnectionsTableView. |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 6 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: UIService. |
| Tests | test | Observed | Groups 8 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: ClientConfig, Connection, NotifTest, TestNodes, TestPreferences, TestRulesEditor. Observed top-level functio… |
| ui package | library | Observed | Groups 143 file(s) under ui package (observed from repository paths and static analysis). Observed top-level classes: Actions, AddressTableModel, AsnDB, AttachedRulesCountWorker, AttachedRulesFetchWorker, AttachedRulesP… |
| utils package | library | Observed | Groups 7 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/build_ebpf_modules.yml` (ci)
- `.github/workflows/generic_validations.yml` (ci)
- `.github/workflows/go.yml` (ci)
- `daemon/Gopkg.toml` (config)
- `daemon/data/default-config.json` (config)
- `daemon/data/network_aliases.json` (config)
- `daemon/data/rules/000-allow-localhost.json` (config)
- `daemon/data/rules/000-allow-localhost6.json` (config)
- `daemon/data/system-fw.json` (config)
- `daemon/data/tasks/tasks.json` (config)
- `daemon/firewall/nftables/testdata/test-sysfw-conf.json` (config)
- `daemon/go.mod` (manifest)
- `daemon/rule/testdata/000-allow-chrome.json` (config)
- `daemon/rule/testdata/001-deny-chrome.json` (config)
- `daemon/rule/testdata/invalid-regexp-list.json` (config)
- `daemon/rule/testdata/invalid-regexp.json` (config)
- `daemon/rule/testdata/live_reload/test-live-reload-delete.json` (config)
- `daemon/rule/testdata/live_reload/test-live-reload-remove.json` (config)
- `daemon/rule/testdata/rule-disabled-operator-list-expanded.json` (config)
- `daemon/rule/testdata/rule-disabled-operator-list.json` (config)
- `daemon/rule/testdata/rule-operator-list-data-empty.json` (config)
- `daemon/rule/testdata/rule-operator-list.json` (config)
- `daemon/ui/testdata/config-invalid-procmon.json` (config)
- `daemon/ui/testdata/default-config.json` (config)
- `ui/MANIFEST.in` (manifest)
- `ui/opensnitch/plugins/downloader/example/downloaders.json` (config)
- `ui/opensnitch/plugins/highlight/example/commonActionsDelegate.json` (config)
- `ui/opensnitch/plugins/highlight/example/rulesActionsDelegate.json` (config)
- `ui/opensnitch/plugins/list_subscriptions/example/hagezi-light.txt.meta.json` (config)
- `ui/opensnitch/plugins/list_subscriptions/example/list_subscriptions.json` (config)
- `ui/opensnitch/plugins/versionchecker/versionchecker.json` (config)
- `ui/opensnitch/plugins/virustotal/example/virustotal.json` (config)
- `ui/opensnitch/utils/network_aliases/network_aliases.json` (config)
- `ui/requirements.txt` (manifest)
- `ui/setup.py` (manifest)
- `utils/packaging/daemon/deb/debian/gitlab-ci.yml` (config)

## Top-level layout

- `ui` — 287 analysed file(s)
- `daemon` — 201 analysed file(s)
- `utils` — 31 analysed file(s)
- `ebpf_prog` — 12 analysed file(s)
- `.github` — 7 analysed file(s)
- `(root files)` — 5 analysed file(s)
- `proto` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- File utils/legacy/make_ads_rules.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `a1353848ba1b660320e90cefea782c3fba272c00` is the revision these paths and observations refer to.
