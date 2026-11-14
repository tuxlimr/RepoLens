# Project structure: browsh-org/browsh

**Analysed commit:** `e6325957514665db86428088b280fc7909334b91`

**Commit reference:** [e6325957514665db86428088b280fc7909334b91](https://github.com/browsh-org/browsh/commit/e6325957514665db86428088b280fc7909334b91)

**Tree at this commit:** [browsh-org/browsh@e63259575146](https://github.com/browsh-org/browsh/tree/e6325957514665db86428088b280fc7909334b91)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | browsh-org/browsh |
| Description | A fully-modern text-based browser, rendering to TTY and browsers |
| Stars | 19128 |
| Forks | 480 |
| Licence | LGPL-2.1 |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `e6325957514665db86428088b280fc7909334b91` |
| Retrieved at | 2026-11-14T19:11:18.140263+00:00 |
| Files in this snapshot | 88 |

## Directory tree

```text
.github/  (4 files)
  ISSUE_TEMPLATE/  (1 files)
    bug_report.md
  workflows/  (2 files)
    lint.yml
    main.yml
  FUNDING.yml
interfacer/  (36 files)
  cmd/  (1 files)
    browsh/  (1 files)
      … 1 files under this directory
  contrib/  (1 files)
    upx_compress_binary.sh
  src/  (22 files)
    browsh/  (22 files)
      … 22 files under this directory
  test/  (10 files)
    http-server/  (2 files)
      … 2 files under this directory
    sites/  (5 files)
      … 5 files under this directory
    tty/  (3 files)
      … 3 files under this directory
  go.mod
  go.sum
scripts/  (6 files)
  bundling.bash
  common.bash
  docker.bash
  misc.bash
  releasing.bash
  tests.bash
webext/  (35 files)
  assets/  (2 files)
    browsh-schema.json
    styles.css
  contrib/  (3 files)
    download_xpi.js
    firefoxheadless.sh
    font_maker.py
  src/  (16 files)
    background/  (6 files)
      … 6 files under this directory
    dom/  (9 files)
      … 9 files under this directory
    utils.js
  test/  (6 files)
    fixtures/  (2 files)
      … 2 files under this directory
    mocks/  (1 files)
      … 1 files under this directory
    graphics_builder_spec.js
    helper.js
    text_builder_spec.js
  .eslintrc
  .mocharc.cjs
  .web-extension-id
  background.js
  content.js
  manifest.json
  package.json
  webpack.config.js
.dockerignore
.gitignore
Dockerfile
LICENSE
README.md
ctl.sh
goreleaser.yml
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| interfacer package | library | Observed | Groups 24 file(s) under interfacer package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 16 file(s) under tests (observed from repository paths and static analysis). |
| webext package | library | Observed | Groups 23 file(s) under webext package (observed from repository paths and static analysis). Observed top-level functions: generate. |

## Important files

- `.dockerignore` (container)
- `.github/FUNDING.yml` (config)
- `.github/workflows/lint.yml` (ci)
- `.github/workflows/main.yml` (ci)
- `Dockerfile` (container)
- `goreleaser.yml` (config)
- `interfacer/go.mod` (manifest)
- `webext/assets/browsh-schema.json` (config)
- `webext/manifest.json` (config)
- `webext/package.json` (manifest)

## Top-level layout

- `interfacer` — 36 analysed file(s)
- `webext` — 35 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `scripts` — 6 analysed file(s)
- `.github` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `e6325957514665db86428088b280fc7909334b91` is the revision these paths and observations refer to.
