# Project structure: owainlewis/awesome-artificial-intelligence

**Analysed commit:** `ab1c3cceef8ab906586505a7a7a293f434280862`

**Commit reference:** [ab1c3cceef8ab906586505a7a7a293f434280862](https://github.com/owainlewis/awesome-artificial-intelligence/commit/ab1c3cceef8ab906586505a7a7a293f434280862)

**Tree at this commit:** [owainlewis/awesome-artificial-intelligence@ab1c3cceef8a](https://github.com/owainlewis/awesome-artificial-intelligence/tree/ab1c3cceef8ab906586505a7a7a293f434280862)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | owainlewis/awesome-artificial-intelligence |
| Description | A curated list of Artificial Intelligence (AI) courses, books, video lectures and papers. |
| Stars | 16839 |
| Forks | 2576 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `ab1c3cceef8ab906586505a7a7a293f434280862` |
| Retrieved at | 2026-11-14T19:08:41.113171+00:00 |
| Files in this snapshot | 18 |

## Directory tree

```text
.github/  (7 files)
  ISSUE_TEMPLATE/  (2 files)
    config.yml
    resource.yml
  codex/  (3 files)
    prompts/  (2 files)
      … 2 files under this directory
    schemas/  (1 files)
      … 1 files under this directory
  workflows/  (1 files)
    quality.yml
  pull_request_template.md
archive/  (1 files)
  README.md
docs/  (1 files)
  weekly-curation/  (1 files)
    design.md
scripts/  (1 files)
  validate_readme.py
tests/  (1 files)
  test_validate_readme.py
.python-version
AUTOMATION.md
CONTRIBUTING.md
CURATION.md
LICENSE
README.md
pyproject.toml
```

## Entry points

- [scripts/validate_readme.py:250](https://github.com/owainlewis/awesome-artificial-intelligence/blob/ab1c3cceef8ab906586505a7a7a293f434280862/scripts/validate_readme.py#L250)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Resource. Observed top-level functions: check_link, check_links, classify_exception, class… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: ValidateReadmeTests. |

## Important files

- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/resource.yml` (config)
- `.github/codex/schemas/curation-review.schema.json` (config)
- `.github/workflows/quality.yml` (ci)
- `pyproject.toml` (manifest)

## Top-level layout

- `(root files)` — 7 analysed file(s)
- `.github` — 7 analysed file(s)
- `archive` — 1 analysed file(s)
- `docs` — 1 analysed file(s)
- `scripts` — 1 analysed file(s)
- `tests` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `ab1c3cceef8ab906586505a7a7a293f434280862` is the revision these paths and observations refer to.
