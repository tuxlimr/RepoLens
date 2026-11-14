# Project structure: vivek9patel/vivek9patel.github.io

**Analysed commit:** `df42a171d42789a576de91cf83fc48b85dbfbc00`

**Commit reference:** [df42a171d42789a576de91cf83fc48b85dbfbc00](https://github.com/vivek9patel/vivek9patel.github.io/commit/df42a171d42789a576de91cf83fc48b85dbfbc00)

**Tree at this commit:** [vivek9patel/vivek9patel.github.io@df42a171d427](https://github.com/vivek9patel/vivek9patel.github.io/tree/df42a171d42789a576de91cf83fc48b85dbfbc00)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | vivek9patel/vivek9patel.github.io |
| Description | Web simulation of Ubuntu 20.04, made using NEXT.js & tailwind CSS |
| Stars | 4325 |
| Forks | 696 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `df42a171d42789a576de91cf83fc48b85dbfbc00` |
| Retrieved at | 2026-11-14T19:14:49.327955+00:00 |
| Files in this snapshot | 76 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (1 files)
    gh-deploy.yml
  FUNDING.yml
.vscode/  (1 files)
  settings.json
components/  (28 files)
  SEO/  (1 files)
    Meta.js
  apps/  (10 files)
    calc.js
    chrome.js
    gedit.js
    settings.js
    spotify.js
    terminal.js
    todoist.js
    trash.js
    vivek.js
    vscode.js
  base/  (3 files)
    side_bar_app.js
    ubuntu_app.js
    window.js
  context menus/  (2 files)
    default.js
    desktop-menu.js
  screen/  (6 files)
    all-applications.js
    booting_screen.js
    desktop.js
    lock_screen.js
    navbar.js
    side_bar.js
  util components/  (5 files)
    background-image.js
    clock.js
    small_arrow.js
    status.js
    status_card.js
  ubuntu.js
pages/  (3 files)
  _app.js
  _document.js
  index.js
public/  (33 files)
  images/  (1 files)
    logos/  (1 files)
      … 1 files under this directory
  themes/  (31 files)
    Yaru/  (31 files)
      … 31 files under this directory
  robots.txt
styles/  (1 files)
  index.css
.gitattributes
.gitignore
LICENSE
README.md
apps.config.js
package.json
postcss.config.js
tailwind.config.js
```

## Entry points

- [pages/index.js](https://github.com/vivek9patel/vivek9patel.github.io/blob/df42a171d42789a576de91cf83fc48b85dbfbc00/pages/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| components package | library | Observed | Groups 28 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| pages package | library | Observed | Groups 3 file(s) under pages package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/workflows/gh-deploy.yml` (ci)
- `.vscode/settings.json` (config)
- `package.json` (manifest)

## Top-level layout

- `public` — 33 analysed file(s)
- `components` — 28 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `pages` — 3 analysed file(s)
- `.github` — 2 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `styles` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `df42a171d42789a576de91cf83fc48b85dbfbc00` is the revision these paths and observations refer to.
