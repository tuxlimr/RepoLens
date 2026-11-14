# Project structure: async-labs/saas

**Analysed commit:** `4b27b6a0a4bb876562da6de93f0c0dd509fd5ffe`

**Commit reference:** [4b27b6a0a4bb876562da6de93f0c0dd509fd5ffe](https://github.com/async-labs/saas/commit/4b27b6a0a4bb876562da6de93f0c0dd509fd5ffe)

**Tree at this commit:** [async-labs/saas@4b27b6a0a4bb](https://github.com/async-labs/saas/tree/4b27b6a0a4bb876562da6de93f0c0dd509fd5ffe)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | async-labs/saas |
| Description | Build your own SaaS business with SaaS boilerplate. Productive stack: React, Material-UI, Next, MobX, WebSockets, Express, Node, Mongoose, MongoDB. Written with TypeScript. |
| Stars | 4535 |
| Forks | 741 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `4b27b6a0a4bb876562da6de93f0c0dd509fd5ffe` |
| Retrieved at | 2026-11-14T19:14:43.958306+00:00 |
| Files in this snapshot | 777 |

## Directory tree

```text
.github/  (1 files)
  FUNDING.yml
.vscode/  (2 files)
  extensions.json
  settings.json
book/  (771 files)
  1-begin/  (1 files)
    .gitignore
  1-end/  (14 files)
    app/  (13 files)
      … 13 files under this directory
    .gitignore
  10-begin/  (94 files)
    api/  (30 files)
      … 30 files under this directory
    app/  (56 files)
      … 56 files under this directory
    lambda/  (7 files)
      … 7 files under this directory
    .gitignore
  10-end/  (104 files)
    api/  (32 files)
      … 32 files under this directory
    app/  (64 files)
      … 64 files under this directory
    lambda/  (7 files)
      … 7 files under this directory
    .gitignore
  10-end-functional/  (106 files)
    api/  (33 files)
      … 33 files under this directory
    app/  (64 files)
      … 64 files under this directory
    lambda/  (8 files)
      … 8 files under this directory
    .gitignore
  2-begin/  (14 files)
    app/  (13 files)
      … 13 files under this directory
    .gitignore
  2-end/  (24 files)
    app/  (23 files)
      … 23 files under this directory
    .gitignore
  3-begin/  (24 files)
    app/  (23 files)
      … 23 files under this directory
    .gitignore
  3-end/  (35 files)
    api/  (8 files)
      … 8 files under this directory
    app/  (26 files)
      … 26 files under this directory
    .gitignore
  4-begin/  (35 files)
    api/  (8 files)
      … 8 files under this directory
    app/  (26 files)
      … 26 files under this directory
    .gitignore
  4-end/  (47 files)
    api/  (17 files)
      … 17 files under this directory
    app/  (29 files)
      … 29 files under this directory
    .gitignore
  5-begin/  (47 files)
    api/  (17 files)
      … 17 files under this directory
    app/  (29 files)
      … 29 files under this directory
    .gitignore
  5-end/  (51 files)
    api/  (18 files)
      … 18 files under this directory
    app/  (32 files)
      … 32 files under this directory
    .gitignore
  6-begin/  (51 files)
    api/  (18 files)
      … 18 files under this directory
    app/  (32 files)
      … 32 files under this directory
    .gitignore
  6-end/  (56 files)
    api/  (23 files)
      … 23 files under this directory
    app/  (32 files)
      … 32 files under this directory
    .gitignore
  7-begin/  (56 files)
    api/  (23 files)
      … 23 files under this directory
    app/  (32 files)
      … 32 files under this directory
    .gitignore
  7-end/  (11 files)
    api/  (10 files)
      … 10 files under this directory
    .gitignore
  .note
.gitignore
LICENSE.md
README.md
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 183 file(s) under api layer (observed from repository paths and static analysis). |
| book package | library | Observed | Groups 352 file(s) under book package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 115 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Inferred | Groups 0 file(s) under data layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 18 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.vscode/extensions.json` (config)
- `.vscode/settings.json` (config)
- `book/1-end/app/package.json` (manifest)
- `book/1-end/app/tsconfig.json` (config)
- `book/1-end/app/tsconfig.server.json` (config)
- `book/10-begin/api/nodemon.json` (config)
- `book/10-begin/api/package.json` (manifest)
- `book/10-begin/api/tsconfig.json` (config)
- `book/10-begin/api/tsconfig.server.json` (config)
- `book/10-begin/app/nodemon.json` (config)
- `book/10-begin/app/package.json` (manifest)
- `book/10-begin/app/tsconfig.json` (config)
- `book/10-begin/app/tsconfig.server.json` (config)
- `book/10-begin/lambda/package.json` (manifest)
- `book/10-begin/lambda/serverless.yml` (config)
- `book/10-begin/lambda/tsconfig.json` (config)
- `book/10-end-functional/api/.elasticbeanstalk/config.yml` (config)
- `book/10-end-functional/api/.env.example` (config)
- `book/10-end-functional/api/nodemon.json` (config)
- `book/10-end-functional/api/package.json` (manifest)
- `book/10-end-functional/api/tsconfig.json` (config)
- `book/10-end-functional/app/.elasticbeanstalk/config.yml` (config)
- `book/10-end-functional/app/.env.example` (config)
- `book/10-end-functional/app/nodemon.json` (config)
- `book/10-end-functional/app/package.json` (manifest)
- `book/10-end-functional/app/tsconfig.json` (config)
- `book/10-end-functional/app/tsconfig.server.json` (config)
- `book/10-end-functional/lambda/package.json` (manifest)
- `book/10-end-functional/lambda/serverless.yml` (config)
- `book/10-end-functional/lambda/tsconfig.json` (config)
- `book/10-end/api/.elasticbeanstalk/config.yml` (config)
- `book/10-end/api/nodemon.json` (config)
- `book/10-end/api/package.json` (manifest)
- `book/10-end/api/tsconfig.json` (config)
- `book/10-end/app/.elasticbeanstalk/config.yml` (config)
- `book/10-end/app/nodemon.json` (config)
- `book/10-end/app/package.json` (manifest)
- `book/10-end/app/tsconfig.json` (config)
- `book/10-end/app/tsconfig.server.json` (config)
- `book/10-end/lambda/package.json` (manifest)
- `book/10-end/lambda/serverless.yml` (config)
- `book/10-end/lambda/tsconfig.json` (config)
- `book/2-begin/app/package.json` (manifest)
- `book/2-begin/app/tsconfig.json` (config)
- `book/2-begin/app/tsconfig.server.json` (config)
- `book/2-end/app/package.json` (manifest)
- `book/2-end/app/tsconfig.json` (config)
- `book/2-end/app/tsconfig.server.json` (config)
- `book/3-begin/app/package.json` (manifest)
- `book/3-begin/app/tsconfig.json` (config)
- `book/3-begin/app/tsconfig.server.json` (config)
- `book/3-end/api/nodemon.json` (config)
- `book/3-end/api/package.json` (manifest)
- `book/3-end/api/tsconfig.json` (config)
- `book/3-end/api/tsconfig.server.json` (config)
- `book/3-end/app/nodemon.json` (config)
- `book/3-end/app/package.json` (manifest)
- `book/3-end/app/tsconfig.json` (config)
- `book/3-end/app/tsconfig.server.json` (config)
- `book/4-begin/api/nodemon.json` (config)
- `book/4-begin/api/package.json` (manifest)
- `book/4-begin/api/tsconfig.json` (config)
- `book/4-begin/api/tsconfig.server.json` (config)
- `book/4-begin/app/nodemon.json` (config)
- `book/4-begin/app/package.json` (manifest)
- `book/4-begin/app/tsconfig.json` (config)
- `book/4-begin/app/tsconfig.server.json` (config)
- `book/4-end/api/nodemon.json` (config)
- `book/4-end/api/package.json` (manifest)
- `book/4-end/api/tsconfig.json` (config)
- `book/4-end/api/tsconfig.server.json` (config)
- `book/4-end/app/nodemon.json` (config)
- `book/4-end/app/package.json` (manifest)
- `book/4-end/app/tsconfig.json` (config)
- `book/4-end/app/tsconfig.server.json` (config)
- `book/5-begin/api/nodemon.json` (config)
- `book/5-begin/api/package.json` (manifest)
- `book/5-begin/api/tsconfig.json` (config)
- `book/5-begin/api/tsconfig.server.json` (config)
- `book/5-begin/app/nodemon.json` (config)
- `book/5-begin/app/package.json` (manifest)
- `book/5-begin/app/tsconfig.json` (config)
- `book/5-begin/app/tsconfig.server.json` (config)
- `book/5-end/api/nodemon.json` (config)
- `book/5-end/api/package.json` (manifest)
- `book/5-end/api/tsconfig.json` (config)
- `book/5-end/api/tsconfig.server.json` (config)
- `book/5-end/app/nodemon.json` (config)
- `book/5-end/app/package.json` (manifest)
- `book/5-end/app/tsconfig.json` (config)
- `book/5-end/app/tsconfig.server.json` (config)
- `book/6-begin/api/nodemon.json` (config)
- `book/6-begin/api/package.json` (manifest)
- `book/6-begin/api/tsconfig.json` (config)
- `book/6-begin/api/tsconfig.server.json` (config)
- `book/6-begin/app/nodemon.json` (config)
- `book/6-begin/app/package.json` (manifest)
- `book/6-begin/app/tsconfig.json` (config)
- `book/6-begin/app/tsconfig.server.json` (config)
- `book/6-end/api/nodemon.json` (config)
- `book/6-end/api/package.json` (manifest)
- `book/6-end/api/tsconfig.json` (config)
- `book/6-end/api/tsconfig.server.json` (config)
- `book/6-end/app/nodemon.json` (config)
- `book/6-end/app/package.json` (manifest)
- `book/6-end/app/tsconfig.json` (config)
- `book/6-end/app/tsconfig.server.json` (config)
- `book/7-begin/api/nodemon.json` (config)
- `book/7-begin/api/package.json` (manifest)
- `book/7-begin/api/tsconfig.json` (config)
- `book/7-begin/api/tsconfig.server.json` (config)
- `book/7-begin/app/nodemon.json` (config)
- `book/7-begin/app/package.json` (manifest)
- `book/7-begin/app/tsconfig.json` (config)
- `book/7-begin/app/tsconfig.server.json` (config)
- `book/7-end/api/nodemon.json` (config)
- `book/7-end/api/package.json` (manifest)

## Top-level layout

- `book` — 771 analysed file(s)
- `(root files)` — 3 analysed file(s)
- `.vscode` — 2 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 23 file(s) were skipped during inventory (23 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `4b27b6a0a4bb876562da6de93f0c0dd509fd5ffe` is the revision these paths and observations refer to.
