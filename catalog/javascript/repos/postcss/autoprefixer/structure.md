# Project structure: postcss/autoprefixer

**Analysed commit:** `58135fad52420576fce568223603ab1e382329ea`

**Commit reference:** [58135fad52420576fce568223603ab1e382329ea](https://github.com/postcss/autoprefixer/commit/58135fad52420576fce568223603ab1e382329ea)

**Tree at this commit:** [postcss/autoprefixer@58135fad5242](https://github.com/postcss/autoprefixer/tree/58135fad52420576fce568223603ab1e382329ea)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | postcss/autoprefixer |
| Description |  Parse CSS and add vendor prefixes to rules by Can I Use |
| Stars | 22197 |
| Forks | 1289 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `58135fad52420576fce568223603ab1e382329ea` |
| Retrieved at | 2026-11-14T19:11:09.015375+00:00 |
| Files in this snapshot | 278 |

## Directory tree

```text
.github/  (4 files)
  workflows/  (2 files)
    release.yml
    test.yml
  CONTRIBUTING.md
  FUNDING.yml
bin/  (1 files)
  autoprefixer
data/  (1 files)
  prefixes.js
lib/  (78 files)
  hacks/  (59 files)
    align-content.js
    align-items.js
    align-self.js
    animation.js
    appearance.js
    autofill.js
    backdrop-filter.js
    background-clip.js
    background-size.js
    block-logical.js
    border-image.js
    border-radius.js
    break-props.js
    cross-fade.js
    display-flex.js
    display-grid.js
    file-selector-button.js
    filter-value.js
    filter.js
    flex-basis.js
    flex-direction.js
    flex-flow.js
    flex-grow.js
    flex-shrink.js
    … 35 more files
  at-rule.js
  autoprefixer.d.ts
  autoprefixer.js
  brackets.js
  browsers.js
  declaration.js
  info.js
  old-selector.js
  old-value.js
  prefixer.js
  prefixes.js
  processor.js
  resolution.js
  selector.js
  supports.js
  transition.js
  utils.js
  value.js
  vendor.js
test/  (180 files)
  cases/  (165 files)
    config/  (4 files)
      … 4 files under this directory
    3d-transform.css
    3d-transform.out.css
    advanced-filter.css
    advanced-filter.out.css
    animation.css
    animation.out.css
    appearance.css
    appearance.out.css
    at-rules.css
    at-rules.out.css
    autofill.css
    autofill.out.css
    backdrop-filter.css
    backdrop-filter.out.css
    backdrop.css
    backdrop.out.css
    background-clip.css
    background-clip.out.css
    background-size.css
    background-size.out.css
    border-image.css
    border-image.out.css
    border-radius.css
    border-radius.out.css
    … 137 more files
  at-rule.test.js
  autoprefixer.test.js
  brackets.test.js
  browsers.test.js
  declaration.test.js
  info.test.js
  old-selector.test.js
  old-value.test.js
  postcss.test.js
  prefixer.test.js
  prefixes.test.js
  selector.test.js
  supports.test.js
  utils.test.js
  value.test.js
.devcontainer.json
.editorconfig
.gitignore
.npmignore
.prettierrc.js
AUTHORS
CHANGELOG.md
LICENSE
README.md
logo.svg
oxfmt.config.ts
oxlint.config.ts
package.json
pnpm-workspace.yaml
```

## Entry points

- [lib/autoprefixer.js](https://github.com/postcss/autoprefixer/blob/58135fad52420576fce568223603ab1e382329ea/lib/autoprefixer.js)
- [bin/autoprefixer](https://github.com/postcss/autoprefixer/blob/58135fad52420576fce568223603ab1e382329ea/bin/autoprefixer)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 78 file(s) under lib package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 180 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.devcontainer.json` (config)
- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `package.json` (manifest)
- `pnpm-workspace.yaml` (config)

## Top-level layout

- `test` — 180 analysed file(s)
- `lib` — 78 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `.github` — 4 analysed file(s)
- `bin` — 1 analysed file(s)
- `data` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `58135fad52420576fce568223603ab1e382329ea` is the revision these paths and observations refer to.
