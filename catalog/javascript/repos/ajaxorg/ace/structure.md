# Project structure: ajaxorg/ace

**Analysed commit:** `2e1b35190636654b14b089383e031ff3f065369b`

**Commit reference:** [2e1b35190636654b14b089383e031ff3f065369b](https://github.com/ajaxorg/ace/commit/2e1b35190636654b14b089383e031ff3f065369b)

**Tree at this commit:** [ajaxorg/ace@2e1b35190636](https://github.com/ajaxorg/ace/tree/2e1b35190636654b14b089383e031ff3f065369b)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | ajaxorg/ace |
| Description | Ace (Ajax.org Cloud9 Editor) |
| Stars | 27134 |
| Forks | 5261 |
| Licence | Other |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `2e1b35190636654b14b089383e031ff3f065369b` |
| Retrieved at | 2026-11-14T19:10:53.654238+00:00 |
| Files in this snapshot | 799 |

## Directory tree

```text
.github/  (12 files)
  ISSUE_TEMPLATE/  (5 files)
    add-to-website.yml
    bug-report.yml
    config.yml
    documentation.yml
    feature-request.yml
  workflows/  (6 files)
    backwards-compatibility-commenter.yml
    close-stale-issues.yml
    issue-reprioritization.yml
    link-comment.yml
    nodejs.yml
    publish.yml
  PULL_REQUEST_TEMPLATE.md
build_support/  (2 files)
  editor.html
  mini_require.js
demo/  (247 files)
  diff/  (4 files)
    examples/  (3 files)
      … 3 files under this directory
    index.html
  kitchen-sink/  (208 files)
    docs/  (198 files)
      … 198 files under this directory
    demo.js
    dev_util.js
    doclist.js
    file_drop.js
    inline_editor.js
    layout.js
    require.js
    styles.css
    token_tooltip.js
    util.js
  r.js/  (2 files)
    build.js
    editor.html
  static-highlighter/  (2 files)
    client.html
    server.js
  test_ace_builds/  (3 files)
    index.ts
    package.json
    tsconfig.json
  test_package/  (3 files)
    index.ts
    package.json
    tsconfig.json
  webpack/  (5 files)
    demo.js
    demo.ts
    index.html
    package.json
    webpack.config.js
  autocompletion.html
  autoresize.html
  code_lens.html
  csp.html
  emmet.html
  i18n.html
  inline_autocompletion.html
  keyboard_shortcuts.html
  modelist.html
  requirejs+build.html
  scrollable-page.html
  settings_menu.html
  shadow-dom.html
  show_own_source.js
  static-highlighter.html
  statusbar.html
  svg.svg
  toolbar.html
  transform.html
  xml.xml
doc/  (27 files)
  site/  (6 files)
    css/  (1 files)
      … 1 files under this directory
    images/  (1 files)
      … 1 files under this directory
    js/  (2 files)
      … 2 files under this directory
    iphone.css
    style.css
  template/  (16 files)
    jade/  (3 files)
      … 3 files under this directory
    resources/  (13 files)
      … 13 files under this directory
  README.md
  additionalObjs.json
  build.js
  index.md
  package.json
experiments/  (11 files)
  animate_folding.html
  basic_animation.html
  bidi.html
  capture.html
  cut_copy.html
  debug_mem_leak.html
  dom.html
  transform.html
  triple_click.html
  worker.html
  worker.js
lib/  (19 files)
  ace/  (19 files)
    mode/  (8 files)
      … 8 files under this directory
    snippets/  (4 files)
      … 4 files under this directory
    worker/  (6 files)
      … 6 files under this directory
    loader_build.js
src/  (460 files)
  autocomplete/  (7 files)
    inline.js
    inline_screenreader.js
    inline_test.js
    popup.js
    popup_test.js
    text_completer.js
    util.js
  commands/  (6 files)
    command_manager.js
    command_manager_test.js
    default_commands.js
    incremental_search_commands.js
    multi_select_commands.js
    occur_commands.js
  css/  (1 files)
    editor-css.js
  edit_session/  (4 files)
    bracket_match.js
    fold.js
    fold_line.js
    folding.js
  ext/  (52 files)
    diff/  (8 files)
      … 8 files under this directory
    menu_tools/  (3 files)
      … 3 files under this directory
    beautify.js
    beautify_test.js
    code_lens.js
    code_lens_test.js
    command_bar.js
    command_bar_test.js
    diff.js
    diff_test.js
    elastic_tabstops_lite.js
    emmet.js
    emmet_test.js
    error_marker.js
    error_marker_test.js
    hardwrap.js
    hardwrap_test.js
    inline_autocomplete.js
    inline_autocomplete_test.js
    keybinding_menu.js
    language_tools.js
    linking.js
    modelist.js
    options.js
    prompt.js
    rtl.js
    … 17 more files
  keyboard/  (14 files)
    emacs.js
    emacs_test.js
    gutter_handler.js
    gutter_handler_test.js
    hash_handler.js
    keybinding.js
    keybinding_test.js
    sublime.js
    sublime_test.js
    textarea.js
    textinput.js
    textinput_test.js
    vim_ace_test.js
    vscode.js
  layer/  (12 files)
    cursor.js
    decorators.js
    font_metrics.js
    gutter.js
    gutter_test.js
    lines.js
    marker.js
    text.js
    text_markers.js
    text_markers_test.js
    text_test.js
    text_util.js
  lib/  (17 files)
    app_config.js
    bidiutil.js
    deep_copy.js
    default_english_messages.js
    dom.js
    es6-shim.js
    event.js
    event_emitter.js
    event_emitter_test.js
    fixoldbrowsers.js
    keys.js
    lang.js
    net.js
    oop.js
    report_error.js
    scroll.js
    useragent.js
  mode/  (318 files)
    _test/  (209 files)
      … 209 files under this directory
    behaviour/  (8 files)
      … 8 files under this directory
    abap.js
    abap_highlight_rules.js
    abc.js
    abc_highlight_rules.js
    actionscript.js
    actionscript_highlight_rules.js
    ada.js
    ada_highlight_rules.js
    ada_test.js
    alda.js
    alda_highlight_rules.js
    apache_conf.js
    apache_conf_highlight_rules.js
    apex.js
    apex_highlight_rules.js
    applescript.js
    applescript_highlight_rules.js
    aql.js
    aql_highlight_rules.js
    asciidoc.js
    asciidoc_highlight_rules.js
    asl.js
    asl_highlight_rules.js
    assembly_arm32.js
    … 77 more files
  ace.js
  ace_test.js
  anchor.js
  anchor_test.js
  apply_delta.js
  autocomplete.js
  autocomplete_test.js
  background_tokenizer.js
  background_tokenizer_test.js
  bidihandler.js
  clipboard.js
  config.js
  config_test.js
  document.js
  document_test.js
  edit_session.js
  edit_session_test.js
  editor.js
  editor_change_document_test.js
  editor_commands_test.js
  editor_highlight_selected_word_test.js
  editor_navigation_test.js
  editor_options_test.js
  editor_text_edit_test.js
  … 5 more files
.eslintignore
.eslintrc
.gitignore
.gitmodules
.nojekyll
CHANGELOG.md
CNAME
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
Makefile
Makefile.dryice.js
Readme.md
_config.yml
ace-internal.d.ts
ace-modes.d.ts
ace.d.ts
amplify.yml
index.html
kitchen-sink.html
package.json
```

## Entry points

- [src/ace.js](https://github.com/ajaxorg/ace/blob/2e1b35190636654b14b089383e031ff3f065369b/src/ace.js)
- [demo/static-highlighter/server.js](https://github.com/ajaxorg/ace/blob/2e1b35190636654b14b089383e031ff3f065369b/demo/static-highlighter/server.js)
- [demo/test_ace_builds/index.ts](https://github.com/ajaxorg/ace/blob/2e1b35190636654b14b089383e031ff3f065369b/demo/test_ace_builds/index.ts)
- [demo/test_package/index.ts](https://github.com/ajaxorg/ace/blob/2e1b35190636654b14b089383e031ff3f065369b/demo/test_package/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| ace.js package | library | Observed | Groups 1 file(s) under ace.js package (observed from repository paths and static analysis). |
| ace_test.js package | library | Observed | Groups 1 file(s) under ace_test.js package (observed from repository paths and static analysis). |
| anchor.js package | library | Observed | Groups 1 file(s) under anchor.js package (observed from repository paths and static analysis). |
| anchor_test.js package | library | Observed | Groups 1 file(s) under anchor_test.js package (observed from repository paths and static analysis). |
| apply_delta.js package | library | Observed | Groups 1 file(s) under apply_delta.js package (observed from repository paths and static analysis). |
| autocomplete package | library | Observed | Groups 7 file(s) under autocomplete package (observed from repository paths and static analysis). |
| autocomplete.js package | library | Observed | Groups 1 file(s) under autocomplete.js package (observed from repository paths and static analysis). |
| autocomplete_test.js package | library | Observed | Groups 1 file(s) under autocomplete_test.js package (observed from repository paths and static analysis). |
| background_tokenizer.js package | library | Observed | Groups 1 file(s) under background_tokenizer.js package (observed from repository paths and static analysis). |
| background_tokenizer_test.js package | library | Observed | Groups 1 file(s) under background_tokenizer_test.js package (observed from repository paths and static analysis). |
| bidihandler.js package | library | Observed | Groups 1 file(s) under bidihandler.js package (observed from repository paths and static analysis). |
| build_support package | library | Observed | Groups 1 file(s) under build_support package (observed from repository paths and static analysis). |
| clipboard.js package | library | Observed | Groups 1 file(s) under clipboard.js package (observed from repository paths and static analysis). |
| commands package | library | Observed | Groups 6 file(s) under commands package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 202 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| config.js package | library | Observed | Groups 1 file(s) under config.js package (observed from repository paths and static analysis). |
| config_test.js package | library | Observed | Groups 1 file(s) under config_test.js package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| css package | library | Observed | Groups 1 file(s) under css package (observed from repository paths and static analysis). |
| demo package | library | Observed | Groups 21 file(s) under demo package (observed from repository paths and static analysis). |
| document.js package | library | Observed | Groups 1 file(s) under document.js package (observed from repository paths and static analysis). |
| document_test.js package | library | Observed | Groups 1 file(s) under document_test.js package (observed from repository paths and static analysis). |
| edit_session package | library | Observed | Groups 4 file(s) under edit_session package (observed from repository paths and static analysis). |
| edit_session.js package | library | Observed | Groups 1 file(s) under edit_session.js package (observed from repository paths and static analysis). |
| edit_session_test.js package | library | Observed | Groups 1 file(s) under edit_session_test.js package (observed from repository paths and static analysis). |
| editor_change_document_test.js package | library | Observed | Groups 1 file(s) under editor_change_document_test.js package (observed from repository paths and static analysis). |
| editor_commands_test.js package | library | Observed | Groups 1 file(s) under editor_commands_test.js package (observed from repository paths and static analysis). |
| editor_highlight_selected_word_test.js package | library | Observed | Groups 1 file(s) under editor_highlight_selected_word_test.js package (observed from repository paths and static analysis). |
| editor.js package | library | Observed | Groups 1 file(s) under editor.js package (observed from repository paths and static analysis). |
| editor_navigation_test.js package | library | Observed | Groups 1 file(s) under editor_navigation_test.js package (observed from repository paths and static analysis). |
| editor_options_test.js package | library | Observed | Groups 1 file(s) under editor_options_test.js package (observed from repository paths and static analysis). |
| editor_text_edit_test.js package | library | Observed | Groups 1 file(s) under editor_text_edit_test.js package (observed from repository paths and static analysis). |
| experiments package | library | Observed | Groups 1 file(s) under experiments package (observed from repository paths and static analysis). |
| ext package | library | Observed | Groups 52 file(s) under ext package (observed from repository paths and static analysis). |
| incremental_search.js package | library | Observed | Groups 1 file(s) under incremental_search.js package (observed from repository paths and static analysis). |
| incremental_search_test.js package | library | Observed | Groups 1 file(s) under incremental_search_test.js package (observed from repository paths and static analysis). |
| keyboard package | library | Observed | Groups 14 file(s) under keyboard package (observed from repository paths and static analysis). |
| layer package | library | Observed | Groups 12 file(s) under layer package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 33 file(s) under lib package (observed from repository paths and static analysis). |
| line_widgets.js package | library | Observed | Groups 1 file(s) under line_widgets.js package (observed from repository paths and static analysis). |
| marker_group.js package | library | Observed | Groups 1 file(s) under marker_group.js package (observed from repository paths and static analysis). |
| marker_group_test.js package | library | Observed | Groups 1 file(s) under marker_group_test.js package (observed from repository paths and static analysis). |
| mode package | library | Observed | Groups 108 file(s) under mode package (observed from repository paths and static analysis). |

## Important files

- `.github/ISSUE_TEMPLATE/add-to-website.yml` (config)
- `.github/ISSUE_TEMPLATE/bug-report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/documentation.yml` (config)
- `.github/ISSUE_TEMPLATE/feature-request.yml` (config)
- `.github/workflows/backwards-compatibility-commenter.yml` (ci)
- `.github/workflows/close-stale-issues.yml` (ci)
- `.github/workflows/issue-reprioritization.yml` (ci)
- `.github/workflows/link-comment.yml` (ci)
- `.github/workflows/nodejs.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `_config.yml` (config)
- `amplify.yml` (config)
- `demo/kitchen-sink/docs/Dockerfile` (container)
- `demo/kitchen-sink/docs/ini.ini` (config)
- `demo/kitchen-sink/docs/json.json` (config)
- `demo/kitchen-sink/docs/toml.toml` (config)
- `demo/kitchen-sink/docs/yaml.yaml` (config)
- `demo/test_ace_builds/package.json` (manifest)
- `demo/test_ace_builds/tsconfig.json` (config)
- `demo/test_package/package.json` (manifest)
- `demo/test_package/tsconfig.json` (config)
- `demo/webpack/package.json` (manifest)
- `doc/additionalObjs.json` (config)
- `doc/package.json` (manifest)
- `lib/ace/mode/_test/tokens_jsoniq.json` (config)
- `lib/ace/mode/_test/tokens_xquery.json` (config)
- `package.json` (manifest)
- `src/mode/_test/tokens_abap.json` (config)
- `src/mode/_test/tokens_abc.json` (config)
- `src/mode/_test/tokens_actionscript.json` (config)
- `src/mode/_test/tokens_ada.json` (config)
- `src/mode/_test/tokens_alda.json` (config)
- `src/mode/_test/tokens_apex.json` (config)
- `src/mode/_test/tokens_aql.json` (config)
- `src/mode/_test/tokens_asciidoc.json` (config)
- `src/mode/_test/tokens_asl.json` (config)
- `src/mode/_test/tokens_assembly_x86.json` (config)
- `src/mode/_test/tokens_autohotkey.json` (config)
- `src/mode/_test/tokens_basic.json` (config)
- `src/mode/_test/tokens_batchfile.json` (config)
- `src/mode/_test/tokens_bibtex.json` (config)
- `src/mode/_test/tokens_c9search.json` (config)
- `src/mode/_test/tokens_c_cpp.json` (config)
- `src/mode/_test/tokens_cirru.json` (config)
- `src/mode/_test/tokens_clojure.json` (config)
- `src/mode/_test/tokens_cobol.json` (config)
- `src/mode/_test/tokens_coffee.json` (config)
- `src/mode/_test/tokens_coldfusion.json` (config)
- `src/mode/_test/tokens_crystal.json` (config)
- `src/mode/_test/tokens_csharp.json` (config)
- `src/mode/_test/tokens_csound_document.json` (config)
- `src/mode/_test/tokens_csound_orchestra.json` (config)
- `src/mode/_test/tokens_csound_score.json` (config)
- `src/mode/_test/tokens_csp.json` (config)
- `src/mode/_test/tokens_css.json` (config)
- `src/mode/_test/tokens_csv.json` (config)
- `src/mode/_test/tokens_curly.json` (config)
- `src/mode/_test/tokens_d.json` (config)
- `src/mode/_test/tokens_dart.json` (config)
- `src/mode/_test/tokens_diff.json` (config)
- `src/mode/_test/tokens_django.json` (config)
- `src/mode/_test/tokens_dot.json` (config)
- `src/mode/_test/tokens_drools.json` (config)
- `src/mode/_test/tokens_edifact.json` (config)
- `src/mode/_test/tokens_eiffel.json` (config)
- `src/mode/_test/tokens_ejs.json` (config)
- `src/mode/_test/tokens_elixir.json` (config)
- `src/mode/_test/tokens_elm.json` (config)
- `src/mode/_test/tokens_erlang.json` (config)
- `src/mode/_test/tokens_flix.json` (config)
- `src/mode/_test/tokens_forth.json` (config)
- `src/mode/_test/tokens_fortran.json` (config)
- `src/mode/_test/tokens_fsharp.json` (config)
- `src/mode/_test/tokens_fsl.json` (config)
- `src/mode/_test/tokens_ftl.json` (config)
- `src/mode/_test/tokens_gcode.json` (config)
- `src/mode/_test/tokens_gdresource.json` (config)
- `src/mode/_test/tokens_gdscript.json` (config)
- `src/mode/_test/tokens_gdshader.json` (config)
- `src/mode/_test/tokens_gherkin.json` (config)
- `src/mode/_test/tokens_gitignore.json` (config)
- `src/mode/_test/tokens_glsl.json` (config)
- `src/mode/_test/tokens_gobstones.json` (config)
- `src/mode/_test/tokens_golang.json` (config)
- `src/mode/_test/tokens_graphqlschema.json` (config)
- `src/mode/_test/tokens_groovy.json` (config)
- `src/mode/_test/tokens_groq.json` (config)
- `src/mode/_test/tokens_haml.json` (config)
- `src/mode/_test/tokens_handlebars.json` (config)
- `src/mode/_test/tokens_haskell.json` (config)
- `src/mode/_test/tokens_haskell_cabal.json` (config)
- `src/mode/_test/tokens_haxe.json` (config)
- `src/mode/_test/tokens_hjson.json` (config)
- `src/mode/_test/tokens_html.json` (config)
- `src/mode/_test/tokens_html_elixir.json` (config)
- `src/mode/_test/tokens_html_ruby.json` (config)
- `src/mode/_test/tokens_ini.json` (config)
- `src/mode/_test/tokens_io.json` (config)
- `src/mode/_test/tokens_ion.json` (config)
- `src/mode/_test/tokens_jack.json` (config)
- `src/mode/_test/tokens_jade.json` (config)
- `src/mode/_test/tokens_java.json` (config)
- `src/mode/_test/tokens_javascript.json` (config)
- `src/mode/_test/tokens_jexl.json` (config)
- `src/mode/_test/tokens_json.json` (config)
- `src/mode/_test/tokens_json5.json` (config)
- `src/mode/_test/tokens_jsp.json` (config)
- `src/mode/_test/tokens_jssm.json` (config)
- `src/mode/_test/tokens_jsx.json` (config)
- `src/mode/_test/tokens_julia.json` (config)
- `src/mode/_test/tokens_kotlin.json` (config)
- `src/mode/_test/tokens_latex.json` (config)
- `src/mode/_test/tokens_latte.json` (config)
- `src/mode/_test/tokens_less.json` (config)
- `src/mode/_test/tokens_liquid.json` (config)
- `src/mode/_test/tokens_lisp.json` (config)
- `src/mode/_test/tokens_livescript.json` (config)
- `src/mode/_test/tokens_logiql.json` (config)
- `src/mode/_test/tokens_logtalk.json` (config)
- `src/mode/_test/tokens_lsl.json` (config)
- `src/mode/_test/tokens_lua.json` (config)
- `src/mode/_test/tokens_luapage.json` (config)
- `src/mode/_test/tokens_lucene.json` (config)
- `src/mode/_test/tokens_markdown.json` (config)
- `src/mode/_test/tokens_mask.json` (config)
- `src/mode/_test/tokens_matlab.json` (config)
- `src/mode/_test/tokens_maze.json` (config)
- `src/mode/_test/tokens_mediawiki.json` (config)
- `src/mode/_test/tokens_mel.json` (config)
- `src/mode/_test/tokens_mips.json` (config)
- `src/mode/_test/tokens_mixal.json` (config)
- `src/mode/_test/tokens_mushcode.json` (config)
- `src/mode/_test/tokens_mysql.json` (config)
- `src/mode/_test/tokens_nasal.json` (config)
- `src/mode/_test/tokens_nginx.json` (config)
- `src/mode/_test/tokens_nim.json` (config)
- `src/mode/_test/tokens_nix.json` (config)
- `src/mode/_test/tokens_nsis.json` (config)
- `src/mode/_test/tokens_nunjucks.json` (config)
- `src/mode/_test/tokens_objectivec.json` (config)
- `src/mode/_test/tokens_ocaml.json` (config)
- `src/mode/_test/tokens_odin.json` (config)
- `src/mode/_test/tokens_partiql.json` (config)
- `src/mode/_test/tokens_pascal.json` (config)
- `src/mode/_test/tokens_perl.json` (config)
- `src/mode/_test/tokens_pgsql.json` (config)
- `src/mode/_test/tokens_php.json` (config)
- `src/mode/_test/tokens_php_laravel_blade.json` (config)
- `src/mode/_test/tokens_pig.json` (config)
- `src/mode/_test/tokens_plsql.json` (config)
- `src/mode/_test/tokens_powershell.json` (config)
- `src/mode/_test/tokens_praat.json` (config)
- `src/mode/_test/tokens_prisma.json` (config)
- `src/mode/_test/tokens_prolog.json` (config)
- `src/mode/_test/tokens_properties.json` (config)
- `src/mode/_test/tokens_protobuf.json` (config)
- `src/mode/_test/tokens_puppet.json` (config)
- `src/mode/_test/tokens_python.json` (config)
- `src/mode/_test/tokens_qml.json` (config)
- `src/mode/_test/tokens_r.json` (config)
- `src/mode/_test/tokens_raku.json` (config)
- `src/mode/_test/tokens_razor.json` (config)
- `src/mode/_test/tokens_rdoc.json` (config)
- `src/mode/_test/tokens_red.json` (config)
- `src/mode/_test/tokens_rhtml.json` (config)
- `src/mode/_test/tokens_robot.json` (config)
- `src/mode/_test/tokens_rst.json` (config)
- `src/mode/_test/tokens_ruby.json` (config)
- `src/mode/_test/tokens_rust.json` (config)
- `src/mode/_test/tokens_sac.json` (config)
- `src/mode/_test/tokens_sass.json` (config)
- `src/mode/_test/tokens_scad.json` (config)
- `src/mode/_test/tokens_scala.json` (config)
- `src/mode/_test/tokens_scheme.json` (config)
- `src/mode/_test/tokens_scrypt.json` (config)
- `src/mode/_test/tokens_scss.json` (config)
- `src/mode/_test/tokens_sh.json` (config)
- `src/mode/_test/tokens_sjs.json` (config)
- `src/mode/_test/tokens_slim.json` (config)
- `src/mode/_test/tokens_smarty.json` (config)
- `src/mode/_test/tokens_smithy.json` (config)
- `src/mode/_test/tokens_snippets.json` (config)
- `src/mode/_test/tokens_soy_template.json` (config)
- `src/mode/_test/tokens_space.json` (config)
- `src/mode/_test/tokens_sparql.json` (config)
- `src/mode/_test/tokens_sql.json` (config)
- `src/mode/_test/tokens_sqlserver.json` (config)
- `src/mode/_test/tokens_stylus.json` (config)
- `src/mode/_test/tokens_svg.json` (config)
- `src/mode/_test/tokens_swift.json` (config)
- `src/mode/_test/tokens_tcl.json` (config)
- `src/mode/_test/tokens_terraform.json` (config)
- `src/mode/_test/tokens_tex.json` (config)
- `src/mode/_test/tokens_text.json` (config)
- `src/mode/_test/tokens_textile.json` (config)
- `src/mode/_test/tokens_toml.json` (config)
- `src/mode/_test/tokens_tsv.json` (config)
- `src/mode/_test/tokens_tsx.json` (config)
- `src/mode/_test/tokens_turtle.json` (config)
- `src/mode/_test/tokens_twig.json` (config)
- `src/mode/_test/tokens_typescript.json` (config)
- `src/mode/_test/tokens_vala.json` (config)
- `src/mode/_test/tokens_vbscript.json` (config)
- `src/mode/_test/tokens_velocity.json` (config)
- `src/mode/_test/tokens_verilog.json` (config)
- `src/mode/_test/tokens_vhdl.json` (config)
- `src/mode/_test/tokens_visualforce.json` (config)
- `src/mode/_test/tokens_vue.json` (config)
- `src/mode/_test/tokens_wollok.json` (config)
- `src/mode/_test/tokens_xml.json` (config)
- `src/mode/_test/tokens_yaml.json` (config)
- `src/mode/_test/tokens_zeek.json` (config)
- `src/mode/dockerfile.js` (container)
- `src/mode/dockerfile_highlight_rules.js` (container)

## Top-level layout

- `src` — 460 analysed file(s)
- `demo` — 247 analysed file(s)
- `doc` — 27 analysed file(s)
- `(root files)` — 21 analysed file(s)
- `lib` — 19 analysed file(s)
- `.github` — 12 analysed file(s)
- `experiments` — 11 analysed file(s)
- `build_support` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x generated/minified file excluded).
- File demo/kitchen-sink/docs/python.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `2e1b35190636654b14b089383e031ff3f065369b` is the revision these paths and observations refer to.
