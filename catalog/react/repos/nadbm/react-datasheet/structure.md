# Project structure: nadbm/react-datasheet

**Analysed commit:** `13b5c35f28b4bab2547402b2c406986ef1913245`

**Commit reference:** [13b5c35f28b4bab2547402b2c406986ef1913245](https://github.com/nadbm/react-datasheet/commit/13b5c35f28b4bab2547402b2c406986ef1913245)

**Tree at this commit:** [nadbm/react-datasheet@13b5c35f28b4](https://github.com/nadbm/react-datasheet/tree/13b5c35f28b4bab2547402b2c406986ef1913245)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | nadbm/react-datasheet |
| Description | Excel-like data grid (table) component for React |
| Stars | 5440 |
| Forks | 445 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `13b5c35f28b4bab2547402b2c406986ef1913245` |
| Retrieved at | 2026-11-14T19:14:19.376365+00:00 |
| Files in this snapshot | 53 |

## Directory tree

```text
docs/  (15 files)
  public/  (1 files)
    index.html
  src/  (12 files)
    examples/  (9 files)
      … 9 files under this directory
    app.js
    index.css
    index.js
  .gitignore
  package.json
lib/  (12 files)
  Cell.js
  CellShape.js
  DataCell.js
  DataEditor.js
  DataSheet.js
  Row.js
  Sheet.js
  ValueViewer.js
  index.js
  keys.js
  react-datasheet.css
  renderHelpers.js
src/  (12 files)
  Cell.js
  CellShape.js
  DataCell.js
  DataEditor.js
  DataSheet.js
  Row.js
  Sheet.js
  ValueViewer.js
  index.js
  keys.js
  react-datasheet.css
  renderHelpers.js
test/  (1 files)
  Datasheet.js
types/  (1 files)
  react-datasheet.d.ts
.babelrc
.codeclimate.yml
.csslintrc
.gitignore
.npmignore
.prettierrc
.travis.yml
LICENSE
README.md
USAGE_TYPESCRIPT.md
package.json
params.json
```

## Entry points

- [lib/index.js](https://github.com/nadbm/react-datasheet/blob/13b5c35f28b4bab2547402b2c406986ef1913245/lib/index.js)
- [src/index.js](https://github.com/nadbm/react-datasheet/blob/13b5c35f28b4bab2547402b2c406986ef1913245/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Cell.js package | library | Observed | Groups 1 file(s) under cell.js package (observed from repository paths and static analysis). |
| CellShape.js package | library | Observed | Groups 1 file(s) under cellshape.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| DataCell.js package | library | Observed | Groups 1 file(s) under datacell.js package (observed from repository paths and static analysis). |
| DataEditor.js package | library | Observed | Groups 1 file(s) under dataeditor.js package (observed from repository paths and static analysis). |
| DataSheet.js package | library | Observed | Groups 1 file(s) under datasheet.js package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| keys.js package | library | Observed | Groups 1 file(s) under keys.js package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 11 file(s) under lib package (observed from repository paths and static analysis). |
| renderHelpers.js package | library | Observed | Groups 1 file(s) under renderhelpers.js package (observed from repository paths and static analysis). |
| Row.js package | library | Observed | Groups 1 file(s) under row.js package (observed from repository paths and static analysis). |
| Sheet.js package | library | Observed | Groups 1 file(s) under sheet.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 1 file(s) under types package (observed from repository paths and static analysis). |
| ValueViewer.js package | library | Observed | Groups 1 file(s) under valueviewer.js package (observed from repository paths and static analysis). |

## Important files

- `.codeclimate.yml` (config)
- `.travis.yml` (ci)
- `docs/package.json` (manifest)
- `package.json` (manifest)
- `params.json` (config)

## Top-level layout

- `docs` — 15 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `lib` — 12 analysed file(s)
- `src` — 12 analysed file(s)
- `test` — 1 analysed file(s)
- `types` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `13b5c35f28b4bab2547402b2c406986ef1913245` is the revision these paths and observations refer to.
