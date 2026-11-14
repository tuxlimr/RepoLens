# Project structure: extension-js/extension.js

**Analysed commit:** `2dac0905f63bfe36ecd265cac6f20ec74338ca2e`

**Commit reference:** [2dac0905f63bfe36ecd265cac6f20ec74338ca2e](https://github.com/extension-js/extension.js/commit/2dac0905f63bfe36ecd265cac6f20ec74338ca2e)

**Tree at this commit:** [extension-js/extension.js@2dac0905f63b](https://github.com/extension-js/extension.js/tree/2dac0905f63bfe36ecd265cac6f20ec74338ca2e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | extension-js/extension.js |
| Description | The cross-browser extension framework. |
| Stars | 5211 |
| Forks | 141 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `2dac0905f63bfe36ecd265cac6f20ec74338ca2e` |
| Retrieved at | 2026-11-14T19:14:24.579733+00:00 |
| Files in this snapshot | 799 |

## Directory tree

```text
.githooks/  (2 files)
  h
  pre-commit
.github/  (27 files)
  actions/  (1 files)
    setup/  (1 files)
      … 1 files under this directory
  workflows/  (21 files)
    actionlint.yml
    browser-channels.yml
    ci.yml
    clean-release-notes.yml
    cli-flags-drift.yml
    codeql.yml
    deps-canary.yml
    discord-notify-releases.yml
    e2e-content-reload-hunt.yml
    e2e-smoke.yml
    e2e.yml
    optional-deps-matrix.yml
    programs-nightly.yml
    publish-release.yml
    release-attest.yml
    reload-matrix-smoke.yml
    safari-nightly.yml
    scorecard.yml
    sync-npm-readme.yml
    telemetry-check.yml
    traffic-snapshot.yml
  CODEOWNERS
  CODE_OF_CONDUCT.md
  FUNDING.yml
  SECURITY.md
  dependabot.yml
.husky/  (1 files)
  pre-commit
.well-known/  (1 files)
  funding-manifest-urls
docs/  (7 files)
  ARCHITECTURE.md
  ASSURANCE_CASE.md
  CONTRIBUTING.md
  MESSAGING.md
  RELEASING.md
  TELEMETRY.md
  VERIFYING_RELEASES.md
extensions/  (23 files)
  extension-js-devtools/  (20 files)
    pages/  (2 files)
      … 2 files under this directory
    public/  (1 files)
      … 1 files under this directory
    src/  (12 files)
      … 12 files under this directory
    .gitignore
    README.md
    package.json
    postcss.config.js
    tsconfig.json
  extension-js-theme/  (3 files)
    README.md
    manifest.json
    package.json
programs/  (723 files)
  create/  (99 files)
    __spec__/  (14 files)
      … 14 files under this directory
    lib/  (22 files)
      … 22 files under this directory
    steps/  (37 files)
      … 37 files under this directory
    templates/  (17 files)
      … 17 files under this directory
    .gitignore
    LICENSE
    README.md
    create.spec.ts
    module.ts
    package.json
    rslib.config.ts
    tsconfig.json
    vitest.config.ts
  develop/  (624 files)
    __spec__/  (192 files)
      … 192 files under this directory
    dev-server/  (89 files)
      … 89 files under this directory
    lib/  (143 files)
      … 143 files under this directory
    plugin-browsers/  (12 files)
      … 12 files under this directory
    plugin-compatibility/  (12 files)
      … 12 files under this directory
    plugin-compilation/  (32 files)
      … 32 files under this directory
    plugin-css/  (53 files)
      … 53 files under this directory
    plugin-js-frameworks/  (35 files)
      … 35 files under this directory
    plugin-perf-budgets/  (6 files)
      … 6 files under this directory
    plugin-playwright/  (12 files)
      … 12 files under this directory
    plugin-reload/  (28 files)
      … 28 files under this directory
    LICENSE
    README.md
    bridge-entry.ts
    command-build.ts
    command-dev.ts
    command-preview.ts
    contracts-entry.ts
    manifest-entry.ts
    module.ts
    package.json
.env.example
.gitattributes
.gitignore
BACKERS.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
RELEASE_HIGHLIGHTS.md
biome.json
context7.json
eslint.config.mjs
package.json
playwright.config.ts
pnpm-workspace.yaml
```

## Entry points

- [programs/develop/dev-server/index.ts](https://github.com/extension-js/extension.js/blob/2dac0905f63bfe36ecd265cac6f20ec74338ca2e/programs/develop/dev-server/index.ts)
- [programs/develop/plugin-browsers/index.ts](https://github.com/extension-js/extension.js/blob/2dac0905f63bfe36ecd265cac6f20ec74338ca2e/programs/develop/plugin-browsers/index.ts)
- [programs/develop/plugin-compatibility/index.ts](https://github.com/extension-js/extension.js/blob/2dac0905f63bfe36ecd265cac6f20ec74338ca2e/programs/develop/plugin-compatibility/index.ts)
- [programs/develop/plugin-compilation/index.ts](https://github.com/extension-js/extension.js/blob/2dac0905f63bfe36ecd265cac6f20ec74338ca2e/programs/develop/plugin-compilation/index.ts)
- [programs/develop/plugin-css/index.ts](https://github.com/extension-js/extension.js/blob/2dac0905f63bfe36ecd265cac6f20ec74338ca2e/programs/develop/plugin-css/index.ts)
- [programs/develop/plugin-js-frameworks/index.ts](https://github.com/extension-js/extension.js/blob/2dac0905f63bfe36ecd265cac6f20ec74338ca2e/programs/develop/plugin-js-frameworks/index.ts)
- [programs/develop/plugin-perf-budgets/index.ts](https://github.com/extension-js/extension.js/blob/2dac0905f63bfe36ecd265cac6f20ec74338ca2e/programs/develop/plugin-perf-budgets/index.ts)
- [programs/develop/plugin-playwright/index.ts](https://github.com/extension-js/extension.js/blob/2dac0905f63bfe36ecd265cac6f20ec74338ca2e/programs/develop/plugin-playwright/index.ts)
- [programs/develop/plugin-reload/index.ts](https://github.com/extension-js/extension.js/blob/2dac0905f63bfe36ecd265cac6f20ec74338ca2e/programs/develop/plugin-reload/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 17 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| extensions package | library | Observed | Groups 11 file(s) under extensions package (observed from repository paths and static analysis). |
| programs package | library | Observed | Groups 696 file(s) under programs package (observed from repository paths and static analysis). |

## Important files

- `.env.example` (config)
- `.github/FUNDING.yml` (config)
- `.github/actions/setup/action.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/actionlint.yml` (ci)
- `.github/workflows/browser-channels.yml` (ci)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/clean-release-notes.yml` (ci)
- `.github/workflows/cli-flags-drift.yml` (ci)
- `.github/workflows/codeql.yml` (ci)
- `.github/workflows/deps-canary.yml` (ci)
- `.github/workflows/discord-notify-releases.yml` (ci)
- `.github/workflows/e2e-content-reload-hunt.yml` (ci)
- `.github/workflows/e2e-smoke.yml` (ci)
- `.github/workflows/e2e.yml` (ci)
- `.github/workflows/optional-deps-matrix.yml` (ci)
- `.github/workflows/programs-nightly.yml` (ci)
- `.github/workflows/publish-release.yml` (ci)
- `.github/workflows/release-attest.yml` (ci)
- `.github/workflows/reload-matrix-smoke.yml` (ci)
- `.github/workflows/safari-nightly.yml` (ci)
- `.github/workflows/scorecard.yml` (ci)
- `.github/workflows/sync-npm-readme.yml` (ci)
- `.github/workflows/telemetry-check.yml` (ci)
- `.github/workflows/traffic-snapshot.yml` (ci)
- `biome.json` (config)
- `context7.json` (config)
- `extensions/extension-js-devtools/package.json` (manifest)
- `extensions/extension-js-devtools/public/extension-js-session.json` (config)
- `extensions/extension-js-devtools/src/manifest.json` (config)
- `extensions/extension-js-devtools/tsconfig.json` (config)
- `extensions/extension-js-theme/manifest.json` (config)
- `extensions/extension-js-theme/package.json` (manifest)
- `package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `programs/create/package.json` (manifest)
- `programs/create/templates/javascript/.mcp.json` (config)
- `programs/create/templates/javascript/package.json` (manifest)
- `programs/create/templates/javascript/src/manifest.json` (config)
- `programs/create/tsconfig.json` (config)
- `programs/develop/package.json` (manifest)
- `programs/develop/plugin-perf-budgets/package.json` (manifest)

## Top-level layout

- `programs` — 723 analysed file(s)
- `.github` — 27 analysed file(s)
- `extensions` — 23 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `docs` — 7 analysed file(s)
- `.githooks` — 2 analysed file(s)
- `.husky` — 1 analysed file(s)
- `.well-known` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `2dac0905f63bfe36ecd265cac6f20ec74338ca2e` is the revision these paths and observations refer to.
