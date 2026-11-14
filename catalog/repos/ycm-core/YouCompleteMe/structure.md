# Project structure: ycm-core/YouCompleteMe

**Analysed commit:** `d4c91430b70a21ce471c8572400b647d313995b4`

**Commit reference:** [d4c91430b70a21ce471c8572400b647d313995b4](https://github.com/ycm-core/YouCompleteMe/commit/d4c91430b70a21ce471c8572400b647d313995b4)

**Tree at this commit:** [ycm-core/YouCompleteMe@d4c91430b70a](https://github.com/ycm-core/YouCompleteMe/tree/d4c91430b70a21ce471c8572400b647d313995b4)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | ycm-core/YouCompleteMe |
| Description | A code-completion engine for Vim |
| Stars | 25875 |
| Forks | 2740 |
| Licence | GPL-3.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `d4c91430b70a21ce471c8572400b647d313995b4` |
| Retrieved at | 2026-11-14T19:07:30.070318+00:00 |
| Files in this snapshot | 140 |

## Directory tree

```text
.github/  (6 files)
  ISSUE_TEMPLATE/  (2 files)
    config.yml
    issue.md
  workflows/  (3 files)
    ci.yml
    lock_old_issues.yaml
    update_vim_docs.yaml
  PULL_REQUEST_TEMPLATE.md
autoload/  (5 files)
  youcompleteme/  (4 files)
    filetypes.vim
    finder.vim
    hierarchy.vim
    symbol.vim
  youcompleteme.vim
doc/  (1 files)
  youcompleteme.txt
plugin/  (1 files)
  youcompleteme.vim
python/  (61 files)
  ycm/  (60 files)
    client/  (15 files)
      … 15 files under this directory
    tests/  (28 files)
      … 28 files under this directory
    __init__.py
    base.py
    buffer.py
    diagnostic_filter.py
    diagnostic_interface.py
    hierarchy_tree.py
    inlay_hints.py
    omni_completer.py
    paths.py
    scrolling_range.py
    semantic_highlighting.py
    signature_help.py
    syntax_parse.py
    text_properties.py
    unsafe_thread_pool_executor.py
    vimsupport.py
    youcompleteme.py
  test_requirements.txt
test/  (47 files)
  docker/  (9 files)
    ci/  (3 files)
      … 3 files under this directory
    manual/  (5 files)
      … 5 files under this directory
    rebuild_all
  lib/  (7 files)
    autoload/  (3 files)
      … 3 files under this directory
    plugin/  (3 files)
      … 3 files under this directory
    run_test.vim
  testdata/  (13 files)
    cpp/  (8 files)
      … 8 files under this directory
    diagnostics/  (2 files)
      … 2 files under this directory
    python/  (2 files)
      … 2 files under this directory
    vim/  (1 files)
      … 1 files under this directory
  .gitignore
  .vimspector.json
  Makefile
  README.md
  commands.test.vim
  completion.common.vim
  completion.test.vim
  completion_info.test.vim
  completion_noresolve.test.vim
  diagnostics.test.vim
  filesize.test.vim
  finder.test.vim
  fixit.test.vim
  hierarchies.test.vim
  hover.test.vim
  run_vim_tests
  signature_help.test.vim
  vimrc
.coveragerc
.gitignore
.gitmodules
.mergify.yml
.readme.utf-8.add
.vimspector.json
.ycm_extra_conf.py
CODE_OF_CONDUCT.md
CONTRIBUTING.md
COPYING.txt
README.md
codecov.yml
install.py
install.sh
print_todos.sh
run_tests.py
tox.ini
update-vim-docs
vimrc_ycm_minimal
```

## Entry points

- [install.py:49](https://github.com/ycm-core/YouCompleteMe/blob/d4c91430b70a21ce471c8572400b647d313995b4/install.py#L49)
- [run_tests.py:115](https://github.com/ycm-core/YouCompleteMe/blob/d4c91430b70a21ce471c8572400b647d313995b4/run_tests.py#L115)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: CheckCall, Main. |
| External integrations | external | Observed | Groups 15 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: BaseRequest, CommandRequest, CompleterAvailableRequest, CompletionRequest, DebugInfoRequest… |
| python package | library | Observed | Groups 17 file(s) under python package (observed from repository paths and static analysis). Observed top-level classes: Buffer, BufferDict, DiagnosticFilter, DiagnosticInterface, DiagnosticProperty, HierarchyNode. Obse… |
| Tests | test | Observed | Groups 75 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH ycm.client.base_request.GetCurrentDirectory, PATCH ycm.client.base_request.GetCurrentDirectory, PATCH ycm.vimsup… |

## Important files

- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/lock_old_issues.yaml` (ci)
- `.github/workflows/update_vim_docs.yaml` (ci)
- `.mergify.yml` (config)
- `.vimspector.json` (config)
- `codecov.yml` (config)
- `test/docker/ci/image/Dockerfile` (container)
- `test/docker/manual/image/Dockerfile` (container)
- `tox.ini` (config)

## Top-level layout

- `python` — 61 analysed file(s)
- `test` — 47 analysed file(s)
- `(root files)` — 19 analysed file(s)
- `.github` — 6 analysed file(s)
- `autoload` — 5 analysed file(s)
- `doc` — 1 analysed file(s)
- `plugin` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `d4c91430b70a21ce471c8572400b647d313995b4` is the revision these paths and observations refer to.
