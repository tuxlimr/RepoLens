# Project structure: ekzhang/rustpad

**Analysed commit:** `54e4a9383c84d7317af42a7ddb177ce8bcba058d`

**Commit reference:** [54e4a9383c84d7317af42a7ddb177ce8bcba058d](https://github.com/ekzhang/rustpad/commit/54e4a9383c84d7317af42a7ddb177ce8bcba058d)

**Tree at this commit:** [ekzhang/rustpad@54e4a9383c84](https://github.com/ekzhang/rustpad/tree/54e4a9383c84d7317af42a7ddb177ce8bcba058d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | ekzhang/rustpad |
| Description | Efficient and minimal collaborative code editor, self-hosted, no database required |
| Stars | 4085 |
| Forks | 222 |
| Licence | MIT |
| Language | Rust |
| Default branch | main |
| Analysed commit | `54e4a9383c84d7317af42a7ddb177ce8bcba058d` |
| Retrieved at | 2026-11-14T19:14:54.406022+00:00 |
| Files in this snapshot | 46 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    ci.yml
public/  (1 files)
  favicon.svg
rustpad-server/  (14 files)
  migrations/  (1 files)
    1_document.sql
  src/  (5 files)
    database.rs
    lib.rs
    main.rs
    ot.rs
    rustpad.rs
  tests/  (7 files)
    common/  (1 files)
      … 1 files under this directory
    cleanup.rs
    persist.rs
    sockets.rs
    stress.rs
    unicode.rs
    users.rs
  Cargo.toml
rustpad-wasm/  (4 files)
  src/  (2 files)
    lib.rs
    utils.rs
  tests/  (1 files)
    web.rs
  Cargo.toml
src/  (13 files)
  App.tsx
  ConnectionStatus.tsx
  Footer.tsx
  ReadCodeConfirm.tsx
  Sidebar.tsx
  User.tsx
  animals.json
  index.css
  index.tsx
  languages.json
  rustpad.ts
  useHash.ts
  vite-env.d.ts
.dockerignore
.editorconfig
.gitignore
.prettierignore
.prettierrc
Cargo.toml
Dockerfile
LICENSE
README.md
index.html
package.json
tsconfig.json
vite.config.ts
```

## Entry points

- [src/App.tsx](https://github.com/ekzhang/rustpad/blob/54e4a9383c84d7317af42a7ddb177ce8bcba058d/src/App.tsx)
- [src/index.tsx](https://github.com/ekzhang/rustpad/blob/54e4a9383c84d7317af42a7ddb177ce8bcba058d/src/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| App.tsx package | library | Observed | Groups 1 file(s) under app.tsx package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 8 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| ConnectionStatus.tsx package | library | Observed | Groups 1 file(s) under connectionstatus.tsx package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Footer.tsx package | library | Observed | Groups 1 file(s) under footer.tsx package (observed from repository paths and static analysis). |
| index.tsx package | library | Observed | Groups 1 file(s) under index.tsx package (observed from repository paths and static analysis). |
| ReadCodeConfirm.tsx package | library | Observed | Groups 1 file(s) under readcodeconfirm.tsx package (observed from repository paths and static analysis). |
| rustpad-server package | library | Observed | Groups 5 file(s) under rustpad-server package (observed from repository paths and static analysis). |
| rustpad.ts package | library | Observed | Groups 1 file(s) under rustpad.ts package (observed from repository paths and static analysis). |
| rustpad-wasm package | library | Observed | Groups 2 file(s) under rustpad-wasm package (observed from repository paths and static analysis). |
| Sidebar.tsx package | library | Observed | Groups 1 file(s) under sidebar.tsx package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 8 file(s) under tests (observed from repository paths and static analysis). |
| useHash.ts package | library | Observed | Groups 1 file(s) under usehash.ts package (observed from repository paths and static analysis). |
| User.tsx package | library | Observed | Groups 1 file(s) under user.tsx package (observed from repository paths and static analysis). |
| vite-env.d.ts package | library | Observed | Groups 1 file(s) under vite-env.d.ts package (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.editorconfig` (config)
- `.github/workflows/ci.yml` (ci)
- `Cargo.toml` (manifest)
- `Dockerfile` (container)
- `package.json` (manifest)
- `rustpad-server/Cargo.toml` (manifest)
- `rustpad-wasm/Cargo.toml` (manifest)
- `src/animals.json` (config)
- `src/languages.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `rustpad-server` — 14 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `src` — 13 analysed file(s)
- `rustpad-wasm` — 4 analysed file(s)
- `.github` — 1 analysed file(s)
- `public` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 3 file(s) were skipped during inventory (1 x likely secret file excluded; 2 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `54e4a9383c84d7317af42a7ddb177ce8bcba058d` is the revision these paths and observations refer to.
