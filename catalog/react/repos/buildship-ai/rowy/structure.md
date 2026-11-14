# Project structure: buildship-ai/rowy

**Analysed commit:** `a5b4316cf04c7b653f007e8420ca189b587637cf`

**Commit reference:** [a5b4316cf04c7b653f007e8420ca189b587637cf](https://github.com/buildship-ai/rowy/commit/a5b4316cf04c7b653f007e8420ca189b587637cf)

**Tree at this commit:** [buildship-ai/rowy@a5b4316cf04c](https://github.com/buildship-ai/rowy/tree/a5b4316cf04c7b653f007e8420ca189b587637cf)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | buildship-ai/rowy |
| Description | Low-code backend platform. Manage database on spreadsheet-like UI and build cloud functions workflows in JS/TS, all in your browser. |
| Stars | 6846 |
| Forks | 562 |
| Licence | Other |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `a5b4316cf04c7b653f007e8420ca189b587637cf` |
| Retrieved at | 2026-11-14T19:14:01.121911+00:00 |
| Files in this snapshot | 718 |

## Directory tree

```text
.github/  (6 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    config.yml
    feature_request.md
  workflows/  (3 files)
    codeql-analysis.yml
    deploy-preview.yml
    tweet_release.yml
.husky/  (1 files)
  pre-commit
.opensource/  (1 files)
  project.json
emulators/  (3 files)
  auth_export/  (2 files)
    accounts.json
    config.json
  firebase-export-metadata.json
public/  (5 files)
  favicon/  (2 files)
    icon.svg
    safari-pinned-tab.svg
  manifest.json
  robots.txt
  site.webmanifest
src/  (677 files)
  assets/  (40 files)
    icons/  (20 files)
      … 20 files under this directory
    logos/  (6 files)
      … 6 files under this directory
    tutorial/  (6 files)
      … 6 files under this directory
    BrandedBackground.tsx
    Favicon.tsx
    Logo.tsx
    LogoRowyRun.tsx
    bg-pattern-dark.svg
    bg-pattern.svg
    favicon.svg
    logo-sticker.svg
  atoms/  (14 files)
    projectScope/  (6 files)
      … 6 files under this directory
    tableScope/  (7 files)
      … 7 files under this directory
    utils.ts
  components/  (509 files)
    CodeEditor/  (13 files)
      … 13 files under this directory
    ColumnMenu/  (3 files)
      … 3 files under this directory
    ColumnModals/  (11 files)
      … 11 files under this directory
    GetStartedChecklist/  (4 files)
      … 4 files under this directory
    Modal/  (6 files)
      … 6 files under this directory
    ProjectSettingsDialog/  (3 files)
      … 3 files under this directory
    SelectColors/  (2 files)
      … 2 files under this directory
    Settings/  (15 files)
      … 15 files under this directory
    Setup/  (8 files)
      … 8 files under this directory
    SideDrawer/  (9 files)
      … 9 files under this directory
    Table/  (43 files)
      … 43 files under this directory
    TableInformationDrawer/  (3 files)
      … 3 files under this directory
    TableModals/  (72 files)
      … 72 files under this directory
    TableSettingsDialog/  (14 files)
      … 14 files under this directory
    TableToolbar/  (25 files)
      … 25 files under this directory
    TableTutorial/  (11 files)
      … 11 files under this directory
    Tables/  (9 files)
      … 9 files under this directory
    fields/  (228 files)
      … 228 files under this directory
    AccessDenied.tsx
    ButtonWithStatus.tsx
    CircularProgressOptical.tsx
    CircularProgressTimed.tsx
    ColorPickerInput.tsx
    ConfirmDialog.tsx
    EmojiAvatar.tsx
    EmptyState.tsx
    ErrorFallback.tsx
    FirebaseUi.tsx
    FloatingSearch.tsx
    FormattedChip.tsx
    FullScreenButton.tsx
    IconSlash.tsx
    InfoTooltip.tsx
    InlineOpenInNewIcon.tsx
    KeyValueInput.tsx
    Loading.tsx
    RenderedHtml.tsx
    RenderedMarkdown.tsx
    RichTextEditor.tsx
    RichTooltip.tsx
    RowyRunModal.tsx
    SectionHeading.tsx
    … 6 more files
  config/  (5 files)
    db.ts
    dbPaths.ts
    firebaseui.ts
    firestoreRules.ts
    storageRules.ts
  constants/  (6 files)
    dates.ts
    externalLinks.ts
    fields.ts
    regions.ts
    routes.tsx
    runRoutes.ts
  contexts/  (3 files)
    SnackLogContext.tsx
    SnackbarContext.tsx
    SwrContext.tsx
  hooks/  (13 files)
    useBasicSearch.ts
    useBeforeUnload.ts
    useDocumentTitle.ts
    useFirebaseStorageUploader.tsx
    useFirestoreCollectionWithAtom.ts
    useFirestoreDocAsCollectionWithAtom.ts
    useFirestoreDocWithAtom.ts
    useKeyPress.ts
    useKeyPressWithAtom.ts
    useOffline.ts
    useSaveOnUnmount.ts
    useScrollToHash.ts
    useUpdateCheck.ts
  layouts/  (19 files)
    Navigation/  (14 files)
      … 14 files under this directory
    AdminRoute.tsx
    AuthLayout.tsx
    MarketingPanel.tsx
    Nav.tsx
    RequireAuth.tsx
  pages/  (21 files)
    Auth/  (5 files)
      … 5 files under this directory
    Settings/  (4 files)
      … 4 files under this directory
    Table/  (5 files)
      … 5 files under this directory
    Test/  (3 files)
      … 3 files under this directory
    NotFoundPage.tsx
    SetupPage.tsx
    TableGroupRedirectPage.tsx
    TablesPage.tsx
  sources/  (14 files)
    ProjectSourceFirebase/  (6 files)
      … 6 files under this directory
    TableSourceFirestore/  (6 files)
      … 6 files under this directory
    FunctionsSourceFirestore.tsx
    MembersSourceFirebase.tsx
  test/  (5 files)
    App.test.tsx
    custom-jest-env.js
    importStub.js
    setupTests.ts
    testUtils.tsx
  theme/  (12 files)
    CheckboxIcon.tsx
    CheckboxIndeterminateIcon.tsx
    RadioIcon.tsx
    RowyThemeProvider.tsx
    breakpoints.ts
    colors.ts
    components.tsx
    index.ts
    palette.ts
    space-grotesk.css
    themes.ts
    typography.ts
  types/  (6 files)
    files.d.ts
    function.d.ts
    json-stable-stringify-without-jsonify.d.ts
    react-element-scroll-hook.d.ts
    settings.d.ts
    table.d.ts
  utils/  (4 files)
    color.ts
    date.ts
    table.ts
    ui.ts
  App.tsx
  Providers.tsx
  analytics.ts
  index.tsx
  reportWebVitals.ts
  vite-env.d.ts
.env.example
.eslintignore
.gitignore
.prettierignore
.prettierrc
.yarnrc
.yarnrc.yml
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
cloudbuild.yaml
craco.config.js
createDotEnv.js
eslint-local-rules.js
firebase.json
firestore.indexes.json
firestore.rules
index.html
package.json
storage.rules
tsconfig.extend.json
tsconfig.json
typedoc.json
… 1 more files
```

## Entry points

- [src/App.tsx](https://github.com/buildship-ai/rowy/blob/a5b4316cf04c7b653f007e8420ca189b587637cf/src/App.tsx)
- [src/assets/icons/index.ts](https://github.com/buildship-ai/rowy/blob/a5b4316cf04c7b653f007e8420ca189b587637cf/src/assets/icons/index.ts)
- [src/atoms/projectScope/index.ts](https://github.com/buildship-ai/rowy/blob/a5b4316cf04c7b653f007e8420ca189b587637cf/src/atoms/projectScope/index.ts)
- [src/atoms/tableScope/index.ts](https://github.com/buildship-ai/rowy/blob/a5b4316cf04c7b653f007e8420ca189b587637cf/src/atoms/tableScope/index.ts)
- [src/components/CodeEditor/index.ts](https://github.com/buildship-ai/rowy/blob/a5b4316cf04c7b653f007e8420ca189b587637cf/src/components/CodeEditor/index.ts)
- [src/components/ColumnMenu/index.ts](https://github.com/buildship-ai/rowy/blob/a5b4316cf04c7b653f007e8420ca189b587637cf/src/components/ColumnMenu/index.ts)
- [src/components/ColumnModals/index.ts](https://github.com/buildship-ai/rowy/blob/a5b4316cf04c7b653f007e8420ca189b587637cf/src/components/ColumnModals/index.ts)
- [src/components/GetStartedChecklist/index.ts](https://github.com/buildship-ai/rowy/blob/a5b4316cf04c7b653f007e8420ca189b587637cf/src/components/GetStartedChecklist/index.ts)
- [src/components/Modal/index.ts](https://github.com/buildship-ai/rowy/blob/a5b4316cf04c7b653f007e8420ca189b587637cf/src/components/Modal/index.ts)
- [src/components/ProjectSettingsDialog/index.ts](https://github.com/buildship-ai/rowy/blob/a5b4316cf04c7b653f007e8420ca189b587637cf/src/components/ProjectSettingsDialog/index.ts)
- [src/components/SelectColors/index.tsx](https://github.com/buildship-ai/rowy/blob/a5b4316cf04c7b653f007e8420ca189b587637cf/src/components/SelectColors/index.tsx)
- [src/components/SideDrawer/index.ts](https://github.com/buildship-ai/rowy/blob/a5b4316cf04c7b653f007e8420ca189b587637cf/src/components/SideDrawer/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| analytics.ts package | library | Observed | Groups 1 file(s) under analytics.ts package (observed from repository paths and static analysis). |
| App.tsx package | library | Observed | Groups 1 file(s) under app.tsx package (observed from repository paths and static analysis). |
| assets package | library | Observed | Groups 24 file(s) under assets package (observed from repository paths and static analysis). |
| atoms package | library | Observed | Groups 14 file(s) under atoms package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 492 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 37 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| constants package | library | Observed | Groups 6 file(s) under constants package (observed from repository paths and static analysis). |
| contexts package | library | Observed | Groups 3 file(s) under contexts package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 13 file(s) under hooks package (observed from repository paths and static analysis). |
| index.tsx package | library | Observed | Groups 1 file(s) under index.tsx package (observed from repository paths and static analysis). |
| layouts package | library | Observed | Groups 19 file(s) under layouts package (observed from repository paths and static analysis). |
| pages package | library | Observed | Groups 14 file(s) under pages package (observed from repository paths and static analysis). |
| Providers.tsx package | library | Observed | Groups 1 file(s) under providers.tsx package (observed from repository paths and static analysis). |
| reportWebVitals.ts package | library | Observed | Groups 1 file(s) under reportwebvitals.ts package (observed from repository paths and static analysis). |
| sources package | library | Observed | Groups 14 file(s) under sources package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 8 file(s) under tests (observed from repository paths and static analysis). |
| theme package | library | Observed | Groups 11 file(s) under theme package (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 6 file(s) under types package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 4 file(s) under utils package (observed from repository paths and static analysis). |
| vite-env.d.ts package | library | Observed | Groups 1 file(s) under vite-env.d.ts package (observed from repository paths and static analysis). |

## Important files

- `.env.example` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/codeql-analysis.yml` (ci)
- `.github/workflows/deploy-preview.yml` (ci)
- `.github/workflows/tweet_release.yml` (ci)
- `.opensource/project.json` (config)
- `.yarnrc.yml` (config)
- `cloudbuild.yaml` (config)
- `emulators/auth_export/accounts.json` (config)
- `emulators/auth_export/config.json` (config)
- `emulators/firebase-export-metadata.json` (config)
- `firebase.json` (config)
- `firestore.indexes.json` (config)
- `package.json` (manifest)
- `public/manifest.json` (config)
- `src/components/CodeEditor/github-dark-default.json` (config)
- `src/components/CodeEditor/github-light-default.json` (config)
- `tsconfig.extend.json` (config)
- `tsconfig.json` (config)
- `typedoc.json` (config)

## Top-level layout

- `src` — 677 analysed file(s)
- `(root files)` — 25 analysed file(s)
- `.github` — 6 analysed file(s)
- `public` — 5 analysed file(s)
- `emulators` — 3 analysed file(s)
- `.husky` — 1 analysed file(s)
- `.opensource` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `a5b4316cf04c7b653f007e8420ca189b587637cf` is the revision these paths and observations refer to.
