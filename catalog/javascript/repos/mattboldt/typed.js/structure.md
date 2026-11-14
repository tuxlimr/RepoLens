# Project structure: mattboldt/typed.js

**Analysed commit:** `b2d6a7d9af6d9cd39830701f6b6a7cd98a37e13f`

**Commit reference:** [b2d6a7d9af6d9cd39830701f6b6a7cd98a37e13f](https://github.com/mattboldt/typed.js/commit/b2d6a7d9af6d9cd39830701f6b6a7cd98a37e13f)

**Tree at this commit:** [mattboldt/typed.js@b2d6a7d9af6d](https://github.com/mattboldt/typed.js/tree/b2d6a7d9af6d9cd39830701f6b6a7cd98a37e13f)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | mattboldt/typed.js |
| Description | A JavaScript Typing Animation Library |
| Stars | 16272 |
| Forks | 1737 |
| Licence | Other |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `b2d6a7d9af6d9cd39830701f6b6a7cd98a37e13f` |
| Retrieved at | 2026-11-14T19:11:33.544101+00:00 |
| Files in this snapshot | 75 |

## Directory tree

```text
.github/  (4 files)
  CONTRIBUTING.md
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
  stale.yml
.vscode/  (2 files)
  launch.json
  settings.json
assets/  (2 files)
  demos.css
  demos.js
docs/  (49 files)
  assets/  (10 files)
    fonts/  (2 files)
      … 2 files under this directory
    anchor.js
    bass-addons.css
    bass.css
    github.css
    site.js
    split.css
    split.js
    style.css
  ast/  (1 files)
    source/  (1 files)
      … 1 files under this directory
  class/  (4 files)
    src/  (4 files)
      … 4 files under this directory
  css/  (8 files)
    github.css
    identifiers.css
    manual.css
    prettify-tomorrow.css
    search.css
    source.css
    style.css
    test.css
  file/  (5 files)
    src/  (5 files)
      … 5 files under this directory
  image/  (2 files)
    badge.svg
    manual-badge.svg
  script/  (10 files)
    prettify/  (2 files)
      … 2 files under this directory
    inherited-summary.js
    inner-link.js
    manual.js
    patch-for-local.js
    pretty-print.js
    search.js
    search_index.js
    test-summary.js
  variable/  (1 files)
    index.html
  API.md
  badge.svg
  coverage.json
  identifiers.html
  index.html
  index.json
  lint.json
  source.html
src/  (4 files)
  defaults.js
  html-parser.js
  initializer.js
  typed.js
.codeclimate.yml
.esdoc.json
.gitignore
.prettierrc
.travis.yml
CODE_OF_CONDUCT.md
LICENSE.txt
LIMITED_COMMERCIAL_LICENSE.md
README.md
UNLIMITED_COMMERCIAL_LICENSE.md
index.d.ts
index.html
package.json
typed.d.ts
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| assets package | library | Observed | Groups 1 file(s) under assets package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| defaults.js package | library | Observed | Groups 1 file(s) under defaults.js package (observed from repository paths and static analysis). |
| html-parser.js package | library | Observed | Groups 1 file(s) under html-parser.js package (observed from repository paths and static analysis). |
| initializer.js package | library | Observed | Groups 1 file(s) under initializer.js package (observed from repository paths and static analysis). |
| typed.js package | library | Observed | Groups 1 file(s) under typed.js package (observed from repository paths and static analysis). |

## Important files

- `.codeclimate.yml` (config)
- `.esdoc.json` (config)
- `.github/stale.yml` (config)
- `.travis.yml` (ci)
- `.vscode/launch.json` (config)
- `.vscode/settings.json` (config)
- `docs/ast/source/.external-ecmascript.js.json` (config)
- `docs/coverage.json` (config)
- `docs/index.json` (config)
- `docs/lint.json` (config)
- `package.json` (manifest)

## Top-level layout

- `docs` — 49 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `.github` — 4 analysed file(s)
- `src` — 4 analysed file(s)
- `.vscode` — 2 analysed file(s)
- `assets` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 3 file(s) were skipped during inventory (3 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `b2d6a7d9af6d9cd39830701f6b6a7cd98a37e13f` is the revision these paths and observations refer to.
