# Project structure: smicallef/spiderfoot

**Analysed commit:** `0f815a203afebf05c98b605dba5cf0475a0ee5fd`

**Commit reference:** [0f815a203afebf05c98b605dba5cf0475a0ee5fd](https://github.com/smicallef/spiderfoot/commit/0f815a203afebf05c98b605dba5cf0475a0ee5fd)

**Tree at this commit:** [smicallef/spiderfoot@0f815a203afe](https://github.com/smicallef/spiderfoot/tree/0f815a203afebf05c98b605dba5cf0475a0ee5fd)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | smicallef/spiderfoot |
| Description | SpiderFoot automates OSINT for threat intelligence and mapping your attack surface. |
| Stars | 24589 |
| Forks | 4084 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `0f815a203afebf05c98b605dba5cf0475a0ee5fd` |
| Retrieved at | 2026-11-14T19:07:36.392057+00:00 |
| Files in this snapshot | 791 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (2 files)
    codeql-analysis.yml
    tests.yaml
  ISSUE_TEMPLATE.md
correlations/  (39 files)
  README.md
  cert_expired.yaml
  cloud_bucket_open.yaml
  cloud_bucket_open_related.yaml
  data_from_base64.yaml
  data_from_docmeta.yaml
  database_exposed.yaml
  dev_or_test_system.yaml
  dns_zone_transfer_possible.yaml
  egress_ip_from_wikipedia.yaml
  email_in_multiple_breaches.yaml
  email_in_whois.yaml
  email_only_from_pasteleak_site.yaml
  host_only_from_bruteforce.yaml
  host_only_from_certificatetransparency.yaml
  http_errors.yaml
  human_name_in_whois.yaml
  internal_host.yaml
  multiple_malicious.yaml
  multiple_malicious_affiliate.yaml
  multiple_malicious_cohost.yaml
  name_only_from_pasteleak_site.yaml
  open_port_version.yaml
  outlier_cloud.yaml
  … 15 more files
docs/  (5 files)
  Makefile
  conf.py
  index.rst
  make.bat
  spiderfoot.rst
modules/  (234 files)
  __init__.py
  sfp__stor_db.py
  sfp__stor_stdout.py
  sfp_abstractapi.py
  sfp_abusech.py
  sfp_abuseipdb.py
  sfp_abusix.py
  sfp_accounts.py
  sfp_adblock.py
  sfp_adguard_dns.py
  sfp_ahmia.py
  sfp_alienvault.py
  sfp_alienvaultiprep.py
  sfp_apple_itunes.py
  sfp_archiveorg.py
  sfp_arin.py
  sfp_azureblobstorage.py
  sfp_base64.py
  sfp_bgpview.py
  sfp_binaryedge.py
  sfp_bingsearch.py
  sfp_bingsharedip.py
  sfp_binstring.py
  sfp_bitcoin.py
  … 210 more files
spiderfoot/  (32 files)
  dicts/  (7 files)
    ispell/  (3 files)
      … 3 files under this directory
    __init__.py
    generic-usernames.txt
    subdomains-10000.txt
    subdomains.txt
  static/  (8 files)
    css/  (2 files)
      … 2 files under this directory
    js/  (5 files)
      … 5 files under this directory
    package.json
  templates/  (7 files)
    FOOTER.tmpl
    HEADER.tmpl
    error.tmpl
    newscan.tmpl
    opts.tmpl
    scaninfo.tmpl
    scanlist.tmpl
  __init__.py
  __version__.py
  correlation.py
  db.py
  event.py
  helpers.py
  logger.py
  plugin.py
  target.py
  threadpool.py
test/  (458 files)
  acceptance/  (3 files)
    requirements.txt
    run
    scan.robot
  integration/  (203 files)
    modules/  (199 files)
      … 199 files under this directory
    __init__.py
    test_sf.py
    test_sfcli.py
    test_sfwebui.py
  unit/  (245 files)
    modules/  (232 files)
      … 232 files under this directory
    spiderfoot/  (7 files)
      … 7 files under this directory
    __init__.py
    test_modules.py
    test_spiderfoot.py
    test_spiderfootcli.py
    test_spiderfootscanner.py
    test_spiderfootwebui.py
  README.md
  __init__.py
  bandit
  conftest.py
  requirements.txt
  run
  update-requirements
.dockerignore
.gitignore
.pylintrc
Dockerfile
Dockerfile.full
LICENSE
README.md
THANKYOU
VERSION
docker-compose-dev.yml
docker-compose-full.yml
docker-compose.yml
generate-certificate
requirements.txt
setup.cfg
sf.py
sfcli.py
sflib.py
sfscan.py
sfwebui.py
```

## Entry points

- [sf.py:607](https://github.com/smicallef/spiderfoot/blob/0f815a203afebf05c98b605dba5cf0475a0ee5fd/sf.py#L607)
- [sfcli.py:1350](https://github.com/smicallef/spiderfoot/blob/0f815a203afebf05c98b605dba5cf0475a0ee5fd/sfcli.py#L1350)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 46 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). Observed top-level classes: SpiderFoot, SpiderFootScanner, SpiderFootWebUi. Observed top-level functions: startSpiderFootScanner. |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: SpiderFootDb. |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: SpiderFootCli, bcolors. Observed top-level functions: handle_abort, main, start_scan, star… |
| External integrations | external | Observed | Groups 1 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: sfp_crobat_api. |
| modules package | library | Observed | Groups 233 file(s) under modules package (observed from repository paths and static analysis). Observed top-level classes: sfp__stor_db, sfp__stor_stdout, sfp_abstractapi, sfp_abusech, sfp_abuseipdb, sfp_abusix. |
| spiderfoot package | library | Observed | Groups 16 file(s) under spiderfoot package (observed from repository paths and static analysis). Observed top-level classes: SpiderFootCorrelator, SpiderFootEvent, SpiderFootHelpers, SpiderFootPlugin, SpiderFootPluginLo… |
| Tests | test | Observed | Groups 458 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: TestModulViewdns, TestModuleAbstractapi, TestModuleAbusech, TestModuleAbuseipdb, TestModuleAbusix, TestMod… |

## Important files

- `.dockerignore` (container)
- `.github/workflows/codeql-analysis.yml` (ci)
- `.github/workflows/tests.yaml` (ci)
- `Dockerfile` (container)
- `Dockerfile.full` (container)
- `correlations/cert_expired.yaml` (config)
- `correlations/cloud_bucket_open.yaml` (config)
- `correlations/cloud_bucket_open_related.yaml` (config)
- `correlations/data_from_base64.yaml` (config)
- `correlations/data_from_docmeta.yaml` (config)
- `correlations/database_exposed.yaml` (config)
- `correlations/dev_or_test_system.yaml` (config)
- `correlations/dns_zone_transfer_possible.yaml` (config)
- `correlations/egress_ip_from_wikipedia.yaml` (config)
- `correlations/email_in_multiple_breaches.yaml` (config)
- `correlations/email_in_whois.yaml` (config)
- `correlations/email_only_from_pasteleak_site.yaml` (config)
- `correlations/host_only_from_bruteforce.yaml` (config)
- `correlations/host_only_from_certificatetransparency.yaml` (config)
- `correlations/http_errors.yaml` (config)
- `correlations/human_name_in_whois.yaml` (config)
- `correlations/internal_host.yaml` (config)
- `correlations/multiple_malicious.yaml` (config)
- `correlations/multiple_malicious_affiliate.yaml` (config)
- `correlations/multiple_malicious_cohost.yaml` (config)
- `correlations/name_only_from_pasteleak_site.yaml` (config)
- `correlations/open_port_version.yaml` (config)
- `correlations/outlier_cloud.yaml` (config)
- `correlations/outlier_country.yaml` (config)
- `correlations/outlier_email.yaml` (config)
- `correlations/outlier_hostname.yaml` (config)
- `correlations/outlier_ipaddress.yaml` (config)
- `correlations/outlier_registrar.yaml` (config)
- `correlations/outlier_webserver.yaml` (config)
- `correlations/remote_desktop_exposed.yaml` (config)
- `correlations/root_path_needs_auth.yaml` (config)
- `correlations/stale_host.yaml` (config)
- `correlations/strong_affiliate_certs.yaml` (config)
- `correlations/strong_similardomain_crossref.yaml` (config)
- `correlations/template.yaml` (config)
- `correlations/vulnerability_critical.yaml` (config)
- `correlations/vulnerability_high.yaml` (config)
- `correlations/vulnerability_mediumlow.yaml` (config)
- `docker-compose-dev.yml` (config)
- `docker-compose-full.yml` (config)
- `docker-compose.yml` (container)
- `requirements.txt` (manifest)
- `setup.cfg` (manifest)
- `spiderfoot/static/package.json` (manifest)

## Top-level layout

- `test` — 458 analysed file(s)
- `modules` — 234 analysed file(s)
- `correlations` — 39 analysed file(s)
- `spiderfoot` — 32 analysed file(s)
- `(root files)` — 20 analysed file(s)
- `docs` — 5 analysed file(s)
- `.github` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 4 file(s) were skipped during inventory (4 x vendored/generated directory excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `0f815a203afebf05c98b605dba5cf0475a0ee5fd` is the revision these paths and observations refer to.
