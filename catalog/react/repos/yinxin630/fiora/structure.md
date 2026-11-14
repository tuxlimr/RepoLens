# Project structure: yinxin630/fiora

**Analysed commit:** `d741c006c5a0a5b904dec742ac09dbc51bd7860d`

**Commit reference:** [d741c006c5a0a5b904dec742ac09dbc51bd7860d](https://github.com/yinxin630/fiora/commit/d741c006c5a0a5b904dec742ac09dbc51bd7860d)

**Tree at this commit:** [yinxin630/fiora@d741c006c5a0](https://github.com/yinxin630/fiora/tree/d741c006c5a0a5b904dec742ac09dbc51bd7860d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | yinxin630/fiora |
| Description | An interesting open source chat application. Developed with node.js, mongoDB, socket.io and react |
| Stars | 7155 |
| Forks | 1403 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `d741c006c5a0a5b904dec742ac09dbc51bd7860d` |
| Retrieved at | 2026-11-14T19:13:59.935284+00:00 |
| Files in this snapshot | 320 |

## Directory tree

```text
.github/  (4 files)
  workflows/  (4 files)
    codeql-analysis.yml
    lint.yml
    test.yml
    ts.yml
.vscode/  (1 files)
  settings.json
packages/  (299 files)
  app/  (62 files)
    src/  (53 files)
      … 53 files under this directory
    tests/  (1 files)
      … 1 files under this directory
    .babelrc
    .eslintrc
    .gitignore
    .watchmanconfig
    App.tsx
    app.json
    package.json
    tsconfig.json
  assets/  (1 files)
    package.json
  bin/  (11 files)
    scripts/  (8 files)
      … 8 files under this directory
    index.ts
    package.json
    tsconfig.json
  config/  (3 files)
    client.ts
    package.json
    server.ts
  database/  (12 files)
    mongoose/  (9 files)
      … 9 files under this directory
    redis/  (1 files)
      … 1 files under this directory
    package.json
    tsconfig.json
  docs/  (43 files)
    docs/  (8 files)
      … 8 files under this directory
    i18n/  (22 files)
      … 22 files under this directory
    src/  (3 files)
      … 3 files under this directory
    static/  (5 files)
      … 5 files under this directory
    .gitignore
    babel.config.js
    docusaurus.config.js
    package.json
    sidebars.js
  i18n/  (6 files)
    en-US/  (2 files)
      … 2 files under this directory
    zh-CN/  (2 files)
      … 2 files under this directory
    node.index.ts
    package.json
  server/  (26 files)
    public/  (3 files)
      … 3 files under this directory
    src/  (15 files)
      … 15 files under this directory
    test/  (5 files)
      … 5 files under this directory
    .nodemonrc
    package.json
    tsconfig.json
  utils/  (17 files)
    test/  (2 files)
      … 2 files under this directory
    compressImage.ts
    const.ts
    convertMessage.ts
    expressions.ts
    getFriendId.ts
    getRandomAvatar.ts
    getRandomColor.ts
    logger.ts
    package.json
    sleep.ts
    socket.ts
    time.ts
    ua.ts
    url.ts
    xss.ts
  web/  (118 files)
    src/  (111 files)
      … 111 files under this directory
    test/  (4 files)
      … 4 files under this directory
    .babelrc
    package.json
    tsconfig.json
.dockerignore
.eslintignore
.eslintrc
.gitignore
.prettierrc
Dockerfile
LICENSE
README.md
docker-compose.yaml
index.ts
jest.config.js
jest.setup.js
jest.transformer.js
lerna.json
package.json
tsconfig.json
```

## Entry points

- [index.ts](https://github.com/yinxin630/fiora/blob/d741c006c5a0a5b904dec742ac09dbc51bd7860d/index.ts)
- [packages/app/App.tsx](https://github.com/yinxin630/fiora/blob/d741c006c5a0a5b904dec742ac09dbc51bd7860d/packages/app/App.tsx)
- [packages/app/src/App.tsx](https://github.com/yinxin630/fiora/blob/d741c006c5a0a5b904dec742ac09dbc51bd7860d/packages/app/src/App.tsx)
- [packages/bin/index.ts](https://github.com/yinxin630/fiora/blob/d741c006c5a0a5b904dec742ac09dbc51bd7860d/packages/bin/index.ts)
- [packages/config/server.ts](https://github.com/yinxin630/fiora/blob/d741c006c5a0a5b904dec742ac09dbc51bd7860d/packages/config/server.ts)
- [packages/database/mongoose/index.ts](https://github.com/yinxin630/fiora/blob/d741c006c5a0a5b904dec742ac09dbc51bd7860d/packages/database/mongoose/index.ts)
- [packages/i18n/en-US/index.ts](https://github.com/yinxin630/fiora/blob/d741c006c5a0a5b904dec742ac09dbc51bd7860d/packages/i18n/en-US/index.ts)
- [packages/i18n/zh-CN/index.ts](https://github.com/yinxin630/fiora/blob/d741c006c5a0a5b904dec742ac09dbc51bd7860d/packages/i18n/zh-CN/index.ts)
- [packages/server/src/app.ts](https://github.com/yinxin630/fiora/blob/d741c006c5a0a5b904dec742ac09dbc51bd7860d/packages/server/src/app.ts)
- [packages/server/src/main.ts](https://github.com/yinxin630/fiora/blob/d741c006c5a0a5b904dec742ac09dbc51bd7860d/packages/server/src/main.ts)
- [packages/web/src/App.tsx](https://github.com/yinxin630/fiora/blob/d741c006c5a0a5b904dec742ac09dbc51bd7860d/packages/web/src/App.tsx)
- [packages/web/src/main.tsx](https://github.com/yinxin630/fiora/blob/d741c006c5a0a5b904dec742ac09dbc51bd7860d/packages/web/src/main.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 6 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 30 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 10 file(s) under data layer (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 164 file(s) under packages package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 12 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.github/workflows/codeql-analysis.yml` (ci)
- `.github/workflows/lint.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `.github/workflows/ts.yml` (ci)
- `.vscode/settings.json` (config)
- `Dockerfile` (container)
- `docker-compose.yaml` (container)
- `lerna.json` (config)
- `package.json` (manifest)
- `packages/app/app.json` (config)
- `packages/app/package.json` (manifest)
- `packages/app/tsconfig.json` (config)
- `packages/assets/package.json` (manifest)
- `packages/bin/package.json` (manifest)
- `packages/bin/tsconfig.json` (config)
- `packages/config/package.json` (manifest)
- `packages/database/package.json` (manifest)
- `packages/database/tsconfig.json` (config)
- `packages/docs/i18n/en/code.json` (config)
- `packages/docs/i18n/en/docusaurus-theme-classic/footer.json` (config)
- `packages/docs/i18n/en/docusaurus-theme-classic/navbar.json` (config)
- `packages/docs/i18n/zh-Hans/code.json` (config)
- `packages/docs/i18n/zh-Hans/docusaurus-theme-classic/footer.json` (config)
- `packages/docs/i18n/zh-Hans/docusaurus-theme-classic/navbar.json` (config)
- `packages/docs/package.json` (manifest)
- `packages/i18n/package.json` (manifest)
- `packages/server/package.json` (manifest)
- `packages/server/public/manifest.json` (config)
- `packages/server/tsconfig.json` (config)
- `packages/utils/package.json` (manifest)
- `packages/web/package.json` (manifest)
- `packages/web/tsconfig.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `packages` — 299 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `.github` — 4 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 9 file(s) were skipped during inventory (6 x lockfile excluded; 3 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `d741c006c5a0a5b904dec742ac09dbc51bd7860d` is the revision these paths and observations refer to.
