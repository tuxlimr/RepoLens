# Project structure: text-mask/text-mask

**Analysed commit:** `120393e0de2c4c7742fb600ff8c5a72ddf3e58cf`

**Commit reference:** [120393e0de2c4c7742fb600ff8c5a72ddf3e58cf](https://github.com/text-mask/text-mask/commit/120393e0de2c4c7742fb600ff8c5a72ddf3e58cf)

**Tree at this commit:** [text-mask/text-mask@120393e0de2c](https://github.com/text-mask/text-mask/tree/120393e0de2c4c7742fb600ff8c5a72ddf3e58cf)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | text-mask/text-mask |
| Description | Input mask for React, Angular, Ember, Vue, & plain JavaScript |
| Stars | 8203 |
| Forks | 809 |
| Licence | Unlicense |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `120393e0de2c4c7742fb600ff8c5a72ddf3e58cf` |
| Retrieved at | 2026-11-14T19:13:42.213722+00:00 |
| Files in this snapshot | 181 |

## Directory tree

```text
addons/  (14 files)
  src/  (5 files)
    createAutoCorrectedDatePipe.js
    createNumberMask.js
    emailMask.js
    emailPipe.js
    index.js
  test/  (4 files)
    addonsBundle.spec.js
    createAutoCorrectedDatePipe.spec.js
    createNumberMask.spec.js
    emailMask.spec.js
  LICENSE
  README.md
  package.json
  publish.sh
  webpack.buildAddons.js
angular1/  (11 files)
  example/  (4 files)
    app.js
    demo.html
    index.html
    webpack.runAngular1Example.js
  src/  (1 files)
    angular1TextMask.js
  test/  (1 files)
    angular1TextMask.spec.js
  LICENSE
  README.md
  package.json
  publish.sh
  webpack.buildAngular1Integration.js
angular2/  (30 files)
  example/  (8 files)
    .gitignore
    app.component.ts
    app.html
    app.module.ts
    index.html
    main.ts
    systemjs.config.js
    tsconfig.json
  src/  (1 files)
    angular2TextMask.ts
  test/  (2 files)
    angular2TextMask.spec.ts
    index.spec.ts
  typings/  (7 files)
    globals/  (6 files)
      … 6 files under this directory
    index.d.ts
  .gitignore
  .npmignore
  LICENSE
  README.md
  bs-config.json
  karma.conf.js
  package.json
  publish.sh
  tsconfig.json
  tsconfig.test.json
  tslint.json
  typings.json
common/  (6 files)
  domSetup.js
  isVerify.js
  keepCharPositionsTests.js
  maskFunctionTests.js
  testParameters.js
  testSetup.js
core/  (16 files)
  src/  (7 files)
    adjustCaretPosition.js
    conformToMask.js
    constants.js
    createTextMaskInputElement.d.ts
    createTextMaskInputElement.js
    index.js
    utilities.js
  test/  (4 files)
    adjustCaretPosition.spec.js
    conformToMask.spec.js
    createTextMaskInputElement.spec.js
    utilities.spec.js
  LICENSE
  README.md
  package.json
  publish.sh
  webpack.buildCore.js
ember/  (45 files)
  addon/  (3 files)
    components/  (1 files)
      … 1 files under this directory
    .gitkeep
    index.js
  app/  (2 files)
    components/  (1 files)
      … 1 files under this directory
    .gitkeep
  config/  (2 files)
    ember-try.js
    environment.js
  tests/  (24 files)
    acceptance/  (1 files)
      … 1 files under this directory
    dummy/  (12 files)
      … 12 files under this directory
    helpers/  (4 files)
      … 4 files under this directory
    integration/  (2 files)
      … 2 files under this directory
    unit/  (2 files)
      … 2 files under this directory
    .eslintrc.js
    index.html
    test-helper.js
  .editorconfig
  .ember-cli
  .eslintrc.js
  .gitignore
  .npmignore
  .travis.yml
  .watchmanconfig
  LICENSE
  README.md
  ember-cli-build.js
  index.js
  package.json
  publish.sh
  testem.js
react/  (12 files)
  example/  (5 files)
    app.js
    index.html
    index.js
    server.js
    webpack.runReactExample.js
  src/  (1 files)
    reactTextMask.js
  test/  (1 files)
    reactTextMask.spec.js
  LICENSE
  README.md
  package.json
  publish.sh
  webpack.buildReactIntegration.js
vanilla/  (10 files)
  example/  (3 files)
    index.html
    index.js
    webpack.runVanillaExample.js
  src/  (1 files)
    vanillaTextMask.js
  test/  (1 files)
    vanillaTextMask.spec.js
  LICENSE
  README.md
  package.json
  publish.sh
  webpack.buildVanillaIntegration.js
vue/  (11 files)
  example/  (4 files)
    App.vue
    index.html
    index.js
    webpack.runVueExample.js
  src/  (1 files)
    vueTextMask.js
  test/  (1 files)
    vueTextMask.spec.js
  LICENSE
  README.md
  package.json
  publish.sh
  webpack.buildVueDirective.js
website/  (15 files)
  src/  (10 files)
    app.js
    app.scss
    choices.js
    constants.js
    createStore.js
    helpPanel.js
    index.js
    partials.js
    redux.js
    styles.scss
  static/  (1 files)
    89889688147bd7575d6327160d64e760.svg
  .babelrc
  server.js
  webpack.buildWebsite.js
  webpack.runWebsiteWithHotReloading.js
.eslintignore
.eslintrc.json
.gitignore
.travis.yml
LICENSE
README.md
componentDocumentation.md
howToContribute.md
index.html
package.json
publish.sh
```

## Entry points

- [addons/src/index.js](https://github.com/text-mask/text-mask/blob/120393e0de2c4c7742fb600ff8c5a72ddf3e58cf/addons/src/index.js)
- [core/src/index.js](https://github.com/text-mask/text-mask/blob/120393e0de2c4c7742fb600ff8c5a72ddf3e58cf/core/src/index.js)
- [ember/addon/index.js](https://github.com/text-mask/text-mask/blob/120393e0de2c4c7742fb600ff8c5a72ddf3e58cf/ember/addon/index.js)
- [ember/index.js](https://github.com/text-mask/text-mask/blob/120393e0de2c4c7742fb600ff8c5a72ddf3e58cf/ember/index.js)
- [website/server.js](https://github.com/text-mask/text-mask/blob/120393e0de2c4c7742fb600ff8c5a72ddf3e58cf/website/server.js)
- [website/src/app.js](https://github.com/text-mask/text-mask/blob/120393e0de2c4c7742fb600ff8c5a72ddf3e58cf/website/src/app.js)
- [website/src/index.js](https://github.com/text-mask/text-mask/blob/120393e0de2c4c7742fb600ff8c5a72ddf3e58cf/website/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| addons package | library | Observed | Groups 7 file(s) under addons package (observed from repository paths and static analysis). |
| angular1 package | library | Observed | Groups 5 file(s) under angular1 package (observed from repository paths and static analysis). |
| angular2 package | library | Observed | Groups 11 file(s) under angular2 package (observed from repository paths and static analysis). |
| common package | library | Observed | Groups 6 file(s) under common package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 22 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| ember package | library | Observed | Groups 8 file(s) under ember package (observed from repository paths and static analysis). |
| react package | library | Observed | Groups 7 file(s) under react package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 9 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 38 file(s) under tests (observed from repository paths and static analysis). |
| vanilla package | library | Observed | Groups 5 file(s) under vanilla package (observed from repository paths and static analysis). |
| vue package | library | Observed | Groups 6 file(s) under vue package (observed from repository paths and static analysis). |
| website package | library | Observed | Groups 11 file(s) under website package (observed from repository paths and static analysis). |

## Important files

- `.eslintrc.json` (config)
- `.travis.yml` (ci)
- `addons/package.json` (manifest)
- `angular1/package.json` (manifest)
- `angular2/bs-config.json` (config)
- `angular2/example/tsconfig.json` (config)
- `angular2/package.json` (manifest)
- `angular2/tsconfig.json` (config)
- `angular2/tsconfig.test.json` (config)
- `angular2/tslint.json` (config)
- `angular2/typings.json` (config)
- `angular2/typings/globals/core-js/typings.json` (config)
- `angular2/typings/globals/jasmine/typings.json` (config)
- `angular2/typings/globals/node/typings.json` (config)
- `core/package.json` (manifest)
- `ember/.editorconfig` (config)
- `ember/.travis.yml` (ci)
- `ember/package.json` (manifest)
- `package.json` (manifest)
- `react/package.json` (manifest)
- `vanilla/package.json` (manifest)
- `vue/package.json` (manifest)

## Top-level layout

- `ember` — 45 analysed file(s)
- `angular2` — 30 analysed file(s)
- `core` — 16 analysed file(s)
- `website` — 15 analysed file(s)
- `addons` — 14 analysed file(s)
- `react` — 12 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `angular1` — 11 analysed file(s)
- `vue` — 11 analysed file(s)
- `vanilla` — 10 analysed file(s)
- `common` — 6 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 14 file(s) were skipped during inventory (14 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `120393e0de2c4c7742fb600ff8c5a72ddf3e58cf` is the revision these paths and observations refer to.
