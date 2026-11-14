# Project structure: jwagner/smartcrop.js

**Analysed commit:** `0e207ed910625f91b07d35865c71a9621a63ebdb`

**Commit reference:** [0e207ed910625f91b07d35865c71a9621a63ebdb](https://github.com/jwagner/smartcrop.js/commit/0e207ed910625f91b07d35865c71a9621a63ebdb)

**Tree at this commit:** [jwagner/smartcrop.js@0e207ed91062](https://github.com/jwagner/smartcrop.js/tree/0e207ed910625f91b07d35865c71a9621a63ebdb)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | jwagner/smartcrop.js |
| Description | Content aware image cropping |
| Stars | 12959 |
| Forks | 570 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `0e207ed910625f91b07d35865c71a9621a63ebdb` |
| Retrieved at | 2026-11-14T19:12:02.864120+00:00 |
| Files in this snapshot | 35 |

## Directory tree

```text
.devcontainer/  (2 files)
  Dockerfile
  devcontainer.json
.github/  (2 files)
  workflows/  (2 files)
    publish.yml
    tests.yml
examples/  (16 files)
  face-api/  (1 files)
    tiny_face_detector_model-weights_manifest.json
  images/  (1 files)
    images.json
  jquery.js
  minimal.html
  q.js
  slideshow.html
  slideshow.js
  smartcrop-debug.js
  style.css
  testbed.html
  testbed.js
  testsuite.html
  testsuite.js
  tracking-face-min.js
  tracking-min.js
  underscore.js
test/  (6 files)
  benchmark-node.js
  benchmark.html
  benchmark.js
  index.html
  smartcrop.js
  types.ts
.editorconfig
.eslintrc.js
.prettierrc
LICENSE
README.md
bower.json
index.d.ts
package.json
smartcrop.js
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 6 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.devcontainer/Dockerfile` (container)
- `.devcontainer/devcontainer.json` (config)
- `.editorconfig` (config)
- `.github/workflows/publish.yml` (ci)
- `.github/workflows/tests.yml` (ci)
- `bower.json` (config)
- `examples/face-api/tiny_face_detector_model-weights_manifest.json` (config)
- `examples/images/images.json` (config)
- `package.json` (manifest)

## Top-level layout

- `examples` — 16 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `test` — 6 analysed file(s)
- `.devcontainer` — 2 analysed file(s)
- `.github` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `0e207ed910625f91b07d35865c71a9621a63ebdb` is the revision these paths and observations refer to.
