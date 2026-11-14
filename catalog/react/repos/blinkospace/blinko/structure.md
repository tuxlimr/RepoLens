# Project structure: blinkospace/blinko

**Analysed commit:** `a1c71e67f653f88aabee93c6e5dc433ef5780d18`

**Commit reference:** [a1c71e67f653f88aabee93c6e5dc433ef5780d18](https://github.com/blinkospace/blinko/commit/a1c71e67f653f88aabee93c6e5dc433ef5780d18)

**Tree at this commit:** [blinkospace/blinko@a1c71e67f653](https://github.com/blinkospace/blinko/tree/a1c71e67f653f88aabee93c6e5dc433ef5780d18)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | blinkospace/blinko |
| Description | An open-source, self-hosted personal AI note tool prioritizing privacy, built using TypeScript . |
| Stars | 11204 |
| Forks | 804 |
| Licence | GPL-3.0 |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `a1c71e67f653f88aabee93c6e5dc433ef5780d18` |
| Retrieved at | 2026-11-14T19:13:26.712024+00:00 |
| Files in this snapshot | 559 |

## Directory tree

```text
.github/  (12 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  changelog/  (1 files)
    changelog.js
  workflows/  (8 files)
    app-release.yml
    build-publish-release.yml
    docker-build.yml
    mark-stable.yml
    security-checks.yml
    test-telegram-notification.yml
    translator.yml
    windows-test-release.yml
  FUNDING.yml
app/  (340 files)
  public/  (21 files)
    locales/  (17 files)
      … 17 files under this directory
    image-fallback.svg
    manifest.json
    run-on-pikapods.svg
    run-on-zimaos-v2.svg
  src/  (226 files)
    assets/  (1 files)
      … 1 files under this directory
    components/  (149 files)
      … 149 files under this directory
    hooks/  (5 files)
      … 5 files under this directory
    lib/  (17 files)
      … 17 files under this directory
    pages/  (19 files)
      … 19 files under this directory
    store/  (27 files)
      … 27 files under this directory
    styles/  (5 files)
      … 5 files under this directory
    App.tsx
    main.tsx
    vite-env.d.ts
  src-tauri/  (55 files)
    capabilities/  (3 files)
      … 3 files under this directory
    gen/  (36 files)
      … 36 files under this directory
    src/  (9 files)
      … 9 files under this directory
    .gitignore
    Cargo.toml
    build.rs
    tauri.android.conf.json
    tauri.conf.json
    tauri.cuda.conf.json
    tauri.ios.conf.json
  tauri-plugin-blinko/  (30 files)
    android/  (9 files)
      … 9 files under this directory
    dist-js/  (3 files)
      … 3 files under this directory
    guest-js/  (1 files)
      … 1 files under this directory
    permissions/  (4 files)
      … 4 files under this directory
    src/  (6 files)
      … 6 files under this directory
    .gitignore
    Cargo.toml
    README.md
    build.rs
    package.json
    rollup.config.js
    tsconfig.json
  .gitignore
  README.md
  index.html
  package.json
  tailwind.config.js
  tsconfig.json
  tsconfig.node.json
  vite.config.ts
blinko-types/  (1 files)
  package.json
docs/  (2 files)
  security-remediation.md
  security-upgrade.md
helm/  (14 files)
  charts/  (1 files)
    .gitignore
  templates/  (8 files)
    NOTES.txt
    _helpers.tpl
    configmap.yaml
    deployment.yaml
    hpa.yaml
    ingress.yaml
    service.yaml
    serviceaccount.yaml
  .helmignore
  Chart.lock
  Chart.yaml
  README.md
  values.yaml
prisma/  (40 files)
  migrations/  (31 files)
    20241026033301_0_0_1/  (1 files)
      … 1 files under this directory
    20241027072348_0_0_3/  (1 files)
      … 1 files under this directory
    20241112084821_0_2_9/  (1 files)
      … 1 files under this directory
    20241121082228_0_6_0/  (1 files)
      … 1 files under this directory
    20241202103221_0_12_11/  (1 files)
      … 1 files under this directory
    20241205035247_18_0_1/  (1 files)
      … 1 files under this directory
    20241212033352_0_23_3/  (1 files)
      … 1 files under this directory
    20241218023101_0_27_0/  (1 files)
      … 1 files under this directory
    20241219062514_0_27_7/  (1 files)
      … 1 files under this directory
    20241226141834_0_30_7/  (1 files)
      … 1 files under this directory
    20241231014246_0_32_0/  (1 files)
      … 1 files under this directory
    20250101032000_0_32_4/  (1 files)
      … 1 files under this directory
    20250108081202_0_34_0/  (1 files)
      … 1 files under this directory
    20250110011520_0_34_13/  (1 files)
      … 1 files under this directory
    20250110022717_0_34_15/  (1 files)
      … 1 files under this directory
    20250110105226_0_36_0/  (1 files)
      … 1 files under this directory
    20250115050059_0_37_0/  (1 files)
      … 1 files under this directory
    20250116052731_0_37_4/  (1 files)
      … 1 files under this directory
    20250219083523_0_39_0/  (1 files)
      … 1 files under this directory
    20250222125610_0_41_0/  (1 files)
      … 1 files under this directory
    20250306102203_0_42_4/  (1 files)
      … 1 files under this directory
    20250331072252_0_48_0/  (1 files)
      … 1 files under this directory
    20250418115430_1_0_0/  (1 files)
      … 1 files under this directory
    20250529145705_1_0_4/  (1 files)
      … 1 files under this directory
    20250921064614_1_5_0/  (1 files)
      … 1 files under this directory
    20250922040757_1_5_1/  (1 files)
      … 1 files under this directory
    20250930000000_add_sort_order_to_notes/  (1 files)
      … 1 files under this directory
    20251221120939_add_mcp_servers/  (1 files)
      … 1 files under this directory
    20251221193000_pg_boss_migration/  (1 files)
      … 1 files under this directory
    20251231140909_add_fonts_table/  (1 files)
      … 1 files under this directory
    migration_lock.toml
  seedfiles/  (1 files)
    story.txt
  defaultFonts.ts
  resetpassword.ts
  schema.prisma
  seed.d.ts
  seed.ts
  seedData.d.ts
  seedData.ts
  tsconfig.json
server/  (116 files)
  __tests__/  (20 files)
    e2e/  (1 files)
      … 1 files under this directory
    integration/  (1 files)
      … 1 files under this directory
    security/  (16 files)
      … 16 files under this directory
    unit/  (2 files)
      … 2 files under this directory
  aiServer/  (22 files)
    mcp/  (3 files)
      … 3 files under this directory
    providers/  (8 files)
      … 8 files under this directory
    tools/  (8 files)
      … 8 files under this directory
    aiModelFactory.ts
    index.ts
    types.ts
  jobs/  (14 files)
    aiScheduledTaskJob.ts
    archivejob.d.ts
    archivejob.ts
    baseScheduleJob.d.ts
    baseScheduleJob.ts
    dbjob.d.ts
    dbjob.ts
    markdownJob.ts
    memosJob.d.ts
    memosJob.ts
    rebuildEmbeddingJob.d.ts
    rebuildEmbeddingJob.ts
    recommandJob.d.ts
    recommandJob.ts
  lib/  (16 files)
    attachmentBinding.ts
    attachmentShare.ts
    commentWebhook.ts
    conversationAccess.ts
    exportDownload.ts
    fileAccessPolicy.ts
    files.ts
    helper.ts
    mcpStdioPolicy.ts
    pgBoss.ts
    pluginPaths.ts
    providerVisibility.ts
    proxy.ts
    publicHttp.ts
    spotify.ts
    twoFactorLogin.ts
  middleware/  (1 files)
    index.ts
  routerExpress/  (11 files)
    auth/  (2 files)
      … 2 files under this directory
    file/  (6 files)
      … 6 files under this directory
    mcp.ts
    openai.ts
    rss.ts
  routerTrpc/  (19 files)
    _app.ts
    ai.ts
    aiScheduledTask.ts
    analytics.ts
    attachment.ts
    comment.ts
    config.ts
    conversation.ts
    follows.ts
    font.ts
    mcpServers.ts
    message.ts
    note.ts
    notification.ts
    plugin.ts
    public.ts
    tag.ts
    task.ts
    user.ts
  scripts/  (1 files)
    test-security.ts
  types/  (2 files)
    express.d.ts
    trpc.d.ts
  vditor/  (2 files)
    js/  (2 files)
      … 2 files under this directory
  context.ts
  esbuild.config.ts
  index.ts
  package.json
  prisma.ts
  swagger.ts
  tsconfig.json
  tsconfig.trpc.json
shared/  (13 files)
  lib/  (10 files)
    __tests__/  (1 files)
      … 1 files under this directory
    cache.ts
    dayjs.ts
    helper.ts
    lodash.ts
    modelTemplates.ts
    pathConstant.ts
    prismaZodType.ts
    sharedConstant.ts
    types.ts
  index.ts
  package.json
  tsconfig.json
test-docker/  (3 files)
  mock-openai/  (1 files)
    server.js
  README.md
  docker-compose.test.yml
.dockerignore
.gitignore
CLAUDE.md
DEV.md
LICENSE
README.md
README.zh-CN.md
SECURITY.md
docker-compose.prod.yml
docker-compose.yml
dockerfile
install.sh
package.json
tsconfig.blinko.json
tsconfig.json
tsconfig.node.json
turbo.json
update.sh
```

## Entry points

- [app/tauri-plugin-blinko/dist-js/index.cjs](https://github.com/blinkospace/blinko/blob/a1c71e67f653f88aabee93c6e5dc433ef5780d18/app/tauri-plugin-blinko/dist-js/index.cjs)
- [shared/index.ts](https://github.com/blinkospace/blinko/blob/a1c71e67f653f88aabee93c6e5dc433ef5780d18/shared/index.ts)
- [app/src/App.tsx](https://github.com/blinkospace/blinko/blob/a1c71e67f653f88aabee93c6e5dc433ef5780d18/app/src/App.tsx)
- [app/src/main.tsx](https://github.com/blinkospace/blinko/blob/a1c71e67f653f88aabee93c6e5dc433ef5780d18/app/src/main.tsx)
- [app/src/pages/index.tsx](https://github.com/blinkospace/blinko/blob/a1c71e67f653f88aabee93c6e5dc433ef5780d18/app/src/pages/index.tsx)
- [app/src/store/index.ts](https://github.com/blinkospace/blinko/blob/a1c71e67f653f88aabee93c6e5dc433ef5780d18/app/src/store/index.ts)
- [app/tauri-plugin-blinko/dist-js/index.js](https://github.com/blinkospace/blinko/blob/a1c71e67f653f88aabee93c6e5dc433ef5780d18/app/tauri-plugin-blinko/dist-js/index.js)
- [app/tauri-plugin-blinko/guest-js/index.ts](https://github.com/blinkospace/blinko/blob/a1c71e67f653f88aabee93c6e5dc433ef5780d18/app/tauri-plugin-blinko/guest-js/index.ts)
- [server/aiServer/index.ts](https://github.com/blinkospace/blinko/blob/a1c71e67f653f88aabee93c6e5dc433ef5780d18/server/aiServer/index.ts)
- [server/aiServer/mcp/index.ts](https://github.com/blinkospace/blinko/blob/a1c71e67f653f88aabee93c6e5dc433ef5780d18/server/aiServer/mcp/index.ts)
- [server/aiServer/providers/index.ts](https://github.com/blinkospace/blinko/blob/a1c71e67f653f88aabee93c6e5dc433ef5780d18/server/aiServer/providers/index.ts)
- [server/index.ts](https://github.com/blinkospace/blinko/blob/a1c71e67f653f88aabee93c6e5dc433ef5780d18/server/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| app package | library | Observed | Groups 243 file(s) under app package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 61 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 1 file(s) under external integrations (observed from repository paths and static analysis). |
| prisma package | library | Observed | Groups 6 file(s) under prisma package (observed from repository paths and static analysis). |
| server package | library | Observed | Groups 112 file(s) under server package (observed from repository paths and static analysis). |
| shared package | library | Observed | Groups 11 file(s) under shared package (observed from repository paths and static analysis). |
| test-docker package | library | Observed | Groups 1 file(s) under test-docker package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.github/FUNDING.yml` (config)
- `.github/workflows/app-release.yml` (ci)
- `.github/workflows/build-publish-release.yml` (ci)
- `.github/workflows/docker-build.yml` (ci)
- `.github/workflows/mark-stable.yml` (ci)
- `.github/workflows/security-checks.yml` (ci)
- `.github/workflows/test-telegram-notification.yml` (ci)
- `.github/workflows/translator.yml` (ci)
- `.github/workflows/windows-test-release.yml` (ci)
- `app/package.json` (manifest)
- `app/public/locales/ar/translation.json` (config)
- `app/public/locales/de/translation.json` (config)
- `app/public/locales/en/translation.json` (config)
- `app/public/locales/es/translation.json` (config)
- `app/public/locales/fr/translation.json` (config)
- `app/public/locales/ja/translation.json` (config)
- `app/public/locales/ka/translation.json` (config)
- `app/public/locales/kab/translation.json` (config)
- `app/public/locales/ko/translation.json` (config)
- `app/public/locales/nl/translation.json` (config)
- `app/public/locales/pl/translation.json` (config)
- `app/public/locales/pt/translation.json` (config)
- `app/public/locales/ru/translation.json` (config)
- `app/public/locales/tr/translation.json` (config)
- `app/public/locales/uk/translation.json` (config)
- `app/public/locales/zh-TW/translation.json` (config)
- `app/public/locales/zh/translation.json` (config)
- `app/public/manifest.json` (config)
- `app/src-tauri/Cargo.toml` (manifest)
- `app/src-tauri/capabilities/default.json` (config)
- `app/src-tauri/capabilities/desktop.json` (config)
- `app/src-tauri/capabilities/mobile.json` (config)
- `app/src-tauri/gen/android/.editorconfig` (config)
- `app/src-tauri/tauri.android.conf.json` (config)
- `app/src-tauri/tauri.conf.json` (config)
- `app/src-tauri/tauri.cuda.conf.json` (config)
- `app/src-tauri/tauri.ios.conf.json` (config)
- `app/tauri-plugin-blinko/Cargo.toml` (manifest)
- `app/tauri-plugin-blinko/package.json` (manifest)
- `app/tauri-plugin-blinko/permissions/autogenerated/commands/setColor.toml` (config)
- `app/tauri-plugin-blinko/permissions/default.toml` (config)
- `app/tauri-plugin-blinko/permissions/schemas/schema.json` (config)
- `app/tauri-plugin-blinko/tsconfig.json` (config)
- `app/tsconfig.json` (config)
- `app/tsconfig.node.json` (config)
- `blinko-types/package.json` (manifest)
- `docker-compose.prod.yml` (config)
- `docker-compose.yml` (container)
- `dockerfile` (container)
- `helm/Chart.yaml` (config)
- `helm/templates/configmap.yaml` (config)
- `helm/templates/deployment.yaml` (config)
- `helm/templates/hpa.yaml` (config)
- `helm/templates/ingress.yaml` (config)
- `helm/templates/service.yaml` (config)
- `helm/templates/serviceaccount.yaml` (config)
- `helm/values.yaml` (config)
- `package.json` (manifest)
- `prisma/migrations/migration_lock.toml` (config)
- `prisma/tsconfig.json` (config)
- `server/package.json` (manifest)
- `server/tsconfig.json` (config)
- `server/tsconfig.trpc.json` (config)
- `shared/package.json` (manifest)
- `shared/tsconfig.json` (config)
- `test-docker/docker-compose.test.yml` (config)
- `tsconfig.blinko.json` (config)
- `tsconfig.json` (config)
- `tsconfig.node.json` (config)
- `turbo.json` (config)

## Top-level layout

- `app` — 340 analysed file(s)
- `server` — 116 analysed file(s)
- `prisma` — 40 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `helm` — 14 analysed file(s)
- `shared` — 13 analysed file(s)
- `.github` — 12 analysed file(s)
- `test-docker` — 3 analysed file(s)
- `docs` — 2 analysed file(s)
- `blinko-types` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 6 file(s) were skipped during inventory (2 x generated/minified file excluded; 3 x likely secret file excluded; 1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `a1c71e67f653f88aabee93c6e5dc433ef5780d18` is the revision these paths and observations refer to.
