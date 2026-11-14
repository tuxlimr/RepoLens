# Project structure: apollographql/react-apollo

**Analysed commit:** `70e692dbf421b3c4c4ed106e3fcb54a5a27c2cc3`

**Commit reference:** [70e692dbf421b3c4c4ed106e3fcb54a5a27c2cc3](https://github.com/apollographql/react-apollo/commit/70e692dbf421b3c4c4ed106e3fcb54a5a27c2cc3)

**Tree at this commit:** [apollographql/react-apollo@70e692dbf421](https://github.com/apollographql/react-apollo/tree/70e692dbf421b3c4c4ed106e3fcb54a5a27c2cc3)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | apollographql/react-apollo |
| Description | :recycle: React integration for Apollo Client |
| Stars | 6789 |
| Forks | 756 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `70e692dbf421b3c4c4ed106e3fcb54a5a27c2cc3` |
| Retrieved at | 2026-11-14T19:14:01.181930+00:00 |
| Files in this snapshot | 39 |

## Directory tree

```text
.github/  (4 files)
  ISSUE_TEMPLATE/  (3 files)
    bug.md
    feature-request.md
    question-discussion.md
  PULL_REQUEST_TEMPLATE.md
.vscode/  (1 files)
  settings.json
packages/  (24 files)
  components/  (5 files)
    README.md
    index.d.ts
    index.esm.js
    index.js
    package.json
  hoc/  (5 files)
    README.md
    index.d.ts
    index.esm.js
    index.js
    package.json
  hooks/  (5 files)
    README.md
    index.d.ts
    index.esm.js
    index.js
    package.json
  ssr/  (5 files)
    README.md
    index.d.ts
    index.esm.js
    index.js
    package.json
  testing/  (4 files)
    README.md
    index.d.ts
    index.js
    package.json
.gitignore
.gitleaks.toml
COLLABORATORS.md
CONTRIBUTING.md
Changelog.md
LICENSE
README.md
lerna.json
package.json
tsconfig.json
```

## Entry points

- [packages/components/index.js](https://github.com/apollographql/react-apollo/blob/70e692dbf421b3c4c4ed106e3fcb54a5a27c2cc3/packages/components/index.js)
- [packages/hoc/index.js](https://github.com/apollographql/react-apollo/blob/70e692dbf421b3c4c4ed106e3fcb54a5a27c2cc3/packages/hoc/index.js)
- [packages/hooks/index.js](https://github.com/apollographql/react-apollo/blob/70e692dbf421b3c4c4ed106e3fcb54a5a27c2cc3/packages/hooks/index.js)
- [packages/ssr/index.js](https://github.com/apollographql/react-apollo/blob/70e692dbf421b3c4c4ed106e3fcb54a5a27c2cc3/packages/ssr/index.js)
- [packages/testing/index.js](https://github.com/apollographql/react-apollo/blob/70e692dbf421b3c4c4ed106e3fcb54a5a27c2cc3/packages/testing/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 8 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 14 file(s) under packages package (observed from repository paths and static analysis). |

## Important files

- `.gitleaks.toml` (config)
- `.vscode/settings.json` (config)
- `lerna.json` (config)
- `package.json` (manifest)
- `packages/components/package.json` (manifest)
- `packages/hoc/package.json` (manifest)
- `packages/hooks/package.json` (manifest)
- `packages/ssr/package.json` (manifest)
- `packages/testing/package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `packages` — 24 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `.github` — 4 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `70e692dbf421b3c4c4ed106e3fcb54a5a27c2cc3` is the revision these paths and observations refer to.
