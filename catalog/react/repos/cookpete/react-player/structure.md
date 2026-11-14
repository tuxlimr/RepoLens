# Project structure: cookpete/react-player

**Analysed commit:** `258fce939638a295f6a429ad683935254d1bfda2`

**Commit reference:** [258fce939638a295f6a429ad683935254d1bfda2](https://github.com/cookpete/react-player/commit/258fce939638a295f6a429ad683935254d1bfda2)

**Tree at this commit:** [cookpete/react-player@258fce939638](https://github.com/cookpete/react-player/tree/258fce939638a295f6a429ad683935254d1bfda2)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | cookpete/react-player |
| Description | A React component for playing a variety of URLs, including file paths, YouTube, Facebook, Twitch, SoundCloud, Streamable, Vimeo, Wistia and DailyMotion |
| Stars | 10291 |
| Forks | 1201 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `258fce939638a295f6a429ad683935254d1bfda2` |
| Retrieved at | 2026-11-14T19:13:31.241800+00:00 |
| Files in this snapshot | 44 |

## Directory tree

```text
.github/  (4 files)
  workflows/  (2 files)
    cd.yml
    ci.yml
  FUNDING.yml
  issue_template.md
examples/  (8 files)
  react/  (8 files)
    public/  (5 files)
      … 5 files under this directory
    src/  (3 files)
      … 3 files under this directory
scripts/  (4 files)
  builder/  (2 files)
    builder.js
    package.json
  tester/  (2 files)
    package.json
    tester.js
src/  (9 files)
  HtmlPlayer.tsx
  Player.tsx
  Preview.tsx
  ReactPlayer.tsx
  index.ts
  patterns.ts
  players.ts
  props.ts
  types.ts
test/  (9 files)
  ReactPlayer/  (4 files)
    instanceMethods.js
    props.tsx
    render.js
    staticMethods.js
  helpers/  (2 files)
    helpers.tsx
    server-safe-globals.js
  Player.test.tsx
  Player.tsx
  react-player-tests.tsx
.gitignore
CHANGELOG.md
CONTRIBUTING.md
LICENSE.md
MIGRATING.md
README.md
biome.json
codecov.yml
package.json
tsconfig.json
```

## Entry points

- [scripts/builder/builder.js](https://github.com/cookpete/react-player/blob/258fce939638a295f6a429ad683935254d1bfda2/scripts/builder/builder.js)
- [scripts/tester/tester.js](https://github.com/cookpete/react-player/blob/258fce939638a295f6a429ad683935254d1bfda2/scripts/tester/tester.js)
- [src/index.ts](https://github.com/cookpete/react-player/blob/258fce939638a295f6a429ad683935254d1bfda2/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| HtmlPlayer.tsx package | library | Observed | Groups 1 file(s) under htmlplayer.tsx package (observed from repository paths and static analysis). |
| index.ts package | library | Observed | Groups 1 file(s) under index.ts package (observed from repository paths and static analysis). |
| patterns.ts package | library | Observed | Groups 1 file(s) under patterns.ts package (observed from repository paths and static analysis). |
| Player.tsx package | library | Observed | Groups 1 file(s) under player.tsx package (observed from repository paths and static analysis). |
| players.ts package | library | Observed | Groups 1 file(s) under players.ts package (observed from repository paths and static analysis). |
| Preview.tsx package | library | Observed | Groups 1 file(s) under preview.tsx package (observed from repository paths and static analysis). |
| props.ts package | library | Observed | Groups 1 file(s) under props.ts package (observed from repository paths and static analysis). |
| ReactPlayer.tsx package | library | Observed | Groups 1 file(s) under reactplayer.tsx package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 2 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 9 file(s) under tests (observed from repository paths and static analysis). |
| types.ts package | library | Observed | Groups 1 file(s) under types.ts package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/workflows/cd.yml` (ci)
- `.github/workflows/ci.yml` (ci)
- `biome.json` (config)
- `codecov.yml` (config)
- `package.json` (manifest)
- `scripts/builder/package.json` (manifest)
- `scripts/tester/package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `(root files)` — 10 analysed file(s)
- `src` — 9 analysed file(s)
- `test` — 9 analysed file(s)
- `examples` — 8 analysed file(s)
- `.github` — 4 analysed file(s)
- `scripts` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `258fce939638a295f6a429ad683935254d1bfda2` is the revision these paths and observations refer to.
