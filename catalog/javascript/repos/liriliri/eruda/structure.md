# Project structure: liriliri/eruda

**Analysed commit:** `0c55928fec802fb2102934c4b5928686178b467b`

**Commit reference:** [0c55928fec802fb2102934c4b5928686178b467b](https://github.com/liriliri/eruda/commit/0c55928fec802fb2102934c4b5928686178b467b)

**Tree at this commit:** [liriliri/eruda@0c55928fec80](https://github.com/liriliri/eruda/tree/0c55928fec802fb2102934c4b5928686178b467b)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | liriliri/eruda |
| Description | Console for mobile browsers |
| Stars | 21245 |
| Forks | 1399 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `0c55928fec802fb2102934c4b5928686178b467b` |
| Retrieved at | 2026-11-14T19:11:13.871494+00:00 |
| Files in this snapshot | 92 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (2 files)
    main.yml
    publish.yml
  FUNDING.yml
src/  (50 files)
  Console/  (2 files)
    Console.js
    Console.scss
  DevTools/  (3 files)
    DevTools.js
    DevTools.scss
    Tool.js
  Elements/  (5 files)
    CssStore.js
    Detail.js
    Elements.js
    Elements.scss
    util.js
  EntryBtn/  (2 files)
    EntryBtn.js
    EntryBtn.scss
  Info/  (3 files)
    Info.js
    Info.scss
    defInfo.js
  Network/  (4 files)
    Detail.js
    Network.js
    Network.scss
    util.js
  Resources/  (5 files)
    Cookie.js
    Resources.js
    Resources.scss
    Storage.js
    util.js
  Settings/  (2 files)
    Settings.js
    Settings.scss
  Snippets/  (4 files)
    Snippets.js
    Snippets.scss
    defSnippets.js
    searchText.scss
  Sources/  (2 files)
    Sources.js
    Sources.scss
  lib/  (8 files)
    chobitsu.js
    emitter.js
    empty.js
    evalCss.js
    logger.js
    micromark.js
    themes.js
    util.js
  style/  (7 files)
    icon.css
    icon.json
    luna.scss
    mixin.scss
    reset.scss
    style.scss
    variable.scss
  eruda.js
  index.js
  polyfill.js
test/  (26 files)
  boot.js
  console.html
  console.js
  data.json
  elements.html
  elements.js
  eruda.html
  eruda.js
  index.html
  info.html
  info.js
  init.js
  inline.html
  manual.html
  network.html
  network.js
  resources.html
  resources.js
  settings.html
  settings.js
  snippets.html
  snippets.js
  sources.html
  sources.js
  … 2 more files
.eustia.js
.gitattributes
.gitignore
.gitmodules
.prettierignore
.prettierrc.json
CHANGELOG.md
LICENSE
README.md
eruda.d.ts
eslint.config.mjs
karma.conf.js
package.json
```

## Entry points

- [src/index.js](https://github.com/liriliri/eruda/blob/0c55928fec802fb2102934c4b5928686178b467b/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Console package | library | Observed | Groups 1 file(s) under console package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| DevTools package | library | Observed | Groups 2 file(s) under devtools package (observed from repository paths and static analysis). |
| Elements package | library | Observed | Groups 4 file(s) under elements package (observed from repository paths and static analysis). |
| EntryBtn package | library | Observed | Groups 1 file(s) under entrybtn package (observed from repository paths and static analysis). |
| eruda.js package | library | Observed | Groups 1 file(s) under eruda.js package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| Info package | library | Observed | Groups 2 file(s) under info package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 8 file(s) under lib package (observed from repository paths and static analysis). |
| Network package | library | Observed | Groups 3 file(s) under network package (observed from repository paths and static analysis). |
| polyfill.js package | library | Observed | Groups 1 file(s) under polyfill.js package (observed from repository paths and static analysis). |
| Resources package | library | Observed | Groups 4 file(s) under resources package (observed from repository paths and static analysis). |
| Snippets package | library | Observed | Groups 2 file(s) under snippets package (observed from repository paths and static analysis). |
| Sources package | library | Observed | Groups 1 file(s) under sources package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 26 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/workflows/main.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.prettierrc.json` (config)
- `package.json` (manifest)
- `src/style/icon.json` (config)

## Top-level layout

- `src` — 50 analysed file(s)
- `test` — 26 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `.github` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 7 file(s) were skipped during inventory (7 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `0c55928fec802fb2102934c4b5928686178b467b` is the revision these paths and observations refer to.
