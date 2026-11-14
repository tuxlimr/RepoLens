# Project structure: jquery/jquery-ui

**Analysed commit:** `dcf10556bbcfdf3e10e3ea30966482e201191411`

**Commit reference:** [dcf10556bbcfdf3e10e3ea30966482e201191411](https://github.com/jquery/jquery-ui/commit/dcf10556bbcfdf3e10e3ea30966482e201191411)

**Tree at this commit:** [jquery/jquery-ui@dcf10556bbcf](https://github.com/jquery/jquery-ui/tree/dcf10556bbcfdf3e10e3ea30966482e201191411)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | jquery/jquery-ui |
| Description | The official jQuery user interface library. |
| Stars | 11336 |
| Forks | 5178 |
| Licence | Other |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `dcf10556bbcfdf3e10e3ea30966482e201191411` |
| Retrieved at | 2026-11-14T19:12:19.324073+00:00 |
| Files in this snapshot | 616 |

## Directory tree

```text
.github/  (5 files)
  workflows/  (4 files)
    browser-tests.yml
    codeql-analysis.yml
    filestash.yml
    node.js.yml
  dependabot.yml
demos/  (168 files)
  accordion/  (7 files)
    collapsible.html
    custom-icons.html
    default.html
    fillspace.html
    index.html
    no-auto-height.html
    sortable.html
  autocomplete/  (14 files)
    categories.html
    combobox.html
    custom-data.html
    default.html
    folding.html
    index.html
    london.xml
    maxheight.html
    multiple-remote.html
    multiple.html
    remote-jsonp.html
    remote-with-cache.html
    remote.html
    xml.html
  button/  (3 files)
    default.html
    icons.html
    index.html
  checkboxradio/  (5 files)
    default.html
    index.html
    no-icons.html
    product-selector.html
    radiogroup.html
  controlgroup/  (4 files)
    default.html
    index.html
    splitbutton.html
    toolbar.html
  datepicker/  (15 files)
    alt-field.html
    animation.html
    buttonbar.html
    date-formats.html
    date-range.html
    default.html
    dropdown-month-year.html
    icon-trigger.html
    index.html
    inline.html
    localization.html
    min-max.html
    multiple-calendars.html
    other-months.html
    show-week.html
  dialog/  (6 files)
    animated.html
    default.html
    index.html
    modal-confirmation.html
    modal-form.html
    modal-message.html
  draggable/  (11 files)
    constrain-movement.html
    cursor-style.html
    default.html
    events.html
    handle.html
    index.html
    revert.html
    scroll.html
    snap-to.html
    sortable.html
    visual-feedback.html
  droppable/  (7 files)
    accepted-elements.html
    default.html
    index.html
    photo-manager.html
    propagation.html
    revert.html
    visual-feedback.html
  effect/  (11 files)
    addClass.html
    animate.html
    default.html
    easing.html
    hide.html
    index.html
    removeClass.html
    show.html
    switchClass.html
    toggle.html
    toggleClass.html
  menu/  (4 files)
    categories.html
    default.html
    icons.html
    index.html
  position/  (3 files)
    cycler.html
    default.html
    index.html
  progressbar/  (5 files)
    default.html
    download.html
    indeterminate.html
    index.html
    label.html
  resizable/  (11 files)
    animate.html
    aspect-ratio.html
    constrain-area.html
    default.html
    helper.html
    index.html
    max-min.html
    snap-to-grid.html
    synchronous-resize.html
    textarea.html
    visual-feedback.html
  selectable/  (4 files)
    default.html
    display-grid.html
    index.html
    serialize.html
  selectmenu/  (4 files)
    custom_render.html
    default.html
    index.html
    product-selection.html
  slider/  (12 files)
    colorpicker.html
    custom-handle.html
    default.html
    hotelrooms.html
    index.html
    multiple-vertical.html
    range-vertical.html
    range.html
    rangemax.html
    rangemin.html
    slider-vertical.html
    steps.html
  sortable/  (8 files)
    connect-lists.html
    default.html
    display-grid.html
    empty-lists.html
    index.html
    items.html
    placeholder.html
    portlets.html
  spinner/  (7 files)
    currency.html
    decimal.html
    default.html
    index.html
    latlong.html
    overflow.html
    time.html
  tabs/  (11 files)
    ajax/  (3 files)
      … 3 files under this directory
    ajax.html
    collapsible.html
    default.html
    index.html
    manipulation.html
    mouseover.html
    sortable.html
    vertical.html
  tooltip/  (10 files)
    ajax/  (2 files)
      … 2 files under this directory
    custom-animation.html
    custom-content.html
    custom-style.html
    default.html
    forms.html
    index.html
    tracking.html
    video-player.html
  widget/  (2 files)
    default.html
    index.html
  bootstrap.js
  demos.css
  index.html
  search.js
external/  (42 files)
  globalize/  (4 files)
    LICENSE
    globalize.culture.de-DE.js
    globalize.culture.ja-JP.js
    globalize.js
  jquery/  (2 files)
    LICENSE.txt
    MIT-LICENSE.txt
  jquery-1.12.4/  (1 files)
    LICENSE.txt
  jquery-2.2.4/  (1 files)
    LICENSE.txt
  jquery-3.0.0/  (1 files)
    LICENSE.txt
  jquery-3.1.0/  (1 files)
    LICENSE.txt
  jquery-3.1.1/  (1 files)
    LICENSE.txt
  jquery-3.2.0/  (1 files)
    LICENSE.txt
  jquery-3.2.1/  (1 files)
    LICENSE.txt
  jquery-3.3.0/  (1 files)
    LICENSE.txt
  jquery-3.3.1/  (1 files)
    LICENSE.txt
  jquery-3.4.0/  (1 files)
    LICENSE.txt
  jquery-3.4.1/  (1 files)
    LICENSE.txt
  jquery-3.5.0/  (1 files)
    LICENSE.txt
  jquery-3.5.1/  (1 files)
    LICENSE.txt
  jquery-3.6.0/  (1 files)
    LICENSE.txt
  jquery-3.6.1/  (1 files)
    LICENSE.txt
  jquery-3.6.2/  (1 files)
    LICENSE.txt
  jquery-3.6.3/  (1 files)
    LICENSE.txt
  jquery-3.6.4/  (1 files)
    LICENSE.txt
  jquery-3.7.0/  (1 files)
    LICENSE.txt
  jquery-3.7.1/  (1 files)
    LICENSE.txt
  jquery-4.0.0/  (1 files)
    LICENSE.txt
  jquery-custom/  (1 files)
    MIT-LICENSE.txt
  jquery-migrate-1.x/  (2 files)
    LICENSE.txt
    jquery-migrate.js
  jquery-migrate-3.x/  (2 files)
    LICENSE.txt
    jquery-migrate.js
  jquery-migrate-4.x/  (2 files)
    LICENSE.txt
    jquery-migrate.js
  jquery-mousewheel/  (2 files)
    LICENSE.txt
    jquery.mousewheel.js
  jquery-simulate/  (2 files)
    LICENSE.txt
    jquery.simulate.js
  qunit/  (3 files)
    LICENSE.txt
    MIT-LICENSE.txt
    qunit.css
  requirejs/  (1 files)
    require.js
tests/  (235 files)
  lib/  (9 files)
    grunt-contrib-qunit-bridges/  (2 files)
      … 2 files under this directory
    bootstrap.js
    common.js
    css.js
    helper.js
    qunit-assert-domequal.js
    qunit.js
    testIframe.js
  unit/  (189 files)
    accordion/  (8 files)
      … 8 files under this directory
    autocomplete/  (10 files)
      … 10 files under this directory
    button/  (10 files)
      … 10 files under this directory
    checkboxradio/  (7 files)
      … 7 files under this directory
    controlgroup/  (6 files)
      … 6 files under this directory
    core/  (4 files)
      … 4 files under this directory
    datepicker/  (8 files)
      … 8 files under this directory
    dialog/  (11 files)
      … 11 files under this directory
    draggable/  (8 files)
      … 8 files under this directory
    droppable/  (11 files)
      … 11 files under this directory
    effects/  (4 files)
      … 4 files under this directory
    form-reset-mixin/  (3 files)
      … 3 files under this directory
    jquery-patch/  (3 files)
      … 3 files under this directory
    menu/  (8 files)
      … 8 files under this directory
    position/  (3 files)
      … 3 files under this directory
    progressbar/  (7 files)
      … 7 files under this directory
    resizable/  (8 files)
      … 8 files under this directory
    selectable/  (7 files)
      … 7 files under this directory
    selectmenu/  (7 files)
      … 7 files under this directory
    slider/  (7 files)
      … 7 files under this directory
    sortable/  (8 files)
      … 8 files under this directory
    spinner/  (12 files)
      … 12 files under this directory
    tabs/  (9 files)
      … 9 files under this directory
    tooltip/  (11 files)
      … 11 files under this directory
    widget/  (6 files)
      … 6 files under this directory
    all.html
    index.html
    subsuite.js
  visual/  (34 files)
    accordion/  (1 files)
      … 1 files under this directory
    addClass/  (1 files)
      … 1 files under this directory
    checkboxradio/  (1 files)
      … 1 files under this directory
    compound/  (10 files)
      … 10 files under this directory
    dialog/  (5 files)
      … 5 files under this directory
    draggable/  (1 files)
      … 1 files under this directory
    effects/  (6 files)
      … 6 files under this directory
    menu/  (1 files)
      … 1 files under this directory
    position/  (2 files)
      … 2 files under this directory
    selectmenu/  (1 files)
      … 1 files under this directory
    slider/  (1 files)
      … 1 files under this directory
    tooltip/  (2 files)
      … 2 files under this directory
    index.html
    visual.css
  index.css
  index.html
  index.js
themes/  (22 files)
  base/  (22 files)
    accordion.css
    all.css
    autocomplete.css
    base.css
    button.css
    checkboxradio.css
    controlgroup.css
    core.css
    datepicker.css
    dialog.css
    draggable.css
    menu.css
    progressbar.css
    resizable.css
    selectable.css
    selectmenu.css
    slider.css
    sortable.css
    spinner.css
    tabs.css
    theme.css
    tooltip.css
ui/  (126 files)
  effects/  (15 files)
    effect-blind.js
    effect-bounce.js
    effect-clip.js
    effect-drop.js
    effect-explode.js
    effect-fade.js
    effect-fold.js
    effect-highlight.js
    effect-puff.js
    effect-pulsate.js
    effect-scale.js
    effect-shake.js
    effect-size.js
    effect-slide.js
    effect-transfer.js
  i18n/  (75 files)
    datepicker-af.js
    datepicker-ar-DZ.js
    datepicker-ar.js
    datepicker-az.js
    datepicker-be.js
    datepicker-bg.js
    datepicker-bs.js
    datepicker-ca.js
    datepicker-cs.js
    datepicker-cy-GB.js
    datepicker-da.js
    datepicker-de-AT.js
    datepicker-de.js
    datepicker-el.js
    datepicker-en-AU.js
    datepicker-en-GB.js
    datepicker-en-NZ.js
    datepicker-eo.js
    datepicker-es.js
    datepicker-et.js
    datepicker-eu.js
    datepicker-fa.js
    datepicker-fi.js
    datepicker-fo.js
    … 51 more files
  widgets/  (20 files)
    accordion.js
    autocomplete.js
    button.js
    checkboxradio.js
    controlgroup.js
    datepicker.js
    dialog.js
    draggable.js
    droppable.js
    menu.js
    mouse.js
    progressbar.js
    resizable.js
    selectable.js
    selectmenu.js
    slider.js
    sortable.js
    spinner.js
    tabs.js
    tooltip.js
  data.js
  disable-selection.js
  effect.js
  focusable.js
  form-reset-mixin.js
  jquery-patch.js
  jquery-var-for-color.js
  keycode.js
  labels.js
  plugin.js
  position.js
  scroll-parent.js
  tabbable.js
  unique-id.js
  version.js
  widget.js
.csslintrc
.editorconfig
.gitattributes
.gitignore
.mailmap
.npmignore
AUTHORS.txt
CONTRIBUTING.md
Gruntfile.js
LICENSE.txt
README.md
SECURITY.md
bower.json
eslint.config.mjs
jtr-git.yml
jtr-stable.yml
jtr.yml
package.json
```

## Entry points

- [ui/widget.js](https://github.com/jquery/jquery-ui/blob/dcf10556bbcfdf3e10e3ea30966482e201191411/ui/widget.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| demos package | library | Observed | Groups 2 file(s) under demos package (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 9 file(s) under external integrations (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 235 file(s) under tests (observed from repository paths and static analysis). |
| ui package | library | Observed | Groups 126 file(s) under ui package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/browser-tests.yml` (ci)
- `.github/workflows/codeql-analysis.yml` (ci)
- `.github/workflows/filestash.yml` (ci)
- `.github/workflows/node.js.yml` (ci)
- `bower.json` (config)
- `jtr-git.yml` (config)
- `jtr-stable.yml` (config)
- `jtr.yml` (config)
- `package.json` (manifest)

## Top-level layout

- `tests` — 235 analysed file(s)
- `demos` — 168 analysed file(s)
- `ui` — 126 analysed file(s)
- `external` — 42 analysed file(s)
- `themes` — 22 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `.github` — 5 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 15 file(s) were skipped during inventory (1 x likely secret file excluded; 1 x lockfile excluded; 13 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `dcf10556bbcfdf3e10e3ea30966482e201191411` is the revision these paths and observations refer to.
