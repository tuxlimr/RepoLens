# Project structure: twobin/react-lazyload

**Analysed commit:** `20abd7806416fe3fa4e92a8040526de96d1f2598`

**Commit reference:** [20abd7806416fe3fa4e92a8040526de96d1f2598](https://github.com/twobin/react-lazyload/commit/20abd7806416fe3fa4e92a8040526de96d1f2598)

**Tree at this commit:** [twobin/react-lazyload@20abd7806416](https://github.com/twobin/react-lazyload/tree/20abd7806416fe3fa4e92a8040526de96d1f2598)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | twobin/react-lazyload |
| Description | Lazy load your component, image or anything matters the performance. |
| Stars | 5885 |
| Forks | 482 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `20abd7806416fe3fa4e92a8040526de96d1f2598` |
| Retrieved at | 2026-11-14T19:14:12.505781+00:00 |
| Files in this snapshot | 43 |

## Directory tree

```text
examples/  (16 files)
  components/  (3 files)
    Operation.js
    Placeholder.js
    Widget.js
  js/  (1 files)
    vendors.js
  pages/  (9 files)
    debounce.js
    decorator.js
    fadein.js
    forcevisible.js
    image.js
    normal.js
    overflow.js
    placeholder.js
    scroll.js
  utils/  (1 files)
    index.js
  app.js
  index.html
lib/  (6 files)
  utils/  (4 files)
    debounce.js
    event.js
    scrollParent.js
    throttle.js
  decorator.js
  index.js
src/  (5 files)
  utils/  (4 files)
    debounce.js
    event.js
    scrollParent.js
    throttle.js
  index.jsx
test/  (6 files)
  specs/  (4 files)
    events.spec.js
    lazyload.debounce.spec.js
    lazyload.spec.js
    lazyload.throttle.spec.js
  Test.component.js
  karma.conf.js
.babelrc
.editorconfig
.eslintrc
.gitignore
.npmignore
.travis.yml
LICENSE
README.md
package.json
webpack.config.js
```

## Entry points

- [lib/index.js](https://github.com/twobin/react-lazyload/blob/20abd7806416fe3fa4e92a8040526de96d1f2598/lib/index.js)
- [src/index.jsx](https://github.com/twobin/react-lazyload/blob/20abd7806416fe3fa4e92a8040526de96d1f2598/src/index.jsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| index.jsx package | library | Observed | Groups 1 file(s) under index.jsx package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 6 file(s) under lib package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 6 file(s) under tests (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 4 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.travis.yml` (ci)
- `package.json` (manifest)

## Top-level layout

- `examples` — 16 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `lib` — 6 analysed file(s)
- `test` — 6 analysed file(s)
- `src` — 5 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `20abd7806416fe3fa4e92a8040526de96d1f2598` is the revision these paths and observations refer to.
