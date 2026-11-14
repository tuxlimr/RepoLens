# Project structure: Renovamen/playground-macos

**Analysed commit:** `2c9e82dca487432ad9922ddf9b0a26aadeae81e5`

**Commit reference:** [2c9e82dca487432ad9922ddf9b0a26aadeae81e5](https://github.com/Renovamen/playground-macos/commit/2c9e82dca487432ad9922ddf9b0a26aadeae81e5)

**Tree at this commit:** [Renovamen/playground-macos@2c9e82dca487](https://github.com/Renovamen/playground-macos/tree/2c9e82dca487432ad9922ddf9b0a26aadeae81e5)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Renovamen/playground-macos |
| Description | My portfolio website simulating macOS's GUI, developed with React and UnoCSS. |
| Stars | 3507 |
| Forks | 382 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `2c9e82dca487432ad9922ddf9b0a26aadeae81e5` |
| Retrieved at | 2026-11-14T19:15:16.884542+00:00 |
| Files in this snapshot | 96 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    deploy.yaml
.husky/  (1 files)
  pre-commit
public/  (21 files)
  img/  (16 files)
    sites/  (16 files)
      … 16 files under this directory
  logo/  (1 files)
    favicon.svg
  markdown/  (3 files)
    about-me.md
    about-site.md
    github-stats.md
  manifest.json
src/  (62 files)
  components/  (17 files)
    apps/  (6 files)
      … 6 files under this directory
    dock/  (2 files)
      … 2 files under this directory
    menus/  (6 files)
      … 6 files under this directory
    AppWindow.tsx
    Launchpad.tsx
    Spotlight.tsx
  configs/  (9 files)
    apps.tsx
    bear.tsx
    index.ts
    launchpad.ts
    music.ts
    terminal.tsx
    user.ts
    wallpapers.ts
    websites.ts
  hooks/  (6 files)
    index.ts
    useAudio.ts
    useBattery.ts
    useClickOutside.ts
    useInterval.ts
    useWindowSize.ts
  pages/  (3 files)
    Boot.tsx
    Desktop.tsx
    Login.tsx
  stores/  (4 files)
    slices/  (3 files)
      … 3 files under this directory
    index.ts
  styles/  (6 files)
    bear.css
    component.css
    font.css
    index.css
    layout.css
    typora.css
  types/  (10 files)
    configs/  (9 files)
      … 9 files under this directory
    index.d.ts
  utils/  (4 files)
    constants.ts
    index.ts
    screen.ts
    url.ts
  auto-imports.d.ts
  index.tsx
  vite-env.d.ts
.editorconfig
.gitattributes
.gitignore
LICENSE
README.md
eslint.config.js
index.html
package.json
tsconfig.json
unocss.config.ts
vite.config.ts
```

## Entry points

- [src/configs/index.ts](https://github.com/Renovamen/playground-macos/blob/2c9e82dca487432ad9922ddf9b0a26aadeae81e5/src/configs/index.ts)
- [src/hooks/index.ts](https://github.com/Renovamen/playground-macos/blob/2c9e82dca487432ad9922ddf9b0a26aadeae81e5/src/hooks/index.ts)
- [src/index.tsx](https://github.com/Renovamen/playground-macos/blob/2c9e82dca487432ad9922ddf9b0a26aadeae81e5/src/index.tsx)
- [src/stores/index.ts](https://github.com/Renovamen/playground-macos/blob/2c9e82dca487432ad9922ddf9b0a26aadeae81e5/src/stores/index.ts)
- [src/utils/index.ts](https://github.com/Renovamen/playground-macos/blob/2c9e82dca487432ad9922ddf9b0a26aadeae81e5/src/utils/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| auto-imports.d.ts package | library | Observed | Groups 1 file(s) under auto-imports.d.ts package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 17 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 21 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 6 file(s) under hooks package (observed from repository paths and static analysis). |
| index.tsx package | library | Observed | Groups 1 file(s) under index.tsx package (observed from repository paths and static analysis). |
| pages package | library | Observed | Groups 3 file(s) under pages package (observed from repository paths and static analysis). |
| stores package | library | Observed | Groups 4 file(s) under stores package (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 1 file(s) under types package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 4 file(s) under utils package (observed from repository paths and static analysis). |
| vite-env.d.ts package | library | Observed | Groups 1 file(s) under vite-env.d.ts package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/workflows/deploy.yaml` (ci)
- `package.json` (manifest)
- `public/manifest.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `src` — 62 analysed file(s)
- `public` — 21 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `.github` — 1 analysed file(s)
- `.husky` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `2c9e82dca487432ad9922ddf9b0a26aadeae81e5` is the revision these paths and observations refer to.
