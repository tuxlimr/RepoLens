# Project structure: benawad/dogehouse

**Analysed commit:** `584055ad407bc37fa35cdf36ebb271622e29d436`

**Commit reference:** [584055ad407bc37fa35cdf36ebb271622e29d436](https://github.com/benawad/dogehouse/commit/584055ad407bc37fa35cdf36ebb271622e29d436)

**Tree at this commit:** [benawad/dogehouse@584055ad407b](https://github.com/benawad/dogehouse/tree/584055ad407bc37fa35cdf36ebb271622e29d436)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | benawad/dogehouse |
| Description | Taking voice conversations to the moon 🚀 |
| Stars | 9006 |
| Forks | 1406 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | staging |
| Analysed commit | `584055ad407bc37fa35cdf36ebb271622e29d436` |
| Retrieved at | 2026-11-14T19:13:36.777930+00:00 |
| Files in this snapshot | 798 |

## Directory tree

```text
.devcontainer/  (6 files)
  scripts/  (3 files)
    environment.sh
    node.sh
    user.sh
  Dockerfile
  devcontainer.json
  docker-compose.yml
.github/  (14 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (11 files)
    baklava-build_and_release.yaml
    dolma-npm_deploy.yaml
    global-label_pr.yml
    global-lint_commit_messages.yaml
    globalkey-npm_deploy.yaml
    kebab-npm_publish.yaml
    kibbeh-e2e_tests.yaml
    kibbeh-lint_and_test.yaml
    kousa-deploy_staging.yaml
    kousa-tests.yaml
    shawarma-deploy_staging.yaml
  labeler.yml
.husky/  (3 files)
  .gitignore
  commit-msg
  pre-commit
.redesign-assets/  (241 files)
  icons/  (235 files)
    flags/  (216 files)
      … 216 files under this directory
    lg-solid-rocket.svg
    lg-solid-time.svg
    sm-outline-globe.svg
    sm-outline-notifications.svg
    sm-solid-bug.svg
    sm-solid-dogenitro.svg
    sm-solid-fullscreen.svg
    sm-solid-help.svg
    sm-solid-megaphone.svg
    sm-solid-messages.svg
    sm-solid-microphone.svg
    sm-solid-notifications.svg
    sm-solid-plus.svg
    sm-solid-search.svg
    sm-solid-settings.svg
    sm-solid-time.svg
    sm-solid-user.svg
    sm-solid-volume.svg
    solid-microphone-off.svg
  mobile/  (5 files)
    icons/  (5 files)
      … 5 files under this directory
  dogehouse_logo.svg
.vscode/  (1 files)
  settings.json
.yarn/  (1 files)
  plugins/  (1 files)
    @yarnpkg/  (1 files)
      … 1 files under this directory
baklava/  (35 files)
  icons/  (1 files)
    electrondoge.svg
  locales/  (1 files)
    en/  (1 files)
      … 1 files under this directory
  resources/  (11 files)
    overlay/  (10 files)
      … 10 files under this directory
    splash/  (1 files)
      … 1 files under this directory
  scripts/  (4 files)
    generateTranslationTypes.ts
    syncTranslations.ts
    traverseTranslations.ts
    tsconfig.json
  settings/  (1 files)
    entitlements.mac.plist
  src/  (12 files)
    generated/  (1 files)
      … 1 files under this directory
    utils/  (7 files)
      … 7 files under this directory
    constants.ts
    dev.ts
    electron.ts
    types.ts
  .gitignore
  .yarnrc.yml
  README.md
  package.json
  tsconfig.json
dinner/  (6 files)
  src/  (2 files)
    create-accounts.ts
    play-audio.ts
  .eslintrc.json
  .gitignore
  package.json
  tsconfig.json
docs/  (6 files)
  Architecture/  (1 files)
    README.md
  Directory/  (1 files)
    README.md
  Elixir Api/  (1 files)
    README.MD
  React Front End/  (1 files)
    README.MD
  Voice Server/  (1 files)
    README.MD
  README.MD
dolma/  (23 files)
  src/  (17 files)
    lib/  (5 files)
      … 5 files under this directory
    test/  (2 files)
      … 2 files under this directory
    tokens/  (7 files)
      … 7 files under this directory
    util/  (2 files)
      … 2 files under this directory
    index.ts
  .editorconfig
  .gitignore
  LICENSE
  README.md
  package.json
  tsconfig.json
globalkey/  (8 files)
  src/  (2 files)
    build.rs
    lib.rs
  .gitignore
  Cargo.toml
  README.md
  index.d.ts
  package.json
  test.js
kebab/  (69 files)
  examples/  (29 files)
    bot/  (4 files)
      … 4 files under this directory
    chat/  (4 files)
      … 4 files under this directory
    create-bot/  (4 files)
      … 4 files under this directory
    mediasoup-audio/  (6 files)
      … 6 files under this directory
    react-chat/  (11 files)
      … 11 files under this directory
  src/  (33 files)
    audio/  (3 files)
      … 3 files under this directory
    client/  (15 files)
      … 15 files under this directory
    http/  (4 files)
      … 4 files under this directory
    util/  (3 files)
      … 3 files under this directory
    websocket/  (4 files)
      … 4 files under this directory
    README.md
    entities.ts
    index.ts
    pagination.ts
  .eslintrc.json
  .gitignore
  .prettierrc.js
  README.md
  jest.config.js
  package.json
  tsconfig.json
kibbeh/  (362 files)
  .storybook/  (4 files)
    main.js
    manager.js
    preview-head.html
    preview.js
  cypress/  (13 files)
    fixtures/  (1 files)
      … 1 files under this directory
    integration/  (4 files)
      … 4 files under this directory
    plugins/  (2 files)
      … 2 files under this directory
    support/  (4 files)
      … 4 files under this directory
    .gitignore
    tsconfig.json
  public/  (77 files)
    locales/  (74 files)
      … 74 files under this directory
    manifest.json
    privacy-policy.html
    terms.html
  scripts/  (3 files)
    syncTranslations.ts
    traverseTranslations.ts
    tsconfig.json
  src/  (250 files)
    form-fields/  (2 files)
      … 2 files under this directory
    global-stores/  (19 files)
      … 19 files under this directory
    icons/  (61 files)
      … 61 files under this directory
    lib/  (14 files)
      … 14 files under this directory
    modules/  (120 files)
      … 120 files under this directory
    pages/  (24 files)
      … 24 files under this directory
    shared-components/  (3 files)
      … 3 files under this directory
    shared-hooks/  (5 files)
      … 5 files under this directory
    globals.d.ts
    jest.config.js
  .babelrc
  .env.example
  .eslintignore
  .eslintrc.json
  .gitignore
  .prettierignore
  .prettierrc.js
  .stylelintrc.json
  README.md
  cypress.json
  deploy.sh
  next-env.d.ts
  next.config.js
  package.json
  postcss.config.js
.dockerignore
.editorconfig
.eslintignore
.gitignore
.prettierignore
.prettierrc.js
.yarnrc.yml
CHANGELOG.md
CODEOWNERS
CODE_OF_CONDUCT.md
CONTRIBUTING.md
CREATE_BOT_ACCOUNT.MD
DESIGN_GUIDELINES.md
FAQ.md
HOW_TO_DEBUG_AUDIO.md
HOW_TO_GET_PERMA_BANNED_FROM_DOGEHOUSE.md
LICENSE
README.md
SECURITY.md
commitlint.config.js
docker-compose.local.yml
docker-compose.prod.yml
docker-compose.yml
```

## Entry points

- [dolma/src/index.ts](https://github.com/benawad/dogehouse/blob/584055ad407bc37fa35cdf36ebb271622e29d436/dolma/src/index.ts)
- [dolma/src/tokens/index.ts](https://github.com/benawad/dogehouse/blob/584055ad407bc37fa35cdf36ebb271622e29d436/dolma/src/tokens/index.ts)
- [kebab/src/client/index.ts](https://github.com/benawad/dogehouse/blob/584055ad407bc37fa35cdf36ebb271622e29d436/kebab/src/client/index.ts)
- [kebab/src/http/index.ts](https://github.com/benawad/dogehouse/blob/584055ad407bc37fa35cdf36ebb271622e29d436/kebab/src/http/index.ts)
- [kebab/src/index.ts](https://github.com/benawad/dogehouse/blob/584055ad407bc37fa35cdf36ebb271622e29d436/kebab/src/index.ts)
- [kebab/src/util/index.ts](https://github.com/benawad/dogehouse/blob/584055ad407bc37fa35cdf36ebb271622e29d436/kebab/src/util/index.ts)
- [kebab/src/websocket/index.ts](https://github.com/benawad/dogehouse/blob/584055ad407bc37fa35cdf36ebb271622e29d436/kebab/src/websocket/index.ts)
- [kibbeh/.storybook/main.js](https://github.com/benawad/dogehouse/blob/584055ad407bc37fa35cdf36ebb271622e29d436/kibbeh/.storybook/main.js)
- [kibbeh/cypress/plugins/index.js](https://github.com/benawad/dogehouse/blob/584055ad407bc37fa35cdf36ebb271622e29d436/kibbeh/cypress/plugins/index.js)
- [kibbeh/cypress/support/index.js](https://github.com/benawad/dogehouse/blob/584055ad407bc37fa35cdf36ebb271622e29d436/kibbeh/cypress/support/index.js)
- [kibbeh/src/icons/index.tsx](https://github.com/benawad/dogehouse/blob/584055ad407bc37fa35cdf36ebb271622e29d436/kibbeh/src/icons/index.tsx)
- [kibbeh/src/pages/index.tsx](https://github.com/benawad/dogehouse/blob/584055ad407bc37fa35cdf36ebb271622e29d436/kibbeh/src/pages/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| baklava package | library | Observed | Groups 18 file(s) under baklava package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 119 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| dinner package | library | Observed | Groups 2 file(s) under dinner package (observed from repository paths and static analysis). |
| dolma package | library | Observed | Groups 15 file(s) under dolma package (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 18 file(s) under external integrations (observed from repository paths and static analysis). |
| globalkey package | library | Observed | Groups 4 file(s) under globalkey package (observed from repository paths and static analysis). |
| kebab package | library | Observed | Groups 26 file(s) under kebab package (observed from repository paths and static analysis). |
| kibbeh package | library | Observed | Groups 259 file(s) under kibbeh package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 4 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.devcontainer/Dockerfile` (container)
- `.devcontainer/devcontainer.json` (config)
- `.devcontainer/docker-compose.yml` (container)
- `.dockerignore` (container)
- `.editorconfig` (config)
- `.github/labeler.yml` (config)
- `.github/workflows/baklava-build_and_release.yaml` (ci)
- `.github/workflows/dolma-npm_deploy.yaml` (ci)
- `.github/workflows/global-label_pr.yml` (ci)
- `.github/workflows/global-lint_commit_messages.yaml` (ci)
- `.github/workflows/globalkey-npm_deploy.yaml` (ci)
- `.github/workflows/kebab-npm_publish.yaml` (ci)
- `.github/workflows/kibbeh-e2e_tests.yaml` (ci)
- `.github/workflows/kibbeh-lint_and_test.yaml` (ci)
- `.github/workflows/kousa-deploy_staging.yaml` (ci)
- `.github/workflows/kousa-tests.yaml` (ci)
- `.github/workflows/shawarma-deploy_staging.yaml` (ci)
- `.vscode/settings.json` (config)
- `.yarnrc.yml` (config)
- `baklava/.yarnrc.yml` (config)
- `baklava/locales/en/translate.json` (config)
- `baklava/package.json` (manifest)
- `baklava/resources/overlay/.yarnrc.yml` (config)
- `baklava/resources/overlay/package.json` (manifest)
- `baklava/scripts/tsconfig.json` (config)
- `baklava/tsconfig.json` (config)
- `dinner/.eslintrc.json` (config)
- `dinner/package.json` (manifest)
- `dinner/tsconfig.json` (config)
- `docker-compose.local.yml` (config)
- `docker-compose.prod.yml` (config)
- `docker-compose.yml` (container)
- `dolma/.editorconfig` (config)
- `dolma/package.json` (manifest)
- `dolma/tsconfig.json` (config)
- `globalkey/Cargo.toml` (manifest)
- `globalkey/package.json` (manifest)
- `kebab/.eslintrc.json` (config)
- `kebab/examples/bot/package.json` (manifest)
- `kebab/examples/bot/tsconfig.json` (config)
- `kebab/examples/chat/package.json` (manifest)
- `kebab/examples/chat/tsconfig.json` (config)
- `kebab/examples/create-bot/package.json` (manifest)
- `kebab/examples/create-bot/tsconfig.json` (config)
- `kebab/examples/mediasoup-audio/package.json` (manifest)
- `kebab/examples/mediasoup-audio/tsconfig.json` (config)
- `kebab/examples/react-chat/package.json` (manifest)
- `kebab/examples/react-chat/public/manifest.json` (config)
- `kebab/examples/react-chat/tsconfig.json` (config)
- `kebab/package.json` (manifest)
- `kebab/tsconfig.json` (config)
- `kibbeh/.env.example` (config)
- `kibbeh/.eslintrc.json` (config)
- `kibbeh/.stylelintrc.json` (config)
- `kibbeh/cypress.json` (config)
- `kibbeh/cypress/fixtures/example.json` (config)
- `kibbeh/cypress/tsconfig.json` (config)
- `kibbeh/package.json` (manifest)
- `kibbeh/public/locales/af/translation.json` (config)
- `kibbeh/public/locales/am/translation.json` (config)
- `kibbeh/public/locales/ar/translation.json` (config)
- `kibbeh/public/locales/az/translation.json` (config)
- `kibbeh/public/locales/bg/translation.json` (config)
- `kibbeh/public/locales/bn/translation.json` (config)
- `kibbeh/public/locales/bottom/translation.json` (config)
- `kibbeh/public/locales/cs/translation.json` (config)
- `kibbeh/public/locales/da/translation.json` (config)
- `kibbeh/public/locales/de-AT/translation.json` (config)
- `kibbeh/public/locales/de/translation.json` (config)
- `kibbeh/public/locales/el/translation.json` (config)
- `kibbeh/public/locales/en-AU/translation.json` (config)
- `kibbeh/public/locales/en-C/translation.json` (config)
- `kibbeh/public/locales/en-CODE/translation.json` (config)
- `kibbeh/public/locales/en-LOLCAT/translation.json` (config)
- `kibbeh/public/locales/en-OWO/translation.json` (config)
- `kibbeh/public/locales/en-PIGLATIN/translation.json` (config)
- `kibbeh/public/locales/en-PIRATE/translation.json` (config)
- `kibbeh/public/locales/en/translation.json` (config)
- `kibbeh/public/locales/eo/translation.json` (config)
- `kibbeh/public/locales/es/translation.json` (config)
- `kibbeh/public/locales/et/translation.json` (config)
- `kibbeh/public/locales/eu/translation.json` (config)
- `kibbeh/public/locales/fa/translation.json` (config)
- `kibbeh/public/locales/fi/translation.json` (config)
- `kibbeh/public/locales/fr/translation.json` (config)
- `kibbeh/public/locales/grc/translation.json` (config)
- `kibbeh/public/locales/gsw/translation.json` (config)
- `kibbeh/public/locales/he/translation.json` (config)
- `kibbeh/public/locales/hi/translation.json` (config)
- `kibbeh/public/locales/hr/translation.json` (config)
- `kibbeh/public/locales/hu/translation.json` (config)
- `kibbeh/public/locales/id/translation.json` (config)
- `kibbeh/public/locales/is/translation.json` (config)
- `kibbeh/public/locales/it/translation.json` (config)
- `kibbeh/public/locales/ja/translation.json` (config)
- `kibbeh/public/locales/kk/translation.json` (config)
- `kibbeh/public/locales/ko/translation.json` (config)
- `kibbeh/public/locales/ku/translation.json` (config)
- `kibbeh/public/locales/li/translation.json` (config)
- `kibbeh/public/locales/lld/translation.json` (config)
- `kibbeh/public/locales/lt/translation.json` (config)
- `kibbeh/public/locales/lv/translation.json` (config)
- `kibbeh/public/locales/nb/translation.json` (config)
- `kibbeh/public/locales/ne/translation.json` (config)
- `kibbeh/public/locales/nl/translation.json` (config)
- `kibbeh/public/locales/pl/translation.json` (config)
- `kibbeh/public/locales/pt-BR/translation.json` (config)
- `kibbeh/public/locales/pt-PT/translation.json` (config)
- `kibbeh/public/locales/ro/translation.json` (config)
- `kibbeh/public/locales/ru/translation.json` (config)
- `kibbeh/public/locales/sa/translation.json` (config)
- `kibbeh/public/locales/si/translation.json` (config)
- `kibbeh/public/locales/sk/translation.json` (config)
- `kibbeh/public/locales/sl/translation.json` (config)
- `kibbeh/public/locales/so/translation.json` (config)
- `kibbeh/public/locales/sq/translation.json` (config)
- `kibbeh/public/locales/sr-LATIN/translation.json` (config)
- `kibbeh/public/locales/sr/translation.json` (config)
- `kibbeh/public/locales/sv/translation.json` (config)
- `kibbeh/public/locales/ta/translation.json` (config)
- `kibbeh/public/locales/te/translation.json` (config)
- `kibbeh/public/locales/th/translation.json` (config)
- `kibbeh/public/locales/tl/translation.json` (config)
- `kibbeh/public/locales/tp/translation.json` (config)
- `kibbeh/public/locales/tr/translation.json` (config)
- `kibbeh/public/locales/uk/translation.json` (config)
- `kibbeh/public/locales/ur/translation.json` (config)
- `kibbeh/public/locales/uz/translation.json` (config)
- `kibbeh/public/locales/vi/translation.json` (config)
- `kibbeh/public/locales/zh-CN/translation.json` (config)
- `kibbeh/public/locales/zh-TW/translation.json` (config)
- `kibbeh/public/manifest.json` (config)
- `kibbeh/scripts/tsconfig.json` (config)

## Top-level layout

- `kibbeh` — 362 analysed file(s)
- `.redesign-assets` — 241 analysed file(s)
- `kebab` — 69 analysed file(s)
- `baklava` — 35 analysed file(s)
- `(root files)` — 23 analysed file(s)
- `dolma` — 23 analysed file(s)
- `.github` — 14 analysed file(s)
- `globalkey` — 8 analysed file(s)
- `.devcontainer` — 6 analysed file(s)
- `dinner` — 6 analysed file(s)
- `docs` — 6 analysed file(s)
- `.husky` — 3 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `.yarn` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `584055ad407bc37fa35cdf36ebb271622e29d436` is the revision these paths and observations refer to.
