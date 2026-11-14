# Project structure: pahen/madge

**Analysed commit:** `456057b85c2d063dad9c10147d7686ded4fc5ce5`

**Commit reference:** [456057b85c2d063dad9c10147d7686ded4fc5ce5](https://github.com/pahen/madge/commit/456057b85c2d063dad9c10147d7686ded4fc5ce5)

**Tree at this commit:** [pahen/madge@456057b85c2d](https://github.com/pahen/madge/tree/456057b85c2d063dad9c10147d7686ded4fc5ce5)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | pahen/madge |
| Description | Create graphs from your CommonJS, AMD or ES6 module dependencies |
| Stars | 10184 |
| Forks | 351 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `456057b85c2d063dad9c10147d7686ded4fc5ce5` |
| Retrieved at | 2026-11-14T19:12:43.609304+00:00 |
| Files in this snapshot | 130 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    nodejs.yml
bin/  (1 files)
  cli.js
lib/  (6 files)
  api.js
  cyclic.js
  graph.js
  log.js
  output.js
  tree.js
test/  (113 files)
  amd/  (29 files)
    circular/  (9 files)
      … 9 files under this directory
    circularAlias/  (3 files)
      … 3 files under this directory
    circularRelative/  (2 files)
      … 2 files under this directory
    nested/  (3 files)
      … 3 files under this directory
    ok/  (5 files)
      … 5 files under this directory
    requirejs/  (5 files)
      … 5 files under this directory
    amdes6.js
    plugin.js
  cjs/  (24 files)
    circular/  (6 files)
      … 6 files under this directory
    multibase/  (2 files)
      … 2 files under this directory
    normal/  (4 files)
      … 4 files under this directory
    a.js
    b.js
    both.js
    c.js
    chained.js
    core.js
    error.js
    missing.js
    nested.js
    npm.js
    strings.js
    word.js
  es6/  (16 files)
    absolute/  (2 files)
      … 2 files under this directory
    circular/  (3 files)
      … 3 files under this directory
    re-export/  (5 files)
      … 5 files under this directory
    webpack/  (4 files)
      … 4 files under this directory
    absolute.js
    error.js
  es7/  (2 files)
    async.js
    other.js
  flow/  (5 files)
    cjs/  (3 files)
      … 3 files under this directory
    es/  (2 files)
      … 2 files under this directory
  git/  (4 files)
    .git_tmp/  (1 files)
      … 1 files under this directory
    a.js
    b.js
    c.js
  jsx/  (2 files)
    basic.jsx
    other.jsx
  typescript/  (13 files)
    custom-paths/  (4 files)
      … 4 files under this directory
    with-config/  (3 files)
      … 3 files under this directory
    export-x.tsx
    export.ts
    import.ts
    mixed.ts
    require-x.tsx
    require.ts
  vue/  (8 files)
    BasicComponent.vue
    BasicComponentTs.vue
    OneNested.vue
    OneNestedTs.vue
    ThreeNested.vue
    TwoNested.vue
    one.ts
    two.js
  amd.js
  api.js
  cjs.js
  es6.js
  es7.js
  flow.js
  jsx.js
  output.sh
  typescript.js
  vue.js
.editorconfig
.eslintrc
.gitignore
.nvmrc
.release-it.json
CHANGELOG.md
LICENSE
README.md
package.json
```

## Entry points

- [bin/cli.js](https://github.com/pahen/madge/blob/456057b85c2d063dad9c10147d7686ded4fc5ce5/bin/cli.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bin package | library | Observed | Groups 1 file(s) under bin package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 6 file(s) under lib package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 113 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/workflows/nodejs.yml` (ci)
- `.release-it.json` (config)
- `package.json` (manifest)

## Top-level layout

- `test` — 113 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `lib` — 6 analysed file(s)
- `.github` — 1 analysed file(s)
- `bin` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 11 file(s) were skipped during inventory (11 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `456057b85c2d063dad9c10147d7686ded4fc5ce5` is the revision these paths and observations refer to.
