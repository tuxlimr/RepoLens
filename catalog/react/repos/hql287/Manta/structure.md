# Project structure: hql287/Manta

**Analysed commit:** `c530133998a99dae1010931055c52906ae410a9e`

**Commit reference:** [c530133998a99dae1010931055c52906ae410a9e](https://github.com/hql287/Manta/commit/c530133998a99dae1010931055c52906ae410a9e)

**Tree at this commit:** [hql287/Manta@c530133998a9](https://github.com/hql287/Manta/tree/c530133998a99dae1010931055c52906ae410a9e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | hql287/Manta |
| Description | 🎉 Flexible invoicing desktop app with beautiful & customizable templates. |
| Stars | 5488 |
| Forks | 481 |
| Licence | LGPL-3.0 |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `c530133998a99dae1010931055c52906ae410a9e` |
| Retrieved at | 2026-11-14T19:14:18.926794+00:00 |
| Files in this snapshot | 342 |

## Directory tree

```text
.github/  (5 files)
  CODE_OF_CONDUCT.md
  CONTRIBUTING.md
  FUNDING.yml
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
__mocks__/  (4 files)
  uuid/  (1 files)
    v4.js
  electron-settings.js
  electron.js
  pouchdb-browser.js
app/  (147 files)
  actions/  (10 files)
    __tests__/  (5 files)
      … 5 files under this directory
    contacts.jsx
    form.jsx
    invoices.jsx
    settings.jsx
    ui.jsx
  components/  (86 files)
    contacts/  (3 files)
      … 3 files under this directory
    form/  (44 files)
      … 44 files under this directory
    invoices/  (3 files)
      … 3 files under this directory
    layout/  (6 files)
      … 6 files under this directory
    settings/  (10 files)
      … 10 files under this directory
    shared/  (20 files)
      … 20 files under this directory
  constants/  (2 files)
    ItemTypes.jsx
    actions.jsx
  containers/  (9 files)
    __tests__/  (5 files)
      … 5 files under this directory
    Contacts.jsx
    Form.jsx
    Invoices.jsx
    Settings.jsx
  helpers/  (9 files)
    __mocks__/  (3 files)
      … 3 files under this directory
    __tests__/  (2 files)
      … 2 files under this directory
    form.js
    image.js
    invoice.js
    pouchDB.js
  middlewares/  (11 files)
    __tests__/  (5 files)
      … 5 files under this directory
    ContactsMW.jsx
    FormMW.jsx
    InvoicesMW.jsx
    MeasureMW.jsx
    SettingsMW.jsx
    UIMiddleware.jsx
  reducers/  (11 files)
    __tests__/  (5 files)
      … 5 files under this directory
    ContactsReducer.jsx
    FormReducer.jsx
    InvoicesReducer.jsx
    SettingsReducer.jsx
    UIReducer.jsx
    index.jsx
  renderers/  (4 files)
    __mocks__/  (1 files)
      … 1 files under this directory
    dialog.js
    menu.js
    startup.js
  store/  (2 files)
    enhancer.jsx
    index.jsx
  App.jsx
  index.html
  index.jsx
helpers/  (5 files)
  __tests__/  (1 files)
    formatNumber.spec.js
  center-on-primary-display.js
  date.js
  formatNumber.js
  notify.js
i18n/  (91 files)
  de/  (10 files)
    common.json
    contacts.json
    dialog.json
    form.json
    index.js
    invoices.json
    messages.json
    preview.json
    settings.json
    tour.json
  en/  (10 files)
    common.json
    contacts.json
    dialog.json
    form.json
    index.js
    invoices.json
    messages.json
    preview.json
    settings.json
    tour.json
  fr/  (10 files)
    common.json
    contacts.json
    dialog.json
    form.json
    index.js
    invoices.json
    messages.json
    preview.json
    settings.json
    tour.json
  id/  (10 files)
    common.json
    contacts.json
    dialog.json
    form.json
    index.js
    invoices.json
    messages.json
    preview.json
    settings.json
    tour.json
  it/  (10 files)
    common.json
    contacts.json
    dialog.json
    form.json
    index.js
    invoices.json
    messages.json
    preview.json
    settings.json
    tour.json
  sk/  (10 files)
    common.json
    contacts.json
    dialog.json
    form.json
    index.js
    invoices.json
    messages.json
    preview.json
    settings.json
    tour.json
  ur-PK/  (10 files)
    common.json
    contacts.json
    dialog.json
    form.json
    index.js
    invoices.json
    messages.json
    preview.json
    settings.json
    tour.json
  vi/  (10 files)
    common.json
    contacts.json
    dialog.json
    form.json
    index.js
    invoices.json
    messages.json
    preview.json
    settings.json
    tour.json
  zh-CN/  (10 files)
    common.json
    contacts.json
    dialog.json
    form.json
    index.js
    invoices.json
    messages.json
    preview.json
    settings.json
    tour.json
  i18n.js
libs/  (6 files)
  __mocks__/  (1 files)
    sounds.js
  __tests__/  (1 files)
    sounds.spec.js
  currencies.json
  dragNdrop.js
  paymentTerms.js
  sounds.js
main/  (6 files)
  preview-window.js
  save-pdf.js
  select-export-directory.js
  select-logo-file.js
  tour.js
  updater.js
modal/  (3 files)
  Dialog.jsx
  index.html
  index.jsx
preview/  (30 files)
  actions/  (2 files)
    __test__/  (1 files)
      … 1 files under this directory
    index.jsx
  components/  (10 files)
    shared/  (1 files)
      … 1 files under this directory
    sidebar/  (9 files)
      … 9 files under this directory
  constants/  (1 files)
    actions.jsx
  containers/  (2 files)
    MainContent.jsx
    SideBar.jsx
  helper/  (1 files)
    index.js
  reducers/  (2 files)
    __test__/  (1 files)
      … 1 files under this directory
    index.jsx
  templates/  (9 files)
    business/  (5 files)
      … 5 files under this directory
    minimal/  (4 files)
      … 4 files under this directory
  Viewer.jsx
  index.html
  index.jsx
static/  (11 files)
  css/  (8 files)
    preview/  (2 files)
      … 2 files under this directory
    contact.css
    date-picker.css
    form.css
    general.css
    items.css
    layout.css
  imgs/  (1 files)
    default_logo.svg
  sounds/  (2 files)
    cs/  (1 files)
      … 1 files under this directory
    default/  (1 files)
      … 1 files under this directory
test/  (2 files)
  helper.js
  spec.js
tour/  (17 files)
  components/  (7 files)
    slides/  (5 files)
      … 5 files under this directory
    Actions.jsx
    Slide.jsx
  containers/  (1 files)
    Slider.jsx
  imgs/  (6 files)
    Create.svg
    Preview.svg
    Save.svg
    Success.svg
    Templates.svg
    Welcome.svg
  Tour.jsx
  index.html
  index.jsx
.babelrc
.eslintrc.yml
.gitignore
.travis.yml
LICENSE
README.md
app.js
dev-app-update.yml
electron-builder.yml
jest.config.js
jest.setup.js
jest.shim.js
package.json
webpack.config.js
webpack.parts.js
```

## Entry points

- [app.js](https://github.com/hql287/Manta/blob/c530133998a99dae1010931055c52906ae410a9e/app.js)
- [app/App.jsx](https://github.com/hql287/Manta/blob/c530133998a99dae1010931055c52906ae410a9e/app/App.jsx)
- [app/index.jsx](https://github.com/hql287/Manta/blob/c530133998a99dae1010931055c52906ae410a9e/app/index.jsx)
- [app/reducers/index.jsx](https://github.com/hql287/Manta/blob/c530133998a99dae1010931055c52906ae410a9e/app/reducers/index.jsx)
- [app/store/index.jsx](https://github.com/hql287/Manta/blob/c530133998a99dae1010931055c52906ae410a9e/app/store/index.jsx)
- [i18n/de/index.js](https://github.com/hql287/Manta/blob/c530133998a99dae1010931055c52906ae410a9e/i18n/de/index.js)
- [i18n/en/index.js](https://github.com/hql287/Manta/blob/c530133998a99dae1010931055c52906ae410a9e/i18n/en/index.js)
- [i18n/fr/index.js](https://github.com/hql287/Manta/blob/c530133998a99dae1010931055c52906ae410a9e/i18n/fr/index.js)
- [i18n/id/index.js](https://github.com/hql287/Manta/blob/c530133998a99dae1010931055c52906ae410a9e/i18n/id/index.js)
- [i18n/it/index.js](https://github.com/hql287/Manta/blob/c530133998a99dae1010931055c52906ae410a9e/i18n/it/index.js)
- [i18n/sk/index.js](https://github.com/hql287/Manta/blob/c530133998a99dae1010931055c52906ae410a9e/i18n/sk/index.js)
- [i18n/ur-PK/index.js](https://github.com/hql287/Manta/blob/c530133998a99dae1010931055c52906ae410a9e/i18n/ur-PK/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| app package | library | Observed | Groups 119 file(s) under app package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 95 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 6 file(s) under core modules (observed from repository paths and static analysis). |
| helpers package | library | Observed | Groups 5 file(s) under helpers package (observed from repository paths and static analysis). |
| i18n package | library | Observed | Groups 10 file(s) under i18n package (observed from repository paths and static analysis). |
| libs package | library | Observed | Groups 5 file(s) under libs package (observed from repository paths and static analysis). |
| main package | library | Observed | Groups 6 file(s) under main package (observed from repository paths and static analysis). |
| __mocks__ package | library | Observed | Groups 4 file(s) under __mocks__ package (observed from repository paths and static analysis). |
| modal package | library | Observed | Groups 2 file(s) under modal package (observed from repository paths and static analysis). |
| preview package | library | Observed | Groups 24 file(s) under preview package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 5 file(s) under service / domain layer (observed from repository paths and static analysis). |
| static package | library | Observed | Groups 2 file(s) under static package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 2 file(s) under tests (observed from repository paths and static analysis). |
| tour package | library | Observed | Groups 10 file(s) under tour package (observed from repository paths and static analysis). |

## Important files

- `.eslintrc.yml` (config)
- `.github/FUNDING.yml` (config)
- `.travis.yml` (ci)
- `dev-app-update.yml` (config)
- `electron-builder.yml` (config)
- `i18n/de/common.json` (config)
- `i18n/de/contacts.json` (config)
- `i18n/de/dialog.json` (config)
- `i18n/de/form.json` (config)
- `i18n/de/invoices.json` (config)
- `i18n/de/messages.json` (config)
- `i18n/de/preview.json` (config)
- `i18n/de/settings.json` (config)
- `i18n/de/tour.json` (config)
- `i18n/en/common.json` (config)
- `i18n/en/contacts.json` (config)
- `i18n/en/dialog.json` (config)
- `i18n/en/form.json` (config)
- `i18n/en/invoices.json` (config)
- `i18n/en/messages.json` (config)
- `i18n/en/preview.json` (config)
- `i18n/en/settings.json` (config)
- `i18n/en/tour.json` (config)
- `i18n/fr/common.json` (config)
- `i18n/fr/contacts.json` (config)
- `i18n/fr/dialog.json` (config)
- `i18n/fr/form.json` (config)
- `i18n/fr/invoices.json` (config)
- `i18n/fr/messages.json` (config)
- `i18n/fr/preview.json` (config)
- `i18n/fr/settings.json` (config)
- `i18n/fr/tour.json` (config)
- `i18n/id/common.json` (config)
- `i18n/id/contacts.json` (config)
- `i18n/id/dialog.json` (config)
- `i18n/id/form.json` (config)
- `i18n/id/invoices.json` (config)
- `i18n/id/messages.json` (config)
- `i18n/id/preview.json` (config)
- `i18n/id/settings.json` (config)
- `i18n/id/tour.json` (config)
- `i18n/it/common.json` (config)
- `i18n/it/contacts.json` (config)
- `i18n/it/dialog.json` (config)
- `i18n/it/form.json` (config)
- `i18n/it/invoices.json` (config)
- `i18n/it/messages.json` (config)
- `i18n/it/preview.json` (config)
- `i18n/it/settings.json` (config)
- `i18n/it/tour.json` (config)
- `i18n/sk/common.json` (config)
- `i18n/sk/contacts.json` (config)
- `i18n/sk/dialog.json` (config)
- `i18n/sk/form.json` (config)
- `i18n/sk/invoices.json` (config)
- `i18n/sk/messages.json` (config)
- `i18n/sk/preview.json` (config)
- `i18n/sk/settings.json` (config)
- `i18n/sk/tour.json` (config)
- `i18n/ur-PK/common.json` (config)
- `i18n/ur-PK/contacts.json` (config)
- `i18n/ur-PK/dialog.json` (config)
- `i18n/ur-PK/form.json` (config)
- `i18n/ur-PK/invoices.json` (config)
- `i18n/ur-PK/messages.json` (config)
- `i18n/ur-PK/preview.json` (config)
- `i18n/ur-PK/settings.json` (config)
- `i18n/ur-PK/tour.json` (config)
- `i18n/vi/common.json` (config)
- `i18n/vi/contacts.json` (config)
- `i18n/vi/dialog.json` (config)
- `i18n/vi/form.json` (config)
- `i18n/vi/invoices.json` (config)
- `i18n/vi/messages.json` (config)
- `i18n/vi/preview.json` (config)
- `i18n/vi/settings.json` (config)
- `i18n/vi/tour.json` (config)
- `i18n/zh-CN/common.json` (config)
- `i18n/zh-CN/contacts.json` (config)
- `i18n/zh-CN/dialog.json` (config)
- `i18n/zh-CN/form.json` (config)
- `i18n/zh-CN/invoices.json` (config)
- `i18n/zh-CN/messages.json` (config)
- `i18n/zh-CN/preview.json` (config)
- `i18n/zh-CN/settings.json` (config)
- `i18n/zh-CN/tour.json` (config)
- `libs/currencies.json` (config)
- `package.json` (manifest)

## Top-level layout

- `app` — 147 analysed file(s)
- `i18n` — 91 analysed file(s)
- `preview` — 30 analysed file(s)
- `tour` — 17 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `static` — 11 analysed file(s)
- `libs` — 6 analysed file(s)
- `main` — 6 analysed file(s)
- `.github` — 5 analysed file(s)
- `helpers` — 5 analysed file(s)
- `__mocks__` — 4 analysed file(s)
- `modal` — 3 analysed file(s)
- `test` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x generated/minified file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `c530133998a99dae1010931055c52906ae410a9e` is the revision these paths and observations refer to.
