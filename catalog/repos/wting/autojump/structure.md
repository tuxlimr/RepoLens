# Project structure: wting/autojump

**Analysed commit:** `ee21082751da739c65fe0ec2d02ca95d4266aebc`

**Commit reference:** [ee21082751da739c65fe0ec2d02ca95d4266aebc](https://github.com/wting/autojump/commit/ee21082751da739c65fe0ec2d02ca95d4266aebc)

**Tree at this commit:** [wting/autojump@ee21082751da](https://github.com/wting/autojump/tree/ee21082751da739c65fe0ec2d02ca95d4266aebc)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | wting/autojump |
| Description | A cd command that learns - easily navigate directories from the command line |
| Stars | 16961 |
| Forks | 704 |
| Licence | Other |
| Language | Python |
| Default branch | master |
| Analysed commit | `ee21082751da739c65fe0ec2d02ca95d4266aebc` |
| Retrieved at | 2026-11-14T19:08:38.974019+00:00 |
| Files in this snapshot | 40 |

## Directory tree

```text
bin/  (17 files)
  _j
  autojump
  autojump.bash
  autojump.bat
  autojump.fish
  autojump.lua
  autojump.sh
  autojump.tcsh
  autojump.zsh
  autojump_argparse.py
  autojump_data.py
  autojump_match.py
  autojump_utils.py
  j.bat
  jc.bat
  jco.bat
  jo.bat
docs/  (5 files)
  autojump.1
  body.md
  header.md
  install.md
  manpage_header.md
tests/  (5 files)
  integration/  (1 files)
    __init__.py
  unit/  (3 files)
    __init__.py
    autojump_match_test.py
    autojump_utils_test.py
  __init__.py
tools/  (1 files)
  autojump_ipython.py
.gitattributes
.gitignore
.pre-commit-config.yaml
.travis.yml
AUTHORS
CHANGES.md
LICENSE
Makefile
README.md
install.py
tox.ini
uninstall.py
```

## Entry points

- [install.py:235](https://github.com/wting/autojump/blob/ee21082751da739c65fe0ec2d02ca95d4266aebc/install.py#L235)
- [uninstall.py:216](https://github.com/wting/autojump/blob/ee21082751da739c65fe0ec2d02ca95d4266aebc/uninstall.py#L216)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bin package | library | Observed | Groups 5 file(s) under bin package (observed from repository paths and static analysis). Observed top-level classes: Action, ArgumentDefaultsHelpFormatter, ArgumentError, ArgumentParser, ArgumentTypeError, FileType. Obs… |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: cp, get_shell, is_empty_dir, main, mkdir, modify_autojump_lua. |
| Tests | test | Observed | Groups 5 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: TestMatchAnywhere, TestMatchConsecutive. Observed top-level functions: test_dont_surround_quotes_not_in_bash… |
| tools package | library | Observed | Groups 1 file(s) under tools package (observed from repository paths and static analysis). Observed top-level functions: j. |

## Important files

- `.pre-commit-config.yaml` (config)
- `.travis.yml` (ci)
- `tox.ini` (config)

## Top-level layout

- `bin` — 17 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `docs` — 5 analysed file(s)
- `tests` — 5 analysed file(s)
- `tools` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `ee21082751da739c65fe0ec2d02ca95d4266aebc` is the revision these paths and observations refer to.
