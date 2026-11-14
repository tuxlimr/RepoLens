# Project structure: fastapi/typer

**Analysed commit:** `73500169e87b4e31717d687818c5ed955b584c18`

**Commit reference:** [73500169e87b4e31717d687818c5ed955b584c18](https://github.com/fastapi/typer/commit/73500169e87b4e31717d687818c5ed955b584c18)

**Tree at this commit:** [fastapi/typer@73500169e87b](https://github.com/fastapi/typer/tree/73500169e87b4e31717d687818c5ed955b584c18)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | fastapi/typer |
| Description | Typer, build great CLIs. Easy to code. Based on Python type hints. |
| Stars | 20353 |
| Forks | 1005 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `73500169e87b4e31717d687818c5ed955b584c18` |
| Retrieved at | 2026-11-14T19:08:02.870323+00:00 |
| Files in this snapshot | 777 |

## Directory tree

```text
.github/  (20 files)
  workflows/  (16 files)
    add-to-project.yml
    build-docs.yml
    bump-pre-commit-hooks.yml
    conflict.yml
    create-draft-release.yml
    deploy-docs.yml
    guard-dependencies.yml
    issue-manager.yml
    pre-commit.yml
    prepare-release.yml
    publish.yml
    smokeshow.yml
    test-cpython-nightly.yml
    test-redistribute.yml
    test.yml
    zizmor.yml
  dependabot.yml
  latest-changes.yml
  pr-push.yml
  pr-submit.yml
docs/  (88 files)
  about/  (1 files)
    index.md
  css/  (2 files)
    custom.css
    termynal.css
  img/  (7 files)
    logo-margin/  (4 files)
      … 4 files under this directory
    github-social-preview.svg
    icon-square.svg
    icon.svg
  js/  (2 files)
    custom.js
    termynal.js
  overrides/  (1 files)
    main.html
  reference/  (6 files)
    context.md
    file_objects.md
    index.md
    parameters.md
    run_launch.md
    typer.md
  resources/  (1 files)
    index.md
  tutorial/  (58 files)
    arguments/  (6 files)
      … 6 files under this directory
    commands/  (8 files)
      … 8 files under this directory
    multiple-values/  (4 files)
      … 4 files under this directory
    options/  (8 files)
      … 8 files under this directory
    parameter-types/  (9 files)
      … 9 files under this directory
    subcommands/  (6 files)
      … 6 files under this directory
    app-dir.md
    click.md
    exceptions.md
    first-steps.md
    index.md
    install.md
    launch.md
    one-file-per-command.md
    options-autocompletion.md
    package.md
    printing.md
    progressbar.md
    prompt.md
    terminating.md
    testing.md
    typer-app.md
    typer-command.md
  ai-development.md
  alternatives.md
  contributing.md
  environment-variables.md
  features.md
  help-typer.md
  index.md
  management.md
  release-notes.md
  virtual-environments.md
docs_src/  (304 files)
  app_dir/  (2 files)
    __init__.py
    tutorial001.py
  arguments/  (38 files)
    default/  (5 files)
      … 5 files under this directory
    envvar/  (7 files)
      … 7 files under this directory
    help/  (17 files)
      … 17 files under this directory
    optional/  (8 files)
      … 8 files under this directory
    __init__.py
  commands/  (39 files)
    arguments/  (2 files)
      … 2 files under this directory
    callback/  (5 files)
      … 5 files under this directory
    context/  (5 files)
      … 5 files under this directory
    help/  (13 files)
      … 13 files under this directory
    index/  (5 files)
      … 5 files under this directory
    name/  (2 files)
      … 2 files under this directory
    one_or_multiple/  (3 files)
      … 3 files under this directory
    options/  (3 files)
      … 3 files under this directory
    __init__.py
  exceptions/  (5 files)
    __init__.py
    tutorial001.py
    tutorial002.py
    tutorial003.py
    tutorial004.py
  first_steps/  (7 files)
    __init__.py
    tutorial001.py
    tutorial002.py
    tutorial003.py
    tutorial004.py
    tutorial005.py
    tutorial006.py
  launch/  (3 files)
    __init__.py
    tutorial001.py
    tutorial002.py
  multiple_values/  (13 files)
    arguments_with_multiple_values/  (4 files)
      … 4 files under this directory
    multiple_options/  (5 files)
      … 5 files under this directory
    options_with_multiple_values/  (3 files)
      … 3 files under this directory
    __init__.py
  one_file_per_command/  (7 files)
    app/  (6 files)
      … 6 files under this directory
    __init__.py
  options/  (53 files)
    callback/  (9 files)
      … 9 files under this directory
    help/  (9 files)
      … 9 files under this directory
    name/  (11 files)
      … 11 files under this directory
    password/  (5 files)
      … 5 files under this directory
    prompt/  (7 files)
      … 7 files under this directory
    required/  (4 files)
      … 4 files under this directory
    version/  (7 files)
      … 7 files under this directory
    __init__.py
  options_autocompletion/  (19 files)
    __init__.py
    tutorial001.py
    tutorial001_non_an.py
    tutorial002.py
    tutorial002_non_an.py
    tutorial003.py
    tutorial003_non_an.py
    tutorial004.py
    tutorial004_non_an.py
    tutorial005.py
    tutorial005_non_an.py
    tutorial006.py
    tutorial006_non_an.py
    tutorial007.py
    tutorial007_non_an.py
    tutorial008.py
    tutorial008_non_an.py
    tutorial009.py
    tutorial009_non_an.py
  parameter_types/  (52 files)
    bool/  (9 files)
      … 9 files under this directory
    custom_types/  (3 files)
      … 3 files under this directory
    datetime/  (4 files)
      … 4 files under this directory
    enum/  (8 files)
      … 8 files under this directory
    file/  (11 files)
      … 11 files under this directory
    index/  (2 files)
      … 2 files under this directory
    number/  (7 files)
      … 7 files under this directory
    path/  (5 files)
      … 5 files under this directory
    uuid/  (2 files)
      … 2 files under this directory
    __init__.py
  printing/  (7 files)
    __init__.py
    tutorial001.py
    tutorial002.py
    tutorial003.py
    tutorial004.py
    tutorial005.py
    tutorial006.py
  progressbar/  (7 files)
    __init__.py
    tutorial001.py
    tutorial002.py
    tutorial003.py
    tutorial004.py
    tutorial005.py
    tutorial006.py
  prompt/  (5 files)
    __init__.py
    tutorial001.py
    tutorial002.py
    tutorial003.py
    tutorial004.py
  subcommands/  (28 files)
    callback_override/  (5 files)
      … 5 files under this directory
    name_help/  (9 files)
      … 9 files under this directory
    tutorial001/  (4 files)
      … 4 files under this directory
    tutorial002/  (2 files)
      … 2 files under this directory
    tutorial003/  (7 files)
      … 7 files under this directory
    __init__.py
  terminating/  (4 files)
    __init__.py
    tutorial001.py
    tutorial002.py
    tutorial003.py
  testing/  (13 files)
    app01/  (3 files)
      … 3 files under this directory
    app02/  (3 files)
      … 3 files under this directory
    app02_non_an/  (3 files)
      … 3 files under this directory
    app03/  (3 files)
      … 3 files under this directory
    __init__.py
  typer_app/  (2 files)
    __init__.py
    tutorial001.py
includes/  (1 files)
  agent-banner.md
scripts/  (13 files)
  docker/  (2 files)
    Dockerfile
    compose.yaml
  add_latest_release_date.py
  agent_banner.py
  deploy_docs_status.py
  docs.py
  format.sh
  get-pwsh-activate.sh
  lint.sh
  prepare_release.py
  test-cov-html.sh
  test-files.sh
  test.sh
tests/  (304 files)
  assets/  (29 files)
    cli/  (17 files)
      … 17 files under this directory
    __init__.py
    completion_argument.py
    completion_no_types.py
    completion_no_types_order.py
    hidden_commands.py
    hidden_option.py
    print_modules.py
    prog_name.py
    type_error_no_rich.py
    type_error_no_rich_short_disable.py
    type_error_normal_traceback.py
    type_error_rich.py
  test_cli/  (20 files)
    __init__.py
    test_app_other_name.py
    test_completion_run.py
    test_doc.py
    test_empty_script.py
    test_extending_app.py
    test_extending_empty_app.py
    test_func_other_name.py
    test_help.py
    test_multi_app.py
    test_multi_app_cli.py
    test_multi_app_sub.py
    test_multi_func.py
    test_not_python.py
    test_parser.py
    test_program_name.py
    test_sub.py
    test_sub_completion.py
    test_sub_help.py
    test_version.py
  test_completion/  (20 files)
    __init__.py
    choice_case_insensitive_example.py
    choice_example.py
    colon_example.py
    completion_option_then_argument.py
    example_rich_tags.py
    file_example.py
    path_example.py
    test_completion.py
    test_completion_choice.py
    test_completion_choice_no_case.py
    test_completion_complete.py
    test_completion_complete_no_help.py
    test_completion_complete_rich.py
    test_completion_file.py
    test_completion_install.py
    test_completion_option_colon.py
    test_completion_path.py
    test_completion_show.py
    test_sanitization.py
  test_tutorial/  (203 files)
    test_app_dir/  (2 files)
      … 2 files under this directory
    test_arguments/  (22 files)
      … 22 files under this directory
    test_commands/  (34 files)
      … 34 files under this directory
    test_exceptions/  (5 files)
      … 5 files under this directory
    test_first_steps/  (7 files)
      … 7 files under this directory
    test_launch/  (2 files)
      … 2 files under this directory
    test_multiple_values/  (9 files)
      … 9 files under this directory
    test_one_file_per_command/  (2 files)
      … 2 files under this directory
    test_options/  (30 files)
      … 30 files under this directory
    test_options_autocompletion/  (9 files)
      … 9 files under this directory
    test_parameter_types/  (33 files)
      … 33 files under this directory
    test_printing/  (7 files)
      … 7 files under this directory
    test_progressbar/  (7 files)
      … 7 files under this directory
    test_prompt/  (5 files)
      … 5 files under this directory
    test_subcommands/  (18 files)
      … 18 files under this directory
    test_terminating/  (4 files)
      … 4 files under this directory
    test_testing/  (4 files)
      … 4 files under this directory
    test_typer_app/  (2 files)
      … 2 files under this directory
    __init__.py
  __init__.py
  atomic_write_example.py
  conftest.py
  test_ambiguous_params.py
  test_annotated.py
  test_atomic_file.py
  test_callback_warning.py
  test_coercion.py
  test_core.py
  test_deprecation.py
  test_docs_cleanup.py
  test_exit_errors.py
  test_future_annotations.py
  test_hidden.py
  test_launch.py
  test_others.py
  test_param_meta_empty.py
  test_prepare_release.py
  test_prog_name.py
  test_progress_bar.py
  test_rich_import.py
  test_rich_markup_mode.py
  test_rich_utils.py
  test_suggest_commands.py
  … 8 more files
typer/  (38 files)
  .agents/  (1 files)
    skills/  (1 files)
      … 1 files under this directory
  _click/  (16 files)
    LICENSE.txt
    __init__.py
    _compat.py
    _termui_impl.py
    _textwrap.py
    _winconsole.py
    core.py
    decorators.py
    exceptions.py
    formatting.py
    globals.py
    parser.py
    py.typed
    shell_completion.py
    termui.py
    utils.py
  __init__.py
  __main__.py
  _adapters.py
  _coercion.py
  _completion_classes.py
  _completion_shared.py
  _display.py
  _param_types.py
  _typing.py
  cli.py
  colors.py
  completion.py
  core.py
  exceptions.py
  main.py
  models.py
  params.py
  py.typed
  rich_utils.py
  testing.py
  utils.py
.gitignore
.pre-commit-config.yaml
.python-version
CITATION.cff
LICENSE
README.md
mkdocs.env.yml
mkdocs.yml
pyproject.toml
```

## Entry points

- [docs_src/app_dir/tutorial001.py:7](https://github.com/fastapi/typer/blob/73500169e87b4e31717d687818c5ed955b584c18/docs_src/app_dir/tutorial001.py#L7)
- [docs_src/arguments/default/tutorial001.py:5](https://github.com/fastapi/typer/blob/73500169e87b4e31717d687818c5ed955b584c18/docs_src/arguments/default/tutorial001.py#L5)
- [docs_src/arguments/default/tutorial001_non_an.py:3](https://github.com/fastapi/typer/blob/73500169e87b4e31717d687818c5ed955b584c18/docs_src/arguments/default/tutorial001_non_an.py#L3)
- [docs_src/arguments/default/tutorial002.py:6](https://github.com/fastapi/typer/blob/73500169e87b4e31717d687818c5ed955b584c18/docs_src/arguments/default/tutorial002.py#L6)
- [docs_src/arguments/default/tutorial002_non_an.py:5](https://github.com/fastapi/typer/blob/73500169e87b4e31717d687818c5ed955b584c18/docs_src/arguments/default/tutorial002_non_an.py#L5)
- [docs_src/arguments/envvar/tutorial001.py:5](https://github.com/fastapi/typer/blob/73500169e87b4e31717d687818c5ed955b584c18/docs_src/arguments/envvar/tutorial001.py#L5)
- [docs_src/arguments/envvar/tutorial001_non_an.py:3](https://github.com/fastapi/typer/blob/73500169e87b4e31717d687818c5ed955b584c18/docs_src/arguments/envvar/tutorial001_non_an.py#L3)
- [docs_src/arguments/envvar/tutorial002.py:5](https://github.com/fastapi/typer/blob/73500169e87b4e31717d687818c5ed955b584c18/docs_src/arguments/envvar/tutorial002.py#L5)
- [docs_src/arguments/envvar/tutorial002_non_an.py:3](https://github.com/fastapi/typer/blob/73500169e87b4e31717d687818c5ed955b584c18/docs_src/arguments/envvar/tutorial002_non_an.py#L3)
- [docs_src/arguments/envvar/tutorial003.py:5](https://github.com/fastapi/typer/blob/73500169e87b4e31717d687818c5ed955b584c18/docs_src/arguments/envvar/tutorial003.py#L5)
- [docs_src/arguments/envvar/tutorial003_non_an.py:3](https://github.com/fastapi/typer/blob/73500169e87b4e31717d687818c5ed955b584c18/docs_src/arguments/envvar/tutorial003_non_an.py#L3)
- [docs_src/arguments/help/tutorial001.py:5](https://github.com/fastapi/typer/blob/73500169e87b4e31717d687818c5ed955b584c18/docs_src/arguments/help/tutorial001.py#L5)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: ArgumentInfo, CallbackParam, CommandInfo, Context, DefaultPlaceholder, DeveloperExceptionConfig. Observ… |
| docs_src package | library | Observed | Groups 59 file(s) under docs_src package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 248 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Typer. Observed top-level classes: CustomClass, Food, LinkData, NeuralNetwor… |
| scripts package | library | Observed | Groups 7 file(s) under scripts package (observed from repository paths and static analysis). Observed top-level classes: AgentBannerExtension, AgentBannerPreprocessor. Observed top-level functions: makeExtension. |
| Tests | test | Observed | Groups 308 file(s) under tests (observed from repository paths and static analysis). Observed application object created via Typer. Observed top-level classes: SomeEnum, User. Observed top-level functions: _capture_writ… |
| typer package | library | Observed | Groups 30 file(s) under typer package (observed from repository paths and static analysis). Observed top-level classes: Abort, AdapterRuntimeParam, AnnotatedParamWithDefaultValueError, BadArgumentUsage, BadOptionUsage,… |

## Important files

- `.github/dependabot.yml` (config)
- `.github/latest-changes.yml` (config)
- `.github/pr-push.yml` (config)
- `.github/pr-submit.yml` (config)
- `.github/workflows/add-to-project.yml` (ci)
- `.github/workflows/build-docs.yml` (ci)
- `.github/workflows/bump-pre-commit-hooks.yml` (ci)
- `.github/workflows/conflict.yml` (ci)
- `.github/workflows/create-draft-release.yml` (ci)
- `.github/workflows/deploy-docs.yml` (ci)
- `.github/workflows/guard-dependencies.yml` (ci)
- `.github/workflows/issue-manager.yml` (ci)
- `.github/workflows/pre-commit.yml` (ci)
- `.github/workflows/prepare-release.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.github/workflows/smokeshow.yml` (ci)
- `.github/workflows/test-cpython-nightly.yml` (ci)
- `.github/workflows/test-redistribute.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `.github/workflows/zizmor.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `mkdocs.env.yml` (config)
- `mkdocs.yml` (config)
- `pyproject.toml` (manifest)
- `scripts/docker/Dockerfile` (container)
- `scripts/docker/compose.yaml` (container)

## Top-level layout

- `docs_src` — 304 analysed file(s)
- `tests` — 304 analysed file(s)
- `docs` — 88 analysed file(s)
- `typer` — 38 analysed file(s)
- `.github` — 20 analysed file(s)
- `scripts` — 13 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `includes` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `73500169e87b4e31717d687818c5ed955b584c18` is the revision these paths and observations refer to.
