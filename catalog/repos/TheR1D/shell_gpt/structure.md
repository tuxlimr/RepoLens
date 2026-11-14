# Project structure: TheR1D/shell_gpt

**Analysed commit:** `a082bd5327ce0c4ef5a0284d9060e833be9444a6`

**Commit reference:** [a082bd5327ce0c4ef5a0284d9060e833be9444a6](https://github.com/TheR1D/shell_gpt/commit/a082bd5327ce0c4ef5a0284d9060e833be9444a6)

**Tree at this commit:** [TheR1D/shell_gpt@a082bd5327ce](https://github.com/TheR1D/shell_gpt/tree/a082bd5327ce0c4ef5a0284d9060e833be9444a6)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | TheR1D/shell_gpt |
| Description | A command-line productivity tool powered by AI large language models like GPT-5, will help you accomplish your tasks faster and more efficiently. |
| Stars | 12309 |
| Forks | 971 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `a082bd5327ce0c4ef5a0284d9060e833be9444a6` |
| Retrieved at | 2026-11-14T19:10:10.354291+00:00 |
| Files in this snapshot | 42 |

## Directory tree

```text
.devcontainer/  (1 files)
  devcontainer.json
.github/  (5 files)
  workflows/  (4 files)
    codespell.yml
    docker.yml
    lint_test.yml
    release.yml
  FUNDING.yml
scripts/  (3 files)
  format.sh
  lint.sh
  test.sh
sgpt/  (20 files)
  handlers/  (5 files)
    __init__.py
    chat_handler.py
    default_handler.py
    handler.py
    repl_handler.py
  llm_functions/  (4 files)
    common/  (1 files)
      … 1 files under this directory
    mac/  (1 files)
      … 1 files under this directory
    __init__.py
    init_functions.py
  __init__.py
  __main__.py
  __version__.py
  app.py
  cache.py
  config.py
  function.py
  integration.py
  printer.py
  role.py
  utils.py
tests/  (8 files)
  __init__.py
  _integration.py
  conftest.py
  test_code.py
  test_default.py
  test_roles.py
  test_shell.py
  utils.py
CONTRIBUTING.md
Dockerfile
LICENSE
README.md
pyproject.toml
```

## Entry points

- [sgpt/__init__.py](https://github.com/TheR1D/shell_gpt/blob/a082bd5327ce0c4ef5a0284d9060e833be9444a6/sgpt/__init__.py)
- [sgpt/app.py:275](https://github.com/TheR1D/shell_gpt/blob/a082bd5327ce0c4ef5a0284d9060e833be9444a6/sgpt/app.py#L275)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 5 file(s) under api layer (observed from repository paths and static analysis). Observed top-level classes: ChatHandler, ChatSession, DefaultHandler, Handler, ReplHandler. |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: Config. |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: entry_point, main. |
| scripts package | library | Observed | Groups 3 file(s) under scripts package (observed from repository paths and static analysis). |
| sgpt package | library | Observed | Groups 12 file(s) under sgpt package (observed from repository paths and static analysis). Observed top-level classes: Cache, DefaultRoles, Function, MarkdownPrinter, Printer, SystemRole. Observed top-level functions: g… |
| Tests | test | Observed | Groups 8 file(s) under tests (observed from repository paths and static analysis). Observed application object created via Typer. Observed routes: PATCH sgpt.handlers.handler.Handler.get_completion, PATCH sgpt.handlers.… |

## Important files

- `.devcontainer/devcontainer.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/workflows/codespell.yml` (ci)
- `.github/workflows/docker.yml` (ci)
- `.github/workflows/lint_test.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `Dockerfile` (container)
- `pyproject.toml` (manifest)

## Top-level layout

- `sgpt` — 20 analysed file(s)
- `tests` — 8 analysed file(s)
- `(root files)` — 5 analysed file(s)
- `.github` — 5 analysed file(s)
- `scripts` — 3 analysed file(s)
- `.devcontainer` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `a082bd5327ce0c4ef5a0284d9060e833be9444a6` is the revision these paths and observations refer to.
