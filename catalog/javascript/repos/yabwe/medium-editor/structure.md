# Project structure: yabwe/medium-editor

**Analysed commit:** `d113a74437fda6f1cbd5f146b0f2c46288b118ea`

**Commit reference:** [d113a74437fda6f1cbd5f146b0f2c46288b118ea](https://github.com/yabwe/medium-editor/commit/d113a74437fda6f1cbd5f146b0f2c46288b118ea)

**Tree at this commit:** [yabwe/medium-editor@d113a74437fd](https://github.com/yabwe/medium-editor/tree/d113a74437fda6f1cbd5f146b0f2c46288b118ea)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | yabwe/medium-editor |
| Description | Medium.com WYSIWYG editor clone. Uses contenteditable API to implement a rich text solution. |
| Stars | 16098 |
| Forks | 1802 |
| Licence | Other |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `d113a74437fda6f1cbd5f146b0f2c46288b118ea` |
| Retrieved at | 2026-11-14T19:11:34.133183+00:00 |
| Files in this snapshot | 115 |

## Directory tree

```text
.github/  (2 files)
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
demo/  (18 files)
  css/  (1 files)
    demo.css
  js/  (1 files)
    extension-table.js
  absolute-container.html
  auto-link.html
  button-example.html
  clean-paste.html
  custom-toolbar.html
  extension-example.html
  index.html
  multi-editor.html
  multi-one-instance.html
  multi-paragraph.html
  nested-editable.html
  pass-instance.html
  relative-toolbar.html
  static-toolbar.html
  table-extension.html
  textarea.html
spec/  (29 files)
  helpers/  (1 files)
    util.js
  anchor-preview.spec.js
  anchor.spec.js
  auto-link.spec.js
  buttons.spec.js
  content.spec.js
  core-api.spec.js
  delay.spec.js
  drag-and-drop.spec.js
  dyn-elements.spec.js
  elements.spec.js
  events.spec.js
  exploits.spec.js
  extension.spec.js
  fontname.spec.js
  fontsize.spec.js
  full-content.spec.js
  header-tags.spec.js
  init.spec.js
  keyboard-commands.spec.js
  paste.spec.js
  placeholder.spec.js
  selection.spec.js
  serialize.spec.js
  setup.spec.js
  … 4 more files
src/  (45 files)
  js/  (26 files)
    defaults/  (2 files)
      … 2 files under this directory
    extensions/  (16 files)
      … 16 files under this directory
    core.js
    events.js
    extension.js
    globals.js
    polyfills.js
    selection.js
    util.js
    version.js
  sass/  (17 files)
    animations/  (2 files)
      … 2 files under this directory
    components/  (5 files)
      … 5 files under this directory
    themes/  (7 files)
      … 7 files under this directory
    util/  (1 files)
      … 1 files under this directory
    _settings.scss
    medium-editor.scss
  wrappers/  (2 files)
    end.js
    start.js
.editorconfig
.gitignore
.jscsrc
.jshintrc
.travis.yml
API.md
CHANGES.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
CUSTOM-EVENTS.md
Gruntfile.js
LICENSE
MAINTAINERS.md
OPTIONS.md
README.md
UPGRADE-5.md
bower.json
index.js
karma.conf.js
karma.dev.conf.js
package.json
```

## Entry points

- [index.js](https://github.com/yabwe/medium-editor/blob/d113a74437fda6f1cbd5f146b0f2c46288b118ea/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| demo package | library | Observed | Groups 1 file(s) under demo package (observed from repository paths and static analysis). |
| js package | library | Observed | Groups 23 file(s) under js package (observed from repository paths and static analysis). |
| spec package | library | Observed | Groups 29 file(s) under spec package (observed from repository paths and static analysis). |
| wrappers package | library | Observed | Groups 2 file(s) under wrappers package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.travis.yml` (ci)
- `bower.json` (config)
- `package.json` (manifest)

## Top-level layout

- `src` — 45 analysed file(s)
- `spec` — 29 analysed file(s)
- `(root files)` — 21 analysed file(s)
- `demo` — 18 analysed file(s)
- `.github` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 19 file(s) were skipped during inventory (1 x likely secret file excluded; 18 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `d113a74437fda6f1cbd5f146b0f2c46288b118ea` is the revision these paths and observations refer to.
