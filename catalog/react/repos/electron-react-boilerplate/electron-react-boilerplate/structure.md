# Project structure: electron-react-boilerplate/electron-react-boilerplate

**Analysed commit:** `e5b8242d8b21a4290c3a1f18ae3b64167e9de04a`

**Commit reference:** [e5b8242d8b21a4290c3a1f18ae3b64167e9de04a](https://github.com/electron-react-boilerplate/electron-react-boilerplate/commit/e5b8242d8b21a4290c3a1f18ae3b64167e9de04a)

**Tree at this commit:** [electron-react-boilerplate/electron-react-boilerplate@e5b8242d8b21](https://github.com/electron-react-boilerplate/electron-react-boilerplate/tree/e5b8242d8b21a4290c3a1f18ae3b64167e9de04a)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | electron-react-boilerplate/electron-react-boilerplate |
| Description | A Foundation for Scalable Cross-Platform Apps |
| Stars | 24250 |
| Forks | 3948 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `e5b8242d8b21a4290c3a1f18ae3b64167e9de04a` |
| Retrieved at | 2026-11-14T19:13:06.155761+00:00 |
| Files in this snapshot | 53 |

## Directory tree

```text
.erb/  (13 files)
  configs/  (1 files)
    paths.ts
  img/  (2 files)
    erb-banner.svg
    palette-sponsor-banner.svg
  mocks/  (2 files)
    fileMock.js
    svgComponentMock.js
  scripts/  (6 files)
    check-build-exists.ts
    electron-rebuild.js
    link-modules.ts
    notarize.js
    register.cjs
    smoke-test.cjs
  tooling/  (2 files)
    README.md
    package.json
.github/  (9 files)
  ISSUE_TEMPLATE/  (3 files)
    1-Bug_report.md
    2-Question.md
    3-Feature_request.md
  workflows/  (3 files)
    codeql-analysis.yml
    publish.yml
    test.yml
  FUNDING.yml
  config.yml
  stale.yml
.vscode/  (3 files)
  extensions.json
  launch.json
  settings.json
assets/  (3 files)
  assets.d.ts
  entitlements.mac.plist
  icon.svg
release/  (1 files)
  app/  (1 files)
    package.json
src/  (12 files)
  __tests__/  (2 files)
    App.test.tsx
    updates.test.ts
  main/  (5 files)
    main.ts
    menu.ts
    preload.ts
    updates.ts
    util.ts
  renderer/  (5 files)
    App.css
    App.tsx
    index.html
    index.tsx
    preload.d.ts
.editorconfig
.gitattributes
.gitignore
CHANGELOG.md
CODE_OF_CONDUCT.md
LICENSE
README.md
electron.vite.config.ts
eslint.config.js
jest.config.js
package.json
tsconfig.json
```

## Entry points

- [src/main/main.ts](https://github.com/electron-react-boilerplate/electron-react-boilerplate/blob/e5b8242d8b21a4290c3a1f18ae3b64167e9de04a/src/main/main.ts)
- [src/renderer/App.tsx](https://github.com/electron-react-boilerplate/electron-react-boilerplate/blob/e5b8242d8b21a4290c3a1f18ae3b64167e9de04a/src/renderer/App.tsx)
- [src/renderer/index.tsx](https://github.com/electron-react-boilerplate/electron-react-boilerplate/blob/e5b8242d8b21a4290c3a1f18ae3b64167e9de04a/src/renderer/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| assets package | library | Observed | Groups 1 file(s) under assets package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| main package | library | Observed | Groups 5 file(s) under main package (observed from repository paths and static analysis). |
| renderer package | library | Observed | Groups 3 file(s) under renderer package (observed from repository paths and static analysis). |
| __tests__ package | library | Observed | Groups 2 file(s) under __tests__ package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.erb/tooling/package.json` (manifest)
- `.github/FUNDING.yml` (config)
- `.github/config.yml` (config)
- `.github/stale.yml` (config)
- `.github/workflows/codeql-analysis.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `.vscode/extensions.json` (config)
- `.vscode/launch.json` (config)
- `.vscode/settings.json` (config)
- `package.json` (manifest)
- `release/app/package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `.erb` — 13 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `src` — 12 analysed file(s)
- `.github` — 9 analysed file(s)
- `.vscode` — 3 analysed file(s)
- `assets` — 3 analysed file(s)
- `release` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `e5b8242d8b21a4290c3a1f18ae3b64167e9de04a` is the revision these paths and observations refer to.
