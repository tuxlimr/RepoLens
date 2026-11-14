# Project structure: pmndrs/react-three-fiber

**Analysed commit:** `d74622ea8ed717f7212d7e19d65ff3e325508389`

**Commit reference:** [d74622ea8ed717f7212d7e19d65ff3e325508389](https://github.com/pmndrs/react-three-fiber/commit/d74622ea8ed717f7212d7e19d65ff3e325508389)

**Tree at this commit:** [pmndrs/react-three-fiber@d74622ea8ed7](https://github.com/pmndrs/react-three-fiber/tree/d74622ea8ed717f7212d7e19d65ff3e325508389)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | pmndrs/react-three-fiber |
| Description | 🇨🇭 A React renderer for Three.js |
| Stars | 33723 |
| Forks | 2108 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `d74622ea8ed717f7212d7e19d65ff3e325508389` |
| Retrieved at | 2026-11-14T19:13:02.728413+00:00 |
| Files in this snapshot | 185 |

## Directory tree

```text
.changeset/  (5 files)
  README.md
  config.json
  portal-leaks-v9.md
  quiet-tags-narrow.md
  sharp-screens-follow.md
.github/  (7 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (2 files)
    docs.yml
    test.yml
  FUNDING.yml
  issue_template.md
  pull_request_template.md
.husky/  (2 files)
  .gitignore
  pre-commit
docs/  (23 files)
  API/  (7 files)
    additional-exports.mdx
    canvas.mdx
    events.mdx
    hooks.mdx
    objects.mdx
    testing.mdx
    typescript.mdx
  advanced/  (2 files)
    pitfalls.mdx
    scaling-performance.mdx
  development/  (1 files)
    CORE.md
  getting-started/  (7 files)
    basic-example-sandpack/  (2 files)
      … 2 files under this directory
    community-r3f-components.mdx
    examples.mdx
    installation.mdx
    introduction.mdx
    your-first-scene.mdx
  tutorials/  (6 files)
    basic-animations.mdx
    events-and-interaction.mdx
    how-it-works.mdx
    loading-models.mdx
    loading-textures.mdx
    v9-migration-guide.mdx
example/  (45 files)
  public/  (5 files)
    apple.gltf
    bottle.gltf
    farm.gltf
    lightning.gltf
    ramen.gltf
  src/  (33 files)
    demos/  (29 files)
      … 29 files under this directory
    App.tsx
    components.tsx
    index.tsx
    styles.css
  .gitignore
  CHANGELOG.md
  favicon.svg
  index.html
  package.json
  tsconfig.json
  vite.config.ts
packages/  (90 files)
  eslint-plugin/  (16 files)
    docs/  (2 files)
      … 2 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    src/  (7 files)
      … 7 files under this directory
    tests/  (2 files)
      … 2 files under this directory
    .npmignore
    CHANGELOG.md
    README.md
    package.json
  fiber/  (48 files)
    __mocks__/  (5 files)
      … 5 files under this directory
    native/  (1 files)
      … 1 files under this directory
    src/  (22 files)
      … 22 files under this directory
    tests/  (16 files)
      … 16 files under this directory
    .npmignore
    CHANGELOG.md
    package.json
    readme.md
  shared/  (1 files)
    setupTests.ts
  test-renderer/  (25 files)
    markdown/  (2 files)
      … 2 files under this directory
    src/  (19 files)
      … 19 files under this directory
    .npmignore
    CHANGELOG.md
    README.md
    package.json
.eslintignore
.eslintrc.json
.gitignore
.prettierignore
.prettierrc
CONTRIBUTING.md
LICENSE
babel.config.js
jest.config.js
package.json
readme.md
tsconfig.json
vite.config.ts
```

## Entry points

- [packages/eslint-plugin/src/index.ts](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/eslint-plugin/src/index.ts)
- [packages/fiber/src/index.tsx](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/fiber/src/index.tsx)
- [packages/test-renderer/src/index.tsx](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/test-renderer/src/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 8 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 38 file(s) under packages package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 14 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 18 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.eslintrc.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/workflows/docs.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `example/package.json` (manifest)
- `example/tsconfig.json` (config)
- `package.json` (manifest)
- `packages/eslint-plugin/package.json` (manifest)
- `packages/fiber/native/package.json` (manifest)
- `packages/fiber/package.json` (manifest)
- `packages/test-renderer/package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `packages` — 90 analysed file(s)
- `example` — 45 analysed file(s)
- `docs` — 23 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `.github` — 7 analysed file(s)
- `.changeset` — 5 analysed file(s)
- `.husky` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `d74622ea8ed717f7212d7e19d65ff3e325508389` is the revision these paths and observations refer to.
