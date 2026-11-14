# Project structure: s0md3v/XSStrike

**Analysed commit:** `ab27955d367432f944d8f29897e09c15356e76f7`

**Commit reference:** [ab27955d367432f944d8f29897e09c15356e76f7](https://github.com/s0md3v/XSStrike/commit/ab27955d367432f944d8f29897e09c15356e76f7)

**Tree at this commit:** [s0md3v/XSStrike@ab27955d3674](https://github.com/s0md3v/XSStrike/tree/ab27955d367432f944d8f29897e09c15356e76f7)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | s0md3v/XSStrike |
| Description | Most advanced XSS scanner. |
| Stars | 15264 |
| Forks | 2098 |
| Licence | GPL-3.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `ab27955d367432f944d8f29897e09c15356e76f7` |
| Retrieved at | 2026-11-14T19:09:05.109965+00:00 |
| Files in this snapshot | 39 |

## Directory tree

```text
.github/  (3 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  PULL_REQUEST_TEMPLATE.md
core/  (19 files)
  __init__.py
  checker.py
  colors.py
  config.py
  dom.py
  encoders.py
  filterChecker.py
  fuzzer.py
  generator.py
  htmlParser.py
  jsContexter.py
  log.py
  photon.py
  prompt.py
  requester.py
  updater.py
  utils.py
  wafDetector.py
  zetanize.py
db/  (2 files)
  definitions.json
  wafSignatures.json
modes/  (5 files)
  __init__.py
  bruteforcer.py
  crawl.py
  scan.py
  singleFuzz.py
plugins/  (2 files)
  __init__.py
  retireJs.py
.gitignore
.travis.yml
CHANGELOG.md
LICENSE
README.md
requirements.txt
test.html
xsstrike.py
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| modes package | library | Observed | Groups 5 file(s) under modes package (observed from repository paths and static analysis). Observed top-level functions: bruteforcer, crawl, scan, singleFuzz. |
| plugins package | library | Observed | Groups 2 file(s) under plugins package (observed from repository paths and static analysis). Observed top-level functions: _is_at_or_above, _replace_version, _replacement_match, _scanhash, _simple_match, _to_comparable. |
| Service / domain layer | service | Observed | Groups 18 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: CustomFormatter, CustomStreamHandler. Observed top-level functions: _get_level_and_log, _g… |

## Important files

- `.travis.yml` (ci)
- `db/definitions.json` (config)
- `db/wafSignatures.json` (config)
- `requirements.txt` (manifest)

## Top-level layout

- `core` — 19 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `modes` — 5 analysed file(s)
- `.github` — 3 analysed file(s)
- `db` — 2 analysed file(s)
- `plugins` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `ab27955d367432f944d8f29897e09c15356e76f7` is the revision these paths and observations refer to.
