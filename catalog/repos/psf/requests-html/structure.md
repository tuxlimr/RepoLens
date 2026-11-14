# Project structure: psf/requests-html

**Analysed commit:** `075ac162dc62fc532037df0d98954ab840a97516`

**Commit reference:** [075ac162dc62fc532037df0d98954ab840a97516](https://github.com/psf/requests-html/commit/075ac162dc62fc532037df0d98954ab840a97516)

**Tree at this commit:** [psf/requests-html@075ac162dc62](https://github.com/psf/requests-html/tree/075ac162dc62fc532037df0d98954ab840a97516)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | psf/requests-html |
| Description | Pythonic HTML Parsing for Humans™ |
| Stars | 13798 |
| Forks | 998 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `075ac162dc62fc532037df0d98954ab840a97516` |
| Retrieved at | 2026-11-14T19:09:42.457407+00:00 |
| Files in this snapshot | 20 |

## Directory tree

```text
docs/  (7 files)
  source/  (5 files)
    _templates/  (3 files)
      … 3 files under this directory
    conf.py
    index.rst
  Makefile
  make.bat
tests/  (3 files)
  python.html
  test_internet.py
  test_requests_html.py
.gitattributes
.gitignore
.travis.yml
LICENSE
Makefile
Pipfile
README.rst
pytest.ini
requests_html.py
setup.py
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: UploadCommand. |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). Observed top-level classes: AsyncHTMLSession, BaseParser, BaseSession, Element, HTML, HTMLResponse. Observed top-level functions:… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 3 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: async_get, get, test_absolute_links, test_anchor_links, test_async_browser_session, test_async_file_get. |

## Important files

- `.travis.yml` (ci)
- `Pipfile` (manifest)
- `pytest.ini` (config)
- `setup.py` (manifest)

## Top-level layout

- `(root files)` — 10 analysed file(s)
- `docs` — 7 analysed file(s)
- `tests` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `075ac162dc62fc532037df0d98954ab840a97516` is the revision these paths and observations refer to.
