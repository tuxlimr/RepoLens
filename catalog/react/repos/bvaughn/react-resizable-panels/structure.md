# Project structure: bvaughn/react-resizable-panels

**Analysed commit:** `6b22da07c2fa712327059f5c0848e7c90d0fc3c3`

**Commit reference:** [6b22da07c2fa712327059f5c0848e7c90d0fc3c3](https://github.com/bvaughn/react-resizable-panels/commit/6b22da07c2fa712327059f5c0848e7c90d0fc3c3)

**Tree at this commit:** [bvaughn/react-resizable-panels@6b22da07c2fa](https://github.com/bvaughn/react-resizable-panels/tree/6b22da07c2fa712327059f5c0848e7c90d0fc3c3)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | bvaughn/react-resizable-panels |
| Description | Not provided |
| Stars | 5481 |
| Forks | 238 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `6b22da07c2fa712327059f5c0848e7c90d0fc3c3` |
| Retrieved at | 2026-11-14T19:14:18.797524+00:00 |
| Files in this snapshot | 799 |

## Directory tree

```text
.github/  (6 files)
  workflows/  (6 files)
    eslint.yml
    pending-changes.yml
    playwright.yml
    prettier.yml
    typescript.yml
    vitest.yml
integrations/  (93 files)
  next/  (14 files)
    app/  (6 files)
      … 6 files under this directory
    .gitignore
    README.md
    eslint.config.mjs
    next-env.d.ts
    next.config.ts
    package.json
    postcss.config.mjs
    tsconfig.json
  tests/  (53 files)
    src/  (37 files)
      … 37 files under this directory
    tests/  (14 files)
      … 14 files under this directory
    package.json
    playwright.config.ts
  vike/  (15 files)
    pages/  (11 files)
      … 11 files under this directory
    README.md
    package.json
    tsconfig.json
    vite.config.ts
  vite/  (11 files)
    src/  (5 files)
      … 5 files under this directory
    README.md
    eslint.config.js
    index.html
    package.json
    tsconfig.json
    vite.config.ts
lib/  (408 files)
  flex/  (40 files)
    components/  (12 files)
      … 12 files under this directory
    contexts/  (3 files)
      … 3 files under this directory
    hooks/  (14 files)
      … 14 files under this directory
    utils/  (10 files)
      … 10 files under this directory
    types.ts
  global/  (109 files)
    cursor/  (7 files)
      … 7 files under this directory
    dom/  (7 files)
      … 7 files under this directory
    event-handlers/  (14 files)
      … 14 files under this directory
    mutable-state/  (4 files)
      … 4 files under this directory
    styles/  (8 files)
      … 8 files under this directory
    test/  (4 files)
      … 4 files under this directory
    utils/  (63 files)
      … 63 files under this directory
    mountAxis.ts
    types.ts
  grid/  (32 files)
    components/  (4 files)
      … 4 files under this directory
    contexts/  (2 files)
      … 2 files under this directory
    hooks/  (7 files)
      … 7 files under this directory
    utils/  (17 files)
      … 17 files under this directory
    constants.ts
    types.ts
  shared/  (32 files)
    components/  (1 files)
      … 1 files under this directory
    hooks/  (10 files)
      … 10 files under this directory
    utils/  (21 files)
      … 21 files under this directory
  workspace/  (192 files)
    components/  (20 files)
      … 20 files under this directory
    contexts/  (7 files)
      … 7 files under this directory
    hooks/  (17 files)
      … 17 files under this directory
    models/  (62 files)
      … 62 files under this directory
    mutable-state/  (2 files)
      … 2 files under this directory
    utils/  (82 files)
      … 82 files under this directory
    constants.ts
    types.ts
  constants.ts
  index.ts
  types.ts
public/  (154 files)
  generated/  (150 files)
    docs/  (16 files)
      … 16 files under this directory
    examples/  (115 files)
      … 115 files under this directory
    types/  (18 files)
      … 18 files under this directory
    site-map.json
  svgs/  (1 files)
    grab-dots.svg
  favicon.svg
  og.svg
  robots.txt
scripts/  (5 files)
  compile-docs.ts
  compile-examples.ts
  compile-search-index.ts
  compile-types.ts
  compress-og-image.ts
src/  (119 files)
  components/  (37 files)
    accordion/  (1 files)
      … 1 files under this directory
    dashboard/  (1 files)
      … 1 files under this directory
    demos/  (3 files)
      … 3 files under this directory
    email/  (3 files)
      … 3 files under this directory
    request-log/  (1 files)
      … 1 files under this directory
    styled-panels/  (8 files)
      … 8 files under this directory
    vs-code/  (7 files)
      … 7 files under this directory
    vs-code-workspace/  (1 files)
      … 1 files under this directory
    workspace/  (6 files)
      … 6 files under this directory
    DemoButton.tsx
    Divider.tsx
    HookReturnType.tsx
    Link.tsx
    MaximizeButton.tsx
    TypeFields.tsx
  embeds/  (1 files)
    DragBetweenAppsEmbed.tsx
  hooks/  (1 files)
    useLocalStorage.ts
  routes/  (78 files)
    AccordionRoute.tsx
    CellPropsRoute.tsx
    CollapsibleGridCellsRoute.tsx
    CollapsiblePanelsRoute.tsx
    ConditionalPanelsRoute.tsx
    CustomStylesRoute.tsx
    DisabledPanelsRoute.tsx
    FixedSizePanelsRoute.tsx
    GridBasicsRoute.tsx
    GridConstraintsRoute.tsx
    GridImperativeHandleRoute.tsx
    GridPersistentLayoutRoute.tsx
    GridPropsRoute.tsx
    GridTrackImperativeHandleRoute.tsx
    GridlinePropsRoute.tsx
    GridlinesRoute.tsx
    GroupImperativeHandleRoute.tsx
    GroupPropsRoute.tsx
    GroupResizeBehaviorRoute.tsx
    LayoutBasicsRoute.tsx
    NestedGroupsRoute.tsx
    OverflowRoute.tsx
    PanelImperativeHandleRoute.tsx
    PanelPropsRoute.tsx
    … 54 more files
  App.tsx
  routes.ts
.gitignore
.prettierignore
CHANGELOG.md
CONTRIBUTING.md
LICENSE.md
README.md
eslint.config.js
index.css
index.html
index.tsx
package.json
pnpm-workspace.yaml
postcss.config.js
prettier.config.js
```

## Entry points

- [integrations/tests/src/index.ts](https://github.com/bvaughn/react-resizable-panels/blob/6b22da07c2fa712327059f5c0848e7c90d0fc3c3/integrations/tests/src/index.ts)
- [index.tsx](https://github.com/bvaughn/react-resizable-panels/blob/6b22da07c2fa712327059f5c0848e7c90d0fc3c3/index.tsx)
- [integrations/next/app/page.tsx](https://github.com/bvaughn/react-resizable-panels/blob/6b22da07c2fa712327059f5c0848e7c90d0fc3c3/integrations/next/app/page.tsx)
- [integrations/vite/src/main.tsx](https://github.com/bvaughn/react-resizable-panels/blob/6b22da07c2fa712327059f5c0848e7c90d0fc3c3/integrations/vite/src/main.tsx)
- [lib/index.ts](https://github.com/bvaughn/react-resizable-panels/blob/6b22da07c2fa712327059f5c0848e7c90d0fc3c3/lib/index.ts)
- [src/App.tsx](https://github.com/bvaughn/react-resizable-panels/blob/6b22da07c2fa712327059f5c0848e7c90d0fc3c3/src/App.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 80 file(s) under api layer (observed from repository paths and static analysis). |
| App.tsx package | library | Observed | Groups 1 file(s) under app.tsx package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 37 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 158 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 62 file(s) under data layer (observed from repository paths and static analysis). |
| embeds package | library | Observed | Groups 1 file(s) under embeds package (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 23 file(s) under external integrations (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 1 file(s) under hooks package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 338 file(s) under lib package (observed from repository paths and static analysis). |
| routes.ts package | library | Observed | Groups 1 file(s) under routes.ts package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 5 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 61 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/eslint.yml` (ci)
- `.github/workflows/pending-changes.yml` (ci)
- `.github/workflows/playwright.yml` (ci)
- `.github/workflows/prettier.yml` (ci)
- `.github/workflows/typescript.yml` (ci)
- `.github/workflows/vitest.yml` (ci)
- `integrations/next/package.json` (manifest)
- `integrations/next/tsconfig.json` (config)
- `integrations/vike/package.json` (manifest)
- `integrations/vike/tsconfig.json` (config)
- `integrations/vite/package.json` (manifest)
- `integrations/vite/tsconfig.json` (config)
- `package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `public/generated/docs/Cell.json` (config)
- `public/generated/docs/Grid.json` (config)
- `public/generated/docs/GridImperativeHandle.json` (config)
- `public/generated/docs/GridTrackImperativeHandle.json` (config)
- `public/generated/docs/Gridline.json` (config)
- `public/generated/docs/Group.json` (config)
- `public/generated/docs/GroupImperativeHandle.json` (config)
- `public/generated/docs/Panel.json` (config)
- `public/generated/docs/PanelImperativeHandle.json` (config)
- `public/generated/docs/Separator.json` (config)
- `public/generated/docs/TabCloseButton.json` (config)
- `public/generated/docs/TabsetCollapseButton.json` (config)
- `public/generated/docs/TabsetDragHandle.json` (config)
- `public/generated/docs/TabsetMaximizeButton.json` (config)
- `public/generated/docs/Workspace.json` (config)
- `public/generated/docs/WorkspaceImperativeHandle.json` (config)
- `public/generated/examples/Accordion.json` (config)
- `public/generated/examples/ClientComponent.json` (config)
- `public/generated/examples/CollapseThreshold.json` (config)
- `public/generated/examples/CollapsibleGridDashboard.json` (config)
- `public/generated/examples/CollapsiblePanels.json` (config)
- `public/generated/examples/CollapsiblePanelsCollapsedByDefault.json` (config)
- `public/generated/examples/CollapsiblePanelsCollapsedSize.json` (config)
- `public/generated/examples/ConditionalSeparators.json` (config)
- `public/generated/examples/ConditionallyRenderPanel.json` (config)
- `public/generated/examples/DisabledPanel.json` (config)
- `public/generated/examples/DisabledPanelAndSeparator.json` (config)
- `public/generated/examples/DisabledPanels.json` (config)
- `public/generated/examples/DisabledSeparator.json` (config)
- `public/generated/examples/FixedSizePanels.json` (config)
- `public/generated/examples/FixedSizePanelsMiddle.json` (config)
- `public/generated/examples/FixedSizePanelsMiddleNoSeparators.json` (config)
- `public/generated/examples/GridConstraints.json` (config)
- `public/generated/examples/GridLayout.json` (config)
- `public/generated/examples/GridPersistentLayout.json` (config)
- `public/generated/examples/GridSpans.json` (config)
- `public/generated/examples/Gridlines.json` (config)
- `public/generated/examples/GridlinesAdvanced.json` (config)
- `public/generated/examples/GroupAndPanelElements.json` (config)
- `public/generated/examples/GroupExplicitHeight.json` (config)
- `public/generated/examples/GroupOverflowClassName.json` (config)
- `public/generated/examples/GroupOverflowStyle.json` (config)
- `public/generated/examples/GroupResizeBehavior.json` (config)
- `public/generated/examples/LayoutBasicsHorizontal.json` (config)
- `public/generated/examples/LayoutBasicsSeparator.json` (config)
- `public/generated/examples/LayoutBasicsVertical.json` (config)
- `public/generated/examples/NestedGroups.json` (config)
- `public/generated/examples/PanelDropShadow.json` (config)
- `public/generated/examples/PanelFocusOutline.json` (config)
- `public/generated/examples/PanelTooltip.json` (config)
- `public/generated/examples/PersistConditionalPanelLayouts.json` (config)
- `public/generated/examples/PersistentLayouts.json` (config)
- `public/generated/examples/ResizePreviewMode.json` (config)
- `public/generated/examples/ResizePreviewWithImplicitSeparator.json` (config)
- `public/generated/examples/ResizePreviewWithSeparatorOverlay.json` (config)
- `public/generated/examples/SeparatorCustomStyles.json` (config)
- `public/generated/examples/SeparatorCustomStylesFocusVisible.json` (config)
- `public/generated/examples/SeparatorDataAttributes.json` (config)
- `public/generated/examples/SeparatorFocusOutline.json` (config)
- `public/generated/examples/ServerComponent.json` (config)
- `public/generated/examples/SizeConstraintsMinMax.json` (config)
- `public/generated/examples/SizeConstraintsPercentage.json` (config)
- `public/generated/examples/UseDefaultGridLayout.json` (config)
- `public/generated/examples/UseDefaultLayout.json` (config)
- `public/generated/examples/UseParentGrid.json` (config)
- `public/generated/examples/UseParentGroup.json` (config)
- `public/generated/examples/UseParentPanel.json` (config)
- `public/generated/examples/UseParentTab.json` (config)
- `public/generated/examples/UseParentTabState.json` (config)
- `public/generated/examples/UseParentTabset.json` (config)
- `public/generated/examples/UseParentTabsetState.json` (config)
- `public/generated/examples/UseParentWorkspace.json` (config)
- `public/generated/examples/UsePopoutWindowsOnOpen.json` (config)
- `public/generated/examples/UsePopoutWindowsRestore.json` (config)
- `public/generated/examples/VSCodeEditorFile.json` (config)
- `public/generated/examples/VSCodeWorkspaceEditorFile.json` (config)
- `public/generated/examples/WorkspaceAcceptExternalDrop.json` (config)
- `public/generated/examples/WorkspaceAcceptFileDrop.json` (config)
- `public/generated/examples/WorkspaceAddTabAtTarget.json` (config)
- `public/generated/examples/WorkspaceBasics.json` (config)
- `public/generated/examples/WorkspaceBeforeModelChange.json` (config)
- `public/generated/examples/WorkspaceClassNames.json` (config)
- `public/generated/examples/WorkspaceClassNamesFunctions.json` (config)
- `public/generated/examples/WorkspaceCollapseButton.json` (config)
- `public/generated/examples/WorkspaceCollapsibleModel.json` (config)
- `public/generated/examples/WorkspaceCopiesOfYourApp.json` (config)
- `public/generated/examples/WorkspaceCopyDragPreview.json` (config)
- `public/generated/examples/WorkspaceCopyTab.json` (config)
- `public/generated/examples/WorkspaceCustomTabConfirmClose.json` (config)
- `public/generated/examples/WorkspaceCustomTabset.json` (config)
- `public/generated/examples/WorkspaceDragGroup.json` (config)
- `public/generated/examples/WorkspaceDragSourceInfo.json` (config)
- `public/generated/examples/WorkspaceExternalDrag.json` (config)
- `public/generated/examples/WorkspaceFloatButton.json` (config)
- `public/generated/examples/WorkspaceFloatingModel.json` (config)
- `public/generated/examples/WorkspaceHiddenTabBehavior.json` (config)
- `public/generated/examples/WorkspaceHiddenTabsMenu.json` (config)
- `public/generated/examples/WorkspaceKeepWhenEmpty.json` (config)
- `public/generated/examples/WorkspaceMaxSizeModel.json` (config)
- `public/generated/examples/WorkspaceMaximizeTabset.json` (config)
- `public/generated/examples/WorkspaceModel.json` (config)
- `public/generated/examples/WorkspaceNormalizeModel.json` (config)
- `public/generated/examples/WorkspaceOpenTab.json` (config)
- `public/generated/examples/WorkspaceOverflowToolbar.json` (config)
- `public/generated/examples/WorkspacePersistence.json` (config)
- `public/generated/examples/WorkspacePopoutWindows.json` (config)
- `public/generated/examples/WorkspaceRenamableTab.json` (config)
- `public/generated/examples/WorkspaceResizeSplit.json` (config)
- `public/generated/examples/WorkspaceRestrictions.json` (config)
- `public/generated/examples/WorkspaceRestrictionsModel.json` (config)
- `public/generated/examples/WorkspaceSelectTab.json` (config)
- `public/generated/examples/WorkspaceSeparators.json` (config)
- `public/generated/examples/WorkspaceServerRendering.json` (config)
- `public/generated/examples/WorkspaceServerRenderingSavedModel.json` (config)
- `public/generated/examples/WorkspaceStyles.json` (config)
- `public/generated/examples/WorkspaceTabHooks.json` (config)
- `public/generated/examples/WorkspaceTabPlacement.json` (config)
- `public/generated/examples/WorkspaceTabPlacementMixed.json` (config)
- `public/generated/examples/WorkspaceTabRemovalSelection.json` (config)
- `public/generated/examples/WorkspaceTabsetDragHandle.json` (config)
- `public/generated/examples/WorkspaceTabsetEventHandlers.json` (config)
- `public/generated/examples/WorkspaceUpdateTab.json` (config)
- `public/generated/examples/cookieStorage.json` (config)
- `public/generated/examples/useGridCallbackRef.json` (config)
- `public/generated/examples/useGridRef.json` (config)
- `public/generated/examples/useGroupCallbackRef.json` (config)
- `public/generated/examples/useGroupRef.json` (config)
- `public/generated/examples/usePanelCallbackRef.json` (config)
- `public/generated/examples/usePanelRef.json` (config)
- `public/generated/examples/useWorkspaceCallbackRef.json` (config)
- `public/generated/examples/useWorkspaceRef.json` (config)
- `public/generated/site-map.json` (config)
- `public/generated/types/ParentGrid.json` (config)
- `public/generated/types/ParentGroup.json` (config)
- `public/generated/types/ParentPanel.json` (config)
- `public/generated/types/ParentTab.json` (config)
- `public/generated/types/ParentTabState.json` (config)
- `public/generated/types/ParentTabset.json` (config)
- `public/generated/types/ParentTabsetState.json` (config)
- `public/generated/types/ParentWorkspace.json` (config)
- `public/generated/types/PopoutWindow.json` (config)
- `public/generated/types/PopoutWindowRect.json` (config)
- `public/generated/types/PopoutWindowState.json` (config)
- `public/generated/types/PopoutWindows.json` (config)
- `public/generated/types/PopoutWorkspaceProps.json` (config)
- `public/generated/types/SplitNode.json` (config)
- `public/generated/types/TabNode.json` (config)
- `public/generated/types/TabsetNode.json` (config)
- `public/generated/types/UsePopoutWindowsOptions.json` (config)
- `public/generated/types/WorkspaceModel.json` (config)

## Top-level layout

- `lib` — 408 analysed file(s)
- `public` — 154 analysed file(s)
- `src` — 119 analysed file(s)
- `integrations` — 93 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `.github` — 6 analysed file(s)
- `scripts` — 5 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `6b22da07c2fa712327059f5c0848e7c90d0fc3c3` is the revision these paths and observations refer to.
