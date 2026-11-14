# Project structure: ShareDropio/sharedrop

**Analysed commit:** `2b6a9fe5e6cada786d1a1f319612537305b204c7`

**Commit reference:** [2b6a9fe5e6cada786d1a1f319612537305b204c7](https://github.com/ShareDropio/sharedrop/commit/2b6a9fe5e6cada786d1a1f319612537305b204c7)

**Tree at this commit:** [ShareDropio/sharedrop@2b6a9fe5e6ca](https://github.com/ShareDropio/sharedrop/tree/2b6a9fe5e6cada786d1a1f319612537305b204c7)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | ShareDropio/sharedrop |
| Description | Easy P2P file transfer powered by WebRTC - inspired by Apple AirDrop |
| Stars | 10768 |
| Forks | 862 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `2b6a9fe5e6cada786d1a1f319612537305b204c7` |
| Retrieved at | 2026-11-14T19:12:31.970540+00:00 |
| Files in this snapshot | 123 |

## Directory tree

```text
app/  (54 files)
  components/  (9 files)
    circular-progress.hbs
    circular-progress.js
    file-field.js
    modal-dialog.js
    peer-avatar.js
    peer-widget.js
    popover-confirm.js
    room-url.js
    user-widget.js
  controllers/  (2 files)
    application.js
    index.js
  helpers/  (1 files)
    is-equal.js
  initializers/  (1 files)
    prerequisites.js
  models/  (2 files)
    peer.js
    user.js
  routes/  (4 files)
    application.js
    error.js
    index.js
    room.js
  services/  (5 files)
    analytics.js
    avatar.js
    file.js
    room.js
    web-rtc.js
  styles/  (14 files)
    base/  (5 files)
      … 5 files under this directory
    layout/  (4 files)
      … 4 files under this directory
    modules/  (4 files)
      … 4 files under this directory
    app.sass
  templates/  (13 files)
    components/  (4 files)
      … 4 files under this directory
    errors/  (4 files)
      … 4 files under this directory
    about-app.hbs
    about-room.hbs
    about-you.hbs
    application.hbs
    index.hbs
  app.js
  index.html
  router.js
config/  (4 files)
  dotenv.js
  environment.js
  optional-features.json
  targets.js
lib/  (2 files)
  google-analytics/  (2 files)
    index.js
    package.json
public/  (35 files)
  .well-known/  (1 files)
    brave-rewards-verification.txt
  assets/  (31 files)
    fonts/  (1 files)
      … 1 files under this directory
    images/  (30 files)
      … 30 files under this directory
  .gitkeep
  crossdomain.xml
  robots.txt
tests/  (5 files)
  helpers/  (1 files)
    .gitkeep
  integration/  (1 files)
    .gitkeep
  unit/  (1 files)
    .gitkeep
  index.html
  test-helper.js
.editorconfig
.ember-cli
.env.sample
.eslintignore
.eslintrc.js
.gitignore
.prettierignore
.template-lintrc.js
.travis.yml
.watchmanconfig
Dockerfile
LICENSE
Procfile
Procfile.dev
README.md
ember-cli-build.js
firebase_rules.json
newrelic.js
package.json
prettier.config.js
server.js
sharedrop.crx
testem.js
```

## Entry points

- [app/app.js](https://github.com/ShareDropio/sharedrop/blob/2b6a9fe5e6cada786d1a1f319612537305b204c7/app/app.js)
- [app/controllers/index.js](https://github.com/ShareDropio/sharedrop/blob/2b6a9fe5e6cada786d1a1f319612537305b204c7/app/controllers/index.js)
- [app/routes/index.js](https://github.com/ShareDropio/sharedrop/blob/2b6a9fe5e6cada786d1a1f319612537305b204c7/app/routes/index.js)
- [lib/google-analytics/index.js](https://github.com/ShareDropio/sharedrop/blob/2b6a9fe5e6cada786d1a1f319612537305b204c7/lib/google-analytics/index.js)
- [server.js](https://github.com/ShareDropio/sharedrop/blob/2b6a9fe5e6cada786d1a1f319612537305b204c7/server.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 6 file(s) under api layer (observed from repository paths and static analysis). |
| app package | library | Observed | Groups 12 file(s) under app package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 8 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 5 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 2 file(s) under data layer (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 1 file(s) under lib package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 5 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 5 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.env.sample` (config)
- `.travis.yml` (ci)
- `Dockerfile` (container)
- `config/optional-features.json` (config)
- `firebase_rules.json` (config)
- `lib/google-analytics/package.json` (manifest)
- `package.json` (manifest)

## Top-level layout

- `app` — 54 analysed file(s)
- `public` — 35 analysed file(s)
- `(root files)` — 23 analysed file(s)
- `tests` — 5 analysed file(s)
- `config` — 4 analysed file(s)
- `lib` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `2b6a9fe5e6cada786d1a1f319612537305b204c7` is the revision these paths and observations refer to.
