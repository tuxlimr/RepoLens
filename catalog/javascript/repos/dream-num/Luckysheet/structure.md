# Project structure: dream-num/Luckysheet

**Analysed commit:** `5b3fe58f5ad2aaa6a3cef15c6d567f5e10ea1f37`

**Commit reference:** [5b3fe58f5ad2aaa6a3cef15c6d567f5e10ea1f37](https://github.com/dream-num/Luckysheet/commit/5b3fe58f5ad2aaa6a3cef15c6d567f5e10ea1f37)

**Tree at this commit:** [dream-num/Luckysheet@5b3fe58f5ad2](https://github.com/dream-num/Luckysheet/tree/5b3fe58f5ad2aaa6a3cef15c6d567f5e10ea1f37)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | dream-num/Luckysheet |
| Description | Luckysheet upgraded to Univer |
| Stars | 16624 |
| Forks | 2596 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `5b3fe58f5ad2aaa6a3cef15c6d567f5e10ea1f37` |
| Retrieved at | 2026-11-14T19:11:31.396023+00:00 |
| Files in this snapshot | 170 |

## Directory tree

```text
.github/  (8 files)
  ISSUE_TEMPLATE/  (4 files)
    bug_report.md
    bug_report_zh.md
    feature_request.md
    feature_request_zh.md
  workflows/  (3 files)
    gitee-mirror.yml
    github-demo.yml
    github-doc.yml
  FUNDING.yml
docs/  (28 files)
  .vuepress/  (1 files)
    config.js
  about/  (3 files)
    README.md
    company.md
    sponsor.md
  guide/  (10 files)
    FAQ.md
    README.md
    api.md
    cell.md
    config.md
    contribute.md
    data.md
    operate.md
    resource.md
    sheet.md
  zh/  (13 files)
    about/  (3 files)
      … 3 files under this directory
    guide/  (9 files)
      … 9 files under this directory
    README.md
  README.md
src/  (122 files)
  assets/  (6 files)
    iconfont/  (6 files)
      … 6 files under this directory
  controllers/  (43 files)
    alternateformat.js
    cellDatePickerCtrl.js
    cellFormat.js
    constant.js
    controlHistory.js
    dataVerificationCtrl.js
    dropCell.js
    expendPlugins.js
    filter.js
    formulaBar.js
    freezen.js
    hyperlinkCtrl.js
    ifFormulaGenerator.js
    imageCtrl.js
    imageUpdateCtrl.js
    inlineString.js
    insertFormula.js
    keyboard.js
    listener.js
    locationCell.js
    luckysheetConfigsetting.js
    matrixOperation.js
    mobile.js
    moreFormat.js
    … 19 more files
  css/  (7 files)
    iconCustom.css
    luckysheet-cellFormat.css
    luckysheet-core.css
    luckysheet-protection.css
    luckysheet-zoom.css
    menuSprite.svg
    sprite38.svg
  data/  (1 files)
    chartJson.js
  demoData/  (13 files)
    chat.js
    demoFeature.js
    sheetCell.js
    sheetChart.js
    sheetComment.js
    sheetConditionFormat.js
    sheetDataVerification.js
    sheetFormula.js
    sheetPicture.js
    sheetPivotTable.js
    sheetPivotTableData.js
    sheetSparkline.js
    sheetTable.js
  expendPlugins/  (6 files)
    chart/  (2 files)
      … 2 files under this directory
    exportXlsx/  (1 files)
      … 1 files under this directory
    print/  (3 files)
      … 3 files under this directory
  function/  (5 files)
    func.js
    functionlist.js
    getLocalizedFunctionList.js
    luckysheet_function.js
    matrix_methods.js
  global/  (29 files)
    analysis.js
    array.js
    border.js
    browser.js
    cleargridelement.js
    count.js
    createdom.js
    createsheet.js
    cursorPos.js
    datecontroll.js
    draw.js
    dynamicArray.js
    editor.js
    extend.js
    format.js
    func_methods.js
    getRowlen.js
    getdata.js
    json.js
    loading.js
    location.js
    method.js
    refresh.js
    rhchInit.js
    … 5 more files
  locale/  (1 files)
    locale.js
  methods/  (2 files)
    get.js
    set.js
  plugins/  (1 files)
    jquery.sPage.css
  store/  (1 files)
    index.js
  utils/  (4 files)
    chartUtil.js
    math.js
    polyfill.js
    util.js
  config.js
  core.js
  index.js
.eslintignore
.gitignore
.prettierignore
.prettierrc.json
CHANGELOG.md
LICENSE
README-zh.md
README.md
commitlint.config.js
deploy.bat
gulpfile.js
package.json
```

## Entry points

- [src/controllers/server.js](https://github.com/dream-num/Luckysheet/blob/5b3fe58f5ad2aaa6a3cef15c6d567f5e10ea1f37/src/controllers/server.js)
- [src/index.js](https://github.com/dream-num/Luckysheet/blob/5b3fe58f5ad2aaa6a3cef15c6d567f5e10ea1f37/src/index.js)
- [src/store/index.js](https://github.com/dream-num/Luckysheet/blob/5b3fe58f5ad2aaa6a3cef15c6d567f5e10ea1f37/src/store/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 43 file(s) under api layer (observed from repository paths and static analysis). |
| assets package | library | Observed | Groups 1 file(s) under assets package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| config.js package | library | Observed | Groups 1 file(s) under config.js package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| core.js package | library | Observed | Groups 1 file(s) under core.js package (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). |
| demoData package | library | Observed | Groups 13 file(s) under demodata package (observed from repository paths and static analysis). |
| expendPlugins package | library | Observed | Groups 4 file(s) under expendplugins package (observed from repository paths and static analysis). |
| function package | library | Observed | Groups 5 file(s) under function package (observed from repository paths and static analysis). |
| global package | library | Observed | Groups 29 file(s) under global package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| locale package | library | Observed | Groups 1 file(s) under locale package (observed from repository paths and static analysis). |
| methods package | library | Observed | Groups 2 file(s) under methods package (observed from repository paths and static analysis). |
| store package | library | Observed | Groups 1 file(s) under store package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 4 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/workflows/gitee-mirror.yml` (ci)
- `.github/workflows/github-demo.yml` (ci)
- `.github/workflows/github-doc.yml` (ci)
- `.prettierrc.json` (config)
- `package.json` (manifest)
- `src/assets/iconfont/iconfont.json` (config)

## Top-level layout

- `src` — 122 analysed file(s)
- `docs` — 28 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `.github` — 8 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 4 file(s) were skipped during inventory (4 x generated/minified file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `5b3fe58f5ad2aaa6a3cef15c6d567f5e10ea1f37` is the revision these paths and observations refer to.
