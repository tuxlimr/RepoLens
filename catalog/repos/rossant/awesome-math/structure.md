# Project structure: rossant/awesome-math

**Analysed commit:** `6f1cb9e5990cde9ca75af90b6d447aa778535c4b`

**Commit reference:** [6f1cb9e5990cde9ca75af90b6d447aa778535c4b](https://github.com/rossant/awesome-math/commit/6f1cb9e5990cde9ca75af90b6d447aa778535c4b)

**Tree at this commit:** [rossant/awesome-math@6f1cb9e5990c](https://github.com/rossant/awesome-math/tree/6f1cb9e5990cde9ca75af90b6d447aa778535c4b)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | rossant/awesome-math |
| Description | A curated list of awesome mathematics resources |
| Stars | 16961 |
| Forks | 1655 |
| Licence | CC0-1.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `6f1cb9e5990cde9ca75af90b6d447aa778535c4b` |
| Retrieved at | 2026-11-14T19:08:38.999106+00:00 |
| Files in this snapshot | 10 |

## Directory tree

```text
.github/  (5 files)
  ISSUE_TEMPLATE/  (3 files)
    config.yml
    maintenance.yml
    resource.yml
  workflows/  (1 files)
    validate.yml
  PULL_REQUEST_TEMPLATE.md
scripts/  (1 files)
  validate.py
CONTRIBUTING.md
LICENSE
README.md
build_toc.py
```

## Entry points

- [build_toc.py:66](https://github.com/rossant/awesome-math/blob/6f1cb9e5990cde9ca75af90b6d447aa778535c4b/build_toc.py#L66)
- [scripts/validate.py:89](https://github.com/rossant/awesome-math/blob/6f1cb9e5990cde9ca75af90b6d447aa778535c4b/scripts/validate.py#L89)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: _anchor, _gen_items, _get_header_item, _iter_headers, _parse_header, _read_md. |

## Important files

- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/maintenance.yml` (config)
- `.github/ISSUE_TEMPLATE/resource.yml` (config)
- `.github/workflows/validate.yml` (ci)

## Top-level layout

- `.github` — 5 analysed file(s)
- `(root files)` — 4 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `6f1cb9e5990cde9ca75af90b6d447aa778535c4b` is the revision these paths and observations refer to.
