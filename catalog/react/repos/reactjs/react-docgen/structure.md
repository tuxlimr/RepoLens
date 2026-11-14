# Project structure: reactjs/react-docgen

**Analysed commit:** `6d4598b70d3776e28debfe1fddc7463fdf2958c6`

**Commit reference:** [6d4598b70d3776e28debfe1fddc7463fdf2958c6](https://github.com/reactjs/react-docgen/commit/6d4598b70d3776e28debfe1fddc7463fdf2958c6)

**Tree at this commit:** [reactjs/react-docgen@6d4598b70d37](https://github.com/reactjs/react-docgen/tree/6d4598b70d3776e28debfe1fddc7463fdf2958c6)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | reactjs/react-docgen |
| Description | A CLI and library to extract information from React component files for documentation generation purposes. |
| Stars | 3819 |
| Forks | 318 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | 8.x |
| Analysed commit | `6d4598b70d3776e28debfe1fddc7463fdf2958c6` |
| Retrieved at | 2026-11-14T19:15:04.595711+00:00 |
| Files in this snapshot | 401 |

## Directory tree

```text
.changeset/  (6 files)
  README.md
  calm-types-travel.md
  config.json
  mixin-class-props.md
  quiet-hooks-listen.md
  tidy-beans-smile.md
.github/  (5 files)
  workflows/  (4 files)
    build.yml
    changesets.yml
    lock.yml
    ossar-analysis.yml
  FUNDING.yml
benchmark/  (2 files)
  index.mjs
  package.json
packages/  (371 files)
  react-docgen/  (246 files)
    src/  (182 files)
      … 182 files under this directory
    tests/  (60 files)
      … 60 files under this directory
    CHANGELOG.md
    package.json
    tsconfig.json
    vitest.config.ts
  react-docgen-cli/  (44 files)
    src/  (8 files)
      … 8 files under this directory
    tests/  (31 files)
      … 31 files under this directory
    CHANGELOG.md
    README.md
    package.json
    tsconfig.json
    vitest.config.ts
  website/  (81 files)
    public/  (3 files)
      … 3 files under this directory
    src/  (67 files)
      … 67 files under this directory
    .gitignore
    .nvmrc
    README.md
    eslint.config.mjs
    netlify.toml
    next-sitemap.config.js
    next.config.mjs
    package.json
    postcss.config.js
    tailwind.config.ts
    tsconfig.json
.editorconfig
.gitattributes
.gitignore
.gitpod.yml
.prettierignore
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
SECURITY.md
eslint.config.mjs
nx.json
package.json
pnpm-workspace.yaml
prettier.config.mjs
renovate.json
tsconfig.base.json
```

## Entry points

- [packages/react-docgen/src/main.ts](https://github.com/reactjs/react-docgen/blob/6d4598b70d3776e28debfe1fddc7463fdf2958c6/packages/react-docgen/src/main.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 20 file(s) under api layer (observed from repository paths and static analysis). |
| benchmark package | library | Observed | Groups 1 file(s) under benchmark package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 14 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 164 file(s) under packages package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 91 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/workflows/build.yml` (ci)
- `.github/workflows/changesets.yml` (ci)
- `.github/workflows/lock.yml` (ci)
- `.github/workflows/ossar-analysis.yml` (ci)
- `.gitpod.yml` (config)
- `benchmark/package.json` (manifest)
- `nx.json` (config)
- `package.json` (manifest)
- `packages/react-docgen-cli/package.json` (manifest)
- `packages/react-docgen-cli/tsconfig.json` (config)
- `packages/react-docgen/package.json` (manifest)
- `packages/react-docgen/tsconfig.json` (config)
- `packages/website/netlify.toml` (config)
- `packages/website/package.json` (manifest)
- `packages/website/src/components/users/users.json` (config)
- `packages/website/tsconfig.json` (config)
- `pnpm-workspace.yaml` (config)
- `renovate.json` (config)
- `tsconfig.base.json` (config)

## Top-level layout

- `packages` — 371 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `.changeset` — 6 analysed file(s)
- `.github` — 5 analysed file(s)
- `benchmark` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 14 file(s) were skipped during inventory (1 x likely secret file excluded; 13 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `6d4598b70d3776e28debfe1fddc7463fdf2958c6` is the revision these paths and observations refer to.
