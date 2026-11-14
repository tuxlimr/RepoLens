# Project structure: nvbn/thefuck

**Analysed commit:** `c7e7e1d884d3bb241ea6448f72a989434c2a35ec`

**Commit reference:** [c7e7e1d884d3bb241ea6448f72a989434c2a35ec](https://github.com/nvbn/thefuck/commit/c7e7e1d884d3bb241ea6448f72a989434c2a35ec)

**Tree at this commit:** [nvbn/thefuck@c7e7e1d884d3](https://github.com/nvbn/thefuck/tree/c7e7e1d884d3bb241ea6448f72a989434c2a35ec)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | nvbn/thefuck |
| Description | Magnificent app which corrects your previous console command. |
| Stars | 97954 |
| Forks | 3979 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `c7e7e1d884d3bb241ea6448f72a989434c2a35ec` |
| Retrieved at | 2026-11-14T19:06:08.363959+00:00 |
| Files in this snapshot | 434 |

## Directory tree

```text
.devcontainer/  (2 files)
  Dockerfile
  devcontainer.json
.github/  (2 files)
  workflows/  (1 files)
    test.yml
  ISSUE_TEMPLATE.md
scripts/  (2 files)
  fuck.bat
  fuck.ps1
tests/  (204 files)
  entrypoints/  (4 files)
    __init__.py
    test_alias.py
    test_fix_command.py
    test_not_configured.py
  functional/  (7 files)
    __init__.py
    conftest.py
    plots.py
    test_bash.py
    test_fish.py
    test_tcsh.py
    test_zsh.py
  output_readers/  (1 files)
    test_rerun.py
  rules/  (168 files)
    __init__.py
    test_adb_unknown_command.py
    test_ag_literal.py
    test_apt_get.py
    test_apt_get_search.py
    test_apt_invalid_operation.py
    test_apt_list_upgradable.py
    test_apt_upgrade.py
    test_aws_cli.py
    test_az_cli.py
    test_brew_cask_dependency.py
    test_brew_install.py
    test_brew_link.py
    test_brew_reinstall.py
    test_brew_uninstall.py
    test_brew_unknown_command.py
    test_brew_update_formula.py
    test_cargo_no_command.py
    test_cat_dir.py
    test_cd_correction.py
    test_cd_cs.py
    test_cd_mkdir.py
    test_cd_parent.py
    test_chmod_x.py
    … 144 more files
  shells/  (8 files)
    __init__.py
    conftest.py
    test_bash.py
    test_fish.py
    test_generic.py
    test_powershell.py
    test_tcsh.py
    test_zsh.py
  specific/  (4 files)
    __init__.py
    test_git.py
    test_npm.py
    test_sudo.py
  Dockerfile
  __init__.py
  conftest.py
  test_argument_parser.py
  test_conf.py
  test_corrector.py
  test_logs.py
  test_readme.py
  test_types.py
  test_ui.py
  test_utils.py
  utils.py
thefuck/  (210 files)
  entrypoints/  (6 files)
    __init__.py
    alias.py
    fix_command.py
    main.py
    not_configured.py
    shell_logger.py
  output_readers/  (4 files)
    __init__.py
    read_log.py
    rerun.py
    shell_logger.py
  rules/  (170 files)
    __init__.py
    adb_unknown_command.py
    ag_literal.py
    apt_get.py
    apt_get_search.py
    apt_invalid_operation.py
    apt_list_upgradable.py
    apt_upgrade.py
    aws_cli.py
    az_cli.py
    brew_cask_dependency.py
    brew_install.py
    brew_link.py
    brew_reinstall.py
    brew_uninstall.py
    brew_unknown_command.py
    brew_update_formula.py
    cargo.py
    cargo_no_command.py
    cat_dir.py
    cd_correction.py
    cd_cs.py
    cd_mkdir.py
    cd_parent.py
    … 146 more files
  shells/  (7 files)
    __init__.py
    bash.py
    fish.py
    generic.py
    powershell.py
    tcsh.py
    zsh.py
  specific/  (10 files)
    __init__.py
    apt.py
    archlinux.py
    brew.py
    dnf.py
    git.py
    nix.py
    npm.py
    sudo.py
    yum.py
  system/  (3 files)
    __init__.py
    unix.py
    win32.py
  __init__.py
  argument_parser.py
  conf.py
  const.py
  corrector.py
  exceptions.py
  logs.py
  types.py
  ui.py
  utils.py
.editorconfig
.gitignore
CONTRIBUTING.md
LICENSE.md
MANIFEST.in
README.md
fastentrypoints.py
install.sh
release.py
requirements.txt
setup.cfg
setup.py
snapcraft.yaml
tox.ini
```

## Entry points

- [thefuck/entrypoints/main.py](https://github.com/nvbn/thefuck/blob/c7e7e1d884d3bb241ea6448f72a989434c2a35ec/thefuck/entrypoints/main.py)
- [thefuck/entrypoints/not_configured.py](https://github.com/nvbn/thefuck/blob/c7e7e1d884d3bb241ea6448f72a989434c2a35ec/thefuck/entrypoints/not_configured.py)
- [thefuck/entrypoints/not_configured.py](https://github.com/nvbn/thefuck/blob/c7e7e1d884d3bb241ea6448f72a989434c2a35ec/thefuck/entrypoints/not_configured.py)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). Observed top-level functions: get_args, get_new_setup_py_lines, main. |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: main. |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 203 file(s) under tests (observed from repository paths and static analysis). Observed application object created via Command. Observed routes: PATCH thefuck.output_readers.rerun._wait_output, PATCH thefuck.outpu… |
| thefuck package | library | Observed | Groups 209 file(s) under thefuck package (observed from repository paths and static analysis). Observed top-level classes: Bash, Cache, Command, CommandSelector, CorrectedCommand, EmptyCommand. Observed top-level functi… |

## Important files

- `.devcontainer/Dockerfile` (container)
- `.devcontainer/devcontainer.json` (config)
- `.editorconfig` (config)
- `.github/workflows/test.yml` (ci)
- `MANIFEST.in` (manifest)
- `requirements.txt` (manifest)
- `setup.cfg` (manifest)
- `setup.py` (manifest)
- `snapcraft.yaml` (config)
- `tests/Dockerfile` (container)
- `tox.ini` (config)

## Top-level layout

- `thefuck` — 210 analysed file(s)
- `tests` — 204 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `.devcontainer` — 2 analysed file(s)
- `.github` — 2 analysed file(s)
- `scripts` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `c7e7e1d884d3bb241ea6448f72a989434c2a35ec` is the revision these paths and observations refer to.
