# Project structure: pypa/pipx

**Analysed commit:** `3ce2b3c742ee06b0d89d19a230e7b08043b75de9`

**Commit reference:** [3ce2b3c742ee06b0d89d19a230e7b08043b75de9](https://github.com/pypa/pipx/commit/3ce2b3c742ee06b0d89d19a230e7b08043b75de9)

**Tree at this commit:** [pypa/pipx@3ce2b3c742ee](https://github.com/pypa/pipx/tree/3ce2b3c742ee06b0d89d19a230e7b08043b75de9)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | pypa/pipx |
| Description | Install and Run Python Applications in Isolated Environments |
| Stars | 13001 |
| Forks | 647 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `3ce2b3c742ee06b0d89d19a230e7b08043b75de9` |
| Retrieved at | 2026-11-14T19:09:56.431591+00:00 |
| Files in this snapshot | 233 |

## Directory tree

```text
.github/  (20 files)
  ISSUE_TEMPLATE/  (3 files)
    bug.md
    config.yml
    feature_request.md
  workflows/  (9 files)
    actions.lock
    codeql.yaml
    news.yaml
    pre-release.yml
    release.yml
    scorecard.yaml
    tests.yml
    upgrade-release-tools.yaml
    zizmor.yml
  CONTRIBUTING.md
  FUNDING.yaml
  PULL_REQUEST_TEMPLATE.md
  SECURITY.md
  config.yml
  dependabot.yaml
  release.yml
  towncrier-template.rst
changelog.d/  (2 files)
  +python-sbom.packaging.rst
  .gitignore
docs/  (45 files)
  _ext/  (2 files)
    __init__.py
    llms_txt.py
  _static/  (2 files)
    custom.css
    logo.svg
  explanation/  (5 files)
    comparisons.rst
    how-pipx-works.rst
    index.rst
    making-packages-compatible.rst
    scope.rst
  how-to/  (18 files)
    configure-paths.rst
    dependency-cooldown.rst
    expose-apps.rst
    index.rst
    inject-packages.rst
    install-pipx.rst
    manage-installed-apps.rst
    move-installation.rst
    pin-packages.rst
    run-scripts.rst
    shell-completions.rst
    standalone-python.rst
    tool-manifest.rst
    troubleshoot.rst
    upgrade-pipx.rst
    use-private-index.rst
    use-uv-backend.rst
    use-with-pre-commit.rst
  man/  (1 files)
    pipx.1.rst
  reference/  (8 files)
    cli.rst
    environment-variables.rst
    examples.rst
    exit-codes.rst
    index.rst
    json-output.rst
    metadata.rst
    programs-to-try.rst
  tutorial/  (4 files)
    getting-started.rst
    index.rst
    install-applications.rst
    run-applications.rst
  README.md
  changelog.rst
  conf.py
  contributing.rst
  index.rst
scripts/  (7 files)
  check_distribution_manpage.py
  generate_man.py
  list_test_packages.py
  migrate_pipsi_to_pipx.py
  release.py
  test_packages_support.py
  update_package_cache.py
src/  (57 files)
  pipx/  (57 files)
    backends/  (5 files)
      … 5 files under this directory
    commands/  (24 files)
      … 24 files under this directory
    __init__.py
    __main__.py
    _env_parsing.py
    animate.py
    colors.py
    constants.py
    emojis.py
    fanout.py
    interpreter.py
    main.py
    options.py
    package_specifier.py
    paths.py
    pipx_metadata_file.py
    redact.py
    requires_python.py
    result.py
    script.py
    self_install.py
    shared_libs.py
    standalone_python.py
    subprocess_runner.py
    trash.py
    util.py
    … 4 more files
testdata/  (27 files)
  empty_project/  (4 files)
    empty_project/  (2 files)
      … 2 files under this directory
    README.md
    pyproject.toml
  test_package_specifier/  (13 files)
    local_completion/  (6 files)
      … 6 files under this directory
    local_extras/  (3 files)
      … 3 files under this directory
    local_manpage/  (4 files)
      … 4 files under this directory
  tests_packages/  (9 files)
    README.md
    macos24-python3.13.txt
    primary_packages.txt
    unix-python3.10.txt
    unix-python3.11.txt
    unix-python3.12.txt
    unix-python3.13.txt
    unix-python3.9.txt
    win-python3.13.txt
  pipx_metadata_multiple_errors.json
tests/  (62 files)
  pipx/  (1 files)
    test_env_parsing.py
  conftest.py
  harness.py
  package_info.py
  test_animate.py
  test_backends.py
  test_backends_install.py
  test_backends_pip.py
  test_cache.py
  test_common.py
  test_completions.py
  test_completions_expose.py
  test_docs_urls.py
  test_emojis.py
  test_ensurepath.py
  test_environment.py
  test_execute.py
  test_expose.py
  test_fanout.py
  test_health.py
  test_imports.py
  test_inject.py
  test_install.py
  test_install_all.py
  test_interpreter.py
  … 37 more files
.deepsource.toml
.gitignore
.pre-commit-config.yaml
.pre-commit-hooks.yaml
.readthedocs.yml
LICENSE
get-pipx.py
hatch_build.py
logo.svg
pylock.toml
pylock.zipapp.toml
pyproject.toml
tox.toml
```

## Entry points

- [src/pipx/__main__.py](https://github.com/pypa/pipx/blob/3ce2b3c742ee06b0d89d19a230e7b08043b75de9/src/pipx/__main__.py)
- [src/pipx/main.py:2360](https://github.com/pypa/pipx/blob/3ce2b3c742ee06b0d89d19a230e7b08043b75de9/src/pipx/main.py#L2360)
- [get-pipx.py:13](https://github.com/pypa/pipx/blob/3ce2b3c742ee06b0d89d19a230e7b08043b75de9/get-pipx.py#L13)
- [scripts/check_distribution_manpage.py:59](https://github.com/pypa/pipx/blob/3ce2b3c742ee06b0d89d19a230e7b08043b75de9/scripts/check_distribution_manpage.py#L59)
- [scripts/generate_man.py:145](https://github.com/pypa/pipx/blob/3ce2b3c742ee06b0d89d19a230e7b08043b75de9/scripts/generate_man.py#L145)
- [scripts/list_test_packages.py:135](https://github.com/pypa/pipx/blob/3ce2b3c742ee06b0d89d19a230e7b08043b75de9/scripts/list_test_packages.py#L135)
- [scripts/migrate_pipsi_to_pipx.py:36](https://github.com/pypa/pipx/blob/3ce2b3c742ee06b0d89d19a230e7b08043b75de9/scripts/migrate_pipsi_to_pipx.py#L36)
- [scripts/release.py:163](https://github.com/pypa/pipx/blob/3ce2b3c742ee06b0d89d19a230e7b08043b75de9/scripts/release.py#L163)
- [scripts/update_package_cache.py:105](https://github.com/pypa/pipx/blob/3ce2b3c742ee06b0d89d19a230e7b08043b75de9/scripts/update_package_cache.py#L105)
- [testdata/empty_project/empty_project/main.py:5](https://github.com/pypa/pipx/blob/3ce2b3c742ee06b0d89d19a230e7b08043b75de9/testdata/empty_project/empty_project/main.py#L5)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 9 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). Observed top-level classes: _CustomBuildHook. |
| Application entry point | entrypoint | Observed | Groups 14 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: InstalledVenvsCompleter, _CompletableAction, _DeprecatedFetchMissingPython, _DispatchCont… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| pipx package | library | Observed | Groups 53 file(s) under pipx package (observed from repository paths and static analysis). Observed top-level classes: AppLookupOptions, Backend, BackendOptions, CacheData, CooldownOptions, EnvironmentOptions. Observed… |
| testdata package | library | Observed | Groups 4 file(s) under testdata package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 63 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: CurrentMetadata, LegacyMetadata, LegacyPackageInfo, MakePylock, _Envelope, _EnvelopeFailure. Observed top-l… |

## Important files

- `.deepsource.toml` (config)
- `.github/FUNDING.yaml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/config.yml` (config)
- `.github/dependabot.yaml` (config)
- `.github/release.yml` (config)
- `.github/workflows/actions.lock` (ci)
- `.github/workflows/codeql.yaml` (ci)
- `.github/workflows/news.yaml` (ci)
- `.github/workflows/pre-release.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/scorecard.yaml` (ci)
- `.github/workflows/tests.yml` (ci)
- `.github/workflows/upgrade-release-tools.yaml` (ci)
- `.github/workflows/zizmor.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `.pre-commit-hooks.yaml` (config)
- `.readthedocs.yml` (config)
- `pylock.toml` (config)
- `pylock.zipapp.toml` (config)
- `pyproject.toml` (manifest)
- `testdata/empty_project/pyproject.toml` (manifest)
- `testdata/pipx_metadata_multiple_errors.json` (config)
- `testdata/test_package_specifier/local_completion/pyproject.toml` (manifest)
- `testdata/test_package_specifier/local_extras/pyproject.toml` (manifest)
- `testdata/test_package_specifier/local_manpage/pyproject.toml` (manifest)
- `tox.toml` (config)

## Top-level layout

- `tests` — 62 analysed file(s)
- `src` — 57 analysed file(s)
- `docs` — 45 analysed file(s)
- `testdata` — 27 analysed file(s)
- `.github` — 20 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `scripts` — 7 analysed file(s)
- `changelog.d` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `3ce2b3c742ee06b0d89d19a230e7b08043b75de9` is the revision these paths and observations refer to.
