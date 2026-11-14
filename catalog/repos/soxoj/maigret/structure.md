# Project structure: soxoj/maigret

**Analysed commit:** `244bc2924c45b649faeba86cd63cff06522384be`

**Commit reference:** [244bc2924c45b649faeba86cd63cff06522384be](https://github.com/soxoj/maigret/commit/244bc2924c45b649faeba86cd63cff06522384be)

**Tree at this commit:** [soxoj/maigret@244bc2924c45](https://github.com/soxoj/maigret/tree/244bc2924c45b649faeba86cd63cff06522384be)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | soxoj/maigret |
| Description | 🕵️‍♂️ Collect a dossier on a person by username from 6K websites |
| Stars | 40669 |
| Forks | 3283 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `244bc2924c45b649faeba86cd63cff06522384be` |
| Retrieved at | 2026-11-14T19:06:41.640619+00:00 |
| Files in this snapshot | 178 |

## Directory tree

```text
.githooks/  (1 files)
  pre-commit
.github/  (11 files)
  ISSUE_TEMPLATE/  (3 files)
    add-a-site.md
    bug.md
    report-false-result.md
  workflows/  (6 files)
    build-docker-image.yml
    codeql-analysis.yml
    pyinstaller.yml
    python-package.yml
    python-publish.yml
    update-site-data.yml
  FUNDING.yml
  dependabot.yml
docs/  (58 files)
  source/  (55 files)
    _static/  (1 files)
      … 1 files under this directory
    locale/  (35 files)
      … 35 files under this directory
    use-cases/  (2 files)
      … 2 files under this directory
    command-line-options.rst
    conf.py
    development.rst
    faq.rst
    features.rst
    index.rst
    installation.rst
    library-usage.rst
    philosophy.rst
    privacy.rst
    quick-start.rst
    release-process.rst
    settings.rst
    supported-identifier-types.rst
    tags.rst
    tor-and-proxies.rst
    usage-examples.rst
  Makefile
  make.bat
  requirements.txt
maigret/  (32 files)
  resources/  (6 files)
    ai_prompt.txt
    db_meta.json
    settings.json
    simple_report.tpl
    simple_report_pdf.css
    simple_report_pdf.tpl
  web/  (7 files)
    templates/  (6 files)
      … 6 files under this directory
    app.py
  __init__.py
  __main__.py
  __version__.py
  activation.py
  ai.py
  checking.py
  db_updater.py
  error_detection.py
  errors.py
  executors.py
  maigret.py
  notify.py
  permutator.py
  report.py
  result.py
  settings.py
  sites.py
  submit.py
  utils.py
pyinstaller/  (3 files)
  maigret_standalone.py
  maigret_standalone.spec
  requirements.txt
snap/  (1 files)
  snapcraft.yaml
static/  (3 files)
  chat_gitter.svg
  recursive_search.md
  report_alexaimephotographycars.html
tests/  (35 files)
  __init__.py
  conftest.py
  db.json
  local.json
  test_activation.py
  test_ai.py
  test_checking.py
  test_cli.py
  test_cloudflare_webgate.py
  test_country_tags.py
  test_data.py
  test_db_updater.py
  test_error_detection.py
  test_errors.py
  test_executors.py
  test_extractors.py
  test_generate_changelog.py
  test_idempotent_writes.py
  test_input_file_bom.py
  test_keyword_filtering.py
  test_maigret.py
  test_mastodon_engine.py
  test_notify.py
  test_permutator.py
  … 11 more files
utils/  (14 files)
  __init__.py
  add_tags.py
  check_engines.py
  check_top_n.py
  cloudshell_install.sh
  fp_probe_top_sites.py
  generate_changelog.py
  generate_db_meta.py
  import_sites.py
  render.yaml
  selfcheck_triage.py
  site_check.py
  sites_diff.py
  update_site_data.py
.dockerignore
.gitignore
.readthedocs.yaml
CHANGELOG.md
CITATION.cff
CODE_OF_CONDUCT.md
CONTRIBUTING.md
Dockerfile
Installer.bat
LICENSE
Makefile
README.fr.md
README.md
README.zh-CN.md
TROUBLESHOOTING.md
cloudshell-tutorial.md
example.ipynb
pyproject.toml
pytest.ini
wizard.py
```

## Entry points

- [maigret/__main__.py:12](https://github.com/soxoj/maigret/blob/244bc2924c45b649faeba86cd63cff06522384be/maigret/__main__.py#L12)
- [maigret/maigret.py:1195](https://github.com/soxoj/maigret/blob/244bc2924c45b649faeba86cd63cff06522384be/maigret/maigret.py#L1195)
- [maigret/web/app.py:28](https://github.com/soxoj/maigret/blob/244bc2924c45b649faeba86cd63cff06522384be/maigret/web/app.py#L28)
- [pyinstaller/maigret_standalone.py:95](https://github.com/soxoj/maigret/blob/244bc2924c45b649faeba86cd63cff06522384be/pyinstaller/maigret_standalone.py#L95)
- [utils/add_tags.py:26](https://github.com/soxoj/maigret/blob/244bc2924c45b649faeba86cd63cff06522384be/utils/add_tags.py#L26)
- [utils/check_engines.py:28](https://github.com/soxoj/maigret/blob/244bc2924c45b649faeba86cd63cff06522384be/utils/check_engines.py#L28)
- [utils/check_top_n.py:479](https://github.com/soxoj/maigret/blob/244bc2924c45b649faeba86cd63cff06522384be/utils/check_top_n.py#L479)
- [utils/fp_probe_top_sites.py:222](https://github.com/soxoj/maigret/blob/244bc2924c45b649faeba86cd63cff06522384be/utils/fp_probe_top_sites.py#L222)
- [utils/generate_changelog.py:142](https://github.com/soxoj/maigret/blob/244bc2924c45b649faeba86cd63cff06522384be/utils/generate_changelog.py#L142)
- [utils/generate_db_meta.py:122](https://github.com/soxoj/maigret/blob/244bc2924c45b649faeba86cd63cff06522384be/utils/generate_db_meta.py#L122)
- [utils/import_sites.py:91](https://github.com/soxoj/maigret/blob/244bc2924c45b649faeba86cd63cff06522384be/utils/import_sites.py#L91)
- [utils/selfcheck_triage.py:126](https://github.com/soxoj/maigret/blob/244bc2924c45b649faeba86cd63cff06522384be/utils/selfcheck_triage.py#L126)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 9 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: Settings. |
| Application entry point | entrypoint | Observed | Groups 15 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Flask. Observed routes: ROUTE /api/scan, ROUTE /api/scan/<job_id>/stream, ROU… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| maigret package | library | Observed | Groups 16 file(s) under maigret package (observed from repository paths and static analysis). Observed top-level classes: AiodnsDomainResolver, AsyncioQueueGeneratorExecutor, CaseConverter, CheckError, CheckerBase, Chec… |
| Tests | test | Observed | Groups 35 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH maigret.db_updater._fetch_meta, PATCH maigret.db_updater._fetch_meta, PATCH maigret.db_updater._fetch_meta, PATC… |
| utils package | library | Observed | Groups 3 file(s) under utils package (observed from repository paths and static analysis). Observed top-level functions: get_match_ratio. |

## Important files

- `.dockerignore` (container)
- `.github/FUNDING.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/build-docker-image.yml` (ci)
- `.github/workflows/codeql-analysis.yml` (ci)
- `.github/workflows/pyinstaller.yml` (ci)
- `.github/workflows/python-package.yml` (ci)
- `.github/workflows/python-publish.yml` (ci)
- `.github/workflows/update-site-data.yml` (ci)
- `.readthedocs.yaml` (config)
- `Dockerfile` (container)
- `docs/requirements.txt` (manifest)
- `maigret/resources/db_meta.json` (config)
- `maigret/resources/settings.json` (config)
- `pyinstaller/requirements.txt` (manifest)
- `pyproject.toml` (manifest)
- `pytest.ini` (config)
- `snap/snapcraft.yaml` (config)
- `utils/render.yaml` (config)

## Top-level layout

- `docs` — 58 analysed file(s)
- `tests` — 35 analysed file(s)
- `maigret` — 32 analysed file(s)
- `(root files)` — 20 analysed file(s)
- `utils` — 14 analysed file(s)
- `.github` — 11 analysed file(s)
- `pyinstaller` — 3 analysed file(s)
- `static` — 3 analysed file(s)
- `.githooks` — 1 analysed file(s)
- `snap` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `244bc2924c45b649faeba86cd63cff06522384be` is the revision these paths and observations refer to.
