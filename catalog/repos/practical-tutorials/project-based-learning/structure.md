# Project structure: practical-tutorials/project-based-learning

**Analysed commit:** `322fb30147c809574ed71d1c34e3480e80a6b0e8`

**Commit reference:** [322fb30147c809574ed71d1c34e3480e80a6b0e8](https://github.com/practical-tutorials/project-based-learning/commit/322fb30147c809574ed71d1c34e3480e80a6b0e8)

**Tree at this commit:** [practical-tutorials/project-based-learning@322fb30147c8](https://github.com/practical-tutorials/project-based-learning/tree/322fb30147c809574ed71d1c34e3480e80a6b0e8)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | practical-tutorials/project-based-learning |
| Description | Curated list of project-based tutorials |
| Stars | 289744 |
| Forks | 36838 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `322fb30147c809574ed71d1c34e3480e80a6b0e8` |
| Retrieved at | 2026-11-14T19:05:59.718663+00:00 |
| Files in this snapshot | 14 |

## Directory tree

```text
.github/  (8 files)
  ISSUE_TEMPLATE/  (3 files)
    1-broken-link.yml
    2-tutorial-suggestion.yml
    config.yml
  workflows/  (3 files)
    link-rot.yml
    stale-prs.yml
    validate-pr.yml
  PULL_REQUEST_TEMPLATE.md
  link-rot-state.json
scripts/  (3 files)
  check_readme.py
  linkcheck-domains.txt
  lint-allow-duplicates.txt
CONTRIBUTING.md
LICENSE.md
README.md
```

## Entry points

- [scripts/check_readme.py:1177](https://github.com/practical-tutorials/project-based-learning/blob/322fb30147c809574ed71d1c34e3480e80a6b0e8/scripts/check_readme.py#L1177)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Diagnostic, Document, DomainLimiter, Entry, Header, _TitleExtractor. Observed top-level fu… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |

## Important files

- `.github/ISSUE_TEMPLATE/1-broken-link.yml` (config)
- `.github/ISSUE_TEMPLATE/2-tutorial-suggestion.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/link-rot-state.json` (config)
- `.github/workflows/link-rot.yml` (ci)
- `.github/workflows/stale-prs.yml` (ci)
- `.github/workflows/validate-pr.yml` (ci)

## Top-level layout

- `.github` — 8 analysed file(s)
- `(root files)` — 3 analysed file(s)
- `scripts` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `322fb30147c809574ed71d1c34e3480e80a6b0e8` is the revision these paths and observations refer to.
