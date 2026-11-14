# Project structure: xnimorz/use-debounce

**Analysed commit:** `771f915e21bf5d8f4cab626b6cb7bebbec2681fb`

**Commit reference:** [771f915e21bf5d8f4cab626b6cb7bebbec2681fb](https://github.com/xnimorz/use-debounce/commit/771f915e21bf5d8f4cab626b6cb7bebbec2681fb)

**Tree at this commit:** [xnimorz/use-debounce@771f915e21bf](https://github.com/xnimorz/use-debounce/tree/771f915e21bf5d8f4cab626b6cb7bebbec2681fb)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | xnimorz/use-debounce |
| Description | A debounce hook for react |
| Stars | 3381 |
| Forks | 119 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `771f915e21bf5d8f4cab626b6cb7bebbec2681fb` |
| Retrieved at | 2026-11-14T19:15:21.463804+00:00 |
| Files in this snapshot | 20 |

## Directory tree

```text
.github/  (3 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (1 files)
    main.yml
src/  (4 files)
  index.ts
  useDebounce.ts
  useDebouncedCallback.ts
  useThrottledCallback.ts
test/  (3 files)
  useDebounce.test.tsx
  useDebouncedCallback.test.tsx
  useThrottledCallback.test.tsx
.eslintrc
.gitignore
.prettierrc
CHANGELOG.md
LICENSE
README.md
jest.config.js
package.json
setupTests.ts
tsconfig.json
```

## Entry points

- [src/index.ts](https://github.com/xnimorz/use-debounce/blob/771f915e21bf5d8f4cab626b6cb7bebbec2681fb/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| index.ts package | library | Observed | Groups 1 file(s) under index.ts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 3 file(s) under tests (observed from repository paths and static analysis). |
| useDebounce.ts package | library | Observed | Groups 1 file(s) under usedebounce.ts package (observed from repository paths and static analysis). |
| useDebouncedCallback.ts package | library | Observed | Groups 1 file(s) under usedebouncedcallback.ts package (observed from repository paths and static analysis). |
| useThrottledCallback.ts package | library | Observed | Groups 1 file(s) under usethrottledcallback.ts package (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/main.yml` (ci)
- `package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `(root files)` — 10 analysed file(s)
- `src` — 4 analysed file(s)
- `.github` — 3 analysed file(s)
- `test` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `771f915e21bf5d8f4cab626b6cb7bebbec2681fb` is the revision these paths and observations refer to.
