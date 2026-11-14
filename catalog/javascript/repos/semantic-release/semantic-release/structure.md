# Project structure: semantic-release/semantic-release

**Analysed commit:** `04c1923646eb801cf6f0f90455cf00b78b94fdb7`

**Commit reference:** [04c1923646eb801cf6f0f90455cf00b78b94fdb7](https://github.com/semantic-release/semantic-release/commit/04c1923646eb801cf6f0f90455cf00b78b94fdb7)

**Tree at this commit:** [semantic-release/semantic-release@04c1923646eb](https://github.com/semantic-release/semantic-release/tree/04c1923646eb801cf6f0f90455cf00b78b94fdb7)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | semantic-release/semantic-release |
| Description | 📦🚀 Fully automated version management and package publishing |
| Stars | 24169 |
| Forks | 1806 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `04c1923646eb801cf6f0f90455cf00b78b94fdb7` |
| Retrieved at | 2026-11-14T19:11:03.173958+00:00 |
| Files in this snapshot | 85 |

## Directory tree

```text
.github/  (7 files)
  ISSUE_TEMPLATE/  (4 files)
    01_bug_report.yml
    02_feature_request.yml
    03_plugin_suggestion.yml
    config.yml
  workflows/  (3 files)
    release.yml
    scorecard.yml
    test.yml
bin/  (1 files)
  semantic-release.js
lib/  (24 files)
  branches/  (4 files)
    expand.js
    get-tags.js
    index.js
    normalize.js
  definitions/  (4 files)
    branches.js
    constants.js
    errors.js
    plugins.js
  plugins/  (4 files)
    index.js
    normalize.js
    pipeline.js
    utils.js
  get-commits.js
  get-config.js
  get-error.js
  get-git-auth-url.js
  get-last-release.js
  get-logger.js
  get-next-version.js
  get-release-to-add.js
  git.js
  hide-sensitive.js
  utils.js
  verify.js
media/  (1 files)
  semantic-release-logo.svg
test/  (39 files)
  branches/  (4 files)
    branches.test.js
    expand.test.js
    get-tags.test.js
    normalize.test.js
  definitions/  (3 files)
    branches.test.js
    errors.test.js
    plugins.test.js
  fixtures/  (10 files)
    index.js
    multi-plugin.cjs
    plugin-error-inherited.js
    plugin-error.js
    plugin-errors.js
    plugin-esm-named-exports.js
    plugin-identity.js
    plugin-log-env.js
    plugin-noop.cjs
    plugin-result-config.js
  helpers/  (4 files)
    config.yaml
    e2e-environment.js
    git-utils.js
    npm-utils.js
  plugins/  (4 files)
    normalize.test.js
    pipeline.test.js
    plugins.test.js
    utils.test.js
  cli.test.js
  e2e.test.js
  get-commits.test.js
  get-config.test.js
  get-git-auth-url.test.js
  get-last-release.test.js
  get-logger.test.js
  get-next-version.test.js
  get-release-to-add.test.js
  git.test.js
  hide-sensitive.test.js
  integration.test.js
  utils.test.js
  verify.test.js
.git-blame-ignore-revs
.gitattributes
.gitignore
.nvmrc
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
cli.js
e2e.compose.yml
index.d.ts
index.js
package.json
```

## Entry points

- [index.js](https://github.com/semantic-release/semantic-release/blob/04c1923646eb801cf6f0f90455cf00b78b94fdb7/index.js)
- [bin/semantic-release.js](https://github.com/semantic-release/semantic-release/blob/04c1923646eb801cf6f0f90455cf00b78b94fdb7/bin/semantic-release.js)
- [lib/branches/index.js](https://github.com/semantic-release/semantic-release/blob/04c1923646eb801cf6f0f90455cf00b78b94fdb7/lib/branches/index.js)
- [lib/plugins/index.js](https://github.com/semantic-release/semantic-release/blob/04c1923646eb801cf6f0f90455cf00b78b94fdb7/lib/plugins/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bin package | library | Observed | Groups 1 file(s) under bin package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 24 file(s) under lib package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 39 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/ISSUE_TEMPLATE/01_bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/02_feature_request.yml` (config)
- `.github/ISSUE_TEMPLATE/03_plugin_suggestion.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/scorecard.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `e2e.compose.yml` (config)
- `package.json` (manifest)

## Top-level layout

- `test` — 39 analysed file(s)
- `lib` — 24 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `.github` — 7 analysed file(s)
- `bin` — 1 analysed file(s)
- `media` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `04c1923646eb801cf6f0f90455cf00b78b94fdb7` is the revision these paths and observations refer to.
