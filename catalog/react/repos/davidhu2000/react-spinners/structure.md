# Project structure: davidhu2000/react-spinners

**Analysed commit:** `5525bb2d1062882e7f46e9ff7929407883f75a1b`

**Commit reference:** [5525bb2d1062882e7f46e9ff7929407883f75a1b](https://github.com/davidhu2000/react-spinners/commit/5525bb2d1062882e7f46e9ff7929407883f75a1b)

**Tree at this commit:** [davidhu2000/react-spinners@5525bb2d1062](https://github.com/davidhu2000/react-spinners/tree/5525bb2d1062882e7f46e9ff7929407883f75a1b)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | davidhu2000/react-spinners |
| Description | A collection of loading spinner components for react |
| Stars | 3356 |
| Forks | 281 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `5525bb2d1062882e7f46e9ff7929407883f75a1b` |
| Retrieved at | 2026-11-14T19:15:22.161001+00:00 |
| Files in this snapshot | 88 |

## Directory tree

```text
.github/  (7 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  actions/  (1 files)
    setup-node/  (1 files)
      … 1 files under this directory
  workflows/  (2 files)
    deploy.yml
    publish.yml
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
.storybook/  (5 files)
  canonical-link/  (1 files)
    register.js
  google-analytics-v4/  (1 files)
    register.js
  main.js
  manager.js
  preview.js
.vscode/  (1 files)
  settings.json
examples/  (12 files)
  components/  (7 files)
    ColorPicker.tsx
    Controls.tsx
    Icons.tsx
    InstallCommand.tsx
    SpinnerCard.tsx
    ThemeToggle.tsx
    index.ts
  index.html
  index.tsx
  loaderProps.ts
  styles.css
  useCopied.ts
scripts/  (4 files)
  build-docs.sh
  mod.rb
  stories.rb
  stories.template
src/  (32 files)
  helpers/  (8 files)
    animation.server.test.ts
    animation.test.ts
    animation.ts
    colors.test.ts
    colors.ts
    props.ts
    unitConverter.test.ts
    unitConverter.ts
  BarLoader.tsx
  BeatLoader.tsx
  BounceLoader.tsx
  CircleLoader.tsx
  ClimbingBoxLoader.tsx
  ClipLoader.tsx
  ClockLoader.tsx
  DotLoader.tsx
  FadeLoader.tsx
  GridLoader.tsx
  HashLoader.tsx
  MoonLoader.tsx
  PacmanLoader.tsx
  PropagateLoader.tsx
  PuffLoader.tsx
  PulseLoader.tsx
  RingLoader.tsx
  RiseLoader.tsx
  RotateLoader.tsx
  ScaleLoader.tsx
  SkewLoader.tsx
  SquareLoader.tsx
  SyncLoader.tsx
  index.ts
stories/  (1 files)
  .keep
test-apps/  (6 files)
  nextjs/  (6 files)
    src/  (2 files)
      … 2 files under this directory
    .gitignore
    next.config.ts
    package.json
    tsconfig.json
tests/  (2 files)
  AllLoaders.test.tsx
  HashLoader.test.tsx
.gitignore
.npmignore
.prettierignore
.prettierrc.cjs
.yarnrc.yml
CHANGELOG.md
CODEOWNERS
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
eslint.config.mjs
jest.config.js
package.json
tsconfig.cjs.json
tsconfig.esm.json
tsconfig.json
vite.config.mjs
```

## Entry points

- [.storybook/main.js](https://github.com/davidhu2000/react-spinners/blob/5525bb2d1062882e7f46e9ff7929407883f75a1b/.storybook/main.js)
- [src/index.ts](https://github.com/davidhu2000/react-spinners/blob/5525bb2d1062882e7f46e9ff7929407883f75a1b/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| BarLoader.tsx package | library | Observed | Groups 1 file(s) under barloader.tsx package (observed from repository paths and static analysis). |
| BeatLoader.tsx package | library | Observed | Groups 1 file(s) under beatloader.tsx package (observed from repository paths and static analysis). |
| BounceLoader.tsx package | library | Observed | Groups 1 file(s) under bounceloader.tsx package (observed from repository paths and static analysis). |
| CircleLoader.tsx package | library | Observed | Groups 1 file(s) under circleloader.tsx package (observed from repository paths and static analysis). |
| ClimbingBoxLoader.tsx package | library | Observed | Groups 1 file(s) under climbingboxloader.tsx package (observed from repository paths and static analysis). |
| ClipLoader.tsx package | library | Observed | Groups 1 file(s) under cliploader.tsx package (observed from repository paths and static analysis). |
| ClockLoader.tsx package | library | Observed | Groups 1 file(s) under clockloader.tsx package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| DotLoader.tsx package | library | Observed | Groups 1 file(s) under dotloader.tsx package (observed from repository paths and static analysis). |
| FadeLoader.tsx package | library | Observed | Groups 1 file(s) under fadeloader.tsx package (observed from repository paths and static analysis). |
| GridLoader.tsx package | library | Observed | Groups 1 file(s) under gridloader.tsx package (observed from repository paths and static analysis). |
| HashLoader.tsx package | library | Observed | Groups 1 file(s) under hashloader.tsx package (observed from repository paths and static analysis). |
| helpers package | library | Observed | Groups 8 file(s) under helpers package (observed from repository paths and static analysis). |
| index.ts package | library | Observed | Groups 1 file(s) under index.ts package (observed from repository paths and static analysis). |
| MoonLoader.tsx package | library | Observed | Groups 1 file(s) under moonloader.tsx package (observed from repository paths and static analysis). |
| PacmanLoader.tsx package | library | Observed | Groups 1 file(s) under pacmanloader.tsx package (observed from repository paths and static analysis). |
| PropagateLoader.tsx package | library | Observed | Groups 1 file(s) under propagateloader.tsx package (observed from repository paths and static analysis). |
| PuffLoader.tsx package | library | Observed | Groups 1 file(s) under puffloader.tsx package (observed from repository paths and static analysis). |
| PulseLoader.tsx package | library | Observed | Groups 1 file(s) under pulseloader.tsx package (observed from repository paths and static analysis). |
| RingLoader.tsx package | library | Observed | Groups 1 file(s) under ringloader.tsx package (observed from repository paths and static analysis). |
| RiseLoader.tsx package | library | Observed | Groups 1 file(s) under riseloader.tsx package (observed from repository paths and static analysis). |
| RotateLoader.tsx package | library | Observed | Groups 1 file(s) under rotateloader.tsx package (observed from repository paths and static analysis). |
| ScaleLoader.tsx package | library | Observed | Groups 1 file(s) under scaleloader.tsx package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 3 file(s) under scripts package (observed from repository paths and static analysis). |
| SkewLoader.tsx package | library | Observed | Groups 1 file(s) under skewloader.tsx package (observed from repository paths and static analysis). |
| SquareLoader.tsx package | library | Observed | Groups 1 file(s) under squareloader.tsx package (observed from repository paths and static analysis). |
| SyncLoader.tsx package | library | Observed | Groups 1 file(s) under syncloader.tsx package (observed from repository paths and static analysis). |
| test-apps package | library | Observed | Groups 3 file(s) under test-apps package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 2 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/actions/setup-node/action.yaml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/deploy.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.vscode/settings.json` (config)
- `.yarnrc.yml` (config)
- `package.json` (manifest)
- `test-apps/nextjs/package.json` (manifest)
- `test-apps/nextjs/tsconfig.json` (config)
- `tsconfig.cjs.json` (config)
- `tsconfig.esm.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `src` — 32 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `examples` — 12 analysed file(s)
- `.github` — 7 analysed file(s)
- `test-apps` — 6 analysed file(s)
- `.storybook` — 5 analysed file(s)
- `scripts` — 4 analysed file(s)
- `tests` — 2 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `stories` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `5525bb2d1062882e7f46e9ff7929407883f75a1b` is the revision these paths and observations refer to.
