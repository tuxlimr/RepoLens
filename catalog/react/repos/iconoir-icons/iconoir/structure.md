# Project structure: iconoir-icons/iconoir

**Analysed commit:** `39834e3f193bc0cca2c36bebb6a650471977433d`

**Commit reference:** [39834e3f193bc0cca2c36bebb6a650471977433d](https://github.com/iconoir-icons/iconoir/commit/39834e3f193bc0cca2c36bebb6a650471977433d)

**Tree at this commit:** [iconoir-icons/iconoir@39834e3f193b](https://github.com/iconoir-icons/iconoir/tree/39834e3f193bc0cca2c36bebb6a650471977433d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | iconoir-icons/iconoir |
| Description | Free, open source (MIT) SVG icon library: 1,383 icons (1,671 SVGs with solid variants) for React, React Native, Vue, Solid, Flutter, CSS, Figma and Framer. |
| Stars | 4642 |
| Forks | 202 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `39834e3f193bc0cca2c36bebb6a650471977433d` |
| Retrieved at | 2026-11-14T19:14:39.785455+00:00 |
| Files in this snapshot | 783 |

## Directory tree

```text
.cursor/  (1 files)
  rules/  (1 files)
    releases.mdc
.github/  (9 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    feature_request.md
    icon_request.md
  actions/  (1 files)
    setup/  (1 files)
      … 1 files under this directory
  workflows/  (4 files)
    build.yaml
    ci.yaml
    release.yaml
    website.yaml
  FUNDING.yml
.vscode/  (2 files)
  extensions.json
  settings.json
bin/  (1 files)
  prepublish.js
css/  (1 files)
  README.md
docs/  (2 files)
  faq.md
  framer.md
examples/  (23 files)
  next/  (6 files)
    app/  (2 files)
      … 2 files under this directory
    .gitignore
    next.config.ts
    package.json
    tsconfig.json
  react-native/  (7 files)
    .gitignore
    App.tsx
    app.json
    index.ts
    metro.config.js
    package.json
    tsconfig.json
  vue/  (10 files)
    src/  (2 files)
      … 2 files under this directory
    .gitignore
    env.d.ts
    index.html
    package.json
    tsconfig.app.json
    tsconfig.json
    tsconfig.node.json
    vite.config.ts
iconoir.com/  (78 files)
  components/  (41 files)
    Button.tsx
    Callout.tsx
    CarbonCoverAd.tsx
    CategoryRow.tsx
    ChangelogEntry.tsx
    CurrentVersion.tsx
    CustomizationEditor.tsx
    DocsMenu.tsx
    DocumentationNavigation.tsx
    DonationPopup.tsx
    Explore.tsx
    FilterDropdown.tsx
    FiltersEditor.tsx
    Footer.tsx
    GA.tsx
    Header.tsx
    Hero.tsx
    HeroIcons.tsx
    Icon.tsx
    IconList.tsx
    IconListEmpty.tsx
    IconSelection.tsx
    IconSheet.tsx
    IconsRow.tsx
    … 17 more files
  lib/  (11 files)
    analytics.ts
    constants.ts
    docs.ts
    docsSeo.ts
    getHeaderProps.ts
    getIcons.ts
    octokit.ts
    responsive.ts
    showNotification.ts
    stats.ts
    svg.ts
  pages/  (8 files)
    docs/  (3 files)
      … 3 files under this directory
    kw/  (1 files)
      … 1 files under this directory
    _app.tsx
    _document.tsx
    index.tsx
    support.tsx
  public/  (8 files)
    fonts/  (1 files)
      … 1 files under this directory
    home-background.svg
    iconoir-logo.svg
    nibol-logo.svg
    robots.txt
    sitemap.xml
    support-background.svg
    vercel.svg
  scripts/  (2 files)
    enrich-icons-csv.py
    generate-agent-files.mts
  styles/  (2 files)
    prism-theme.css
    theme.css
  .gitignore
  icons.csv
  next-env.d.ts
  next.config.ts
  package.json
  tsconfig.json
icons/  (656 files)
  regular/  (656 files)
    accessibility-sign.svg
    accessibility-tech.svg
    accessibility.svg
    activity.svg
    adobe-after-effects.svg
    adobe-illustrator.svg
    adobe-indesign.svg
    adobe-lightroom.svg
    adobe-photoshop.svg
    adobe-xd.svg
    african-tree.svg
    agile.svg
    air-conditioner.svg
    airplane-helix-45deg.svg
    airplane-helix.svg
    airplane-off.svg
    airplane-rotation.svg
    airplane.svg
    airplay.svg
    alarm.svg
    album-carousel.svg
    album-list.svg
    album-open.svg
    album.svg
    … 632 more files
.gitignore
.node-version
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
NAMING_CONVENTION.md
README.md
analysis_options.yaml
context7.json
eslint.config.js
```

## Entry points

- [iconoir.com/scripts/enrich-icons-csv.py:516](https://github.com/iconoir-icons/iconoir/blob/39834e3f193bc0cca2c36bebb6a650471977433d/iconoir.com/scripts/enrich-icons-csv.py#L516)
- [examples/react-native/index.ts](https://github.com/iconoir-icons/iconoir/blob/39834e3f193bc0cca2c36bebb6a650471977433d/examples/react-native/index.ts)
- [iconoir.com/pages/index.tsx](https://github.com/iconoir-icons/iconoir/blob/39834e3f193bc0cca2c36bebb6a650471977433d/iconoir.com/pages/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bin package | library | Observed | Groups 1 file(s) under bin package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: collect_keywords, join_tags, main, split_tags. |
| iconoir.com package | library | Observed | Groups 59 file(s) under iconoir.com package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/actions/setup/action.yml` (config)
- `.github/workflows/build.yaml` (ci)
- `.github/workflows/ci.yaml` (ci)
- `.github/workflows/release.yaml` (ci)
- `.github/workflows/website.yaml` (ci)
- `.vscode/extensions.json` (config)
- `.vscode/settings.json` (config)
- `analysis_options.yaml` (config)
- `context7.json` (config)
- `examples/next/package.json` (manifest)
- `examples/next/tsconfig.json` (config)
- `examples/react-native/app.json` (config)
- `examples/react-native/package.json` (manifest)
- `examples/react-native/tsconfig.json` (config)
- `examples/vue/package.json` (manifest)
- `examples/vue/tsconfig.app.json` (config)
- `examples/vue/tsconfig.json` (config)
- `examples/vue/tsconfig.node.json` (config)
- `iconoir.com/package.json` (manifest)
- `iconoir.com/tsconfig.json` (config)

## Top-level layout

- `icons` — 656 analysed file(s)
- `iconoir.com` — 78 analysed file(s)
- `examples` — 23 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `.github` — 9 analysed file(s)
- `.vscode` — 2 analysed file(s)
- `docs` — 2 analysed file(s)
- `.cursor` — 1 analysed file(s)
- `bin` — 1 analysed file(s)
- `css` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 17 file(s) were skipped during inventory (17 x vendored/generated directory excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `39834e3f193bc0cca2c36bebb6a650471977433d` is the revision these paths and observations refer to.
