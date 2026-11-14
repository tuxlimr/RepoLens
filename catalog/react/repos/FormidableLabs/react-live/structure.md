# Project structure: FormidableLabs/react-live

**Analysed commit:** `aec1504d87a3a0b7ee552d1238a9264af9e4ef94`

**Commit reference:** [aec1504d87a3a0b7ee552d1238a9264af9e4ef94](https://github.com/FormidableLabs/react-live/commit/aec1504d87a3a0b7ee552d1238a9264af9e4ef94)

**Tree at this commit:** [FormidableLabs/react-live@aec1504d87a3](https://github.com/FormidableLabs/react-live/tree/aec1504d87a3a0b7ee552d1238a9264af9e4ef94)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | FormidableLabs/react-live |
| Description | A flexible playground for live editing React components |
| Stars | 4616 |
| Forks | 256 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `aec1504d87a3a0b7ee552d1238a9264af9e4ef94` |
| Retrieved at | 2026-11-14T19:14:41.053061+00:00 |
| Files in this snapshot | 87 |

## Directory tree

```text
.changeset/  (1 files)
  config.json
.github/  (2 files)
  workflows/  (2 files)
    ci.yml
    release.yml
docs/  (5 files)
  api.md
  faq.md
  installation.md
  introduction.mdx
  usage.md
packages/  (42 files)
  react-live/  (42 files)
    src/  (24 files)
      … 24 files under this directory
    stories/  (9 files)
      … 9 files under this directory
    CHANGELOG.md
    package.json
    tsconfig.json
    tsconfig.stories.json
    tsdown.config.mts
    vite.stories.mts
    vitest.browser.mts
    vitest.config.mts
    vitest.setup.js
website/  (25 files)
  src/  (11 files)
    components/  (8 files)
      … 8 files under this directory
    css/  (1 files)
      … 1 files under this directory
    pages/  (1 files)
      … 1 files under this directory
    globals.d.ts
  static/  (6 files)
    img/  (5 files)
      … 5 files under this directory
    .nojekyll
  .gitignore
  README.md
  docusaurus.config.js
  package.json
  sidebars.js
  tailwind.config.js
  tsconfig.json
  vercel.json
.editorconfig
.gitignore
.nvmrc
.oxlintrc.json
.prettierignore
.prettierrc
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
package.json
```

## Entry points

- [packages/react-live/src/index.ts](https://github.com/FormidableLabs/react-live/blob/aec1504d87a3a0b7ee552d1238a9264af9e4ef94/packages/react-live/src/index.ts)
- [packages/react-live/stories/main.tsx](https://github.com/FormidableLabs/react-live/blob/aec1504d87a3a0b7ee552d1238a9264af9e4ef94/packages/react-live/stories/main.tsx)
- [website/src/pages/index.tsx](https://github.com/FormidableLabs/react-live/blob/aec1504d87a3a0b7ee552d1238a9264af9e4ef94/website/src/pages/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 28 file(s) under packages package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 5 file(s) under tests (observed from repository paths and static analysis). |
| website package | library | Observed | Groups 13 file(s) under website package (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.editorconfig` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.oxlintrc.json` (config)
- `package.json` (manifest)
- `packages/react-live/package.json` (manifest)
- `packages/react-live/tsconfig.json` (config)
- `packages/react-live/tsconfig.stories.json` (config)
- `website/package.json` (manifest)
- `website/tsconfig.json` (config)
- `website/vercel.json` (config)

## Top-level layout

- `packages` — 42 analysed file(s)
- `website` — 25 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `docs` — 5 analysed file(s)
- `.github` — 2 analysed file(s)
- `.changeset` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `aec1504d87a3a0b7ee552d1238a9264af9e4ef94` is the revision these paths and observations refer to.
