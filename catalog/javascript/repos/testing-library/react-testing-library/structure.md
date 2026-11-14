# Project structure: testing-library/react-testing-library

**Analysed commit:** `20ce75f2907ca0e5c5a8ae595c0e9a4e368c7800`

**Commit reference:** [20ce75f2907ca0e5c5a8ae595c0e9a4e368c7800](https://github.com/testing-library/react-testing-library/commit/20ce75f2907ca0e5c5a8ae595c0e9a4e368c7800)

**Tree at this commit:** [testing-library/react-testing-library@20ce75f2907c](https://github.com/testing-library/react-testing-library/tree/20ce75f2907ca0e5c5a8ae595c0e9a4e368c7800)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | testing-library/react-testing-library |
| Description | 🐐 Simple and complete React DOM testing utilities that encourage good testing practices. |
| Stars | 19681 |
| Forks | 1171 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `20ce75f2907ca0e5c5a8ae595c0e9a4e368c7800` |
| Retrieved at | 2026-11-14T19:11:16.923788+00:00 |
| Files in this snapshot | 63 |

## Directory tree

```text
.codesandbox/  (1 files)
  ci.json
.github/  (7 files)
  ISSUE_TEMPLATE/  (3 files)
    Bug_Report.md
    Feature_Request.md
    Question.md
  workflows/  (2 files)
    release.yml
    validate.yml
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
other/  (4 files)
  design files/  (1 files)
    README.txt
  MAINTAINING.md
  USERS.md
  manual-releases.md
src/  (23 files)
  __mocks__/  (1 files)
    axios.js
  __tests__/  (17 files)
    __snapshots__/  (1 files)
      … 1 files under this directory
    act.js
    auto-cleanup-skip.js
    auto-cleanup.js
    cleanup.js
    config.js
    debug.js
    end-to-end.js
    error-handlers.js
    event-wrapper-nesting.js
    events.js
    multi-base.js
    new-act.js
    render.js
    renderHook.js
    rerender.js
    stopwatch.js
  act-compat.js
  config.js
  fire-event.js
  index.js
  pure.js
tests/  (4 files)
  failOnUnexpectedConsoleCalls.js
  setup-env.js
  shouldIgnoreConsoleError.js
  toWarnDev.js
types/  (4 files)
  index.d.ts
  pure.d.ts
  test.tsx
  tsconfig.json
.all-contributorsrc
.bundle.main.env
.bundle.pure.env
.gitattributes
.gitignore
.huskyrc.js
.prettierignore
.prettierrc.js
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
codecov.yml
dont-cleanup-after-each.js
jest.config.js
package.json
pure.d.ts
pure.js
tsconfig.json
```

## Entry points

- [src/index.js](https://github.com/testing-library/react-testing-library/blob/20ce75f2907ca0e5c5a8ae595c0e9a4e368c7800/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| act-compat.js package | library | Observed | Groups 1 file(s) under act-compat.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| config.js package | library | Observed | Groups 1 file(s) under config.js package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| fire-event.js package | library | Observed | Groups 1 file(s) under fire-event.js package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| __mocks__ package | library | Observed | Groups 1 file(s) under __mocks__ package (observed from repository paths and static analysis). |
| pure.js package | library | Observed | Groups 1 file(s) under pure.js package (observed from repository paths and static analysis). |
| __tests__ package | library | Observed | Groups 20 file(s) under __tests__ package (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 3 file(s) under types package (observed from repository paths and static analysis). |

## Important files

- `.codesandbox/ci.json` (config)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/validate.yml` (ci)
- `codecov.yml` (config)
- `package.json` (manifest)
- `tsconfig.json` (config)
- `types/tsconfig.json` (config)

## Top-level layout

- `src` — 23 analysed file(s)
- `(root files)` — 20 analysed file(s)
- `.github` — 7 analysed file(s)
- `other` — 4 analysed file(s)
- `tests` — 4 analysed file(s)
- `types` — 4 analysed file(s)
- `.codesandbox` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `20ce75f2907ca0e5c5a8ae595c0e9a4e368c7800` is the revision these paths and observations refer to.
