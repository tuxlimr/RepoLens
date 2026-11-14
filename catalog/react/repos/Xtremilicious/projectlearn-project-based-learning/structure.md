# Project structure: Xtremilicious/projectlearn-project-based-learning

**Analysed commit:** `5f5f694ebd0209679c10fdc96f437c821157ee56`

**Commit reference:** [5f5f694ebd0209679c10fdc96f437c821157ee56](https://github.com/Xtremilicious/projectlearn-project-based-learning/commit/5f5f694ebd0209679c10fdc96f437c821157ee56)

**Tree at this commit:** [Xtremilicious/projectlearn-project-based-learning@5f5f694ebd02](https://github.com/Xtremilicious/projectlearn-project-based-learning/tree/5f5f694ebd0209679c10fdc96f437c821157ee56)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Xtremilicious/projectlearn-project-based-learning |
| Description | A curated list of project tutorials for project-based learning. |
| Stars | 6403 |
| Forks | 539 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `5f5f694ebd0209679c10fdc96f437c821157ee56` |
| Retrieved at | 2026-11-14T19:14:06.092570+00:00 |
| Files in this snapshot | 89 |

## Directory tree

```text
pages/  (18 files)
  api/  (3 files)
    auth/  (1 files)
      … 1 files under this directory
    github/  (1 files)
      … 1 files under this directory
    init-analytics.ts
  blog/  (2 files)
    [slug].tsx
    index.tsx
  contribute/  (1 files)
    index.tsx
  learn/  (8 files)
    game-development/  (2 files)
      … 2 files under this directory
    machine-learning-and-ai/  (2 files)
      … 2 files under this directory
    mobile-development/  (2 files)
      … 2 files under this directory
    web-development/  (2 files)
      … 2 files under this directory
  _app.tsx
  _document.tsx
  index.tsx
  learn.tsx
posts/  (1 files)
  projectlearn-project-based-learning.md
public/  (4 files)
  img/  (1 files)
    art.svg
  static/  (1 files)
    images/  (1 files)
      … 1 files under this directory
  data.json
  robots.txt
src/  (50 files)
  components/  (37 files)
    blog/  (3 files)
      … 3 files under this directory
    dashboard/  (10 files)
      … 10 files under this directory
    landing/  (6 files)
      … 6 files under this directory
    ui/  (16 files)
      … 16 files under this directory
    GitHubLogin.tsx
    theme-provider.tsx
  images/  (1 files)
    pl-splash.svg
  lib/  (2 files)
    analytics.js
    utils.ts
  redux/  (4 files)
    actions/  (1 files)
      … 1 files under this directory
    reducers/  (1 files)
      … 1 files under this directory
    store.ts
    types.ts
  utils/  (6 files)
    data.ts
    functions.ts
    generate_readme.ts
    generate_sitemap.ts
    styles.ts
    technologies.ts
styles/  (3 files)
  contribute.module.scss
  globals.css
  markdown-styles.module.scss
.babelrc
.gitignore
CONTRIBUTE.md
LICENSE
README.md
components.json
gulpfile.mjs
next-env.d.ts
next.config.js
package.json
postcss.config.js
tailwind.config.js
tsconfig.json
```

## Entry points

- [pages/blog/index.tsx](https://github.com/Xtremilicious/projectlearn-project-based-learning/blob/5f5f694ebd0209679c10fdc96f437c821157ee56/pages/blog/index.tsx)
- [pages/contribute/index.tsx](https://github.com/Xtremilicious/projectlearn-project-based-learning/blob/5f5f694ebd0209679c10fdc96f437c821157ee56/pages/contribute/index.tsx)
- [pages/index.tsx](https://github.com/Xtremilicious/projectlearn-project-based-learning/blob/5f5f694ebd0209679c10fdc96f437c821157ee56/pages/index.tsx)
- [pages/learn/game-development/index.tsx](https://github.com/Xtremilicious/projectlearn-project-based-learning/blob/5f5f694ebd0209679c10fdc96f437c821157ee56/pages/learn/game-development/index.tsx)
- [pages/learn/machine-learning-and-ai/index.tsx](https://github.com/Xtremilicious/projectlearn-project-based-learning/blob/5f5f694ebd0209679c10fdc96f437c821157ee56/pages/learn/machine-learning-and-ai/index.tsx)
- [pages/learn/mobile-development/index.tsx](https://github.com/Xtremilicious/projectlearn-project-based-learning/blob/5f5f694ebd0209679c10fdc96f437c821157ee56/pages/learn/mobile-development/index.tsx)
- [pages/learn/web-development/index.tsx](https://github.com/Xtremilicious/projectlearn-project-based-learning/blob/5f5f694ebd0209679c10fdc96f437c821157ee56/pages/learn/web-development/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 3 file(s) under api layer (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 37 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 5 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 2 file(s) under lib package (observed from repository paths and static analysis). |
| pages package | library | Observed | Groups 15 file(s) under pages package (observed from repository paths and static analysis). |
| redux package | library | Observed | Groups 4 file(s) under redux package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 6 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `components.json` (config)
- `package.json` (manifest)
- `public/data.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `src` — 50 analysed file(s)
- `pages` — 18 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `public` — 4 analysed file(s)
- `styles` — 3 analysed file(s)
- `posts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `5f5f694ebd0209679c10fdc96f437c821157ee56` is the revision these paths and observations refer to.
