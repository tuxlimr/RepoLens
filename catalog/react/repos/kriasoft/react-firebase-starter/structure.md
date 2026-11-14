# Project structure: kriasoft/react-firebase-starter

**Analysed commit:** `69328e57cbc832c87b9cce9a9955fa21515545de`

**Commit reference:** [69328e57cbc832c87b9cce9a9955fa21515545de](https://github.com/kriasoft/react-firebase-starter/commit/69328e57cbc832c87b9cce9a9955fa21515545de)

**Tree at this commit:** [kriasoft/react-firebase-starter@69328e57cbc8](https://github.com/kriasoft/react-firebase-starter/tree/69328e57cbc832c87b9cce9a9955fa21515545de)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | kriasoft/react-firebase-starter |
| Description | Boilerplate (seed) project for creating web apps with React.js, GraphQL.js and Relay |
| Stars | 4511 |
| Forks | 746 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `69328e57cbc832c87b9cce9a9955fa21515545de` |
| Retrieved at | 2026-11-14T19:14:43.625607+00:00 |
| Files in this snapshot | 139 |

## Directory tree

```text
.circleci/  (2 files)
  Dockerfile
  config.yml
.github/  (1 files)
  FUNDING.yml
.vscode/  (3 files)
  snippets/  (1 files)
    javascript.json
  launch.json
  settings.json
migrations/  (1 files)
  20180101000000_initial.js
public/  (1 files)
  manifest.json
scripts/  (8 files)
  db-backup.js
  db-restore.js
  db.js
  post-deploy.js
  pre-deploy.js
  psql.js
  setup.js
  update-schema.js
seeds/  (1 files)
  seed.js
src/  (107 files)
  admin/  (4 files)
    AdminLayout.js
    AdminStoryList.js
    AdminUserList.js
    index.js
  common/  (15 files)
    App.js
    App.test.js
    AppBar.js
    AutoUpdater.js
    CustomerChat.js
    ErrorPage.js
    Layout.js
    LayoutFooter.js
    Link.js
    LoginButton.js
    LoginDialog.js
    LoginForm.js
    TextField.js
    UserMenu.js
    UserSettingsDialog.js
  hooks/  (9 files)
    index.js
    useAuth.js
    useConfig.js
    useFacebook.js
    useFirebase.js
    useGoogleMaps.js
    useHistory.js
    useRelay.js
    useReset.js
  icons/  (7 files)
    Facebook.js
    GitHub.js
    Google.js
    Instagram.js
    Logout.js
    Settings.js
    Twitter.js
  landing/  (5 files)
    Home.js
    HomeHero.js
    HomeSponsors.js
    HomeStack.js
    index.js
  legal/  (3 files)
    Privacy.js
    Terms.js
    index.js
  misc/  (2 files)
    About.js
    index.js
  mutations/  (4 files)
    DeleteUser.js
    LikeStory.js
    UpdateUser.js
    UpsertStory.js
  news/  (4 files)
    News.js
    Story.js
    SubmitDialog.js
    index.js
  server/  (39 files)
    mutations/  (4 files)
      … 4 files under this directory
    queries/  (4 files)
      … 4 files under this directory
    templates/  (4 files)
      … 4 files under this directory
    types/  (6 files)
      … 6 files under this directory
    utils/  (7 files)
      … 7 files under this directory
    api.js
    app.js
    config.js
    context.js
    db.js
    errors.js
    index.js
    login.js
    node.js
    passport.js
    relay.js
    schema.js
    ssr.js
    validator.js
  user/  (4 files)
    Account.js
    Login.js
    UserProfile.js
    index.js
  utils/  (6 files)
    env.js
    gtag.js
    index.js
    loading.js
    openWindow.js
    scrolling.js
  index.js
  relay.js
  router.js
  serviceWorker.js
  theme.js
ssl/  (1 files)
  README.md
.babelrc
.editorconfig
.eslintrc
.gitattributes
.gitignore
.prettierignore
.prettierrc
LICENSE.txt
README.md
firebase.json
knexfile.js
package.json
schema.graphql
storage.rules
```

## Entry points

- [src/admin/index.js](https://github.com/kriasoft/react-firebase-starter/blob/69328e57cbc832c87b9cce9a9955fa21515545de/src/admin/index.js)
- [src/common/App.js](https://github.com/kriasoft/react-firebase-starter/blob/69328e57cbc832c87b9cce9a9955fa21515545de/src/common/App.js)
- [src/hooks/index.js](https://github.com/kriasoft/react-firebase-starter/blob/69328e57cbc832c87b9cce9a9955fa21515545de/src/hooks/index.js)
- [src/index.js](https://github.com/kriasoft/react-firebase-starter/blob/69328e57cbc832c87b9cce9a9955fa21515545de/src/index.js)
- [src/landing/index.js](https://github.com/kriasoft/react-firebase-starter/blob/69328e57cbc832c87b9cce9a9955fa21515545de/src/landing/index.js)
- [src/legal/index.js](https://github.com/kriasoft/react-firebase-starter/blob/69328e57cbc832c87b9cce9a9955fa21515545de/src/legal/index.js)
- [src/misc/index.js](https://github.com/kriasoft/react-firebase-starter/blob/69328e57cbc832c87b9cce9a9955fa21515545de/src/misc/index.js)
- [src/news/index.js](https://github.com/kriasoft/react-firebase-starter/blob/69328e57cbc832c87b9cce9a9955fa21515545de/src/news/index.js)
- [src/server/app.js](https://github.com/kriasoft/react-firebase-starter/blob/69328e57cbc832c87b9cce9a9955fa21515545de/src/server/app.js)
- [src/server/index.js](https://github.com/kriasoft/react-firebase-starter/blob/69328e57cbc832c87b9cce9a9955fa21515545de/src/server/index.js)
- [src/server/mutations/index.js](https://github.com/kriasoft/react-firebase-starter/blob/69328e57cbc832c87b9cce9a9955fa21515545de/src/server/mutations/index.js)
- [src/server/queries/index.js](https://github.com/kriasoft/react-firebase-starter/blob/69328e57cbc832c87b9cce9a9955fa21515545de/src/server/queries/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| admin package | library | Observed | Groups 4 file(s) under admin package (observed from repository paths and static analysis). |
| common package | library | Observed | Groups 15 file(s) under common package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 9 file(s) under hooks package (observed from repository paths and static analysis). |
| icons package | library | Observed | Groups 7 file(s) under icons package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| landing package | library | Observed | Groups 5 file(s) under landing package (observed from repository paths and static analysis). |
| legal package | library | Observed | Groups 3 file(s) under legal package (observed from repository paths and static analysis). |
| migrations package | library | Observed | Groups 1 file(s) under migrations package (observed from repository paths and static analysis). |
| misc package | library | Observed | Groups 2 file(s) under misc package (observed from repository paths and static analysis). |
| mutations package | library | Observed | Groups 4 file(s) under mutations package (observed from repository paths and static analysis). |
| news package | library | Observed | Groups 4 file(s) under news package (observed from repository paths and static analysis). |
| relay.js package | library | Observed | Groups 1 file(s) under relay.js package (observed from repository paths and static analysis). |
| router.js package | library | Observed | Groups 1 file(s) under router.js package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 8 file(s) under scripts package (observed from repository paths and static analysis). |
| seeds package | library | Observed | Groups 1 file(s) under seeds package (observed from repository paths and static analysis). |
| server package | library | Observed | Groups 33 file(s) under server package (observed from repository paths and static analysis). |
| serviceWorker.js package | library | Observed | Groups 1 file(s) under serviceworker.js package (observed from repository paths and static analysis). |
| theme.js package | library | Observed | Groups 1 file(s) under theme.js package (observed from repository paths and static analysis). |
| user package | library | Observed | Groups 4 file(s) under user package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 6 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.circleci/Dockerfile` (ci)
- `.circleci/config.yml` (ci)
- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.vscode/launch.json` (config)
- `.vscode/settings.json` (config)
- `.vscode/snippets/javascript.json` (config)
- `firebase.json` (config)
- `package.json` (manifest)
- `public/manifest.json` (config)

## Top-level layout

- `src` — 107 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `scripts` — 8 analysed file(s)
- `.vscode` — 3 analysed file(s)
- `.circleci` — 2 analysed file(s)
- `.github` — 1 analysed file(s)
- `migrations` — 1 analysed file(s)
- `public` — 1 analysed file(s)
- `seeds` — 1 analysed file(s)
- `ssl` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 3 file(s) were skipped during inventory (3 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `69328e57cbc832c87b9cce9a9955fa21515545de` is the revision these paths and observations refer to.
