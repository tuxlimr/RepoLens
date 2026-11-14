# Project structure: myliang/x-spreadsheet

**Analysed commit:** `0c55f3ee1e708002eaef280432d6efeaeabdc886`

**Commit reference:** [0c55f3ee1e708002eaef280432d6efeaeabdc886](https://github.com/myliang/x-spreadsheet/commit/0c55f3ee1e708002eaef280432d6efeaeabdc886)

**Tree at this commit:** [myliang/x-spreadsheet@0c55f3ee1e70](https://github.com/myliang/x-spreadsheet/tree/0c55f3ee1e708002eaef280432d6efeaeabdc886)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | myliang/x-spreadsheet |
| Description | The project has been migrated to @wolf-table/table https://github.com/wolf-table/table |
| Stars | 14571 |
| Forks | 1747 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `0c55f3ee1e708002eaef280432d6efeaeabdc886` |
| Retrieved at | 2026-11-14T19:11:44.230066+00:00 |
| Files in this snapshot | 128 |

## Directory tree

```text
.github/  (1 files)
  FUNDING.yml
assets/  (2 files)
  material_common_sprite82.svg
  sprite.svg
docs/  (9 files)
  locale/  (4 files)
    de.js
    en.js
    nl.js
    zh-cn.js
  58eaeb4e52248a5c75936c6f4c33a370.svg
  ece3e4fa05d4292823fdef970eaf1233.svg
  index.html
  xspreadsheet.css
  xspreadsheet.js
src/  (96 files)
  algorithm/  (2 files)
    bitmap.js
    expression.js
  canvas/  (2 files)
    draw.js
    draw2.js
  component/  (64 files)
    toolbar/  (28 files)
      … 28 files under this directory
    border_palette.js
    bottombar.js
    button.js
    calendar.js
    color_palette.js
    contextmenu.js
    datepicker.js
    dropdown.js
    dropdown_align.js
    dropdown_border.js
    dropdown_color.js
    dropdown_font.js
    dropdown_fontsize.js
    dropdown_format.js
    dropdown_formula.js
    dropdown_linetype.js
    editor.js
    element.js
    event.js
    form_field.js
    form_input.js
    form_select.js
    icon.js
    message.js
    … 12 more files
  core/  (19 files)
    _.prototypes.js
    alphabet.js
    auto_filter.js
    cell.js
    cell_range.js
    clipboard.js
    col.js
    data_proxy.js
    font.js
    format.js
    formula.js
    helper.js
    history.js
    merge.js
    row.js
    scroll.js
    selector.js
    validation.js
    validator.js
  locale/  (5 files)
    de.js
    en.js
    locale.js
    nl.js
    zh-cn.js
  config.js
  index.d.ts
  index.js
  index.less
test/  (9 files)
  core/  (6 files)
    alphabet_test.js
    cell_range_test.js
    cell_test.js
    font_test.js
    format_test.js
    formula_test.js
  locale/  (1 files)
    locale_test.js
  helper_test.js
  index_test.js
.babelrc
.eslintignore
.eslintrc.js
.gitignore
.travis.yml
CODE_OF_CONDUCT.md
LICENSE
index.html
npmx.txt
package.json
readme.md
```

## Entry points

- [src/index.js](https://github.com/myliang/x-spreadsheet/blob/0c55f3ee1e708002eaef280432d6efeaeabdc886/src/index.js)
- [src/component/toolbar/index.js](https://github.com/myliang/x-spreadsheet/blob/0c55f3ee1e708002eaef280432d6efeaeabdc886/src/component/toolbar/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| algorithm package | library | Observed | Groups 2 file(s) under algorithm package (observed from repository paths and static analysis). |
| canvas package | library | Observed | Groups 2 file(s) under canvas package (observed from repository paths and static analysis). |
| component package | library | Observed | Groups 64 file(s) under component package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| config.js package | library | Observed | Groups 1 file(s) under config.js package (observed from repository paths and static analysis). |
| index.d.ts package | library | Observed | Groups 1 file(s) under index.d.ts package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| locale package | library | Observed | Groups 5 file(s) under locale package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 19 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 9 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.travis.yml` (ci)
- `package.json` (manifest)

## Top-level layout

- `src` — 96 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `docs` — 9 analysed file(s)
- `test` — 9 analysed file(s)
- `assets` — 2 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 22 file(s) were skipped during inventory (22 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `0c55f3ee1e708002eaef280432d6efeaeabdc886` is the revision these paths and observations refer to.
