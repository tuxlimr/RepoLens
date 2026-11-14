# Project structure: strongloop/loopback

**Analysed commit:** `13371fd2a138a6f39db77e5a455b3170e5d4a0f5`

**Commit reference:** [13371fd2a138a6f39db77e5a455b3170e5d4a0f5](https://github.com/strongloop/loopback/commit/13371fd2a138a6f39db77e5a455b3170e5d4a0f5)

**Tree at this commit:** [strongloop/loopback@13371fd2a138](https://github.com/strongloop/loopback/tree/13371fd2a138a6f39db77e5a455b3170e5d4a0f5)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | strongloop/loopback |
| Description | LoopBack makes it easy to build modern applications that require complex integrations. |
| Stars | 13140 |
| Forks | 1168 |
| Licence | Other |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `13371fd2a138a6f39db77e5a455b3170e5d4a0f5` |
| Retrieved at | 2026-11-14T19:12:00.550756+00:00 |
| Files in this snapshot | 241 |

## Directory tree

```text
.github/  (6 files)
  ISSUE_TEMPLATE/  (4 files)
    Bug_report.md
    Feature_request.md
    Question.md
    config.yml
  PULL_REQUEST_TEMPLATE.md
  stale.yml
common/  (23 files)
  models/  (23 files)
    README.md
    access-token.js
    access-token.json
    acl.js
    acl.json
    application.js
    application.json
    change.js
    change.json
    checkpoint.js
    checkpoint.json
    email.js
    email.json
    key-value-model.js
    key-value-model.json
    role-mapping.js
    role-mapping.json
    role.js
    role.json
    scope.js
    scope.json
    user.js
    user.json
docs/  (1 files)
  api-explorer-details.md
example/  (7 files)
  client-server/  (3 files)
    client.js
    models.js
    server.js
  colors/  (1 files)
    app.js
  mobile-models/  (1 files)
    app.js
  replication/  (1 files)
    app.js
  simple-data-source/  (1 files)
    app.js
intl/  (15 files)
  cs/  (1 files)
    messages.json
  de/  (1 files)
    messages.json
  en/  (1 files)
    messages.json
  es/  (1 files)
    messages.json
  fr/  (1 files)
    messages.json
  it/  (1 files)
    messages.json
  ja/  (1 files)
    messages.json
  ko/  (1 files)
    messages.json
  nl/  (1 files)
    messages.json
  pl/  (1 files)
    messages.json
  pt/  (1 files)
    messages.json
  ru/  (1 files)
    messages.json
  tr/  (1 files)
    messages.json
  zh-Hans/  (1 files)
    messages.json
  zh-Hant/  (1 files)
    messages.json
lib/  (17 files)
  connectors/  (3 files)
    base-connector.js
    mail.js
    memory.js
  access-context.js
  application.js
  browser-express.js
  builtin-models.js
  configure-shared-methods.js
  current-context.js
  globalize.js
  loopback.js
  model.js
  persisted-model.js
  registry.js
  runtime.js
  server-app.js
  utils.js
server/  (8 files)
  middleware/  (8 files)
    context.js
    error-handler.js
    favicon.js
    rest.js
    static.js
    status.js
    token.js
    url-not-found.js
templates/  (2 files)
  reset-form.ejs
  verify.ejs
test/  (148 files)
  e2e/  (2 files)
    remote-connector.e2e.js
    replication.e2e.js
  fixtures/  (100 files)
    access-control/  (12 files)
      … 12 files under this directory
    e2e/  (2 files)
      … 2 files under this directory
    shared-methods/  (54 files)
      … 54 files under this directory
    simple-app/  (8 files)
      … 8 files under this directory
    simple-integration-app/  (17 files)
      … 17 files under this directory
    user-integration-app/  (7 files)
      … 7 files under this directory
  helpers/  (5 files)
    error-loggers.js
    expect.js
    loopback-testing-helper.js
    use-english.js
    wait-for-event.js
  util/  (3 files)
    describe.js
    it.js
    model-tests.js
  access-control.integration.js
  access-token.test.js
  acl.test.js
  app.test.js
  authorization-scopes.test.js
  change-stream.test.js
  change.test.js
  checkpoint.test.js
  context-options.test.js
  data-source.test.js
  email.test.js
  error-handler.test.js
  geo-point.test.js
  hidden-properties.test.js
  integration.test.js
  karma.conf.js
  key-value-model.test.js
  loopback.test.js
  memory.test.js
  mocha.opts
  model.application.test.js
  model.test.js
  multiple-user-principal-accessing-another-user-model.js
  multiple-user-principal-types.test.js
  … 14 more files
.eslintignore
.eslintrc
.gitignore
.nycrc
.travis.yml
CHANGES.md
CODEOWNERS
CONTRIBUTING.md
Gruntfile.js
LICENSE
README.md
docs.json
index.js
package.json
```

## Entry points

- [index.js](https://github.com/strongloop/loopback/blob/13371fd2a138a6f39db77e5a455b3170e5d4a0f5/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 28 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 11 file(s) under data layer (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 17 file(s) under lib package (observed from repository paths and static analysis). |
| server package | library | Observed | Groups 8 file(s) under server package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 148 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/stale.yml` (config)
- `.travis.yml` (ci)
- `common/models/access-token.json` (config)
- `common/models/acl.json` (config)
- `common/models/application.json` (config)
- `common/models/change.json` (config)
- `common/models/checkpoint.json` (config)
- `common/models/email.json` (config)
- `common/models/key-value-model.json` (config)
- `common/models/role-mapping.json` (config)
- `common/models/role.json` (config)
- `common/models/scope.json` (config)
- `common/models/user.json` (config)
- `docs.json` (config)
- `intl/cs/messages.json` (config)
- `intl/de/messages.json` (config)
- `intl/en/messages.json` (config)
- `intl/es/messages.json` (config)
- `intl/fr/messages.json` (config)
- `intl/it/messages.json` (config)
- `intl/ja/messages.json` (config)
- `intl/ko/messages.json` (config)
- `intl/nl/messages.json` (config)
- `intl/pl/messages.json` (config)
- `intl/pt/messages.json` (config)
- `intl/ru/messages.json` (config)
- `intl/tr/messages.json` (config)
- `intl/zh-Hans/messages.json` (config)
- `intl/zh-Hant/messages.json` (config)
- `package.json` (manifest)

## Top-level layout

- `test` — 148 analysed file(s)
- `common` — 23 analysed file(s)
- `lib` — 17 analysed file(s)
- `intl` — 15 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `server` — 8 analysed file(s)
- `example` — 7 analysed file(s)
- `.github` — 6 analysed file(s)
- `templates` — 2 analysed file(s)
- `docs` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `13371fd2a138a6f39db77e5a455b3170e5d4a0f5` is the revision these paths and observations refer to.
