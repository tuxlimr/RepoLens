# Project structure: docker-archive-public/docker.kitematic

**Analysed commit:** `445bfbae698ce977784c712756d6dc57c3fe6cbf`

**Commit reference:** [445bfbae698ce977784c712756d6dc57c3fe6cbf](https://github.com/docker-archive-public/docker.kitematic/commit/445bfbae698ce977784c712756d6dc57c3fe6cbf)

**Tree at this commit:** [docker-archive-public/docker.kitematic@445bfbae698c](https://github.com/docker-archive-public/docker.kitematic/tree/445bfbae698ce977784c712756d6dc57c3fe6cbf)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | docker-archive-public/docker.kitematic |
| Description | Visual Docker Container Management on Mac & Windows |
| Stars | 12116 |
| Forks | 1369 |
| Licence | Apache-2.0 |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `445bfbae698ce977784c712756d6dc57c3fe6cbf` |
| Retrieved at | 2026-11-14T19:12:10.377117+00:00 |
| Files in this snapshot | 194 |

## Directory tree

```text
.circleci/  (1 files)
  config.yml
.github/  (1 files)
  ISSUE_TEMPLATE.md
__integration__/  (2 files)
  HubUtil-integration.js
  RegHubUtil-integration.js
__mocks__/  (3 files)
  app.js
  electron.js
  remote.js
__tests__/  (1 files)
  Util-test.js
docs/  (1 files)
  README.md
fonts/  (1 files)
  kitematic.svg
resources/  (3 files)
  MSYS_LICENSE
  OPENSSH_LICENSE
  terminal
src/  (66 files)
  actions/  (13 files)
    AccountActions.js
    AccountServerActions.js
    ContainerActions.js
    ContainerServerActions.js
    ImageActions.js
    ImageServerActions.js
    NetworkActions.js
    RepositoryActions.js
    RepositoryServerActions.js
    SetupActions.js
    SetupServerActions.js
    TagActions.js
    TagServerActions.js
  components/  (28 files)
    About.react.js
    Account.react.js
    AccountLogin.react.js
    AccountSignup.react.js
    ContainerDetails.react.js
    ContainerDetailsHeader.react.js
    ContainerDetailsSubheader.react.js
    ContainerHome.react.js
    ContainerHomeFolders.react.js
    ContainerHomeIpPortsPreview.react.js
    ContainerHomeLogs.react.js
    ContainerList.react.js
    ContainerListItem.react.js
    ContainerProgress.react.js
    ContainerSettings.react.js
    ContainerSettingsAdvanced.react.js
    ContainerSettingsGeneral.react.js
    ContainerSettingsNetwork.react.js
    ContainerSettingsPorts.react.js
    ContainerSettingsVolumes.react.js
    Containers.react.js
    Header.react.js
    ImageCard.react.js
    Loading.react.js
    … 4 more files
  stores/  (7 files)
    AccountStore.js
    ContainerStore.js
    ImageStore.js
    NetworkStore.js
    RepositoryStore.js
    SetupStore.js
    TagStore.js
  utils/  (10 files)
    ContainerUtil.js
    DockerMachineUtil.js
    DockerUtil.js
    HubUtil.js
    MetricsUtil.js
    RegHubUtil.js
    SetupUtil.js
    Util.js
    VirtualBoxUtil.js
    WebUtil.js
  alt.js
  app.js
  browser.js
  main.js
  main.ts
  menutemplate.js
  router.js
  routes.js
styles/  (91 files)
  bootstrap/  (70 files)
    mixins/  (29 files)
      … 29 files under this directory
    alerts.less
    badges.less
    bootstrap.less
    breadcrumbs.less
    button-groups.less
    buttons.less
    carousel.less
    close.less
    code.less
    component-animations.less
    dropdowns.less
    forms.less
    glyphicons.less
    grid.less
    input-groups.less
    jumbotron.less
    labels.less
    list-group.less
    media.less
    mixins.less
    modals.less
    navbar.less
    navs.less
    normalize.less
    … 17 more files
  animation.less
  container-home.less
  container-logs.less
  container-progress.less
  container-settings.less
  header.less
  icons.less
  layout.less
  left-panel.less
  loading.less
  main.less
  mixins.less
  new-container.less
  preferences.less
  radial.less
  retina.less
  right-panel.less
  setup.less
  spinner.less
  theme.less
  variables.less
util/  (6 files)
  Info.plist
  VirtualBox_Uninstall.tool
  prepare.js
  reset
  reset.ps1
  testenv.js
.babelrc
.eslintrc
.gitignore
.travis.yml
CONTRIBUTING.md
Gruntfile.js
LICENSE
MAINTAINERS
Makefile
README.md
ROADMAP.md
electron-builder.json
index.html
jest-integration.json
jest-unit.json
package.json
tsconfig.json
tslint.json
```

## Entry points

- [__mocks__/app.js](https://github.com/docker-archive-public/docker.kitematic/blob/445bfbae698ce977784c712756d6dc57c3fe6cbf/__mocks__/app.js)
- [src/app.js](https://github.com/docker-archive-public/docker.kitematic/blob/445bfbae698ce977784c712756d6dc57c3fe6cbf/src/app.js)
- [src/main.js](https://github.com/docker-archive-public/docker.kitematic/blob/445bfbae698ce977784c712756d6dc57c3fe6cbf/src/main.js)
- [src/main.ts](https://github.com/docker-archive-public/docker.kitematic/blob/445bfbae698ce977784c712756d6dc57c3fe6cbf/src/main.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| actions package | library | Observed | Groups 13 file(s) under actions package (observed from repository paths and static analysis). |
| alt.js package | library | Observed | Groups 1 file(s) under alt.js package (observed from repository paths and static analysis). |
| app.js package | library | Observed | Groups 1 file(s) under app.js package (observed from repository paths and static analysis). |
| browser.js package | library | Observed | Groups 1 file(s) under browser.js package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 28 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| __integration__ package | library | Observed | Groups 2 file(s) under __integration__ package (observed from repository paths and static analysis). |
| main.js package | library | Observed | Groups 1 file(s) under main.js package (observed from repository paths and static analysis). |
| main.ts package | library | Observed | Groups 1 file(s) under main.ts package (observed from repository paths and static analysis). |
| menutemplate.js package | library | Observed | Groups 1 file(s) under menutemplate.js package (observed from repository paths and static analysis). |
| __mocks__ package | library | Observed | Groups 3 file(s) under __mocks__ package (observed from repository paths and static analysis). |
| router.js package | library | Observed | Groups 1 file(s) under router.js package (observed from repository paths and static analysis). |
| routes.js package | library | Observed | Groups 1 file(s) under routes.js package (observed from repository paths and static analysis). |
| stores package | library | Observed | Groups 7 file(s) under stores package (observed from repository paths and static analysis). |
| __tests__ package | library | Observed | Groups 1 file(s) under __tests__ package (observed from repository paths and static analysis). |
| util package | library | Observed | Groups 2 file(s) under util package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 10 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.circleci/config.yml` (ci)
- `.travis.yml` (ci)
- `electron-builder.json` (config)
- `jest-integration.json` (config)
- `jest-unit.json` (config)
- `package.json` (manifest)
- `tsconfig.json` (config)
- `tslint.json` (config)

## Top-level layout

- `styles` — 91 analysed file(s)
- `src` — 66 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `util` — 6 analysed file(s)
- `__mocks__` — 3 analysed file(s)
- `resources` — 3 analysed file(s)
- `__integration__` — 2 analysed file(s)
- `.circleci` — 1 analysed file(s)
- `.github` — 1 analysed file(s)
- `__tests__` — 1 analysed file(s)
- `docs` — 1 analysed file(s)
- `fonts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `445bfbae698ce977784c712756d6dc57c3fe6cbf` is the revision these paths and observations refer to.
