# Project structure: chriskiehl/Gooey

**Analysed commit:** `c541920465c7bcaaefa47a15a858eb477d2666fd`

**Commit reference:** [c541920465c7bcaaefa47a15a858eb477d2666fd](https://github.com/chriskiehl/Gooey/commit/c541920465c7bcaaefa47a15a858eb477d2666fd)

**Tree at this commit:** [chriskiehl/Gooey@c541920465c7](https://github.com/chriskiehl/Gooey/tree/c541920465c7bcaaefa47a15a858eb477d2666fd)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | chriskiehl/Gooey |
| Description | Turn (almost) any Python command line program into a full GUI application with one line |
| Stars | 21897 |
| Forks | 1048 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `c541920465c7bcaaefa47a15a858eb477d2666fd` |
| Retrieved at | 2026-11-14T19:07:56.655521+00:00 |
| Files in this snapshot | 221 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    block-pr-to-master.yml
docs/  (19 files)
  packaging/  (4 files)
    Packaging-Custom-Images.md
    Packaging-Gooey.md
    build-osx.spec
    build-win.spec
  releases/  (11 files)
    1.0.3-release-notes.md
    1.0.4-release-notes.md
    1.0.5-release-notes.md
    1.0.6-release-notes.md
    1.0.7-release-notes.md
    1.0.8-release-notes.md
    1.0.8.1-release-notes.md
    1.0.8.2-release-notes.md
    1.2.0-ALPHA-release-notes.md
    pypi-distribution.md
    release-checklist.md
  Gooey-Options.md
  Gracefully-Stopping.md
  Using-Richtext-Controls.md
  pull_request_template.md
gooey/  (190 files)
  gui/  (76 files)
    application/  (3 files)
      … 3 files under this directory
    components/  (44 files)
      … 44 files under this directory
    containers/  (2 files)
      … 2 files under this directory
    lang/  (3 files)
      … 3 files under this directory
    util/  (8 files)
      … 8 files under this directory
    __init__.py
    bootstrap.py
    cli.py
    constants.py
    events.py
    formatters.py
    host.py
    image_repository.py
    imageutil.py
    processor.py
    pubsub.py
    seeder.py
    state.py
    three_to_four.py
    validation.py
    validators.py
  images/  (1 files)
    __init__.py
  languages/  (26 files)
    Hindi.json
    __init__.py
    bengali.json
    bosnian.json
    chinese.json
    croatian.json
    czech.json
    dutch.json
    english.json
    french.json
    german.json
    greek.json
    hebrew.json
    italian.json
    japanese.json
    korean.json
    polish.json
    portuguese.json
    russian.json
    serbian.json
    spanish.json
    tamil.json
    traditional-chinese.json
    turkish.json
    … 2 more files
  python_bindings/  (17 files)
    parser/  (1 files)
      … 1 files under this directory
    __init__.py
    argparse_to_json.py
    cmd_args.py
    coms.py
    config_generator.py
    constants.py
    constraints.py
    control.py
    dynamics.py
    gooey_decorator.py
    gooey_parser.py
    parameters.py
    parser_exceptions.py
    schema.py
    signal_support.py
    types.py
  tests/  (66 files)
    dynamics/  (8 files)
      … 8 files under this directory
    integration/  (13 files)
      … 13 files under this directory
    processor/  (6 files)
      … 6 files under this directory
    __init__.py
    all_widgets.py
    all_widgets_subparser.py
    auto_start.py
    gooey_config__autostart.json
    gooey_config__normal.json
    gooey_config__subparser.json
    gooey_config__validation.json
    harness.py
    test_application.py
    test_argparse_to_json.py
    test_checkbox.py
    test_chooser_results.py
    test_cli.py
    test_cmd_args.py
    test_common.py
    test_config_generator.py
    test_constraints.py
    test_control.py
    test_counter.py
    test_decoration.py
    test_dropdown.py
    test_filterable_dropdown.py
    test_filtering.py
    … 15 more files
  util/  (2 files)
    __init__.py
    functional.py
  __init__.py
  __main__.py
.gitignore
.gitmodules
CONTRIBUTING.md
ISSUE_TEMPLATE.md
LICENSE.txt
MANIFEST.in
README.md
TODO.md
pip_deploy.py
requirements.txt
setup.py
```

## Entry points

- [gooey/gui/components/options/validators.py:176](https://github.com/chriskiehl/Gooey/blob/c541920465c7bcaaefa47a15a858eb477d2666fd/gooey/gui/components/options/validators.py#L176)
- [gooey/gui/imageutil.py:33](https://github.com/chriskiehl/Gooey/blob/c541920465c7bcaaefa47a15a858eb477d2666fd/gooey/gui/imageutil.py#L33)
- [gooey/python_bindings/parser_exceptions.py:18](https://github.com/chriskiehl/Gooey/blob/c541920465c7bcaaefa47a15a858eb477d2666fd/gooey/python_bindings/parser_exceptions.py#L18)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 29 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: ConfigPage, TabbedConfigPage. |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 5 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: ArgumentError, ParserError, SuperBool. Observed top-level functions: buildCliString, build… |
| gooey package | library | Observed | Groups 90 file(s) under gooey package (observed from repository paths and static analysis). Observed top-level classes: AutoWrappedStaticText, BaseChooser, BaseDialog, BaseWidget, BasicField, BasicTextConsole. Observed… |
| Service / domain layer | service | Observed | Groups 3 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: Chooser, ColourChooser, DateChooser, DirChooser, FileChooser, FileSaver. Observed top-level… |
| Tests | test | Observed | Groups 66 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH gui.containers.application.modals.confirmForceStop. Observed top-level classes: MockWxMDD, TestApp, TestArgparse… |

## Important files

- `.github/workflows/block-pr-to-master.yml` (ci)
- `MANIFEST.in` (manifest)
- `gooey/languages/Hindi.json` (config)
- `gooey/languages/bengali.json` (config)
- `gooey/languages/bosnian.json` (config)
- `gooey/languages/chinese.json` (config)
- `gooey/languages/croatian.json` (config)
- `gooey/languages/czech.json` (config)
- `gooey/languages/dutch.json` (config)
- `gooey/languages/english.json` (config)
- `gooey/languages/french.json` (config)
- `gooey/languages/german.json` (config)
- `gooey/languages/greek.json` (config)
- `gooey/languages/hebrew.json` (config)
- `gooey/languages/italian.json` (config)
- `gooey/languages/japanese.json` (config)
- `gooey/languages/korean.json` (config)
- `gooey/languages/polish.json` (config)
- `gooey/languages/portuguese.json` (config)
- `gooey/languages/russian.json` (config)
- `gooey/languages/serbian.json` (config)
- `gooey/languages/spanish.json` (config)
- `gooey/languages/tamil.json` (config)
- `gooey/languages/traditional-chinese.json` (config)
- `gooey/languages/turkish.json` (config)
- `gooey/languages/ukrainian.json` (config)
- `gooey/languages/vietnamese.json` (config)
- `requirements.txt` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `gooey` — 190 analysed file(s)
- `docs` — 19 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `c541920465c7bcaaefa47a15a858eb477d2666fd` is the revision these paths and observations refer to.
