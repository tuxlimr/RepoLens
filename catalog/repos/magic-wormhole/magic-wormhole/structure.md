# Project structure: magic-wormhole/magic-wormhole

**Analysed commit:** `657bd5d51c67db2109219ff57b7d997afa57261f`

**Commit reference:** [657bd5d51c67db2109219ff57b7d997afa57261f](https://github.com/magic-wormhole/magic-wormhole/commit/657bd5d51c67db2109219ff57b7d997afa57261f)

**Tree at this commit:** [magic-wormhole/magic-wormhole@657bd5d51c67](https://github.com/magic-wormhole/magic-wormhole/tree/657bd5d51c67db2109219ff57b7d997afa57261f)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | magic-wormhole/magic-wormhole |
| Description | get things from one computer to another, safely |
| Stars | 23098 |
| Forks | 769 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `657bd5d51c67db2109219ff57b7d997afa57261f` |
| Retrieved at | 2026-11-14T19:07:50.858231+00:00 |
| Files in this snapshot | 231 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (3 files)
    codespell.yml
    documentation-links.yml
    test.yml
docs/  (46 files)
  releases/  (6 files)
    release-announce-0.14.0.asc
    release-announce-0.15.0.asc
    release-announce-0.19.0.asc
    release-announce-0.19.1.asc
    release-announce-0.19.2.asc
    release-announce-0.24.0.asc
  state-machines/  (16 files)
    Makefile
    _connection.dot
    allocator.dot
    boss.dot
    code.dot
    dilation.dot
    input.dot
    key.dot
    lister.dot
    machines.dot
    mailbox.dot
    nameplate.dot
    order.dot
    receive.dot
    send.dot
    terminator.dot
  CONTRIBUTING.rst
  Makefile
  api-example.py
  api.rst
  attacks.rst
  client-protocol.rst
  conf.py
  dilation-protocol.rst
  ecosystem.rst
  file-transfer-protocol.rst
  how-to-release.rst
  index.rst
  introduction.rst
  journal.rst
  new-protocol.svg
  requirements.txt
  server-protocol.rst
  server.seqdiag
  tor.rst
  transit.rst
  using-the-cli.rst
  w.dot
  welcome.rst
  wormhole.1
misc/  (7 files)
  web/  (3 files)
    timeline.css
    timeline.html
    timeline.js
  demo-journal.py
  dump-stats.py
  dump-timing.py
  windows-build.cmd
pyi/  (2 files)
  build-exe
  wormhole.exe.spec
signatures/  (61 files)
  README
  magic-wormhole-0.10.0.tar.gz.asc
  magic-wormhole-0.10.1.tar.gz.asc
  magic-wormhole-0.10.2.tar.gz.asc
  magic-wormhole-0.10.3.tar.gz.asc
  magic-wormhole-0.10.4.tar.gz.asc
  magic-wormhole-0.10.5.tar.gz.asc
  magic-wormhole-0.11.0.tar.gz.asc
  magic-wormhole-0.11.1.tar.gz.asc
  magic-wormhole-0.11.2.tar.gz.asc
  magic-wormhole-0.12.0.tar.gz.asc
  magic-wormhole-0.13.0.tar.gz.asc
  magic-wormhole-0.15.0.tar.gz.asc
  magic-wormhole-0.16.0.tar.gz.asc
  magic-wormhole-0.7.0.tar.gz.asc
  magic-wormhole-0.7.5.tar.gz.asc
  magic-wormhole-0.8.0.tar.gz.asc
  magic-wormhole-0.8.1.tar.gz.asc
  magic-wormhole-0.8.2.tar.gz.asc
  magic-wormhole-0.9.0.tar.gz.asc
  magic-wormhole-0.9.1.tar.gz.asc
  magic-wormhole-0.9.2.tar.gz.asc
  magic_wormhole-0.10.0-py2.py3-none-any.whl.asc
  magic_wormhole-0.10.1-py2.py3-none-any.whl.asc
  … 37 more files
src/  (90 files)
  wormhole/  (90 files)
    _dilation/  (10 files)
      … 10 files under this directory
    cli/  (7 files)
      … 7 files under this directory
    test/  (41 files)
      … 41 files under this directory
    __init__.py
    __main__.py
    _allocator.py
    _boss.py
    _code.py
    _hints.py
    _input.py
    _interfaces.py
    _key.py
    _lister.py
    _mailbox.py
    _nameplate.py
    _order.py
    _receive.py
    _rendezvous.py
    _rlcompleter.py
    _send.py
    _status.py
    _terminator.py
    _version.py
    _wordlist.py
    errors.py
    eventual.py
    ipaddrs.py
    … 8 more files
.appveyor.yml
.coveragerc
.gitattributes
.gitignore
.readthedocs.yaml
LICENSE
MANIFEST.in
Makefile
NEWS.md
README.md
bash-completions-version-4.patch
newest-version.py
pyproject.toml
setup.cfg
setup.py
snapcraft.yaml
tox.ini
update-version.py
versioneer.py
wormhole_complete.bash
wormhole_complete.fish
wormhole_complete.zsh
```

## Entry points

- [src/wormhole/__main__.py:1](https://github.com/magic-wormhole/magic-wormhole/blob/657bd5d51c67db2109219ff57b7d997afa57261f/src/wormhole/__main__.py#L1)
- [src/wormhole/cli/cli.py](https://github.com/magic-wormhole/magic-wormhole/blob/657bd5d51c67db2109219ff57b7d997afa57261f/src/wormhole/cli/cli.py)
- [src/wormhole/cli/cli.py](https://github.com/magic-wormhole/magic-wormhole/blob/657bd5d51c67db2109219ff57b7d997afa57261f/src/wormhole/cli/cli.py)
- [misc/demo-journal.py:275](https://github.com/magic-wormhole/magic-wormhole/blob/657bd5d51c67db2109219ff57b7d997afa57261f/misc/demo-journal.py#L275)
- [newest-version.py:25](https://github.com/magic-wormhole/magic-wormhole/blob/657bd5d51c67db2109219ff57b7d997afa57261f/newest-version.py#L25)
- [update-version.py:109](https://github.com/magic-wormhole/magic-wormhole/blob/657bd5d51c67db2109219ff57b7d997afa57261f/update-version.py#L109)
- [versioneer.py:2273](https://github.com/magic-wormhole/magic-wormhole/blob/657bd5d51c67db2109219ff57b7d997afa57261f/versioneer.py#L2273)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 6 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Action, Agent, AliasedGroup, Config, NotThisMethod, Root. Observed top-level functions: _c… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| misc package | library | Observed | Groups 3 file(s) under misc package (observed from repository paths and static analysis). Observed top-level functions: web. |
| Tests | test | Observed | Groups 41 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH wormhole._rlcompleter.CodeInputter, PATCH wormhole._rlcompleter.readline, PATCH wormhole._rlcompleter.input, PAT… |
| wormhole package | library | Observed | Groups 47 file(s) under wormhole package (observed from repository paths and static analysis). Observed top-level classes: AllegedSharedKey, AllocatedCode, Allocator, AlreadyChoseNameplateError, AlreadyChoseWordsError,… |

## Important files

- `.appveyor.yml` (config)
- `.github/workflows/codespell.yml` (ci)
- `.github/workflows/documentation-links.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `.readthedocs.yaml` (config)
- `MANIFEST.in` (manifest)
- `docs/requirements.txt` (manifest)
- `pyproject.toml` (manifest)
- `setup.cfg` (manifest)
- `setup.py` (manifest)
- `snapcraft.yaml` (config)
- `tox.ini` (config)

## Top-level layout

- `src` — 90 analysed file(s)
- `signatures` — 61 analysed file(s)
- `docs` — 46 analysed file(s)
- `(root files)` — 22 analysed file(s)
- `misc` — 7 analysed file(s)
- `.github` — 3 analysed file(s)
- `pyi` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `657bd5d51c67db2109219ff57b7d997afa57261f` is the revision these paths and observations refer to.
