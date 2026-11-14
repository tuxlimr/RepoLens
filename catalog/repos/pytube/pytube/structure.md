# Project structure: pytube/pytube

**Analysed commit:** `a32fff39058a6f7e5e59ecd06a7467b71197ce35`

**Commit reference:** [a32fff39058a6f7e5e59ecd06a7467b71197ce35](https://github.com/pytube/pytube/commit/a32fff39058a6f7e5e59ecd06a7467b71197ce35)

**Tree at this commit:** [pytube/pytube@a32fff39058a](https://github.com/pytube/pytube/tree/a32fff39058a6f7e5e59ecd06a7467b71197ce35)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | pytube/pytube |
| Description | Lightweight, dependency-free Python library and CLI for downloading YouTube videos, playlists, and captions. |
| Stars | 13209 |
| Forks | 2477 |
| Licence | Unlicense |
| Language | Python |
| Default branch | master |
| Analysed commit | `a32fff39058a6f7e5e59ecd06a7467b71197ce35` |
| Retrieved at | 2026-11-14T19:09:54.971036+00:00 |
| Files in this snapshot | 60 |

## Directory tree

```text
.github/  (5 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (3 files)
    ci.yml
    greetings.yml
    pypi-publish.yml
pytube/  (21 files)
  contrib/  (4 files)
    __init__.py
    channel.py
    playlist.py
    search.py
  __init__.py
  __main__.py
  captions.py
  cipher.py
  cli.py
  exceptions.py
  extract.py
  helpers.py
  innertube.py
  itags.py
  metadata.py
  monostate.py
  parser.py
  query.py
  request.py
  streams.py
  version.py
tests/  (17 files)
  contrib/  (2 files)
    test_channel.py
    test_playlist.py
  __init__.py
  conftest.py
  test_captions.py
  test_cipher.py
  test_cli.py
  test_exceptions.py
  test_extract.py
  test_helpers.py
  test_itags.py
  test_main.py
  test_metadata.py
  test_parser.py
  test_query.py
  test_request.py
  test_streams.py
.bumpversion.cfg
.deepsource.toml
.editorconfig
.envrc
.flake8
.gitattributes
.gitignore
.pre-commit-config.yaml
.readthedocs.yml
CODE_OF_CONDUCT.md
Contributing.md
LICENSE
MANIFEST.in
Makefile
Pipfile
README.md
setup.py
```

## Entry points

- [pytube/cli.py](https://github.com/pytube/pytube/blob/a32fff39058a6f7e5e59ecd06a7467b71197ce35/pytube/cli.py)
- [pytube/version.py:3](https://github.com/pytube/pytube/blob/a32fff39058a6f7e5e59ecd06a7467b71197ce35/pytube/version.py#L3)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 3 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: YouTube. Observed top-level functions: _download, _ffmpeg_downloader, _parse_args, _perfor… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| pytube package | library | Observed | Groups 18 file(s) under pytube package (observed from repository paths and static analysis). Observed top-level classes: AgeRestrictedError, Caption, CaptionQuery, Channel, Cipher, DeferredGeneratorList. Observed top-le… |
| Tests | test | Observed | Groups 17 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH pytube.request.urlopen, PATCH pytube.request.get, PATCH pytube.request.get, PATCH pytube.request.get, PATCH pytu… |

## Important files

- `.bumpversion.cfg` (config)
- `.deepsource.toml` (config)
- `.editorconfig` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/greetings.yml` (ci)
- `.github/workflows/pypi-publish.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `.readthedocs.yml` (config)
- `MANIFEST.in` (manifest)
- `Pipfile` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `pytube` — 21 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `tests` — 17 analysed file(s)
- `.github` — 5 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `a32fff39058a6f7e5e59ecd06a7467b71197ce35` is the revision these paths and observations refer to.
