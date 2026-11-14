# Project structure: samdenty/gqless

**Analysed commit:** `27e289932cf45536c4e91190b96a4c9ce3d95063`

**Commit reference:** [27e289932cf45536c4e91190b96a4c9ce3d95063](https://github.com/samdenty/gqless/commit/27e289932cf45536c4e91190b96a4c9ce3d95063)

**Tree at this commit:** [samdenty/gqless@27e289932cf4](https://github.com/samdenty/gqless/tree/27e289932cf45536c4e91190b96a4c9ce3d95063)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | samdenty/gqless |
| Description | a GraphQL client without queries |
| Stars | 3654 |
| Forks | 52 |
| Licence | Not detected |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `27e289932cf45536c4e91190b96a4c9ce3d95063` |
| Retrieved at | 2026-11-14T19:15:11.120877+00:00 |
| Files in this snapshot | 391 |

## Directory tree

```text
.changeset/  (2 files)
  README.md
  config.json
.github/  (3 files)
  workflows/  (2 files)
    release.yaml
    tests.yaml
  FUNDING.yml
.husky/  (2 files)
  .gitignore
  pre-commit
.vscode/  (2 files)
  extensions.json
  settings.json
docs/  (99 files)
  cli/  (4 files)
    codegen.mdx
    config.mdx
    javascript.mdx
    programmatic.mdx
  client/  (44 files)
    api/  (37 files)
      … 37 files under this directory
    config.mdx
    fetching-data.mdx
    helper-functions.mdx
    mutations.mdx
    persistence.mdx
    subscriptions.mdx
    upload.mdx
  development/  (1 files)
    logger.mdx
  intro/  (3 files)
    features.mdx
    how-it-works.mdx
    new-in-2.mdx
  react/  (44 files)
    api/  (37 files)
      … 37 files under this directory
    config.mdx
    fetching-data.mdx
    meta.mdx
    mutations.mdx
    ssr.mdx
    subscriptions.mdx
    suspense.mdx
  contributing.mdx
  getting-started.mdx
  intro.mdx
examples/  (80 files)
  cra/  (23 files)
    public/  (3 files)
      … 3 files under this directory
    src/  (13 files)
      … 13 files under this directory
    .gitignore
    .prettierrc
    README.md
    gqless.config.js
    package.json
    sandbox.config.json
    tsconfig.json
  github/  (5 files)
    src/  (1 files)
      … 1 files under this directory
    test/  (1 files)
      … 1 files under this directory
    gqless.config.cjs
    jest.config.js
    package.json
  mercurius/  (17 files)
    src/  (5 files)
      … 5 files under this directory
    test/  (2 files)
      … 2 files under this directory
    .browserslistrc
    .gitignore
    LICENSE.md
    README.md
    generate.ts
    gqless.config.cjs
    jest.config.js
    listen.js
    package.json
    tsconfig.json
  react/  (35 files)
    api/  (2 files)
      … 2 files under this directory
    src/  (27 files)
      … 27 files under this directory
    gqless.config.cjs
    next-env.d.ts
    next.config.js
    open-browser.mjs
    package.json
    tsconfig.json
internal/  (60 files)
  build-utils/  (10 files)
    bin/  (3 files)
      … 3 files under this directory
    src/  (5 files)
      … 5 files under this directory
    package.json
    tsconfig.json
  test-utils/  (17 files)
    bin/  (1 files)
      … 1 files under this directory
    src/  (4 files)
      … 4 files under this directory
    test/  (3 files)
      … 3 files under this directory
    types/  (2 files)
      … 2 files under this directory
    .gitignore
    LICENSE.md
    README.md
    jest.config.js
    jest.config.ts
    package.json
    tsconfig.json
  website/  (33 files)
    sidebars/  (2 files)
      … 2 files under this directory
    src/  (16 files)
      … 16 files under this directory
    static/  (8 files)
      … 8 files under this directory
    .prettierrc
    docusaurus.config.js
    fix-typedoc-plugin.js
    fix-typedoc.js
    package.json
    sidebars.js
    tsconfig.json
packages/  (132 files)
  cli/  (24 files)
    bin/  (1 files)
      … 1 files under this directory
    src/  (8 files)
      … 8 files under this directory
    test/  (7 files)
      … 7 files under this directory
    .browserslistrc
    .gitignore
    CHANGELOG.md
    LICENSE.md
    README.md
    jest.config.js
    package.json
    tsconfig.json
  gqless/  (60 files)
    src/  (36 files)
      … 36 files under this directory
    test/  (17 files)
      … 17 files under this directory
    .browserslistrc
    CHANGELOG.md
    README.md
    jest.config.js
    nodemon.json
    package.json
    tsconfig.json
  logger/  (9 files)
    src/  (1 files)
      … 1 files under this directory
    test/  (1 files)
      … 1 files under this directory
    .browserslistrc
    CHANGELOG.md
    LICENSE.md
    README.md
    jest.config.js
    package.json
    tsconfig.json
  react/  (26 files)
    src/  (15 files)
      … 15 files under this directory
    test/  (3 files)
      … 3 files under this directory
    .browserslistrc
    .gitignore
    CHANGELOG.md
    LICENSE.md
    README.md
    jest.config.js
    package.json
    tsconfig.json
  subscriptions/  (13 files)
    src/  (4 files)
      … 4 files under this directory
    test/  (1 files)
      … 1 files under this directory
    .browserslistrc
    CHANGELOG.md
    LICENSE.md
    README.md
    jest.config.js
    package.json
    tsconfig.dev.json
    tsconfig.json
.gitignore
.prettierignore
.prettierrc
CONTRIBUTING.md
README.md
dev-react.mjs
dev.mjs
nodemon.json
package.json
pnpm-workspace.yaml
tsconfig.json
```

## Entry points

- [internal/build-utils/bin/build.js](https://github.com/samdenty/gqless/blob/27e289932cf45536c4e91190b96a4c9ce3d95063/internal/build-utils/bin/build.js)
- [internal/build-utils/bin/github-release.js](https://github.com/samdenty/gqless/blob/27e289932cf45536c4e91190b96a4c9ce3d95063/internal/build-utils/bin/github-release.js)
- [internal/build-utils/bin/watch.js](https://github.com/samdenty/gqless/blob/27e289932cf45536c4e91190b96a4c9ce3d95063/internal/build-utils/bin/watch.js)
- [internal/test-utils/bin/jest-test.js](https://github.com/samdenty/gqless/blob/27e289932cf45536c4e91190b96a4c9ce3d95063/internal/test-utils/bin/jest-test.js)
- [packages/cli/bin/gqless.js](https://github.com/samdenty/gqless/blob/27e289932cf45536c4e91190b96a4c9ce3d95063/packages/cli/bin/gqless.js)
- [internal/build-utils/src/index.js](https://github.com/samdenty/gqless/blob/27e289932cf45536c4e91190b96a4c9ce3d95063/internal/build-utils/src/index.js)
- [internal/test-utils/src/app.ts](https://github.com/samdenty/gqless/blob/27e289932cf45536c4e91190b96a4c9ce3d95063/internal/test-utils/src/app.ts)
- [internal/test-utils/src/index.ts](https://github.com/samdenty/gqless/blob/27e289932cf45536c4e91190b96a4c9ce3d95063/internal/test-utils/src/index.ts)
- [packages/cli/src/index.ts](https://github.com/samdenty/gqless/blob/27e289932cf45536c4e91190b96a4c9ce3d95063/packages/cli/src/index.ts)
- [packages/gqless/src/index.ts](https://github.com/samdenty/gqless/blob/27e289932cf45536c4e91190b96a4c9ce3d95063/packages/gqless/src/index.ts)
- [packages/logger/src/index.ts](https://github.com/samdenty/gqless/blob/27e289932cf45536c4e91190b96a4c9ce3d95063/packages/logger/src/index.ts)
- [packages/react/src/index.tsx](https://github.com/samdenty/gqless/blob/27e289932cf45536c4e91190b96a4c9ce3d95063/packages/react/src/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 23 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 3 file(s) under external integrations (observed from repository paths and static analysis). |
| internal package | library | Observed | Groups 38 file(s) under internal package (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 67 file(s) under packages package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 35 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/workflows/release.yaml` (ci)
- `.github/workflows/tests.yaml` (ci)
- `.vscode/extensions.json` (config)
- `.vscode/settings.json` (config)
- `examples/cra/package.json` (manifest)
- `examples/cra/public/manifest.json` (config)
- `examples/cra/sandbox.config.json` (config)
- `examples/cra/tsconfig.json` (config)
- `examples/github/package.json` (manifest)
- `examples/mercurius/package.json` (manifest)
- `examples/mercurius/tsconfig.json` (config)
- `examples/react/package.json` (manifest)
- `examples/react/tsconfig.json` (config)
- `internal/build-utils/package.json` (manifest)
- `internal/build-utils/tsconfig.json` (config)
- `internal/test-utils/package.json` (manifest)
- `internal/test-utils/tsconfig.json` (config)
- `internal/website/package.json` (manifest)
- `internal/website/static/icon/manifest.json` (config)
- `internal/website/tsconfig.json` (config)
- `nodemon.json` (config)
- `package.json` (manifest)
- `packages/cli/package.json` (manifest)
- `packages/cli/tsconfig.json` (config)
- `packages/gqless/nodemon.json` (config)
- `packages/gqless/package.json` (manifest)
- `packages/gqless/tsconfig.json` (config)
- `packages/logger/package.json` (manifest)
- `packages/logger/tsconfig.json` (config)
- `packages/react/package.json` (manifest)
- `packages/react/tsconfig.json` (config)
- `packages/subscriptions/package.json` (manifest)
- `packages/subscriptions/tsconfig.dev.json` (config)
- `packages/subscriptions/tsconfig.json` (config)
- `pnpm-workspace.yaml` (config)
- `tsconfig.json` (config)

## Top-level layout

- `packages` — 132 analysed file(s)
- `docs` — 99 analysed file(s)
- `examples` — 80 analysed file(s)
- `internal` — 60 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `.github` — 3 analysed file(s)
- `.changeset` — 2 analysed file(s)
- `.husky` — 2 analysed file(s)
- `.vscode` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `27e289932cf45536c4e91190b96a4c9ce3d95063` is the revision these paths and observations refer to.
