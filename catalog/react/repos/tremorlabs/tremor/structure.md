# Project structure: tremorlabs/tremor

**Analysed commit:** `ca4d588f47820ff3d514d37fa4ee08a4222dec11`

**Commit reference:** [ca4d588f47820ff3d514d37fa4ee08a4222dec11](https://github.com/tremorlabs/tremor/commit/ca4d588f47820ff3d514d37fa4ee08a4222dec11)

**Tree at this commit:** [tremorlabs/tremor@ca4d588f4782](https://github.com/tremorlabs/tremor/tree/ca4d588f47820ff3d514d37fa4ee08a4222dec11)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | tremorlabs/tremor |
| Description | Copy & Paste React components to build modern web applications.  |
| Stars | 3701 |
| Forks | 200 |
| Licence | Apache-2.0 |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `ca4d588f47820ff3d514d37fa4ee08a4222dec11` |
| Retrieved at | 2026-11-14T19:15:08.323078+00:00 |
| Files in this snapshot | 196 |

## Directory tree

```text
.github/  (5 files)
  ISSUE_TEMPLATE/  (3 files)
    bug-report.yml
    config.yml
    feature-request.yml
  workflows/  (1 files)
    playwright.yml
  pull_request_template.md
.storybook/  (3 files)
  main.ts
  manager.ts
  preview.ts
public/  (2 files)
  images/  (2 files)
    tremor-logo-dark.svg
    tremor-logo-light.svg
scripts/  (1 files)
  component-folder.js
src/  (172 files)
  components/  (159 files)
    Accordion/  (4 files)
      … 4 files under this directory
    AreaChart/  (4 files)
      … 4 files under this directory
    Badge/  (4 files)
      … 4 files under this directory
    BarChart/  (4 files)
      … 4 files under this directory
    BarList/  (4 files)
      … 4 files under this directory
    Button/  (4 files)
      … 4 files under this directory
    Calendar/  (4 files)
      … 4 files under this directory
    Callout/  (4 files)
      … 4 files under this directory
    Card/  (4 files)
      … 4 files under this directory
    CategoryBar/  (4 files)
      … 4 files under this directory
    Checkbox/  (4 files)
      … 4 files under this directory
    ComboChart/  (4 files)
      … 4 files under this directory
    DatePicker/  (5 files)
      … 5 files under this directory
    Dialog/  (4 files)
      … 4 files under this directory
    Divider/  (4 files)
      … 4 files under this directory
    DonutChart/  (4 files)
      … 4 files under this directory
    Drawer/  (4 files)
      … 4 files under this directory
    DropdownMenu/  (4 files)
      … 4 files under this directory
    Input/  (4 files)
      … 4 files under this directory
    Label/  (4 files)
      … 4 files under this directory
    LineChart/  (4 files)
      … 4 files under this directory
    Popover/  (4 files)
      … 4 files under this directory
    ProgressBar/  (4 files)
      … 4 files under this directory
    ProgressCircle/  (4 files)
      … 4 files under this directory
    RadioCardGroup/  (4 files)
      … 4 files under this directory
    RadioGroup/  (4 files)
      … 4 files under this directory
    Select/  (4 files)
      … 4 files under this directory
    SelectNative/  (4 files)
      … 4 files under this directory
    Slider/  (4 files)
      … 4 files under this directory
    SparkChart/  (6 files)
      … 6 files under this directory
    Switch/  (4 files)
      … 4 files under this directory
    TabNavigation/  (4 files)
      … 4 files under this directory
    Table/  (4 files)
      … 4 files under this directory
    Tabs/  (4 files)
      … 4 files under this directory
    Textarea/  (4 files)
      … 4 files under this directory
    Toast/  (4 files)
      … 4 files under this directory
    Toggle/  (4 files)
      … 4 files under this directory
    Tooltip/  (4 files)
      … 4 files under this directory
    Tracker/  (4 files)
      … 4 files under this directory
  hooks/  (3 files)
    changelog.md
    useOnWindowResize.ts
    useToast.ts
  utils/  (9 files)
    changelog.md
    chartColors.ts
    cx.ts
    focusInput.ts
    focusRing.ts
    getYAxisDomain.ts
    hasErrorInput.ts
    hasOnlyOneValueForKey.ts
    utils.spec.ts
  globals.css
.eslintrc.cjs
.gitignore
.prettierignore
.prettierrc
LICENSE
README.md
package.json
playwright.config.ts
postcss.config.js
tsconfig.json
tsconfig.node.json
vite.config.ts
vitest.config.ts
```

## Entry points

- [.storybook/main.ts](https://github.com/tremorlabs/tremor/blob/ca4d588f47820ff3d514d37fa4ee08a4222dec11/.storybook/main.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| components package | library | Observed | Groups 120 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 2 file(s) under hooks package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 8 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.github/ISSUE_TEMPLATE/bug-report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature-request.yml` (config)
- `.github/workflows/playwright.yml` (ci)
- `package.json` (manifest)
- `tsconfig.json` (config)
- `tsconfig.node.json` (config)

## Top-level layout

- `src` — 172 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `.github` — 5 analysed file(s)
- `.storybook` — 3 analysed file(s)
- `public` — 2 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `ca4d588f47820ff3d514d37fa4ee08a4222dec11` is the revision these paths and observations refer to.
