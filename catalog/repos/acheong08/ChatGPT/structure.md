# Project structure: acheong08/ChatGPT

**Analysed commit:** `9167b325addc7d3520987face684e8230bd62b46`

**Commit reference:** [9167b325addc7d3520987face684e8230bd62b46](https://github.com/acheong08/ChatGPT/commit/9167b325addc7d3520987face684e8230bd62b46)

**Tree at this commit:** [acheong08/ChatGPT@9167b325addc](https://github.com/acheong08/ChatGPT/tree/9167b325addc7d3520987face684e8230bd62b46)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | acheong08/ChatGPT |
| Description | Reverse engineered ChatGPT API |
| Stars | 27994 |
| Forks | 4363 |
| Licence | GPL-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `9167b325addc7d3520987face684e8230bd62b46` |
| Retrieved at | 2026-11-14T19:07:17.920705+00:00 |
| Files in this snapshot | 44 |

## Directory tree

```text
.devcontainer/  (1 files)
  devcontainer.json
.github/  (7 files)
  ISSUE_TEMPLATE/  (4 files)
    bug_report.yml
    config.yml
    custom.md
    feature_request.yml
  workflows/  (2 files)
    codeql.yml
    python-publish.yml
  FUNDING.yml
.vscode/  (2 files)
  extensions.json
  settings.json
docs/  (16 files)
  wiki/  (7 files)
    Authentication.md
    Code-examples.md
    Home.md
    Recipient.md
    Star-history.md
    V1.md
    V3.md
  CODE_OF_CONDUCT.md
  CONTRIBUTING.md
  PRIVACY.md
  README.md
  README_ja.md
  README_ko.md
  README_sp.md
  README_zh.md
  SECURITY.md
src/  (8 files)
  revChatGPT/  (8 files)
    config/  (1 files)
      … 1 files under this directory
    V1.py
    V3.py
    __init__.py
    __main__.py
    typings.py
    utils.py
    version.py
tests/  (2 files)
  debug.bat
  test_recipient.py
.gitignore
.pre-commit-config.yaml
LICENSE
Makefile
config.json.example
requirements.txt
setup.cfg
setup.py
```

## Entry points

- [src/revChatGPT/V1.py:1739](https://github.com/acheong08/ChatGPT/blob/9167b325addc7d3520987face684e8230bd62b46/src/revChatGPT/V1.py#L1739)
- [src/revChatGPT/V3.py:758](https://github.com/acheong08/ChatGPT/blob/9167b325addc7d3520987face684e8230bd62b46/src/revChatGPT/V3.py#L758)
- [src/revChatGPT/__main__.py:64](https://github.com/acheong08/ChatGPT/blob/9167b325addc7d3520987face684e8230bd62b46/src/revChatGPT/__main__.py#L64)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 3 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: AsyncChatbot, Chatbot, ChatbotCLI. Observed top-level functions: captcha_solver, configure… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| revChatGPT package | library | Observed | Groups 4 file(s) under revchatgpt package (observed from repository paths and static analysis). Observed top-level classes: APIConnectionError, ActionError, ActionNotAllowedError, ActionRefuseError, AuthenticationError,… |
| Tests | test | Observed | Groups 2 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: main, sync_main. |

## Important files

- `.devcontainer/devcontainer.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/workflows/codeql.yml` (ci)
- `.github/workflows/python-publish.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `.vscode/extensions.json` (config)
- `.vscode/settings.json` (config)
- `requirements.txt` (manifest)
- `setup.cfg` (manifest)
- `setup.py` (manifest)
- `src/revChatGPT/config/enable_internet.json` (config)

## Top-level layout

- `docs` — 16 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `src` — 8 analysed file(s)
- `.github` — 7 analysed file(s)
- `.vscode` — 2 analysed file(s)
- `tests` — 2 analysed file(s)
- `.devcontainer` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- The GitHub repository was marked archived at selection time.

Commit `9167b325addc7d3520987face684e8230bd62b46` is the revision these paths and observations refer to.
