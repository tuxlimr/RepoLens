# Project structure: tomkp/react-split-pane

**Analysed commit:** `594b0cb35189975a2b760459120f8dd4c6ab3307`

**Commit reference:** [594b0cb35189975a2b760459120f8dd4c6ab3307](https://github.com/tomkp/react-split-pane/commit/594b0cb35189975a2b760459120f8dd4c6ab3307)

**Tree at this commit:** [tomkp/react-split-pane@594b0cb35189](https://github.com/tomkp/react-split-pane/tree/594b0cb35189975a2b760459120f8dd4c6ab3307)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | tomkp/react-split-pane |
| Description | React split-pane component |
| Stars | 3386 |
| Forks | 407 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `594b0cb35189975a2b760459120f8dd4c6ab3307` |
| Retrieved at | 2026-11-14T19:15:20.991327+00:00 |
| Files in this snapshot | 53 |

## Directory tree

```text
.github/  (5 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    feature_request.md
    pull_request_template.md
  workflows/  (2 files)
    build-test.yml
    deploy-examples.yml
examples/  (10 files)
  BasicExample.tsx
  ControlledExample.tsx
  NestedExample.tsx
  PercentageExample.tsx
  SnapPointsExample.tsx
  StyledExample.tsx
  index.html
  main.tsx
  styles.css
  vite.config.ts
src/  (21 files)
  components/  (4 files)
    Divider.tsx
    Pane.tsx
    SplitPane.test.tsx
    SplitPane.tsx
  hooks/  (4 files)
    useKeyboardResize.test.ts
    useKeyboardResize.ts
    useResizer.test.ts
    useResizer.ts
  test/  (1 files)
    setup.ts
  types/  (1 files)
    index.ts
  utils/  (7 files)
    accessibility.test.ts
    accessibility.ts
    calculations.test.ts
    calculations.ts
    classNames.test.ts
    classNames.ts
    useIsomorphicLayoutEffect.ts
  index.ts
  keyboard.ts
  persistence.test.ts
  persistence.ts
.editorconfig
.gitignore
.prettierignore
.prettierrc
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
MIGRATION.md
README.md
TAILWIND.md
eslint.config.js
package.json
rollup.config.mjs
styles.css
tsconfig.json
vitest.config.ts
```

## Entry points

- [src/index.ts](https://github.com/tomkp/react-split-pane/blob/594b0cb35189975a2b760459120f8dd4c6ab3307/src/index.ts)
- [src/types/index.ts](https://github.com/tomkp/react-split-pane/blob/594b0cb35189975a2b760459120f8dd4c6ab3307/src/types/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| components package | library | Observed | Groups 4 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 4 file(s) under hooks package (observed from repository paths and static analysis). |
| index.ts package | library | Observed | Groups 1 file(s) under index.ts package (observed from repository paths and static analysis). |
| keyboard.ts package | library | Observed | Groups 1 file(s) under keyboard.ts package (observed from repository paths and static analysis). |
| persistence.test.ts package | library | Observed | Groups 1 file(s) under persistence.test.ts package (observed from repository paths and static analysis). |
| persistence.ts package | library | Observed | Groups 1 file(s) under persistence.ts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 1 file(s) under types package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 7 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/workflows/build-test.yml` (ci)
- `.github/workflows/deploy-examples.yml` (ci)
- `package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `src` — 21 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `examples` — 10 analysed file(s)
- `.github` — 5 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `594b0cb35189975a2b760459120f8dd4c6ab3307` is the revision these paths and observations refer to.
