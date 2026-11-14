# Project structure: cristianbote/goober

**Analysed commit:** `e7e6d33e210ed1f886fb4f372fc25ffd22d358d0`

**Commit reference:** [e7e6d33e210ed1f886fb4f372fc25ffd22d358d0](https://github.com/cristianbote/goober/commit/e7e6d33e210ed1f886fb4f372fc25ffd22d358d0)

**Tree at this commit:** [cristianbote/goober@e7e6d33e210e](https://github.com/cristianbote/goober/tree/e7e6d33e210ed1f886fb4f372fc25ffd22d358d0)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | cristianbote/goober |
| Description | 🥜 goober, a less than 1KB 🎉  css-in-js alternative with a familiar API |
| Stars | 3277 |
| Forks | 128 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `e7e6d33e210ed1f886fb4f372fc25ffd22d358d0` |
| Retrieved at | 2026-11-14T19:15:26.637044+00:00 |
| Files in this snapshot | 130 |

## Directory tree

```text
.codesandbox/  (1 files)
  ci.json
.github/  (4 files)
  workflows/  (3 files)
    docs.yml
    pr_build.yml
    pr_size.yml
  FUNDING.yml
benchmarks/  (7 files)
  perf-hash.cjs
  perf-parse.cjs
  perf-parse.modern.cjs
  perf.cjs
  perf.compare.cjs
  perf.compare.modern.cjs
  run-ab.cjs
docs/  (30 files)
  docs/  (19 files)
    api/  (8 files)
      … 8 files under this directory
    features/  (4 files)
      … 4 files under this directory
    integrations/  (5 files)
      … 5 files under this directory
    contributing.md
    introduction.md
  src/  (1 files)
    css/  (1 files)
      … 1 files under this directory
  static/  (2 files)
    .nojekyll
    CNAME
  .gitignore
  .prettierignore
  LICENSE
  README.md
  babel.config.js
  docusaurus.config.js
  package.json
  sidebars.js
global/  (7 files)
  src/  (4 files)
    __tests__/  (3 files)
      … 3 files under this directory
    index.js
  babel.config.cjs
  global.d.ts
  package.json
macro/  (2 files)
  index.js
  package.json
packages/  (12 files)
  babel-plugin-transform-goober/  (7 files)
    __tests__/  (4 files)
      … 4 files under this directory
    README.md
    index.js
    package.json
  gatsby-plugin-goober/  (5 files)
    README.md
    gatsby-browser.js
    gatsby-ssr.js
    index.js
    package.json
prefixer/  (7 files)
  __tests__/  (1 files)
    index.test.js
  src/  (1 files)
    index.js
  LICENSE
  README.md
  autoprefixer.d.ts
  babel.config.cjs
  package.json
should-forward-prop/  (5 files)
  src/  (2 files)
    __tests__/  (1 files)
      … 1 files under this directory
    index.js
  babel.config.cjs
  package.json
  should-forward-prop.d.ts
src/  (21 files)
  __tests__/  (4 files)
    css.test.js
    index.test.js
    integrations.test.js
    styled.test.js
  core/  (14 files)
    __tests__/  (7 files)
      … 7 files under this directory
    astish.js
    compile.js
    get-sheet.js
    hash.js
    parse.js
    to-hash.js
    update.js
  css.js
  index.js
  styled.js
tests/  (1 files)
  setup.js
ts-tests/  (2 files)
  test-api.tsx
  tsconfig.json
website/  (21 files)
  public/  (1 files)
    robots.txt
  src/  (14 files)
    components/  (7 files)
      … 7 files under this directory
    pages/  (3 files)
      … 3 files under this directory
    styles/  (2 files)
      … 2 files under this directory
    App.jsx
    main.jsx
  .gitignore
  LICENSE
  index.html
  package.json
  prerender.js
  vite.config.ts
.gitignore
.prettierignore
.prettierrc
CNAME
LICENSE
README.md
babel.config.cjs
goober.d.ts
package.json
typings.json
```

## Entry points

- [macro/index.js](https://github.com/cristianbote/goober/blob/e7e6d33e210ed1f886fb4f372fc25ffd22d358d0/macro/index.js)
- [packages/babel-plugin-transform-goober/index.js](https://github.com/cristianbote/goober/blob/e7e6d33e210ed1f886fb4f372fc25ffd22d358d0/packages/babel-plugin-transform-goober/index.js)
- [packages/gatsby-plugin-goober/index.js](https://github.com/cristianbote/goober/blob/e7e6d33e210ed1f886fb4f372fc25ffd22d358d0/packages/gatsby-plugin-goober/index.js)
- [global/src/index.js](https://github.com/cristianbote/goober/blob/e7e6d33e210ed1f886fb4f372fc25ffd22d358d0/global/src/index.js)
- [prefixer/src/index.js](https://github.com/cristianbote/goober/blob/e7e6d33e210ed1f886fb4f372fc25ffd22d358d0/prefixer/src/index.js)
- [should-forward-prop/src/index.js](https://github.com/cristianbote/goober/blob/e7e6d33e210ed1f886fb4f372fc25ffd22d358d0/should-forward-prop/src/index.js)
- [src/index.js](https://github.com/cristianbote/goober/blob/e7e6d33e210ed1f886fb4f372fc25ffd22d358d0/src/index.js)
- [website/src/App.jsx](https://github.com/cristianbote/goober/blob/e7e6d33e210ed1f886fb4f372fc25ffd22d358d0/website/src/App.jsx)
- [website/src/main.jsx](https://github.com/cristianbote/goober/blob/e7e6d33e210ed1f886fb4f372fc25ffd22d358d0/website/src/main.jsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| benchmarks package | library | Observed | Groups 7 file(s) under benchmarks package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 10 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| css.js package | library | Observed | Groups 1 file(s) under css.js package (observed from repository paths and static analysis). |
| global package | library | Observed | Groups 5 file(s) under global package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| macro package | library | Observed | Groups 1 file(s) under macro package (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 5 file(s) under packages package (observed from repository paths and static analysis). |
| prefixer package | library | Observed | Groups 4 file(s) under prefixer package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 14 file(s) under service / domain layer (observed from repository paths and static analysis). |
| should-forward-prop package | library | Observed | Groups 4 file(s) under should-forward-prop package (observed from repository paths and static analysis). |
| styled.js package | library | Observed | Groups 1 file(s) under styled.js package (observed from repository paths and static analysis). |
| __tests__ package | library | Observed | Groups 5 file(s) under __tests__ package (observed from repository paths and static analysis). |
| ts-tests package | library | Observed | Groups 1 file(s) under ts-tests package (observed from repository paths and static analysis). |
| website package | library | Observed | Groups 16 file(s) under website package (observed from repository paths and static analysis). |

## Important files

- `.codesandbox/ci.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/workflows/docs.yml` (ci)
- `.github/workflows/pr_build.yml` (ci)
- `.github/workflows/pr_size.yml` (ci)
- `docs/package.json` (manifest)
- `global/package.json` (manifest)
- `macro/package.json` (manifest)
- `package.json` (manifest)
- `packages/babel-plugin-transform-goober/package.json` (manifest)
- `packages/gatsby-plugin-goober/package.json` (manifest)
- `prefixer/package.json` (manifest)
- `should-forward-prop/package.json` (manifest)
- `ts-tests/tsconfig.json` (config)
- `typings.json` (config)
- `website/package.json` (manifest)

## Top-level layout

- `docs` — 30 analysed file(s)
- `src` — 21 analysed file(s)
- `website` — 21 analysed file(s)
- `packages` — 12 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `benchmarks` — 7 analysed file(s)
- `global` — 7 analysed file(s)
- `prefixer` — 7 analysed file(s)
- `should-forward-prop` — 5 analysed file(s)
- `.github` — 4 analysed file(s)
- `macro` — 2 analysed file(s)
- `ts-tests` — 2 analysed file(s)
- `.codesandbox` — 1 analysed file(s)
- `tests` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `e7e6d33e210ed1f886fb4f372fc25ffd22d358d0` is the revision these paths and observations refer to.
