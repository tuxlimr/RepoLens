# Project structure: geist-org/geist-ui

**Analysed commit:** `6894bfdf12bca17ae292617cf2b69c63731fd5d4`

**Commit reference:** [6894bfdf12bca17ae292617cf2b69c63731fd5d4](https://github.com/geist-org/geist-ui/commit/6894bfdf12bca17ae292617cf2b69c63731fd5d4)

**Tree at this commit:** [geist-org/geist-ui@6894bfdf12bc](https://github.com/geist-org/geist-ui/tree/6894bfdf12bca17ae292617cf2b69c63731fd5d4)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | geist-org/geist-ui |
| Description | A design system for building modern websites and applications. |
| Stars | 4543 |
| Forks | 335 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `6894bfdf12bca17ae292617cf2b69c63731fd5d4` |
| Retrieved at | 2026-11-14T19:14:42.996984+00:00 |
| Files in this snapshot | 752 |

## Directory tree

```text
.circleci/  (1 files)
  config.yml
.github/  (8 files)
  ISSUE_TEMPLATE/  (4 files)
    1-bug-report.md
    2-feature-request.md
    3-docs.md
    config.yml
  workflows/  (1 files)
    publish.yml
  CODE_OF_CONDUCT.md
  CONTRIBUTING.md
  PULL_REQUEST_TEMPLATE.md
components/  (426 files)
  auto-complete/  (12 files)
    __tests__/  (5 files)
      … 5 files under this directory
    auto-complete-context.ts
    auto-complete-dropdown.tsx
    auto-complete-empty.tsx
    auto-complete-item.tsx
    auto-complete-searching.tsx
    auto-complete.tsx
    index.ts
  avatar/  (5 files)
    __tests__/  (2 files)
      … 2 files under this directory
    avatar-group.tsx
    avatar.tsx
    index.ts
  badge/  (7 files)
    __tests__/  (4 files)
      … 4 files under this directory
    badge-anchor.tsx
    badge.tsx
    index.ts
  breadcrumbs/  (6 files)
    __tests__/  (2 files)
      … 2 files under this directory
    breadcrumbs-item.tsx
    breadcrumbs-separator.tsx
    breadcrumbs.tsx
    index.ts
  button/  (11 files)
    __tests__/  (4 files)
      … 4 files under this directory
    button-icon.tsx
    button-loading.tsx
    button.drip.tsx
    button.tsx
    index.ts
    styles.ts
    utils.tsx
  button-dropdown/  (7 files)
    __tests__/  (1 files)
      … 1 files under this directory
    button-dropdown-context.ts
    button-dropdown-item.tsx
    button-dropdown.tsx
    icon.tsx
    index.ts
    styles.ts
  button-group/  (5 files)
    __tests__/  (2 files)
      … 2 files under this directory
    button-group-context.ts
    button-group.tsx
    index.ts
  capacity/  (4 files)
    __tests__/  (2 files)
      … 2 files under this directory
    capacity.tsx
    index.ts
  card/  (8 files)
    __tests__/  (3 files)
      … 3 files under this directory
    card-content.tsx
    card-footer.tsx
    card.tsx
    index.ts
    styles.ts
  checkbox/  (10 files)
    __tests__/  (4 files)
      … 4 files under this directory
    checkbox-context.ts
    checkbox-group.tsx
    checkbox.icon.tsx
    checkbox.tsx
    index.ts
    styles.ts
  code/  (4 files)
    __tests__/  (2 files)
      … 2 files under this directory
    code.tsx
    index.ts
  col/  (4 files)
    __tests__/  (2 files)
      … 2 files under this directory
    col.tsx
    index.ts
  collapse/  (7 files)
    __tests__/  (2 files)
      … 2 files under this directory
    collapse-context.ts
    collapse-group.tsx
    collapse-icon.tsx
    collapse.tsx
    index.ts
  css-baseline/  (4 files)
    __tests__/  (2 files)
      … 2 files under this directory
    css-baseline.tsx
    index.ts
  description/  (4 files)
    __tests__/  (2 files)
      … 2 files under this directory
    description.tsx
    index.ts
  display/  (4 files)
    __tests__/  (2 files)
      … 2 files under this directory
    display.tsx
    index.ts
  divider/  (4 files)
    __tests__/  (2 files)
      … 2 files under this directory
    divider.tsx
    index.ts
  dot/  (4 files)
    __tests__/  (2 files)
      … 2 files under this directory
    dot.tsx
    index.ts
  drawer/  (7 files)
    __tests__/  (3 files)
      … 3 files under this directory
    drawer-wrapper.tsx
    drawer.tsx
    helper.ts
    index.ts
  fieldset/  (11 files)
    __tests__/  (3 files)
      … 3 files under this directory
    fieldset-content.tsx
    fieldset-context.ts
    fieldset-footer.tsx
    fieldset-group.tsx
    fieldset-subtitle.tsx
    fieldset-title.tsx
    fieldset.tsx
    index.ts
  geist-provider/  (3 files)
    geist-provider.tsx
    index.ts
    theme-provider.tsx
  grid/  (7 files)
    __tests__/  (2 files)
      … 2 files under this directory
    basic-item.tsx
    grid-container.tsx
    grid-types.ts
    grid.tsx
    index.ts
  image/  (10 files)
    __tests__/  (3 files)
      … 3 files under this directory
    helpers.ts
    image-browser-https-icon.tsx
    image-browser.tsx
    image.skeleton.tsx
    image.tsx
    index.ts
    styles.ts
  input/  (14 files)
    __tests__/  (4 files)
      … 4 files under this directory
    index.ts
    input-block-label.tsx
    input-icon-clear.tsx
    input-icon.tsx
    input-label.tsx
    input-props.ts
    input.tsx
    password-icon.tsx
    password.tsx
    styles.ts
  keyboard/  (4 files)
    __tests__/  (2 files)
      … 2 files under this directory
    index.ts
    keyboard.tsx
  link/  (5 files)
    __tests__/  (2 files)
      … 2 files under this directory
    icon.tsx
    index.ts
    link.tsx
  loading/  (4 files)
    __tests__/  (2 files)
      … 2 files under this directory
    index.ts
    loading.tsx
  modal/  (11 files)
    __tests__/  (2 files)
      … 2 files under this directory
    index.ts
    modal-action.tsx
    modal-actions.tsx
    modal-content.tsx
    modal-context.ts
    modal-subtitle.tsx
    modal-title.tsx
    modal-wrapper.tsx
    modal.tsx
  note/  (4 files)
    __tests__/  (2 files)
      … 2 files under this directory
    index.ts
    note.tsx
  page/  (9 files)
    __tests__/  (4 files)
      … 4 files under this directory
    index.ts
    page-content.tsx
    page-footer.tsx
    page-header.tsx
    page.tsx
  pagination/  (10 files)
    __tests__/  (2 files)
      … 2 files under this directory
    index.ts
    pagination-context.ts
    pagination-ellipsis.tsx
    pagination-item.tsx
    pagination-next.tsx
    pagination-pages.tsx
    pagination-previous.tsx
    pagination.tsx
  popover/  (6 files)
    __tests__/  (2 files)
      … 2 files under this directory
    index.ts
    popover-context.ts
    popover-item.tsx
    popover.tsx
  progress/  (4 files)
    __tests__/  (2 files)
      … 2 files under this directory
    index.ts
    progress.tsx
  radio/  (10 files)
    __tests__/  (4 files)
      … 4 files under this directory
    index.ts
    radio-context.ts
    radio-description.tsx
    radio-group.tsx
    radio.tsx
    styles.ts
  rating/  (5 files)
    __tests__/  (2 files)
      … 2 files under this directory
    index.ts
    rating-icon.tsx
    rating.tsx
  row/  (4 files)
    __tests__/  (2 files)
      … 2 files under this directory
    index.ts
    row.tsx
  select/  (15 files)
    __tests__/  (5 files)
      … 5 files under this directory
    index.ts
    select-context.ts
    select-dropdown.tsx
    select-icon-clear.tsx
    select-icon.tsx
    select-input.tsx
    select-multiple-value.tsx
    select-option.tsx
    select.tsx
    styles.ts
  shared/  (14 files)
    __tests__/  (8 files)
      … 8 files under this directory
    backdrop.tsx
    css-transition.tsx
    dropdown.tsx
    ellipsis.tsx
    expand.tsx
    highlight.tsx
  slider/  (7 files)
    __tests__/  (2 files)
      … 2 files under this directory
    index.ts
    slider-dot.tsx
    slider-mark.tsx
    slider.tsx
    styles.ts
  snippet/  (6 files)
    __tests__/  (2 files)
      … 2 files under this directory
    index.ts
    snippet-icon.tsx
    snippet.tsx
    styles.ts
  spacer/  (4 files)
    __tests__/  (2 files)
      … 2 files under this directory
    index.ts
    spacer.tsx
  spinner/  (4 files)
    __tests__/  (2 files)
      … 2 files under this directory
    index.ts
    spinner.tsx
  table/  (10 files)
    __tests__/  (2 files)
      … 2 files under this directory
    index.ts
    table-body.tsx
    table-cell.tsx
    table-column.tsx
    table-context.ts
    table-head.tsx
    table-types.ts
    table.tsx
  tabs/  (6 files)
    __tests__/  (2 files)
      … 2 files under this directory
    index.ts
    tabs-context.ts
    tabs-item.tsx
    tabs.tsx
  tag/  (4 files)
    __tests__/  (2 files)
      … 2 files under this directory
    index.ts
    tag.tsx
  text/  (5 files)
    __tests__/  (2 files)
      … 2 files under this directory
    child.tsx
    index.ts
    text.tsx
  textarea/  (4 files)
    __tests__/  (2 files)
      … 2 files under this directory
    index.ts
    textarea.tsx
  themes/  (6 files)
    presets/  (4 files)
      … 4 files under this directory
    index.ts
    themes.ts
  toggle/  (5 files)
    __tests__/  (2 files)
      … 2 files under this directory
    index.ts
    styles.ts
    toggle.tsx
  tooltip/  (8 files)
    __test__/  (1 files)
      … 1 files under this directory
    helper.ts
    index.ts
    placement.ts
    styles.ts
    tooltip-content.tsx
    tooltip-icon.tsx
    tooltip.tsx
  tree/  (12 files)
    __tests__/  (2 files)
      … 2 files under this directory
    index.ts
    tree-context.ts
    tree-file-icon.tsx
    tree-file.tsx
    tree-folder-icon.tsx
    tree-folder.tsx
    tree-help.ts
    tree-indents.tsx
    tree-status-icon.tsx
    tree.tsx
  use-all-themes/  (2 files)
    all-themes-context.ts
    index.ts
  use-body-scroll/  (3 files)
    __tests__/  (1 files)
      … 1 files under this directory
    index.ts
    use-body-scroll.ts
  use-classes/  (3 files)
    __tests__/  (1 files)
      … 1 files under this directory
    index.ts
    use-classes.ts
  use-click-away/  (3 files)
    __tests__/  (1 files)
      … 1 files under this directory
    index.ts
    use-click-away.ts
  use-clipboard/  (3 files)
    __tests__/  (1 files)
      … 1 files under this directory
    index.ts
    use-clipboard.ts
  use-current-state/  (3 files)
    __tests__/  (1 files)
      … 1 files under this directory
    index.ts
    use-current-state.ts
  use-input/  (3 files)
    __tests__/  (1 files)
      … 1 files under this directory
    index.ts
    use-input.tsx
  use-keyboard/  (5 files)
    __tests__/  (1 files)
      … 1 files under this directory
    codes.ts
    helper.ts
    index.ts
    use-keyboard.ts
  use-media-query/  (3 files)
    __tests__/  (1 files)
      … 1 files under this directory
    index.ts
    use-media-query.ts
  use-modal/  (3 files)
    __tests__/  (1 files)
      … 1 files under this directory
    index.ts
    use-modal.ts
  use-scale/  (5 files)
    __tests__/  (1 files)
      … 1 files under this directory
    index.ts
    scale-context.ts
    utils.ts
    with-scale.tsx
  use-tabs/  (3 files)
    __tests__/  (1 files)
      … 1 files under this directory
    index.ts
    use-tabs.ts
  use-theme/  (2 files)
    index.ts
    theme-context.ts
  use-toasts/  (7 files)
    __tests__/  (2 files)
      … 2 files under this directory
    helpers.tsx
    index.ts
    toast-container.tsx
    toast-item.tsx
    use-toast.tsx
  user/  (5 files)
    __tests__/  (2 files)
      … 2 files under this directory
    index.ts
    user-link.tsx
    user.tsx
  utils/  (24 files)
    __tests__/  (1 files)
      … 1 files under this directory
    use-context-state/  (2 files)
      … 2 files under this directory
    calculations.ts
    collections.ts
    color.ts
    layouts.ts
    prop-types.ts
    types.ts
    use-body-scroll.ts
    use-click-anywhere.ts
    use-click-away.ts
    use-clipboard.ts
    use-current-state.ts
    use-default-props.ts
    use-dom-observer.ts
    use-drag.ts
    use-geist-ui-context.ts
    use-portal.ts
    use-previous.ts
    use-real-shape.ts
    use-resize.ts
    use-ssr.ts
    use-warning.ts
  index.ts
examples/  (59 files)
  create-next-app/  (9 files)
    pages/  (3 files)
      … 3 files under this directory
    .eslintrc.json
    README.md
    next-env.d.ts
    next.config.js
    package.json
    tsconfig.json
  create-react-app/  (1 files)
    README.md
  custom-styles/  (6 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (3 files)
      … 3 files under this directory
    README.md
    package.json
  custom-themes/  (6 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (3 files)
      … 3 files under this directory
    README.md
    package.json
  extends-components/  (8 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (4 files)
      … 4 files under this directory
    README.md
    package.json
    tsconfig.json
  remix/  (11 files)
    api/  (1 files)
      … 1 files under this directory
    app/  (4 files)
      … 4 files under this directory
    README.md
    package.json
    remix.config.js
    remix.env.d.ts
    tsconfig.json
    vercel.json
  tree-shaking-create-react-app/  (5 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (2 files)
      … 2 files under this directory
    README.md
    package.json
  tree-shaking-nextjs/  (6 files)
    pages/  (3 files)
      … 3 files under this directory
    README.md
    next.config.js
    package.json
  tree-shaking-webpack/  (6 files)
    src/  (2 files)
      … 2 files under this directory
    .babelrc
    README.md
    package.json
    webpack.config.js
  with-typescript/  (1 files)
    README.md
lib/  (73 files)
  components/  (61 files)
    attributes/  (5 files)
      … 5 files under this directory
    customization/  (7 files)
      … 7 files under this directory
    layout/  (15 files)
      … 15 files under this directory
    mdx-widgets/  (17 files)
      … 17 files under this directory
    playground/  (6 files)
      … 6 files under this directory
    pures/  (4 files)
      … 4 files under this directory
    search/  (6 files)
      … 6 files under this directory
    index.ts
  data/  (6 files)
    index.ts
    metadata-en-us.json
    metadata-zh-cn.json
    seeds-en-us.json
    seeds-zh-cn.json
    seeds.ts
  config-context.ts
  config-provider.tsx
  constants.ts
  redirect.tsx
  use-dom-clean.ts
  use-locale.ts
pages/  (146 files)
  en-us/  (72 files)
    components/  (49 files)
      … 49 files under this directory
    guide/  (8 files)
      … 8 files under this directory
    hooks/  (14 files)
      … 14 files under this directory
    index.tsx
  zh-cn/  (72 files)
    components/  (49 files)
      … 49 files under this directory
    guide/  (8 files)
      … 8 files under this directory
    hooks/  (14 files)
      … 14 files under this directory
    index.tsx
  _app.tsx
  _document.tsx
public/  (1 files)
  _redirects
scripts/  (16 files)
  built-in/  (3 files)
    styled-jsx-server.es.js
    styled-jsx.cjs.js
    styled-jsx.es.js
  seeds/  (4 files)
    codesandbox.json
    links.json
    presets.js
    update.js
  babel.config.js
  collect-meta.js
  locales.js
  move-built-in.js
  rollup.config.js
  side-effects.js
  tsconfig.json
  tsconfig.test.json
  webpack.config.js
tests/  (4 files)
  __mocks__/  (1 files)
    styled-jsx/  (1 files)
      … 1 files under this directory
  .babelrc.js
  setup.ts
  utils.ts
typings/  (3 files)
  mdx.d.ts
  meta.d.ts
  styled.d.ts
.codecov.yml
.eslintignore
.eslintrc.js
.gitignore
.jest.config.js
.prettierignore
.travis.yml
.vercelignore
LICENSE
README.md
next-env.d.ts
next.config.js
now.json
package.json
tsconfig.json
```

## Entry points

- [components/auto-complete/index.ts](https://github.com/geist-org/geist-ui/blob/6894bfdf12bca17ae292617cf2b69c63731fd5d4/components/auto-complete/index.ts)
- [components/avatar/index.ts](https://github.com/geist-org/geist-ui/blob/6894bfdf12bca17ae292617cf2b69c63731fd5d4/components/avatar/index.ts)
- [components/badge/index.ts](https://github.com/geist-org/geist-ui/blob/6894bfdf12bca17ae292617cf2b69c63731fd5d4/components/badge/index.ts)
- [components/breadcrumbs/index.ts](https://github.com/geist-org/geist-ui/blob/6894bfdf12bca17ae292617cf2b69c63731fd5d4/components/breadcrumbs/index.ts)
- [components/button-dropdown/index.ts](https://github.com/geist-org/geist-ui/blob/6894bfdf12bca17ae292617cf2b69c63731fd5d4/components/button-dropdown/index.ts)
- [components/button-group/index.ts](https://github.com/geist-org/geist-ui/blob/6894bfdf12bca17ae292617cf2b69c63731fd5d4/components/button-group/index.ts)
- [components/button/index.ts](https://github.com/geist-org/geist-ui/blob/6894bfdf12bca17ae292617cf2b69c63731fd5d4/components/button/index.ts)
- [components/capacity/index.ts](https://github.com/geist-org/geist-ui/blob/6894bfdf12bca17ae292617cf2b69c63731fd5d4/components/capacity/index.ts)
- [components/card/index.ts](https://github.com/geist-org/geist-ui/blob/6894bfdf12bca17ae292617cf2b69c63731fd5d4/components/card/index.ts)
- [components/checkbox/index.ts](https://github.com/geist-org/geist-ui/blob/6894bfdf12bca17ae292617cf2b69c63731fd5d4/components/checkbox/index.ts)
- [components/code/index.ts](https://github.com/geist-org/geist-ui/blob/6894bfdf12bca17ae292617cf2b69c63731fd5d4/components/code/index.ts)
- [components/col/index.ts](https://github.com/geist-org/geist-ui/blob/6894bfdf12bca17ae292617cf2b69c63731fd5d4/components/col/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| components package | library | Observed | Groups 367 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 11 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 2 file(s) under data layer (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 66 file(s) under lib package (observed from repository paths and static analysis). |
| pages package | library | Observed | Groups 10 file(s) under pages package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 12 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 4 file(s) under tests (observed from repository paths and static analysis). |
| typings package | library | Observed | Groups 3 file(s) under typings package (observed from repository paths and static analysis). |

## Important files

- `.circleci/config.yml` (ci)
- `.codecov.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/publish.yml` (ci)
- `.travis.yml` (ci)
- `examples/create-next-app/.eslintrc.json` (config)
- `examples/create-next-app/package.json` (manifest)
- `examples/create-next-app/tsconfig.json` (config)
- `examples/custom-styles/package.json` (manifest)
- `examples/custom-themes/package.json` (manifest)
- `examples/extends-components/package.json` (manifest)
- `examples/extends-components/tsconfig.json` (config)
- `examples/remix/package.json` (manifest)
- `examples/remix/tsconfig.json` (config)
- `examples/remix/vercel.json` (config)
- `examples/tree-shaking-create-react-app/package.json` (manifest)
- `examples/tree-shaking-nextjs/package.json` (manifest)
- `examples/tree-shaking-webpack/package.json` (manifest)
- `lib/data/metadata-en-us.json` (config)
- `lib/data/metadata-zh-cn.json` (config)
- `lib/data/seeds-en-us.json` (config)
- `lib/data/seeds-zh-cn.json` (config)
- `now.json` (config)
- `package.json` (manifest)
- `scripts/seeds/codesandbox.json` (config)
- `scripts/seeds/links.json` (config)
- `scripts/tsconfig.json` (config)
- `scripts/tsconfig.test.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `components` — 426 analysed file(s)
- `pages` — 146 analysed file(s)
- `lib` — 73 analysed file(s)
- `examples` — 59 analysed file(s)
- `scripts` — 16 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `.github` — 8 analysed file(s)
- `tests` — 4 analysed file(s)
- `typings` — 3 analysed file(s)
- `.circleci` — 1 analysed file(s)
- `public` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 4 file(s) were skipped during inventory (4 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `6894bfdf12bca17ae292617cf2b69c63731fd5d4` is the revision these paths and observations refer to.
