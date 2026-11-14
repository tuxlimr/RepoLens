# Project structure: garmeeh/next-seo

**Analysed commit:** `738ef7e774ee6216f6e90c26a3b5b99dd5d166b4`

**Commit reference:** [738ef7e774ee6216f6e90c26a3b5b99dd5d166b4](https://github.com/garmeeh/next-seo/commit/738ef7e774ee6216f6e90c26a3b5b99dd5d166b4)

**Tree at this commit:** [garmeeh/next-seo@738ef7e774ee](https://github.com/garmeeh/next-seo/tree/738ef7e774ee6216f6e90c26a3b5b99dd5d166b4)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | garmeeh/next-seo |
| Description | Next SEO is a plug in that makes managing your SEO easier in Next.js projects. |
| Stars | 8545 |
| Forks | 468 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `738ef7e774ee6216f6e90c26a3b5b99dd5d166b4` |
| Retrieved at | 2026-11-14T19:13:40.956419+00:00 |
| Files in this snapshot | 290 |

## Directory tree

```text
.changeset/  (2 files)
  README.md
  config.json
.github/  (8 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (4 files)
    changeset-check.yml
    changesets.yml
    ci.yml
    release.yml
  dependabot.yml
  pull_request_template.md
.husky/  (1 files)
  pre-commit
.vscode/  (1 files)
  settings.json
examples/  (124 files)
  app-router-showcase/  (124 files)
    app/  (110 files)
      … 110 files under this directory
    components/  (2 files)
      … 2 files under this directory
    public/  (5 files)
      … 5 files under this directory
    .gitignore
    CLAUDE.md
    README.md
    eslint.config.mjs
    next.config.ts
    package.json
    tsconfig.json
src/  (99 files)
  components/  (56 files)
    .gitkeep
    AggregateRatingJsonLd.test.tsx
    AggregateRatingJsonLd.tsx
    ArticleJsonLd.test.tsx
    ArticleJsonLd.tsx
    BreadcrumbJsonLd.test.tsx
    BreadcrumbJsonLd.tsx
    CLAUDE.md
    CarouselJsonLd.test.tsx
    CarouselJsonLd.tsx
    ClaimReviewJsonLd.test.tsx
    ClaimReviewJsonLd.tsx
    CourseJsonLd.test.tsx
    CourseJsonLd.tsx
    CreativeWorkJsonLd.test.tsx
    CreativeWorkJsonLd.tsx
    DatasetJsonLd.test.tsx
    DatasetJsonLd.tsx
    DiscussionForumPostingJsonLd.test.tsx
    DiscussionForumPostingJsonLd.tsx
    EmployerAggregateRatingJsonLd.test.tsx
    EmployerAggregateRatingJsonLd.tsx
    EventJsonLd.test.tsx
    EventJsonLd.tsx
    … 32 more files
  core/  (2 files)
    JsonLdScript.test.tsx
    JsonLdScript.tsx
  pages/  (7 files)
    core/  (3 files)
      … 3 files under this directory
    types/  (1 files)
      … 1 files under this directory
    utils/  (1 files)
      … 1 files under this directory
    README.md
    index.ts
  types/  (28 files)
    article.types.ts
    breadcrumb.types.ts
    carousel.types.ts
    claimreview.types.ts
    common.types.ts
    course.types.ts
    creativework.types.ts
    dataset.types.ts
    discussionforum.types.ts
    employer-aggregate-rating.types.ts
    event.types.ts
    faq.types.ts
    howto.types.ts
    image.types.ts
    index.ts
    jobposting.types.ts
    localbusiness.types.ts
    merchantreturnpolicy.types.ts
    movie-carousel.types.ts
    organization.types.ts
    product.types.ts
    profile.types.ts
    quiz.types.ts
    recipe.types.ts
    … 4 more files
  utils/  (5 files)
    processors.export.ts
    processors.test.ts
    processors.ts
    stringify.test.ts
    stringify.ts
  index.ts
tests/  (34 files)
  e2e/  (33 files)
    .gitkeep
    CLAUDE.md
    aggregateRatingJsonLd.e2e.spec.ts
    articleJsonLd.e2e.spec.ts
    breadcrumbJsonLd.e2e.spec.ts
    carouselJsonLd.e2e.spec.ts
    claimReviewJsonLd.e2e.spec.ts
    courseJsonLd.e2e.spec.ts
    creativeWorkJsonLd.e2e.spec.ts
    customComponents.e2e.spec.ts
    datasetJsonLd.e2e.spec.ts
    discussionForumPostingJsonLd.e2e.spec.ts
    employerAggregateRatingJsonLd.e2e.spec.ts
    eventJsonLd.e2e.spec.ts
    faqJsonLd.e2e.spec.ts
    howtoJsonLd.e2e.spec.ts
    imageJsonLd.e2e.spec.ts
    jobPostingJsonLd.e2e.spec.ts
    jsonLdScript.e2e.spec.ts
    jsonValidation.e2e.spec.ts
    localBusinessJsonLd.e2e.spec.ts
    merchantReturnPolicyJsonLd.e2e.spec.ts
    movieCarouselJsonLd.e2e.spec.ts
    organizationJsonLd.e2e.spec.ts
    … 9 more files
  unit/  (1 files)
    setup.ts
.editorconfig
.gitignore
.npmignore
.prettierignore
ADDING_NEW_COMPONENTS.md
AGENTS.md
CHANGELOG.md
CLAUDE.md
CONTRIBUTING.md
CUSTOM_COMPONENTS.md
LICENSE
LICENSE.md
LIST.md
eslint.config.mjs
package.json
playwright.config.ts
pnpm-workspace.yaml
repomix.config.json
tsconfig.json
tsup.config.ts
vitest.config.ts
```

## Entry points

- [src/index.ts](https://github.com/garmeeh/next-seo/blob/738ef7e774ee6216f6e90c26a3b5b99dd5d166b4/src/index.ts)
- [src/pages/index.ts](https://github.com/garmeeh/next-seo/blob/738ef7e774ee6216f6e90c26a3b5b99dd5d166b4/src/pages/index.ts)
- [src/pages/types/index.ts](https://github.com/garmeeh/next-seo/blob/738ef7e774ee6216f6e90c26a3b5b99dd5d166b4/src/pages/types/index.ts)
- [src/types/index.ts](https://github.com/garmeeh/next-seo/blob/738ef7e774ee6216f6e90c26a3b5b99dd5d166b4/src/types/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| components package | library | Observed | Groups 54 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| index.ts package | library | Observed | Groups 1 file(s) under index.ts package (observed from repository paths and static analysis). |
| pages package | library | Observed | Groups 3 file(s) under pages package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 4 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 34 file(s) under tests (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 28 file(s) under types package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 5 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.editorconfig` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/changeset-check.yml` (ci)
- `.github/workflows/changesets.yml` (ci)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.vscode/settings.json` (config)
- `examples/app-router-showcase/package.json` (manifest)
- `examples/app-router-showcase/tsconfig.json` (config)
- `package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `repomix.config.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `examples` — 124 analysed file(s)
- `src` — 99 analysed file(s)
- `tests` — 34 analysed file(s)
- `(root files)` — 21 analysed file(s)
- `.github` — 8 analysed file(s)
- `.changeset` — 2 analysed file(s)
- `.husky` — 1 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `738ef7e774ee6216f6e90c26a3b5b99dd5d166b4` is the revision these paths and observations refer to.
