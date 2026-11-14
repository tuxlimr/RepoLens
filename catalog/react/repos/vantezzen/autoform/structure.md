# Project structure: vantezzen/autoform

**Analysed commit:** `96bd1b7408465345ee715ad1491214d4ba1570e5`

**Commit reference:** [96bd1b7408465345ee715ad1491214d4ba1570e5](https://github.com/vantezzen/autoform/commit/96bd1b7408465345ee715ad1491214d4ba1570e5)

**Tree at this commit:** [vantezzen/autoform@96bd1b740846](https://github.com/vantezzen/autoform/tree/96bd1b7408465345ee715ad1491214d4ba1570e5)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | vantezzen/autoform |
| Description | 🌟 Automatically render forms for your existing data schema |
| Stars | 3494 |
| Forks | 147 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `96bd1b7408465345ee715ad1491214d4ba1570e5` |
| Retrieved at | 2026-11-14T19:15:17.538092+00:00 |
| Files in this snapshot | 585 |

## Directory tree

```text
.changeset/  (3 files)
  README.md
  config.json
  form-control-resolver.md
.github/  (1 files)
  workflows/  (1 files)
    cypress.yml
apps/  (262 files)
  docs/  (135 files)
    app/  (12 files)
      … 12 files under this directory
    components/  (80 files)
      … 80 files under this directory
    content/  (23 files)
      … 23 files under this directory
    lib/  (6 files)
      … 6 files under this directory
    styles/  (1 files)
      … 1 files under this directory
    .gitignore
    CHANGELOG.md
    LICENSE
    README.md
    cli.json
    mdx-components.tsx
    next-env.d.ts
    next.config.mjs
    package.json
    postcss.config.mjs
    proxy.ts
    source.config.ts
    tsconfig.json
  web/  (127 files)
    app/  (15 files)
      … 15 files under this directory
    components/  (9 files)
      … 9 files under this directory
    cypress/  (88 files)
      … 88 files under this directory
    public/  (5 files)
      … 5 files under this directory
    .eslintrc.js
    .gitignore
    CHANGELOG.md
    README.md
    cypress.config.ts
    next.config.mjs
    package.json
    postcss.config.cjs
    tailwind.config.ts
    tsconfig.json
packages/  (297 files)
  ant/  (25 files)
    src/  (17 files)
      … 17 files under this directory
    .eslintrc.cjs
    CHANGELOG.md
    LICENSE
    README.md
    package.json
    tsconfig.json
    tsconfig.lint.json
    tsdown.config.ts
  chakra/  (38 files)
    src/  (28 files)
      … 28 files under this directory
    .eslintrc.cjs
    .npmignore
    CHANGELOG.md
    LICENSE
    README.md
    package.json
    tsconfig.json
    tsconfig.lint.json
    tsconfig.node.json
    tsdown.config.ts
  core/  (14 files)
    src/  (5 files)
      … 5 files under this directory
    .eslintrc.cjs
    .npmignore
    CHANGELOG.md
    LICENSE
    README.md
    package.json
    tsconfig.json
    tsconfig.lint.json
    tsdown.config.ts
  eslint-config/  (6 files)
    CHANGELOG.md
    README.md
    library.js
    next.js
    package.json
    react-internal.js
  joi/  (17 files)
    src/  (8 files)
      … 8 files under this directory
    .eslintrc.cjs
    .npmignore
    CHANGELOG.md
    LICENSE
    README.md
    package.json
    tsconfig.json
    tsconfig.lint.json
    tsdown.config.ts
  mantine/  (26 files)
    src/  (17 files)
      … 17 files under this directory
    .eslintrc.cjs
    .npmignore
    CHANGELOG.md
    LICENSE
    README.md
    package.json
    tsconfig.json
    tsconfig.lint.json
    tsdown.config.ts
  mui/  (26 files)
    src/  (17 files)
      … 17 files under this directory
    .eslintrc.cjs
    .npmignore
    CHANGELOG.md
    LICENSE
    README.md
    package.json
    tsconfig.json
    tsconfig.lint.json
    tsdown.config.ts
  react/  (27 files)
    src/  (18 files)
      … 18 files under this directory
    .eslintrc.cjs
    .npmignore
    CHANGELOG.md
    LICENSE
    README.md
    package.json
    tsconfig.json
    tsconfig.lint.json
    tsdown.config.ts
  shadcn/  (63 files)
    registry/  (19 files)
      … 19 files under this directory
    src/  (33 files)
      … 33 files under this directory
    .eslintrc.cjs
    .npmignore
    CHANGELOG.md
    components.json
    package.json
    postcss.config.mjs
    tailwind.config.ts
    tsconfig.json
    tsconfig.lint.json
    tsconfig.node.json
    turbo.json
  typescript-config/  (5 files)
    CHANGELOG.md
    base.json
    nextjs.json
    package.json
    react-library.json
  yup/  (17 files)
    src/  (8 files)
      … 8 files under this directory
    .eslintrc.cjs
    .npmignore
    CHANGELOG.md
    LICENSE
    README.md
    package.json
    tsconfig.json
    tsconfig.lint.json
    tsdown.config.ts
  zod/  (33 files)
    src/  (24 files)
      … 24 files under this directory
    .eslintrc.cjs
    .npmignore
    CHANGELOG.md
    LICENSE
    README.md
    package.json
    tsconfig.json
    tsconfig.lint.json
    tsdown.config.ts
scripts/  (1 files)
  check-package-boundaries.mjs
skills/  (12 files)
  autoform/  (12 files)
    references/  (10 files)
      … 10 files under this directory
    README.md
    SKILL.md
.gitattributes
.gitignore
.nvmrc
LICENSE
README.md
package.json
pnpm-workspace.yaml
registry.json
turbo.json
```

## Entry points

- [apps/web/app/page.tsx](https://github.com/vantezzen/autoform/blob/96bd1b7408465345ee715ad1491214d4ba1570e5/apps/web/app/page.tsx)
- [packages/core/src/index.ts](https://github.com/vantezzen/autoform/blob/96bd1b7408465345ee715ad1491214d4ba1570e5/packages/core/src/index.ts)
- [packages/joi/src/index.ts](https://github.com/vantezzen/autoform/blob/96bd1b7408465345ee715ad1491214d4ba1570e5/packages/joi/src/index.ts)
- [packages/react/src/index.tsx](https://github.com/vantezzen/autoform/blob/96bd1b7408465345ee715ad1491214d4ba1570e5/packages/react/src/index.tsx)
- [packages/yup/src/index.ts](https://github.com/vantezzen/autoform/blob/96bd1b7408465345ee715ad1491214d4ba1570e5/packages/yup/src/index.ts)
- [packages/zod/src/index.ts](https://github.com/vantezzen/autoform/blob/96bd1b7408465345ee715ad1491214d4ba1570e5/packages/zod/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| apps package | library | Observed | Groups 102 file(s) under apps package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 73 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 191 file(s) under packages package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 7 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 12 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.github/workflows/cypress.yml` (ci)
- `apps/docs/cli.json` (config)
- `apps/docs/content/docs/meta.json` (config)
- `apps/docs/content/docs/react/meta.json` (config)
- `apps/docs/content/docs/schema-providers/meta.json` (config)
- `apps/docs/content/docs/tanstack/meta.json` (config)
- `apps/docs/content/docs/technical/meta.json` (config)
- `apps/docs/package.json` (manifest)
- `apps/docs/tsconfig.json` (config)
- `apps/web/cypress/fixtures/example.json` (config)
- `apps/web/package.json` (manifest)
- `apps/web/tsconfig.json` (config)
- `package.json` (manifest)
- `packages/ant/package.json` (manifest)
- `packages/ant/tsconfig.json` (config)
- `packages/ant/tsconfig.lint.json` (config)
- `packages/chakra/package.json` (manifest)
- `packages/chakra/tsconfig.json` (config)
- `packages/chakra/tsconfig.lint.json` (config)
- `packages/chakra/tsconfig.node.json` (config)
- `packages/core/package.json` (manifest)
- `packages/core/tsconfig.json` (config)
- `packages/core/tsconfig.lint.json` (config)
- `packages/eslint-config/package.json` (manifest)
- `packages/joi/package.json` (manifest)
- `packages/joi/tsconfig.json` (config)
- `packages/joi/tsconfig.lint.json` (config)
- `packages/mantine/package.json` (manifest)
- `packages/mantine/tsconfig.json` (config)
- `packages/mantine/tsconfig.lint.json` (config)
- `packages/mui/package.json` (manifest)
- `packages/mui/tsconfig.json` (config)
- `packages/mui/tsconfig.lint.json` (config)
- `packages/react/package.json` (manifest)
- `packages/react/tsconfig.json` (config)
- `packages/react/tsconfig.lint.json` (config)
- `packages/shadcn/components.json` (config)
- `packages/shadcn/package.json` (manifest)
- `packages/shadcn/registry/autoform-react-source-rhf.json` (config)
- `packages/shadcn/registry/autoform-react-source-tanstack.json` (config)
- `packages/shadcn/registry/autoform-rhf.json` (config)
- `packages/shadcn/registry/autoform-tanstack.json` (config)
- `packages/shadcn/registry/custom-fields-demo.json` (config)
- `packages/shadcn/registry/dialog-submit-demo.json` (config)
- `packages/shadcn/registry/ecommerce-checkout-demo.json` (config)
- `packages/shadcn/registry/interactive-schema-demo.json` (config)
- `packages/shadcn/registry/multistep-form-demo.json` (config)
- `packages/shadcn/registry/nested-autoform-demo.json` (config)
- `packages/shadcn/registry/realtime-validation-demo.json` (config)
- `packages/shadcn/registry/registry.json` (config)
- `packages/shadcn/registry/tanstack-custom-fields-demo.json` (config)
- `packages/shadcn/registry/tanstack-dialog-submit-demo.json` (config)
- `packages/shadcn/registry/tanstack-ecommerce-checkout-demo.json` (config)
- `packages/shadcn/registry/tanstack-interactive-schema-demo.json` (config)
- `packages/shadcn/registry/tanstack-multistep-form-demo.json` (config)
- `packages/shadcn/registry/tanstack-nested-autoform-demo.json` (config)
- `packages/shadcn/registry/tanstack-realtime-validation-demo.json` (config)
- `packages/shadcn/tsconfig.json` (config)
- `packages/shadcn/tsconfig.lint.json` (config)
- `packages/shadcn/tsconfig.node.json` (config)
- `packages/shadcn/turbo.json` (config)
- `packages/typescript-config/base.json` (config)
- `packages/typescript-config/nextjs.json` (config)
- `packages/typescript-config/package.json` (manifest)
- `packages/typescript-config/react-library.json` (config)
- `packages/yup/package.json` (manifest)
- `packages/yup/tsconfig.json` (config)
- `packages/yup/tsconfig.lint.json` (config)
- `packages/zod/package.json` (manifest)
- `packages/zod/tsconfig.json` (config)
- `packages/zod/tsconfig.lint.json` (config)
- `pnpm-workspace.yaml` (config)
- `registry.json` (config)
- `turbo.json` (config)

## Top-level layout

- `packages` — 297 analysed file(s)
- `apps` — 262 analysed file(s)
- `skills` — 12 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `.changeset` — 3 analysed file(s)
- `.github` — 1 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `96bd1b7408465345ee715ad1491214d4ba1570e5` is the revision these paths and observations refer to.
