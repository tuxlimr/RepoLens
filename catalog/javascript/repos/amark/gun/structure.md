# Project structure: amark/gun

**Analysed commit:** `56278eb4a37c0b2ad543e15678fc39d2eeb974a2`

**Commit reference:** [56278eb4a37c0b2ad543e15678fc39d2eeb974a2](https://github.com/amark/gun/commit/56278eb4a37c0b2ad543e15678fc39d2eeb974a2)

**Tree at this commit:** [amark/gun@56278eb4a37c](https://github.com/amark/gun/tree/56278eb4a37c0b2ad543e15678fc39d2eeb974a2)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | amark/gun |
| Description | An open source cybersecurity protocol for syncing decentralized graph data. |
| Stars | 19159 |
| Forks | 1245 |
| Licence | Other |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `56278eb4a37c0b2ad543e15678fc39d2eeb974a2` |
| Retrieved at | 2026-11-14T19:11:18.229764+00:00 |
| Files in this snapshot | 568 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (1 files)
    ci.yml
  FUNDING.yml
examples/  (184 files)
  angular/  (31 files)
    e2e/  (3 files)
      … 3 files under this directory
    src/  (18 files)
      … 18 files under this directory
    .angular-cli.json
    .editorconfig
    .gitignore
    README.md
    example_package.json
    karma.conf.js
    protractor.conf.js
    server.js
    tsconfig.json
    tslint.json
  basic/  (15 files)
    chat.html
    emoji.html
    meet.html
    note.html
    paste.html
    poll.html
    post.html
    private.html
    schedule.html
    screen.html
    stream.html
    tables.html
    upload.html
    user.html
    video.html
  chat/  (2 files)
    index.html
    user.html
  contact/  (1 files)
    index.html
  game/  (4 files)
    furball.html
    nts.html
    space.html
    win.html
  infinite-scroll/  (4 files)
    ScrollWindow.js
    index.html
    index.js
    style.css
  json/  (1 files)
    index.html
  move/  (1 files)
    index.html
  react/  (11 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (8 files)
      … 8 files under this directory
    README.md
    todo.html
  react-native/  (60 files)
    android/  (17 files)
      … 17 files under this directory
    ios/  (12 files)
      … 12 files under this directory
    src/  (20 files)
      … 20 files under this directory
    .babelrc
    .buckconfig
    .flowconfig
    .gitattributes
    .gitignore
    .watchmanconfig
    README.md
    app.json
    index.js
    package.json
    shim.js
  relay-sqlite-example/  (22 files)
    src/  (15 files)
      … 15 files under this directory
    README.md
    capacitor.config.ts
    index.html
    package.json
    tsconfig.json
    tsconfig.node.json
    vite.config.ts
  todo/  (1 files)
    index.html
  vanilla/  (4 files)
    screen.html
    todo.html
    user.html
    video.html
  vue/  (2 files)
    index.html
    todo.html
  webpack/  (5 files)
    src/  (2 files)
      … 2 files under this directory
    .gitignore
    package.json
    webpack.config.js
  where/  (1 files)
    index.html
  .gitignore
  Main.js
  axe.html
  docs.html
  express.js
  hapi.js
  http.js
  https.sh
  index.html
  install.sh
  jquery.js
  party.html
  relay.service
  reliable-network-read.html
  smoothie.js
  start.js.html
  stats.html
  style.css
  wave.html
hooks/  (1 files)
  post_push
kit/  (2 files)
  web.css
  web.js
lib/  (98 files)
  text-encoding/  (5 files)
    lib/  (1 files)
      … 1 files under this directory
    LICENSE.md
    README.md
    index.js
    package.json
  afore.js
  aws.js
  axe.js
  book.js
  bye.js
  crashed.js
  cryptomodules.js
  debug.js
  dom.js
  email.js
  erase.js
  evict.js
  file.js
  forget.js
  fork.js
  fsrm.js
  fun.js
  hot.js
  http.js
  hub.js
  ipfs.js
  ison.js
  jsonp.js
  later.d.ts
  … 69 more files
sea/  (26 files)
  aeskey.js
  array.js
  auth.js
  base64.js
  buffer.js
  certify.js
  create.js
  decrypt.js
  encrypt.js
  https.js
  index.js
  pair.js
  recall.js
  root.js
  sea.js
  secret.js
  settings.js
  sha1.js
  sha256.js
  share.js
  shim.js
  sign.js
  then.js
  user.js
  … 2 more files
src/  (21 files)
  polyfill/  (1 files)
    unbuild.js
  ask.js
  back.js
  book.js
  chain.js
  core.js
  dup.js
  get.js
  index.js
  localStorage.js
  map.js
  mesh.js
  on.js
  onto.js
  put.js
  root.js
  set.js
  shim.js
  state.js
  valid.js
  websocket.js
test/  (137 files)
  bug/  (6 files)
    121.js
    1243.js
    322.js
    686.js
    783.js
    axe-offline-retry.js
  debug/  (1 files)
    deep-set.html
  https/  (6 files)
    ca.crt
    ca.csr
    server.crt
    server.csr
    server.key.passphrase
    test.js
  hub/  (4 files)
    whatever/  (1 files)
      … 1 files under this directory
    .hubignore
    hub-test.js
    index.html
  normalize/  (1 files)
    normalize.html
  old/  (11 files)
    all.js
    interface.js
    performance.js
    s3pricing.html
    server.js
    set.js
    shoot.html
    shoot.js
    shotgun.js
    timelines.txt
    tmp.js
  panic/  (51 files)
    axe/  (9 files)
      … 9 files under this directory
    e2e/  (6 files)
      … 6 files under this directory
    infinite-scroll/  (2 files)
      … 2 files under this directory
    util/  (2 files)
      … 2 files under this directory
    1putackget.js
    2getget.js
    3puts.js
    4putackdedup.js
    b2s2s2b.js
    bulkimport.js
    chat-user.js
    chat.js
    curl-server.js
    holy-grail.js
    index.html
    large-nodes.js
    latency.js
    level.js
    lexical.js
    livestream.js
    load.js
    map-late-subscribe.js
    no-override.js
    on-recovery.js
    radisk.js
    radisk_split_failure.js
    s2s-all-delayed-peer-add.js
    s2s-all.js
    … 8 more files
  ptsd/  (12 files)
    benchmark.js
    memdisk.html
    memdisk.js
    memory.html
    perf.js
    ptsd.html
    ptsd.js
    radix.html
    radix.js
    spam.js
    stool.css
    streampipe.js
  rad/  (13 files)
    old2020json/  (2 files)
      … 2 files under this directory
    2020and2021.js
    bench.js
    book.html
    book.js
    browser.html
    crash.js
    mocha.html
    parse.rad
    rad.book.spec.js
    rad.js
    recover.js
  sea/  (5 files)
    nodeauth.js
    sea-tmp.html
    sea.html
    sea.js
    sea_old.js
  server/  (3 files)
    http.js
    node-client.js
    node-write.js
  tmp/  (11 files)
    mitra/  (2 files)
      … 2 files under this directory
    bigsync.js
    contact.html
    indexedDB.html
    radisk.html
    say.html
    seanode.js
    space.html
    time.html
    tmp.html
  abc.js
  download-log.html
  expect.js
  gun.html
  index.js
  json2.js
  mocha.css
  mocha.html
  panic.html
  radix.js
  trace.html
  trace.js
  wire.txt
types/  (70 files)
  gun/  (37 files)
    GunCallbackGet.d.ts
    GunCallbackMap.d.ts
    GunCallbackOn.d.ts
    GunCallbackOnce.d.ts
    GunCallbackPut.d.ts
    GunDataNode.d.ts
    GunHookCallbackBye.d.ts
    GunHookCallbackCreate.d.ts
    GunHookCallbackGet.d.ts
    GunHookCallbackHi.d.ts
    GunHookCallbackIn.d.ts
    GunHookCallbackOpt.d.ts
    GunHookCallbackOut.d.ts
    GunHookCallbackPut.d.ts
    GunNodeGet.d.ts
    GunNodePut.d.ts
    GunOptions.d.ts
    GunOptionsOn.d.ts
    GunOptionsOnce.d.ts
    GunOptionsPut.d.ts
    GunPeer.d.ts
    GunSchema.d.ts
    GunSoul.d.ts
    GunValueSimple.d.ts
    … 13 more files
  sea/  (16 files)
    GunCallbackUserAuth.d.ts
    GunCallbackUserCreate.d.ts
    GunHookCallbackAuth.d.ts
    GunUser.d.ts
    IGun.d.ts
    IGunInstance.d.ts
    IGunInstanceHookHandler.d.ts
    IGunInstanceRoot.d.ts
    IGunUserInstance.d.ts
    IPolicy.d.ts
    ISEA.d.ts
    ISEAPair.d.ts
    OptionsUserAuth.d.ts
    OptionsUserRecall.d.ts
    Policy.d.ts
    index.d.ts
  test/  (15 files)
    gun-back.test-d.ts
    gun-get.test-d.ts
    gun-instance.test-d.ts
    gun-map.test-d.ts
    gun-on.test-d.ts
    gun-once.test-d.ts
    gun-opt.test-d.ts
    gun-put.test-d.ts
    gun-set.test-d.ts
    gun-user-auth.test-d.ts
    gun-user-leave.test-d.ts
    gun-user-recall.test-d.ts
    gun-user.test-d.ts
    sea-certify.test-d.ts
    sea.test-d.ts
  index.d.ts
  utils.d.ts
.dockerignore
.gitignore
.npmignore
.prettierignore
.travis.yml
CHANGELOG.md
Dockerfile
LICENSE.md
Procfile
README.md
RELEASE.md
SECURITY.md
app.json
as.js
axe.js
bower.json
browser.js
gun.d.ts
gun.js
index.d.ts
index.js
nts.js
package.json
rad.js
… 3 more files
```

## Entry points

- [lib/text-encoding/index.js](https://github.com/amark/gun/blob/56278eb4a37c0b2ad543e15678fc39d2eeb974a2/lib/text-encoding/index.js)
- [index.js](https://github.com/amark/gun/blob/56278eb4a37c0b2ad543e15678fc39d2eeb974a2/index.js)
- [test/panic/e2e/distributed.js](https://github.com/amark/gun/blob/56278eb4a37c0b2ad543e15678fc39d2eeb974a2/test/panic/e2e/distributed.js)
- [lib/server.js](https://github.com/amark/gun/blob/56278eb4a37c0b2ad543e15678fc39d2eeb974a2/lib/server.js)
- [sea/index.js](https://github.com/amark/gun/blob/56278eb4a37c0b2ad543e15678fc39d2eeb974a2/sea/index.js)
- [src/index.js](https://github.com/amark/gun/blob/56278eb4a37c0b2ad543e15678fc39d2eeb974a2/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| ask.js package | library | Observed | Groups 1 file(s) under ask.js package (observed from repository paths and static analysis). |
| back.js package | library | Observed | Groups 1 file(s) under back.js package (observed from repository paths and static analysis). |
| book.js package | library | Observed | Groups 1 file(s) under book.js package (observed from repository paths and static analysis). |
| chain.js package | library | Observed | Groups 1 file(s) under chain.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 11 file(s) under core modules (observed from repository paths and static analysis). |
| core.js package | library | Observed | Groups 1 file(s) under core.js package (observed from repository paths and static analysis). |
| dup.js package | library | Observed | Groups 1 file(s) under dup.js package (observed from repository paths and static analysis). |
| get.js package | library | Observed | Groups 1 file(s) under get.js package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| kit package | library | Observed | Groups 1 file(s) under kit package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 95 file(s) under lib package (observed from repository paths and static analysis). |
| localStorage.js package | library | Observed | Groups 1 file(s) under localstorage.js package (observed from repository paths and static analysis). |
| map.js package | library | Observed | Groups 1 file(s) under map.js package (observed from repository paths and static analysis). |
| mesh.js package | library | Observed | Groups 1 file(s) under mesh.js package (observed from repository paths and static analysis). |
| on.js package | library | Observed | Groups 1 file(s) under on.js package (observed from repository paths and static analysis). |
| onto.js package | library | Observed | Groups 1 file(s) under onto.js package (observed from repository paths and static analysis). |
| polyfill package | library | Observed | Groups 1 file(s) under polyfill package (observed from repository paths and static analysis). |
| put.js package | library | Observed | Groups 1 file(s) under put.js package (observed from repository paths and static analysis). |
| root.js package | library | Observed | Groups 1 file(s) under root.js package (observed from repository paths and static analysis). |
| sea package | library | Observed | Groups 26 file(s) under sea package (observed from repository paths and static analysis). |
| set.js package | library | Observed | Groups 1 file(s) under set.js package (observed from repository paths and static analysis). |
| shim.js package | library | Observed | Groups 1 file(s) under shim.js package (observed from repository paths and static analysis). |
| state.js package | library | Observed | Groups 1 file(s) under state.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 152 file(s) under tests (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 55 file(s) under types package (observed from repository paths and static analysis). |
| valid.js package | library | Observed | Groups 1 file(s) under valid.js package (observed from repository paths and static analysis). |
| websocket.js package | library | Observed | Groups 1 file(s) under websocket.js package (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.github/FUNDING.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.travis.yml` (ci)
- `Dockerfile` (container)
- `app.json` (config)
- `bower.json` (config)
- `examples/angular/.angular-cli.json` (config)
- `examples/angular/.editorconfig` (config)
- `examples/angular/e2e/tsconfig.e2e.json` (config)
- `examples/angular/example_package.json` (config)
- `examples/angular/src/tsconfig.app.json` (config)
- `examples/angular/src/tsconfig.spec.json` (config)
- `examples/angular/tsconfig.json` (config)
- `examples/angular/tslint.json` (config)
- `examples/react-native/android/app/build.gradle` (manifest)
- `examples/react-native/android/build.gradle` (manifest)
- `examples/react-native/app.json` (config)
- `examples/react-native/ios/GunDemo/Images.xcassets/AppIcon.appiconset/Contents.json` (config)
- `examples/react-native/ios/GunDemo/Images.xcassets/Contents.json` (config)
- `examples/react-native/package.json` (manifest)
- `examples/relay-sqlite-example/package.json` (manifest)
- `examples/relay-sqlite-example/tsconfig.json` (config)
- `examples/relay-sqlite-example/tsconfig.node.json` (config)
- `examples/webpack/package.json` (manifest)
- `lib/text-encoding/package.json` (manifest)
- `package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `examples` — 184 analysed file(s)
- `test` — 137 analysed file(s)
- `lib` — 98 analysed file(s)
- `types` — 70 analysed file(s)
- `(root files)` — 27 analysed file(s)
- `sea` — 26 analysed file(s)
- `src` — 21 analysed file(s)
- `.github` — 2 analysed file(s)
- `kit` — 2 analysed file(s)
- `hooks` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 4 file(s) were skipped during inventory (2 x likely secret file excluded; 1 x lockfile excluded; 1 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `56278eb4a37c0b2ad543e15678fc39d2eeb974a2` is the revision these paths and observations refer to.
