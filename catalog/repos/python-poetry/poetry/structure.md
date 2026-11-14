# Project structure: python-poetry/poetry

**Analysed commit:** `4acc75e19f128c8340c6f977a35e53b5f7f39071`

**Commit reference:** [4acc75e19f128c8340c6f977a35e53b5f7f39071](https://github.com/python-poetry/poetry/commit/4acc75e19f128c8340c6f977a35e53b5f7f39071)

**Tree at this commit:** [python-poetry/poetry@4acc75e19f12](https://github.com/python-poetry/poetry/tree/4acc75e19f128c8340c6f977a35e53b5f7f39071)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | python-poetry/poetry |
| Description | Python packaging and dependency management made easy |
| Stars | 34323 |
| Forks | 2581 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `4acc75e19f128c8340c6f977a35e53b5f7f39071` |
| Retrieved at | 2026-11-14T19:06:59.477396+00:00 |
| Files in this snapshot | 760 |

## Directory tree

```text
.github/  (15 files)
  ISSUE_TEMPLATE/  (4 files)
    ---bug-report.yml
    ---documentation.yml
    ---feature-request.yml
    config.yml
  actions/  (2 files)
    bootstrap-poetry/  (1 files)
      … 1 files under this directory
    poetry-install/  (1 files)
      … 1 files under this directory
  scripts/  (1 files)
    backport.sh
  workflows/  (6 files)
    .tests-matrix.yaml
    backport.yaml
    docs.yaml
    lock-threads.yaml
    release.yaml
    tests.yaml
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
docs/  (16 files)
  _index.md
  basic-usage.md
  building-extension-modules.md
  cli.md
  community.md
  configuration.md
  contributing.md
  dependency-specification.md
  faq.md
  libraries.md
  managing-dependencies.md
  managing-environments.md
  plugins.md
  pre-commit-hooks.md
  pyproject.md
  repositories.md
src/  (195 files)
  poetry/  (195 files)
    config/  (6 files)
      … 6 files under this directory
    console/  (66 files)
      … 66 files under this directory
    inspection/  (3 files)
      … 3 files under this directory
    installation/  (12 files)
      … 12 files under this directory
    json/  (2 files)
      … 2 files under this directory
    layouts/  (3 files)
      … 3 files under this directory
    masonry/  (4 files)
      … 4 files under this directory
    mixology/  (10 files)
      … 10 files under this directory
    packages/  (6 files)
      … 6 files under this directory
    plugins/  (5 files)
      … 5 files under this directory
    publishing/  (4 files)
      … 4 files under this directory
    puzzle/  (5 files)
      … 5 files under this directory
    pyproject/  (2 files)
      … 2 files under this directory
    repositories/  (19 files)
      … 19 files under this directory
    toml/  (3 files)
      … 3 files under this directory
    utils/  (32 files)
      … 32 files under this directory
    vcs/  (4 files)
      … 4 files under this directory
    version/  (2 files)
      … 2 files under this directory
    __main__.py
    __version__.py
    exceptions.py
    factory.py
    locations.py
    poetry.py
    py.typed
tests/  (525 files)
  config/  (6 files)
    __init__.py
    test_config.py
    test_config_source.py
    test_dict_config_source.py
    test_file_config_source.py
    test_source.py
  console/  (69 files)
    commands/  (55 files)
      … 55 files under this directory
    logging/  (5 files)
      … 5 files under this directory
    __init__.py
    conftest.py
    test_application.py
    test_application_command_not_found.py
    test_application_global_options.py
    test_application_removed_commands.py
    test_command_loader.py
    test_exceptions_console_message.py
    test_exceptions_poetry_runtime_error.py
  fixtures/  (219 files)
    bad_scripts_project/  (6 files)
      … 6 files under this directory
    build_constraints/  (1 files)
      … 1 files under this directory
    build_constraints_empty/  (1 files)
      … 1 files under this directory
    build_system_requires_not_available/  (3 files)
      … 3 files under this directory
    build_systems/  (24 files)
      … 24 files under this directory
    deleted_directory_dependency/  (1 files)
      … 1 files under this directory
    deleted_file_dependency/  (1 files)
      … 1 files under this directory
    directory/  (6 files)
      … 6 files under this directory
    excluded_subpackage/  (5 files)
      … 5 files under this directory
    extended_project/  (4 files)
      … 4 files under this directory
    extended_project_without_setup/  (4 files)
      … 4 files under this directory
    extended_with_no_setup/  (5 files)
      … 5 files under this directory
    file_scripts_dir_ref_project/  (3 files)
      … 3 files under this directory
    file_scripts_missing_ref_project/  (2 files)
      … 2 files under this directory
    file_scripts_no_ref_field_project/  (2 files)
      … 2 files under this directory
    file_scripts_project/  (3 files)
      … 3 files under this directory
    git/  (31 files)
      … 31 files under this directory
    incompatible_lock/  (1 files)
      … 1 files under this directory
    inspection/  (13 files)
      … 13 files under this directory
    invalid_lock/  (1 files)
      … 1 files under this directory
    invalid_pyproject/  (1 files)
      … 1 files under this directory
    invalid_pyproject_dep_name/  (1 files)
      … 1 files under this directory
    missing_directory_dependency/  (1 files)
      … 1 files under this directory
    missing_extra_directory_dependency/  (1 files)
      … 1 files under this directory
    missing_file_dependency/  (1 files)
      … 1 files under this directory
    nameless_pyproject/  (1 files)
      … 1 files under this directory
    no_name_project/  (2 files)
      … 2 files under this directory
    non_package_mode/  (1 files)
      … 1 files under this directory
    old_lock/  (1 files)
      … 1 files under this directory
    old_lock_path_dependency/  (2 files)
      … 2 files under this directory
    outdated_lock/  (1 files)
      … 1 files under this directory
    private_pyproject/  (1 files)
      … 1 files under this directory
    project_plugins/  (9 files)
      … 9 files under this directory
    project_with_extras/  (2 files)
      … 2 files under this directory
    project_with_git_dev_dependency/  (1 files)
      … 1 files under this directory
    project_with_local_dependencies/  (1 files)
      … 1 files under this directory
    project_with_multi_constraints_dependency/  (2 files)
      … 2 files under this directory
    project_with_nested_local/  (4 files)
      … 4 files under this directory
    project_with_setup/  (2 files)
      … 2 files under this directory
    project_with_setup_calls_script/  (3 files)
      … 3 files under this directory
    pypi_reference/  (1 files)
      … 1 files under this directory
    sample_project/  (2 files)
      … 2 files under this directory
    scripts/  (6 files)
      … 6 files under this directory
    self_version_not_ok/  (1 files)
      … 1 files under this directory
    self_version_not_ok_invalid_config/  (1 files)
      … 1 files under this directory
    self_version_ok/  (1 files)
      … 1 files under this directory
    simple_project/  (4 files)
      … 4 files under this directory
    simple_project_legacy/  (4 files)
      … 4 files under this directory
    up_to_date_lock/  (1 files)
      … 1 files under this directory
    up_to_date_lock_non_package/  (1 files)
      … 1 files under this directory
    with-include/  (14 files)
      … 14 files under this directory
    with_conditional_path_deps/  (3 files)
      … 3 files under this directory
    with_explicit_pypi_and_other/  (1 files)
      … 1 files under this directory
    with_explicit_pypi_and_other_explicit/  (1 files)
      … 1 files under this directory
    with_explicit_pypi_no_other/  (1 files)
      … 1 files under this directory
    with_explicit_source/  (1 files)
      … 1 files under this directory
    with_local_config/  (3 files)
      … 3 files under this directory
    with_multiple_dist_dir/  (3 files)
      … 3 files under this directory
    with_multiple_readme_files/  (4 files)
      … 4 files under this directory
    with_multiple_sources/  (1 files)
      … 1 files under this directory
    with_multiple_sources_pypi/  (1 files)
      … 1 files under this directory
    with_multiple_supplemental_sources/  (1 files)
      … 1 files under this directory
    with_path_dependency/  (2 files)
      … 2 files under this directory
    with_primary_source_explicit/  (1 files)
      … 1 files under this directory
    with_primary_source_implicit/  (1 files)
      … 1 files under this directory
    with_source/  (2 files)
      … 2 files under this directory
    with_supplemental_source/  (1 files)
      … 1 files under this directory
    complete.toml
  inspection/  (3 files)
    __init__.py
    test_info.py
    test_lazy_wheel.py
  installation/  (56 files)
    fixtures/  (47 files)
      … 47 files under this directory
    __init__.py
    conftest.py
    test_chef.py
    test_chooser.py
    test_chooser_errors.py
    test_executor.py
    test_installer.py
    test_uninstaller.py
    test_wheel_installer.py
  integration/  (2 files)
    __init__.py
    test_utils_vcs_git.py
  json/  (9 files)
    fixtures/  (7 files)
      … 7 files under this directory
    __init__.py
    test_schema.py
  masonry/  (7 files)
    builders/  (7 files)
      … 7 files under this directory
  mixology/  (11 files)
    version_solver/  (8 files)
      … 8 files under this directory
    __init__.py
    helpers.py
    test_incompatibility.py
  packages/  (4 files)
    __init__.py
    test_direct_origin.py
    test_locker.py
    test_transitive_package_info.py
  plugins/  (2 files)
    __init__.py
    test_plugin_manager.py
  publishing/  (4 files)
    __init__.py
    test_hash_manager.py
    test_publisher.py
    test_uploader.py
  puzzle/  (6 files)
    __init__.py
    conftest.py
    test_provider.py
    test_solver.py
    test_solver_internals.py
    test_transaction.py
  pyproject/  (4 files)
    __init__.py
    conftest.py
    test_pyproject_toml.py
    test_pyproject_toml_file.py
  repositories/  (120 files)
    fixtures/  (118 files)
      … 118 files under this directory
    __init__.py
    conftest.py
  __init__.py
  conftest.py
  helpers.py
.gitattributes
.gitignore
.pre-commit-config.yaml
.pre-commit-hooks.yaml
CITATION.cff
CODE_OF_CONDUCT.md
LICENSE
README.md
pyproject.toml
```

## Entry points

- [src/poetry/__main__.py:6](https://github.com/python-poetry/poetry/blob/4acc75e19f128c8340c6f977a35e53b5f7f39071/src/poetry/__main__.py#L6)
- [src/poetry/console/application.py](https://github.com/python-poetry/poetry/blob/4acc75e19f128c8340c6f977a35e53b5f7f39071/src/poetry/console/application.py)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 9 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: Config, ConfigCommand, ConfigSetting, ConfigSource, ConfigSourceMigration, DictConfig… |
| Data layer | data | Observed | Groups 19 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AbstractRepository, CachedRepository, HTMLPage, HTMLPageParser, HTTPRepository, InstalledRepository. O… |
| Application entry point | entrypoint | Observed | Groups 3 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Application, RunCommand. Observed top-level functions: load_command, main. |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| poetry package | library | Observed | Groups 164 file(s) under poetry package (observed from repository paths and static analysis). Observed top-level classes: AboutCommand, AddCommand, ApplicationPlugin, ArtifactCache, Assignment, AtomicCachedProperty. Obs… |
| Tests | test | Observed | Groups 525 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: AddCommandPlugin, CheckProjectPathCommand, Chef, Config, CustomInstalledRepository, DistributionHash. Obse… |

## Important files

- `.github/ISSUE_TEMPLATE/---bug-report.yml` (config)
- `.github/ISSUE_TEMPLATE/---documentation.yml` (config)
- `.github/ISSUE_TEMPLATE/---feature-request.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/actions/bootstrap-poetry/action.yaml` (config)
- `.github/actions/poetry-install/action.yaml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/.tests-matrix.yaml` (ci)
- `.github/workflows/backport.yaml` (ci)
- `.github/workflows/docs.yaml` (ci)
- `.github/workflows/lock-threads.yaml` (ci)
- `.github/workflows/release.yaml` (ci)
- `.github/workflows/tests.yaml` (ci)
- `.pre-commit-config.yaml` (config)
- `.pre-commit-hooks.yaml` (config)
- `pyproject.toml` (manifest)
- `src/poetry/json/schemas/poetry.json` (config)

## Top-level layout

- `tests` — 525 analysed file(s)
- `src` — 195 analysed file(s)
- `docs` — 16 analysed file(s)
- `.github` — 15 analysed file(s)
- `(root files)` — 9 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 40 file(s) were skipped during inventory (13 x lockfile excluded; 27 x vendored/generated directory excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `4acc75e19f128c8340c6f977a35e53b5f7f39071` is the revision these paths and observations refer to.
