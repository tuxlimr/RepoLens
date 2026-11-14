# Project structure: remy/nodemon

**Analysed commit:** `df00a4e463547383a4c1c5eaab280f395d439c23`

**Commit reference:** [df00a4e463547383a4c1c5eaab280f395d439c23](https://github.com/remy/nodemon/commit/df00a4e463547383a4c1c5eaab280f395d439c23)

**Tree at this commit:** [remy/nodemon@df00a4e46354](https://github.com/remy/nodemon/tree/df00a4e463547383a4c1c5eaab280f395d439c23)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | remy/nodemon |
| Description | Monitor for any changes in your node.js application and automatically restart the server - perfect for development |
| Stars | 26664 |
| Forks | 1737 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `df00a4e463547383a4c1c5eaab280f395d439c23` |
| Retrieved at | 2026-11-14T19:10:54.918249+00:00 |
| Files in this snapshot | 162 |

## Directory tree

```text
.github/  (11 files)
  ISSUE_TEMPLATE/  (1 files)
    bug_report.md
  workflows/  (5 files)
    commits.yml
    node.js.yml
    release.yml
    stale.yml
    website.yml
  CONTRIBUTING.md
  FUNDING.yml
  ISSUE_TEMPLATE.md
  no-response.yml
  oliver.yml
bin/  (1 files)
  nodemon.js
doc/  (14 files)
  cli/  (8 files)
    authors.txt
    config.txt
    help.txt
    logo.txt
    options.txt
    topics.txt
    usage.txt
    whoami.txt
  arch.md
  events.md
  option-parsing-logic.md
  requireable.md
  rules.md
  sample-nodemon.md
lib/  (26 files)
  cli/  (2 files)
    index.js
    parse.js
  config/  (5 files)
    command.js
    defaults.js
    exec.js
    index.js
    load.js
  help/  (1 files)
    index.js
  monitor/  (5 files)
    index.js
    match.js
    run.js
    signals.js
    watch.js
  rules/  (3 files)
    add.js
    index.js
    parse.js
  utils/  (6 files)
    bus.js
    clone.js
    colour.js
    index.js
    log.js
    merge.js
  index.js
  nodemon.js
  spawn.js
  version.js
test/  (87 files)
  cli/  (2 files)
    exec.test.js
    parse.test.js
  config/  (3 files)
    env.test.js
    load-logging.test.js
    load.test.js
  events/  (2 files)
    complete.test.js
    scripts.test.js
  fixtures/  (55 files)
    .dotfolder/  (3 files)
      … 3 files under this directory
    1246/  (2 files)
      … 2 files under this directory
    configs/  (5 files)
      … 5 files under this directory
    events/  (2 files)
      … 2 files under this directory
    global/  (1 files)
      … 1 files under this directory
    legacy/  (1 files)
      … 1 files under this directory
    packages/  (15 files)
      … 15 files under this directory
    super-legacy/  (1 files)
      … 1 files under this directory
    watch-count/  (6 files)
      … 6 files under this directory
    .dotfile
    app with spaces.js
    app.coffee
    app.js
    comments
    default
    default.json
    env.js
    hello.ls
    hello.py
    help.txt
    log.coffee
    nodemon.json
    package.json
    regexp
    repl.js
    sigint.js
    simple
    simple.json
  fork/  (5 files)
    change-detect.test.js
    config.test.js
    run-mac-only.test.js
    run.test.js
    watch-restart.test.js
  help/  (1 files)
    help.test.js
  lib/  (3 files)
    events.test.js
    require-restartable.test.js
    require.test.js
  misc/  (2 files)
    listeners.test.js
    sigint.test.js
  monitor/  (6 files)
    count.test.js
    ignore.test.js
    match.test.js
    run.test.js
    watch-restart.test.js
    watch.test.js
  rules/  (1 files)
    index.test.js
  utils/  (4 files)
    colour.test.js
    log.test.js
    merge.test.js
    stringify.test.js
  docker.sh
  mocha.opts
  utils.js
website/  (6 files)
  index.html
  nodemon.svg
  oc.jq
  oc.js
  sparkpost.svg
  style.css
.eslintrc.json
.gitignore
.jshintrc
.npmignore
.prettierrc.json
.releaserc
.travis.yml
CODE_OF_CONDUCT.md
Dockerfile
LICENSE
README.md
TODO.md
commitlint.config.js
faq.md
index.d.ts
jsconfig.json
package.json
```

## Entry points

- [bin/nodemon.js](https://github.com/remy/nodemon/blob/df00a4e463547383a4c1c5eaab280f395d439c23/bin/nodemon.js)
- [test/fixtures/app.js](https://github.com/remy/nodemon/blob/df00a4e463547383a4c1c5eaab280f395d439c23/test/fixtures/app.js)
- [test/fixtures/packages/main-and-index/server.js](https://github.com/remy/nodemon/blob/df00a4e463547383a4c1c5eaab280f395d439c23/test/fixtures/packages/main-and-index/server.js)
- [test/fixtures/packages/main-and-start/index.js](https://github.com/remy/nodemon/blob/df00a4e463547383a4c1c5eaab280f395d439c23/test/fixtures/packages/main-and-start/index.js)
- [lib/cli/index.js](https://github.com/remy/nodemon/blob/df00a4e463547383a4c1c5eaab280f395d439c23/lib/cli/index.js)
- [lib/config/index.js](https://github.com/remy/nodemon/blob/df00a4e463547383a4c1c5eaab280f395d439c23/lib/config/index.js)
- [lib/help/index.js](https://github.com/remy/nodemon/blob/df00a4e463547383a4c1c5eaab280f395d439c23/lib/help/index.js)
- [lib/index.js](https://github.com/remy/nodemon/blob/df00a4e463547383a4c1c5eaab280f395d439c23/lib/index.js)
- [lib/monitor/index.js](https://github.com/remy/nodemon/blob/df00a4e463547383a4c1c5eaab280f395d439c23/lib/monitor/index.js)
- [lib/rules/index.js](https://github.com/remy/nodemon/blob/df00a4e463547383a4c1c5eaab280f395d439c23/lib/rules/index.js)
- [lib/utils/index.js](https://github.com/remy/nodemon/blob/df00a4e463547383a4c1c5eaab280f395d439c23/lib/utils/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bin package | library | Observed | Groups 1 file(s) under bin package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 8 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 21 file(s) under lib package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 87 file(s) under tests (observed from repository paths and static analysis). |
| website package | library | Observed | Groups 1 file(s) under website package (observed from repository paths and static analysis). |

## Important files

- `.eslintrc.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/no-response.yml` (config)
- `.github/oliver.yml` (config)
- `.github/workflows/commits.yml` (ci)
- `.github/workflows/node.js.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/stale.yml` (ci)
- `.github/workflows/website.yml` (ci)
- `.prettierrc.json` (config)
- `.travis.yml` (ci)
- `Dockerfile` (container)
- `jsconfig.json` (config)
- `package.json` (manifest)

## Top-level layout

- `test` — 87 analysed file(s)
- `lib` — 26 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `doc` — 14 analysed file(s)
- `.github` — 11 analysed file(s)
- `website` — 6 analysed file(s)
- `bin` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 244 file(s) were skipped during inventory (1 x likely secret file excluded; 243 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `df00a4e463547383a4c1c5eaab280f395d439c23` is the revision these paths and observations refer to.
