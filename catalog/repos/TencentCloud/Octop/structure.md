# Project structure: TencentCloud/Octop

**Analysed commit:** `cd17e8d3551a22e6757f11e030879420243c089f`

**Commit reference:** [cd17e8d3551a22e6757f11e030879420243c089f](https://github.com/TencentCloud/Octop/commit/cd17e8d3551a22e6757f11e030879420243c089f)

**Tree at this commit:** [TencentCloud/Octop@cd17e8d3551a](https://github.com/TencentCloud/Octop/tree/cd17e8d3551a22e6757f11e030879420243c089f)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | TencentCloud/Octop |
| Description | A smarter, self-hosted AI assistant — multi-user, multi-agent. |
| Stars | 12043 |
| Forks | 1691 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `cd17e8d3551a22e6757f11e030879420243c089f` |
| Retrieved at | 2026-11-14T19:10:17.359492+00:00 |
| Files in this snapshot | 799 |

## Directory tree

```text
.cursor/  (1 files)
  skills/  (1 files)
    publish/  (1 files)
      … 1 files under this directory
.githooks/  (1 files)
  pre-commit
.github/  (17 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    config.yml
    feature_request.md
  codeql/  (1 files)
    codeql-config.yml
  workflows/  (11 files)
    anti-spam-issues.yml
    auto-tag-on-release.yml
    ci.yml
    codeql.yml
    docker-publish.yml
    fnos-build-fpk.yml
    octop-desktop.yml
    release.yml
    restrict-pr-authors.yml
    sync-main-to-develop.yml
    upload-release-cos.yml
  pr-author-allowlist.txt
  pull_request_template.md
.vscode/  (2 files)
  css-custom-data.json
  settings.json
dashboard/  (765 files)
  public/  (64 files)
    assets/  (16 files)
      … 16 files under this directory
    experts/  (40 files)
      … 40 files under this directory
    favico.svg
    logo_mark.svg
    logo_vertical_dark.svg
    logo_vertical_white.svg
    manifest.json
    notify-sw.js
    offline.html
    pcm-processor.js
  scripts/  (1 files)
    gen-asset-index.mjs
  src/  (697 files)
    api/  (84 files)
      … 84 files under this directory
    assets/  (77 files)
      … 77 files under this directory
    components/  (162 files)
      … 162 files under this directory
    context/  (8 files)
      … 8 files under this directory
    hooks/  (69 files)
      … 69 files under this directory
    layouts/  (23 files)
      … 23 files under this directory
    pages/  (270 files)
      … 270 files under this directory
    App.tsx
    browserCompatibility.test.ts
    i18n.ts
    main.tsx
  eslint.config.js
  index.html
  package.json
.dockerignore
.env.example
.gitignore
.pre-commit-config.yaml
AGENTS.md
CHANGELOG.md
CONTRIBUTING.md
LICENSE
Makefile
README.md
README_CN.md
SECURITY.md
conftest.py
```

## Entry points

- [dashboard/src/App.tsx](https://github.com/TencentCloud/Octop/blob/cd17e8d3551a22e6757f11e030879420243c089f/dashboard/src/App.tsx)
- [dashboard/src/api/index.ts](https://github.com/TencentCloud/Octop/blob/cd17e8d3551a22e6757f11e030879420243c089f/dashboard/src/api/index.ts)
- [dashboard/src/main.tsx](https://github.com/TencentCloud/Octop/blob/cd17e8d3551a22e6757f11e030879420243c089f/dashboard/src/main.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 84 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| dashboard package | library | Observed | Groups 441 file(s) under dashboard package (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 10 file(s) under data layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.env.example` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/codeql/codeql-config.yml` (config)
- `.github/workflows/anti-spam-issues.yml` (ci)
- `.github/workflows/auto-tag-on-release.yml` (ci)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/codeql.yml` (ci)
- `.github/workflows/docker-publish.yml` (ci)
- `.github/workflows/fnos-build-fpk.yml` (ci)
- `.github/workflows/octop-desktop.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/restrict-pr-authors.yml` (ci)
- `.github/workflows/sync-main-to-develop.yml` (ci)
- `.github/workflows/upload-release-cos.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `.vscode/css-custom-data.json` (config)
- `.vscode/settings.json` (config)
- `dashboard/package.json` (manifest)
- `dashboard/public/manifest.json` (config)

## Top-level layout

- `dashboard` — 765 analysed file(s)
- `.github` — 17 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `.vscode` — 2 analysed file(s)
- `.cursor` — 1 analysed file(s)
- `.githooks` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `cd17e8d3551a22e6757f11e030879420243c089f` is the revision these paths and observations refer to.
