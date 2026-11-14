# Project structure: atlassian/react-beautiful-dnd

**Analysed commit:** `2baf5c6344cbb7862cf21ee697152bffb3765fa9`

**Commit reference:** [2baf5c6344cbb7862cf21ee697152bffb3765fa9](https://github.com/atlassian/react-beautiful-dnd/commit/2baf5c6344cbb7862cf21ee697152bffb3765fa9)

**Tree at this commit:** [atlassian/react-beautiful-dnd@2baf5c6344cb](https://github.com/atlassian/react-beautiful-dnd/tree/2baf5c6344cbb7862cf21ee697152bffb3765fa9)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | atlassian/react-beautiful-dnd |
| Description | Beautiful and accessible drag and drop for lists with React |
| Stars | 33884 |
| Forks | 2684 |
| Licence | Other |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `2baf5c6344cbb7862cf21ee697152bffb3765fa9` |
| Retrieved at | 2026-11-14T19:13:01.829112+00:00 |
| Files in this snapshot | 782 |

## Directory tree

```text
.circleci/  (1 files)
  config.yml
.github/  (3 files)
  ISSUE_TEMPLATE/  (3 files)
    bug-report.md
    feature-request.md
    tree-issue.md
.storybook/  (7 files)
  custom-decorators/  (1 files)
    global-styles.jsx
  .babelrc
  babel-setup.md
  compressed-logo-rbd.svg
  config.js
  main.js
  preview-head.html
csp-server/  (7 files)
  .eslintrc.js
  app.jsx
  client.js
  main.js
  server.js
  start.sh
  webpack.config.js
cypress/  (12 files)
  fixtures/  (1 files)
    .gitkeep
  integration/  (7 files)
    content-security-policy.spec.js
    focus.spec.js
    move-between-lists.spec.js
    reorder-lists.spec.js
    reorder-virtual.spec.js
    reorder.spec.js
    util.js
  plugins/  (1 files)
    index.js
  support/  (2 files)
    commands.js
    index.js
  .eslintrc.js
docs/  (41 files)
  about/  (6 files)
    accessibility.md
    animations.md
    browser-support.md
    design-principles.md
    examples.md
    installation.md
  api/  (4 files)
    drag-drop-context.md
    draggable.md
    droppable.md
    reset-server-context.md
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
flow-typed/  (71 files)
  custom/  (2 files)
    cypress.js
    raf.js
  npm/  (69 files)
    @atlaskit/  (2 files)
      … 2 files under this directory
    @babel/  (9 files)
      … 9 files under this directory
    @emotion/  (1 files)
      … 1 files under this directory
    @storybook/  (2 files)
      … 2 files under this directory
    @testing-library/  (1 files)
      … 1 files under this directory
    babel-core_vx.x.x.js
    babel-eslint_vx.x.x.js
    babel-jest_vx.x.x.js
    babel-loader_vx.x.x.js
    babel-plugin-dev-expression_vx.x.x.js
    cross-env_vx.x.x.js
    cypress_vx.x.x.js
    enzyme-adapter-react-16_vx.x.x.js
    enzyme_v3.x.x.js
    eslint-config-airbnb_vx.x.x.js
    eslint-config-prettier_vx.x.x.js
    eslint-plugin-cypress_vx.x.x.js
    eslint-plugin-es5_vx.x.x.js
    eslint-plugin-flowtype_vx.x.x.js
    eslint-plugin-import_vx.x.x.js
    eslint-plugin-jest_vx.x.x.js
    eslint-plugin-jsx-a11y_vx.x.x.js
    eslint-plugin-prettier_vx.x.x.js
    eslint-plugin-react-hooks_vx.x.x.js
    eslint-plugin-react_vx.x.x.js
    eslint_vx.x.x.js
    flow-bin_v0.x.x.js
    fs-extra_vx.x.x.js
    globby_vx.x.x.js
    … 30 more files
src/  (231 files)
  debug/  (5 files)
    middleware/  (4 files)
      … 4 files under this directory
    timings.js
  state/  (126 files)
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
    action-creators.js
    axis.js
    can-start-drag.js
    create-store.js
    did-start-after-critical.js
    dimension-structures.js
    get-combined-item-displacement.js
    get-displaced-by.js
    get-displacement-groups.js
    get-draggables-inside-droppable.js
    get-droppable-over.js
    get-frame.js
    get-home-location.js
    get-impact-location.js
    get-is-displaced.js
    get-lift-effect.js
    get-max-scroll.js
    is-movement-allowed.js
    is-within.js
    no-impact.js
    patch-dimension-map.js
    patch-droppable-map.js
    position.js
    recompute-placeholders.js
    … 6 more files
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
    check-is-valid-inner-ref.js
    data-attributes.js
    get-body-element.js
    get-border-box-center-position.js
    get-document-element.js
    is-strict-equal.js
    key-codes.js
    scroll-listener.js
    throw-if-invalid-inner-ref.js
    use-dev-setup-warning.js
    use-dev.js
    use-isomorphic-layout-effect.js
    use-previous-ref.js
    use-required-context.js
    use-unique-id.js
    visually-hidden-style.js
  animation.js
  dev-warning.js
  empty.js
  index.js
  invariant.js
  native-with-fallback.js
  screen-reader-message-preset.js
  types.js
stories/  (82 files)
  src/  (58 files)
    accessible/  (5 files)
      … 5 files under this directory
    board/  (2 files)
      … 2 files under this directory
    custom-drop/  (2 files)
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
    virtual/  (6 files)
      … 6 files under this directory
    constants.js
    data.js
    reorder.js
    types.js
  .eslintrc.js
  1-single-vertical-list.stories.js
  10-table.stories.js
  11-portal.stories.js
  12-dynamic.stories.js
  15-on-before-capture.stories.js
  2-single-horizontal.stories.js
  20-super-simple.stories.js
  21-change-on-drag-start.stories.js
  25-fixed-list.stories.js
  3-board.stories.stories.js
  30-custom-drop.stories.js
  35-function-component.stories.js
  4-complex-vertical-list.stories.js
  40-programmatic.stories.js
  45-virtual.stories.js
  5-multiple-vertical-lists.stories.js
  50-multiple-contexts.stories.js
  55-mixed-sizes.stories.js
  6-multiple-horizontal-lists.stories.js
  7-interactive-elements.stories.js
  8-accessibility.stories.js
  9-multi-drag.stories.js
  99-debug.stories.js
test/  (302 files)
  unit/  (275 files)
    docs/  (2 files)
      … 2 files under this directory
    health/  (2 files)
      … 2 files under this directory
    integration/  (75 files)
      … 75 files under this directory
    state/  (130 files)
      … 130 files under this directory
    view/  (65 files)
      … 65 files under this directory
    dev-warning.spec.js
  util/  (23 files)
    after-point.js
    before-point.js
    cause-runtime-error.js
    clone-impact.js
    console.js
    create-ref.js
    dimension-marshal.js
    dimension.js
    dragging-state.js
    force-update.js
    get-simple-state-preset.js
    impact.js
    no-after-critical.js
    pass-through-props.jsx
    preset-action-args.js
    registry.js
    reorder.js
    set-window-scroll-size.js
    set-window-scroll.js
    spacing.js
    try-clean-prototype-stubs.js
    user-input-util.js
    viewport.js
  .eslintrc.js
  env-setup.js
  test-flow-types.js
  test-setup.js
test-reports/  (1 files)
  lighthouse/  (1 files)
    .gitkeep
.browserlistrc
.eslintignore
.eslintrc.js
.flowconfig
.gitignore
.nvmrc
.prettierignore
.prettierrc
.size-snapshot.json
.stylelintrc.json
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
a11y-audit-parse.js
babel.config.js
browser-test-harness.js
cypress.json
jest.config.js
package.json
renovate.json
rollup.config.js
server-ports.js
```

## Entry points

- [.storybook/main.js](https://github.com/atlassian/react-beautiful-dnd/blob/2baf5c6344cbb7862cf21ee697152bffb3765fa9/.storybook/main.js)
- [csp-server/app.jsx](https://github.com/atlassian/react-beautiful-dnd/blob/2baf5c6344cbb7862cf21ee697152bffb3765fa9/csp-server/app.jsx)
- [csp-server/main.js](https://github.com/atlassian/react-beautiful-dnd/blob/2baf5c6344cbb7862cf21ee697152bffb3765fa9/csp-server/main.js)
- [csp-server/server.js](https://github.com/atlassian/react-beautiful-dnd/blob/2baf5c6344cbb7862cf21ee697152bffb3765fa9/csp-server/server.js)
- [cypress/plugins/index.js](https://github.com/atlassian/react-beautiful-dnd/blob/2baf5c6344cbb7862cf21ee697152bffb3765fa9/cypress/plugins/index.js)
- [cypress/support/index.js](https://github.com/atlassian/react-beautiful-dnd/blob/2baf5c6344cbb7862cf21ee697152bffb3765fa9/cypress/support/index.js)
- [src/index.js](https://github.com/atlassian/react-beautiful-dnd/blob/2baf5c6344cbb7862cf21ee697152bffb3765fa9/src/index.js)
- [src/state/auto-scroller/index.js](https://github.com/atlassian/react-beautiful-dnd/blob/2baf5c6344cbb7862cf21ee697152bffb3765fa9/src/state/auto-scroller/index.js)
- [src/state/get-drag-impact/index.js](https://github.com/atlassian/react-beautiful-dnd/blob/2baf5c6344cbb7862cf21ee697152bffb3765fa9/src/state/get-drag-impact/index.js)
- [src/state/move-in-direction/index.js](https://github.com/atlassian/react-beautiful-dnd/blob/2baf5c6344cbb7862cf21ee697152bffb3765fa9/src/state/move-in-direction/index.js)
- [src/state/publish-while-dragging-in-virtual/index.js](https://github.com/atlassian/react-beautiful-dnd/blob/2baf5c6344cbb7862cf21ee697152bffb3765fa9/src/state/publish-while-dragging-in-virtual/index.js)
- [src/view/animate-in-out/index.js](https://github.com/atlassian/react-beautiful-dnd/blob/2baf5c6344cbb7862cf21ee697152bffb3765fa9/src/view/animate-in-out/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| animation.js package | library | Observed | Groups 1 file(s) under animation.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 6 file(s) under core modules (observed from repository paths and static analysis). |
| csp-server package | library | Observed | Groups 7 file(s) under csp-server package (observed from repository paths and static analysis). |
| cypress package | library | Observed | Groups 4 file(s) under cypress package (observed from repository paths and static analysis). |
| debug package | library | Observed | Groups 5 file(s) under debug package (observed from repository paths and static analysis). |
| dev-warning.js package | library | Observed | Groups 1 file(s) under dev-warning.js package (observed from repository paths and static analysis). |
| empty.js package | library | Observed | Groups 1 file(s) under empty.js package (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 7 file(s) under external integrations (observed from repository paths and static analysis). |
| flow-typed package | library | Observed | Groups 71 file(s) under flow-typed package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| invariant.js package | library | Observed | Groups 1 file(s) under invariant.js package (observed from repository paths and static analysis). |
| native-with-fallback.js package | library | Observed | Groups 1 file(s) under native-with-fallback.js package (observed from repository paths and static analysis). |
| screen-reader-message-preset.js package | library | Observed | Groups 1 file(s) under screen-reader-message-preset.js package (observed from repository paths and static analysis). |
| state package | library | Observed | Groups 126 file(s) under state package (observed from repository paths and static analysis). |
| stories package | library | Observed | Groups 82 file(s) under stories package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 302 file(s) under tests (observed from repository paths and static analysis). |
| types.js package | library | Observed | Groups 1 file(s) under types.js package (observed from repository paths and static analysis). |
| view package | library | Observed | Groups 92 file(s) under view package (observed from repository paths and static analysis). |

## Important files

- `.circleci/config.yml` (ci)
- `.size-snapshot.json` (config)
- `.stylelintrc.json` (config)
- `cypress.json` (config)
- `package.json` (manifest)
- `renovate.json` (config)

## Top-level layout

- `test` — 302 analysed file(s)
- `src` — 231 analysed file(s)
- `stories` — 82 analysed file(s)
- `flow-typed` — 71 analysed file(s)
- `docs` — 41 analysed file(s)
- `(root files)` — 24 analysed file(s)
- `cypress` — 12 analysed file(s)
- `.storybook` — 7 analysed file(s)
- `csp-server` — 7 analysed file(s)
- `.github` — 3 analysed file(s)
- `.circleci` — 1 analysed file(s)
- `test-reports` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `2baf5c6344cbb7862cf21ee697152bffb3765fa9` is the revision these paths and observations refer to.
