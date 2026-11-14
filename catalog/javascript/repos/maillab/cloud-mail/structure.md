# Project structure: maillab/cloud-mail

**Analysed commit:** `a792cdcd5c3291ac718b97489b1be19367121969`

**Commit reference:** [a792cdcd5c3291ac718b97489b1be19367121969](https://github.com/maillab/cloud-mail/commit/a792cdcd5c3291ac718b97489b1be19367121969)

**Tree at this commit:** [maillab/cloud-mail@a792cdcd5c32](https://github.com/maillab/cloud-mail/tree/a792cdcd5c3291ac718b97489b1be19367121969)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | maillab/cloud-mail |
| Description | An all-in-one email service platform powered by Cloudflare  | 基于 Cloudflare 的一站式邮箱服务平台  | Cloudflare Email 邮箱 Mail |
| Stars | 15882 |
| Forks | 23603 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `a792cdcd5c3291ac718b97489b1be19367121969` |
| Retrieved at | 2026-11-14T19:11:35.273345+00:00 |
| Files in this snapshot | 256 |

## Directory tree

```text
.github/  (4 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    feature_request.md
    need-help.md
  workflows/  (1 files)
    deploy-cloudflare.yml
mail-vue/  (154 files)
  public/  (71 files)
    tinymce/  (69 files)
      … 69 files under this directory
    _headers
    content.css
  src/  (78 files)
    axios/  (1 files)
      … 1 files under this directory
    components/  (10 files)
      … 10 files under this directory
    db/  (1 files)
      … 1 files under this directory
    echarts/  (1 files)
      … 1 files under this directory
    enums/  (3 files)
      … 3 files under this directory
    i18n/  (3 files)
      … 3 files under this directory
    icons/  (1 files)
      … 1 files under this directory
    init/  (1 files)
      … 1 files under this directory
    layout/  (6 files)
      … 6 files under this directory
    perm/  (1 files)
      … 1 files under this directory
    request/  (12 files)
      … 12 files under this directory
    router/  (1 files)
      … 1 files under this directory
    store/  (10 files)
      … 10 files under this directory
    utils/  (9 files)
      … 9 files under this directory
    views/  (15 files)
      … 15 files under this directory
    App.vue
    main.js
    style.css
  index.html
  jsconfig.json
  package.json
  pnpm-workspace.yaml
  vite.config.js
mail-worker/  (93 files)
  src/  (83 files)
    api/  (18 files)
      … 18 files under this directory
    const/  (3 files)
      … 3 files under this directory
    dao/  (1 files)
      … 1 files under this directory
    email/  (1 files)
      … 1 files under this directory
    entity/  (13 files)
      … 13 files under this directory
    error/  (1 files)
      … 1 files under this directory
    hono/  (2 files)
      … 2 files under this directory
    i18n/  (3 files)
      … 3 files under this directory
    init/  (1 files)
      … 1 files under this directory
    lib/  (1 files)
      … 1 files under this directory
    model/  (1 files)
      … 1 files under this directory
    security/  (2 files)
      … 2 files under this directory
    service/  (22 files)
      … 22 files under this directory
    template/  (3 files)
      … 3 files under this directory
    utils/  (10 files)
      … 10 files under this directory
    index.js
  test/  (1 files)
    index.spec.js
  .editorconfig
  .prettierrc
  package.json
  pnpm-workspace.yaml
  vitest.config.js
  wrangler-action.toml
  wrangler-dev.toml
  wrangler-test.toml
  wrangler.toml
.gitignore
LICENSE
README-en.md
README-ja.md
README.md
```

## Entry points

- [mail-vue/src/axios/index.js](https://github.com/maillab/cloud-mail/blob/a792cdcd5c3291ac718b97489b1be19367121969/mail-vue/src/axios/index.js)
- [mail-vue/src/echarts/index.js](https://github.com/maillab/cloud-mail/blob/a792cdcd5c3291ac718b97489b1be19367121969/mail-vue/src/echarts/index.js)
- [mail-vue/src/i18n/index.js](https://github.com/maillab/cloud-mail/blob/a792cdcd5c3291ac718b97489b1be19367121969/mail-vue/src/i18n/index.js)
- [mail-vue/src/icons/index.js](https://github.com/maillab/cloud-mail/blob/a792cdcd5c3291ac718b97489b1be19367121969/mail-vue/src/icons/index.js)
- [mail-vue/src/main.js](https://github.com/maillab/cloud-mail/blob/a792cdcd5c3291ac718b97489b1be19367121969/mail-vue/src/main.js)
- [mail-vue/src/router/index.js](https://github.com/maillab/cloud-mail/blob/a792cdcd5c3291ac718b97489b1be19367121969/mail-vue/src/router/index.js)
- [mail-worker/src/index.js](https://github.com/maillab/cloud-mail/blob/a792cdcd5c3291ac718b97489b1be19367121969/mail-worker/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 32 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 10 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). |
| mail-vue package | library | Observed | Groups 127 file(s) under mail-vue package (observed from repository paths and static analysis). |
| mail-worker package | library | Observed | Groups 44 file(s) under mail-worker package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 22 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 2 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/deploy-cloudflare.yml` (ci)
- `mail-vue/jsconfig.json` (config)
- `mail-vue/package.json` (manifest)
- `mail-vue/pnpm-workspace.yaml` (config)
- `mail-worker/.editorconfig` (config)
- `mail-worker/package.json` (manifest)
- `mail-worker/pnpm-workspace.yaml` (config)
- `mail-worker/wrangler-action.toml` (config)
- `mail-worker/wrangler-dev.toml` (config)
- `mail-worker/wrangler-test.toml` (config)
- `mail-worker/wrangler.toml` (config)

## Top-level layout

- `mail-vue` — 154 analysed file(s)
- `mail-worker` — 93 analysed file(s)
- `(root files)` — 5 analysed file(s)
- `.github` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 27 file(s) were skipped during inventory (22 x generated/minified file excluded; 3 x likely secret file excluded; 2 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `a792cdcd5c3291ac718b97489b1be19367121969` is the revision these paths and observations refer to.
