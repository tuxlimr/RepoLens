# Project structure: feathericons/feather

**Analysed commit:** `3dc050d97405062eba78aa57115c0a15c63abdaa`

**Commit reference:** [3dc050d97405062eba78aa57115c0a15c63abdaa](https://github.com/feathericons/feather/commit/3dc050d97405062eba78aa57115c0a15c63abdaa)

**Tree at this commit:** [feathericons/feather@3dc050d97405](https://github.com/feathericons/feather/tree/3dc050d97405062eba78aa57115c0a15c63abdaa)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | feathericons/feather |
| Description | Simply beautiful open-source icons |
| Stars | 26040 |
| Forks | 1281 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `3dc050d97405062eba78aa57115c0a15c63abdaa` |
| Retrieved at | 2026-11-14T19:10:55.445428+00:00 |
| Files in this snapshot | 343 |

## Directory tree

```text
.changeset/  (2 files)
  README.md
  config.json
.github/  (5 files)
  ISSUE_TEMPLATE/  (2 files)
    01-icon-request.yml
    02-bug-report.yml
  workflows/  (2 files)
    ci.yml
    release.yml
  CODEOWNERS
bin/  (16 files)
  __tests__/  (6 files)
    __snapshots__/  (3 files)
      … 3 files under this directory
    build-icons-object.test.js
    build-sprite-string.test.js
    optimize-svg.test.js
  .eslintrc.json
  build-icons-json.js
  build-icons-object.js
  build-sprite-string.js
  build-sprite.js
  build-svgs.js
  build.sh
  optimize-svg.js
  optimize-svgs.js
  setup.sh
examples/  (1 files)
  index.html
icons/  (287 files)
  activity.svg
  airplay.svg
  alert-circle.svg
  alert-octagon.svg
  alert-triangle.svg
  align-center.svg
  align-justify.svg
  align-left.svg
  align-right.svg
  anchor.svg
  aperture.svg
  archive.svg
  arrow-down-circle.svg
  arrow-down-left.svg
  arrow-down-right.svg
  arrow-down.svg
  arrow-left-circle.svg
  arrow-left.svg
  arrow-right-circle.svg
  arrow-right.svg
  arrow-up-circle.svg
  arrow-up-left.svg
  arrow-up-right.svg
  arrow-up.svg
  … 263 more files
src/  (18 files)
  __tests__/  (11 files)
    __snapshots__/  (5 files)
      … 5 files under this directory
    icon.test.js
    icons.test.js
    index.test.js
    replace.node.test.js
    replace.test.js
    to-svg.test.js
  default-attrs.json
  icon.js
  icons.js
  index.js
  replace.js
  tags.json
  to-svg.js
.babelrc
.eslintignore
.eslintrc.js
.gitignore
.lintstagedrc
.prettierignore
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
commitlint.config.js
package.json
webpack.config.js
```

## Entry points

- [src/index.js](https://github.com/feathericons/feather/blob/3dc050d97405062eba78aa57115c0a15c63abdaa/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bin package | library | Observed | Groups 12 file(s) under bin package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| icon.js package | library | Observed | Groups 1 file(s) under icon.js package (observed from repository paths and static analysis). |
| icons.js package | library | Observed | Groups 1 file(s) under icons.js package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| replace.js package | library | Observed | Groups 1 file(s) under replace.js package (observed from repository paths and static analysis). |
| __tests__ package | library | Observed | Groups 6 file(s) under __tests__ package (observed from repository paths and static analysis). |
| to-svg.js package | library | Observed | Groups 1 file(s) under to-svg.js package (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.github/ISSUE_TEMPLATE/01-icon-request.yml` (config)
- `.github/ISSUE_TEMPLATE/02-bug-report.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `bin/.eslintrc.json` (config)
- `package.json` (manifest)
- `src/default-attrs.json` (config)
- `src/tags.json` (config)

## Top-level layout

- `icons` — 287 analysed file(s)
- `src` — 18 analysed file(s)
- `bin` — 16 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `.github` — 5 analysed file(s)
- `.changeset` — 2 analysed file(s)
- `examples` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `3dc050d97405062eba78aa57115c0a15c63abdaa` is the revision these paths and observations refer to.
