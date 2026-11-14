# Project structure: advplyr/audiobookshelf

**Analysed commit:** `c5e6e463e44de153006ea5aa739021d9a769e82b`

**Commit reference:** [c5e6e463e44de153006ea5aa739021d9a769e82b](https://github.com/advplyr/audiobookshelf/commit/c5e6e463e44de153006ea5aa739021d9a769e82b)

**Tree at this commit:** [advplyr/audiobookshelf@c5e6e463e44d](https://github.com/advplyr/audiobookshelf/tree/c5e6e463e44de153006ea5aa739021d9a769e82b)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | advplyr/audiobookshelf |
| Description | Self-hosted audiobook and podcast server |
| Stars | 15005 |
| Forks | 1260 |
| Licence | GPL-3.0 |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `c5e6e463e44de153006ea5aa739021d9a769e82b` |
| Retrieved at | 2026-11-14T19:11:41.708323+00:00 |
| Files in this snapshot | 791 |

## Directory tree

```text
.devcontainer/  (4 files)
  Dockerfile
  dev.js
  devcontainer.json
  post-create.sh
.github/  (17 files)
  ISSUE_TEMPLATE/  (3 files)
    bug.yaml
    config.yml
    feature.yml
  workflows/  (13 files)
    apply_comments.yaml
    close-issues-on-release.yml
    close_blank_issues.yaml
    codeql.yml
    component-tests.yml
    docker-build-v3.yml
    docker-build.yml
    i18n-integration.yml
    integration-test.yml
    lint-openapi.yml
    notify-abs-windows.yml
    translate-credits.yml
    unit-tests.yml
  pull_request_template.md
.vscode/  (4 files)
  extensions.json
  launch.json
  settings.json
  tasks.json
client/  (329 files)
  assets/  (11 files)
    ebooks/  (3 files)
      … 3 files under this directory
    absicons.css
    app.css
    defaultStyles.css
    draggable.css
    fonts.css
    tailwind.css
    transitions.css
    trix.css
  components/  (184 files)
    app/  (9 files)
      … 9 files under this directory
    cards/  (19 files)
      … 19 files under this directory
    content/  (1 files)
      … 1 files under this directory
    controls/  (7 files)
      … 7 files under this directory
    covers/  (6 files)
      … 6 files under this directory
    modals/  (58 files)
      … 58 files under this directory
    player/  (3 files)
      … 3 files under this directory
    prompt/  (2 files)
      … 2 files under this directory
    readers/  (5 files)
      … 5 files under this directory
    stats/  (7 files)
      … 7 files under this directory
    tables/  (21 files)
      … 21 files under this directory
    ui/  (29 files)
      … 29 files under this directory
    widgets/  (17 files)
      … 17 files under this directory
  cypress/  (9 files)
    support/  (3 files)
      … 3 files under this directory
    tests/  (6 files)
      … 6 files under this directory
  layouts/  (3 files)
    blank.vue
    default.vue
    error.vue
  middleware/  (1 files)
    authenticated.js
  mixins/  (3 files)
    bookshelfCardsHelpers.js
    menuKeyboardNavigation.js
    uploadHelpers.js
  pages/  (42 files)
    audiobook/  (3 files)
      … 3 files under this directory
    author/  (1 files)
      … 1 files under this directory
    batch/  (1 files)
      … 1 files under this directory
    collection/  (1 files)
      … 1 files under this directory
    config/  (18 files)
      … 18 files under this directory
    item/  (1 files)
      … 1 files under this directory
    library/  (9 files)
      … 9 files under this directory
    playlist/  (1 files)
      … 1 files under this directory
    share/  (1 files)
      … 1 files under this directory
    upload/  (1 files)
      … 1 files under this directory
    account.vue
    config.vue
    index.vue
    login.vue
    oops.vue
  players/  (5 files)
    AudioTrack.js
    CastPlayer.js
    LocalAudioPlayer.js
    PlayerHandler.js
    castUtils.js
  plugins/  (8 files)
    axios.js
    chromecast.js
    constants.js
    i18n.js
    init.client.js
    toast.js
    utils.js
    version.js
  static/  (9 files)
    fonts/  (3 files)
      … 3 files under this directory
    libarchive/  (2 files)
      … 2 files under this directory
    libs/  (2 files)
      … 2 files under this directory
    icon.svg
    robots.txt
  store/  (7 files)
    globals.js
    index.js
    libraries.js
    scanners.js
    tasks.js
    user.js
    users.js
  strings/  (43 files)
    ar.json
    be.json
    bg.json
    bn.json
    ca.json
    cs.json
    da.json
    de.json
    el.json
    en-us.json
    es.json
    et.json
    eu.json
    fa.json
    fi.json
    fr.json
    gu.json
    he.json
    hi.json
    hr.json
    hu.json
    is.json
    it.json
    ja.json
    … 19 more files
  cypress.config.js
  nuxt.config.js
  package.json
  postcss.config.js
docs/  (28 files)
  controllers/  (6 files)
    AuthorController.yaml
    EmailController.yaml
    LibraryController.yaml
    NotificationController.yaml
    PodcastController.yaml
    SeriesController.yaml
  objects/  (18 files)
    entities/  (3 files)
      … 3 files under this directory
    files/  (3 files)
      … 3 files under this directory
    mediaTypes/  (3 files)
      … 3 files under this directory
    metadata/  (4 files)
      … 4 files under this directory
    settings/  (1 files)
      … 1 files under this directory
    Folder.yaml
    Library.yaml
    LibraryItem.yaml
    Notification.yaml
  README.md
  openapi.json
  root.yaml
  schemas.yaml
images/  (1 files)
  banner.svg
server/  (393 files)
  auth/  (3 files)
    LocalAuthStrategy.js
    OidcAuthStrategy.js
    TokenManager.js
  controllers/  (23 files)
    ApiKeyController.js
    AuthorController.js
    BackupController.js
    CacheController.js
    CollectionController.js
    CustomMetadataProviderController.js
    EmailController.js
    FileSystemController.js
    LibraryController.js
    LibraryItemController.js
    MeController.js
    MiscController.js
    NotificationController.js
    PlaylistController.js
    PodcastController.js
    RSSFeedController.js
    SearchController.js
    SeriesController.js
    SessionController.js
    ShareController.js
    StatsController.js
    ToolsController.js
    UserController.js
  finders/  (3 files)
    AuthorFinder.js
    BookFinder.js
    PodcastFinder.js
  libs/  (302 files)
    archiver/  (107 files)
      … 107 files under this directory
    async/  (2 files)
      … 2 files under this directory
    bcryptjs/  (2 files)
      … 2 files under this directory
    busboy/  (5 files)
      … 5 files under this directory
    commandLineArgs/  (1 files)
      … 1 files under this directory
    dateAndTime/  (2 files)
      … 2 files under this directory
    expressFileupload/  (10 files)
      … 10 files under this directory
    fastSort/  (2 files)
      … 2 files under this directory
    fluentFfmpeg/  (18 files)
      … 18 files under this directory
    fsExtra/  (24 files)
      … 24 files under this directory
    fusejs/  (1 files)
      … 1 files under this directory
    imageType/  (3 files)
      … 3 files under this directory
    isexe/  (4 files)
      … 4 files under this directory
    jsonwebtoken/  (9 files)
      … 9 files under this directory
    jwa/  (7 files)
      … 7 files under this directory
    jws/  (6 files)
      … 6 files under this directory
    libarchive/  (5 files)
      … 5 files under this directory
    lodash.once/  (2 files)
      … 2 files under this directory
    memorystore/  (2 files)
      … 2 files under this directory
    nodeCron/  (16 files)
      … 16 files under this directory
    nodeFfprobe/  (2 files)
      … 2 files under this directory
    nodeStreamZip/  (2 files)
      … 2 files under this directory
    passportLocal/  (3 files)
      … 3 files under this directory
    readChunk/  (4 files)
      … 4 files under this directory
    recursiveReaddirAsync/  (2 files)
      … 2 files under this directory
    requestIp/  (3 files)
      … 3 files under this directory
    rss/  (2 files)
      … 2 files under this directory
    sanitizeHtml/  (2 files)
      … 2 files under this directory
    streamsearch/  (2 files)
      … 2 files under this directory
    uaParser/  (2 files)
      … 2 files under this directory
    umzug/  (11 files)
      … 11 files under this directory
    universalify/  (2 files)
      … 2 files under this directory
    watcher/  (32 files)
      … 32 files under this directory
    which/  (2 files)
      … 2 files under this directory
    xml/  (3 files)
      … 3 files under this directory
  managers/  (18 files)
    AbMergeManager.js
    ApiCacheManager.js
    AudioMetadataManager.js
    BackupManager.js
    BinaryManager.js
    CacheManager.js
    CoverManager.js
    CoverSearchManager.js
    CronManager.js
    EmailManager.js
    LogManager.js
    MigrationManager.js
    NotificationManager.js
    PlaybackSessionManager.js
    PodcastManager.js
    RssFeedManager.js
    ShareManager.js
    TaskManager.js
  migrations/  (17 files)
    changelog.md
    readme.md
    v2.15.0-series-column-unique.js
    v2.15.1-reindex-nocase.js
    v2.15.2-index-creation.js
    v2.17.0-uuid-replacement.js
    v2.17.3-fk-constraints.js
    v2.17.4-use-subfolder-for-oidc-redirect-uris.js
    v2.17.5-remove-host-from-feed-urls.js
    v2.17.6-share-add-isdownloadable.js
    v2.17.7-add-indices.js
    v2.19.1-copy-title-to-library-items.js
    v2.19.4-improve-podcast-queries.js
    v2.20.0-improve-author-sort-queries.js
    v2.26.0-create-auth-tables.js
    v2.33.0-add-discover-query-indexes.js
    v2.35.0-add-last-refresh-token.js
  models/  (21 files)
    ApiKey.js
    Author.js
    Book.js
    BookAuthor.js
    BookSeries.js
    Collection.js
    CollectionBook.js
    CustomMetadataProvider.js
    Device.js
    Feed.js
    FeedEpisode.js
    Library.js
    LibraryFolder.js
    LibraryItem.js
    MediaItemShare.js
    MediaProgress.js
    PlaybackSession.js
    Playlist.js
    PlaylistMediaItem.js
    Podcast.js
    PodcastEpisode.js
  Auth.js
  Database.js
  Logger.js
  Server.js
  SocketAuthority.js
  Watcher.js
.dockerignore
.editorconfig
.gitattributes
.gitignore
.prettierrc
Dockerfile
LICENSE
custom-metadata-provider-specification.yaml
docker-compose.yml
docker-template.xml
eslint.config.mjs
index.js
package.json
prod.js
readme.md
```

## Entry points

- [client/store/index.js](https://github.com/advplyr/audiobookshelf/blob/c5e6e463e44de153006ea5aa739021d9a769e82b/client/store/index.js)
- [index.js](https://github.com/advplyr/audiobookshelf/blob/c5e6e463e44de153006ea5aa739021d9a769e82b/index.js)
- [server/Server.js](https://github.com/advplyr/audiobookshelf/blob/c5e6e463e44de153006ea5aa739021d9a769e82b/server/Server.js)
- [server/libs/archiver/index.js](https://github.com/advplyr/audiobookshelf/blob/c5e6e463e44de153006ea5aa739021d9a769e82b/server/libs/archiver/index.js)
- [server/libs/async/index.js](https://github.com/advplyr/audiobookshelf/blob/c5e6e463e44de153006ea5aa739021d9a769e82b/server/libs/async/index.js)
- [server/libs/bcryptjs/index.js](https://github.com/advplyr/audiobookshelf/blob/c5e6e463e44de153006ea5aa739021d9a769e82b/server/libs/bcryptjs/index.js)
- [server/libs/busboy/index.js](https://github.com/advplyr/audiobookshelf/blob/c5e6e463e44de153006ea5aa739021d9a769e82b/server/libs/busboy/index.js)
- [server/libs/commandLineArgs/index.js](https://github.com/advplyr/audiobookshelf/blob/c5e6e463e44de153006ea5aa739021d9a769e82b/server/libs/commandLineArgs/index.js)
- [server/libs/dateAndTime/index.js](https://github.com/advplyr/audiobookshelf/blob/c5e6e463e44de153006ea5aa739021d9a769e82b/server/libs/dateAndTime/index.js)
- [server/libs/expressFileupload/index.js](https://github.com/advplyr/audiobookshelf/blob/c5e6e463e44de153006ea5aa739021d9a769e82b/server/libs/expressFileupload/index.js)
- [server/libs/fastSort/index.js](https://github.com/advplyr/audiobookshelf/blob/c5e6e463e44de153006ea5aa739021d9a769e82b/server/libs/fastSort/index.js)
- [server/libs/fluentFfmpeg/index.js](https://github.com/advplyr/audiobookshelf/blob/c5e6e463e44de153006ea5aa739021d9a769e82b/server/libs/fluentFfmpeg/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 23 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 48 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 27 file(s) under data layer (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 264 file(s) under external integrations (observed from repository paths and static analysis). |
| server package | library | Observed | Groups 284 file(s) under server package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 6 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.devcontainer/Dockerfile` (container)
- `.devcontainer/devcontainer.json` (config)
- `.dockerignore` (container)
- `.editorconfig` (config)
- `.github/ISSUE_TEMPLATE/bug.yaml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature.yml` (config)
- `.github/workflows/apply_comments.yaml` (ci)
- `.github/workflows/close-issues-on-release.yml` (ci)
- `.github/workflows/close_blank_issues.yaml` (ci)
- `.github/workflows/codeql.yml` (ci)
- `.github/workflows/component-tests.yml` (ci)
- `.github/workflows/docker-build-v3.yml` (ci)
- `.github/workflows/docker-build.yml` (ci)
- `.github/workflows/i18n-integration.yml` (ci)
- `.github/workflows/integration-test.yml` (ci)
- `.github/workflows/lint-openapi.yml` (ci)
- `.github/workflows/notify-abs-windows.yml` (ci)
- `.github/workflows/translate-credits.yml` (ci)
- `.github/workflows/unit-tests.yml` (ci)
- `.vscode/extensions.json` (config)
- `.vscode/launch.json` (config)
- `.vscode/settings.json` (config)
- `.vscode/tasks.json` (config)
- `Dockerfile` (container)
- `client/package.json` (manifest)
- `client/strings/ar.json` (config)
- `client/strings/be.json` (config)
- `client/strings/bg.json` (config)
- `client/strings/bn.json` (config)
- `client/strings/ca.json` (config)
- `client/strings/cs.json` (config)
- `client/strings/da.json` (config)
- `client/strings/de.json` (config)
- `client/strings/el.json` (config)
- `client/strings/en-us.json` (config)
- `client/strings/es.json` (config)
- `client/strings/et.json` (config)
- `client/strings/eu.json` (config)
- `client/strings/fa.json` (config)
- `client/strings/fi.json` (config)
- `client/strings/fr.json` (config)
- `client/strings/gu.json` (config)
- `client/strings/he.json` (config)
- `client/strings/hi.json` (config)
- `client/strings/hr.json` (config)
- `client/strings/hu.json` (config)
- `client/strings/is.json` (config)
- `client/strings/it.json` (config)
- `client/strings/ja.json` (config)
- `client/strings/ko.json` (config)
- `client/strings/lt.json` (config)
- `client/strings/lv.json` (config)
- `client/strings/nl.json` (config)
- `client/strings/no.json` (config)
- `client/strings/pl.json` (config)
- `client/strings/pt-br.json` (config)
- `client/strings/ro.json` (config)
- `client/strings/ru.json` (config)
- `client/strings/sk.json` (config)
- `client/strings/sl.json` (config)
- `client/strings/sv.json` (config)
- `client/strings/ta.json` (config)
- `client/strings/tr.json` (config)
- `client/strings/uk.json` (config)
- `client/strings/uz.json` (config)
- `client/strings/vi-vn.json` (config)
- `client/strings/zh-cn.json` (config)
- `client/strings/zh-tw.json` (config)
- `custom-metadata-provider-specification.yaml` (config)
- `docker-compose.yml` (container)
- `docs/controllers/AuthorController.yaml` (config)
- `docs/controllers/EmailController.yaml` (config)
- `docs/controllers/LibraryController.yaml` (config)
- `docs/controllers/NotificationController.yaml` (config)
- `docs/controllers/PodcastController.yaml` (config)
- `docs/controllers/SeriesController.yaml` (config)
- `docs/objects/Folder.yaml` (config)
- `docs/objects/Library.yaml` (config)
- `docs/objects/LibraryItem.yaml` (config)
- `docs/objects/Notification.yaml` (config)
- `docs/objects/entities/Author.yaml` (config)
- `docs/objects/entities/PodcastEpisode.yaml` (config)
- `docs/objects/entities/Series.yaml` (config)
- `docs/objects/files/AudioFile.yaml` (config)
- `docs/objects/files/AudioTrack.yaml` (config)
- `docs/objects/files/EBookFile.yaml` (config)
- `docs/objects/mediaTypes/Book.yaml` (config)
- `docs/objects/mediaTypes/Podcast.yaml` (config)
- `docs/objects/mediaTypes/media.yaml` (config)
- `docs/objects/metadata/AudioMetaTags.yaml` (config)
- `docs/objects/metadata/BookMetadata.yaml` (config)
- `docs/objects/metadata/FileMetadata.yaml` (config)
- `docs/objects/metadata/PodcastMetadata.yaml` (config)
- `docs/objects/settings/EmailSettings.yaml` (config)
- `docs/openapi.json` (config)
- `docs/root.yaml` (config)
- `docs/schemas.yaml` (config)
- `package.json` (manifest)

## Top-level layout

- `server` — 393 analysed file(s)
- `client` — 329 analysed file(s)
- `docs` — 28 analysed file(s)
- `.github` — 17 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `.devcontainer` — 4 analysed file(s)
- `.vscode` — 4 analysed file(s)
- `images` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 9 file(s) were skipped during inventory (9 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `c5e6e463e44de153006ea5aa739021d9a769e82b` is the revision these paths and observations refer to.
