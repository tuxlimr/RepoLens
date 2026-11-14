# Project structure: balderdashy/sails

**Analysed commit:** `7b76422cc27823df033572bdda5c4910a68b697f`

**Commit reference:** [7b76422cc27823df033572bdda5c4910a68b697f](https://github.com/balderdashy/sails/commit/7b76422cc27823df033572bdda5c4910a68b697f)

**Tree at this commit:** [balderdashy/sails@7b76422cc278](https://github.com/balderdashy/sails/tree/7b76422cc27823df033572bdda5c4910a68b697f)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | balderdashy/sails |
| Description | Realtime MVC Framework for Node.js |
| Stars | 22773 |
| Forks | 1907 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `7b76422cc27823df033572bdda5c4910a68b697f` |
| Retrieved at | 2026-11-14T19:11:07.224381+00:00 |
| Files in this snapshot | 716 |

## Directory tree

```text
.github/  (2 files)
  ISSUE_TEMPLATE
  PULL_REQUEST_TEMPLATE
accessible/  (2 files)
  generate.js
  rc.js
bin/  (15 files)
  private/  (2 files)
    patched-commander.js
    read-repl-history-and-start-transcribing.js
  sails-console.js
  sails-debug-console.js
  sails-debug.js
  sails-deploy.js
  sails-generate.js
  sails-inspect.js
  sails-lift.js
  sails-migrate.js
  sails-new.js
  sails-run.js
  sails-upgrade.js
  sails-www.js
  sails.js
docs/  (434 files)
  anatomy/  (93 files)
    api/  (9 files)
      … 9 files under this directory
    assets/  (13 files)
      … 13 files under this directory
    config/  (24 files)
      … 24 files under this directory
    tasks/  (27 files)
      … 27 files under this directory
    views/  (8 files)
      … 8 files under this directory
    .editorconfig.md
    .eslintignore.md
    .eslintrc.md
    .htmlhintrc.md
    Gruntfile.js.md
    README.md
    README.md.md
    anatomy.md
    app.js.md
    gitignore.md
    package.json.md
    sailsrc.md
  concepts/  (101 files)
    ActionsAndControllers/  (3 files)
      … 3 files under this directory
    Assets/  (4 files)
      … 4 files under this directory
    Blueprints/  (3 files)
      … 3 files under this directory
    Configuration/  (3 files)
      … 3 files under this directory
    Deployment/  (4 files)
      … 4 files under this directory
    E-commerce/  (1 files)
      … 1 files under this directory
    File Uploads/  (3 files)
      … 3 files under this directory
    Globals/  (2 files)
      … 2 files under this directory
    Helpers/  (2 files)
      … 2 files under this directory
    Internationalization/  (3 files)
      … 3 files under this directory
    Logging/  (2 files)
      … 2 files under this directory
    Middleware/  (2 files)
      … 2 files under this directory
    ORM/  (17 files)
      … 17 files under this directory
    Policies/  (2 files)
      … 2 files under this directory
    Programmatic Usage/  (2 files)
      … 2 files under this directory
    Realtime/  (4 files)
      … 4 files under this directory
    Routes/  (2 files)
      … 2 files under this directory
    Security/  (10 files)
      … 10 files under this directory
    Services/  (1 files)
      … 1 files under this directory
    Sessions/  (1 files)
      … 1 files under this directory
    Testing/  (1 files)
      … 1 files under this directory
    Views/  (5 files)
      … 5 files under this directory
    extending-sails/  (21 files)
      … 21 files under this directory
    shell-scripts/  (1 files)
      … 1 files under this directory
    README.md
    concepts.md
  contributing/  (15 files)
    code-submission-guidelines/  (4 files)
      … 4 files under this directory
    proposing-features/  (2 files)
      … 2 files under this directory
    adapter-specification.md
    code-of-conduct.md
    contributing-to-the-documentation.md
    contributors-pledge.md
    core-maintainers.md
    intro-to-custom-adapters.md
    issue-contributions.md
    preface.md
    stability-index.md
  faq/  (2 files)
    README.md
    faq.md
  irc/  (1 files)
    irc.md
  reference/  (189 files)
    application/  (19 files)
      … 19 files under this directory
    blueprint-api/  (10 files)
      … 10 files under this directory
    cli/  (8 files)
      … 8 files under this directory
    req/  (35 files)
      … 35 files under this directory
    res/  (20 files)
      … 20 files under this directory
    sails.config/  (17 files)
      … 17 files under this directory
    waterline/  (48 files)
      … 48 files under this directory
    websockets/  (30 files)
      … 30 files under this directory
    README.md
    reference.md
  security/  (2 files)
    README.md
    SAILS-SECURITY-POLICY.md
  tutorials/  (6 files)
    coffeeScript.md
    full-stack-javascript.md
    low-level-mysql-access.md
    mongo.md
    tutorials.md
    typeScript.md
  upgrading/  (5 files)
    To0.10.md
    To0.11.md
    To0.12.md
    To1.0.md
    upgrading.md
  version-notes/  (18 files)
    0.10.x/  (3 files)
      … 3 files under this directory
    0.11.x/  (2 files)
      … 2 files under this directory
    0.12.x/  (2 files)
      … 2 files under this directory
    0.8.x/  (5 files)
      … 5 files under this directory
    0.9.x/  (5 files)
      … 5 files under this directory
    1.0.x/  (1 files)
      … 1 files under this directory
  PAGE_NEEDED.md
  README.md
errors/  (4 files)
  README.md
  fatal.js
  index.js
  warn.js
lib/  (124 files)
  app/  (31 files)
    configuration/  (4 files)
      … 4 files under this directory
    private/  (14 files)
      … 14 files under this directory
    README.md
    Sails.js
    get-actions.js
    get-route-for.js
    get-url-for.js
    index.js
    lift.js
    load.js
    lower.js
    register-action-middleware.js
    register-action.js
    reload-actions.js
    request.js
  hooks/  (78 files)
    blueprints/  (15 files)
      … 15 files under this directory
    helpers/  (3 files)
      … 3 files under this directory
    http/  (6 files)
      … 6 files under this directory
    i18n/  (1 files)
      … 1 files under this directory
    logger/  (3 files)
      … 3 files under this directory
    moduleloader/  (2 files)
      … 2 files under this directory
    policies/  (2 files)
      … 2 files under this directory
    pubsub/  (2 files)
      … 2 files under this directory
    request/  (8 files)
      … 8 files under this directory
    responses/  (9 files)
      … 9 files under this directory
    security/  (7 files)
      … 7 files under this directory
    services/  (1 files)
      … 1 files under this directory
    session/  (2 files)
      … 2 files under this directory
    userconfig/  (2 files)
      … 2 files under this directory
    userhooks/  (2 files)
      … 2 files under this directory
    views/  (11 files)
      … 11 files under this directory
    README.md
    index.js
  router/  (8 files)
    README.md
    bind.js
    bindDefaultHandlers.js
    index.js
    mock-req.js
    mock-res.js
    req.js
    res.js
  util/  (4 files)
    check-origin-url.js
    deep-extend.js
    detect-verb.js
    rc.js
  EVENTS.md
  README.md
  index.js
test/  (121 files)
  benchmarks/  (4 files)
    helpers/  (1 files)
      … 1 files under this directory
    README.md
    sails.load.test.js
    sails.request.generic.test.js
  fixtures/  (3 files)
    constants.js
    customHooks.js
    middleware.js
  helpers/  (5 files)
    RouteFactory.helper.js
    router.js
    sails.js
    test-spawning-sails-child-process-in-cwd.js
    test-spawning-sails-lift-child-process-in-cwd.js
  hooks/  (14 files)
    blueprints/  (1 files)
      … 1 files under this directory
    http/  (1 files)
      … 1 files under this directory
    pubsub/  (1 files)
      … 1 files under this directory
    request/  (3 files)
      … 3 files under this directory
    views/  (8 files)
      … 8 files under this directory
  integration/  (72 files)
    fixtures/  (30 files)
      … 30 files under this directory
    helpers/  (3 files)
      … 3 files under this directory
    README.md
    generate.test.js
    globals.test.js
    hook.3rdparty.test.js
    hook.blueprints.action.routes.test.js
    hook.blueprints.blacklist.test.js
    hook.blueprints.index.routes.test.js
    hook.blueprints.restful.routes.test.js
    hook.blueprints.shortcut.routes.test.js
    hook.cors.test.js
    hook.csrf.test.js
    hook.helpers.test.js
    hook.i18n.test.js
    hook.policies.test.js
    hook.pubsub.modelEvents.noSubscribers.test.js
    hook.pubsub.modelEvents.subscribers.test.js
    hook.sockets.interpreter.test.js
    hook.userconfig.test.js
    hook.views.test.js
    hooks.user.test.js
    lift.https.test.js
    lift.lower.test.js
    lift.test.js
    middleware.404.test.js
    … 15 more files
  unit/  (19 files)
    App.prototype.load.test.js
    README.md
    app.getRouteFor.test.js
    app.getUrlFor.test.js
    app.initializeHooks.test.js
    app.lower.test.js
    app.registerAction.test.js
    app.reloadActions.test.js
    bootstrap.test.js
    controller.test.js
    req.errors.test.js
    req.session.test.js
    req.test.js
    res.test.js
    router.bind.test.js
    router.ordering.test.js
    router.test.js
    router.unbind.test.js
    virtual-request-interpreter.test.js
  .eslintrc
  README.md
  init.js
  mocha.opts
.editorconfig
.eslintrc
.gitignore
.npmignore
.travis.yml
CHANGELOG.md
CODE-OF-CONDUCT.md
CONTRIBUTING.md
LICENSE.md
MODULES.md
README.md
ROADMAP.md
appveyor.yml
package.json
```

## Entry points

- [lib/index.js](https://github.com/balderdashy/sails/blob/7b76422cc27823df033572bdda5c4910a68b697f/lib/index.js)
- [bin/sails.js](https://github.com/balderdashy/sails/blob/7b76422cc27823df033572bdda5c4910a68b697f/bin/sails.js)
- [test/integration/fixtures/hooks/installable/add-policy/index.js](https://github.com/balderdashy/sails/blob/7b76422cc27823df033572bdda5c4910a68b697f/test/integration/fixtures/hooks/installable/add-policy/index.js)
- [test/integration/fixtures/hooks/installable/shout/index.js](https://github.com/balderdashy/sails/blob/7b76422cc27823df033572bdda5c4910a68b697f/test/integration/fixtures/hooks/installable/shout/index.js)
- [errors/index.js](https://github.com/balderdashy/sails/blob/7b76422cc27823df033572bdda5c4910a68b697f/errors/index.js)
- [lib/app/configuration/index.js](https://github.com/balderdashy/sails/blob/7b76422cc27823df033572bdda5c4910a68b697f/lib/app/configuration/index.js)
- [lib/app/index.js](https://github.com/balderdashy/sails/blob/7b76422cc27823df033572bdda5c4910a68b697f/lib/app/index.js)
- [lib/hooks/blueprints/index.js](https://github.com/balderdashy/sails/blob/7b76422cc27823df033572bdda5c4910a68b697f/lib/hooks/blueprints/index.js)
- [lib/hooks/helpers/index.js](https://github.com/balderdashy/sails/blob/7b76422cc27823df033572bdda5c4910a68b697f/lib/hooks/helpers/index.js)
- [lib/hooks/http/index.js](https://github.com/balderdashy/sails/blob/7b76422cc27823df033572bdda5c4910a68b697f/lib/hooks/http/index.js)
- [lib/hooks/i18n/index.js](https://github.com/balderdashy/sails/blob/7b76422cc27823df033572bdda5c4910a68b697f/lib/hooks/i18n/index.js)
- [lib/hooks/index.js](https://github.com/balderdashy/sails/blob/7b76422cc27823df033572bdda5c4910a68b697f/lib/hooks/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| accessible package | library | Observed | Groups 2 file(s) under accessible package (observed from repository paths and static analysis). |
| API layer | api | Observed | Groups 11 file(s) under api layer (observed from repository paths and static analysis). |
| bin package | library | Observed | Groups 15 file(s) under bin package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| errors package | library | Observed | Groups 3 file(s) under errors package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 94 file(s) under lib package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 1 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 121 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.travis.yml` (ci)
- `appveyor.yml` (config)
- `package.json` (manifest)

## Top-level layout

- `docs` — 434 analysed file(s)
- `lib` — 124 analysed file(s)
- `test` — 121 analysed file(s)
- `bin` — 15 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `errors` — 4 analysed file(s)
- `.github` — 2 analysed file(s)
- `accessible` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `7b76422cc27823df033572bdda5c4910a68b697f` is the revision these paths and observations refer to.
