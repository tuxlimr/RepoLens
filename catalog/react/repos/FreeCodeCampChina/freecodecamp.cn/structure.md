# Project structure: FreeCodeCampChina/freecodecamp.cn

**Analysed commit:** `b09a3a0dec1fa0b0620601a705ff2e9b97564f97`

**Commit reference:** [b09a3a0dec1fa0b0620601a705ff2e9b97564f97](https://github.com/FreeCodeCampChina/freecodecamp.cn/commit/b09a3a0dec1fa0b0620601a705ff2e9b97564f97)

**Tree at this commit:** [FreeCodeCampChina/freecodecamp.cn@b09a3a0dec1f](https://github.com/FreeCodeCampChina/freecodecamp.cn/tree/b09a3a0dec1fa0b0620601a705ff2e9b97564f97)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | FreeCodeCampChina/freecodecamp.cn |
| Description | FCC China open source codebase and curriculum. Learn to code and help nonprofits. |
| Stars | 37789 |
| Forks | 1414 |
| Licence | Other |
| Language | CSS |
| Default branch | dev |
| Analysed commit | `b09a3a0dec1fa0b0620601a705ff2e9b97564f97` |
| Retrieved at | 2026-11-14T19:13:01.607707+00:00 |
| Files in this snapshot | 503 |

## Directory tree

```text
.github/  (2 files)
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
client/  (142 files)
  commonFramework/  (18 files)
    add-loop-protect.js
    bindings.js
    code-storage.js
    code-uri.js
    create-editor.js
    detect-unsafe-code-stream.js
    display-test-results.js
    end.js
    execute-challenge-stream.js
    get-iframe.js
    init.js
    output-display.js
    phone-scroll-lock.js
    report-issue.js
    run-tests-stream.js
    show-completion.js
    step-challenge.js
    update-preview.js
  less/  (112 files)
    lib/  (104 files)
      … 104 files under this directory
    challenge.less
    chat.less
    jobs.less
    main.less
    map.less
    signin.less
    toastr.less
    wiki.less
  sagas/  (6 files)
    README.md
    err-saga.js
    hard-go-to-saga.js
    index.js
    local-storage-saga.js
    title-saga.js
  README.md
  es6-shims.js
  iFrameScripts.js
  index.js
  main.js
  plugin.js
common/  (89 files)
  app/  (71 files)
    components/  (12 files)
      … 12 files under this directory
    redux/  (6 files)
      … 6 files under this directory
    routes/  (39 files)
      … 39 files under this directory
    shared/  (1 files)
      … 1 files under this directory
    utils/  (6 files)
      … 6 files under this directory
    App.jsx
    create-app.jsx
    create-reducer.js
    index.js
    middlewares.js
    provide-store.js
    sagas.js
  models/  (12 files)
    User-Credential.json
    User-Identity.js
    User-Identity.json
    challenge.json
    job.json
    nonprofit.json
    pledge.json
    promo.js
    promo.json
    story.json
    user.js
    user.json
  utils/  (5 files)
    ajax-stream.js
    constantStrings.json
    index.js
    jsonp$.js
    services-creator.js
  config.global.js
config/  (1 files)
  secrets.js
public/  (48 files)
  css/  (5 files)
    themes/  (2 files)
      … 2 files under this directory
    Vimeo.css
    lato.css
    ubuntu.css
  favicons/  (2 files)
    android-chrome-manifest.json
    browserconfig.xml
  images/  (11 files)
    challenges.svg
    content.svg
    d3-logo.svg
    freecodecamp_logo.svg
    landingIcons_connect.svg
    landingIcons_learn.svg
    landingIcons_nonprofits.svg
    landingIcons_portfolio.svg
    logo-footer.svg
    react.svg
    timeline.svg
  js/  (21 files)
    lib/  (9 files)
      … 9 files under this directory
    .jshintrc
    calculator.js
    commonFramework-2c9795240d.js
    commonFramework-2f0be7f94b.js
    commonFramework-64e637bbe5.js
    commonFramework-e9a2482e6b.js
    commonFramework.js
    dashboard.js
    greensock.js
    join-group.js
    join-race.js
    sidecar.v1.js
  json/  (2 files)
    bootcamps.json
    cats.json
  browserconfig.xml
  code.html
  favicons.html
  grouth-hacker.html
  leader-board.html
  progress.html
  robots.txt
seed/  (56 files)
  challenges/  (48 files)
    00-getting-started/  (1 files)
      … 1 files under this directory
    01-front-end-development-certification/  (13 files)
      … 13 files under this directory
    02-data-visualization-certification/  (6 files)
      … 6 files under this directory
    03-back-end-development-certification/  (7 files)
      … 7 files under this directory
    04-video-challenges/  (21 files)
      … 21 files under this directory
  bonfireMDNlinks.js
  create-challenge-bundle.js
  get-challenge-completion.js
  get-emails.js
  getChallenges.js
  index.js
  loopbackMigration.js
  test-challenges.js
server/  (138 files)
  boot/  (18 files)
    a-extendUser.js
    a-extendUserIdent.js
    a-react.js
    a-services.js
    about.js
    authentication.js
    certificate.js
    challenge.js
    commit.js
    explorer.js
    home.js
    randomAPIs.js
    redirectHttps.js
    redirects.js
    restApi.js
    story.js
    t-wiki.js
    user.js
  manifests/  (1 files)
    README.md
  middlewares/  (13 files)
    add-return-to.js
    constant-headers.js
    cookie-parser.js
    csp.js
    error-handlers.js
    express-rx.js
    global-locals.js
    jade-helpers.js
    keymetrics.js
    migrate-completed-challenges.js
    revision-helpers.js
    sessions.js
    validator.js
  resources/  (2 files)
    labs.json
    testimonials.json
  services/  (3 files)
    hikes.js
    job.js
    user.js
  utils/  (15 files)
    auth.js
    bad-id-map.js
    certTypes.json
    commit-goals.json
    commit.js
    commit.json
    constantStrings.json
    constants.js
    date-utils.js
    getFromDisk$.js
    index.js
    middleware.js
    resources.json
    rx.js
    user-stats.js
  views/  (72 files)
    account/  (7 files)
      … 7 files under this directory
    certificate/  (7 files)
      … 7 files under this directory
    challenges/  (6 files)
      … 6 files under this directory
    commit/  (3 files)
      … 3 files under this directory
    map/  (1 files)
      … 1 files under this directory
    partials/  (9 files)
      … 9 files under this directory
    resources/  (23 files)
      … 23 files under this directory
    sponsors/  (2 files)
      … 2 files under this directory
    stories/  (6 files)
      … 6 files under this directory
    wiki/  (1 files)
      … 1 files under this directory
    feed.jade
    home.jade
    layout-react.jade
    layout-wide.jade
    layout.jade
    redirect-https.html
    redirect-https.jade
  README.md
  config.development.js
  config.json
  config.local.js
  config.production.js
  datasources.json
  datasources.local.js
  debug-entry.js
  middleware.json
  model-config.json
  passport-providers.js
  production-start.js
  server.js
  ssl-config.js
test/  (2 files)
  server/  (2 files)
    utils/  (2 files)
      … 2 files under this directory
.babelrc
.bowerrc
.editorconfig
.eslintignore
.eslintrc
.gitattributes
.gitignore
.jshintrc
.node-inspectorrc
.travis.yml
CONTRIBUTING.md
LICENSE
LICENSE-freeCodeCamp-Curriculum.md
LICENSE-freeCodeCamp-Translation.md
README.md
bower.json
dataAsync.js
gulpfile.js
leanTest.js
package.json
pm2Start.js
sample.env
simple-json.js
webpack.config.js
… 1 more files
```

## Entry points

- [client/index.js](https://github.com/FreeCodeCampChina/freecodecamp.cn/blob/b09a3a0dec1fa0b0620601a705ff2e9b97564f97/client/index.js)
- [client/main.js](https://github.com/FreeCodeCampChina/freecodecamp.cn/blob/b09a3a0dec1fa0b0620601a705ff2e9b97564f97/client/main.js)
- [client/sagas/index.js](https://github.com/FreeCodeCampChina/freecodecamp.cn/blob/b09a3a0dec1fa0b0620601a705ff2e9b97564f97/client/sagas/index.js)
- [common/app/App.jsx](https://github.com/FreeCodeCampChina/freecodecamp.cn/blob/b09a3a0dec1fa0b0620601a705ff2e9b97564f97/common/app/App.jsx)
- [common/app/index.js](https://github.com/FreeCodeCampChina/freecodecamp.cn/blob/b09a3a0dec1fa0b0620601a705ff2e9b97564f97/common/app/index.js)
- [common/app/redux/index.js](https://github.com/FreeCodeCampChina/freecodecamp.cn/blob/b09a3a0dec1fa0b0620601a705ff2e9b97564f97/common/app/redux/index.js)
- [common/app/routes/index.js](https://github.com/FreeCodeCampChina/freecodecamp.cn/blob/b09a3a0dec1fa0b0620601a705ff2e9b97564f97/common/app/routes/index.js)
- [common/utils/index.js](https://github.com/FreeCodeCampChina/freecodecamp.cn/blob/b09a3a0dec1fa0b0620601a705ff2e9b97564f97/common/utils/index.js)
- [seed/index.js](https://github.com/FreeCodeCampChina/freecodecamp.cn/blob/b09a3a0dec1fa0b0620601a705ff2e9b97564f97/seed/index.js)
- [server/server.js](https://github.com/FreeCodeCampChina/freecodecamp.cn/blob/b09a3a0dec1fa0b0620601a705ff2e9b97564f97/server/server.js)
- [server/utils/index.js](https://github.com/FreeCodeCampChina/freecodecamp.cn/blob/b09a3a0dec1fa0b0620601a705ff2e9b97564f97/server/utils/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 36 file(s) under api layer (observed from repository paths and static analysis). |
| common package | library | Observed | Groups 32 file(s) under common package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 77 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 7 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 3 file(s) under data layer (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 28 file(s) under external integrations (observed from repository paths and static analysis). |
| public package | library | Observed | Groups 18 file(s) under public package (observed from repository paths and static analysis). |
| seed package | library | Observed | Groups 8 file(s) under seed package (observed from repository paths and static analysis). |
| server package | library | Observed | Groups 50 file(s) under server package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 3 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 2 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.travis.yml` (ci)
- `bower.json` (config)
- `common/app/components/Footer/links.json` (config)
- `common/app/components/Nav/links.json` (config)
- `common/models/User-Credential.json` (config)
- `common/models/User-Identity.json` (config)
- `common/models/challenge.json` (config)
- `common/models/job.json` (config)
- `common/models/nonprofit.json` (config)
- `common/models/pledge.json` (config)
- `common/models/promo.json` (config)
- `common/models/story.json` (config)
- `common/models/user.json` (config)
- `common/utils/constantStrings.json` (config)
- `package.json` (manifest)
- `public/favicons/android-chrome-manifest.json` (config)
- `public/json/bootcamps.json` (config)
- `public/json/cats.json` (config)
- `seed/challenges/00-getting-started/getting-started.json` (config)
- `seed/challenges/01-front-end-development-certification/advanced-bonfires.json` (config)
- `seed/challenges/01-front-end-development-certification/advanced-ziplines.json` (config)
- `seed/challenges/01-front-end-development-certification/basic-bonfires.json` (config)
- `seed/challenges/01-front-end-development-certification/basic-ziplines.json` (config)
- `seed/challenges/01-front-end-development-certification/bootstrap.json` (config)
- `seed/challenges/01-front-end-development-certification/front-end-development-certificate.json` (config)
- `seed/challenges/01-front-end-development-certification/gear-up-for-success.json` (config)
- `seed/challenges/01-front-end-development-certification/html5-and-css.json` (config)
- `seed/challenges/01-front-end-development-certification/intermediate-bonfires.json` (config)
- `seed/challenges/01-front-end-development-certification/intermediate-ziplines.json` (config)
- `seed/challenges/01-front-end-development-certification/jquery.json` (config)
- `seed/challenges/01-front-end-development-certification/json-apis-and-ajax.json` (config)
- `seed/challenges/01-front-end-development-certification/object-oriented-and-functional-programming.json` (config)
- `seed/challenges/02-data-visualization-certification/d3.json` (config)
- `seed/challenges/02-data-visualization-certification/data-visualization-certificate.json` (config)
- `seed/challenges/02-data-visualization-certification/data-visualization-projects.json` (config)
- `seed/challenges/02-data-visualization-certification/react-projects.json` (config)
- `seed/challenges/02-data-visualization-certification/react.json` (config)
- `seed/challenges/02-data-visualization-certification/sass.json` (config)
- `seed/challenges/03-back-end-development-certification/api-projects.json` (config)
- `seed/challenges/03-back-end-development-certification/automated-testing-and-debugging.json` (config)
- `seed/challenges/03-back-end-development-certification/back-end-development-certificate.json` (config)
- `seed/challenges/03-back-end-development-certification/dynamic-web-applications.json` (config)
- `seed/challenges/03-back-end-development-certification/git.json` (config)
- `seed/challenges/03-back-end-development-certification/mongodb.json` (config)
- `seed/challenges/03-back-end-development-certification/nodejs-and-expressjs.json` (config)
- `seed/challenges/04-video-challenges/accessibility.json` (config)
- `seed/challenges/04-video-challenges/agile.json` (config)
- `seed/challenges/04-video-challenges/bigonotation.json` (config)
- `seed/challenges/04-video-challenges/chromedevtools.json` (config)
- `seed/challenges/04-video-challenges/computer-basics.json` (config)
- `seed/challenges/04-video-challenges/computer-science.json` (config)
- `seed/challenges/04-video-challenges/data-visualization.json` (config)
- `seed/challenges/04-video-challenges/devops.json` (config)
- `seed/challenges/04-video-challenges/dom.json` (config)
- `seed/challenges/04-video-challenges/embedded-and-internet-of-things.json` (config)
- `seed/challenges/04-video-challenges/game-development.json` (config)
- `seed/challenges/04-video-challenges/gamification.json` (config)
- `seed/challenges/04-video-challenges/jslingo.json` (config)
- `seed/challenges/04-video-challenges/machine-learning.json` (config)
- `seed/challenges/04-video-challenges/math-for-programmers.json` (config)
- `seed/challenges/04-video-challenges/mobile-javascript-development.json` (config)
- `seed/challenges/04-video-challenges/software-engineering-principles.json` (config)
- `seed/challenges/04-video-challenges/statistics.json` (config)
- `seed/challenges/04-video-challenges/tools.json` (config)
- `seed/challenges/04-video-challenges/user-experience-design.json` (config)
- `seed/challenges/04-video-challenges/visual-design.json` (config)
- `server/config.json` (config)
- `server/datasources.json` (config)
- `server/middleware.json` (config)
- `server/model-config.json` (config)
- `server/resources/labs.json` (config)
- `server/resources/testimonials.json` (config)
- `server/utils/certTypes.json` (config)
- `server/utils/commit-goals.json` (config)
- `server/utils/commit.json` (config)
- `server/utils/constantStrings.json` (config)
- `server/utils/resources.json` (config)

## Top-level layout

- `client` — 142 analysed file(s)
- `server` — 138 analysed file(s)
- `common` — 89 analysed file(s)
- `seed` — 56 analysed file(s)
- `public` — 48 analysed file(s)
- `(root files)` — 25 analysed file(s)
- `.github` — 2 analysed file(s)
- `test` — 2 analysed file(s)
- `config` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x generated/minified file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `b09a3a0dec1fa0b0620601a705ff2e9b97564f97` is the revision these paths and observations refer to.
