# Project structure: typicode/hotel

**Analysed commit:** `bcbdade4a5ce5f9f8ac0d66def7ba0a4efec2366`

**Commit reference:** [bcbdade4a5ce5f9f8ac0d66def7ba0a4efec2366](https://github.com/typicode/hotel/commit/bcbdade4a5ce5f9f8ac0d66def7ba0a4efec2366)

**Tree at this commit:** [typicode/hotel@bcbdade4a5ce](https://github.com/typicode/hotel/tree/bcbdade4a5ce5f9f8ac0d66def7ba0a4efec2366)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | typicode/hotel |
| Description | 🏩 A simple process manager for developers. Start apps from your browser and access them using local domains |
| Stars | 9986 |
| Forks | 440 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `bcbdade4a5ce5f9f8ac0d66def7ba0a4efec2366` |
| Retrieved at | 2026-11-14T19:12:46.407200+00:00 |
| Files in this snapshot | 76 |

## Directory tree

```text
.github/  (1 files)
  FUNDING.yml
bin/  (1 files)
  uninstall.js
docs/  (2 files)
  Docker.md
  README.md
src/  (45 files)
  app/  (17 files)
    components/  (11 files)
      … 11 files under this directory
    Store.ts
    api.ts
    formatter.ts
    global.d.ts
    index.html
    index.tsx
  cli/  (5 files)
    bin.js
    daemon.js
    index.js
    run.js
    servers.js
  daemon/  (18 files)
    public/  (1 files)
      … 1 files under this directory
    routers/  (4 files)
      … 4 files under this directory
    vhosts/  (1 files)
      … 1 files under this directory
    views/  (5 files)
      … 5 files under this directory
    app.js
    group.js
    index.js
    loader.js
    log.js
    pem.js
    tcp-proxy.js
  scripts/  (1 files)
    uninstall.js
  common.js
  conf.js
  get-cmd.js
  pid-file.js
test/  (9 files)
  cli/  (3 files)
    daemon.js
    run.js
    servers.js
  daemon/  (3 files)
    app.js
    group.js
    pem.js
  fixtures/  (2 files)
    app/  (1 files)
      … 1 files under this directory
    verbose/  (1 files)
      … 1 files under this directory
  _setup.js
.babelrc
.eslintrc.js
.gitattributes
.gitignore
.npmignore
.stylelintrc
.travis.yml
CHANGELOG.md
LICENSE
README.md
appveyor.yml
nodemon.json
package.json
tsconfig.json
tslint.json
webpack.common.js
webpack.dev.js
webpack.prod.js
```

## Entry points

- [src/app/index.tsx](https://github.com/typicode/hotel/blob/bcbdade4a5ce5f9f8ac0d66def7ba0a4efec2366/src/app/index.tsx)
- [src/cli/index.js](https://github.com/typicode/hotel/blob/bcbdade4a5ce5f9f8ac0d66def7ba0a4efec2366/src/cli/index.js)
- [src/daemon/app.js](https://github.com/typicode/hotel/blob/bcbdade4a5ce5f9f8ac0d66def7ba0a4efec2366/src/daemon/app.js)
- [src/daemon/index.js](https://github.com/typicode/hotel/blob/bcbdade4a5ce5f9f8ac0d66def7ba0a4efec2366/src/daemon/index.js)
- [src/daemon/routers/index.js](https://github.com/typicode/hotel/blob/bcbdade4a5ce5f9f8ac0d66def7ba0a4efec2366/src/daemon/routers/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 4 file(s) under api layer (observed from repository paths and static analysis). |
| app package | library | Observed | Groups 11 file(s) under app package (observed from repository paths and static analysis). |
| bin package | library | Observed | Groups 1 file(s) under bin package (observed from repository paths and static analysis). |
| cli package | library | Observed | Groups 5 file(s) under cli package (observed from repository paths and static analysis). |
| common.js package | library | Observed | Groups 1 file(s) under common.js package (observed from repository paths and static analysis). |
| conf.js package | library | Observed | Groups 1 file(s) under conf.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| daemon package | library | Observed | Groups 8 file(s) under daemon package (observed from repository paths and static analysis). |
| get-cmd.js package | library | Observed | Groups 1 file(s) under get-cmd.js package (observed from repository paths and static analysis). |
| pid-file.js package | library | Observed | Groups 1 file(s) under pid-file.js package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 9 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.travis.yml` (ci)
- `appveyor.yml` (config)
- `nodemon.json` (config)
- `package.json` (manifest)
- `tsconfig.json` (config)
- `tslint.json` (config)

## Top-level layout

- `src` — 45 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `test` — 9 analysed file(s)
- `docs` — 2 analysed file(s)
- `.github` — 1 analysed file(s)
- `bin` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `bcbdade4a5ce5f9f8ac0d66def7ba0a4efec2366` is the revision these paths and observations refer to.
