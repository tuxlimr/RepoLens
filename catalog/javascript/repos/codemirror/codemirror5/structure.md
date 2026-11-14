# Project structure: codemirror/codemirror5

**Analysed commit:** `9b4f0603cb042286a7ac2262b98245493d0d7e4b`

**Commit reference:** [9b4f0603cb042286a7ac2262b98245493d0d7e4b](https://github.com/codemirror/codemirror5/commit/9b4f0603cb042286a7ac2262b98245493d0d7e4b)

**Tree at this commit:** [codemirror/codemirror5@9b4f0603cb04](https://github.com/codemirror/codemirror5/tree/9b4f0603cb042286a7ac2262b98245493d0d7e4b)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | codemirror/codemirror5 |
| Description | In-browser code editor (version 5, legacy) |
| Stars | 27192 |
| Forks | 4919 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `9b4f0603cb042286a7ac2262b98245493d0d7e4b` |
| Retrieved at | 2026-11-14T19:10:54.844949+00:00 |
| Files in this snapshot | 578 |

## Directory tree

```text
.github/  (1 files)
  FUNDING.yml
addon/  (66 files)
  comment/  (2 files)
    comment.js
    continuecomment.js
  dialog/  (2 files)
    dialog.css
    dialog.js
  display/  (6 files)
    autorefresh.js
    fullscreen.css
    fullscreen.js
    panel.js
    placeholder.js
    rulers.js
  edit/  (6 files)
    closebrackets.js
    closetag.js
    continuelist.js
    matchbrackets.js
    matchtags.js
    trailingspace.js
  fold/  (8 files)
    brace-fold.js
    comment-fold.js
    foldcode.js
    foldgutter.css
    foldgutter.js
    indent-fold.js
    markdown-fold.js
    xml-fold.js
  hint/  (8 files)
    anyword-hint.js
    css-hint.js
    html-hint.js
    javascript-hint.js
    show-hint.css
    show-hint.js
    sql-hint.js
    xml-hint.js
  lint/  (8 files)
    coffeescript-lint.js
    css-lint.js
    html-lint.js
    javascript-lint.js
    json-lint.js
    lint.css
    lint.js
    yaml-lint.js
  merge/  (2 files)
    merge.css
    merge.js
  mode/  (5 files)
    loadmode.js
    multiplex.js
    multiplex_test.js
    overlay.js
    simple.js
  runmode/  (2 files)
    colorize.js
    runmode.js
  scroll/  (4 files)
    annotatescrollbar.js
    scrollpastend.js
    simplescrollbars.css
    simplescrollbars.js
  search/  (6 files)
    jump-to-line.js
    match-highlighter.js
    matchesonscrollbar.css
    matchesonscrollbar.js
    search.js
    searchcursor.js
  selection/  (3 files)
    active-line.js
    mark-selection.js
    selection-pointer.js
  tern/  (3 files)
    tern.css
    tern.js
    worker.js
  wrap/  (1 files)
    hardwrap.js
bin/  (5 files)
  authors.sh
  lint
  release
  source-highlight
  upload-release.js
demo/  (45 files)
  activeline.html
  anywordhint.html
  bidi.html
  btree.html
  buffers.html
  changemode.html
  closebrackets.html
  closetag.html
  complete.html
  emacs.html
  folding.html
  fullscreen.html
  hardwrap.html
  html5complete.html
  indentwrap.html
  lint.html
  loadmode.html
  marker.html
  markselection.html
  matchhighlighter.html
  matchtags.html
  merge.html
  multiplex.html
  mustache.html
  … 21 more files
doc/  (9 files)
  activebookmark.js
  docs.css
  internals.html
  logo.svg
  releases.html
  reporting.html
  upgrade_v2.2.html
  upgrade_v3.html
  upgrade_v4.html
keymap/  (2 files)
  emacs.js
  sublime.js
lib/  (1 files)
  codemirror.css
mode/  (287 files)
  apl/  (2 files)
    apl.js
    index.html
  asciiarmor/  (2 files)
    asciiarmor.js
    index.html
  asn.1/  (2 files)
    asn.1.js
    index.html
  asterisk/  (2 files)
    asterisk.js
    index.html
  brainfuck/  (2 files)
    brainfuck.js
    index.html
  clike/  (4 files)
    clike.js
    index.html
    scala.html
    test.js
  clojure/  (3 files)
    clojure.js
    index.html
    test.js
  cmake/  (2 files)
    cmake.js
    index.html
  cobol/  (2 files)
    cobol.js
    index.html
  coffeescript/  (2 files)
    coffeescript.js
    index.html
  commonlisp/  (2 files)
    commonlisp.js
    index.html
  crystal/  (2 files)
    crystal.js
    index.html
  css/  (9 files)
    css.js
    gss.html
    gss_test.js
    index.html
    less.html
    less_test.js
    scss.html
    scss_test.js
    test.js
  cypher/  (3 files)
    cypher.js
    index.html
    test.js
  d/  (3 files)
    d.js
    index.html
    test.js
  dart/  (2 files)
    dart.js
    index.html
  diff/  (2 files)
    diff.js
    index.html
  django/  (2 files)
    django.js
    index.html
  dockerfile/  (3 files)
    dockerfile.js
    index.html
    test.js
  dtd/  (2 files)
    dtd.js
    index.html
  dylan/  (3 files)
    dylan.js
    index.html
    test.js
  ebnf/  (2 files)
    ebnf.js
    index.html
  ecl/  (2 files)
    ecl.js
    index.html
  eiffel/  (2 files)
    eiffel.js
    index.html
  elm/  (2 files)
    elm.js
    index.html
  erlang/  (2 files)
    erlang.js
    index.html
  factor/  (2 files)
    factor.js
    index.html
  fcl/  (2 files)
    fcl.js
    index.html
  forth/  (2 files)
    forth.js
    index.html
  fortran/  (2 files)
    fortran.js
    index.html
  gas/  (2 files)
    gas.js
    index.html
  gfm/  (3 files)
    gfm.js
    index.html
    test.js
  gherkin/  (2 files)
    gherkin.js
    index.html
  go/  (2 files)
    go.js
    index.html
  groovy/  (2 files)
    groovy.js
    index.html
  haml/  (3 files)
    haml.js
    index.html
    test.js
  handlebars/  (2 files)
    handlebars.js
    index.html
  haskell/  (2 files)
    haskell.js
    index.html
  haskell-literate/  (2 files)
    haskell-literate.js
    index.html
  haxe/  (2 files)
    haxe.js
    index.html
  htmlembedded/  (2 files)
    htmlembedded.js
    index.html
  htmlmixed/  (2 files)
    htmlmixed.js
    index.html
  http/  (2 files)
    http.js
    index.html
  idl/  (2 files)
    idl.js
    index.html
  javascript/  (5 files)
    index.html
    javascript.js
    json-ld.html
    test.js
    typescript.html
  jinja2/  (2 files)
    index.html
    jinja2.js
  jsx/  (3 files)
    index.html
    jsx.js
    test.js
  julia/  (2 files)
    index.html
    julia.js
  livescript/  (2 files)
    index.html
    livescript.js
  lua/  (2 files)
    index.html
    lua.js
  markdown/  (3 files)
    index.html
    markdown.js
    test.js
  mathematica/  (2 files)
    index.html
    mathematica.js
  mbox/  (2 files)
    index.html
    mbox.js
  mirc/  (2 files)
    index.html
    mirc.js
  mllike/  (2 files)
    index.html
    mllike.js
  modelica/  (2 files)
    index.html
    modelica.js
  mscgen/  (5 files)
    index.html
    mscgen.js
    mscgen_test.js
    msgenny_test.js
    xu_test.js
  mumps/  (2 files)
    index.html
    mumps.js
  nginx/  (2 files)
    index.html
    nginx.js
  nsis/  (2 files)
    index.html
    nsis.js
  ntriples/  (2 files)
    index.html
    ntriples.js
  octave/  (2 files)
    index.html
    octave.js
  oz/  (2 files)
    index.html
    oz.js
  pascal/  (2 files)
    index.html
    pascal.js
  pegjs/  (2 files)
    index.html
    pegjs.js
  perl/  (2 files)
    index.html
    perl.js
  php/  (3 files)
    index.html
    php.js
    test.js
  pig/  (2 files)
    index.html
    pig.js
  powershell/  (3 files)
    index.html
    powershell.js
    test.js
  properties/  (2 files)
    index.html
    properties.js
  protobuf/  (2 files)
    index.html
    protobuf.js
  pug/  (2 files)
    index.html
    pug.js
  puppet/  (2 files)
    index.html
    puppet.js
  python/  (3 files)
    index.html
    python.js
    test.js
  q/  (2 files)
    index.html
    q.js
  r/  (2 files)
    index.html
    r.js
  rpm/  (3 files)
    changes/  (1 files)
      … 1 files under this directory
    index.html
    rpm.js
  rst/  (2 files)
    index.html
    rst.js
  ruby/  (3 files)
    index.html
    ruby.js
    test.js
  rust/  (3 files)
    index.html
    rust.js
    test.js
  sas/  (2 files)
    index.html
    sas.js
  sass/  (3 files)
    index.html
    sass.js
    test.js
  scheme/  (2 files)
    index.html
    scheme.js
  shell/  (3 files)
    index.html
    shell.js
    test.js
  sieve/  (2 files)
    index.html
    sieve.js
  slim/  (3 files)
    index.html
    slim.js
    test.js
  smalltalk/  (2 files)
    index.html
    smalltalk.js
  smarty/  (2 files)
    index.html
    smarty.js
  solr/  (2 files)
    index.html
    solr.js
  soy/  (3 files)
    index.html
    soy.js
    test.js
  sparql/  (2 files)
    index.html
    sparql.js
  spreadsheet/  (2 files)
    index.html
    spreadsheet.js
  sql/  (2 files)
    index.html
    sql.js
  stex/  (3 files)
    index.html
    stex.js
    test.js
  stylus/  (2 files)
    index.html
    stylus.js
  swift/  (3 files)
    index.html
    swift.js
    test.js
  tcl/  (2 files)
    index.html
    tcl.js
  textile/  (3 files)
    index.html
    test.js
    textile.js
  tiddlywiki/  (3 files)
    index.html
    tiddlywiki.css
    tiddlywiki.js
  tiki/  (3 files)
    index.html
    tiki.css
    tiki.js
  toml/  (2 files)
    index.html
    toml.js
  tornado/  (2 files)
    index.html
    tornado.js
  troff/  (2 files)
    index.html
    troff.js
  ttcn/  (2 files)
    index.html
    ttcn.js
  ttcn-cfg/  (2 files)
    index.html
    ttcn-cfg.js
  turtle/  (2 files)
    index.html
    turtle.js
  twig/  (2 files)
    index.html
    twig.js
  vb/  (2 files)
    index.html
    vb.js
  vbscript/  (2 files)
    index.html
    vbscript.js
  velocity/  (2 files)
    index.html
    velocity.js
  verilog/  (3 files)
    index.html
    test.js
    verilog.js
  vhdl/  (2 files)
    index.html
    vhdl.js
  vue/  (2 files)
    index.html
    vue.js
  wast/  (3 files)
    index.html
    test.js
    wast.js
  webidl/  (2 files)
    index.html
    webidl.js
  xml/  (3 files)
    index.html
    test.js
    xml.js
  xquery/  (3 files)
    index.html
    test.js
    xquery.js
  yacas/  (2 files)
    index.html
    yacas.js
  yaml/  (2 files)
    index.html
    yaml.js
  yaml-frontmatter/  (2 files)
    index.html
    yaml-frontmatter.js
  z80/  (2 files)
    index.html
    z80.js
  index.html
  meta.js
src/  (67 files)
  addon/  (4 files)
    runmode/  (4 files)
      … 4 files under this directory
  display/  (15 files)
    Display.js
    focus.js
    gutters.js
    highlight_worker.js
    line_numbers.js
    mode_state.js
    operations.js
    scroll_events.js
    scrollbars.js
    scrolling.js
    selection.js
    update_display.js
    update_line.js
    update_lines.js
    view_tracking.js
  edit/  (13 files)
    CodeMirror.js
    commands.js
    deleteNearSelection.js
    drop_events.js
    fromTextArea.js
    global_events.js
    key_events.js
    legacy.js
    main.js
    methods.js
    mouse_events.js
    options.js
    utils.js
  input/  (7 files)
    ContentEditableInput.js
    TextareaInput.js
    indent.js
    input.js
    keymap.js
    keynames.js
    movement.js
  line/  (6 files)
    highlight.js
    line_data.js
    pos.js
    saw_special_spans.js
    spans.js
    utils_line.js
  measurement/  (2 files)
    position_measurement.js
    widgets.js
  model/  (10 files)
    Doc.js
    change_measurement.js
    changes.js
    chunk.js
    document_data.js
    history.js
    line_widget.js
    mark_text.js
    selection.js
    selection_updates.js
  util/  (8 files)
    StringStream.js
    bidi.js
    browser.js
    dom.js
    event.js
    feature_detection.js
    misc.js
    operation_group.js
  codemirror.js
  modes.js
test/  (18 files)
  annotatescrollbar.js
  comment_test.js
  contenteditable_test.js
  doc_test.js
  driver.js
  emacs_test.js
  html-hint-test.js
  index.html
  lint.js
  mode_test.css
  mode_test.js
  multi_test.js
  run.js
  scroll_test.js
  search_test.js
  sql-hint-test.js
  sublime_test.js
  test.js
theme/  (65 files)
  3024-day.css
  3024-night.css
  abbott.css
  abcdef.css
  ambiance-mobile.css
  ambiance.css
  ayu-dark.css
  ayu-mirage.css
  base16-dark.css
  base16-light.css
  bespin.css
  blackboard.css
  cobalt.css
  colorforth.css
  darcula.css
  dracula.css
  duotone-dark.css
  duotone-light.css
  eclipse.css
  elegant.css
  erlang-dark.css
  gruvbox-dark.css
  hopscotch.css
  icecoder.css
  … 41 more files
.editorconfig
.gitattributes
.gitignore
.npmignore
AUTHORS
CHANGELOG.md
CONTRIBUTING.md
LICENSE
README.md
index.html
package.json
rollup.config.js
```

## Entry points

- [src/edit/main.js](https://github.com/codemirror/codemirror5/blob/9b4f0603cb042286a7ac2262b98245493d0d7e4b/src/edit/main.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| addon package | library | Observed | Groups 61 file(s) under addon package (observed from repository paths and static analysis). |
| bin package | library | Observed | Groups 2 file(s) under bin package (observed from repository paths and static analysis). |
| codemirror.js package | library | Observed | Groups 1 file(s) under codemirror.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| display package | library | Observed | Groups 15 file(s) under display package (observed from repository paths and static analysis). |
| edit package | library | Observed | Groups 13 file(s) under edit package (observed from repository paths and static analysis). |
| input package | library | Observed | Groups 7 file(s) under input package (observed from repository paths and static analysis). |
| keymap package | library | Observed | Groups 2 file(s) under keymap package (observed from repository paths and static analysis). |
| line package | library | Observed | Groups 6 file(s) under line package (observed from repository paths and static analysis). |
| measurement package | library | Observed | Groups 2 file(s) under measurement package (observed from repository paths and static analysis). |
| mode package | library | Observed | Groups 155 file(s) under mode package (observed from repository paths and static analysis). |
| model package | library | Observed | Groups 10 file(s) under model package (observed from repository paths and static analysis). |
| modes.js package | library | Observed | Groups 1 file(s) under modes.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 18 file(s) under tests (observed from repository paths and static analysis). |
| util package | library | Observed | Groups 8 file(s) under util package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `mode/dockerfile/dockerfile.js` (container)
- `package.json` (manifest)

## Top-level layout

- `mode` — 287 analysed file(s)
- `src` — 67 analysed file(s)
- `addon` — 66 analysed file(s)
- `theme` — 65 analysed file(s)
- `demo` — 45 analysed file(s)
- `test` — 18 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `doc` — 9 analysed file(s)
- `bin` — 5 analysed file(s)
- `keymap` — 2 analysed file(s)
- `.github` — 1 analysed file(s)
- `lib` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `9b4f0603cb042286a7ac2262b98245493d0d7e4b` is the revision these paths and observations refer to.
