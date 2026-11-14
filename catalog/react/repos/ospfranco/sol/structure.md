# Project structure: ospfranco/sol

**Analysed commit:** `873ae1c28b153f190a57a56a5ad2bea2159611f8`

**Commit reference:** [873ae1c28b153f190a57a56a5ad2bea2159611f8](https://github.com/ospfranco/sol/commit/873ae1c28b153f190a57a56a5ad2bea2159611f8)

**Tree at this commit:** [ospfranco/sol@873ae1c28b15](https://github.com/ospfranco/sol/tree/873ae1c28b153f190a57a56a5ad2bea2159611f8)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | ospfranco/sol |
| Description | MacOS launcher & command palette |
| Stars | 3211 |
| Forks | 195 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `873ae1c28b153f190a57a56a5ad2bea2159611f8` |
| Retrieved at | 2026-11-14T19:15:28.460865+00:00 |
| Files in this snapshot | 198 |

## Directory tree

```text
.github/  (3 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  FUNDING.yml
.vscode/  (1 files)
  settings.json
fastlane/  (4 files)
  actions/  (1 files)
    check_apple_agreement.rb
  Appfile
  Fastfile
  README.md
macos/  (89 files)
  sol-macOS/  (76 files)
    Assets.xcassets/  (2 files)
      … 2 files under this directory
    Base.lproj/  (1 files)
      … 1 files under this directory
    extensions/  (7 files)
      … 7 files under this directory
    lib/  (43 files)
      … 43 files under this directory
    managers/  (5 files)
      … 5 files under this directory
    views/  (13 files)
      … 13 files under this directory
    AppDelegate.swift
    Info.plist
    sol-macOS-Bridging-Header.h
    sol-macOS.entitlements
    sol.entitlements
  sol.xcodeproj/  (4 files)
    project.xcworkspace/  (1 files)
      … 1 files under this directory
    xcshareddata/  (2 files)
      … 2 files under this directory
    project.pbxproj
  sol.xcworkspace/  (4 files)
    xcshareddata/  (3 files)
      … 3 files under this directory
    contents.xcworkspacedata
  .gitignore
  .xcode.env
  Podfile
  Podfile.lock
  PrivacyInfo.xcprivacy
patches/  (2 files)
  react-native-macos@0.81.7.patch
  react-native-restart-newarch@1.0.85.patch
releases/  (1 files)
  appcast.xml
scripts/  (2 files)
  appcast.js
  bump-version.sh
src/  (78 files)
  components/  (19 files)
    BackButton.tsx
    BlurView.tsx
    Dropdown.tsx
    Fade.tsx
    Favicon.tsx
    FileIcon.tsx
    FullCalendar.tsx
    GradientView.tsx
    Input.tsx
    Key.tsx
    KeyboardShortcutRecorderView.tsx
    LoadingBar.tsx
    MainInput.tsx
    MyRadioButton.tsx
    MySwitch.tsx
    PermissionsBar.tsx
    SelectableButton.tsx
    SolButton.tsx
    SystemPreferencesIcon.tsx
  containers/  (2 files)
    index.ts
    root.container.tsx
  hooks/  (3 files)
    index.ts
    useBoolean.ts
    useFullSize.ts
  lib/  (15 files)
    SolNative.ts
    calendar.ts
    constants.ts
    emojiCompatibility.test.js
    emojiCompatibility.ts
    emojiSkinToneVariants.ts
    emojiSkinTones.test.js
    emojiSkinTones.ts
    github.ts
    languages.ts
    shortcuts.tsx
    symbols.ts
    translator.ts
    various.ts
    weather.ts
  stores/  (12 files)
    calendar.store.tsx
    clipboard.store.tsx
    config.ts
    emoji.store.tsx
    items.tsx
    keystroke.store.ts
    persisted-config.ts
    processes.store.tsx
    scripts.store.tsx
    systemPreferences.tsx
    ui.store.helpers.ts
    ui.store.tsx
  widgets/  (18 files)
    settings/  (7 files)
      … 7 files under this directory
    calendar.widget.tsx
    clipboard.widget.tsx
    createItem.widget.tsx
    emojis.widget.tsx
    fileSearch.widget.tsx
    onboarding.widget.tsx
    processes.widget.tsx
    scratchpad.widget.tsx
    search.widget.tsx
    settings.widget.tsx
    translation.widget.tsx
  app.tsx
  assets.ts
  colors.js
  config.ts
  global.css
  globals.d.ts
  mytailwind.ts
  nativewind-macos.d.ts
  store.ts
tests/  (2 files)
  screen-selection/  (2 files)
    Stubs.swift
    main.swift
.gitignore
.prettierrc
Gemfile
Gemfile.lock
LICENSE
README.md
app.json
babel.config.js
biome.json
index.js
metro.config.js
mise.toml
nativewind-env.d.ts
package.json
tailwind.config.js
tsconfig.json
```

## Entry points

- [index.js](https://github.com/ospfranco/sol/blob/873ae1c28b153f190a57a56a5ad2bea2159611f8/index.js)
- [src/app.tsx](https://github.com/ospfranco/sol/blob/873ae1c28b153f190a57a56a5ad2bea2159611f8/src/app.tsx)
- [src/containers/index.ts](https://github.com/ospfranco/sol/blob/873ae1c28b153f190a57a56a5ad2bea2159611f8/src/containers/index.ts)
- [src/hooks/index.ts](https://github.com/ospfranco/sol/blob/873ae1c28b153f190a57a56a5ad2bea2159611f8/src/hooks/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| app.tsx package | library | Observed | Groups 1 file(s) under app.tsx package (observed from repository paths and static analysis). |
| assets.ts package | library | Observed | Groups 1 file(s) under assets.ts package (observed from repository paths and static analysis). |
| colors.js package | library | Observed | Groups 1 file(s) under colors.js package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 19 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 14 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| config.ts package | library | Observed | Groups 1 file(s) under config.ts package (observed from repository paths and static analysis). |
| containers package | library | Observed | Groups 2 file(s) under containers package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 5 file(s) under core modules (observed from repository paths and static analysis). |
| fastlane package | library | Observed | Groups 1 file(s) under fastlane package (observed from repository paths and static analysis). |
| globals.d.ts package | library | Observed | Groups 1 file(s) under globals.d.ts package (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 3 file(s) under hooks package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 15 file(s) under lib package (observed from repository paths and static analysis). |
| macos package | library | Observed | Groups 10 file(s) under macos package (observed from repository paths and static analysis). |
| mytailwind.ts package | library | Observed | Groups 1 file(s) under mytailwind.ts package (observed from repository paths and static analysis). |
| nativewind-macos.d.ts package | library | Observed | Groups 1 file(s) under nativewind-macos.d.ts package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 2 file(s) under scripts package (observed from repository paths and static analysis). |
| store.ts package | library | Observed | Groups 1 file(s) under store.ts package (observed from repository paths and static analysis). |
| stores package | library | Observed | Groups 12 file(s) under stores package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 2 file(s) under tests (observed from repository paths and static analysis). |
| widgets package | library | Observed | Groups 11 file(s) under widgets package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.vscode/settings.json` (config)
- `app.json` (config)
- `biome.json` (config)
- `macos/sol-macOS/Assets.xcassets/AppIcon.appiconset/Contents.json` (config)
- `macos/sol-macOS/Assets.xcassets/Contents.json` (config)
- `mise.toml` (config)
- `package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `macos` — 89 analysed file(s)
- `src` — 78 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `fastlane` — 4 analysed file(s)
- `.github` — 3 analysed file(s)
- `patches` — 2 analysed file(s)
- `scripts` — 2 analysed file(s)
- `tests` — 2 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `releases` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `873ae1c28b153f190a57a56a5ad2bea2159611f8` is the revision these paths and observations refer to.
