# Project structure: m3y54m/Embedded-Engineering-Roadmap

**Analysed commit:** `792e6cdf6cd4233c6fbd99c65c1236e5637da363`

**Commit reference:** [792e6cdf6cd4233c6fbd99c65c1236e5637da363](https://github.com/m3y54m/Embedded-Engineering-Roadmap/commit/792e6cdf6cd4233c6fbd99c65c1236e5637da363)

**Tree at this commit:** [m3y54m/Embedded-Engineering-Roadmap@792e6cdf6cd4](https://github.com/m3y54m/Embedded-Engineering-Roadmap/tree/792e6cdf6cd4233c6fbd99c65c1236e5637da363)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | m3y54m/Embedded-Engineering-Roadmap |
| Description | Comprehensive roadmap for aspiring Embedded Systems Engineers, featuring a curated list of learning resources |
| Stars | 13899 |
| Forks | 1363 |
| Licence | CC-BY-SA-4.0 |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `792e6cdf6cd4233c6fbd99c65c1236e5637da363` |
| Retrieved at | 2026-11-14T19:11:48.991601+00:00 |
| Files in this snapshot | 35 |

## Directory tree

```text
.github/  (12 files)
  ISSUE_TEMPLATE/  (3 files)
    config.yml
    report-link-problem.yml
    suggest-resource.yml
  scripts/  (2 files)
    check_readme.py
    next-version.sh
  workflows/  (3 files)
    link-check.yml
    markdown-lint.yml
    pages.yml
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
  lychee.toml
explorer/  (17 files)
  assets/  (2 files)
    cc-by-sa.svg
    logo.svg
  fonts/  (1 files)
    OFL.txt
  tools/  (2 files)
    coverage.mjs
    render.mjs
  app.js
  diagram.js
  dom.js
  index.html
  layout.js
  map.css
  map.json
  mapview.js
  parser.js
  parser.test.mjs
  sitemap.xml
  styles.css
.gitignore
.markdownlint.json
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
```

## Entry points

- [.github/scripts/check_readme.py:46](https://github.com/m3y54m/Embedded-Engineering-Roadmap/blob/792e6cdf6cd4233c6fbd99c65c1236e5637da363/.github/scripts/check_readme.py#L46)
- [explorer/app.js](https://github.com/m3y54m/Embedded-Engineering-Roadmap/blob/792e6cdf6cd4233c6fbd99c65c1236e5637da363/explorer/app.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| explorer package | library | Observed | Groups 9 file(s) under explorer package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/report-link-problem.yml` (config)
- `.github/ISSUE_TEMPLATE/suggest-resource.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/lychee.toml` (config)
- `.github/workflows/link-check.yml` (ci)
- `.github/workflows/markdown-lint.yml` (ci)
- `.github/workflows/pages.yml` (ci)
- `.markdownlint.json` (config)
- `explorer/map.json` (config)

## Top-level layout

- `explorer` — 17 analysed file(s)
- `.github` — 12 analysed file(s)
- `(root files)` — 6 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `792e6cdf6cd4233c6fbd99c65c1236e5637da363` is the revision these paths and observations refer to.
