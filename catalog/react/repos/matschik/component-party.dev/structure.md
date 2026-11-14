# Project structure: matschik/component-party.dev

**Analysed commit:** `ef3b7a29ad97749f1134a5de1083e7ff9ebdfb77`

**Commit reference:** [ef3b7a29ad97749f1134a5de1083e7ff9ebdfb77](https://github.com/matschik/component-party.dev/commit/ef3b7a29ad97749f1134a5de1083e7ff9ebdfb77)

**Tree at this commit:** [matschik/component-party.dev@ef3b7a29ad97](https://github.com/matschik/component-party.dev/tree/ef3b7a29ad97749f1134a5de1083e7ff9ebdfb77)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | matschik/component-party.dev |
| Description | 🎉 Web component JS frameworks overview by their syntax and features |
| Stars | 3347 |
| Forks | 268 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `ef3b7a29ad97749f1134a5de1083e7ff9ebdfb77` |
| Retrieved at | 2026-11-14T19:15:22.404891+00:00 |
| Files in this snapshot | 678 |

## Directory tree

```text
.github/  (3 files)
  actions/  (1 files)
    setup-node-pnpm/  (1 files)
      … 1 files under this directory
  workflows/  (2 files)
    ci.yml
    setup-node-pnpm.yml
.vite-hooks/  (1 files)
  pre-commit
.vscode/  (1 files)
  extensions.json
content/  (588 files)
  1-reactivity/  (63 files)
    1-declare-state/  (21 files)
      … 21 files under this directory
    2-update-state/  (21 files)
      … 21 files under this directory
    3-computed-state/  (21 files)
      … 21 files under this directory
  2-templating/  (125 files)
    1-minimal-template/  (18 files)
      … 18 files under this directory
    2-styling/  (24 files)
      … 24 files under this directory
    3-loop/  (20 files)
      … 20 files under this directory
    4-event-click/  (21 files)
      … 21 files under this directory
    5-dom-ref/  (21 files)
      … 21 files under this directory
    6-conditional/  (21 files)
      … 21 files under this directory
  3-lifecycle/  (42 files)
    1-on-mount/  (21 files)
      … 21 files under this directory
    2-on-unmount/  (21 files)
      … 21 files under this directory
  4-component-composition/  (196 files)
    1-props/  (40 files)
      … 40 files under this directory
    2-emit-to-parent/  (40 files)
      … 40 files under this directory
    3-slot/  (35 files)
      … 35 files under this directory
    4-slot-fallback/  (35 files)
      … 35 files under this directory
    5-context/  (46 files)
      … 46 files under this directory
  6-form-input/  (84 files)
    1-input-text/  (21 files)
      … 21 files under this directory
    2-checkbox/  (21 files)
      … 21 files under this directory
    3-radio/  (21 files)
      … 21 files under this directory
    4-select/  (21 files)
      … 21 files under this directory
  7-webapp-features/  (78 files)
    1-render-app/  (47 files)
      … 47 files under this directory
    2-fetch-data/  (31 files)
      … 31 files under this directory
docs/  (4 files)
  superpowers/  (4 files)
    plans/  (2 files)
      … 2 files under this directory
    specs/  (2 files)
      … 2 files under this directory
scripts/  (4 files)
  check-toolchain.sh
  generateContent.ts
  generateReadMeProgress.ts
  npmDownloadStats.ts
src/  (35 files)
  lib/  (19 files)
    components/  (8 files)
      … 8 files under this directory
    buildDate.ts
    comparisonPairs.test.ts
    comparisonPairs.ts
    constants.ts
    copyToClipboard.ts
    createLocaleStorage.ts
    footerNavigation.ts
    frameworkUrl.test.ts
    frameworkUrl.ts
    seo.ts
    types.ts
  routes/  (12 files)
    _redirects/  (1 files)
      … 1 files under this directory
    compare/  (2 files)
      … 2 files under this directory
    og/  (3 files)
      … 3 files under this directory
    sitemap.xml/  (1 files)
      … 1 files under this directory
    +error.svelte
    +layout.svelte
    +layout.ts
    +page.svelte
    +page.ts
  app.css
  app.html
  svelte.d.ts
  vite-env.d.ts
static/  (18 files)
  framework/  (14 files)
    alpine.svg
    angular-renaissance.svg
    angular.svg
    aurelia.svg
    ember.svg
    lit.svg
    marko.svg
    mithril.svg
    qwik.svg
    react.svg
    ripple.svg
    solid.svg
    svelte.svg
    vue.svg
  _headers
  manifest.json
  popper.svg
  robots.txt
test/  (7 files)
  e2e/  (5 files)
    config/  (1 files)
      … 1 files under this directory
    utils/  (1 files)
      … 1 files under this directory
    framework-comparison.test.ts
    home.test.ts
    integration.test.ts
  og-jsonld.test.ts
  prerender.test.ts
types/  (1 files)
  micache.d.ts
.git-blame-ignore-revs
.gitignore
.node-version
CONTRIBUTING.md
LICENSE
README.md
frameworks.ts
knip.json
package.json
playwright.config.ts
pnpm-workspace.yaml
renovate.json
tsconfig.json
tsconfig.node.json
vite.config.ts
void.config.ts
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 12 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| content package | library | Observed | Groups 385 file(s) under content package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 19 file(s) under lib package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 4 file(s) under scripts package (observed from repository paths and static analysis). |
| svelte.d.ts package | library | Observed | Groups 1 file(s) under svelte.d.ts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 7 file(s) under tests (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 1 file(s) under types package (observed from repository paths and static analysis). |
| vite-env.d.ts package | library | Observed | Groups 1 file(s) under vite-env.d.ts package (observed from repository paths and static analysis). |

## Important files

- `.github/actions/setup-node-pnpm/action.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/setup-node-pnpm.yml` (ci)
- `.vscode/extensions.json` (config)
- `knip.json` (config)
- `package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `renovate.json` (config)
- `static/manifest.json` (config)
- `tsconfig.json` (config)
- `tsconfig.node.json` (config)

## Top-level layout

- `content` — 588 analysed file(s)
- `src` — 35 analysed file(s)
- `static` — 18 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `test` — 7 analysed file(s)
- `docs` — 4 analysed file(s)
- `scripts` — 4 analysed file(s)
- `.github` — 3 analysed file(s)
- `.vite-hooks` — 1 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `types` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 13 file(s) were skipped during inventory (13 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `ef3b7a29ad97749f1134a5de1083e7ff9ebdfb77` is the revision these paths and observations refer to.
