# Project structure: insin/nwb

**Analysed commit:** `d95ab83f05d09c40dd2b7c65f4c6b15776c8526d`

**Commit reference:** [d95ab83f05d09c40dd2b7c65f4c6b15776c8526d](https://github.com/insin/nwb/commit/d95ab83f05d09c40dd2b7c65f4c6b15776c8526d)

**Tree at this commit:** [insin/nwb@d95ab83f05d0](https://github.com/insin/nwb/tree/d95ab83f05d09c40dd2b7c65f4c6b15776c8526d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | insin/nwb |
| Description | A toolkit for React, Preact, Inferno & vanilla JS apps, React libraries and other npm modules for the web, with no configuration (until you need it) |
| Stars | 5524 |
| Forks | 316 |
| Licence | Other |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `d95ab83f05d09c40dd2b7c65f4c6b15776c8526d` |
| Retrieved at | 2026-11-14T19:14:18.481575+00:00 |
| Files in this snapshot | 255 |

## Directory tree

```text
.github/  (3 files)
  CONTRIBUTING.md
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
.vscode/  (2 files)
  extensions.json
  settings.json
docs/  (17 files)
  guides/  (4 files)
    QuickDevelopment.md
    README.md
    ReactApps.md
    ReactComponents.md
  BrowserSupport.md
  Commands.md
  Configuration.md
  Examples.md
  FAQ.md
  Features.md
  ImplementingPlugins.md
  Middleware.md
  Plugins.md
  README.md
  Stylesheets.md
  Testing.md
  Versioning.md
flow-typed/  (7 files)
  npm/  (6 files)
    debug_v2.x.x.js
    expect_v1.x.x.js
    minimist_v1.x.x.js
    mocha_v3.1.x.js
    run-series_v1.x.x.js
    semver_v5.1.x.js
  libdefs.js
resources/  (1 files)
  config.dot
src/  (78 files)
  bin/  (1 files)
    nwb.js
  commands/  (39 files)
    build-demo.js
    build-inferno-app.js
    build-inferno.js
    build-preact-app.js
    build-preact.js
    build-react-app.js
    build-react-component.js
    build-react.js
    build-web-app.js
    build-web-module.js
    build-web.js
    build.js
    check-config.js
    clean-app.js
    clean-demo.js
    clean-module.js
    clean.js
    inferno.js
    init.js
    new.js
    preact.js
    react.js
    serve-inferno-app.js
    serve-inferno.js
    … 15 more files
  config/  (8 files)
    UserConfigReport.js
    babel.js
    index.js
    karma.js
    npm.js
    plugin.js
    user.js
    webpack.js
  inferno/  (3 files)
    index.js
    inferno-preset.js
    renderShim.js
  preact/  (3 files)
    index.js
    preact-preset.js
    renderShim.js
  react/  (2 files)
    index.js
    renderShim.js
  web/  (1 files)
    index.js
  WebpackStatusPlugin.js
  appCommands.js
  cli.js
  constants.js
  createBabelConfig.js
  createKarmaConfig.js
  createProject.js
  createServerWebpackConfig.js
  createWebpackConfig.js
  debug.js
  devServer.js
  errors.js
  expressMiddleware.js
  karmaServer.js
  moduleBuild.js
  quickCommands.js
  types.js
  utils.js
  webpackBuild.js
  webpackServer.js
  webpackUtils.js
templates/  (77 files)
  inferno-app/  (15 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (6 files)
      … 6 files under this directory
    tests/  (2 files)
      … 2 files under this directory
    CONTRIBUTING.md
    README.md
    _.gitignore
    _.travis.yml
    _package.json
    nwb.config.js
  preact-app/  (16 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (7 files)
      … 7 files under this directory
    tests/  (2 files)
      … 2 files under this directory
    CONTRIBUTING.md
    README.md
    _.gitignore
    _.travis.yml
    _package.json
    nwb.config.js
  react-app/  (15 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (6 files)
      … 6 files under this directory
    tests/  (2 files)
      … 2 files under this directory
    CONTRIBUTING.md
    README.md
    _.gitignore
    _.travis.yml
    _package.json
    nwb.config.js
  react-component/  (10 files)
    demo/  (1 files)
      … 1 files under this directory
    src/  (1 files)
      … 1 files under this directory
    tests/  (2 files)
      … 2 files under this directory
    CONTRIBUTING.md
    README.md
    _.gitignore
    _.travis.yml
    _package.json
    nwb.config.js
  web-app/  (11 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (2 files)
      … 2 files under this directory
    tests/  (2 files)
      … 2 files under this directory
    CONTRIBUTING.md
    README.md
    _.gitignore
    _.travis.yml
    _package.json
    nwb.config.js
  web-module/  (9 files)
    src/  (1 files)
      … 1 files under this directory
    tests/  (2 files)
      … 2 files under this directory
    CONTRIBUTING.md
    README.md
    _.gitignore
    _.travis.yml
    _package.json
    nwb.config.js
  webpack-template.html
tests/  (55 files)
  commands/  (5 files)
    build-test.js
    new-init-test.js
    projects-test.js
    serve-test.js
    test-test.js
  fixtures/  (43 files)
    plugins/  (1 files)
      … 1 files under this directory
    projects/  (39 files)
      … 39 files under this directory
    bad-config.js
    invalid-config.js
    worst-config.js
  .eslintrc
  config-test.js
  createBabelConfig-test.js
  createKarmaConfig-test.js
  createProject-test.js
  createWebpackConfig-test.js
  utils-test.js
.editorconfig
.eslintignore
.flowconfig
.gitattributes
.gitignore
.travis.yml
CHANGES.md
CHANGES.old.md
LICENSE
README.md
TODO
appveyor.yml
express.js
package-changelog.js
package.json
```

## Entry points

- [src/config/index.js](https://github.com/insin/nwb/blob/d95ab83f05d09c40dd2b7c65f4c6b15776c8526d/src/config/index.js)
- [src/inferno/index.js](https://github.com/insin/nwb/blob/d95ab83f05d09c40dd2b7c65f4c6b15776c8526d/src/inferno/index.js)
- [src/preact/index.js](https://github.com/insin/nwb/blob/d95ab83f05d09c40dd2b7c65f4c6b15776c8526d/src/preact/index.js)
- [src/react/index.js](https://github.com/insin/nwb/blob/d95ab83f05d09c40dd2b7c65f4c6b15776c8526d/src/react/index.js)
- [src/web/index.js](https://github.com/insin/nwb/blob/d95ab83f05d09c40dd2b7c65f4c6b15776c8526d/src/web/index.js)
- [templates/inferno-app/src/App.js](https://github.com/insin/nwb/blob/d95ab83f05d09c40dd2b7c65f4c6b15776c8526d/templates/inferno-app/src/App.js)
- [templates/inferno-app/src/index.js](https://github.com/insin/nwb/blob/d95ab83f05d09c40dd2b7c65f4c6b15776c8526d/templates/inferno-app/src/index.js)
- [templates/preact-app/src/App.js](https://github.com/insin/nwb/blob/d95ab83f05d09c40dd2b7c65f4c6b15776c8526d/templates/preact-app/src/App.js)
- [templates/preact-app/src/index.js](https://github.com/insin/nwb/blob/d95ab83f05d09c40dd2b7c65f4c6b15776c8526d/templates/preact-app/src/index.js)
- [templates/react-app/src/App.js](https://github.com/insin/nwb/blob/d95ab83f05d09c40dd2b7c65f4c6b15776c8526d/templates/react-app/src/App.js)
- [templates/react-app/src/index.js](https://github.com/insin/nwb/blob/d95ab83f05d09c40dd2b7c65f4c6b15776c8526d/templates/react-app/src/index.js)
- [templates/react-component/src/index.js](https://github.com/insin/nwb/blob/d95ab83f05d09c40dd2b7c65f4c6b15776c8526d/templates/react-component/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| appCommands.js package | library | Observed | Groups 1 file(s) under appcommands.js package (observed from repository paths and static analysis). |
| bin package | library | Observed | Groups 1 file(s) under bin package (observed from repository paths and static analysis). |
| cli.js package | library | Observed | Groups 1 file(s) under cli.js package (observed from repository paths and static analysis). |
| commands package | library | Observed | Groups 39 file(s) under commands package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 22 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| constants.js package | library | Observed | Groups 1 file(s) under constants.js package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| createBabelConfig.js package | library | Observed | Groups 1 file(s) under createbabelconfig.js package (observed from repository paths and static analysis). |
| createKarmaConfig.js package | library | Observed | Groups 1 file(s) under createkarmaconfig.js package (observed from repository paths and static analysis). |
| createProject.js package | library | Observed | Groups 1 file(s) under createproject.js package (observed from repository paths and static analysis). |
| createServerWebpackConfig.js package | library | Observed | Groups 1 file(s) under createserverwebpackconfig.js package (observed from repository paths and static analysis). |
| createWebpackConfig.js package | library | Observed | Groups 1 file(s) under createwebpackconfig.js package (observed from repository paths and static analysis). |
| debug.js package | library | Observed | Groups 1 file(s) under debug.js package (observed from repository paths and static analysis). |
| devServer.js package | library | Observed | Groups 1 file(s) under devserver.js package (observed from repository paths and static analysis). |
| errors.js package | library | Observed | Groups 1 file(s) under errors.js package (observed from repository paths and static analysis). |
| expressMiddleware.js package | library | Observed | Groups 1 file(s) under expressmiddleware.js package (observed from repository paths and static analysis). |
| flow-typed package | library | Observed | Groups 7 file(s) under flow-typed package (observed from repository paths and static analysis). |
| inferno package | library | Observed | Groups 3 file(s) under inferno package (observed from repository paths and static analysis). |
| karmaServer.js package | library | Observed | Groups 1 file(s) under karmaserver.js package (observed from repository paths and static analysis). |
| moduleBuild.js package | library | Observed | Groups 1 file(s) under modulebuild.js package (observed from repository paths and static analysis). |
| preact package | library | Observed | Groups 3 file(s) under preact package (observed from repository paths and static analysis). |
| quickCommands.js package | library | Observed | Groups 1 file(s) under quickcommands.js package (observed from repository paths and static analysis). |
| react package | library | Observed | Groups 2 file(s) under react package (observed from repository paths and static analysis). |
| templates package | library | Observed | Groups 16 file(s) under templates package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 67 file(s) under tests (observed from repository paths and static analysis). |
| types.js package | library | Observed | Groups 1 file(s) under types.js package (observed from repository paths and static analysis). |
| utils.js package | library | Observed | Groups 1 file(s) under utils.js package (observed from repository paths and static analysis). |
| web package | library | Observed | Groups 1 file(s) under web package (observed from repository paths and static analysis). |
| webpackBuild.js package | library | Observed | Groups 1 file(s) under webpackbuild.js package (observed from repository paths and static analysis). |
| webpackServer.js package | library | Observed | Groups 1 file(s) under webpackserver.js package (observed from repository paths and static analysis). |
| WebpackStatusPlugin.js package | library | Observed | Groups 1 file(s) under webpackstatusplugin.js package (observed from repository paths and static analysis). |
| webpackUtils.js package | library | Observed | Groups 1 file(s) under webpackutils.js package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.travis.yml` (ci)
- `.vscode/extensions.json` (config)
- `.vscode/settings.json` (config)
- `appveyor.yml` (config)
- `package.json` (manifest)
- `templates/inferno-app/_.travis.yml` (config)
- `templates/inferno-app/_package.json` (config)
- `templates/preact-app/_.travis.yml` (config)
- `templates/preact-app/_package.json` (config)
- `templates/react-app/_.travis.yml` (config)
- `templates/react-app/_package.json` (config)
- `templates/react-component/_.travis.yml` (config)
- `templates/react-component/_package.json` (config)
- `templates/web-app/_.travis.yml` (config)
- `templates/web-app/_package.json` (config)
- `templates/web-module/_.travis.yml` (config)
- `templates/web-module/_package.json` (config)

## Top-level layout

- `src` — 78 analysed file(s)
- `templates` — 77 analysed file(s)
- `tests` — 55 analysed file(s)
- `docs` — 17 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `flow-typed` — 7 analysed file(s)
- `.github` — 3 analysed file(s)
- `.vscode` — 2 analysed file(s)
- `resources` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 3 file(s) were skipped during inventory (1 x likely secret file excluded; 2 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `d95ab83f05d09c40dd2b7c65f4c6b15776c8526d` is the revision these paths and observations refer to.
