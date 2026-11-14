# Project structure: getpelican/pelican

**Analysed commit:** `e8748aba9ad0907a8801646e957b37a02709240d`

**Commit reference:** [e8748aba9ad0907a8801646e957b37a02709240d](https://github.com/getpelican/pelican/commit/e8748aba9ad0907a8801646e957b37a02709240d)

**Tree at this commit:** [getpelican/pelican@e8748aba9ad0](https://github.com/getpelican/pelican/tree/e8748aba9ad0907a8801646e957b37a02709240d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | getpelican/pelican |
| Description | Static site generator that supports Markdown and reST syntax. Powered by Python. |
| Stars | 13374 |
| Forks | 1835 |
| Licence | AGPL-3.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `e8748aba9ad0907a8801646e957b37a02709240d` |
| Retrieved at | 2026-11-14T19:09:50.735740+00:00 |
| Files in this snapshot | 448 |

## Directory tree

```text
.github/  (12 files)
  ISSUE_TEMPLATE/  (4 files)
    ---bug-report.md
    ---documentation.md
    ---enhancement-request.md
    config.yml
  workflows/  (2 files)
    github_pages.yml
    main.yml
  CODEOWNERS
  FUNDING.yml
  copilot-instructions.md
  dependabot.yml
  pull_request_template.md
  stale.yml
docs/  (38 files)
  _static/  (2 files)
    pelican-logo.svg
    theme_overrides.css
  _templates/  (1 files)
    page.html
  locale/  (17 files)
    zh_CN/  (17 files)
      … 17 files under this directory
  Makefile
  changelog.rst
  conf.py
  content.rst
  contribute.rst
  faq.rst
  importer.rst
  index.rst
  install.rst
  internals.rst
  pelican-themes.rst
  plugins.rst
  publish.rst
  quickstart.rst
  report.rst
  settings.rst
  themes.rst
  tips.rst
pelican/  (348 files)
  plugins/  (2 files)
    _utils.py
    signals.py
  tests/  (280 files)
    TestPages/  (13 files)
      … 13 files under this directory
    build_test/  (2 files)
      … 2 files under this directory
    content/  (56 files)
      … 56 files under this directory
    cyclic_intersite_links/  (3 files)
      … 3 files under this directory
    dummy_plugins/  (7 files)
      … 7 files under this directory
    mixed_content/  (1 files)
      … 1 files under this directory
    nested_content/  (2 files)
      … 2 files under this directory
    output/  (172 files)
      … 172 files under this directory
    parse_error/  (1 files)
      … 1 files under this directory
    theme_overrides/  (3 files)
      … 3 files under this directory
    __init__.py
    default_conf.py
    support.py
    test_cache.py
    test_cli.py
    test_contents.py
    test_generators.py
    test_importer.py
    test_log.py
    test_paginator.py
    test_pelican.py
    test_plugins.py
    test_readers.py
    test_rstdirectives.py
    test_server.py
    test_settings.py
    test_testsuite.py
    test_theme.py
    test_urlwrappers.py
    test_utils.py
  themes/  (43 files)
    notmyidea/  (29 files)
      … 29 files under this directory
    simple/  (14 files)
      … 14 files under this directory
  tools/  (8 files)
    templates/  (4 files)
      … 4 files under this directory
    __init__.py
    pelican_import.py
    pelican_quickstart.py
    pelican_themes.py
  __init__.py
  __main__.py
  cache.py
  contents.py
  generators.py
  log.py
  paginator.py
  readers.py
  rstdirectives.py
  server.py
  settings.py
  signals.py
  urlwrappers.py
  utils.py
  writers.py
requirements/  (4 files)
  developer.pip
  docs.pip
  owner.pip
  test.pip
samples/  (30 files)
  content/  (21 files)
    cat1/  (4 files)
      … 4 files under this directory
    extra/  (1 files)
      … 1 files under this directory
    pages/  (5 files)
      … 5 files under this directory
    2012-11-30_filename-metadata.rst
    another_super_article-fr.rst
    another_super_article.rst
    article2-fr.rst
    article2.rst
    article_tag_baz.rst
    draft_article without_date.rst
    draft_article.rst
    super_article.rst
    unbelievable.rst
    unwanted_file
  kinda/  (2 files)
    exciting/  (2 files)
      … 2 files under this directory
  theme_standard/  (2 files)
    a_stylesheet
    a_template
  very/  (3 files)
    exciting/  (3 files)
      … 3 files under this directory
  pelican.conf.py
  pelican.conf_FR.py
.coveragerc
.editorconfig
.git-blame-ignore-revs
.gitattributes
.gitignore
.mailmap
.pre-commit-config.yaml
.readthedocs.yaml
.vale.ini
CONTRIBUTING.rst
LICENSE
README.rst
THANKS
pyproject.toml
tasks.py
tox.ini
```

## Entry points

- [pelican/__main__.py](https://github.com/getpelican/pelican/blob/e8748aba9ad0907a8801646e957b37a02709240d/pelican/__main__.py)
- [pelican/log.py:162](https://github.com/getpelican/pelican/blob/e8748aba9ad0907a8801646e957b37a02709240d/pelican/log.py#L162)
- [pelican/plugins/_utils.py](https://github.com/getpelican/pelican/blob/e8748aba9ad0907a8801646e957b37a02709240d/pelican/plugins/_utils.py)
- [pelican/server.py:140](https://github.com/getpelican/pelican/blob/e8748aba9ad0907a8801646e957b37a02709240d/pelican/server.py#L140)
- [pelican/tools/pelican_import.py](https://github.com/getpelican/pelican/blob/e8748aba9ad0907a8801646e957b37a02709240d/pelican/tools/pelican_import.py)
- [pelican/tools/pelican_quickstart.py](https://github.com/getpelican/pelican/blob/e8748aba9ad0907a8801646e957b37a02709240d/pelican/tools/pelican_quickstart.py)
- [pelican/tools/pelican_themes.py](https://github.com/getpelican/pelican/blob/e8748aba9ad0907a8801646e957b37a02709240d/pelican/tools/pelican_themes.py)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: _printf_s_to_format_field, configure_settings, get_jinja_environment, get_settings_… |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). Observed top-level functions: coverage, docbuild, docserve, formatcode, lint, precommit. |
| Application entry point | entrypoint | Observed | Groups 4 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: ComplexHTTPRequestHandler, FatalLogger, FilteredMessage, LimitFilter, LimitLogger, RootedH… |
| pelican package | library | Observed | Groups 16 file(s) under pelican package (observed from repository paths and static analysis). Observed top-level classes: Article, ArticlesGenerator, Author, BaseReader, CachingGenerator, Category. Observed top-level fu… |
| samples package | library | Observed | Groups 2 file(s) under samples package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 281 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH pelican.tools.pelican_import._get_tumblr_posts, PATCH pelican.tools.pelican_import._get_tumblr_posts, PATCH pel… |

## Important files

- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/stale.yml` (config)
- `.github/workflows/github_pages.yml` (ci)
- `.github/workflows/main.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `.readthedocs.yaml` (config)
- `.vale.ini` (config)
- `pyproject.toml` (manifest)
- `tox.ini` (config)

## Top-level layout

- `pelican` — 348 analysed file(s)
- `docs` — 38 analysed file(s)
- `samples` — 30 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `.github` — 12 analysed file(s)
- `requirements` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `e8748aba9ad0907a8801646e957b37a02709240d` is the revision these paths and observations refer to.
