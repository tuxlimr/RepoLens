# Project structure: alan2207/bulletproof-react

**Analysed commit:** `9506629ed003a561c6627735480cce4994244bb4`

**Commit reference:** [9506629ed003a561c6627735480cce4994244bb4](https://github.com/alan2207/bulletproof-react/commit/9506629ed003a561c6627735480cce4994244bb4)

**Tree at this commit:** [alan2207/bulletproof-react@9506629ed003](https://github.com/alan2207/bulletproof-react/tree/9506629ed003a561c6627735480cce4994244bb4)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | alan2207/bulletproof-react |
| Description | 🛡️ ⚛️ A simple, scalable, and powerful architecture for building production ready React applications.  |
| Stars | 36080 |
| Forks | 3277 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `9506629ed003a561c6627735480cce4994244bb4` |
| Retrieved at | 2026-11-14T19:13:00.884070+00:00 |
| Files in this snapshot | 519 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (3 files)
    nextjs-app-ci.yml
    nextjs-pages-ci.yml
    react-vite-ci.yml
.husky/  (1 files)
  pre-commit
apps/  (497 files)
  nextjs-app/  (167 files)
    .storybook/  (2 files)
      … 2 files under this directory
    .vscode/  (2 files)
      … 2 files under this directory
    __mocks__/  (2 files)
      … 2 files under this directory
    e2e/  (4 files)
      … 4 files under this directory
    generators/  (4 files)
      … 4 files under this directory
    public/  (4 files)
      … 4 files under this directory
    src/  (131 files)
      … 131 files under this directory
    .env.example
    .eslintrc.cjs
    .gitignore
    .prettierignore
    .prettierrc
    README.md
    index.html
    lint-staged.config.mjs
    mock-server.ts
    next-env.d.ts
    next.config.mjs
    package.json
    playwright.config.ts
    plopfile.cjs
    postcss.config.cjs
    tailwind.config.cjs
    tsconfig.json
    vitest.config.ts
  nextjs-pages/  (167 files)
    .storybook/  (2 files)
      … 2 files under this directory
    .vscode/  (2 files)
      … 2 files under this directory
    __mocks__/  (2 files)
      … 2 files under this directory
    e2e/  (4 files)
      … 4 files under this directory
    generators/  (4 files)
      … 4 files under this directory
    public/  (4 files)
      … 4 files under this directory
    src/  (132 files)
      … 132 files under this directory
    .env.example
    .eslintrc.cjs
    .gitignore
    .prettierignore
    .prettierrc
    README.md
    lint-staged.config.mjs
    mock-server.ts
    next-env.d.ts
    next.config.mjs
    package.json
    playwright.config.ts
    plopfile.cjs
    postcss.config.cjs
    tailwind.config.cjs
    tsconfig.json
    vitest.config.ts
  react-vite/  (163 files)
    .storybook/  (2 files)
      … 2 files under this directory
    .vscode/  (2 files)
      … 2 files under this directory
    __mocks__/  (2 files)
      … 2 files under this directory
    e2e/  (4 files)
      … 4 files under this directory
    generators/  (4 files)
      … 4 files under this directory
    public/  (3 files)
      … 3 files under this directory
    src/  (130 files)
      … 130 files under this directory
    .env.example
    .eslintrc.cjs
    .gitignore
    .prettierignore
    .prettierrc
    README.md
    index.html
    mock-server.ts
    package.json
    playwright.config.ts
    plopfile.cjs
    postcss.config.cjs
    tailwind.config.cjs
    tsconfig.json
    vite-env.d.ts
    vite.config.ts
docs/  (13 files)
  assets/  (1 files)
    logo.svg
  additional-resources.md
  api-layer.md
  application-overview.md
  components-and-styling.md
  deployment.md
  error-handling.md
  performance.md
  project-standards.md
  project-structure.md
  security.md
  state-management.md
  testing.md
.gitignore
AGENTS.md
LICENSE
README.md
package.json
```

## Entry points

- [apps/nextjs-app/.storybook/main.ts](https://github.com/alan2207/bulletproof-react/blob/9506629ed003a561c6627735480cce4994244bb4/apps/nextjs-app/.storybook/main.ts)
- [apps/nextjs-pages/.storybook/main.ts](https://github.com/alan2207/bulletproof-react/blob/9506629ed003a561c6627735480cce4994244bb4/apps/nextjs-pages/.storybook/main.ts)
- [apps/react-vite/.storybook/main.ts](https://github.com/alan2207/bulletproof-react/blob/9506629ed003a561c6627735480cce4994244bb4/apps/react-vite/.storybook/main.ts)
- [apps/react-vite/src/main.tsx](https://github.com/alan2207/bulletproof-react/blob/9506629ed003a561c6627735480cce4994244bb4/apps/react-vite/src/main.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 66 file(s) under api layer (observed from repository paths and static analysis). |
| apps package | library | Observed | Groups 366 file(s) under apps package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 22 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 9 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/nextjs-app-ci.yml` (ci)
- `.github/workflows/nextjs-pages-ci.yml` (ci)
- `.github/workflows/react-vite-ci.yml` (ci)
- `apps/nextjs-app/.env.example` (config)
- `apps/nextjs-app/.vscode/extensions.json` (config)
- `apps/nextjs-app/.vscode/settings.json` (config)
- `apps/nextjs-app/package.json` (manifest)
- `apps/nextjs-app/tsconfig.json` (config)
- `apps/nextjs-pages/.env.example` (config)
- `apps/nextjs-pages/.vscode/extensions.json` (config)
- `apps/nextjs-pages/.vscode/settings.json` (config)
- `apps/nextjs-pages/package.json` (manifest)
- `apps/nextjs-pages/tsconfig.json` (config)
- `apps/react-vite/.env.example` (config)
- `apps/react-vite/.vscode/extensions.json` (config)
- `apps/react-vite/.vscode/settings.json` (config)
- `apps/react-vite/package.json` (manifest)
- `apps/react-vite/tsconfig.json` (config)
- `package.json` (manifest)

## Top-level layout

- `apps` — 497 analysed file(s)
- `docs` — 13 analysed file(s)
- `(root files)` — 5 analysed file(s)
- `.github` — 3 analysed file(s)
- `.husky` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 3 file(s) were skipped during inventory (3 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `9506629ed003a561c6627735480cce4994244bb4` is the revision these paths and observations refer to.
