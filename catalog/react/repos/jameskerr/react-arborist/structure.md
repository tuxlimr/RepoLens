# Project structure: jameskerr/react-arborist

**Analysed commit:** `b44e01af4907cab7cf0738288e25d09acdd0c4d0`

**Commit reference:** [b44e01af4907cab7cf0738288e25d09acdd0c4d0](https://github.com/jameskerr/react-arborist/commit/b44e01af4907cab7cf0738288e25d09acdd0c4d0)

**Tree at this commit:** [jameskerr/react-arborist@b44e01af4907](https://github.com/jameskerr/react-arborist/tree/b44e01af4907cab7cf0738288e25d09acdd0c4d0)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | jameskerr/react-arborist |
| Description | The complete tree view component for React |
| Stars | 3717 |
| Forks | 188 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `b44e01af4907cab7cf0738288e25d09acdd0c4d0` |
| Retrieved at | 2026-11-14T19:15:07.759308+00:00 |
| Files in this snapshot | 178 |

## Directory tree

```text
.changes/  (1 files)
  README.md
.github/  (4 files)
  workflows/  (3 files)
    build-and-test.yml
    changeset.yml
    publish.yml
  pull_request_template.md
.yarn/  (7 files)
  versions/  (7 files)
    10de8bbe.yml
    29c64826.yml
    5b5c1471.yml
    894d7021.yml
    9ef5f981.yml
    b57f0b1e.yml
    c94fa517.yml
bin/  (2 files)
  publish
  release.mjs
modules/  (151 files)
  docs/  (47 files)
    archetypes/  (1 files)
      … 1 files under this directory
    assets/  (25 files)
      … 25 files under this directory
    content/  (2 files)
      … 2 files under this directory
    layouts/  (11 files)
      … 11 files under this directory
    .gitignore
    .hugo_build.lock
    .prettierrc
    README.md
    hugo.toml
    package.json
    postcss.config.js
    tailwind.config.js
  e2e/  (12 files)
    cypress/  (8 files)
      … 8 files under this directory
    .gitignore
    README.md
    cypress.config.js
    package.json
  react-arborist/  (66 files)
    src/  (62 files)
      … 62 files under this directory
    .gitignore
    jest.config.cjs
    package.json
    tsconfig.json
  showcase/  (26 files)
    components/  (3 files)
      … 3 files under this directory
    data/  (1 files)
      … 1 files under this directory
    pages/  (9 files)
      … 9 files under this directory
    public/  (1 files)
      … 1 files under this directory
    styles/  (6 files)
      … 6 files under this directory
    .eslintrc.json
    .gitignore
    README.md
    next.config.js
    package.json
    tsconfig.json
.editorconfig
.gitignore
.node-version
.oxfmtrc.json
.oxlintrc.json
.yarnrc.yml
AGENTS.md
CHANGELOG.md
CONTRIBUTING.md
LICENSE
README.md
netlify.toml
package.json
```

## Entry points

- [modules/react-arborist/src/index.ts](https://github.com/jameskerr/react-arborist/blob/b44e01af4907cab7cf0738288e25d09acdd0c4d0/modules/react-arborist/src/index.ts)
- [modules/showcase/pages/index.tsx](https://github.com/jameskerr/react-arborist/blob/b44e01af4907cab7cf0738288e25d09acdd0c4d0/modules/showcase/pages/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bin package | library | Observed | Groups 1 file(s) under bin package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 16 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 9 file(s) under data layer (observed from repository paths and static analysis). |
| modules package | library | Observed | Groups 76 file(s) under modules package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/workflows/build-and-test.yml` (ci)
- `.github/workflows/changeset.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.oxfmtrc.json` (config)
- `.oxlintrc.json` (config)
- `.yarn/versions/10de8bbe.yml` (config)
- `.yarn/versions/29c64826.yml` (config)
- `.yarn/versions/5b5c1471.yml` (config)
- `.yarn/versions/894d7021.yml` (config)
- `.yarn/versions/9ef5f981.yml` (config)
- `.yarn/versions/b57f0b1e.yml` (config)
- `.yarn/versions/c94fa517.yml` (config)
- `.yarnrc.yml` (config)
- `modules/docs/assets/design-tokens/colors.json` (config)
- `modules/docs/assets/design-tokens/fonts.json` (config)
- `modules/docs/assets/design-tokens/text-leading.json` (config)
- `modules/docs/assets/design-tokens/text-weights.json` (config)
- `modules/docs/assets/design-tokens/viewports.json` (config)
- `modules/docs/hugo.toml` (config)
- `modules/docs/package.json` (manifest)
- `modules/e2e/cypress/fixtures/example.json` (config)
- `modules/e2e/package.json` (manifest)
- `modules/react-arborist/package.json` (manifest)
- `modules/react-arborist/tsconfig.json` (config)
- `modules/showcase/.eslintrc.json` (config)
- `modules/showcase/package.json` (manifest)
- `modules/showcase/tsconfig.json` (config)
- `netlify.toml` (config)
- `package.json` (manifest)

## Top-level layout

- `modules` — 151 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `.yarn` — 7 analysed file(s)
- `.github` — 4 analysed file(s)
- `bin` — 2 analysed file(s)
- `.changes` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `b44e01af4907cab7cf0738288e25d09acdd0c4d0` is the revision these paths and observations refer to.
