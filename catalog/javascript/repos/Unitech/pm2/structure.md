# Project structure: Unitech/pm2

**Analysed commit:** `7a7fb4e22e9a26ec79c870ce8daafd2f78b648d1`

**Commit reference:** [7a7fb4e22e9a26ec79c870ce8daafd2f78b648d1](https://github.com/Unitech/pm2/commit/7a7fb4e22e9a26ec79c870ce8daafd2f78b648d1)

**Tree at this commit:** [Unitech/pm2@7a7fb4e22e9a](https://github.com/Unitech/pm2/tree/7a7fb4e22e9a26ec79c870ce8daafd2f78b648d1)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Unitech/pm2 |
| Description | Node.js/Typescript/Bun Production Process Manager with a built-in Load Balancer. |
| Stars | 43334 |
| Forks | 2730 |
| Licence | Other |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `7a7fb4e22e9a26ec79c870ce8daafd2f78b648d1` |
| Retrieved at | 2026-11-14T19:10:38.764286+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.github/  (5 files)
  workflows/  (2 files)
    docker-images.yml
    node.js.yml
  CONTRIBUTING.md
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
bin/  (5 files)
  pm2
  pm2-dev
  pm2-docker
  pm2-runtime
  pm2.ps1
examples/  (171 files)
  api-pm2/  (3 files)
    README.md
    api.js
    http.js
  c-compile/  (1 files)
    hello.c
  cluster-http/  (4 files)
    README.md
    ecosystem.config.js
    http-no-exit.js
    http.js
  cluster-tcp/  (4 files)
    README.md
    http.js
    process.config.js
    tcp.js
  custom-nodejs-version/  (2 files)
    ecosystem.config.js
    http.js
  docker-pm2/  (5 files)
    app/  (3 files)
      … 3 files under this directory
    Dockerfile
    README.md
  echo/  (2 files)
    log.js
    stdout.js
  ecosystem-file/  (7 files)
    apps/  (3 files)
      … 3 files under this directory
    README.md
    process.config.js
    process.json
    process.yml
  esm/  (3 files)
    addTwo.js
    app.js
    package.json
  exception/  (2 files)
    fast.js
    slow.js
  expose-custom-metrics/  (3 files)
    README.md
    process-metrics.js
    process.config.js
  expose-triggerable-functions/  (4 files)
    index.js
    process.yml
    trigger-param.js
    trigger-ping.js
  import/  (3 files)
    circle.js
    index.js
    package.json
  interact-via-stdin/  (2 files)
    README.md
    stdin.js
  misc-examples/  (64 files)
    apps/  (11 files)
      … 11 files under this directory
    001-test.js
    args.js
    auto-restart-all.js
    auto-restart-threshold.js
    auto-save.js
    beforeExit.js
    child-echo.json
    child-env.js
    child-pm2.json
    child.js
    child.js-pm2.json
    child2.js
    client.js
    cwd.js
    echo.coffee
    echo.js
    echokill.js
    env.js
    env_args.js
    exec_watch.json
    exit.js
    expose_method.js
    graceful-exit.js
    harmony.js
    … 29 more files
  module-extra-meta/  (2 files)
    index.js
    package.json
  module-test/  (3 files)
    README.md
    app.js
    package.json
  npm-start/  (2 files)
    http.js
    package.json
  pmx-test-all/  (13 files)
    elements/  (12 files)
      … 12 files under this directory
    process.config.js
  run-php-python-ruby-bash/  (6 files)
    bashscript.sh
    echo.php
    echo.py
    echo.rb
    leak-mem.py
    process.yml
  send-msg/  (3 files)
    pm2-app.js
    pm2-msg.js
    t2.js
  signal-catching/  (1 files)
    graceful-http.js
  sourcemap-auto-resolve/  (3 files)
    API.js
    README.md
    process.config.js
  start-a-binary/  (1 files)
    ls.yml
  test-all-keymetrics-features/  (15 files)
    README.md
    actions-fibonacci.js
    custom_action.js
    custom_action_with_params.js
    event.js
    http_app.js
    http_transaction.js
    pm2_probe.js
    probes.js
    process-load.config.js
    process-transpose.js
    process.config.js
    scoped-actions.js
    test-threshold.js
    throw.js
  treekill/  (2 files)
    app.js
    process.json
  udp/  (2 files)
    client.js
    server.js
  using-pm2-and-transpilers/  (6 files)
    README.md
    echo.coffee
    echo.ls
    echo.ts
    http.ts
    node.d.ts
  wait-ready/  (3 files)
    app.js
    ecosystem.json
    http-simple.js
lib/  (116 files)
  API/  (34 files)
    ExtraMgmt/  (1 files)
      … 1 files under this directory
    Modules/  (6 files)
      … 6 files under this directory
    UX/  (5 files)
      … 5 files under this directory
    pm2-plus/  (9 files)
      … 9 files under this directory
    Configuration.js
    Containerizer.js
    Dashboard.js
    Deploy.js
    Extra.js
    Log.js
    LogManagement.js
    Monit.js
    Serve.js
    Startup.js
    Version.js
    interpreter.json
    schema.json
  God/  (6 files)
    ActionMethods.js
    ClusterMode.js
    ForkMode.js
    Methods.js
    Reload.js
    StdioLogger.js
  binaries/  (4 files)
    CLI.js
    DevCLI.js
    Runtime.js
    Runtime4Docker.js
  templates/  (27 files)
    Dockerfiles/  (1 files)
      … 1 files under this directory
    init-scripts/  (9 files)
      … 9 files under this directory
    logrotate.d/  (1 files)
      … 1 files under this directory
    sample-apps/  (12 files)
      … 12 files under this directory
    ecosystem-es.tpl
    ecosystem-simple-es.tpl
    ecosystem-simple.tpl
    ecosystem.tpl
  tools/  (23 files)
    multimeter/  (4 files)
      … 4 files under this directory
    Config.js
    SysMetrics.js
    copydirSync.js
    deleteFolderRecursive.js
    find-package-json.js
    fmt.js
    interpreter.js
    isbinaryfile.js
    json5.js
    open.js
    passwd.js
    pm2-config-keys.js
    prompt.js
    serviceStop.js
    sexec.js
    treeify.js
    typestrip.js
    which.js
    xdg-open
  API.js
  Client.js
  Common.js
  Configuration.js
  Daemon.js
  Event.js
  God.js
  HttpInterface.js
  OtelManager.js
  ProcessContainer.js
  ProcessContainerBun.js
  ProcessContainerFork.js
  ProcessContainerForkBun.js
  ProcessUtils.js
  TreeKill.js
  Utility.js
  VersionCheck.js
  Watcher.js
  Worker.js
  completion.js
  completion.sh
  motd
modules/  (232 files)
  blessed/  (24 files)
    lib/  (20 files)
      … 20 files under this directory
    usr/  (1 files)
      … 1 files under this directory
    LICENSE
    README.md
    index.js
  chokidar/  (7 files)
    lib/  (4 files)
      … 4 files under this directory
    LICENSE
    VENDORED.md
    index.js
  pm2-axon/  (64 files)
    lib/  (19 files)
      … 19 files under this directory
    test/  (44 files)
      … 44 files under this directory
    index.js
  pm2-axon-rpc/  (5 files)
    lib/  (2 files)
      … 2 files under this directory
    test/  (2 files)
      … 2 files under this directory
    index.js
  pm2-io-agent/  (40 files)
    src/  (17 files)
      … 17 files under this directory
    test/  (18 files)
      … 18 files under this directory
    LICENSE
    README.md
    config.js
    constants.js
    index.js
  pm2-io-bpm/  (86 files)
    features/  (6 files)
      … 6 files under this directory
    metrics/  (5 files)
      … 5 files under this directory
    otel/  (8 files)
      … 8 files under this directory
    profilers/  (2 files)
      … 2 files under this directory
    services/  (5 files)
      … 5 files under this directory
    test/  (39 files)
      … 39 files under this directory
    transports/  (1 files)
      … 1 files under this directory
    utils/  (14 files)
      … 14 files under this directory
    configuration.js
    constants.js
    featureManager.js
    index.js
    pmx.js
    serviceManager.js
  vizion/  (5 files)
    lib/  (2 files)
      … 2 files under this directory
    LICENSE
    README.md
    index.js
  fclone.js
packager/  (17 files)
  alpine/  (2 files)
    pm2/  (1 files)
      … 1 files under this directory
    pm2_io.rsa.pub
  debian/  (7 files)
    control
    copyright
    description
    lintian-overrides
    postinst
    postrm
    prerm
  rhel/  (3 files)
    postinst
    postrm
    prerm
  build-deb-rpm.sh
  build-dist.sh
  publish_deb_rpm.sh
  setup.deb.sh
  setup.rpm.sh
pres/  (1 files)
  TMP.md
test/  (237 files)
  benchmarks/  (3 files)
    monit-daemon.sh
    monit.sh
    result.monit
  e2e/  (79 files)
    binaries/  (2 files)
      … 2 files under this directory
    cli/  (31 files)
      … 31 files under this directory
    internals/  (11 files)
      … 11 files under this directory
    logs/  (11 files)
      … 11 files under this directory
    misc/  (9 files)
      … 9 files under this directory
    modules/  (3 files)
      … 3 files under this directory
    process-file/  (7 files)
      … 7 files under this directory
    docker.sh
    esmodule.sh
    file-descriptor.sh
    include.sh
    pull.sh
  fixtures/  (151 files)
    app-config-update/  (3 files)
      … 3 files under this directory
    args/  (2 files)
      … 2 files under this directory
    c-compile/  (1 files)
      … 1 files under this directory
    cluster/  (1 files)
      … 1 files under this directory
    containerizer/  (2 files)
      … 2 files under this directory
    custom_actions/  (1 files)
      … 1 files under this directory
    docker/  (5 files)
      … 5 files under this directory
    ecosystem/  (1 files)
      … 1 files under this directory
    env-switching/  (2 files)
      … 2 files under this directory
    esmodules/  (5 files)
      … 5 files under this directory
    events/  (3 files)
      … 3 files under this directory
    extra-lang/  (4 files)
      … 4 files under this directory
    git/  (20 files)
      … 20 files under this directory
    homogen-json-action/  (2 files)
      … 2 files under this directory
    increment-var/  (2 files)
      … 2 files under this directory
    inside/  (5 files)
      … 5 files under this directory
    interface/  (7 files)
      … 7 files under this directory
    interpreter/  (5 files)
      … 5 files under this directory
    js-configuration/  (2 files)
      … 2 files under this directory
    json-reload/  (6 files)
      … 6 files under this directory
    listen-timeout/  (1 files)
      … 1 files under this directory
    log-create-not-exist-dir/  (1 files)
      … 1 files under this directory
    log-json/  (2 files)
      … 2 files under this directory
    log-namespace/  (1 files)
      … 1 files under this directory
    mjs/  (4 files)
      … 4 files under this directory
    module-fixture/  (2 files)
      … 2 files under this directory
    001-test.js
    all.json
    all2.json
    append-env-to-name.json
    args.js
    bashscript.sh
    big-array-es6.js
    big-array-listen.js
    big-array.js
    big-log-burst.js
    binary-js-file
    binary-js-file.js
    binary-py-file.py
    change_cwd.json
    child.js
    child_no_http.js
    cluster-alias.json
    cluster-atypical-node.config.js
    cluster-non-node.json
    cluster-pm2.json
    conf.json
    configuration.js
    configuration.json
    cron-stop.js
    … 37 more files
  Dockerfile
  README.md
  docker-parallel.sh
  e2e.sh
.editorconfig
.gitattributes
.gitignore
.mocharc.js
.npmignore
CHANGELOG.md
CONTRIBUTING.md
GNU-AGPL-3.0.txt
LICENSE
README.md
SECURITY.md
constants.js
index.js
package.json
paths.js
pm2
```

## Entry points

- [examples/esm/addTwo.js](https://github.com/Unitech/pm2/blob/7a7fb4e22e9a26ec79c870ce8daafd2f78b648d1/examples/esm/addTwo.js)
- [examples/import/index.js](https://github.com/Unitech/pm2/blob/7a7fb4e22e9a26ec79c870ce8daafd2f78b648d1/examples/import/index.js)
- [examples/module-extra-meta/index.js](https://github.com/Unitech/pm2/blob/7a7fb4e22e9a26ec79c870ce8daafd2f78b648d1/examples/module-extra-meta/index.js)
- [examples/module-test/app.js](https://github.com/Unitech/pm2/blob/7a7fb4e22e9a26ec79c870ce8daafd2f78b648d1/examples/module-test/app.js)
- [index.js](https://github.com/Unitech/pm2/blob/7a7fb4e22e9a26ec79c870ce8daafd2f78b648d1/index.js)
- [bin/pm2](https://github.com/Unitech/pm2/blob/7a7fb4e22e9a26ec79c870ce8daafd2f78b648d1/bin/pm2)
- [bin/pm2-dev](https://github.com/Unitech/pm2/blob/7a7fb4e22e9a26ec79c870ce8daafd2f78b648d1/bin/pm2-dev)
- [bin/pm2-docker](https://github.com/Unitech/pm2/blob/7a7fb4e22e9a26ec79c870ce8daafd2f78b648d1/bin/pm2-docker)
- [bin/pm2-runtime](https://github.com/Unitech/pm2/blob/7a7fb4e22e9a26ec79c870ce8daafd2f78b648d1/bin/pm2-runtime)
- [test/fixtures/esmodules/packagemodule/index.js](https://github.com/Unitech/pm2/blob/7a7fb4e22e9a26ec79c870ce8daafd2f78b648d1/test/fixtures/esmodules/packagemodule/index.js)
- [test/fixtures/mjs/index.mjs](https://github.com/Unitech/pm2/blob/7a7fb4e22e9a26ec79c870ce8daafd2f78b648d1/test/fixtures/mjs/index.mjs)
- [test/fixtures/module-fixture/scoped-action.js](https://github.com/Unitech/pm2/blob/7a7fb4e22e9a26ec79c870ce8daafd2f78b648d1/test/fixtures/module-fixture/scoped-action.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 29 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 12 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Inferred | Groups 0 file(s) under data layer (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 60 file(s) under lib package (observed from repository paths and static analysis). |
| modules package | library | Observed | Groups 111 file(s) under modules package (observed from repository paths and static analysis). |
| packager package | library | Observed | Groups 5 file(s) under packager package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 5 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 336 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/workflows/docker-images.yml` (ci)
- `.github/workflows/node.js.yml` (ci)
- `examples/docker-pm2/Dockerfile` (container)
- `examples/docker-pm2/app/package.json` (manifest)
- `examples/ecosystem-file/process.json` (config)
- `examples/ecosystem-file/process.yml` (config)
- `examples/esm/package.json` (manifest)
- `examples/expose-triggerable-functions/process.yml` (config)
- `examples/import/package.json` (manifest)
- `examples/misc-examples/apps/all-pm2.json` (config)
- `examples/misc-examples/apps/args.json` (config)
- `examples/misc-examples/apps/auto-kill-echo.json` (config)
- `examples/misc-examples/apps/cluster-pm2.json` (config)
- `examples/misc-examples/apps/cron-pm2.json` (config)
- `examples/misc-examples/apps/default-path-echo.json` (config)
- `examples/misc-examples/apps/echo-pm2.json` (config)
- `examples/misc-examples/apps/env-pm2.json` (config)
- `examples/misc-examples/apps/killfast.json` (config)
- `examples/misc-examples/apps/multi-pm2.json` (config)
- `examples/misc-examples/apps/no-name-echo.json` (config)
- `examples/misc-examples/child-echo.json` (config)
- `examples/misc-examples/child-pm2.json` (config)
- `examples/misc-examples/child.js-pm2.json` (config)
- `examples/misc-examples/exec_watch.json` (config)
- `examples/misc-examples/inside.json` (config)
- `examples/misc-examples/malformated.json` (config)
- `examples/misc-examples/package.json` (manifest)
- `examples/misc-examples/process.json` (config)
- `examples/module-extra-meta/package.json` (manifest)
- `examples/module-test/package.json` (manifest)
- `examples/npm-start/package.json` (manifest)
- `examples/run-php-python-ruby-bash/process.yml` (config)
- `examples/start-a-binary/ls.yml` (config)
- `examples/treekill/process.json` (config)
- `examples/wait-ready/ecosystem.json` (config)
- `lib/API/interpreter.json` (config)
- `lib/API/schema.json` (config)
- `lib/templates/Dockerfiles/Dockerfile-nodejs.tpl` (container)
- `lib/templates/sample-apps/http-server/package.json` (manifest)
- `lib/templates/sample-apps/pm2-plus-metrics-actions/package.json` (manifest)
- `lib/templates/sample-apps/python-app/package.json` (manifest)
- `modules/pm2-axon/lib/configurable/package.json` (manifest)
- `package.json` (manifest)
- `test/Dockerfile` (container)
- `test/fixtures/containerizer/Dockerfile.dev` (container)
- `test/fixtures/containerizer/Dockerfile.prod` (container)
- `test/fixtures/docker/expressor/Dockerfile.bak` (container)

## Top-level layout

- `test` — 237 analysed file(s)
- `modules` — 232 analysed file(s)
- `examples` — 171 analysed file(s)
- `lib` — 116 analysed file(s)
- `packager` — 17 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `.github` — 5 analysed file(s)
- `bin` — 5 analysed file(s)
- `pres` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- File test/fixtures/binary-py-file.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `7a7fb4e22e9a26ec79c870ce8daafd2f78b648d1` is the revision these paths and observations refer to.
