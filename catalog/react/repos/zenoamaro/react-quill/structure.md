# Project structure: zenoamaro/react-quill

**Analysed commit:** `615b4bf730e7a34c1dda1707447123c1d727f9d1`

**Commit reference:** [615b4bf730e7a34c1dda1707447123c1d727f9d1](https://github.com/zenoamaro/react-quill/commit/615b4bf730e7a34c1dda1707447123c1d727f9d1)

**Tree at this commit:** [zenoamaro/react-quill@615b4bf730e7](https://github.com/zenoamaro/react-quill/tree/615b4bf730e7a34c1dda1707447123c1d727f9d1)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | zenoamaro/react-quill |
| Description | A Quill component for React. |
| Stars | 6996 |
| Forks | 937 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `615b4bf730e7a34c1dda1707447123c1d727f9d1` |
| Retrieved at | 2026-11-14T19:14:00.265645+00:00 |
| Files in this snapshot | 21 |

## Directory tree

```text
.github/  (1 files)
  ISSUE_TEMPLATE.md
demo/  (3 files)
  index.html
  index.js
  test.html
src/  (1 files)
  index.tsx
test/  (6 files)
  polyfills/  (2 files)
    MutationObserver.js
    getSelection.js
  index.js
  index.spec.js
  setup.js
  utils.js
.gitignore
.prettierrc
.travis.yml
CHANGELOG.md
LICENSE
README.md
cypress.json
package.json
tsconfig.json
webpack.config.js
```

## Entry points

- [demo/index.js](https://github.com/zenoamaro/react-quill/blob/615b4bf730e7a34c1dda1707447123c1d727f9d1/demo/index.js)
- [src/index.tsx](https://github.com/zenoamaro/react-quill/blob/615b4bf730e7a34c1dda1707447123c1d727f9d1/src/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| demo package | library | Observed | Groups 1 file(s) under demo package (observed from repository paths and static analysis). |
| index.tsx package | library | Observed | Groups 1 file(s) under index.tsx package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 6 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.travis.yml` (ci)
- `cypress.json` (config)
- `package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `(root files)` — 10 analysed file(s)
- `test` — 6 analysed file(s)
- `demo` — 3 analysed file(s)
- `.github` — 1 analysed file(s)
- `src` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `615b4bf730e7a34c1dda1707447123c1d727f9d1` is the revision these paths and observations refer to.
