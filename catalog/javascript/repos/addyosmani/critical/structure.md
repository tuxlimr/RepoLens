# Project structure: addyosmani/critical

**Analysed commit:** `03897c82e255416ca7104774a9d19142bd1e2744`

**Commit reference:** [03897c82e255416ca7104774a9d19142bd1e2744](https://github.com/addyosmani/critical/commit/03897c82e255416ca7104774a9d19142bd1e2744)

**Tree at this commit:** [addyosmani/critical@03897c82e255](https://github.com/addyosmani/critical/tree/03897c82e255416ca7104774a9d19142bd1e2744)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | addyosmani/critical |
| Description | Extract & Inline Critical-path CSS in HTML pages |
| Stars | 10302 |
| Forks | 394 |
| Licence | Apache-2.0 |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `03897c82e255416ca7104774a9d19142bd1e2744` |
| Retrieved at | 2026-11-14T19:12:41.612303+00:00 |
| Files in this snapshot | 49 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (2 files)
    docker.yml
    test.yml
.vite-hooks/  (1 files)
  pre-commit
bench/  (2 files)
  lib.mjs
  vs-beasties.mjs
fixtures/  (10 files)
  rebase/  (2 files)
    styles/  (1 files)
      … 1 files under this directory
    index.html
  app.css
  index.html
  long.html
  spa-app.html
  spa-external.html
  spa-external.js
  spa.html
  styles.css
src/  (10 files)
  engines/  (2 files)
    render.js
    static.js
  css.js
  detect.js
  index.d.ts
  index.js
  inline.js
  mcp.d.ts
  mcp.js
  source.js
test/  (11 files)
  api.test.js
  cli.test.js
  critical.test.js
  css-option.test.js
  fold-aware.test.js
  issues.test.js
  mcp.test.js
  remote.test.js
  source.test.js
  spa.test.js
  vs-beasties.test.js
.editorconfig
.gitattributes
.gitignore
CHANGELOG.md
COMPARISON.md
CONTRIBUTING.md
Dockerfile
README.md
cli.js
license
package.json
pnpm-workspace.yaml
vite.config.ts
```

## Entry points

- [cli.js](https://github.com/addyosmani/critical/blob/03897c82e255416ca7104774a9d19142bd1e2744/cli.js)
- [src/index.js](https://github.com/addyosmani/critical/blob/03897c82e255416ca7104774a9d19142bd1e2744/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bench package | library | Observed | Groups 2 file(s) under bench package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| css.js package | library | Observed | Groups 1 file(s) under css.js package (observed from repository paths and static analysis). |
| detect.js package | library | Observed | Groups 1 file(s) under detect.js package (observed from repository paths and static analysis). |
| engines package | library | Observed | Groups 2 file(s) under engines package (observed from repository paths and static analysis). |
| fixtures package | library | Observed | Groups 1 file(s) under fixtures package (observed from repository paths and static analysis). |
| index.d.ts package | library | Observed | Groups 1 file(s) under index.d.ts package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| inline.js package | library | Observed | Groups 1 file(s) under inline.js package (observed from repository paths and static analysis). |
| mcp.d.ts package | library | Observed | Groups 1 file(s) under mcp.d.ts package (observed from repository paths and static analysis). |
| mcp.js package | library | Observed | Groups 1 file(s) under mcp.js package (observed from repository paths and static analysis). |
| source.js package | library | Observed | Groups 1 file(s) under source.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 11 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/workflows/docker.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `Dockerfile` (container)
- `package.json` (manifest)
- `pnpm-workspace.yaml` (config)

## Top-level layout

- `(root files)` — 13 analysed file(s)
- `test` — 11 analysed file(s)
- `fixtures` — 10 analysed file(s)
- `src` — 10 analysed file(s)
- `.github` — 2 analysed file(s)
- `bench` — 2 analysed file(s)
- `.vite-hooks` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (1 x likely secret file excluded; 1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `03897c82e255416ca7104774a9d19142bd1e2744` is the revision these paths and observations refer to.
