# Project structure: ts-rest/ts-rest

**Analysed commit:** `3d572e3336bd998b0c33a9d65b12292b158d0aec`

**Commit reference:** [3d572e3336bd998b0c33a9d65b12292b158d0aec](https://github.com/ts-rest/ts-rest/commit/3d572e3336bd998b0c33a9d65b12292b158d0aec)

**Tree at this commit:** [ts-rest/ts-rest@3d572e3336bd](https://github.com/ts-rest/ts-rest/tree/3d572e3336bd998b0c33a9d65b12292b158d0aec)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | ts-rest/ts-rest |
| Description | 🌄 - RPC-like client, contract, and server implementation for a pure REST API |
| Stars | 3340 |
| Forks | 183 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `3d572e3336bd998b0c33a9d65b12292b158d0aec` |
| Retrieved at | 2026-11-14T19:15:23.357920+00:00 |
| Files in this snapshot | 683 |

## Directory tree

```text
.changeset/  (13 files)
  README.md
  big-camels-complain.md
  config.json
  cuddly-lions-buy.md
  giant-dragons-burn.md
  khaki-scissors-doubt.md
  new-berries-camp.md
  odd-papayas-happen.md
  plenty-seahorses-wait.md
  rare-elephants-itch.md
  rich-coins-move.md
  shy-vans-float.md
  soft-dolls-leave.md
.github/  (3 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.yml
    config.yml
    feature_request.md
.vscode/  (2 files)
  extensions.json
  settings.json
apps/  (180 files)
  docs/  (1 files)
    content/  (1 files)
      … 1 files under this directory
  example-azure-function/  (12 files)
    src/  (2 files)
      … 2 files under this directory
    .eslintrc.json
    .funcignore
    .gitignore
    host.json
    jest.config.ts
    package.json
    project.json
    tsconfig.app.json
    tsconfig.json
    tsconfig.spec.json
  example-cloudflare-worker/  (10 files)
    src/  (2 files)
      … 2 files under this directory
    .eslintrc.json
    .gitignore
    jest.config.ts
    project.json
    tsconfig.app.json
    tsconfig.json
    tsconfig.spec.json
    wrangler.toml
  example-express/  (19 files)
    src/  (11 files)
      … 11 files under this directory
    .babelrc
    .eslintrc.json
    jest.config.ts
    package.json
    project.json
    tsconfig.app.json
    tsconfig.json
    tsconfig.spec.json
  example-fastify/  (10 files)
    src/  (4 files)
      … 4 files under this directory
    .eslintrc.json
    jest.config.ts
    project.json
    tsconfig.app.json
    tsconfig.json
    tsconfig.spec.json
  example-microservice/  (60 files)
    posts-service/  (12 files)
      … 12 files under this directory
    users-service/  (13 files)
      … 13 files under this directory
    web-app/  (11 files)
      … 11 files under this directory
    web-app-solid/  (11 files)
      … 11 files under this directory
    web-app-vue/  (13 files)
      … 13 files under this directory
  example-nest/  (23 files)
    src/  (14 files)
      … 14 files under this directory
    .babelrc
    .eslintrc.json
    jest.config.ts
    package.json
    project.json
    test.http
    tsconfig.app.json
    tsconfig.json
    tsconfig.spec.json
  example-next/  (45 files)
    app/  (14 files)
      … 14 files under this directory
    components/  (3 files)
      … 3 files under this directory
    contracts/  (1 files)
      … 1 files under this directory
    hooks/  (1 files)
      … 1 files under this directory
    pages/  (9 files)
      … 9 files under this directory
    public/  (1 files)
      … 1 files under this directory
    server/  (1 files)
      … 1 files under this directory
    tests/  (1 files)
      … 1 files under this directory
    .eslintrc.json
    index.d.ts
    jest.config.ts
    next-env.d.ts
    next.config.js
    package.json
    pages-tsr.ts
    postcss.config.js
    project.json
    state.ts
    tailwind.config.js
    test.http
    tsconfig.json
    tsconfig.spec.json
docs/  (45 files)
  app/  (6 files)
    (home)/  (2 files)
      … 2 files under this directory
    api/  (1 files)
      … 1 files under this directory
    global.css
    layout.config.tsx
    layout.tsx
  components/  (2 files)
    CookieBanner.tsx
    PostHogProvider.tsx
  content/  (24 files)
    docs/  (24 files)
      … 24 files under this directory
  lib/  (3 files)
    InstallTabs.tsx
    posthog.ts
    source.ts
  .gitignore
  README.md
  bun.lock
  generate-changelog.js
  mdx-components.tsx
  next.config.mjs
  package.json
  postcss.config.mjs
  source.config.ts
  tsconfig.json
libs/  (307 files)
  example-contracts/  (13 files)
    src/  (4 files)
      … 4 files under this directory
    .babelrc
    .eslintrc.json
    README.md
    jest.config.ts
    package.json
    project.json
    tsconfig.json
    tsconfig.lib.json
    tsconfig.spec.json
  example-microservice/  (22 files)
    util-posts-api/  (11 files)
      … 11 files under this directory
    util-users-api/  (11 files)
      … 11 files under this directory
  non-strict-mode-test/  (10 files)
    src/  (2 files)
      … 2 files under this directory
    .eslintrc.json
    README.md
    package.json
    project.json
    tsconfig.json
    tsconfig.lib.json
    tsconfig.spec.json
    vite.config.ts
  ts-rest/  (262 files)
    core/  (42 files)
      … 42 files under this directory
    express/  (18 files)
      … 18 files under this directory
    fastify/  (14 files)
      … 14 files under this directory
    nest/  (22 files)
      … 22 files under this directory
    next/  (19 files)
      … 19 files under this directory
    open-api/  (29 files)
      … 29 files under this directory
    react-query/  (19 files)
      … 19 files under this directory
    react-query-v5/  (28 files)
      … 28 files under this directory
    serverless/  (41 files)
      … 41 files under this directory
    solid-query/  (13 files)
      … 13 files under this directory
    vue-query/  (17 files)
      … 17 files under this directory
patches/  (1 files)
  @nx__rollup@17.1.1.patch
prisma/  (1 files)
  schema.prisma
test-projects/  (103 files)
  arktype/  (7 files)
    .gitignore
    Makefile
    bun.lock
    index.spec.ts
    index.ts
    package.json
    tsconfig.json
  express-4/  (7 files)
    .gitignore
    Makefile
    bun.lock
    index.spec.ts
    index.ts
    package.json
    tsconfig.json
  express-5/  (7 files)
    .gitignore
    Makefile
    bun.lock
    index.spec.ts
    index.ts
    package.json
    tsconfig.json
  nest-10/  (18 files)
    src/  (6 files)
      … 6 files under this directory
    test/  (2 files)
      … 2 files under this directory
    .eslintrc.js
    .gitignore
    .prettierrc
    Makefile
    README.md
    nest-cli.json
    package.json
    pnpm-workspace.yaml
    tsconfig.build.json
    tsconfig.json
  nest-11/  (18 files)
    src/  (6 files)
      … 6 files under this directory
    test/  (2 files)
      … 2 files under this directory
    .gitignore
    .prettierrc
    Makefile
    README.md
    eslint.config.mjs
    nest-cli.json
    package.json
    pnpm-workspace.yaml
    tsconfig.build.json
    tsconfig.json
  nest-9/  (18 files)
    src/  (6 files)
      … 6 files under this directory
    test/  (2 files)
      … 2 files under this directory
    .eslintrc.js
    .gitignore
    .prettierrc
    Makefile
    README.md
    nest-cli.json
    package.json
    pnpm-workspace.yaml
    tsconfig.build.json
    tsconfig.json
  no-validator/  (7 files)
    .gitignore
    Makefile
    bun.lock
    index.spec.ts
    index.ts
    package.json
    tsconfig.json
  valibot/  (7 files)
    .gitignore
    Makefile
    bun.lock
    index.spec.ts
    index.ts
    package.json
    tsconfig.json
  zod-3/  (7 files)
    .gitignore
    Makefile
    bun.lock
    index.spec.ts
    index.ts
    package.json
    tsconfig.json
  zod-4/  (7 files)
    .gitignore
    Makefile
    bun.lock
    index.spec.ts
    index.ts
    package.json
    tsconfig.json
tools/  (4 files)
  scripts/  (2 files)
    docs-redirects.ts
    rollup.config.js
  workflows/  (1 files)
    nx-affected.ts
  tsconfig.tools.json
.all-contributorsrc
.editorconfig
.eslintignore
.eslintrc.json
.gitignore
.nvmrc
.prettierignore
.prettierrc
CONTRIBUTING.md
LICENCE
Makefile
README.md
SECURITY.md
babel.config.json
docker-compose.yml
jest.config.ts
jest.preset.js
migrations.json
nx.json
package.json
pnpm-workspace.yaml
tsconfig.base.json
tsconfig.settings.json
typedoc.base.json
```

## Entry points

- [apps/example-cloudflare-worker/src/index.ts](https://github.com/ts-rest/ts-rest/blob/3d572e3336bd998b0c33a9d65b12292b158d0aec/apps/example-cloudflare-worker/src/index.ts)
- [apps/example-express/src/main.ts](https://github.com/ts-rest/ts-rest/blob/3d572e3336bd998b0c33a9d65b12292b158d0aec/apps/example-express/src/main.ts)
- [apps/example-fastify/src/main.ts](https://github.com/ts-rest/ts-rest/blob/3d572e3336bd998b0c33a9d65b12292b158d0aec/apps/example-fastify/src/main.ts)
- [apps/example-nest/src/main.ts](https://github.com/ts-rest/ts-rest/blob/3d572e3336bd998b0c33a9d65b12292b158d0aec/apps/example-nest/src/main.ts)
- [apps/example-next/pages/index.tsx](https://github.com/ts-rest/ts-rest/blob/3d572e3336bd998b0c33a9d65b12292b158d0aec/apps/example-next/pages/index.tsx)
- [libs/example-contracts/src/index.ts](https://github.com/ts-rest/ts-rest/blob/3d572e3336bd998b0c33a9d65b12292b158d0aec/libs/example-contracts/src/index.ts)
- [libs/non-strict-mode-test/src/index.ts](https://github.com/ts-rest/ts-rest/blob/3d572e3336bd998b0c33a9d65b12292b158d0aec/libs/non-strict-mode-test/src/index.ts)
- [test-projects/arktype/index.ts](https://github.com/ts-rest/ts-rest/blob/3d572e3336bd998b0c33a9d65b12292b158d0aec/test-projects/arktype/index.ts)
- [test-projects/express-4/index.ts](https://github.com/ts-rest/ts-rest/blob/3d572e3336bd998b0c33a9d65b12292b158d0aec/test-projects/express-4/index.ts)
- [test-projects/express-5/index.ts](https://github.com/ts-rest/ts-rest/blob/3d572e3336bd998b0c33a9d65b12292b158d0aec/test-projects/express-5/index.ts)
- [test-projects/nest-10/src/main.ts](https://github.com/ts-rest/ts-rest/blob/3d572e3336bd998b0c33a9d65b12292b158d0aec/test-projects/nest-10/src/main.ts)
- [test-projects/nest-11/src/main.ts](https://github.com/ts-rest/ts-rest/blob/3d572e3336bd998b0c33a9d65b12292b158d0aec/test-projects/nest-11/src/main.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 11 file(s) under api layer (observed from repository paths and static analysis). |
| apps package | library | Observed | Groups 85 file(s) under apps package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 200 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Inferred | Groups 0 file(s) under data layer (observed from repository paths and static analysis). |
| libs package | library | Observed | Groups 124 file(s) under libs package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 31 file(s) under service / domain layer (observed from repository paths and static analysis). |
| test-projects package | library | Observed | Groups 35 file(s) under test-projects package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 13 file(s) under tests (observed from repository paths and static analysis). |
| tools package | library | Observed | Groups 3 file(s) under tools package (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.editorconfig` (config)
- `.eslintrc.json` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.vscode/extensions.json` (config)
- `.vscode/settings.json` (config)
- `apps/example-azure-function/.eslintrc.json` (config)
- `apps/example-azure-function/host.json` (config)
- `apps/example-azure-function/package.json` (manifest)
- `apps/example-azure-function/project.json` (config)
- `apps/example-azure-function/tsconfig.app.json` (config)
- `apps/example-azure-function/tsconfig.json` (config)
- `apps/example-azure-function/tsconfig.spec.json` (config)
- `apps/example-cloudflare-worker/.eslintrc.json` (config)
- `apps/example-cloudflare-worker/project.json` (config)
- `apps/example-cloudflare-worker/tsconfig.app.json` (config)
- `apps/example-cloudflare-worker/tsconfig.json` (config)
- `apps/example-cloudflare-worker/tsconfig.spec.json` (config)
- `apps/example-cloudflare-worker/wrangler.toml` (config)
- `apps/example-express/.eslintrc.json` (config)
- `apps/example-express/package.json` (manifest)
- `apps/example-express/project.json` (config)
- `apps/example-express/src/http-client.env.json` (config)
- `apps/example-express/tsconfig.app.json` (config)
- `apps/example-express/tsconfig.json` (config)
- `apps/example-express/tsconfig.spec.json` (config)
- `apps/example-fastify/.eslintrc.json` (config)
- `apps/example-fastify/project.json` (config)
- `apps/example-fastify/tsconfig.app.json` (config)
- `apps/example-fastify/tsconfig.json` (config)
- `apps/example-fastify/tsconfig.spec.json` (config)
- `apps/example-microservice/posts-service/.eslintrc.json` (config)
- `apps/example-microservice/posts-service/project.json` (config)
- `apps/example-microservice/posts-service/tsconfig.app.json` (config)
- `apps/example-microservice/posts-service/tsconfig.json` (config)
- `apps/example-microservice/posts-service/tsconfig.spec.json` (config)
- `apps/example-microservice/users-service/.eslintrc.json` (config)
- `apps/example-microservice/users-service/project.json` (config)
- `apps/example-microservice/users-service/tsconfig.app.json` (config)
- `apps/example-microservice/users-service/tsconfig.json` (config)
- `apps/example-microservice/users-service/tsconfig.spec.json` (config)
- `apps/example-microservice/web-app-solid/package.json` (manifest)
- `apps/example-microservice/web-app-solid/project.json` (config)
- `apps/example-microservice/web-app-solid/tsconfig.json` (config)
- `apps/example-microservice/web-app-vue/package.json` (manifest)
- `apps/example-microservice/web-app-vue/project.json` (config)
- `apps/example-microservice/web-app-vue/tsconfig.json` (config)
- `apps/example-microservice/web-app/.eslintrc.json` (config)
- `apps/example-microservice/web-app/package.json` (manifest)
- `apps/example-microservice/web-app/project.json` (config)
- `apps/example-microservice/web-app/tsconfig.json` (config)
- `apps/example-microservice/web-app/tsconfig.spec.json` (config)
- `apps/example-nest/.eslintrc.json` (config)
- `apps/example-nest/package.json` (manifest)
- `apps/example-nest/project.json` (config)
- `apps/example-nest/tsconfig.app.json` (config)
- `apps/example-nest/tsconfig.json` (config)
- `apps/example-nest/tsconfig.spec.json` (config)
- `apps/example-next/.eslintrc.json` (config)
- `apps/example-next/package.json` (manifest)
- `apps/example-next/project.json` (config)
- `apps/example-next/tsconfig.json` (config)
- `apps/example-next/tsconfig.spec.json` (config)
- `babel.config.json` (config)
- `docker-compose.yml` (container)
- `docs/content/docs/client/meta.json` (config)
- `docs/content/docs/meta.json` (config)
- `docs/package.json` (manifest)
- `docs/tsconfig.json` (config)
- `libs/example-contracts/.eslintrc.json` (config)
- `libs/example-contracts/package.json` (manifest)
- `libs/example-contracts/project.json` (config)
- `libs/example-contracts/tsconfig.json` (config)
- `libs/example-contracts/tsconfig.lib.json` (config)
- `libs/example-contracts/tsconfig.spec.json` (config)
- `libs/example-microservice/util-posts-api/.eslintrc.json` (config)
- `libs/example-microservice/util-posts-api/package.json` (manifest)
- `libs/example-microservice/util-posts-api/project.json` (config)
- `libs/example-microservice/util-posts-api/tsconfig.json` (config)
- `libs/example-microservice/util-posts-api/tsconfig.lib.json` (config)
- `libs/example-microservice/util-posts-api/tsconfig.spec.json` (config)
- `libs/example-microservice/util-users-api/.eslintrc.json` (config)
- `libs/example-microservice/util-users-api/package.json` (manifest)
- `libs/example-microservice/util-users-api/project.json` (config)
- `libs/example-microservice/util-users-api/tsconfig.json` (config)
- `libs/example-microservice/util-users-api/tsconfig.lib.json` (config)
- `libs/example-microservice/util-users-api/tsconfig.spec.json` (config)
- `libs/non-strict-mode-test/.eslintrc.json` (config)
- `libs/non-strict-mode-test/package.json` (manifest)
- `libs/non-strict-mode-test/project.json` (config)
- `libs/non-strict-mode-test/tsconfig.json` (config)
- `libs/non-strict-mode-test/tsconfig.lib.json` (config)
- `libs/non-strict-mode-test/tsconfig.spec.json` (config)
- `libs/ts-rest/core/.eslintrc.json` (config)
- `libs/ts-rest/core/package.json` (manifest)
- `libs/ts-rest/core/project.json` (config)
- `libs/ts-rest/core/tsconfig.json` (config)
- `libs/ts-rest/core/tsconfig.lib.json` (config)
- `libs/ts-rest/core/tsconfig.spec.json` (config)
- `libs/ts-rest/core/typedoc.json` (config)
- `libs/ts-rest/express/.eslintrc.json` (config)
- `libs/ts-rest/express/package.json` (manifest)
- `libs/ts-rest/express/project.json` (config)
- `libs/ts-rest/express/tsconfig.json` (config)
- `libs/ts-rest/express/tsconfig.lib.json` (config)
- `libs/ts-rest/express/tsconfig.spec.json` (config)
- `libs/ts-rest/express/typedoc.json` (config)
- `libs/ts-rest/fastify/.eslintrc.json` (config)
- `libs/ts-rest/fastify/package.json` (manifest)
- `libs/ts-rest/fastify/project.json` (config)
- `libs/ts-rest/fastify/tsconfig.json` (config)
- `libs/ts-rest/fastify/tsconfig.lib.json` (config)
- `libs/ts-rest/fastify/tsconfig.spec.json` (config)
- `libs/ts-rest/fastify/typedoc.json` (config)
- `libs/ts-rest/nest/.eslintrc.json` (config)
- `libs/ts-rest/nest/package.json` (manifest)
- `libs/ts-rest/nest/project.json` (config)
- `libs/ts-rest/nest/tsconfig.json` (config)
- `libs/ts-rest/nest/tsconfig.lib.json` (config)
- `libs/ts-rest/nest/tsconfig.spec.json` (config)
- `libs/ts-rest/nest/typedoc.json` (config)
- `libs/ts-rest/next/.eslintrc.json` (config)
- `libs/ts-rest/next/package.json` (manifest)
- `libs/ts-rest/next/project.json` (config)
- `libs/ts-rest/next/tsconfig.json` (config)
- `libs/ts-rest/next/tsconfig.lib.json` (config)
- `libs/ts-rest/next/tsconfig.spec.json` (config)
- `libs/ts-rest/next/typedoc.json` (config)
- `libs/ts-rest/open-api/.eslintrc.json` (config)
- `libs/ts-rest/open-api/package.json` (manifest)
- `libs/ts-rest/open-api/project.json` (config)
- `libs/ts-rest/open-api/tsconfig.json` (config)
- `libs/ts-rest/open-api/tsconfig.lib.json` (config)
- `libs/ts-rest/open-api/tsconfig.spec.json` (config)
- `libs/ts-rest/open-api/typedoc.json` (config)
- `libs/ts-rest/react-query-v5/.eslintrc.json` (config)
- `libs/ts-rest/react-query-v5/package.json` (manifest)
- `libs/ts-rest/react-query-v5/project.json` (config)
- `libs/ts-rest/react-query-v5/tsconfig.json` (config)
- `libs/ts-rest/react-query-v5/tsconfig.lib.json` (config)
- `libs/ts-rest/react-query-v5/tsconfig.spec.json` (config)
- `libs/ts-rest/react-query-v5/typedoc.json` (config)
- `libs/ts-rest/react-query/.eslintrc.json` (config)
- `libs/ts-rest/react-query/package.json` (manifest)
- `libs/ts-rest/react-query/project.json` (config)
- `libs/ts-rest/react-query/tsconfig.json` (config)
- `libs/ts-rest/react-query/tsconfig.lib.json` (config)
- `libs/ts-rest/react-query/tsconfig.spec.json` (config)
- `libs/ts-rest/react-query/typedoc.json` (config)
- `libs/ts-rest/serverless/.eslintrc.json` (config)
- `libs/ts-rest/serverless/package.json` (manifest)
- `libs/ts-rest/serverless/project.json` (config)
- `libs/ts-rest/serverless/src/lib/mappers/aws/test-data/api-gateway-event-v1.json` (config)
- `libs/ts-rest/serverless/src/lib/mappers/aws/test-data/api-gateway-event-v2.json` (config)
- `libs/ts-rest/serverless/src/lib/mappers/aws/test-data/api-gateway-post-event-v1.json` (config)
- `libs/ts-rest/serverless/src/lib/mappers/aws/test-data/api-gateway-post-event-v2.json` (config)
- `libs/ts-rest/serverless/tsconfig.json` (config)
- `libs/ts-rest/serverless/tsconfig.lib.json` (config)
- `libs/ts-rest/serverless/tsconfig.spec.json` (config)
- `libs/ts-rest/solid-query/.eslintrc.json` (config)
- `libs/ts-rest/solid-query/package.json` (manifest)
- `libs/ts-rest/solid-query/project.json` (config)
- `libs/ts-rest/solid-query/tsconfig.json` (config)
- `libs/ts-rest/solid-query/tsconfig.lib.json` (config)
- `libs/ts-rest/solid-query/tsconfig.spec.json` (config)
- `libs/ts-rest/solid-query/typedoc.json` (config)
- `libs/ts-rest/vue-query/.eslintrc.json` (config)
- `libs/ts-rest/vue-query/package.json` (manifest)
- `libs/ts-rest/vue-query/project.json` (config)
- `libs/ts-rest/vue-query/tsconfig.json` (config)
- `libs/ts-rest/vue-query/tsconfig.lib.json` (config)
- `libs/ts-rest/vue-query/tsconfig.spec.json` (config)
- `libs/ts-rest/vue-query/typedoc.json` (config)
- `migrations.json` (config)
- `nx.json` (config)
- `package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `test-projects/arktype/package.json` (manifest)
- `test-projects/arktype/tsconfig.json` (config)
- `test-projects/express-4/package.json` (manifest)
- `test-projects/express-4/tsconfig.json` (config)
- `test-projects/express-5/package.json` (manifest)
- `test-projects/express-5/tsconfig.json` (config)
- `test-projects/nest-10/nest-cli.json` (config)
- `test-projects/nest-10/package.json` (manifest)
- `test-projects/nest-10/pnpm-workspace.yaml` (config)
- `test-projects/nest-10/tsconfig.build.json` (config)
- `test-projects/nest-10/tsconfig.json` (config)
- `test-projects/nest-11/nest-cli.json` (config)
- `test-projects/nest-11/package.json` (manifest)
- `test-projects/nest-11/pnpm-workspace.yaml` (config)
- `test-projects/nest-11/tsconfig.build.json` (config)
- `test-projects/nest-11/tsconfig.json` (config)
- `test-projects/nest-9/nest-cli.json` (config)
- `test-projects/nest-9/package.json` (manifest)
- `test-projects/nest-9/pnpm-workspace.yaml` (config)
- `test-projects/nest-9/tsconfig.build.json` (config)
- `test-projects/nest-9/tsconfig.json` (config)
- `test-projects/no-validator/package.json` (manifest)
- `test-projects/no-validator/tsconfig.json` (config)
- `test-projects/valibot/package.json` (manifest)
- `test-projects/valibot/tsconfig.json` (config)
- `test-projects/zod-3/package.json` (manifest)
- `test-projects/zod-3/tsconfig.json` (config)
- `test-projects/zod-4/package.json` (manifest)
- `test-projects/zod-4/tsconfig.json` (config)
- `tools/tsconfig.tools.json` (config)
- `tsconfig.base.json` (config)
- `tsconfig.settings.json` (config)
- `typedoc.base.json` (config)

## Top-level layout

- `libs` — 307 analysed file(s)
- `apps` — 180 analysed file(s)
- `test-projects` — 103 analysed file(s)
- `docs` — 45 analysed file(s)
- `(root files)` — 24 analysed file(s)
- `.changeset` — 13 analysed file(s)
- `tools` — 4 analysed file(s)
- `.github` — 3 analysed file(s)
- `.vscode` — 2 analysed file(s)
- `patches` — 1 analysed file(s)
- `prisma` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (1 x likely secret file excluded; 1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `3d572e3336bd998b0c33a9d65b12292b158d0aec` is the revision these paths and observations refer to.
