# Project structure: BrowserSync/browser-sync

**Analysed commit:** `dc74bc0a6bcbe70eea5f2f94b524b2902436efb1`

**Commit reference:** [dc74bc0a6bcbe70eea5f2f94b524b2902436efb1](https://github.com/BrowserSync/browser-sync/commit/dc74bc0a6bcbe70eea5f2f94b524b2902436efb1)

**Tree at this commit:** [BrowserSync/browser-sync@dc74bc0a6bcb](https://github.com/BrowserSync/browser-sync/tree/dc74bc0a6bcbe70eea5f2f94b524b2902436efb1)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | BrowserSync/browser-sync |
| Description | Keep multiple browsers & devices in sync when building websites. https://browsersync.io |
| Stars | 12288 |
| Forks | 745 |
| Licence | Apache-2.0 |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `dc74bc0a6bcbe70eea5f2f94b524b2902436efb1` |
| Retrieved at | 2026-11-14T19:12:06.899746+00:00 |
| Files in this snapshot | 720 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    main.yml
examples/  (32 files)
  basic/  (1 files)
    run.js
  snippet/  (2 files)
    index.html
    run.js
  404.js
  callback.js
  express.js
  less.js
  middleware.css.injection.js
  notify-styles.js
  options.snippetOptions.js
  proxy.gzip.js
  proxy.headers.js
  proxy.localhost.js
  proxy.middleware.js
  proxy.middleware.multi.js
  proxy.proxyRes.js
  proxy.rewriteRules.advanced.js
  proxy.rewriteRules.simple.js
  proxy.secure.js
  proxy.vhost.js
  server.basedir.js
  server.basedir.mulitple.js
  server.default.js
  server.gzip.js
  server.http2.js
  server.latency.js
  server.middleware.js
  … 5 more files
packages/  (669 files)
  browser-sync/  (306 files)
    certs/  (3 files)
      … 3 files under this directory
    cli-options/  (4 files)
      … 4 files under this directory
    lib/  (58 files)
      … 58 files under this directory
    templates/  (4 files)
      … 4 files under this directory
    test/  (232 files)
      … 232 files under this directory
    .gitignore
    .prettierignore
    package.json
    readme.md
    tsconfig.json
  browser-sync-client/  (86 files)
    lib/  (42 files)
      … 42 files under this directory
    test/  (36 files)
      … 36 files under this directory
    .gitignore
    .travis.yml
    LICENSE-MIT
    README.md
    index.js
    package.json
    tsconfig.json
    webpack.config.js
  browser-sync-ui/  (277 files)
    lib/  (66 files)
      … 66 files under this directory
    public/  (9 files)
      … 9 files under this directory
    src/  (124 files)
      … 124 files under this directory
    static/  (12 files)
      … 12 files under this directory
    tasks/  (2 files)
      … 2 files under this directory
    templates/  (6 files)
      … 6 files under this directory
    test/  (48 files)
      … 48 files under this directory
    .editorconfig
    .gitignore
    .jshintrc
    LICENSE
    README.md
    crossbow.yaml
    example.stream.js
    index.js
    package.json
    webpack.config.js
tests/  (5 files)
  examples/  (4 files)
    basic/  (1 files)
      … 1 files under this directory
    html-inject/  (1 files)
      … 1 files under this directory
    snippet/  (1 files)
      … 1 files under this directory
    tailwind/  (1 files)
      … 1 files under this directory
  utils.ts
.editorconfig
.gitattributes
.gitignore
.travis.yml
CONTRIBUTING.md
ISSUE_TEMPLATE.md
LICENSE
README.md
changelog.js
lerna.json
nx.json
package.json
playwright.config.ts
```

## Entry points

- [packages/browser-sync-client/index.js](https://github.com/BrowserSync/browser-sync/blob/dc74bc0a6bcbe70eea5f2f94b524b2902436efb1/packages/browser-sync-client/index.js)
- [packages/browser-sync-ui/test/fixtures/plugin-multi-templates/index.plugin.js](https://github.com/BrowserSync/browser-sync/blob/dc74bc0a6bcbe70eea5f2f94b524b2902436efb1/packages/browser-sync-ui/test/fixtures/plugin-multi-templates/index.plugin.js)
- [packages/browser-sync-ui/test/fixtures/plugin-noui/index.plugin.js](https://github.com/BrowserSync/browser-sync/blob/dc74bc0a6bcbe70eea5f2f94b524b2902436efb1/packages/browser-sync-ui/test/fixtures/plugin-noui/index.plugin.js)
- [packages/browser-sync-ui/test/fixtures/plugin/index.plugin.js](https://github.com/BrowserSync/browser-sync/blob/dc74bc0a6bcbe70eea5f2f94b524b2902436efb1/packages/browser-sync-ui/test/fixtures/plugin/index.plugin.js)
- [packages/browser-sync-client/lib/index.ts](https://github.com/BrowserSync/browser-sync/blob/dc74bc0a6bcbe70eea5f2f94b524b2902436efb1/packages/browser-sync-client/lib/index.ts)
- [packages/browser-sync-ui/index.js](https://github.com/BrowserSync/browser-sync/blob/dc74bc0a6bcbe70eea5f2f94b524b2902436efb1/packages/browser-sync-ui/index.js)
- [packages/browser-sync-ui/lib/server.js](https://github.com/BrowserSync/browser-sync/blob/dc74bc0a6bcbe70eea5f2f94b524b2902436efb1/packages/browser-sync-ui/lib/server.js)
- [packages/browser-sync/lib/index.js](https://github.com/BrowserSync/browser-sync/blob/dc74bc0a6bcbe70eea5f2f94b524b2902436efb1/packages/browser-sync/lib/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 16 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 171 file(s) under packages package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 2 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 321 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/workflows/main.yml` (ci)
- `.travis.yml` (ci)
- `lerna.json` (config)
- `nx.json` (config)
- `package.json` (manifest)
- `packages/browser-sync-client/.travis.yml` (ci)
- `packages/browser-sync-client/package.json` (manifest)
- `packages/browser-sync-client/tsconfig.json` (config)
- `packages/browser-sync-ui/.editorconfig` (config)
- `packages/browser-sync-ui/crossbow.yaml` (config)
- `packages/browser-sync-ui/package.json` (manifest)
- `packages/browser-sync-ui/src/crossbow/_config.yml` (config)
- `packages/browser-sync/cli-options/opts.init.json` (config)
- `packages/browser-sync/cli-options/opts.recipe.json` (config)
- `packages/browser-sync/cli-options/opts.reload.json` (config)
- `packages/browser-sync/cli-options/opts.start.json` (config)
- `packages/browser-sync/package.json` (manifest)
- `packages/browser-sync/tsconfig.json` (config)

## Top-level layout

- `packages` — 669 analysed file(s)
- `examples` — 32 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `tests` — 5 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 9 file(s) were skipped during inventory (2 x generated/minified file excluded; 1 x likely secret file excluded; 1 x lockfile excluded; 5 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `dc74bc0a6bcbe70eea5f2f94b524b2902436efb1` is the revision these paths and observations refer to.
