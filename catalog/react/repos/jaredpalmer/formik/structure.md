# Project structure: jaredpalmer/formik

**Analysed commit:** `91475adbf33579561e580eceea0c031f4ec2e992`

**Commit reference:** [91475adbf33579561e580eceea0c031f4ec2e992](https://github.com/jaredpalmer/formik/commit/91475adbf33579561e580eceea0c031f4ec2e992)

**Tree at this commit:** [jaredpalmer/formik@91475adbf335](https://github.com/jaredpalmer/formik/tree/91475adbf33579561e580eceea0c031f4ec2e992)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | jaredpalmer/formik |
| Description | Build forms in React, without the tears 😭  |
| Stars | 34299 |
| Forks | 2769 |
| Licence | Apache-2.0 |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `91475adbf33579561e580eceea0c031f4ec2e992` |
| Retrieved at | 2026-11-14T19:13:01.684583+00:00 |
| Files in this snapshot | 290 |

## Directory tree

```text
.changeset/  (2 files)
  README.md
  config.json
.codesandbox/  (1 files)
  ci.json
.github/  (10 files)
  ISSUE_TEMPLATE/  (3 files)
    1.Bug-report.md
    2.Feature-request.md
    config.yml
  workflows/  (3 files)
    ci.yml
    release.yml
    stale.yml
  CODEOWNERS
  CODE_OF_CONDUCT.md
  CONTRIBUTING.md
  FUNDING.yml
.vscode/  (1 files)
  settings.json
app/  (10 files)
  pages/  (4 files)
    _app.js
    basic.js
    index.tsx
    sign-in.js
  styles/  (1 files)
    globals.css
  .gitignore
  README.md
  next-env.d.ts
  package.json
  tsconfig.json
docs/  (35 files)
  api/  (12 files)
    connect.md
    errormessage.md
    fastfield.md
    field.md
    fieldarray.md
    form.md
    formik.md
    useField.md
    useFormik.md
    useFormikContext.md
    utils.md
    withFormik.md
  examples/  (11 files)
    async-submission.md
    basic.md
    checkboxes.md
    dependent-fields-async-api-request.md
    dependent-fields.md
    field-arrays.md
    instant-feedback.md
    more-examples.md
    radio-group.md
    typescript.md
    with-material-ui.md
  guides/  (5 files)
    arrays.md
    form-submission.md
    react-native.md
    typescript.md
    validation.md
  3rd-party-bindings.md
  examples.md
  manifest.json
  migrating-v2.md
  overview.md
  resources.md
  tutorial.md
e2e/  (1 files)
  basic.test.ts
examples/  (52 files)
  async-submission/  (3 files)
    README.md
    index.js
    package.json
  basic/  (3 files)
    README.md
    index.js
    package.json
  basic-typescript/  (5 files)
    README.md
    index.html
    index.tsx
    package.json
    tsconfig.json
  checkboxes/  (3 files)
    README.md
    index.js
    package.json
  dependent-fields/  (4 files)
    README.md
    index.js
    package.json
    styles.css
  dependent-fields-async-api-request/  (4 files)
    README.md
    index.js
    package.json
    styles.css
  field-arrays/  (3 files)
    README.md
    index.js
    package.json
  field-level-validation/  (3 files)
    README.md
    index.js
    package.json
  instant-feedback/  (4 files)
    README.md
    index.js
    package.json
    styles.css
  radio-group/  (3 files)
    README.md
    index.js
    package.json
  with-material-ui/  (3 files)
    README.md
    index.js
    package.json
  AsyncValidation.js
  CombinedValidations.js
  CustomInputs.js
  DebouncedAutoSave.js
  Debug.js
  ErrorMessage.js
  FastField.js
  MultistepWizard.js
  RoutedMultistepWizard.js
  RoutedMultistepWizard2.js
  SchemaValidation.js
  SyncValidation.js
  ValidateFieldWithSchema.js
  withFormik.js
packages/  (39 files)
  formik/  (31 files)
    src/  (12 files)
      … 12 files under this directory
    test/  (11 files)
      … 11 files under this directory
    types/  (2 files)
      … 2 files under this directory
    .gitignore
    CHANGELOG.md
    MIGRATING-v2.md
    README.md
    package.json
    tsconfig.build.json
  formik-native/  (8 files)
    src/  (1 files)
      … 1 files under this directory
    test/  (1 files)
      … 1 files under this directory
    .gitignore
    CHANGELOG.md
    CONTRIBUTING.md
    README.md
    package.json
    tsconfig.build.json
scripts/  (3 files)
  benchmark.tsx
  btag.sh
  retag.sh
website/  (123 files)
  public/  (42 files)
    images/  (37 files)
      … 37 files under this directory
    twemoji/  (4 files)
      … 4 files under this directory
    robots.txt
  scripts/  (1 files)
    build-sitemap.js
  src/  (69 files)
    blog/  (2 files)
      … 2 files under this directory
    components/  (37 files)
      … 37 files under this directory
    lib/  (15 files)
      … 15 files under this directory
    manifests/  (4 files)
      … 4 files under this directory
    pages/  (7 files)
      … 7 files under this directory
    styles/  (1 files)
      … 1 files under this directory
    index.d.ts
    siteConfig.tsx
    users.ts
  .eslintignore
  .eslintrc
  .gitignore
  .prettierignore
  README.md
  next-env.d.ts
  next.config.js
  package.json
  postcss.config.js
  tailwind.config.js
  tsconfig.json
.all-contributorsrc
.eslintrc.js
.gitignore
.kodiak.toml
.nvmrc
.prettierrc
LICENSE
SECURITY.md
package.json
playwright.config.ts
tsconfig.base.json
tsconfig.json
turbo.json
```

## Entry points

- [examples/async-submission/index.js](https://github.com/jaredpalmer/formik/blob/91475adbf33579561e580eceea0c031f4ec2e992/examples/async-submission/index.js)
- [examples/basic-typescript/index.tsx](https://github.com/jaredpalmer/formik/blob/91475adbf33579561e580eceea0c031f4ec2e992/examples/basic-typescript/index.tsx)
- [examples/basic/index.js](https://github.com/jaredpalmer/formik/blob/91475adbf33579561e580eceea0c031f4ec2e992/examples/basic/index.js)
- [examples/checkboxes/index.js](https://github.com/jaredpalmer/formik/blob/91475adbf33579561e580eceea0c031f4ec2e992/examples/checkboxes/index.js)
- [examples/dependent-fields-async-api-request/index.js](https://github.com/jaredpalmer/formik/blob/91475adbf33579561e580eceea0c031f4ec2e992/examples/dependent-fields-async-api-request/index.js)
- [examples/dependent-fields/index.js](https://github.com/jaredpalmer/formik/blob/91475adbf33579561e580eceea0c031f4ec2e992/examples/dependent-fields/index.js)
- [examples/field-arrays/index.js](https://github.com/jaredpalmer/formik/blob/91475adbf33579561e580eceea0c031f4ec2e992/examples/field-arrays/index.js)
- [examples/field-level-validation/index.js](https://github.com/jaredpalmer/formik/blob/91475adbf33579561e580eceea0c031f4ec2e992/examples/field-level-validation/index.js)
- [examples/instant-feedback/index.js](https://github.com/jaredpalmer/formik/blob/91475adbf33579561e580eceea0c031f4ec2e992/examples/instant-feedback/index.js)
- [examples/radio-group/index.js](https://github.com/jaredpalmer/formik/blob/91475adbf33579561e580eceea0c031f4ec2e992/examples/radio-group/index.js)
- [examples/with-material-ui/index.js](https://github.com/jaredpalmer/formik/blob/91475adbf33579561e580eceea0c031f4ec2e992/examples/with-material-ui/index.js)
- [app/pages/index.tsx](https://github.com/jaredpalmer/formik/blob/91475adbf33579561e580eceea0c031f4ec2e992/app/pages/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| app package | library | Observed | Groups 5 file(s) under app package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 15 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| e2e package | library | Observed | Groups 1 file(s) under e2e package (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 3 file(s) under external integrations (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 15 file(s) under packages package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 3 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 12 file(s) under tests (observed from repository paths and static analysis). |
| website package | library | Observed | Groups 54 file(s) under website package (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.codesandbox/ci.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/stale.yml` (ci)
- `.kodiak.toml` (config)
- `.vscode/settings.json` (config)
- `app/package.json` (manifest)
- `app/tsconfig.json` (config)
- `docs/manifest.json` (config)
- `examples/async-submission/package.json` (manifest)
- `examples/basic-typescript/package.json` (manifest)
- `examples/basic-typescript/tsconfig.json` (config)
- `examples/basic/package.json` (manifest)
- `examples/checkboxes/package.json` (manifest)
- `examples/dependent-fields-async-api-request/package.json` (manifest)
- `examples/dependent-fields/package.json` (manifest)
- `examples/field-arrays/package.json` (manifest)
- `examples/field-level-validation/package.json` (manifest)
- `examples/instant-feedback/package.json` (manifest)
- `examples/radio-group/package.json` (manifest)
- `examples/with-material-ui/package.json` (manifest)
- `package.json` (manifest)
- `packages/formik-native/package.json` (manifest)
- `packages/formik-native/tsconfig.build.json` (config)
- `packages/formik/package.json` (manifest)
- `packages/formik/tsconfig.build.json` (config)
- `tsconfig.base.json` (config)
- `tsconfig.json` (config)
- `turbo.json` (config)
- `website/package.json` (manifest)
- `website/src/manifests/manifest-1.3.0.json` (config)
- `website/src/manifests/manifest-2.1.4.json` (config)
- `website/src/manifests/manifest.json` (config)
- `website/tsconfig.json` (config)

## Top-level layout

- `website` — 123 analysed file(s)
- `examples` — 52 analysed file(s)
- `packages` — 39 analysed file(s)
- `docs` — 35 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `.github` — 10 analysed file(s)
- `app` — 10 analysed file(s)
- `scripts` — 3 analysed file(s)
- `.changeset` — 2 analysed file(s)
- `.codesandbox` — 1 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `e2e` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `91475adbf33579561e580eceea0c031f4ec2e992` is the revision these paths and observations refer to.
