# Project structure: chjj/blessed

**Analysed commit:** `eab243fc7ad27f1d2932db6134f7382825ee3488`

**Commit reference:** [eab243fc7ad27f1d2932db6134f7382825ee3488](https://github.com/chjj/blessed/commit/eab243fc7ad27f1d2932db6134f7382825ee3488)

**Tree at this commit:** [chjj/blessed@eab243fc7ad2](https://github.com/chjj/blessed/tree/eab243fc7ad27f1d2932db6134f7382825ee3488)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | chjj/blessed |
| Description | A high-level terminal interface library for node.js. |
| Stars | 11883 |
| Forks | 560 |
| Licence | Other |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `eab243fc7ad27f1d2932db6134f7382825ee3488` |
| Retrieved at | 2026-11-14T19:12:14.253671+00:00 |
| Files in this snapshot | 121 |

## Directory tree

```text
bin/  (1 files)
  tput.js
browser/  (2 files)
  Makefile
  transform.js
example/  (13 files)
  ansi-viewer/  (6 files)
    LICENSE
    README.md
    ansi-art.list
    index.js
    package.json
    singlebyte.js
  blessed-telnet.js
  index.js
  multiplex.js
  ping
  simple-form.js
  time.js
  widget.js
lib/  (45 files)
  widgets/  (34 files)
    ansiimage.js
    bigtext.js
    box.js
    button.js
    checkbox.js
    element.js
    filemanager.js
    form.js
    image.js
    input.js
    layout.js
    line.js
    list.js
    listbar.js
    listtable.js
    loading.js
    log.js
    message.js
    node.js
    overlayimage.js
    progressbar.js
    prompt.js
    question.js
    radiobutton.js
    … 10 more files
  alias.js
  blessed.js
  colors.js
  events.js
  gpmclient.js
  helpers.js
  keys.js
  program.js
  tput.js
  unicode.js
  widget.js
test/  (46 files)
  logs/  (1 files)
    .gitignore
  git.diff
  helpers.js
  lorem.txt
  program-mouse.js
  tail.js
  terminfo
  tput
  tput.js
  widget-autopad.js
  widget-bigtext.js
  widget-csr.js
  widget-dock-noborder.js
  widget-dock.js
  widget-exit.js
  widget-file.js
  widget-form.js
  widget-image.js
  widget-insert.js
  widget-layout.js
  widget-listbar.js
  widget-listtable.js
  widget-log.js
  widget-nested-attr.js
  widget-noalt.js
  … 21 more files
usr/  (5 files)
  fonts/  (3 files)
    AUTHORS
    LICENSE
    README
  xterm.termcap
  xterm.terminfo
.gitignore
.jscsrc
.jshintrc
.npmignore
CHANGELOG.md
LICENSE
README.md
index.js
package.json
```

## Entry points

- [example/ansi-viewer/index.js](https://github.com/chjj/blessed/blob/eab243fc7ad27f1d2932db6134f7382825ee3488/example/ansi-viewer/index.js)
- [lib/blessed.js](https://github.com/chjj/blessed/blob/eab243fc7ad27f1d2932db6134f7382825ee3488/lib/blessed.js)
- [bin/tput.js](https://github.com/chjj/blessed/blob/eab243fc7ad27f1d2932db6134f7382825ee3488/bin/tput.js)
- [index.js](https://github.com/chjj/blessed/blob/eab243fc7ad27f1d2932db6134f7382825ee3488/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bin package | library | Observed | Groups 1 file(s) under bin package (observed from repository paths and static analysis). |
| browser package | library | Observed | Groups 1 file(s) under browser package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 45 file(s) under lib package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 46 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `example/ansi-viewer/package.json` (manifest)
- `package.json` (manifest)

## Top-level layout

- `test` — 46 analysed file(s)
- `lib` — 45 analysed file(s)
- `example` — 13 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `usr` — 5 analysed file(s)
- `browser` — 2 analysed file(s)
- `bin` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `eab243fc7ad27f1d2932db6134f7382825ee3488` is the revision these paths and observations refer to.
