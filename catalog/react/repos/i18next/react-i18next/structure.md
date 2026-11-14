# Project structure: i18next/react-i18next

**Analysed commit:** `f97f5f82605c0ddd3ae3af6c0112c33cf7c0ab70`

**Commit reference:** [f97f5f82605c0ddd3ae3af6c0112c33cf7c0ab70](https://github.com/i18next/react-i18next/commit/f97f5f82605c0ddd3ae3af6c0112c33cf7c0ab70)

**Tree at this commit:** [i18next/react-i18next@f97f5f82605c](https://github.com/i18next/react-i18next/tree/f97f5f82605c0ddd3ae3af6c0112c33cf7c0ab70)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | i18next/react-i18next |
| Description | Internationalization for react done right. Using the i18next i18n ecosystem. |
| Stars | 10066 |
| Forks | 1053 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `f97f5f82605c0ddd3ae3af6c0112c33cf7c0ab70` |
| Retrieved at | 2026-11-14T19:13:32.112928+00:00 |
| Files in this snapshot | 453 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (2 files)
    CI.yml
    types-compat.yml
  stale.yml
.husky/  (1 files)
  pre-commit
example/  (293 files)
  ReactNativeLocizeProject/  (41 files)
    .bundle/  (1 files)
      … 1 files under this directory
    __tests__/  (1 files)
      … 1 files under this directory
    android/  (14 files)
      … 14 files under this directory
    ios/  (11 files)
      … 11 files under this directory
    .gitignore
    .prettierrc.js
    .watchmanconfig
    App.tsx
    Gemfile
    README.md
    app.json
    babel.config.js
    i18n.js
    index.js
    jest.config.js
    metro.config.js
    package.json
    tsconfig.json
  ReactNativeProject/  (43 files)
    .bundle/  (1 files)
      … 1 files under this directory
    __tests__/  (1 files)
      … 1 files under this directory
    android/  (14 files)
      … 14 files under this directory
    ios/  (11 files)
      … 11 files under this directory
    locales/  (2 files)
      … 2 files under this directory
    .gitignore
    .prettierrc.js
    .watchmanconfig
    App.tsx
    Gemfile
    README.md
    app.json
    babel.config.js
    i18n.js
    index.js
    jest.config.js
    metro.config.js
    package.json
    tsconfig.json
  devserver-save-missing/  (14 files)
    public/  (3 files)
      … 3 files under this directory
    src/  (6 files)
      … 6 files under this directory
    .gitignore
    README.md
    index.html
    package.json
    vite.config.js
  locize/  (13 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (6 files)
      … 6 files under this directory
    .eslintrc.js
    .gitignore
    README.md
    index.html
    package.json
    vite.config.js
  razzle-ssr/  (17 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (10 files)
      … 10 files under this directory
    .gitignore
    README.md
    index.html
    package.json
    server.js
    vite.config.js
  react/  (15 files)
    public/  (4 files)
      … 4 files under this directory
    src/  (6 files)
      … 6 files under this directory
    .gitignore
    README.md
    index.html
    package.json
    vite.config.js
  react-component-lib/  (16 files)
    public/  (4 files)
      … 4 files under this directory
    src/  (7 files)
      … 7 files under this directory
    .gitignore
    README.md
    index.html
    package.json
    vite.config.js
  react-fluent/  (13 files)
    public/  (3 files)
      … 3 files under this directory
    src/  (6 files)
      … 6 files under this directory
    .gitignore
    index.html
    package.json
    vite.config.js
  react-icu/  (20 files)
    public/  (5 files)
      … 5 files under this directory
    src/  (10 files)
      … 10 files under this directory
    .gitignore
    README.md
    index.html
    package.json
    vite.config.js
  react-localstorage/  (14 files)
    public/  (3 files)
      … 3 files under this directory
    src/  (6 files)
      … 6 files under this directory
    .gitignore
    README.md
    index.html
    package.json
    vite.config.js
  react-typescript/  (37 files)
    public/  (1 files)
      … 1 files under this directory
    simple/  (16 files)
      … 16 files under this directory
    simple-multi-namespaces/  (20 files)
      … 20 files under this directory
  storybook/  (19 files)
    .storybook/  (2 files)
      … 2 files under this directory
    public/  (4 files)
      … 4 files under this directory
    src/  (8 files)
      … 8 files under this directory
    .gitignore
    README.md
    index.html
    package.json
    vite.config.js
  test-jest/  (31 files)
    public/  (4 files)
      … 4 files under this directory
    src/  (20 files)
      … 20 files under this directory
    .gitignore
    README.md
    babel.config.js
    index.html
    jest.config.js
    package.json
    vite.config.js
src/  (23 files)
  IcuTransUtils/  (5 files)
    TranslationParserError.js
    htmlEntityDecoder.js
    index.js
    renderTranslation.js
    tokenizer.js
  I18nextProvider.js
  IcuTrans.js
  IcuTransWithoutContext.js
  Trans.js
  TransWithoutContext.js
  Translation.js
  context.js
  defaults.js
  i18nInstance.js
  index.js
  index.react-server.js
  initReactI18next.js
  unescape.js
  useSSR.js
  useTranslation.js
  utils.js
  withSSR.js
  withTranslation.js
test/  (102 files)
  IcuTrans/  (5 files)
    utils/  (3 files)
      … 3 files under this directory
    IcuTrans.spec.jsx
    IcuTransWithoutContext.spec.jsx
  typescript/  (65 files)
    augment-react-not-imported/  (3 files)
      … 3 files under this directory
    custom-types/  (8 files)
      … 8 files under this directory
    icu-arguments/  (3 files)
      … 3 files under this directory
    issue-1899/  (4 files)
      … 4 files under this directory
    key-separator-false/  (3 files)
      … 3 files under this directory
    mf2-arguments/  (3 files)
      … 3 files under this directory
    misc/  (14 files)
      … 14 files under this directory
    selector-custom-types/  (8 files)
      … 8 files under this directory
    selector-default-ns-false/  (3 files)
      … 3 files under this directory
    selector-optimize/  (8 files)
      … 8 files under this directory
    selector-strict/  (4 files)
      … 4 files under this directory
    strict-interpolation/  (3 files)
      … 3 files under this directory
    _stub.js
  I18nextProvider.spec.jsx
  Translation.spec.jsx
  backendLngAwareMock.js
  backendMock.js
  hasLoadedNamespaceMock.js
  i18n.js
  i18nNoLng.js
  index.react-server.spec.js
  initReactI18next.spec.js
  setup.js
  trans.languageChange.spec.jsx
  trans.nodeToString.spec.jsx
  trans.render.childValues.spec.jsx
  trans.render.dynamic.spec.jsx
  trans.render.icu.spec.jsx
  trans.render.noLng.spec.jsx
  trans.render.object.spec.jsx
  trans.render.spec.jsx
  unescape.spec.js
  useSSR.spec.js
  useTranslation.advanced.spec.js
  useTranslation.bindI18nStore.spec.jsx
  useTranslation.loading.spec.js
  useTranslation.loadingLng.spec.js
  … 8 more files
.all-contributorsrc
.babelrc
.codeclimate.yml
.coveralls.yml
.editorconfig
.gitignore
.prettierignore
.prettierrc.json
CHANGELOG.md
IcuTransWithoutContext.d.mts
IcuTransWithoutContext.d.ts
LICENSE
README.md
TransWithoutContext.d.mts
TransWithoutContext.d.ts
augment-react.d.mts
augment-react.d.ts
augment-react.js
eslint.config.mjs
helpers.d.ts
index.d.mts
index.d.ts
initReactI18next.d.mts
initReactI18next.d.ts
… 7 more files
```

## Entry points

- [src/IcuTransUtils/index.js](https://github.com/i18next/react-i18next/blob/f97f5f82605c0ddd3ae3af6c0112c33cf7c0ab70/src/IcuTransUtils/index.js)
- [src/index.js](https://github.com/i18next/react-i18next/blob/f97f5f82605c0ddd3ae3af6c0112c33cf7c0ab70/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| context.js package | library | Observed | Groups 1 file(s) under context.js package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 11 file(s) under core modules (observed from repository paths and static analysis). |
| defaults.js package | library | Observed | Groups 1 file(s) under defaults.js package (observed from repository paths and static analysis). |
| I18nextProvider.js package | library | Observed | Groups 1 file(s) under i18nextprovider.js package (observed from repository paths and static analysis). |
| i18nInstance.js package | library | Observed | Groups 1 file(s) under i18ninstance.js package (observed from repository paths and static analysis). |
| IcuTrans.js package | library | Observed | Groups 1 file(s) under icutrans.js package (observed from repository paths and static analysis). |
| IcuTransUtils package | library | Observed | Groups 5 file(s) under icutransutils package (observed from repository paths and static analysis). |
| IcuTransWithoutContext.js package | library | Observed | Groups 1 file(s) under icutranswithoutcontext.js package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| index.react-server.js package | library | Observed | Groups 1 file(s) under index.react-server.js package (observed from repository paths and static analysis). |
| initReactI18next.js package | library | Observed | Groups 1 file(s) under initreacti18next.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 102 file(s) under tests (observed from repository paths and static analysis). |
| Trans.js package | library | Observed | Groups 1 file(s) under trans.js package (observed from repository paths and static analysis). |
| Translation.js package | library | Observed | Groups 1 file(s) under translation.js package (observed from repository paths and static analysis). |
| TransWithoutContext.js package | library | Observed | Groups 1 file(s) under transwithoutcontext.js package (observed from repository paths and static analysis). |
| unescape.js package | library | Observed | Groups 1 file(s) under unescape.js package (observed from repository paths and static analysis). |
| useSSR.js package | library | Observed | Groups 1 file(s) under usessr.js package (observed from repository paths and static analysis). |
| useTranslation.js package | library | Observed | Groups 1 file(s) under usetranslation.js package (observed from repository paths and static analysis). |
| utils.js package | library | Observed | Groups 1 file(s) under utils.js package (observed from repository paths and static analysis). |
| withSSR.js package | library | Observed | Groups 1 file(s) under withssr.js package (observed from repository paths and static analysis). |
| withTranslation.js package | library | Observed | Groups 1 file(s) under withtranslation.js package (observed from repository paths and static analysis). |

## Important files

- `.codeclimate.yml` (config)
- `.coveralls.yml` (config)
- `.editorconfig` (config)
- `.github/stale.yml` (config)
- `.github/workflows/CI.yml` (ci)
- `.github/workflows/types-compat.yml` (ci)
- `.prettierrc.json` (config)
- `example/ReactNativeLocizeProject/android/app/build.gradle` (manifest)
- `example/ReactNativeLocizeProject/android/build.gradle` (manifest)
- `example/ReactNativeLocizeProject/app.json` (config)
- `example/ReactNativeLocizeProject/ios/ReactNativeLocizeProject/Images.xcassets/AppIcon.appiconset/Contents.json` (config)
- `example/ReactNativeLocizeProject/ios/ReactNativeLocizeProject/Images.xcassets/Contents.json` (config)
- `example/ReactNativeLocizeProject/package.json` (manifest)
- `example/ReactNativeLocizeProject/tsconfig.json` (config)
- `example/ReactNativeProject/android/app/build.gradle` (manifest)
- `example/ReactNativeProject/android/build.gradle` (manifest)
- `example/ReactNativeProject/app.json` (config)
- `example/ReactNativeProject/ios/ReactNativeProject/Images.xcassets/AppIcon.appiconset/Contents.json` (config)
- `example/ReactNativeProject/ios/ReactNativeProject/Images.xcassets/Contents.json` (config)
- `example/ReactNativeProject/locales/de/translation.json` (config)
- `example/ReactNativeProject/locales/en/translation.json` (config)
- `example/ReactNativeProject/package.json` (manifest)
- `example/ReactNativeProject/tsconfig.json` (config)
- `example/devserver-save-missing/package.json` (manifest)
- `example/devserver-save-missing/public/locales/de/translation.json` (config)
- `example/devserver-save-missing/public/locales/en/translation.json` (config)
- `example/devserver-save-missing/public/manifest.json` (config)
- `example/locize/package.json` (manifest)
- `example/locize/public/manifest.json` (config)
- `example/razzle-ssr/package.json` (manifest)
- `example/razzle-ssr/src/locales/de/translations.json` (config)
- `example/razzle-ssr/src/locales/en/translations.json` (config)
- `example/react-component-lib/package.json` (manifest)
- `example/react-component-lib/public/locales/de/translation.json` (config)
- `example/react-component-lib/public/locales/en/translation.json` (config)
- `example/react-component-lib/public/manifest.json` (config)
- `example/react-fluent/package.json` (manifest)
- `example/react-fluent/public/manifest.json` (config)
- `example/react-icu/package.json` (manifest)
- `example/react-icu/public/locales/de/translations.json` (config)
- `example/react-icu/public/locales/en/translations.json` (config)
- `example/react-icu/public/locales/ru/translations.json` (config)
- `example/react-icu/public/manifest.json` (config)
- `example/react-localstorage/package.json` (manifest)
- `example/react-localstorage/public/locales/de/translation.json` (config)
- `example/react-localstorage/public/locales/en/translation.json` (config)
- `example/react-localstorage/public/manifest.json` (config)
- `example/react-typescript/public/locales/sv/translation.json` (config)
- `example/react-typescript/simple-multi-namespaces/package.json` (manifest)
- `example/react-typescript/simple-multi-namespaces/public/manifest.json` (config)
- `example/react-typescript/simple-multi-namespaces/src/i18n/en/ns1.json` (config)
- `example/react-typescript/simple-multi-namespaces/src/i18n/en/ns2.json` (config)
- `example/react-typescript/simple-multi-namespaces/tsconfig.json` (config)
- `example/react-typescript/simple/package.json` (manifest)
- `example/react-typescript/simple/public/manifest.json` (config)
- `example/react-typescript/simple/src/i18n/en/translation.json` (config)
- `example/react-typescript/simple/tsconfig.json` (config)
- `example/react/package.json` (manifest)
- `example/react/public/locales/de/translation.json` (config)
- `example/react/public/locales/en/translation.json` (config)
- `example/react/public/locales/sv/translation.json` (config)
- `example/react/public/manifest.json` (config)
- `example/storybook/package.json` (manifest)
- `example/storybook/public/locales/ar/translation.json` (config)
- `example/storybook/public/locales/de/translation.json` (config)
- `example/storybook/public/locales/en/translation.json` (config)
- `example/storybook/public/manifest.json` (config)
- `example/test-jest/package.json` (manifest)
- `example/test-jest/public/locales/de/translations.json` (config)
- `example/test-jest/public/locales/en/translations.json` (config)
- `example/test-jest/public/locales/sv/translations.json` (config)
- `example/test-jest/public/manifest.json` (config)
- `package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `example` — 293 analysed file(s)
- `test` — 102 analysed file(s)
- `(root files)` — 31 analysed file(s)
- `src` — 23 analysed file(s)
- `.github` — 3 analysed file(s)
- `.husky` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 11 file(s) were skipped during inventory (11 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `f97f5f82605c0ddd3ae3af6c0112c33cf7c0ab70` is the revision these paths and observations refer to.
