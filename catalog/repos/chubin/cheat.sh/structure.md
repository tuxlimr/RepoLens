# Project structure: chubin/cheat.sh

**Analysed commit:** `06af0000259bde1a347da368225c5962d7ffed3e`

**Commit reference:** [06af0000259bde1a347da368225c5962d7ffed3e](https://github.com/chubin/cheat.sh/commit/06af0000259bde1a347da368225c5962d7ffed3e)

**Tree at this commit:** [chubin/cheat.sh@06af0000259b](https://github.com/chubin/cheat.sh/tree/06af0000259bde1a347da368225c5962d7ffed3e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | chubin/cheat.sh |
| Description | the only cheat sheet you need |
| Stars | 41859 |
| Forks | 1919 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `06af0000259bde1a347da368225c5962d7ffed3e` |
| Retrieved at | 2026-11-14T19:06:40.944710+00:00 |
| Files in this snapshot | 112 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (2 files)
    tests-macos.yml
    tests-ubuntu.yml
bin/  (4 files)
  app.py
  clean_cache.py
  release.py
  srv.py
doc/  (2 files)
  README-ja.md
  standalone.md
etc/  (1 files)
  config.yaml
lib/  (40 files)
  adapter/  (14 files)
    __init__.py
    adapter.py
    cheat_cheat.py
    cheat_sheets.py
    cmd.py
    common.py
    git_adapter.py
    internal.py
    latenz.py
    learnxiny.py
    question.py
    rosetta.py
    tldr.py
    upstream.py
  fmt/  (4 files)
    __init__.py
    comments.py
    internal.py
    markdown.py
  frontend/  (3 files)
    __init__.py
    ansi.py
    html.py
  panela/  (3 files)
    colors.json
    colors.py
    panela_colors.py
  buttons.py
  cache.py
  cheat_wrapper.py
  cheat_wrapper_test.py
  config.py
  fetch.py
  globals.py
  languages_data.py
  limits.py
  options.py
  post.py
  postprocessing.py
  routing.py
  search.py
  standalone.py
  stateful_queries.py
share/  (26 files)
  adapters/  (4 files)
    chmod.grc
    chmod.sh
    oeis.sh
    rfc.sh
  scripts/  (2 files)
    cacheCleanup.go
    remove-from-cache.sh
  static/  (4 files)
    1.html
    malformed-response.html
    opensearch.xml
    style.css
  vim/  (1 files)
    .vimrc
  ansi2html.sh
  bash_completion.txt
  cht.sh.txt
  emacs-ivy.txt
  emacs.txt
  firstpage-v1.txt
  firstpage-v2.pnl
  firstpage-v2.txt
  fish.txt
  help.txt
  intro.txt
  post.txt
  styles-demo.txt
  vim.txt
  zsh.txt
tests/  (28 files)
  results/  (25 files)
    1
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    2
    20
    21
    22
    23
    24
    25
    3
    4
    5
    6
    7
    8
    … 1 more files
  README.md
  run-tests.sh
  tests.txt
.dockerignore
.gitignore
CONTRIBUTING.md
Dockerfile
LICENSE
README.md
docker-compose.debug.yml
docker-compose.yml
requirements.txt
```

## Entry points

- [bin/app.py:75](https://github.com/chubin/cheat.sh/blob/06af0000259bde1a347da368225c5962d7ffed3e/bin/app.py#L75)
- [lib/config.py:278](https://github.com/chubin/cheat.sh/blob/06af0000259bde1a347da368225c5962d7ffed3e/lib/config.py#L278)
- [lib/fetch.py:263](https://github.com/chubin/cheat.sh/blob/06af0000259bde1a347da368225c5962d7ffed3e/lib/fetch.py#L263)
- [lib/fmt/comments.py:349](https://github.com/chubin/cheat.sh/blob/06af0000259bde1a347da368225c5962d7ffed3e/lib/fmt/comments.py#L349)
- [lib/languages_data.py:271](https://github.com/chubin/cheat.sh/blob/06af0000259bde1a347da368225c5962d7ffed3e/lib/languages_data.py#L271)
- [lib/panela/panela_colors.py:696](https://github.com/chubin/cheat.sh/blob/06af0000259bde1a347da368225c5962d7ffed3e/lib/panela/panela_colors.py#L696)
- [lib/standalone.py:74](https://github.com/chubin/cheat.sh/blob/06af0000259bde1a347da368225c5962d7ffed3e/lib/standalone.py#L74)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bin package | library | Observed | Groups 3 file(s) under bin package (observed from repository paths and static analysis). Observed top-level functions: run. |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 7 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Flask. Observed routes: ROUTE /files/<path:path>, ROUTE /favicon.ico, ROUTE /m… |
| External integrations | external | Observed | Groups 3 file(s) under external integrations (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 32 file(s) under lib package (observed from repository paths and static analysis). Observed top-level classes: Adapter, AdapterChmod, AdapterMC, AdapterOeis, AdapterRfc, Cheat. Observed top-level functions: _add_… |
| share package | library | Observed | Groups 3 file(s) under share package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 29 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: test_header_split. |

## Important files

- `.dockerignore` (container)
- `.github/workflows/tests-macos.yml` (ci)
- `.github/workflows/tests-ubuntu.yml` (ci)
- `Dockerfile` (container)
- `docker-compose.debug.yml` (config)
- `docker-compose.yml` (container)
- `etc/config.yaml` (config)
- `lib/panela/colors.json` (config)
- `requirements.txt` (manifest)

## Top-level layout

- `lib` — 40 analysed file(s)
- `tests` — 28 analysed file(s)
- `share` — 26 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `bin` — 4 analysed file(s)
- `.github` — 2 analysed file(s)
- `doc` — 2 analysed file(s)
- `etc` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `06af0000259bde1a347da368225c5962d7ffed3e` is the revision these paths and observations refer to.
