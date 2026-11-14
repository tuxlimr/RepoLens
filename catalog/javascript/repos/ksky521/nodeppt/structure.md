# Project structure: ksky521/nodeppt

**Analysed commit:** `44f4babb6586d3d0f2dad830e9956a1e39507d47`

**Commit reference:** [44f4babb6586d3d0f2dad830e9956a1e39507d47](https://github.com/ksky521/nodeppt/commit/44f4babb6586d3d0f2dad830e9956a1e39507d47)

**Tree at this commit:** [ksky521/nodeppt@44f4babb6586](https://github.com/ksky521/nodeppt/tree/44f4babb6586d3d0f2dad830e9956a1e39507d47)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | ksky521/nodeppt |
| Description | This is probably the best web presentation tool so far! |
| Stars | 10329 |
| Forks | 2017 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `44f4babb6586d3d0f2dad830e9956a1e39507d47` |
| Retrieved at | 2026-11-14T19:12:41.471270+00:00 |
| Files in this snapshot | 170 |

## Directory tree

```text
.github/  (1 files)
  ISSUE_TEMPLATE.md
packages/  (151 files)
  nodeppt/  (8 files)
    __tests__/  (1 files)
      … 1 files under this directory
    bin/  (1 files)
      … 1 files under this directory
    commands/  (1 files)
      … 1 files under this directory
    lib/  (2 files)
      … 2 files under this directory
    .npmignore
    README.md
    package.json
  nodeppt-js/  (65 files)
    assets/  (57 files)
      … 57 files under this directory
    plugins/  (5 files)
      … 5 files under this directory
    .npmignore
    index.js
    package.json
  nodeppt-parser/  (45 files)
    __tests__/  (3 files)
      … 3 files under this directory
    lib/  (37 files)
      … 37 files under this directory
    template/  (1 files)
      … 1 files under this directory
    .npmignore
    defaults.js
    index.js
    package.json
  nodeppt-serve/  (17 files)
    commands/  (2 files)
      … 2 files under this directory
    config/  (5 files)
      … 5 files under this directory
    lib/  (2 files)
      … 2 files under this directory
    template/  (2 files)
      … 2 files under this directory
    .npmignore
    PluginAPI.js
    Service.js
    index.js
    options.js
    package.json
  nodeppt-shared-utils/  (16 files)
    lib/  (13 files)
      … 13 files under this directory
    .npmignore
    index.js
    package.json
site/  (10 files)
  public/  (1 files)
    background.js
  animation.md
  background.md
  classes.md
  component.md
  echarts.md
  index.md
  layout.md
  media.md
  mermaid.md
.editorconfig
.gitignore
.prettierrc
MIT-LICENSE.txt
README.md
gh-page.sh
lerna.json
package.json
```

## Entry points

- [packages/nodeppt-js/index.js](https://github.com/ksky521/nodeppt/blob/44f4babb6586d3d0f2dad830e9956a1e39507d47/packages/nodeppt-js/index.js)
- [packages/nodeppt-parser/index.js](https://github.com/ksky521/nodeppt/blob/44f4babb6586d3d0f2dad830e9956a1e39507d47/packages/nodeppt-parser/index.js)
- [packages/nodeppt-serve/index.js](https://github.com/ksky521/nodeppt/blob/44f4babb6586d3d0f2dad830e9956a1e39507d47/packages/nodeppt-serve/index.js)
- [packages/nodeppt-shared-utils/index.js](https://github.com/ksky521/nodeppt/blob/44f4babb6586d3d0f2dad830e9956a1e39507d47/packages/nodeppt-shared-utils/index.js)
- [packages/nodeppt/bin/nodeppt](https://github.com/ksky521/nodeppt/blob/44f4babb6586d3d0f2dad830e9956a1e39507d47/packages/nodeppt/bin/nodeppt)
- [packages/nodeppt-serve/config/app.js](https://github.com/ksky521/nodeppt/blob/44f4babb6586d3d0f2dad830e9956a1e39507d47/packages/nodeppt-serve/config/app.js)
- [packages/nodeppt-serve/template/main.js](https://github.com/ksky521/nodeppt/blob/44f4babb6586d3d0f2dad830e9956a1e39507d47/packages/nodeppt-serve/template/main.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 12 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 73 file(s) under packages package (observed from repository paths and static analysis). |
| site package | library | Observed | Groups 1 file(s) under site package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `lerna.json` (config)
- `package.json` (manifest)
- `packages/nodeppt-js/package.json` (manifest)
- `packages/nodeppt-parser/package.json` (manifest)
- `packages/nodeppt-serve/package.json` (manifest)
- `packages/nodeppt-shared-utils/package.json` (manifest)
- `packages/nodeppt/package.json` (manifest)

## Top-level layout

- `packages` — 151 analysed file(s)
- `site` — 10 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `44f4babb6586d3d0f2dad830e9956a1e39507d47` is the revision these paths and observations refer to.
