# Project structure: pmndrs/leva

**Analysed commit:** `402a1e9d0899e6d384993aaffe8dc0d2c39110e1`

**Commit reference:** [402a1e9d0899e6d384993aaffe8dc0d2c39110e1](https://github.com/pmndrs/leva/commit/402a1e9d0899e6d384993aaffe8dc0d2c39110e1)

**Tree at this commit:** [pmndrs/leva@402a1e9d0899](https://github.com/pmndrs/leva/tree/402a1e9d0899e6d384993aaffe8dc0d2c39110e1)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | pmndrs/leva |
| Description | 🌋 React-first components GUI |
| Stars | 6274 |
| Forks | 238 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `402a1e9d0899e6d384993aaffe8dc0d2c39110e1` |
| Retrieved at | 2026-11-14T19:14:08.515511+00:00 |
| Files in this snapshot | 319 |

## Directory tree

```text
.changeset/  (4 files)
  README.md
  config.json
  kind-owls-grin.md
  many-games-eat.md
.codesandbox/  (1 files)
  ci.json
.github/  (4 files)
  workflows/  (4 files)
    chromatic.yml
    docs.yml
    main.yml
    release.yml
.husky/  (2 files)
  .gitignore
  pre-commit
.storybook/  (2 files)
  main.js
  preview.js
.vscode/  (1 files)
  settings.json
demo/  (73 files)
  src/  (68 files)
    sandboxes/  (64 files)
      … 64 files under this directory
    App.jsx
    index.css
    index.jsx
    styles.module.css
  index.html
  package.json
  serve.json
  tsconfig.json
  vite.config.js
docs/  (9 files)
  advanced/  (2 files)
    controlled-inputs.md
    creating-plugins.md
  getting-started/  (7 files)
    configuration.md
    inputs.md
    introduction.md
    plugins.md
    special-inputs.md
    styling.md
    typescript.md
packages/  (207 files)
  leva/  (162 files)
    headless/  (1 files)
      … 1 files under this directory
    plugin/  (1 files)
      … 1 files under this directory
    src/  (130 files)
      … 130 files under this directory
    stories/  (27 files)
      … 27 files under this directory
    .npmignore
    CHANGELOG.md
    package.json
  plugin-bezier/  (13 files)
    src/  (10 files)
      … 10 files under this directory
    CHANGELOG.md
    README.md
    package.json
  plugin-dates/  (10 files)
    src/  (7 files)
      … 7 files under this directory
    CHANGELOG.md
    README.md
    package.json
  plugin-plot/  (11 files)
    src/  (8 files)
      … 8 files under this directory
    CHANGELOG.md
    README.md
    package.json
  plugin-spring/  (11 files)
    src/  (8 files)
      … 8 files under this directory
    CHANGELOG.md
    README.md
    package.json
.all-contributorsrc
.eslintignore
.eslintrc.json
.gitignore
.prettierignore
.yarnrc.yml
LICENSE
README.md
babel.config.js
code_of_conduct.md
contributing.md
package.json
pnpm-workspace.yaml
tsconfig.json
vitest.config.ts
vitest.setup.ts
```

## Entry points

- [demo/src/sandboxes/leva-advanced-panels/src/index.jsx](https://github.com/pmndrs/leva/blob/402a1e9d0899e6d384993aaffe8dc0d2c39110e1/demo/src/sandboxes/leva-advanced-panels/src/index.jsx)
- [demo/src/sandboxes/leva-custom-plugin/src/index.tsx](https://github.com/pmndrs/leva/blob/402a1e9d0899e6d384993aaffe8dc0d2c39110e1/demo/src/sandboxes/leva-custom-plugin/src/index.tsx)
- [demo/src/sandboxes/leva-minimal/src/index.jsx](https://github.com/pmndrs/leva/blob/402a1e9d0899e6d384993aaffe8dc0d2c39110e1/demo/src/sandboxes/leva-minimal/src/index.jsx)
- [demo/src/sandboxes/leva-scroll/src/index.jsx](https://github.com/pmndrs/leva/blob/402a1e9d0899e6d384993aaffe8dc0d2c39110e1/demo/src/sandboxes/leva-scroll/src/index.jsx)
- [demo/src/sandboxes/leva-theme/src/index.jsx](https://github.com/pmndrs/leva/blob/402a1e9d0899e6d384993aaffe8dc0d2c39110e1/demo/src/sandboxes/leva-theme/src/index.jsx)
- [demo/src/sandboxes/leva-transient/src/index.jsx](https://github.com/pmndrs/leva/blob/402a1e9d0899e6d384993aaffe8dc0d2c39110e1/demo/src/sandboxes/leva-transient/src/index.jsx)
- [demo/src/sandboxes/leva-ui/src/index.jsx](https://github.com/pmndrs/leva/blob/402a1e9d0899e6d384993aaffe8dc0d2c39110e1/demo/src/sandboxes/leva-ui/src/index.jsx)
- [.storybook/main.js](https://github.com/pmndrs/leva/blob/402a1e9d0899e6d384993aaffe8dc0d2c39110e1/.storybook/main.js)
- [demo/src/App.jsx](https://github.com/pmndrs/leva/blob/402a1e9d0899e6d384993aaffe8dc0d2c39110e1/demo/src/App.jsx)
- [demo/src/index.jsx](https://github.com/pmndrs/leva/blob/402a1e9d0899e6d384993aaffe8dc0d2c39110e1/demo/src/index.jsx)
- [packages/leva/src/index.ts](https://github.com/pmndrs/leva/blob/402a1e9d0899e6d384993aaffe8dc0d2c39110e1/packages/leva/src/index.ts)
- [packages/plugin-bezier/src/index.ts](https://github.com/pmndrs/leva/blob/402a1e9d0899e6d384993aaffe8dc0d2c39110e1/packages/plugin-bezier/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 25 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| demo package | library | Observed | Groups 28 file(s) under demo package (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 188 file(s) under packages package (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.codesandbox/ci.json` (config)
- `.eslintrc.json` (config)
- `.github/workflows/chromatic.yml` (ci)
- `.github/workflows/docs.yml` (ci)
- `.github/workflows/main.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.vscode/settings.json` (config)
- `.yarnrc.yml` (config)
- `demo/package.json` (manifest)
- `demo/serve.json` (config)
- `demo/src/sandboxes/leva-advanced-panels/package.json` (manifest)
- `demo/src/sandboxes/leva-busy/package.json` (manifest)
- `demo/src/sandboxes/leva-custom-plugin/package.json` (manifest)
- `demo/src/sandboxes/leva-minimal/package.json` (manifest)
- `demo/src/sandboxes/leva-plugin-bezier/package.json` (manifest)
- `demo/src/sandboxes/leva-plugin-dates/package.json` (manifest)
- `demo/src/sandboxes/leva-plugin-plot/package.json` (manifest)
- `demo/src/sandboxes/leva-plugin-spring/package.json` (manifest)
- `demo/src/sandboxes/leva-scroll/package.json` (manifest)
- `demo/src/sandboxes/leva-theme/package.json` (manifest)
- `demo/src/sandboxes/leva-transient/package.json` (manifest)
- `demo/src/sandboxes/leva-ui/package.json` (manifest)
- `demo/tsconfig.json` (config)
- `package.json` (manifest)
- `packages/leva/headless/package.json` (manifest)
- `packages/leva/package.json` (manifest)
- `packages/leva/plugin/package.json` (manifest)
- `packages/plugin-bezier/package.json` (manifest)
- `packages/plugin-dates/package.json` (manifest)
- `packages/plugin-plot/package.json` (manifest)
- `packages/plugin-spring/package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `tsconfig.json` (config)

## Top-level layout

- `packages` — 207 analysed file(s)
- `demo` — 73 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `docs` — 9 analysed file(s)
- `.changeset` — 4 analysed file(s)
- `.github` — 4 analysed file(s)
- `.husky` — 2 analysed file(s)
- `.storybook` — 2 analysed file(s)
- `.codesandbox` — 1 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `402a1e9d0899e6d384993aaffe8dc0d2c39110e1` is the revision these paths and observations refer to.
