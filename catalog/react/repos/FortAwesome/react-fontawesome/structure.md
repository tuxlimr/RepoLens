# Project structure: FortAwesome/react-fontawesome

**Analysed commit:** `3017221bae25d8a9bf08f15129e888e42f814e8e`

**Commit reference:** [3017221bae25d8a9bf08f15129e888e42f814e8e](https://github.com/FortAwesome/react-fontawesome/commit/3017221bae25d8a9bf08f15129e888e42f814e8e)

**Tree at this commit:** [FortAwesome/react-fontawesome@3017221bae25](https://github.com/FortAwesome/react-fontawesome/tree/3017221bae25d8a9bf08f15129e888e42f814e8e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | FortAwesome/react-fontawesome |
| Description | Official React Component for Font Awesome Icons |
| Stars | 3742 |
| Forks | 269 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `3017221bae25d8a9bf08f15129e888e42f814e8e` |
| Retrieved at | 2026-11-14T19:15:05.956004+00:00 |
| Files in this snapshot | 62 |

## Directory tree

```text
.github/  (5 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (3 files)
    ci.yml
    docs.yml
    publish.yml
.husky/  (2 files)
  commit-msg
  pre-commit
.vscode/  (2 files)
  extensions.json
  settings.json
docs/  (1 files)
  src/  (1 files)
    API-Reference-Readme.md
scripts/  (1 files)
  publish.sh
src/  (30 files)
  __tests__/  (1 files)
    converter.test.ts
  components/  (7 files)
    __fixtures__/  (1 files)
      … 1 files under this directory
    __tests__/  (2 files)
      … 2 files under this directory
    rsc/  (2 files)
      … 2 files under this directory
    FontAwesomeIcon.tsx
    FontAwesomeLayers.tsx
  hooks/  (2 files)
    __tests__/  (1 files)
      … 1 files under this directory
    useAccessibilityId.ts
  types/  (5 files)
    animation-props.ts
    css-variables.ts
    gradients.ts
    icon-props.ts
    transform-props.ts
  utils/  (11 files)
    __tests__/  (5 files)
      … 5 files under this directory
    camelize.ts
    constants.ts
    get-class-list-from-props.ts
    gradients.ts
    normalize-icon-args.ts
    typed-object-keys.ts
  converter.ts
  global.d.ts
  index.ts
  logger.ts
test-setup/  (1 files)
  jest.setup.ts
.editorconfig
.gitignore
.prettierignore
.prettierrc.json
.tool-versions
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
DEVELOPMENT.md
LICENSE.txt
README.md
babel.config.js
commitlint.config.ts
eslint.config.mjs
jest.config.ts
package.json
release.config.mjs
tsconfig.json
tsup.config.ts
typedoc.config.mjs
```

## Entry points

- [src/index.ts](https://github.com/FortAwesome/react-fontawesome/blob/3017221bae25d8a9bf08f15129e888e42f814e8e/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| components package | library | Observed | Groups 7 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| converter.ts package | library | Observed | Groups 1 file(s) under converter.ts package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 7 file(s) under core modules (observed from repository paths and static analysis). |
| global.d.ts package | library | Observed | Groups 1 file(s) under global.d.ts package (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 2 file(s) under hooks package (observed from repository paths and static analysis). |
| index.ts package | library | Observed | Groups 1 file(s) under index.ts package (observed from repository paths and static analysis). |
| logger.ts package | library | Observed | Groups 1 file(s) under logger.ts package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| test-setup package | library | Observed | Groups 1 file(s) under test-setup package (observed from repository paths and static analysis). |
| __tests__ package | library | Observed | Groups 1 file(s) under __tests__ package (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 5 file(s) under types package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 11 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/docs.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.prettierrc.json` (config)
- `.vscode/extensions.json` (config)
- `.vscode/settings.json` (config)
- `package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `src` — 30 analysed file(s)
- `(root files)` — 20 analysed file(s)
- `.github` — 5 analysed file(s)
- `.husky` — 2 analysed file(s)
- `.vscode` — 2 analysed file(s)
- `docs` — 1 analysed file(s)
- `scripts` — 1 analysed file(s)
- `test-setup` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `3017221bae25d8a9bf08f15129e888e42f814e8e` is the revision these paths and observations refer to.
