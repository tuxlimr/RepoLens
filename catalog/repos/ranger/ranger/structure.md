# Project structure: ranger/ranger

**Analysed commit:** `46e957af9762dd2fcaabfbef4d3c45c16edd1184`

**Commit reference:** [46e957af9762dd2fcaabfbef4d3c45c16edd1184](https://github.com/ranger/ranger/commit/46e957af9762dd2fcaabfbef4d3c45c16edd1184)

**Tree at this commit:** [ranger/ranger@46e957af9762](https://github.com/ranger/ranger/tree/46e957af9762dd2fcaabfbef4d3c45c16edd1184)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | ranger/ranger |
| Description | A VIM-inspired filemanager for the console |
| Stars | 17464 |
| Forks | 938 |
| Licence | GPL-3.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `46e957af9762dd2fcaabfbef4d3c45c16edd1184` |
| Retrieved at | 2026-11-14T19:08:33.406313+00:00 |
| Files in this snapshot | 157 |

## Directory tree

```text
.github/  (6 files)
  workflows/  (4 files)
    pr.yml
    pypy.yml
    python.yml
    shellcheck.yml
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
doc/  (11 files)
  tools/  (4 files)
    convert_papermode_to_metadata.py
    performance_test.py
    print_colors.py
    print_keys.py
  colorschemes.md
  howto-publish-a-release.md
  ranger.1
  ranger.desktop
  ranger.pod
  rifle.1
  rifle.pod
examples/  (19 files)
  README
  fish_automatic_cd.fish
  plugin_avfs.py
  plugin_chmod_keybindings.py
  plugin_fasd_add.py
  plugin_file_filter.py
  plugin_hello_world.py
  plugin_ipc.py
  plugin_linemode.py
  plugin_new_macro.py
  plugin_new_sorting_method.py
  plugin_pmount.py
  plugin_pmount_dynamic.py
  rc_emacs.conf
  rifle_different_file_opener.conf
  rifle_sxiv.sh
  shell_automatic_cd.sh
  shell_subshell_notice.sh
  vim_file_chooser.vim
ranger/  (91 files)
  api/  (2 files)
    __init__.py
    commands.py
  colorschemes/  (5 files)
    __init__.py
    default.py
    jungle.py
    snow.py
    solarized.py
  config/  (6 files)
    .pylintrc
    __init__.py
    commands.py
    commands_sample.py
    rc.conf
    rifle.conf
  container/  (8 files)
    __init__.py
    bookmarks.py
    directory.py
    file.py
    fsobject.py
    history.py
    settings.py
    tags.py
  core/  (11 files)
    __init__.py
    actions.py
    filter_stack.py
    fm.py
    linemode.py
    loader.py
    main.py
    metadata.py
    runner.py
    shared.py
    tab.py
  data/  (3 files)
    mime.types
    rowcolumn_diacritics.py
    scope.sh
  ext/  (35 files)
    vcs/  (6 files)
      … 6 files under this directory
    __init__.py
    abc.py
    accumulator.py
    cached_function.py
    curses_interrupt_handler.py
    direction.py
    get_executables.py
    hash.py
    human_readable.py
    img_display.py
    iter_tools.py
    keybinding_parser.py
    lazy_property.py
    logutils.py
    macrodict.py
    mount_path.py
    openstruct.py
    popen23.py
    popen_forked.py
    posix_signals.py
    relative_symlink.py
    rifle.py
    safe_path.py
    shell_escape.py
    … 5 more files
  gui/  (20 files)
    widgets/  (10 files)
      … 10 files under this directory
    __init__.py
    ansi.py
    bar.py
    color.py
    colorscheme.py
    context.py
    curses_shortcuts.py
    displayable.py
    mouse_event.py
    ui.py
  __init__.py
tests/  (17 files)
  pylint/  (4 files)
    conftest.py
    py2_compat.py
    python3.py
    test_py2_compat.py
  ranger/  (11 files)
    container/  (5 files)
      … 5 files under this directory
    core/  (2 files)
      … 2 files under this directory
    ext/  (2 files)
      … 2 files under this directory
    gui/  (1 files)
      … 1 files under this directory
    __init__.py
  __init__.py
  manpage_completion_test.py
.flake8
.gitignore
.pylintrc
AUTHORS
CHANGELOG.md
CONTRIBUTING.md
HACKING.md
LICENSE
Makefile
README.md
ranger.py
requirements.txt
setup.py
```

## Entry points

- [ranger/api/commands.py:452](https://github.com/ranger/ranger/blob/46e957af9762dd2fcaabfbef4d3c45c16edd1184/ranger/api/commands.py#L452)
- [ranger/ext/direction.py:186](https://github.com/ranger/ranger/blob/46e957af9762dd2fcaabfbef4d3c45c16edd1184/ranger/ext/direction.py#L186)
- [ranger/ext/human_readable.py:74](https://github.com/ranger/ranger/blob/46e957af9762dd2fcaabfbef4d3c45c16edd1184/ranger/ext/human_readable.py#L74)
- [ranger/ext/iter_tools.py:48](https://github.com/ranger/ranger/blob/46e957af9762dd2fcaabfbef4d3c45c16edd1184/ranger/ext/iter_tools.py#L48)
- [ranger/ext/keybinding_parser.py:290](https://github.com/ranger/ranger/blob/46e957af9762dd2fcaabfbef4d3c45c16edd1184/ranger/ext/keybinding_parser.py#L290)
- [ranger/ext/lazy_property.py:60](https://github.com/ranger/ranger/blob/46e957af9762dd2fcaabfbef4d3c45c16edd1184/ranger/ext/lazy_property.py#L60)
- [ranger/ext/macrodict.py:80](https://github.com/ranger/ranger/blob/46e957af9762dd2fcaabfbef4d3c45c16edd1184/ranger/ext/macrodict.py#L80)
- [ranger/ext/rifle.py:645](https://github.com/ranger/ranger/blob/46e957af9762dd2fcaabfbef4d3c45c16edd1184/ranger/ext/rifle.py#L645)
- [ranger/ext/signals.py:288](https://github.com/ranger/ranger/blob/46e957af9762dd2fcaabfbef4d3c45c16edd1184/ranger/ext/signals.py#L288)
- [ranger/ext/widestring.py:166](https://github.com/ranger/ranger/blob/46e957af9762dd2fcaabfbef4d3c45c16edd1184/ranger/ext/widestring.py#L166)
- [ranger/gui/ansi.py:185](https://github.com/ranger/ranger/blob/46e957af9762dd2fcaabfbef4d3c45c16edd1184/ranger/gui/ansi.py#L185)
- [ranger/gui/widgets/console.py:609](https://github.com/ranger/ranger/blob/46e957af9762dd2fcaabfbef4d3c45c16edd1184/ranger/gui/widgets/console.py#L609)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 1 file(s) under api layer (observed from repository paths and static analysis). Observed top-level functions: hook_init, hook_ready, register_linemode. |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: InstallLib, LocalSettings, Settings, alias, bulkrename, cd. Observed top-level functi… |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 2 file(s) under data layer (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 13 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Command, CommandContainer, Console, Direction, KeyBuffer, KeyMaps. Observed top-level fun… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| ranger package | library | Observed | Groups 57 file(s) under ranger package (observed from repository paths and static analysis). Observed top-level classes: Accumulator, Bar, BarSide, Bookmarks, BrowserColumn, Bzr. Observed top-level functions: Popen23, P… |
| Service / domain layer | service | Observed | Groups 10 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: Actions, AndFilter, BaseFilter, CommandLoader, Context, CopyLoader. Observed top-level fun… |
| Tests | test | Observed | Groups 18 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: FileManager, MockFM, NotValidatedBookmarks, Py2CompatibilityChecker, Python3Checker, Python3TokenChecker. O… |

## Important files

- `.github/workflows/pr.yml` (ci)
- `.github/workflows/pypy.yml` (ci)
- `.github/workflows/python.yml` (ci)
- `.github/workflows/shellcheck.yml` (ci)
- `requirements.txt` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `ranger` — 91 analysed file(s)
- `examples` — 19 analysed file(s)
- `tests` — 17 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `doc` — 11 analysed file(s)
- `.github` — 6 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `46e957af9762dd2fcaabfbef4d3c45c16edd1184` is the revision these paths and observations refer to.
