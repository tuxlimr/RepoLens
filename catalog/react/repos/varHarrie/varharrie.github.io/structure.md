# Project structure: varHarrie/varharrie.github.io

**Analysed commit:** `5e592ebac9c6eb6642121b49487889ebbc01fb87`

**Commit reference:** [5e592ebac9c6eb6642121b49487889ebbc01fb87](https://github.com/varHarrie/varharrie.github.io/commit/5e592ebac9c6eb6642121b49487889ebbc01fb87)

**Tree at this commit:** [varHarrie/varharrie.github.io@5e592ebac9c6](https://github.com/varHarrie/varharrie.github.io/tree/5e592ebac9c6eb6642121b49487889ebbc01fb87)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | varHarrie/varharrie.github.io |
| Description | :blue_book: Personal blog site based on github issues. |
| Stars | 3671 |
| Forks | 538 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | v2 |
| Analysed commit | `5e592ebac9c6eb6642121b49487889ebbc01fb87` |
| Retrieved at | 2026-11-14T19:15:10.051527+00:00 |
| Files in this snapshot | 54 |

## Directory tree

```text
src/  (39 files)
  components/  (13 files)
    ShapeEffect/  (2 files)
      … 2 files under this directory
    ArticleItem.tsx
    ArticleSkeleton.tsx
    CommentItem.tsx
    CommentSkeleton.tsx
    LabelItem.tsx
    MarkdownHtml.tsx
    Pagination.tsx
    Playground.tsx
    ProjectItem.tsx
    ProjectSkeleton.tsx
    Skeleton.tsx
  hooks/  (4 files)
    use-dark-mode.ts
    use-handling.ts
    use-local-storage.ts
    use-query.ts
  i18n/  (5 files)
    locales/  (4 files)
      … 4 files under this directory
    index.ts
  models/  (6 files)
    ArticleModel.ts
    CategoryModel.ts
    CommentModel.ts
    LabelModel.ts
    ProjectModel.ts
    UserModel.ts
  services/  (1 files)
    github.ts
  styles/  (1 files)
    BaseStyles.tsx
  views/  (5 files)
    Article.tsx
    Articles.tsx
    Home.tsx
    Main.tsx
    Projects.tsx
  App.tsx
  favicon.svg
  main.tsx
  utils.ts
types/  (4 files)
  env.d.ts
  react-i18next.d.ts
  twin.d.ts
  vite-env.d.ts
.env.example
.gitignore
.prettierrc
LICENSE
README.md
index.html
package.json
tailwind.config.js
tsconfig.json
tsconfig.node.json
vite.config.ts
```

## Entry points

- [src/App.tsx](https://github.com/varHarrie/varharrie.github.io/blob/5e592ebac9c6eb6642121b49487889ebbc01fb87/src/App.tsx)
- [src/i18n/index.ts](https://github.com/varHarrie/varharrie.github.io/blob/5e592ebac9c6eb6642121b49487889ebbc01fb87/src/i18n/index.ts)
- [src/main.tsx](https://github.com/varHarrie/varharrie.github.io/blob/5e592ebac9c6eb6642121b49487889ebbc01fb87/src/main.tsx)
- [src/views/Main.tsx](https://github.com/varHarrie/varharrie.github.io/blob/5e592ebac9c6eb6642121b49487889ebbc01fb87/src/views/Main.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 5 file(s) under api layer (observed from repository paths and static analysis). |
| App.tsx package | library | Observed | Groups 1 file(s) under app.tsx package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 13 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 6 file(s) under data layer (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 4 file(s) under hooks package (observed from repository paths and static analysis). |
| i18n package | library | Observed | Groups 3 file(s) under i18n package (observed from repository paths and static analysis). |
| main.tsx package | library | Observed | Groups 1 file(s) under main.tsx package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 1 file(s) under service / domain layer (observed from repository paths and static analysis). |
| styles package | library | Observed | Groups 1 file(s) under styles package (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 4 file(s) under types package (observed from repository paths and static analysis). |
| utils.ts package | library | Observed | Groups 1 file(s) under utils.ts package (observed from repository paths and static analysis). |

## Important files

- `.env.example` (config)
- `package.json` (manifest)
- `src/i18n/locales/cn/translation.json` (config)
- `src/i18n/locales/en/translation.json` (config)
- `tsconfig.json` (config)
- `tsconfig.node.json` (config)

## Top-level layout

- `src` — 39 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `types` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `5e592ebac9c6eb6642121b49487889ebbc01fb87` is the revision these paths and observations refer to.
