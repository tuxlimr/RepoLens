# Project structure: microsoft/markitdown

**Analysed commit:** `ed178952a6672abdfd35b5f9e76a80b6cefc086e`

**Commit reference:** [ed178952a6672abdfd35b5f9e76a80b6cefc086e](https://github.com/microsoft/markitdown/commit/ed178952a6672abdfd35b5f9e76a80b6cefc086e)

**Tree at this commit:** [microsoft/markitdown@ed178952a667](https://github.com/microsoft/markitdown/tree/ed178952a6672abdfd35b5f9e76a80b6cefc086e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | microsoft/markitdown |
| Description | Python tool for converting files and office documents to Markdown. |
| Stars | 195364 |
| Forks | 14757 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `ed178952a6672abdfd35b5f9e76a80b6cefc086e` |
| Retrieved at | 2026-11-14T19:06:00.907521+00:00 |
| Files in this snapshot | 136 |

## Directory tree

```text
.devcontainer/  (1 files)
  devcontainer.json
.github/  (5 files)
  actions/  (1 files)
    build-arm-cryptography/  (1 files)
      … 1 files under this directory
  workflows/  (2 files)
    pre-commit.yml
    tests.yml
  constraints.txt
  dependabot.yml
packages/  (120 files)
  markitdown/  (80 files)
    src/  (42 files)
      … 42 files under this directory
    tests/  (35 files)
      … 35 files under this directory
    README.md
    ThirdPartyNotices.md
    pyproject.toml
  markitdown-mcp/  (11 files)
    src/  (4 files)
      … 4 files under this directory
    tests/  (4 files)
      … 4 files under this directory
    Dockerfile
    README.md
    pyproject.toml
  markitdown-ocr/  (20 files)
    src/  (8 files)
      … 8 files under this directory
    tests/  (9 files)
      … 9 files under this directory
    LICENSE
    README.md
    pyproject.toml
  markitdown-sample-plugin/  (9 files)
    src/  (4 files)
      … 4 files under this directory
    tests/  (3 files)
      … 3 files under this directory
    README.md
    pyproject.toml
.dockerignore
.gitattributes
.gitignore
.pre-commit-config.yaml
CODE_OF_CONDUCT.md
Dockerfile
LICENSE
README.md
SECURITY.md
SUPPORT.md
```

## Entry points

- [packages/markitdown-mcp/src/markitdown_mcp/__main__.py:138](https://github.com/microsoft/markitdown/blob/ed178952a6672abdfd35b5f9e76a80b6cefc086e/packages/markitdown-mcp/src/markitdown_mcp/__main__.py#L138)
- [packages/markitdown/src/markitdown/__main__.py:327](https://github.com/microsoft/markitdown/blob/ed178952a6672abdfd35b5f9e76a80b6cefc086e/packages/markitdown/src/markitdown/__main__.py#L327)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: _exit_with_error, _handle_output, check_plugins_enabled, convert_to_markdown, create_sta… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 52 file(s) under packages package (observed from repository paths and static analysis). Observed top-level classes: AudioConverter, BingSerpConverter, ContentUnderstandingConverter, ContentUnderstandingFileType,… |
| Service / domain layer | service | Observed | Groups 1 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: LLMVisionOCRService, OCRResult. Observed top-level functions: _extract_text_with_metadata. |
| Tests | test | Observed | Groups 51 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: FileTestVector, MockOCRService, TestAcceptsExtension, TestAcceptsFileTypeRestriction, TestAcceptsMime, Test… |

## Important files

- `.devcontainer/devcontainer.json` (config)
- `.dockerignore` (container)
- `.github/actions/build-arm-cryptography/action.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/pre-commit.yml` (ci)
- `.github/workflows/tests.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `Dockerfile` (container)
- `packages/markitdown-mcp/Dockerfile` (container)
- `packages/markitdown-mcp/pyproject.toml` (manifest)
- `packages/markitdown-ocr/pyproject.toml` (manifest)
- `packages/markitdown-sample-plugin/pyproject.toml` (manifest)
- `packages/markitdown/pyproject.toml` (manifest)

## Top-level layout

- `packages` — 120 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `.github` — 5 analysed file(s)
- `.devcontainer` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `ed178952a6672abdfd35b5f9e76a80b6cefc086e` is the revision these paths and observations refer to.
