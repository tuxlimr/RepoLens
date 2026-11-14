# Project structure: axios/axios

**Analysed commit:** `4ee8d46fc463770b8f5da718d5449a5b027b2c08`

**Commit reference:** [4ee8d46fc463770b8f5da718d5449a5b027b2c08](https://github.com/axios/axios/commit/4ee8d46fc463770b8f5da718d5449a5b027b2c08)

**Tree at this commit:** [axios/axios@4ee8d46fc463](https://github.com/axios/axios/tree/4ee8d46fc463770b8f5da718d5449a5b027b2c08)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | axios/axios |
| Description | Promise based HTTP client for the browser and node.js |
| Stars | 109391 |
| Forks | 12017 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | v1.x |
| Analysed commit | `4ee8d46fc463770b8f5da718d5449a5b027b2c08` |
| Retrieved at | 2026-11-14T19:10:32.677083+00:00 |
| Files in this snapshot | 506 |

## Directory tree

```text
.devcontainer/  (1 files)
  devcontainer.json
.github/  (14 files)
  workflows/  (8 files)
    bundle-size.yml
    lockfile-lint.yml
    moderator.yml
    publish.yml
    release-branch.yml
    run-ci.yml
    verify-build-reproducibility.yml
    zizmor.yml
  CODEOWNERS
  FUNDING.yml
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
  copilot-instructions.md
  dependabot.yml
.husky/  (1 files)
  commit-msg
docs/  (171 files)
  .vitepress/  (15 files)
    theme/  (11 files)
      … 11 files under this directory
    config.mts
    search.mts
    tokenizeSearchText.js
    tokenizeSearchText.test.js
  blog/  (3 files)
    herodevs-nes-for-axios-v0.md
    index.md
    posts.data.ts
  data/  (1 files)
    partners.json
  es/  (35 files)
    pages/  (34 files)
      … 34 files under this directory
    index.md
  fr/  (35 files)
    pages/  (34 files)
      … 34 files under this directory
    index.md
  pages/  (34 files)
    advanced/  (25 files)
      … 25 files under this directory
    getting-started/  (5 files)
      … 5 files under this directory
    misc/  (4 files)
      … 4 files under this directory
  patches/  (1 files)
    @splidejs+splide+4.1.4.patch
  public/  (6 files)
    sponsors/  (1 files)
      … 1 files under this directory
    logo-light.svg
    logo.svg
    site.webmanifest
    words-light.svg
    words.svg
  scripts/  (3 files)
    process-sponsors.js
    selectLatestSponsorsBySlug.js
    utils.js
  zh/  (35 files)
    pages/  (34 files)
      … 34 files under this directory
    index.md
  index.md
  package.json
  site.webmanifest
examples/  (17 files)
  abort-controller/  (2 files)
    index.html
    server.js
  all/  (1 files)
    index.html
  amd/  (1 files)
    index.html
  get/  (2 files)
    index.html
    server.js
  post/  (2 files)
    index.html
    server.js
  postMultipartFormData/  (2 files)
    index.html
    server.js
  transform-response/  (1 files)
    index.html
  upload/  (2 files)
    index.html
    server.js
  README.md
  improved-network-errors.md
  network_enhanced.js
  server.js
lib/  (76 files)
  adapters/  (5 files)
    README.md
    adapters.js
    fetch.js
    http.js
    xhr.js
  cancel/  (3 files)
    CancelToken.js
    CanceledError.js
    isCancel.js
  core/  (14 files)
    Axios.js
    AxiosError.js
    AxiosHeaders.js
    InterceptorManager.js
    README.md
    assertParamsAcyclic.js
    buildFullPath.js
    createMultipartBody.js
    dispatchRequest.js
    mergeConfig.js
    methodList.js
    setFormDataHeaders.js
    settle.js
    transformData.js
  defaults/  (2 files)
    index.js
    transitional.js
  env/  (3 files)
    classes/  (1 files)
      … 1 files under this directory
    README.md
    data.js
  helpers/  (37 files)
    AxiosTransformStream.js
    AxiosURLSearchParams.js
    Http2Sessions.js
    HttpStatusCode.js
    README.md
    ZlibHeaderTransformStream.js
    bind.js
    buildURL.js
    callbackify.js
    combineURLs.js
    composeSignals.js
    cookies.js
    deprecatedMethod.js
    estimateDataURLDecodedBytes.js
    formDataToBlob.js
    formDataToJSON.js
    formDataToStream.js
    fromDataURI.js
    isAbsoluteURL.js
    isAxiosError.js
    isURLSameOrigin.js
    normalizeURLForProtocolCheck.js
    null.js
    parseHeaders.js
    … 13 more files
  platform/  (10 files)
    browser/  (4 files)
      … 4 files under this directory
    common/  (1 files)
      … 1 files under this directory
    node/  (4 files)
      … 4 files under this directory
    index.js
  axios.js
  utils.js
sandbox/  (3 files)
  client.html
  client.js
  server.js
scripts/  (2 files)
  axios-build-instance.js
  benchmark-merge-config.js
tests/  (193 files)
  browser/  (28 files)
    adapter.browser.test.js
    baseURLResolution.browser.test.js
    basicAuth.browser.test.js
    cancel.browser.test.js
    cancelToken.browser.test.js
    cookies.browser.test.js
    defaults.browser.test.js
    errorStack.browser.test.js
    fetchCache.browser.test.js
    fetchHeaders.browser.test.js
    fetchResponseErrors.browser.test.js
    formBodyLength.browser.test.js
    formdata.browser.test.js
    headers.browser.test.js
    instance.browser.test.js
    interceptors.browser.test.js
    isURLSameOrigin.browser.test.js
    options.browser.test.js
    progress.browser.test.js
    promise.browser.test.js
    requestUrl.browser.test.js
    requests.browser.test.js
    responseDuration.browser.test.js
    settle.browser.test.js
    … 4 more files
  module/  (26 files)
    cjs/  (13 files)
      … 13 files under this directory
    esm/  (13 files)
      … 13 files under this directory
  setup/  (6 files)
    adapters.js
    browser.setup.js
    formBodyLengthCases.js
    nativeCookieStore.js
    runModuleInChildProcess.js
    server.js
  smoke/  (56 files)
    bun/  (12 files)
      … 12 files under this directory
    cjs/  (18 files)
      … 18 files under this directory
    deno/  (7 files)
      … 7 files under this directory
    esm/  (19 files)
      … 19 files under this directory
  unit/  (76 files)
    adapters/  (15 files)
      … 15 files under this directory
    cancel/  (2 files)
      … 2 files under this directory
    core/  (9 files)
      … 9 files under this directory
    helpers/  (24 files)
      … 24 files under this directory
    utils/  (10 files)
      … 10 files under this directory
    api.test.js
    axios.test.js
    axiosHeaders.test.js
    composeSignals.test.js
    estimateDataURLDecodedBytes.test.js
    fromDataURI.test.js
    parseProtocol.test.js
    platform.test.js
    prototypePollution.test.js
    query.test.js
    regression.test.js
    runModuleInChildProcess.test.js
    syntaxCompat.test.js
    toFormData.test.js
    transformResponse.test.js
    utils.test.js
  README.md
.gitignore
.prettierignore
.prettierrc
AGENTS.md
CHANGELOG.md
CODE_OF_CONDUCT.md
COLLABORATOR_GUIDE.md
CONTRIBUTING.md
CONTRIBUTORS.md
ECOSYSTEM.md
LICENSE
MIGRATION_GUIDE.md
PRE_RELEASE_CHANGELOG.md
PRE_RELEASE_DOCS.md
README.md
SECURITY.md
THREATMODEL.md
eslint.config.js
gulpfile.js
index.d.cts
index.d.ts
index.js
package.json
rollup.config.js
… 4 more files
```

## Entry points

- [index.js](https://github.com/axios/axios/blob/4ee8d46fc463770b8f5da718d5449a5b027b2c08/index.js)
- [lib/defaults/index.js](https://github.com/axios/axios/blob/4ee8d46fc463770b8f5da718d5449a5b027b2c08/lib/defaults/index.js)
- [lib/platform/browser/index.js](https://github.com/axios/axios/blob/4ee8d46fc463770b8f5da718d5449a5b027b2c08/lib/platform/browser/index.js)
- [lib/platform/index.js](https://github.com/axios/axios/blob/4ee8d46fc463770b8f5da718d5449a5b027b2c08/lib/platform/index.js)
- [lib/platform/node/index.js](https://github.com/axios/axios/blob/4ee8d46fc463770b8f5da718d5449a5b027b2c08/lib/platform/node/index.js)
- [sandbox/server.js](https://github.com/axios/axios/blob/4ee8d46fc463770b8f5da718d5449a5b027b2c08/sandbox/server.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 7 file(s) under core modules (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 4 file(s) under external integrations (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 55 file(s) under lib package (observed from repository paths and static analysis). |
| sandbox package | library | Observed | Groups 2 file(s) under sandbox package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 2 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 13 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 193 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.devcontainer/devcontainer.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/bundle-size.yml` (ci)
- `.github/workflows/lockfile-lint.yml` (ci)
- `.github/workflows/moderator.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.github/workflows/release-branch.yml` (ci)
- `.github/workflows/run-ci.yml` (ci)
- `.github/workflows/verify-build-reproducibility.yml` (ci)
- `.github/workflows/zizmor.yml` (ci)
- `docs/data/partners.json` (config)
- `docs/package.json` (manifest)
- `package.json` (manifest)
- `tsconfig.json` (config)
- `tslint.json` (config)

## Top-level layout

- `tests` — 193 analysed file(s)
- `docs` — 171 analysed file(s)
- `lib` — 76 analysed file(s)
- `(root files)` — 28 analysed file(s)
- `examples` — 17 analysed file(s)
- `.github` — 14 analysed file(s)
- `sandbox` — 3 analysed file(s)
- `scripts` — 2 analysed file(s)
- `.devcontainer` — 1 analysed file(s)
- `.husky` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 8 file(s) were skipped during inventory (3 x likely secret file excluded; 5 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `4ee8d46fc463770b8f5da718d5449a5b027b2c08` is the revision these paths and observations refer to.
