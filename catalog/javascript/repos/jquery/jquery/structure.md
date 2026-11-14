# Project structure: jquery/jquery

**Analysed commit:** `feaa9fcdb68cdeadf013d97d8fd40848d4618578`

**Commit reference:** [feaa9fcdb68cdeadf013d97d8fd40848d4618578](https://github.com/jquery/jquery/commit/feaa9fcdb68cdeadf013d97d8fd40848d4618578)

**Tree at this commit:** [jquery/jquery@feaa9fcdb68c](https://github.com/jquery/jquery/tree/feaa9fcdb68cdeadf013d97d8fd40848d4618578)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | jquery/jquery |
| Description | jQuery JavaScript Library |
| Stars | 59946 |
| Forks | 20706 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `feaa9fcdb68cdeadf013d97d8fd40848d4618578` |
| Retrieved at | 2026-11-14T19:10:36.419652+00:00 |
| Files in this snapshot | 321 |

## Directory tree

```text
.github/  (12 files)
  workflows/  (9 files)
    browser-tests-beta.yml
    browser-tests.yml
    browserstack-dispatch.yml
    browserstack.yml
    codeql-analysis.yml
    filestash.yml
    lock-threads.yml
    node.js.yml
    verify-release.yml
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
.husky/  (2 files)
  commit-msg
  pre-push
dist-module/  (3 files)
  wrappers/  (2 files)
    jquery.node-module-wrapper.js
    jquery.node-module-wrapper.slim.js
  package.json
src/  (138 files)
  ajax/  (8 files)
    var/  (3 files)
      … 3 files under this directory
    binary.js
    jsonp.js
    load.js
    script.js
    xhr.js
  attributes/  (4 files)
    attr.js
    classes.js
    prop.js
    val.js
  core/  (16 files)
    var/  (1 files)
      … 1 files under this directory
    DOMEval.js
    access.js
    camelCase.js
    init.js
    isArrayLike.js
    isAttached.js
    isObviousHtml.js
    nodeName.js
    parseHTML.js
    parseXML.js
    ready-no-deferred.js
    ready.js
    readyException.js
    stripAndCollapse.js
    toType.js
  css/  (13 files)
    var/  (5 files)
      … 5 files under this directory
    adjustCSS.js
    cssCamelCase.js
    curCSS.js
    finalPropName.js
    hiddenVisibleSelectors.js
    isAutoPx.js
    showHide.js
    support.js
  data/  (4 files)
    var/  (3 files)
      … 3 files under this directory
    Data.js
  deferred/  (1 files)
    exceptionHook.js
  deprecated/  (2 files)
    ajax-event-alias.js
    event.js
  effects/  (2 files)
    Tween.js
    animatedSelector.js
  event/  (1 files)
    trigger.js
  exports/  (2 files)
    amd.js
    global.js
  manipulation/  (8 files)
    var/  (2 files)
      … 2 files under this directory
    _evalUrl.js
    buildFragment.js
    domManip.js
    getAll.js
    setGlobalEval.js
    wrapMap.js
  queue/  (1 files)
    delay.js
  selector/  (21 files)
    var/  (10 files)
      … 10 files under this directory
    createCache.js
    escapeSelector.js
    filterMatchExpr.js
    preFilter.js
    rbuggyQSA.js
    selectorError.js
    testContext.js
    toSelector.js
    tokenize.js
    unescapeSelector.js
    uniqueSort.js
  traversing/  (4 files)
    var/  (3 files)
      … 3 files under this directory
    findFilter.js
  var/  (27 files)
    ObjectFunctionString.js
    arr.js
    class2type.js
    createElement.js
    document.js
    documentElement.js
    flat.js
    fnToString.js
    getProto.js
    hasOwn.js
    indexOf.js
    isIE.js
    isWindow.js
    pnum.js
    pop.js
    push.js
    rcheckableType.js
    rcssNum.js
    rdoubleDash.js
    rnothtmlwhite.js
    rtrimCSS.js
    slice.js
    sort.js
    splice.js
    … 3 more files
  ajax.js
  attributes.js
  callbacks.js
  core.js
  css.js
  data.js
  deferred.js
  deprecated.js
  dimensions.js
  effects.js
  event.js
  jquery.js
  manipulation.js
  offset.js
  queue.js
  selector-native.js
  selector.js
  serialize.js
  traversing.js
  wrap.js
  wrapper-esm.js
  wrapper-factory-esm.js
  wrapper-factory.js
  wrapper.js
test/  (150 files)
  bundler_smoke_tests/  (11 files)
    lib/  (3 files)
      … 3 files under this directory
    src-esm-commonjs/  (2 files)
      … 2 files under this directory
    src-pure-esm/  (1 files)
      … 1 files under this directory
    rollup-commonjs.config.js
    rollup-pure-esm.config.js
    run-jsdom-tests.js
    test.html
    webpack.config.cjs
  data/  (81 files)
    ajax/  (3 files)
      … 3 files under this directory
    core/  (7 files)
      … 7 files under this directory
    css/  (4 files)
      … 4 files under this directory
    data/  (1 files)
      … 1 files under this directory
    dimensions/  (1 files)
      … 1 files under this directory
    event/  (7 files)
      … 7 files under this directory
    manipulation/  (3 files)
      … 3 files under this directory
    offset/  (8 files)
      … 8 files under this directory
    selector/  (3 files)
      … 3 files under this directory
    support/  (6 files)
      … 6 files under this directory
    1x1.svg
    badcall.js
    badjson.js
    cleanScript.html
    csp-ajax-script-downloaded.js
    csp-ajax-script.html
    csp-ajax-script.js
    csp-nonce-external.html
    csp-nonce-external.js
    csp-nonce-globaleval.html
    csp-nonce-globaleval.js
    csp-nonce.html
    csp-nonce.js
    csp.include.html
    dashboard.xml
    frame.html
    iframe.html
    iframeTest.js
    inner_module.js
    inner_nomodule.js
    json_obj.js
    mock.php
    module.js
    name.html
    … 14 more files
  integration/  (5 files)
    data/  (3 files)
      … 3 files under this directory
    gh-1764-fullscreen.html
    gh-2343-ie-radio-click.html
  node_smoke_tests/  (20 files)
    commonjs/  (8 files)
      … 8 files under this directory
    dual/  (4 files)
      … 4 files under this directory
    module/  (8 files)
      … 8 files under this directory
  promises_aplus_adapters/  (2 files)
    deferred.cjs
    when.cjs
  unit/  (24 files)
    ajax.js
    animation.js
    attributes.js
    basic.js
    callbacks.js
    core.js
    css.js
    data.js
    deferred.js
    deprecated.js
    dimensions.js
    effects.js
    event.js
    exports.js
    manipulation.js
    offset.js
    queue.js
    ready.js
    selector.js
    serialize.js
    support.js
    traversing.js
    tween.js
    wrap.js
  delegatetest.html
  hovertest.html
  index.html
  jquery.js
  middleware-mockserver.cjs
  networkerror.html
  xhtml.php
.editorconfig
.gitattributes
.gitignore
.mailmap
.npmignore
.release-it.cjs
AUTHORS.txt
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE.txt
README.md
SECURITY.md
changelog.md
eslint.config.js
jtr-isolate.yml
package.json
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| ajax package | library | Observed | Groups 8 file(s) under ajax package (observed from repository paths and static analysis). |
| ajax.js package | library | Observed | Groups 1 file(s) under ajax.js package (observed from repository paths and static analysis). |
| attributes package | library | Observed | Groups 4 file(s) under attributes package (observed from repository paths and static analysis). |
| attributes.js package | library | Observed | Groups 1 file(s) under attributes.js package (observed from repository paths and static analysis). |
| callbacks.js package | library | Observed | Groups 1 file(s) under callbacks.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| core.js package | library | Observed | Groups 1 file(s) under core.js package (observed from repository paths and static analysis). |
| css package | library | Observed | Groups 13 file(s) under css package (observed from repository paths and static analysis). |
| css.js package | library | Observed | Groups 1 file(s) under css.js package (observed from repository paths and static analysis). |
| data.js package | library | Observed | Groups 1 file(s) under data.js package (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 4 file(s) under data layer (observed from repository paths and static analysis). |
| deferred package | library | Observed | Groups 1 file(s) under deferred package (observed from repository paths and static analysis). |
| deferred.js package | library | Observed | Groups 1 file(s) under deferred.js package (observed from repository paths and static analysis). |
| deprecated package | library | Observed | Groups 2 file(s) under deprecated package (observed from repository paths and static analysis). |
| deprecated.js package | library | Observed | Groups 1 file(s) under deprecated.js package (observed from repository paths and static analysis). |
| dimensions.js package | library | Observed | Groups 1 file(s) under dimensions.js package (observed from repository paths and static analysis). |
| dist-module package | library | Observed | Groups 2 file(s) under dist-module package (observed from repository paths and static analysis). |
| effects package | library | Observed | Groups 2 file(s) under effects package (observed from repository paths and static analysis). |
| effects.js package | library | Observed | Groups 1 file(s) under effects.js package (observed from repository paths and static analysis). |
| event package | library | Observed | Groups 1 file(s) under event package (observed from repository paths and static analysis). |
| event.js package | library | Observed | Groups 1 file(s) under event.js package (observed from repository paths and static analysis). |
| exports package | library | Observed | Groups 2 file(s) under exports package (observed from repository paths and static analysis). |
| jquery.js package | library | Observed | Groups 1 file(s) under jquery.js package (observed from repository paths and static analysis). |
| manipulation package | library | Observed | Groups 8 file(s) under manipulation package (observed from repository paths and static analysis). |
| manipulation.js package | library | Observed | Groups 1 file(s) under manipulation.js package (observed from repository paths and static analysis). |
| offset.js package | library | Observed | Groups 1 file(s) under offset.js package (observed from repository paths and static analysis). |
| queue package | library | Observed | Groups 1 file(s) under queue package (observed from repository paths and static analysis). |
| queue.js package | library | Observed | Groups 1 file(s) under queue.js package (observed from repository paths and static analysis). |
| selector package | library | Observed | Groups 21 file(s) under selector package (observed from repository paths and static analysis). |
| selector.js package | library | Observed | Groups 1 file(s) under selector.js package (observed from repository paths and static analysis). |
| selector-native.js package | library | Observed | Groups 1 file(s) under selector-native.js package (observed from repository paths and static analysis). |
| serialize.js package | library | Observed | Groups 1 file(s) under serialize.js package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 16 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 150 file(s) under tests (observed from repository paths and static analysis). |
| traversing package | library | Observed | Groups 4 file(s) under traversing package (observed from repository paths and static analysis). |
| traversing.js package | library | Observed | Groups 1 file(s) under traversing.js package (observed from repository paths and static analysis). |
| var package | library | Observed | Groups 27 file(s) under var package (observed from repository paths and static analysis). |
| wrap.js package | library | Observed | Groups 1 file(s) under wrap.js package (observed from repository paths and static analysis). |
| wrapper-esm.js package | library | Observed | Groups 1 file(s) under wrapper-esm.js package (observed from repository paths and static analysis). |
| wrapper-factory-esm.js package | library | Observed | Groups 1 file(s) under wrapper-factory-esm.js package (observed from repository paths and static analysis). |
| wrapper-factory.js package | library | Observed | Groups 1 file(s) under wrapper-factory.js package (observed from repository paths and static analysis). |
| wrapper.js package | library | Observed | Groups 1 file(s) under wrapper.js package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/browser-tests-beta.yml` (ci)
- `.github/workflows/browser-tests.yml` (ci)
- `.github/workflows/browserstack-dispatch.yml` (ci)
- `.github/workflows/browserstack.yml` (ci)
- `.github/workflows/codeql-analysis.yml` (ci)
- `.github/workflows/filestash.yml` (ci)
- `.github/workflows/lock-threads.yml` (ci)
- `.github/workflows/node.js.yml` (ci)
- `.github/workflows/verify-release.yml` (ci)
- `dist-module/package.json` (manifest)
- `jtr-isolate.yml` (config)
- `package.json` (manifest)

## Top-level layout

- `test` — 150 analysed file(s)
- `src` — 138 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `.github` — 12 analysed file(s)
- `dist-module` — 3 analysed file(s)
- `.husky` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 27 file(s) were skipped during inventory (1 x likely secret file excluded; 26 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `feaa9fcdb68cdeadf013d97d8fd40848d4618578` is the revision these paths and observations refer to.
