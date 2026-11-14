# Project structure: Blazity/next-enterprise

**Analysed commit:** `97c4f3ed6be0a5b255d0e71606c7b355138281a9`

**Commit reference:** [97c4f3ed6be0a5b255d0e71606c7b355138281a9](https://github.com/Blazity/next-enterprise/commit/97c4f3ed6be0a5b255d0e71606c7b355138281a9)

**Tree at this commit:** [Blazity/next-enterprise@97c4f3ed6be0](https://github.com/Blazity/next-enterprise/tree/97c4f3ed6be0a5b255d0e71606c7b355138281a9)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Blazity/next-enterprise |
| Description | 💼 An enterprise-grade Next.js boilerplate for high-performance, maintainable apps. Packed with features like Tailwind CSS, TypeScript, ESLint, Prettier, testing tools, and more to accelerate your development. |
| Stars | 7472 |
| Forks | 1941 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `97c4f3ed6be0a5b255d0e71606c7b355138281a9` |
| Retrieved at | 2026-11-14T19:13:50.360462+00:00 |
| Files in this snapshot | 44 |

## Directory tree

```text
.github/  (4 files)
  workflows/  (3 files)
    check.yml
    nextjs_bundle_analysis.yml
    playwright.yml
  nodejs.version
.storybook/  (2 files)
  main.ts
  preview.ts
.vscode/  (1 files)
  settings.json
app/  (3 files)
  api/  (1 files)
    health/  (1 files)
      … 1 files under this directory
  layout.tsx
  page.tsx
assets/  (2 files)
  blazity-logo-dark.svg
  blazity-logo-light.svg
components/  (4 files)
  Button/  (3 files)
    Button.stories.tsx
    Button.test.tsx
    Button.tsx
  Tooltip/  (1 files)
    Tooltip.tsx
e2e/  (1 files)
  example.spec.ts
styles/  (1 files)
  tailwind.css
.all-contributorsrc
.gitignore
.pre-commit-config.yaml
.prettierignore
.releaserc
LICENSE
README.md
env.mjs
eslint.config.mjs
git-conventional-commits.yaml
graph.svg
instrumentation.ts
lp-items.tsx
next-env.d.ts
next.config.ts
package.json
playwright.config.ts
postcss.config.js
prettier.config.js
renovate.json
report-bundle-size.js
reset.d.ts
tsconfig.json
vercel.json
… 2 more files
```

## Entry points

- [.storybook/main.ts](https://github.com/Blazity/next-enterprise/blob/97c4f3ed6be0a5b255d0e71606c7b355138281a9/.storybook/main.ts)
- [app/page.tsx](https://github.com/Blazity/next-enterprise/blob/97c4f3ed6be0a5b255d0e71606c7b355138281a9/app/page.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 1 file(s) under api layer (observed from repository paths and static analysis). |
| app package | library | Observed | Groups 2 file(s) under app package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 4 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 13 file(s) under core modules (observed from repository paths and static analysis). |
| e2e package | library | Observed | Groups 1 file(s) under e2e package (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/check.yml` (ci)
- `.github/workflows/nextjs_bundle_analysis.yml` (ci)
- `.github/workflows/playwright.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `.vscode/settings.json` (config)
- `git-conventional-commits.yaml` (config)
- `package.json` (manifest)
- `renovate.json` (config)
- `tsconfig.json` (config)
- `vercel.json` (config)

## Top-level layout

- `(root files)` — 26 analysed file(s)
- `.github` — 4 analysed file(s)
- `components` — 4 analysed file(s)
- `app` — 3 analysed file(s)
- `.storybook` — 2 analysed file(s)
- `assets` — 2 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `e2e` — 1 analysed file(s)
- `styles` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `97c4f3ed6be0a5b255d0e71606c7b355138281a9` is the revision these paths and observations refer to.
