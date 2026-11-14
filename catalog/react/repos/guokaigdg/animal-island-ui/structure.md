# Project structure: guokaigdg/animal-island-ui

**Analysed commit:** `956f23cb7a388f178dbd98c8cfb9df958a3e3f9f`

**Commit reference:** [956f23cb7a388f178dbd98c8cfb9df958a3e3f9f](https://github.com/guokaigdg/animal-island-ui/commit/956f23cb7a388f178dbd98c8cfb9df958a3e3f9f)

**Tree at this commit:** [guokaigdg/animal-island-ui@956f23cb7a38](https://github.com/guokaigdg/animal-island-ui/tree/956f23cb7a388f178dbd98c8cfb9df958a3e3f9f)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | guokaigdg/animal-island-ui |
| Description | A Kawaii React UI component library  一个可爱的 React UI  组件库 |
| Stars | 5157 |
| Forks | 49 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `956f23cb7a388f178dbd98c8cfb9df958a3e3f9f` |
| Retrieved at | 2026-11-14T19:14:26.931559+00:00 |
| Files in this snapshot | 429 |

## Directory tree

```text
.githooks/  (1 files)
  pre-commit
.github/  (2 files)
  workflows/  (1 files)
    ci.yml
  FUNDING.yml
.trae/  (1 files)
  documents/  (1 files)
    icon-refactor.md
demo/  (76 files)
  components/  (66 files)
    Avatar/  (1 files)
      … 1 files under this directory
    BackTop/  (1 files)
      … 1 files under this directory
    Background/  (1 files)
      … 1 files under this directory
    Badge/  (1 files)
      … 1 files under this directory
    Button/  (1 files)
      … 1 files under this directory
    Calendar/  (1 files)
      … 1 files under this directory
    Card/  (1 files)
      … 1 files under this directory
    Carousel/  (1 files)
      … 1 files under this directory
    Chart/  (11 files)
      … 11 files under this directory
    Checkbox/  (1 files)
      … 1 files under this directory
    CodeBlock/  (1 files)
      … 1 files under this directory
    Collapse/  (1 files)
      … 1 files under this directory
    CountUp/  (1 files)
      … 1 files under this directory
    Countdown/  (5 files)
      … 5 files under this directory
    Cursor/  (1 files)
      … 1 files under this directory
    DatePicker/  (1 files)
      … 1 files under this directory
    Divider/  (2 files)
      … 2 files under this directory
    Drawer/  (1 files)
      … 1 files under this directory
    Footer/  (1 files)
      … 1 files under this directory
    Form/  (1 files)
      … 1 files under this directory
    Icon/  (1 files)
      … 1 files under this directory
    Image/  (1 files)
      … 1 files under this directory
    Input/  (1 files)
      … 1 files under this directory
    Loading/  (1 files)
      … 1 files under this directory
    Modal/  (1 files)
      … 1 files under this directory
    NoData/  (2 files)
      … 2 files under this directory
    Notification/  (1 files)
      … 1 files under this directory
    Pagination/  (1 files)
      … 1 files under this directory
    Progress/  (2 files)
      … 2 files under this directory
    Radio/  (1 files)
      … 1 files under this directory
    Rate/  (1 files)
      … 1 files under this directory
    Select/  (1 files)
      … 1 files under this directory
    Skeleton/  (1 files)
      … 1 files under this directory
    Skill/  (5 files)
      … 5 files under this directory
    Switch/  (1 files)
      … 1 files under this directory
    Table/  (1 files)
      … 1 files under this directory
    Tabs/  (1 files)
      … 1 files under this directory
    Tag/  (1 files)
      … 1 files under this directory
    Time/  (1 files)
      … 1 files under this directory
    TimePicker/  (1 files)
      … 1 files under this directory
    Title/  (1 files)
      … 1 files under this directory
    Tooltip/  (1 files)
      … 1 files under this directory
    Typewriter/  (1 files)
      … 1 files under this directory
    Upload/  (2 files)
      … 2 files under this directory
  tools/  (1 files)
    index.tsx
  App.tsx
  ComponentPage.tsx
  HomePage.tsx
  chartPages.ts
  fonts.css
  gradients.ts
  main.tsx
  pageInfo.ts
  vite-env.d.ts
docs/  (71 files)
  adr/  (8 files)
    0001-zero-runtime-dependencies.md
    0002-dual-design-token-system.md
    0003-vite-library-mode-build.md
    0004-docs-sync-automation.md
    0005-dayjs-as-the-date-layer.md
    0006-time-locale-formatting.md
    0007-timepicker-date-layer.md
    README.md
  design-system/  (18 files)
    components/  (13 files)
      … 13 files under this directory
    README.md
    css-variables.md
    demo-site.md
    design-rules.md
    design-tokens.md
  development/  (7 files)
    README.md
    build-and-release.md
    coding-standards.md
    component-development.md
    contributing.md
    repository-structure.md
    testing.md
  zh-CN/  (35 files)
    adr/  (8 files)
      … 8 files under this directory
    design-system/  (18 files)
      … 18 files under this directory
    development/  (7 files)
      … 7 files under this directory
    design-prompts.md
    one-click-prompt.md
  README.zh-CN.md
  design-prompts.md
  one-click-prompt.md
scripts/  (3 files)
  check-bundle.mjs
  check-docs-sync.mjs
  generate-coverage-badges.mjs
skills/  (25 files)
  animal-island-ui-style/  (25 files)
    references/  (22 files)
      … 22 files under this directory
    README.md
    SKILL.md
    SKILL.zh-CN.md
src/  (225 files)
  assets/  (29 files)
    image/  (29 files)
      … 29 files under this directory
  components/  (186 files)
    Avatar/  (4 files)
      … 4 files under this directory
    BackTop/  (4 files)
      … 4 files under this directory
    Background/  (4 files)
      … 4 files under this directory
    Badge/  (4 files)
      … 4 files under this directory
    Button/  (4 files)
      … 4 files under this directory
    Calendar/  (4 files)
      … 4 files under this directory
    Card/  (4 files)
      … 4 files under this directory
    Carousel/  (4 files)
      … 4 files under this directory
    Chart/  (11 files)
      … 11 files under this directory
    Checkbox/  (4 files)
      … 4 files under this directory
    CodeBlock/  (4 files)
      … 4 files under this directory
    Collapse/  (4 files)
      … 4 files under this directory
    CountUp/  (4 files)
      … 4 files under this directory
    Countdown/  (5 files)
      … 5 files under this directory
    Cursor/  (4 files)
      … 4 files under this directory
    DatePicker/  (4 files)
      … 4 files under this directory
    Divider/  (4 files)
      … 4 files under this directory
    Drawer/  (4 files)
      … 4 files under this directory
    Footer/  (4 files)
      … 4 files under this directory
    Form/  (9 files)
      … 9 files under this directory
    Image/  (4 files)
      … 4 files under this directory
    Input/  (4 files)
      … 4 files under this directory
    Loading/  (7 files)
      … 7 files under this directory
    Modal/  (4 files)
      … 4 files under this directory
    NoData/  (4 files)
      … 4 files under this directory
    Notification/  (6 files)
      … 6 files under this directory
    Pagination/  (4 files)
      … 4 files under this directory
    Progress/  (5 files)
      … 5 files under this directory
    Radio/  (4 files)
      … 4 files under this directory
    Rate/  (4 files)
      … 4 files under this directory
    Select/  (4 files)
      … 4 files under this directory
    Skeleton/  (4 files)
      … 4 files under this directory
    Switch/  (4 files)
      … 4 files under this directory
    Table/  (4 files)
      … 4 files under this directory
    Tabs/  (4 files)
      … 4 files under this directory
    Tag/  (4 files)
      … 4 files under this directory
    Time/  (4 files)
      … 4 files under this directory
    TimePicker/  (4 files)
      … 4 files under this directory
    Title/  (4 files)
      … 4 files under this directory
    Tooltip/  (4 files)
      … 4 files under this directory
    Typewriter/  (3 files)
      … 3 files under this directory
    Upload/  (4 files)
      … 4 files under this directory
  internal/  (2 files)
    Wave.tsx
    wave.module.less
  styles/  (5 files)
    themes/  (1 files)
      … 1 files under this directory
    fonts.less
    index.less
    reset.less
    variables.less
  index.ts
  typings.d.ts
  vite-env.d.ts
test/  (4 files)
  a11y.test.tsx
  components.tsx
  setup.ts
  utils.tsx
.editorconfig
.gitignore
.prettierignore
.prettierrc
AGENTS.md
CHANGELOG.md
CLAUDE.md
CONTRIBUTING.md
LICENSE
README.md
eslint.config.js
index.html
items.d.ts
package.json
tsconfig.build.json
tsconfig.json
tsconfig.test.json
vite.config.demo.ts
vite.config.ts
vitest.a11y.config.ts
vitest.config.ts
```

## Entry points

- [demo/App.tsx](https://github.com/guokaigdg/animal-island-ui/blob/956f23cb7a388f178dbd98c8cfb9df958a3e3f9f/demo/App.tsx)
- [demo/components/Avatar/index.tsx](https://github.com/guokaigdg/animal-island-ui/blob/956f23cb7a388f178dbd98c8cfb9df958a3e3f9f/demo/components/Avatar/index.tsx)
- [demo/components/BackTop/index.tsx](https://github.com/guokaigdg/animal-island-ui/blob/956f23cb7a388f178dbd98c8cfb9df958a3e3f9f/demo/components/BackTop/index.tsx)
- [demo/components/Background/index.tsx](https://github.com/guokaigdg/animal-island-ui/blob/956f23cb7a388f178dbd98c8cfb9df958a3e3f9f/demo/components/Background/index.tsx)
- [demo/components/Badge/index.tsx](https://github.com/guokaigdg/animal-island-ui/blob/956f23cb7a388f178dbd98c8cfb9df958a3e3f9f/demo/components/Badge/index.tsx)
- [demo/components/Button/index.tsx](https://github.com/guokaigdg/animal-island-ui/blob/956f23cb7a388f178dbd98c8cfb9df958a3e3f9f/demo/components/Button/index.tsx)
- [demo/components/Calendar/index.tsx](https://github.com/guokaigdg/animal-island-ui/blob/956f23cb7a388f178dbd98c8cfb9df958a3e3f9f/demo/components/Calendar/index.tsx)
- [demo/components/Card/index.tsx](https://github.com/guokaigdg/animal-island-ui/blob/956f23cb7a388f178dbd98c8cfb9df958a3e3f9f/demo/components/Card/index.tsx)
- [demo/components/Carousel/index.tsx](https://github.com/guokaigdg/animal-island-ui/blob/956f23cb7a388f178dbd98c8cfb9df958a3e3f9f/demo/components/Carousel/index.tsx)
- [demo/components/Chart/index.tsx](https://github.com/guokaigdg/animal-island-ui/blob/956f23cb7a388f178dbd98c8cfb9df958a3e3f9f/demo/components/Chart/index.tsx)
- [demo/components/Checkbox/index.tsx](https://github.com/guokaigdg/animal-island-ui/blob/956f23cb7a388f178dbd98c8cfb9df958a3e3f9f/demo/components/Checkbox/index.tsx)
- [demo/components/CodeBlock/index.tsx](https://github.com/guokaigdg/animal-island-ui/blob/956f23cb7a388f178dbd98c8cfb9df958a3e3f9f/demo/components/CodeBlock/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| assets package | library | Observed | Groups 1 file(s) under assets package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 144 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 6 file(s) under core modules (observed from repository paths and static analysis). |
| demo package | library | Observed | Groups 72 file(s) under demo package (observed from repository paths and static analysis). |
| index.ts package | library | Observed | Groups 1 file(s) under index.ts package (observed from repository paths and static analysis). |
| internal package | library | Observed | Groups 1 file(s) under internal package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 3 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 4 file(s) under tests (observed from repository paths and static analysis). |
| typings.d.ts package | library | Observed | Groups 1 file(s) under typings.d.ts package (observed from repository paths and static analysis). |
| vite-env.d.ts package | library | Observed | Groups 1 file(s) under vite-env.d.ts package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `package.json` (manifest)
- `tsconfig.build.json` (config)
- `tsconfig.json` (config)
- `tsconfig.test.json` (config)

## Top-level layout

- `src` — 225 analysed file(s)
- `demo` — 76 analysed file(s)
- `docs` — 71 analysed file(s)
- `skills` — 25 analysed file(s)
- `(root files)` — 21 analysed file(s)
- `test` — 4 analysed file(s)
- `scripts` — 3 analysed file(s)
- `.github` — 2 analysed file(s)
- `.githooks` — 1 analysed file(s)
- `.trae` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `956f23cb7a388f178dbd98c8cfb9df958a3e3f9f` is the revision these paths and observations refer to.
