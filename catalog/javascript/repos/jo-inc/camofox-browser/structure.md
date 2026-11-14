# Project structure: jo-inc/camofox-browser

**Analysed commit:** `31376c27db94204ffdc635ae71a7f61328e91a5e`

**Commit reference:** [31376c27db94204ffdc635ae71a7f61328e91a5e](https://github.com/jo-inc/camofox-browser/commit/31376c27db94204ffdc635ae71a7f61328e91a5e)

**Tree at this commit:** [jo-inc/camofox-browser@31376c27db94](https://github.com/jo-inc/camofox-browser/tree/31376c27db94204ffdc635ae71a7f61328e91a5e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | jo-inc/camofox-browser |
| Description | Stealth headless browser for AI agents — bypass Cloudflare, bot detection, and anti-scraping. Drop-in Puppeteer/Playwright replacement. |
| Stars | 12279 |
| Forks | 1234 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `31376c27db94204ffdc635ae71a7f61328e91a5e` |
| Retrieved at | 2026-11-14T19:12:06.821175+00:00 |
| Files in this snapshot | 259 |

## Directory tree

```text
.github/  (10 files)
  workflows/  (8 files)
    agenthook-notify.yml
    auto-close-old-reports.yml
    ci.yml
    clawhub-publish.yml
    docker.yml
    mirror-camoufox.yml
    publish.yml
    telemetry-deploy.yml
  CODEOWNERS
  FUNDING.yml
bin/  (1 files)
  camofox-browser.js
changelog/  (1 files)
  1.4.0.md
docs/  (2 files)
  api.html
  openapi.json
lib/  (49 files)
  aria-annotate.js
  auth.js
  browser-errors.js
  browser-identity.js
  browser-key.js
  browser-processes.js
  camoufox-download.js
  camoufox-executable.js
  config.js
  cookies.js
  downloads.js
  extract.js
  fingerprint-os.js
  fly.js
  google-serp.js
  health-probe.js
  images.js
  inflight.js
  interaction-params.js
  interactive-roles.js
  launcher.js
  macros.js
  mcp-tool-contracts.mjs
  metrics.js
  … 25 more files
mcp/  (6 files)
  lib/  (3 files)
    config.mjs
    cookies.mjs
    tool-contracts.mjs
  README.md
  package.json
  server.mjs
plugins/  (24 files)
  persistence/  (5 files)
    AGENTS.md
    README.md
    index.js
    persistence.test.js
    plugin.test.js
  vnc/  (12 files)
    AGENTS.md
    README.md
    apt.txt
    index.js
    plugin.json
    spawn.js
    vnc-launcher.js
    vnc-launcher.test.js
    vnc-watcher-lib.sh
    vnc-watcher.sh
    vnc-watcher.test.js
    vnc.test.js
  youtube/  (7 files)
    AGENTS.md
    apt.txt
    index.js
    post-install.sh
    post-install.test.js
    youtube.js
    youtube.test.js
scripts/  (13 files)
  lib/  (1 files)
    npm-command.mjs
  exec.js
  generate-openapi.js
  install-plugin-deps.sh
  mcp-call.mjs
  mcp-run.mjs
  plugin.js
  plugin.test.js
  postinstall.js
  postinstall.test.js
  sync-version.js
  test-mcp-package.mjs
  test-mcp.mjs
tests/  (122 files)
  e2e/  (21 files)
    clickRefs.test.js
    concurrency.test.js
    downloadsImages.test.js
    drag.test.js
    evaluateNavigationRace.test.js
    formSubmission.test.js
    globalSetup.js
    globalTeardown.js
    macroNavigation.test.js
    navigation.test.js
    screenshot.test.js
    scroll.test.js
    sharedEnv.js
    snapshot-truncation.test.js
    snapshotLinks.test.js
    snapshotScreenshot.test.js
    tabCreateCleanup.test.js
    tabLifecycle.test.js
    typingEnter.test.js
    upload.test.js
    viewport.test.js
  helpers/  (4 files)
    client.js
    startServer.js
    test-env.js
    testSite.js
  live/  (3 files)
    amazonProductPrices.test.js
    googleSearch.test.js
    macroExpansion.test.js
  unit/  (93 files)
    accessKey.test.js
    amazonSearchNavigation.test.js
    ariaAnnotate.test.js
    auth.test.js
    autoCloseOldReports.test.js
    autoCookieImport.test.js
    browserErrors.test.js
    browserIdentity.test.js
    browserKey.test.js
    browserProcesses.test.js
    browserRestart410.test.js
    browserRestartWindow.test.js
    camoufoxDownload.test.js
    camoufoxExecutable.test.js
    camoufoxVersionConsistency.test.js
    clickBoundingBoxTimeout.test.js
    clientRetry.test.js
    config.test.js
    consentDismissal.test.js
    cookies.test.js
    crashRelay.test.js
    crashRelayWorker.test.js
    downloads.test.js
    dragEndpoint.test.js
    … 69 more files
  vnc-linux-smoke.sh
tools/  (6 files)
  windows-utm/  (6 files)
    .gitignore
    README.md
    build-fat-bootstrap.py
    build-installer-autoboot-iso.sh
    build-provisioning-iso.sh
    create-vm.sh
workers/  (2 files)
  crash-reporter/  (2 files)
    index.ts
    wrangler.toml
.gitattributes
.gitignore
AGENTS.md
CONTRIBUTING.md
Dockerfile
Dockerfile.ci
LICENSE
Makefile
README.md
build.ps1
camofox.config.json
jest.config.cjs
jest.config.e2e.cjs
openapi.json
openclaw.plugin.json
package.json
plugin.js
plugin.ts
postinstall.js
railway.toml
release.sh
run.sh
tsconfig.json
```

## Entry points

- [tools/windows-utm/build-fat-bootstrap.py:152](https://github.com/jo-inc/camofox-browser/blob/31376c27db94204ffdc635ae71a7f61328e91a5e/tools/windows-utm/build-fat-bootstrap.py#L152)
- [mcp/server.mjs](https://github.com/jo-inc/camofox-browser/blob/31376c27db94204ffdc635ae71a7f61328e91a5e/mcp/server.mjs)
- [bin/camofox-browser.js](https://github.com/jo-inc/camofox-browser/blob/31376c27db94204ffdc635ae71a7f61328e91a5e/bin/camofox-browser.js)
- [plugins/persistence/index.js](https://github.com/jo-inc/camofox-browser/blob/31376c27db94204ffdc635ae71a7f61328e91a5e/plugins/persistence/index.js)
- [plugins/vnc/index.js](https://github.com/jo-inc/camofox-browser/blob/31376c27db94204ffdc635ae71a7f61328e91a5e/plugins/vnc/index.js)
- [plugins/youtube/index.js](https://github.com/jo-inc/camofox-browser/blob/31376c27db94204ffdc635ae71a7f61328e91a5e/plugins/youtube/index.js)
- [workers/crash-reporter/index.ts](https://github.com/jo-inc/camofox-browser/blob/31376c27db94204ffdc635ae71a7f61328e91a5e/workers/crash-reporter/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bin package | library | Observed | Groups 1 file(s) under bin package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 11 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 7 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 3 file(s) under data layer (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: build, lfn_entries, main, short_name, udf_tree. |
| lib package | library | Observed | Groups 49 file(s) under lib package (observed from repository paths and static analysis). |
| mcp package | library | Observed | Groups 4 file(s) under mcp package (observed from repository paths and static analysis). |
| plugins package | library | Observed | Groups 13 file(s) under plugins package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 13 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 122 file(s) under tests (observed from repository paths and static analysis). |
| tools package | library | Observed | Groups 3 file(s) under tools package (observed from repository paths and static analysis). |
| workers package | library | Observed | Groups 1 file(s) under workers package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/workflows/agenthook-notify.yml` (ci)
- `.github/workflows/auto-close-old-reports.yml` (ci)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/clawhub-publish.yml` (ci)
- `.github/workflows/docker.yml` (ci)
- `.github/workflows/mirror-camoufox.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.github/workflows/telemetry-deploy.yml` (ci)
- `Dockerfile` (container)
- `Dockerfile.ci` (container)
- `camofox.config.json` (config)
- `docs/openapi.json` (config)
- `mcp/package.json` (manifest)
- `openapi.json` (config)
- `openclaw.plugin.json` (config)
- `package.json` (manifest)
- `plugins/vnc/plugin.json` (config)
- `railway.toml` (config)
- `tsconfig.json` (config)
- `workers/crash-reporter/wrangler.toml` (config)

## Top-level layout

- `tests` — 122 analysed file(s)
- `lib` — 49 analysed file(s)
- `plugins` — 24 analysed file(s)
- `(root files)` — 23 analysed file(s)
- `scripts` — 13 analysed file(s)
- `.github` — 10 analysed file(s)
- `mcp` — 6 analysed file(s)
- `tools` — 6 analysed file(s)
- `docs` — 2 analysed file(s)
- `workers` — 2 analysed file(s)
- `bin` — 1 analysed file(s)
- `changelog` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `31376c27db94204ffdc635ae71a7f61328e91a5e` is the revision these paths and observations refer to.
