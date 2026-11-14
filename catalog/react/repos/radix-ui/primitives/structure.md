# Project structure: radix-ui/primitives

**Analysed commit:** `eb3a2b7091293e27df8f9ba906632d8daa3d81a3`

**Commit reference:** [eb3a2b7091293e27df8f9ba906632d8daa3d81a3](https://github.com/radix-ui/primitives/commit/eb3a2b7091293e27df8f9ba906632d8daa3d81a3)

**Tree at this commit:** [radix-ui/primitives@eb3a2b709129](https://github.com/radix-ui/primitives/tree/eb3a2b7091293e27df8f9ba906632d8daa3d81a3)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | radix-ui/primitives |
| Description | Radix Primitives is an open-source UI component library for building high-quality, accessible design systems and web apps. Maintained by @workos. |
| Stars | 19498 |
| Forks | 1321 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `eb3a2b7091293e27df8f9ba906632d8daa3d81a3` |
| Retrieved at | 2026-11-14T19:13:11.458930+00:00 |
| Files in this snapshot | 699 |

## Directory tree

```text
.changeset/  (19 files)
  README.md
  calm-taps-close.md
  changelog.cjs
  closing-menu-pointer-focus.md
  config.json
  deep-breads-push.md
  five-zoos-smash.md
  fix-nested-context-menu-long-press.md
  hot-areas-teach.md
  lazy-scripts-skip.md
  lemon-experts-vanish.md
  ninety-roses-remain.md
  quiet-bats-defer.md
  quiet-kanji-wait.md
  slick-breads-tap.md
  smart-games-stick.md
  sweet-tigers-wink.md
  tame-bears-call.md
  warm-menus-stay.md
.github/  (15 files)
  ISSUE_TEMPLATE/  (4 files)
    Bug_report.md
    Documentation.md
    Feature_request.md
    Question.md
  actions/  (4 files)
    ci-setup/  (1 files)
      … 1 files under this directory
    detect-snapshot-changes/  (1 files)
      … 1 files under this directory
    publish-snapshot/  (1 files)
      … 1 files under this directory
    publish-stable/  (1 files)
      … 1 files under this directory
  workflows/  (4 files)
    build.yml
    chromatic.yml
    publish.yml
    ssr.yml
  CODEOWNERS
  CONTRIBUTING.md
  PULL_REQUEST_TEMPLATE.md
apps/  (137 files)
  ssr-testing/  (51 files)
    app/  (45 files)
      … 45 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    .gitignore
    README.md
    next.config.js
    package.json
    tsconfig.json
  storybook/  (86 files)
    .storybook/  (5 files)
      … 5 files under this directory
    public/  (1 files)
      … 1 files under this directory
    stories/  (76 files)
      … 76 files under this directory
    .gitignore
    index.d.ts
    package.json
    tsconfig.json
e2e/  (14 files)
  collection.spec.ts
  context-menu.spec.ts
  dialog.spec.ts
  dropdown-menu.spec.ts
  form.spec.ts
  helpers.ts
  menubar.spec.ts
  popover.spec.ts
  popper.spec.ts
  scroll-area.spec.ts
  select.spec.ts
  toast.spec.ts
  toggle-group.spec.ts
  tsconfig.json
internal/  (17 files)
  builder/  (4 files)
    builder.js
    package.json
    radix-build.js
    tsconfig.json
  test-data/  (3 files)
    foods.ts
    package.json
    tsconfig.json
  test-utils/  (3 files)
    package.json
    ref-stability.tsx
    tsconfig.json
  typescript-config/  (7 files)
    react-library/  (1 files)
      … 1 files under this directory
    base.json
    nextjs.json
    package.json
    react-library.json
    vite-app.json
    vite-node.json
packages/  (474 files)
  core/  (31 files)
    env-check/  (7 files)
      … 7 files under this directory
    number/  (6 files)
      … 6 files under this directory
    primitive/  (12 files)
      … 12 files under this directory
    rect/  (6 files)
      … 6 files under this directory
  react/  (443 files)
    accessible-icon/  (7 files)
      … 7 files under this directory
    accordion/  (7 files)
      … 7 files under this directory
    alert-dialog/  (7 files)
      … 7 files under this directory
    announce/  (7 files)
      … 7 files under this directory
    arrow/  (7 files)
      … 7 files under this directory
    aspect-ratio/  (7 files)
      … 7 files under this directory
    avatar/  (7 files)
      … 7 files under this directory
    checkbox/  (7 files)
      … 7 files under this directory
    collapsible/  (7 files)
      … 7 files under this directory
    collection/  (10 files)
      … 10 files under this directory
    compose-refs/  (6 files)
      … 6 files under this directory
    context/  (6 files)
      … 6 files under this directory
    context-menu/  (7 files)
      … 7 files under this directory
    dialog/  (7 files)
      … 7 files under this directory
    direction/  (6 files)
      … 6 files under this directory
    dismissable-layer/  (7 files)
      … 7 files under this directory
    dropdown-menu/  (7 files)
      … 7 files under this directory
    focus-guards/  (7 files)
      … 7 files under this directory
    focus-scope/  (7 files)
      … 7 files under this directory
    form/  (7 files)
      … 7 files under this directory
    hover-card/  (7 files)
      … 7 files under this directory
    id/  (6 files)
      … 6 files under this directory
    label/  (7 files)
      … 7 files under this directory
    menu/  (6 files)
      … 6 files under this directory
    menubar/  (7 files)
      … 7 files under this directory
    navigation-menu/  (7 files)
      … 7 files under this directory
    one-time-password-field/  (7 files)
      … 7 files under this directory
    password-toggle-field/  (7 files)
      … 7 files under this directory
    popover/  (7 files)
      … 7 files under this directory
    popper/  (7 files)
      … 7 files under this directory
    portal/  (7 files)
      … 7 files under this directory
    presence/  (8 files)
      … 8 files under this directory
    primitive/  (7 files)
      … 7 files under this directory
    progress/  (7 files)
      … 7 files under this directory
    radio-group/  (8 files)
      … 8 files under this directory
    radix-ui/  (41 files)
      … 41 files under this directory
    roving-focus/  (6 files)
      … 6 files under this directory
    scroll-area/  (8 files)
      … 8 files under this directory
    select/  (7 files)
      … 7 files under this directory
    separator/  (7 files)
      … 7 files under this directory
    slider/  (7 files)
      … 7 files under this directory
    slot/  (8 files)
      … 8 files under this directory
    switch/  (7 files)
      … 7 files under this directory
    tabs/  (7 files)
      … 7 files under this directory
    toast/  (7 files)
      … 7 files under this directory
    toggle/  (7 files)
      … 7 files under this directory
    toggle-group/  (7 files)
      … 7 files under this directory
    toolbar/  (7 files)
      … 7 files under this directory
    tooltip/  (7 files)
      … 7 files under this directory
    use-callback-ref/  (6 files)
      … 6 files under this directory
    use-controllable-state/  (8 files)
      … 8 files under this directory
    use-effect-event/  (6 files)
      … 6 files under this directory
    use-escape-keydown/  (6 files)
      … 6 files under this directory
    use-is-hydrated/  (7 files)
      … 7 files under this directory
    use-layout-effect/  (6 files)
      … 6 files under this directory
    use-previous/  (6 files)
      … 6 files under this directory
    use-rect/  (6 files)
      … 6 files under this directory
    use-size/  (7 files)
      … 7 files under this directory
    visually-hidden/  (7 files)
      … 7 files under this directory
patches/  (1 files)
  @changesets__apply-release-plan.patch
scripts/  (4 files)
  check-composed-refs.mjs
  rsc-client-boundary-stub.mts
  rsc-compatibility.rsc.test.ts
  setup-tests.ts
types/  (2 files)
  global.d.ts
  index.d.ts
.editorconfig
.gitignore
.nvmrc
.oxfmtrc.json
.oxlintrc.json
AGENTS.md
CODE_OF_CONDUCT.md
LICENSE
README.md
context7.json
package.json
philosophy.md
playwright.config.ts
pnpm-workspace.yaml
release-process.md
vitest.config.mts
```

## Entry points

- [internal/builder/builder.js](https://github.com/radix-ui/primitives/blob/eb3a2b7091293e27df8f9ba906632d8daa3d81a3/internal/builder/builder.js)
- [internal/builder/radix-build.js](https://github.com/radix-ui/primitives/blob/eb3a2b7091293e27df8f9ba906632d8daa3d81a3/internal/builder/radix-build.js)
- [packages/core/number/src/index.ts](https://github.com/radix-ui/primitives/blob/eb3a2b7091293e27df8f9ba906632d8daa3d81a3/packages/core/number/src/index.ts)
- [packages/core/primitive/src/index.ts](https://github.com/radix-ui/primitives/blob/eb3a2b7091293e27df8f9ba906632d8daa3d81a3/packages/core/primitive/src/index.ts)
- [packages/core/rect/src/index.ts](https://github.com/radix-ui/primitives/blob/eb3a2b7091293e27df8f9ba906632d8daa3d81a3/packages/core/rect/src/index.ts)
- [packages/react/accessible-icon/src/index.ts](https://github.com/radix-ui/primitives/blob/eb3a2b7091293e27df8f9ba906632d8daa3d81a3/packages/react/accessible-icon/src/index.ts)
- [packages/react/accordion/src/index.ts](https://github.com/radix-ui/primitives/blob/eb3a2b7091293e27df8f9ba906632d8daa3d81a3/packages/react/accordion/src/index.ts)
- [packages/react/alert-dialog/src/index.ts](https://github.com/radix-ui/primitives/blob/eb3a2b7091293e27df8f9ba906632d8daa3d81a3/packages/react/alert-dialog/src/index.ts)
- [packages/react/announce/src/index.ts](https://github.com/radix-ui/primitives/blob/eb3a2b7091293e27df8f9ba906632d8daa3d81a3/packages/react/announce/src/index.ts)
- [packages/react/arrow/src/index.ts](https://github.com/radix-ui/primitives/blob/eb3a2b7091293e27df8f9ba906632d8daa3d81a3/packages/react/arrow/src/index.ts)
- [packages/react/aspect-ratio/src/index.ts](https://github.com/radix-ui/primitives/blob/eb3a2b7091293e27df8f9ba906632d8daa3d81a3/packages/react/aspect-ratio/src/index.ts)
- [packages/react/avatar/src/index.ts](https://github.com/radix-ui/primitives/blob/eb3a2b7091293e27df8f9ba906632d8daa3d81a3/packages/react/avatar/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| apps package | library | Observed | Groups 94 file(s) under apps package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 146 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| e2e package | library | Observed | Groups 13 file(s) under e2e package (observed from repository paths and static analysis). |
| internal package | library | Observed | Groups 5 file(s) under internal package (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 206 file(s) under packages package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 3 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 14 file(s) under service / domain layer (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 2 file(s) under types package (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.editorconfig` (config)
- `.github/actions/ci-setup/action.yml` (config)
- `.github/actions/detect-snapshot-changes/action.yml` (config)
- `.github/actions/publish-snapshot/action.yml` (config)
- `.github/actions/publish-stable/action.yml` (config)
- `.github/workflows/build.yml` (ci)
- `.github/workflows/chromatic.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.github/workflows/ssr.yml` (ci)
- `.oxfmtrc.json` (config)
- `.oxlintrc.json` (config)
- `apps/ssr-testing/package.json` (manifest)
- `apps/ssr-testing/tsconfig.json` (config)
- `apps/storybook/package.json` (manifest)
- `apps/storybook/tsconfig.json` (config)
- `context7.json` (config)
- `e2e/tsconfig.json` (config)
- `internal/builder/package.json` (manifest)
- `internal/builder/tsconfig.json` (config)
- `internal/test-data/package.json` (manifest)
- `internal/test-data/tsconfig.json` (config)
- `internal/test-utils/package.json` (manifest)
- `internal/test-utils/tsconfig.json` (config)
- `internal/typescript-config/base.json` (config)
- `internal/typescript-config/nextjs.json` (config)
- `internal/typescript-config/package.json` (manifest)
- `internal/typescript-config/react-library.json` (config)
- `internal/typescript-config/vite-app.json` (config)
- `internal/typescript-config/vite-node.json` (config)
- `package.json` (manifest)
- `packages/core/env-check/package.json` (manifest)
- `packages/core/env-check/tsconfig.json` (config)
- `packages/core/number/package.json` (manifest)
- `packages/core/number/tsconfig.json` (config)
- `packages/core/primitive/package.json` (manifest)
- `packages/core/primitive/tsconfig.json` (config)
- `packages/core/rect/package.json` (manifest)
- `packages/core/rect/tsconfig.json` (config)
- `packages/react/accessible-icon/package.json` (manifest)
- `packages/react/accessible-icon/tsconfig.json` (config)
- `packages/react/accordion/package.json` (manifest)
- `packages/react/accordion/tsconfig.json` (config)
- `packages/react/alert-dialog/package.json` (manifest)
- `packages/react/alert-dialog/tsconfig.json` (config)
- `packages/react/announce/package.json` (manifest)
- `packages/react/announce/tsconfig.json` (config)
- `packages/react/arrow/package.json` (manifest)
- `packages/react/arrow/tsconfig.json` (config)
- `packages/react/aspect-ratio/package.json` (manifest)
- `packages/react/aspect-ratio/tsconfig.json` (config)
- `packages/react/avatar/package.json` (manifest)
- `packages/react/avatar/tsconfig.json` (config)
- `packages/react/checkbox/package.json` (manifest)
- `packages/react/checkbox/tsconfig.json` (config)
- `packages/react/collapsible/package.json` (manifest)
- `packages/react/collapsible/tsconfig.json` (config)
- `packages/react/collection/package.json` (manifest)
- `packages/react/collection/tsconfig.json` (config)
- `packages/react/compose-refs/package.json` (manifest)
- `packages/react/compose-refs/tsconfig.json` (config)
- `packages/react/context-menu/package.json` (manifest)
- `packages/react/context-menu/tsconfig.json` (config)
- `packages/react/context/package.json` (manifest)
- `packages/react/context/tsconfig.json` (config)
- `packages/react/dialog/package.json` (manifest)
- `packages/react/dialog/tsconfig.json` (config)
- `packages/react/direction/package.json` (manifest)
- `packages/react/direction/tsconfig.json` (config)
- `packages/react/dismissable-layer/package.json` (manifest)
- `packages/react/dismissable-layer/tsconfig.json` (config)
- `packages/react/dropdown-menu/package.json` (manifest)
- `packages/react/dropdown-menu/tsconfig.json` (config)
- `packages/react/focus-guards/package.json` (manifest)
- `packages/react/focus-guards/tsconfig.json` (config)
- `packages/react/focus-scope/package.json` (manifest)
- `packages/react/focus-scope/tsconfig.json` (config)
- `packages/react/form/package.json` (manifest)
- `packages/react/form/tsconfig.json` (config)
- `packages/react/hover-card/package.json` (manifest)
- `packages/react/hover-card/tsconfig.json` (config)
- `packages/react/id/package.json` (manifest)
- `packages/react/id/tsconfig.json` (config)
- `packages/react/label/package.json` (manifest)
- `packages/react/label/tsconfig.json` (config)
- `packages/react/menu/package.json` (manifest)
- `packages/react/menu/tsconfig.json` (config)
- `packages/react/menubar/package.json` (manifest)
- `packages/react/menubar/tsconfig.json` (config)
- `packages/react/navigation-menu/package.json` (manifest)
- `packages/react/navigation-menu/tsconfig.json` (config)
- `packages/react/one-time-password-field/package.json` (manifest)
- `packages/react/one-time-password-field/tsconfig.json` (config)
- `packages/react/password-toggle-field/package.json` (manifest)
- `packages/react/password-toggle-field/tsconfig.json` (config)
- `packages/react/popover/package.json` (manifest)
- `packages/react/popover/tsconfig.json` (config)
- `packages/react/popper/package.json` (manifest)
- `packages/react/popper/tsconfig.json` (config)
- `packages/react/portal/package.json` (manifest)
- `packages/react/portal/tsconfig.json` (config)
- `packages/react/presence/package.json` (manifest)
- `packages/react/presence/tsconfig.json` (config)
- `packages/react/primitive/package.json` (manifest)
- `packages/react/primitive/tsconfig.json` (config)
- `packages/react/progress/package.json` (manifest)
- `packages/react/progress/tsconfig.json` (config)
- `packages/react/radio-group/package.json` (manifest)
- `packages/react/radio-group/tsconfig.json` (config)
- `packages/react/radix-ui/package.json` (manifest)
- `packages/react/radix-ui/tsconfig.json` (config)
- `packages/react/roving-focus/package.json` (manifest)
- `packages/react/roving-focus/tsconfig.json` (config)
- `packages/react/scroll-area/package.json` (manifest)
- `packages/react/scroll-area/tsconfig.json` (config)
- `packages/react/select/package.json` (manifest)
- `packages/react/select/tsconfig.json` (config)
- `packages/react/separator/package.json` (manifest)
- `packages/react/separator/tsconfig.json` (config)
- `packages/react/slider/package.json` (manifest)
- `packages/react/slider/tsconfig.json` (config)
- `packages/react/slot/package.json` (manifest)
- `packages/react/slot/tsconfig.json` (config)
- `packages/react/switch/package.json` (manifest)
- `packages/react/switch/tsconfig.json` (config)
- `packages/react/tabs/package.json` (manifest)
- `packages/react/tabs/tsconfig.json` (config)
- `packages/react/toast/package.json` (manifest)
- `packages/react/toast/tsconfig.json` (config)
- `packages/react/toggle-group/package.json` (manifest)
- `packages/react/toggle-group/tsconfig.json` (config)
- `packages/react/toggle/package.json` (manifest)
- `packages/react/toggle/tsconfig.json` (config)
- `packages/react/toolbar/package.json` (manifest)
- `packages/react/toolbar/tsconfig.json` (config)
- `packages/react/tooltip/package.json` (manifest)
- `packages/react/tooltip/tsconfig.json` (config)
- `packages/react/use-callback-ref/package.json` (manifest)
- `packages/react/use-callback-ref/tsconfig.json` (config)
- `packages/react/use-controllable-state/package.json` (manifest)
- `packages/react/use-controllable-state/tsconfig.json` (config)
- `packages/react/use-effect-event/package.json` (manifest)
- `packages/react/use-effect-event/tsconfig.json` (config)
- `packages/react/use-escape-keydown/package.json` (manifest)
- `packages/react/use-escape-keydown/tsconfig.json` (config)
- `packages/react/use-is-hydrated/package.json` (manifest)
- `packages/react/use-is-hydrated/tsconfig.json` (config)
- `packages/react/use-layout-effect/package.json` (manifest)
- `packages/react/use-layout-effect/tsconfig.json` (config)
- `packages/react/use-previous/package.json` (manifest)
- `packages/react/use-previous/tsconfig.json` (config)
- `packages/react/use-rect/package.json` (manifest)
- `packages/react/use-rect/tsconfig.json` (config)
- `packages/react/use-size/package.json` (manifest)
- `packages/react/use-size/tsconfig.json` (config)
- `packages/react/visually-hidden/package.json` (manifest)
- `packages/react/visually-hidden/tsconfig.json` (config)
- `pnpm-workspace.yaml` (config)

## Top-level layout

- `packages` — 474 analysed file(s)
- `apps` — 137 analysed file(s)
- `.changeset` — 19 analysed file(s)
- `internal` — 17 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `.github` — 15 analysed file(s)
- `e2e` — 14 analysed file(s)
- `scripts` — 4 analysed file(s)
- `types` — 2 analysed file(s)
- `patches` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `eb3a2b7091293e27df8f9ba906632d8daa3d81a3` is the revision these paths and observations refer to.
