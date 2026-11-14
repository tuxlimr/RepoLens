# Project structure: jlmakes/scrollreveal

**Analysed commit:** `411043d3fd1d13d21a824f9c3e24e3f180197bd5`

**Commit reference:** [411043d3fd1d13d21a824f9c3e24e3f180197bd5](https://github.com/jlmakes/scrollreveal/commit/411043d3fd1d13d21a824f9c3e24e3f180197bd5)

**Tree at this commit:** [jlmakes/scrollreveal@411043d3fd1d](https://github.com/jlmakes/scrollreveal/tree/411043d3fd1d13d21a824f9c3e24e3f180197bd5)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | jlmakes/scrollreveal |
| Description | Animate elements as they scroll into view. |
| Stars | 22469 |
| Forks | 2191 |
| Licence | Not detected |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `411043d3fd1d13d21a824f9c3e24e3f180197bd5` |
| Retrieved at | 2026-11-14T19:11:08.725689+00:00 |
| Files in this snapshot | 50 |

## Directory tree

```text
.github/  (2 files)
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
src/  (27 files)
  instance/  (13 files)
    functions/  (6 files)
      … 6 files under this directory
    methods/  (4 files)
      … 4 files under this directory
    constructor.js
    defaults.js
    mount.js
  polyfills/  (1 files)
    math-sign.js
  utils/  (12 files)
    deep-assign.js
    each.js
    get-geometry.js
    get-prefixed-css-prop.js
    get-scrolled.js
    is-element-visible.js
    is-mobile.js
    is-object.js
    is-transform-supported.js
    is-transition-supported.js
    logger.js
    next-unique-id.js
  index.js
test/  (14 files)
  instance/  (1 files)
    constructor.spec.js
  polyfills/  (1 files)
    math-sign.spec.js
  utils/  (9 files)
    deep-assign.spec.js
    each.spec.js
    get-prefixed-css-prop.spec.js
    is-mobile.spec.js
    is-object.spec.js
    is-transform-supported.spec.js
    is-transition-supported.spec.js
    logger.spec.js
    next-unique-id.spec.js
  karma.conf.js
  sauce.conf.js
  timeout.spec.js
.eslintrc.json
.gitattributes
.gitignore
.travis.yml
CHANGELOG.md
README.md
package.json
```

## Entry points

- [src/index.js](https://github.com/jlmakes/scrollreveal/blob/411043d3fd1d13d21a824f9c3e24e3f180197bd5/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| instance package | library | Observed | Groups 13 file(s) under instance package (observed from repository paths and static analysis). |
| polyfills package | library | Observed | Groups 1 file(s) under polyfills package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 14 file(s) under tests (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 12 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.eslintrc.json` (config)
- `.travis.yml` (ci)
- `package.json` (manifest)

## Top-level layout

- `src` — 27 analysed file(s)
- `test` — 14 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `.github` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 4 file(s) were skipped during inventory (4 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `411043d3fd1d13d21a824f9c3e24e3f180197bd5` is the revision these paths and observations refer to.
