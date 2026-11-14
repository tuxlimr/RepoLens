# Project structure: ianstormtaylor/slate

**Analysed commit:** `0c2c0b02b7726a7a59ac344b5f7a68608cc2ec44`

**Commit reference:** [0c2c0b02b7726a7a59ac344b5f7a68608cc2ec44](https://github.com/ianstormtaylor/slate/commit/0c2c0b02b7726a7a59ac344b5f7a68608cc2ec44)

**Tree at this commit:** [ianstormtaylor/slate@0c2c0b02b772](https://github.com/ianstormtaylor/slate/tree/0c2c0b02b7726a7a59ac344b5f7a68608cc2ec44)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | ianstormtaylor/slate |
| Description | A completely customizable framework for building rich text editors. (Currently in beta.) |
| Stars | 31745 |
| Forks | 3305 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `0c2c0b02b7726a7a59ac344b5f7a68608cc2ec44` |
| Retrieved at | 2026-11-14T19:13:02.825324+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.changeset/  (2 files)
  README.md
  config.json
.github/  (10 files)
  ISSUE_TEMPLATE/  (5 files)
    bug-core.md
    bug-platform.md
    config.yml
    request-feature.md
    request-improvement.md
  workflows/  (4 files)
    ci.yml
    codeql.yml
    comment.yml
    release.yml
  PULL_REQUEST_TEMPLATE.md
.vscode/  (3 files)
  extensions.json
  launch.json
  settings.json
.yarn/  (15 files)
  sdks/  (15 files)
    eslint/  (4 files)
      … 4 files under this directory
    prettier/  (3 files)
      … 3 files under this directory
    typescript/  (7 files)
      … 7 files under this directory
    integrations.yml
config/  (5 files)
  babel/  (1 files)
    register.cjs
  docs/  (1 files)
    check-typescript.cjs
  rollup/  (1 files)
    rollup.config.js
  typescript/  (2 files)
    tsconfig.json
    tsconfig.test.json
docs/  (62 files)
  api/  (20 files)
    locations/  (10 files)
      … 10 files under this directory
    nodes/  (6 files)
      … 6 files under this directory
    operations/  (2 files)
      … 2 files under this directory
    scrubber.md
    transforms.md
  concepts/  (13 files)
    01-interfaces.md
    02-nodes.md
    03-locations.md
    04-transforms.md
    05-operations.md
    06-commands.md
    07-editor.md
    08-plugins.md
    09-rendering.md
    10-serializing.md
    11-normalizing.md
    12-typescript.md
    xx-migrating.md
  general/  (4 files)
    changelog.md
    contributing.md
    faq.md
    resources.md
  libraries/  (12 files)
    slate-history/  (4 files)
      … 4 files under this directory
    slate-react/  (7 files)
      … 7 files under this directory
    slate-hyperscript.md
  walkthroughs/  (11 files)
    01-installing-slate.md
    02-adding-event-handlers.md
    03-defining-custom-elements.md
    04-applying-custom-formatting.md
    05-executing-commands.md
    06-saving-to-a-database.md
    07-enabling-collaborative-editing.md
    08-using-the-bundled-source.md
    09-performance.md
    10-collaboration-with-yjs.md
    11-accessibility.md
  Introduction.md
  Summary.md
packages/  (687 files)
  slate/  (485 files)
    src/  (125 files)
      … 125 files under this directory
    test/  (357 files)
      … 357 files under this directory
    CHANGELOG.md
    Readme.md
    package.json
  slate-dom/  (18 files)
    src/  (15 files)
      … 15 files under this directory
    CHANGELOG.md
    package.json
    tsconfig.json
  slate-history/  (34 files)
    src/  (5 files)
      … 5 files under this directory
    test/  (25 files)
      … 25 files under this directory
    CHANGELOG.md
    Readme.md
    package.json
    tsconfig.json
  slate-hyperscript/  (47 files)
    src/  (5 files)
      … 5 files under this directory
    test/  (38 files)
      … 38 files under this directory
    CHANGELOG.md
    Readme.md
    package.json
    tsconfig.json
  slate-react/  (103 files)
    src/  (47 files)
      … 47 files under this directory
    test/  (52 files)
      … 52 files under this directory
    CHANGELOG.md
    Readme.md
    package.json
    tsconfig.json
.editorconfig
.gitattributes
.gitbook.yaml
.gitignore
.markdownlint.json
.nvmrc
.prettierignore
.prettierrc
.yarnrc.yml
License.md
Readme.md
babel.config.js
eslint.config.mjs
jest.config.js
now.json
package.json
```

## Entry points

- [.yarn/sdks/eslint/lib/api.js](https://github.com/ianstormtaylor/slate/blob/0c2c0b02b7726a7a59ac344b5f7a68608cc2ec44/.yarn/sdks/eslint/lib/api.js)
- [.yarn/sdks/eslint/bin/eslint.js](https://github.com/ianstormtaylor/slate/blob/0c2c0b02b7726a7a59ac344b5f7a68608cc2ec44/.yarn/sdks/eslint/bin/eslint.js)
- [.yarn/sdks/prettier/index.cjs](https://github.com/ianstormtaylor/slate/blob/0c2c0b02b7726a7a59ac344b5f7a68608cc2ec44/.yarn/sdks/prettier/index.cjs)
- [.yarn/sdks/prettier/bin/prettier.cjs](https://github.com/ianstormtaylor/slate/blob/0c2c0b02b7726a7a59ac344b5f7a68608cc2ec44/.yarn/sdks/prettier/bin/prettier.cjs)
- [.yarn/sdks/typescript/lib/typescript.js](https://github.com/ianstormtaylor/slate/blob/0c2c0b02b7726a7a59ac344b5f7a68608cc2ec44/.yarn/sdks/typescript/lib/typescript.js)
- [.yarn/sdks/typescript/bin/tsc](https://github.com/ianstormtaylor/slate/blob/0c2c0b02b7726a7a59ac344b5f7a68608cc2ec44/.yarn/sdks/typescript/bin/tsc)
- [.yarn/sdks/typescript/bin/tsserver](https://github.com/ianstormtaylor/slate/blob/0c2c0b02b7726a7a59ac344b5f7a68608cc2ec44/.yarn/sdks/typescript/bin/tsserver)
- [packages/slate-dom/src/index.ts](https://github.com/ianstormtaylor/slate/blob/0c2c0b02b7726a7a59ac344b5f7a68608cc2ec44/packages/slate-dom/src/index.ts)
- [packages/slate-history/src/index.ts](https://github.com/ianstormtaylor/slate/blob/0c2c0b02b7726a7a59ac344b5f7a68608cc2ec44/packages/slate-history/src/index.ts)
- [packages/slate-hyperscript/src/index.ts](https://github.com/ianstormtaylor/slate/blob/0c2c0b02b7726a7a59ac344b5f7a68608cc2ec44/packages/slate-hyperscript/src/index.ts)
- [packages/slate-react/src/index.ts](https://github.com/ianstormtaylor/slate/blob/0c2c0b02b7726a7a59ac344b5f7a68608cc2ec44/packages/slate-react/src/index.ts)
- [packages/slate/src/index.ts](https://github.com/ianstormtaylor/slate/blob/0c2c0b02b7726a7a59ac344b5f7a68608cc2ec44/packages/slate/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 15 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 188 file(s) under packages package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 9 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 472 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.editorconfig` (config)
- `.gitbook.yaml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/codeql.yml` (ci)
- `.github/workflows/comment.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.markdownlint.json` (config)
- `.vscode/extensions.json` (config)
- `.vscode/launch.json` (config)
- `.vscode/settings.json` (config)
- `.yarn/sdks/eslint/package.json` (manifest)
- `.yarn/sdks/integrations.yml` (config)
- `.yarn/sdks/prettier/package.json` (manifest)
- `.yarn/sdks/typescript/package.json` (manifest)
- `.yarnrc.yml` (config)
- `config/typescript/tsconfig.json` (config)
- `config/typescript/tsconfig.test.json` (config)
- `now.json` (config)
- `package.json` (manifest)
- `packages/slate-dom/package.json` (manifest)
- `packages/slate-dom/tsconfig.json` (config)
- `packages/slate-history/package.json` (manifest)
- `packages/slate-history/tsconfig.json` (config)
- `packages/slate-hyperscript/package.json` (manifest)
- `packages/slate-hyperscript/tsconfig.json` (config)
- `packages/slate-react/package.json` (manifest)
- `packages/slate-react/tsconfig.json` (config)
- `packages/slate/package.json` (manifest)

## Top-level layout

- `packages` — 687 analysed file(s)
- `docs` — 62 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `.yarn` — 15 analysed file(s)
- `.github` — 10 analysed file(s)
- `config` — 5 analysed file(s)
- `.vscode` — 3 analysed file(s)
- `.changeset` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `0c2c0b02b7726a7a59ac344b5f7a68608cc2ec44` is the revision these paths and observations refer to.
