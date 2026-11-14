# Project structure: sshuttle/sshuttle

**Analysed commit:** `a12eaa854353dcfa03eff1f09781bc0d0dc55b74`

**Commit reference:** [a12eaa854353dcfa03eff1f09781bc0d0dc55b74](https://github.com/sshuttle/sshuttle/commit/a12eaa854353dcfa03eff1f09781bc0d0dc55b74)

**Tree at this commit:** [sshuttle/sshuttle@a12eaa854353](https://github.com/sshuttle/sshuttle/tree/a12eaa854353dcfa03eff1f09781bc0d0dc55b74)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | sshuttle/sshuttle |
| Description | Transparent proxy server that works as a poor man's VPN.  Forwards over ssh.  Doesn't require admin.  Works with Linux and MacOS.  Supports DNS tunneling. |
| Stars | 13665 |
| Forks | 805 |
| Licence | LGPL-2.1 |
| Language | Python |
| Default branch | master |
| Analysed commit | `a12eaa854353dcfa03eff1f09781bc0d0dc55b74` |
| Retrieved at | 2026-11-14T19:09:44.654008+00:00 |
| Files in this snapshot | 92 |

## Directory tree

```text
.github/  (6 files)
  workflows/  (5 files)
    codeql.yml
    conventional-commits.yml
    osv-scanner.yml
    pythonpackage.yml
    release-please.yml
  dependabot.yml
docs/  (18 files)
  Makefile
  changes.rst
  chromeos.rst
  conf.py
  how-it-works.rst
  index.rst
  installation.rst
  make.bat
  manpage.rst
  openwrt.rst
  overview.rst
  platform.rst
  requirements.rst
  support.rst
  tproxy.rst
  trivia.rst
  usage.rst
  windows.rst
scripts/  (9 files)
  Containerfile
  README.md
  compose.yml
  container.setup.sh
  exec-sshuttle
  exec-tool
  run-benchmark
  run-checks
  test-bed
sshuttle/  (24 files)
  methods/  (7 files)
    __init__.py
    ipfw.py
    nat.py
    nft.py
    pf.py
    tproxy.py
    windivert.py
  __init__.py
  __main__.py
  assembler.py
  client.py
  cmdline.py
  firewall.py
  helpers.py
  hostwatch.py
  linux.py
  namespace.py
  options.py
  sdnotify.py
  server.py
  ssh.py
  ssnet.py
  ssyslog.py
  sudoers.py
tests/  (17 files)
  client/  (15 files)
    test_auto_nets.py
    test_firewall.py
    test_group.py
    test_helpers.py
    test_listeners.py
    test_methods_nat.py
    test_methods_nft.py
    test_methods_pf.py
    test_methods_tproxy.py
    test_no_flush_dns.py
    test_options.py
    test_sdnotify.py
    test_ssnet.py
    test_sudoers.py
    test_tmark.py
  server/  (1 files)
    test_server.py
  ssh/  (1 files)
    test_parse_hostport.py
.envrc
.gitignore
.prospector.yml
.readthedocs.yaml
.tool-versions
CHANGELOG.md
CHANGES.rst
LICENSE
MANIFEST.in
README.rst
bandit.yml
flake.lock
flake.nix
pyproject.toml
run
setup.cfg
tox.ini
windows_check.ps1
```

## Entry points

- [sshuttle/cmdline.py](https://github.com/sshuttle/sshuttle/blob/a12eaa854353dcfa03eff1f09781bc0d0dc55b74/sshuttle/cmdline.py)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: DnsProxy, Hostwatch, UdpProxy. Observed top-level functions: _exc_dump, _ipmatch, _ipstr,… |
| External integrations | external | Observed | Groups 1 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: FirewallClient, MultiListener. Observed top-level functions: _main, check_daemon, daemon_cle… |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| sshuttle package | library | Observed | Groups 21 file(s) under sshuttle package (observed from repository paths and static analysis). Observed top-level classes: BaseMethod, Concat, ConnState, ConnTrack, Darwin, Fatal. Observed top-level functions: _add, _ch… |
| Tests | test | Observed | Groups 17 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH os.link, PATCH os.rename, PATCH sshuttle.firewall.rewrite_etc_hosts, PATCH sshuttle.firewall.setup_daemon, PATCH… |

## Important files

- `.github/dependabot.yml` (config)
- `.github/workflows/codeql.yml` (ci)
- `.github/workflows/conventional-commits.yml` (ci)
- `.github/workflows/osv-scanner.yml` (ci)
- `.github/workflows/pythonpackage.yml` (ci)
- `.github/workflows/release-please.yml` (ci)
- `.prospector.yml` (config)
- `.readthedocs.yaml` (config)
- `MANIFEST.in` (manifest)
- `bandit.yml` (config)
- `pyproject.toml` (manifest)
- `scripts/compose.yml` (container)
- `setup.cfg` (manifest)
- `tox.ini` (config)

## Top-level layout

- `sshuttle` — 24 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `docs` — 18 analysed file(s)
- `tests` — 17 analysed file(s)
- `scripts` — 9 analysed file(s)
- `.github` — 6 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `a12eaa854353dcfa03eff1f09781bc0d0dc55b74` is the revision these paths and observations refer to.
