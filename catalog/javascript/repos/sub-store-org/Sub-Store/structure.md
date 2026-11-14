# Project structure: sub-store-org/Sub-Store

**Analysed commit:** `2e7a63c6f4d5f067415eefc12bbbf012123e7f8d`

**Commit reference:** [2e7a63c6f4d5f067415eefc12bbbf012123e7f8d](https://github.com/sub-store-org/Sub-Store/commit/2e7a63c6f4d5f067415eefc12bbbf012123e7f8d)

**Tree at this commit:** [sub-store-org/Sub-Store@2e7a63c6f4d5](https://github.com/sub-store-org/Sub-Store/tree/2e7a63c6f4d5f067415eefc12bbbf012123e7f8d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | sub-store-org/Sub-Store |
| Description | Advanced Subscription Manager for QX, Loon, Surge, Stash, Egern and Shadowrocket! |
| Stars | 10904 |
| Forks | 1440 |
| Licence | AGPL-3.0 |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `2e7a63c6f4d5f067415eefc12bbbf012123e7f8d` |
| Retrieved at | 2026-11-14T19:12:28.636510+00:00 |
| Files in this snapshot | 179 |

## Directory tree

```text
.github/  (4 files)
  ISSUE_TEMPLATE/  (2 files)
    功能建议.yml
    问题反馈.yml
  workflows/  (2 files)
    main.yml
    star-history.yml
backend/  (150 files)
  patches/  (1 files)
    http-proxy@1.18.1.patch
  src/  (139 files)
    core/  (34 files)
      … 34 files under this directory
    products/  (5 files)
      … 5 files under this directory
    restful/  (23 files)
      … 23 files under this directory
    runtime/  (9 files)
      … 9 files under this directory
    test/  (39 files)
      … 39 files under this directory
    utils/  (27 files)
      … 27 files under this directory
    constants.js
    main.js
  .babelrc
  .eslintrc.json
  .prettierrc.json
  banner
  bundle-esbuild.js
  dev-esbuild.js
  esbuild-dev.js
  jsconfig.json
  package.json
  pnpm-workspace.yaml
config/  (11 files)
  Egern.yaml
  Loon-parser.plugin
  Loon.plugin
  QX-Task.json
  QX.snippet
  README.md
  Stash.stoverride
  Surge-Beta.sgmodule
  Surge-Noability.sgmodule
  Surge-ability.sgmodule
  Surge.sgmodule
scripts/  (9 files)
  demo.js
  fancy-characters.js
  ip-flag-node.js
  ip-flag.js
  media-filter.js
  revert.js
  tls-fingerprint.js
  udp-filter.js
  vmess-ws-obfs-host.js
.gitignore
.node-version
LICENSE
README.md
vs.code-workspace
```

## Entry points

- [backend/src/main.js](https://github.com/sub-store-org/Sub-Store/blob/2e7a63c6f4d5f067415eefc12bbbf012123e7f8d/backend/src/main.js)
- [backend/src/core/app.js](https://github.com/sub-store-org/Sub-Store/blob/2e7a63c6f4d5f067415eefc12bbbf012123e7f8d/backend/src/core/app.js)
- [backend/src/restful/index.js](https://github.com/sub-store-org/Sub-Store/blob/2e7a63c6f4d5f067415eefc12bbbf012123e7f8d/backend/src/restful/index.js)
- [backend/src/utils/index.js](https://github.com/sub-store-org/Sub-Store/blob/2e7a63c6f4d5f067415eefc12bbbf012123e7f8d/backend/src/utils/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| backend package | library | Observed | Groups 69 file(s) under backend package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 9 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 34 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 39 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/ISSUE_TEMPLATE/功能建议.yml` (config)
- `.github/ISSUE_TEMPLATE/问题反馈.yml` (config)
- `.github/workflows/main.yml` (ci)
- `.github/workflows/star-history.yml` (ci)
- `backend/.eslintrc.json` (config)
- `backend/.prettierrc.json` (config)
- `backend/jsconfig.json` (config)
- `backend/package.json` (manifest)
- `backend/pnpm-workspace.yaml` (config)
- `config/Egern.yaml` (config)
- `config/QX-Task.json` (config)

## Top-level layout

- `backend` — 150 analysed file(s)
- `config` — 11 analysed file(s)
- `scripts` — 9 analysed file(s)
- `(root files)` — 5 analysed file(s)
- `.github` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 9 file(s) were skipped during inventory (1 x lockfile excluded; 8 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `2e7a63c6f4d5f067415eefc12bbbf012123e7f8d` is the revision these paths and observations refer to.
