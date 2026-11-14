# Project structure: xanderfrangos/twinkle-tray

**Analysed commit:** `f4b36e12e2dbedd415a588b9baa2b8c65cf01f30`

**Commit reference:** [f4b36e12e2dbedd415a588b9baa2b8c65cf01f30](https://github.com/xanderfrangos/twinkle-tray/commit/f4b36e12e2dbedd415a588b9baa2b8c65cf01f30)

**Tree at this commit:** [xanderfrangos/twinkle-tray@f4b36e12e2db](https://github.com/xanderfrangos/twinkle-tray/tree/f4b36e12e2dbedd415a588b9baa2b8c65cf01f30)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | xanderfrangos/twinkle-tray |
| Description | Easily manage the brightness of your monitors in Windows from the system tray |
| Stars | 9357 |
| Forks | 351 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `f4b36e12e2dbedd415a588b9baa2b8c65cf01f30` |
| Retrieved at | 2026-11-14T19:13:34.047562+00:00 |
| Files in this snapshot | 177 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (1 files)
    ci.yml
  FUNDING.yml
.vscode/  (1 files)
  settings.json
resources/  (3 files)
  appx/  (1 files)
    extensions.xml
  nsis/  (1 files)
    installer.nsh
  afterPack.js
src/  (163 files)
  components/  (16 files)
    light-sensor/  (4 files)
      … 4 files under this directory
    utilts/  (1 files)
      … 1 files under this directory
    BrightnessPanel.jsx
    DDCCISliders.jsx
    HDRSliders.jsx
    IntroWindow.jsx
    MonitorFeatures.jsx
    MonitorInfo.jsx
    SafeRender.jsx
    SettingsOption.jsx
    SettingsWindow.jsx
    Slider.jsx
    Titlebar.jsx
  css/  (9 files)
    common.scss
    intro.scss
    light-sensor.scss
    mica.scss
    page.scss
    panel.scss
    settings-option.scss
    slider.scss
    vars.scss
  hooks/  (1 files)
    useObject.js
  html/  (3 files)
    index.html
    intro.html
    settings.html
  light-sensor/  (5 files)
    sensors/  (3 files)
      … 3 files under this directory
    light-sensor.js
    light-sensor.utilts.js
  localization/  (38 files)
    ar.json
    az.json
    bn.json
    ckb.json
    cs.json
    de.json
    el.json
    en-GB.json
    en.json
    es.json
    fa.json
    fi.json
    fr.json
    he.json
    hi.json
    hr.json
    hu.json
    id.json
    it.json
    ja.json
    ko.json
    lt.json
    nb.json
    nl.json
    … 14 more files
  modules/  (73 files)
    acrylic/  (5 files)
      … 5 files under this directory
    node-active-window/  (19 files)
      … 19 files under this directory
    node-ddcci/  (9 files)
      … 9 files under this directory
    tt-windows-utils/  (11 files)
      … 11 files under this directory
    win32-displayconfig/  (12 files)
      … 12 files under this directory
    windows-ambient-sensor/  (7 files)
      … 7 files under this directory
    windows-hdr/  (5 files)
      … 5 files under this directory
    wmi-bridge/  (5 files)
      … 5 files under this directory
  utils/  (1 files)
    BrightnessPanel/  (1 files)
      … 1 files under this directory
  Logger.js
  Monitors.js
  Translate.js
  TranslateReact.js
  Utils.js
  intro-preload.js
  intro.js
  monitor-rules.json
  panel-preload.js
  panel.js
  parcel.js
  parcelAPI.js
  settings-preload.js
  settings.js
  vcp-codes.js
  volume-utils.js
  wmi-bridge-test.js
tests/  (1 files)
  volume-values.test.cjs
.babelrc
.gitattributes
.gitignore
.sassrc
LICENSE
README.md
package.json
```

## Entry points

- [src/modules/acrylic/index.js](https://github.com/xanderfrangos/twinkle-tray/blob/f4b36e12e2dbedd415a588b9baa2b8c65cf01f30/src/modules/acrylic/index.js)
- [src/modules/node-ddcci/index.js](https://github.com/xanderfrangos/twinkle-tray/blob/f4b36e12e2dbedd415a588b9baa2b8c65cf01f30/src/modules/node-ddcci/index.js)
- [src/modules/tt-windows-utils/index.js](https://github.com/xanderfrangos/twinkle-tray/blob/f4b36e12e2dbedd415a588b9baa2b8c65cf01f30/src/modules/tt-windows-utils/index.js)
- [src/modules/win32-displayconfig/index.js](https://github.com/xanderfrangos/twinkle-tray/blob/f4b36e12e2dbedd415a588b9baa2b8c65cf01f30/src/modules/win32-displayconfig/index.js)
- [src/modules/windows-ambient-sensor/index.js](https://github.com/xanderfrangos/twinkle-tray/blob/f4b36e12e2dbedd415a588b9baa2b8c65cf01f30/src/modules/windows-ambient-sensor/index.js)
- [src/modules/windows-hdr/index.js](https://github.com/xanderfrangos/twinkle-tray/blob/f4b36e12e2dbedd415a588b9baa2b8c65cf01f30/src/modules/windows-hdr/index.js)
- [src/modules/wmi-bridge/index.js](https://github.com/xanderfrangos/twinkle-tray/blob/f4b36e12e2dbedd415a588b9baa2b8c65cf01f30/src/modules/wmi-bridge/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| components package | library | Observed | Groups 16 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 52 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 1 file(s) under hooks package (observed from repository paths and static analysis). |
| intro.js package | library | Observed | Groups 1 file(s) under intro.js package (observed from repository paths and static analysis). |
| intro-preload.js package | library | Observed | Groups 1 file(s) under intro-preload.js package (observed from repository paths and static analysis). |
| light-sensor package | library | Observed | Groups 5 file(s) under light-sensor package (observed from repository paths and static analysis). |
| Logger.js package | library | Observed | Groups 1 file(s) under logger.js package (observed from repository paths and static analysis). |
| modules package | library | Observed | Groups 23 file(s) under modules package (observed from repository paths and static analysis). |
| Monitors.js package | library | Observed | Groups 1 file(s) under monitors.js package (observed from repository paths and static analysis). |
| panel.js package | library | Observed | Groups 1 file(s) under panel.js package (observed from repository paths and static analysis). |
| panel-preload.js package | library | Observed | Groups 1 file(s) under panel-preload.js package (observed from repository paths and static analysis). |
| parcel.js package | library | Observed | Groups 1 file(s) under parcel.js package (observed from repository paths and static analysis). |
| parcelAPI.js package | library | Observed | Groups 1 file(s) under parcelapi.js package (observed from repository paths and static analysis). |
| resources package | library | Observed | Groups 1 file(s) under resources package (observed from repository paths and static analysis). |
| settings.js package | library | Observed | Groups 1 file(s) under settings.js package (observed from repository paths and static analysis). |
| settings-preload.js package | library | Observed | Groups 1 file(s) under settings-preload.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). |
| Translate.js package | library | Observed | Groups 1 file(s) under translate.js package (observed from repository paths and static analysis). |
| TranslateReact.js package | library | Observed | Groups 1 file(s) under translatereact.js package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 1 file(s) under utils package (observed from repository paths and static analysis). |
| Utils.js package | library | Observed | Groups 1 file(s) under utils.js package (observed from repository paths and static analysis). |
| vcp-codes.js package | library | Observed | Groups 1 file(s) under vcp-codes.js package (observed from repository paths and static analysis). |
| volume-utils.js package | library | Observed | Groups 1 file(s) under volume-utils.js package (observed from repository paths and static analysis). |
| wmi-bridge-test.js package | library | Observed | Groups 1 file(s) under wmi-bridge-test.js package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.vscode/settings.json` (config)
- `package.json` (manifest)
- `src/localization/ar.json` (config)
- `src/localization/az.json` (config)
- `src/localization/bn.json` (config)
- `src/localization/ckb.json` (config)
- `src/localization/cs.json` (config)
- `src/localization/de.json` (config)
- `src/localization/el.json` (config)
- `src/localization/en-GB.json` (config)
- `src/localization/en.json` (config)
- `src/localization/es.json` (config)
- `src/localization/fa.json` (config)
- `src/localization/fi.json` (config)
- `src/localization/fr.json` (config)
- `src/localization/he.json` (config)
- `src/localization/hi.json` (config)
- `src/localization/hr.json` (config)
- `src/localization/hu.json` (config)
- `src/localization/id.json` (config)
- `src/localization/it.json` (config)
- `src/localization/ja.json` (config)
- `src/localization/ko.json` (config)
- `src/localization/lt.json` (config)
- `src/localization/nb.json` (config)
- `src/localization/nl.json` (config)
- `src/localization/pl.json` (config)
- `src/localization/pt-BR.json` (config)
- `src/localization/pt.json` (config)
- `src/localization/ro.json` (config)
- `src/localization/ru.json` (config)
- `src/localization/sk.json` (config)
- `src/localization/sv.json` (config)
- `src/localization/ta.json` (config)
- `src/localization/th.json` (config)
- `src/localization/tr.json` (config)
- `src/localization/uk.json` (config)
- `src/localization/vi.json` (config)
- `src/localization/zh-Hant.json` (config)
- `src/localization/zh_Hans.json` (config)
- `src/modules/acrylic/package.json` (manifest)
- `src/modules/node-active-window/.eslintrc.json` (config)
- `src/modules/node-active-window/.prettierrc.json` (config)
- `src/modules/node-active-window/package.json` (manifest)
- `src/modules/node-active-window/tsconfig.build.json` (config)
- `src/modules/node-active-window/tsconfig.json` (config)
- `src/modules/node-ddcci/package.json` (manifest)
- `src/modules/tt-windows-utils/package.json` (manifest)
- `src/modules/win32-displayconfig/package.json` (manifest)
- `src/modules/windows-ambient-sensor/package.json` (manifest)
- `src/modules/windows-hdr/package.json` (manifest)
- `src/modules/wmi-bridge/package.json` (manifest)
- `src/monitor-rules.json` (config)

## Top-level layout

- `src` — 163 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `resources` — 3 analysed file(s)
- `.github` — 2 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `tests` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 7 file(s) were skipped during inventory (3 x lockfile excluded; 4 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `f4b36e12e2dbedd415a588b9baa2b8c65cf01f30` is the revision these paths and observations refer to.
