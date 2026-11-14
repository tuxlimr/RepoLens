# Project structure: blocks/blocks

**Analysed commit:** `70bee97e65353fd3e2ad0ba7040a07f2637b9b97`

**Commit reference:** [70bee97e65353fd3e2ad0ba7040a07f2637b9b97](https://github.com/blocks/blocks/commit/70bee97e65353fd3e2ad0ba7040a07f2637b9b97)

**Tree at this commit:** [blocks/blocks@70bee97e6535](https://github.com/blocks/blocks/tree/70bee97e65353fd3e2ad0ba7040a07f2637b9b97)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | blocks/blocks |
| Description | A JSX-based page builder for creating beautiful websites without writing code |
| Stars | 5096 |
| Forks | 325 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `70bee97e65353fd3e2ad0ba7040a07f2637b9b97` |
| Retrieved at | 2026-11-14T19:14:28.566814+00:00 |
| Files in this snapshot | 188 |

## Directory tree

```text
.changeset/  (2 files)
  README.md
  config.json
.github/  (3 files)
  workflows/  (3 files)
    lint.yml
    release.yml
    test.yml
packages/  (136 files)
  blocks-ui/  (113 files)
    src/  (111 files)
      … 111 files under this directory
    CHANGELOG.md
    package.json
  gatsby-plugin-blocks/  (7 files)
    src/  (3 files)
      … 3 files under this directory
    CHANGELOG.md
    gatsby-node.js
    index.js
    package.json
  property-controls/  (4 files)
    src/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    package.json
    readme.md
  react/  (12 files)
    src/  (9 files)
      … 9 files under this directory
    CHANGELOG.md
    package.json
    readme.md
src/  (32 files)
  components/  (5 files)
    block.js
    layout.js
    minimal-layout.js
    seo.js
    subscribe.js
  gatsby-plugin-theme-ui/  (2 files)
    components.js
    index.js
  pages/  (22 files)
    docs/  (9 files)
      … 9 files under this directory
    404.mdx
    about.mdx
    blocks-old.js
    blocks.mdx
    confirm.mdx
    confirmed.mdx
    demo.js
    getting-started.mdx
    index.mdx
    newsletter.mdx
    prior-art.mdx
    uses.mdx
    vision.mdx
  templates/  (1 files)
    block.js
  blocks.js
  nav.js
.eslintignore
.eslintrc.js
.gitignore
.nowignore
.prettierrc
babel.config.js
code-of-conduct.md
contributing.md
gatsby-config.js
gatsby-node.js
license
now.json
package.json
readme.md
renovate.json
```

## Entry points

- [packages/blocks-ui/src/index.js](https://github.com/blocks/blocks/blob/70bee97e65353fd3e2ad0ba7040a07f2637b9b97/packages/blocks-ui/src/index.js)
- [packages/gatsby-plugin-blocks/index.js](https://github.com/blocks/blocks/blob/70bee97e65353fd3e2ad0ba7040a07f2637b9b97/packages/gatsby-plugin-blocks/index.js)
- [packages/property-controls/src/index.js](https://github.com/blocks/blocks/blob/70bee97e65353fd3e2ad0ba7040a07f2637b9b97/packages/property-controls/src/index.js)
- [packages/react/src/index.js](https://github.com/blocks/blocks/blob/70bee97e65353fd3e2ad0ba7040a07f2637b9b97/packages/react/src/index.js)
- [src/gatsby-plugin-theme-ui/index.js](https://github.com/blocks/blocks/blob/70bee97e65353fd3e2ad0ba7040a07f2637b9b97/src/gatsby-plugin-theme-ui/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| blocks.js package | library | Observed | Groups 1 file(s) under blocks.js package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 5 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| gatsby-plugin-theme-ui package | library | Observed | Groups 2 file(s) under gatsby-plugin-theme-ui package (observed from repository paths and static analysis). |
| nav.js package | library | Observed | Groups 1 file(s) under nav.js package (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 125 file(s) under packages package (observed from repository paths and static analysis). |
| pages package | library | Observed | Groups 2 file(s) under pages package (observed from repository paths and static analysis). |
| templates package | library | Observed | Groups 1 file(s) under templates package (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.github/workflows/lint.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `now.json` (config)
- `package.json` (manifest)
- `packages/blocks-ui/package.json` (manifest)
- `packages/gatsby-plugin-blocks/package.json` (manifest)
- `packages/property-controls/package.json` (manifest)
- `packages/react/package.json` (manifest)
- `renovate.json` (config)

## Top-level layout

- `packages` — 136 analysed file(s)
- `src` — 32 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `.github` — 3 analysed file(s)
- `.changeset` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `70bee97e65353fd3e2ad0ba7040a07f2637b9b97` is the revision these paths and observations refer to.
