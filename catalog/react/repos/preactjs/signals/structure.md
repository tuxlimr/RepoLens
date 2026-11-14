# Project structure: preactjs/signals

**Analysed commit:** `8d5e9b757f88e52b7bafd7e804ac0582b2a86659`

**Commit reference:** [8d5e9b757f88e52b7bafd7e804ac0582b2a86659](https://github.com/preactjs/signals/commit/8d5e9b757f88e52b7bafd7e804ac0582b2a86659)

**Tree at this commit:** [preactjs/signals@8d5e9b757f88](https://github.com/preactjs/signals/tree/8d5e9b757f88e52b7bafd7e804ac0582b2a86659)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | preactjs/signals |
| Description | Manage state with style in every framework |
| Stars | 4505 |
| Forks | 133 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `8d5e9b757f88e52b7bafd7e804ac0582b2a86659` |
| Retrieved at | 2026-11-14T19:14:44.176032+00:00 |
| Files in this snapshot | 229 |

## Directory tree

```text
.changeset/  (3 files)
  README.md
  config.json
  quick-spies-fetch.md
.devcontainer/  (2 files)
  Dockerfile
  devcontainer.json
.github/  (8 files)
  ISSUE_TEMPLATE/  (2 files)
    bug-report.md
    feature-request.md
  scripts/  (2 files)
    has-unpublished-packages.mjs
    stage-packages.mjs
  workflows/  (3 files)
    compressed-size.yml
    main.yml
    release.yml
  CODEOWNERS
.husky/  (1 files)
  pre-commit
docs/  (31 files)
  demos/  (24 files)
    animation/  (2 files)
      … 2 files under this directory
    auth-form/  (2 files)
      … 2 files under this directory
    linting/  (2 files)
      … 2 files under this directory
    nesting/  (2 files)
      … 2 files under this directory
    react/  (4 files)
      … 4 files under this directory
    todo/  (2 files)
      … 2 files under this directory
    EmbeddedDevtools.tsx
    Unmount.tsx
    basic.html
    bench.tsx
    devtools.css
    devtools.tsx
    index.html
    index.tsx
    render-flasher.tsx
    style.css
  .oxlintrc.json
  eslint.config.mjs
  index.html
  index.tsx
  package.json
  tsconfig.json
  vite.config.ts
extension/  (19 files)
  src/  (5 files)
    components/  (2 files)
      … 2 files under this directory
    models/  (1 files)
      … 1 files under this directory
    panel.tsx
    popup.tsx
  .gitignore
  CHANGELOG.md
  README.md
  background.js
  content.js
  devtools-init.js
  devtools.html
  inject.js
  manifest.json
  package.json
  panel.html
  popup.html
  tsconfig.json
  vite.config.ts
packages/  (140 files)
  core/  (6 files)
    src/  (1 files)
      … 1 files under this directory
    test/  (2 files)
      … 2 files under this directory
    CHANGELOG.md
    README.md
    package.json
  debug/  (11 files)
    src/  (5 files)
      … 5 files under this directory
    test/  (3 files)
      … 3 files under this directory
    CHANGELOG.md
    README.md
    package.json
  devtools-adapter/  (11 files)
    src/  (7 files)
      … 7 files under this directory
    test/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    README.md
    package.json
  devtools-ui/  (32 files)
    examples/  (2 files)
      … 2 files under this directory
    src/  (24 files)
      … 24 files under this directory
    test/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    README.md
    package.json
    tsconfig.json
    vitest.config.mjs
  eslint-plugin-signals/  (18 files)
    src/  (8 files)
      … 8 files under this directory
    test/  (7 files)
      … 7 files under this directory
    CHANGELOG.md
    README.md
    package.json
  preact/  (14 files)
    src/  (2 files)
      … 2 files under this directory
    test/  (6 files)
      … 6 files under this directory
    utils/  (3 files)
      … 3 files under this directory
    CHANGELOG.md
    README.md
    package.json
  preact-transform/  (5 files)
    src/  (1 files)
      … 1 files under this directory
    test/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    README.md
    package.json
  react/  (25 files)
    runtime/  (9 files)
      … 9 files under this directory
    src/  (1 files)
      … 1 files under this directory
    test/  (8 files)
      … 8 files under this directory
    utils/  (4 files)
      … 4 files under this directory
    CHANGELOG.md
    README.md
    package.json
  react-transform/  (7 files)
    src/  (1 files)
      … 1 files under this directory
    test/  (3 files)
      … 3 files under this directory
    CHANGELOG.md
    README.md
    package.json
  vite-plugin/  (11 files)
    src/  (7 files)
      … 7 files under this directory
    test/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    README.md
    package.json
patches/  (2 files)
  babel-plugin-transform-rename-properties@0.1.0.patch
  microbundle@0.15.1.patch
scripts/  (4 files)
  mangle-plugin.mjs
  pack-all.mjs
  sync-eslint-plugin-meta-version.mjs
  transform-plugin.mjs
skills/  (1 files)
  signals-debugging/  (1 files)
    SKILL.md
test/  (3 files)
  browser/  (3 files)
    babel.js
    mockFs.js
    nodeGlobals.js
tools/  (1 files)
  postbuild-vite-plugin.mjs
.editorconfig
.gitignore
.oxfmtrc.jsonc
.oxlintrc.json
CONTRIBUTING.md
LICENSE
README.md
global.d.ts
mangle.json
netlify.toml
package.json
pnpm-workspace.yaml
tsconfig.json
vitest.config.mjs
```

## Entry points

- [packages/eslint-plugin-signals/src/index.mjs](https://github.com/preactjs/signals/blob/8d5e9b757f88e52b7bafd7e804ac0582b2a86659/packages/eslint-plugin-signals/src/index.mjs)
- [packages/core/src/index.ts](https://github.com/preactjs/signals/blob/8d5e9b757f88e52b7bafd7e804ac0582b2a86659/packages/core/src/index.ts)
- [packages/debug/src/index.ts](https://github.com/preactjs/signals/blob/8d5e9b757f88e52b7bafd7e804ac0582b2a86659/packages/debug/src/index.ts)
- [packages/devtools-adapter/src/index.ts](https://github.com/preactjs/signals/blob/8d5e9b757f88e52b7bafd7e804ac0582b2a86659/packages/devtools-adapter/src/index.ts)
- [packages/devtools-ui/src/index.ts](https://github.com/preactjs/signals/blob/8d5e9b757f88e52b7bafd7e804ac0582b2a86659/packages/devtools-ui/src/index.ts)
- [packages/preact-transform/src/index.ts](https://github.com/preactjs/signals/blob/8d5e9b757f88e52b7bafd7e804ac0582b2a86659/packages/preact-transform/src/index.ts)
- [packages/preact/src/index.ts](https://github.com/preactjs/signals/blob/8d5e9b757f88e52b7bafd7e804ac0582b2a86659/packages/preact/src/index.ts)
- [packages/react-transform/src/index.ts](https://github.com/preactjs/signals/blob/8d5e9b757f88e52b7bafd7e804ac0582b2a86659/packages/react-transform/src/index.ts)
- [packages/react/src/index.ts](https://github.com/preactjs/signals/blob/8d5e9b757f88e52b7bafd7e804ac0582b2a86659/packages/react/src/index.ts)
- [packages/vite-plugin/src/index.ts](https://github.com/preactjs/signals/blob/8d5e9b757f88e52b7bafd7e804ac0582b2a86659/packages/vite-plugin/src/index.ts)
- [packages/vite-plugin/src/server.ts](https://github.com/preactjs/signals/blob/8d5e9b757f88e52b7bafd7e804ac0582b2a86659/packages/vite-plugin/src/server.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 22 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 7 file(s) under data layer (observed from repository paths and static analysis). |
| extension package | library | Observed | Groups 9 file(s) under extension package (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 53 file(s) under packages package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 4 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 1 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 45 file(s) under tests (observed from repository paths and static analysis). |
| tools package | library | Observed | Groups 1 file(s) under tools package (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.devcontainer/Dockerfile` (container)
- `.devcontainer/devcontainer.json` (config)
- `.editorconfig` (config)
- `.github/workflows/compressed-size.yml` (ci)
- `.github/workflows/main.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.oxlintrc.json` (config)
- `docs/.oxlintrc.json` (config)
- `docs/demos/react/tsconfig.json` (config)
- `docs/package.json` (manifest)
- `docs/tsconfig.json` (config)
- `extension/manifest.json` (config)
- `extension/package.json` (manifest)
- `extension/tsconfig.json` (config)
- `mangle.json` (config)
- `netlify.toml` (config)
- `package.json` (manifest)
- `packages/core/package.json` (manifest)
- `packages/debug/package.json` (manifest)
- `packages/devtools-adapter/package.json` (manifest)
- `packages/devtools-ui/package.json` (manifest)
- `packages/devtools-ui/tsconfig.json` (config)
- `packages/eslint-plugin-signals/package.json` (manifest)
- `packages/preact-transform/package.json` (manifest)
- `packages/preact/package.json` (manifest)
- `packages/preact/utils/package.json` (manifest)
- `packages/react-transform/package.json` (manifest)
- `packages/react/package.json` (manifest)
- `packages/react/runtime/package.json` (manifest)
- `packages/react/utils/package.json` (manifest)
- `packages/vite-plugin/package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `tsconfig.json` (config)

## Top-level layout

- `packages` — 140 analysed file(s)
- `docs` — 31 analysed file(s)
- `extension` — 19 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `.github` — 8 analysed file(s)
- `scripts` — 4 analysed file(s)
- `.changeset` — 3 analysed file(s)
- `test` — 3 analysed file(s)
- `.devcontainer` — 2 analysed file(s)
- `patches` — 2 analysed file(s)
- `.husky` — 1 analysed file(s)
- `skills` — 1 analysed file(s)
- `tools` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `8d5e9b757f88e52b7bafd7e804ac0582b2a86659` is the revision these paths and observations refer to.
