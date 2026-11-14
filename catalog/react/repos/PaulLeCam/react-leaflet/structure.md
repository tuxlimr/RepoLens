# Project structure: PaulLeCam/react-leaflet

**Analysed commit:** `374882f6b73bb741785968be6d81257767da366d`

**Commit reference:** [374882f6b73bb741785968be6d81257767da366d](https://github.com/PaulLeCam/react-leaflet/commit/374882f6b73bb741785968be6d81257767da366d)

**Tree at this commit:** [PaulLeCam/react-leaflet@374882f6b73b](https://github.com/PaulLeCam/react-leaflet/tree/374882f6b73bb741785968be6d81257767da366d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | PaulLeCam/react-leaflet |
| Description | React components for Leaflet maps |
| Stars | 5609 |
| Forks | 897 |
| Licence | Other |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `374882f6b73bb741785968be6d81257767da366d` |
| Retrieved at | 2026-11-14T19:14:16.032025+00:00 |
| Files in this snapshot | 94 |

## Directory tree

```text
.github/  (2 files)
  ISSUE_TEMPLATE/  (1 files)
    bug-report-v5.md
  workflows/  (1 files)
    main.yml
example/  (5 files)
  App.tsx
  index.css
  index.html
  main.tsx
  package.json
packages/  (75 files)
  core/  (35 files)
    __tests__/  (14 files)
      … 14 files under this directory
    src/  (16 files)
      … 16 files under this directory
    .gitignore
    LICENSE.md
    README.md
    package.json
    tsconfig.json
  react-leaflet/  (40 files)
    __tests__/  (12 files)
      … 12 files under this directory
    src/  (24 files)
      … 24 files under this directory
    LICENSE.md
    README.md
    package.json
    tsconfig.json
.gitignore
.swcrc
CHANGELOG.md
CONTRIBUTING.md
LICENSE.md
README.md
biome.json
package.json
pnpm-workspace.yaml
tsconfig.build.json
tsconfig.json
turbo.json
```

## Entry points

- [packages/core/src/index.ts](https://github.com/PaulLeCam/react-leaflet/blob/374882f6b73bb741785968be6d81257767da366d/packages/core/src/index.ts)
- [packages/react-leaflet/src/index.ts](https://github.com/PaulLeCam/react-leaflet/blob/374882f6b73bb741785968be6d81257767da366d/packages/react-leaflet/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 10 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 30 file(s) under packages package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 30 file(s) under service / domain layer (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/main.yml` (ci)
- `biome.json` (config)
- `example/package.json` (manifest)
- `package.json` (manifest)
- `packages/core/package.json` (manifest)
- `packages/core/tsconfig.json` (config)
- `packages/react-leaflet/package.json` (manifest)
- `packages/react-leaflet/tsconfig.json` (config)
- `pnpm-workspace.yaml` (config)
- `tsconfig.build.json` (config)
- `tsconfig.json` (config)
- `turbo.json` (config)

## Top-level layout

- `packages` — 75 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `example` — 5 analysed file(s)
- `.github` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `374882f6b73bb741785968be6d81257767da366d` is the revision these paths and observations refer to.
