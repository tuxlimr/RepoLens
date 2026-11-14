# Project structure: darkroomengineering/lenis

**Analysed commit:** `bd89165aa6ab64c4ae68242c8d2a5e90b76ff77d`

**Commit reference:** [bd89165aa6ab64c4ae68242c8d2a5e90b76ff77d](https://github.com/darkroomengineering/lenis/commit/bd89165aa6ab64c4ae68242c8d2a5e90b76ff77d)

**Tree at this commit:** [darkroomengineering/lenis@bd89165aa6ab](https://github.com/darkroomengineering/lenis/tree/bd89165aa6ab64c4ae68242c8d2a5e90b76ff77d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | darkroomengineering/lenis |
| Description | Smooth scroll as it should be |
| Stars | 17264 |
| Forks | 792 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `bd89165aa6ab64c4ae68242c8d2a5e90b76ff77d` |
| Retrieved at | 2026-11-14T19:13:13.156652+00:00 |
| Files in this snapshot | 108 |

## Directory tree

```text
.github/  (5 files)
  ISSUE_TEMPLATE/  (1 files)
    bug_report.md
  workflows/  (1 files)
    ci.yml
  CODEOWNERS
  FUNDING.yml
  dependabot.yml
.vscode/  (2 files)
  extensions.json
  settings.json
packages/  (41 files)
  core/  (13 files)
    src/  (8 files)
      … 8 files under this directory
    test/  (1 files)
      … 1 files under this directory
    browser.ts
    index.ts
    lenis.css
    package.json
  react/  (7 files)
    src/  (4 files)
      … 4 files under this directory
    README.md
    index.ts
    package.json
  snap/  (11 files)
    src/  (5 files)
      … 5 files under this directory
    test/  (2 files)
      … 2 files under this directory
    README.md
    browser.ts
    index.ts
    package.json
  vue/  (10 files)
    nuxt/  (4 files)
      … 4 files under this directory
    src/  (3 files)
      … 3 files under this directory
    README.md
    index.ts
    package.json
playground/  (50 files)
  core/  (4 files)
    browser.js
    static.html
    style.css
    test.ts
  horizontal/  (4 files)
    browser.js
    static.html
    style.css
    test.ts
  infinite/  (4 files)
    browser.js
    static.html
    style.css
    test.ts
  nuxt/  (12 files)
    components/  (1 files)
      … 1 files under this directory
    pages/  (2 files)
      … 2 files under this directory
    plugins/  (1 files)
      … 1 files under this directory
    public/  (1 files)
      … 1 files under this directory
    server/  (1 files)
      … 1 files under this directory
    .gitignore
    README.md
    app.vue
    nuxt.config.ts
    package.json
    tsconfig.json
  react/  (2 files)
    app.tsx
    style.css
  snap/  (2 files)
    style.css
    test.ts
  touch-debug/  (1 files)
    test.ts
  vue/  (5 files)
    App.vue
    Child.vue
    InnerChild.vue
    setup.ts
    style.css
  www/  (11 files)
    layouts/  (1 files)
      … 1 files under this directory
    pages/  (10 files)
      … 10 files under this directory
  .gitignore
  astro.config.mjs
  package.json
  stats-js.d.ts
  tsconfig.json
scripts/  (1 files)
  update-readme.js
.gitignore
CONTRIBUTING.md
LICENSE
MANIFESTO.md
README.md
V2-ROADMAP.md
package.json
tsconfig.json
vite.config.ts
```

## Entry points

- [packages/core/index.ts](https://github.com/darkroomengineering/lenis/blob/bd89165aa6ab64c4ae68242c8d2a5e90b76ff77d/packages/core/index.ts)
- [packages/react/index.ts](https://github.com/darkroomengineering/lenis/blob/bd89165aa6ab64c4ae68242c8d2a5e90b76ff77d/packages/react/index.ts)
- [packages/snap/index.ts](https://github.com/darkroomengineering/lenis/blob/bd89165aa6ab64c4ae68242c8d2a5e90b76ff77d/packages/snap/index.ts)
- [packages/vue/index.ts](https://github.com/darkroomengineering/lenis/blob/bd89165aa6ab64c4ae68242c8d2a5e90b76ff77d/packages/vue/index.ts)
- [playground/react/app.tsx](https://github.com/darkroomengineering/lenis/blob/bd89165aa6ab64c4ae68242c8d2a5e90b76ff77d/playground/react/app.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 11 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 20 file(s) under packages package (observed from repository paths and static analysis). |
| playground package | library | Observed | Groups 19 file(s) under playground package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 12 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 3 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.vscode/extensions.json` (config)
- `.vscode/settings.json` (config)
- `package.json` (manifest)
- `packages/core/package.json` (manifest)
- `packages/react/package.json` (manifest)
- `packages/snap/package.json` (manifest)
- `packages/vue/package.json` (manifest)
- `playground/nuxt/package.json` (manifest)
- `playground/nuxt/server/tsconfig.json` (config)
- `playground/nuxt/tsconfig.json` (config)
- `playground/package.json` (manifest)
- `playground/tsconfig.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `playground` — 50 analysed file(s)
- `packages` — 41 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `.github` — 5 analysed file(s)
- `.vscode` — 2 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `bd89165aa6ab64c4ae68242c8d2a5e90b76ff77d` is the revision these paths and observations refer to.
