# Project structure: soimort/you-get

**Analysed commit:** `049548f3f3f35e67ba8d3181c71fdc71d11cf260`

**Commit reference:** [049548f3f3f35e67ba8d3181c71fdc71d11cf260](https://github.com/soimort/you-get/commit/049548f3f3f35e67ba8d3181c71fdc71d11cf260)

**Tree at this commit:** [soimort/you-get@049548f3f3f3](https://github.com/soimort/you-get/tree/049548f3f3f35e67ba8d3181c71fdc71d11cf260)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | soimort/you-get |
| Description | :arrow_double_down: Dumb downloader that scrapes the web |
| Stars | 56849 |
| Forks | 9652 |
| Licence | Other |
| Language | Python |
| Default branch | develop |
| Analysed commit | `049548f3f3f35e67ba8d3181c71fdc71d11cf260` |
| Retrieved at | 2026-11-14T19:06:26.176103+00:00 |
| Files in this snapshot | 155 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    python-package.yml
contrib/  (3 files)
  completion/  (3 files)
    _you-get
    you-get-completion.bash
    you-get.fish
src/  (132 files)
  you_get/  (132 files)
    cli_wrapper/  (14 files)
      … 14 files under this directory
    extractors/  (99 files)
      … 99 files under this directory
    processor/  (6 files)
      … 6 files under this directory
    util/  (7 files)
      … 7 files under this directory
    __init__.py
    __main__.py
    common.py
    extractor.py
    json_output.py
    version.py
tests/  (4 files)
  __init__.py
  test.py
  test_common.py
  test_util.py
.gitignore
CHANGELOG.rst
CONTRIBUTING.md
LICENSE.txt
MANIFEST.in
Makefile
README.md
README.rst
SECURITY.md
requirements.txt
setup.cfg
setup.py
you-get
you-get.json
you-get.plugin.zsh
```

## Entry points

- [src/you_get/__main__.py:94](https://github.com/soimort/you-get/blob/049548f3f3f35e67ba8d3181c71fdc71d11cf260/src/you_get/__main__.py#L94)
- [src/you_get/processor/join_flv.py:364](https://github.com/soimort/you-get/blob/049548f3f3f35e67ba8d3181c71fdc71d11cf260/src/you_get/processor/join_flv.py#L364)
- [src/you_get/processor/join_mp4.py:944](https://github.com/soimort/you-get/blob/049548f3f3f35e67ba8d3181c71fdc71d11cf260/src/you_get/processor/join_mp4.py#L944)
- [src/you_get/processor/join_ts.py:64](https://github.com/soimort/you-get/blob/049548f3f3f35e67ba8d3181c71fdc71d11cf260/src/you_get/processor/join_ts.py#L64)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: load_source. |
| Application entry point | entrypoint | Observed | Groups 5 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Atom, CompositeAtom, ECMAObject, VariableAtom. Observed top-level functions: concat_flv, c… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 4 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: TestCommon, TestUtil, YouGetTests. |
| you_get package | library | Observed | Groups 127 file(s) under you_get package (observed from repository paths and static analysis). Observed top-level classes: AcFun, Bigthink, Bilibili, BokeCC, CNTV, DummyProgressBar. Observed top-level functions: _get_re… |

## Important files

- `.github/workflows/python-package.yml` (ci)
- `MANIFEST.in` (manifest)
- `requirements.txt` (manifest)
- `setup.cfg` (manifest)
- `setup.py` (manifest)
- `you-get.json` (config)

## Top-level layout

- `src` — 132 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `tests` — 4 analysed file(s)
- `contrib` — 3 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `049548f3f3f35e67ba8d3181c71fdc71d11cf260` is the revision these paths and observations refer to.
