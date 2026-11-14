# Project structure: Modernizr/Modernizr

**Analysed commit:** `612ec65ccdba311e8b1153b1076d18f0251943f6`

**Commit reference:** [612ec65ccdba311e8b1153b1076d18f0251943f6](https://github.com/Modernizr/Modernizr/commit/612ec65ccdba311e8b1153b1076d18f0251943f6)

**Tree at this commit:** [Modernizr/Modernizr@612ec65ccdba](https://github.com/Modernizr/Modernizr/tree/612ec65ccdba311e8b1153b1076d18f0251943f6)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Modernizr/Modernizr |
| Description | Modernizr is a JavaScript library that detects HTML5 and CSS3 features in the user’s browser. |
| Stars | 25676 |
| Forks | 2913 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `612ec65ccdba311e8b1153b1076d18f0251943f6` |
| Retrieved at | 2026-11-14T19:10:59.909086+00:00 |
| Files in this snapshot | 475 |

## Directory tree

```text
.github/  (10 files)
  ISSUE_TEMPLATE/  (4 files)
    ---bug-report.md
    ---test-request.md
    good-first-issue.md
    question.md
  workflows/  (3 files)
    coverage.yml
    deploy.yml
    testing.yml
  CODE_OF_CONDUCT.md
  codecov.yml
  dependabot.yaml
bin/  (2 files)
  modernizr
  modernizr.bat
feature-detects/  (305 files)
  a/  (3 files)
    aping.js
    areaping.js
    download.js
  audio/  (5 files)
    audio.js
    autoplay.js
    loop.js
    preload.js
    webaudio.js
  battery/  (2 files)
    battery.js
    lowbattery.js
  canvas/  (5 files)
    blending.js
    canvas.js
    text.js
    todataurl.js
    winding.js
  crypto/  (1 files)
    getrandomvalues.js
  css/  (86 files)
    all.js
    animations.js
    appearance.js
    aspectratio.js
    backdropfilter.js
    backgroundblendmode.js
    backgroundcliptext.js
    backgroundposition-shorthand.js
    backgroundposition-xy.js
    backgroundrepeat.js
    backgroundsize.js
    backgroundsizecover.js
    borderimage.js
    borderradius.js
    boxdecorationbreak.js
    boxshadow.js
    boxsizing.js
    calc.js
    checked.js
    chunit.js
    columns.js
    cssgrid.js
    cubicbezierrange.js
    customproperties.js
    … 62 more files
  dom/  (11 files)
    classlist.js
    createElement-attrs.js
    dataset.js
    documentfragment.js
    hidden.js
    intersection-observer.js
    microdata.js
    mutationObserver.js
    passiveeventlisteners.js
    shadowroot.js
    shadowrootlegacy.js
  elem/  (10 files)
    bdi.js
    details.js
    output.js
    picture.js
    progress-meter.js
    ruby.js
    template.js
    time.js
    track.js
    unknown.js
  es5/  (9 files)
    array.js
    date.js
    function.js
    object.js
    specification.js
    strictmode.js
    string.js
    syntax.js
    undefined.js
  es6/  (14 files)
    array.js
    arrow.js
    class.js
    collections.js
    generators.js
    math.js
    number.js
    object.js
    promises.js
    rest-parameters.js
    spread-array.js
    string-template.js
    string.js
    symbol.js
  es7/  (3 files)
    array.js
    rest-destructuring.js
    spread-object.js
  es8/  (1 files)
    object.js
  event/  (8 files)
    customevent.js
    deviceorientation-motion.js
    eventlistener.js
    forcetouch.js
    hashchange.js
    oninput.js
    pointerevents.js
    proximity.js
  file/  (2 files)
    api.js
    filesystem.js
  iframe/  (3 files)
    sandbox.js
    seamless.js
    srcdoc.js
  img/  (13 files)
    apng.js
    avif.js
    crossorigin.js
    exif-orientation.js
    jpeg2000.js
    jpegxr.js
    lazyloading.js
    sizes.js
    srcset.js
    webp-alpha.js
    webp-animation.js
    webp-lossless.js
    webp.js
  input/  (16 files)
    capture.js
    fileinput.js
    fileinputdirectory.js
    formaction.js
    formattribute.js
    formenctype.js
    formmethod.js
    formnovalidate.js
    formtarget.js
    input.js
    inputnumber-l10n.js
    inputsearchevent.js
    inputtypes.js
    placeholder.js
    requestautocomplete.js
    validation.js
  link/  (1 files)
    prefetch.js
  mediaquery/  (2 files)
    hovermq.js
    pointermq.js
  network/  (12 files)
    beacon.js
    connection-effectivetype.js
    connection.js
    eventsource.js
    fetch.js
    xhr-responsetype-arraybuffer.js
    xhr-responsetype-blob.js
    xhr-responsetype-document.js
    xhr-responsetype-json.js
    xhr-responsetype-text.js
    xhr-responsetype.js
    xhr2.js
  script/  (2 files)
    async.js
    defer.js
  speech/  (2 files)
    speech-recognition.js
    speech-synthesis.js
  storage/  (9 files)
    cookies.js
    indexeddb.js
    indexeddb2.js
    indexeddbblob.js
    localstorage.js
    quota-management-api.js
    sessionstorage.js
    userdata.js
    websqldatabase.js
  style/  (1 files)
    scoped.js
  svg/  (7 files)
    asimg.js
    clippaths.js
    filters.js
    foreignobject.js
    inline.js
    smil.js
    svg.js
  textarea/  (1 files)
    maxlength.js
  url/  (4 files)
    bloburls.js
    data-uri.js
    parser.js
    urlsearchparams.js
  video/  (5 files)
    autoplay.js
    crossorigin.js
    loop.js
    preload.js
    video.js
  webauthn/  (1 files)
    publickeycredential.js
  webgl/  (2 files)
    extensions.js
    webgl.js
  webrtc/  (4 files)
    datachannel.js
    getusermedia.js
    mediastream.js
    peerconnection.js
  websockets/  (1 files)
    binary.js
  window/  (5 files)
    atob-btoa.js
    framed.js
    matchmedia.js
    pushmanager.js
    resizeobserver.js
  workers/  (6 files)
    blobworkers.js
    dataworkers.js
    sharedworkers.js
    transferables.js
    webworkers.js
    workertypeoption.js
  ambientlight.js
  applicationcache.js
  blob.js
  broadcastchannel.js
  clipboard.js
  contenteditable.js
  contextmenu.js
  cors.js
  crypto.js
  custom-elements.js
  custom-protocol-handler.js
  dart.js
  dataview-api.js
  emoji.js
  flash.js
  fullscreen-api.js
  gamepad.js
  geolocation.js
  hiddenscroll.js
  history.js
  htmlimports.js
  ie8compat.js
  intl.js
  json.js
  … 24 more files
legacy/  (2 files)
  .coveralls.yml
  Gruntfile.js
lib/  (8 files)
  build-query.js
  build.js
  cli.js
  config-all.json
  generate-banner.js
  metadata.js
  options.js
  polyfills.json
media/  (6 files)
  .gitattributes
  Modernizr 2 Logo vertical big.ai
  Modernizr 2 Logo vertical medium.ai
  Modernizr 2 Logo vertical small.ai
  Modernizr 2 Logo.ai
  Modernizr 2 Logo.svg
scripts/  (2 files)
  generate-gh-pages.sh
  generate-license.js
src/  (48 files)
  Modernizr.js
  ModernizrProto.js
  addTest.js
  atRule.js
  classes.js
  computedStyle.js
  contains.js
  createElement.js
  cssToDOM.js
  cssomPrefixes.js
  docElement.js
  domPrefixes.js
  domPrefixesAll.js
  domToCSS.js
  fnBind.js
  generate.js
  getBody.js
  hasEvent.js
  hasOwnProp.js
  html5printshiv.js
  html5shiv.js
  injectElementWithStyles.js
  inputElem.js
  is.js
  … 24 more files
test/  (73 files)
  browser/  (62 files)
    integration/  (10 files)
      … 10 files under this directory
    src/  (45 files)
      … 45 files under this directory
    iframe.pug
    integration.css
    integration.pug
    sauce-browsers.json
    setup.js
    svgUnit.js
    unit.pug
  img/  (2 files)
    integration.svg
    unit.svg
  mocks/  (2 files)
    lib/  (2 files)
      … 2 files under this directory
  node/  (4 files)
    lib/  (4 files)
      … 4 files under this directory
  universal/  (2 files)
    lib/  (2 files)
      … 2 files under this directory
  cleanup.js
.babelrc
.editorconfig
.eslintrc
.gitattributes
.gitignore
HOW_TO_WRITE_FEATURE_DETECTS.md
LICENSE
README.hi.md
README.id.md
README.ka.md
README.md
README.pt_br.md
README.sp.md
README.sv.md
README.ta.md
README.tr.md
gulpfile.babel.js
inch.json
package.json
```

## Entry points

- [lib/cli.js](https://github.com/Modernizr/Modernizr/blob/612ec65ccdba311e8b1153b1076d18f0251943f6/lib/cli.js)
- [bin/modernizr](https://github.com/Modernizr/Modernizr/blob/612ec65ccdba311e8b1153b1076d18f0251943f6/bin/modernizr)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| addTest.js package | library | Observed | Groups 1 file(s) under addtest.js package (observed from repository paths and static analysis). |
| atRule.js package | library | Observed | Groups 1 file(s) under atrule.js package (observed from repository paths and static analysis). |
| classes.js package | library | Observed | Groups 1 file(s) under classes.js package (observed from repository paths and static analysis). |
| computedStyle.js package | library | Observed | Groups 1 file(s) under computedstyle.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| contains.js package | library | Observed | Groups 1 file(s) under contains.js package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| createElement.js package | library | Observed | Groups 1 file(s) under createelement.js package (observed from repository paths and static analysis). |
| cssomPrefixes.js package | library | Observed | Groups 1 file(s) under cssomprefixes.js package (observed from repository paths and static analysis). |
| cssToDOM.js package | library | Observed | Groups 1 file(s) under csstodom.js package (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 9 file(s) under data layer (observed from repository paths and static analysis). |
| docElement.js package | library | Observed | Groups 1 file(s) under docelement.js package (observed from repository paths and static analysis). |
| domPrefixes.js package | library | Observed | Groups 1 file(s) under domprefixes.js package (observed from repository paths and static analysis). |
| domPrefixesAll.js package | library | Observed | Groups 1 file(s) under domprefixesall.js package (observed from repository paths and static analysis). |
| domToCSS.js package | library | Observed | Groups 1 file(s) under domtocss.js package (observed from repository paths and static analysis). |
| feature-detects package | library | Observed | Groups 296 file(s) under feature-detects package (observed from repository paths and static analysis). |
| fnBind.js package | library | Observed | Groups 1 file(s) under fnbind.js package (observed from repository paths and static analysis). |
| generate.js package | library | Observed | Groups 1 file(s) under generate.js package (observed from repository paths and static analysis). |
| getBody.js package | library | Observed | Groups 1 file(s) under getbody.js package (observed from repository paths and static analysis). |
| hasEvent.js package | library | Observed | Groups 1 file(s) under hasevent.js package (observed from repository paths and static analysis). |
| hasOwnProp.js package | library | Observed | Groups 1 file(s) under hasownprop.js package (observed from repository paths and static analysis). |
| html5printshiv.js package | library | Observed | Groups 1 file(s) under html5printshiv.js package (observed from repository paths and static analysis). |
| html5shiv.js package | library | Observed | Groups 1 file(s) under html5shiv.js package (observed from repository paths and static analysis). |
| injectElementWithStyles.js package | library | Observed | Groups 1 file(s) under injectelementwithstyles.js package (observed from repository paths and static analysis). |
| inputElem.js package | library | Observed | Groups 1 file(s) under inputelem.js package (observed from repository paths and static analysis). |
| is.js package | library | Observed | Groups 1 file(s) under is.js package (observed from repository paths and static analysis). |
| isSVG.js package | library | Observed | Groups 1 file(s) under issvg.js package (observed from repository paths and static analysis). |
| legacy package | library | Observed | Groups 1 file(s) under legacy package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 6 file(s) under lib package (observed from repository paths and static analysis). |
| load.js package | library | Observed | Groups 1 file(s) under load.js package (observed from repository paths and static analysis). |
| modElem.js package | library | Observed | Groups 1 file(s) under modelem.js package (observed from repository paths and static analysis). |
| Modernizr.js package | library | Observed | Groups 1 file(s) under modernizr.js package (observed from repository paths and static analysis). |
| ModernizrProto.js package | library | Observed | Groups 1 file(s) under modernizrproto.js package (observed from repository paths and static analysis). |
| mq.js package | library | Observed | Groups 1 file(s) under mq.js package (observed from repository paths and static analysis). |
| mStyle.js package | library | Observed | Groups 1 file(s) under mstyle.js package (observed from repository paths and static analysis). |
| nativeTestProps.js package | library | Observed | Groups 1 file(s) under nativetestprops.js package (observed from repository paths and static analysis). |
| omPrefixes.js package | library | Observed | Groups 1 file(s) under omprefixes.js package (observed from repository paths and static analysis). |
| prefixed.js package | library | Observed | Groups 1 file(s) under prefixed.js package (observed from repository paths and static analysis). |
| prefixedCSS.js package | library | Observed | Groups 1 file(s) under prefixedcss.js package (observed from repository paths and static analysis). |
| prefixedCSSValue.js package | library | Observed | Groups 1 file(s) under prefixedcssvalue.js package (observed from repository paths and static analysis). |
| prefixes.js package | library | Observed | Groups 1 file(s) under prefixes.js package (observed from repository paths and static analysis). |
| roundedEquals.js package | library | Observed | Groups 1 file(s) under roundedequals.js package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 2 file(s) under scripts package (observed from repository paths and static analysis). |
| setClasses.js package | library | Observed | Groups 1 file(s) under setclasses.js package (observed from repository paths and static analysis). |
| slice.js package | library | Observed | Groups 1 file(s) under slice.js package (observed from repository paths and static analysis). |
| testAllProps.js package | library | Observed | Groups 1 file(s) under testallprops.js package (observed from repository paths and static analysis). |
| testDOMProps.js package | library | Observed | Groups 1 file(s) under testdomprops.js package (observed from repository paths and static analysis). |
| testProp.js package | library | Observed | Groups 1 file(s) under testprop.js package (observed from repository paths and static analysis). |
| testProps.js package | library | Observed | Groups 1 file(s) under testprops.js package (observed from repository paths and static analysis). |
| testPropsAll.js package | library | Observed | Groups 1 file(s) under testpropsall.js package (observed from repository paths and static analysis). |
| testRunner.js package | library | Observed | Groups 1 file(s) under testrunner.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 73 file(s) under tests (observed from repository paths and static analysis). |
| tests.js package | library | Observed | Groups 1 file(s) under tests.js package (observed from repository paths and static analysis). |
| testStyles.js package | library | Observed | Groups 1 file(s) under teststyles.js package (observed from repository paths and static analysis). |
| testXhrType.js package | library | Observed | Groups 1 file(s) under testxhrtype.js package (observed from repository paths and static analysis). |
| toStringFn.js package | library | Observed | Groups 1 file(s) under tostringfn.js package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/codecov.yml` (config)
- `.github/dependabot.yaml` (config)
- `.github/workflows/coverage.yml` (ci)
- `.github/workflows/deploy.yml` (ci)
- `.github/workflows/testing.yml` (ci)
- `inch.json` (config)
- `legacy/.coveralls.yml` (config)
- `lib/config-all.json` (config)
- `lib/polyfills.json` (config)
- `package.json` (manifest)

## Top-level layout

- `feature-detects` — 305 analysed file(s)
- `test` — 73 analysed file(s)
- `src` — 48 analysed file(s)
- `(root files)` — 19 analysed file(s)
- `.github` — 10 analysed file(s)
- `lib` — 8 analysed file(s)
- `media` — 6 analysed file(s)
- `bin` — 2 analysed file(s)
- `legacy` — 2 analysed file(s)
- `scripts` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `612ec65ccdba311e8b1153b1076d18f0251943f6` is the revision these paths and observations refer to.
