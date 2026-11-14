# Project structure: sdelements/lets-chat

**Analysed commit:** `617207ff3c0c0bf8e3c7a915bd9ec03f1dd8390c`

**Commit reference:** [617207ff3c0c0bf8e3c7a915bd9ec03f1dd8390c](https://github.com/sdelements/lets-chat/commit/617207ff3c0c0bf8e3c7a915bd9ec03f1dd8390c)

**Tree at this commit:** [sdelements/lets-chat@617207ff3c0c](https://github.com/sdelements/lets-chat/tree/617207ff3c0c0bf8e3c7a915bd9ec03f1dd8390c)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | sdelements/lets-chat |
| Description | Self-hosted chat app for small teams |
| Stars | 9787 |
| Forks | 1552 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `617207ff3c0c0bf8e3c7a915bd9ec03f1dd8390c` |
| Retrieved at | 2026-11-14T19:12:52.980479+00:00 |
| Files in this snapshot | 170 |

## Directory tree

```text
app/  (73 files)
  auth/  (2 files)
    index.js
    local.js
  controllers/  (12 files)
    account.js
    connections.js
    extras.js
    files.js
    index.js
    messages.js
    misc.js
    presence.js
    rooms.js
    transcript.js
    usermessages.js
    users.js
  core/  (16 files)
    files/  (1 files)
      … 1 files under this directory
    presence/  (5 files)
      … 5 files under this directory
    account.js
    avatar-cache.js
    files.js
    helpers.js
    index.js
    messages.js
    presence.js
    rooms.js
    usermessages.js
    users.js
  middlewares/  (4 files)
    cleanupFiles.js
    index.js
    requireLogin.js
    roomRoute.js
  misc/  (2 files)
    art.txt
    robots.txt
  models/  (6 files)
    file.js
    index.js
    message.js
    room.js
    user.js
    usermessage.js
  xmpp/  (29 files)
    events/  (9 files)
      … 9 files under this directory
    msg-processors/  (16 files)
      … 16 files under this directory
    event-listener.js
    index.js
    msg-processor.js
    xmpp-connection.js
  config.js
  plugins.js
docker/  (4 files)
  .dockerignore
  Dockerfile
  README.md
  docker-compose.yml
extras/  (5 files)
  emotes/  (4 files)
    public/  (1 files)
      … 1 files under this directory
    default.yml
    lets-chat.yml
    local.yml.sample
  replacements/  (1 files)
    local.yml.sample
locales/  (17 files)
  az.json
  de.json
  en.json
  es.json
  fi.json
  fr.json
  is.json
  it.json
  ja.json
  ko.json
  nl.json
  pl.json
  pt.json
  ru.json
  tr.json
  zh-TW.json
  zh.json
media/  (30 files)
  img/  (1 files)
    loading.svg
  js/  (17 files)
    util/  (1 files)
      … 1 files under this directory
    views/  (9 files)
      … 9 files under this directory
    chat.js
    client.js
    common.js
    login.js
    models.js
    transcript.js
    vendor.js
  less/  (12 files)
    style/  (10 files)
      … 10 files under this directory
    style.less
    vendor.less
templates/  (21 files)
  includes/  (17 files)
    js/  (8 files)
      … 8 files under this directory
    modals/  (9 files)
      … 9 files under this directory
  base.html
  chat.html
  login.html
  transcript.html
uploads/  (1 files)
  .gitignore
.editorconfig
.eslintignore
.eslintrc
.gitignore
.travis.yml
CHANGELOG.md
CONTRIBUTING.md
Gruntfile.js
LICENSE
Procfile
README.md
TROUBLESHOOTING.md
Vagrantfile
app.js
app.json
bower.json
defaults.yml
package.json
settings.yml.sample
```

## Entry points

- [app.js](https://github.com/sdelements/lets-chat/blob/617207ff3c0c0bf8e3c7a915bd9ec03f1dd8390c/app.js)
- [app/auth/index.js](https://github.com/sdelements/lets-chat/blob/617207ff3c0c0bf8e3c7a915bd9ec03f1dd8390c/app/auth/index.js)
- [app/controllers/index.js](https://github.com/sdelements/lets-chat/blob/617207ff3c0c0bf8e3c7a915bd9ec03f1dd8390c/app/controllers/index.js)
- [app/core/index.js](https://github.com/sdelements/lets-chat/blob/617207ff3c0c0bf8e3c7a915bd9ec03f1dd8390c/app/core/index.js)
- [app/middlewares/index.js](https://github.com/sdelements/lets-chat/blob/617207ff3c0c0bf8e3c7a915bd9ec03f1dd8390c/app/middlewares/index.js)
- [app/models/index.js](https://github.com/sdelements/lets-chat/blob/617207ff3c0c0bf8e3c7a915bd9ec03f1dd8390c/app/models/index.js)
- [app/xmpp/index.js](https://github.com/sdelements/lets-chat/blob/617207ff3c0c0bf8e3c7a915bd9ec03f1dd8390c/app/xmpp/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 21 file(s) under api layer (observed from repository paths and static analysis). |
| app package | library | Observed | Groups 37 file(s) under app package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 26 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 6 file(s) under data layer (observed from repository paths and static analysis). |
| media package | library | Observed | Groups 8 file(s) under media package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 16 file(s) under service / domain layer (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.travis.yml` (ci)
- `app.json` (config)
- `bower.json` (config)
- `defaults.yml` (config)
- `docker/.dockerignore` (container)
- `docker/Dockerfile` (container)
- `docker/docker-compose.yml` (container)
- `extras/emotes/default.yml` (config)
- `extras/emotes/lets-chat.yml` (config)
- `locales/az.json` (config)
- `locales/de.json` (config)
- `locales/en.json` (config)
- `locales/es.json` (config)
- `locales/fi.json` (config)
- `locales/fr.json` (config)
- `locales/is.json` (config)
- `locales/it.json` (config)
- `locales/ja.json` (config)
- `locales/ko.json` (config)
- `locales/nl.json` (config)
- `locales/pl.json` (config)
- `locales/pt.json` (config)
- `locales/ru.json` (config)
- `locales/tr.json` (config)
- `locales/zh-TW.json` (config)
- `locales/zh.json` (config)
- `package.json` (manifest)

## Top-level layout

- `app` — 73 analysed file(s)
- `media` — 30 analysed file(s)
- `templates` — 21 analysed file(s)
- `(root files)` — 19 analysed file(s)
- `locales` — 17 analysed file(s)
- `extras` — 5 analysed file(s)
- `docker` — 4 analysed file(s)
- `uploads` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 181 file(s) were skipped during inventory (181 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `617207ff3c0c0bf8e3c7a915bd9ec03f1dd8390c` is the revision these paths and observations refer to.
