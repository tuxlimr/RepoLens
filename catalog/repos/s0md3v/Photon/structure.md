# Project structure: s0md3v/Photon

**Analysed commit:** `c8d2566841d69a268b244609921143d84b72b0c6`

**Commit reference:** [c8d2566841d69a268b244609921143d84b72b0c6](https://github.com/s0md3v/Photon/commit/c8d2566841d69a268b244609921143d84b72b0c6)

**Tree at this commit:** [s0md3v/Photon@c8d2566841d6](https://github.com/s0md3v/Photon/tree/c8d2566841d69a268b244609921143d84b72b0c6)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | s0md3v/Photon |
| Description | Incredibly fast crawler designed for OSINT. |
| Stars | 13346 |
| Forks | 1693 |
| Licence | GPL-3.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `c8d2566841d69a268b244609921143d84b72b0c6` |
| Retrieved at | 2026-11-14T19:09:52.312025+00:00 |
| Files in this snapshot | 27 |

## Directory tree

```text
core/  (12 files)
  __init__.py
  colors.py
  config.py
  flash.py
  mirror.py
  prompt.py
  regex.py
  requester.py
  updater.py
  user-agents.txt
  utils.py
  zap.py
plugins/  (5 files)
  __init__.py
  dnsdumpster.py
  exporter.py
  find_subdomains.py
  wayback.py
.gitignore
.travis.yml
.whitesource
CHANGELOG.md
Dockerfile
LICENSE.md
MANIFEST.in
README.md
photon.py
requirements.txt
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). Observed top-level functions: extractor, intel_extractor, js_extractor, jscanner, remove_file. |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| plugins package | library | Observed | Groups 5 file(s) under plugins package (observed from repository paths and static analysis). Observed top-level functions: dnsdumpster, exporter, find_subdomains, time_machine. |
| Service / domain layer | service | Observed | Groups 10 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level functions: entropy, extract_headers, flash, is_good_proxy, is_link, is_proxy_list. |

## Important files

- `.travis.yml` (ci)
- `Dockerfile` (container)
- `MANIFEST.in` (manifest)
- `requirements.txt` (manifest)

## Top-level layout

- `core` — 12 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `plugins` — 5 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `c8d2566841d69a268b244609921143d84b72b0c6` is the revision these paths and observations refer to.
