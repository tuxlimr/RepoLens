# Project structure: requirejs/requirejs

**Analysed commit:** `7faea6492e190f0ff2ded4b86a76f11eaf1ae6d9`

**Commit reference:** [7faea6492e190f0ff2ded4b86a76f11eaf1ae6d9](https://github.com/requirejs/requirejs/commit/7faea6492e190f0ff2ded4b86a76f11eaf1ae6d9)

**Tree at this commit:** [requirejs/requirejs@7faea6492e19](https://github.com/requirejs/requirejs/tree/7faea6492e190f0ff2ded4b86a76f11eaf1ae6d9)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | requirejs/requirejs |
| Description | A file and module loader for JavaScript |
| Stars | 12899 |
| Forks | 2309 |
| Licence | Other |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `7faea6492e190f0ff2ded4b86a76f11eaf1ae6d9` |
| Retrieved at | 2026-11-14T19:12:02.973897+00:00 |
| Files in this snapshot | 633 |

## Directory tree

```text
.github/  (1 files)
  CONTRIBUTING.md
docs/  (19 files)
  design/  (1 files)
    packages.md
  api.html
  commonjs.html
  contributing.html
  dojo.html
  download.html
  errors.html
  faq-advanced.html
  faq-optimization.html
  faq.html
  history.html
  jquery.html
  node.html
  optimization.html
  plugins.html
  requirements.html
  start.html
  why.html
  whyamd.html
tests/  (601 files)
  anon/  (11 files)
    sub/  (1 files)
      … 1 files under this directory
    a.js
    anon-tests.js
    anonSimple.html
    blue.js
    c.js
    green.js
    magenta.js
    message.txt
    red.js
    yellow.js
  bundles/  (5 files)
    bundles-tests.js
    bundles.html
    main.js
    second.js
    third.js
  circular/  (31 files)
    414/  (6 files)
      … 6 files under this directory
    complexPlugin/  (9 files)
      … 9 files under this directory
    dupe/  (3 files)
      … 3 files under this directory
    transpiler/  (7 files)
      … 7 files under this directory
    a.js
    b.js
    c.js
    circularPlugin-tests.js
    circularPlugin.html
    plugin.js
  cjsSpace/  (7 files)
    a.js
    b.js
    c.js
    cjsDotRequire-tests.js
    cjsDotRequire.html
    cjsSpace-tests.js
    cjsSpace.html
  commentParen/  (3 files)
    a.js
    b.js
    commentParen.html
  commonjs/  (53 files)
    tests/  (53 files)
      … 53 files under this directory
  dataMain/  (14 files)
    baseUrl/  (3 files)
      … 3 files under this directory
    dataMainIndex/  (2 files)
      … 2 files under this directory
    dataMainPlugin/  (4 files)
      … 4 files under this directory
    skipDataMain/  (3 files)
      … 3 files under this directory
    dataMain.html
    dataMain.js
  datauri/  (1 files)
    datauri.html
  defineDouble/  (1 files)
    defineDouble.html
  definedSpecified/  (4 files)
    a.js
    b.js
    definedSpecified-tests.js
    definedSpecified.html
  delayedDefine/  (2 files)
    delayedDefine-tests.js
    delayedDefine.html
  doh/  (9 files)
    _sounds/  (1 files)
      … 1 files under this directory
    LICENSE
    README
    _browserRunner.js
    _nodeRunner.js
    _rhinoRunner.js
    runner.html
    runner.js
    runner.sh
  domReady/  (6 files)
    domReady-tests.js
    domReady.html
    domReadyExtraConfig-tests.js
    domReadyExtraConfig.html
    one.js
    two.js
  dotTrim/  (6 files)
    sub/  (1 files)
      … 1 files under this directory
    util/  (1 files)
      … 1 files under this directory
    b.js
    dotTrim-tests.js
    dotTrim.html
    spell.js
  error/  (17 files)
    doubleRequire/  (3 files)
      … 3 files under this directory
    a.js
    b.js
    c.js
    d.js
    defineError.js
    defineErrorLocal.html
    errorChild.html
    errorContinue.html
    errorContinueLocal.html
    globalOnError.html
    plug.js
    pluginErrorContinue.html
    pluginErrorContinueLocal.html
    requireErrback.html
  exports/  (14 files)
    am.js
    assign.js
    assign2.js
    bm.js
    cm.js
    exports-tests.js
    exports.html
    funcSet.js
    implicitModule.js
    moduleAndExports-tests.js
    moduleAndExports.html
    simpleReturn.js
    usethis.js
    vanilla.js
  hasOwnProperty/  (5 files)
    hasOwnProperty-tests.js
    hasOwnProperty.html
    hasOwnProperty.js
    prototype.js
    toString.js
  i18n/  (8 files)
    nls/  (3 files)
      … 3 files under this directory
    common.html
    commonA.js
    commonB.js
    i18n.html
    testModule.js
  isBrowser/  (3 files)
    a.js
    isBrowser-tests.js
    isBrowser.html
  issue379/  (2 files)
    issue379.html
    issue379.js
  jquery/  (11 files)
    scripts/  (8 files)
      … 8 files under this directory
    jquery.html
    jqueryDynamic.html
    jqueryDynamic2.html
  jsonp/  (3 files)
    jsonp.html
    lamp.js
    twitter.html
  layers/  (5 files)
    build.sh
    epsilon.js
    helloWorld.txt
    layer1.js
    layers.html
  mapConfig/  (44 files)
    a1/  (1 files)
      … 1 files under this directory
    adapter/  (1 files)
      … 1 files under this directory
    another/  (4 files)
      … 4 files under this directory
    built/  (8 files)
      … 8 files under this directory
    c/  (1 files)
      … 1 files under this directory
    c1/  (1 files)
      … 1 files under this directory
    c2/  (1 files)
      … 1 files under this directory
    plug/  (3 files)
      … 3 files under this directory
    a1.js
    b.js
    c.js
    c1.js
    c2.js
    d.js
    e.js
    mapConfig-tests.js
    mapConfig.html
    mapConfigDelayed-tests.js
    mapConfigDelayed.html
    mapConfigMulti-tests.js
    mapConfigMulti.html
    mapConfigPlugin-tests.js
    mapConfigPlugin.html
    mapConfigRelative-tests.js
    mapConfigRelative.html
    mapConfigSpecificity-tests.js
    mapConfigSpecificity.html
    mapConfigStar-tests.js
    mapConfigStar.html
    mapConfigStarAdapter-tests.js
    mapConfigStarAdapter.html
    plug.js
  moduleConfig/  (5 files)
    b/  (1 files)
      … 1 files under this directory
    a.js
    moduleConfig-tests.js
    moduleConfig.html
    plain.js
  moduleExports/  (2 files)
    adder.js
    moduleExports.html
  nestedDefine/  (6 files)
    four.js
    nestedDefine.html
    nestedDefine2.html
    nestedDefine2.js
    one.js
    two.js
  nestedRelativeRequire/  (4 files)
    sub/  (2 files)
      … 2 files under this directory
    main.js
    nestedRelativeRequire.html
  nestedRequire/  (4 files)
    a.js
    base.js
    nestedRequire-tests.js
    nestedRequire.html
  nestedRequireConfig/  (2 files)
    nestedRequireConfig.html
    nestedRequireConfig.js
  onResourceLoad/  (4 files)
    a.js
    b.js
    nestedRequire-tests.js
    nestedRequire.html
  packages/  (32 files)
    bar/  (1 files)
      … 1 files under this directory
    baz/  (2 files)
      … 2 files under this directory
    config/  (2 files)
      … 2 files under this directory
    dojox/  (3 files)
      … 3 files under this directory
    foo/  (2 files)
      … 2 files under this directory
    funky/  (2 files)
      … 2 files under this directory
    optimizing/  (9 files)
      … 9 files under this directory
    pkgs/  (8 files)
      … 8 files under this directory
    packages-tests.js
    packages.html
    replace.js
  packagesMultiLevel/  (11 files)
    @foo/  (2 files)
      … 2 files under this directory
    baz@2.0.0/  (2 files)
      … 2 files under this directory
    build.js
    config.js
    expected-built.js
    packagesMultiLevel-built.html
    packagesMultiLevel-tests-built.js
    packagesMultiLevel-tests.js
    packagesMultiLevel.html
  packagesNestedMain/  (4 files)
    foo/  (2 files)
      … 2 files under this directory
    packagesNestedMain-tests.js
    packagesNestedMain.html
  packagesNode/  (2 files)
    packagesNode-tests.js
    packagesNode.html
  packagesNodeAdapter/  (2 files)
    packagesNodeAdapter-tests.js
    packagesNodeAdapter.html
  pathArray/  (6 files)
    withMap/  (3 files)
      … 3 files under this directory
    pathArray.html
    pathArrayFail.html
    real.js
  paths/  (12 files)
    first.js/  (2 files)
      … 2 files under this directory
    impl/  (2 files)
      … 2 files under this directory
    relativeNormalize/  (4 files)
      … 4 files under this directory
    paths.html
    relativeModuleId-tests.js
    relativeModuleId.html
    util.js
  pluginNormalize/  (1 files)
    pluginNormalize.html
  pluginNormalizeLoad/  (2 files)
    Plugin.js
    pluginNormalizeLoad.html
  plugins/  (87 files)
    complexNormalize/  (6 files)
      … 6 files under this directory
    delegated/  (4 files)
      … 4 files under this directory
    fromText/  (7 files)
      … 7 files under this directory
    fromTextEvalError/  (4 files)
      … 4 files under this directory
    fromTextNoDefine/  (4 files)
      … 4 files under this directory
    onerror/  (3 files)
      … 3 files under this directory
    pluginBundles/  (3 files)
      … 3 files under this directory
    pluginBundlesSeparateText/  (4 files)
      … 4 files under this directory
    pluginLast/  (12 files)
      … 12 files under this directory
    pluginMap/  (8 files)
      … 8 files under this directory
    pluginMapSameName/  (3 files)
      … 3 files under this directory
    pluginNormalize/  (4 files)
      … 4 files under this directory
    pluginShim/  (4 files)
      … 4 files under this directory
    prime/  (4 files)
      … 4 files under this directory
    textDepend/  (4 files)
      … 4 files under this directory
    a.js
    b.js
    c.js
    double.html
    double.js
    earth.js
    index.js
    indexBuilder.js
    nameOnly-tests.js
    nameOnly.html
    nameOnly.js
    sync-tests.js
    sync.html
  relative/  (16 files)
    foo/  (5 files)
      … 5 files under this directory
    greek/  (2 files)
      … 2 files under this directory
    outsideBaseUrl/  (4 files)
      … 4 files under this directory
    relative-tests.js
    relative.html
    relativeBaseUrl-tests.js
    relativeBaseUrl.html
    top.js
  remoteUrls/  (5 files)
    jqwrap.js
    remoteUrls-tests.js
    remoteUrls.html
    util.js
    util2.js
  requireAsync/  (2 files)
    requireAsync-tests.js
    requireAsync.html
  requirePluginLoad/  (2 files)
    requirePluginLoad-tests.js
    requirePluginLoad.html
  secondLateConfigPlugin/  (7 files)
    app/  (4 files)
      … 4 files under this directory
    plugin1_ko/  (2 files)
      … 2 files under this directory
    secondLateConfigPlugin.html
  shim/  (10 files)
    built/  (2 files)
      … 2 files under this directory
    a.js
    b.js
    basic-tests.js
    basic.html
    c.js
    d.js
    e.js
    f.js
  specialDeps/  (3 files)
    foo.js
    specialDeps-tests.js
    specialDeps.html
  text/  (16 files)
    resources/  (2 files)
      … 2 files under this directory
    local.js
    plain.txt
    separate.js
    subwidget.html
    subwidget.js
    subwidget2.html
    text.html
    textBuilt.html
    textBuilt.js
    textOnError.html
    textOnXhr.html
    textOnly.html
    widget.html
    widget.js
  toUrl/  (10 files)
    sub/  (4 files)
      … 4 files under this directory
    .hidden.html
    auxil.html
    main.html
    main.js
    toUrl-tests.js
    toUrl.html
  trailingComma/  (3 files)
    a.js
    trailingComma.html
    trailingComma.js
  undef/  (7 files)
    globalFoo.js
    real.js
    undef.html
    undefEnforceShim.html
    undefLocal.html
    undefNoRequire.html
    undefNoRequire2.html
  uniques/  (4 files)
    one.js
    three.js
    two.js
    uniques.html
  universal/  (9 files)
    eye.js
    newt.js
    spell.js
    tail.js
    universal-built.html
    universal-tests-built-expected.js
    universal-tests-built.js
    universal-tests.js
    universal.html
  unorderedDefine/  (3 files)
    app.js
    bar.js
    unorderedDefine.html
  urlfetch/  (4 files)
    one.js
    three.js
    two.js
    urlfetch.html
  version1/  (4 files)
    alpha.js
    beta.js
    gamma.js
    omega.js
  version2/  (4 files)
    alpha.js
    beta.js
    epsilon.js
    omega.js
  NAMESPACE.html
  afterload.html
  afterloadreadystate.js
  all.js
  bar
  baseUrl.html
  circular-tests.js
  circular.html
  config.html
  configRequirejs.html
  depEmpty.html
  depoverlap.html
  depoverlap.js
  dimple.js
  dos.js
  foo
  func.js
  funcFour.js
  funcOne.js
  funcThree.js
  funcTwo.js
  index.html
  map.js
  multiversion.html
  … 17 more files
.gitignore
.jscsrc
.jshintrc
.travis.yml
LICENSE
README.md
index.html
package.json
require.js
tasks.txt
testBaseUrl.js
updatesubs.sh
```

## Entry points

- [require.js](https://github.com/requirejs/requirejs/blob/7faea6492e190f0ff2ded4b86a76f11eaf1ae6d9/require.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 601 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.travis.yml` (ci)
- `package.json` (manifest)

## Top-level layout

- `tests` — 601 analysed file(s)
- `docs` — 19 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 17 file(s) were skipped during inventory (17 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `7faea6492e190f0ff2ded4b86a76f11eaf1ae6d9` is the revision these paths and observations refer to.
