# Project structure: pandao/editor.md

**Analysed commit:** `63786e671e2c1a1fd2be25b54a8910cd3bbc7c0a`

**Commit reference:** [63786e671e2c1a1fd2be25b54a8910cd3bbc7c0a](https://github.com/pandao/editor.md/commit/63786e671e2c1a1fd2be25b54a8910cd3bbc7c0a)

**Tree at this commit:** [pandao/editor.md@63786e671e2c](https://github.com/pandao/editor.md/tree/63786e671e2c1a1fd2be25b54a8910cd3bbc7c0a)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | pandao/editor.md |
| Description | The open source embeddable online markdown editor (component). |
| Stars | 14311 |
| Forks | 2437 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `63786e671e2c1a1fd2be25b54a8910cd3bbc7c0a` |
| Retrieved at | 2026-11-14T19:11:45.815427+00:00 |
| Files in this snapshot | 447 |

## Directory tree

```text
css/  (3 files)
  editormd.css
  editormd.logo.css
  editormd.preview.css
docs/  (15 files)
  fonts/  (6 files)
    OpenSans-Bold-webfont.svg
    OpenSans-BoldItalic-webfont.svg
    OpenSans-Italic-webfont.svg
    OpenSans-Light-webfont.svg
    OpenSans-LightItalic-webfont.svg
    OpenSans-Regular-webfont.svg
  scripts/  (4 files)
    prettify/  (3 files)
      … 3 files under this directory
    linenumber.js
  styles/  (3 files)
    jsdoc-default.css
    prettify-jsdoc.css
    prettify-tomorrow.css
  editormd.js.html
  index.html
examples/  (58 files)
  css/  (1 files)
    style.css
  js/  (2 files)
    sea.js
    seajs-main.js
  php/  (5 files)
    cross-domain-upload.php
    editormd.uploader.class.php
    post.php
    upload.php
    upload_callback.html
  @links.html
  auto-height.html
  change-mode.html
  code-fold.html
  custom-keyboard-shortcuts.html
  custom-toolbar.html
  define-plugin.html
  delay-renderer-preview.html
  dynamic-create-editormd.html
  emoji.html
  extends.html
  external-use.html
  flowchart.html
  form-get-value.html
  full.html
  goto-line.html
  html-preview-markdown-to-html-custom-toc-container.html
  html-preview-markdown-to-html.html
  html-tags-decode.html
  image-cross-domain-upload.html
  image-upload.html
  index.html
  katex.html
  manually-load-modules.html
  … 26 more files
fonts/  (1 files)
  editormd-logo.svg
languages/  (2 files)
  en.js
  zh-tw.js
lib/  (314 files)
  codemirror/  (314 files)
    addon/  (65 files)
      … 65 files under this directory
    lib/  (1 files)
      … 1 files under this directory
    mode/  (210 files)
      … 210 files under this directory
    theme/  (33 files)
      … 33 files under this directory
    AUTHORS
    LICENSE
    README.md
    bower.json
    package.json
plugins/  (15 files)
  code-block-dialog/  (1 files)
    code-block-dialog.js
  emoji-dialog/  (2 files)
    emoji-dialog.js
    emoji.json
  goto-line-dialog/  (1 files)
    goto-line-dialog.js
  help-dialog/  (2 files)
    help-dialog.js
    help.md
  html-entities-dialog/  (2 files)
    html-entities-dialog.js
    html-entities.json
  image-dialog/  (1 files)
    image-dialog.js
  link-dialog/  (1 files)
    link-dialog.js
  preformatted-text-dialog/  (1 files)
    preformatted-text-dialog.js
  reference-link-dialog/  (1 files)
    reference-link-dialog.js
  table-dialog/  (1 files)
    table-dialog.js
  test-plugin/  (1 files)
    test-plugin.js
  plugin-template.js
scss/  (16 files)
  lib/  (2 files)
    prefixes.scss
    variables.scss
  editormd.codemirror.scss
  editormd.dialog.scss
  editormd.form.scss
  editormd.grid.scss
  editormd.logo.scss
  editormd.menu.scss
  editormd.preview.scss
  editormd.preview.themes.scss
  editormd.scss
  editormd.tab.scss
  editormd.themes.scss
  font-awesome.scss
  github-markdown.scss
  prettify.scss
src/  (1 files)
  editormd.js
tests/  (11 files)
  js/  (1 files)
    searchbox.js
  qunit/  (2 files)
    qunit-1.16.0.css
    qunit-1.16.0.js
  bootstrap-test.html
  codemirror-searchbox-test.html
  codemirror-test.html
  katex-tests.html
  marked-@at-test.html
  marked-emoji-test.html
  marked-heading-link-test.html
  marked-todo-list-test.html
.gitignore
.jshintrc
BUGS.md
CHANGE.md
Gulpfile.js
LICENSE
README.md
bower.json
editormd.amd.js
editormd.js
package.json
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| editormd.js package | library | Observed | Groups 1 file(s) under editormd.js package (observed from repository paths and static analysis). |
| languages package | library | Observed | Groups 2 file(s) under languages package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 164 file(s) under lib package (observed from repository paths and static analysis). |
| plugins package | library | Observed | Groups 12 file(s) under plugins package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 11 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `bower.json` (config)
- `lib/codemirror/bower.json` (config)
- `lib/codemirror/mode/dockerfile/dockerfile.js` (container)
- `lib/codemirror/package.json` (manifest)
- `package.json` (manifest)
- `plugins/emoji-dialog/emoji.json` (config)
- `plugins/html-entities-dialog/html-entities.json` (config)

## Top-level layout

- `lib` — 314 analysed file(s)
- `examples` — 58 analysed file(s)
- `scss` — 16 analysed file(s)
- `docs` — 15 analysed file(s)
- `plugins` — 15 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `tests` — 11 analysed file(s)
- `css` — 3 analysed file(s)
- `languages` — 2 analysed file(s)
- `fonts` — 1 analysed file(s)
- `src` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 6 file(s) were skipped during inventory (6 x generated/minified file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `63786e671e2c1a1fd2be25b54a8910cd3bbc7c0a` is the revision these paths and observations refer to.
