# Project structure: nosir/cleave.js

**Analysed commit:** `a966c95cf5193f223485a10eec8405bb32b8f6dd`

**Commit reference:** [a966c95cf5193f223485a10eec8405bb32b8f6dd](https://github.com/nosir/cleave.js/commit/a966c95cf5193f223485a10eec8405bb32b8f6dd)

**Tree at this commit:** [nosir/cleave.js@a966c95cf519](https://github.com/nosir/cleave.js/tree/a966c95cf5193f223485a10eec8405bb32b8f6dd)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | nosir/cleave.js |
| Description | Format input text content when you are typing... |
| Stars | 17835 |
| Forks | 1557 |
| Licence | Apache-2.0 |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `a966c95cf5193f223485a10eec8405bb32b8f6dd` |
| Retrieved at | 2026-11-14T19:11:23.759653+00:00 |
| Files in this snapshot | 232 |

## Directory tree

```text
doc/  (10 files)
  angularjs-directive-usage.md
  constructor.md
  doc.md
  js-api.md
  not-in-the-plan.md
  options.md
  phone-lib-addon.md
  public-methods.md
  reactjs-component-usage.md
  vue.md
gulp-tasks/  (6 files)
  addon.js
  browserify.js
  build.js
  rollup.js
  test.js
  webpack.js
src/  (203 files)
  addons/  (197 files)
    phone-type-formatter.ac.js
    phone-type-formatter.ad.js
    phone-type-formatter.ae.js
    phone-type-formatter.af.js
    phone-type-formatter.ag.js
    phone-type-formatter.ai.js
    phone-type-formatter.al.js
    phone-type-formatter.am.js
    phone-type-formatter.ao.js
    phone-type-formatter.ar.js
    phone-type-formatter.as.js
    phone-type-formatter.at.js
    phone-type-formatter.au-cn.js
    phone-type-formatter.au.js
    phone-type-formatter.aw.js
    phone-type-formatter.ax.js
    phone-type-formatter.az.js
    phone-type-formatter.ba.js
    phone-type-formatter.bb.js
    phone-type-formatter.bd.js
    phone-type-formatter.be.js
    phone-type-formatter.bf.js
    phone-type-formatter.bg.js
    phone-type-formatter.bh.js
    … 173 more files
  common/  (1 files)
    DefaultProperties.js
  shortcuts/  (2 files)
    CreditCardDetector.js
    PhoneFormatter.js
  Cleave.angular.js
  Cleave.js
  Cleave.react.js
test/  (1 files)
  browser/  (1 files)
    phone.js
.eslintignore
.eslintrc.js
.gitignore
.travis.yml
ISSUE_TEMPLATE
LICENSE
README.md
bower.json
codacy.json
gulpfile.js
package.json
react.js
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| addons package | library | Observed | Groups 197 file(s) under addons package (observed from repository paths and static analysis). |
| Cleave.angular.js package | library | Observed | Groups 1 file(s) under cleave.angular.js package (observed from repository paths and static analysis). |
| Cleave.js package | library | Observed | Groups 1 file(s) under cleave.js package (observed from repository paths and static analysis). |
| Cleave.react.js package | library | Observed | Groups 1 file(s) under cleave.react.js package (observed from repository paths and static analysis). |
| common package | library | Observed | Groups 1 file(s) under common package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| gulp-tasks package | library | Observed | Groups 6 file(s) under gulp-tasks package (observed from repository paths and static analysis). |
| shortcuts package | library | Observed | Groups 2 file(s) under shortcuts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.travis.yml` (ci)
- `bower.json` (config)
- `codacy.json` (config)
- `package.json` (manifest)

## Top-level layout

- `src` — 203 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `doc` — 10 analysed file(s)
- `gulp-tasks` — 6 analysed file(s)
- `test` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 252 file(s) were skipped during inventory (252 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `a966c95cf5193f223485a10eec8405bb32b8f6dd` is the revision these paths and observations refer to.
