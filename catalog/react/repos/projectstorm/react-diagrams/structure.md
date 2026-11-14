# Project structure: projectstorm/react-diagrams

**Analysed commit:** `cd3bdd119376836a0c675be5e3e58ee807cfd0c1`

**Commit reference:** [cd3bdd119376836a0c675be5e3e58ee807cfd0c1](https://github.com/projectstorm/react-diagrams/commit/cd3bdd119376836a0c675be5e3e58ee807cfd0c1)

**Tree at this commit:** [projectstorm/react-diagrams@cd3bdd119376](https://github.com/projectstorm/react-diagrams/tree/cd3bdd119376836a0c675be5e3e58ee807cfd0c1)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | projectstorm/react-diagrams |
| Description | a super simple, no-nonsense diagramming library written in react that just works |
| Stars | 9437 |
| Forks | 1177 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `cd3bdd119376836a0c675be5e3e58ee807cfd0c1` |
| Retrieved at | 2026-11-14T19:13:33.840103+00:00 |
| Files in this snapshot | 229 |

## Directory tree

```text
.changeset/  (3 files)
  README.md
  cold-drinks-unite.md
  config.json
.github/  (4 files)
  workflows/  (3 files)
    prettier.yml
    release.yml
    test.yml
  PULL_REQUEST_TEMPLATE.md
diagrams-demo-gallery/  (58 files)
  .storybook/  (5 files)
    main.js
    manager.js
    preview-head.html
    preview.js
    theme.js
  demos/  (49 files)
    demo-alternative-linking/  (3 files)
      … 3 files under this directory
    demo-animation/  (1 files)
      … 1 files under this directory
    demo-canvas-drag/  (1 files)
      … 1 files under this directory
    demo-cloning/  (1 files)
      … 1 files under this directory
    demo-custom-action/  (1 files)
      … 1 files under this directory
    demo-custom-link-label/  (4 files)
      … 4 files under this directory
    demo-custom-link1/  (1 files)
      … 1 files under this directory
    demo-custom-link2/  (1 files)
      … 1 files under this directory
    demo-custom-node1/  (6 files)
      … 6 files under this directory
    demo-custom_delete_keys/  (1 files)
      … 1 files under this directory
    demo-dagre/  (1 files)
      … 1 files under this directory
    demo-drag-and-drop/  (5 files)
      … 5 files under this directory
    demo-dynamic-ports/  (1 files)
      … 1 files under this directory
    demo-grid/  (1 files)
      … 1 files under this directory
    demo-labelled-links/  (1 files)
      … 1 files under this directory
    demo-listeners/  (1 files)
      … 1 files under this directory
    demo-locks/  (1 files)
      … 1 files under this directory
    demo-mutate-graph/  (1 files)
      … 1 files under this directory
    demo-pan-and-zoom/  (1 files)
      … 1 files under this directory
    demo-performance/  (1 files)
      … 1 files under this directory
    demo-right-angles-routing/  (1 files)
      … 1 files under this directory
    demo-serializing/  (1 files)
      … 1 files under this directory
    demo-simple/  (1 files)
      … 1 files under this directory
    demo-simple-flow/  (1 files)
      … 1 files under this directory
    demo-smart-routing/  (1 files)
      … 1 files under this directory
    demo-zoom-to-fit/  (1 files)
      … 1 files under this directory
    demo-zoom-to-fit-nodes/  (1 files)
      … 1 files under this directory
    helpers/  (4 files)
      … 4 files under this directory
    1_SimpleUsage.stories.tsx
    2_AdvancedUsage.stories.tsx
    3_Customization.stories.tsx
    4_Libraries.stories.tsx
  .babelrc.json
  CHANGELOG.md
  package.json
  tsconfig.json
diagrams-demo-project/  (16 files)
  src/  (9 files)
    custom-node-js/  (3 files)
      … 3 files under this directory
    custom-node-ts/  (3 files)
      … 3 files under this directory
    BodyWidget.tsx
    main.css
    main.tsx
  .babelrc
  CHANGELOG.md
  README.md
  index.html
  package.json
  tsconfig.json
  webpack.config.js
docs/  (9 files)
  about-the-project/  (2 files)
    architecture-questions.md
    testing.md
  customizing/  (4 files)
    README.md
    extending-default-links.md
    nodes.md
    ports.md
  getting-started/  (2 files)
    README.md
    using-the-library.md
  README.md
packages/  (124 files)
  geometry/  (13 files)
    src/  (8 files)
      … 8 files under this directory
    .npmignore
    CHANGELOG.md
    package.json
    tsconfig.json
    webpack.config.js
  react-canvas-core/  (39 files)
    src/  (34 files)
      … 34 files under this directory
    .npmignore
    CHANGELOG.md
    package.json
    tsconfig.json
    webpack.config.js
  react-diagrams/  (7 files)
    src/  (1 files)
      … 1 files under this directory
    .npmignore
    CHANGELOG.md
    README.md
    package.json
    tsconfig.json
    webpack.config.js
  react-diagrams-core/  (27 files)
    src/  (21 files)
      … 21 files under this directory
    .npmignore
    CHANGELOG.md
    README.md
    package.json
    tsconfig.json
    webpack.config.js
  react-diagrams-defaults/  (21 files)
    src/  (15 files)
      … 15 files under this directory
    .npmignore
    CHANGELOG.md
    README.md
    package.json
    tsconfig.json
    webpack.config.js
  react-diagrams-routing/  (17 files)
    src/  (9 files)
      … 9 files under this directory
    tests/  (1 files)
      … 1 files under this directory
    .npmignore
    CHANGELOG.md
    README.md
    jest.config.js
    package.json
    tsconfig.json
    webpack.config.js
.editorconfig
.envrc
.gitbook.yaml
.gitignore
.prettierignore
.prettierrc
CHANGELOG.md
CONTRIBUTING.md
LICENSE
README.md
package.json
pnpm-workspace.yaml
tsconfig.base.json
tsconfig.json
webpack.shared.js
```

## Entry points

- [diagrams-demo-gallery/.storybook/main.js](https://github.com/projectstorm/react-diagrams/blob/cd3bdd119376836a0c675be5e3e58ee807cfd0c1/diagrams-demo-gallery/.storybook/main.js)
- [diagrams-demo-gallery/demos/demo-alternative-linking/index.tsx](https://github.com/projectstorm/react-diagrams/blob/cd3bdd119376836a0c675be5e3e58ee807cfd0c1/diagrams-demo-gallery/demos/demo-alternative-linking/index.tsx)
- [diagrams-demo-gallery/demos/demo-animation/index.tsx](https://github.com/projectstorm/react-diagrams/blob/cd3bdd119376836a0c675be5e3e58ee807cfd0c1/diagrams-demo-gallery/demos/demo-animation/index.tsx)
- [diagrams-demo-gallery/demos/demo-canvas-drag/index.tsx](https://github.com/projectstorm/react-diagrams/blob/cd3bdd119376836a0c675be5e3e58ee807cfd0c1/diagrams-demo-gallery/demos/demo-canvas-drag/index.tsx)
- [diagrams-demo-gallery/demos/demo-cloning/index.tsx](https://github.com/projectstorm/react-diagrams/blob/cd3bdd119376836a0c675be5e3e58ee807cfd0c1/diagrams-demo-gallery/demos/demo-cloning/index.tsx)
- [diagrams-demo-gallery/demos/demo-custom-action/index.tsx](https://github.com/projectstorm/react-diagrams/blob/cd3bdd119376836a0c675be5e3e58ee807cfd0c1/diagrams-demo-gallery/demos/demo-custom-action/index.tsx)
- [diagrams-demo-gallery/demos/demo-custom-link-label/index.tsx](https://github.com/projectstorm/react-diagrams/blob/cd3bdd119376836a0c675be5e3e58ee807cfd0c1/diagrams-demo-gallery/demos/demo-custom-link-label/index.tsx)
- [diagrams-demo-gallery/demos/demo-custom-link1/index.tsx](https://github.com/projectstorm/react-diagrams/blob/cd3bdd119376836a0c675be5e3e58ee807cfd0c1/diagrams-demo-gallery/demos/demo-custom-link1/index.tsx)
- [diagrams-demo-gallery/demos/demo-custom-link2/index.tsx](https://github.com/projectstorm/react-diagrams/blob/cd3bdd119376836a0c675be5e3e58ee807cfd0c1/diagrams-demo-gallery/demos/demo-custom-link2/index.tsx)
- [diagrams-demo-gallery/demos/demo-custom-node1/index.tsx](https://github.com/projectstorm/react-diagrams/blob/cd3bdd119376836a0c675be5e3e58ee807cfd0c1/diagrams-demo-gallery/demos/demo-custom-node1/index.tsx)
- [diagrams-demo-gallery/demos/demo-custom_delete_keys/index.tsx](https://github.com/projectstorm/react-diagrams/blob/cd3bdd119376836a0c675be5e3e58ee807cfd0c1/diagrams-demo-gallery/demos/demo-custom_delete_keys/index.tsx)
- [diagrams-demo-gallery/demos/demo-dagre/index.tsx](https://github.com/projectstorm/react-diagrams/blob/cd3bdd119376836a0c675be5e3e58ee807cfd0c1/diagrams-demo-gallery/demos/demo-dagre/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 21 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). |
| diagrams-demo-gallery package | library | Observed | Groups 52 file(s) under diagrams-demo-gallery package (observed from repository paths and static analysis). |
| diagrams-demo-project package | library | Observed | Groups 9 file(s) under diagrams-demo-project package (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 88 file(s) under packages package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 6 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.editorconfig` (config)
- `.gitbook.yaml` (config)
- `.github/workflows/prettier.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `diagrams-demo-gallery/.babelrc.json` (config)
- `diagrams-demo-gallery/package.json` (manifest)
- `diagrams-demo-gallery/tsconfig.json` (config)
- `diagrams-demo-project/package.json` (manifest)
- `diagrams-demo-project/tsconfig.json` (config)
- `package.json` (manifest)
- `packages/geometry/package.json` (manifest)
- `packages/geometry/tsconfig.json` (config)
- `packages/react-canvas-core/package.json` (manifest)
- `packages/react-canvas-core/tsconfig.json` (config)
- `packages/react-diagrams-core/package.json` (manifest)
- `packages/react-diagrams-core/tsconfig.json` (config)
- `packages/react-diagrams-defaults/package.json` (manifest)
- `packages/react-diagrams-defaults/tsconfig.json` (config)
- `packages/react-diagrams-routing/package.json` (manifest)
- `packages/react-diagrams-routing/tsconfig.json` (config)
- `packages/react-diagrams/package.json` (manifest)
- `packages/react-diagrams/tsconfig.json` (config)
- `pnpm-workspace.yaml` (config)
- `tsconfig.base.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `packages` — 124 analysed file(s)
- `diagrams-demo-gallery` — 58 analysed file(s)
- `diagrams-demo-project` — 16 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `docs` — 9 analysed file(s)
- `.github` — 4 analysed file(s)
- `.changeset` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `cd3bdd119376836a0c675be5e3e58ee807cfd0c1` is the revision these paths and observations refer to.
