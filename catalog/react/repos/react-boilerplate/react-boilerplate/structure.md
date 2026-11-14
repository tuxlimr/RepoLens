# Project structure: react-boilerplate/react-boilerplate

**Analysed commit:** `d19099afeff64ecfb09133c06c1cb18c0d40887e`

**Commit reference:** [d19099afeff64ecfb09133c06c1cb18c0d40887e](https://github.com/react-boilerplate/react-boilerplate/commit/d19099afeff64ecfb09133c06c1cb18c0d40887e)

**Tree at this commit:** [react-boilerplate/react-boilerplate@d19099afeff6](https://github.com/react-boilerplate/react-boilerplate/tree/d19099afeff64ecfb09133c06c1cb18c0d40887e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | react-boilerplate/react-boilerplate |
| Description | 🔥 A highly scalable, offline-first foundation with the best developer experience and a focus on performance and best practices. |
| Stars | 29440 |
| Forks | 5958 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `d19099afeff64ecfb09133c06c1cb18c0d40887e` |
| Retrieved at | 2026-11-14T19:13:03.166952+00:00 |
| Files in this snapshot | 325 |

## Directory tree

```text
.github/  (5 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  PULL_REQUEST_TEMPLATE.md
  issue-close-app.yml
  lock.yml
app/  (175 files)
  components/  (69 files)
    A/  (2 files)
      … 2 files under this directory
    Button/  (9 files)
      … 9 files under this directory
    Footer/  (6 files)
      … 6 files under this directory
    H1/  (2 files)
      … 2 files under this directory
    H2/  (2 files)
      … 2 files under this directory
    H3/  (2 files)
      … 2 files under this directory
    Header/  (12 files)
      … 12 files under this directory
    Img/  (2 files)
      … 2 files under this directory
    IssueIcon/  (2 files)
      … 2 files under this directory
    List/  (6 files)
      … 6 files under this directory
    ListItem/  (6 files)
      … 6 files under this directory
    LoadingIndicator/  (7 files)
      … 7 files under this directory
    ReposList/  (3 files)
      … 3 files under this directory
    Toggle/  (5 files)
      … 5 files under this directory
    ToggleOption/  (3 files)
      … 3 files under this directory
  containers/  (79 files)
    App/  (10 files)
      … 10 files under this directory
    FeaturePage/  (11 files)
      … 11 files under this directory
    HomePage/  (25 files)
      … 25 files under this directory
    LanguageProvider/  (9 files)
      … 9 files under this directory
    LocaleToggle/  (6 files)
      … 6 files under this directory
    NotFoundPage/  (4 files)
      … 4 files under this directory
    RepoListItem/  (14 files)
      … 14 files under this directory
  tests/  (2 files)
    i18n.test.js
    store.test.js
  translations/  (2 files)
    de.json
    en.json
  utils/  (15 files)
    tests/  (6 files)
      … 6 files under this directory
    checkStore.js
    constants.js
    history.js
    injectReducer.js
    injectSaga.js
    loadable.js
    reducerInjectors.js
    request.js
    sagaInjectors.js
  .htaccess
  .nginx.conf
  app.js
  configureStore.js
  global-styles.js
  i18n.js
  index.html
  reducers.js
docs/  (32 files)
  css/  (4 files)
    README.md
    linting.md
    remove.md
    sanitize.md
  forks/  (1 files)
    README.md
  general/  (12 files)
    README.md
    commands.md
    components.md
    debugging.md
    deployment.md
    editor.md
    faq.md
    files.md
    gotchas.md
    introduction.md
    remove.md
    server-configs.md
  js/  (9 files)
    README.md
    async-components.md
    i18n.md
    immer.md
    redux-saga.md
    redux.md
    remove.md
    reselect.md
    routing.md
  maintenance/  (1 files)
    dependency.md
  testing/  (4 files)
    README.md
    component-testing.md
    remote-testing.md
    unit-testing.md
  README.md
internals/  (87 files)
  generators/  (28 files)
    component/  (5 files)
      … 5 files under this directory
    container/  (13 files)
      … 13 files under this directory
    language/  (8 files)
      … 8 files under this directory
    utils/  (1 files)
      … 1 files under this directory
    index.js
  mocks/  (2 files)
    cssModule.js
    image.js
  scripts/  (10 files)
    helpers/  (4 files)
      … 4 files under this directory
    analyze.js
    clean.js
    extract-intl.js
    generate-templates-for-linting.js
    npmcheckversion.js
    setup.js
  templates/  (43 files)
    containers/  (21 files)
      … 21 files under this directory
    tests/  (2 files)
      … 2 files under this directory
    translations/  (1 files)
      … 1 files under this directory
    utils/  (13 files)
      … 13 files under this directory
    app.js
    configureStore.js
    global-styles.js
    i18n.js
    index.html
    reducers.js
  testing/  (1 files)
    test-bundler.js
  webpack/  (3 files)
    webpack.base.babel.js
    webpack.dev.babel.js
    webpack.prod.babel.js
server/  (7 files)
  middlewares/  (3 files)
    addDevMiddlewares.js
    addProdMiddlewares.js
    frontendMiddleware.js
  argv.js
  index.js
  logger.js
  port.js
.all-contributorsrc
.editorconfig
.eslintrc.js
.gitattributes
.gitignore
.nvmrc
.prettierignore
.prettierrc
.stylelintrc
.travis.yml
CODE_OF_CONDUCT.md
CONTRIBUTING.md
Changelog.md
LICENSE.md
README.md
appveyor.yml
babel.config.js
jest.config.js
package.json
```

## Entry points

- [app/app.js](https://github.com/react-boilerplate/react-boilerplate/blob/d19099afeff64ecfb09133c06c1cb18c0d40887e/app/app.js)
- [app/components/A/index.js](https://github.com/react-boilerplate/react-boilerplate/blob/d19099afeff64ecfb09133c06c1cb18c0d40887e/app/components/A/index.js)
- [app/components/Button/index.js](https://github.com/react-boilerplate/react-boilerplate/blob/d19099afeff64ecfb09133c06c1cb18c0d40887e/app/components/Button/index.js)
- [app/components/Footer/index.js](https://github.com/react-boilerplate/react-boilerplate/blob/d19099afeff64ecfb09133c06c1cb18c0d40887e/app/components/Footer/index.js)
- [app/components/H1/index.js](https://github.com/react-boilerplate/react-boilerplate/blob/d19099afeff64ecfb09133c06c1cb18c0d40887e/app/components/H1/index.js)
- [app/components/H2/index.js](https://github.com/react-boilerplate/react-boilerplate/blob/d19099afeff64ecfb09133c06c1cb18c0d40887e/app/components/H2/index.js)
- [app/components/H3/index.js](https://github.com/react-boilerplate/react-boilerplate/blob/d19099afeff64ecfb09133c06c1cb18c0d40887e/app/components/H3/index.js)
- [app/components/Header/index.js](https://github.com/react-boilerplate/react-boilerplate/blob/d19099afeff64ecfb09133c06c1cb18c0d40887e/app/components/Header/index.js)
- [app/components/Img/index.js](https://github.com/react-boilerplate/react-boilerplate/blob/d19099afeff64ecfb09133c06c1cb18c0d40887e/app/components/Img/index.js)
- [app/components/IssueIcon/index.js](https://github.com/react-boilerplate/react-boilerplate/blob/d19099afeff64ecfb09133c06c1cb18c0d40887e/app/components/IssueIcon/index.js)
- [app/components/List/index.js](https://github.com/react-boilerplate/react-boilerplate/blob/d19099afeff64ecfb09133c06c1cb18c0d40887e/app/components/List/index.js)
- [app/components/ListItem/index.js](https://github.com/react-boilerplate/react-boilerplate/blob/d19099afeff64ecfb09133c06c1cb18c0d40887e/app/components/ListItem/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| app package | library | Observed | Groups 87 file(s) under app package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| internals package | library | Observed | Groups 48 file(s) under internals package (observed from repository paths and static analysis). |
| server package | library | Observed | Groups 7 file(s) under server package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 97 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/issue-close-app.yml` (config)
- `.github/lock.yml` (config)
- `.travis.yml` (ci)
- `app/translations/de.json` (config)
- `app/translations/en.json` (config)
- `appveyor.yml` (config)
- `internals/templates/translations/en.json` (config)
- `package.json` (manifest)

## Top-level layout

- `app` — 175 analysed file(s)
- `internals` — 87 analysed file(s)
- `docs` — 32 analysed file(s)
- `(root files)` — 19 analysed file(s)
- `server` — 7 analysed file(s)
- `.github` — 5 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `d19099afeff64ecfb09133c06c1cb18c0d40887e` is the revision these paths and observations refer to.
