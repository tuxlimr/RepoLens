# Project structure: michalsnik/aos

**Analysed commit:** `329fb34f777034345f4d3f4def4dc3bcc300cc2e`

**Commit reference:** [329fb34f777034345f4d3f4def4dc3bcc300cc2e](https://github.com/michalsnik/aos/commit/329fb34f777034345f4d3f4def4dc3bcc300cc2e)

**Tree at this commit:** [michalsnik/aos@329fb34f7770](https://github.com/michalsnik/aos/tree/329fb34f777034345f4d3f4def4dc3bcc300cc2e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | michalsnik/aos |
| Description | Animate on scroll library |
| Stars | 28054 |
| Forks | 2618 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | next |
| Analysed commit | `329fb34f777034345f4d3f4def4dc3bcc300cc2e` |
| Retrieved at | 2026-11-14T19:10:50.569505+00:00 |
| Files in this snapshot | 57 |

## Directory tree

```text
cypress/  (20 files)
  integration/  (17 files)
    aos_spec.js
    js_events_spec.js
    mutation_spec.js
    settings_anchorPlacement_spec.js
    settings_anchor_spec.js
    settings_animatedClassName_spec.js
    settings_delay_spec.js
    settings_disableMutationObserver_spec.js
    settings_disable_spec.js
    settings_duration_spec.js
    settings_easing_spec.js
    settings_initClassName_spec.js
    settings_mirror.js
    settings_offset_spec.js
    settings_once_spec.js
    settings_startEvent_spec.js
    settings_useClassNames.js
  plugins/  (1 files)
    index.js
  support/  (2 files)
    commands.js
    index.js
demo/  (7 files)
  css/  (1 files)
    styles.css
  anchor.html
  animatecss.html
  async.html
  index.html
  offset.html
  once.html
scripts/  (2 files)
  run-cypress-tests.js
  start-server.js
src/  (13 files)
  js/  (9 files)
    helpers/  (6 files)
      … 6 files under this directory
    libs/  (2 files)
      … 2 files under this directory
    aos.js
  sass/  (4 files)
    _animations.scss
    _core.scss
    _easing.scss
    aos.scss
.babelrc
.editorconfig
.eslintrc.json
.gitattributes
.gitignore
.npmignore
.travis.yml
CONTRIBUTING.md
ISSUE_TEMPLATE.md
LICENSE
PULL_REQUEST_TEMPLATE.md
README.md
cypress.json
package.json
rollup.config.js
```

## Entry points

- [cypress/plugins/index.js](https://github.com/michalsnik/aos/blob/329fb34f777034345f4d3f4def4dc3bcc300cc2e/cypress/plugins/index.js)
- [cypress/support/index.js](https://github.com/michalsnik/aos/blob/329fb34f777034345f4d3f4def4dc3bcc300cc2e/cypress/support/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| cypress package | library | Observed | Groups 3 file(s) under cypress package (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 17 file(s) under external integrations (observed from repository paths and static analysis). |
| js package | library | Observed | Groups 9 file(s) under js package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 2 file(s) under scripts package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.eslintrc.json` (config)
- `.travis.yml` (ci)
- `cypress.json` (config)
- `package.json` (manifest)

## Top-level layout

- `cypress` — 20 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `src` — 13 analysed file(s)
- `demo` — 7 analysed file(s)
- `scripts` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `329fb34f777034345f4d3f4def4dc3bcc300cc2e` is the revision these paths and observations refer to.
