# Project structure: shuding/nextra

**Analysed commit:** `d6e80e1dd627b781429a6ee989b15ebba688c8ea`

**Commit reference:** [d6e80e1dd627b781429a6ee989b15ebba688c8ea](https://github.com/shuding/nextra/commit/d6e80e1dd627b781429a6ee989b15ebba688c8ea)

**Tree at this commit:** [shuding/nextra@d6e80e1dd627](https://github.com/shuding/nextra/tree/d6e80e1dd627b781429a6ee989b15ebba688c8ea)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | shuding/nextra |
| Description | Simple, powerful and flexible site generation framework with everything you love from Next.js. |
| Stars | 13954 |
| Forks | 1406 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `d6e80e1dd627b781429a6ee989b15ebba688c8ea` |
| Retrieved at | 2026-11-14T19:13:18.802217+00:00 |
| Files in this snapshot | 749 |

## Directory tree

```text
.changeset/  (1 files)
  config.json
.github/  (7 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (3 files)
    lint.yml
    release.yml
    test.yml
  CODE_OF_CONDUCT.md
  PULL_REQUEST_TEMPLATE.md
docs/  (130 files)
  app/  (75 files)
    _components/  (6 files)
      … 6 files under this directory
    about/  (1 files)
      … 1 files under this directory
    api/  (2 files)
      … 2 files under this directory
    blog/  (1 files)
      … 1 files under this directory
    docs/  (52 files)
      … 52 files under this directory
    og/  (1 files)
      … 1 files under this directory
    showcase/  (2 files)
      … 2 files under this directory
    sponsors/  (1 files)
      … 1 files under this directory
    _meta.global.tsx
    env.d.ts
    globals.css
    icon.svg
    layout.tsx
    not-found.ts
    page.css
    page.module.css
    page.tsx
  components/  (46 files)
    _table/  (2 files)
      … 2 files under this directory
    icons/  (31 files)
      … 31 files under this directory
    _slider.tsx
    content-and-app-file-tree.tsx
    example-code.tsx
    example-tsdoc.mdx
    generate-api-reference.ts
    get-page-map.ts
    inkeep-chat-button.tsx
    install-nextra-theme.mdx
    playground-demo.tsx
    ready-to-go.mdx
    shadow.jsx
    toggle-visibility-section.tsx
    video.tsx
  public/  (2 files)
    assets/  (1 files)
      … 1 files under this directory
    logo.svg
  mdx-components.tsx
  next-sitemap.config.js
  next.config.ts
  package.json
  postcss.config.mjs
  tsconfig.json
  vercel.json
examples/  (235 files)
  blog/  (17 files)
    app/  (14 files)
      … 14 files under this directory
    mdx-components.jsx
    next.config.js
    package.json
  custom-theme/  (16 files)
    app/  (11 files)
      … 11 files under this directory
    public/  (1 files)
      … 1 files under this directory
    mdx-components.jsx
    next.config.ts
    package.json
    tsconfig.json
  docs/  (33 files)
    src/  (30 files)
      … 30 files under this directory
    mdx-components.js
    next.config.mjs
    package.json
  swr-site/  (169 files)
    app/  (36 files)
      … 36 files under this directory
    content/  (114 files)
      … 114 files under this directory
    nextra-remote-filepaths/  (3 files)
      … 3 files under this directory
    public/  (8 files)
      … 8 files under this directory
    README.md
    mdx-components.ts
    next.config.ts
    package.json
    postcss.config.js
    proxy.ts
    tsconfig.json
    vercel.json
packages/  (360 files)
  esbuild-react-compiler-plugin/  (5 files)
    src/  (2 files)
      … 2 files under this directory
    package.json
    tsconfig.json
    tsup.config.ts
  eslint-config/  (4 files)
    src/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    package.json
    tsconfig.json
  nextra/  (248 files)
    src/  (233 files)
      … 233 files under this directory
    styles/  (7 files)
      … 7 files under this directory
    CHANGELOG.md
    default-entry.ts
    loader.cjs
    package.json
    setup-files.ts
    tsconfig.json
    tsup.config.ts
    vitest.config.ts
  nextra-theme-blog/  (24 files)
    __test__/  (1 files)
      … 1 files under this directory
    src/  (15 files)
      … 15 files under this directory
    CHANGELOG.md
    LICENSE
    README.md
    package.json
    postcss.config.mjs
    tsconfig.json
    tsup.config.ts
    vitest.config.mts
  nextra-theme-docs/  (52 files)
    css/  (2 files)
      … 2 files under this directory
    src/  (40 files)
      … 40 files under this directory
    CHANGELOG.md
    LICENSE
    README.md
    package.json
    postcss.config.mjs
    setup-files.ts
    tailwind.config.ts
    tsconfig.json
    tsup.config.ts
    vitest.config.mts
  prettier-config/  (3 files)
    src/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    package.json
  tsdoc/  (24 files)
    src/  (19 files)
      … 19 files under this directory
    README.md
    package.json
    tsconfig.json
    tsup.config.ts
    vitest.config.ts
patches/  (5 files)
  @changesets__assemble-release-plan.patch
  esbuild-plugin-svgr.patch
  eslint-plugin-tailwindcss.patch
  next.patch
  tsup.patch
.editorconfig
.gitignore
.node-version
.prettierignore
LICENSE
README.md
package.json
pnpm-workspace.yaml
prettier.config.mjs
renovate.json5
turbo.jsonc
```

## Entry points

- [packages/esbuild-react-compiler-plugin/src/index.ts](https://github.com/shuding/nextra/blob/d6e80e1dd627b781429a6ee989b15ebba688c8ea/packages/esbuild-react-compiler-plugin/src/index.ts)
- [packages/eslint-config/src/index.ts](https://github.com/shuding/nextra/blob/d6e80e1dd627b781429a6ee989b15ebba688c8ea/packages/eslint-config/src/index.ts)
- [packages/nextra-theme-blog/src/index.ts](https://github.com/shuding/nextra/blob/d6e80e1dd627b781429a6ee989b15ebba688c8ea/packages/nextra-theme-blog/src/index.ts)
- [packages/nextra-theme-docs/src/index.ts](https://github.com/shuding/nextra/blob/d6e80e1dd627b781429a6ee989b15ebba688c8ea/packages/nextra-theme-docs/src/index.ts)
- [packages/prettier-config/src/index.js](https://github.com/shuding/nextra/blob/d6e80e1dd627b781429a6ee989b15ebba688c8ea/packages/prettier-config/src/index.js)
- [packages/tsdoc/src/index.ts](https://github.com/shuding/nextra/blob/d6e80e1dd627b781429a6ee989b15ebba688c8ea/packages/tsdoc/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 27 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 54 file(s) under external integrations (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 170 file(s) under packages package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.editorconfig` (config)
- `.github/workflows/lint.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `docs/package.json` (manifest)
- `docs/tsconfig.json` (config)
- `docs/vercel.json` (config)
- `examples/blog/package.json` (manifest)
- `examples/custom-theme/package.json` (manifest)
- `examples/custom-theme/tsconfig.json` (config)
- `examples/docs/package.json` (manifest)
- `examples/swr-site/nextra-remote-filepaths/graphql-eslint.json` (config)
- `examples/swr-site/nextra-remote-filepaths/graphql-yoga.json` (config)
- `examples/swr-site/package.json` (manifest)
- `examples/swr-site/tsconfig.json` (config)
- `examples/swr-site/vercel.json` (config)
- `package.json` (manifest)
- `packages/esbuild-react-compiler-plugin/package.json` (manifest)
- `packages/esbuild-react-compiler-plugin/tsconfig.json` (config)
- `packages/eslint-config/package.json` (manifest)
- `packages/eslint-config/tsconfig.json` (config)
- `packages/nextra-theme-blog/package.json` (manifest)
- `packages/nextra-theme-blog/tsconfig.json` (config)
- `packages/nextra-theme-docs/package.json` (manifest)
- `packages/nextra-theme-docs/tsconfig.json` (config)
- `packages/nextra/package.json` (manifest)
- `packages/nextra/tsconfig.json` (config)
- `packages/prettier-config/package.json` (manifest)
- `packages/tsdoc/package.json` (manifest)
- `packages/tsdoc/src/__tests__/snapshots/flattened.json` (config)
- `packages/tsdoc/src/__tests__/snapshots/get-smooth-step-path.json` (config)
- `packages/tsdoc/src/__tests__/snapshots/get-viewport-for-bounds.json` (config)
- `packages/tsdoc/src/__tests__/snapshots/head.json` (config)
- `packages/tsdoc/src/__tests__/snapshots/layout-props.json` (config)
- `packages/tsdoc/src/__tests__/snapshots/navbar.json` (config)
- `packages/tsdoc/src/__tests__/snapshots/nextra-config.json` (config)
- `packages/tsdoc/src/__tests__/snapshots/react-flow-instance.json` (config)
- `packages/tsdoc/src/__tests__/snapshots/search.json` (config)
- `packages/tsdoc/src/__tests__/snapshots/use-config.json` (config)
- `packages/tsdoc/src/__tests__/snapshots/use-edges-state.json` (config)
- `packages/tsdoc/src/__tests__/snapshots/use-theme-config.json` (config)
- `packages/tsdoc/tsconfig.json` (config)
- `pnpm-workspace.yaml` (config)

## Top-level layout

- `packages` — 360 analysed file(s)
- `examples` — 235 analysed file(s)
- `docs` — 130 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `.github` — 7 analysed file(s)
- `patches` — 5 analysed file(s)
- `.changeset` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `d6e80e1dd627b781429a6ee989b15ebba688c8ea` is the revision these paths and observations refer to.
