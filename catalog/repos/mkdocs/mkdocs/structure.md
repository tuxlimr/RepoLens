# Project structure: mkdocs/mkdocs

**Analysed commit:** `2862536793b3c67d9d83c33e0dd6d50a791928f8`

**Commit reference:** [2862536793b3c67d9d83c33e0dd6d50a791928f8](https://github.com/mkdocs/mkdocs/commit/2862536793b3c67d9d83c33e0dd6d50a791928f8)

**Tree at this commit:** [mkdocs/mkdocs@2862536793b3](https://github.com/mkdocs/mkdocs/tree/2862536793b3c67d9d83c33e0dd6d50a791928f8)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | mkdocs/mkdocs |
| Description | Project documentation with Markdown. |
| Stars | 22550 |
| Forks | 2663 |
| Licence | BSD-2-Clause |
| Language | Python |
| Default branch | master |
| Analysed commit | `2862536793b3c67d9d83c33e0dd6d50a791928f8` |
| Retrieved at | 2026-11-14T19:07:52.205412+00:00 |
| Files in this snapshot | 230 |

## Directory tree

```text
.github/  (4 files)
  workflows/  (4 files)
    autofix.yml
    ci.yml
    deploy-release.yml
    docs.yml
docs/  (24 files)
  about/  (3 files)
    contributing.md
    license.md
    release-notes.md
  css/  (1 files)
    extra.css
  dev-guide/  (5 files)
    README.md
    api.md
    plugins.md
    themes.md
    translations.md
  img/  (2 files)
    plugin-events.py
    plugin-events.svg
  user-guide/  (9 files)
    README.md
    choosing-your-theme.md
    cli.md
    configuration.md
    customizing-your-theme.md
    deploying-your-docs.md
    installation.md
    localizing-your-theme.md
    writing-your-docs.md
  CNAME
  getting-started.md
  hooks.py
  index.md
mkdocs/  (185 files)
  commands/  (5 files)
    __init__.py
    build.py
    gh_deploy.py
    new.py
    serve.py
  config/  (4 files)
    __init__.py
    base.py
    config_options.py
    defaults.py
  contrib/  (38 files)
    search/  (37 files)
      … 37 files under this directory
    __init__.py
  livereload/  (1 files)
    __init__.py
  structure/  (5 files)
    __init__.py
    files.py
    nav.py
    pages.py
    toc.py
  templates/  (1 files)
    sitemap.xml
  tests/  (51 files)
    config/  (5 files)
      … 5 files under this directory
    integration/  (25 files)
      … 25 files under this directory
    structure/  (5 files)
      … 5 files under this directory
    utils/  (4 files)
      … 4 files under this directory
    __init__.py
    base.py
    build_tests.py
    cli_tests.py
    gh_deploy_tests.py
    integration.py
    livereload_tests.py
    localization_tests.py
    new_tests.py
    plugin_tests.py
    search_tests.py
    theme_tests.py
  themes/  (65 files)
    mkdocs/  (31 files)
      … 31 files under this directory
    readthedocs/  (32 files)
      … 32 files under this directory
    __init__.py
    babel.cfg
  utils/  (8 files)
    __init__.py
    babel_stub.py
    cache.py
    filters.py
    meta.py
    rendering.py
    templates.py
    yaml.py
  __init__.py
  __main__.py
  exceptions.py
  localization.py
  plugins.py
  py.typed
  theme.py
requirements/  (2 files)
  requirements-docs.txt
  requirements-style.txt
.codecov.yml
.coveragerc
.editorconfig
.gitattributes
.gitignore
.jshintignore
.markdownlint.yaml
CONTRIBUTING.md
FUNDING.yml
LICENSE
README.md
hatch_build.py
mkdocs.yml
pyproject.toml
setup.py
```

## Entry points

- [mkdocs/__main__.py](https://github.com/mkdocs/mkdocs/blob/2862536793b3c67d9d83c33e0dd6d50a791928f8/mkdocs/__main__.py)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 13 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: BaseConfigOption, Choice, Config, ConfigItems, Deprecated, DictOfItems. Observed top… |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). Observed top-level classes: CustomBuildHook. |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: ColorFormatter, State. Observed top-level functions: _enable_warnings, _showwarning, add_o… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| mkdocs package | library | Observed | Groups 69 file(s) under mkdocs package (observed from repository paths and static analysis). Observed top-level classes: Abort, AnchorLink, BasePlugin, BuildError, CombinedEvent, ConfigDirPlaceholder. Observed top-level… |
| Tests | test | Observed | Groups 51 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH mkdocs.utils.write_file, PATCH mkdocs.commands.build._build_template, PATCH mkdocs.utils.write_file, PATCH mkdoc… |

## Important files

- `.codecov.yml` (config)
- `.editorconfig` (config)
- `.github/workflows/autofix.yml` (ci)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/deploy-release.yml` (ci)
- `.github/workflows/docs.yml` (ci)
- `.markdownlint.yaml` (config)
- `FUNDING.yml` (config)
- `mkdocs.yml` (config)
- `mkdocs/themes/babel.cfg` (config)
- `mkdocs/themes/mkdocs/mkdocs_theme.yml` (config)
- `mkdocs/themes/readthedocs/mkdocs_theme.yml` (config)
- `pyproject.toml` (manifest)
- `requirements/requirements-docs.txt` (manifest)
- `requirements/requirements-style.txt` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `mkdocs` — 185 analysed file(s)
- `docs` — 24 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `.github` — 4 analysed file(s)
- `requirements` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 4 file(s) were skipped during inventory (4 x generated/minified file excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `2862536793b3c67d9d83c33e0dd6d50a791928f8` is the revision these paths and observations refer to.
