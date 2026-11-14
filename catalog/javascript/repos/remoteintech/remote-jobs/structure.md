# Project structure: remoteintech/remote-jobs

**Analysed commit:** `155939ad935d22afa8edbaaf0770b99f9d0dbf0d`

**Commit reference:** [155939ad935d22afa8edbaaf0770b99f9d0dbf0d](https://github.com/remoteintech/remote-jobs/commit/155939ad935d22afa8edbaaf0770b99f9d0dbf0d)

**Tree at this commit:** [remoteintech/remote-jobs@155939ad935d](https://github.com/remoteintech/remote-jobs/tree/155939ad935d22afa8edbaaf0770b99f9d0dbf0d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | remoteintech/remote-jobs |
| Description | Source for remoteintech.company — a community-maintained directory of remote-friendly tech companies |
| Stars | 41155 |
| Forks | 3970 |
| Licence | Other |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `155939ad935d22afa8edbaaf0770b99f9d0dbf0d` |
| Retrieved at | 2026-11-14T19:10:40.311617+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.github/  (12 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    config.yml
    new_company.md
  scripts/  (1 files)
    validate-companies.js
  workflows/  (3 files)
    ci.yml
    codeql-analysis.yml
    validate-companies.yml
  CODE_OF_CONDUCT.md
  CONTRIBUTING.md
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.MD
  dependabot.yml
scripts/  (3 files)
  README.md
  check-links.sh
  fix-links.mjs
src/  (771 files)
  _config/  (26 files)
    events/  (3 files)
      … 3 files under this directory
    filters/  (9 files)
      … 9 files under this directory
    plugins/  (3 files)
      … 3 files under this directory
    setup/  (2 files)
      … 2 files under this directory
    shortcodes/  (2 files)
      … 2 files under this directory
    utils/  (2 files)
      … 2 files under this directory
    collections.js
    events.js
    filters.js
    plugins.js
    shortcodes.js
  _data/  (16 files)
    designTokens/  (9 files)
      … 9 files under this directory
    changelog.json
    companyHelpers.js
    helpers.js
    labels.js
    meta.js
    navigation.js
    personal.js
  _includes/  (24 files)
    head/  (6 files)
      … 6 files under this directory
    partials/  (12 files)
      … 12 files under this directory
    schemas/  (4 files)
      … 4 files under this directory
    webc/  (2 files)
      … 2 files under this directory
  _layouts/  (5 files)
    base.njk
    company.njk
    page.njk
    post.njk
    tags.njk
  assets/  (76 files)
    css/  (43 files)
      … 43 files under this directory
    images/  (2 files)
      … 2 files under this directory
    scripts/  (8 files)
      … 8 files under this directory
    svg/  (23 files)
      … 23 files under this directory
  blog/  (13 files)
    2017-10-03-announcing-remote-in-tech-company.md
    2017-10-09-so-is-this-just-another-job-board.md
    2017-12-06-popular-company-profiles-and-the-github-traffic-charts.md
    2017-12-28-highest-view-count.md
    2018-01-01-new-year-new-job.md
    2018-01-06-advice-from-a-constant-job-seeker.md
    2018-09-19-website-updates.md
    2018-09-25-hacktoberfest-is-back.md
    2026-01-13-the-big-redesign.md
    2026-01-17-seo-improvements.md
    2026-02-15-keeping-things-tidy.md
    2026-05-07-anatomy-of-a-traffic-spike.md
    blog.json
  common/  (12 files)
    404.njk
    _redirects.njk
    carbon.njk
    feed-atom.njk
    feed-json.njk
    humans.njk
    og-images.njk
    robots.njk
    site-manifest.njk
    sitemap.njk
    tagList.njk
    tags.njk
  companies/  (599 files)
    10up.md
    15five.md
    1password.md
    37signals.md
    3blocks.md
    42-technologies.md
    90-seconds.md
    a-1-auto-transport.md
    abiturma.md
    ably.md
    abstract.md
    acquia.md
    activecampaign.md
    ad-hoc.md
    adaface.md
    addstructure.md
    adeva.md
    adzuna.md
    aerolab.md
    aerostrat.md
    aestudio.md
    aha.md
    aiir.md
    aim-india.md
    … 575 more files
.eleventyignore
.env-sample
.gitignore
.nojekyll
.nvmrc
.prettierignore
.prettierrc
CLAUDE.md
CONTRIBUTING.md
LICENSE
README.md
SECURITY.md
eleventy.config.js
package.json
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| assets package | library | Observed | Groups 8 file(s) under assets package (observed from repository paths and static analysis). |
| companies package | library | Observed | Groups 1 file(s) under companies package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 39 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| _data package | library | Observed | Groups 6 file(s) under _data package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 2 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 2 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/codeql-analysis.yml` (ci)
- `.github/workflows/validate-companies.yml` (ci)
- `package.json` (manifest)
- `src/_data/changelog.json` (config)
- `src/_data/designTokens/borderRadius.json` (config)
- `src/_data/designTokens/colors.json` (config)
- `src/_data/designTokens/colorsBase.json` (config)
- `src/_data/designTokens/fonts.json` (config)
- `src/_data/designTokens/spacing.json` (config)
- `src/_data/designTokens/textLeading.json` (config)
- `src/_data/designTokens/textSizes.json` (config)
- `src/_data/designTokens/textWeights.json` (config)
- `src/_data/designTokens/viewports.json` (config)
- `src/blog/blog.json` (config)
- `src/companies/companies.json` (config)

## Top-level layout

- `src` — 771 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `.github` — 12 analysed file(s)
- `scripts` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `155939ad935d22afa8edbaaf0770b99f9d0dbf0d` is the revision these paths and observations refer to.
