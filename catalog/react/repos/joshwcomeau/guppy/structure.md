# Project structure: joshwcomeau/guppy

**Analysed commit:** `72d84495d9c15d22053b0010ac1fd9a1061a7054`

**Commit reference:** [72d84495d9c15d22053b0010ac1fd9a1061a7054](https://github.com/joshwcomeau/guppy/commit/72d84495d9c15d22053b0010ac1fd9a1061a7054)

**Tree at this commit:** [joshwcomeau/guppy@72d84495d9c1](https://github.com/joshwcomeau/guppy/tree/72d84495d9c15d22053b0010ac1fd9a1061a7054)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | joshwcomeau/guppy |
| Description | 🐠A friendly application manager and task runner for React.js |
| Stars | 3237 |
| Forks | 150 |
| Licence | ISC |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `72d84495d9c15d22053b0010ac1fd9a1061a7054` |
| Retrieved at | 2026-11-14T19:15:27.652861+00:00 |
| Files in this snapshot | 411 |

## Directory tree

```text
.circleci/  (1 files)
  config.yml
.github/  (3 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  PULL_REQUEST_TEMPLATE.md
.storybook/  (8 files)
  components/  (4 files)
    Showcase/  (2 files)
      … 2 files under this directory
    Wrapper/  (2 files)
      … 2 files under this directory
  .babelrc
  config.js
  manager-head.html
  webpack-config.js
.vscode/  (3 files)
  extensions.json
  launch.json
  settings.json
config/  (14 files)
  jest/  (5 files)
    babelTransform.js
    cssTransform.js
    electron.js
    fileTransform.js
    graphqlTransform.js
  .eslintrc.js
  env.js
  enzyme-setup.js
  paths.js
  polyfills.js
  testFrameworkSetup.js
  webpack.config.dev.js
  webpack.config.prod.js
  webpackDevServer.config.js
docs/  (6 files)
  dev-info/  (3 files)
    misc/  (1 files)
      … 1 files under this directory
    code-structure.md
    style-guide.md
  adding-a-project.md
  getting-started.md
  understanding-package.json.md
public/  (2 files)
  guppy-logo.svg
  index.html
scripts/  (4 files)
  .eslintrc.js
  build.js
  start.js
  test.js
src/  (359 files)
  __mocks__/  (5 files)
    electron-log.js
    electron-store.js
    electron-updater.js
    electron.js
    mixpanel-browser.js
  actions/  (2 files)
    index.js
    types.js
  assets/  (2 files)
    images/  (2 files)
      … 2 files under this directory
  components/  (272 files)
    App/  (2 files)
      … 2 files under this directory
    AppSettingsModal/  (4 files)
      … 4 files under this directory
    ApplicationMenu/  (2 files)
      … 2 files under this directory
    AvailableWidth/  (2 files)
      … 2 files under this directory
    BigClickableButton/  (4 files)
      … 4 files under this directory
    Button/  (13 files)
      … 13 files under this directory
    ButtonWithIcon/  (5 files)
      … 5 files under this directory
    Card/  (2 files)
      … 2 files under this directory
    CircularOutline/  (3 files)
      … 3 files under this directory
    CodesandboxLogo/  (2 files)
      … 2 files under this directory
    CreateNewProjectWizard/  (34 files)
      … 34 files under this directory
    CustomHighlight/  (2 files)
      … 2 files under this directory
    Debounced/  (2 files)
      … 2 files under this directory
    DependencyManagementPane/  (30 files)
      … 30 files under this directory
    DetectActive/  (2 files)
      … 2 files under this directory
    DevTools/  (3 files)
      … 3 files under this directory
    DevelopmentServerPane/  (4 files)
      … 4 files under this directory
    DevelopmentServerStatus/  (2 files)
      … 2 files under this directory
    DirectoryPicker/  (2 files)
      … 2 files under this directory
    Divider/  (2 files)
      … 2 files under this directory
    Earth/  (2 files)
      … 2 files under this directory
    EjectButton/  (4 files)
      … 4 files under this directory
    ExternalLink/  (2 files)
      … 2 files under this directory
    FadeIn/  (2 files)
      … 2 files under this directory
    FadeOnChange/  (2 files)
      … 2 files under this directory
    FeedbackButton/  (2 files)
      … 2 files under this directory
    FormField/  (2 files)
      … 2 files under this directory
    FullWidth/  (2 files)
      … 2 files under this directory
    Heading/  (2 files)
      … 2 files under this directory
    HelpButton/  (2 files)
      … 2 files under this directory
    HoverableOutlineButton/  (2 files)
      … 2 files under this directory
    Icons/  (1 files)
      … 1 files under this directory
    ImportProjectButton/  (2 files)
      … 2 files under this directory
    Initialization/  (3 files)
      … 3 files under this directory
    IntroScreen/  (2 files)
      … 2 files under this directory
    Label/  (2 files)
      … 2 files under this directory
    LargeLED/  (3 files)
      … 3 files under this directory
    License/  (2 files)
      … 2 files under this directory
    LoadingScreen/  (2 files)
      … 2 files under this directory
    Logo/  (3 files)
      … 3 files under this directory
    MainContentWrapper/  (2 files)
      … 2 files under this directory
    Middot/  (2 files)
      … 2 files under this directory
    Modal/  (2 files)
      … 2 files under this directory
    ModalHeader/  (2 files)
      … 2 files under this directory
    Module/  (2 files)
      … 2 files under this directory
    MountAfter/  (3 files)
      … 3 files under this directory
    NodeProvider/  (2 files)
      … 2 files under this directory
    OnlineChecker/  (2 files)
      … 2 files under this directory
    OnlyOn/  (2 files)
      … 2 files under this directory
    Paragraph/  (2 files)
      … 2 files under this directory
    PixelShifter/  (2 files)
      … 2 files under this directory
    Planet/  (9 files)
      … 9 files under this directory
    ProgressBar/  (5 files)
      … 5 files under this directory
    ProjectConfigurationModal/  (4 files)
      … 4 files under this directory
    ProjectIconSelection/  (3 files)
      … 3 files under this directory
    ProjectPage/  (4 files)
      … 4 files under this directory
    ProjectTitle/  (3 files)
      … 3 files under this directory
    ProjectTypeSelection/  (2 files)
      … 2 files under this directory
    ScrollDisabler/  (2 files)
      … 2 files under this directory
    SelectableImage/  (2 files)
      … 2 files under this directory
    SelectableItem/  (2 files)
      … 2 files under this directory
    SettingsButton/  (2 files)
      … 2 files under this directory
    Sidebar/  (7 files)
      … 7 files under this directory
    Spacer/  (2 files)
      … 2 files under this directory
    Spinner/  (2 files)
      … 2 files under this directory
    TaskDetailsModal/  (2 files)
      … 2 files under this directory
    TaskRunnerPane/  (3 files)
      … 3 files under this directory
    TaskRunnerPaneRow/  (2 files)
      … 2 files under this directory
    TerminalOutput/  (4 files)
      … 4 files under this directory
    TextButton/  (2 files)
      … 2 files under this directory
    TextInput/  (2 files)
      … 2 files under this directory
    TextInputWithButton/  (2 files)
      … 2 files under this directory
    Titlebar/  (2 files)
      … 2 files under this directory
    Toggle/  (3 files)
      … 3 files under this directory
    TwoPaneModal/  (2 files)
      … 2 files under this directory
    WhimsicalInstaller/  (8 files)
      … 8 files under this directory
    WindowDimensions/  (2 files)
      … 2 files under this directory
  config/  (2 files)
    app.js
    project-types.js
  reducers/  (20 files)
    __snapshots__/  (1 files)
      … 1 files under this directory
    app-loaded.reducer.js
    app-settings.reducer.js
    app-settings.reducer.test.js
    app-status.reducer.js
    app-status.reducer.test.js
    dependencies.reducer.js
    dependencies.reducer.test.js
    index.js
    modal.reducer.js
    modal.reducer.test.js
    onboarding-status.reducer.js
    paths.reducer.js
    paths.reducer.test.js
    projects.reducer.js
    projects.reducer.test.js
    queue.reducer.js
    queue.reducer.test.js
    tasks.reducer.js
    tasks.reducer.test.js
  sagas/  (19 files)
    analytics.saga.js
    analytics.saga.test.js
    delete-project.saga.js
    delete-project.saga.test.js
    dependency.saga.js
    dependency.saga.test.js
    development.saga.js
    development.saga.test.js
    import-project.saga.js
    import-project.saga.test.js
    index.js
    queue.saga.js
    queue.saga.test.js
    refresh-projects.saga.js
    refresh-projects.saga.test.js
    save-project-settings.saga.js
    save-project-settings.saga.test.js
    task.saga.js
    task.saga.test.js
  services/  (22 files)
    analytics.service.js
    analytics.service.test.js
    check-if-url-exists.service.js
    config-variables.service.js
    config-variables.service.test.js
    create-project.fixtures.js
    create-project.service.js
    create-project.service.test.js
    dependencies.service.js
    electron-store.service.js
    find-available-port.service.js
    kill-process-id.service.js
    kill-process-id.service.test.js
    platform.service.js
    platform.service.test.js
    process-logger.service.js
    project-name-service.test.js
    project-name.service.js
    project-type-specifics.js
    project-type-specifics.test.js
    read-from-disk.service.js
    shell.service.js
  store/  (4 files)
    index.js
    migrations.js
    migrations.test.js
    storage-engine.js
  stories/  (1 files)
    colors.stories.js
  test-helpers/  (1 files)
    factories.js
  base.css
  constants.js
  electron.js
  electron.test.js
  fonts.css
  global-styles.js
  index.js
  types.js
  utils.js
.eslintrc.js
.flowconfig
.gitignore
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE.md
PRIVACY.md
README.md
codecov.yml
package.json
prettier.config.js
```

## Entry points

- [src/electron.js](https://github.com/joshwcomeau/guppy/blob/72d84495d9c15d22053b0010ac1fd9a1061a7054/src/electron.js)
- [.storybook/components/Showcase/index.js](https://github.com/joshwcomeau/guppy/blob/72d84495d9c15d22053b0010ac1fd9a1061a7054/.storybook/components/Showcase/index.js)
- [.storybook/components/Wrapper/index.js](https://github.com/joshwcomeau/guppy/blob/72d84495d9c15d22053b0010ac1fd9a1061a7054/.storybook/components/Wrapper/index.js)
- [src/actions/index.js](https://github.com/joshwcomeau/guppy/blob/72d84495d9c15d22053b0010ac1fd9a1061a7054/src/actions/index.js)
- [src/components/App/App.js](https://github.com/joshwcomeau/guppy/blob/72d84495d9c15d22053b0010ac1fd9a1061a7054/src/components/App/App.js)
- [src/components/App/index.js](https://github.com/joshwcomeau/guppy/blob/72d84495d9c15d22053b0010ac1fd9a1061a7054/src/components/App/index.js)
- [src/components/AppSettingsModal/index.js](https://github.com/joshwcomeau/guppy/blob/72d84495d9c15d22053b0010ac1fd9a1061a7054/src/components/AppSettingsModal/index.js)
- [src/components/ApplicationMenu/index.js](https://github.com/joshwcomeau/guppy/blob/72d84495d9c15d22053b0010ac1fd9a1061a7054/src/components/ApplicationMenu/index.js)
- [src/components/AvailableWidth/index.js](https://github.com/joshwcomeau/guppy/blob/72d84495d9c15d22053b0010ac1fd9a1061a7054/src/components/AvailableWidth/index.js)
- [src/components/BigClickableButton/index.js](https://github.com/joshwcomeau/guppy/blob/72d84495d9c15d22053b0010ac1fd9a1061a7054/src/components/BigClickableButton/index.js)
- [src/components/Button/index.js](https://github.com/joshwcomeau/guppy/blob/72d84495d9c15d22053b0010ac1fd9a1061a7054/src/components/Button/index.js)
- [src/components/ButtonWithIcon/index.js](https://github.com/joshwcomeau/guppy/blob/72d84495d9c15d22053b0010ac1fd9a1061a7054/src/components/ButtonWithIcon/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| actions package | library | Observed | Groups 2 file(s) under actions package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 247 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 18 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| constants.js package | library | Observed | Groups 1 file(s) under constants.js package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| electron.js package | library | Observed | Groups 1 file(s) under electron.js package (observed from repository paths and static analysis). |
| electron.test.js package | library | Observed | Groups 1 file(s) under electron.test.js package (observed from repository paths and static analysis). |
| global-styles.js package | library | Observed | Groups 1 file(s) under global-styles.js package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| __mocks__ package | library | Observed | Groups 5 file(s) under __mocks__ package (observed from repository paths and static analysis). |
| reducers package | library | Observed | Groups 19 file(s) under reducers package (observed from repository paths and static analysis). |
| sagas package | library | Observed | Groups 19 file(s) under sagas package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 4 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 22 file(s) under service / domain layer (observed from repository paths and static analysis). |
| store package | library | Observed | Groups 4 file(s) under store package (observed from repository paths and static analysis). |
| stories package | library | Observed | Groups 1 file(s) under stories package (observed from repository paths and static analysis). |
| test-helpers package | library | Observed | Groups 1 file(s) under test-helpers package (observed from repository paths and static analysis). |
| types.js package | library | Observed | Groups 1 file(s) under types.js package (observed from repository paths and static analysis). |
| utils.js package | library | Observed | Groups 1 file(s) under utils.js package (observed from repository paths and static analysis). |

## Important files

- `.circleci/config.yml` (ci)
- `.vscode/extensions.json` (config)
- `.vscode/launch.json` (config)
- `.vscode/settings.json` (config)
- `codecov.yml` (config)
- `package.json` (manifest)

## Top-level layout

- `src` — 359 analysed file(s)
- `config` — 14 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `.storybook` — 8 analysed file(s)
- `docs` — 6 analysed file(s)
- `scripts` — 4 analysed file(s)
- `.github` — 3 analysed file(s)
- `.vscode` — 3 analysed file(s)
- `public` — 2 analysed file(s)
- `.circleci` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `72d84495d9c15d22053b0010ac1fd9a1061a7054` is the revision these paths and observations refer to.
