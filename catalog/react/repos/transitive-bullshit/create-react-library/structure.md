# Project structure: transitive-bullshit/create-react-library

**Analysed commit:** `43c4f5bcf97203b8e095558ab0d33b1e45f04182`

**Commit reference:** [43c4f5bcf97203b8e095558ab0d33b1e45f04182](https://github.com/transitive-bullshit/create-react-library/commit/43c4f5bcf97203b8e095558ab0d33b1e45f04182)

**Tree at this commit:** [transitive-bullshit/create-react-library@43c4f5bcf972](https://github.com/transitive-bullshit/create-react-library/tree/43c4f5bcf97203b8e095558ab0d33b1e45f04182)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | transitive-bullshit/create-react-library |
| Description | CLI for creating reusable react libraries. |
| Stars | 4746 |
| Forks | 287 |
| Licence | Not detected |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `43c4f5bcf97203b8e095558ab0d33b1e45f04182` |
| Retrieved at | 2026-11-14T19:14:37.048428+00:00 |
| Files in this snapshot | 85 |

## Directory tree

```text
lib/  (7 files)
  cli.js
  config.js
  create-library.js
  create-library.test.js
  get-default-library-params.js
  prompt-library-params.js
  prompt-library-params.test.js
media/  (2 files)
  demo.svg
  tree.svg
template/  (66 files)
  default/  (20 files)
    example/  (8 files)
      … 8 files under this directory
    src/  (4 files)
      … 4 files under this directory
    .editorconfig
    .eslintignore
    .eslintrc
    .gitignore
    .prettierrc
    .travis.yml
    README.md
    package.json
  flow/  (20 files)
    example/  (8 files)
      … 8 files under this directory
    src/  (4 files)
      … 4 files under this directory
    .editorconfig
    .eslintignore
    .eslintrc
    .gitignore
    .prettierrc
    .travis.yml
    README.md
    package.json
  typescript/  (26 files)
    example/  (11 files)
      … 11 files under this directory
    src/  (5 files)
      … 5 files under this directory
    .editorconfig
    .eslintignore
    .eslintrc
    .gitignore
    .prettierrc
    .travis.yml
    README.md
    package.json
    tsconfig.json
    tsconfig.test.json
.editorconfig
.eslintrc
.gitignore
.npmignore
.travis.yml
index.js
index.test.js
package.json
readme.md
readme.zh-CN.md
```

## Entry points

- [index.js](https://github.com/transitive-bullshit/create-react-library/blob/43c4f5bcf97203b8e095558ab0d33b1e45f04182/index.js)
- [template/default/src/index.js](https://github.com/transitive-bullshit/create-react-library/blob/43c4f5bcf97203b8e095558ab0d33b1e45f04182/template/default/src/index.js)
- [template/flow/src/index.js](https://github.com/transitive-bullshit/create-react-library/blob/43c4f5bcf97203b8e095558ab0d33b1e45f04182/template/flow/src/index.js)
- [template/typescript/src/index.tsx](https://github.com/transitive-bullshit/create-react-library/blob/43c4f5bcf97203b8e095558ab0d33b1e45f04182/template/typescript/src/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 19 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 7 file(s) under lib package (observed from repository paths and static analysis). |
| template package | library | Observed | Groups 18 file(s) under template package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.travis.yml` (ci)
- `package.json` (manifest)
- `template/default/.editorconfig` (config)
- `template/default/.travis.yml` (ci)
- `template/default/example/package.json` (manifest)
- `template/default/example/public/manifest.json` (config)
- `template/default/package.json` (manifest)
- `template/flow/.editorconfig` (config)
- `template/flow/.travis.yml` (ci)
- `template/flow/example/package.json` (manifest)
- `template/flow/example/public/manifest.json` (config)
- `template/flow/package.json` (manifest)
- `template/typescript/.editorconfig` (config)
- `template/typescript/.travis.yml` (ci)
- `template/typescript/example/package.json` (manifest)
- `template/typescript/example/public/manifest.json` (config)
- `template/typescript/example/tsconfig.json` (config)
- `template/typescript/package.json` (manifest)
- `template/typescript/tsconfig.json` (config)
- `template/typescript/tsconfig.test.json` (config)

## Top-level layout

- `template` — 66 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `lib` — 7 analysed file(s)
- `media` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `43c4f5bcf97203b8e095558ab0d33b1e45f04182` is the revision these paths and observations refer to.
