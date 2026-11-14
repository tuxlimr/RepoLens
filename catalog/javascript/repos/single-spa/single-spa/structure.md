# Project structure: single-spa/single-spa

**Analysed commit:** `297483c11265050542d7ef107d14c44936c51883`

**Commit reference:** [297483c11265050542d7ef107d14c44936c51883](https://github.com/single-spa/single-spa/commit/297483c11265050542d7ef107d14c44936c51883)

**Tree at this commit:** [single-spa/single-spa@297483c11265](https://github.com/single-spa/single-spa/tree/297483c11265050542d7ef107d14c44936c51883)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | single-spa/single-spa |
| Description | The router for easy microfrontends |
| Stars | 13882 |
| Forks | 919 |
| Licence | Other |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `297483c11265050542d7ef107d14c44936c51883` |
| Retrieved at | 2026-11-14T19:11:49.091544+00:00 |
| Files in this snapshot | 153 |

## Directory tree

```text
.changeset/  (4 files)
  README.md
  clean-bags-jog.md
  config.json
  violet-jokes-add.md
.github/  (4 files)
  ISSUE_TEMPLATE/  (2 files)
    bugs-or-questions.md
    config.yml
  workflows/  (1 files)
    build-and-test.yml
  FUNDING.yml
.husky/  (1 files)
  pre-commit
docs/  (10 files)
  README.md
  applications.md
  migrating-existing-spas.md
  parcel-api.md
  parcels.md
  root-application.md
  separating-applications.md
  single-spa-api.md
  single-spa-config.md
  single-spa-ecosystem.md
examples/  (1 files)
  README.md
node-spec/  (1 files)
  nodejs.spec.js
scripts/  (1 files)
  copy-types.js
spec/  (89 files)
  apis/  (18 files)
    app-names.spec.js
    check-activity-functions.spec.js
    delayed-start-popstate.spec.js
    error-handlers.spec.js
    event-listeners.spec.js
    first-mount.spec.js
    multiple-instances.spec.js
    navigate-before-patch-history.spec.js
    navigate-to-url.spec.js
    patch-history-api.spec.js
    path-to-active-when.spec.js
    register-application.spec.js
    single-spa-events-api.spec.js
    start-api.spec.js
    timeout-apis.spec.js
    unregister-application.spec.js
    url-reroute-only-default.spec.js
    url-reroute-only-false.spec.js
  apps/  (67 files)
    bootstrap-rejects/  (2 files)
      … 2 files under this directory
    bootstrap-times-out/  (2 files)
      … 2 files under this directory
    bootstrap-times-out-dies/  (2 files)
      … 2 files under this directory
    delayed-start/  (2 files)
      … 2 files under this directory
    empty-array-lifecycles/  (2 files)
      … 2 files under this directory
    happy-active-when/  (2 files)
      … 2 files under this directory
    happy-basic/  (2 files)
      … 2 files under this directory
    happy-register-object/  (2 files)
      … 2 files under this directory
    happy-unload/  (2 files)
      … 2 files under this directory
    invalid-bootstrap/  (2 files)
      … 2 files under this directory
    invalid-load-function/  (1 files)
      … 1 files under this directory
    invalid-mount/  (2 files)
      … 2 files under this directory
    invalid-no-mount/  (2 files)
      … 2 files under this directory
    invalid-no-unmount/  (2 files)
      … 2 files under this directory
    invalid-unload/  (2 files)
      … 2 files under this directory
    invalid-unmount/  (2 files)
      … 2 files under this directory
    lifecycle-props/  (2 files)
      … 2 files under this directory
    lifecycle-props-function/  (2 files)
      … 2 files under this directory
    load-error/  (1 files)
      … 1 files under this directory
    mount-before-other-loads/  (1 files)
      … 1 files under this directory
    mount-fails/  (2 files)
      … 2 files under this directory
    mount-rejects/  (2 files)
      … 2 files under this directory
    mount-times-out/  (2 files)
      … 2 files under this directory
    mount-times-out-dies/  (2 files)
      … 2 files under this directory
    mounting-status/  (2 files)
      … 2 files under this directory
    multiple-lifecycle-functions/  (2 files)
      … 2 files under this directory
    no-bootstrap/  (2 files)
      … 2 files under this directory
    no-object-prototype/  (1 files)
      … 1 files under this directory
    partial-rerouting/  (1 files)
      … 1 files under this directory
    profiler-basic/  (3 files)
      … 3 files under this directory
    register-with-object/  (1 files)
      … 1 files under this directory
    returns-non-native-promise/  (2 files)
      … 2 files under this directory
    unmount-rejects/  (2 files)
      … 2 files under this directory
    unmount-times-out/  (2 files)
      … 2 files under this directory
    unmount-times-out-dies/  (2 files)
      … 2 files under this directory
    warning-timeouts/  (2 files)
      … 2 files under this directory
  parcels/  (4 files)
    app-mounts-parcel.spec.js
    mount-root-parcel.spec.js
    parcel-error-handlers.spec.js
    parcel-mounts-parcel.spec.js
src/  (25 files)
  applications/  (4 files)
    app-errors.js
    app.helpers.js
    apps.js
    timeouts.js
  devtools/  (3 files)
    devtools.js
    profiler-api.js
    profiler.js
  lifecycles/  (8 files)
    bootstrap.js
    lifecycle.helpers.js
    load.js
    mount.js
    prop.helpers.js
    unload.js
    unmount.js
    update.js
  navigation/  (2 files)
    navigation-events.js
    reroute.js
  parcels/  (1 files)
    mount-parcel.js
  utils/  (3 files)
    assign.js
    find.js
    runtime-environment.js
  jquery-support.js
  single-spa.js
  single-spa.profile.js
  start.js
typings/  (2 files)
  single-spa.d.ts
  single-spa.test-d.ts
.babelrc
.eslintrc
.gitignore
.npmignore
.prettierignore
.prettierrc.json
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
jest-browser.config.js
jest-node.config.js
package.json
rollup.config.js
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| applications package | library | Observed | Groups 4 file(s) under applications package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| devtools package | library | Observed | Groups 3 file(s) under devtools package (observed from repository paths and static analysis). |
| jquery-support.js package | library | Observed | Groups 1 file(s) under jquery-support.js package (observed from repository paths and static analysis). |
| lifecycles package | library | Observed | Groups 8 file(s) under lifecycles package (observed from repository paths and static analysis). |
| navigation package | library | Observed | Groups 2 file(s) under navigation package (observed from repository paths and static analysis). |
| node-spec package | library | Observed | Groups 1 file(s) under node-spec package (observed from repository paths and static analysis). |
| parcels package | library | Observed | Groups 1 file(s) under parcels package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| single-spa.js package | library | Observed | Groups 1 file(s) under single-spa.js package (observed from repository paths and static analysis). |
| single-spa.profile.js package | library | Observed | Groups 1 file(s) under single-spa.profile.js package (observed from repository paths and static analysis). |
| spec package | library | Observed | Groups 89 file(s) under spec package (observed from repository paths and static analysis). |
| start.js package | library | Observed | Groups 1 file(s) under start.js package (observed from repository paths and static analysis). |
| typings package | library | Observed | Groups 2 file(s) under typings package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 3 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/build-and-test.yml` (ci)
- `.prettierrc.json` (config)
- `package.json` (manifest)

## Top-level layout

- `spec` — 89 analysed file(s)
- `src` — 25 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `docs` — 10 analysed file(s)
- `.changeset` — 4 analysed file(s)
- `.github` — 4 analysed file(s)
- `typings` — 2 analysed file(s)
- `.husky` — 1 analysed file(s)
- `examples` — 1 analysed file(s)
- `node-spec` — 1 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `297483c11265050542d7ef107d14c44936c51883` is the revision these paths and observations refer to.
