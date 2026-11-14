# Project structure: fail2ban/fail2ban

**Analysed commit:** `66de71930412d3c2780d8c7f1dead70824344784`

**Commit reference:** [66de71930412d3c2780d8c7f1dead70824344784](https://github.com/fail2ban/fail2ban/commit/66de71930412d3c2780d8c7f1dead70824344784)

**Tree at this commit:** [fail2ban/fail2ban@66de71930412](https://github.com/fail2ban/fail2ban/tree/66de71930412d3c2780d8c7f1dead70824344784)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | fail2ban/fail2ban |
| Description | Daemon to ban hosts that cause multiple authentication errors |
| Stars | 19007 |
| Forks | 1516 |
| Licence | Other |
| Language | Python |
| Default branch | master |
| Analysed commit | `66de71930412d3c2780d8c7f1dead70824344784` |
| Retrieved at | 2026-11-14T19:08:20.076657+00:00 |
| Files in this snapshot | 526 |

## Directory tree

```text
.github/  (8 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    feature_request.md
    filter_request.md
  workflows/  (3 files)
    codespell.yml
    main.yml
    publish.yml
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
bin/  (4 files)
  fail2ban-client
  fail2ban-regex
  fail2ban-server
  fail2ban-testcases
config/  (180 files)
  action.d/  (66 files)
    abuseipdb.conf
    apf.conf
    apprise.conf
    blocklist_de.conf
    bsd-ipfw.conf
    cloudflare-token.conf
    cloudflare.conf
    complain.conf
    csf.conf
    dshield.conf
    dummy.conf
    firewallcmd-allports.conf
    firewallcmd-common.conf
    firewallcmd-ipset.conf
    firewallcmd-multiport.conf
    firewallcmd-new.conf
    firewallcmd-rich-logging.conf
    firewallcmd-rich-rules.conf
    helpers-common.conf
    hostsdeny.conf
    ipfilter.conf
    ipfw.conf
    iptables-allports.conf
    iptables-ipset-proto4.conf
    … 42 more files
  filter.d/  (105 files)
    ignorecommands/  (1 files)
      … 1 files under this directory
    3proxy.conf
    apache-auth.conf
    apache-badbots.conf
    apache-botsearch.conf
    apache-common.conf
    apache-fakegooglebot.conf
    apache-modsecurity.conf
    apache-nohome.conf
    apache-noscript.conf
    apache-overflows.conf
    apache-pass.conf
    apache-shellshock.conf
    assp.conf
    asterisk.conf
    authelia.conf
    bitwarden.conf
    botsearch-common.conf
    centreon.conf
    common.conf
    counter-strike.conf
    courier-auth.conf
    courier-smtp.conf
    cowrie.conf
    cyrus-imap.conf
    … 80 more files
  fail2ban.conf
  jail.conf
  paths-arch.conf
  paths-common.conf
  paths-debian.conf
  paths-fedora.conf
  paths-freebsd.conf
  paths-opensuse.conf
  paths-osx.conf
doc/  (48 files)
  Doxyfile
  Makefile
  conf.py
  develop.rst
  fail2ban.client.actionreader.rst
  fail2ban.client.beautifier.rst
  fail2ban.client.configparserinc.rst
  fail2ban.client.configreader.rst
  fail2ban.client.configurator.rst
  fail2ban.client.csocket.rst
  fail2ban.client.fail2banreader.rst
  fail2ban.client.filterreader.rst
  fail2ban.client.jailreader.rst
  fail2ban.client.jailsreader.rst
  fail2ban.client.rst
  fail2ban.exceptions.rst
  fail2ban.helpers.rst
  fail2ban.protocol.rst
  fail2ban.rst
  fail2ban.server.action.rst
  fail2ban.server.actions.rst
  fail2ban.server.asyncserver.rst
  fail2ban.server.banmanager.rst
  fail2ban.server.database.rst
  … 24 more files
fail2ban/  (224 files)
  client/  (15 files)
    __init__.py
    actionreader.py
    beautifier.py
    configparserinc.py
    configreader.py
    configurator.py
    csocket.py
    fail2banclient.py
    fail2bancmdline.py
    fail2banreader.py
    fail2banregex.py
    fail2banserver.py
    filterreader.py
    jailreader.py
    jailsreader.py
  compat/  (2 files)
    asynchat.py
    asyncore.py
  server/  (25 files)
    __init__.py
    action.py
    actions.py
    asyncserver.py
    banmanager.py
    database.py
    datedetector.py
    datetemplate.py
    failmanager.py
    failregex.py
    filter.py
    filterpoll.py
    filterpyinotify.py
    filtersystemd.py
    ipdns.py
    jail.py
    jails.py
    jailthread.py
    mytime.py
    observer.py
    server.py
    strptime.py
    ticket.py
    transmitter.py
    … 1 more files
  tests/  (176 files)
    action_d/  (2 files)
      … 2 files under this directory
    config/  (11 files)
      … 11 files under this directory
    files/  (143 files)
      … 143 files under this directory
    __init__.py
    actionstestcase.py
    actiontestcase.py
    banmanagertestcase.py
    clientbeautifiertestcase.py
    clientreadertestcase.py
    databasetestcase.py
    datedetectortestcase.py
    dummyjail.py
    fail2banclienttestcase.py
    fail2banregextestcase.py
    failmanagertestcase.py
    filtertestcase.py
    misctestcase.py
    observertestcase.py
    samplestestcase.py
    servertestcase.py
    sockettestcase.py
    tickettestcase.py
    utils.py
  __init__.py
  exceptions.py
  helpers.py
  protocol.py
  setup.py
  version.py
files/  (24 files)
  cacti/  (3 files)
    README
    cacti_host_template_fail2ban.xml
    fail2ban_stats.sh
  logwatch/  (3 files)
    fail2ban
    fail2ban-0.8.log
    fail2ban-0.9.log
  monit/  (1 files)
    fail2ban
  nagios/  (2 files)
    README
    check_fail2ban
  bash-completion
  debian-initd
  fail2ban-logrotate
  fail2ban-openrc.conf
  fail2ban-openrc.init.in
  fail2ban.service.in
  fail2ban.socket.in
  fail2ban.upstart
  gen_badbots
  ipmasq-ZZZzzz_fail2ban.rul
  macosx-initd
  redhat-initd
  solaris-fail2ban.xml
  solaris-svc-fail2ban
  suse-initd
man/  (13 files)
  fail2ban-client.1
  fail2ban-client.h2m
  fail2ban-python.1
  fail2ban-python.h2m
  fail2ban-regex.1
  fail2ban-regex.h2m
  fail2ban-server.1
  fail2ban-server.h2m
  fail2ban-testcases.1
  fail2ban-testcases.h2m
  fail2ban.1
  generate-man
  jail.conf.5
.codespellrc
.coveragerc
.gitattributes
.gitignore
.mailmap
.pylintrc
.typos.toml
CONTRIBUTING.md
COPYING
ChangeLog
DEVELOP
FILTERS
MANIFEST
MANIFEST.in
README.Solaris
README.md
RELEASE
THANKS
TODO
Vagrantfile
fail2ban-testcases-all
fail2ban-testcases-all-python3
kill-server
setup.cfg
… 1 more files
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: SMTPAction, install_command_f2b, install_scripts_f2b. Observed top-level functions: u… |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: Fail2BanDb. Observed top-level functions: _json_default, _json_dumps_safe, _json_loads_safe, commitandr… |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Server, ServerInitializationError. Observed top-level functions: _make_file_path, _thread_… |
| External integrations | external | Observed | Groups 15 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: ActionReader, BasicInterpolationWithName, Beautifier, CSocket, ConfigReader, ConfigReaderUn… |
| fail2ban package | library | Observed | Groups 30 file(s) under fail2ban package (observed from repository paths and static analysis). Observed top-level classes: ActionBase, Actions, AsyncServer, AsyncServerException, BanManager, BanTicket. Observed top-leve… |
| files package | library | Observed | Groups 1 file(s) under files package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 176 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: AddFailure, BanTimeIncr, BanTimeIncrDB, BasicFilter, BeautifierTest, ClientMisc. Observed top-level functi… |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/workflows/codespell.yml` (ci)
- `.github/workflows/main.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.typos.toml` (config)
- `MANIFEST.in` (manifest)
- `doc/requirements.txt` (manifest)
- `fail2ban/setup.py` (manifest)
- `setup.cfg` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `fail2ban` — 224 analysed file(s)
- `config` — 180 analysed file(s)
- `doc` — 48 analysed file(s)
- `(root files)` — 25 analysed file(s)
- `files` — 24 analysed file(s)
- `man` — 13 analysed file(s)
- `.github` — 8 analysed file(s)
- `bin` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `66de71930412d3c2780d8c7f1dead70824344784` is the revision these paths and observations refer to.
