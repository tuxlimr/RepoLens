# Project structure: vuejs/vuepress

**Analysed commit:** `9fb4bb00925d9409e6732118e996411c6a82c85d`

**Commit reference:** [9fb4bb00925d9409e6732118e996411c6a82c85d](https://github.com/vuejs/vuepress/commit/9fb4bb00925d9409e6732118e996411c6a82c85d)

**Tree at this commit:** [vuejs/vuepress@9fb4bb00925d](https://github.com/vuejs/vuepress/tree/9fb4bb00925d9409e6732118e996411c6a82c85d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | vuejs/vuepress |
| Description | 📝 Minimalistic Vue-powered static site generator |
| Stars | 22716 |
| Forks | 4605 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `9fb4bb00925d9409e6732118e996411c6a82c85d` |
| Retrieved at | 2026-11-14T19:11:07.387745+00:00 |
| Files in this snapshot | 506 |

## Directory tree

```text
.dependabot/  (1 files)
  config.yml
.github/  (7 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (1 files)
    pull-request-ci.yml
  CONTRIBUTING.md
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
  semantic.yml
.vscode/  (2 files)
  extensions.json
  settings.json
__mocks__/  (18 files)
  @org/  (3 files)
    vuepress-theme-a/  (1 files)
      … 1 files under this directory
    vuepress-plugin-a.js
    vuepress-plugin-b.js
  @vuepress/  (2 files)
    theme-a/  (1 files)
      … 1 files under this directory
    plugin-a.js
  vuepress-theme-a/  (1 files)
    index.js
  vuepress-theme-child/  (3 files)
    components/  (1 files)
      … 1 files under this directory
    Layout.vue
    index.js
  vuepress-theme-parent/  (4 files)
    components/  (2 files)
      … 2 files under this directory
    Layout.vue
    index.js
  vuepress-theme-without-index/  (3 files)
    Layout.vue
    index.js
    package.json
  vuepress-plugin-a.js
  vuepress-plugin-b.js
art/  (1 files)
  vuepress-icon.svg
changelog/  (1 files)
  1.9.2.md
packages/  (453 files)
  @vuepress/  (330 files)
    core/  (98 files)
      … 98 files under this directory
    markdown/  (50 files)
      … 50 files under this directory
    markdown-loader/  (4 files)
      … 4 files under this directory
    plugin-active-header-links/  (5 files)
      … 5 files under this directory
    plugin-back-to-top/  (6 files)
      … 6 files under this directory
    plugin-google-analytics/  (5 files)
      … 5 files under this directory
    plugin-last-updated/  (4 files)
      … 4 files under this directory
    plugin-medium-zoom/  (6 files)
      … 6 files under this directory
    plugin-nprogress/  (7 files)
      … 7 files under this directory
    plugin-pwa/  (10 files)
      … 10 files under this directory
    plugin-register-components/  (4 files)
      … 4 files under this directory
    plugin-search/  (8 files)
      … 8 files under this directory
    shared-utils/  (44 files)
      … 44 files under this directory
    test-utils/  (15 files)
      … 15 files under this directory
    theme-default/  (38 files)
      … 38 files under this directory
    theme-vue/  (7 files)
      … 7 files under this directory
    types/  (19 files)
      … 19 files under this directory
  docs/  (113 files)
    docs/  (110 files)
      … 110 files under this directory
    .remarkrc
    .textlintrc.js
    package.json
  vuepress/  (10 files)
    lib/  (4 files)
      … 4 files under this directory
    README.md
    cli.js
    config.d.ts
    config.js
    index.js
    package.json
rfcs/  (3 files)
  002.plugin-git-log.md
  README.md
  template.md
scripts/  (4 files)
  bootstrap.js
  jest.config.js
  remote-version.js
  test.js
.all-contributorsrc
.commitlintrc.js
.editorconfig
.eslintignore
.eslintrc.js
.gitignore
.gitpod.yml
.npmignore
CHANGELOG.md
CODE_OF_CONDUCT.md
LICENSE
README.md
babel.config.js
lerna.json
package.json
tsconfig.json
```

## Entry points

- [__mocks__/vuepress-theme-without-index/Layout.vue](https://github.com/vuejs/vuepress/blob/9fb4bb00925d9409e6732118e996411c6a82c85d/__mocks__/vuepress-theme-without-index/Layout.vue)
- [packages/@vuepress/core/lib/index.js](https://github.com/vuejs/vuepress/blob/9fb4bb00925d9409e6732118e996411c6a82c85d/packages/%40vuepress/core/lib/index.js)
- [packages/@vuepress/markdown-loader/index.js](https://github.com/vuejs/vuepress/blob/9fb4bb00925d9409e6732118e996411c6a82c85d/packages/%40vuepress/markdown-loader/index.js)
- [packages/@vuepress/markdown/index.js](https://github.com/vuejs/vuepress/blob/9fb4bb00925d9409e6732118e996411c6a82c85d/packages/%40vuepress/markdown/index.js)
- [packages/@vuepress/plugin-active-header-links/index.js](https://github.com/vuejs/vuepress/blob/9fb4bb00925d9409e6732118e996411c6a82c85d/packages/%40vuepress/plugin-active-header-links/index.js)
- [packages/@vuepress/plugin-back-to-top/index.js](https://github.com/vuejs/vuepress/blob/9fb4bb00925d9409e6732118e996411c6a82c85d/packages/%40vuepress/plugin-back-to-top/index.js)
- [packages/@vuepress/plugin-google-analytics/index.js](https://github.com/vuejs/vuepress/blob/9fb4bb00925d9409e6732118e996411c6a82c85d/packages/%40vuepress/plugin-google-analytics/index.js)
- [packages/@vuepress/plugin-last-updated/index.js](https://github.com/vuejs/vuepress/blob/9fb4bb00925d9409e6732118e996411c6a82c85d/packages/%40vuepress/plugin-last-updated/index.js)
- [packages/@vuepress/plugin-medium-zoom/index.js](https://github.com/vuejs/vuepress/blob/9fb4bb00925d9409e6732118e996411c6a82c85d/packages/%40vuepress/plugin-medium-zoom/index.js)
- [packages/@vuepress/plugin-nprogress/index.js](https://github.com/vuejs/vuepress/blob/9fb4bb00925d9409e6732118e996411c6a82c85d/packages/%40vuepress/plugin-nprogress/index.js)
- [packages/@vuepress/plugin-pwa/index.js](https://github.com/vuejs/vuepress/blob/9fb4bb00925d9409e6732118e996411c6a82c85d/packages/%40vuepress/plugin-pwa/index.js)
- [packages/@vuepress/plugin-register-components/index.js](https://github.com/vuejs/vuepress/blob/9fb4bb00925d9409e6732118e996411c6a82c85d/packages/%40vuepress/plugin-register-components/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 27 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 21 file(s) under external integrations (observed from repository paths and static analysis). |
| __mocks__ package | library | Observed | Groups 17 file(s) under __mocks__ package (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 148 file(s) under packages package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 4 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 63 file(s) under service / domain layer (observed from repository paths and static analysis). |

## Important files

- `.dependabot/config.yml` (config)
- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/semantic.yml` (config)
- `.github/workflows/pull-request-ci.yml` (ci)
- `.gitpod.yml` (config)
- `.vscode/extensions.json` (config)
- `.vscode/settings.json` (config)
- `__mocks__/vuepress-theme-without-index/package.json` (manifest)
- `lerna.json` (config)
- `package.json` (manifest)
- `packages/@vuepress/core/package.json` (manifest)
- `packages/@vuepress/markdown-loader/package.json` (manifest)
- `packages/@vuepress/markdown/__tests__/fragments/Dockerfile` (container)
- `packages/@vuepress/markdown/package.json` (manifest)
- `packages/@vuepress/plugin-active-header-links/package.json` (manifest)
- `packages/@vuepress/plugin-back-to-top/package.json` (manifest)
- `packages/@vuepress/plugin-google-analytics/package.json` (manifest)
- `packages/@vuepress/plugin-last-updated/package.json` (manifest)
- `packages/@vuepress/plugin-medium-zoom/package.json` (manifest)
- `packages/@vuepress/plugin-nprogress/package.json` (manifest)
- `packages/@vuepress/plugin-pwa/package.json` (manifest)
- `packages/@vuepress/plugin-register-components/package.json` (manifest)
- `packages/@vuepress/plugin-search/package.json` (manifest)
- `packages/@vuepress/shared-utils/package.json` (manifest)
- `packages/@vuepress/shared-utils/tsconfig.json` (config)
- `packages/@vuepress/test-utils/package.json` (manifest)
- `packages/@vuepress/theme-default/package.json` (manifest)
- `packages/@vuepress/theme-vue/package.json` (manifest)
- `packages/@vuepress/types/package.json` (manifest)
- `packages/@vuepress/types/tsconfig.json` (config)
- `packages/docs/docs/.vuepress/public/manifest.json` (config)
- `packages/docs/package.json` (manifest)
- `packages/vuepress/package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `packages` — 453 analysed file(s)
- `__mocks__` — 18 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `.github` — 7 analysed file(s)
- `scripts` — 4 analysed file(s)
- `rfcs` — 3 analysed file(s)
- `.vscode` — 2 analysed file(s)
- `.dependabot` — 1 analysed file(s)
- `art` — 1 analysed file(s)
- `changelog` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (1 x file exceeds per-file size limit (200000 bytes); 1 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `9fb4bb00925d9409e6732118e996411c6a82c85d` is the revision these paths and observations refer to.
