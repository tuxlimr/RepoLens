# Project structure: threat9/routersploit

**Analysed commit:** `723b574c36ae202857e3f93e4f3c2ab9a1638ed4`

**Commit reference:** [723b574c36ae202857e3f93e4f3c2ab9a1638ed4](https://github.com/threat9/routersploit/commit/723b574c36ae202857e3f93e4f3c2ab9a1638ed4)

**Tree at this commit:** [threat9/routersploit@723b574c36ae](https://github.com/threat9/routersploit/tree/723b574c36ae202857e3f93e4f3c2ab9a1638ed4)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | threat9/routersploit |
| Description | Exploitation Framework for Embedded Devices |
| Stars | 13304 |
| Forks | 2401 |
| Licence | Other |
| Language | Python |
| Default branch | master |
| Analysed commit | `723b574c36ae202857e3f93e4f3c2ab9a1638ed4` |
| Retrieved at | 2026-11-14T19:09:52.928978+00:00 |
| Files in this snapshot | 791 |

## Directory tree

```text
.github/  (2 files)
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
.travis/  (2 files)
  install.sh
  run.sh
docs/  (206 files)
  modules/  (206 files)
    creds/  (150 files)
      … 150 files under this directory
    encoders/  (6 files)
      … 6 files under this directory
    exploits/  (17 files)
      … 17 files under this directory
    generic/  (1 files)
      … 1 files under this directory
    payloads/  (32 files)
      … 32 files under this directory
routersploit/  (540 files)
  core/  (29 files)
    bluetooth/  (5 files)
      … 5 files under this directory
    exploit/  (9 files)
      … 9 files under this directory
    ftp/  (2 files)
      … 2 files under this directory
    http/  (2 files)
      … 2 files under this directory
    snmp/  (2 files)
      … 2 files under this directory
    ssh/  (2 files)
      … 2 files under this directory
    tcp/  (2 files)
      … 2 files under this directory
    telnet/  (2 files)
      … 2 files under this directory
    udp/  (2 files)
      … 2 files under this directory
    __init__.py
  libs/  (5 files)
    apiros/  (2 files)
      … 2 files under this directory
    lzs/  (2 files)
      … 2 files under this directory
    __init__.py
  modules/  (489 files)
    creds/  (228 files)
      … 228 files under this directory
    encoders/  (9 files)
      … 9 files under this directory
    exploits/  (194 files)
      … 194 files under this directory
    generic/  (7 files)
      … 7 files under this directory
    payloads/  (42 files)
      … 42 files under this directory
    scanners/  (8 files)
      … 8 files under this directory
    __init__.py
  resources/  (15 files)
    ssh_keys/  (9 files)
      … 9 files under this directory
    wordlists/  (5 files)
      … 5 files under this directory
    __init__.py
  __init__.py
  interpreter.py
tests/  (27 files)
  core/  (2 files)
    __init__.py
    test_option.py
  creds/  (23 files)
    cameras/  (22 files)
      … 22 files under this directory
    __init__.py
  __init__.py
  conftest.py
.dockerignore
.gitignore
.travis.yml
CONTRIBUTING.md
Dockerfile
LICENSE
MANIFEST.in
Makefile
README.md
docker-compose.yaml
requirements-dev.txt
requirements.txt
rsf.py
setup.py
```

## Entry points

- [rsf.py:26](https://github.com/threat9/routersploit/blob/723b574c36ae202857e3f93e4f3c2ab9a1638ed4/rsf.py#L26)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 256 file(s) under api layer (observed from repository paths and static analysis). Observed top-level classes: Exploit, ExploitError. |
| Configuration and deployment | config | Observed | Groups 15 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: routersploit. |
| External integrations | external | Observed | Groups 9 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: ApiRosClient, BTLEClient, CreateSocketError, FTPCli, FTPClient, HTTPClient. |
| routersploit package | library | Observed | Groups 241 file(s) under routersploit package (observed from repository paths and static analysis). Observed top-level classes: BaseInterpreter, BitReader, Encoder, Exploit, Payload, RingList. Observed top-level functio… |
| Service / domain layer | service | Observed | Groups 21 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: ArchitectureSpecificPayload, BTLEScanner, BaseEncoder, BaseExploit, BasePayload, BindTCPPa… |
| Tests | test | Observed | Groups 27 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: apply_response, empty_target, error_target, generic_target, not_found_target, redirect_target. |

## Important files

- `.dockerignore` (container)
- `.travis.yml` (ci)
- `Dockerfile` (container)
- `MANIFEST.in` (manifest)
- `docker-compose.yaml` (container)
- `requirements-dev.txt` (manifest)
- `requirements.txt` (manifest)
- `routersploit/resources/ssh_keys/array-networks-vapv-vxag.json` (config)
- `routersploit/resources/ssh_keys/barracuda_load_balancer_vm.json` (config)
- `routersploit/resources/ssh_keys/ceragon-fibeair-cve-2015-0936.json` (config)
- `routersploit/resources/ssh_keys/exagrid-cve-2016-1561.json` (config)
- `routersploit/resources/ssh_keys/f5-bigip-cve-2012-1493.json` (config)
- `routersploit/resources/ssh_keys/loadbalancer.org-enterprise-va.json` (config)
- `routersploit/resources/ssh_keys/monroe-dasdec-cve-2013-0137.json` (config)
- `routersploit/resources/ssh_keys/quantum-dxi-v1000.json` (config)
- `routersploit/resources/ssh_keys/vagrant.json` (config)
- `setup.py` (manifest)

## Top-level layout

- `routersploit` — 540 analysed file(s)
- `docs` — 206 analysed file(s)
- `tests` — 27 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `.github` — 2 analysed file(s)
- `.travis` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 9 file(s) were skipped during inventory (9 x likely secret file excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `723b574c36ae202857e3f93e4f3c2ab9a1638ed4` is the revision these paths and observations refer to.
