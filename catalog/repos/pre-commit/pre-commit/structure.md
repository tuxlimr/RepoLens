# Project structure: pre-commit/pre-commit

**Analysed commit:** `ba5c4209a6d561b0dff5db24620778d2133d068e`

**Commit reference:** [ba5c4209a6d561b0dff5db24620778d2133d068e](https://github.com/pre-commit/pre-commit/commit/ba5c4209a6d561b0dff5db24620778d2133d068e)

**Tree at this commit:** [pre-commit/pre-commit@ba5c4209a6d5](https://github.com/pre-commit/pre-commit/tree/ba5c4209a6d561b0dff5db24620778d2133d068e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | pre-commit/pre-commit |
| Description | A framework for managing and maintaining multi-language pre-commit hooks. |
| Stars | 15696 |
| Forks | 1019 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `ba5c4209a6d561b0dff5db24620778d2133d068e` |
| Retrieved at | 2026-11-14T19:08:59.330982+00:00 |
| Files in this snapshot | 197 |

## Directory tree

```text
.github/  (6 files)
  ISSUE_TEMPLATE/  (3 files)
    00_bug.yaml
    01_feature.yaml
    config.yml
  actions/  (1 files)
    pre-test/  (1 files)
      … 1 files under this directory
  workflows/  (2 files)
    languages.yaml
    main.yml
pre_commit/  (80 files)
  commands/  (14 files)
    __init__.py
    autoupdate.py
    clean.py
    gc.py
    hazmat.py
    hook_impl.py
    init_templatedir.py
    install_uninstall.py
    migrate_config.py
    run.py
    sample_config.py
    try_repo.py
    validate_config.py
    validate_manifest.py
  languages/  (22 files)
    __init__.py
    conda.py
    coursier.py
    dart.py
    docker.py
    docker_image.py
    dotnet.py
    fail.py
    golang.py
    haskell.py
    julia.py
    lua.py
    node.py
    perl.py
    pygrep.py
    python.py
    r.py
    ruby.py
    rust.py
    swift.py
    unsupported.py
    unsupported_script.py
  meta_hooks/  (4 files)
    __init__.py
    check_hooks_apply.py
    check_useless_excludes.py
    identity.py
  resources/  (15 files)
    __init__.py
    empty_template_Cargo.toml
    empty_template_LICENSE.renv
    empty_template_Makefile.PL
    empty_template_activate.R
    empty_template_environment.yml
    empty_template_go.mod
    empty_template_main.go
    empty_template_main.rs
    empty_template_pre-commit-package-dev-1.rockspec
    empty_template_pre_commit_placeholder_package.gemspec
    empty_template_pubspec.yaml
    empty_template_renv.lock
    empty_template_setup.py
    hook-tmpl
  __init__.py
  __main__.py
  all_languages.py
  clientlib.py
  color.py
  constants.py
  envcontext.py
  error_handler.py
  errors.py
  file_lock.py
  git.py
  hook.py
  lang_base.py
  logging_handler.py
  main.py
  output.py
  parse_shebang.py
  prefix.py
  repository.py
  staged_files_only.py
  store.py
  util.py
  xargs.py
  yaml.py
  … 1 more files
testing/  (41 files)
  resources/  (28 files)
    arbitrary_bytes_repo/  (2 files)
      … 2 files under this directory
    arg_per_line_hooks_repo/  (2 files)
      … 2 files under this directory
    exclude_types_repo/  (2 files)
      … 2 files under this directory
    failing_hook_repo/  (2 files)
      … 2 files under this directory
    logfile_repo/  (2 files)
      … 2 files under this directory
    modified_file_returns_zero_repo/  (4 files)
      … 4 files under this directory
    not_found_exe/  (1 files)
      … 1 files under this directory
    prints_cwd_repo/  (1 files)
      … 1 files under this directory
    python_hooks_repo/  (3 files)
      … 3 files under this directory
    script_hooks_repo/  (2 files)
      … 2 files under this directory
    stdout_stderr_repo/  (3 files)
      … 3 files under this directory
    types_or_repo/  (2 files)
      … 2 files under this directory
    types_repo/  (2 files)
      … 2 files under this directory
  zipapp/  (4 files)
    Dockerfile
    entry
    make
    python
  __init__.py
  auto_namedtuple.py
  fixtures.py
  get-coursier.sh
  get-dart.sh
  language_helpers.py
  languages
  make-archives
  util.py
tests/  (59 files)
  commands/  (14 files)
    __init__.py
    autoupdate_test.py
    clean_test.py
    gc_test.py
    hazmat_test.py
    hook_impl_test.py
    init_templatedir_test.py
    install_uninstall_test.py
    migrate_config_test.py
    run_test.py
    sample_config_test.py
    try_repo_test.py
    validate_config_test.py
    validate_manifest_test.py
  languages/  (22 files)
    __init__.py
    conda_test.py
    coursier_test.py
    dart_test.py
    docker_image_test.py
    docker_test.py
    dotnet_test.py
    fail_test.py
    golang_test.py
    haskell_test.py
    julia_test.py
    lua_test.py
    node_test.py
    perl_test.py
    pygrep_test.py
    python_test.py
    r_test.py
    ruby_test.py
    rust_test.py
    swift_test.py
    unsupported_script_test.py
    unsupported_test.py
  meta_hooks/  (4 files)
    __init__.py
    check_hooks_apply_test.py
    check_useless_excludes_test.py
    identity_test.py
  __init__.py
  clientlib_test.py
  color_test.py
  conftest.py
  envcontext_test.py
  error_handler_test.py
  git_test.py
  lang_base_test.py
  logging_handler_test.py
  main_test.py
  output_test.py
  parse_shebang_test.py
  prefix_test.py
  repository_test.py
  staged_files_only_test.py
  store_test.py
  util_test.py
  xargs_test.py
  yaml_rewrite_test.py
.gitignore
.pre-commit-config.yaml
.pre-commit-hooks.yaml
CHANGELOG.md
CONTRIBUTING.md
LICENSE
README.md
requirements-dev.txt
setup.cfg
setup.py
tox.ini
```

## Entry points

- [pre_commit/__main__.py:6](https://github.com/pre-commit/pre-commit/blob/ba5c4209a6d561b0dff5db24620778d2133d068e/pre_commit/__main__.py#L6)
- [pre_commit/commands/hazmat.py:94](https://github.com/pre-commit/pre-commit/blob/ba5c4209a6d561b0dff5db24620778d2133d068e/pre_commit/commands/hazmat.py#L94)
- [pre_commit/languages/pygrep.py:132](https://github.com/pre-commit/pre-commit/blob/ba5c4209a6d561b0dff5db24620778d2133d068e/pre_commit/languages/pygrep.py#L132)
- [pre_commit/main.py:453](https://github.com/pre-commit/pre-commit/blob/ba5c4209a6d561b0dff5db24620778d2133d068e/pre_commit/main.py#L453)
- [pre_commit/meta_hooks/check_hooks_apply.py:42](https://github.com/pre-commit/pre-commit/blob/ba5c4209a6d561b0dff5db24620778d2133d068e/pre_commit/meta_hooks/check_hooks_apply.py#L42)
- [pre_commit/meta_hooks/check_useless_excludes.py:82](https://github.com/pre-commit/pre-commit/blob/ba5c4209a6d561b0dff5db24620778d2133d068e/pre_commit/meta_hooks/check_useless_excludes.py#L82)
- [pre_commit/meta_hooks/identity.py:16](https://github.com/pre-commit/pre-commit/blob/ba5c4209a6d561b0dff5db24620778d2133d068e/pre_commit/meta_hooks/identity.py#L16)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 22 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 8 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Choice, Classifier. Observed top-level functions: _add_config_option, _add_hook_type_optio… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| pre_commit package | library | Observed | Groups 61 file(s) under pre_commit package (observed from repository paths and static analysis). Observed top-level classes: ArgumentTooLongError, CalledProcessError, DeprecatedDefaultStagesWarning, DeprecatedStagesWarn… |
| testing package | library | Observed | Groups 19 file(s) under testing package (observed from repository paths and static analysis). Observed top-level functions: add_config_to_repo, auto_namedtuple, cmd_output_mocked_pre_commit_home, copy_tree_to_path, get_… |
| Tests | test | Observed | Groups 59 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: Fixture. Observed top-level functions: _add_test_file, _args, _avoid_cache, _config_count, _create_repo_wit… |

## Important files

- `.github/ISSUE_TEMPLATE/00_bug.yaml` (config)
- `.github/ISSUE_TEMPLATE/01_feature.yaml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/actions/pre-test/action.yml` (config)
- `.github/workflows/languages.yaml` (ci)
- `.github/workflows/main.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `.pre-commit-hooks.yaml` (config)
- `pre_commit/resources/empty_template_Cargo.toml` (config)
- `pre_commit/resources/empty_template_environment.yml` (config)
- `pre_commit/resources/empty_template_pubspec.yaml` (config)
- `requirements-dev.txt` (manifest)
- `setup.cfg` (manifest)
- `setup.py` (manifest)
- `testing/resources/arbitrary_bytes_repo/.pre-commit-hooks.yaml` (config)
- `testing/resources/arg_per_line_hooks_repo/.pre-commit-hooks.yaml` (config)
- `testing/resources/exclude_types_repo/.pre-commit-hooks.yaml` (config)
- `testing/resources/failing_hook_repo/.pre-commit-hooks.yaml` (config)
- `testing/resources/logfile_repo/.pre-commit-hooks.yaml` (config)
- `testing/resources/modified_file_returns_zero_repo/.pre-commit-hooks.yaml` (config)
- `testing/resources/not_found_exe/.pre-commit-hooks.yaml` (config)
- `testing/resources/prints_cwd_repo/.pre-commit-hooks.yaml` (config)
- `testing/resources/python_hooks_repo/.pre-commit-hooks.yaml` (config)
- `testing/resources/python_hooks_repo/setup.py` (manifest)
- `testing/resources/script_hooks_repo/.pre-commit-hooks.yaml` (config)
- `testing/resources/stdout_stderr_repo/.pre-commit-hooks.yaml` (config)
- `testing/resources/types_or_repo/.pre-commit-hooks.yaml` (config)
- `testing/resources/types_repo/.pre-commit-hooks.yaml` (config)
- `testing/zipapp/Dockerfile` (container)
- `tox.ini` (config)

## Top-level layout

- `pre_commit` — 80 analysed file(s)
- `tests` — 59 analysed file(s)
- `testing` — 41 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `.github` — 6 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `ba5c4209a6d561b0dff5db24620778d2133d068e` is the revision these paths and observations refer to.
