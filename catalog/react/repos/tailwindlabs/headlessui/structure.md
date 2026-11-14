# Project structure: tailwindlabs/headlessui

**Analysed commit:** `eea57cf46fd6767ed1059012f7073b88eb159fba`

**Commit reference:** [eea57cf46fd6767ed1059012f7073b88eb159fba](https://github.com/tailwindlabs/headlessui/commit/eea57cf46fd6767ed1059012f7073b88eb159fba)

**Tree at this commit:** [tailwindlabs/headlessui@eea57cf46fd6](https://github.com/tailwindlabs/headlessui/tree/eea57cf46fd6767ed1059012f7073b88eb159fba)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | tailwindlabs/headlessui |
| Description | Completely unstyled, fully accessible UI components, designed to integrate beautifully with Tailwind CSS. |
| Stars | 28828 |
| Forks | 1218 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `eea57cf46fd6767ed1059012f7073b88eb159fba` |
| Retrieved at | 2026-11-14T19:13:03.383740+00:00 |
| Files in this snapshot | 470 |

## Directory tree

```text
.github/  (7 files)
  ISSUE_TEMPLATE/  (2 files)
    bug-report.md
    config.yml
  workflows/  (3 files)
    main.yml
    prepare-release.yml
    release.yml
  CONTRIBUTING.md
  FUNDING.yml
jest/  (3 files)
  create-jest-config.cjs
  custom-matchers.ts
  polyfills.ts
packages/  (330 files)
  @headlessui-react/  (213 files)
    src/  (205 files)
      … 205 files under this directory
    types/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    LICENSE
    README.md
    jest.config.cjs
    jest.setup.js
    package.json
    tsconfig.json
  @headlessui-tailwindcss/  (10 files)
    scripts/  (1 files)
      … 1 files under this directory
    src/  (3 files)
      … 3 files under this directory
    CHANGELOG.md
    LICENSE
    README.md
    jest.config.cjs
    package.json
    tsconfig.json
  @headlessui-vue/  (107 files)
    src/  (100 files)
      … 100 files under this directory
    types/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    LICENSE
    README.md
    jest.config.cjs
    package.json
    tsconfig.json
playgrounds/  (111 files)
  react/  (64 files)
    app/  (5 files)
      … 5 files under this directory
    components/  (2 files)
      … 2 files under this directory
    page-examples/  (46 files)
      … 46 files under this directory
    utils/  (4 files)
      … 4 files under this directory
    .prettierignore
    data.ts
    next-env.d.ts
    next.config.js
    package.json
    postcss.config.js
    tsconfig.json
  vue/  (47 files)
    src/  (41 files)
      … 41 files under this directory
    index.html
    package.json
    postcss.config.js
    tsconfig.json
    vercel.json
    vite.config.js
scripts/  (10 files)
  build.sh
  lint.sh
  make-nextjs-happy.js
  package-path.js
  release-channel.js
  release-notes.js
  resolve-files.js
  rewrite-imports.js
  test.sh
  watch.sh
.eslintignore
.gitignore
.prettierignore
.swcrc
CHANGELOG.md
LICENSE
README.md
jest.config.cjs
package.json
```

## Entry points

- [packages/@headlessui-react/src/index.ts](https://github.com/tailwindlabs/headlessui/blob/eea57cf46fd6767ed1059012f7073b88eb159fba/packages/%40headlessui-react/src/index.ts)
- [packages/@headlessui-tailwindcss/src/index.ts](https://github.com/tailwindlabs/headlessui/blob/eea57cf46fd6767ed1059012f7073b88eb159fba/packages/%40headlessui-tailwindcss/src/index.ts)
- [packages/@headlessui-vue/src/index.ts](https://github.com/tailwindlabs/headlessui/blob/eea57cf46fd6767ed1059012f7073b88eb159fba/packages/%40headlessui-vue/src/index.ts)
- [playgrounds/react/app/page.tsx](https://github.com/tailwindlabs/headlessui/blob/eea57cf46fd6767ed1059012f7073b88eb159fba/playgrounds/react/app/page.tsx)
- [playgrounds/vue/src/main.ts](https://github.com/tailwindlabs/headlessui/blob/eea57cf46fd6767ed1059012f7073b88eb159fba/playgrounds/vue/src/main.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 12 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| jest package | library | Observed | Groups 3 file(s) under jest package (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 305 file(s) under packages package (observed from repository paths and static analysis). |
| playgrounds package | library | Observed | Groups 101 file(s) under playgrounds package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 10 file(s) under scripts package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/main.yml` (ci)
- `.github/workflows/prepare-release.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `package.json` (manifest)
- `packages/@headlessui-react/package.json` (manifest)
- `packages/@headlessui-react/tsconfig.json` (config)
- `packages/@headlessui-tailwindcss/package.json` (manifest)
- `packages/@headlessui-tailwindcss/tsconfig.json` (config)
- `packages/@headlessui-vue/package.json` (manifest)
- `packages/@headlessui-vue/tsconfig.json` (config)
- `playgrounds/react/package.json` (manifest)
- `playgrounds/react/tsconfig.json` (config)
- `playgrounds/vue/package.json` (manifest)
- `playgrounds/vue/tsconfig.json` (config)
- `playgrounds/vue/vercel.json` (config)

## Top-level layout

- `packages` — 330 analysed file(s)
- `playgrounds` — 111 analysed file(s)
- `scripts` — 10 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `.github` — 7 analysed file(s)
- `jest` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 3 file(s) were skipped during inventory (3 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `eea57cf46fd6767ed1059012f7073b88eb159fba` is the revision these paths and observations refer to.
