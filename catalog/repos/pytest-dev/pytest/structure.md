# Project structure: pytest-dev/pytest

**Analysed commit:** `fc9a7ef678f64d17f1c03b619f3842ea1d127e74`

**Commit reference:** [fc9a7ef678f64d17f1c03b619f3842ea1d127e74](https://github.com/pytest-dev/pytest/commit/fc9a7ef678f64d17f1c03b619f3842ea1d127e74)

**Tree at this commit:** [pytest-dev/pytest@fc9a7ef678f6](https://github.com/pytest-dev/pytest/tree/fc9a7ef678f64d17f1c03b619f3842ea1d127e74)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | pytest-dev/pytest |
| Description | The pytest framework makes it easy to write small tests, yet scales to support complex functional testing |
| Stars | 14685 |
| Forks | 3629 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `fc9a7ef678f64d17f1c03b619f3842ea1d127e74` |
| Retrieved at | 2026-11-14T19:09:19.905635+00:00 |
| Files in this snapshot | 632 |

## Directory tree

```text
.github/  (18 files)
  ISSUE_TEMPLATE/  (4 files)
    1_bug_report.md
    2_feature_request.md
    3_security_vulnerability.md
    config.yml
  actions/  (1 files)
    setup-tox/  (1 files)
      … 1 files under this directory
  workflows/  (6 files)
    deploy.yml
    doc-check-links.yml
    prepare-release-pr.yml
    stale.yml
    test.yml
    update-plugin-list.yml
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
  chronographer.yml
  config.yml
  dependabot.yml
  labels.toml
  patchback.yml
bench/  (7 files)
  bench.py
  bench_argcomplete.py
  empty.py
  manyparam.py
  skip.py
  unit_test.py
  xunit.py
changelog/  (10 files)
  .gitignore
  12582.improvement.rst
  15201.bugfix.rst
  15284.bugfix.rst
  15290.bugfix.rst
  15290.deprecation.rst
  15361.bugfix.rst
  15370.bugfix.rst
  README.rst
  _template.rst
doc/  (302 files)
  en/  (302 files)
    _static/  (1 files)
      … 1 files under this directory
    _templates/  (1 files)
      … 1 files under this directory
    announce/  (189 files)
      … 189 files under this directory
    example/  (45 files)
      … 45 files under this directory
    explanation/  (8 files)
      … 8 files under this directory
    how-to/  (24 files)
      … 24 files under this directory
    img/  (1 files)
      … 1 files under this directory
    proposals/  (1 files)
      … 1 files under this directory
    reference/  (5 files)
      … 5 files under this directory
    Makefile
    adopt.rst
    backwards-compatibility.rst
    broken-dep-constraints.txt
    builtin.rst
    conf.py
    conftest.py
    contact.rst
    contents.rst
    contributing.rst
    deprecations.rst
    development_guide.rst
    funcarg_compare.rst
    funcargs.rst
    getting-started.rst
    historical-notes.rst
    history.rst
    index.rst
    license.rst
    naming20.rst
    pytest.ini
    recwarn.rst
    requirements.txt
    sponsor.rst
    … 3 more files
extra/  (1 files)
  get_issues.py
scripts/  (10 files)
  .gitignore
  diff-assert-rewrite.py
  generate-gh-release-notes.py
  prepare-release-pr.py
  release.major.rst
  release.minor.rst
  release.patch.rst
  release.pre.rst
  release.py
  update-plugin-list.py
src/  (83 files)
  _pytest/  (79 files)
    _code/  (3 files)
      … 3 files under this directory
    _io/  (5 files)
      … 5 files under this directory
    _py/  (3 files)
      … 3 files under this directory
    assertion/  (12 files)
      … 12 files under this directory
    config/  (4 files)
      … 4 files under this directory
    mark/  (3 files)
      … 3 files under this directory
    __init__.py
    _argcomplete.py
    approx.py
    cacheprovider.py
    capture.py
    compat.py
    debugging.py
    deprecated.py
    doctest.py
    faulthandler.py
    fixtures.py
    freeze_support.py
    helpconfig.py
    hookspec.py
    junitxml.py
    legacypath.py
    logging.py
    main.py
    monkeypatch.py
    nodeid.py
    nodes.py
    outcomes.py
    pastebin.py
    pathlib.py
    … 25 more files
  pytest/  (3 files)
    __init__.py
    __main__.py
    py.typed
  py.py
testing/  (179 files)
  _py/  (1 files)
    test_local.py
  code/  (3 files)
    test_code.py
    test_excinfo.py
    test_source.py
  example_scripts/  (81 files)
    acceptance/  (1 files)
      … 1 files under this directory
    collect/  (9 files)
      … 9 files under this directory
    config/  (3 files)
      … 3 files under this directory
    conftest_usageerror/  (2 files)
      … 2 files under this directory
    customdirectory/  (6 files)
      … 6 files under this directory
    dataclasses/  (7 files)
      … 7 files under this directory
    doctest/  (2 files)
      … 2 files under this directory
    fixtures/  (26 files)
      … 26 files under this directory
    issue88_initial_file_multinodes/  (3 files)
      … 3 files under this directory
    marks/  (3 files)
      … 3 files under this directory
    perf_examples/  (3 files)
      … 3 files under this directory
    tmpdir/  (1 files)
      … 1 files under this directory
    unittest/  (7 files)
      … 7 files under this directory
    warnings/  (3 files)
      … 3 files under this directory
    README.rst
    __init__.py
    issue_519.py
    junit-10.xsd
    pytest.ini
  examples/  (1 files)
    test_issue519.py
  freeze/  (6 files)
    tests/  (2 files)
      … 2 files under this directory
    .gitignore
    create_executable.py
    runtests_script.py
    tox_run.py
  io/  (4 files)
    test_pprint.py
    test_saferepr.py
    test_terminalwriter.py
    test_wcwidth.py
  logging/  (3 files)
    test_fixture.py
    test_formatter.py
    test_reporting.py
  plugins_integration/  (14 files)
    .gitignore
    README.rst
    bdd_wallet.feature
    bdd_wallet.py
    django_settings.py
    pytest.ini
    pytest_anyio_integration.py
    pytest_asyncio_integration.py
    pytest_mock_integration.py
    pytest_rerunfailures_integration.py
    pytest_trio_integration.py
    pytest_twisted_integration.py
    requirements.txt
    simple_integration.py
  python/  (8 files)
    approx.py
    collect.py
    fixtures.py
    integration.py
    metafunc.py
    raises.py
    raises_group.py
    show_fixtures_per_test.py
  acceptance_test.py
  conftest.py
  deprecated_test.py
  test_argcomplete.py
  test_assertion.py
  test_assertrewrite.py
  test_assertrewrite_coverage.py
  test_cacheprovider.py
  test_capture.py
  test_collect_imported_tests.py
  test_collection.py
  test_compat.py
  test_config.py
  test_conftest.py
  test_debugging.py
  test_doctest.py
  test_entry_points.py
  test_error_diffs.py
  test_faulthandler.py
  test_findpaths.py
  test_helpconfig.py
  test_junitxml.py
  test_legacypath.py
  test_link_resolve.py
  … 34 more files
.git-blame-ignore-revs
.git_archival.txt
.gitattributes
.gitignore
.mailmap
.pre-commit-config.yaml
.readthedocs.yaml
AUTHORS
CHANGELOG.rst
CITATION
CODE_OF_CONDUCT.md
CONTRIBUTING.rst
LICENSE
MANIFEST.in
OPENCOLLECTIVE.rst
README.rst
RELEASING.rst
SECURITY.md
TIDELIFT.rst
codecov.yml
pyproject.toml
tox.ini
```

## Entry points

- [src/_pytest/config/__init__.py](https://github.com/pytest-dev/pytest/blob/fc9a7ef678f64d17f1c03b619f3842ea1d127e74/src/_pytest/config/__init__.py)
- [src/_pytest/config/__init__.py](https://github.com/pytest-dev/pytest/blob/fc9a7ef678f64d17f1c03b619f3842ea1d127e74/src/_pytest/config/__init__.py)
- [src/pytest/__main__.py:8](https://github.com/pytest-dev/pytest/blob/fc9a7ef678f64d17f1c03b619f3842ea1d127e74/src/pytest/__main__.py#L8)
- [bench/bench.py:6](https://github.com/pytest-dev/pytest/blob/fc9a7ef678f64d17f1c03b619f3842ea1d127e74/bench/bench.py#L6)
- [bench/bench_argcomplete.py:20](https://github.com/pytest-dev/pytest/blob/fc9a7ef678f64d17f1c03b619f3842ea1d127e74/bench/bench_argcomplete.py#L20)
- [extra/get_issues.py:78](https://github.com/pytest-dev/pytest/blob/fc9a7ef678f64d17f1c03b619f3842ea1d127e74/extra/get_issues.py#L78)
- [scripts/diff-assert-rewrite.py:156](https://github.com/pytest-dev/pytest/blob/fc9a7ef678f64d17f1c03b619f3842ea1d127e74/scripts/diff-assert-rewrite.py#L156)
- [scripts/generate-gh-release-notes.py:68](https://github.com/pytest-dev/pytest/blob/fc9a7ef678f64d17f1c03b619f3842ea1d127e74/scripts/generate-gh-release-notes.py#L68)
- [scripts/prepare-release-pr.py:179](https://github.com/pytest-dev/pytest/blob/fc9a7ef678f64d17f1c03b619f3842ea1d127e74/scripts/prepare-release-pr.py#L179)
- [scripts/release.py:147](https://github.com/pytest-dev/pytest/blob/fc9a7ef678f64d17f1c03b619f3842ea1d127e74/scripts/release.py#L147)
- [scripts/update-plugin-list.py:229](https://github.com/pytest-dev/pytest/blob/fc9a7ef678f64d17f1c03b619f3842ea1d127e74/scripts/update-plugin-list.py#L229)
- [testing/example_scripts/perf_examples/collect_stats/generate_folders.py:29](https://github.com/pytest-dev/pytest/blob/fc9a7ef678f64d17f1c03b619f3842ea1d127e74/testing/example_scripts/perf_examples/collect_stats/generate_folders.py#L29)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bench package | library | Observed | Groups 4 file(s) under bench package (observed from repository paths and static analysis). Observed top-level functions: foo, test_foo, test_it, test_it2. |
| Configuration and deployment | config | Observed | Groups 13 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: Argument, Config, ConfigValue, ConftestImportFailure, DropShorterLongHelpFormatter,… |
| Application entry point | entrypoint | Observed | Groups 15 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: CollectionArgument, Dir, FSHookProxy, Failed, Interrupted, InvalidFeatureRelease. Observe… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| py.py package | library | Observed | Groups 1 file(s) under py.py package (observed from repository paths and static analysis). |
| _pytest package | library | Observed | Groups 74 file(s) under _pytest package (observed from repository paths and static analysis). Observed top-level classes: AbstractRaises, Approx, ApproxDecimal, ApproxMapping, ApproxNumpy, ApproxScalar. Observed top-lev… |
| testing package | library | Observed | Groups 27 file(s) under testing package (observed from repository paths and static analysis). Observed top-level classes: MyTestCase, MyVec3, TestApprox, TestApproxDatetime, TestAutouseDiscovery, TestAutouseManagement.… |
| Tests | test | Observed | Groups 156 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: Action, AsyncArguments, Base, BaseFunctionalTests, Broken, C. Observed top-level functions: ConftestWithSe… |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/actions/setup-tox/action.yml` (config)
- `.github/chronographer.yml` (config)
- `.github/config.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/labels.toml` (config)
- `.github/patchback.yml` (config)
- `.github/workflows/deploy.yml` (ci)
- `.github/workflows/doc-check-links.yml` (ci)
- `.github/workflows/prepare-release-pr.yml` (ci)
- `.github/workflows/stale.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `.github/workflows/update-plugin-list.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `.readthedocs.yaml` (config)
- `MANIFEST.in` (manifest)
- `codecov.yml` (config)
- `doc/en/example/customdirectory/pytest.ini` (config)
- `doc/en/pytest.ini` (config)
- `doc/en/requirements.txt` (manifest)
- `pyproject.toml` (manifest)
- `testing/example_scripts/collect/collect_init_tests/pytest.ini` (config)
- `testing/example_scripts/customdirectory/pytest.ini` (config)
- `testing/example_scripts/pytest.ini` (config)
- `testing/plugins_integration/pytest.ini` (config)
- `testing/plugins_integration/requirements.txt` (manifest)
- `tox.ini` (config)

## Top-level layout

- `doc` — 302 analysed file(s)
- `testing` — 179 analysed file(s)
- `src` — 83 analysed file(s)
- `(root files)` — 22 analysed file(s)
- `.github` — 18 analysed file(s)
- `changelog` — 10 analysed file(s)
- `scripts` — 10 analysed file(s)
- `bench` — 7 analysed file(s)
- `extra` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `fc9a7ef678f64d17f1c03b619f3842ea1d127e74` is the revision these paths and observations refer to.
