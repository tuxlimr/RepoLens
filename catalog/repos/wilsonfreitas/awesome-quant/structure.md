# Project structure: wilsonfreitas/awesome-quant

**Analysed commit:** `f7230363d2b5d8a43244144646c14978dc375016`

**Commit reference:** [f7230363d2b5d8a43244144646c14978dc375016](https://github.com/wilsonfreitas/awesome-quant/commit/f7230363d2b5d8a43244144646c14978dc375016)

**Tree at this commit:** [wilsonfreitas/awesome-quant@f7230363d2b5](https://github.com/wilsonfreitas/awesome-quant/tree/f7230363d2b5d8a43244144646c14978dc375016)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | wilsonfreitas/awesome-quant |
| Description | A curated list of insanely awesome libraries, packages and resources for Quants (Quantitative Finance) |
| Stars | 30637 |
| Forks | 4364 |
| Licence | Not detected |
| Language | Python |
| Default branch | main |
| Analysed commit | `f7230363d2b5d8a43244144646c14978dc375016` |
| Retrieved at | 2026-11-14T19:07:09.460773+00:00 |
| Files in this snapshot | 45 |

## Directory tree

```text
.agents/  (6 files)
  skills/  (6 files)
    bprr/  (1 files)
      … 1 files under this directory
    create-entry/  (1 files)
      … 1 files under this directory
    sprr/  (1 files)
      … 1 files under this directory
    update-pypi-dates/  (3 files)
      … 3 files under this directory
.github/  (5 files)
  workflows/  (5 files)
    build.yml
    pr-review.yml
    pr-validate.yml
    readme-audit.yml
    tests.yml
docs/  (1 files)
  codex-setup.md
scripts/  (6 files)
  audit_readme.py
  pypi_metadata.py
  readme_entries.py
  review_pr.py
  url_probe.py
  validate_readme.py
site/  (4 files)
  static/  (2 files)
    main.js
    style.css
  .nojekyll
  generate.py
tests/  (15 files)
  __init__.py
  test_audit_readme.py
  test_historical_projects.py
  test_manual_tools.py
  test_nested_reference_repairs.py
  test_pr_review_workflow.py
  test_pypi_date_updater.py
  test_pypi_metadata.py
  test_readme_audit_workflow.py
  test_readme_entries.py
  test_review_documentation.py
  test_review_pr.py
  test_site_generation.py
  test_test_workflow.py
  test_url_probe.py
.gitignore
AGENTS.md
CONTRIBUTING.md
README.md
cranscrape.py
parse.py
pyproject.toml
topic.py
```

## Entry points

- [.agents/skills/update-pypi-dates/scripts/check_pypi_dates.py:92](https://github.com/wilsonfreitas/awesome-quant/blob/f7230363d2b5d8a43244144646c14978dc375016/.agents/skills/update-pypi-dates/scripts/check_pypi_dates.py#L92)
- [cranscrape.py:84](https://github.com/wilsonfreitas/awesome-quant/blob/f7230363d2b5d8a43244144646c14978dc375016/cranscrape.py#L84)
- [parse.py:253](https://github.com/wilsonfreitas/awesome-quant/blob/f7230363d2b5d8a43244144646c14978dc375016/parse.py#L253)
- [scripts/audit_readme.py:538](https://github.com/wilsonfreitas/awesome-quant/blob/f7230363d2b5d8a43244144646c14978dc375016/scripts/audit_readme.py#L538)
- [scripts/review_pr.py:884](https://github.com/wilsonfreitas/awesome-quant/blob/f7230363d2b5d8a43244144646c14978dc375016/scripts/review_pr.py#L884)
- [scripts/validate_readme.py:395](https://github.com/wilsonfreitas/awesome-quant/blob/f7230363d2b5d8a43244144646c14978dc375016/scripts/validate_readme.py#L395)
- [site/generate.py:439](https://github.com/wilsonfreitas/awesome-quant/blob/f7230363d2b5d8a43244144646c14978dc375016/site/generate.py#L439)
- [topic.py:24](https://github.com/wilsonfreitas/awesome-quant/blob/f7230363d2b5d8a43244144646c14978dc375016/topic.py#L24)
- [site/static/main.js](https://github.com/wilsonfreitas/awesome-quant/blob/f7230363d2b5d8a43244144646c14978dc375016/site/static/main.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 7 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: AuditTarget, Candidate, Finding, FindingKind, Issue, PinnedHTTPSConnection. Observed top-l… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 3 file(s) under scripts package (observed from repository paths and static analysis). Observed top-level classes: Outcome, RawResponse, ReadmeEntry, UnsafeUrlError, UrlObservation, _PinnedHTTPConnection. Observed… |
| site package | library | Observed | Groups 1 file(s) under site package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 15 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: AuditReadmeMainTests, AuditReadmeTests, FakeBaseRepository, FakeClient, FakeGithubClient, FakeIssue. Observ… |

## Important files

- `.github/workflows/build.yml` (ci)
- `.github/workflows/pr-review.yml` (ci)
- `.github/workflows/pr-validate.yml` (ci)
- `.github/workflows/readme-audit.yml` (ci)
- `.github/workflows/tests.yml` (ci)
- `pyproject.toml` (manifest)

## Top-level layout

- `tests` — 15 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `.agents` — 6 analysed file(s)
- `scripts` — 6 analysed file(s)
- `.github` — 5 analysed file(s)
- `site` — 4 analysed file(s)
- `docs` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `f7230363d2b5d8a43244144646c14978dc375016` is the revision these paths and observations refer to.
