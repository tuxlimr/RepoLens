# Project structure: prazzon/Flexbox-Labs

**Analysed commit:** `39416e136100825caf10e1963579e6bd3c19f873`

**Commit reference:** [39416e136100825caf10e1963579e6bd3c19f873](https://github.com/prazzon/Flexbox-Labs/commit/39416e136100825caf10e1963579e6bd3c19f873)

**Tree at this commit:** [prazzon/Flexbox-Labs@39416e136100](https://github.com/prazzon/Flexbox-Labs/tree/39416e136100825caf10e1963579e6bd3c19f873)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | prazzon/Flexbox-Labs |
| Description | A web app for creating flexible layouts with the power of CSS Flexbox. |
| Stars | 4061 |
| Forks | 366 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `39416e136100825caf10e1963579e6bd3c19f873` |
| Retrieved at | 2026-11-14T19:14:55.585152+00:00 |
| Files in this snapshot | 171 |

## Directory tree

```text
.github/  (3 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  FUNDING.yml
app/  (135 files)
  (playground)/  (2 files)
    flexbox/  (1 files)
      … 1 files under this directory
    grid/  (1 files)
      … 1 files under this directory
  _components/  (91 files)
    Header/  (2 files)
      … 2 files under this directory
    Pages/  (15 files)
      … 15 files under this directory
    Playground/  (8 files)
      … 8 files under this directory
    SideBar/  (26 files)
      … 26 files under this directory
    UI/  (38 files)
      … 38 files under this directory
    CustomToaster.tsx
    SettingsInit.tsx
  _context/  (1 files)
    SettingsContext.tsx
  _data/  (7 files)
    flexbox/  (3 files)
      … 3 files under this directory
    grid/  (3 files)
      … 3 files under this directory
    dataTypes.ts
  _helpers/  (1 files)
    helpers.ts
  _hooks/  (10 files)
    useFlexbox.ts
    useGrid.ts
    useInsideContainerClick.ts
    useKeyPress.ts
    useOutsideClick.ts
    usePersistedState.ts
    useRaisedShadow.ts
    useResize.ts
    useRipple.ts
    useSettings.ts
  _lib/  (10 files)
    features/  (4 files)
      … 4 files under this directory
    hooks/  (1 files)
      … 1 files under this directory
    types/  (2 files)
      … 2 files under this directory
    history.ts
    hooks.ts
    store.ts
  _utils/  (5 files)
    cssTailwindConverter.ts
    formatters.ts
    generateFullHtml.ts
    generateGridArea.ts
    generateGridElements.ts
  error.module.scss
  error.tsx
  global.scss
  layout.tsx
  loading.tsx
  page.tsx
  storeProvider.tsx
  types.ts
public/  (24 files)
  img/  (23 files)
    12columnSystem.svg
    alignCenter.svg
    alternatingGrid.svg
    collage.svg
    fillRemainingSpace.svg
    fillRemainingSpace2.svg
    fillSpace.svg
    grid3x3.svg
    grid4x4.svg
    horizontalBars.svg
    html5-2.svg
    html5.svg
    infiniteColumns.svg
    infiniteRows.svg
    logo.svg
    masonryColumn.svg
    masonryRow.svg
    pancakeStack.svg
    rowWrap.svg
    sidebar.svg
    stretchMiddle.svg
    verticalBars.svg
    verticalStack.svg
  loader.css
.gitignore
.nvmrc
LICENSE
README.md
bun.lock
eslint.config.js
next.config.ts
package.json
tsconfig.json
```

## Entry points

- [app/(playground)/flexbox/page.tsx](https://github.com/prazzon/Flexbox-Labs/blob/39416e136100825caf10e1963579e6bd3c19f873/app/%28playground%29/flexbox/page.tsx)
- [app/(playground)/grid/page.tsx](https://github.com/prazzon/Flexbox-Labs/blob/39416e136100825caf10e1963579e6bd3c19f873/app/%28playground%29/grid/page.tsx)
- [app/page.tsx](https://github.com/prazzon/Flexbox-Labs/blob/39416e136100825caf10e1963579e6bd3c19f873/app/page.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| app package | library | Observed | Groups 95 file(s) under app package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `app` — 135 analysed file(s)
- `public` — 24 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `.github` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `39416e136100825caf10e1963579e6bd3c19f873` is the revision these paths and observations refer to.
