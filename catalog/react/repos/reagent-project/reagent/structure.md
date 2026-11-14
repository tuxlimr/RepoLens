# Project structure: reagent-project/reagent

**Analysed commit:** `7ad8cdf2c05737256bd4583b845164d93a3becf4`

**Commit reference:** [7ad8cdf2c05737256bd4583b845164d93a3becf4](https://github.com/reagent-project/reagent/commit/7ad8cdf2c05737256bd4583b845164d93a3becf4)

**Tree at this commit:** [reagent-project/reagent@7ad8cdf2c057](https://github.com/reagent-project/reagent/tree/7ad8cdf2c05737256bd4583b845164d93a3becf4)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | reagent-project/reagent |
| Description | A minimalistic ClojureScript interface to React.js |
| Stars | 4897 |
| Forks | 412 |
| Licence | MIT |
| Language | Clojure |
| Default branch | master |
| Analysed commit | `7ad8cdf2c05737256bd4583b845164d93a3becf4` |
| Retrieved at | 2026-11-14T19:14:34.014614+00:00 |
| Files in this snapshot | 209 |

## Directory tree

```text
.claude/  (2 files)
  launch.json
  settings.json
.clj-kondo/  (2 files)
  funcool/  (1 files)
    promesa/  (1 files)
      … 1 files under this directory
  config.edn
.github/  (4 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (1 files)
    clojure.yml
  issue_template.md
.lsp/  (1 files)
  config.edn
demo/  (20 files)
  reagentdemo/  (19 files)
    news/  (11 files)
      … 11 files under this directory
    common.cljs
    core.cljs
    dev.cljs
    intro.cljs
    main.cljs
    news.cljs
    syntax.clj
    syntax.cljs
  sitetools/  (1 files)
    core.cljs
doc/  (30 files)
  FAQ/  (8 files)
    CljsjsReactProblems.md
    ComponentNotRerendering.md
    ForcingComponentRecreation.md
    HtmlEntities.md
    MyAttributesAreMissing.md
    UsingAnEntity.md
    UsingRefs.md
    dangerouslySetInnerHTML.md
  examples/  (2 files)
    material-ui.md
    smooth-ui.md
  0.8-upgrade.md
  2.0-upgrade.md
  BatchingAndTiming.md
  ControlledInputs.md
  CreatingReagentComponents.md
  InteropWithReact.md
  ManagingState.md
  README.md
  React19.md
  ReactFeatures.md
  ReactRenderers.md
  ReagentCompiler.md
  Security.md
  ServerSideRendering.md
  UsingHiccupToDescribeHTML.md
  UsingSquareBracketsInsteadOfParens.md
  WhenDoComponentsUpdate.md
  cljdoc.edn
  development.md
  reagent1.md
examples/  (62 files)
  functional-components-and-hooks/  (7 files)
    resources/  (2 files)
      … 2 files under this directory
    src/  (1 files)
      … 1 files under this directory
    README.md
    deps.edn
    package.json
    shadow-cljs.edn
  geometry/  (9 files)
    resources/  (2 files)
      … 2 files under this directory
    src/  (3 files)
      … 3 files under this directory
    README.md
    deps.edn
    package.json
    shadow-cljs.edn
  material-ui/  (6 files)
    resources/  (1 files)
      … 1 files under this directory
    src/  (1 files)
      … 1 files under this directory
    README.md
    deps.edn
    package.json
    shadow-cljs.edn
  react-context/  (6 files)
    resources/  (1 files)
      … 1 files under this directory
    src/  (1 files)
      … 1 files under this directory
    README.md
    deps.edn
    package.json
    shadow-cljs.edn
  react-mde/  (6 files)
    resources/  (1 files)
      … 1 files under this directory
    src/  (1 files)
      … 1 files under this directory
    README.md
    deps.edn
    package.json
    shadow-cljs.edn
  react-transition-group/  (7 files)
    resources/  (2 files)
      … 2 files under this directory
    src/  (1 files)
      … 1 files under this directory
    README.md
    deps.edn
    package.json
    shadow-cljs.edn
  shadow-dom-input/  (7 files)
    resources/  (2 files)
      … 2 files under this directory
    src/  (1 files)
      … 1 files under this directory
    README.md
    deps.edn
    package.json
    shadow-cljs.edn
  simple/  (7 files)
    resources/  (2 files)
      … 2 files under this directory
    src/  (1 files)
      … 1 files under this directory
    README.md
    deps.edn
    package.json
    shadow-cljs.edn
  todomvc/  (7 files)
    resources/  (2 files)
      … 2 files under this directory
    src/  (1 files)
      … 1 files under this directory
    README.md
    deps.edn
    package.json
    shadow-cljs.edn
lib/  (1 files)
  modules.js
logo/  (2 files)
  logo-text.svg
  logo.svg
outsite/  (1 files)
  public/  (1 files)
    README.md
prerender/  (1 files)
  sitetools/  (1 files)
    prerender.cljs
site/  (3 files)
  public/  (3 files)
    css/  (2 files)
      … 2 files under this directory
    index.html
src/  (20 files)
  clj-kondo/  (1 files)
    clj-kondo.exports/  (1 files)
      … 1 files under this directory
  reagent/  (19 files)
    dom/  (2 files)
      … 2 files under this directory
    impl/  (7 files)
      … 7 files under this directory
    core.clj
    core.cljs
    debug.clj
    debug.cljs
    dom.cljs
    hooks.cljs
    interop.clj
    interop.cljs
    ratom.clj
    ratom.cljs
test/  (15 files)
  reagent/  (2 files)
    impl/  (2 files)
      … 2 files under this directory
  reagenttest/  (12 files)
    performancetest.cljs
    runtests.cljs
    testcursor.cljs
    testhooks.cljs
    testratom.cljs
    testratomasync.cljs
    testreagent.cljs
    testtrack.cljs
    testwithlet.cljs
    testwrap.cljs
    utils.clj
    utils.cljs
  runners/  (1 files)
    karma.conf.js
test-environments/  (20 files)
  browser-cljsjs/  (1 files)
    test.sh
  browser-cljsjs-prod/  (1 files)
    test.sh
  browser-npm/  (1 files)
    test.sh
  browser-npm-prod/  (1 files)
    test.sh
  bundle/  (5 files)
    build.edn
    karma.conf.js
    test.sh
    webpack.config.js
    workaround.js
  bundle-adv/  (7 files)
    README.md
    build.edn
    build.sh
    karma.conf.js
    karma.edn
    test.sh
    webpack.config.js
  node-cljsjs/  (1 files)
    test_disabled.sh
  node-npm/  (1 files)
    test.sh
  shadow-cljs-prod/  (2 files)
    karma.conf.js
    test.sh
.cljfmt.edn
.git-blame-ignore-revs
.gitignore
.nvmrc
CHANGELOG.md
CLAUDE.md
CONTRIBUTING.md
LICENSE
README.md
ROADMAP.md
SECURITY.md
bb.edn
build-docs-index.sh
build-docs.sh
build-example-site.sh
cljfmt.sh
codecov.yml
deps.edn
package.json
prepare-tests.sh
project.clj
react-18-package-lock.json
react-18-package.json
run-tests.sh
… 1 more files
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 6 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 1 file(s) under lib package (observed from repository paths and static analysis). |
| test-environments package | library | Observed | Groups 15 file(s) under test-environments package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 16 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.claude/launch.json` (config)
- `.claude/settings.json` (config)
- `.github/workflows/clojure.yml` (ci)
- `codecov.yml` (config)
- `examples/functional-components-and-hooks/package.json` (manifest)
- `examples/geometry/package.json` (manifest)
- `examples/material-ui/package.json` (manifest)
- `examples/react-context/package.json` (manifest)
- `examples/react-mde/package.json` (manifest)
- `examples/react-transition-group/package.json` (manifest)
- `examples/shadow-dom-input/package.json` (manifest)
- `examples/simple/package.json` (manifest)
- `examples/todomvc/package.json` (manifest)
- `package.json` (manifest)
- `react-18-package-lock.json` (config)
- `react-18-package.json` (config)

## Top-level layout

- `examples` — 62 analysed file(s)
- `doc` — 30 analysed file(s)
- `(root files)` — 25 analysed file(s)
- `demo` — 20 analysed file(s)
- `src` — 20 analysed file(s)
- `test-environments` — 20 analysed file(s)
- `test` — 15 analysed file(s)
- `.github` — 4 analysed file(s)
- `site` — 3 analysed file(s)
- `.claude` — 2 analysed file(s)
- `.clj-kondo` — 2 analysed file(s)
- `logo` — 2 analysed file(s)
- `.lsp` — 1 analysed file(s)
- `lib` — 1 analysed file(s)
- `outsite` — 1 analysed file(s)
- `prerender` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 10 file(s) were skipped during inventory (10 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `7ad8cdf2c05737256bd4583b845164d93a3becf4` is the revision these paths and observations refer to.
