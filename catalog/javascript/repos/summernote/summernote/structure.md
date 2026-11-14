# Project structure: summernote/summernote

**Analysed commit:** `ac5460e0e9a0b622ad7deff162915a3960ff4b96`

**Commit reference:** [ac5460e0e9a0b622ad7deff162915a3960ff4b96](https://github.com/summernote/summernote/commit/ac5460e0e9a0b622ad7deff162915a3960ff4b96)

**Tree at this commit:** [summernote/summernote@ac5460e0e9a0](https://github.com/summernote/summernote/tree/ac5460e0e9a0b622ad7deff162915a3960ff4b96)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | summernote/summernote |
| Description | Super Simple WYSIWYG Editor |
| Stars | 11841 |
| Forks | 2245 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `ac5460e0e9a0b622ad7deff162915a3960ff4b96` |
| Retrieved at | 2026-11-14T19:12:13.710667+00:00 |
| Files in this snapshot | 264 |

## Directory tree

```text
.github/  (12 files)
  ISSUE_TEMPLATE/  (4 files)
    bug_report.yml
    config.yml
    feature_request.yml
    improve_documentation.yml
  workflows/  (3 files)
    build.yml
    codeql-analysis.yml
    npm-publish.yml
  CODE_OF_CONDUCT.md
  CONTRIBUTING.md
  FUNDING.yml
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
examples/  (29 files)
  README.md
  airmode.html
  codemirror.html
  custom-style.html
  example.css
  external-api.html
  external-codemirror.html
  hint-emoji.html
  hint-math.html
  hint-userdefine.html
  hint-words.html
  history-limit.html
  index.html
  jquery-custom-event.html
  lang.html
  link-blank.html
  mode-switcher.html
  ondialog-multitab.html
  ondialog.html
  placeholder.html
  plugin-hello.html
  recordEveryKeyStroke.html
  summernote-bs3.html
  summernote-bs4.html
  … 5 more files
public/  (52 files)
  font/  (1 files)
    summernote.hash
  lang/  (47 files)
    README.md
    summernote-ar-AR.js
    summernote-az-AZ.js
    summernote-bg-BG.js
    summernote-bn-BD.js
    summernote-ca-ES.js
    summernote-cs-CZ.js
    summernote-da-DK.js
    summernote-de-CH.js
    summernote-de-DE.js
    summernote-el-GR.js
    summernote-es-ES.js
    summernote-es-EU.js
    summernote-fa-IR.js
    summernote-fi-FI.js
    summernote-fr-FR.js
    summernote-gl-ES.js
    summernote-he-IL.js
    summernote-hr-HR.js
    summernote-hu-HU.js
    summernote-id-ID.js
    summernote-it-IT.js
    summernote-ja-JP.js
    summernote-ko-KR.js
    … 23 more files
  plugin/  (4 files)
    databasic/  (2 files)
      … 2 files under this directory
    hello/  (1 files)
      … 1 files under this directory
    specialchars/  (1 files)
      … 1 files under this directory
scripts/  (3 files)
  vite-plugins/  (1 files)
    vitePostCSSSourceMap.mjs
  build-all.js
  build-fonts.js
src/  (133 files)
  font/  (58 files)
    icons/  (56 files)
      … 56 files under this directory
    summernote.hash
    template.scss
  js/  (39 files)
    core/  (7 files)
      … 7 files under this directory
    editing/  (5 files)
      … 5 files under this directory
    module/  (22 files)
      … 22 files under this directory
    Context.js
    renderer.js
    settings.js
    summernote-en-US.js
    summernote.js
  styles/  (36 files)
    bs3/  (4 files)
      … 4 files under this directory
    bs4/  (4 files)
      … 4 files under this directory
    bs5/  (4 files)
      … 4 files under this directory
    lite/  (19 files)
      … 19 files under this directory
    summernote/  (4 files)
      … 4 files under this directory
    README.md
test/  (19 files)
  base/  (17 files)
    core/  (5 files)
      … 5 files under this directory
    editing/  (3 files)
      … 3 files under this directory
    module/  (8 files)
      … 8 files under this directory
    Context.spec.js
  util.js
  vitest.setup.js
.babelrc
.editorconfig
.eslintrc
.gitignore
.npmignore
.prettierrc.js
.yarnrc.yml
CHANGES.md
LICENSE
MAINTAINING.md
README.md
index.html
package.json
vite.config.dev.js
vite.config.js
vitest.config.js
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| js package | library | Observed | Groups 32 file(s) under js package (observed from repository paths and static analysis). |
| public package | library | Observed | Groups 49 file(s) under public package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 3 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 7 file(s) under service / domain layer (observed from repository paths and static analysis). |
| styles package | library | Observed | Groups 7 file(s) under styles package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 19 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/ISSUE_TEMPLATE/improve_documentation.yml` (config)
- `.github/workflows/build.yml` (ci)
- `.github/workflows/codeql-analysis.yml` (ci)
- `.github/workflows/npm-publish.yml` (ci)
- `.yarnrc.yml` (config)
- `examples/symbols_mathematical-symbols_Greek-letters.json` (config)
- `package.json` (manifest)
- `src/styles/bs3/summernote-bs3.json` (config)
- `src/styles/bs4/summernote-bs4.json` (config)
- `src/styles/bs5/summernote-bs5.json` (config)
- `src/styles/lite/summernote-lite.json` (config)

## Top-level layout

- `src` — 133 analysed file(s)
- `public` — 52 analysed file(s)
- `examples` — 29 analysed file(s)
- `test` — 19 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `.github` — 12 analysed file(s)
- `scripts` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `ac5460e0e9a0b622ad7deff162915a3960ff4b96` is the revision these paths and observations refer to.
