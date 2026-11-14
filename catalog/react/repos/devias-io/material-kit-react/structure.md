# Project structure: devias-io/material-kit-react

**Analysed commit:** `6423e1a2f092c50d7e1e22f3e43344df02af41de`

**Commit reference:** [6423e1a2f092c50d7e1e22f3e43344df02af41de](https://github.com/devias-io/material-kit-react/commit/6423e1a2f092c50d7e1e22f3e43344df02af41de)

**Tree at this commit:** [devias-io/material-kit-react@6423e1a2f092](https://github.com/devias-io/material-kit-react/tree/6423e1a2f092c50d7e1e22f3e43344df02af41de)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | devias-io/material-kit-react |
| Description | React Dashboard made with Material UI’s components. Our pro template contains features like TypeScript version, authentication system with Firebase and Auth0 plus many other  |
| Stars | 5581 |
| Forks | 2551 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `6423e1a2f092c50d7e1e22f3e43344df02af41de` |
| Retrieved at | 2026-11-14T19:14:16.298987+00:00 |
| Files in this snapshot | 97 |

## Directory tree

```text
public/  (4 files)
  assets/  (4 files)
    logo--dark.svg
    logo-emblem--dark.svg
    logo-emblem.svg
    logo.svg
src/  (80 files)
  app/  (13 files)
    auth/  (3 files)
      … 3 files under this directory
    dashboard/  (6 files)
      … 6 files under this directory
    errors/  (1 files)
      … 1 files under this directory
    layout.tsx
    not-found.tsx
    page.tsx
  components/  (34 files)
    auth/  (6 files)
      … 6 files under this directory
    core/  (6 files)
      … 6 files under this directory
    dashboard/  (22 files)
      … 22 files under this directory
  contexts/  (1 files)
    user-context.tsx
  hooks/  (3 files)
    use-popover.ts
    use-selection.ts
    use-user.ts
  lib/  (5 files)
    auth/  (1 files)
      … 1 files under this directory
    default-logger.ts
    get-site-url.ts
    is-nav-item-active.ts
    logger.ts
  styles/  (20 files)
    theme/  (19 files)
      … 19 files under this directory
    global.css
  types/  (2 files)
    nav.d.ts
    user.ts
  config.ts
  paths.ts
.editorconfig
.gitattributes
.gitignore
.prettierignore
CHANGELOG.md
LICENSE.md
README.md
eslint.config.mjs
next-env.d.ts
next.config.mjs
package.json
prettier.config.mjs
tsconfig.json
```

## Entry points

- [src/app/dashboard/page.tsx](https://github.com/devias-io/material-kit-react/blob/6423e1a2f092c50d7e1e22f3e43344df02af41de/src/app/dashboard/page.tsx)
- [src/app/page.tsx](https://github.com/devias-io/material-kit-react/blob/6423e1a2f092c50d7e1e22f3e43344df02af41de/src/app/page.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| app package | library | Observed | Groups 11 file(s) under app package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 24 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| config.ts package | library | Observed | Groups 1 file(s) under config.ts package (observed from repository paths and static analysis). |
| contexts package | library | Observed | Groups 1 file(s) under contexts package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 3 file(s) under external integrations (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 3 file(s) under hooks package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 5 file(s) under lib package (observed from repository paths and static analysis). |
| paths.ts package | library | Observed | Groups 1 file(s) under paths.ts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 6 file(s) under service / domain layer (observed from repository paths and static analysis). |
| styles package | library | Observed | Groups 19 file(s) under styles package (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 2 file(s) under types package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `src` — 80 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `public` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `6423e1a2f092c50d7e1e22f3e43344df02af41de` is the revision these paths and observations refer to.
