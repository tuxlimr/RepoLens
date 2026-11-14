# Project structure: asweigart/pyautogui

**Analysed commit:** `b4255d0be42c377154c7d92337d7f8515fc63234`

**Commit reference:** [b4255d0be42c377154c7d92337d7f8515fc63234](https://github.com/asweigart/pyautogui/commit/b4255d0be42c377154c7d92337d7f8515fc63234)

**Tree at this commit:** [asweigart/pyautogui@b4255d0be42c](https://github.com/asweigart/pyautogui/tree/b4255d0be42c377154c7d92337d7f8515fc63234)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | asweigart/pyautogui |
| Description | A cross-platform GUI automation Python module for human beings. Used to programmatically control the mouse & keyboard. |
| Stars | 12757 |
| Forks | 1438 |
| Licence | BSD-3-Clause |
| Language | Python |
| Default branch | master |
| Analysed commit | `b4255d0be42c377154c7d92337d7f8515fc63234` |
| Retrieved at | 2026-11-14T19:09:59.284652+00:00 |
| Files in this snapshot | 31 |

## Directory tree

```text
docs/  (15 files)
  source/  (2 files)
    modules.rst
    pyautogui.rst
  Makefile
  conf.py
  index.rst
  install.rst
  keyboard.rst
  make.bat
  mouse.rst
  msgbox.rst
  quickstart.rst
  roadmap.rst
  screenshot.rst
  simplified-chinese.ipynb
  tests.rst
pyautogui/  (6 files)
  __init__.py
  __main__.py
  _pyautogui_java.py
  _pyautogui_osx.py
  _pyautogui_win.py
  _pyautogui_x11.py
tests/  (1 files)
  test_pyautogui.py
.gitignore
AUTHORS.txt
CHANGES.txt
LICENSE.txt
MANIFEST.in
Pipfile
README.md
setup.py
tox.ini
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). |
| pyautogui package | library | Observed | Groups 5 file(s) under pyautogui package (observed from repository paths and static analysis). Observed top-level classes: FailSafeException, HARDWAREINPUT, INPUT, ImageNotFoundException, KEYBDINPUT, MOUSEINPUT. Observe… |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: HoldThread, P, PressThread, TestDoctests, TestFailSafe, TestGeneral. |

## Important files

- `MANIFEST.in` (manifest)
- `Pipfile` (manifest)
- `setup.py` (manifest)
- `tox.ini` (config)

## Top-level layout

- `docs` — 15 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `pyautogui` — 6 analysed file(s)
- `tests` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `b4255d0be42c377154c7d92337d7f8515fc63234` is the revision these paths and observations refer to.
