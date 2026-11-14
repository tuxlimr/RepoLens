# Project structure: typicode/json-server

**Analysed commit:** `89a34a44b7a6a5311dc84f3b8a1b8b45c0905aea`

**Commit reference:** [89a34a44b7a6a5311dc84f3b8a1b8b45c0905aea](https://github.com/typicode/json-server/commit/89a34a44b7a6a5311dc84f3b8a1b8b45c0905aea)

**Tree at this commit:** [typicode/json-server@89a34a44b7a6](https://github.com/typicode/json-server/tree/89a34a44b7a6a5311dc84f3b8a1b8b45c0905aea)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | typicode/json-server |
| Description | Get a full fake REST API with zero coding in less than 30 seconds (seriously) |
| Stars | 75743 |
| Forks | 7278 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `89a34a44b7a6a5311dc84f3b8a1b8b45c0905aea` |
| Retrieved at | 2026-11-14T19:10:33.483654+00:00 |
| Files in this snapshot | 32 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (2 files)
    node.js.yml
    publish.yml
  FUNDING.yml
.husky/  (1 files)
  pre-commit
fixtures/  (2 files)
  db.json
  db.json5
public/  (1 files)
  test.html
src/  (16 files)
  adapters/  (3 files)
    normalized-adapter.test.ts
    normalized-adapter.ts
    observer.ts
  app.test.ts
  app.ts
  bin.ts
  matches-where.test.ts
  matches-where.ts
  paginate.test.ts
  paginate.ts
  parse-where.test.ts
  parse-where.ts
  random-id.ts
  service.test.ts
  service.ts
  where-operators.ts
views/  (1 files)
  index.html
.gitattributes
.gitignore
.oxfmtrc.json
LICENSE
README.md
package.json
schema.json
tsconfig.json
```

## Entry points

- [src/app.ts](https://github.com/typicode/json-server/blob/89a34a44b7a6a5311dc84f3b8a1b8b45c0905aea/src/app.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| app.test.ts package | library | Observed | Groups 1 file(s) under app.test.ts package (observed from repository paths and static analysis). |
| app.ts package | library | Observed | Groups 1 file(s) under app.ts package (observed from repository paths and static analysis). |
| bin.ts package | library | Observed | Groups 1 file(s) under bin.ts package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 3 file(s) under external integrations (observed from repository paths and static analysis). |
| matches-where.test.ts package | library | Observed | Groups 1 file(s) under matches-where.test.ts package (observed from repository paths and static analysis). |
| matches-where.ts package | library | Observed | Groups 1 file(s) under matches-where.ts package (observed from repository paths and static analysis). |
| paginate.test.ts package | library | Observed | Groups 1 file(s) under paginate.test.ts package (observed from repository paths and static analysis). |
| paginate.ts package | library | Observed | Groups 1 file(s) under paginate.ts package (observed from repository paths and static analysis). |
| parse-where.test.ts package | library | Observed | Groups 1 file(s) under parse-where.test.ts package (observed from repository paths and static analysis). |
| parse-where.ts package | library | Observed | Groups 1 file(s) under parse-where.ts package (observed from repository paths and static analysis). |
| random-id.ts package | library | Observed | Groups 1 file(s) under random-id.ts package (observed from repository paths and static analysis). |
| service.test.ts package | library | Observed | Groups 1 file(s) under service.test.ts package (observed from repository paths and static analysis). |
| service.ts package | library | Observed | Groups 1 file(s) under service.ts package (observed from repository paths and static analysis). |
| where-operators.ts package | library | Observed | Groups 1 file(s) under where-operators.ts package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/workflows/node.js.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.oxfmtrc.json` (config)
- `fixtures/db.json` (config)
- `package.json` (manifest)
- `schema.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `src` — 16 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `.github` — 3 analysed file(s)
- `fixtures` — 2 analysed file(s)
- `.husky` — 1 analysed file(s)
- `public` — 1 analysed file(s)
- `views` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `89a34a44b7a6a5311dc84f3b8a1b8b45c0905aea` is the revision these paths and observations refer to.
