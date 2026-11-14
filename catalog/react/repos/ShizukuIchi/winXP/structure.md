# Project structure: ShizukuIchi/winXP

**Analysed commit:** `856bb554b3667f62078010b4cee10cc2645761e1`

**Commit reference:** [856bb554b3667f62078010b4cee10cc2645761e1](https://github.com/ShizukuIchi/winXP/commit/856bb554b3667f62078010b4cee10cc2645761e1)

**Tree at this commit:** [ShizukuIchi/winXP@856bb554b366](https://github.com/ShizukuIchi/winXP/tree/856bb554b3667f62078010b4cee10cc2645761e1)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | ShizukuIchi/winXP |
| Description | 🏁 Web based Windows XP desktop recreation.  |
| Stars | 5865 |
| Forks | 475 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `856bb554b3667f62078010b4cee10cc2645761e1` |
| Retrieved at | 2026-11-14T19:14:14.203392+00:00 |
| Files in this snapshot | 55 |

## Directory tree

```text
public/  (2 files)
  index.html
  manifest.json
src/  (46 files)
  WinXP/  (25 files)
    Footer/  (3 files)
      … 3 files under this directory
    Icons/  (1 files)
      … 1 files under this directory
    Modal/  (1 files)
      … 1 files under this directory
    Windows/  (2 files)
      … 2 files under this directory
    apps/  (15 files)
      … 15 files under this directory
    constants/  (2 files)
      … 2 files under this directory
    index.js
  assets/  (3 files)
    windowsIcons/  (1 files)
      … 1 files under this directory
    clear.css
    font.css
  components/  (11 files)
    Balloon/  (1 files)
      … 1 files under this directory
    DashedBox/  (1 files)
      … 1 files under this directory
    Google/  (5 files)
      … 5 files under this directory
    SubMenu/  (1 files)
      … 1 files under this directory
    WindowDropDowns/  (2 files)
      … 2 files under this directory
    index.js
  hooks/  (3 files)
    index.js
    useElementResize.js
    useGA.js
  App.js
  index.css
  index.js
  serviceWorker.js
.gitignore
.prettierrc
LICENSE
README.md
jsconfig.json
now.json
package.json
```

## Entry points

- [src/App.js](https://github.com/ShizukuIchi/winXP/blob/856bb554b3667f62078010b4cee10cc2645761e1/src/App.js)
- [src/WinXP/Footer/index.js](https://github.com/ShizukuIchi/winXP/blob/856bb554b3667f62078010b4cee10cc2645761e1/src/WinXP/Footer/index.js)
- [src/WinXP/Icons/index.js](https://github.com/ShizukuIchi/winXP/blob/856bb554b3667f62078010b4cee10cc2645761e1/src/WinXP/Icons/index.js)
- [src/WinXP/Modal/index.js](https://github.com/ShizukuIchi/winXP/blob/856bb554b3667f62078010b4cee10cc2645761e1/src/WinXP/Modal/index.js)
- [src/WinXP/Windows/index.js](https://github.com/ShizukuIchi/winXP/blob/856bb554b3667f62078010b4cee10cc2645761e1/src/WinXP/Windows/index.js)
- [src/WinXP/apps/index.js](https://github.com/ShizukuIchi/winXP/blob/856bb554b3667f62078010b4cee10cc2645761e1/src/WinXP/apps/index.js)
- [src/WinXP/constants/index.js](https://github.com/ShizukuIchi/winXP/blob/856bb554b3667f62078010b4cee10cc2645761e1/src/WinXP/constants/index.js)
- [src/WinXP/index.js](https://github.com/ShizukuIchi/winXP/blob/856bb554b3667f62078010b4cee10cc2645761e1/src/WinXP/index.js)
- [src/components/Balloon/index.js](https://github.com/ShizukuIchi/winXP/blob/856bb554b3667f62078010b4cee10cc2645761e1/src/components/Balloon/index.js)
- [src/components/DashedBox/index.js](https://github.com/ShizukuIchi/winXP/blob/856bb554b3667f62078010b4cee10cc2645761e1/src/components/DashedBox/index.js)
- [src/components/Google/Main.js](https://github.com/ShizukuIchi/winXP/blob/856bb554b3667f62078010b4cee10cc2645761e1/src/components/Google/Main.js)
- [src/components/Google/index.js](https://github.com/ShizukuIchi/winXP/blob/856bb554b3667f62078010b4cee10cc2645761e1/src/components/Google/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| App.js package | library | Observed | Groups 1 file(s) under app.js package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 9 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 3 file(s) under hooks package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| serviceWorker.js package | library | Observed | Groups 1 file(s) under serviceworker.js package (observed from repository paths and static analysis). |
| WinXP package | library | Observed | Groups 25 file(s) under winxp package (observed from repository paths and static analysis). |

## Important files

- `jsconfig.json` (config)
- `now.json` (config)
- `package.json` (manifest)
- `public/manifest.json` (config)

## Top-level layout

- `src` — 46 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `public` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `856bb554b3667f62078010b4cee10cc2645761e1` is the revision these paths and observations refer to.
