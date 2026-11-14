# Project structure: exceljs/exceljs

**Analysed commit:** `5bed18b45e824f409b08456b59b87430ded023ab`

**Commit reference:** [5bed18b45e824f409b08456b59b87430ded023ab](https://github.com/exceljs/exceljs/commit/5bed18b45e824f409b08456b59b87430ded023ab)

**Tree at this commit:** [exceljs/exceljs@5bed18b45e82](https://github.com/exceljs/exceljs/tree/5bed18b45e824f409b08456b59b87430ded023ab)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | exceljs/exceljs |
| Description | Excel Workbook Manager |
| Stars | 15517 |
| Forks | 2076 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `5bed18b45e824f409b08456b59b87430ded023ab` |
| Retrieved at | 2026-11-14T19:11:37.779180+00:00 |
| Files in this snapshot | 501 |

## Directory tree

```text
.github/  (8 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    feature.md
    question.md
  workflows/  (2 files)
    asset-size.yml
    tests.yml
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
  lock.yml
lib/  (178 files)
  csv/  (3 files)
    csv.js
    line-buffer.js
    stream-converter.js
  doc/  (16 files)
    data/  (1 files)
      … 1 files under this directory
    anchor.js
    cell.js
    column.js
    data-validations.js
    defined-names.js
    enums.js
    image.js
    modelcontainer.js
    note.js
    pivot-table.js
    range.js
    row.js
    table.js
    workbook.js
    worksheet.js
  stream/  (7 files)
    xlsx/  (7 files)
      … 7 files under this directory
  utils/  (21 files)
    auto-drain.js
    browser-buffer-decode.js
    browser-buffer-encode.js
    cell-matrix.js
    col-cache.js
    copy-style.js
    encryptor.js
    iterate-stream.js
    parse-sax.js
    shared-formula.js
    shared-strings.js
    stream-base64.js
    stream-buf.js
    string-buf.js
    string-builder.js
    stuttered-pipe.js
    typed-stack.js
    under-dash.js
    utils.js
    xml-stream.js
    zip-stream.js
  xlsx/  (128 files)
    xform/  (118 files)
      … 118 files under this directory
    xml/  (2 files)
      … 2 files under this directory
    .rels
    calcChain.xml
    core.xml
    defaultnumformats.js
    rel-type.js
    styles.xml
    workbook.xml
    xlsx.js
  exceljs.bare.js
  exceljs.browser.js
  exceljs.nodejs.js
spec/  (234 files)
  browser/  (1 files)
    exceljs.spec.js
  config/  (2 files)
    setup-unit.js
    setup.js
  end-to-end/  (1 files)
    express.spec.js
  integration/  (49 files)
    data/  (5 files)
      … 5 files under this directory
    issues/  (23 files)
      … 23 files under this directory
    pr/  (12 files)
      … 12 files under this directory
    workbook/  (4 files)
      … 4 files under this directory
    workbook-xlsx-writer/  (1 files)
      … 1 files under this directory
    gold.spec.js
    workbook-xlsx-reader.spec.js
    worksheet-xlsx-writer.spec.js
    worksheet.spec.js
  manual/  (3 files)
    public/  (2 files)
      … 2 files under this directory
    app.js
  out/  (1 files)
    README.md
  typescript/  (1 files)
    exceljs.spec.ts
  unit/  (157 files)
    data/  (1 files)
      … 1 files under this directory
    doc/  (16 files)
      … 16 files under this directory
    utils/  (11 files)
      … 11 files under this directory
    xlsx/  (129 files)
      … 129 files under this directory
  utils/  (17 files)
    data/  (8 files)
      … 8 files under this directory
    index.js
    test-conditional-formatting-sheet.js
    test-data-validation-sheet.js
    test-spliced-sheet.js
    test-values-sheet.js
    test-workbook-reader.js
    tools.js
    under-dash.js
    verquire.js
  .eslintrc
  .jshintrc
test/  (62 files)
  regression/  (4 files)
    utils/  (1 files)
      … 1 files under this directory
    package.json
    testBookIn.js
    testBookOut.js
  utils/  (3 files)
    column-sum.js
    hr-stopwatch.js
    utils.js
  .eslintrc
  test-a1.js
  test-cf.js
  test-chart.js
  test-colour-cell.js
  test-comment-new.js
  test-comment-stream-writer.js
  test-comments.js
  test-copy.js
  test-default-height.js
  test-formula.js
  test-header-footer.js
  test-hyperlink.js
  test-image-one-cell-anchor.js
  test-image-oneCell.js
  test-image-out.js
  test-image-stream-writer.js
  test-issue-530.js
  test-issue-581.js
  test-jszip.js
  test-merge-align.js
  test-newline.js
  test-pivot-table.js
  test-protection-spinCount.js
  … 31 more files
.babelrc
.browserslistrc
.eslintignore
.eslintrc
.gitignore
.prettier
.prettierignore
LICENSE
MODEL.md
README_zh.md
TODO.txt
UPGRADE-4.0.md
benchmark.js
excel.js
gruntfile.js
index.d.ts
index.ts
package.json
tsconfig.json
```

## Entry points

- [excel.js](https://github.com/exceljs/exceljs/blob/5bed18b45e824f409b08456b59b87430ded023ab/excel.js)
- [index.ts](https://github.com/exceljs/exceljs/blob/5bed18b45e824f409b08456b59b87430ded023ab/index.ts)
- [spec/manual/app.js](https://github.com/exceljs/exceljs/blob/5bed18b45e824f409b08456b59b87430ded023ab/spec/manual/app.js)
- [spec/utils/index.js](https://github.com/exceljs/exceljs/blob/5bed18b45e824f409b08456b59b87430ded023ab/spec/utils/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 40 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 5 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 5 file(s) under data layer (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 44 file(s) under external integrations (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 164 file(s) under lib package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 13 file(s) under service / domain layer (observed from repository paths and static analysis). |
| spec package | library | Observed | Groups 109 file(s) under spec package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 62 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/lock.yml` (config)
- `.github/workflows/asset-size.yml` (ci)
- `.github/workflows/tests.yml` (ci)
- `lib/doc/data/theme1.json` (config)
- `package.json` (manifest)
- `spec/integration/data/rich-text-sample-a1.json` (config)
- `spec/integration/data/testmodel.json` (config)
- `spec/unit/data/simpleWorkbook.json` (config)
- `spec/unit/xlsx/xform/book/data/book.1.1.json` (config)
- `spec/unit/xlsx/xform/book/data/book.1.3.json` (config)
- `spec/unit/xlsx/xform/book/data/book.2.3.json` (config)
- `spec/unit/xlsx/xform/core/data/worksheet.rels.1.json` (config)
- `spec/unit/xlsx/xform/sheet/data/sheet.1.0.json` (config)
- `spec/unit/xlsx/xform/sheet/data/sheet.1.1.json` (config)
- `spec/unit/xlsx/xform/sheet/data/sheet.1.3.json` (config)
- `spec/unit/xlsx/xform/sheet/data/sheet.1.4.json` (config)
- `spec/unit/xlsx/xform/sheet/data/sheet.2.0.json` (config)
- `spec/unit/xlsx/xform/sheet/data/sheet.2.1.json` (config)
- `spec/unit/xlsx/xform/sheet/data/sheet.3.1.json` (config)
- `spec/unit/xlsx/xform/sheet/data/sheet.4.0.json` (config)
- `spec/unit/xlsx/xform/sheet/data/sheet.5.0.json` (config)
- `spec/unit/xlsx/xform/sheet/data/sheet.5.1.json` (config)
- `spec/unit/xlsx/xform/sheet/data/sheet.5.3.json` (config)
- `spec/unit/xlsx/xform/sheet/data/sheet.5.4.json` (config)
- `spec/unit/xlsx/xform/sheet/data/sheet.6.1.json` (config)
- `spec/unit/xlsx/xform/sheet/data/sheet.6.3.json` (config)
- `spec/unit/xlsx/xform/sheet/data/sheet.7.0.json` (config)
- `spec/unit/xlsx/xform/sheet/data/sheet.7.1.json` (config)
- `spec/unit/xlsx/xform/strings/data/sharedStrings.json` (config)
- `spec/unit/xlsx/xform/style/data/styles.1.1.json` (config)
- `spec/unit/xlsx/xform/table/data/table.1.1.json` (config)
- `spec/unit/xlsx/xform/table/data/table.1.3.json` (config)
- `spec/utils/data/conditional-formatting.json` (config)
- `spec/utils/data/data-validations.json` (config)
- `spec/utils/data/header-footer.json` (config)
- `spec/utils/data/page-setup.json` (config)
- `spec/utils/data/sheet-properties.json` (config)
- `spec/utils/data/sheet-values.json` (config)
- `spec/utils/data/styles.json` (config)
- `spec/utils/data/views.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `spec` — 234 analysed file(s)
- `lib` — 178 analysed file(s)
- `test` — 62 analysed file(s)
- `(root files)` — 19 analysed file(s)
- `.github` — 8 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (1 x likely secret file excluded; 1 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `5bed18b45e824f409b08456b59b87430ded023ab` is the revision these paths and observations refer to.
