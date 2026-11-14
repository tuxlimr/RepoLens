# Project structure: expo/create-react-native-app

**Analysed commit:** `3a7b11ee859c5c38fe09be58419e97a286a22c13`

**Commit reference:** [3a7b11ee859c5c38fe09be58419e97a286a22c13](https://github.com/expo/create-react-native-app/commit/3a7b11ee859c5c38fe09be58419e97a286a22c13)

**Tree at this commit:** [expo/create-react-native-app@3a7b11ee859c](https://github.com/expo/create-react-native-app/tree/3a7b11ee859c5c38fe09be58419e97a286a22c13)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | expo/create-react-native-app |
| Description | Create React Native apps that run on iOS, Android, and web |
| Stars | 13243 |
| Forks | 1335 |
| Licence | BSD-3-Clause |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `3a7b11ee859c5c38fe09be58419e97a286a22c13` |
| Retrieved at | 2026-11-14T19:11:58.945981+00:00 |
| Files in this snapshot | 21 |

## Directory tree

```text
.gh-assets/  (1 files)
  banner.svg
.github/  (4 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    config.yml
  workflows/  (2 files)
    size.yml
    test.yml
src/  (2 files)
  __tests__/  (1 files)
    index.test.js
  index.ts
template/  (1 files)
  gitignore
.all-contributorsrc
.eslintignore
.eslintrc.js
.gitignore
.prettierignore
.prettierrc
CHANGELOG.md
CONTRIBUTING.md
LICENSE
README.md
jest.config.js
package.json
tsconfig.json
```

## Entry points

- [src/index.ts](https://github.com/expo/create-react-native-app/blob/3a7b11ee859c5c38fe09be58419e97a286a22c13/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| index.ts package | library | Observed | Groups 1 file(s) under index.ts package (observed from repository paths and static analysis). |
| __tests__ package | library | Observed | Groups 1 file(s) under __tests__ package (observed from repository paths and static analysis). |

## Important files

- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/size.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `(root files)` — 13 analysed file(s)
- `.github` — 4 analysed file(s)
- `src` — 2 analysed file(s)
- `.gh-assets` — 1 analysed file(s)
- `template` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `3a7b11ee859c5c38fe09be58419e97a286a22c13` is the revision these paths and observations refer to.
