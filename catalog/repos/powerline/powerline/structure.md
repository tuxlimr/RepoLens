# Project structure: powerline/powerline

**Analysed commit:** `11808cbe5c16e4621edcaefa916b5add81eab799`

**Commit reference:** [11808cbe5c16e4621edcaefa916b5add81eab799](https://github.com/powerline/powerline/commit/11808cbe5c16e4621edcaefa916b5add81eab799)

**Tree at this commit:** [powerline/powerline@11808cbe5c16](https://github.com/powerline/powerline/tree/11808cbe5c16e4621edcaefa916b5add81eab799)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | powerline/powerline |
| Description | Powerline is a statusline plugin for vim, and provides statuslines and prompts for several other applications, including zsh, bash, tmux, IPython, Awesome and Qtile. |
| Stars | 14844 |
| Forks | 996 |
| Licence | Other |
| Language | Python |
| Default branch | develop |
| Analysed commit | `11808cbe5c16e4621edcaefa916b5add81eab799` |
| Retrieved at | 2026-11-14T19:09:12.325385+00:00 |
| Files in this snapshot | 366 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    main.yaml
client/  (3 files)
  powerline.c
  powerline.py
  powerline.sh
docs/  (44 files)
  source/  (42 files)
    _static/  (1 files)
      … 1 files under this directory
    commands/  (4 files)
      … 4 files under this directory
    configuration/  (12 files)
      … 12 files under this directory
    develop/  (5 files)
      … 5 files under this directory
    installation/  (2 files)
      … 2 files under this directory
    troubleshooting/  (2 files)
      … 2 files under this directory
    usage/  (3 files)
      … 3 files under this directory
    commands.rst
    conf.py
    configuration.rst
    develop.rst
    index.rst
    installation.rst
    license-and-credits.rst
    overview.rst
    powerline_autodoc.py
    powerline_automan.py
    tips-and-tricks.rst
    troubleshooting.rst
    usage.rst
  .gitignore
  Makefile
font/  (1 files)
  10-powerline-symbols.conf
powerline/  (200 files)
  bindings/  (37 files)
    awesome/  (2 files)
      … 2 files under this directory
    bar/  (1 files)
      … 1 files under this directory
    bash/  (1 files)
      … 1 files under this directory
    fish/  (1 files)
      … 1 files under this directory
    i3/  (1 files)
      … 1 files under this directory
    ipython/  (5 files)
      … 5 files under this directory
    lemonbar/  (1 files)
      … 1 files under this directory
    pdb/  (2 files)
      … 2 files under this directory
    qtile/  (2 files)
      … 2 files under this directory
    rc/  (1 files)
      … 1 files under this directory
    shell/  (1 files)
      … 1 files under this directory
    tcsh/  (1 files)
      … 1 files under this directory
    tmux/  (9 files)
      … 9 files under this directory
    vim/  (3 files)
      … 3 files under this directory
    wm/  (2 files)
      … 2 files under this directory
    zsh/  (2 files)
      … 2 files under this directory
    __init__.py
    config.py
  commands/  (6 files)
    __init__.py
    config.py
    daemon.py
    lemonbar.py
    lint.py
    main.py
  config_files/  (46 files)
    colorschemes/  (15 files)
      … 15 files under this directory
    themes/  (29 files)
      … 29 files under this directory
    colors.json
    config.json
  lib/  (24 files)
    vcs/  (4 files)
      … 4 files under this directory
    watcher/  (5 files)
      … 5 files under this directory
    __init__.py
    config.py
    debug.py
    dict.py
    encoding.py
    humanize_bytes.py
    inotify.py
    memoize.py
    monotonic.py
    overrides.py
    path.py
    shell.py
    threaded.py
    unicode.py
    url.py
  lint/  (20 files)
    markedjson/  (13 files)
      … 13 files under this directory
    __init__.py
    checks.py
    context.py
    imp.py
    inspect.py
    selfcheck.py
    spec.py
  listers/  (4 files)
    __init__.py
    i3wm.py
    pdb.py
    vim.py
  matchers/  (6 files)
    vim/  (5 files)
      … 5 files under this directory
    __init__.py
  renderers/  (18 files)
    ipython/  (4 files)
      … 4 files under this directory
    shell/  (7 files)
      … 7 files under this directory
    __init__.py
    i3bar.py
    lemonbar.py
    pango_markup.py
    pdb.py
    tmux.py
    vim.py
  segments/  (25 files)
    common/  (10 files)
      … 10 files under this directory
    vim/  (9 files)
      … 9 files under this directory
    __init__.py
    i3wm.py
    ipython.py
    pdb.py
    shell.py
    tmux.py
  selectors/  (2 files)
    __init__.py
    vim.py
  __init__.py
  colorscheme.py
  config.py
  ipython.py
  lemonbar.py
  pdb.py
  renderer.py
  segment.py
  shell.py
  theme.py
  version.py
  vim.py
scripts/  (6 files)
  .gitignore
  powerline-config
  powerline-daemon
  powerline-lint
  powerline-release.py
  powerline-render
tests/  (98 files)
  modules/  (8 files)
    lib/  (5 files)
      … 5 files under this directory
    __init__.py
    matchers.py
    vim.py
  shlib/  (3 files)
    common.sh
    vim.sh
    vterm.sh
  test_awesome/  (5 files)
    path/  (1 files)
      … 1 files under this directory
    powerline/  (3 files)
      … 3 files under this directory
    test.sh
  test_bar/  (6 files)
    path/  (2 files)
      … 2 files under this directory
    powerline/  (3 files)
      … 3 files under this directory
    test.sh
  test_daemon/  (1 files)
    test.sh
  test_in_vterm/  (8 files)
    shell/  (1 files)
      … 1 files under this directory
    test.sh
    test_shells.py
    test_shells.sh
    test_tmux.py
    test_tmux.sh
    test_vim.py
    test_vim.sh
  test_lint/  (1 files)
    test.sh
  test_python/  (14 files)
    empty
    test.sh
    test_cmdline.py
    test_config_merging.py
    test_config_reload.py
    test_configuration.py
    test_lib.py
    test_lib_config.py
    test_listers.py
    test_logging.py
    test_provided_config_files.py
    test_segments.py
    test_selectors.py
    test_watcher.py
  test_shells/  (37 files)
    inputs/  (10 files)
      … 10 files under this directory
    ipython_home/  (1 files)
      … 1 files under this directory
    outputs/  (18 files)
      … 18 files under this directory
    bgscript.sh
    pdb-main.py
    pdb-script.py
    postproc.py
    run_script.py
    test.sh
    waitpid.sh
    zsh_test_script.zsh
  test_vim/  (11 files)
    pyfiles/  (1 files)
      … 1 files under this directory
    tests/  (8 files)
      … 8 files under this directory
    test.sh
    vim_utils.vim
  vim_sys_path/  (1 files)
    vim.py
  __init__.py
  install.sh
  test.sh
tools/  (3 files)
  colors_find.py
  generate_gradients.py
  purge-PRs.py
.editorconfig
.gitattributes
.gitignore
.local.vimrc
.travis.yml
CONTRIBUTING.rst
LICENSE
MANIFEST.in
README.rst
setup.py
```

## Entry points

- [powerline/bindings/awesome/powerline-awesome.py:19](https://github.com/powerline/powerline/blob/11808cbe5c16e4621edcaefa916b5add81eab799/powerline/bindings/awesome/powerline-awesome.py#L19)
- [powerline/bindings/bar/powerline-bar.py:17](https://github.com/powerline/powerline/blob/11808cbe5c16e4621edcaefa916b5add81eab799/powerline/bindings/bar/powerline-bar.py#L17)
- [powerline/bindings/i3/powerline-i3.py:24](https://github.com/powerline/powerline/blob/11808cbe5c16e4621edcaefa916b5add81eab799/powerline/bindings/i3/powerline-i3.py#L24)
- [powerline/bindings/lemonbar/powerline-lemonbar.py:16](https://github.com/powerline/powerline/blob/11808cbe5c16e4621edcaefa916b5add81eab799/powerline/bindings/lemonbar/powerline-lemonbar.py#L16)
- [powerline/bindings/pdb/__main__.py:8](https://github.com/powerline/powerline/blob/11808cbe5c16e4621edcaefa916b5add81eab799/powerline/bindings/pdb/__main__.py#L8)
- [scripts/powerline-release.py:233](https://github.com/powerline/powerline/blob/11808cbe5c16e4621edcaefa916b5add81eab799/scripts/powerline-release.py#L233)
- [tools/generate_gradients.py:176](https://github.com/powerline/powerline/blob/11808cbe5c16e4621edcaefa916b5add81eab799/tools/generate_gradients.py#L176)
- [tools/purge-PRs.py:16](https://github.com/powerline/powerline/blob/11808cbe5c16e4621edcaefa916b5add81eab799/tools/purge-PRs.py#L16)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 52 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: ConfigArgParser, ConfigLoader, DeferredWatcher, DummyWatcher, EmptyArgs, StrFunction… |
| Application entry point | entrypoint | Observed | Groups 9 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: I3Powerline. Observed top-level functions: color, compute_steps, create_ebuilds, create_re… |
| External integrations | external | Observed | Groups 3 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level functions: eintr_retry_call, tobytes. |
| powerline package | library | Observed | Groups 129 file(s) under powerline package (observed from repository paths and static analysis). Observed top-level classes: AliasEvent, Args, AwesomeThread, BaseConstructor, BaseDirChanged, BaseResolver. Observed top-l… |
| Tests | test | Observed | Groups 98 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: Args, AttrReplace, CTypesFunction, CTypesLibraryFuncsCollection, EvenSimplerRenderer, ExpectProcess. Observ… |
| tools package | library | Observed | Groups 1 file(s) under tools package (observed from repository paths and static analysis). Observed top-level functions: find_color, get_lab, get_rgb, get_upscaled_values, lab_to_csi. |

## Important files

- `.editorconfig` (config)
- `.github/workflows/main.yaml` (ci)
- `.travis.yml` (ci)
- `MANIFEST.in` (manifest)
- `powerline/config_files/colors.json` (config)
- `powerline/config_files/colorschemes/default.json` (config)
- `powerline/config_files/colorschemes/ipython/__main__.json` (config)
- `powerline/config_files/colorschemes/pdb/__main__.json` (config)
- `powerline/config_files/colorschemes/pdb/default.json` (config)
- `powerline/config_files/colorschemes/pdb/solarized.json` (config)
- `powerline/config_files/colorschemes/shell/__main__.json` (config)
- `powerline/config_files/colorschemes/shell/default.json` (config)
- `powerline/config_files/colorschemes/shell/solarized.json` (config)
- `powerline/config_files/colorschemes/solarized.json` (config)
- `powerline/config_files/colorschemes/tmux/default.json` (config)
- `powerline/config_files/colorschemes/tmux/solarized.json` (config)
- `powerline/config_files/colorschemes/vim/__main__.json` (config)
- `powerline/config_files/colorschemes/vim/default.json` (config)
- `powerline/config_files/colorschemes/vim/solarized.json` (config)
- `powerline/config_files/colorschemes/vim/solarizedlight.json` (config)
- `powerline/config_files/config.json` (config)
- `powerline/config_files/themes/ascii.json` (config)
- `powerline/config_files/themes/ipython/in.json` (config)
- `powerline/config_files/themes/ipython/in2.json` (config)
- `powerline/config_files/themes/ipython/out.json` (config)
- `powerline/config_files/themes/ipython/rewrite.json` (config)
- `powerline/config_files/themes/pdb/default.json` (config)
- `powerline/config_files/themes/powerline.json` (config)
- `powerline/config_files/themes/powerline_terminus.json` (config)
- `powerline/config_files/themes/powerline_unicode7.json` (config)
- `powerline/config_files/themes/shell/__main__.json` (config)
- `powerline/config_files/themes/shell/continuation.json` (config)
- `powerline/config_files/themes/shell/default.json` (config)
- `powerline/config_files/themes/shell/default_leftonly.json` (config)
- `powerline/config_files/themes/shell/select.json` (config)
- `powerline/config_files/themes/tmux/default.json` (config)
- `powerline/config_files/themes/unicode.json` (config)
- `powerline/config_files/themes/unicode_terminus.json` (config)
- `powerline/config_files/themes/unicode_terminus_condensed.json` (config)
- `powerline/config_files/themes/vim/__main__.json` (config)
- `powerline/config_files/themes/vim/cmdwin.json` (config)
- `powerline/config_files/themes/vim/default.json` (config)
- `powerline/config_files/themes/vim/help.json` (config)
- `powerline/config_files/themes/vim/plugin_commandt.json` (config)
- `powerline/config_files/themes/vim/plugin_gundo-preview.json` (config)
- `powerline/config_files/themes/vim/plugin_gundo.json` (config)
- `powerline/config_files/themes/vim/plugin_nerdtree.json` (config)
- `powerline/config_files/themes/vim/quickfix.json` (config)
- `powerline/config_files/themes/vim/tabline.json` (config)
- `powerline/config_files/themes/wm/default.json` (config)
- `setup.py` (manifest)

## Top-level layout

- `powerline` — 200 analysed file(s)
- `tests` — 98 analysed file(s)
- `docs` — 44 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `scripts` — 6 analysed file(s)
- `client` — 3 analysed file(s)
- `tools` — 3 analysed file(s)
- `.github` — 1 analysed file(s)
- `font` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x vendored/generated directory excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `11808cbe5c16e4621edcaefa916b5add81eab799` is the revision these paths and observations refer to.
