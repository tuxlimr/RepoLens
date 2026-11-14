# Project structure: anuraghazra/github-readme-stats

**Analysed commit:** `54a7985aeefda00d5eadb55b80c17c7f976c37d2`

**Commit reference:** [54a7985aeefda00d5eadb55b80c17c7f976c37d2](https://github.com/anuraghazra/github-readme-stats/commit/54a7985aeefda00d5eadb55b80c17c7f976c37d2)

**Tree at this commit:** [anuraghazra/github-readme-stats@54a7985aeefd](https://github.com/anuraghazra/github-readme-stats/tree/54a7985aeefda00d5eadb55b80c17c7f976c37d2)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | anuraghazra/github-readme-stats |
| Description | :zap: Dynamically generated stats for your github readmes |
| Stars | 79842 |
| Forks | 38282 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `54a7985aeefda00d5eadb55b80c17c7f976c37d2` |
| Retrieved at | 2026-11-14T19:10:33.175516+00:00 |
| Files in this snapshot | 131 |

## Directory tree

```text
.devcontainer/  (1 files)
  devcontainer.json
.github/  (23 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.yml
    config.yml
    feature_request.yml
  workflows/  (15 files)
    codeql-analysis.yml
    deploy-prep.py
    deploy-prep.yml
    e2e-test.yml
    empty-issues-closer.yml
    generate-theme-doc.yml
    label-pr.yml
    ossf-analysis.yml
    preview-theme.yml
    prs-cache-clean.yml
    stale-theme-pr-closer.yml
    test.yml
    theme-prs-closer.yml
    top-issues-dashboard.yml
    update-langs.yml
  CODEOWNERS
  FUNDING.yml
  dependabot.yml
  labeler.yml
  stale.yml
.husky/  (2 files)
  .gitignore
  pre-commit
.vscode/  (2 files)
  extensions.json
  settings.json
api/  (7 files)
  status/  (2 files)
    pat-info.js
    up.js
  gist.js
  index.js
  pin.js
  top-langs.js
  wakatime.js
scripts/  (6 files)
  close-stale-theme-prs.js
  generate-langs-json.js
  generate-theme-doc.js
  helpers.js
  preview-theme.js
  push-theme-readme.sh
src/  (34 files)
  cards/  (7 files)
    gist.js
    index.js
    repo.js
    stats.js
    top-languages.js
    types.d.ts
    wakatime.js
  common/  (18 files)
    Card.js
    I18n.js
    access.js
    blacklist.js
    cache.js
    color.js
    envs.js
    error.js
    fmt.js
    html.js
    http.js
    icons.js
    index.js
    languageColors.json
    log.js
    ops.js
    render.js
    retryer.js
  fetchers/  (6 files)
    gist.js
    repo.js
    stats.js
    top-languages.js
    types.d.ts
    wakatime.js
  calculateRank.js
  index.js
  translations.js
tests/  (34 files)
  __snapshots__/  (1 files)
    renderWakatimeCard.test.js.snap
  bench/  (5 files)
    api.bench.js
    calculateRank.bench.js
    gist.bench.js
    pin.bench.js
    utils.js
  e2e/  (1 files)
    e2e.test.js
  api.test.js
  calculateRank.test.js
  card.test.js
  color.test.js
  fetchGist.test.js
  fetchRepo.test.js
  fetchStats.test.js
  fetchTopLanguages.test.js
  fetchWakatime.test.js
  flexLayout.test.js
  fmt.test.js
  gist.test.js
  html.test.js
  i18n.test.js
  ops.test.js
  pat-info.test.js
  pin.test.js
  render.test.js
  renderGistCard.test.js
  renderRepoCard.test.js
  renderStatsCard.test.js
  renderTopLanguagesCard.test.js
  renderWakatimeCard.test.js
  retryer.test.js
  … 3 more files
themes/  (2 files)
  README.md
  index.js
.eslintrc.json
.gitignore
.nvmrc
.prettierignore
.prettierrc.json
.vercelignore
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
SECURITY.md
codecov.yml
eslint.config.mjs
express.js
jest.bench.config.js
jest.config.js
jest.e2e.config.js
package.json
powered-by-vercel.svg
readme.md
vercel.json
```

## Entry points

- [src/index.js](https://github.com/anuraghazra/github-readme-stats/blob/54a7985aeefda00d5eadb55b80c17c7f976c37d2/src/index.js)
- [api/index.js](https://github.com/anuraghazra/github-readme-stats/blob/54a7985aeefda00d5eadb55b80c17c7f976c37d2/api/index.js)
- [src/cards/index.js](https://github.com/anuraghazra/github-readme-stats/blob/54a7985aeefda00d5eadb55b80c17c7f976c37d2/src/cards/index.js)
- [src/common/index.js](https://github.com/anuraghazra/github-readme-stats/blob/54a7985aeefda00d5eadb55b80c17c7f976c37d2/src/common/index.js)
- [themes/index.js](https://github.com/anuraghazra/github-readme-stats/blob/54a7985aeefda00d5eadb55b80c17c7f976c37d2/themes/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 7 file(s) under api layer (observed from repository paths and static analysis). |
| calculateRank.js package | library | Observed | Groups 1 file(s) under calculaterank.js package (observed from repository paths and static analysis). |
| cards package | library | Observed | Groups 7 file(s) under cards package (observed from repository paths and static analysis). |
| common package | library | Observed | Groups 17 file(s) under common package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 5 file(s) under core modules (observed from repository paths and static analysis). |
| fetchers package | library | Observed | Groups 6 file(s) under fetchers package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 6 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 34 file(s) under tests (observed from repository paths and static analysis). |
| themes package | library | Observed | Groups 1 file(s) under themes package (observed from repository paths and static analysis). |
| translations.js package | library | Observed | Groups 1 file(s) under translations.js package (observed from repository paths and static analysis). |

## Important files

- `.devcontainer/devcontainer.json` (config)
- `.eslintrc.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/labeler.yml` (config)
- `.github/stale.yml` (config)
- `.github/workflows/codeql-analysis.yml` (ci)
- `.github/workflows/deploy-prep.py` (ci)
- `.github/workflows/deploy-prep.yml` (ci)
- `.github/workflows/e2e-test.yml` (ci)
- `.github/workflows/empty-issues-closer.yml` (ci)
- `.github/workflows/generate-theme-doc.yml` (ci)
- `.github/workflows/label-pr.yml` (ci)
- `.github/workflows/ossf-analysis.yml` (ci)
- `.github/workflows/preview-theme.yml` (ci)
- `.github/workflows/prs-cache-clean.yml` (ci)
- `.github/workflows/stale-theme-pr-closer.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `.github/workflows/theme-prs-closer.yml` (ci)
- `.github/workflows/top-issues-dashboard.yml` (ci)
- `.github/workflows/update-langs.yml` (ci)
- `.prettierrc.json` (config)
- `.vscode/extensions.json` (config)
- `.vscode/settings.json` (config)
- `codecov.yml` (config)
- `package.json` (manifest)
- `src/common/languageColors.json` (config)
- `vercel.json` (config)

## Top-level layout

- `src` — 34 analysed file(s)
- `tests` — 34 analysed file(s)
- `.github` — 23 analysed file(s)
- `(root files)` — 20 analysed file(s)
- `api` — 7 analysed file(s)
- `scripts` — 6 analysed file(s)
- `.husky` — 2 analysed file(s)
- `.vscode` — 2 analysed file(s)
- `themes` — 2 analysed file(s)
- `.devcontainer` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `54a7985aeefda00d5eadb55b80c17c7f976c37d2` is the revision these paths and observations refer to.
