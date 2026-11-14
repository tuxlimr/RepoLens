# Project structure: meta/jscodeshift

**Analysed commit:** `938bc3c355dd77fd3cc8063c8615ee0f9caeed89`

**Commit reference:** [938bc3c355dd77fd3cc8063c8615ee0f9caeed89](https://github.com/meta/jscodeshift/commit/938bc3c355dd77fd3cc8063c8615ee0f9caeed89)

**Tree at this commit:** [meta/jscodeshift@938bc3c355dd](https://github.com/meta/jscodeshift/tree/938bc3c355dd77fd3cc8063c8615ee0f9caeed89)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | meta/jscodeshift |
| Description | A JavaScript codemod toolkit. |
| Stars | 10048 |
| Forks | 500 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `938bc3c355dd77fd3cc8063c8615ee0f9caeed89` |
| Retrieved at | 2026-11-14T19:12:46.500279+00:00 |
| Files in this snapshot | 102 |

## Directory tree

```text
.changeset/  (3 files)
  README.md
  config.json
  export-declaration-insert.md
.github/  (4 files)
  workflows/  (4 files)
    cr.yml
    pull_request.yml
    push.yml
    test.yml
bin/  (3 files)
  __tests__/  (1 files)
    jscodeshift-test.js
  jscodeshift.js
  jscodeshift.sh
parser/  (9 files)
  __tests__/  (3 files)
    __snapshots__/  (1 files)
      … 1 files under this directory
    .eslintrc
    tsx-test.js
  babel5Compat.js
  babylon.js
  flow.js
  ts.js
  tsOptions.js
  tsx.js
recipes/  (1 files)
  retain-first-comment.md
sample/  (7 files)
  __testfixtures__/  (4 files)
    typescript/  (2 files)
      … 2 files under this directory
    reverse-identifiers.input.js
    reverse-identifiers.output.js
  __tests__/  (2 files)
    __snapshots__/  (1 files)
      … 1 files under this directory
    reverse-identifiers-test.js
  reverse-identifiers.js
src/  (47 files)
  __testfixtures__/  (9 files)
    test-async-transform.input.js
    test-async-transform.js
    test-async-transform.output.js
    test-sync-transform.input.js
    test-sync-transform.js
    test-sync-transform.output.js
    test-tsx-transform.input.tsx
    test-tsx-transform.js
    test-tsx-transform.output.tsx
  __tests__/  (11 files)
    __snapshots__/  (1 files)
      … 1 files under this directory
    .eslintrc
    Collection-test.js
    Worker-test.js
    argsParser-test.js
    core-test.js
    ignoreFiles-test.js
    matchNode-test.js
    template-test.js
    testUtils-test.js
    ts-decorator-auto-accessor-test.js
  collections/  (11 files)
    __tests__/  (6 files)
      … 6 files under this directory
    ImportDeclaration.js
    JSXElement.js
    Node.js
    VariableDeclarator.js
    index.js
  utils/  (6 files)
    __tests__/  (3 files)
      … 3 files under this directory
    intersection.js
    once.js
    union.js
  Collection.js
  Runner.js
  Worker.js
  argsParser.js
  core.js
  getParser.js
  ignoreFiles.js
  matchNode.js
  template.js
  testUtils.js
utils/  (2 files)
  requirePackage.js
  testUtils.js
website/  (12 files)
  .astro/  (2 files)
    settings.json
    types.d.ts
  public/  (1 files)
    favicon.svg
  src/  (5 files)
    content/  (4 files)
      … 4 files under this directory
    env.d.ts
  README.md
  astro.config.mjs
  package.json
  tsconfig.json
.editorconfig
.eslintignore
.eslintrc
.gitattributes
.gitignore
.node-version
.npmignore
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
index.js
package.json
```

## Entry points

- [index.js](https://github.com/meta/jscodeshift/blob/938bc3c355dd77fd3cc8063c8615ee0f9caeed89/index.js)
- [bin/jscodeshift.js](https://github.com/meta/jscodeshift/blob/938bc3c355dd77fd3cc8063c8615ee0f9caeed89/bin/jscodeshift.js)
- [src/collections/index.js](https://github.com/meta/jscodeshift/blob/938bc3c355dd77fd3cc8063c8615ee0f9caeed89/src/collections/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| argsParser.js package | library | Observed | Groups 1 file(s) under argsparser.js package (observed from repository paths and static analysis). |
| bin package | library | Observed | Groups 3 file(s) under bin package (observed from repository paths and static analysis). |
| Collection.js package | library | Observed | Groups 1 file(s) under collection.js package (observed from repository paths and static analysis). |
| collections package | library | Observed | Groups 9 file(s) under collections package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| core.js package | library | Observed | Groups 1 file(s) under core.js package (observed from repository paths and static analysis). |
| getParser.js package | library | Observed | Groups 1 file(s) under getparser.js package (observed from repository paths and static analysis). |
| ignoreFiles.js package | library | Observed | Groups 1 file(s) under ignorefiles.js package (observed from repository paths and static analysis). |
| matchNode.js package | library | Observed | Groups 1 file(s) under matchnode.js package (observed from repository paths and static analysis). |
| parser package | library | Observed | Groups 7 file(s) under parser package (observed from repository paths and static analysis). |
| Runner.js package | library | Observed | Groups 1 file(s) under runner.js package (observed from repository paths and static analysis). |
| sample package | library | Observed | Groups 6 file(s) under sample package (observed from repository paths and static analysis). |
| template.js package | library | Observed | Groups 1 file(s) under template.js package (observed from repository paths and static analysis). |
| __testfixtures__ package | library | Observed | Groups 9 file(s) under __testfixtures__ package (observed from repository paths and static analysis). |
| __tests__ package | library | Observed | Groups 9 file(s) under __tests__ package (observed from repository paths and static analysis). |
| testUtils.js package | library | Observed | Groups 1 file(s) under testutils.js package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 8 file(s) under utils package (observed from repository paths and static analysis). |
| website package | library | Observed | Groups 4 file(s) under website package (observed from repository paths and static analysis). |
| Worker.js package | library | Observed | Groups 1 file(s) under worker.js package (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.editorconfig` (config)
- `.github/workflows/cr.yml` (ci)
- `.github/workflows/pull_request.yml` (ci)
- `.github/workflows/push.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `package.json` (manifest)
- `website/.astro/settings.json` (config)
- `website/package.json` (manifest)
- `website/tsconfig.json` (config)

## Top-level layout

- `src` — 47 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `website` — 12 analysed file(s)
- `parser` — 9 analysed file(s)
- `sample` — 7 analysed file(s)
- `.github` — 4 analysed file(s)
- `.changeset` — 3 analysed file(s)
- `bin` — 3 analysed file(s)
- `utils` — 2 analysed file(s)
- `recipes` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 4 file(s) were skipped during inventory (2 x lockfile excluded; 2 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `938bc3c355dd77fd3cc8063c8615ee0f9caeed89` is the revision these paths and observations refer to.
