# Project structure: microsoft/code-push

**Analysed commit:** `d3b163d8d7522f02081eee2b5d735705b5d54c00`

**Commit reference:** [d3b163d8d7522f02081eee2b5d735705b5d54c00](https://github.com/microsoft/code-push/commit/d3b163d8d7522f02081eee2b5d735705b5d54c00)

**Tree at this commit:** [microsoft/code-push@d3b163d8d752](https://github.com/microsoft/code-push/tree/d3b163d8d7522f02081eee2b5d735705b5d54c00)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | microsoft/code-push |
| Description | A cloud service that enables Cordova and React Native developers to deploy mobile app updates directly to their users’ devices. |
| Stars | 4410 |
| Forks | 527 |
| Licence | Other |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `d3b163d8d7522f02081eee2b5d735705b5d54c00` |
| Retrieved at | 2026-11-14T19:14:46.708369+00:00 |
| Files in this snapshot | 33 |

## Directory tree

```text
.azurepipelines/  (1 files)
  build-code-push-1es.yml
.github/  (5 files)
  policies/  (1 files)
    resourceManagement.yml
  scripts/  (1 files)
    check-for-declaration.ts
  workflows/  (1 files)
    code-push-ci.yml
  CODEOWNERS
  ISSUE_TEMPLATE.md
.vscode/  (3 files)
  launch.json
  settings.json
  tasks.json
src/  (13 files)
  @types/  (1 files)
    recursive-fs.d.ts
  script/  (5 files)
    acquisition-sdk.ts
    code-push-error.ts
    index.ts
    management-sdk.ts
    types.ts
  test/  (4 files)
    acquisition-rest-mock.ts
    acquisition-sdk.ts
    management-sdk.ts
    superagent-mock-config.js
  utils/  (3 files)
    adapter/  (2 files)
      … 2 files under this directory
    request-manager.ts
.gitignore
.npmignore
LICENSE.md
README.md
SDK.njsproj
SECURITY.md
migration-notice.md
mocha.opts
package.json
tsconfig-release.json
tsconfig.json
```

## Entry points

- [src/script/index.ts](https://github.com/microsoft/code-push/blob/d3b163d8d7522f02081eee2b5d735705b5d54c00/src/script/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| script package | library | Observed | Groups 5 file(s) under script package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 4 file(s) under tests (observed from repository paths and static analysis). |
| @types package | library | Observed | Groups 1 file(s) under @types package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 3 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.azurepipelines/build-code-push-1es.yml` (config)
- `.github/policies/resourceManagement.yml` (config)
- `.github/workflows/code-push-ci.yml` (ci)
- `.vscode/launch.json` (config)
- `.vscode/settings.json` (config)
- `.vscode/tasks.json` (config)
- `package.json` (manifest)
- `tsconfig-release.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `src` — 13 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `.github` — 5 analysed file(s)
- `.vscode` — 3 analysed file(s)
- `.azurepipelines` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `d3b163d8d7522f02081eee2b5d735705b5d54c00` is the revision these paths and observations refer to.
