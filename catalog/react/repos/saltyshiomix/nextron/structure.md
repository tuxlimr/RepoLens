# Project structure: saltyshiomix/nextron

**Analysed commit:** `d128307b62cca08c3711a1556e0a0f564c5eb766`

**Commit reference:** [d128307b62cca08c3711a1556e0a0f564c5eb766](https://github.com/saltyshiomix/nextron/commit/d128307b62cca08c3711a1556e0a0f564c5eb766)

**Tree at this commit:** [saltyshiomix/nextron@d128307b62cc](https://github.com/saltyshiomix/nextron/tree/d128307b62cca08c3711a1556e0a0f564c5eb766)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | saltyshiomix/nextron |
| Description | ⚡ Next.js + Electron ⚡ |
| Stars | 4439 |
| Forks | 252 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `d128307b62cca08c3711a1556e0a0f564c5eb766` |
| Retrieved at | 2026-11-14T19:14:46.670754+00:00 |
| Files in this snapshot | 188 |

## Directory tree

```text
.github/  (1 files)
  FUNDING.yml
.vscode/  (1 files)
  settings.json
examples/  (151 files)
  _template/  (11 files)
    js/  (5 files)
      … 5 files under this directory
    ts/  (5 files)
      … 5 files under this directory
    gitignore.txt
  basic-lang-javascript/  (6 files)
    renderer/  (3 files)
      … 3 files under this directory
    README.md
    electron-builder.yml
    package.json
  basic-lang-typescript/  (9 files)
    renderer/  (5 files)
      … 5 files under this directory
    README.md
    electron-builder.yml
    package.json
    tsconfig.json
  basic-launch-app-from-url/  (11 files)
    main/  (2 files)
      … 2 files under this directory
    renderer/  (5 files)
      … 5 files under this directory
    README.md
    electron-builder.yml
    package.json
    tsconfig.json
  basic-store-data/  (10 files)
    main/  (1 files)
      … 1 files under this directory
    renderer/  (5 files)
      … 5 files under this directory
    README.md
    electron-builder.yml
    package.json
    tsconfig.json
  custom-build-options/  (10 files)
    renderer/  (5 files)
      … 5 files under this directory
    README.md
    electron-builder.prod.yml
    electron-builder.yml
    package.json
    tsconfig.json
  custom-renderer-port/  (9 files)
    renderer/  (5 files)
      … 5 files under this directory
    README.md
    electron-builder.yml
    package.json
    tsconfig.json
  with-ant-design/  (10 files)
    renderer/  (6 files)
      … 6 files under this directory
    README.md
    electron-builder.yml
    package.json
    tsconfig.json
  with-chakra-ui/  (17 files)
    renderer/  (13 files)
      … 13 files under this directory
    README.md
    electron-builder.yml
    package.json
    tsconfig.json
  with-emotion/  (14 files)
    renderer/  (10 files)
      … 10 files under this directory
    README.md
    electron-builder.yml
    package.json
    tsconfig.json
  with-material-ui/  (13 files)
    renderer/  (9 files)
      … 9 files under this directory
    README.md
    electron-builder.yml
    package.json
    tsconfig.json
  with-next-i18next/  (19 files)
    main/  (6 files)
      … 6 files under this directory
    renderer/  (9 files)
      … 9 files under this directory
    README.md
    electron-builder.yml
    next-i18next.config.cjs
    package.json
  with-tailwindcss/  (12 files)
    renderer/  (8 files)
      … 8 files under this directory
    README.md
    electron-builder.yml
    package.json
    tsconfig.json
lib/  (14 files)
  helpers/  (5 files)
    check-next-config.ts
    get-next-config.ts
    get-nextron-config.ts
    get-project-settings.ts
    load-script.ts
  webpack/  (5 files)
    development/  (2 files)
      … 2 files under this directory
    production/  (1 files)
      … 1 files under this directory
    get-base-config-main.ts
    get-base-config-preload.ts
  logger.ts
  nextron-build.ts
  nextron-dev.ts
  nextron.ts
scripts/  (4 files)
  detect-package-manager.ts
  dev.ts
  package.json
  tsconfig.json
.gitignore
.node-version
.prettierignore
.prettierrc.json
CHANGELOG.md
LICENSE
README.md
eslint.config.ts
lefthook.yaml
lerna.json
package.json
pnpm-workspace.yaml
tsconfig.base.json
tsconfig.json
tsconfig.nextron.json
tsdown.config.mts
types.d.ts
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 9 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 14 file(s) under lib package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 2 file(s) under scripts package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.prettierrc.json` (config)
- `.vscode/settings.json` (config)
- `examples/_template/js/.vscode/launch.json` (config)
- `examples/_template/js/.vscode/tasks.json` (config)
- `examples/_template/ts/.vscode/launch.json` (config)
- `examples/_template/ts/.vscode/tasks.json` (config)
- `examples/basic-lang-javascript/electron-builder.yml` (config)
- `examples/basic-lang-javascript/package.json` (manifest)
- `examples/basic-lang-typescript/electron-builder.yml` (config)
- `examples/basic-lang-typescript/package.json` (manifest)
- `examples/basic-lang-typescript/renderer/tsconfig.json` (config)
- `examples/basic-lang-typescript/tsconfig.json` (config)
- `examples/basic-launch-app-from-url/electron-builder.yml` (config)
- `examples/basic-launch-app-from-url/package.json` (manifest)
- `examples/basic-launch-app-from-url/renderer/tsconfig.json` (config)
- `examples/basic-launch-app-from-url/tsconfig.json` (config)
- `examples/basic-store-data/electron-builder.yml` (config)
- `examples/basic-store-data/package.json` (manifest)
- `examples/basic-store-data/renderer/tsconfig.json` (config)
- `examples/basic-store-data/tsconfig.json` (config)
- `examples/custom-build-options/electron-builder.prod.yml` (config)
- `examples/custom-build-options/electron-builder.yml` (config)
- `examples/custom-build-options/package.json` (manifest)
- `examples/custom-build-options/renderer/tsconfig.json` (config)
- `examples/custom-build-options/tsconfig.json` (config)
- `examples/custom-renderer-port/electron-builder.yml` (config)
- `examples/custom-renderer-port/package.json` (manifest)
- `examples/custom-renderer-port/renderer/tsconfig.json` (config)
- `examples/custom-renderer-port/tsconfig.json` (config)
- `examples/with-ant-design/electron-builder.yml` (config)
- `examples/with-ant-design/package.json` (manifest)
- `examples/with-ant-design/renderer/tsconfig.json` (config)
- `examples/with-ant-design/tsconfig.json` (config)
- `examples/with-chakra-ui/electron-builder.yml` (config)
- `examples/with-chakra-ui/package.json` (manifest)
- `examples/with-chakra-ui/renderer/tsconfig.json` (config)
- `examples/with-chakra-ui/tsconfig.json` (config)
- `examples/with-emotion/electron-builder.yml` (config)
- `examples/with-emotion/package.json` (manifest)
- `examples/with-emotion/renderer/tsconfig.json` (config)
- `examples/with-emotion/tsconfig.json` (config)
- `examples/with-material-ui/electron-builder.yml` (config)
- `examples/with-material-ui/package.json` (manifest)
- `examples/with-material-ui/renderer/tsconfig.json` (config)
- `examples/with-material-ui/tsconfig.json` (config)
- `examples/with-next-i18next/electron-builder.yml` (config)
- `examples/with-next-i18next/package.json` (manifest)
- `examples/with-next-i18next/renderer/public/locales/de/common.json` (config)
- `examples/with-next-i18next/renderer/public/locales/en/common.json` (config)
- `examples/with-tailwindcss/electron-builder.yml` (config)
- `examples/with-tailwindcss/package.json` (manifest)
- `examples/with-tailwindcss/renderer/tsconfig.json` (config)
- `examples/with-tailwindcss/tsconfig.json` (config)
- `lefthook.yaml` (config)
- `lerna.json` (config)
- `package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `scripts/package.json` (manifest)
- `scripts/tsconfig.json` (config)
- `tsconfig.base.json` (config)
- `tsconfig.json` (config)
- `tsconfig.nextron.json` (config)

## Top-level layout

- `examples` — 151 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `lib` — 14 analysed file(s)
- `scripts` — 4 analysed file(s)
- `.github` — 1 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `d128307b62cca08c3711a1556e0a0f564c5eb766` is the revision these paths and observations refer to.
