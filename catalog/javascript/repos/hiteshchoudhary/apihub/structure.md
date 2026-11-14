# Project structure: hiteshchoudhary/apihub

**Analysed commit:** `3163bf09d9ee23e29378c402ae4d581e544d6c9f`

**Commit reference:** [3163bf09d9ee23e29378c402ae4d581e544d6c9f](https://github.com/hiteshchoudhary/apihub/commit/3163bf09d9ee23e29378c402ae4d581e544d6c9f)

**Tree at this commit:** [hiteshchoudhary/apihub@3163bf09d9ee](https://github.com/hiteshchoudhary/apihub/tree/3163bf09d9ee23e29378c402ae4d581e544d6c9f)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | hiteshchoudhary/apihub |
| Description | Your own API Hub to learn and master API interaction. Ideal for frontend, mobile dev and backend developers.  |
| Stars | 9869 |
| Forks | 1518 |
| Licence | Other |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `3163bf09d9ee23e29378c402ae4d581e544d6c9f` |
| Retrieved at | 2026-11-14T19:12:48.086186+00:00 |
| Files in this snapshot | 550 |

## Directory tree

```text
.github/  (5 files)
  ISSUE_TEMPLATE/  (5 files)
    bug_report.yaml
    code_coverage.yaml
    config.yml
    feature_request.yaml
    frontend_contribution.yaml
.husky/  (2 files)
  commit-msg
  pre-commit
e2e/  (10 files)
  routes/  (7 files)
    apps/  (1 files)
      … 1 files under this directory
    seeds/  (5 files)
      … 5 files under this directory
    healthcheck.test.js
  common.js
  db.js
  test-server.js
examples/  (372 files)
  apps/  (293 files)
    auth/  (1 files)
      … 1 files under this directory
    chat-app/  (37 files)
      … 37 files under this directory
    ecommerce/  (223 files)
      … 223 files under this directory
    social-media/  (1 files)
      … 1 files under this directory
    todo/  (31 files)
      … 31 files under this directory
  kitchen-sink/  (69 files)
    cookies/  (1 files)
      … 1 files under this directory
    httpmethods/  (1 files)
      … 1 files under this directory
    images/  (1 files)
      … 1 files under this directory
    redirects/  (1 files)
      … 1 files under this directory
    requestinspections/  (1 files)
      … 1 files under this directory
    responseinspections/  (1 files)
      … 1 files under this directory
    statuscodes/  (63 files)
      … 63 files under this directory
  public/  (10 files)
    books/  (1 files)
      … 1 files under this directory
    cats/  (1 files)
      … 1 files under this directory
    dogs/  (1 files)
      … 1 files under this directory
    meals/  (1 files)
      … 1 files under this directory
    quotes/  (1 files)
      … 1 files under this directory
    randomjokes/  (1 files)
      … 1 files under this directory
    randomproducts/  (1 files)
      … 1 files under this directory
    randomusers/  (1 files)
      … 1 files under this directory
    stocks/  (1 files)
      … 1 files under this directory
    youtube/  (1 files)
      … 1 files under this directory
public/  (5 files)
  assets/  (3 files)
    images/  (1 files)
      … 1 files under this directory
    templates/  (2 files)
      … 2 files under this directory
  images/  (1 files)
    .gitkeep
  temp/  (1 files)
    .gitkeep
src/  (137 files)
  controllers/  (35 files)
    apps/  (17 files)
      … 17 files under this directory
    kitchen-sink/  (7 files)
      … 7 files under this directory
    public/  (10 files)
      … 10 files under this directory
    healthcheck.controllers.js
  db/  (1 files)
    index.js
  json/  (8 files)
    youtube/  (2 files)
      … 2 files under this directory
    cats.json
    dogs.json
    quotes.json
    randomjoke.json
    randomproduct.json
    status-codes.json
  logger/  (2 files)
    morgan.logger.js
    winston.logger.js
  middlewares/  (3 files)
    auth.middlewares.js
    error.middlewares.js
    multer.middlewares.js
  models/  (17 files)
    apps/  (17 files)
      … 17 files under this directory
  passport/  (1 files)
    index.js
  routes/  (35 files)
    apps/  (17 files)
      … 17 files under this directory
    kitchen-sink/  (7 files)
      … 7 files under this directory
    public/  (10 files)
      … 10 files under this directory
    healthcheck.routes.js
  seeds/  (6 files)
    _constants.js
    chat-app.seeds.js
    ecommerce.seeds.js
    social-media.seeds.js
    todo.seeds.js
    user.seeds.js
  socket/  (1 files)
    index.js
  utils/  (5 files)
    ApiError.js
    ApiResponse.js
    asyncHandler.js
    helpers.js
    mail.js
  validators/  (20 files)
    apps/  (14 files)
      … 14 files under this directory
    common/  (1 files)
      … 1 files under this directory
    kitchen-sink/  (4 files)
      … 4 files under this directory
    validate.js
  app.js
  constants.js
  index.js
.commitlintrc.json
.dockerignore
.env.sample
.gitignore
.lintstagedrc
.prettierignore
.prettierrc
CONTRIBUTING.md
CONTRIBUTING_CODE_COVERAGE.md
CONTRIBUTING_FRONTEND.md
Dockerfile
LICENSE.md
README.md
docker-compose.prod.yml
docker-compose.yml
nodemon.json
package.json
playwright.config.js
prepare.js
```

## Entry points

- [src/index.js](https://github.com/hiteshchoudhary/apihub/blob/3163bf09d9ee23e29378c402ae4d581e544d6c9f/src/index.js)
- [src/app.js](https://github.com/hiteshchoudhary/apihub/blob/3163bf09d9ee23e29378c402ae4d581e544d6c9f/src/app.js)
- [src/db/index.js](https://github.com/hiteshchoudhary/apihub/blob/3163bf09d9ee23e29378c402ae4d581e544d6c9f/src/db/index.js)
- [src/passport/index.js](https://github.com/hiteshchoudhary/apihub/blob/3163bf09d9ee23e29378c402ae4d581e544d6c9f/src/passport/index.js)
- [src/socket/index.js](https://github.com/hiteshchoudhary/apihub/blob/3163bf09d9ee23e29378c402ae4d581e544d6c9f/src/socket/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 77 file(s) under api layer (observed from repository paths and static analysis). |
| app.js package | library | Observed | Groups 1 file(s) under app.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 13 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| constants.js package | library | Observed | Groups 1 file(s) under constants.js package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 18 file(s) under data layer (observed from repository paths and static analysis). |
| e2e package | library | Observed | Groups 3 file(s) under e2e package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| logger package | library | Observed | Groups 2 file(s) under logger package (observed from repository paths and static analysis). |
| middlewares package | library | Observed | Groups 3 file(s) under middlewares package (observed from repository paths and static analysis). |
| passport package | library | Observed | Groups 1 file(s) under passport package (observed from repository paths and static analysis). |
| seeds package | library | Observed | Groups 6 file(s) under seeds package (observed from repository paths and static analysis). |
| socket package | library | Observed | Groups 1 file(s) under socket package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 5 file(s) under utils package (observed from repository paths and static analysis). |
| validators package | library | Observed | Groups 20 file(s) under validators package (observed from repository paths and static analysis). |

## Important files

- `.commitlintrc.json` (config)
- `.dockerignore` (container)
- `.env.sample` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yaml` (config)
- `.github/ISSUE_TEMPLATE/code_coverage.yaml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yaml` (config)
- `.github/ISSUE_TEMPLATE/frontend_contribution.yaml` (config)
- `Dockerfile` (container)
- `docker-compose.prod.yml` (config)
- `docker-compose.yml` (container)
- `examples/apps/chat-app/web/react-vite-tailwind/.env.sample` (config)
- `examples/apps/chat-app/web/react-vite-tailwind/package.json` (manifest)
- `examples/apps/chat-app/web/react-vite-tailwind/tsconfig.json` (config)
- `examples/apps/chat-app/web/react-vite-tailwind/tsconfig.node.json` (config)
- `examples/apps/ecommerce/web/react-vite-redux-tailwind/.env.sample` (config)
- `examples/apps/ecommerce/web/react-vite-redux-tailwind/package.json` (manifest)
- `examples/apps/ecommerce/web/react-vite-redux-tailwind/public/locales/ar/translation.json` (config)
- `examples/apps/ecommerce/web/react-vite-redux-tailwind/public/locales/en/translation.json` (config)
- `examples/apps/ecommerce/web/react-vite-redux-tailwind/public/locales/hn/translation.json` (config)
- `examples/apps/ecommerce/web/react-vite-redux-tailwind/tsconfig.json` (config)
- `examples/apps/ecommerce/web/react-vite-redux-tailwind/tsconfig.node.json` (config)
- `examples/apps/todo/web/react-vite-tailwind/.env.sample` (config)
- `examples/apps/todo/web/react-vite-tailwind/package.json` (manifest)
- `examples/apps/todo/web/react-vite-tailwind/tsconfig.json` (config)
- `examples/apps/todo/web/react-vite-tailwind/tsconfig.node.json` (config)
- `examples/kitchen-sink/statuscodes/web/react-shadcn-tailwind-zustand/components.json` (config)
- `examples/kitchen-sink/statuscodes/web/react-shadcn-tailwind-zustand/package.json` (manifest)
- `examples/kitchen-sink/statuscodes/web/react-shadcn-tailwind-zustand/tsconfig.json` (config)
- `examples/kitchen-sink/statuscodes/web/react-shadcn-tailwind-zustand/tsconfig.node.json` (config)
- `nodemon.json` (config)
- `package.json` (manifest)
- `src/json/cats.json` (config)
- `src/json/dogs.json` (config)
- `src/json/quotes.json` (config)
- `src/json/randomjoke.json` (config)
- `src/json/randomproduct.json` (config)
- `src/json/status-codes.json` (config)
- `src/json/youtube/channel.json` (config)
- `src/json/youtube/playlists.json` (config)

## Top-level layout

- `examples` — 372 analysed file(s)
- `src` — 137 analysed file(s)
- `(root files)` — 19 analysed file(s)
- `e2e` — 10 analysed file(s)
- `.github` — 5 analysed file(s)
- `public` — 5 analysed file(s)
- `.husky` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 5 file(s) were skipped during inventory (5 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `3163bf09d9ee23e29378c402ae4d581e544d6c9f` is the revision these paths and observations refer to.
