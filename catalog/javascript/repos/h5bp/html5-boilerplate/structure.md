# Project structure: h5bp/html5-boilerplate

**Analysed commit:** `abc52d91fb7cb36c35b50a11aa76b19d2935d7fe`

**Commit reference:** [abc52d91fb7cb36c35b50a11aa76b19d2935d7fe](https://github.com/h5bp/html5-boilerplate/commit/abc52d91fb7cb36c35b50a11aa76b19d2935d7fe)

**Tree at this commit:** [h5bp/html5-boilerplate@abc52d91fb7c](https://github.com/h5bp/html5-boilerplate/tree/abc52d91fb7cb36c35b50a11aa76b19d2935d7fe)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | h5bp/html5-boilerplate |
| Description | A professional front-end template for building fast, robust, and adaptable web apps or sites. |
| Stars | 57679 |
| Forks | 12232 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `abc52d91fb7cb36c35b50a11aa76b19d2935d7fe` |
| Retrieved at | 2026-11-14T19:10:36.906677+00:00 |
| Files in this snapshot | 56 |

## Directory tree

```text
.github/  (17 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.yml
    config.yml
    feature_request.yml
  workflows/  (8 files)
    build-dist.yml
    codeql-analysis.yml
    dependency-review.yml
    ossf-scorecard.yml
    publish.yml
    push-to-template.yml
    spellcheck.yml
    test.yml
  CODE_OF_CONDUCT.md
  CONTRIBUTING.md
  PROPOSAL_GUIDELINES.md
  PULL_REQUEST_TEMPLATE.md
  SUPPORT.md
  dependabot.yml
.vscode/  (2 files)
  extensions.json
  settings.json
docs/  (9 files)
  TOC.md
  about-this-repo.md
  css.md
  extend.md
  faq.md
  html.md
  js.md
  misc.md
  usage.md
src/  (14 files)
  img/  (1 files)
    .gitkeep
  js/  (1 files)
    app.js
  .editorconfig
  .gitattributes
  .gitignore
  404.html
  icon.svg
  index.html
  package.json
  robots.txt
  site.webmanifest
  webpack.common.js
  webpack.config.dev.js
  webpack.config.prod.js
test/  (2 files)
  file_content.mjs
  file_existence.mjs
.cspell.json
.editorconfig
.gitattributes
.gitignore
.prettierignore
.prettierrc.json
CHANGELOG.md
LICENSE.txt
README.md
eslint.config.mjs
gulpfile.mjs
package.json
```

## Entry points

- [src/js/app.js](https://github.com/h5bp/html5-boilerplate/blob/abc52d91fb7cb36c35b50a11aa76b19d2935d7fe/src/js/app.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| js package | library | Observed | Groups 1 file(s) under js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 2 file(s) under tests (observed from repository paths and static analysis). |
| webpack.common.js package | library | Observed | Groups 1 file(s) under webpack.common.js package (observed from repository paths and static analysis). |
| webpack.config.dev.js package | library | Observed | Groups 1 file(s) under webpack.config.dev.js package (observed from repository paths and static analysis). |
| webpack.config.prod.js package | library | Observed | Groups 1 file(s) under webpack.config.prod.js package (observed from repository paths and static analysis). |

## Important files

- `.cspell.json` (config)
- `.editorconfig` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/build-dist.yml` (ci)
- `.github/workflows/codeql-analysis.yml` (ci)
- `.github/workflows/dependency-review.yml` (ci)
- `.github/workflows/ossf-scorecard.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.github/workflows/push-to-template.yml` (ci)
- `.github/workflows/spellcheck.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `.prettierrc.json` (config)
- `.vscode/extensions.json` (config)
- `.vscode/settings.json` (config)
- `package.json` (manifest)
- `src/.editorconfig` (config)
- `src/package.json` (manifest)

## Top-level layout

- `.github` — 17 analysed file(s)
- `src` — 14 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `docs` — 9 analysed file(s)
- `.vscode` — 2 analysed file(s)
- `test` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 20 file(s) were skipped during inventory (1 x likely secret file excluded; 1 x lockfile excluded; 18 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `abc52d91fb7cb36c35b50a11aa76b19d2935d7fe` is the revision these paths and observations refer to.
