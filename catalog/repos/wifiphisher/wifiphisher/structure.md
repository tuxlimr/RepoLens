# Project structure: wifiphisher/wifiphisher

**Analysed commit:** `4ae336518bf29eed13d3b09f2ee6a16e7973c997`

**Commit reference:** [4ae336518bf29eed13d3b09f2ee6a16e7973c997](https://github.com/wifiphisher/wifiphisher/commit/4ae336518bf29eed13d3b09f2ee6a16e7973c997)

**Tree at this commit:** [wifiphisher/wifiphisher@4ae336518bf2](https://github.com/wifiphisher/wifiphisher/tree/4ae336518bf29eed13d3b09f2ee6a16e7973c997)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | wifiphisher/wifiphisher |
| Description | The Rogue Access Point Framework |
| Stars | 14972 |
| Forks | 2746 |
| Licence | GPL-3.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `4ae336518bf29eed13d3b09f2ee6a16e7973c997` |
| Retrieved at | 2026-11-14T19:09:10.388940+00:00 |
| Files in this snapshot | 94 |

## Directory tree

```text
bin/  (1 files)
  wifiphisher
docs/  (7 files)
  Makefile
  conf.py
  custom_phishing_scenario.rst
  extensions.rst
  faq.rst
  index.rst
  opmodes.rst
tests/  (6 files)
  __init__.py
  test_deauth.py
  test_extensions.py
  test_interfaces.py
  test_lure10.py
  test_victims.py
wifiphisher/  (67 files)
  common/  (17 files)
    __init__.py
    accesspoint.py
    constants.py
    extensions.py
    firewall.py
    globals.py
    interfaces.py
    macmatcher.py
    opmode.py
    phishinghttp.py
    phishingpage.py
    recon.py
    sniffer.py
    tui.py
    uimethods.py
    utilities.py
    victim.py
  data/  (41 files)
    locs/  (1 files)
      … 1 files under this directory
    phishing-pages/  (38 files)
      … 38 files under this directory
    wifiphisher-known-open-wlans
    wifiphisher-os-initial-requests
  extensions/  (7 files)
    __init__.py
    deauth.py
    handshakeverify.py
    knownbeacons.py
    lure10.py
    roguehostapdinfo.py
    wpspbc.py
  __init__.py
  pywifiphisher.py
.editorconfig
.gitignore
.style.yapf
.travis.yml
CHANGELOG
CODE_OF_CONDUCT.md
FUNDING.yml
ISSUE_TEMPLATE.md
LICENSE.txt
MANIFEST.in
README.md
pylintrc
setup.py
```

## Entry points

- [wifiphisher/pywifiphisher.py](https://github.com/wifiphisher/wifiphisher/blob/4ae336518bf29eed13d3b09f2ee6a16e7973c997/wifiphisher/pywifiphisher.py)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: CleanCommand. Observed top-level functions: check_dnsmasq, check_required_library. |
| Data layer | data | Observed | Groups 7 file(s) under data layer (observed from repository paths and static analysis). |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 6 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH wifiphisher.extensions.deauth.ord, PATCH wifiphisher.extensions.deauth.ord, PATCH wifiphisher.extensions.deauth.o… |
| wifiphisher package | library | Observed | Groups 26 file(s) under wifiphisher package (observed from repository paths and static analysis). Observed top-level classes: AccessPoint, AccessPointFinder, ApDisplayInfo, BackendHandler, CaptivePortalHandler, Deauth.… |

## Important files

- `.editorconfig` (config)
- `.travis.yml` (ci)
- `FUNDING.yml` (config)
- `MANIFEST.in` (manifest)
- `setup.py` (manifest)
- `wifiphisher/data/phishing-pages/firmware-upgrade/config.ini` (config)
- `wifiphisher/data/phishing-pages/oauth-login/config.ini` (config)
- `wifiphisher/data/phishing-pages/plugin_update/config.ini` (config)
- `wifiphisher/data/phishing-pages/wifi_connect/config.ini` (config)

## Top-level layout

- `wifiphisher` — 67 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `docs` — 7 analysed file(s)
- `tests` — 6 analysed file(s)
- `bin` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 8 file(s) were skipped during inventory (7 x generated/minified file excluded; 1 x likely secret file excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `4ae336518bf29eed13d3b09f2ee6a16e7973c997` is the revision these paths and observations refer to.
