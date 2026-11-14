# Project structure: stitchesjs/stitches

**Analysed commit:** `50fd8a1adc6360340fe348a8b3ebc8b06d38e230`

**Commit reference:** [50fd8a1adc6360340fe348a8b3ebc8b06d38e230](https://github.com/stitchesjs/stitches/commit/50fd8a1adc6360340fe348a8b3ebc8b06d38e230)

**Tree at this commit:** [stitchesjs/stitches@50fd8a1adc63](https://github.com/stitchesjs/stitches/tree/50fd8a1adc6360340fe348a8b3ebc8b06d38e230)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | stitchesjs/stitches |
| Description | [Not Actively Maintained] CSS-in-JS with near-zero runtime, SSR, multi-variant support, and a best-in-class developer experience. |
| Stars | 7758 |
| Forks | 250 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | canary |
| Analysed commit | `50fd8a1adc6360340fe348a8b3ebc8b06d38e230` |
| Retrieved at | 2026-11-14T19:13:49.181129+00:00 |
| Files in this snapshot | 174 |

## Directory tree

```text
.codesandbox/  (1 files)
  ci.json
.github/  (4 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (1 files)
    test.yml
  CODEOWNERS
.task/  (23 files)
  internal/  (14 files)
    child_process.js
    color.js
    dirs.js
    expect.js
    fs-test.js
    fs.js
    js.js
    js.transformDestructuring.js
    js.transformIIFE.js
    js.transformModulesToCJS.js
    js.transformOptionalCatchToParam.js
    process.js
    readline.js
    url.js
  build-csstype.js
  build.js
  lint-esm.js
  lint-pkg.js
  lint-tsc.js
  lint.js
  release.js
  test-coverage.js
  test.js
.vscode/  (2 files)
  package.schema.json
  settings.json
packages/  (135 files)
  core/  (69 files)
    src/  (27 files)
      … 27 files under this directory
    tests/  (33 files)
      … 33 files under this directory
    types/  (7 files)
      … 7 files under this directory
    README.md
    package.json
  react/  (35 files)
    src/  (4 files)
      … 4 files under this directory
    tests/  (22 files)
      … 22 files under this directory
    types/  (7 files)
      … 7 files under this directory
    README.md
    package.json
  stringify/  (14 files)
    src/  (4 files)
      … 4 files under this directory
    tests/  (7 files)
      … 7 files under this directory
    types/  (1 files)
      … 1 files under this directory
    README.md
    package.json
  test/  (17 files)
    built-types/  (7 files)
      … 7 files under this directory
    .eslintrc
    Issue-803-core.ts
    Issue-803-react.ts
    Issue-813-core.ts
    Issue-813-react.ts
    index.tsx
    issue-749-react.tsx
    package.json
    stitches.config.ts
    tsconfig.json
.editorconfig
.gitignore
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE.md
README.md
package.json
tsconfig.json
tslint.json
```

## Entry points

- [packages/core/src/index.js](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/core/src/index.js)
- [packages/react/src/index.js](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/react/src/index.js)
- [packages/stringify/src/index.js](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/stringify/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 16 file(s) under packages package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 34 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 79 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.codesandbox/ci.json` (config)
- `.editorconfig` (config)
- `.github/workflows/test.yml` (ci)
- `.vscode/package.schema.json` (config)
- `.vscode/settings.json` (config)
- `package.json` (manifest)
- `packages/core/package.json` (manifest)
- `packages/react/package.json` (manifest)
- `packages/stringify/package.json` (manifest)
- `tsconfig.json` (config)
- `tslint.json` (config)

## Top-level layout

- `packages` — 135 analysed file(s)
- `.task` — 23 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `.github` — 4 analysed file(s)
- `.vscode` — 2 analysed file(s)
- `.codesandbox` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `50fd8a1adc6360340fe348a8b3ebc8b06d38e230` is the revision these paths and observations refer to.
