# Project structure: negomi/react-burger-menu

**Analysed commit:** `a3df3e6d7b6718faf215a6d15f7cf1f8ebf77acb`

**Commit reference:** [a3df3e6d7b6718faf215a6d15f7cf1f8ebf77acb](https://github.com/negomi/react-burger-menu/commit/a3df3e6d7b6718faf215a6d15f7cf1f8ebf77acb)

**Tree at this commit:** [negomi/react-burger-menu@a3df3e6d7b67](https://github.com/negomi/react-burger-menu/tree/a3df3e6d7b6718faf215a6d15f7cf1f8ebf77acb)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | negomi/react-burger-menu |
| Description | :hamburger: An off-canvas sidebar component with a collection of effects and styles using CSS transitions and SVG path animations |
| Stars | 5082 |
| Forks | 568 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `a3df3e6d7b6718faf215a6d15f7cf1f8ebf77acb` |
| Retrieved at | 2026-11-14T19:14:28.770503+00:00 |
| Files in this snapshot | 73 |

## Directory tree

```text
.github/  (1 files)
  stale.yml
example/  (5 files)
  src/  (5 files)
    .gitignore
    example.js
    example.less
    index.html
    normalize.css
lib/  (18 files)
  components/  (2 files)
    BurgerIcon.js
    CrossIcon.js
  helpers/  (4 files)
    baseStyles.js
    dom.js
    snapsvgImporter.js
    utils.js
  menus/  (10 files)
    bubble.js
    elastic.js
    fallDown.js
    push.js
    pushRotate.js
    reveal.js
    scaleDown.js
    scaleRotate.js
    slide.js
    stack.js
  BurgerMenu.js
  menuFactory.js
src/  (18 files)
  components/  (2 files)
    BurgerIcon.js
    CrossIcon.js
  helpers/  (4 files)
    baseStyles.js
    dom.js
    snapsvgImporter.js
    utils.js
  menus/  (10 files)
    bubble.js
    elastic.js
    fallDown.js
    push.js
    pushRotate.js
    reveal.js
    scaleDown.js
    scaleRotate.js
    slide.js
    stack.js
  BurgerMenu.js
  menuFactory.js
tasks/  (1 files)
  release.js
test/  (19 files)
  utils/  (3 files)
    createMountedComponent.js
    createShallowComponent.js
    renderIntoDocument.js
  .eslintrc.json
  BurgerIcon.spec.js
  BurgerMenu.spec.js
  CrossIcon.spec.js
  baseStyles.spec.js
  bubble.spec.js
  elastic.spec.js
  fallDown.spec.js
  menuFactory.spec.js
  push.spec.js
  pushRotate.spec.js
  reveal.spec.js
  scaleDown.spec.js
  scaleRotate.spec.js
  slide.spec.js
  stack.spec.js
.babelrc
.editorconfig
.eslintignore
.eslintrc.json
.gitignore
.travis.yml
LICENSE
README.md
bower.json
gulpfile.js
package.json
```

## Entry points

- [lib/BurgerMenu.js](https://github.com/negomi/react-burger-menu/blob/a3df3e6d7b6718faf215a6d15f7cf1f8ebf77acb/lib/BurgerMenu.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| BurgerMenu.js package | library | Observed | Groups 1 file(s) under burgermenu.js package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 2 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| helpers package | library | Observed | Groups 4 file(s) under helpers package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 18 file(s) under lib package (observed from repository paths and static analysis). |
| menuFactory.js package | library | Observed | Groups 1 file(s) under menufactory.js package (observed from repository paths and static analysis). |
| menus package | library | Observed | Groups 10 file(s) under menus package (observed from repository paths and static analysis). |
| tasks package | library | Observed | Groups 1 file(s) under tasks package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 19 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.eslintrc.json` (config)
- `.github/stale.yml` (config)
- `.travis.yml` (ci)
- `bower.json` (config)
- `package.json` (manifest)

## Top-level layout

- `test` — 19 analysed file(s)
- `lib` — 18 analysed file(s)
- `src` — 18 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `example` — 5 analysed file(s)
- `.github` — 1 analysed file(s)
- `tasks` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (1 x generated/minified file excluded; 1 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `a3df3e6d7b6718faf215a6d15f7cf1f8ebf77acb` is the revision these paths and observations refer to.
