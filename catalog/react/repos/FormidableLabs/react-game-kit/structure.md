# Project structure: FormidableLabs/react-game-kit

**Analysed commit:** `3c4eab99902ce071346edb8fe993c080e7880e4c`

**Commit reference:** [3c4eab99902ce071346edb8fe993c080e7880e4c](https://github.com/FormidableLabs/react-game-kit/commit/3c4eab99902ce071346edb8fe993c080e7880e4c)

**Tree at this commit:** [FormidableLabs/react-game-kit@3c4eab99902c](https://github.com/FormidableLabs/react-game-kit/tree/3c4eab99902ce071346edb8fe993c080e7880e4c)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | FormidableLabs/react-game-kit |
| Description | Component library for making games with React  & React Native |
| Stars | 4601 |
| Forks | 309 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `3c4eab99902ce071346edb8fe993c080e7880e4c` |
| Retrieved at | 2026-11-14T19:14:41.682798+00:00 |
| Files in this snapshot | 76 |

## Directory tree

```text
demo/  (43 files)
  code-samples/  (25 files)
    loop-use.example
    loop.example
    physics-body-update.example
    physics-body.example
    physics-mobx-update.example
    physics-simple.example
    physics-store.example
    physics-style.example
    physics-update.example
    physics-world-init.example
    physics-world.example
    raf.example
    sprite-manual.example
    sprite-style.example
    sprite.example
    stage-blurry.example
    stage-size.example
    stage-use.example
    stage.example
    tilemap-buildings.example
    tilemap-custom.example
    tilemap-manual.example
    tilemap-map.example
    tilemap-render.example
    … 1 more files
  game/  (5 files)
    stores/  (1 files)
      … 1 files under this directory
    character.js
    fade.js
    index.js
    level.js
  slides/  (8 files)
    basics.js
    index.js
    loop.js
    physics.js
    scaling.js
    slide.js
    sprites.js
    tilemaps.js
  index.css
  index.html
  index.js
  intro.js
  presentation.js
src/  (17 files)
  components/  (6 files)
    body.js
    loop.js
    sprite.js
    stage.js
    tile-map.js
    world.js
  native/  (7 files)
    components/  (6 files)
      … 6 files under this directory
    utils/  (1 files)
      … 1 files under this directory
  utils/  (3 files)
    audio-player.js
    game-loop.js
    key-listener.js
  index.js
.babelrc
.eslintignore
.eslintrc
.flowconfig
.gitignore
.npmignore
.prettierrc
.travis.yml
CONTRIBUTING.md
LICENSE.md
README.md
native.js
package.json
tsconfig.json
webpack.config.dev.js
webpack.config.js
```

## Entry points

- [demo/game/index.js](https://github.com/FormidableLabs/react-game-kit/blob/3c4eab99902ce071346edb8fe993c080e7880e4c/demo/game/index.js)
- [demo/index.js](https://github.com/FormidableLabs/react-game-kit/blob/3c4eab99902ce071346edb8fe993c080e7880e4c/demo/index.js)
- [demo/slides/index.js](https://github.com/FormidableLabs/react-game-kit/blob/3c4eab99902ce071346edb8fe993c080e7880e4c/demo/slides/index.js)
- [src/index.js](https://github.com/FormidableLabs/react-game-kit/blob/3c4eab99902ce071346edb8fe993c080e7880e4c/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| components package | library | Observed | Groups 6 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| demo package | library | Observed | Groups 16 file(s) under demo package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| native package | library | Observed | Groups 7 file(s) under native package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 3 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.travis.yml` (ci)
- `package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `demo` — 43 analysed file(s)
- `src` — 17 analysed file(s)
- `(root files)` — 16 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `3c4eab99902ce071346edb8fe993c080e7880e4c` is the revision these paths and observations refer to.
