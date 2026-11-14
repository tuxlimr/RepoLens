# Project structure: PrismJS/prism

**Analysed commit:** `59759136a1da88be0c54d98ed3152ec8135ce905`

**Commit reference:** [59759136a1da88be0c54d98ed3152ec8135ce905](https://github.com/PrismJS/prism/commit/59759136a1da88be0c54d98ed3152ec8135ce905)

**Tree at this commit:** [PrismJS/prism@59759136a1da](https://github.com/PrismJS/prism/tree/59759136a1da88be0c54d98ed3152ec8135ce905)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | PrismJS/prism |
| Description | Lightweight, robust, elegant syntax highlighting. |
| Stars | 13068 |
| Forks | 1411 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | v2 |
| Analysed commit | `59759136a1da88be0c54d98ed3152ec8135ce905` |
| Retrieved at | 2026-11-14T19:12:01.236016+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.github/  (9 files)
  ISSUE_TEMPLATE/  (5 files)
    bug_report.md
    config.yml
    feature_request.md
    highlighting-bug-report.md
    new-language-request.md
  workflows/  (3 files)
    autofix.yml
    test.yml
    website-rebuild.yml
  dependabot.yml
.husky/  (1 files)
  pre-commit
.vscode/  (1 files)
  settings.json
benchmark/  (2 files)
  benchmark.js
  config.js
scripts/  (4 files)
  build.js
  create-changelog.js
  linkify-changelog.js
  tasks.js
src/  (439 files)
  core/  (20 files)
    classes/  (9 files)
      … 9 files under this directory
    tokenize/  (4 files)
      … 4 files under this directory
    highlight-all.js
    highlight-element.js
    highlight.js
    linked-list.js
    prism.js
    registry.js
    stringify.js
  languages/  (309 files)
    abap.js
    abnf.js
    actionscript.js
    ada.js
    agda.js
    al.js
    antlr4.js
    apacheconf.js
    apex.js
    apl.js
    applescript.js
    aql.js
    arduino.js
    arff.js
    armasm.js
    arturo.js
    asciidoc.js
    asm6502.js
    asmatmel.js
    aspnet.js
    autohotkey.js
    autoit.js
    avisynth.js
    avro-idl.js
    … 285 more files
  plugins/  (74 files)
    autolinker/  (3 files)
      … 3 files under this directory
    autoloader/  (3 files)
      … 3 files under this directory
    command-line/  (3 files)
      … 3 files under this directory
    copy-to-clipboard/  (2 files)
      … 2 files under this directory
    custom-class/  (2 files)
      … 2 files under this directory
    data-uri-highlight/  (2 files)
      … 2 files under this directory
    download-button/  (2 files)
      … 2 files under this directory
    file-highlight/  (2 files)
      … 2 files under this directory
    filter-highlight-all/  (3 files)
      … 3 files under this directory
    highlight-keywords/  (2 files)
      … 2 files under this directory
    inline-color/  (3 files)
      … 3 files under this directory
    jsonp-highlight/  (3 files)
      … 3 files under this directory
    keep-markup/  (2 files)
      … 2 files under this directory
    line-highlight/  (3 files)
      … 3 files under this directory
    line-numbers/  (3 files)
      … 3 files under this directory
    match-braces/  (3 files)
      … 3 files under this directory
    normalize-whitespace/  (3 files)
      … 3 files under this directory
    previewers/  (3 files)
      … 3 files under this directory
    show-invisibles/  (3 files)
      … 3 files under this directory
    show-language/  (2 files)
      … 2 files under this directory
    toolbar/  (4 files)
      … 4 files under this directory
    treeview-icons/  (15 files)
      … 15 files under this directory
    unescaped-markup/  (3 files)
      … 3 files under this directory
  shared/  (8 files)
    languages/  (2 files)
      … 2 files under this directory
    meta/  (3 files)
      … 3 files under this directory
    dom-util.js
    tokenize-strings.js
    util.js
  themes/  (8 files)
    coy.css
    dark.css
    funky.css
    okaidia.css
    prism.css
    solarizedlight.css
    tomorrow.css
    twilight.css
  util/  (11 files)
    async.js
    combine-callbacks.js
    extend.js
    grammar-patch.js
    insert.js
    iterables.js
    language-id.js
    language-util.js
    objects.js
    token-stream.js
    without-tokenize.js
  auto-start.js
  components.json
  config.js
  core.js
  global.js
  index.js
  load-languages.js
  shared.js
  types.d.ts
tests/  (328 files)
  core/  (8 files)
    __snapshots__/  (1 files)
      … 1 files under this directory
    document-ready.js
    embedding.js
    greedy.js
    highlight-all.js
    hooks.js
    registry.js
    token-stream.js
  helper/  (8 files)
    args.js
    prism-dom-util.js
    prism-loader.js
    snapshot.js
    test-case.js
    test-discovery.js
    token-stream-transformer.js
    util.js
  languages/  (309 files)
    abap/  (7 files)
      … 7 files under this directory
    abnf/  (10 files)
      … 10 files under this directory
    actionscript/  (2 files)
      … 2 files under this directory
    ada/  (10 files)
      … 10 files under this directory
    agda/  (5 files)
      … 5 files under this directory
    al/  (8 files)
      … 8 files under this directory
    antlr4/  (10 files)
      … 10 files under this directory
    apacheconf/  (7 files)
      … 7 files under this directory
    apex/  (10 files)
      … 10 files under this directory
    apl/  (11 files)
      … 11 files under this directory
    applescript/  (7 files)
      … 7 files under this directory
    aql/  (9 files)
      … 9 files under this directory
    arduino/  (3 files)
      … 3 files under this directory
    arff/  (4 files)
      … 4 files under this directory
    armasm/  (11 files)
      … 11 files under this directory
    arturo/  (16 files)
      … 16 files under this directory
    arturo!+bash/  (1 files)
      … 1 files under this directory
    arturo!+css/  (1 files)
      … 1 files under this directory
    arturo!+javascript/  (1 files)
      … 1 files under this directory
    arturo!+markdown/  (1 files)
      … 1 files under this directory
    arturo!+markup/  (1 files)
      … 1 files under this directory
    arturo!+sql/  (1 files)
      … 1 files under this directory
    asciidoc/  (23 files)
      … 23 files under this directory
    asm6502/  (7 files)
      … 7 files under this directory
    asmatmel/  (8 files)
      … 8 files under this directory
    aspnet/  (2 files)
      … 2 files under this directory
    autohotkey/  (15 files)
      … 15 files under this directory
    autoit/  (10 files)
      … 10 files under this directory
    avisynth/  (8 files)
      … 8 files under this directory
    avro-idl/  (9 files)
      … 9 files under this directory
    awk/  (9 files)
      … 9 files under this directory
    bash/  (19 files)
      … 19 files under this directory
    basic/  (7 files)
      … 7 files under this directory
    batch/  (4 files)
      … 4 files under this directory
    bbcode/  (1 files)
      … 1 files under this directory
    bbj/  (7 files)
      … 7 files under this directory
    bicep/  (11 files)
      … 11 files under this directory
    birb/  (6 files)
      … 6 files under this directory
    bison/  (7 files)
      … 7 files under this directory
    bnf/  (4 files)
      … 4 files under this directory
    bqn/  (6 files)
      … 6 files under this directory
    brainfuck/  (1 files)
      … 1 files under this directory
    brightscript/  (9 files)
      … 9 files under this directory
  components-test.js
  coverage.js
  identifier-test.js
.editorconfig
.gitattributes
.gitignore
.jsdoc.json
.npmignore
.prettierignore
.prettierrc.js
CNAME
LICENSE
MAINTAINERS.md
README.md
SECURITY.md
_headers
composer.json
eslint.config.mjs
package.json
```

## Entry points

- [src/index.js](https://github.com/PrismJS/prism/blob/59759136a1da88be0c54d98ed3152ec8135ce905/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| auto-start.js package | library | Observed | Groups 1 file(s) under auto-start.js package (observed from repository paths and static analysis). |
| benchmark package | library | Observed | Groups 2 file(s) under benchmark package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| config.js package | library | Observed | Groups 1 file(s) under config.js package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| core.js package | library | Observed | Groups 1 file(s) under core.js package (observed from repository paths and static analysis). |
| global.js package | library | Observed | Groups 1 file(s) under global.js package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| languages package | library | Observed | Groups 309 file(s) under languages package (observed from repository paths and static analysis). |
| load-languages.js package | library | Observed | Groups 1 file(s) under load-languages.js package (observed from repository paths and static analysis). |
| plugins package | library | Observed | Groups 27 file(s) under plugins package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 4 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 20 file(s) under service / domain layer (observed from repository paths and static analysis). |
| shared package | library | Observed | Groups 8 file(s) under shared package (observed from repository paths and static analysis). |
| shared.js package | library | Observed | Groups 1 file(s) under shared.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 328 file(s) under tests (observed from repository paths and static analysis). |
| types.d.ts package | library | Observed | Groups 1 file(s) under types.d.ts package (observed from repository paths and static analysis). |
| util package | library | Observed | Groups 11 file(s) under util package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/autofix.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `.github/workflows/website-rebuild.yml` (ci)
- `.jsdoc.json` (config)
- `.vscode/settings.json` (config)
- `composer.json` (config)
- `package.json` (manifest)
- `src/components.json` (config)

## Top-level layout

- `src` — 439 analysed file(s)
- `tests` — 328 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `.github` — 9 analysed file(s)
- `scripts` — 4 analysed file(s)
- `benchmark` — 2 analysed file(s)
- `.husky` — 1 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `59759136a1da88be0c54d98ed3152ec8135ce905` is the revision these paths and observations refer to.
