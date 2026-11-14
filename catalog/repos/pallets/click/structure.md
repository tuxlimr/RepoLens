# Project structure: pallets/click

**Analysed commit:** `e38188e9e205005d5af5f9e59df51904c984586a`

**Commit reference:** [e38188e9e205005d5af5f9e59df51904c984586a](https://github.com/pallets/click/commit/e38188e9e205005d5af5f9e59df51904c984586a)

**Tree at this commit:** [pallets/click@e38188e9e205](https://github.com/pallets/click/tree/e38188e9e205005d5af5f9e59df51904c984586a)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | pallets/click |
| Description | Python composable command line interface toolkit |
| Stars | 16000 |
| Forks | 1400 |
| Licence | BSD-3-Clause |
| Language | Python |
| Default branch | main |
| Analysed commit | `e38188e9e205005d5af5f9e59df51904c984586a` |
| Retrieved at | 2026-11-14T19:02:12.841719+00:00 |
| Files in this snapshot | 176 |

## Directory tree

```text
.devcontainer/  (2 files)
  devcontainer.json
  on-create-command.sh
.github/  (10 files)
  ISSUE_TEMPLATE/  (3 files)
    bug-report.md
    config.yml
    feature-request.md
  workflows/  (6 files)
    lock.yaml
    nightly.yaml
    pre-commit.yaml
    publish.yaml
    tests.yaml
    zizmor.yaml
  pull_request_template.md
docs/  (42 files)
  _static/  (3 files)
    click-icon.svg
    click-logo.svg
    click-name.svg
  advanced.md
  api.md
  arguments.md
  changes.md
  click-concepts.md
  command-line-reference.md
  commands-and-groups.md
  commands.md
  complex.md
  conf.py
  contrib.md
  contributing.md
  design-opinions.md
  documentation.md
  entry-points.md
  exceptions.md
  extending-click.md
  faqs.md
  handling-files.md
  index.md
  license.md
  option-decorators.md
  options.md
  parameter-types.md
  … 15 more files
examples/  (37 files)
  aliases/  (4 files)
    README
    aliases.ini
    aliases.py
    pyproject.toml
  colors/  (3 files)
    README
    colors.py
    pyproject.toml
  completion/  (3 files)
    README
    completion.py
    pyproject.toml
  complex/  (7 files)
    complex/  (5 files)
      … 5 files under this directory
    README
    pyproject.toml
  imagepipe/  (4 files)
    .gitignore
    README
    imagepipe.py
    pyproject.toml
  inout/  (3 files)
    README
    inout.py
    pyproject.toml
  naval/  (3 files)
    README
    naval.py
    pyproject.toml
  repo/  (3 files)
    README
    pyproject.toml
    repo.py
  termui/  (3 files)
    README
    pyproject.toml
    termui.py
  validation/  (3 files)
    README
    pyproject.toml
    validation.py
  README
src/  (18 files)
  click/  (18 files)
    __init__.py
    _compat.py
    _termui_impl.py
    _textwrap.py
    _utils.py
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
    testing.py
    types.py
    utils.py
tests/  (59 files)
  test_exceptions/  (2 files)
    __init__.py
    test_FileError.py
  test_types/  (9 files)
    __init__.py
    test_Choice.py
    test_File.py
    test_FloatRange.py
    test_FuncParamType.py
    test_IntRange.py
    test_ParamType.py
    test_Path.py
    test_convert_type.py
  test_utils/  (14 files)
    __init__.py
    test_KeepOpenFile.py
    test_LazyFile.py
    test__detect_program_name.py
    test__expand_args.py
    test_confirm.py
    test_echo.py
    test_echo_via_pager.py
    test_format_filename.py
    test_make_default_short_help.py
    test_open_file.py
    test_prompt.py
    test_sentinel.py
    test_style.py
  typing/  (12 files)
    typing_aliased_group.py
    typing_confirmation_option.py
    typing_edit.py
    typing_group_kw_options.py
    typing_help_option.py
    typing_options.py
    typing_password_option.py
    typing_path.py
    typing_progressbar.py
    typing_prompt.py
    typing_simple_example.py
    typing_version_option.py
  conftest.py
  test_abort_interrupt.py
  test_arguments.py
  test_basic.py
  test_chain.py
  test_command_decorators.py
  test_commands.py
  test_compat.py
  test_context.py
  test_custom_classes.py
  test_defaults.py
  test_deprecations.py
  test_formatting.py
  test_imports.py
  test_info_dict.py
  test_normalization.py
  test_options.py
  test_parser.py
  test_shell_completion.py
  test_stream_lifecycle.py
  test_termui.py
  test_testing.py
.editorconfig
.gitignore
.pre-commit-config.yaml
.readthedocs.yaml
CHANGES.md
LICENSE.txt
README.md
pyproject.toml
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| click package | library | Observed | Groups 17 file(s) under click package (observed from repository paths and static analysis). Observed top-level classes: Abort, Argument, BadArgumentUsage, BadOptionUsage, BadParameter, BashComplete. Observed top-level f… |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 59 file(s) under tests (observed from repository paths and static analysis). Observed application object created via Command, Group. Observed top-level classes: AliasedGroup, Class1, Class2, Color, ColorInt, Doub… |

## Important files

- `.devcontainer/devcontainer.json` (config)
- `.editorconfig` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/lock.yaml` (ci)
- `.github/workflows/nightly.yaml` (ci)
- `.github/workflows/pre-commit.yaml` (ci)
- `.github/workflows/publish.yaml` (ci)
- `.github/workflows/tests.yaml` (ci)
- `.github/workflows/zizmor.yaml` (ci)
- `.pre-commit-config.yaml` (config)
- `.readthedocs.yaml` (config)
- `examples/aliases/aliases.ini` (config)
- `examples/aliases/pyproject.toml` (manifest)
- `examples/colors/pyproject.toml` (manifest)
- `examples/completion/pyproject.toml` (manifest)
- `examples/complex/pyproject.toml` (manifest)
- `examples/imagepipe/pyproject.toml` (manifest)
- `examples/inout/pyproject.toml` (manifest)
- `examples/naval/pyproject.toml` (manifest)
- `examples/repo/pyproject.toml` (manifest)
- `examples/termui/pyproject.toml` (manifest)
- `examples/validation/pyproject.toml` (manifest)
- `pyproject.toml` (manifest)

## Top-level layout

- `tests` — 59 analysed file(s)
- `docs` — 42 analysed file(s)
- `examples` — 37 analysed file(s)
- `src` — 18 analysed file(s)
- `.github` — 10 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `.devcontainer` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `e38188e9e205005d5af5f9e59df51904c984586a` is the revision these paths and observations refer to.
