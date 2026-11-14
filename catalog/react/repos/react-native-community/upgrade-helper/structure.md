# Project structure: react-native-community/upgrade-helper

**Analysed commit:** `f44a405d9834c797d527c87dbf05d5b7d636367b`

**Commit reference:** [f44a405d9834c797d527c87dbf05d5b7d636367b](https://github.com/react-native-community/upgrade-helper/commit/f44a405d9834c797d527c87dbf05d5b7d636367b)

**Tree at this commit:** [react-native-community/upgrade-helper@f44a405d9834](https://github.com/react-native-community/upgrade-helper/tree/f44a405d9834c797d527c87dbf05d5b7d636367b)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | react-native-community/upgrade-helper |
| Description | ⚛️ A web tool to support React Native developers in upgrading their apps. |
| Stars | 4074 |
| Forks | 129 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `f44a405d9834c797d527c87dbf05d5b7d636367b` |
| Retrieved at | 2026-11-14T19:14:54.982300+00:00 |
| Files in this snapshot | 100 |

## Directory tree

```text
.github/  (7 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    feature_request.md
    question.md
  workflows/  (2 files)
    deploy.yml
    push.yml
  CODEOWNERS
  PULL_REQUEST_TEMPLATE.md
@types/  (2 files)
  emotion.d.ts
  global.d.ts
__mocks__/  (1 files)
  react-github-btn.js
public/  (2 files)
  index.html
  manifest.json
src/  (68 files)
  __fixtures__/  (1 files)
    releases/  (1 files)
      … 1 files under this directory
  __tests__/  (4 files)
    components/  (2 files)
      … 2 files under this directory
    Home.e2e.spec.ts
    utils.spec.ts
  assets/  (2 files)
    loading.svg
    logo.svg
  components/  (28 files)
    common/  (27 files)
      … 27 files under this directory
    pages/  (1 files)
      … 1 files under this directory
  hooks/  (4 files)
    fetch-diff.ts
    fetch-release-versions.ts
    get-language-from-url.ts
    get-package-name-from-url.ts
  mocks/  (2 files)
    0.63.2..0.64.2.diff
    repositoryInfo.json
  releases/  (17 files)
    __mocks__/  (1 files)
      … 1 files under this directory
    react-native/  (14 files)
      … 14 files under this directory
    index.js
    types.d.ts
  theme/  (1 files)
    index.ts
  utils/  (3 files)
    device-sizes.ts
    test-utils.ts
    update-url.ts
  App.tsx
  constants.ts
  index.css
  index.jsx
  serviceWorker.ts
  utils.ts
.dockerignore
.eslintignore
.eslintrc.js
.gitignore
.node-version
.prettierrc
AGENTS.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
Dockerfile
LICENSE
README.md
config-overrides.js
docker-compose.yml
jest.config.js
jest.setup.js
mise.toml
package.json
renovate.json
tsconfig.json
```

## Entry points

- [src/App.tsx](https://github.com/react-native-community/upgrade-helper/blob/f44a405d9834c797d527c87dbf05d5b7d636367b/src/App.tsx)
- [src/components/common/index.ts](https://github.com/react-native-community/upgrade-helper/blob/f44a405d9834c797d527c87dbf05d5b7d636367b/src/components/common/index.ts)
- [src/index.jsx](https://github.com/react-native-community/upgrade-helper/blob/f44a405d9834c797d527c87dbf05d5b7d636367b/src/index.jsx)
- [src/releases/__mocks__/index.ts](https://github.com/react-native-community/upgrade-helper/blob/f44a405d9834c797d527c87dbf05d5b7d636367b/src/releases/__mocks__/index.ts)
- [src/releases/index.js](https://github.com/react-native-community/upgrade-helper/blob/f44a405d9834c797d527c87dbf05d5b7d636367b/src/releases/index.js)
- [src/theme/index.ts](https://github.com/react-native-community/upgrade-helper/blob/f44a405d9834c797d527c87dbf05d5b7d636367b/src/theme/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| App.tsx package | library | Observed | Groups 1 file(s) under app.tsx package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 28 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 8 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| constants.ts package | library | Observed | Groups 1 file(s) under constants.ts package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| __fixtures__ package | library | Observed | Groups 1 file(s) under __fixtures__ package (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 4 file(s) under hooks package (observed from repository paths and static analysis). |
| index.jsx package | library | Observed | Groups 1 file(s) under index.jsx package (observed from repository paths and static analysis). |
| __mocks__ package | library | Observed | Groups 1 file(s) under __mocks__ package (observed from repository paths and static analysis). |
| releases package | library | Observed | Groups 17 file(s) under releases package (observed from repository paths and static analysis). |
| serviceWorker.ts package | library | Observed | Groups 1 file(s) under serviceworker.ts package (observed from repository paths and static analysis). |
| __tests__ package | library | Observed | Groups 4 file(s) under __tests__ package (observed from repository paths and static analysis). |
| theme package | library | Observed | Groups 1 file(s) under theme package (observed from repository paths and static analysis). |
| @types package | library | Observed | Groups 2 file(s) under @types package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 3 file(s) under utils package (observed from repository paths and static analysis). |
| utils.ts package | library | Observed | Groups 1 file(s) under utils.ts package (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.github/workflows/deploy.yml` (ci)
- `.github/workflows/push.yml` (ci)
- `Dockerfile` (container)
- `docker-compose.yml` (container)
- `mise.toml` (config)
- `package.json` (manifest)
- `public/manifest.json` (config)
- `renovate.json` (config)
- `src/mocks/repositoryInfo.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `src` — 68 analysed file(s)
- `(root files)` — 20 analysed file(s)
- `.github` — 7 analysed file(s)
- `@types` — 2 analysed file(s)
- `public` — 2 analysed file(s)
- `__mocks__` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `f44a405d9834c797d527c87dbf05d5b7d636367b` is the revision these paths and observations refer to.
