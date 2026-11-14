# Project structure: react-grid-layout/react-grid-layout

**Analysed commit:** `f0dd77c5b2fee2d2cb09541d220c00d6814c7242`

**Commit reference:** [f0dd77c5b2fee2d2cb09541d220c00d6814c7242](https://github.com/react-grid-layout/react-grid-layout/commit/f0dd77c5b2fee2d2cb09541d220c00d6814c7242)

**Tree at this commit:** [react-grid-layout/react-grid-layout@f0dd77c5b2fe](https://github.com/react-grid-layout/react-grid-layout/tree/f0dd77c5b2fee2d2cb09541d220c00d6814c7242)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | react-grid-layout/react-grid-layout |
| Description | A draggable and resizable grid layout with responsive breakpoints, for React. |
| Stars | 22492 |
| Forks | 2697 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `f0dd77c5b2fee2d2cb09541d220c00d6814c7242` |
| Retrieved at | 2026-11-14T19:13:08.400241+00:00 |
| Files in this snapshot | 562 |

## Directory tree

```text
.claude/  (2 files)
  commands/  (1 files)
    fix-issue.md
  skills/  (1 files)
    fix-issue.md
.github/  (15 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.yml
    config.yml
  workflows/  (9 files)
    audit.yml
    changelog.yml
    frames.yml
    gh-pages.yml
    label.yml
    lint.yml
    release.yml
    stale.yml
    test.yml
  PULL_REQUEST_TEMPLATE.md
  changelog-configuration.json
  labeler.yml
  release.yml
.husky/  (2 files)
  .gitignore
  pre-commit
.out-of-scope/  (2 files)
  drop-target-threshold.md
  resize-neighbors.md
__mocks__/  (1 files)
  react-grid-layout.js
codemaps/  (4 files)
  architecture.md
  backend.md
  data.md
  frontend.md
css/  (1 files)
  styles.css
docs/  (1 files)
  warnings.md
examples/  (4 files)
  util/  (4 files)
    example-styles.css
    generate.js
    template.ejs
    vars.js
rfcs/  (2 files)
  0001-v2-typescript-rewrite.md
  0002-pluggable-constraints.md
scripts/  (2 files)
  check-release.cjs
  record-playwright-frames.cjs
src/  (43 files)
  core/  (19 files)
    compaction/  (2 files)
      … 2 files under this directory
    geometry/  (3 files)
      … 3 files under this directory
    interaction/  (2 files)
      … 2 files under this directory
    calculate.ts
    collision.ts
    compactors.ts
    constraints.ts
    dev.ts
    index.ts
    layout.ts
    position.ts
    responsive.ts
    sort.ts
    types.ts
    validation.ts
  extras/  (5 files)
    GridBackground.tsx
    fastHorizontalCompactor.ts
    fastVerticalCompactor.ts
    index.ts
    wrapCompactor.ts
  legacy/  (4 files)
    ReactGridLayout.tsx
    ResponsiveReactGridLayout.tsx
    WidthProvider.tsx
    index.ts
  react/  (14 files)
    components/  (8 files)
      … 8 files under this directory
    hooks/  (4 files)
      … 4 files under this directory
    types/  (1 files)
      … 1 files under this directory
    index.ts
  index.ts
test/  (456 files)
  bench/  (9 files)
    README.md
    baseline.json
    counters.ts
    instrument.cjs
    nonfinite.bench-test.ts
    opcounts.bench-test.ts
    scenarios.ts
    security-scenarios.ts
    security.bench-test.ts
  e2e/  (102 files)
    __frames__/  (93 files)
      … 93 files under this directory
    dist.spec.ts
    grid-smoke.spec.ts
    harness-app.jsx
    known-browser-divergences.json
    live-interaction.spec.ts
    scenarioDriver.ts
    scenarios.spec.ts
    touch-drop.spec.ts
    webpack.harness.config.js
  examples/  (23 files)
    00-showcase.jsx
    01-basic.jsx
    02-no-dragging.jsx
    03-messy.jsx
    04-grid-property.jsx
    05-static-elements.jsx
    06-dynamic-add-remove.jsx
    07-localstorage.jsx
    08-localstorage-responsive.jsx
    09-min-max-wh.jsx
    10-dynamic-min-max-wh.jsx
    11-toolbox.jsx
    12-drag-from-outside.jsx
    13-bounded.jsx
    14-responsive-bootstrap-style.jsx
    15-scale.jsx
    16-allow-overlap.jsx
    17-resizable-handles.jsx
    18-compactors.jsx
    19-constraints.jsx
    20-aspect-ratio.jsx
    21-custom-constraints.jsx
    test_demo.jsx
  golden/  (90 files)
    __golden__/  (72 files)
      … 72 files under this directory
    cases/  (12 files)
      … 12 files under this directory
    README.md
    capture.ts
    expectGolden.ts
    generators.ts
    rng.ts
    serialize.ts
  golden-react/  (173 files)
    __golden__/  (158 files)
      … 158 files under this directory
    scenarios/  (4 files)
      … 4 files under this directory
    README.md
    drop.ts
    expectGolden.ts
    fixture.tsx
    formatTrace.ts
    geometry.ts
    hookHarness.tsx
    pointer.ts
    recorder.ts
    scenarioDefinitions.ts
    verification.md
  spec/  (52 files)
    __snapshots__/  (1 files)
      … 1 files under this directory
    helpers/  (1 files)
      … 1 files under this directory
    oracles/  (5 files)
      … 5 files under this directory
    backcompat-test.js
    benchmark-test.js
    bounds-regressions-test.tsx
    classic-compaction-differential-test.ts
    compactor-resync-test.tsx
    compactors-test.ts
    constraints-test.ts
    core-functions-test.ts
    correct-bounds-differential-test.ts
    correct-bounds-sweep-test.ts
    dev-warnings-test.tsx
    drag-resolution-test.ts
    drag-stop-race-test.tsx
    drop-alignment.test.ts
    drop-edge-scroll-test.tsx
    drop-placeholder-ports-test.tsx
    edgeScroll-test.ts
    external-drop-push-test.tsx
    fast-compactor-test.js
    fast-horizontal-compaction-differential-test.ts
    fast-horizontal-compactor-test.js
    hooks-test.tsx
    layout-input-test.tsx
    lifecycle-test.js
    … 21 more files
  util/  (3 files)
    deepFreeze.js
    examples-server.cjs
    setupTests.js
  dev-hook.jsx
  jest.bench.cjs
  jest.ops.cjs
  test-hook.jsx
.babelrc.js
.browserslistrc
.coderabbit.yaml
.gitignore
.graphifyignore
.npmignore
.prettierignore
.prettierrc
.yarnrc.yml
AGENTS.md
CHANGELOG.md
CLAUDE.md
LICENSE
Makefile
README.md
eslint.config.mjs
index-dev.html
index-dev.js
index.html
index.js
index.js.flow
package.json
playwright.config.ts
tsconfig.json
… 3 more files
```

## Entry points

- [index.js](https://github.com/react-grid-layout/react-grid-layout/blob/f0dd77c5b2fee2d2cb09541d220c00d6814c7242/index.js)
- [src/core/index.ts](https://github.com/react-grid-layout/react-grid-layout/blob/f0dd77c5b2fee2d2cb09541d220c00d6814c7242/src/core/index.ts)
- [src/extras/index.ts](https://github.com/react-grid-layout/react-grid-layout/blob/f0dd77c5b2fee2d2cb09541d220c00d6814c7242/src/extras/index.ts)
- [src/index.ts](https://github.com/react-grid-layout/react-grid-layout/blob/f0dd77c5b2fee2d2cb09541d220c00d6814c7242/src/index.ts)
- [src/legacy/index.ts](https://github.com/react-grid-layout/react-grid-layout/blob/f0dd77c5b2fee2d2cb09541d220c00d6814c7242/src/legacy/index.ts)
- [src/react/components/index.ts](https://github.com/react-grid-layout/react-grid-layout/blob/f0dd77c5b2fee2d2cb09541d220c00d6814c7242/src/react/components/index.ts)
- [src/react/hooks/index.ts](https://github.com/react-grid-layout/react-grid-layout/blob/f0dd77c5b2fee2d2cb09541d220c00d6814c7242/src/react/hooks/index.ts)
- [src/react/index.ts](https://github.com/react-grid-layout/react-grid-layout/blob/f0dd77c5b2fee2d2cb09541d220c00d6814c7242/src/react/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 7 file(s) under core modules (observed from repository paths and static analysis). |
| extras package | library | Observed | Groups 5 file(s) under extras package (observed from repository paths and static analysis). |
| index.ts package | library | Observed | Groups 1 file(s) under index.ts package (observed from repository paths and static analysis). |
| legacy package | library | Observed | Groups 4 file(s) under legacy package (observed from repository paths and static analysis). |
| __mocks__ package | library | Observed | Groups 1 file(s) under __mocks__ package (observed from repository paths and static analysis). |
| react package | library | Observed | Groups 14 file(s) under react package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 2 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 19 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 456 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.coderabbit.yaml` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/changelog-configuration.json` (config)
- `.github/labeler.yml` (config)
- `.github/release.yml` (config)
- `.github/workflows/audit.yml` (ci)
- `.github/workflows/changelog.yml` (ci)
- `.github/workflows/frames.yml` (ci)
- `.github/workflows/gh-pages.yml` (ci)
- `.github/workflows/label.yml` (ci)
- `.github/workflows/lint.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/stale.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `.yarnrc.yml` (config)
- `package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `test` — 456 analysed file(s)
- `src` — 43 analysed file(s)
- `(root files)` — 27 analysed file(s)
- `.github` — 15 analysed file(s)
- `codemaps` — 4 analysed file(s)
- `examples` — 4 analysed file(s)
- `.claude` — 2 analysed file(s)
- `.husky` — 2 analysed file(s)
- `.out-of-scope` — 2 analysed file(s)
- `rfcs` — 2 analysed file(s)
- `scripts` — 2 analysed file(s)
- `__mocks__` — 1 analysed file(s)
- `css` — 1 analysed file(s)
- `docs` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `f0dd77c5b2fee2d2cb09541d220c00d6814c7242` is the revision these paths and observations refer to.
