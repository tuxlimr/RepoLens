# Project structure: Netflix/pollyjs

**Analysed commit:** `d031861625f58423169b396e5afc8a0110d1b232`

**Commit reference:** [d031861625f58423169b396e5afc8a0110d1b232](https://github.com/Netflix/pollyjs/commit/d031861625f58423169b396e5afc8a0110d1b232)

**Tree at this commit:** [Netflix/pollyjs@d031861625f5](https://github.com/Netflix/pollyjs/tree/d031861625f58423169b396e5afc8a0110d1b232)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Netflix/pollyjs |
| Description | Record, Replay, and Stub HTTP Interactions. |
| Stars | 10250 |
| Forks | 358 |
| Licence | Apache-2.0 |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `d031861625f58423169b396e5afc8a0110d1b232` |
| Retrieved at | 2026-11-14T19:12:42.205475+00:00 |
| Files in this snapshot | 392 |

## Directory tree

```text
.github/  (2 files)
  issue_template.md
  pull_request_template.md
.husky/  (2 files)
  commit-msg
  pre-commit
docs/  (34 files)
  adapters/  (6 files)
    custom.md
    fetch.md
    node-http.md
    playwright.md
    puppeteer.md
    xhr.md
  assets/  (1 files)
    styles.css
  cli/  (2 files)
    commands.md
    overview.md
  frameworks/  (1 files)
    ember-cli.md
  node-server/  (2 files)
    express-integrations.md
    overview.md
  persisters/  (4 files)
    custom.md
    fs.md
    local-storage.md
    rest.md
  server/  (7 files)
    api.md
    event.md
    events-and-middleware.md
    overview.md
    request.md
    response.md
    route-handler.md
  test-frameworks/  (3 files)
    jest-jasmine.md
    mocha.md
    qunit.md
  .nojekyll
  _coverpage.md
  _sidebar.md
  api.md
  configuration.md
  examples.md
  index.html
  quick-start.md
examples/  (50 files)
  client-server/  (5 files)
    tests/  (3 files)
      … 3 files under this directory
    index.html
    package.json
  dummy-app/  (12 files)
    public/  (2 files)
      … 2 files under this directory
    src/  (6 files)
      … 6 files under this directory
    .eslintrc.js
    .gitignore
    README.md
    package.json
  jest-node-fetch/  (8 files)
    __recordings__/  (2 files)
      … 2 files under this directory
    __tests__/  (1 files)
      … 1 files under this directory
    src/  (3 files)
      … 3 files under this directory
    .eslintrc.js
    package.json
  jest-puppeteer/  (6 files)
    __recordings__/  (1 files)
      … 1 files under this directory
    __tests__/  (1 files)
      … 1 files under this directory
    .eslintrc.js
    jest-puppeteer.config.js
    jest.config.js
    package.json
  node-fetch/  (3 files)
    recordings/  (1 files)
      … 1 files under this directory
    tests/  (1 files)
      … 1 files under this directory
    package.json
  puppeteer/  (3 files)
    recordings/  (1 files)
      … 1 files under this directory
    index.js
    package.json
  rest-persister/  (5 files)
    recordings/  (1 files)
      … 1 files under this directory
    tests/  (2 files)
      … 2 files under this directory
    index.html
    package.json
  typescript-jest-node-fetch/  (7 files)
    __recordings__/  (1 files)
      … 1 files under this directory
    src/  (3 files)
      … 3 files under this directory
    jest.config.ts
    package.json
    tsconfig.json
  .eslintrc.js
packages/  (266 files)
  @pollyjs/  (266 files)
    adapter/  (14 files)
      … 14 files under this directory
    adapter-fetch/  (13 files)
      … 13 files under this directory
    adapter-node-http/  (23 files)
      … 23 files under this directory
    adapter-puppeteer/  (11 files)
      … 11 files under this directory
    adapter-xhr/  (11 files)
      … 11 files under this directory
    cli/  (6 files)
      … 6 files under this directory
    core/  (53 files)
      … 53 files under this directory
    ember/  (43 files)
      … 43 files under this directory
    node-server/  (11 files)
      … 11 files under this directory
    persister/  (16 files)
      … 16 files under this directory
    persister-fs/  (10 files)
      … 10 files under this directory
    persister-in-memory/  (6 files)
      … 6 files under this directory
    persister-local-storage/  (7 files)
      … 7 files under this directory
    persister-rest/  (8 files)
      … 8 files under this directory
    utils/  (34 files)
      … 34 files under this directory
scripts/  (9 files)
  rollup/  (7 files)
    browser.config.js
    browser.test.config.js
    default.config.js
    jest.test.config.js
    node.config.js
    node.test.config.js
    utils.js
  require-clean-work-tree.sh
  require-test-build.sh
tests/  (13 files)
  helpers/  (4 files)
    file.js
    global-node-fetch.js
    setup-fetch-record.js
    setup-persister.js
  integration/  (6 files)
    adapter-browser-tests.js
    adapter-identifier-tests.js
    adapter-node-tests.js
    adapter-polly-tests.js
    adapter-tests.js
    persister-tests.js
  index.mustache
  middleware.js
  node-setup.js
.commitlintrc.js
.eslintignore
.eslintrc.js
.gitignore
.mocharc.js
.prettierrc.js
.travis.yml
CHANGELOG.md
CONTRIBUTING.md
LICENSE
OSSMETADATA
README.md
jest.config.js
lerna.json
package.json
testem.js
```

## Entry points

- [packages/@pollyjs/cli/bin/cli.js](https://github.com/Netflix/pollyjs/blob/d031861625f58423169b396e5afc8a0110d1b232/packages/%40pollyjs/cli/bin/cli.js)
- [packages/@pollyjs/ember/index.js](https://github.com/Netflix/pollyjs/blob/d031861625f58423169b396e5afc8a0110d1b232/packages/%40pollyjs/ember/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 22 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 91 file(s) under packages package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 9 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 30 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 94 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.travis.yml` (ci)
- `examples/client-server/package.json` (manifest)
- `examples/dummy-app/package.json` (manifest)
- `examples/dummy-app/public/manifest.json` (config)
- `examples/jest-node-fetch/package.json` (manifest)
- `examples/jest-puppeteer/package.json` (manifest)
- `examples/node-fetch/package.json` (manifest)
- `examples/puppeteer/package.json` (manifest)
- `examples/rest-persister/package.json` (manifest)
- `examples/typescript-jest-node-fetch/package.json` (manifest)
- `examples/typescript-jest-node-fetch/tsconfig.json` (config)
- `lerna.json` (config)
- `package.json` (manifest)
- `packages/@pollyjs/adapter-fetch/package.json` (manifest)
- `packages/@pollyjs/adapter-node-http/package.json` (manifest)
- `packages/@pollyjs/adapter-puppeteer/package.json` (manifest)
- `packages/@pollyjs/adapter-xhr/package.json` (manifest)
- `packages/@pollyjs/adapter/package.json` (manifest)
- `packages/@pollyjs/cli/package.json` (manifest)
- `packages/@pollyjs/core/package.json` (manifest)
- `packages/@pollyjs/ember/.editorconfig` (config)
- `packages/@pollyjs/ember/package.json` (manifest)
- `packages/@pollyjs/node-server/package.json` (manifest)
- `packages/@pollyjs/persister-fs/package.json` (manifest)
- `packages/@pollyjs/persister-in-memory/package.json` (manifest)
- `packages/@pollyjs/persister-local-storage/package.json` (manifest)
- `packages/@pollyjs/persister-rest/package.json` (manifest)
- `packages/@pollyjs/persister/package.json` (manifest)
- `packages/@pollyjs/utils/package.json` (manifest)

## Top-level layout

- `packages` — 266 analysed file(s)
- `examples` — 50 analysed file(s)
- `docs` — 34 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `tests` — 13 analysed file(s)
- `scripts` — 9 analysed file(s)
- `.github` — 2 analysed file(s)
- `.husky` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `d031861625f58423169b396e5afc8a0110d1b232` is the revision these paths and observations refer to.
