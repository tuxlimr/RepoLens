# Project structure: meetalva/alva

**Analysed commit:** `bfdb6aef4a55b5d99ed154a1dcced1acf9aca894`

**Commit reference:** [bfdb6aef4a55b5d99ed154a1dcced1acf9aca894](https://github.com/meetalva/alva/commit/bfdb6aef4a55b5d99ed154a1dcced1acf9aca894)

**Tree at this commit:** [meetalva/alva@bfdb6aef4a55](https://github.com/meetalva/alva/tree/bfdb6aef4a55b5d99ed154a1dcced1acf9aca894)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | meetalva/alva |
| Description | Create living prototypes with code components. |
| Stars | 3689 |
| Forks | 214 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `bfdb6aef4a55b5d99ed154a1dcced1acf9aca894` |
| Retrieved at | 2026-11-14T19:15:10.333096+00:00 |
| Files in this snapshot | 641 |

## Directory tree

```text
.circleci/  (1 files)
  config.yml
.github/  (3 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  pull_request_template.md
.vscode/  (3 files)
  extensions.json
  launch.json
  settings.json
docs/  (27 files)
  contributors/  (6 files)
    RELEASE.md
    architecture-diagram.md
    architecture-diagram.svg
    contributing.md
    develop-alva.md
    test-autoupdater.md
  guides-design/  (4 files)
    design-drafts.md
    getting-started.md
    interaction.md
    variables.md
  guides-dev/  (4 files)
    create-library.md
    create-pattern.md
    create-properties.md
    install-local-library.md
  references/  (4 files)
    glossary.md
    library-requirements.md
    properties.md
    reference.md
  about-us.md
  github.md
  gitter.md
  guides-design.md
  guides-dev.md
  howtos.md
  legalnotice.md
  privacypolicy.md
  start.md
packages/  (587 files)
  analyzer/  (82 files)
    src/  (78 files)
      … 78 files under this directory
    index.d.ts
    index.js
    package.json
    tsconfig.json
  analyzer-cli/  (4 files)
    bin/  (1 files)
      … 1 files under this directory
    src/  (1 files)
      … 1 files under this directory
    package.json
    tsconfig.json
  components/  (159 files)
    src/  (155 files)
      … 155 files under this directory
    index.d.ts
    index.js
    package.json
    tsconfig.json
  core/  (213 files)
    bin/  (1 files)
      … 1 files under this directory
    src/  (206 files)
      … 206 files under this directory
    .prettierignore
    dev-app-update.yml
    package.json
    package.ncc.json
    tsconfig.json
    tslint.json
  essentials/  (9 files)
    src/  (7 files)
      … 7 files under this directory
    package.json
    tsconfig.json
  message/  (8 files)
    src/  (4 files)
      … 4 files under this directory
    index.d.ts
    index.js
    package.json
    tsconfig.json
  model/  (58 files)
    src/  (54 files)
      … 54 files under this directory
    index.d.ts
    index.js
    package.json
    tsconfig.json
  model-tree/  (6 files)
    src/  (2 files)
      … 2 files under this directory
    index.d.ts
    index.js
    package.json
    tsconfig.json
  site/  (8 files)
    src/  (6 files)
      … 6 files under this directory
    package.json
    tsconfig.json
  tools/  (8 files)
    src/  (1 files)
      … 1 files under this directory
    alva-dependencies.js
    alva-deploy.js
    alva-release.js
    alva-trigger.js
    alva-version.js
    package.json
    tsconfig.json
  types/  (17 files)
    src/  (13 files)
      … 13 files under this directory
    index.d.ts
    index.js
    package.json
    tsconfig.json
  util/  (15 files)
    src/  (11 files)
      … 11 files under this directory
    index.d.ts
    index.js
    package.json
    tsconfig.json
.editorconfig
.gitattributes
.gitignore
.prettierignore
.yarnclean
.yarnrc
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
commitlint.config.js
jest.config.js
lerna.json
package.json
patternplate.config.js
renovate.json
tsconfig.json
tslint.json
webpack.config.js
```

## Entry points

- [packages/core/bin/alva.js](https://github.com/meetalva/alva/blob/bfdb6aef4a55b5d99ed154a1dcced1acf9aca894/packages/core/bin/alva.js)
- [packages/tools/alva-dependencies.js](https://github.com/meetalva/alva/blob/bfdb6aef4a55b5d99ed154a1dcced1acf9aca894/packages/tools/alva-dependencies.js)
- [packages/tools/alva-deploy.js](https://github.com/meetalva/alva/blob/bfdb6aef4a55b5d99ed154a1dcced1acf9aca894/packages/tools/alva-deploy.js)
- [packages/tools/alva-trigger.js](https://github.com/meetalva/alva/blob/bfdb6aef4a55b5d99ed154a1dcced1acf9aca894/packages/tools/alva-trigger.js)
- [packages/tools/alva-version.js](https://github.com/meetalva/alva/blob/bfdb6aef4a55b5d99ed154a1dcced1acf9aca894/packages/tools/alva-version.js)
- [packages/tools/alva-release.js](https://github.com/meetalva/alva/blob/bfdb6aef4a55b5d99ed154a1dcced1acf9aca894/packages/tools/alva-release.js)
- [packages/analyzer/index.js](https://github.com/meetalva/alva/blob/bfdb6aef4a55b5d99ed154a1dcced1acf9aca894/packages/analyzer/index.js)
- [packages/analyzer/src/index.ts](https://github.com/meetalva/alva/blob/bfdb6aef4a55b5d99ed154a1dcced1acf9aca894/packages/analyzer/src/index.ts)
- [packages/components/index.js](https://github.com/meetalva/alva/blob/bfdb6aef4a55b5d99ed154a1dcced1acf9aca894/packages/components/index.js)
- [packages/components/src/index.ts](https://github.com/meetalva/alva/blob/bfdb6aef4a55b5d99ed154a1dcced1acf9aca894/packages/components/src/index.ts)
- [packages/essentials/src/index.ts](https://github.com/meetalva/alva/blob/bfdb6aef4a55b5d99ed154a1dcced1acf9aca894/packages/essentials/src/index.ts)
- [packages/essentials/src/page.tsx](https://github.com/meetalva/alva/blob/bfdb6aef4a55b5d99ed154a1dcced1acf9aca894/packages/essentials/src/page.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 9 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 72 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 2 file(s) under data layer (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 7 file(s) under external integrations (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 307 file(s) under packages package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 184 file(s) under service / domain layer (observed from repository paths and static analysis). |

## Important files

- `.circleci/config.yml` (ci)
- `.editorconfig` (config)
- `.vscode/extensions.json` (config)
- `.vscode/launch.json` (config)
- `.vscode/settings.json` (config)
- `lerna.json` (config)
- `package.json` (manifest)
- `packages/analyzer-cli/package.json` (manifest)
- `packages/analyzer-cli/tsconfig.json` (config)
- `packages/analyzer/package.json` (manifest)
- `packages/analyzer/tsconfig.json` (config)
- `packages/components/package.json` (manifest)
- `packages/components/src/add-button/pattern.json` (config)
- `packages/components/src/badge-icon/pattern.json` (config)
- `packages/components/src/button/pattern.json` (config)
- `packages/components/src/chrome-button/pattern.json` (config)
- `packages/components/src/chrome/pattern.json` (config)
- `packages/components/src/colors/pattern.json` (config)
- `packages/components/src/copy/pattern.json` (config)
- `packages/components/src/drag-area/pattern.json` (config)
- `packages/components/src/editable-title/pattern.json` (config)
- `packages/components/src/element-slot/pattern.json` (config)
- `packages/components/src/element/pattern.json` (config)
- `packages/components/src/empty-state/pattern.json` (config)
- `packages/components/src/fonts/pattern.json` (config)
- `packages/components/src/headline/pattern.json` (config)
- `packages/components/src/icons/pattern.json` (config)
- `packages/components/src/image/pattern.json` (config)
- `packages/components/src/layout-switch/pattern.json` (config)
- `packages/components/src/layout/pattern.json` (config)
- `packages/components/src/library-box/pattern.json` (config)
- `packages/components/src/link-icon/pattern.json` (config)
- `packages/components/src/link/pattern.json` (config)
- `packages/components/src/list/pattern.json` (config)
- `packages/components/src/page-tile/pattern.json` (config)
- `packages/components/src/pattern-list/pattern.json` (config)
- `packages/components/src/property-box/pattern.json` (config)
- `packages/components/src/property-details/pattern.json` (config)
- `packages/components/src/property-item-asset/pattern.json` (config)
- `packages/components/src/property-item-boolean/pattern.json` (config)
- `packages/components/src/property-item-buttongroup/pattern.json` (config)
- `packages/components/src/property-item-color/pattern.json` (config)
- `packages/components/src/property-item-number/pattern.json` (config)
- `packages/components/src/property-item-select/pattern.json` (config)
- `packages/components/src/property-item-string/pattern.json` (config)
- `packages/components/src/search/pattern.json` (config)
- `packages/components/src/select/pattern.json` (config)
- `packages/components/src/space/pattern.json` (config)
- `packages/components/src/splash-screen/pattern.json` (config)
- `packages/components/src/tab/pattern.json` (config)
- `packages/components/src/teaser/pattern.json` (config)
- `packages/components/src/view-switch/pattern.json` (config)
- `packages/components/tsconfig.json` (config)
- `packages/core/dev-app-update.yml` (config)
- `packages/core/package.json` (manifest)
- `packages/core/package.ncc.json` (config)
- `packages/core/tsconfig.json` (config)
- `packages/core/tslint.json` (config)
- `packages/essentials/package.json` (manifest)
- `packages/essentials/tsconfig.json` (config)
- `packages/message/package.json` (manifest)
- `packages/message/tsconfig.json` (config)
- `packages/model-tree/package.json` (manifest)
- `packages/model-tree/tsconfig.json` (config)
- `packages/model/package.json` (manifest)
- `packages/model/tsconfig.json` (config)
- `packages/site/package.json` (manifest)
- `packages/site/tsconfig.json` (config)
- `packages/tools/package.json` (manifest)
- `packages/tools/tsconfig.json` (config)
- `packages/types/package.json` (manifest)
- `packages/types/tsconfig.json` (config)
- `packages/util/package.json` (manifest)
- `packages/util/tsconfig.json` (config)
- `renovate.json` (config)
- `tsconfig.json` (config)
- `tslint.json` (config)

## Top-level layout

- `packages` — 587 analysed file(s)
- `docs` — 27 analysed file(s)
- `(root files)` — 20 analysed file(s)
- `.github` — 3 analysed file(s)
- `.vscode` — 3 analysed file(s)
- `.circleci` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `bfdb6aef4a55b5d99ed154a1dcced1acf9aca894` is the revision these paths and observations refer to.
