# Project structure: jaredpalmer/react-fns

**Analysed commit:** `8e28fd0e0fd181c4dc1b609520e18c5551b1042a`

**Commit reference:** [8e28fd0e0fd181c4dc1b609520e18c5551b1042a](https://github.com/jaredpalmer/react-fns/commit/8e28fd0e0fd181c4dc1b609520e18c5551b1042a)

**Tree at this commit:** [jaredpalmer/react-fns@8e28fd0e0fd1](https://github.com/jaredpalmer/react-fns/tree/8e28fd0e0fd181c4dc1b609520e18c5551b1042a)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | jaredpalmer/react-fns |
| Description | Browser API's turned into declarative React components and HoC's |
| Stars | 3697 |
| Forks | 97 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `8e28fd0e0fd181c4dc1b609520e18c5551b1042a` |
| Retrieved at | 2026-11-14T19:15:09.444248+00:00 |
| Files in this snapshot | 71 |

## Directory tree

```text
.github/  (2 files)
  FUNDING.yml
  stale.yml
docs/  (3 files)
  api.md
  how-it-works.md
  installation.md
src/  (40 files)
  DeviceMotion/  (3 files)
    DeviceMotion.tsx
    index.tsx
    withDeviceMotion.tsx
  DeviceOrientation/  (3 files)
    DeviceOrientation.tsx
    index.tsx
    withDeviceOrientation.tsx
  GeoPosition/  (3 files)
    GeoPosition.tsx
    index.tsx
    withGeoPosition.tsx
  Locales/  (3 files)
    Locales.tsx
    index.tsx
    withLocales.tsx
  Media/  (2 files)
    Media.tsx
    index.tsx
  Network/  (5 files)
    __tests__/  (2 files)
      … 2 files under this directory
    Network.tsx
    index.tsx
    withNetwork.tsx
  Scroll/  (5 files)
    __tests__/  (2 files)
      … 2 files under this directory
    Scroll.tsx
    index.tsx
    withScroll.tsx
  WindowSize/  (5 files)
    __tests__/  (2 files)
      … 2 files under this directory
    WindowSize.tsx
    index.tsx
    withWindowSize.tsx
  utils/  (5 files)
    debounce.ts
    featureDetection.ts
    index.tsx
    isEmptyChildren.tsx
    throttle.ts
  Mailto.tsx
  ReducerComponent.tsx
  Sms.tsx
  hoistStatics.tsx
  index.tsx
  types.tsx
website/  (18 files)
  core/  (1 files)
    Footer.js
  i18n/  (1 files)
    en.json
  pages/  (2 files)
    en/  (2 files)
      … 2 files under this directory
  static/  (9 files)
    css/  (2 files)
      … 2 files under this directory
    img/  (2 files)
      … 2 files under this directory
    js/  (4 files)
      … 4 files under this directory
    circle.yml
  deploy.js
  languages.js
  package.json
  sidebars.json
  siteConfig.js
.all-contributorsrc
.gitignore
.travis.yml
LICENSE
README.md
package.json
rollup.config.js
tsconfig.json
```

## Entry points

- [src/DeviceMotion/index.tsx](https://github.com/jaredpalmer/react-fns/blob/8e28fd0e0fd181c4dc1b609520e18c5551b1042a/src/DeviceMotion/index.tsx)
- [src/DeviceOrientation/index.tsx](https://github.com/jaredpalmer/react-fns/blob/8e28fd0e0fd181c4dc1b609520e18c5551b1042a/src/DeviceOrientation/index.tsx)
- [src/GeoPosition/index.tsx](https://github.com/jaredpalmer/react-fns/blob/8e28fd0e0fd181c4dc1b609520e18c5551b1042a/src/GeoPosition/index.tsx)
- [src/Locales/index.tsx](https://github.com/jaredpalmer/react-fns/blob/8e28fd0e0fd181c4dc1b609520e18c5551b1042a/src/Locales/index.tsx)
- [src/Media/index.tsx](https://github.com/jaredpalmer/react-fns/blob/8e28fd0e0fd181c4dc1b609520e18c5551b1042a/src/Media/index.tsx)
- [src/Network/index.tsx](https://github.com/jaredpalmer/react-fns/blob/8e28fd0e0fd181c4dc1b609520e18c5551b1042a/src/Network/index.tsx)
- [src/Scroll/index.tsx](https://github.com/jaredpalmer/react-fns/blob/8e28fd0e0fd181c4dc1b609520e18c5551b1042a/src/Scroll/index.tsx)
- [src/WindowSize/index.tsx](https://github.com/jaredpalmer/react-fns/blob/8e28fd0e0fd181c4dc1b609520e18c5551b1042a/src/WindowSize/index.tsx)
- [src/index.tsx](https://github.com/jaredpalmer/react-fns/blob/8e28fd0e0fd181c4dc1b609520e18c5551b1042a/src/index.tsx)
- [src/utils/index.tsx](https://github.com/jaredpalmer/react-fns/blob/8e28fd0e0fd181c4dc1b609520e18c5551b1042a/src/utils/index.tsx)
- [website/pages/en/index.js](https://github.com/jaredpalmer/react-fns/blob/8e28fd0e0fd181c4dc1b609520e18c5551b1042a/website/pages/en/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| DeviceMotion package | library | Observed | Groups 3 file(s) under devicemotion package (observed from repository paths and static analysis). |
| DeviceOrientation package | library | Observed | Groups 3 file(s) under deviceorientation package (observed from repository paths and static analysis). |
| GeoPosition package | library | Observed | Groups 3 file(s) under geoposition package (observed from repository paths and static analysis). |
| hoistStatics.tsx package | library | Observed | Groups 1 file(s) under hoiststatics.tsx package (observed from repository paths and static analysis). |
| index.tsx package | library | Observed | Groups 1 file(s) under index.tsx package (observed from repository paths and static analysis). |
| Locales package | library | Observed | Groups 3 file(s) under locales package (observed from repository paths and static analysis). |
| Mailto.tsx package | library | Observed | Groups 1 file(s) under mailto.tsx package (observed from repository paths and static analysis). |
| Media package | library | Observed | Groups 2 file(s) under media package (observed from repository paths and static analysis). |
| Network package | library | Observed | Groups 5 file(s) under network package (observed from repository paths and static analysis). |
| ReducerComponent.tsx package | library | Observed | Groups 1 file(s) under reducercomponent.tsx package (observed from repository paths and static analysis). |
| Scroll package | library | Observed | Groups 5 file(s) under scroll package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 1 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Sms.tsx package | library | Observed | Groups 1 file(s) under sms.tsx package (observed from repository paths and static analysis). |
| types.tsx package | library | Observed | Groups 1 file(s) under types.tsx package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 5 file(s) under utils package (observed from repository paths and static analysis). |
| website package | library | Observed | Groups 9 file(s) under website package (observed from repository paths and static analysis). |
| WindowSize package | library | Observed | Groups 5 file(s) under windowsize package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/stale.yml` (config)
- `.travis.yml` (ci)
- `package.json` (manifest)
- `tsconfig.json` (config)
- `website/i18n/en.json` (config)
- `website/package.json` (manifest)
- `website/sidebars.json` (config)
- `website/static/circle.yml` (config)

## Top-level layout

- `src` — 40 analysed file(s)
- `website` — 18 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `docs` — 3 analysed file(s)
- `.github` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `8e28fd0e0fd181c4dc1b609520e18c5551b1042a` is the revision these paths and observations refer to.
