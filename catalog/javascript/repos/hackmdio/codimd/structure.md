# Project structure: hackmdio/codimd

**Analysed commit:** `b1188a5648a23d970b9ad58612376e6602431f6f`

**Commit reference:** [b1188a5648a23d970b9ad58612376e6602431f6f](https://github.com/hackmdio/codimd/commit/b1188a5648a23d970b9ad58612376e6602431f6f)

**Tree at this commit:** [hackmdio/codimd@b1188a5648a2](https://github.com/hackmdio/codimd/tree/b1188a5648a23d970b9ad58612376e6602431f6f)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | hackmdio/codimd |
| Description | CodiMD - Realtime collaborative markdown notes on all platforms. |
| Stars | 10163 |
| Forks | 1122 |
| Licence | AGPL-3.0 |
| Language | JavaScript |
| Default branch | develop |
| Analysed commit | `b1188a5648a23d970b9ad58612376e6602431f6f` |
| Retrieved at | 2026-11-14T19:12:44.634091+00:00 |
| Files in this snapshot | 302 |

## Directory tree

```text
.devcontainer/  (3 files)
  Dockerfile
  devcontainer.json
  docker-compose.yml
.github/  (5 files)
  tests/  (2 files)
    README.md
    pull-request.json
  workflows/  (3 files)
    build.yml
    check-release.yml
    push-image.yml
bin/  (4 files)
  heroku
  heroku_start.sh
  manage_users
  setup
contribute/  (1 files)
  developer-certificate-of-origin
deployments/  (4 files)
  Dockerfile
  build.sh
  docker-compose.yml
  docker-entrypoint.sh
lib/  (88 files)
  auth/  (16 files)
    bitbucket/  (1 files)
      … 1 files under this directory
    dropbox/  (1 files)
      … 1 files under this directory
    email/  (1 files)
      … 1 files under this directory
    facebook/  (1 files)
      … 1 files under this directory
    github/  (1 files)
      … 1 files under this directory
    gitlab/  (1 files)
      … 1 files under this directory
    google/  (1 files)
      … 1 files under this directory
    ldap/  (1 files)
      … 1 files under this directory
    mattermost/  (1 files)
      … 1 files under this directory
    oauth2/  (2 files)
      … 2 files under this directory
    openid/  (1 files)
      … 1 files under this directory
    saml/  (1 files)
      … 1 files under this directory
    twitter/  (1 files)
      … 1 files under this directory
    index.js
    utils.js
  config/  (7 files)
    default.js
    defaultSSL.js
    dockerSecret.js
    enum.js
    environment.js
    index.js
    utils.js
  errorPage/  (1 files)
    index.js
  history/  (1 files)
    index.js
  homepage/  (1 files)
    index.js
  imageRouter/  (7 files)
    azure.js
    filesystem.js
    imgur.js
    index.js
    lutim.js
    minio.js
    s3.js
  middleware/  (4 files)
    checkURIValid.js
    codiMDVersion.js
    redirectWithoutTrailingSlashes.js
    tooBusy.js
  migrations/  (19 files)
    20150504155329-create-users.js
    20150508114741-create-notes.js
    20150515125813-create-temp.js
    20150702001020-update-to-0_3_1.js
    20150915153700-change-notes-title-to-text.js
    20160112220142-note-add-lastchange.js
    20160420180355-note-add-alias.js
    20160515114000-user-add-tokens.js
    20160607060246-support-revision.js
    20160703062241-support-authorship.js
    20161009040430-support-delete-note.js
    20161201050312-support-email-signin.js
    20171009121200-longtext-for-mysql.js
    20180209120907-longtext-of-authorship.js
    20180306150303-fix-enum.js
    20180326103000-use-text-in-tokens.js
    20180525153000-user-add-delete-token.js
    20200104215332-remove-temp-table.js
    20240114120250-revision-add-index.js
  models/  (5 files)
    author.js
    index.js
    note.js
    revision.js
    user.js
  note/  (2 files)
    index.js
    noteActions.js
  ot/  (8 files)
    client.js
    editor-socketio-server.js
    index.js
    selection.js
    server.js
    simple-text-operation.js
    text-operation.js
    wrapped-operation.js
  realtime/  (6 files)
    processQueue.js
    realtime.js
    realtimeCleanDanglingUserJob.js
    realtimeClientConnection.js
    realtimeSaveRevisionJob.js
    realtimeUpdateDirtyNoteJob.js
  status/  (1 files)
    index.js
  user/  (1 files)
    index.js
  web/  (1 files)
    middleware/  (1 files)
      … 1 files under this directory
  workers/  (1 files)
    dmpWorker.js
  csp.js
  letter-avatars.js
  logger.js
  metrics.js
  response.js
  routes.js
  utils.js
locales/  (24 files)
  ca.json
  da.json
  de.json
  el.json
  en.json
  eo.json
  es.json
  fr.json
  hi.json
  hr.json
  id.json
  it.json
  ja.json
  ko.json
  nl.json
  pl.json
  pt.json
  ru.json
  sr.json
  sv.json
  tr.json
  uk.json
  zh-CN.json
  zh-TW.json
public/  (127 files)
  css/  (18 files)
    codemirror-extend/  (5 files)
      … 5 files under this directory
    bootstrap-social.css
    center.css
    cover.css
    extra.css
    font.css
    github-extract.css
    google-font.css
    index.css
    markdown.css
    mermaid.css
    site.css
    slide-preview.css
    slide.css
  docs/  (5 files)
    features.md
    privacy.md.example
    release-notes.md
    slide-example.md
    yaml-metadata.md
  images/  (1 files)
    mattermost-logo.svg
  js/  (73 files)
    lib/  (59 files)
      … 59 files under this directory
    revealjs-plugins/  (2 files)
      … 2 files under this directory
    cover.js
    extra.js
    history.js
    htmlExport.js
    index.js
    locale.js
    mathjax-config-extra.js
    pretty.js
    render.js
    reveal-markdown.js
    slide.js
    utils.js
  markdown-lint/  (1 files)
    css/  (1 files)
      … 1 files under this directory
  uploads/  (1 files)
    .gitkeep
  views/  (26 files)
    codimd/  (5 files)
      … 5 files under this directory
    includes/  (2 files)
      … 2 files under this directory
    index/  (5 files)
      … 5 files under this directory
    shared/  (8 files)
      … 8 files under this directory
    codimd.ejs
    error.ejs
    html.hbs
    index.ejs
    pretty.ejs
    slide.ejs
  .eslintrc.js
  default.md
test/  (20 files)
  auth/  (1 files)
    oauth2/  (1 files)
      … 1 files under this directory
  realtime/  (12 files)
    cleanDanglingUser.test.js
    connection.test.js
    dirtyNoteUpdate.test.js
    disconnect-process.test.js
    extractNoteIdFromSocket.test.js
    ifMayEdit.test.js
    parseNoteIdFromSocket.test.js
    realtime.test.js
    saveRevisionJob.test.js
    socket-events.test.js
    updateNote.test.js
    utils.js
  testDoubles/  (4 files)
    ProcessQueueFake.js
    loggerFake.js
    otFake.js
    realtimeJobStub.js
  connectionQueue.test.js
  csp.js
  letter-avatars.js
utils/  (1 files)
  string.js
.buildpacks
.dockerignore
.editorconfig
.gitignore
.mailmap
.nvmrc
.sequelizerc.example
AUTHORS
Aptfile
CONTRIBUTING.md
FUNDING.json
LICENSE
Procfile
README.md
app.js
app.json
babel.config.js
config.js
config.json.example
package.json
scalingo.json
webpack.common.js
webpack.dev.js
webpack.htmlexport.js
… 1 more files
```

## Entry points

- [app.js](https://github.com/hackmdio/codimd/blob/b1188a5648a23d970b9ad58612376e6602431f6f/app.js)
- [lib/auth/bitbucket/index.js](https://github.com/hackmdio/codimd/blob/b1188a5648a23d970b9ad58612376e6602431f6f/lib/auth/bitbucket/index.js)
- [lib/auth/dropbox/index.js](https://github.com/hackmdio/codimd/blob/b1188a5648a23d970b9ad58612376e6602431f6f/lib/auth/dropbox/index.js)
- [lib/auth/email/index.js](https://github.com/hackmdio/codimd/blob/b1188a5648a23d970b9ad58612376e6602431f6f/lib/auth/email/index.js)
- [lib/auth/facebook/index.js](https://github.com/hackmdio/codimd/blob/b1188a5648a23d970b9ad58612376e6602431f6f/lib/auth/facebook/index.js)
- [lib/auth/github/index.js](https://github.com/hackmdio/codimd/blob/b1188a5648a23d970b9ad58612376e6602431f6f/lib/auth/github/index.js)
- [lib/auth/gitlab/index.js](https://github.com/hackmdio/codimd/blob/b1188a5648a23d970b9ad58612376e6602431f6f/lib/auth/gitlab/index.js)
- [lib/auth/google/index.js](https://github.com/hackmdio/codimd/blob/b1188a5648a23d970b9ad58612376e6602431f6f/lib/auth/google/index.js)
- [lib/auth/index.js](https://github.com/hackmdio/codimd/blob/b1188a5648a23d970b9ad58612376e6602431f6f/lib/auth/index.js)
- [lib/auth/ldap/index.js](https://github.com/hackmdio/codimd/blob/b1188a5648a23d970b9ad58612376e6602431f6f/lib/auth/ldap/index.js)
- [lib/auth/mattermost/index.js](https://github.com/hackmdio/codimd/blob/b1188a5648a23d970b9ad58612376e6602431f6f/lib/auth/mattermost/index.js)
- [lib/auth/oauth2/index.js](https://github.com/hackmdio/codimd/blob/b1188a5648a23d970b9ad58612376e6602431f6f/lib/auth/oauth2/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bin package | library | Observed | Groups 1 file(s) under bin package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 38 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 7 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 5 file(s) under data layer (observed from repository paths and static analysis). |
| deployments package | library | Observed | Groups 2 file(s) under deployments package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 76 file(s) under lib package (observed from repository paths and static analysis). |
| public package | library | Observed | Groups 31 file(s) under public package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 22 file(s) under tests (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 1 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.devcontainer/Dockerfile` (container)
- `.devcontainer/devcontainer.json` (config)
- `.devcontainer/docker-compose.yml` (container)
- `.dockerignore` (container)
- `.editorconfig` (config)
- `.github/workflows/build.yml` (ci)
- `.github/workflows/check-release.yml` (ci)
- `.github/workflows/push-image.yml` (ci)
- `FUNDING.json` (config)
- `app.json` (config)
- `deployments/Dockerfile` (container)
- `deployments/docker-compose.yml` (container)
- `locales/ca.json` (config)
- `locales/da.json` (config)
- `locales/de.json` (config)
- `locales/el.json` (config)
- `locales/en.json` (config)
- `locales/eo.json` (config)
- `locales/es.json` (config)
- `locales/fr.json` (config)
- `locales/hi.json` (config)
- `locales/hr.json` (config)
- `locales/id.json` (config)
- `locales/it.json` (config)
- `locales/ja.json` (config)
- `locales/ko.json` (config)
- `locales/nl.json` (config)
- `locales/pl.json` (config)
- `locales/pt.json` (config)
- `locales/ru.json` (config)
- `locales/sr.json` (config)
- `locales/sv.json` (config)
- `locales/tr.json` (config)
- `locales/uk.json` (config)
- `locales/zh-CN.json` (config)
- `locales/zh-TW.json` (config)
- `package.json` (manifest)
- `scalingo.json` (config)

## Top-level layout

- `public` — 127 analysed file(s)
- `lib` — 88 analysed file(s)
- `(root files)` — 25 analysed file(s)
- `locales` — 24 analysed file(s)
- `test` — 20 analysed file(s)
- `.github` — 5 analysed file(s)
- `bin` — 4 analysed file(s)
- `deployments` — 4 analysed file(s)
- `.devcontainer` — 3 analysed file(s)
- `contribute` — 1 analysed file(s)
- `utils` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 20 file(s) were skipped during inventory (20 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `b1188a5648a23d970b9ad58612376e6602431f6f` is the revision these paths and observations refer to.
