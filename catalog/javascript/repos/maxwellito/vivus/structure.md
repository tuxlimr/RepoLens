# Project structure: maxwellito/vivus

**Analysed commit:** `06b7adb5d543b6b1d0d93fa83dea137b1f8644a5`

**Commit reference:** [06b7adb5d543b6b1d0d93fa83dea137b1f8644a5](https://github.com/maxwellito/vivus/commit/06b7adb5d543b6b1d0d93fa83dea137b1f8644a5)

**Tree at this commit:** [maxwellito/vivus@06b7adb5d543](https://github.com/maxwellito/vivus/tree/06b7adb5d543b6b1d0d93fa83dea137b1f8644a5)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | maxwellito/vivus |
| Description | JavaScript library to make drawing animation on SVG |
| Stars | 15479 |
| Forks | 1122 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `06b7adb5d543b6b1d0d93fa83dea137b1f8644a5` |
| Retrieved at | 2026-11-14T19:11:38.133214+00:00 |
| Files in this snapshot | 25 |

## Directory tree

```text
.github/  (1 files)
  ISSUE_TEMPLATE.md
assets/  (1 files)
  timelines.svg
src/  (3 files)
  _build.js
  pathformer.js
  vivus.js
test/  (9 files)
  manual/  (5 files)
    hi-there.svg
    index.html
    obturateur.svg
    polaroid.svg
    synth.svg
  unit/  (2 files)
    pathformer.spec.js
    vivus.spec.js
  karma.conf.js
  unit.setup.js
.eslintrc.json
.gitignore
.npmignore
.travis.yml
CONTRIBUTING.md
LICENSE
bower.json
hacks.md
index.html
package.json
readme.md
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| _build.js package | library | Observed | Groups 1 file(s) under _build.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| pathformer.js package | library | Observed | Groups 1 file(s) under pathformer.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 9 file(s) under tests (observed from repository paths and static analysis). |
| vivus.js package | library | Observed | Groups 1 file(s) under vivus.js package (observed from repository paths and static analysis). |

## Important files

- `.eslintrc.json` (config)
- `.travis.yml` (ci)
- `bower.json` (config)
- `package.json` (manifest)

## Top-level layout

- `(root files)` — 11 analysed file(s)
- `test` — 9 analysed file(s)
- `src` — 3 analysed file(s)
- `.github` — 1 analysed file(s)
- `assets` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (1 x lockfile excluded; 1 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `06b7adb5d543b6b1d0d93fa83dea137b1f8644a5` is the revision these paths and observations refer to.
