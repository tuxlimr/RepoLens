# Project structure: reactchartjs/react-chartjs-2

**Analysed commit:** `7c7be48ae5b585f45bc6aef718cc8d4b51f34d0a`

**Commit reference:** [7c7be48ae5b585f45bc6aef718cc8d4b51f34d0a](https://github.com/reactchartjs/react-chartjs-2/commit/7c7be48ae5b585f45bc6aef718cc8d4b51f34d0a)

**Tree at this commit:** [reactchartjs/react-chartjs-2@7c7be48ae5b5](https://github.com/reactchartjs/react-chartjs-2/tree/7c7be48ae5b585f45bc6aef718cc8d4b51f34d0a)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | reactchartjs/react-chartjs-2 |
| Description | React components for Chart.js, the most popular charting library |
| Stars | 6937 |
| Forks | 2423 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `7c7be48ae5b585f45bc6aef718cc8d4b51f34d0a` |
| Retrieved at | 2026-11-14T19:14:00.777276+00:00 |
| Files in this snapshot | 209 |

## Directory tree

```text
.github/  (9 files)
  ISSUE_TEMPLATE/  (3 files)
    bug-report.yml
    config.yml
    feature-request.yml
  workflows/  (5 files)
    checks.yml
    ci.yml
    commit.yml
    release.yml
    website.yml
  renovate.json
.storybook/  (5 files)
  main.js
  manager.js
  package.json
  preview.js
  theme.js
sandboxes/  (88 files)
  bar/  (20 files)
    grouped/  (5 files)
      … 5 files under this directory
    horizontal/  (5 files)
      … 5 files under this directory
    stacked/  (5 files)
      … 5 files under this directory
    vertical/  (5 files)
      … 5 files under this directory
  bubble/  (5 files)
    default/  (5 files)
      … 5 files under this directory
  chart/  (20 files)
    canvas/  (5 files)
      … 5 files under this directory
    events/  (5 files)
      … 5 files under this directory
    multitype/  (5 files)
      … 5 files under this directory
    ref/  (5 files)
      … 5 files under this directory
  doughnut/  (5 files)
    default/  (5 files)
      … 5 files under this directory
  line/  (15 files)
    area/  (5 files)
      … 5 files under this directory
    default/  (5 files)
      … 5 files under this directory
    multiaxis/  (5 files)
      … 5 files under this directory
  pie/  (5 files)
    default/  (5 files)
      … 5 files under this directory
  polarArea/  (5 files)
    default/  (5 files)
      … 5 files under this directory
  radar/  (5 files)
    default/  (5 files)
      … 5 files under this directory
  scatter/  (5 files)
    default/  (5 files)
      … 5 files under this directory
  package.json
  pnpm-workspace.yaml
  tsconfig.json
src/  (5 files)
  chart.tsx
  index.ts
  typedCharts.tsx
  types.ts
  utils.ts
stories/  (11 files)
  Bar.stories.tsx
  Bubble.stories.tsx
  Chart.data.ts
  Chart.stories.tsx
  Doughnut.stories.tsx
  Line.stories.tsx
  Pie.stories.tsx
  PolarArea.stories.tsx
  Radar.stories.tsx
  Scatter.stories.tsx
  data.ts
test/  (4 files)
  .eslintrc.json
  chart.test-d.tsx
  chart.test.tsx
  setup.ts
website/  (65 files)
  docs/  (49 files)
    components/  (11 files)
      … 11 files under this directory
    examples/  (19 files)
      … 19 files under this directory
    faq/  (11 files)
      … 11 files under this directory
    chartjs-v2.mdx
    chartjs-v3.mdx
    docs.js
    index.mdx
    migration-to-v4.md
    migration-to-v5.md
    working-with-datasets.md
    working-with-events.md
  src/  (4 files)
    components/  (2 files)
      … 2 files under this directory
    css/  (1 files)
      … 1 files under this directory
    theme/  (1 files)
      … 1 files under this directory
  static/  (2 files)
    img/  (1 files)
      … 1 files under this directory
    .nojekyll
  .gitignore
  CNAME
  README.md
  babel.config.js
  docusaurus.config.js
  package.json
  pnpm-workspace.yaml
  sandboxes.js
  sidebars.js
  tsconfig.json
.clean-publish
.commitlintrc.json
.czrc
.editorconfig
.eslintignore
.eslintrc.json
.gitignore
.nano-staged.json
.prettierrc
.simple-git-hooks.json
.simple-release.json
.size-limit.json
.tool-versions
CHANGELOG.md
LICENSE
LICENSE.md
README.md
package.json
pnpm-workspace.yaml
rollup.config.js
tsconfig.json
vite.config.js
```

## Entry points

- [.storybook/main.js](https://github.com/reactchartjs/react-chartjs-2/blob/7c7be48ae5b585f45bc6aef718cc8d4b51f34d0a/.storybook/main.js)
- [sandboxes/bar/grouped/App.tsx](https://github.com/reactchartjs/react-chartjs-2/blob/7c7be48ae5b585f45bc6aef718cc8d4b51f34d0a/sandboxes/bar/grouped/App.tsx)
- [sandboxes/bar/grouped/index.tsx](https://github.com/reactchartjs/react-chartjs-2/blob/7c7be48ae5b585f45bc6aef718cc8d4b51f34d0a/sandboxes/bar/grouped/index.tsx)
- [sandboxes/bar/horizontal/App.tsx](https://github.com/reactchartjs/react-chartjs-2/blob/7c7be48ae5b585f45bc6aef718cc8d4b51f34d0a/sandboxes/bar/horizontal/App.tsx)
- [sandboxes/bar/horizontal/index.tsx](https://github.com/reactchartjs/react-chartjs-2/blob/7c7be48ae5b585f45bc6aef718cc8d4b51f34d0a/sandboxes/bar/horizontal/index.tsx)
- [sandboxes/bar/stacked/App.tsx](https://github.com/reactchartjs/react-chartjs-2/blob/7c7be48ae5b585f45bc6aef718cc8d4b51f34d0a/sandboxes/bar/stacked/App.tsx)
- [sandboxes/bar/stacked/index.tsx](https://github.com/reactchartjs/react-chartjs-2/blob/7c7be48ae5b585f45bc6aef718cc8d4b51f34d0a/sandboxes/bar/stacked/index.tsx)
- [sandboxes/bar/vertical/App.tsx](https://github.com/reactchartjs/react-chartjs-2/blob/7c7be48ae5b585f45bc6aef718cc8d4b51f34d0a/sandboxes/bar/vertical/App.tsx)
- [sandboxes/bar/vertical/index.tsx](https://github.com/reactchartjs/react-chartjs-2/blob/7c7be48ae5b585f45bc6aef718cc8d4b51f34d0a/sandboxes/bar/vertical/index.tsx)
- [sandboxes/bubble/default/App.tsx](https://github.com/reactchartjs/react-chartjs-2/blob/7c7be48ae5b585f45bc6aef718cc8d4b51f34d0a/sandboxes/bubble/default/App.tsx)
- [sandboxes/bubble/default/index.tsx](https://github.com/reactchartjs/react-chartjs-2/blob/7c7be48ae5b585f45bc6aef718cc8d4b51f34d0a/sandboxes/bubble/default/index.tsx)
- [sandboxes/chart/canvas/App.tsx](https://github.com/reactchartjs/react-chartjs-2/blob/7c7be48ae5b585f45bc6aef718cc8d4b51f34d0a/sandboxes/chart/canvas/App.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| chart.tsx package | library | Observed | Groups 1 file(s) under chart.tsx package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 26 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| index.ts package | library | Observed | Groups 1 file(s) under index.ts package (observed from repository paths and static analysis). |
| sandboxes package | library | Observed | Groups 51 file(s) under sandboxes package (observed from repository paths and static analysis). |
| stories package | library | Observed | Groups 11 file(s) under stories package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 4 file(s) under tests (observed from repository paths and static analysis). |
| typedCharts.tsx package | library | Observed | Groups 1 file(s) under typedcharts.tsx package (observed from repository paths and static analysis). |
| types.ts package | library | Observed | Groups 1 file(s) under types.ts package (observed from repository paths and static analysis). |
| utils.ts package | library | Observed | Groups 1 file(s) under utils.ts package (observed from repository paths and static analysis). |
| website package | library | Observed | Groups 7 file(s) under website package (observed from repository paths and static analysis). |

## Important files

- `.commitlintrc.json` (config)
- `.editorconfig` (config)
- `.eslintrc.json` (config)
- `.github/ISSUE_TEMPLATE/bug-report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature-request.yml` (config)
- `.github/renovate.json` (config)
- `.github/workflows/checks.yml` (ci)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/commit.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/website.yml` (ci)
- `.nano-staged.json` (config)
- `.simple-git-hooks.json` (config)
- `.simple-release.json` (config)
- `.size-limit.json` (config)
- `.storybook/package.json` (manifest)
- `package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `sandboxes/bar/grouped/package.json` (manifest)
- `sandboxes/bar/horizontal/package.json` (manifest)
- `sandboxes/bar/stacked/package.json` (manifest)
- `sandboxes/bar/vertical/package.json` (manifest)
- `sandboxes/bubble/default/package.json` (manifest)
- `sandboxes/chart/canvas/package.json` (manifest)
- `sandboxes/chart/events/package.json` (manifest)
- `sandboxes/chart/multitype/package.json` (manifest)
- `sandboxes/chart/ref/package.json` (manifest)
- `sandboxes/doughnut/default/package.json` (manifest)
- `sandboxes/line/area/package.json` (manifest)
- `sandboxes/line/default/package.json` (manifest)
- `sandboxes/line/multiaxis/package.json` (manifest)
- `sandboxes/package.json` (manifest)
- `sandboxes/pie/default/package.json` (manifest)
- `sandboxes/pnpm-workspace.yaml` (config)
- `sandboxes/polarArea/default/package.json` (manifest)
- `sandboxes/radar/default/package.json` (manifest)
- `sandboxes/scatter/default/package.json` (manifest)
- `sandboxes/tsconfig.json` (config)
- `tsconfig.json` (config)
- `website/package.json` (manifest)
- `website/pnpm-workspace.yaml` (config)
- `website/tsconfig.json` (config)

## Top-level layout

- `sandboxes` — 88 analysed file(s)
- `website` — 65 analysed file(s)
- `(root files)` — 22 analysed file(s)
- `stories` — 11 analysed file(s)
- `.github` — 9 analysed file(s)
- `.storybook` — 5 analysed file(s)
- `src` — 5 analysed file(s)
- `test` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `7c7be48ae5b585f45bc6aef718cc8d4b51f34d0a` is the revision these paths and observations refer to.
