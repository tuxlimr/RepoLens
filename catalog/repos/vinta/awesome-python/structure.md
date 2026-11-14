# Project structure: vinta/awesome-python

**Analysed commit:** `234dee17f146c30669fe44bac81eda8114727d02`

**Commit reference:** [234dee17f146c30669fe44bac81eda8114727d02](https://github.com/vinta/awesome-python/commit/234dee17f146c30669fe44bac81eda8114727d02)

**Tree at this commit:** [vinta/awesome-python@234dee17f146](https://github.com/vinta/awesome-python/tree/234dee17f146c30669fe44bac81eda8114727d02)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | vinta/awesome-python |
| Description | The definitive list that answers "I want to do X in Python, which tool should I use?" |
| Stars | 334732 |
| Forks | 29103 |
| Licence | Other |
| Language | Python |
| Default branch | master |
| Analysed commit | `234dee17f146c30669fe44bac81eda8114727d02` |
| Retrieved at | 2026-11-14T19:05:59.932724+00:00 |
| Files in this snapshot | 127 |

## Directory tree

```text
.claude/  (7 files)
  skills/  (7 files)
    audit-the-list/  (2 files)
      … 2 files under this directory
    preview-verdicts/  (2 files)
      … 2 files under this directory
    review-prs/  (1 files)
      … 1 files under this directory
    scan-github-stars/  (2 files)
      … 2 files under this directory
.github/  (4 files)
  workflows/  (2 files)
    ci.yml
    deploy-website.yml
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
docs/  (2 files)
  adr/  (1 files)
    0001-shortlist-not-catalog.md
  audit-logs.md
website/  (103 files)
  data/  (76 files)
    category_intros/  (74 files)
      … 74 files under this directory
    pypi_name_overrides.json
    redirects.json
  static/  (4 files)
    favicon.svg
    main.js
    og-image.svg
    style.css
  templates/  (12 files)
    _category_nav.html
    _entry_rows.html
    _final_cta.html
    _projects_table.html
    _sponsor_band.html
    _topbar.html
    base.html
    category.html
    index.html
    llms.txt
    redirect.html
    sponsorship.html
  tests/  (5 files)
    test_build.py
    test_fetch_github_stars.py
    test_preview_verdicts.py
    test_readme_parser.py
    test_scan_github_stars.py
  build.py
  fetch_github_stars.py
  fetch_pypi_downloads_via_bigquery.py
  fetch_pypi_downloads_via_clickpy.py
  fetch_pypi_downloads_via_pepy.py
  readme_parser.py
.gitignore
AGENTS.md
CLAUDE.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
DESIGN.md
LICENSE
Makefile
README.md
SPONSORSHIP.md
pyproject.toml
```

## Entry points

- [.claude/skills/audit-the-list/scripts/audit_priority.py:127](https://github.com/vinta/awesome-python/blob/234dee17f146c30669fe44bac81eda8114727d02/.claude/skills/audit-the-list/scripts/audit_priority.py#L127)
- [.claude/skills/scan-github-stars/scripts/scan_github_stars.py:157](https://github.com/vinta/awesome-python/blob/234dee17f146c30669fe44bac81eda8114727d02/.claude/skills/scan-github-stars/scripts/scan_github_stars.py#L157)
- [website/build.py:1042](https://github.com/vinta/awesome-python/blob/234dee17f146c30669fe44bac81eda8114727d02/website/build.py#L1042)
- [website/fetch_github_stars.py:179](https://github.com/vinta/awesome-python/blob/234dee17f146c30669fe44bac81eda8114727d02/website/fetch_github_stars.py#L179)
- [website/fetch_pypi_downloads_via_bigquery.py:81](https://github.com/vinta/awesome-python/blob/234dee17f146c30669fe44bac81eda8114727d02/website/fetch_pypi_downloads_via_bigquery.py#L81)
- [website/fetch_pypi_downloads_via_clickpy.py:107](https://github.com/vinta/awesome-python/blob/234dee17f146c30669fe44bac81eda8114727d02/website/fetch_pypi_downloads_via_clickpy.py#L107)
- [website/fetch_pypi_downloads_via_pepy.py:75](https://github.com/vinta/awesome-python/blob/234dee17f146c30669fe44bac81eda8114727d02/website/fetch_pypi_downloads_via_pepy.py#L75)
- [website/static/main.js](https://github.com/vinta/awesome-python/blob/234dee17f146c30669fe44bac81eda8114727d02/website/static/main.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 5 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: EntryGroup, SyntheticCategory, TemplateEntry, TemplateSubcategory. Observed top-level func… |
| Tests | test | Observed | Groups 5 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: HeadMetadataParser, TestAnnotateEntriesWithStats, TestBuild, TestBuildGraphqlQuery, TestDetectSourceType, Te… |
| website package | library | Observed | Groups 2 file(s) under website package (observed from repository paths and static analysis). Observed top-level classes: AlsoSee, ParsedEntry, ParsedGroup, ParsedSection, ParsedSponsor. Observed top-level functions: _bu… |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/deploy-website.yml` (ci)
- `pyproject.toml` (manifest)
- `website/data/pypi_name_overrides.json` (config)
- `website/data/redirects.json` (config)

## Top-level layout

- `website` — 103 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `.claude` — 7 analysed file(s)
- `.github` — 4 analysed file(s)
- `docs` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `234dee17f146c30669fe44bac81eda8114727d02` is the revision these paths and observations refer to.
