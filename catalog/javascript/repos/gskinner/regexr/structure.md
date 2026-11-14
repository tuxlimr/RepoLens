# Project structure: gskinner/regexr

**Analysed commit:** `d18630d02372b38614f220576bd1888326cf8e78`

**Commit reference:** [d18630d02372b38614f220576bd1888326cf8e78](https://github.com/gskinner/regexr/commit/d18630d02372b38614f220576bd1888326cf8e78)

**Tree at this commit:** [gskinner/regexr@d18630d02372](https://github.com/gskinner/regexr/tree/d18630d02372b38614f220576bd1888326cf8e78)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | gskinner/regexr |
| Description | RegExr is a HTML/JS based tool for creating, testing, and learning about Regular Expressions. |
| Stars | 10388 |
| Forks | 1002 |
| Licence | GPL-3.0 |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `d18630d02372b38614f220576bd1888326cf8e78` |
| Retrieved at | 2026-11-14T19:12:40.976123+00:00 |
| Files in this snapshot | 152 |

## Directory tree

```text
assets/  (7 files)
  icons/  (3 files)
    browserconfig.xml
    safari-pinned-tab.svg
    site.webmanifest
  themes/  (2 files)
    dark.css
    light.css
  workers/  (1 files)
    RegExWorker.js
  privacy.html
dev/  (100 files)
  icons/  (30 files)
    RegExr.svg
    add.svg
    alert.svg
    arrowleft.svg
    arrowright.svg
    cheatsheet.svg
    check.svg
    close.svg
    code.svg
    community.svg
    copy.svg
    delete.svg
    distractor.svg
    dropdown.svg
    favorites.svg
    flags.svg
    github.svg
    google.svg
    help.svg
    info.svg
    link.svg
    load.svg
    menu.svg
    moon.svg
    … 6 more files
  inject/  (1 files)
    icons.svg
  lib/  (3 files)
    clipboard.js
    codemirror.css
    native.js
  sass/  (22 files)
    views/  (11 files)
      … 11 files under this directory
    codemirror.scss
    colors.scss
    colors_dark.scss
    colors_light.scss
    controls.scss
    export.scss
    fonts.scss
    mobile.scss
    regexr.scss
    styles.scss
    variables.scss
  src/  (44 files)
    controls/  (4 files)
      … 4 files under this directory
    docs/  (3 files)
      … 3 files under this directory
    events/  (2 files)
      … 2 files under this directory
    helpers/  (3 files)
      … 3 files under this directory
    net/  (1 files)
      … 1 files under this directory
    profiles/  (4 files)
      … 4 files under this directory
    utils/  (5 files)
      … 5 files under this directory
    views/  (16 files)
      … 16 files under this directory
    ExpressionLexer.js
    Flavor.js
    RefCoverage.js
    RegExr.js
    SubstLexer.js
    app.js
server/  (34 files)
  actions/  (14 files)
    account/  (4 files)
      … 4 files under this directory
    patterns/  (8 files)
      … 8 files under this directory
    regex/  (1 files)
      … 1 files under this directory
    oauthCallback.php
  core/  (11 files)
    API.php
    APIError.php
    AbstractAction.php
    Authentication.php
    Cache.php
    DB.php
    ErrorCodes.php
    NotImplemented.php
    PatternVisibility.php
    Result.php
    Session.php
  .editorconfig
  Config.sample.php
  Maintenance.php
  api.php
  apiDocs.php
  bootstrap.php
  composer.json
  schema.sql
  utils.php
.editorconfig
.gitattributes
.gitignore
.htaccess
.nvmrc
LICENSE
README.md
gulpfile.babel.js
index.html
index.php
package.json
```

## Entry points

- [dev/src/app.js](https://github.com/gskinner/regexr/blob/d18630d02372b38614f220576bd1888326cf8e78/dev/src/app.js)
- [dev/src/net/Server.js](https://github.com/gskinner/regexr/blob/d18630d02372b38614f220576bd1888326cf8e78/dev/src/net/Server.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 16 file(s) under api layer (observed from repository paths and static analysis). |
| assets package | library | Observed | Groups 1 file(s) under assets package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| dev package | library | Observed | Groups 27 file(s) under dev package (observed from repository paths and static analysis). |
| server package | library | Observed | Groups 20 file(s) under server package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 11 file(s) under service / domain layer (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `package.json` (manifest)
- `server/.editorconfig` (config)
- `server/composer.json` (config)

## Top-level layout

- `dev` — 100 analysed file(s)
- `server` — 34 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `assets` — 7 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `d18630d02372b38614f220576bd1888326cf8e78` is the revision these paths and observations refer to.
