# Project structure: instaloader/instaloader

**Analysed commit:** `7acd1b6a75d9964b6e7bf91c0769e172e2a64359`

**Commit reference:** [7acd1b6a75d9964b6e7bf91c0769e172e2a64359](https://github.com/instaloader/instaloader/commit/7acd1b6a75d9964b6e7bf91c0769e172e2a64359)

**Tree at this commit:** [instaloader/instaloader@7acd1b6a75d9](https://github.com/instaloader/instaloader/tree/7acd1b6a75d9964b6e7bf91c0769e172e2a64359)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | instaloader/instaloader |
| Description | Download pictures (or videos) along with their captions and other metadata from Instagram. |
| Stars | 13891 |
| Forks | 1669 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `7acd1b6a75d9964b6e7bf91c0769e172e2a64359` |
| Retrieved at | 2026-11-14T19:09:39.005718+00:00 |
| Files in this snapshot | 71 |

## Directory tree

```text
.github/  (12 files)
  ISSUE_TEMPLATE/  (4 files)
    bug_report.md
    config.yml
    feature_request.md
    question.md
  workflows/  (5 files)
    documentation.yml
    lint.yml
    packages.yml
    stale.yml
    windows_exe.yml
  dependabot.yml
  funding.yml
  pull_request_template.md
deploy/  (7 files)
  arch/  (3 files)
    .SRCINFO.template
    PKGBUILD.template
    deploy.sh
  windows/  (4 files)
    GPL-3.0.txt
    NOTICE.txt
    create_exe.py
    instaloader.spec
docs/  (32 files)
  _static/  (2 files)
    instaloaderdoc.css
    instaloaderdoc.js
  _templates/  (3 files)
    layout.html
    page.html
    search.html
  codesnippets/  (8 files)
    113_only_one_per_user.py
    120_ghost_followers.py
    121_since_until.py
    194_top_x_of_user.py
    56_track_deleted.py
    615_import_firefox_session.py
    666_historical_hashtag_data.py
    README.md
  module/  (5 files)
    exceptions.rst
    instaloader.rst
    instaloadercontext.rst
    nodeiterator.rst
    structures.rst
  .gitignore
  Makefile
  README.md
  as-module.rst
  basic-usage.rst
  cli-options.rst
  codesnippets.rst
  conf.py
  contributing.rst
  index.rst
  installation.rst
  logo.svg
  sponsors.rst
  troubleshooting.rst
instaloader/  (10 files)
  __init__.py
  __main__.py
  exceptions.py
  instaloader.py
  instaloadercontext.py
  lateststamps.py
  nodeiterator.py
  py.typed
  sectioniterator.py
  structures.py
test/  (1 files)
  README.md
.gitignore
.pylintrc
AUTHORS.md
CODE_OF_CONDUCT.md
LICENSE
Pipfile
README.rst
instaloader.py
setup.py
```

## Entry points

- [instaloader.py:5](https://github.com/instaloader/instaloader/blob/7acd1b6a75d9964b6e7bf91c0769e172e2a64359/instaloader.py#L5)
- [instaloader/__main__.py](https://github.com/instaloader/instaloader/blob/7acd1b6a75d9964b6e7bf91c0769e172e2a64359/instaloader/__main__.py)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: get_version. |
| deploy package | library | Observed | Groups 2 file(s) under deploy package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: ExitCode. Observed top-level functions: _main, filterstr_to_filterfunc, get_cookies_from_i… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| instaloader package | library | Observed | Groups 8 file(s) under instaloader package (observed from repository paths and static analysis). Observed top-level classes: AbortDownloadException, BadCredentialsException, BadResponseException, ConnectionException, Fr… |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/funding.yml` (config)
- `.github/workflows/documentation.yml` (ci)
- `.github/workflows/lint.yml` (ci)
- `.github/workflows/packages.yml` (ci)
- `.github/workflows/stale.yml` (ci)
- `.github/workflows/windows_exe.yml` (ci)
- `Pipfile` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `docs` — 32 analysed file(s)
- `.github` — 12 analysed file(s)
- `instaloader` — 10 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `deploy` — 7 analysed file(s)
- `test` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `7acd1b6a75d9964b6e7bf91c0769e172e2a64359` is the revision these paths and observations refer to.
