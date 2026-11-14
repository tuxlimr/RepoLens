# Project structure: danilowoz/react-content-loader

**Analysed commit:** `c8a6b6c6669d7e663f9d7e1efecec08e876b0e5d`

**Commit reference:** [c8a6b6c6669d7e663f9d7e1efecec08e876b0e5d](https://github.com/danilowoz/react-content-loader/commit/c8a6b6c6669d7e663f9d7e1efecec08e876b0e5d)

**Tree at this commit:** [danilowoz/react-content-loader@c8a6b6c6669d](https://github.com/danilowoz/react-content-loader/tree/c8a6b6c6669d7e663f9d7e1efecec08e876b0e5d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | danilowoz/react-content-loader |
| Description | ⚪ SVG-Powered component to easily create skeleton loadings. |
| Stars | 13997 |
| Forks | 421 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `c8a6b6c6669d7e663f9d7e1efecec08e876b0e5d` |
| Retrieved at | 2026-11-14T19:13:17.554079+00:00 |
| Files in this snapshot | 74 |

## Directory tree

```text
.codesandbox/  (1 files)
  tasks.json
.devcontainer/  (1 files)
  devcontainer.json
.github/  (6 files)
  workflows/  (2 files)
    ci.yml
    release.yml
  FUNDING.yml
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
.storybook/  (3 files)
  main.ts
  preview-head.html
  preview.tsx
__mocks__/  (1 files)
  react-native-svg.js
docs/  (1 files)
  index.stories.tsx
src/  (48 files)
  native/  (23 files)
    __tests__/  (14 files)
      … 14 files under this directory
    presets/  (5 files)
      … 5 files under this directory
    ContentLoader.tsx
    Svg.tsx
    index.ts
    package.json
  shared/  (1 files)
    uid.ts
  web/  (24 files)
    __tests__/  (16 files)
      … 16 files under this directory
    presets/  (5 files)
      … 5 files under this directory
    ContentLoader.tsx
    Svg.tsx
    index.ts
.gitignore
.prettierrc.js
CODE_OF_CONDUCT.md
LICENSE
README.md
babel.config.js
jest.native.config.js
jest.web.config.js
package.json
rollup.config.js
tsconfig.base.json
tsconfig.json
tsconfig.test.json
```

## Entry points

- [.storybook/main.ts](https://github.com/danilowoz/react-content-loader/blob/c8a6b6c6669d7e663f9d7e1efecec08e876b0e5d/.storybook/main.ts)
- [src/native/index.ts](https://github.com/danilowoz/react-content-loader/blob/c8a6b6c6669d7e663f9d7e1efecec08e876b0e5d/src/native/index.ts)
- [src/web/index.ts](https://github.com/danilowoz/react-content-loader/blob/c8a6b6c6669d7e663f9d7e1efecec08e876b0e5d/src/web/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| __mocks__ package | library | Observed | Groups 1 file(s) under __mocks__ package (observed from repository paths and static analysis). |
| native package | library | Observed | Groups 16 file(s) under native package (observed from repository paths and static analysis). |
| shared package | library | Observed | Groups 1 file(s) under shared package (observed from repository paths and static analysis). |
| web package | library | Observed | Groups 18 file(s) under web package (observed from repository paths and static analysis). |

## Important files

- `.codesandbox/tasks.json` (config)
- `.devcontainer/devcontainer.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `package.json` (manifest)
- `src/native/package.json` (manifest)
- `tsconfig.base.json` (config)
- `tsconfig.json` (config)
- `tsconfig.test.json` (config)

## Top-level layout

- `src` — 48 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `.github` — 6 analysed file(s)
- `.storybook` — 3 analysed file(s)
- `.codesandbox` — 1 analysed file(s)
- `.devcontainer` — 1 analysed file(s)
- `__mocks__` — 1 analysed file(s)
- `docs` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `c8a6b6c6669d7e663f9d7e1efecec08e876b0e5d` is the revision these paths and observations refer to.
