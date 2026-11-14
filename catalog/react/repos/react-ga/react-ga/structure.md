# Project structure: react-ga/react-ga

**Analysed commit:** `087837dc03d482549ded7669ac559df0c7cc5498`

**Commit reference:** [087837dc03d482549ded7669ac559df0c7cc5498](https://github.com/react-ga/react-ga/commit/087837dc03d482549ded7669ac559df0c7cc5498)

**Tree at this commit:** [react-ga/react-ga@087837dc03d4](https://github.com/react-ga/react-ga/tree/087837dc03d482549ded7669ac559df0c7cc5498)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | react-ga/react-ga |
| Description | React Google Analytics Module |
| Stars | 5092 |
| Forks | 427 |
| Licence | Other |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `087837dc03d482549ded7669ac559df0c7cc5498` |
| Retrieved at | 2026-11-14T19:14:28.534547+00:00 |
| Files in this snapshot | 69 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (2 files)
    release.yml
    tests.yml
.husky/  (2 files)
  commit-msg
  pre-commit
demo/  (6 files)
  app/  (4 files)
    Events.jsx
    Router.jsx
    index.jsx
    withTracker.jsx
  index.jsx
  webpack.config.js
src/  (14 files)
  components/  (1 files)
    OutboundLink.js
  utils/  (11 files)
    __mocks__/  (1 files)
      … 1 files under this directory
    console/  (2 files)
      … 2 files under this directory
    format.js
    loadGA.js
    mightBeEmail.js
    redactEmail.js
    removeLeadingSlash.js
    testModeAPI.js
    toTitleCase.js
    trim.js
  core.js
  index.js
test/  (21 files)
  components/  (1 files)
    OutboundLink.test.jsx
  functionality/  (11 files)
    event.test.js
    exception.test.js
    ga.test.js
    initialize.test.js
    modalview.test.js
    outboundLink.test.jsx
    pageview.test.js
    plugin.test.js
    send.test.js
    set.test.js
    timing.test.js
  utils/  (8 files)
    console/  (2 files)
      … 2 files under this directory
    format.test.js
    mightBeEmail.test.js
    removeLeadingSlash.test.js
    testMode.test.js
    toTitleCase.test.js
    trim.test.js
  index.test.js
types/  (3 files)
  index.d.ts
  react-ga-tests.ts
  tsconfig.json
.babelrc
.eslintignore
.eslintrc.js
.gitignore
.lintstagedrc.js
.npmignore
.nvmrc
.prettierrc.js
.releaserc.json
CONTRIBUTING.md
LICENSE
README.md
bower.json
commitlint.config.js
core.d.ts
core.js
jest.config.js
jest.setup.js
package.json
version-bower.js
webpack.config.js
```

## Entry points

- [demo/app/index.jsx](https://github.com/react-ga/react-ga/blob/087837dc03d482549ded7669ac559df0c7cc5498/demo/app/index.jsx)
- [demo/index.jsx](https://github.com/react-ga/react-ga/blob/087837dc03d482549ded7669ac559df0c7cc5498/demo/index.jsx)
- [src/index.js](https://github.com/react-ga/react-ga/blob/087837dc03d482549ded7669ac559df0c7cc5498/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| components package | library | Observed | Groups 1 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 7 file(s) under core modules (observed from repository paths and static analysis). |
| core.js package | library | Observed | Groups 1 file(s) under core.js package (observed from repository paths and static analysis). |
| demo package | library | Observed | Groups 6 file(s) under demo package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 21 file(s) under tests (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 2 file(s) under types package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 11 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/release.yml` (ci)
- `.github/workflows/tests.yml` (ci)
- `.releaserc.json` (config)
- `bower.json` (config)
- `package.json` (manifest)
- `types/tsconfig.json` (config)

## Top-level layout

- `(root files)` — 21 analysed file(s)
- `test` — 21 analysed file(s)
- `src` — 14 analysed file(s)
- `demo` — 6 analysed file(s)
- `types` — 3 analysed file(s)
- `.github` — 2 analysed file(s)
- `.husky` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `087837dc03d482549ded7669ac559df0c7cc5498` is the revision these paths and observations refer to.
