# Project structure: ai-job-search-dev/ai-job-search

**Analysed commit:** `0d0d1a907a21454affa1b694acc4e2c5008a0d21`

**Commit reference:** [0d0d1a907a21454affa1b694acc4e2c5008a0d21](https://github.com/ai-job-search-dev/ai-job-search/commit/0d0d1a907a21454affa1b694acc4e2c5008a0d21)

**Tree at this commit:** [ai-job-search-dev/ai-job-search@0d0d1a907a21](https://github.com/ai-job-search-dev/ai-job-search/tree/0d0d1a907a21454affa1b694acc4e2c5008a0d21)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | ai-job-search-dev/ai-job-search |
| Description | The job search that runs on your machine. AI job application framework built on Claude Code: evaluate postings, tailor CVs, write cover letters, prep interviews. Fork it and own it. |
| Stars | 71723 |
| Forks | 23134 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `0d0d1a907a21454affa1b694acc4e2c5008a0d21` |
| Retrieved at | 2026-11-14T19:06:13.960413+00:00 |
| Files in this snapshot | 296 |

## Directory tree

```text
.agents/  (140 files)
  skills/  (140 files)
    freehire-search/  (20 files)
      … 20 files under this directory
    jobbank-search/  (23 files)
      … 23 files under this directory
    jobdanmark-search/  (26 files)
      … 26 files under this directory
    jobindex-search/  (22 files)
      … 22 files under this directory
    jobnet-search/  (25 files)
      … 25 files under this directory
    linkedin-search/  (24 files)
      … 24 files under this directory
.claude/  (29 files)
  agents/  (3 files)
    application-reviewer.md
    posting-fetcher.md
    posting-scorer.md
  commands/  (12 files)
    add-portal.md
    add-template.md
    apply.md
    expand.md
    gmail-sync.md
    html-report.md
    interview.md
    notion-sync.md
    outcome.md
    rank.md
    reset.md
    setup.md
  skills/  (13 files)
    job-application-assistant/  (10 files)
      … 10 files under this directory
    job-scraper/  (2 files)
      … 2 files under this directory
    upskill/  (1 files)
      … 1 files under this directory
  settings.json
.github/  (8 files)
  ISSUE_TEMPLATE/  (2 files)
    bug-report.md
    config.yml
  workflows/  (3 files)
    ci.yml
    release.yml
    upstream-watch.yml
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
  upstream-wontport.txt
assets/  (4 files)
  readme/  (4 files)
    apply.svg
    hero.svg
    letters.svg
    route.svg
company_research/  (1 files)
  .gitkeep
cover_letters/  (2 files)
  cover.cls
  cover_example.tex
cv/  (1 files)
  main_example.tex
documents/  (8 files)
  applications/  (1 files)
    .gitkeep
  cv/  (1 files)
    .gitkeep
  diplomas/  (1 files)
    .gitkeep
  linkedin/  (1 files)
    .gitkeep
  postings/  (1 files)
    .gitkeep
  projects/  (1 files)
    .gitkeep
  references/  (1 files)
    .gitkeep
  README.md
job_scraper/  (1 files)
  .gitkeep
templates/  (1 files)
  README.md
tests/  (73 files)
  __init__.py
  _bash.py
  _upstream.py
  test_add_portal_command.py
  test_add_template_build_dir.py
  test_apply_host_check.py
  test_apply_page_count.py
  test_apply_records_application.py
  test_bash.py
  test_changelog_structure.py
  test_check_framework_version.py
  test_check_upstream_updates.py
  test_company_research_cache.py
  test_convert_salary_excel.py
  test_convert_salary_excel_integration.py
  test_expand_command.py
  test_fetch_deflate.py
  test_fetch_page.py
  test_gmail_sync_command.py
  test_html_report_command.py
  test_install_portal_clis.py
  test_install_portal_hooks.py
  test_job_key.py
  test_latex_guidance.py
  … 49 more files
tools/  (17 files)
  README_SALARY_TOOL.md
  check_framework_version.py
  check_upstream_updates.py
  convert_salary_excel.py
  fetch_page.py
  install_portal_clis.py
  job_key.py
  lint_skills.py
  page_decode.py
  posting_guard.py
  rank_state.py
  robots_check.py
  scrape_state.py
  security_guards.py
  upstream_triage.py
  verify_layout.py
  verify_pdf.py
upskill/  (1 files)
  .gitkeep
.cz.toml
.gitignore
AGENTS.md
CLAUDE.md
CONTRIBUTING.md
LICENSE
README.md
SECURITY.md
SETUP.md
salary_lookup.py
```

## Entry points

- [salary_lookup.py:479](https://github.com/ai-job-search-dev/ai-job-search/blob/0d0d1a907a21454affa1b694acc4e2c5008a0d21/salary_lookup.py#L479)
- [tools/check_framework_version.py:161](https://github.com/ai-job-search-dev/ai-job-search/blob/0d0d1a907a21454affa1b694acc4e2c5008a0d21/tools/check_framework_version.py#L161)
- [tools/check_upstream_updates.py:216](https://github.com/ai-job-search-dev/ai-job-search/blob/0d0d1a907a21454affa1b694acc4e2c5008a0d21/tools/check_upstream_updates.py#L216)
- [tools/convert_salary_excel.py:490](https://github.com/ai-job-search-dev/ai-job-search/blob/0d0d1a907a21454affa1b694acc4e2c5008a0d21/tools/convert_salary_excel.py#L490)
- [tools/fetch_page.py:326](https://github.com/ai-job-search-dev/ai-job-search/blob/0d0d1a907a21454affa1b694acc4e2c5008a0d21/tools/fetch_page.py#L326)
- [tools/install_portal_clis.py:158](https://github.com/ai-job-search-dev/ai-job-search/blob/0d0d1a907a21454affa1b694acc4e2c5008a0d21/tools/install_portal_clis.py#L158)
- [tools/job_key.py:393](https://github.com/ai-job-search-dev/ai-job-search/blob/0d0d1a907a21454affa1b694acc4e2c5008a0d21/tools/job_key.py#L393)
- [tools/lint_skills.py:121](https://github.com/ai-job-search-dev/ai-job-search/blob/0d0d1a907a21454affa1b694acc4e2c5008a0d21/tools/lint_skills.py#L121)
- [tools/posting_guard.py:580](https://github.com/ai-job-search-dev/ai-job-search/blob/0d0d1a907a21454affa1b694acc4e2c5008a0d21/tools/posting_guard.py#L580)
- [tools/rank_state.py:567](https://github.com/ai-job-search-dev/ai-job-search/blob/0d0d1a907a21454affa1b694acc4e2c5008a0d21/tools/rank_state.py#L567)
- [tools/robots_check.py:227](https://github.com/ai-job-search-dev/ai-job-search/blob/0d0d1a907a21454affa1b694acc4e2c5008a0d21/tools/robots_check.py#L227)
- [tools/scrape_state.py:170](https://github.com/ai-job-search-dev/ai-job-search/blob/0d0d1a907a21454affa1b694acc4e2c5008a0d21/tools/scrape_state.py#L170)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Application entry point | entrypoint | Observed | Groups 16 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Line, Page, VerificationError, _NoRedirects. Observed top-level functions: _attrs, _bare_… |
| Tests | test | Observed | Groups 156 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH tools.verify_pdf._extract_pypdf, PATCH tools.verify_pdf.run_tool, PATCH tools.verify_pdf._extract_pypdf, PATCH… |
| tools package | library | Observed | Groups 1 file(s) under tools package (observed from repository paths and static analysis). Observed top-level functions: declared_codec, decode_page. |

## Important files

- `.agents/skills/freehire-search/cli/package.json` (manifest)
- `.agents/skills/freehire-search/cli/tsconfig.json` (config)
- `.agents/skills/jobbank-search/cli/package.json` (manifest)
- `.agents/skills/jobbank-search/cli/tsconfig.json` (config)
- `.agents/skills/jobdanmark-search/cli/package.json` (manifest)
- `.agents/skills/jobdanmark-search/cli/tsconfig.json` (config)
- `.agents/skills/jobindex-search/cli/package.json` (manifest)
- `.agents/skills/jobindex-search/cli/tsconfig.json` (config)
- `.agents/skills/jobnet-search/cli/package.json` (manifest)
- `.agents/skills/jobnet-search/cli/tsconfig.json` (config)
- `.agents/skills/linkedin-search/cli/package.json` (manifest)
- `.agents/skills/linkedin-search/cli/tsconfig.json` (config)
- `.claude/settings.json` (config)
- `.cz.toml` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/upstream-watch.yml` (ci)

## Top-level layout

- `.agents` — 140 analysed file(s)
- `tests` — 73 analysed file(s)
- `.claude` — 29 analysed file(s)
- `tools` — 17 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `.github` — 8 analysed file(s)
- `documents` — 8 analysed file(s)
- `assets` — 4 analysed file(s)
- `cover_letters` — 2 analysed file(s)
- `company_research` — 1 analysed file(s)
- `cv` — 1 analysed file(s)
- `job_scraper` — 1 analysed file(s)
- `templates` — 1 analysed file(s)
- `upskill` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `0d0d1a907a21454affa1b694acc4e2c5008a0d21` is the revision these paths and observations refer to.
