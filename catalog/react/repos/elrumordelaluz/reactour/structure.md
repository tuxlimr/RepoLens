# Project structure: elrumordelaluz/reactour

**Analysed commit:** `f38832ffd0b610e98dbed01d9dff6b058b1ec1a4`

**Commit reference:** [f38832ffd0b610e98dbed01d9dff6b058b1ec1a4](https://github.com/elrumordelaluz/reactour/commit/f38832ffd0b610e98dbed01d9dff6b058b1ec1a4)

**Tree at this commit:** [elrumordelaluz/reactour@f38832ffd0b6](https://github.com/elrumordelaluz/reactour/tree/f38832ffd0b610e98dbed01d9dff6b058b1ec1a4)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | elrumordelaluz/reactour |
| Description | Tourist Guide into your React Components |
| Stars | 4098 |
| Forks | 350 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `f38832ffd0b610e98dbed01d9dff6b058b1ec1a4` |
| Retrieved at | 2026-11-14T19:14:53.188806+00:00 |
| Files in this snapshot | 197 |

## Directory tree

```text
.changeset/  (2 files)
  README.md
  config.json
.github/  (4 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (2 files)
    ci.yml
    nextjs.yml
apps/  (89 files)
  docs/  (45 files)
    app/  (17 files)
      … 17 files under this directory
    components/  (20 files)
      … 20 files under this directory
    public/  (2 files)
      … 2 files under this directory
    mdx-components.js
    next-env.d.ts
    next.config.mjs
    package.json
    postcss.config.mjs
    tsconfig.json
  web/  (44 files)
    components/  (19 files)
      … 19 files under this directory
    icons/  (6 files)
      … 6 files under this directory
    pages/  (5 files)
      … 5 files under this directory
    public/  (4 files)
      … 4 files under this directory
    .eslintrc.js
    CHANGELOG.md
    README.md
    hooks.tsx
    next-env.d.ts
    next.config.js
    package.json
    styles.css
    tsconfig.json
    utils.js
packages/  (85 files)
  config/  (3 files)
    CHANGELOG.md
    eslint-preset.js
    package.json
  mask/  (11 files)
    __tests__/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    LICENSE
    Mask.tsx
    README.md
    index.tsx
    logo.svg
    package.json
    styles.tsx
    tsconfig.json
    vitest.config.ts
  popover/  (12 files)
    __tests__/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    LICENSE
    Popover.tsx
    README.md
    index.tsx
    logo.svg
    package.json
    styles.css
    styles.tsx
    tsconfig.json
    vitest.config.ts
  tour/  (31 files)
    __tests__/  (10 files)
      … 10 files under this directory
    components/  (6 files)
      … 6 files under this directory
    CHANGELOG.md
    Context.tsx
    Keyboard.tsx
    LICENSE
    README.md
    Tour.tsx
    hooks.tsx
    index.tsx
    package.json
    styles.css
    styles.tsx
    tsconfig.json
    types.tsx
    vitest.config.ts
    withTour.tsx
  tsconfig/  (6 files)
    CHANGELOG.md
    README.md
    base.json
    nextjs.json
    package.json
    react-library.json
  utils/  (22 files)
    __tests__/  (6 files)
      … 6 files under this directory
    CHANGELOG.md
    LICENSE
    Observables.tsx
    Portal.tsx
    README.md
    build.config.ts
    helpers.tsx
    index.tsx
    logo.svg
    package.json
    smoothScroll.tsx
    tsconfig.json
    types.tsx
    useIntersectionObserver.tsx
    useRect.tsx
    vitest.config.ts
.babelrc
.eslintignore
.eslintrc.json
.gitignore
.prettierrc.json
CODE_OF_CONDUCT.md
CONTRIBUTING.md
FUNDING.yml
LICENSE
README.md
logo.svg
package.json
pnpm-workspace.yaml
turbo.json
vercel.json
vitest.setup.ts
vitest.shared.ts
```

## Entry points

- [apps/web/icons/index.tsx](https://github.com/elrumordelaluz/reactour/blob/f38832ffd0b610e98dbed01d9dff6b058b1ec1a4/apps/web/icons/index.tsx)
- [apps/web/pages/index.tsx](https://github.com/elrumordelaluz/reactour/blob/f38832ffd0b610e98dbed01d9dff6b058b1ec1a4/apps/web/pages/index.tsx)
- [packages/mask/index.tsx](https://github.com/elrumordelaluz/reactour/blob/f38832ffd0b610e98dbed01d9dff6b058b1ec1a4/packages/mask/index.tsx)
- [packages/popover/index.tsx](https://github.com/elrumordelaluz/reactour/blob/f38832ffd0b610e98dbed01d9dff6b058b1ec1a4/packages/popover/index.tsx)
- [packages/tour/components/index.tsx](https://github.com/elrumordelaluz/reactour/blob/f38832ffd0b610e98dbed01d9dff6b058b1ec1a4/packages/tour/components/index.tsx)
- [packages/tour/index.tsx](https://github.com/elrumordelaluz/reactour/blob/f38832ffd0b610e98dbed01d9dff6b058b1ec1a4/packages/tour/index.tsx)
- [packages/utils/index.tsx](https://github.com/elrumordelaluz/reactour/blob/f38832ffd0b610e98dbed01d9dff6b058b1ec1a4/packages/utils/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| apps package | library | Observed | Groups 34 file(s) under apps package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 24 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 51 file(s) under packages package (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.eslintrc.json` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/nextjs.yml` (ci)
- `.prettierrc.json` (config)
- `FUNDING.yml` (config)
- `apps/docs/package.json` (manifest)
- `apps/docs/tsconfig.json` (config)
- `apps/web/package.json` (manifest)
- `apps/web/public/manifest.json` (config)
- `apps/web/tsconfig.json` (config)
- `package.json` (manifest)
- `packages/config/package.json` (manifest)
- `packages/mask/package.json` (manifest)
- `packages/mask/tsconfig.json` (config)
- `packages/popover/package.json` (manifest)
- `packages/popover/tsconfig.json` (config)
- `packages/tour/package.json` (manifest)
- `packages/tour/tsconfig.json` (config)
- `packages/tsconfig/base.json` (config)
- `packages/tsconfig/nextjs.json` (config)
- `packages/tsconfig/package.json` (manifest)
- `packages/tsconfig/react-library.json` (config)
- `packages/utils/package.json` (manifest)
- `packages/utils/tsconfig.json` (config)
- `pnpm-workspace.yaml` (config)
- `turbo.json` (config)
- `vercel.json` (config)

## Top-level layout

- `apps` — 89 analysed file(s)
- `packages` — 85 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `.github` — 4 analysed file(s)
- `.changeset` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `f38832ffd0b610e98dbed01d9dff6b058b1ec1a4` is the revision these paths and observations refer to.
