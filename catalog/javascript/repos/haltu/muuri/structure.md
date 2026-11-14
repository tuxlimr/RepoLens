# Project structure: haltu/muuri

**Analysed commit:** `219e00893327dc22cf241103bef0ca63ee6fde2e`

**Commit reference:** [219e00893327dc22cf241103bef0ca63ee6fde2e](https://github.com/haltu/muuri/commit/219e00893327dc22cf241103bef0ca63ee6fde2e)

**Tree at this commit:** [haltu/muuri@219e00893327](https://github.com/haltu/muuri/tree/219e00893327dc22cf241103bef0ca63ee6fde2e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | haltu/muuri |
| Description | Infinite responsive, sortable, filterable and draggable layouts |
| Stars | 10935 |
| Forks | 645 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `219e00893327dc22cf241103bef0ca63ee6fde2e` |
| Retrieved at | 2026-11-14T19:12:28.193514+00:00 |
| Files in this snapshot | 174 |

## Directory tree

```text
.github/  (1 files)
  FUNDING.yml
docs/  (12 files)
  .vitepress/  (3 files)
    theme/  (2 files)
      … 2 files under this directory
    config.js
  public/  (1 files)
    muuri-icon.svg
  examples.md
  getting-started.md
  grid-constructor.md
  grid-events.md
  grid-methods.md
  grid-options.md
  index.md
  item-methods.md
src/  (66 files)
  Animator/  (1 files)
    Animator.js
  AutoScroller/  (7 files)
    AutoScroller.js
    LICENSE.md
    Pool.js
    ScrollAction.js
    ScrollRequest.js
    constants.js
    utils.js
  Dragger/  (3 files)
    Dragger.js
    EdgeHack.js
    LICENSE.md
  Emitter/  (2 files)
    Emitter.js
    LICENSE.md
  Grid/  (1 files)
    Grid.js
  Item/  (7 files)
    Item.js
    ItemDrag.js
    ItemDragPlaceholder.js
    ItemDragRelease.js
    ItemLayout.js
    ItemMigrate.js
    ItemVisibility.js
  Packer/  (3 files)
    LICENSE.md
    Packer.js
    PackerProcessor.js
  Ticker/  (2 files)
    LICENSE.md
    Ticker.js
  utils/  (36 files)
    addClass.js
    arrayInsert.js
    arrayMove.js
    arraySwap.js
    createUid.js
    debounce.js
    elementMatches.js
    getContainingBlock.js
    getCurrentStyles.js
    getIntersectionArea.js
    getIntersectionScore.js
    getOffsetDiff.js
    getPrefixedPropName.js
    getScrollableAncestors.js
    getStyle.js
    getStyleAsFloat.js
    getStyleName.js
    getTranslate.js
    getTranslateString.js
    getUnprefixedPropName.js
    hasPassiveEvents.js
    isFunction.js
    isNative.js
    isNodeList.js
    … 12 more files
  constants.js
  index.d.ts
  index.js
  ticker.js
tests/  (81 files)
  grid-constructor/  (2 files)
    container.js
    instance.js
  grid-events/  (26 files)
    add.js
    beforeReceive.js
    beforeSend.js
    destroy.js
    dragEnd.js
    dragInit.js
    dragMove.js
    dragReleaseEnd.js
    dragReleaseStart.js
    dragScroll.js
    dragStart.js
    draggerEvent.js
    filter.js
    hideEnd.js
    hideStart.js
    layoutAbort.js
    layoutEnd.js
    layoutStart.js
    move.js
    receive.js
    remove.js
    send.js
    showEnd.js
    showStart.js
    … 2 more files
  grid-methods/  (17 files)
    add.js
    destroy.js
    filter.js
    getElement.js
    getItems.js
    hide.js
    layout.js
    move.js
    off.js
    on.js
    refreshItems.js
    refreshSortData.js
    remove.js
    send.js
    show.js
    sort.js
    synchronize.js
  grid-options/  (20 files)
    containerClass.js
    dragAutoScroll.js
    dragAxis.js
    dragContainer.js
    dragEnabled.js
    dragPlaceholder.js
    dragSort.js
    dragSortPredicate.js
    dragStartPredicate.js
    hideDuration.js
    itemClass.js
    itemDraggingClass.js
    itemHiddenClass.js
    itemPositioningClass.js
    itemReleasingClass.js
    itemVisibleClass.js
    items.js
    layout.js
    showDuration.js
    visibleStyles-hiddenStyles.js
  item-methods/  (14 files)
    getElement.js
    getGrid.js
    getHeight.js
    getMargin.js
    getPosition.js
    getWidth.js
    isActive.js
    isDestroyed.js
    isDragging.js
    isHiding.js
    isPositioning.js
    isReleasing.js
    isShowing.js
    isVisible.js
  index.js
  utils.js
.eslintrc.js
.gitignore
.prettierrc.json
.travis.yml
AUTHORS.txt
CONTRIBUTING.md
LICENSE.md
README.md
gulpfile.js
karma.conf.js
karma.defaults.js
package.json
rollup.banner.js
rollup.config.js
```

## Entry points

- [src/index.js](https://github.com/haltu/muuri/blob/219e00893327dc22cf241103bef0ca63ee6fde2e/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Animator package | library | Observed | Groups 1 file(s) under animator package (observed from repository paths and static analysis). |
| AutoScroller package | library | Observed | Groups 6 file(s) under autoscroller package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| constants.js package | library | Observed | Groups 1 file(s) under constants.js package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 5 file(s) under core modules (observed from repository paths and static analysis). |
| Dragger package | library | Observed | Groups 2 file(s) under dragger package (observed from repository paths and static analysis). |
| Emitter package | library | Observed | Groups 1 file(s) under emitter package (observed from repository paths and static analysis). |
| Grid package | library | Observed | Groups 1 file(s) under grid package (observed from repository paths and static analysis). |
| index.d.ts package | library | Observed | Groups 1 file(s) under index.d.ts package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| Item package | library | Observed | Groups 7 file(s) under item package (observed from repository paths and static analysis). |
| Packer package | library | Observed | Groups 2 file(s) under packer package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 81 file(s) under tests (observed from repository paths and static analysis). |
| Ticker package | library | Observed | Groups 1 file(s) under ticker package (observed from repository paths and static analysis). |
| ticker.js package | library | Observed | Groups 1 file(s) under ticker.js package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 36 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.prettierrc.json` (config)
- `.travis.yml` (ci)
- `package.json` (manifest)

## Top-level layout

- `tests` — 81 analysed file(s)
- `src` — 66 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `docs` — 12 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `219e00893327dc22cf241103bef0ca63ee6fde2e` is the revision these paths and observations refer to.
