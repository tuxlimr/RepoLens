# Project structure: joke2k/faker

**Analysed commit:** `affa2c5aada23fc5c00127298a8e904375d32832`

**Commit reference:** [affa2c5aada23fc5c00127298a8e904375d32832](https://github.com/joke2k/faker/commit/affa2c5aada23fc5c00127298a8e904375d32832)

**Tree at this commit:** [joke2k/faker@affa2c5aada2](https://github.com/joke2k/faker/tree/affa2c5aada23fc5c00127298a8e904375d32832)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | joke2k/faker |
| Description | Faker is a Python package that generates fake data for you. |
| Stars | 19491 |
| Forks | 2144 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `affa2c5aada23fc5c00127298a8e904375d32832` |
| Retrieved at | 2026-11-14T19:08:11.032496+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.agents/  (3 files)
  skills/  (3 files)
    new-release/  (1 files)
      … 1 files under this directory
    prepare-release/  (1 files)
      … 1 files under this directory
    update-changelog/  (1 files)
      … 1 files under this directory
.github/  (7 files)
  workflows/  (3 files)
    ci.yml
    gh-release.yml
    issues.yml
  FUNDING.yml
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
docs/  (13 files)
  _templates/  (1 files)
    breadcrumbs.html
  includes/  (1 files)
    substitutions.rst
  locales/  (1 files)
    .happygit
  providers/  (1 files)
    .happygit
  Makefile
  coding_style.rst
  communityproviders.rst
  conf.py
  fakerclass.rst
  index.rst
  make.bat
  pytest-fixtures.rst
  writing-docs.rst
faker/  (750 files)
  contrib/  (3 files)
    pytest/  (2 files)
      … 2 files under this directory
    __init__.py
  decode/  (1 files)
    __init__.py
  providers/  (722 files)
    address/  (67 files)
      … 67 files under this directory
    automotive/  (54 files)
      … 54 files under this directory
    bank/  (39 files)
      … 39 files under this directory
    barcode/  (6 files)
      … 6 files under this directory
    color/  (33 files)
      … 33 files under this directory
    company/  (47 files)
      … 47 files under this directory
    credit_card/  (7 files)
      … 7 files under this directory
    currency/  (37 files)
      … 37 files under this directory
    date_time/  (50 files)
      … 50 files under this directory
    doi/  (1 files)
      … 1 files under this directory
    emoji/  (2 files)
      … 2 files under this directory
    file/  (2 files)
      … 2 files under this directory
    geo/  (14 files)
      … 14 files under this directory
    internet/  (46 files)
      … 46 files under this directory
    isbn/  (4 files)
      … 4 files under this directory
    job/  (41 files)
      … 41 files under this directory
    lorem/  (33 files)
      … 33 files under this directory
    misc/  (5 files)
      … 5 files under this directory
    passport/  (6 files)
      … 6 files under this directory
    person/  (87 files)
      … 87 files under this directory
    phone_number/  (73 files)
      … 73 files under this directory
    profile/  (2 files)
      … 2 files under this directory
    python/  (2 files)
      … 2 files under this directory
    sbn/  (4 files)
      … 4 files under this directory
    ssn/  (57 files)
      … 57 files under this directory
    user_agent/  (2 files)
      … 2 files under this directory
    __init__.py
  sphinx/  (5 files)
    __init__.py
    autodoc.py
    docstring.py
    documentor.py
    validator.py
  utils/  (7 files)
    __init__.py
    checksums.py
    datasets.py
    decorators.py
    distribution.py
    loading.py
    text.py
  __init__.py
  __main__.py
  cli.py
  config.py
  documentor.py
  exceptions.py
  factory.py
  generator.py
  proxy.py
  proxy.pyi
  py.typed
  typing.py
scripts/  (1 files)
  check_test_class_order.py
tests/  (4 files)
  mymodule/  (2 files)
    en_US/  (1 files)
      … 1 files under this directory
    __init__.py
  __init__.py
  conftest.py
.bumpversion.cfg
.coveragerc
.dockerignore
.gitignore
.isort.cfg
CHANGELOG.md
CITATION.cff
CONTRIBUTING.rst
LICENSE.txt
MANIFEST.in
Makefile
README.rst
RELEASE_PROCESS.rst
SECURITY.md
VERSION
build-alpine.sh
dev-requirements.txt
generate_stubs.py
mypy.ini
readthedocs.yml
setup.cfg
setup.py
```

## Entry points

- [faker/__main__.py:1](https://github.com/joke2k/faker/blob/affa2c5aada23fc5c00127298a8e904375d32832/faker/__main__.py#L1)
- [faker/cli.py](https://github.com/joke2k/faker/blob/affa2c5aada23fc5c00127298a8e904375d32832/faker/cli.py)
- [scripts/check_test_class_order.py:125](https://github.com/joke2k/faker/blob/affa2c5aada23fc5c00127298a8e904375d32832/scripts/check_test_class_order.py#L125)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). Observed top-level classes: UniqueMemberFunctionsAndVariables. Observed top-level functions: get_import_str, get_member_functions… |
| Application entry point | entrypoint | Observed | Groups 3 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Command. Observed top-level classes: Command. Observed top-level functions: _c… |
| faker package | library | Observed | Groups 745 file(s) under faker package (observed from repository paths and static analysis). Observed top-level classes: BaseFakerException, BaseProvider, Country, CreditCard, Documentor, DynamicProvider. Observed top-l… |
| Tests | test | Observed | Groups 4 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: Provider. |

## Important files

- `.bumpversion.cfg` (config)
- `.dockerignore` (container)
- `.github/FUNDING.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/gh-release.yml` (ci)
- `.github/workflows/issues.yml` (ci)
- `.isort.cfg` (config)
- `MANIFEST.in` (manifest)
- `mypy.ini` (config)
- `readthedocs.yml` (config)
- `setup.cfg` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `faker` — 750 analysed file(s)
- `(root files)` — 22 analysed file(s)
- `docs` — 13 analysed file(s)
- `.github` — 7 analysed file(s)
- `tests` — 4 analysed file(s)
- `.agents` — 3 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `affa2c5aada23fc5c00127298a8e904375d32832` is the revision these paths and observations refer to.
