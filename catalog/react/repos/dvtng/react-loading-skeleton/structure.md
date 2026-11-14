# Project structure: dvtng/react-loading-skeleton

**Analysed commit:** `f8b040dade9cfaad7e3e6fbc50243d79f508f1ca`

**Commit reference:** [f8b040dade9cfaad7e3e6fbc50243d79f508f1ca](https://github.com/dvtng/react-loading-skeleton/commit/f8b040dade9cfaad7e3e6fbc50243d79f508f1ca)

**Tree at this commit:** [dvtng/react-loading-skeleton@f8b040dade9c](https://github.com/dvtng/react-loading-skeleton/tree/f8b040dade9cfaad7e3e6fbc50243d79f508f1ca)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | dvtng/react-loading-skeleton |
| Description | Create skeleton screens that automatically adapt to your app! |
| Stars | 4213 |
| Forks | 163 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `f8b040dade9cfaad7e3e6fbc50243d79f508f1ca` |
| Retrieved at | 2026-11-14T19:14:51.737361+00:00 |
| Files in this snapshot | 43 |

## Directory tree

```text
.github/  (4 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (1 files)
    ci.yml
  CODE_OF_CONDUCT.md
.husky/  (1 files)
  pre-commit
.storybook/  (3 files)
  main.ts
  preview.ts
  storybook.css
assets/  (2 files)
  logo-inkscape-src.svg
  logo.svg
src/  (18 files)
  __stories__/  (8 files)
    components/  (4 files)
      … 4 files under this directory
    styles/  (1 files)
      … 1 files under this directory
    Post.stories.tsx
    Skeleton.stories.tsx
    SkeletonTheme.stories.tsx
  __tests__/  (4 files)
    __helpers__/  (1 files)
      … 1 files under this directory
    Skeleton.test.tsx
    SkeletonTheme.test.tsx
    index.test.tsx
  Skeleton.tsx
  SkeletonStyleProps.ts
  SkeletonTheme.tsx
  SkeletonThemeContext.ts
  index.ts
  skeleton.css
.editorconfig
.eslintrc.cjs
.gitignore
.prettierignore
.prettierrc.cjs
.swcrc
.yarnrc.yml
CHANGELOG.md
CONTRIBUTING.md
LICENSE
README.md
package.json
rollup.config.js
tsconfig.json
vite.config.ts
```

## Entry points

- [.storybook/main.ts](https://github.com/dvtng/react-loading-skeleton/blob/f8b040dade9cfaad7e3e6fbc50243d79f508f1ca/.storybook/main.ts)
- [src/__stories__/components/index.ts](https://github.com/dvtng/react-loading-skeleton/blob/f8b040dade9cfaad7e3e6fbc50243d79f508f1ca/src/__stories__/components/index.ts)
- [src/index.ts](https://github.com/dvtng/react-loading-skeleton/blob/f8b040dade9cfaad7e3e6fbc50243d79f508f1ca/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| index.ts package | library | Observed | Groups 1 file(s) under index.ts package (observed from repository paths and static analysis). |
| Skeleton.tsx package | library | Observed | Groups 1 file(s) under skeleton.tsx package (observed from repository paths and static analysis). |
| SkeletonStyleProps.ts package | library | Observed | Groups 1 file(s) under skeletonstyleprops.ts package (observed from repository paths and static analysis). |
| SkeletonTheme.tsx package | library | Observed | Groups 1 file(s) under skeletontheme.tsx package (observed from repository paths and static analysis). |
| SkeletonThemeContext.ts package | library | Observed | Groups 1 file(s) under skeletonthemecontext.ts package (observed from repository paths and static analysis). |
| __stories__ package | library | Observed | Groups 7 file(s) under __stories__ package (observed from repository paths and static analysis). |
| __tests__ package | library | Observed | Groups 4 file(s) under __tests__ package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/workflows/ci.yml` (ci)
- `.yarnrc.yml` (config)
- `package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `src` — 18 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `.github` — 4 analysed file(s)
- `.storybook` — 3 analysed file(s)
- `assets` — 2 analysed file(s)
- `.husky` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `f8b040dade9cfaad7e3e6fbc50243d79f508f1ca` is the revision these paths and observations refer to.
