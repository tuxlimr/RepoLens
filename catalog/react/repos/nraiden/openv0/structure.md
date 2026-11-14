# Project structure: nraiden/openv0

**Analysed commit:** `8d87809b09a4c65d5af7b0fa8ee7c9475b378286`

**Commit reference:** [8d87809b09a4c65d5af7b0fa8ee7c9475b378286](https://github.com/nraiden/openv0/commit/8d87809b09a4c65d5af7b0fa8ee7c9475b378286)

**Tree at this commit:** [nraiden/openv0@8d87809b09a4](https://github.com/nraiden/openv0/tree/8d87809b09a4c65d5af7b0fa8ee7c9475b378286)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | nraiden/openv0 |
| Description | AI generated UI components |
| Stars | 3955 |
| Forks | 341 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `8d87809b09a4c65d5af7b0fa8ee7c9475b378286` |
| Retrieved at | 2026-11-14T19:14:57.770152+00:00 |
| Files in this snapshot | 352 |

## Directory tree

```text
npx/  (3 files)
  .gitignore
  bin.js
  package.json
server/  (63 files)
  library/  (14 files)
    components/  (11 files)
      … 11 files under this directory
    icons/  (2 files)
      … 2 files under this directory
    README.md
  modules/  (38 files)
    log/  (1 files)
      … 1 files under this directory
    multipass/  (36 files)
      … 36 files under this directory
    README.md
  .gitignore
  .prettierignore
  _test.build.js
  _test.component_from_json.example.js
  _test.db_build.js
  _test.multipass.js
  _validate+postprocess.test.js
  api.js
  build.js
  db.js
  package.json
webapps-starters/  (283 files)
  react/  (102 files)
    flowbite/  (19 files)
      … 19 files under this directory
    nextui/  (19 files)
      … 19 files under this directory
    shadcn/  (64 files)
      … 64 files under this directory
  svelte/  (180 files)
    flowbite/  (14 files)
      … 14 files under this directory
    shadcn/  (166 files)
      … 166 files under this directory
  README.md
.gitignore
LICENSE
README.md
```

## Entry points

- [npx/bin.js](https://github.com/nraiden/openv0/blob/8d87809b09a4c65d5af7b0fa8ee7c9475b378286/npx/bin.js)
- [server/modules/log/index.js](https://github.com/nraiden/openv0/blob/8d87809b09a4c65d5af7b0fa8ee7c9475b378286/server/modules/log/index.js)
- [server/modules/multipass/index.js](https://github.com/nraiden/openv0/blob/8d87809b09a4c65d5af7b0fa8ee7c9475b378286/server/modules/multipass/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 16 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 27 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Inferred | Groups 0 file(s) under data layer (observed from repository paths and static analysis). |
| npx package | library | Observed | Groups 1 file(s) under npx package (observed from repository paths and static analysis). |
| server package | library | Observed | Groups 30 file(s) under server package (observed from repository paths and static analysis). |
| webapps-starters package | library | Observed | Groups 224 file(s) under webapps-starters package (observed from repository paths and static analysis). |

## Important files

- `npx/package.json` (manifest)
- `server/library/components/next/flowbite/metadata.json` (config)
- `server/library/components/next/nextui/metadata.json` (config)
- `server/library/components/next/shadcn/dump.json` (config)
- `server/library/components/next/shadcn/metadata.json` (config)
- `server/library/components/react/flowbite/metadata.json` (config)
- `server/library/components/react/nextui/metadata.json` (config)
- `server/library/components/react/shadcn/dump.json` (config)
- `server/library/components/react/shadcn/metadata.json` (config)
- `server/library/components/svelte/flowbite/metadata.json` (config)
- `server/library/components/svelte/shadcn/dump.json` (config)
- `server/library/components/svelte/shadcn/metadata.json` (config)
- `server/library/icons/lucide/metadata.json` (config)
- `server/package.json` (manifest)
- `webapps-starters/react/flowbite/package.json` (manifest)
- `webapps-starters/react/flowbite/tsconfig.json` (config)
- `webapps-starters/react/flowbite/tsconfig.node.json` (config)
- `webapps-starters/react/nextui/package.json` (manifest)
- `webapps-starters/react/nextui/tsconfig.json` (config)
- `webapps-starters/react/nextui/tsconfig.node.json` (config)
- `webapps-starters/react/shadcn/components.json` (config)
- `webapps-starters/react/shadcn/package.json` (manifest)
- `webapps-starters/react/shadcn/tsconfig.json` (config)
- `webapps-starters/react/shadcn/tsconfig.node.json` (config)
- `webapps-starters/svelte/flowbite/package.json` (manifest)
- `webapps-starters/svelte/shadcn/components.json` (config)
- `webapps-starters/svelte/shadcn/package.json` (manifest)

## Top-level layout

- `webapps-starters` — 283 analysed file(s)
- `server` — 63 analysed file(s)
- `(root files)` — 3 analysed file(s)
- `npx` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 23 file(s) were skipped during inventory (3 x likely secret file excluded; 3 x lockfile excluded; 17 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `8d87809b09a4c65d5af7b0fa8ee7c9475b378286` is the revision these paths and observations refer to.
