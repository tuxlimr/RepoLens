# Project structure: sivel/speedtest-cli

**Analysed commit:** `22210ca35228f0bbcef75a7c14587c4ecb875ab4`

**Commit reference:** [22210ca35228f0bbcef75a7c14587c4ecb875ab4](https://github.com/sivel/speedtest-cli/commit/22210ca35228f0bbcef75a7c14587c4ecb875ab4)

**Tree at this commit:** [sivel/speedtest-cli@22210ca35228](https://github.com/sivel/speedtest-cli/tree/22210ca35228f0bbcef75a7c14587c4ecb875ab4)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | sivel/speedtest-cli |
| Description | Command line interface for testing internet bandwidth using speedtest.net |
| Stars | 14036 |
| Forks | 1903 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `22210ca35228f0bbcef75a7c14587c4ecb875ab4` |
| Retrieved at | 2026-11-14T19:09:35.229121+00:00 |
| Files in this snapshot | 12 |

## Directory tree

```text
tests/  (1 files)
  scripts/  (1 files)
    source.py
.gitignore
.travis.yml
CONTRIBUTING.md
LICENSE
MANIFEST.in
README.rst
setup.cfg
setup.py
speedtest-cli.1
speedtest.py
tox.ini
```

## Entry points

- [speedtest.py](https://github.com/sivel/speedtest-cli/blob/22210ca35228f0bbcef75a7c14587c4ecb875ab4/speedtest.py)
- [speedtest.py](https://github.com/sivel/speedtest-cli/blob/22210ca35228f0bbcef75a7c14587c4ecb875ab4/speedtest.py)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: find_version. |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: ConfigRetrievalError, FakeShutdownEvent, GzipDecodedResponse, HTTPDownloader, HTTPUploader… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.travis.yml` (ci)
- `MANIFEST.in` (manifest)
- `setup.cfg` (manifest)
- `setup.py` (manifest)
- `tox.ini` (config)

## Top-level layout

- `(root files)` — 11 analysed file(s)
- `tests` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- The GitHub repository was marked archived at selection time.

Commit `22210ca35228f0bbcef75a7c14587c4ecb875ab4` is the revision these paths and observations refer to.
