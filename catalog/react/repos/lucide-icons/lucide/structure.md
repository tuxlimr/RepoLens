# Project structure: lucide-icons/lucide

**Analysed commit:** `55782beff3a0133df79c417eb68f96e8f19e2404`

**Commit reference:** [55782beff3a0133df79c417eb68f96e8f19e2404](https://github.com/lucide-icons/lucide/commit/55782beff3a0133df79c417eb68f96e8f19e2404)

**Tree at this commit:** [lucide-icons/lucide@55782beff3a0](https://github.com/lucide-icons/lucide/tree/55782beff3a0133df79c417eb68f96e8f19e2404)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | lucide-icons/lucide |
| Description | Beautiful & consistent icon toolkit made by the community. Lucide is an open-source icon library that provides 2000+ vector (svg) files for displaying icons and symbols in digital and non-digital projects.  |
| Stars | 25757 |
| Forks | 1688 |
| Licence | Other |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `55782beff3a0133df79c417eb68f96e8f19e2404` |
| Retrieved at | 2026-11-14T19:13:05.623149+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.cspell/  (1 files)
  custom-words.txt
.github/  (57 files)
  DISCUSSION_TEMPLATE/  (1 files)
    icon-design.yml
  ISSUE_TEMPLATE/  (4 files)
    01_icon_request.yml
    02_bug_report.yml
    03_bug_report_site.yml
    04_feature_request.yml
  actions/  (15 files)
    icon-preview/  (4 files)
      … 4 files under this directory
    suggest-metadata/  (11 files)
      … 11 files under this directory
  instructions/  (3 files)
    groups.instructions.md
    metadata.instructions.md
    ux-writing.instructions.md
  workflows/  (28 files)
    angular.yml
    ci.yml
    close-issue-with-banned-phrases.yml
    close-stale-prs.yml
    docs.yml
    generate-pr-title.yml
    icons.yml
    labeler.yml
    lint-code.yml
    linting-icons.yml
    lucide-astro.yml
    lucide-font.yml
    lucide-lab.yml
    lucide-preact.yml
    lucide-react-native.yml
    lucide-react.yml
    lucide-shared.yml
    lucide-solid.yml
    lucide-static.yml
    lucide-svelte-5.yml
    lucide-vue.yml
    lucide.yml
    pull-request-icon-preview.yml
    pull-request-metadata-suggestions.yml
    … 4 more files
  FUNDING.yml
  conventional-commit-types.json
  copilot-instructions.md
  dependabot.yml
  labeler.yml
  pull_request_template.md
.husky/  (1 files)
  pre-commit
.vscode/  (3 files)
  launch.json
  settings.json
  svg.code-snippets
.well-known/  (1 files)
  funding-manifest-urls
categories/  (43 files)
  accessibility.json
  account.json
  animals.json
  arrows.json
  buildings.json
  charts.json
  communication.json
  connectivity.json
  cursors.json
  design.json
  development.json
  devices.json
  emoji.json
  files.json
  finance.json
  food-beverage.json
  gaming.json
  home.json
  layout.json
  letters-digits.json
  mail.json
  math.json
  medical.json
  multimedia.json
  … 19 more files
docs/  (580 files)
  .vitepress/  (208 files)
    api/  (13 files)
      … 13 files under this directory
    data/  (7 files)
      … 7 files under this directory
    lib/  (18 files)
      … 18 files under this directory
    markdown/  (4 files)
      … 4 files under this directory
    sidebar/  (12 files)
      … 12 files under this directory
    theme/  (148 files)
      … 148 files under this directory
    config.ts
    createOGImage.ts
    getHeadConfig.ts
    getStructuredData.ts
    transformPageData.ts
    types.d.ts
  contribute/  (13 files)
    icons/  (12 files)
      … 12 files under this directory
    index.md
  guide/  (129 files)
    angular/  (13 files)
      … 13 files under this directory
    astro/  (10 files)
      … 10 files under this directory
    icons/  (1 files)
      … 1 files under this directory
    lucide/  (12 files)
      … 12 files under this directory
    preact/  (13 files)
      … 13 files under this directory
    react/  (15 files)
      … 15 files under this directory
    react-native/  (13 files)
      … 13 files under this directory
    solid/  (13 files)
      … 13 files under this directory
    static/  (10 files)
      … 10 files under this directory
    svelte/  (12 files)
      … 12 files under this directory
    vue/  (13 files)
      … 13 files under this directory
    index.md
    installation.md
    version-1.md
    vscode.md
  how-to/  (3 files)
    accessibility.md
    icon-guide.md
    index.md
  icons/  (10 files)
    lab/  (3 files)
      … 3 files under this directory
    [name].md
    [name].paths.ts
    categories.data.ts
    categories.md
    codeExamples.data.ts
    icons.data.ts
    index.md
  images/  (102 files)
    a11y/  (18 files)
      … 18 files under this directory
    how-to/  (17 files)
      … 17 files under this directory
    package-logos/  (10 files)
      … 10 files under this directory
    1px-border-radius.svg
    1px-element-spacing.svg
    1px-inner-gap.svg
    1px-inner-spacing.svg
    1px-padding-violation.svg
    1px-padding.svg
    24px-24px-violation.svg
    24px-24px.svg
    2px-border-radius.svg
    2px-element-spacing-abrupt-cut.svg
    2px-element-spacing-connected.svg
    2px-element-spacing.svg
    2px-inner-gap.svg
    2px-inner-spacing.svg
    2px-stroke-violation.svg
    2px-stroke.svg
    border-radius-90deg.svg
    border-radius-arbitrary.svg
    border-radius-correct.svg
    border-radius-line-join-violation.svg
    border-radius-line-join.svg
    border-radius-violation.svg
    centered-strokes-violation.svg
    centered-strokes.svg
    … 33 more files
  public/  (87 files)
    company-logos/  (12 files)
      … 12 files under this directory
    framework-logos/  (27 files)
      … 27 files under this directory
    icons-raw/  (1 files)
      … 1 files under this directory
    library-logos/  (5 files)
      … 5 files under this directory
    package-logos/  (21 files)
      … 21 files under this directory
    sponsors/  (7 files)
      … 7 files under this directory
    browserconfig.xml
    digitalocean.svg
    favicon.svg
    funding.json
    logo-icon.svg
    logo-text.svg
    logo.dark.svg
    logo.light.svg
    logo.svg
    lucide-logo-repo-dark.svg
    lucide-logo-repo.svg
    safari-pinned-tab.svg
    site.webmanifest
    vercel.svg
  scripts/  (14 files)
    helpers/  (1 files)
      … 1 files under this directory
    writeBrandStopwords.mts
    writeCategoriesMetadata.mts
    writeIconDetails.mts
    writeIconMetaIndex.mts
    writeIconNodes.mts
    writeIconRelatedIcons.mts
    writeLabIconMetaIndex.mts
    writeLabIconNodes.mts
    writeReleaseMetadata.mts
    writeSponsorsData.mts
    writeVercelOutput.mts
    writeiconPopularity.mts
    writeiconPopularityIndex.mts
  README.md
  brand-logo-statement.md
  code-of-conduct.md
  community.md
  index.md
  license.md
  nitro.config.ts
  package.json
  packages.md
  privacy.md
  showcase.md
  sponsor.md
  tsconfig.json
  vercel.json
groups/  (53 files)
  chart.json
  check.json
  clock.json
  code.json
  cog.json
  currency.json
  dashed.json
  digit.json
  direction-down-left.json
  direction-down-right.json
  direction-down.json
  direction-left.json
  direction-right.json
  direction-up-left.json
  direction-up-right.json
  direction-up.json
  dot.json
  emoticon.json
  enter.json
  exclamation-mark.json
  exit.json
  graph.json
  heart.json
  key.json
  … 29 more files
icons/  (45 files)
  a-arrow-down.json
  a-arrow-down.svg
  a-arrow-up.json
  a-arrow-up.svg
  a-large-small.json
  a-large-small.svg
  accessibility.json
  accessibility.svg
  activity.json
  activity.svg
  ad.json
  ad.svg
  air-vent.json
  air-vent.svg
  airplay.json
  airplay.svg
  alarm-clock-check.json
  alarm-clock-check.svg
  alarm-clock-minus.json
  alarm-clock-minus.svg
  alarm-clock-off.json
  alarm-clock-off.svg
  alarm-clock-plus.json
  alarm-clock-plus.svg
  … 21 more files
.editorconfig
.gitignore
.npmignore
.prettierignore
BRAND_LOGOS_STATEMENT.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
brand-stopwords.json
category.schema.json
comment-markup.md
cspell.json
eslint.config.js
group.schema.json
icon.schema.json
```

## Entry points

- [docs/.vitepress/theme/components/editors/preact/index.js](https://github.com/lucide-icons/lucide/blob/55782beff3a0133df79c417eb68f96e8f19e2404/docs/.vitepress/theme/components/editors/preact/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 124 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/DISCUSSION_TEMPLATE/icon-design.yml` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/01_icon_request.yml` (config)
- `.github/ISSUE_TEMPLATE/02_bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/03_bug_report_site.yml` (config)
- `.github/ISSUE_TEMPLATE/04_feature_request.yml` (config)
- `.github/actions/icon-preview/.env.example` (config)
- `.github/actions/icon-preview/action.yml` (config)
- `.github/actions/icon-preview/package.json` (manifest)
- `.github/actions/suggest-metadata/.env.example` (config)
- `.github/actions/suggest-metadata/action.yml` (config)
- `.github/actions/suggest-metadata/package.json` (manifest)
- `.github/conventional-commit-types.json` (config)
- `.github/dependabot.yml` (config)
- `.github/labeler.yml` (config)
- `.github/workflows/angular.yml` (ci)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/close-issue-with-banned-phrases.yml` (ci)
- `.github/workflows/close-stale-prs.yml` (ci)
- `.github/workflows/docs.yml` (ci)
- `.github/workflows/generate-pr-title.yml` (ci)
- `.github/workflows/icons.yml` (ci)
- `.github/workflows/labeler.yml` (ci)
- `.github/workflows/lint-code.yml` (ci)
- `.github/workflows/linting-icons.yml` (ci)
- `.github/workflows/lucide-astro.yml` (ci)
- `.github/workflows/lucide-font.yml` (ci)
- `.github/workflows/lucide-lab.yml` (ci)
- `.github/workflows/lucide-preact.yml` (ci)
- `.github/workflows/lucide-react-native.yml` (ci)
- `.github/workflows/lucide-react.yml` (ci)
- `.github/workflows/lucide-shared.yml` (ci)
- `.github/workflows/lucide-solid.yml` (ci)
- `.github/workflows/lucide-static.yml` (ci)
- `.github/workflows/lucide-svelte-5.yml` (ci)
- `.github/workflows/lucide-vue.yml` (ci)
- `.github/workflows/lucide.yml` (ci)
- `.github/workflows/pull-request-icon-preview.yml` (ci)
- `.github/workflows/pull-request-metadata-suggestions.yml` (ci)
- `.github/workflows/release-lab.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/request-review.yml` (ci)
- `.github/workflows/solid-2.yml` (ci)
- `.vscode/launch.json` (config)
- `.vscode/settings.json` (config)
- `brand-stopwords.json` (config)
- `categories/accessibility.json` (config)
- `categories/account.json` (config)
- `categories/animals.json` (config)
- `categories/arrows.json` (config)
- `categories/buildings.json` (config)
- `categories/charts.json` (config)
- `categories/communication.json` (config)
- `categories/connectivity.json` (config)
- `categories/cursors.json` (config)
- `categories/design.json` (config)
- `categories/development.json` (config)
- `categories/devices.json` (config)
- `categories/emoji.json` (config)
- `categories/files.json` (config)
- `categories/finance.json` (config)
- `categories/food-beverage.json` (config)
- `categories/gaming.json` (config)
- `categories/home.json` (config)
- `categories/layout.json` (config)
- `categories/letters-digits.json` (config)
- `categories/mail.json` (config)
- `categories/math.json` (config)
- `categories/medical.json` (config)
- `categories/multimedia.json` (config)
- `categories/nature.json` (config)
- `categories/navigation.json` (config)
- `categories/notifications.json` (config)
- `categories/people.json` (config)
- `categories/photography.json` (config)
- `categories/science.json` (config)
- `categories/seasons.json` (config)
- `categories/security.json` (config)
- `categories/shapes.json` (config)
- `categories/shopping.json` (config)
- `categories/social.json` (config)
- `categories/sports.json` (config)
- `categories/sustainability.json` (config)
- `categories/text.json` (config)
- `categories/time.json` (config)
- `categories/tools.json` (config)
- `categories/transportation.json` (config)
- `categories/travel.json` (config)
- `categories/weather.json` (config)
- `category.schema.json` (config)
- `cspell.json` (config)
- `docs/.vitepress/data/categoriesData.json` (config)
- `docs/.vitepress/data/companiesData.json` (config)
- `docs/.vitepress/data/componentLibrariesData.json` (config)
- `docs/.vitepress/data/packageData.json` (config)
- `docs/.vitepress/data/packageData.thirdParty.json` (config)
- `docs/.vitepress/data/teamData.json` (config)
- `docs/.vitepress/theme/components/editors/preact/package.json` (manifest)
- `docs/.vitepress/theme/sandpackTheme.json` (config)
- `docs/package.json` (manifest)
- `docs/public/funding.json` (config)
- `docs/tsconfig.json` (config)
- `docs/vercel.json` (config)
- `group.schema.json` (config)
- `groups/chart.json` (config)
- `groups/check.json` (config)
- `groups/clock.json` (config)
- `groups/code.json` (config)
- `groups/cog.json` (config)
- `groups/currency.json` (config)
- `groups/dashed.json` (config)
- `groups/digit.json` (config)
- `groups/direction-down-left.json` (config)
- `groups/direction-down-right.json` (config)
- `groups/direction-down.json` (config)
- `groups/direction-left.json` (config)
- `groups/direction-right.json` (config)
- `groups/direction-up-left.json` (config)
- `groups/direction-up-right.json` (config)
- `groups/direction-up.json` (config)
- `groups/dot.json` (config)
- `groups/emoticon.json` (config)
- `groups/enter.json` (config)
- `groups/exclamation-mark.json` (config)
- `groups/exit.json` (config)
- `groups/graph.json` (config)
- `groups/heart.json` (config)
- `groups/key.json` (config)
- `groups/layout-resize.json` (config)
- `groups/letter.json` (config)
- `groups/line.json` (config)
- `groups/lock.json` (config)
- `groups/minus.json` (config)
- `groups/navigation-first.json` (config)
- `groups/navigation-last.json` (config)
- `groups/navigation-next.json` (config)
- `groups/navigation-previous.json` (config)
- `groups/off.json` (config)
- `groups/pause.json` (config)
- `groups/pen.json` (config)
- `groups/percent.json` (config)
- `groups/play.json` (config)
- `groups/plus.json` (config)
- `groups/position-bottom.json` (config)
- `groups/position-left.json` (config)
- `groups/position-right.json` (config)
- `groups/position-top.json` (config)
- `groups/question-mark.json` (config)
- `groups/search.json` (config)
- `groups/shield.json` (config)
- `groups/sort.json` (config)
- `groups/sparkles.json` (config)
- `groups/star.json` (config)
- `groups/stop.json` (config)
- `groups/sync.json` (config)
- `groups/user.json` (config)
- `groups/x.json` (config)
- `icon.schema.json` (config)
- `icons/a-arrow-down.json` (config)
- `icons/a-arrow-up.json` (config)
- `icons/a-large-small.json` (config)
- `icons/accessibility.json` (config)
- `icons/activity.json` (config)
- `icons/ad.json` (config)
- `icons/air-vent.json` (config)
- `icons/airplay.json` (config)
- `icons/alarm-clock-check.json` (config)
- `icons/alarm-clock-minus.json` (config)
- `icons/alarm-clock-off.json` (config)
- `icons/alarm-clock-plus.json` (config)
- `icons/alarm-clock.json` (config)
- `icons/alarm-smoke.json` (config)
- `icons/align-center-horizontal.json` (config)
- `icons/align-center-vertical.json` (config)
- `icons/align-end-horizontal.json` (config)
- `icons/align-end-vertical.json` (config)
- `icons/align-horizontal-distribute-center.json` (config)
- `icons/align-horizontal-distribute-end.json` (config)
- `icons/align-horizontal-distribute-start.json` (config)
- `icons/align-horizontal-justify-center.json` (config)
- `icons/align-horizontal-justify-end.json` (config)

## Top-level layout

- `docs` — 580 analysed file(s)
- `.github` — 57 analysed file(s)
- `groups` — 53 analysed file(s)
- `icons` — 45 analysed file(s)
- `categories` — 43 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `.vscode` — 3 analysed file(s)
- `.cspell` — 1 analysed file(s)
- `.husky` — 1 analysed file(s)
- `.well-known` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `55782beff3a0133df79c417eb68f96e8f19e2404` is the revision these paths and observations refer to.
