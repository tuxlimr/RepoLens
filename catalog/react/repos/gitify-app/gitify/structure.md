# Project structure: gitify-app/gitify

**Analysed commit:** `67c00229d77d09e0c7f7044da7c24b42b484dcb0`

**Commit reference:** [67c00229d77d09e0c7f7044da7c24b42b484dcb0](https://github.com/gitify-app/gitify/commit/67c00229d77d09e0c7f7044da7c24b42b484dcb0)

**Tree at this commit:** [gitify-app/gitify@67c00229d77d](https://github.com/gitify-app/gitify/tree/67c00229d77d09e0c7f7044da7c24b42b484dcb0)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | gitify-app/gitify |
| Description | Git notifications on your menu bar. Available on macOS, Windows & Linux. |
| Stars | 5398 |
| Forks | 299 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `67c00229d77d09e0c7f7044da7c24b42b484dcb0` |
| Retrieved at | 2026-11-14T19:14:21.613669+00:00 |
| Files in this snapshot | 635 |

## Directory tree

```text
.github/  (21 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.yml
    config.yml
    feature_request.yml
  scripts/  (1 files)
    notify-release-pull-requests.mjs
  workflows/  (11 files)
    build.yml
    ci.yml
    lint.yml
    milestone.yml
    publish.yml
    release.yml
    renovate.yml
    test.yml
    triage.yml
    website.yml
    zizmor.yml
  CODEOWNERS
  actionlint.yaml
  copilot-instructions.md
  labeler.yml
  release.yml
  zizmor.yml
.husky/  (1 files)
  pre-commit
.opencode/  (12 files)
  commands/  (6 files)
    opsx-apply.md
    opsx-archive.md
    opsx-explore.md
    opsx-propose.md
    opsx-sync.md
    opsx-update.md
  skills/  (6 files)
    openspec-apply-change/  (1 files)
      … 1 files under this directory
    openspec-archive-change/  (1 files)
      … 1 files under this directory
    openspec-explore/  (1 files)
      … 1 files under this directory
    openspec-propose/  (1 files)
      … 1 files under this directory
    openspec-sync-specs/  (1 files)
      … 1 files under this directory
    openspec-update-change/  (1 files)
      … 1 files under this directory
.vscode/  (2 files)
  extensions.json
  settings.json
assets/  (1 files)
  entitlements.mac.plist
openspec/  (1 files)
  config.yaml
scripts/  (9 files)
  afterPack.js
  afterSign.js
  check-en-locales.mjs
  check-t-defaults.mjs
  prepare-dev-electron.mjs
  validate-runtime-dependencies.mjs
  verifyFuses.js
  verifyPackagedDependencies.js
  visual.sh
src/  (564 files)
  __helpers__/  (5 files)
    README.md
    electron-log.setup.ts
    fail-on-act-warnings.setup.ts
    gitify-bridge.ts
    restore-test-spies.setup.ts
  main/  (51 files)
    handlers/  (15 files)
      … 15 files under this directory
    lifecycle/  (11 files)
      … 11 files under this directory
    badge.test.ts
    badge.ts
    ciDependencyCompatibility.test.ts
    config.test.ts
    config.ts
    events.test.ts
    events.ts
    icons.test.ts
    icons.ts
    index.test.ts
    index.ts
    menu.test.ts
    menu.ts
    notifications.test.ts
    notifications.ts
    ozone.test.ts
    ozone.ts
    update-manager.test.ts
    update-manager.ts
    updater.test.ts
    updater.ts
    utils.test.ts
    utils.ts
    zoom.test.ts
    … 1 more files
  preload/  (6 files)
    index.test.ts
    index.ts
    preload.d.ts
    types.ts
    utils.test.ts
    utils.ts
  renderer/  (493 files)
    __helpers__/  (6 files)
      … 6 files under this directory
    __mocks__/  (4 files)
      … 4 files under this directory
    components/  (178 files)
      … 178 files under this directory
    hooks/  (27 files)
      … 27 files under this directory
    i18n/  (5 files)
      … 5 files under this directory
    icons/  (10 files)
      … 10 files under this directory
    routes/  (41 files)
      … 41 files under this directory
    stores/  (15 files)
      … 15 files under this directory
    utils/  (197 files)
      … 197 files under this directory
    App.css
    App.test.tsx
    App.tsx
    constants.ts
    index.html
    index.tsx
    nav.ts
    router.test.ts
    router.tsx
    types.ts
  shared/  (9 files)
    constants.ts
    events.ts
    logger.test.ts
    logger.ts
    nativeNotifications.test.ts
    nativeNotifications.ts
    platform.test.ts
    platform.ts
    theme.ts
.env.template
.gitattributes
.gitignore
.nvmrc
.release-please-manifest.json
ARCHITECTURE.md
CHANGELOG.md
CONTRIBUTING.md
LICENSE
MAINTAINERS.md
README.md
codegen.ts
electron-builder.js
graphql.config.ts
i18next.config.ts
package.json
pnpm-workspace.yaml
release-please-config.json
renovate.json
sonar-project.properties
tailwind.config.mts
tsconfig.json
vite.config.mts
vitest.config.mts
```

## Entry points

- [src/main/handlers/app.ts](https://github.com/gitify-app/gitify/blob/67c00229d77d09e0c7f7044da7c24b42b484dcb0/src/main/handlers/app.ts)
- [src/main/handlers/index.ts](https://github.com/gitify-app/gitify/blob/67c00229d77d09e0c7f7044da7c24b42b484dcb0/src/main/handlers/index.ts)
- [src/main/index.ts](https://github.com/gitify-app/gitify/blob/67c00229d77d09e0c7f7044da7c24b42b484dcb0/src/main/index.ts)
- [src/main/lifecycle/index.ts](https://github.com/gitify-app/gitify/blob/67c00229d77d09e0c7f7044da7c24b42b484dcb0/src/main/lifecycle/index.ts)
- [src/preload/index.ts](https://github.com/gitify-app/gitify/blob/67c00229d77d09e0c7f7044da7c24b42b484dcb0/src/preload/index.ts)
- [src/renderer/App.tsx](https://github.com/gitify-app/gitify/blob/67c00229d77d09e0c7f7044da7c24b42b484dcb0/src/renderer/App.tsx)
- [src/renderer/i18n/index.ts](https://github.com/gitify-app/gitify/blob/67c00229d77d09e0c7f7044da7c24b42b484dcb0/src/renderer/i18n/index.ts)
- [src/renderer/index.tsx](https://github.com/gitify-app/gitify/blob/67c00229d77d09e0c7f7044da7c24b42b484dcb0/src/renderer/index.tsx)
- [src/renderer/stores/index.ts](https://github.com/gitify-app/gitify/blob/67c00229d77d09e0c7f7044da7c24b42b484dcb0/src/renderer/stores/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 94 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 33 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| __helpers__ package | library | Observed | Groups 4 file(s) under __helpers__ package (observed from repository paths and static analysis). |
| main package | library | Observed | Groups 36 file(s) under main package (observed from repository paths and static analysis). |
| preload package | library | Observed | Groups 6 file(s) under preload package (observed from repository paths and static analysis). |
| renderer package | library | Observed | Groups 333 file(s) under renderer package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 9 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 6 file(s) under service / domain layer (observed from repository paths and static analysis). |
| shared package | library | Observed | Groups 9 file(s) under shared package (observed from repository paths and static analysis). |

## Important files

- `.env.template` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/actionlint.yaml` (config)
- `.github/labeler.yml` (config)
- `.github/release.yml` (config)
- `.github/workflows/build.yml` (ci)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/lint.yml` (ci)
- `.github/workflows/milestone.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/renovate.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `.github/workflows/triage.yml` (ci)
- `.github/workflows/website.yml` (ci)
- `.github/workflows/zizmor.yml` (ci)
- `.github/zizmor.yml` (config)
- `.release-please-manifest.json` (config)
- `.vscode/extensions.json` (config)
- `.vscode/settings.json` (config)
- `openspec/config.yaml` (config)
- `package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `release-please-config.json` (config)
- `renovate.json` (config)
- `src/renderer/i18n/locales/en.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `src` — 564 analysed file(s)
- `(root files)` — 24 analysed file(s)
- `.github` — 21 analysed file(s)
- `.opencode` — 12 analysed file(s)
- `scripts` — 9 analysed file(s)
- `.vscode` — 2 analysed file(s)
- `.husky` — 1 analysed file(s)
- `assets` — 1 analysed file(s)
- `openspec` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `67c00229d77d09e0c7f7044da7c24b42b484dcb0` is the revision these paths and observations refer to.
