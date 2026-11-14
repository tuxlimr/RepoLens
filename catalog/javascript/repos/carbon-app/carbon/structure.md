# Project structure: carbon-app/carbon

**Analysed commit:** `3e9efcc506bdccb6d3834f66f30f8e883f80e49d`

**Commit reference:** [3e9efcc506bdccb6d3834f66f30f8e883f80e49d](https://github.com/carbon-app/carbon/commit/3e9efcc506bdccb6d3834f66f30f8e883f80e49d)

**Tree at this commit:** [carbon-app/carbon@3e9efcc506bd](https://github.com/carbon-app/carbon/tree/3e9efcc506bdccb6d3834f66f30f8e883f80e49d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | carbon-app/carbon |
| Description | :black_heart: Create and share beautiful images of your source code |
| Stars | 36148 |
| Forks | 1973 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `3e9efcc506bdccb6d3834f66f30f8e883f80e49d` |
| Retrieved at | 2026-11-14T19:10:42.039410+00:00 |
| Files in this snapshot | 153 |

## Directory tree

```text
.github/  (10 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    feature_request.md
    other.md
  workflows/  (1 files)
    validate.yml
  CODE_OF_CONDUCT.md
  CONTRIBUTING.md
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
  ranger.yml
bin/  (1 files)
  deploy.sh
components/  (62 files)
  Themes/  (3 files)
    GlobalHighlights.js
    ThemeCreate.js
    index.js
  style/  (3 files)
    Font.js
    Reset.js
    Typography.js
  svg/  (11 files)
    Arrows.js
    Checkmark.js
    Controls.js
    Copy.js
    Language.js
    Logo.js
    Remove.js
    Settings.js
    Theme.js
    Watermark.js
    WindowThemes.js
  Announcement.js
  ApiContext.js
  AuthContext.js
  BackgroundSelect.js
  Billing.js
  Button.js
  Carbon.js
  ColorPicker.js
  ConfirmButton.js
  CopyMenu.js
  Dropdown.js
  Editor.js
  EditorContainer.js
  ExportMenu.js
  FontFace.js
  FontSelect.js
  Footer.js
  Header.js
  ImagePicker.js
  Input.js
  ListSetting.js
  LoginButton.js
  MenuButton.js
  Meta.js
  … 21 more files
cypress/  (11 files)
  integration/  (7 files)
    background-color.spec.js
    basic.spec.js
    embed.spec.js
    gist.spec.js
    localStorage.spec.js
    security.spec.js
    visual-testing.spec.js
  plugins/  (1 files)
    index.js
  support/  (1 files)
    index.js
  config.json
  util.js
docs/  (24 files)
  README.ar.md
  README.bn.md
  README.br.pt.md
  README.cn.zh.md
  README.de.md
  README.es.md
  README.fa.md
  README.fr.md
  README.he.md
  README.hi.md
  README.in.md
  README.it.md
  README.ja.md
  README.kr.md
  README.ml.md
  README.nl.md
  README.pl.md
  README.ru.md
  README.se.md
  README.ta.md
  README.tr.md
  README.tw.zh.md
  README.ua.md
  README.uz.md
lib/  (14 files)
  custom/  (7 files)
    modes/  (6 files)
      … 6 files under this directory
    autoCloseBrackets.js
  api.js
  client.js
  constants.js
  dom-to-image.js
  highlight-languages.js
  routing.js
  util.js
pages/  (10 files)
  api/  (2 files)
    image/  (1 files)
      … 1 files under this directory
    oembed.js
  embed/  (2 files)
    [id].js
    index.js
  [id].js
  _document.js
  about.js
  account.js
  index.js
  snippets.js
public/  (9 files)
  static/  (7 files)
    svg/  (6 files)
      … 6 files under this directory
    react-crop.css
  manifest.json
  robots.txt
.all-contributorsrc
.eslintrc.js
.gitignore
.prettierrc
.vercelignore
LICENSE
README.md
SECURITY.md
next.config.js
package.json
release.js
vercel.json
```

## Entry points

- [components/Page.js](https://github.com/carbon-app/carbon/blob/3e9efcc506bdccb6d3834f66f30f8e883f80e49d/components/Page.js)
- [components/Themes/index.js](https://github.com/carbon-app/carbon/blob/3e9efcc506bdccb6d3834f66f30f8e883f80e49d/components/Themes/index.js)
- [cypress/plugins/index.js](https://github.com/carbon-app/carbon/blob/3e9efcc506bdccb6d3834f66f30f8e883f80e49d/cypress/plugins/index.js)
- [cypress/support/index.js](https://github.com/carbon-app/carbon/blob/3e9efcc506bdccb6d3834f66f30f8e883f80e49d/cypress/support/index.js)
- [pages/embed/index.js](https://github.com/carbon-app/carbon/blob/3e9efcc506bdccb6d3834f66f30f8e883f80e49d/pages/embed/index.js)
- [pages/index.js](https://github.com/carbon-app/carbon/blob/3e9efcc506bdccb6d3834f66f30f8e883f80e49d/pages/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 2 file(s) under api layer (observed from repository paths and static analysis). |
| bin package | library | Observed | Groups 1 file(s) under bin package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 62 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| cypress package | library | Observed | Groups 3 file(s) under cypress package (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 7 file(s) under external integrations (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 14 file(s) under lib package (observed from repository paths and static analysis). |
| pages package | library | Observed | Groups 8 file(s) under pages package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/ranger.yml` (config)
- `.github/workflows/validate.yml` (ci)
- `cypress/config.json` (config)
- `package.json` (manifest)
- `public/manifest.json` (config)
- `vercel.json` (config)

## Top-level layout

- `components` — 62 analysed file(s)
- `docs` — 24 analysed file(s)
- `lib` — 14 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `cypress` — 11 analysed file(s)
- `.github` — 10 analysed file(s)
- `pages` — 10 analysed file(s)
- `public` — 9 analysed file(s)
- `bin` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 7 file(s) were skipped during inventory (6 x generated/minified file excluded; 1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `3e9efcc506bdccb6d3834f66f30f8e883f80e49d` is the revision these paths and observations refer to.
