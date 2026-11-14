# Project structure: brianc/node-postgres

**Analysed commit:** `2a5850fb0db18f5e40a642bbb4a4743de412ab54`

**Commit reference:** [2a5850fb0db18f5e40a642bbb4a4743de412ab54](https://github.com/brianc/node-postgres/commit/2a5850fb0db18f5e40a642bbb4a4743de412ab54)

**Tree at this commit:** [brianc/node-postgres@2a5850fb0db1](https://github.com/brianc/node-postgres/tree/2a5850fb0db18f5e40a642bbb4a4743de412ab54)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | brianc/node-postgres |
| Description | PostgreSQL client for node.js. |
| Stars | 13236 |
| Forks | 1387 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `2a5850fb0db18f5e40a642bbb4a4743de412ab54` |
| Retrieved at | 2026-11-14T19:11:59.263922+00:00 |
| Files in this snapshot | 359 |

## Directory tree

```text
.devcontainer/  (3 files)
  Dockerfile
  devcontainer.json
  docker-compose.yml
.github/  (5 files)
  workflows/  (2 files)
    benchmark.yml
    ci.yml
  CODEOWNERS
  FUNDING.yml
  dependabot.yaml
benchmark/  (3 files)
  README.md
  compare.js
  worker.js
docs/  (35 files)
  components/  (3 files)
    alert.tsx
    info.tsx
    logo.tsx
  pages/  (27 files)
    apis/  (7 files)
      … 7 files under this directory
    features/  (11 files)
      … 11 files under this directory
    guides/  (5 files)
      … 5 files under this directory
    _app.js
    _meta.js
    announcements.mdx
    index.mdx
  .gitignore
  README.md
  next.config.js
  package.json
  theme.config.js
packages/  (300 files)
  pg/  (152 files)
    esm/  (1 files)
      … 1 files under this directory
    lib/  (16 files)
      … 16 files under this directory
    script/  (1 files)
      … 1 files under this directory
    test/  (129 files)
      … 129 files under this directory
    Makefile
    README.md
    bench-pipelining.js
    bench.js
    package.json
  pg-bundler-test/  (10 files)
    src/  (1 files)
      … 1 files under this directory
    esbuild-cloudflare.config.mjs
    esbuild-empty.config.mjs
    package.json
    rollup-cloudflare.config.mjs
    rollup-empty.config.mjs
    vite-cloudflare.config.mjs
    vite-empty.config.mjs
    webpack-cloudflare.config.mjs
    webpack-empty.config.mjs
  pg-cloudflare/  (7 files)
    esm/  (1 files)
      … 1 files under this directory
    src/  (3 files)
      … 3 files under this directory
    README.md
    package.json
    tsconfig.json
  pg-connection-string/  (14 files)
    esm/  (1 files)
      … 1 files under this directory
    test/  (4 files)
      … 4 files under this directory
    .coveralls.yml
    .gitignore
    .mocharc.json
    LICENSE
    README.md
    index.d.ts
    index.js
    package.json
    tsconfig.json
  pg-cursor/  (14 files)
    esm/  (1 files)
      … 1 files under this directory
    test/  (10 files)
      … 10 files under this directory
    README.md
    index.js
    package.json
  pg-esm-test/  (11 files)
    README.md
    common-js-imports.test.cjs
    package.json
    pg-cloudflare.test.js
    pg-connection-string.test.js
    pg-cursor.test.js
    pg-native.test.js
    pg-pool.test.js
    pg-protocol.test.js
    pg-query-stream.test.js
    pg.test.js
  pg-native/  (32 files)
    bench/  (2 files)
      … 2 files under this directory
    esm/  (1 files)
      … 1 files under this directory
    lib/  (2 files)
      … 2 files under this directory
    test/  (24 files)
      … 24 files under this directory
    README.md
    index.js
    package.json
  pg-pool/  (22 files)
    esm/  (1 files)
      … 1 files under this directory
    test/  (17 files)
      … 17 files under this directory
    LICENSE
    README.md
    index.js
    package.json
  pg-protocol/  (15 files)
    esm/  (1 files)
      … 1 files under this directory
    src/  (11 files)
      … 11 files under this directory
    README.md
    package.json
    tsconfig.json
  pg-query-stream/  (23 files)
    esm/  (1 files)
      … 1 files under this directory
    src/  (1 files)
      … 1 files under this directory
    test/  (17 files)
      … 17 files under this directory
    LICENSE
    README.md
    package.json
    tsconfig.json
.gitattributes
.gitignore
.yarnrc
CHANGELOG.md
LICENSE
LOCAL_DEV.md
README.md
SPONSORS.md
eslint.config.mjs
lerna.json
package.json
tea.yaml
tsconfig.json
```

## Entry points

- [docs/next.config.js](https://github.com/brianc/node-postgres/blob/2a5850fb0db18f5e40a642bbb4a4743de412ab54/docs/next.config.js)
- [packages/pg-connection-string/index.js](https://github.com/brianc/node-postgres/blob/2a5850fb0db18f5e40a642bbb4a4743de412ab54/packages/pg-connection-string/index.js)
- [packages/pg-cursor/index.js](https://github.com/brianc/node-postgres/blob/2a5850fb0db18f5e40a642bbb4a4743de412ab54/packages/pg-cursor/index.js)
- [packages/pg-native/index.js](https://github.com/brianc/node-postgres/blob/2a5850fb0db18f5e40a642bbb4a4743de412ab54/packages/pg-native/index.js)
- [packages/pg-pool/index.js](https://github.com/brianc/node-postgres/blob/2a5850fb0db18f5e40a642bbb4a4743de412ab54/packages/pg-pool/index.js)
- [packages/pg-cloudflare/src/index.ts](https://github.com/brianc/node-postgres/blob/2a5850fb0db18f5e40a642bbb4a4743de412ab54/packages/pg-cloudflare/src/index.ts)
- [packages/pg-native/bench/index.js](https://github.com/brianc/node-postgres/blob/2a5850fb0db18f5e40a642bbb4a4743de412ab54/packages/pg-native/bench/index.js)
- [packages/pg-protocol/esm/index.js](https://github.com/brianc/node-postgres/blob/2a5850fb0db18f5e40a642bbb4a4743de412ab54/packages/pg-protocol/esm/index.js)
- [packages/pg-protocol/src/index.ts](https://github.com/brianc/node-postgres/blob/2a5850fb0db18f5e40a642bbb4a4743de412ab54/packages/pg-protocol/src/index.ts)
- [packages/pg-query-stream/src/index.ts](https://github.com/brianc/node-postgres/blob/2a5850fb0db18f5e40a642bbb4a4743de412ab54/packages/pg-query-stream/src/index.ts)
- [packages/pg/lib/index.js](https://github.com/brianc/node-postgres/blob/2a5850fb0db18f5e40a642bbb4a4743de412ab54/packages/pg/lib/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| benchmark package | library | Observed | Groups 2 file(s) under benchmark package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 20 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Inferred | Groups 0 file(s) under data layer (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 69 file(s) under packages package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 201 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.devcontainer/Dockerfile` (container)
- `.devcontainer/devcontainer.json` (config)
- `.devcontainer/docker-compose.yml` (container)
- `.github/FUNDING.yml` (config)
- `.github/dependabot.yaml` (config)
- `.github/workflows/benchmark.yml` (ci)
- `.github/workflows/ci.yml` (ci)
- `docs/package.json` (manifest)
- `lerna.json` (config)
- `package.json` (manifest)
- `packages/pg-bundler-test/package.json` (manifest)
- `packages/pg-cloudflare/package.json` (manifest)
- `packages/pg-cloudflare/tsconfig.json` (config)
- `packages/pg-connection-string/.coveralls.yml` (config)
- `packages/pg-connection-string/.mocharc.json` (config)
- `packages/pg-connection-string/package.json` (manifest)
- `packages/pg-connection-string/tsconfig.json` (config)
- `packages/pg-cursor/package.json` (manifest)
- `packages/pg-esm-test/package.json` (manifest)
- `packages/pg-native/package.json` (manifest)
- `packages/pg-pool/package.json` (manifest)
- `packages/pg-protocol/package.json` (manifest)
- `packages/pg-protocol/tsconfig.json` (config)
- `packages/pg-query-stream/package.json` (manifest)
- `packages/pg-query-stream/tsconfig.json` (config)
- `packages/pg/package.json` (manifest)
- `tea.yaml` (config)
- `tsconfig.json` (config)

## Top-level layout

- `packages` — 300 analysed file(s)
- `docs` — 35 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `.github` — 5 analysed file(s)
- `.devcontainer` — 3 analysed file(s)
- `benchmark` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 6 file(s) were skipped during inventory (5 x likely secret file excluded; 1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `2a5850fb0db18f5e40a642bbb4a4743de412ab54` is the revision these paths and observations refer to.
