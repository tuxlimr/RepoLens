# Project structure: hello-pangea/dnd

**Analysed commit:** `28c47a7a0139a09b1bf0a77a010e7121c39246d4`

**Commit reference:** [28c47a7a0139a09b1bf0a77a010e7121c39246d4](https://github.com/hello-pangea/dnd/commit/28c47a7a0139a09b1bf0a77a010e7121c39246d4)

**Tree at this commit:** [hello-pangea/dnd@28c47a7a0139](https://github.com/hello-pangea/dnd/tree/28c47a7a0139a09b1bf0a77a010e7121c39246d4)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | hello-pangea/dnd |
| Description | 💅 Beautiful and accessible drag and drop for lists with React. ⭐️ Star to support our work! |
| Stars | 4048 |
| Forks | 133 |
| Licence | Other |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `28c47a7a0139a09b1bf0a77a010e7121c39246d4` |
| Retrieved at | 2026-11-14T19:14:55.695852+00:00 |
| Files in this snapshot | 742 |

## Directory tree

```text
.circleci/  (1 files)
  config.yml
.github/  (5 files)
  ISSUE_TEMPLATE/  (3 files)
    bug-report.md
    feature-request.md
    tree-issue.md
  workflows/  (2 files)
    chromatic.yml
    commitlint.yml
.husky/  (1 files)
  commit-msg
.storybook/  (11 files)
  custom-decorators/  (1 files)
    global-styles.ts
  .eslintrc.js
  environment.d.ts
  main.ts
  manager.ts
  preview-head.html
  preview.tsx
  storybook-theme.ts
  tsconfig.json
  typings.d.ts
  welcome-message.ts
csp-server/  (8 files)
  app.tsx
  client.tsx
  environment.d.ts
  main.js
  server.tsx
  start.sh
  tsconfig.json
  webpack.config.js
cypress/  (14 files)
  fixtures/  (1 files)
    .gitkeep
  integration/  (7 files)
    content-security-policy.spec.ts
    focus.spec.ts
    move-between-lists.spec.ts
    reorder-lists.spec.ts
    reorder-virtual.spec.ts
    reorder.spec.ts
    util.ts
  support/  (4 files)
    commands.ts
    component-index.html
    component.ts
    e2e.ts
  .eslintrc.js
  tsconfig.json
docs/  (40 files)
  about/  (6 files)
    accessibility.md
    animations.md
    browser-support.md
    design-principles.md
    examples.md
    installation.md
  api/  (3 files)
    drag-drop-context.md
    draggable.md
    droppable.md
  guides/  (20 files)
    auto-scrolling.md
    avoiding-image-flickering.md
    browser-focus.md
    changes-while-dragging.md
    combining.md
    common-setup-issues.md
    content-security-policy.md
    doctype.md
    dragging-svgs.md
    drop-animation.md
    how-we-detect-scroll-containers.md
    how-we-use-dom-events.md
    identifiers.md
    preset-styles.md
    reparenting.md
    responders.md
    screen-reader.md
    setup-problem-detection-and-error-recovery.md
    types.md
    using-inner-ref.md
  patterns/  (3 files)
    multi-drag.md
    tables.md
    virtual-lists.md
  sensors/  (4 files)
    keyboard.md
    mouse.md
    sensor-api.md
    touch.md
  support/  (4 files)
    community-and-addons.md
    engineering-health.md
    media.md
    upgrading.md
src/  (237 files)
  debug/  (5 files)
    middleware/  (4 files)
      … 4 files under this directory
    timings.ts
  state/  (127 files)
    auto-scroller/  (20 files)
      … 20 files under this directory
    calculate-drag-impact/  (1 files)
      … 1 files under this directory
    dimension-marshal/  (4 files)
      … 4 files under this directory
    droppable/  (9 files)
      … 9 files under this directory
    get-center-from-impact/  (6 files)
      … 6 files under this directory
    get-drag-impact/  (3 files)
      … 3 files under this directory
    middleware/  (21 files)
      … 21 files under this directory
    move-in-direction/  (13 files)
      … 13 files under this directory
    post-reducer/  (2 files)
      … 2 files under this directory
    publish-while-dragging-in-virtual/  (3 files)
      … 3 files under this directory
    registry/  (3 files)
      … 3 files under this directory
    update-displacement-visibility/  (2 files)
      … 2 files under this directory
    visibility/  (5 files)
      … 5 files under this directory
    with-scroll-change/  (4 files)
      … 4 files under this directory
    action-creators.ts
    axis.ts
    can-start-drag.ts
    create-store.ts
    did-start-after-critical.ts
    dimension-structures.ts
    get-combined-item-displacement.ts
    get-displaced-by.ts
    get-displacement-groups.ts
    get-draggables-inside-droppable.ts
    get-droppable-over.ts
    get-frame.ts
    get-home-location.ts
    get-impact-location.ts
    get-is-displaced.ts
    get-lift-effect.ts
    get-max-scroll.ts
    is-dragging.ts
    is-movement-allowed.ts
    is-within.ts
    no-impact.ts
    patch-dimension-map.ts
    patch-droppable-map.ts
    position.ts
    … 7 more files
  view/  (92 files)
    animate-in-out/  (2 files)
      … 2 files under this directory
    context/  (3 files)
      … 3 files under this directory
    drag-drop-context/  (9 files)
      … 9 files under this directory
    draggable/  (7 files)
      … 7 files under this directory
    droppable/  (5 files)
      … 5 files under this directory
    event-bindings/  (2 files)
      … 2 files under this directory
    get-elements/  (2 files)
      … 2 files under this directory
    is-type-of-element/  (3 files)
      … 3 files under this directory
    placeholder/  (3 files)
      … 3 files under this directory
    use-announcer/  (2 files)
      … 2 files under this directory
    use-draggable-publisher/  (3 files)
      … 3 files under this directory
    use-droppable-publisher/  (9 files)
      … 9 files under this directory
    use-focus-marshal/  (3 files)
      … 3 files under this directory
    use-hidden-text-element/  (2 files)
      … 2 files under this directory
    use-sensor-marshal/  (12 files)
      … 12 files under this directory
    use-style-marshal/  (4 files)
      … 4 files under this directory
    window/  (5 files)
      … 5 files under this directory
    check-is-valid-inner-ref.ts
    data-attributes.ts
    get-body-element.ts
    get-border-box-center-position.ts
    get-document-element.ts
    is-strict-equal.ts
    key-codes.ts
    scroll-listener.ts
    throw-if-invalid-inner-ref.ts
    use-dev-setup-warning.ts
    use-dev.ts
    use-isomorphic-layout-effect.ts
    use-previous-ref.ts
    use-required-context.ts
    use-unique-id.ts
    visually-hidden-style.ts
  animation.ts
  are-inputs-equal.ts
  dev-warning.ts
  empty.ts
  global.d.ts
  index.ts
  invariant.ts
  lib-types.ts
  memoize-one.ts
  query-selector-all.ts
  screen-reader-message-preset.ts
  types.ts
  use-memo-one.ts
stories/  (85 files)
  examples/  (24 files)
    1-single-vertical-list.stories.tsx
    10-table.stories.tsx
    11-portal.stories.tsx
    12-dynamic.stories.tsx
    15-on-before-capture.stories.tsx
    2-single-horizontal.stories.tsx
    20-super-simple.stories.tsx
    21-change-on-drag-start.stories.tsx
    25-fixed-list.stories.tsx
    3-board.stories.stories.tsx
    30-custom-drop.stories.tsx
    35-function-component.stories.tsx
    4-complex-vertical-list.stories.tsx
    40-programmatic.stories.tsx
    45-virtual.stories.tsx
    5-multiple-vertical-lists.stories.tsx
    50-multiple-contexts.stories.tsx
    55-mixed-sizes.stories.tsx
    6-multiple-horizontal-lists.stories.tsx
    60-autoscroll-options.stories.tsx
    7-interactive-elements.stories.tsx
    8-accessibility.stories.tsx
    9-multi-drag.stories.tsx
    99-debug.stories.tsx
  src/  (57 files)
    accessible/  (5 files)
      … 5 files under this directory
    board/  (2 files)
      … 2 files under this directory
    custom-drop/  (2 files)
      … 2 files under this directory
    customize-autoscroll/  (2 files)
      … 2 files under this directory
    dynamic/  (2 files)
      … 2 files under this directory
    fixed-list/  (1 files)
      … 1 files under this directory
    function-component/  (1 files)
      … 1 files under this directory
    horizontal/  (1 files)
      … 1 files under this directory
    interactive-elements/  (1 files)
      … 1 files under this directory
    mixed-sizes/  (3 files)
      … 3 files under this directory
    multi-drag/  (6 files)
      … 6 files under this directory
    multiple-horizontal/  (1 files)
      … 1 files under this directory
    multiple-vertical/  (1 files)
      … 1 files under this directory
    on-before-capture/  (1 files)
      … 1 files under this directory
    portal/  (1 files)
      … 1 files under this directory
    primatives/  (5 files)
      … 5 files under this directory
    programmatic/  (3 files)
      … 3 files under this directory
    simple/  (3 files)
      … 3 files under this directory
    table/  (4 files)
      … 4 files under this directory
    vertical/  (1 files)
      … 1 files under this directory
    vertical-grouped/  (1 files)
      … 1 files under this directory
    vertical-nested/  (3 files)
      … 3 files under this directory
    virtual/  (3 files)
      … 3 files under this directory
    constants.ts
    data.ts
    reorder.ts
    types.ts
  .eslintrc.js
  Welcome.mdx
  tsconfig.json
  typings.d.ts
test/  (310 files)
  setup/  (6 files)
    attach-raf-stub.ts
    browser.ts
    env-setup.ts
    environment.ts
    test-setup.ts
    transition-event-polyfill.ts
  typings/  (3 files)
    environment.d.ts
    raf-stub.d.ts
    testing-library-dom.d.ts
  unit/  (276 files)
    docs/  (2 files)
      … 2 files under this directory
    health/  (2 files)
      … 2 files under this directory
    integration/  (74 files)
      … 74 files under this directory
    state/  (131 files)
      … 131 files under this directory
    view/  (64 files)
      … 64 files under this directory
    dev-warning.spec.ts
    memoize-one.spec.ts
    use-memo-one.spec.tsx
  util/  (23 files)
    after-point.ts
    before-point.ts
    cause-runtime-error.ts
    clone-impact.ts
    console.ts
    create-ref.ts
    dimension-marshal.ts
    dimension.ts
    dragging-state.ts
    get-react-major-version.ts
    get-simple-state-preset.ts
    impact.ts
    is-running-in-ci.ts
    no-after-critical.ts
    preset-action-args.ts
    registry.ts
    reorder.ts
    set-dom-rect.ts
    set-window-scroll-size.ts
    set-window-scroll.ts
    spacing.ts
    viewport.ts
    writable.ts
  .eslintrc.js
  tsconfig.json
test-reports/  (1 files)
  lighthouse/  (1 files)
    .gitkeep
.browserslistrc
.commitlintrc.json
.czrc
.eslintignore
.eslintrc.js
.gitignore
.node-version
.prettierignore
.prettierrc
.release-it.json
.stylelintignore
.stylelintrc.json
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
SECURITY.md
a11y-audit-parse.js
babel.config.js
browser-test-harness.js
cypress.config.ts
jest.config.ts
lighthouse.config.js
… 5 more files
```

## Entry points

- [.storybook/main.ts](https://github.com/hello-pangea/dnd/blob/28c47a7a0139a09b1bf0a77a010e7121c39246d4/.storybook/main.ts)
- [csp-server/app.tsx](https://github.com/hello-pangea/dnd/blob/28c47a7a0139a09b1bf0a77a010e7121c39246d4/csp-server/app.tsx)
- [csp-server/main.js](https://github.com/hello-pangea/dnd/blob/28c47a7a0139a09b1bf0a77a010e7121c39246d4/csp-server/main.js)
- [src/index.ts](https://github.com/hello-pangea/dnd/blob/28c47a7a0139a09b1bf0a77a010e7121c39246d4/src/index.ts)
- [src/state/auto-scroller/index.ts](https://github.com/hello-pangea/dnd/blob/28c47a7a0139a09b1bf0a77a010e7121c39246d4/src/state/auto-scroller/index.ts)
- [src/state/get-drag-impact/index.ts](https://github.com/hello-pangea/dnd/blob/28c47a7a0139a09b1bf0a77a010e7121c39246d4/src/state/get-drag-impact/index.ts)
- [src/state/move-in-direction/index.ts](https://github.com/hello-pangea/dnd/blob/28c47a7a0139a09b1bf0a77a010e7121c39246d4/src/state/move-in-direction/index.ts)
- [src/state/publish-while-dragging-in-virtual/index.ts](https://github.com/hello-pangea/dnd/blob/28c47a7a0139a09b1bf0a77a010e7121c39246d4/src/state/publish-while-dragging-in-virtual/index.ts)
- [src/view/animate-in-out/index.ts](https://github.com/hello-pangea/dnd/blob/28c47a7a0139a09b1bf0a77a010e7121c39246d4/src/view/animate-in-out/index.ts)
- [src/view/drag-drop-context/app.tsx](https://github.com/hello-pangea/dnd/blob/28c47a7a0139a09b1bf0a77a010e7121c39246d4/src/view/drag-drop-context/app.tsx)
- [src/view/drag-drop-context/index.ts](https://github.com/hello-pangea/dnd/blob/28c47a7a0139a09b1bf0a77a010e7121c39246d4/src/view/drag-drop-context/index.ts)
- [src/view/draggable/index.ts](https://github.com/hello-pangea/dnd/blob/28c47a7a0139a09b1bf0a77a010e7121c39246d4/src/view/draggable/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| animation.ts package | library | Observed | Groups 1 file(s) under animation.ts package (observed from repository paths and static analysis). |
| are-inputs-equal.ts package | library | Observed | Groups 1 file(s) under are-inputs-equal.ts package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 8 file(s) under core modules (observed from repository paths and static analysis). |
| csp-server package | library | Observed | Groups 7 file(s) under csp-server package (observed from repository paths and static analysis). |
| cypress package | library | Observed | Groups 4 file(s) under cypress package (observed from repository paths and static analysis). |
| debug package | library | Observed | Groups 5 file(s) under debug package (observed from repository paths and static analysis). |
| dev-warning.ts package | library | Observed | Groups 1 file(s) under dev-warning.ts package (observed from repository paths and static analysis). |
| empty.ts package | library | Observed | Groups 1 file(s) under empty.ts package (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 7 file(s) under external integrations (observed from repository paths and static analysis). |
| global.d.ts package | library | Observed | Groups 1 file(s) under global.d.ts package (observed from repository paths and static analysis). |
| index.ts package | library | Observed | Groups 1 file(s) under index.ts package (observed from repository paths and static analysis). |
| invariant.ts package | library | Observed | Groups 1 file(s) under invariant.ts package (observed from repository paths and static analysis). |
| lib-types.ts package | library | Observed | Groups 1 file(s) under lib-types.ts package (observed from repository paths and static analysis). |
| memoize-one.ts package | library | Observed | Groups 1 file(s) under memoize-one.ts package (observed from repository paths and static analysis). |
| query-selector-all.ts package | library | Observed | Groups 1 file(s) under query-selector-all.ts package (observed from repository paths and static analysis). |
| screen-reader-message-preset.ts package | library | Observed | Groups 1 file(s) under screen-reader-message-preset.ts package (observed from repository paths and static analysis). |
| state package | library | Observed | Groups 127 file(s) under state package (observed from repository paths and static analysis). |
| stories package | library | Observed | Groups 83 file(s) under stories package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 310 file(s) under tests (observed from repository paths and static analysis). |
| types.ts package | library | Observed | Groups 1 file(s) under types.ts package (observed from repository paths and static analysis). |
| use-memo-one.ts package | library | Observed | Groups 1 file(s) under use-memo-one.ts package (observed from repository paths and static analysis). |
| view package | library | Observed | Groups 92 file(s) under view package (observed from repository paths and static analysis). |

## Important files

- `.circleci/config.yml` (ci)
- `.commitlintrc.json` (config)
- `.github/workflows/chromatic.yml` (ci)
- `.github/workflows/commitlint.yml` (ci)
- `.release-it.json` (config)
- `.storybook/tsconfig.json` (config)
- `.stylelintrc.json` (config)
- `csp-server/tsconfig.json` (config)
- `cypress/tsconfig.json` (config)
- `package.json` (manifest)
- `stories/tsconfig.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `test` — 310 analysed file(s)
- `src` — 237 analysed file(s)
- `stories` — 85 analysed file(s)
- `docs` — 40 analysed file(s)
- `(root files)` — 29 analysed file(s)
- `cypress` — 14 analysed file(s)
- `.storybook` — 11 analysed file(s)
- `csp-server` — 8 analysed file(s)
- `.github` — 5 analysed file(s)
- `.circleci` — 1 analysed file(s)
- `.husky` — 1 analysed file(s)
- `test-reports` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `28c47a7a0139a09b1bf0a77a010e7121c39246d4` is the revision these paths and observations refer to.
