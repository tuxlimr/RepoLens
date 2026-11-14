# Project structure: nraiden/cofounder

**Analysed commit:** `19ba19f61737d654493175208df468395e2193f4`

**Commit reference:** [19ba19f61737d654493175208df468395e2193f4](https://github.com/nraiden/cofounder/commit/19ba19f61737d654493175208df468395e2193f4)

**Tree at this commit:** [nraiden/cofounder@19ba19f61737](https://github.com/nraiden/cofounder/tree/19ba19f61737d654493175208df468395e2193f4)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | nraiden/cofounder |
| Description | ai-generated apps , full stack + generative UI |
| Stars | 6648 |
| Forks | 713 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `19ba19f61737d654493175208df468395e2193f4` |
| Retrieved at | 2026-11-14T19:14:02.841995+00:00 |
| Files in this snapshot | 306 |

## Directory tree

```text
apps/  (1 files)
  README.md
benchmarks/  (1 files)
  README.md
cofounder/  (298 files)
  api/  (110 files)
    db/  (4 files)
      … 4 files under this directory
    system/  (90 files)
      … 90 files under this directory
    utils/  (9 files)
      … 9 files under this directory
    .gitignore
    .prettierignore
    .prettierrc
    README.md
    build.js
    package.json
    server.js
  boilerplate/  (93 files)
    backend-boilerplate/  (5 files)
      … 5 files under this directory
    vitereact-boilerplate/  (86 files)
      … 86 files under this directory
    README.md
    package.json
  dashboard/  (95 files)
    src/  (80 files)
      … 80 files under this directory
    .gitignore
    .prettierignore
    .prettierrc
    README.md
    components.json
    eslint.config.js
    index.html
    package.json
    postcss.config.js
    tailwind.config.js
    tailwind.config.js.bak
    tsconfig.app.json
    tsconfig.json
    tsconfig.node.json
    vite.config.ts
.gitignore
CONTRIBUTING.md
LICENSE
README.md
ROADMAP.md
TODO.md
```

## Entry points

- [cofounder/api/server.js](https://github.com/nraiden/cofounder/blob/19ba19f61737d654493175208df468395e2193f4/cofounder/api/server.js)
- [cofounder/api/utils/index.js](https://github.com/nraiden/cofounder/blob/19ba19f61737d654493175208df468395e2193f4/cofounder/api/utils/index.js)
- [cofounder/boilerplate/backend-boilerplate/server.js](https://github.com/nraiden/cofounder/blob/19ba19f61737d654493175208df468395e2193f4/cofounder/boilerplate/backend-boilerplate/server.js)
- [cofounder/dashboard/src/App.tsx](https://github.com/nraiden/cofounder/blob/19ba19f61737d654493175208df468395e2193f4/cofounder/dashboard/src/App.tsx)
- [cofounder/dashboard/src/main.tsx](https://github.com/nraiden/cofounder/blob/19ba19f61737d654493175208df468395e2193f4/cofounder/dashboard/src/main.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 44 file(s) under api layer (observed from repository paths and static analysis). |
| cofounder package | library | Observed | Groups 138 file(s) under cofounder package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 43 file(s) under configuration and deployment (observed from repository paths and static analysis). |

## Important files

- `cofounder/api/package.json` (manifest)
- `cofounder/api/system/presets/ui/design/systems/protoboy-v1/primitives/ontology.yaml` (config)
- `cofounder/api/system/presets/ui/design/systems/shadcn/primitives/ontology.yaml` (config)
- `cofounder/api/system/structure/nodes/backend/asyncapi.yaml` (config)
- `cofounder/api/system/structure/nodes/backend/openapi.yaml` (config)
- `cofounder/api/system/structure/nodes/backend/server.yaml` (config)
- `cofounder/api/system/structure/nodes/db/postgres.yaml` (config)
- `cofounder/api/system/structure/nodes/db/schemas.yaml` (config)
- `cofounder/api/system/structure/nodes/designer/layoutv1.yaml` (config)
- `cofounder/api/system/structure/nodes/op/convert.yaml` (config)
- `cofounder/api/system/structure/nodes/op/indexdb.yaml` (config)
- `cofounder/api/system/structure/nodes/op/llm.yaml` (config)
- `cofounder/api/system/structure/nodes/op/project.yaml` (config)
- `cofounder/api/system/structure/nodes/op/render.yaml` (config)
- `cofounder/api/system/structure/nodes/pm/brd.yaml` (config)
- `cofounder/api/system/structure/nodes/pm/drb.yaml` (config)
- `cofounder/api/system/structure/nodes/pm/fjmd.yaml` (config)
- `cofounder/api/system/structure/nodes/pm/frd.yaml` (config)
- `cofounder/api/system/structure/nodes/pm/prd.yaml` (config)
- `cofounder/api/system/structure/nodes/pm/uxdmd.yaml` (config)
- `cofounder/api/system/structure/nodes/pm/uxsmd.yaml` (config)
- `cofounder/api/system/structure/nodes/swarm/augment.yaml` (config)
- `cofounder/api/system/structure/nodes/swarm/fix.yaml` (config)
- `cofounder/api/system/structure/nodes/swarm/review.yaml` (config)
- `cofounder/api/system/structure/nodes/ux/datamap.yaml` (config)
- `cofounder/api/system/structure/nodes/ux/sitemap.yaml` (config)
- `cofounder/api/system/structure/nodes/webapp/root.yaml` (config)
- `cofounder/api/system/structure/nodes/webapp/store.yaml` (config)
- `cofounder/api/system/structure/nodes/webapp/view.yaml` (config)
- `cofounder/api/system/structure/sequences/projectInit.yaml` (config)
- `cofounder/boilerplate/backend-boilerplate/package.json` (manifest)
- `cofounder/boilerplate/package.json` (manifest)
- `cofounder/boilerplate/vitereact-boilerplate/components.json` (config)
- `cofounder/boilerplate/vitereact-boilerplate/package.json` (manifest)
- `cofounder/boilerplate/vitereact-boilerplate/src/_cofounder/meta.json` (config)
- `cofounder/boilerplate/vitereact-boilerplate/tsconfig.app.json` (config)
- `cofounder/boilerplate/vitereact-boilerplate/tsconfig.json` (config)
- `cofounder/boilerplate/vitereact-boilerplate/tsconfig.node.json` (config)
- `cofounder/dashboard/components.json` (config)
- `cofounder/dashboard/package.json` (manifest)
- `cofounder/dashboard/tsconfig.app.json` (config)
- `cofounder/dashboard/tsconfig.json` (config)
- `cofounder/dashboard/tsconfig.node.json` (config)

## Top-level layout

- `cofounder` — 298 analysed file(s)
- `(root files)` — 6 analysed file(s)
- `apps` — 1 analysed file(s)
- `benchmarks` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 4 file(s) were skipped during inventory (2 x likely secret file excluded; 2 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `19ba19f61737d654493175208df468395e2193f4` is the revision these paths and observations refer to.
