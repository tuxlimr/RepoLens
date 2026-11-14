# Project structure: public-apis/public-apis

**Analysed commit:** `51bc64abb499c7c532619d89c3f3a083899d3c61`

**Commit reference:** [51bc64abb499c7c532619d89c3f3a083899d3c61](https://github.com/public-apis/public-apis/commit/51bc64abb499c7c532619d89c3f3a083899d3c61)

**Tree at this commit:** [public-apis/public-apis@51bc64abb499](https://github.com/public-apis/public-apis/tree/51bc64abb499c7c532619d89c3f3a083899d3c61)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | public-apis/public-apis |
| Description | A collective list of free APIs |
| Stars | 498993 |
| Forks | 55906 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `51bc64abb499c7c532619d89c3f3a083899d3c61` |
| Retrieved at | 2026-11-14T19:05:59.216600+00:00 |
| Files in this snapshot | 12 |

## Directory tree

```text
scripts/  (8 files)
  tests/  (3 files)
    __init__.py
    test_validate_format.py
    test_validate_links.py
  validate/  (3 files)
    __init__.py
    format.py
    links.py
  github_pull_request.sh
  requirements.txt
.gitattributes
.gitignore
CONTRIBUTING.md
LICENSE
```

## Entry points

- [scripts/validate/format.py:267](https://github.com/public-apis/public-apis/blob/51bc64abb499c7c532619d89c3f3a083899d3c61/scripts/validate/format.py#L267)
- [scripts/validate/links.py:256](https://github.com/public-apis/public-apis/blob/51bc64abb499c7c532619d89c3f3a083899d3c61/scripts/validate/links.py#L256)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: check_alphabetical_order, check_auth, check_cors, check_description, check_duplicate_lin… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 2 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 3 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: FakeResponse, TestValidadeFormat, TestValidateLinks. |

## Important files

- `scripts/requirements.txt` (manifest)

## Top-level layout

- `scripts` — 8 analysed file(s)
- `(root files)` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `51bc64abb499c7c532619d89c3f3a083899d3c61` is the revision these paths and observations refer to.
