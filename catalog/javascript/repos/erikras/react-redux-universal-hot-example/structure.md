# Project structure: erikras/react-redux-universal-hot-example

**Analysed commit:** `076e24bcd9b363a9ce84f0ebbd0fe036f15561e2`

**Commit reference:** [076e24bcd9b363a9ce84f0ebbd0fe036f15561e2](https://github.com/erikras/react-redux-universal-hot-example/commit/076e24bcd9b363a9ce84f0ebbd0fe036f15561e2)

**Tree at this commit:** [erikras/react-redux-universal-hot-example@076e24bcd9b3](https://github.com/erikras/react-redux-universal-hot-example/tree/076e24bcd9b363a9ce84f0ebbd0fe036f15561e2)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | erikras/react-redux-universal-hot-example |
| Description | A starter boilerplate for a universal webapp using express, react, redux, webpack, and react-transform |
| Stars | 12049 |
| Forks | 2444 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `076e24bcd9b363a9ce84f0ebbd0fe036f15561e2` |
| Retrieved at | 2026-11-14T19:12:11.141231+00:00 |
| Files in this snapshot | 97 |

## Directory tree

```text
api/  (16 files)
  __tests__/  (1 files)
    api-test.js
  actions/  (13 files)
    __tests__/  (3 files)
      … 3 files under this directory
    survey/  (2 files)
      … 2 files under this directory
    widget/  (3 files)
      … 3 files under this directory
    index.js
    loadAuth.js
    loadInfo.js
    login.js
    logout.js
  utils/  (1 files)
    url.js
  api.js
bin/  (2 files)
  api.js
  server.js
docs/  (7 files)
  AddingAPage/  (1 files)
    AddingAPage.md
  AddingToHomePage/  (1 files)
    AddingToHomePage.md
  ExploringTheDemoApp/  (1 files)
    ExploringTheDemoApp.md
  InstallingTheKit/  (1 files)
    InstallingTheKit.md
  ApiConfig.md
  Ducks.md
  InlineStyles.md
src/  (53 files)
  components/  (12 files)
    CounterButton/  (1 files)
      … 1 files under this directory
    GithubButton/  (1 files)
      … 1 files under this directory
    InfoBar/  (2 files)
      … 2 files under this directory
    MiniInfoBar/  (1 files)
      … 1 files under this directory
    SurveyForm/  (3 files)
      … 3 files under this directory
    WidgetForm/  (2 files)
      … 2 files under this directory
    __tests__/  (1 files)
      … 1 files under this directory
    index.js
  containers/  (19 files)
    About/  (1 files)
      … 1 files under this directory
    App/  (2 files)
      … 2 files under this directory
    Chat/  (2 files)
      … 2 files under this directory
    DevTools/  (1 files)
      … 1 files under this directory
    Home/  (2 files)
      … 2 files under this directory
    Login/  (2 files)
      … 2 files under this directory
    LoginSuccess/  (1 files)
      … 1 files under this directory
    NotFound/  (1 files)
      … 1 files under this directory
    Pagination/  (3 files)
      … 3 files under this directory
    Survey/  (1 files)
      … 1 files under this directory
    Widgets/  (2 files)
      … 2 files under this directory
    index.js
  helpers/  (2 files)
    ApiClient.js
    Html.js
  redux/  (8 files)
    middleware/  (1 files)
      … 1 files under this directory
    modules/  (6 files)
      … 6 files under this directory
    create.js
  theme/  (7 files)
    bootstrap.config.js
    bootstrap.config.prod.js
    bootstrap.overrides.scss
    font-awesome.config.js
    font-awesome.config.less
    font-awesome.config.prod.js
    variables.scss
  utils/  (1 files)
    validation.js
  client.js
  config.js
  routes.js
  server.js
webpack/  (4 files)
  dev.config.js
  prod.config.js
  webpack-dev-server.js
  webpack-isomorphic-tools.js
.babelrc
.editorconfig
.eslintignore
.eslintrc
.gitignore
.travis.yml
CONTRIBUTING.md
LICENSE
README.md
app.json
circle.yml
karma.conf.js
package.json
server.babel.js
tests.webpack.js
```

## Entry points

- [bin/server.js](https://github.com/erikras/react-redux-universal-hot-example/blob/076e24bcd9b363a9ce84f0ebbd0fe036f15561e2/bin/server.js)
- [api/actions/index.js](https://github.com/erikras/react-redux-universal-hot-example/blob/076e24bcd9b363a9ce84f0ebbd0fe036f15561e2/api/actions/index.js)
- [api/actions/survey/index.js](https://github.com/erikras/react-redux-universal-hot-example/blob/076e24bcd9b363a9ce84f0ebbd0fe036f15561e2/api/actions/survey/index.js)
- [api/actions/widget/index.js](https://github.com/erikras/react-redux-universal-hot-example/blob/076e24bcd9b363a9ce84f0ebbd0fe036f15561e2/api/actions/widget/index.js)
- [src/components/index.js](https://github.com/erikras/react-redux-universal-hot-example/blob/076e24bcd9b363a9ce84f0ebbd0fe036f15561e2/src/components/index.js)
- [src/containers/App/App.js](https://github.com/erikras/react-redux-universal-hot-example/blob/076e24bcd9b363a9ce84f0ebbd0fe036f15561e2/src/containers/App/App.js)
- [src/containers/index.js](https://github.com/erikras/react-redux-universal-hot-example/blob/076e24bcd9b363a9ce84f0ebbd0fe036f15561e2/src/containers/index.js)
- [src/server.js](https://github.com/erikras/react-redux-universal-hot-example/blob/076e24bcd9b363a9ce84f0ebbd0fe036f15561e2/src/server.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 16 file(s) under api layer (observed from repository paths and static analysis). |
| bin package | library | Observed | Groups 2 file(s) under bin package (observed from repository paths and static analysis). |
| client.js package | library | Observed | Groups 1 file(s) under client.js package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 10 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| config.js package | library | Observed | Groups 1 file(s) under config.js package (observed from repository paths and static analysis). |
| containers package | library | Observed | Groups 12 file(s) under containers package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| helpers package | library | Observed | Groups 2 file(s) under helpers package (observed from repository paths and static analysis). |
| redux package | library | Observed | Groups 8 file(s) under redux package (observed from repository paths and static analysis). |
| routes.js package | library | Observed | Groups 1 file(s) under routes.js package (observed from repository paths and static analysis). |
| server.js package | library | Observed | Groups 1 file(s) under server.js package (observed from repository paths and static analysis). |
| theme package | library | Observed | Groups 4 file(s) under theme package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 1 file(s) under utils package (observed from repository paths and static analysis). |
| webpack package | library | Observed | Groups 4 file(s) under webpack package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.travis.yml` (ci)
- `app.json` (config)
- `circle.yml` (config)
- `package.json` (manifest)

## Top-level layout

- `src` — 53 analysed file(s)
- `api` — 16 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `docs` — 7 analysed file(s)
- `webpack` — 4 analysed file(s)
- `bin` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `076e24bcd9b363a9ce84f0ebbd0fe036f15561e2` is the revision these paths and observations refer to.
