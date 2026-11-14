# Project structure: MithrilJS/mithril.js

**Analysed commit:** `092989a259f2eba05b406a024cca89bd97417f92`

**Commit reference:** [092989a259f2eba05b406a024cca89bd97417f92](https://github.com/MithrilJS/mithril.js/commit/092989a259f2eba05b406a024cca89bd97417f92)

**Tree at this commit:** [MithrilJS/mithril.js@092989a259f2](https://github.com/MithrilJS/mithril.js/tree/092989a259f2eba05b406a024cca89bd97417f92)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | MithrilJS/mithril.js |
| Description | A JavaScript Framework for Building Brilliant Applications |
| Stars | 14516 |
| Forks | 923 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `092989a259f2eba05b406a024cca89bd97417f92` |
| Retrieved at | 2026-11-14T19:11:44.970636+00:00 |
| Files in this snapshot | 137 |

## Directory tree

```text
.github/  (13 files)
  ISSUE_TEMPLATE/  (3 files)
    1-core.yml
    2-stream.yml
    config.yml
  workflows/  (7 files)
    issue-create.yml
    notify-release.yml
    pr-create-release.yml
    publish-prerelease.yml
    push-release.yml
    rollback.yml
    test.yml
  CODEOWNERS
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
api/  (5 files)
  tests/  (3 files)
    test-mountRedraw.js
    test-router.js
    test-routerGetSet.js
  mount-redraw.js
  router.js
docs/  (5 files)
  code-of-conduct.md
  contributing.md
  credits.md
  recent-changes.md
  releasing.md
pathname/  (6 files)
  tests/  (3 files)
    test-buildPathname.js
    test-compileTemplate.js
    test-parsePathname.js
  build.js
  compileTemplate.js
  parse.js
performance/  (2 files)
  index.html
  test-perf.js
querystring/  (4 files)
  tests/  (2 files)
    test-buildQueryString.js
    test-parseQueryString.js
  build.js
  parse.js
render/  (47 files)
  tests/  (37 files)
    manual/  (5 files)
      … 5 files under this directory
    .eslintrc.js
    test-attributes.js
    test-component.js
    test-createElement.js
    test-createFragment.js
    test-createHTML.js
    test-createNodes.js
    test-createText.js
    test-domFor.js
    test-event.js
    test-fragment.js
    test-hyperscript.js
    test-input.js
    test-normalize.js
    test-normalizeChildren.js
    test-normalizeComponentChildren.js
    test-onbeforeremove.js
    test-onbeforeupdate.js
    test-oncreate.js
    test-oninit.js
    test-onremove.js
    test-onupdate.js
    test-render-hyperscript-integration.js
    test-render.js
    … 8 more files
  cachedAttrsIsStaticMap.js
  delayedRemoval.js
  domFor.js
  emptyAttrs.js
  fragment.js
  hyperscript.js
  hyperscriptVnode.js
  render.js
  trust.js
  vnode.js
request/  (2 files)
  tests/  (1 files)
    test-request.js
  request.js
scripts/  (7 files)
  tests/  (1 files)
    test-bundler.js
  .eslintrc.js
  _bundler-impl.js
  bundler-readme.md
  bundler.js
  minify-stream.js
  set-versioned-branch.sh
stream/  (4 files)
  tests/  (3 files)
    test-scan.js
    test-scanMerge.js
    test-stream.js
  stream.js
test-utils/  (16 files)
  tests/  (8 files)
    test-browserMock.js
    test-callAsync.js
    test-components.js
    test-domMock.js
    test-parseURL.js
    test-pushStateMock.js
    test-throttleMock.js
    test-xhrMock.js
  browserMock.js
  callAsync.js
  components.js
  domMock.js
  parseURL.js
  pushStateMock.js
  throttleMock.js
  xhrMock.js
tests/  (1 files)
  test-api.js
util/  (5 files)
  tests/  (2 files)
    test-censor.js
    test-decodeURIComponentSafe.js
  censor.js
  decodeURIComponentSafe.js
  hasOwn.js
.editorconfig
.eslintignore
.eslintrc.js
.gitattributes
.gitignore
.npmignore
LICENSE
README.md
browser.js
hyperscript.js
index.js
mithril.js
mount-redraw.js
mount.js
package.json
redraw.js
render.js
request.js
route.js
stream.js
```

## Entry points

- [index.js](https://github.com/MithrilJS/mithril.js/blob/092989a259f2eba05b406a024cca89bd97417f92/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 2 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 11 file(s) under core modules (observed from repository paths and static analysis). |
| pathname package | library | Observed | Groups 3 file(s) under pathname package (observed from repository paths and static analysis). |
| performance package | library | Observed | Groups 1 file(s) under performance package (observed from repository paths and static analysis). |
| querystring package | library | Observed | Groups 2 file(s) under querystring package (observed from repository paths and static analysis). |
| render package | library | Observed | Groups 10 file(s) under render package (observed from repository paths and static analysis). |
| request package | library | Observed | Groups 1 file(s) under request package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 5 file(s) under scripts package (observed from repository paths and static analysis). |
| stream package | library | Observed | Groups 1 file(s) under stream package (observed from repository paths and static analysis). |
| test-utils package | library | Observed | Groups 8 file(s) under test-utils package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 61 file(s) under tests (observed from repository paths and static analysis). |
| util package | library | Observed | Groups 3 file(s) under util package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/ISSUE_TEMPLATE/1-core.yml` (config)
- `.github/ISSUE_TEMPLATE/2-stream.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/issue-create.yml` (ci)
- `.github/workflows/notify-release.yml` (ci)
- `.github/workflows/pr-create-release.yml` (ci)
- `.github/workflows/publish-prerelease.yml` (ci)
- `.github/workflows/push-release.yml` (ci)
- `.github/workflows/rollback.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `package.json` (manifest)

## Top-level layout

- `render` — 47 analysed file(s)
- `(root files)` — 20 analysed file(s)
- `test-utils` — 16 analysed file(s)
- `.github` — 13 analysed file(s)
- `scripts` — 7 analysed file(s)
- `pathname` — 6 analysed file(s)
- `api` — 5 analysed file(s)
- `docs` — 5 analysed file(s)
- `util` — 5 analysed file(s)
- `querystring` — 4 analysed file(s)
- `stream` — 4 analysed file(s)
- `performance` — 2 analysed file(s)
- `request` — 2 analysed file(s)
- `tests` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `092989a259f2eba05b406a024cca89bd97417f92` is the revision these paths and observations refer to.
