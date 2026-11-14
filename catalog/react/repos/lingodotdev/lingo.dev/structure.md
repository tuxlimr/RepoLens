# Project structure: lingodotdev/lingo.dev

**Analysed commit:** `fbc666cf717bbe80a57ce49b8d0fce690ee1766f`

**Commit reference:** [fbc666cf717bbe80a57ce49b8d0fce690ee1766f](https://github.com/lingodotdev/lingo.dev/commit/fbc666cf717bbe80a57ce49b8d0fce690ee1766f)

**Tree at this commit:** [lingodotdev/lingo.dev@fbc666cf717b](https://github.com/lingodotdev/lingo.dev/tree/fbc666cf717bbe80a57ce49b8d0fce690ee1766f)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | lingodotdev/lingo.dev |
| Description | Open-source localization engineering tools. Connects to Lingo.dev localization engineering platform for consistent, quality translations. |
| Stars | 5402 |
| Forks | 813 |
| Licence | Apache-2.0 |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `fbc666cf717bbe80a57ce49b8d0fce690ee1766f` |
| Retrieved at | 2026-11-14T19:14:20.771051+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.changeset/  (2 files)
  README.md
  config.json
.claude/  (4 files)
  agents/  (1 files)
    code-architect-reviewer.md
  commands/  (2 files)
    analyze-bucket-type.md
    create-bucket-docs.md
  settings.local.json
.github/  (12 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.yml
    documentation.yml
    feature_request.yml
  workflows/  (7 files)
    docker.yml
    pr-assignment-check.yml
    pr-check.yml
    pr-lint.yml
    pr-merge-conflict-check.yml
    pr-stale-check.yml
    release.yml
  dependabot.yml
  pull_request_template.md
.husky/  (1 files)
  commit-msg
.lingo/  (1 files)
  config.json
.vscode/  (3 files)
  extensions.json
  launch.json
  settings.json
community/  (1 files)
  README.md
demo/  (80 files)
  new-cli/  (28 files)
    .lingo/  (2 files)
      … 2 files under this directory
    content/  (24 files)
      … 24 files under this directory
    README.md
    package.json
  new-compiler-next16/  (24 files)
    app/  (8 files)
      … 8 files under this directory
    components/  (4 files)
      … 4 files under this directory
    public/  (5 files)
      … 5 files under this directory
    .gitignore
    CHANGELOG.md
    README.md
    next.config.ts
    package.json
    postcss.config.mjs
    tsconfig.json
  new-compiler-vite-react-spa/  (28 files)
    public/  (7 files)
      … 7 files under this directory
    src/  (13 files)
      … 13 files under this directory
    .cta.json
    .gitignore
    README.md
    analyze-bundle.sh
    index.html
    package.json
    tsconfig.json
    vite.config.ts
docs/  (2 files)
  svelte-integration-guide.md
  vue-integration-guide.md
integrations/  (12 files)
  directus/  (12 files)
    src/  (3 files)
      … 3 files under this directory
    .gitignore
    CHANGELOG.md
    Dockerfile
    README.md
    docker-compose.yml
    package.json
    tsconfig.json
    tsconfig.test.json
    tsup.config.ts
legacy/  (9 files)
  cli/  (4 files)
    bin/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    package.json
    readme.md
  sdk/  (5 files)
    CHANGELOG.md
    README.md
    index.d.ts
    index.js
    package.json
packages/  (660 files)
  cli/  (371 files)
    bin/  (1 files)
      … 1 files under this directory
    demo/  (131 files)
      … 131 files under this directory
    src/  (224 files)
      … 224 files under this directory
    tests/  (1 files)
      … 1 files under this directory
    types/  (2 files)
      … 2 files under this directory
    CHANGELOG.md
    README.md
    WATCH_MODE.md
    agents.md
    i18n.json
    i18n.lock
    package.json
    troubleshooting.md
    tsconfig.json
    tsconfig.test.json
    tsup.config.ts
    vitest.config.ts
  compiler/  (101 files)
    src/  (95 files)
      … 95 files under this directory
    CHANGELOG.md
    README.md
    package.json
    tsconfig.json
    tsup.config.ts
    vitest.config.ts
  locales/  (16 files)
    src/  (11 files)
      … 11 files under this directory
    CHANGELOG.md
    README.md
    package.json
    tsconfig.json
    tsup.config.ts
  logging/  (11 files)
    src/  (7 files)
      … 7 files under this directory
    CHANGELOG.md
    package.json
    tsconfig.json
    tsup.config.ts
  new-compiler/  (129 files)
    docs/  (1 files)
      … 1 files under this directory
    src/  (111 files)
      … 111 files under this directory
    tests/  (8 files)
      … 8 files under this directory
    .gitignore
    CHANGELOG.md
    README.md
    Requirements.md
    package.json
    playwright.config.ts
    tsconfig.json
    tsdown.config.ts
    vitest.config.ts
  react/  (32 files)
    src/  (28 files)
      … 28 files under this directory
    CHANGELOG.md
    README.md
    build.config.ts
    package.json
.editorconfig
.gitignore
.prettierrc
.syncpackrc.json
CLAUDE.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
Dockerfile
LICENSE.md
action.yml
commitlint.config.js
composer.json
package.json
```

## Entry points

- [legacy/cli/bin/cli.mjs](https://github.com/lingodotdev/lingo.dev/blob/fbc666cf717bbe80a57ce49b8d0fce690ee1766f/legacy/cli/bin/cli.mjs)
- [legacy/sdk/index.js](https://github.com/lingodotdev/lingo.dev/blob/fbc666cf717bbe80a57ce49b8d0fce690ee1766f/legacy/sdk/index.js)
- [packages/cli/bin/cli.mjs](https://github.com/lingodotdev/lingo.dev/blob/fbc666cf717bbe80a57ce49b8d0fce690ee1766f/packages/cli/bin/cli.mjs)
- [demo/new-compiler-next16/app/page.tsx](https://github.com/lingodotdev/lingo.dev/blob/fbc666cf717bbe80a57ce49b8d0fce690ee1766f/demo/new-compiler-next16/app/page.tsx)
- [demo/new-compiler-vite-react-spa/src/main.tsx](https://github.com/lingodotdev/lingo.dev/blob/fbc666cf717bbe80a57ce49b8d0fce690ee1766f/demo/new-compiler-vite-react-spa/src/main.tsx)
- [integrations/directus/src/app.ts](https://github.com/lingodotdev/lingo.dev/blob/fbc666cf717bbe80a57ce49b8d0fce690ee1766f/integrations/directus/src/app.ts)
- [packages/compiler/src/index.ts](https://github.com/lingodotdev/lingo.dev/blob/fbc666cf717bbe80a57ce49b8d0fce690ee1766f/packages/compiler/src/index.ts)
- [packages/locales/src/index.ts](https://github.com/lingodotdev/lingo.dev/blob/fbc666cf717bbe80a57ce49b8d0fce690ee1766f/packages/locales/src/index.ts)
- [packages/logging/src/index.ts](https://github.com/lingodotdev/lingo.dev/blob/fbc666cf717bbe80a57ce49b8d0fce690ee1766f/packages/logging/src/index.ts)
- [packages/new-compiler/src/index.ts](https://github.com/lingodotdev/lingo.dev/blob/fbc666cf717bbe80a57ce49b8d0fce690ee1766f/packages/new-compiler/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 11 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 96 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| demo package | library | Observed | Groups 14 file(s) under demo package (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 24 file(s) under external integrations (observed from repository paths and static analysis). |
| legacy package | library | Observed | Groups 3 file(s) under legacy package (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 446 file(s) under packages package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 8 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 10 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.claude/settings.local.json` (config)
- `.editorconfig` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/documentation.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/docker.yml` (ci)
- `.github/workflows/pr-assignment-check.yml` (ci)
- `.github/workflows/pr-check.yml` (ci)
- `.github/workflows/pr-lint.yml` (ci)
- `.github/workflows/pr-merge-conflict-check.yml` (ci)
- `.github/workflows/pr-stale-check.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.lingo/config.json` (config)
- `.syncpackrc.json` (config)
- `.vscode/extensions.json` (config)
- `.vscode/launch.json` (config)
- `.vscode/settings.json` (config)
- `Dockerfile` (container)
- `action.yml` (config)
- `composer.json` (config)
- `demo/new-cli/.lingo/config.json` (config)
- `demo/new-cli/.lingo/lock.json` (config)
- `demo/new-cli/content/de/api.yaml` (config)
- `demo/new-cli/content/de/app.json` (config)
- `demo/new-cli/content/en/api.yaml` (config)
- `demo/new-cli/content/en/app.json` (config)
- `demo/new-cli/content/es/api.yaml` (config)
- `demo/new-cli/content/es/app.json` (config)
- `demo/new-cli/content/fr/api.yaml` (config)
- `demo/new-cli/content/fr/app.json` (config)
- `demo/new-cli/package.json` (manifest)
- `demo/new-compiler-next16/app/.lingo/cache/de.json` (config)
- `demo/new-compiler-next16/app/.lingo/cache/en.json` (config)
- `demo/new-compiler-next16/app/.lingo/cache/es.json` (config)
- `demo/new-compiler-next16/app/.lingo/cache/ru.json` (config)
- `demo/new-compiler-next16/package.json` (manifest)
- `demo/new-compiler-next16/tsconfig.json` (config)
- `demo/new-compiler-vite-react-spa/.cta.json` (config)
- `demo/new-compiler-vite-react-spa/package.json` (manifest)
- `demo/new-compiler-vite-react-spa/public/manifest.json` (config)
- `demo/new-compiler-vite-react-spa/public/translations/de.json` (config)
- `demo/new-compiler-vite-react-spa/public/translations/en.json` (config)
- `demo/new-compiler-vite-react-spa/public/translations/es.json` (config)
- `demo/new-compiler-vite-react-spa/public/translations/fr.json` (config)
- `demo/new-compiler-vite-react-spa/src/.lingo/cache/de.json` (config)
- `demo/new-compiler-vite-react-spa/src/.lingo/cache/en.json` (config)
- `demo/new-compiler-vite-react-spa/src/.lingo/cache/es.json` (config)
- `demo/new-compiler-vite-react-spa/src/.lingo/cache/fr.json` (config)
- `demo/new-compiler-vite-react-spa/tsconfig.json` (config)
- `integrations/directus/Dockerfile` (container)
- `integrations/directus/docker-compose.yml` (container)
- `integrations/directus/package.json` (manifest)
- `integrations/directus/tsconfig.json` (config)
- `integrations/directus/tsconfig.test.json` (config)
- `legacy/cli/package.json` (manifest)
- `legacy/sdk/package.json` (manifest)
- `package.json` (manifest)
- `packages/cli/demo/ail/i18n.json` (config)
- `packages/cli/demo/android/i18n.json` (config)
- `packages/cli/demo/csv-per-locale/i18n.json` (config)
- `packages/cli/demo/csv/i18n.json` (config)
- `packages/cli/demo/ejs/i18n.json` (config)
- `packages/cli/demo/flutter/i18n.json` (config)
- `packages/cli/demo/html/i18n.json` (config)
- `packages/cli/demo/json-dictionary/example.json` (config)
- `packages/cli/demo/json-dictionary/i18n.json` (config)
- `packages/cli/demo/json/en/example.json` (config)
- `packages/cli/demo/json/es/example.json` (config)
- `packages/cli/demo/json/i18n.json` (config)
- `packages/cli/demo/json5/i18n.json` (config)
- `packages/cli/demo/jsonc/i18n.json` (config)
- `packages/cli/demo/markdoc/i18n.json` (config)
- `packages/cli/demo/markdown/i18n.json` (config)
- `packages/cli/demo/mdx/i18n.json` (config)
- `packages/cli/demo/mjml/i18n.json` (config)
- `packages/cli/demo/php/i18n.json` (config)
- `packages/cli/demo/po/i18n.json` (config)
- `packages/cli/demo/properties/i18n.json` (config)
- `packages/cli/demo/srt/i18n.json` (config)
- `packages/cli/demo/twig/i18n.json` (config)
- `packages/cli/demo/txt/i18n.json` (config)
- `packages/cli/demo/typescript/i18n.json` (config)
- `packages/cli/demo/vtt/i18n.json` (config)
- `packages/cli/demo/vue-json/i18n.json` (config)
- `packages/cli/demo/xcode-strings/i18n.json` (config)
- `packages/cli/demo/xcode-stringsdict/i18n.json` (config)
- `packages/cli/demo/xcode-xcstrings-v2/i18n.json` (config)
- `packages/cli/demo/xcode-xcstrings/i18n.json` (config)
- `packages/cli/demo/xliff/i18n.json` (config)
- `packages/cli/demo/xml/i18n.json` (config)
- `packages/cli/demo/yaml-root-key/en/example.yml` (config)
- `packages/cli/demo/yaml-root-key/es/example.yml` (config)
- `packages/cli/demo/yaml-root-key/i18n.json` (config)
- `packages/cli/demo/yaml/en/example.yml` (config)
- `packages/cli/demo/yaml/es/example.yml` (config)
- `packages/cli/demo/yaml/i18n.json` (config)
- `packages/cli/i18n.json` (config)
- `packages/cli/package.json` (manifest)
- `packages/cli/tsconfig.json` (config)
- `packages/cli/tsconfig.test.json` (config)
- `packages/compiler/package.json` (manifest)
- `packages/compiler/tsconfig.json` (config)
- `packages/locales/package.json` (manifest)
- `packages/locales/tsconfig.json` (config)
- `packages/logging/package.json` (manifest)
- `packages/logging/tsconfig.json` (config)
- `packages/new-compiler/package.json` (manifest)
- `packages/new-compiler/tsconfig.json` (config)
- `packages/react/package.json` (manifest)

## Top-level layout

- `packages` — 660 analysed file(s)
- `demo` — 80 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `.github` — 12 analysed file(s)
- `integrations` — 12 analysed file(s)
- `legacy` — 9 analysed file(s)
- `.claude` — 4 analysed file(s)
- `.vscode` — 3 analysed file(s)
- `.changeset` — 2 analysed file(s)
- `docs` — 2 analysed file(s)
- `.husky` — 1 analysed file(s)
- `.lingo` — 1 analysed file(s)
- `community` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `fbc666cf717bbe80a57ce49b8d0fce690ee1766f` is the revision these paths and observations refer to.
