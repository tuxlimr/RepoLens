# Project structure: obytes/react-native-template-obytes

**Analysed commit:** `fd9b358ed11913d2a49fd9ffa6582fe03ba130e7`

**Commit reference:** [fd9b358ed11913d2a49fd9ffa6582fe03ba130e7](https://github.com/obytes/react-native-template-obytes/commit/fd9b358ed11913d2a49fd9ffa6582fe03ba130e7)

**Tree at this commit:** [obytes/react-native-template-obytes@fd9b358ed119](https://github.com/obytes/react-native-template-obytes/tree/fd9b358ed11913d2a49fd9ffa6582fe03ba130e7)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | obytes/react-native-template-obytes |
| Description | 📱 A template for your next React Native project: Expo, PNPM, TypeScript, TailwindCSS, Husky, EAS, GitHub Actions, Env Vars, expo-router, react-query, react-hook-form. |
| Stars | 4370 |
| Forks | 679 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `fd9b358ed11913d2a49fd9ffa6582fe03ba130e7` |
| Retrieved at | 2026-11-14T19:14:48.239697+00:00 |
| Files in this snapshot | 202 |

## Directory tree

```text
.github/  (19 files)
  actions/  (3 files)
    eas-build/  (1 files)
      … 1 files under this directory
    setup-jdk-generate-apk/  (1 files)
      … 1 files under this directory
    setup-node-pnpm-install/  (1 files)
      … 1 files under this directory
  scripts/  (1 files)
    expo-doctor.sh
  workflows/  (13 files)
    compress-images.yml
    e2e-android-eas-build.yml
    e2e-android-maestro.yml
    e2e-android.yml
    eas-build-preview.yml
    eas-build-prod.yml
    expo-doctor.yml
    lint-ts.yml
    new-app-version.yml
    new-github-release.yml
    stale.yml
    test.yml
    type-check.yml
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
.husky/  (5 files)
  .gitignore
  commit-msg
  common.sh
  post-merge
  pre-commit
.maestro/  (11 files)
  app/  (2 files)
    create-post.yaml
    tabs.yaml
  auth/  (2 files)
    login-with-validation.yaml
    onboarding.yaml
  utils/  (6 files)
    hide-keyboard-android.yaml
    hide-keyboard-ios.yaml
    hide-keyboard.yaml
    login.yaml
    onboarding-and-login.yaml
    onboarding.yaml
  config.yaml
.vscode/  (3 files)
  extensions.json
  project.code-snippets
  settings.json
__mocks__/  (5 files)
  @gorhom/  (1 files)
    bottom-sheet.ts
  expo-localization.ts
  moti.ts
  react-native-gesture-handler.ts
  react-native-keyboard-controller.ts
cli/  (6 files)
  README.md
  clone-repo.js
  index.js
  package.json
  setup-project.js
  utils.js
docs/  (47 files)
  public/  (2 files)
    _redirects
    favicon.svg
  src/  (40 files)
    assets/  (1 files)
      … 1 files under this directory
    components/  (6 files)
      … 6 files under this directory
    content/  (30 files)
      … 30 files under this directory
    styles/  (1 files)
      … 1 files under this directory
    content.config.ts
    env.d.ts
  .gitignore
  README.md
  astro.config.mjs
  package.json
  tsconfig.json
scripts/  (2 files)
  genrate-apk-and-install
  i18next-syntax-validation.js
src/  (85 files)
  app/  (11 files)
    (app)/  (4 files)
      … 4 files under this directory
    feed/  (2 files)
      … 2 files under this directory
    +html.tsx
    [...messing].tsx
    _layout.tsx
    login.tsx
    onboarding.tsx
  components/  (33 files)
    ui/  (33 files)
      … 33 files under this directory
  features/  (22 files)
    auth/  (4 files)
      … 4 files under this directory
    feed/  (5 files)
      … 5 files under this directory
    onboarding/  (2 files)
      … 2 files under this directory
    settings/  (5 files)
      … 5 files under this directory
    style-demo/  (6 files)
      … 6 files under this directory
  lib/  (16 files)
    api/  (4 files)
      … 4 files under this directory
    auth/  (1 files)
      … 1 files under this directory
    hooks/  (3 files)
      … 3 files under this directory
    i18n/  (5 files)
      … 5 files under this directory
    storage.tsx
    test-utils.tsx
    utils.ts
  translations/  (2 files)
    ar.json
    en.json
  global.css
.gitignore
LICENSE
README-project.md
README.md
app.config.ts
babel.config.js
claude.md
commitlint.config.js
eas.json
env.ts
eslint.config.mjs
jest-setup.ts
jest.config.js
lint-staged.config.js
metro.config.js
nativewind-env.d.ts
package.json
tsconfig.json
uniwind-types.d.ts
```

## Entry points

- [cli/index.js](https://github.com/obytes/react-native-template-obytes/blob/fd9b358ed11913d2a49fd9ffa6582fe03ba130e7/cli/index.js)
- [src/app/(app)/index.tsx](https://github.com/obytes/react-native-template-obytes/blob/fd9b358ed11913d2a49fd9ffa6582fe03ba130e7/src/app/%28app%29/index.tsx)
- [src/components/ui/index.tsx](https://github.com/obytes/react-native-template-obytes/blob/fd9b358ed11913d2a49fd9ffa6582fe03ba130e7/src/components/ui/index.tsx)
- [src/lib/api/index.ts](https://github.com/obytes/react-native-template-obytes/blob/fd9b358ed11913d2a49fd9ffa6582fe03ba130e7/src/lib/api/index.ts)
- [src/lib/hooks/index.tsx](https://github.com/obytes/react-native-template-obytes/blob/fd9b358ed11913d2a49fd9ffa6582fe03ba130e7/src/lib/hooks/index.tsx)
- [src/lib/i18n/index.tsx](https://github.com/obytes/react-native-template-obytes/blob/fd9b358ed11913d2a49fd9ffa6582fe03ba130e7/src/lib/i18n/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 4 file(s) under api layer (observed from repository paths and static analysis). |
| app package | library | Observed | Groups 11 file(s) under app package (observed from repository paths and static analysis). |
| cli package | library | Observed | Groups 4 file(s) under cli package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 33 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 11 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 11 file(s) under core modules (observed from repository paths and static analysis). |
| features package | library | Observed | Groups 17 file(s) under features package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 12 file(s) under lib package (observed from repository paths and static analysis). |
| __mocks__ package | library | Observed | Groups 5 file(s) under __mocks__ package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |

## Important files

- `.github/actions/eas-build/action.yml` (config)
- `.github/actions/setup-jdk-generate-apk/action.yml` (config)
- `.github/actions/setup-node-pnpm-install/action.yml` (config)
- `.github/workflows/compress-images.yml` (ci)
- `.github/workflows/e2e-android-eas-build.yml` (ci)
- `.github/workflows/e2e-android-maestro.yml` (ci)
- `.github/workflows/e2e-android.yml` (ci)
- `.github/workflows/eas-build-preview.yml` (ci)
- `.github/workflows/eas-build-prod.yml` (ci)
- `.github/workflows/expo-doctor.yml` (ci)
- `.github/workflows/lint-ts.yml` (ci)
- `.github/workflows/new-app-version.yml` (ci)
- `.github/workflows/new-github-release.yml` (ci)
- `.github/workflows/stale.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `.github/workflows/type-check.yml` (ci)
- `.maestro/app/create-post.yaml` (config)
- `.maestro/app/tabs.yaml` (config)
- `.maestro/auth/login-with-validation.yaml` (config)
- `.maestro/auth/onboarding.yaml` (config)
- `.maestro/config.yaml` (config)
- `.maestro/utils/hide-keyboard-android.yaml` (config)
- `.maestro/utils/hide-keyboard-ios.yaml` (config)
- `.maestro/utils/hide-keyboard.yaml` (config)
- `.maestro/utils/login.yaml` (config)
- `.maestro/utils/onboarding-and-login.yaml` (config)
- `.maestro/utils/onboarding.yaml` (config)
- `.vscode/extensions.json` (config)
- `.vscode/settings.json` (config)
- `cli/package.json` (manifest)
- `docs/package.json` (manifest)
- `docs/tsconfig.json` (config)
- `eas.json` (config)
- `package.json` (manifest)
- `src/translations/ar.json` (config)
- `src/translations/en.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `src` — 85 analysed file(s)
- `docs` — 47 analysed file(s)
- `(root files)` — 19 analysed file(s)
- `.github` — 19 analysed file(s)
- `.maestro` — 11 analysed file(s)
- `cli` — 6 analysed file(s)
- `.husky` — 5 analysed file(s)
- `__mocks__` — 5 analysed file(s)
- `.vscode` — 3 analysed file(s)
- `scripts` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 4 file(s) were skipped during inventory (2 x likely secret file excluded; 2 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `fd9b358ed11913d2a49fd9ffa6582fe03ba130e7` is the revision these paths and observations refer to.
